from __future__ import annotations

from pathlib import Path

from packages.acceptance_hub.checks.base import result
from packages.acceptance_hub.models import AcceptanceCheckResult
from packages.construction_core.models.export_package import ExportPackage


def run_check(package: ExportPackage, project_root: str | None = None) -> list[AcceptanceCheckResult]:
    root = Path(project_root or ".")
    items: list[AcceptanceCheckResult] = []
    for gf in package.generated_files:
        if gf.required and not (root / gf.file_path).exists():
            items.append(result("check_generated_files", "fail", f"required file missing: {gf.file_path}", gf.file_id))
    if not items:
        items.append(result("check_generated_files", "pass", "all required generated files exist"))
    return items
