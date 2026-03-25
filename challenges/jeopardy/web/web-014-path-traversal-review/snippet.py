from pathlib import Path


def read_note(base_dir: Path, name: str) -> str:
    target = base_dir / name
    return target.read_text(encoding="utf-8")
