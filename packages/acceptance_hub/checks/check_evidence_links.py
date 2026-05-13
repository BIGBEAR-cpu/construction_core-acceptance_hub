from __future__ import annotations

from packages.acceptance_hub.checks.base import result
from packages.acceptance_hub.models import AcceptanceCheckResult
from packages.construction_core.models.export_package import ExportPackage


def run_check(package: ExportPackage, project_root: str | None = None) -> list[AcceptanceCheckResult]:
    items: list[AcceptanceCheckResult] = []
    valid_ids = {e.evidence_id for e in package.evidence_links}
    if not package.evidence_links:
        items.append(result("check_evidence_links", "warning", "evidence_links is empty"))
    refs: list[tuple[str, str, list[str]]] = []
    refs += [("calculation", c.calc_id, c.evidence_ids) for c in package.calculations]
    refs += [("drawing", d.drawing_id, d.evidence_ids) for d in package.drawings]
    refs += [("quantity", q.quantity_id, q.evidence_ids) for q in package.quantities]
    refs += [("document", d.document_id, d.evidence_ids) for d in package.documents]
    for kind, rid, ids in refs:
        for eid in ids:
            if eid not in valid_ids:
                items.append(result("check_evidence_links", "warning", f"{kind} references missing evidence_id: {eid}", rid))
    if not items:
        items.append(result("check_evidence_links", "pass", "evidence link checks passed"))
    return items
