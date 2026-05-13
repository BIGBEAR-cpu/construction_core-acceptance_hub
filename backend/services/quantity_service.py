from __future__ import annotations

from typing import Any, Dict

from backend.models.core_models import QuantityItem
from backend.services.rule_service import RuleService


class QuantityService:
    def __init__(self, rule_service: RuleService) -> None:
        self.rule_service = rule_service

    def explain_quantity(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        rule_id = payload.get("rule_id")
        if not rule_id:
            return {"ok": False, "error": "rule_id is required"}

        rule = self.rule_service.get_rule_by_id(rule_id)
        if not rule:
            return {"ok": False, "error": f"rule not found: {rule_id}"}

        inputs = payload.get("inputs") or {}
        length = float(inputs.get("length", 0))
        width = float(inputs.get("width", 0))
        height = float(inputs.get("height", 0))
        quantity = round(length * width * (height if height else 1), 3)

        item = QuantityItem(
            item_id=f"qty-{rule_id}",
            name=rule.title,
            unit=inputs.get("unit", "m3"),
            quantity=quantity,
            formula=rule.formula or "length * width * height",
            inputs=inputs,
            explanation="P0 sample quantity explanation based on provided dimensions.",
        )
        return {"ok": True, "rule_id": rule_id, "quantity_item": item.model_dump()}
