from __future__ import annotations

from packages.acceptance_hub.checks.base import result
from packages.acceptance_hub.models import AcceptanceCheckResult
from packages.construction_core.models.export_package import ExportPackage


def run_check(package: ExportPackage, project_root: str | None = None) -> list[AcceptanceCheckResult]:
    items: list[AcceptanceCheckResult] = []
    pi = package.project_info
    if not pi:
        return [result("check_project_info", "fail", "project_info is missing")]
    if not pi.project_id:
        items.append(result("check_project_info", "fail", "project_id is missing"))
    if not pi.project_name:
        items.append(result("check_project_info", "fail", "project_name is missing"))
    if not items:
        items.append(result("check_project_info", "pass", "project_info is valid"))
    return items
