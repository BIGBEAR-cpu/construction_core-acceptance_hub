# construction_core & acceptance_hub 架构说明（P2）

> 声明：本文涉及的数据结构与样例均为 **mock/sample**，不包含真实工程规范条文、真实公式、真实定额或真实工程数据。

## 目标
- 为 midasW、超危大工程文档自动输出、AI 自动计量提供统一的导出包模型（construction_core）。
- 提供统一验收入口（acceptance_hub）执行结构完整性、证据链完整性与关键字段检查。

## 关键模块
- `packages/construction_core/models`：核心数据模型。
- `packages/construction_core/validators`：包级校验入口。
- `packages/acceptance_hub/checks`：验收检查项。
- `packages/acceptance_hub/reports`：Markdown/JSON 报告输出。

## 接入方式
1. 业务项目生成 ExportPackage JSON。
2. 验收中台调用 `run_acceptance(package_path, project_root)`。
3. 输出结构化报告并进入人工复核或合并流程。
