from __future__ import annotations

from packages.acceptance_hub.checks.base import result
from packages.acceptance_hub.models import AcceptanceCheckResult
from packages.construction_core.models.export_package import ExportPackage


def run_check(package: ExportPackage, project_root: str | None = None) -> list[AcceptanceCheckResult]:
    items: list[AcceptanceCheckResult] = []
    for d in package.drawings:
        if not d.drawing_type or not d.file_path or not d.validation_status:
            items.append(result("check_drawings", "fail", "required drawing fields missing", d.drawing_id))
        if d.validation_status == "fail":
            items.append(result("check_drawings", "fail", "drawing validation failed", d.drawing_id))
        elif d.validation_status == "not_checked":
            items.append(result("check_drawings", "warning", "drawing not checked", d.drawing_id))
        if not d.evidence_ids:
            items.append(result("check_drawings", "warning", "drawing evidence_ids is empty", d.drawing_id))
    if not items:
        items.append(result("check_drawings", "pass", "drawing checks passed"))
    return items
