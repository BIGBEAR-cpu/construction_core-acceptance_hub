from __future__ import annotations

from packages.acceptance_hub.checks.base import result
from packages.acceptance_hub.models import AcceptanceCheckResult
from packages.construction_core.models.export_package import ExportPackage


def run_check(package: ExportPackage, project_root: str | None = None) -> list[AcceptanceCheckResult]:
    items: list[AcceptanceCheckResult] = []
    for q in package.quantities:
        if not q.item_name or not q.unit or not q.expression:
            items.append(result("check_quantities", "fail", "item_name/unit/expression required", q.quantity_id))
        if q.need_review and q.value is None:
            items.append(result("check_quantities", "warning", "need_review=true and value empty; manual review required", q.quantity_id))
        if not q.need_review and q.value is None:
            items.append(result("check_quantities", "fail", "need_review=false but value empty", q.quantity_id))
        if not q.rule_ref:
            items.append(result("check_quantities", "warning", "rule_ref is empty", q.quantity_id))
    if not items:
        items.append(result("check_quantities", "pass", "quantity checks passed"))
    return items
