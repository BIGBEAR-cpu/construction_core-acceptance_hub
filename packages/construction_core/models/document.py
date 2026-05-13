"""Document artifact models."""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


DocumentReviewStatus = Literal["draft", "reviewed", "approved", "rejected", "needs_revision"]


class DocumentArtifact(BaseModel):
    """Represents generated engineering document artifacts."""

    document_id: str
    project_id: str
    document_type: str
    file_path: str
    section_summaries: list[str] = Field(default_factory=list)
    source_citation_ids: list[str] = Field(default_factory=list)
    linked_calculation_ids: list[str] = Field(default_factory=list)
    linked_drawing_ids: list[str] = Field(default_factory=list)
    linked_quantity_ids: list[str] = Field(default_factory=list)
    review_status: DocumentReviewStatus
    evidence_ids: list[str] = Field(default_factory=list)
