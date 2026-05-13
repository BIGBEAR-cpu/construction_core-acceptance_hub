from __future__ import annotations

from packages.acceptance_hub.models import AcceptanceReport


def render_markdown_report(report: AcceptanceReport) -> str:
    """Render acceptance report to markdown text."""
    lines = [
        "# Project Group Acceptance Report (MOCK SAMPLE)",
        "",
        "- 数据声明：本报告基于 **mock/sample** 数据，仅用于流程演示。",
        f"- package_id: {report.package_id}",
        f"- project_id: {report.project_id}",
        f"- overall_status: {report.overall_status}",
        f"- passed_count: {report.passed_count}",
        f"- warning_count: {report.warning_count}",
        f"- failed_count: {report.failed_count}",
        "",
        "## Check Results",
    ]
    for item in report.results:
        lines.append(f"- [{item.status}] {item.check_name}: {item.message} ({item.related_id or 'N/A'})")
    return "\n".join(lines)
