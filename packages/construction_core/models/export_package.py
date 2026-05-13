"""Export package model aggregation and serialization helpers."""
from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from .calculation import CalculationResult
from .dangerous_work import DangerousWork
from .document import DocumentArtifact
from .drawing import DrawingArtifact
from .evidence import EvidenceLink, SourceCitation
from .project import ProjectInfo
from .quantity import QuantityResult
from .review import GeneratedFile, ReviewIssue


class ExportPackage(BaseModel):
    """Top-level package used for cross-project delivery and acceptance."""

    package_id: str
    project_info: ProjectInfo
    dangerous_work: DangerousWork
    source_citations: list[SourceCitation] = Field(default_factory=list)
    evidence_links: list[EvidenceLink] = Field(default_factory=list)
    calculations: list[CalculationResult] = Field(default_factory=list)
    drawings: list[DrawingArtifact] = Field(default_factory=list)
    quantities: list[QuantityResult] = Field(default_factory=list)
    documents: list[DocumentArtifact] = Field(default_factory=list)
    review_issues: list[ReviewIssue] = Field(default_factory=list)
    generated_files: list[GeneratedFile] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)

    @classmethod
    def from_json_file(cls, path: str | Path) -> "ExportPackage":
        """Load an :class:`ExportPackage` from a JSON file path."""
        payload = Path(path).read_text(encoding="utf-8")
        return cls.model_validate_json(payload)

    def to_json_file(self, path: str | Path) -> None:
        """Write the package to a JSON file with UTF-8 encoding."""
        Path(path).write_text(self.model_dump_json(indent=2), encoding="utf-8")
