from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def run_pytest() -> int:
    cmd = [sys.executable, "-m", "pytest", "-q"]
    result = subprocess.run(cmd, check=False)
    return result.returncode


def check_import() -> None:
    from backend.api.main import app  # noqa: F401


def check_files() -> None:
    required_examples = [
        "sample_components.json",
        "sample_quantity_request.json",
        "sample_review_request.json",
        "sample_drawing_raw.json",
        "sample_parsed_drawing.json",
        "sample_floor_plan_elements.json",
    ]
    for filename in required_examples:
        path = Path("examples") / filename
        if not path.exists():
            raise FileNotFoundError(f"missing example file: {path}")

    rules = list(Path("knowledge_base/rules").glob("*.json"))
    if len(rules) < 3:
        raise RuntimeError("knowledge_base/rules requires at least 3 rule files")

    required_docs = [
        Path("docs/P0_ACCEPTANCE.md"),
        Path("docs/COMMON_DRAWING_DATA.md"),
    ]
    for path in required_docs:
        if not path.exists():
            raise FileNotFoundError(f"missing doc file: {path}")


def main() -> int:
    check_import()
    check_files()
    return run_pytest()


if __name__ == "__main__":
    raise SystemExit(main())
