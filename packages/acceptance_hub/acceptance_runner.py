"""Acceptance runner for export packages."""
from __future__ import annotations

import argparse
from pathlib import Path

from packages.acceptance_hub.checks import (
    check_calculations,
    check_documents,
    check_drawings,
    check_evidence_links,
    check_generated_files,
    check_project_info,
    check_quantities,
)
from packages.acceptance_hub.models import AcceptanceCheckResult, AcceptanceReport
from packages.acceptance_hub.reports.markdown_report import render_markdown_report
from packages.construction_core.models.export_package import ExportPackage


def run_acceptance(package_path: str, project_root: str | None = None) -> AcceptanceReport:
    """Run acceptance checks against a package file."""
    package = ExportPackage.from_json_file(package_path)
    root = project_root or str(Path(package_path).resolve().parents[2])
    checks = [
        check_project_info.run_check,
        check_generated_files.run_check,
        check_calculations.run_check,
        check_drawings.run_check,
        check_quantities.run_check,
        check_documents.run_check,
        check_evidence_links.run_check,
    ]
    results: list[AcceptanceCheckResult] = []
    for check in checks:
        results.extend(check(package, root))

    failed_count = sum(1 for r in results if r.status == "fail")
    warning_count = sum(1 for r in results if r.status == "warning")
    passed_count = sum(1 for r in results if r.status == "pass")

    overall_status = "PASS"
    if failed_count > 0:
        overall_status = "FAIL"
    elif warning_count > 0:
        overall_status = "PARTIAL_PASS"

    return AcceptanceReport(
        package_id=package.package_id,
        project_id=package.project_info.project_id,
        overall_status=overall_status,  # type: ignore[arg-type]
        passed_count=passed_count,
        warning_count=warning_count,
        failed_count=failed_count,
        results=results,
    )


def main() -> None:
    """CLI entrypoint."""
    parser = argparse.ArgumentParser(description="Run acceptance checks for mock export package")
    parser.add_argument("package_path", help="Path to export package JSON")
    parser.add_argument("--project-root", default=None)
    args = parser.parse_args()
    report = run_acceptance(args.package_path, args.project_root)
    print(render_markdown_report(report))


if __name__ == "__main__":
    main()
