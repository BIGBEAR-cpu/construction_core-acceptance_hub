# P0.1 Acceptance Report

Date: 2026-05-13 (UTC)

## Scope
本次仅进行 P0 验收修复：依赖与可复现、测试执行路径、CI、检查脚本与验收记录。未新增 P1 能力，未实现真实 PDF/CAD/DWG/IFC/RVT 解析。

## Commands Actually Executed

1. `python -m pytest -q`
   - Result: **Failed in collection**
   - Error Summary:
     - `ModuleNotFoundError: No module named 'fastapi'`
     - `ModuleNotFoundError: No module named 'pydantic'`
   - Conclusion: 当前执行环境缺少依赖，pytest 未通过。

2. `python scripts/check_all.py`
   - Result: **Failed**
   - Error Summary:
     - `ModuleNotFoundError: No module named 'fastapi'` during `import backend.api.main:app`
   - Conclusion: 检查脚本逻辑已就位，但环境未安装依赖导致失败。

## What Was Added/Adjusted in This P0.1 Fix

- Added `pyproject.toml` with:
  - project name: `construction-core-acceptance-hub`
  - version: `0.1.0`
  - python: `>=3.10`
  - minimal pytest config
  - dependency set aligned with `requirements.txt`
- Added GitHub Actions CI workflow at `.github/workflows/ci.yml`:
  - checkout
  - setup-python (3.10 / 3.11)
  - `pip install -r requirements.txt`
  - `python -m pytest -q`
- Added `scripts/check_all.py`:
  - run `python -m pytest -q`
  - import `backend.api.main:app`
  - verify required files in `examples/`
  - verify at least 3 rule files in `knowledge_base/rules/`
  - verify docs: `docs/P0_ACCEPTANCE.md` and `docs/COMMON_DRAWING_DATA.md`

## Pytest Status
- Local current environment: **NOT PASSING** (dependency installation unavailable in this environment).
- CI status: **Configured**; should serve as acceptance environment once network/package index is available.

## CI Status
- CI workflow added: `.github/workflows/ci.yml`

## Currently Supported (P0)
- FastAPI API skeleton and endpoint set.
- Core Pydantic models and common drawing data model.
- Rule loading/query service and sample rules.
- Mock drawing parse/normalize flow.
- Basic quantity explanation and review output.

## Explicitly NOT Supported
- Real PDF/CAD/DWG/IFC/RVT parsing.
- Complex AI reasoning.
- Full code-compliance checking and production-grade quantity engine.

