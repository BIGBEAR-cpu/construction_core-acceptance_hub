"""Evidence and source citation models."""
from __future__ import annotations

from pydantic import BaseModel, Field


class SourceCitation(BaseModel):
    """Traceable source citation used by generated outputs."""

    citation_id: str
    source_type: str
    source_name: str
    source_location: str
    quoted_text: str
    is_mock: bool = True


class EvidenceLink(BaseModel):
    """Evidence linkage between outputs and upstream sources."""

    evidence_id: str
    related_output_id: str
    source_type: str
    source_name: str
    source_location: str
    confidence: float = Field(ge=0.0, le=1.0)
    note: str
    is_mock: bool = True
