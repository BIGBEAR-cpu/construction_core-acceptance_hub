"""Review issue models."""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel


ReviewSeverity = Literal["info", "warning", "error", "critical"]
ReviewStatus = Literal["open", "resolved", "ignored"]


class ReviewIssue(BaseModel):
    """Represents a review issue found during quality/compliance checks."""

    issue_id: str
    severity: ReviewSeverity
    category: str
    message: str
    related_artifact_id: str
    suggestion: str
    status: ReviewStatus


class GeneratedFile(BaseModel):
    """Represents generated files expected from a project package."""

    file_id: str
    artifact_type: str
    file_path: str
    description: str
    required: bool
