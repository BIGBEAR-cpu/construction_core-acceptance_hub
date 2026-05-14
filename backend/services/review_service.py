from __future__ import annotations

from typing import Any, Dict, List

from backend.models.core_models import ReviewIssue
from backend.services.rule_service import RuleService


class ReviewService:
    def __init__(self, rule_service: RuleService) -> None:
        self.rule_service = rule_service

    def review_basic(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        rule_id = payload.get("rule_id")
        elements = payload.get("elements") or []
        issues: List[ReviewIssue] = []

        if not rule_id:
            return {"ok": False, "error": "rule_id is required", "issues": []}

        rule = self.rule_service.get_rule_by_id(rule_id)
        if not rule:
            return {"ok": False, "error": f"rule not found: {rule_id}", "issues": []}

        if not elements:
            return {"ok": True, "issues": []}

        for idx, element in enumerate(elements):
            if element.get("confidence", 0) < 0.5:
                issues.append(
                    ReviewIssue(
                        issue_id=f"issue-{idx}",
                        rule_id=rule_id,
                        severity="warning",
                        message="Low confidence element found.",
                        element_refs=[element.get("element_id", f"idx-{idx}")],
                        suggestion="Verify this element manually.",
                    )
                )
        return {"ok": True, "issues": [issue.model_dump() for issue in issues]}
