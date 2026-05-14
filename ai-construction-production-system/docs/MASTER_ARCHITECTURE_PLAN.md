# AI Construction Production System 总控架构文档（迁移自 PR #3）

## 1. 系统定位
AI Construction Production System（以下简称 ACPS）是面向施工生产全生命周期的工程智能系统，而非单一聊天机器人。系统目标是通过统一公共数据、统一知识库、统一规则引擎、统一验收体系，把图纸解析、工程量计算、危大专项方案、施工详图、质量验收与资料生成等能力打通，形成可验证、可追溯、可迭代的生产链路。

## 2. 系统目标（Goals）
- 建立跨模块一致的公共数据模型与 API 契约，避免“同名异义”与重复建模。
- 建立统一 Knowledge & Rule Center，确保知识、规则、引用、版本可治理。
- 建立端到端可审计链路：输入来源可追溯、AI 判断有置信度、低置信度可进入人工复核。
- 建立 Acceptance Hub 作为统一验收与冻结机制，保证阶段性成果可控上线。
- 支撑多子项目协作：construction_core-acceptance_hub、AI-计量、bigxiangmu（危大）及后续模块。

## 3. 非目标（Non-Goals）
- 不把系统描述为可替代专业工程师、注册执业人员或专家论证。
- 不在当前阶段承诺“全自动、零人工复核”的生产级能力。
- 不在 Core Foundation 内直接实现完整 PDF/CAD/BIM 解析或全量业务规则。
- 不允许各子项目独立建设互不兼容的知识库、规则体系与核心模型。

## 4. 当前阶段（v0.1）
当前为架构规划与基线对齐阶段，重点是“先统一骨架，再扩展能力”：
- 统一公共模型与字段语义。
- 统一知识与规则中心治理策略。
- 统一模块边界与依赖方向。
- 统一阶段路线图与冻结门槛。

## 5. 总体模块划分
- **Core Foundation（construction_core-acceptance_hub）**：公共模型、API 契约、可追溯字段规范、验收基线。
- **Knowledge & Rule Center（未来建设）**：知识包与规则包统一治理、版本发布、状态管理。
- **Drawing Ingestion（未来建设）**：PDF/DXF/CAD/BIM 到 Common Drawing Data 的结构化转换。
- **Quantity Takeoff Engine（AI-计量）**：工程量计算、规则匹配、定额建议、审计导出。
- **Weida Plan Engine（bigxiangmu）**：危大/超危大判定、专项方案生成、合规检查与导出。
- **Detailing Engine（未来建设）**：构造节点建议、标准详图匹配、施工节点推荐。
- **Quality Acceptance / Document Engine（未来建设）**：质量验收项、资料生成、归档输出。
- **Acceptance Hub（construction_core-acceptance_hub）**：跨项目测试、审核、冻结、合并决策。

## 6. 子项目关系
- **construction_core-acceptance_hub**：作为“底座 + 验收中心”，定义公共契约并治理跨项目一致性。
- **AI-（计量子项目）**：消费公共模型与知识规则，输出计量与审计结果。
- **bigxiangmu（危大/超危大）**：消费公共模型与知识规则，输出专项方案与合规结论。
- **后续模块（Drawing/Detailing/Quality/Document）**：均以 Core 契约为唯一基础接口，并通过 Knowledge Center 共享知识。

## 7. 为什么必须统一 Core Foundation
- 同一 `DrawingElement`、`QuantityItem`、`ReviewIssue` 在不同项目含义必须一致。
- 统一 `source_ref` / `citation` / `confidence` / `requires_review` / `status` 字段，才能完成跨模块审计链路。
- 如果无统一 Core，后续会出现 API 碎片化、集成成本飙升、验收口径不一致。

## 8. 为什么必须统一 Knowledge & Rule Center
- 知识来源、版本、状态、引用口径必须集中治理，否则结果不可追溯。
- 同一规范条款在计量、危大、质检模块应复用同一知识实体，避免冲突结论。
- 规则包需要统一版本策略，支持回溯“某次输出为何如此判断”。

## 9. 为什么不能每个项目各搞一套知识库和数据模型
- 会导致重复录入、冲突更新、无法对齐版本。
- 会导致同一工程对象跨系统映射成本高，接口兼容性差。
- 会导致审计与责任追溯断链，无法形成企业级生产闭环。
- 会导致后期“推倒重来”，与本规划目标相悖。
