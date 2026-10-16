from pathlib import Path
import sys
if __name__ == '__main__':
    sys.path.insert(0, str(Path('scripts').resolve()))
    import ds_graph_engine as engine
    engine.initialize(Path('graphify-out/runs/2026-10-13-web-characters-fix').resolve())
    engine.ast()
