# Project Group Acceptance Report (MOCK SAMPLE)

- 数据声明：本报告基于 **mock/sample** 数据，仅用于验收流程示例。
- package_id: pkg_mock_deep_excavation_001
- project_id: proj_mock_001
- overall_status: PARTIAL_PASS
- passed_count: 4
- warning_count: 4
- failed_count: 0

## Check Results（示例）
- [pass] check_project_info: project_info is valid
- [pass] check_generated_files: all required generated files exist
- [pass] check_calculations: calculations checks passed
- [warning] check_drawings: drawing not checked (drawing_001)
- [warning] check_quantities: need_review=true and value empty; manual review required (quantity_002)
- [warning] check_quantities: rule_ref is empty (quantity_002)
- [pass] check_documents: document checks passed
- [warning] check_evidence_links: quantity references missing evidence_id (quantity_002)

## 备注
- `need_review=true` 的工程量项需要人工复核。
- 本报告不代表真实工程结论。
