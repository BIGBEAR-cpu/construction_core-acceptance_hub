from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional

from backend.models.core_models import Rule


class RuleService:
    def __init__(self, rules_dir: Path | None = None) -> None:
        self.rules_dir = rules_dir or Path("knowledge_base/rules")
        self._rules: List[Rule] = []
        self.reload_rules()

    def reload_rules(self) -> None:
        loaded: List[Rule] = []
        if not self.rules_dir.exists():
            self._rules = []
            return
        for path in sorted(self.rules_dir.glob("*.json")):
            data = json.loads(path.read_text(encoding="utf-8"))
            loaded.append(Rule.model_validate(data))
        self._rules = loaded

    def get_all_rules(self) -> List[Rule]:
        return self._rules

    def get_rule_by_id(self, rule_id: str) -> Optional[Rule]:
        for rule in self._rules:
            if rule.rule_id == rule_id:
                return rule
        return None
