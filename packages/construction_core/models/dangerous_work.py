"""Dangerous work classification models."""
from __future__ import annotations

from pydantic import BaseModel, Field


class DangerousWork(BaseModel):
    """Describes whether a project work item is dangerous/super-dangerous."""

    work_type: str
    is_dangerous: bool
    is_super_dangerous: bool
    trigger_reason: str
    threshold_rule_ref: str
    required_documents: list[str] = Field(default_factory=list)
    required_calculations: list[str] = Field(default_factory=list)
    required_drawings: list[str] = Field(default_factory=list)
