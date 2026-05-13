from packages.construction_core.models.export_package import ExportPackage


SAMPLE_PATH = "data/samples/deep_excavation_export_package.json"


def test_export_package_can_parse() -> None:
    package = ExportPackage.from_json_file(SAMPLE_PATH)
    assert package.package_id


def test_project_info_project_id_exists() -> None:
    package = ExportPackage.from_json_file(SAMPLE_PATH)
    assert package.project_info.project_id


def test_dangerous_work_is_super_dangerous_true() -> None:
    package = ExportPackage.from_json_file(SAMPLE_PATH)
    assert package.dangerous_work.is_super_dangerous is True


def test_required_artifact_lists_have_data() -> None:
    package = ExportPackage.from_json_file(SAMPLE_PATH)
    assert len(package.calculations) >= 1
    assert len(package.drawings) >= 1
    assert len(package.quantities) >= 1
    assert len(package.documents) >= 1
