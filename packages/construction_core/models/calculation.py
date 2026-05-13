"""Calculation result models."""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class CalculationResult(BaseModel):
    """Structured calculation output with traceable evidence links."""

    calc_id: str
    project_id: str
    calc_type: str
    input_parameters: dict[str, Any] = Field(default_factory=dict)
    formula_refs: list[str] = Field(default_factory=list)
    intermediate_steps: list[dict[str, Any]] = Field(default_factory=list)
    final_result: Any
    pass_fail: str
    warnings: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)
