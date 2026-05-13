from pathlib import Path

from packages.acceptance_hub.acceptance_runner import run_acceptance
from packages.construction_core.models.export_package import ExportPackage


SAMPLE_PATH = "data/samples/deep_excavation_export_package.json"


def test_run_acceptance_on_sample() -> None:
    report = run_acceptance(SAMPLE_PATH, project_root=".")
    assert report.overall_status in {"PASS", "PARTIAL_PASS", "FAIL"}


def test_overall_status_not_crash_and_expected_range() -> None:
    report = run_acceptance(SAMPLE_PATH, project_root=".")
    assert report.overall_status in {"PASS", "PARTIAL_PASS"}


def test_missing_evidence_links_produces_warning(tmp_path: Path) -> None:
    package = ExportPackage.from_json_file(SAMPLE_PATH)
    package.evidence_links = []
    test_file = tmp_path / "no_evidence.json"
    package.to_json_file(test_file)
    report = run_acceptance(str(test_file), project_root=".")
    assert any(r.check_name == "check_evidence_links" and r.status == "warning" for r in report.results)


def test_missing_required_generated_file_produces_fail(tmp_path: Path) -> None:
    package = ExportPackage.from_json_file(SAMPLE_PATH)
    package.generated_files[0].file_path = "data/samples/generated_files/not_exists.mock"
    test_file = tmp_path / "missing_file.json"
    package.to_json_file(test_file)
    report = run_acceptance(str(test_file), project_root=".")
    assert any(r.check_name == "check_generated_files" and r.status == "fail" for r in report.results)


def test_drawing_validation_fail_produces_fail(tmp_path: Path) -> None:
    package = ExportPackage.from_json_file(SAMPLE_PATH)
    package.drawings[0].validation_status = "fail"
    test_file = tmp_path / "drawing_fail.json"
    package.to_json_file(test_file)
    report = run_acceptance(str(test_file), project_root=".")
    assert any(r.check_name == "check_drawings" and r.status == "fail" for r in report.results)


def test_need_review_true_quantity_warns_or_info(tmp_path: Path) -> None:
    package = ExportPackage.from_json_file(SAMPLE_PATH)
    package.quantities[1].need_review = True
    package.quantities[1].value = None
    test_file = tmp_path / "qty_review.json"
    package.to_json_file(test_file)
    report = run_acceptance(str(test_file), project_root=".")
    assert any(r.check_name == "check_quantities" and r.status in {"warning", "pass"} for r in report.results)
