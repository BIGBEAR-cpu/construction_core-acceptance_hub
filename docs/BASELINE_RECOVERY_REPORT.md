# Baseline Recovery Report

Date: 2026-05-13  
Repo: `construction_core-acceptance_hub`  
Branch checked: `work`

## 1) PR 状态检查（#1/#2/#3/#4）

当前本地仓库没有配置远程（`git remote -v` 为空），且本地提交历史仅包含 `Initial commit` 与 `docs: add P0.1 blocked acceptance snapshot`。因此无法直接查询 GitHub 上 PR #1/#2/#3/#4 的实时状态（open/merged/closed）。

结论：**PR 状态 = NOT VERIFIED（信息来源缺失，不是代码执行失败）**。

## 2) 推荐合并顺序

建议采用以下顺序恢复主干基线：
1. PR #1（治理模板）
2. PR #3（总控架构）
3. PR #2（Core Foundation P0 初始脚手架）
4. PR #4（阻塞快照）不建议直接合并到主干能力基线；仅作为历史问题记录，并标记“已过期/已处置”。

## 3) 已合并内容（在当前本地可见）

当前分支可见内容：
- `.gitattributes`
- `README.md`（阻塞说明）
- `docs/P0_ACCEPTANCE.md`
- `docs/P0_1_ACCEPTANCE.md`

> 以上内容来自阻塞态记录，并不等于目标主干基线。

## 4) 未合并内容（目标基线缺口）

当前仓库**缺失**以下目标基线关键项：
- `AGENTS.md`
- `docs/management/`
- `docs/MASTER_ARCHITECTURE_PLAN.md`
- `docs/DATA_CONTRACTS.md`
- `docs/ARCHITECTURE_GUARDRAILS.md`
- `backend/`
- `requirements.txt` 或 `pyproject.toml`
- `scripts/check_all.py`
- `tests/`
- 可执行的 P0 级核心代码基线

## 5) main 当前包含的关键目录（以当前可见仓库内容为准）

由于未能获取主干远程状态，这里仅报告当前工作副本 HEAD：
- `docs/`（仅验收阻塞文档）
- 未包含 `backend/`、`tests/`、`scripts/`

结论：**不满足基线恢复目标**。

## 6) 测试命令与真实结果

1. `git status`
   - 结果：PASS（工作区干净）
2. `git ls-tree --name-only -r HEAD`
   - 结果：PASS（仅列出 4 个文件）
3. `pip install -r requirements.txt`
   - 结果：BLOCKED（代码基线缺失：`requirements.txt` 不存在）
4. `python -m pytest -q`
   - 结果：NOT VERIFIED（无测试文件，`no tests ran`）
5. `python scripts/check_all.py`
   - 结果：BLOCKED（代码基线缺失：脚本不存在）

## 7) 是否可以重新启动 Core Foundation P0.1

结论：**当前不可启动**。

原因：P0.1 依赖的治理、总控架构、初始脚手架尚未进入当前仓库基线。

## 8) 对 PR #4 的处理建议

- PR #4 应保留为“历史阻塞记录”，用于解释当时 main 空仓库导致的验收失败背景。
- 当 PR #1/#3/#2 完成并形成有效主干后，建议：
  - 将 PR #4 标记为 **Superseded / Historical**；
  - 或改写为 issue 附件，不作为功能/基线 PR 合并依据。

## 9) 下一步执行建议（操作清单）

1. 在有远程权限的环境拉取并核对 PR #1/#3/#2 代码内容。
2. 按推荐顺序完成合并并处理冲突。
3. 合并后复跑：
   - `pip install -r requirements.txt`
   - `python -m pytest -q`
   - `python scripts/check_all.py`
4. 仅在真实通过后，把 P0/P0.1 状态从 BLOCKED 切换为可执行。
