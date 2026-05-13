"""Drawing artifact models."""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


DrawingValidationStatus = Literal["pass", "warning", "fail", "not_checked"]


class DrawingArtifact(BaseModel):
    """Represents an engineering drawing output artifact."""

    drawing_id: str
    project_id: str
    drawing_type: str
    file_path: str
    validation_status: DrawingValidationStatus
    layer_summary: dict[str, int] = Field(default_factory=dict)
    related_calculation_ids: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)
