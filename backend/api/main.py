from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from backend.services.drawing_ingestion_service import DrawingIngestionService
from backend.services.quantity_service import QuantityService
from backend.services.review_service import ReviewService
from backend.services.rule_service import RuleService

app = FastAPI(title="AI Construction Detailing Engine - P0")

rule_service = RuleService()
quantity_service = QuantityService(rule_service)
review_service = ReviewService(rule_service)
drawing_service = DrawingIngestionService()


@app.get("/health")
def health() -> dict:
    return {"ok": True, "stage": "P0", "service": "construction-detailing-engine"}


@app.get("/rules")
def get_rules() -> dict:
    return {"ok": True, "rules": [r.model_dump() for r in rule_service.get_all_rules()]}


@app.get("/rules/{rule_id}")
def get_rule(rule_id: str):
    if not rule_id.strip():
        return JSONResponse(status_code=400, content={"ok": False, "error": "rule_id cannot be empty"})
    rule = rule_service.get_rule_by_id(rule_id)
    if not rule:
        return JSONResponse(status_code=404, content={"ok": False, "error": f"rule not found: {rule_id}"})
    return {"ok": True, "rule": rule.model_dump()}


@app.post("/quantity/explain")
def quantity_explain(payload: dict):
    return quantity_service.explain_quantity(payload)


@app.post("/review/basic")
def review_basic(payload: dict):
    return review_service.review_basic(payload)


@app.post("/drawings/parse/mock")
def drawings_parse_mock():
    try:
        return {"ok": True, "result": drawing_service.mock_parse().model_dump()}
    except Exception as exc:  # noqa: BLE001
        return JSONResponse(status_code=500, content={"ok": False, "error": f"mock parse failed: {exc}"})


@app.post("/drawings/normalize")
def drawings_normalize(payload: dict):
    try:
        result = drawing_service.normalize_elements(payload)
        return {"ok": True, "result": result.model_dump()}
    except ValidationError as exc:
        return JSONResponse(status_code=400, content={"ok": False, "error": "invalid drawing payload", "details": exc.errors()})


@app.get("/drawings/schema")
def drawings_schema():
    return {
        "ok": True,
        "flow": "PDF/CAD/BIM Source -> Drawing Ingestion -> Common Drawing Data -> Quantity/Review/Detailing",
        "source_type": ["PDF", "DXF", "DWG", "IFC", "RVT"],
        "geometry_types": ["point", "line", "polyline", "polygon", "circle", "arc", "bbox"],
        "core_fields": {
            "source_ref": "trace to file/page/layer/original_object_id",
            "confidence": "0~1 detection confidence",
        },
    }
