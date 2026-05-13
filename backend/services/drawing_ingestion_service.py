from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from backend.models.drawing_models import ParsedDrawingResult


class DrawingIngestionService:
    def __init__(self, examples_dir: Path | None = None) -> None:
        self.examples_dir = examples_dir or Path("examples")

    def mock_parse(self) -> ParsedDrawingResult:
        data = json.loads((self.examples_dir / "sample_drawing_raw.json").read_text(encoding="utf-8"))
        return ParsedDrawingResult.model_validate(data)

    def normalize_elements(self, payload: Dict[str, Any]) -> ParsedDrawingResult:
        return ParsedDrawingResult.model_validate(payload)

    def validate_parsed_result(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        ParsedDrawingResult.model_validate(payload)
        return {"ok": True}
