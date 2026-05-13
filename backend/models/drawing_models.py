from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field

SourceType = Literal["PDF", "DXF", "DWG", "IFC", "RVT"]
GeometryType = Literal["point", "line", "polyline", "polygon", "circle", "arc", "bbox"]


class Geometry(BaseModel):
    geometry_type: GeometryType
    coordinates: Any
    properties: Dict[str, Any] = Field(default_factory=dict)


class DrawingFile(BaseModel):
    file_id: str
    filename: str
    source_type: SourceType
    uri: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class DrawingLayer(BaseModel):
    layer_id: str
    name: str
    category: Optional[str] = None


class SourceRef(BaseModel):
    file_id: str
    page_id: Optional[str] = None
    layer_id: Optional[str] = None
    original_object_id: Optional[str] = None


class DrawingElement(BaseModel):
    element_id: str
    element_type: str
    geometry: Geometry
    layer_id: Optional[str] = None
    properties: Dict[str, Any] = Field(default_factory=dict)
    source_ref: SourceRef
    confidence: float


class TextAnnotation(BaseModel):
    annotation_id: str
    text: str
    position: Geometry
    source_ref: SourceRef
    confidence: float


class DimensionAnnotation(BaseModel):
    annotation_id: str
    label: str
    value: float
    unit: str = "mm"
    geometry: Geometry
    source_ref: SourceRef
    confidence: float


class GridLine(BaseModel):
    grid_id: str
    name: str
    axis: Literal["X", "Y"]
    geometry: Geometry
    source_ref: SourceRef
    confidence: float


class ComponentCandidate(BaseModel):
    candidate_id: str
    category: str
    linked_element_ids: List[str] = Field(default_factory=list)
    inferred_properties: Dict[str, Any] = Field(default_factory=dict)
    source_ref: SourceRef
    confidence: float


class DrawingPage(BaseModel):
    page_id: str
    page_number: int
    name: Optional[str] = None
    layers: List[DrawingLayer] = Field(default_factory=list)
    elements: List[DrawingElement] = Field(default_factory=list)
    text_annotations: List[TextAnnotation] = Field(default_factory=list)
    dimension_annotations: List[DimensionAnnotation] = Field(default_factory=list)
    grid_lines: List[GridLine] = Field(default_factory=list)
    component_candidates: List[ComponentCandidate] = Field(default_factory=list)


class ParsedDrawingResult(BaseModel):
    drawing_file: DrawingFile
    pages: List[DrawingPage] = Field(default_factory=list)
    parse_notes: List[str] = Field(default_factory=list)
    parser_version: str = "mock-parser-0.1"
