# Core Foundation P0.1 Freeze Report

日期：2026-05-14  
仓库：construction_core-acceptance_hub

## 1. 当前支持能力
- 提供 `backend.api.main:app` 的 FastAPI 应用入口。
- 提供核心模型、图纸公共数据结构与 mock 解析链路。
- 提供 `knowledge_base/rules` 示例规则及加载机制。
- 提供 `tests/` 自动化测试与 `scripts/check_all.py` 验收脚本框架。

## 2. 当前不支持能力
- 不支持真实 PDF / DWG / RVT / IFC 解析。
- 不支持生产级工程量计算、规范审图与施工详图生成。
- 不支持总控架构能力（已拆分到独立仓库维护）。

## 3. 测试结果（本次冻结执行）
- `pip install -r requirements.txt`：`BLOCKED`（网络/索引访问 403，依赖无法下载）。
- `python -m pytest -q`：失败（依赖缺失导致 `fastapi`、`pydantic` 无法导入）。
- `python scripts/check_all.py`：失败（`import backend.api.main:app` 阶段失败）。
- `uvicorn backend.api.main:app --reload`：`BLOCKED`（依赖未安装）。

## 4. 已知风险
- 运行依赖对外部 Python 包索引可用性敏感；离线或受限网络下不可复现。
- 当前验收对环境准备有前置要求（至少需可安装 FastAPI/Pydantic/Pytest/Uvicorn）。
- 若不引入内部镜像源或锁定离线包，冻结版本可运行性受环境波动影响。

## 5. 下一阶段建议
- 提供可访问的内部 PyPI 镜像或离线 wheel 包清单，降低安装失败风险。
- 在 CI 中增加 “依赖安装 + check_all” 的强制门禁，避免未验证状态进入主干。
- 为 `scripts/check_all.py` 增加更清晰的失败分类输出（依赖问题/文件问题/测试失败）。
- 维持当前“仅 Core Foundation + Acceptance Hub”边界，不引入总控架构代码。
