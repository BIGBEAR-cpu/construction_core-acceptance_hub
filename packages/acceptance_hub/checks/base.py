from __future__ import annotations

from packages.acceptance_hub.models import AcceptanceCheckResult
from packages.construction_core.models.export_package import ExportPackage


def result(check_name: str, status: str, message: str, related_id: str | None = None, suggestion: str | None = None) -> AcceptanceCheckResult:
    """Create a standard acceptance check result item."""
    return AcceptanceCheckResult(
        check_name=check_name,
        status=status,  # type: ignore[arg-type]
        severity=status,
        message=message,
        related_id=related_id,
        suggestion=suggestion,
    )


def run_check(package: ExportPackage, project_root: str | None = None) -> list[AcceptanceCheckResult]:
    raise NotImplementedError
