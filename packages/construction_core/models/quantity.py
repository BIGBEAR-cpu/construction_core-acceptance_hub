"""Quantity output models."""
from __future__ import annotations

from pydantic import BaseModel, Field


class QuantityResult(BaseModel):
    """Represents a quantity result and its rule/evidence context."""

    quantity_id: str
    project_id: str
    source_element_id: str
    item_name: str
    unit: str
    expression: str
    value: float | None = None
    rule_ref: str | None = None
    quota_suggestion: str | None = None
    need_review: bool
    evidence_ids: list[str] = Field(default_factory=list)
