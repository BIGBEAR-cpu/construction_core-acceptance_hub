from __future__ import annotations

from packages.acceptance_hub.models import AcceptanceReport


def render_json_report(report: AcceptanceReport) -> str:
    """Render acceptance report to JSON string."""
    return report.model_dump_json(indent=2)
