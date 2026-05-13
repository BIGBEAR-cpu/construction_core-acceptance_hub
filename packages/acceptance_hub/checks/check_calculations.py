from __future__ import annotations

from packages.acceptance_hub.checks.base import result
from packages.acceptance_hub.models import AcceptanceCheckResult
from packages.construction_core.models.export_package import ExportPackage


def run_check(package: ExportPackage, project_root: str | None = None) -> list[AcceptanceCheckResult]:
    items: list[AcceptanceCheckResult] = []
    for calc in package.calculations:
        if not calc.input_parameters:
            items.append(result("check_calculations", "fail", "input_parameters is empty", calc.calc_id))
        if calc.final_result is None:
            items.append(result("check_calculations", "fail", "final_result is empty", calc.calc_id))
        if not calc.formula_refs:
            items.append(result("check_calculations", "warning", "formula_refs is empty", calc.calc_id))
        if not calc.evidence_ids:
            items.append(result("check_calculations", "warning", "evidence_ids is empty", calc.calc_id))
    if not items:
        items.append(result("check_calculations", "pass", "calculations checks passed"))
    return items
