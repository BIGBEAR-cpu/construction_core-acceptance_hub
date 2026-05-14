from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field


class SourceCitation(BaseModel):
    source_name: str
    location: Optional[str] = None
    note: Optional[str] = None


class Component(BaseModel):
    component_id: str
    category: str
    name: str
    properties: Dict[str, Any] = Field(default_factory=dict)
    source_ref: Dict[str, Any] = Field(default_factory=dict)
    confidence: float = 1.0


class DrawingElement(BaseModel):
    element_id: str
    element_type: str
    geometry_ref: Dict[str, Any] = Field(default_factory=dict)
    properties: Dict[str, Any] = Field(default_factory=dict)
    source_ref: Dict[str, Any] = Field(default_factory=dict)
    confidence: float = 1.0


class DetailNode(BaseModel):
    node_id: str
    title: str
    description: Optional[str] = None
    related_components: List[str] = Field(default_factory=list)


class QuantityItem(BaseModel):
    item_id: str
    name: str
    unit: str
    quantity: float
    formula: str
    inputs: Dict[str, Any] = Field(default_factory=dict)
    explanation: str


class Rule(BaseModel):
    rule_id: str
    title: str
    discipline: str
    description: str
    formula: Optional[str] = None
    check_logic: Optional[str] = None
    inputs: List[str] = Field(default_factory=list)
    source_citation: SourceCitation
    version: str


class ReviewIssue(BaseModel):
    issue_id: str
    rule_id: str
    severity: Literal["info", "warning", "error"] = "warning"
    message: str
    element_refs: List[str] = Field(default_factory=list)
    suggestion: Optional[str] = None
