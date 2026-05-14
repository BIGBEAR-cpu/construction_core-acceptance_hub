from __future__ import annotations

import json
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
    from backend.api.main import app

    if app is None:
        raise RuntimeError("backend.api.main:app is not importable")


def check_examples_exists() -> None:
    examples_dir = Path("examples")
    if not examples_dir.exists() or not examples_dir.is_dir():
        raise FileNotFoundError("examples directory is missing")



def check_rules_loadable() -> None:
    rules_dir = Path("knowledge_base/rules")
    if not rules_dir.exists() or not rules_dir.is_dir():
        raise FileNotFoundError("knowledge_base/rules directory is missing")

    rules = sorted(rules_dir.glob("*.json"))
    if not rules:
        raise RuntimeError("knowledge_base/rules has no rule json files")

    for rule_path in rules:
        with rule_path.open("r", encoding="utf-8") as fp:
            json.load(fp)


def check_docs_exists() -> None:
    p0_acceptance = Path("docs/P0_ACCEPTANCE.md")
    if not p0_acceptance.exists():
        raise FileNotFoundError("docs/P0_ACCEPTANCE.md is missing")


def main() -> int:
    check_import()
    check_examples_exists()
    check_rules_loadable()
    check_docs_exists()
    return run_pytest()


if __name__ == "__main__":
    raise SystemExit(main())
