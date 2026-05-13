from __future__ import annotations

from packages.acceptance_hub.checks.base import result
from packages.acceptance_hub.models import AcceptanceCheckResult
from packages.construction_core.models.export_package import ExportPackage


def run_check(package: ExportPackage, project_root: str | None = None) -> list[AcceptanceCheckResult]:
    items: list[AcceptanceCheckResult] = []
    for d in package.documents:
        if not d.document_type:
            items.append(result("check_documents", "fail", "document_type is required", d.document_id))
        if not d.section_summaries:
            items.append(result("check_documents", "warning", "section_summaries is empty", d.document_id))
        if not d.source_citation_ids:
            items.append(result("check_documents", "warning", "source_citation_ids is empty", d.document_id))
        if d.review_status == "needs_revision":
            items.append(result("check_documents", "warning", "review_status needs_revision", d.document_id))
    if not items:
        items.append(result("check_documents", "pass", "document checks passed"))
    return items
