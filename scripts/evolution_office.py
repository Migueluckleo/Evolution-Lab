#!/usr/bin/env python3
"""Local office ledger and read-only HTML. Does not start agents or contact services."""
import argparse
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import uuid

ROOT = Path(__file__).resolve().parents[1]
KINDS = {"request", "response", "decision", "note"}
RESULTS = {"RECORDED", "DISPATCHED", "PASS", "FAIL", "BLOCKED", "COMPLETED", "NOT_RUN"}


def digest(event):
    clean = {k: v for k, v in event.items() if k != "sha256"}
    return hashlib.sha256(json.dumps(clean, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def validate(config, events, root=ROOT):
    agents = {a["id"] for a in config["agents"]} | {"user"}
    objectives = {o["id"] for o in config["objectives"]}
    seen, answered, previous = {}, set(), None
    for event in events:
        for key in ("id", "timestamp", "kind", "from", "to", "message", "why", "scope", "deliverable", "objective", "status"):
            if not isinstance(event.get(key), str) or not event[key].strip():
                raise ValueError(f"Campo obligatorio: {key}")
        if event["id"] in seen or event["from"] not in agents or event["to"] not in agents:
            raise ValueError("Identidad duplicada o agente desconocido")
        if event["kind"] not in KINDS or event["status"] not in RESULTS or event["objective"] not in objectives:
            raise ValueError("Tipo, estado u objetivo desconocido")
        stamp = dt.datetime.fromisoformat(event["timestamp"])
        if stamp.tzinfo is None:
            raise ValueError("La fecha debe incluir zona horaria")
        if event.get("previous") != previous or event.get("sha256") != digest(event):
            raise ValueError("La cadena del registro fue alterada")
        evidence = event.get("evidence")
        if not isinstance(evidence, list) or any(not isinstance(p, str) for p in evidence):
            raise ValueError("Evidencia debe ser una lista de rutas locales")
        if event["status"] in {"PASS", "COMPLETED"} and not evidence:
            raise ValueError("Un resultado terminado requiere evidencia")
        for path in evidence:
            target = (root / path).resolve()
            if Path(path).is_absolute() or not target.is_relative_to(root.resolve()) or not target.is_file():
                raise ValueError(f"Evidencia inexistente o fuera del repositorio: {path}")
        reply = event.get("reply_to")
        if event["kind"] == "response":
            request = seen.get(reply)
            if not request or request["kind"] != "request" or reply in answered:
                raise ValueError("La respuesta requiere una solicitud pendiente")
            if (event["from"], event["to"]) != (request["to"], request["from"]):
                raise ValueError("La respuesta no corresponde a los interlocutores")
            if event["objective"] != request["objective"]:
                raise ValueError("La respuesta cambió el objetivo del encargo")
            answered.add(reply)
        elif reply is not None:
            raise ValueError("Solo una respuesta utiliza reply_to")
        if event["kind"] == "request" and event["status"] != "DISPATCHED":
            raise ValueError("Una solicitud registrada debe haber sido enviada")
        seen[event["id"]] = event
        previous = event["sha256"]
    return answered


def load(root=ROOT):
    config = json.loads((root / "office/config.json").read_text())
    path = root / "office/events.jsonl"
    events = [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []
    validate(config, events, root)
    return config, events


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(dir=path.parent, prefix=".office-")
    try:
        with os.fdopen(fd, "w") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def record(payload, root=ROOT):
    # Serializes writers. Evidence proves an artifact exists, not that an agent really spoke.
    # The Codex operator is responsible for recording only verified dispatches/results.
    with (root / "office/.ledger.lock").open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        config, events = load(root)
        event = dict(payload)
        event["id"] = event.get("id") or str(uuid.uuid4())
        event["timestamp"] = dt.datetime.now(dt.timezone.utc).isoformat()
        event["previous"] = events[-1]["sha256"] if events else None
        event["sha256"] = digest(event)
        validate(config, events + [event], root)
        state = make_data(config, events + [event])
        page = render_text(config, events + [event], root, state)
        atomic_write(root / "office/events.jsonl", "".join(json.dumps(e, ensure_ascii=False) + "\n" for e in events + [event]))
        try:
            atomic_write(root / "office/dist/index.html", page)
            atomic_write(root / "office/dist/state.json", json.dumps(state, ensure_ascii=False))
        except OSError:
            print(f"Evento guardado: {event['id']}. Panel pendiente; ejecuta render, no repitas record.", file=sys.stderr)
        return event["id"]


def make_data(config, events):
    return {"config": config, "events": events, "generated": dt.datetime.now(dt.timezone.utc).isoformat(), "revision": digest({"config": config, "events": events})}


def render_text(config, events, root=ROOT, data=None):
    data = data or make_data(config, events)
    # Embedded JSON stays inert even when a message contains HTML/script delimiters.
    encoded = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")
    template = (root / "office/dashboard.html").read_text()
    if template.count("__OFFICE_DATA__") != 1:
        raise ValueError("Plantilla de panel incompatible")
    return template.replace("__OFFICE_DATA__", encoded)


def render(root=ROOT):
    with (root / "office/.ledger.lock").open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        config, events = load(root)
        state = make_data(config, events)
        atomic_write(root / "office/dist/index.html", render_text(config, events, root, state))
        atomic_write(root / "office/dist/state.json", json.dumps(state, ensure_ascii=False))
        return len(events)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    subs.add_parser("check")
    subs.add_parser("render")
    command = subs.add_parser("record")
    command.add_argument("--file", required=True, type=Path)
    args = parser.parse_args()
    try:
        if args.command == "record":
            print(record(json.loads(args.file.read_text())))
        elif args.command == "render":
            print(f"Panel generado: {render()} eventos; office/dist/index.html")
        else:
            config, events = load()
            print(f"PASS: {len(config['agents'])} perfiles; {len(events)} eventos válidos")
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f"Office: {error}\n")


if __name__ == "__main__":
    main()
