# Core Foundation P0.1 (Blocked Snapshot)

当前仓库状态无法进入 P0/P0.1 正常开发：仓库仅包含 `.gitattributes`，缺少 PR #2 / PR #3 所述代码与文档基线。

## 当前定位
- 目标定位应为 **Core Foundation P0/P0.1**。
- 理论上应仅支持 mock parse。
- 理论上不支持真实 PDF/DWG/RVT/IFC 解析。
- 理论上不支持生产级算量、审图、详图。

## 阻塞原因
- 缺失 `backend/`、`scripts/`、`docs/DATA_CONTRACTS.md`、`docs/ARCHITECTURE_GUARDRAILS.md` 等核心文件。
- 无法执行 DATA_CONTRACTS 对齐、模型检查、check_all 强化等任务。

## 建议
1. 先同步包含 PR #2 与 PR #3 的完整仓库内容到当前分支。
2. 重新触发 P0.1 开发任务。
