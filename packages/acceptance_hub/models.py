"""Acceptance hub report models."""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

CheckStatus = Literal["pass", "warning", "fail"]
OverallStatus = Literal["PASS", "PARTIAL_PASS", "FAIL"]


class AcceptanceCheckResult(BaseModel):
    """Single acceptance check result."""

    check_name: str
    status: CheckStatus
    severity: str
    message: str
    related_id: str | None = None
    suggestion: str | None = None


class AcceptanceReport(BaseModel):
    """Aggregated acceptance report for an export package."""

    package_id: str
    project_id: str
    overall_status: OverallStatus
    passed_count: int
    warning_count: int
    failed_count: int
    results: list[AcceptanceCheckResult] = Field(default_factory=list)
