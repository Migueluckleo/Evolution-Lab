#!/usr/bin/env python3
"""Loopback-only Evolution Lab composer; each message starts a new Codex execution."""
import argparse
import codecs
import datetime as dt
import hashlib
import fcntl
import json
import os
from pathlib import Path
import re
import secrets
import selectors
import signal
import subprocess
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlsplit

import evolution_office as ledger

ROOT = Path(__file__).resolve().parents[1]
MAX_BODY = 32768
MAX_MESSAGE = 8000
ID = re.compile(r"^[A-Za-z0-9_-]{8,80}$")


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def private_write(path, value):
    ledger.atomic_write(path, json.dumps(value, ensure_ascii=False))
    path.chmod(0o600)


class Busy(Exception):
    pass


class OfficeRuntime:
    def __init__(self, root=ROOT, codex="codex", timeout=1800):
        self.root = Path(root).resolve()
        self.codex, self.timeout = str(codex), timeout
        self.token = secrets.token_urlsafe(32)
        self.lock = threading.RLock()
        self.jobs, self.processes, self.threads = {}, {}, []
        self.active = None
        self.closed = False
        self.folder = self.root / "output/office-runtime/jobs"
        self.folder.mkdir(parents=True, exist_ok=True)
        self.folder.chmod(0o700)
        self.instance_lock = (self.folder.parent / ".server.lock").open("w")
        try:
            fcntl.flock(self.instance_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            self.instance_lock.close()
            raise RuntimeError("Ya hay un servidor de oficina activo")
        for path in self.folder.glob("*/job.json"):
            job = json.loads(path.read_text())
            if ID.fullmatch(job.get("id", "")):
                if job["status"] in {"received", "running"}:
                    job.update(status="failed", error="La ejecución anterior fue interrumpida; no se reintentó automáticamente.")
                    private_write(path, job)
                job.setdefault("updates", [])
                job.setdefault("started_at", None)
                job.setdefault("last_activity_at", dt.datetime.fromtimestamp(path.stat().st_mtime, dt.timezone.utc).isoformat())
                job.setdefault("activity", "Registro recuperado")
                self.jobs[job["id"]] = job

    def public(self, job):
        return {key: job.get(key) for key in ("id", "request_id", "status", "message", "error", "result", "updates", "last_activity_at", "started_at", "activity", "updates_truncated")}

    def persist(self, job):
        private_write(self.folder / job["id"] / "job.json", job)

    def event(self, job, response=False, success=True):
        result_path = f"output/office-runtime/jobs/{job['id']}/result.json"
        payload = {
            "kind": "response" if response else "request", "from": "eva" if response else "user",
            "to": "user" if response else "eva", "message": (job["result"] or job["error"]) if response else job["message"],
            "why": "Solicitud del usuario desde el compositor local; ejecución real de Codex.",
            "scope": "Alcance solicitado por el usuario y protocolos vigentes del repositorio.",
            "deliverable": "Respuesta y evidencia de la ejecución; QA solo cuando exista comprobación.",
            "objective": "construction", "status": ("RECORDED" if success else "FAIL") if response else "DISPATCHED",
            "evidence": [result_path] if response else [],
            "tool_ref": "codex-exec:" + job["id"],
        }
        if response:
            payload["reply_to"] = job["event_id"]
        return ledger.record(payload, self.root)

    def submit(self, request_id, message):
        if not isinstance(request_id, str) or not ID.fullmatch(request_id):
            raise ValueError("request_id debe tener 8–80 caracteres alfanuméricos, guiones o guiones bajos")
        if not isinstance(message, str) or not message.strip() or len(message) > MAX_MESSAGE:
            raise ValueError("Mensaje vacío o demasiado largo")
        with self.lock:
            existing = self.jobs.get(request_id)
            if existing:
                if existing["message"] != message:
                    raise Busy("request_id ya se usó con otro mensaje")
                return self.public(existing), False
            if self.closed or self.active:
                raise Busy("Hay una ejecución activa o el servidor está cerrándose")
            folder = self.folder / request_id
            folder.mkdir(mode=0o700, exist_ok=True)
            job = {"id": request_id, "request_id": request_id, "status": "received", "message": message, "error": None, "result": None, "updates": [], "last_activity_at": now(), "started_at": None, "activity": "Solicitud recibida", "updates_truncated": 0}
            self.jobs[request_id] = job
            self.active = request_id
            try:
                self.persist(job)
            except OSError:
                self.jobs.pop(request_id, None)
                self.active = None
                raise
            prompt = (
                "Eres Eva, orquestadora de Evolution Lab. Esta es una ejecución NUEVA por solicitud; "
                "no presupongas memoria de otra conversación. Lee AGENTS.md, office/config.json y "
                "office/OPERATING-PROTOCOL.md, y consulta registros pertinentes. Atiende el siguiente encargo "
                "dentro de su alcance. Usa los perfiles necesarios, registra SOLO intercambios realmente "
                "despachados y resultados comprobados. El servidor ya registra la solicitud y registrará tu "
                "respuesta final; no dupliques esos dos eventos. No inventes actividad, mediciones ni QA. "
                "Emite avances públicos breves cuando haya hallazgos, decisiones o bloqueos concretos; "
                "no esperes al final para comunicar resultados parciales útiles. Al delegar, identifica el rol "
                "y nombre del agente real y explica su encargo; nunca finjas diálogos ni actividad. "
                "No publiques razonamiento privado ni detalles secretos de herramientas. "
                "No modifiques el servidor ni sus trabajos para ocultar fallos.\n\nSolicitud del usuario:\n" + message
            )
            try:
                proc = subprocess.Popen(
                    [self.codex, "exec", "--json", "--approve-for-me", "-C", str(self.root), "-"],
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                    text=True, encoding="utf-8", errors="replace", start_new_session=True, cwd=self.root,
                )
                self.processes[request_id] = proc
                job["event_id"] = self.event(job)
                job.update(status="running", started_at=now(), last_activity_at=now(), activity="Ejecución de Codex iniciada")
                self.persist(job)
                thread = threading.Thread(target=self.run, args=(job, proc, prompt), daemon=True)
                self.threads.append(thread)
                thread.start()
            except Exception:
                proc = self.processes.pop(request_id, None)
                if proc:
                    self.terminate(proc)
                job.update(status="failed", error="No se pudo iniciar o registrar la ejecución. Consulta la evidencia local.")
                try:
                    private_write(folder / "result.json", self.public(job))
                    self.persist(job)
                except OSError:
                    pass
                finally:
                    self.active = None
            return self.public(job), True

    @staticmethod
    def terminate(proc):
        try:
            os.killpg(proc.pid, signal.SIGTERM)
        except ProcessLookupError:
            return
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            proc.wait(timeout=3)

    def update(self, job, update_id, message, kind="message", tool_ref=None):
        with self.lock:
            updates = job.setdefault("updates", [])
            previous = next((item for item in updates if item["id"] == update_id), None)
            if previous and previous["message"] == message and previous["kind"] == kind:
                return
            stamp = now()
            entry = {"id": update_id, "actor": "eva", "message": message[:24000], "kind": kind, "timestamp": stamp}
            if tool_ref:
                entry["tool_ref"] = tool_ref
            if previous:
                updates[updates.index(previous)] = entry
            else:
                updates.append(entry)
            if len(updates) > 500:
                job["updates_truncated"] = job.get("updates_truncated", 0) + len(updates) - 500
                del updates[:-500]
            job.update(last_activity_at=stamp, activity="Respuesta pública recibida" if kind == "message" else message)
            self.persist(job)

    def consume(self, job, event):
        """Only public agent messages and known, sanitized tool event shapes cross the API."""
        if not isinstance(event, dict):
            return None
        if event.get("channel") in {"analysis", "reasoning"} or event.get("phase") in {"analysis", "reasoning"}:
            return None
        event_type = event.get("type")
        if event_type not in {"item.started", "item.updated", "item.completed"}:
            return None
        item = event.get("item")
        if not isinstance(item, dict):
            return None
        item_type = item.get("type")
        if item.get("channel") in {"analysis", "reasoning"} or item.get("phase") in {"analysis", "reasoning"}:
            return None
        text = item.get("text")
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id:
            item_id = hashlib.sha256(json.dumps(item, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:20]
        if item_type == "agent_message" and isinstance(text, str) and text.strip():
            self.update(job, "message:" + item_id, text, "message")
            return text if event_type == "item.completed" else None
        labels = {"command_execution": "Ejecutando una comprobación o comando", "file_change": "Actualizando archivos del trabajo", "mcp_tool_call": "Consultando una herramienta conectada", "web_search": "Consultando fuentes", "collab_agent_tool_call": "Coordinando una ejecución de agente"}
        if item_type not in labels:
            return None
        label = labels[item_type]
        if event_type == "item.completed":
            label = "Actividad de herramienta finalizada"
        tool_ref = None
        # Supported collab shape: a named operation and an explicit list of receiver thread IDs.
        # Neither prompts nor returned agent text is surfaced; a thread ID is never a person's name.
        if item_type == "collab_agent_tool_call" and item.get("tool") in {"spawn_agent", "send_message", "wait", "close_agent", "resume_agent"}:
            receivers = item.get("receiver_thread_ids")
            if isinstance(receivers, list) and all(isinstance(x, str) and re.fullmatch(r"[A-Za-z0-9_-]{1,100}", x) for x in receivers):
                tool_ref = {"type": "collab_agent_tool_call", "receiver_thread_ids": receivers}
        self.update(job, "tool:" + item_id + ":" + event_type, label, "delegation" if tool_ref else "activity", tool_ref)
        return None

    def stream(self, job, proc, prompt):
        selector = selectors.DefaultSelector()
        decoders = {name: codecs.getincrementaldecoder("utf-8")("replace") for name in ("stdout", "stderr")}
        captured = {"stdout": [], "stderr": []}
        pending, messages, writer_errors = "", [], []
        deadline = time.monotonic() + self.timeout
        drain_deadline, error = None, None

        def write_input():
            try:
                proc.stdin.write(prompt)
                proc.stdin.close()
            except (OSError, ValueError):
                writer_errors.append(True)

        writer = threading.Thread(target=write_input, daemon=True)
        try:
            for name in ("stdout", "stderr"):
                pipe = getattr(proc, name)
                os.set_blocking(pipe.fileno(), False)
                selector.register(pipe, selectors.EVENT_READ, name)
            writer.start()
            while selector.get_map():
                current = time.monotonic()
                if drain_deadline is None and current >= deadline:
                    error = "La ejecución superó el tiempo permitido y fue detenida."
                    self.terminate(proc)
                    drain_deadline = time.monotonic() + 3
                if drain_deadline is not None and current >= drain_deadline:
                    break
                for key, _ in selector.select(timeout=.1):
                    chunk = os.read(key.fileobj.fileno(), 65536)
                    name = key.data
                    decoded = decoders[name].decode(chunk, final=not chunk)
                    captured[name].append(decoded)
                    if name == "stdout":
                        pending += decoded
                        while "\n" in pending:
                            line, pending = pending.split("\n", 1)
                            try:
                                event = json.loads(line)
                            except ValueError:
                                continue
                            text = self.consume(job, event)
                            if text:
                                messages.append(text)
                    if not chunk:
                        selector.unregister(key.fileobj)
            if pending.strip():
                try:
                    text = self.consume(job, json.loads(pending))
                    if text:
                        messages.append(text)
                except ValueError:
                    pass
            try:
                proc.wait(timeout=max(.1, deadline - time.monotonic()) if error is None else 3)
            except subprocess.TimeoutExpired:
                error = "La ejecución superó el tiempo permitido y fue detenida."
                self.terminate(proc)
            writer.join(timeout=1)
            if writer_errors and error is None:
                error = "No se pudo entregar la solicitud completa a Codex."
            return "".join(captured["stdout"]), "".join(captured["stderr"]), messages, error
        except Exception:
            try:
                self.terminate(proc)
            except (OSError, subprocess.SubprocessError):
                pass
            return "".join(captured["stdout"]), "".join(captured["stderr"]), messages, "La lectura de la ejecución falló; consulta la evidencia local."
        finally:
            selector.close()
            if writer.ident is not None:
                writer.join(timeout=3)
            for name in ("stdin", "stdout", "stderr"):
                try:
                    getattr(proc, name).close()
                except (OSError, ValueError):
                    pass

    def run(self, job, proc, prompt):
        stdout, stderr, result, error = "", "", None, None
        try:
            stdout, stderr, messages, error = self.stream(job, proc, prompt)
            if error is None:
                if proc.returncode == 0 and messages:
                    result = messages[-1][:24000]
                else:
                    error = "Codex no completó una respuesta verificable. Consulta la evidencia local."
        except Exception:
            error = "La ejecución falló; consulta la evidencia local."
            try:
                self.terminate(proc)
            except (OSError, subprocess.SubprocessError):
                pass
        finally:
            with self.lock:
                if self.closed:
                    error, result = "El servidor se cerró y detuvo la ejecución.", None
                job.update(status="failed" if error else "completed", result=result, error=error, last_activity_at=now(), activity="Ejecución fallida" if error else "Ejecución terminada")
                folder = self.folder / job["id"]
                try:
                    private_write(folder / "logs.json", {"stdout": stdout, "stderr": stderr, "returncode": proc.returncode})
                    private_write(folder / "result.json", {**self.public(job), "returncode": proc.returncode, "execution_mode": "new_execution_per_message"})
                    try:
                        self.event(job, response=True, success=not error)
                    except Exception:
                        job.update(status="failed", error="La ejecución terminó, pero no se pudo registrar su respuesta. Consulta la evidencia local.")
                        private_write(folder / "result.json", self.public(job))
                    self.persist(job)
                except Exception:
                    job.update(status="failed", error="No se pudo guardar toda la evidencia de la ejecución; revisa el almacenamiento local.")
                    try:
                        self.persist(job)
                    except OSError:
                        pass
                finally:
                    self.processes.pop(job["id"], None)
                    self.active = None

    def shutdown(self):
        with self.lock:
            self.closed = True
            processes = list(self.processes.values())
        for proc in processes:
            self.terminate(proc)
        for thread in self.threads:
            thread.join(timeout=8)
        if not self.instance_lock.closed:
            self.instance_lock.close()

    def allowed_file(self, route):
        relative = unquote(route).lstrip("/")
        if not relative:
            relative = "office/dist/index.html"
        fixed = {"office/dist/index.html", "office/dist/state.json", "office/config.json", "office/README.md", "office/OPERATING-PROTOCOL.md", "EVOLUTION-LAB.md"}
        _, events = ledger.load(self.root)
        allowed = fixed | {p for e in events for p in e.get("evidence", [])}
        if relative not in allowed or any(part.startswith(".") for part in Path(relative).parts):
            return None
        if relative.startswith("output/office-runtime/") and not re.fullmatch(r"output/office-runtime/jobs/[A-Za-z0-9_-]{8,80}/result\.json", relative):
            return None
        path = self.root / relative
        resolved = path.resolve()
        if not resolved.is_relative_to(self.root) or any(part.startswith(".") for part in resolved.relative_to(self.root).parts) or not path.is_file() or path.is_symlink():
            return None
        return path


class Handler(BaseHTTPRequestHandler):
    def setup(self):
        super().setup()
        self.connection.settimeout(10)

    def log_message(self, *_):
        pass

    def send(self, code, value):
        data = json.dumps(value, ensure_ascii=False).encode()
        self.send_bytes(code, data, "application/json; charset=utf-8")

    def send_bytes(self, code, data, content_type):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "frame-ancestors 'none'; base-uri 'none'")
        self.end_headers()
        self.wfile.write(data)

    def trusted(self, post=False):
        expected = self.headers.get("Host", "")
        allowed_hosts = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
        origin = self.headers.get("Origin")
        if expected not in allowed_hosts or (origin is not None and origin != "http://" + expected):
            self.send(403, {"error": "Origen no permitido"})
            return False
        if self.headers.get("Sec-Fetch-Site") in {"cross-site", "same-site"}:
            self.send(403, {"error": "Origen no permitido"})
            return False
        if post and (origin != "http://" + expected or not secrets.compare_digest(self.headers.get("X-Office-Token", ""), self.server.runtime.token)):
            self.send(403, {"error": "Sesión inválida; recarga la oficina"})
            return False
        return True

    def do_GET(self):
        if not self.trusted():
            return
        runtime = self.server.runtime
        route = urlsplit(self.path).path
        with runtime.lock:
            if route == "/api/session":
                last = max(runtime.jobs.values(), key=lambda j: j.get("started_at") or j.get("last_activity_at") or "", default=None)
                self.send(200, {"token": runtime.token, "active_job": runtime.public(runtime.jobs[runtime.active]) if runtime.active else None, "last_job": runtime.public(last) if last else None, "server_now": now(), "session_mode": "new_execution_per_message"})
                return
            if route.startswith("/api/jobs/"):
                if not secrets.compare_digest(self.headers.get("X-Office-Token", ""), runtime.token):
                    self.send(403, {"error": "Sesión inválida; recarga la oficina"})
                    return
                job = runtime.jobs.get(route.removeprefix("/api/jobs/"))
                self.send(200 if job else 404, {"job": runtime.public(job)} if job else {"error": "Trabajo desconocido"})
                return
        try:
            path = runtime.allowed_file(route)
            if path:
                mime = {".html": "text/html", ".json": "application/json", ".md": "text/plain"}.get(path.suffix, "application/octet-stream")
                if path.suffix == ".html" and path != runtime.root / "office/dist/index.html":
                    mime = "text/plain"
                self.send_bytes(200, path.read_bytes(), mime + "; charset=utf-8")
                return
        except (ValueError, OSError):
            self.send(503, {"error": "Registro temporalmente no disponible"})
            return
        self.send(404, {"error": "Recurso no disponible"})

    def do_POST(self):
        if not self.trusted(post=True):
            return
        if self.path != "/api/messages":
            self.send(404, {"error": "Ruta desconocida"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 1 or length > MAX_BODY or self.headers.get("Transfer-Encoding"):
                self.send(413, {"error": "Solicitud demasiado grande o vacía"})
                return
            if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
                self.send(415, {"error": "Se requiere JSON"})
                return
            payload = json.loads(self.rfile.read(length))
            if not isinstance(payload, dict) or set(payload) != {"message", "request_id"}:
                raise ValueError("Se requieren message y request_id")
            job, created = self.server.runtime.submit(payload["request_id"], payload["message"])
            self.send(202 if created else 200, {"job": job})
        except Busy as error:
            self.send(409, {"error": str(error)})
        except (ValueError, UnicodeError):
            self.send(400, {"error": "Solicitud inválida"})
        except Exception:
            self.send(500, {"error": "No se pudo aceptar la solicitud"})


def make_server(runtime, port=8766):
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.runtime = runtime
    server.daemon_threads = True
    return server


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8766)
    parser.add_argument("--codex", default="codex")
    parser.add_argument("--timeout", type=int, default=1800)
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("timeout debe ser positivo")
    runtime = OfficeRuntime(codex=args.codex, timeout=args.timeout)
    server = make_server(runtime, args.port)
    def stop(*_):
        threading.Thread(target=server.shutdown, daemon=True).start()
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    print(f"Evolution Lab: http://127.0.0.1:{server.server_port}", flush=True)
    try:
        server.serve_forever()
    finally:
        runtime.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
