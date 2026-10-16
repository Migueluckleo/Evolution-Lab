from pathlib import Path
import sys
if __name__ == '__main__':
    root=Path(__file__).resolve().parents[3]
    sys.path.insert(0,str(root/'scripts'))
    import ds_graph_engine as engine
    engine.initialize(Path(__file__).resolve().parent)
    engine.ast()
