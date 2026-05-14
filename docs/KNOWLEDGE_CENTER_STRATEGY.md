# KNOWLEDGE CENTER STRATEGY（知识中心策略）v0.1

## 1. 核心策略
采用“**统一知识库中心 + 分包架构**”。
- 不允许每个项目各建一套生产知识库。
- 不允许把所有知识堆成单一巨大 JSON 或单一总向量库。

## 2. 知识包目录（Package Taxonomy）
- `regulations`
- `technical_codes`
- `construction_methods`
- `calculation_templates`
- `quality_rules`
- `safety_rules`
- `quantity_rules`
- `document_templates`
- `cases`
- `project_overlays`

## 3. 统一标识与元数据
### 3.1 ID 规则（示例）
`{package}.{domain}.{item_slug}.v{major}.{minor}`

示例：
- `technical_codes.concrete.gb50010_clause_8_3.v1.0`
- `quantity_rules.rebar.length_calc_template_a.v2.1`

### 3.2 统一 metadata
最小字段建议：
- `knowledge_id`
- `package`
- `domain`
- `title`
- `version`
- `status`
- `language`
- `region`
- `effective_date`
- `updated_at`
- `owners`
- `citation`
- `source_ref`

## 4. 统一 citation 规范
- 每个知识项必须有 citation，至少包含来源类型、出处定位、摘录信息。
- 规则项引用规范条款时必须保留“规则 -> 条款”映射关系。
- 无 citation 的知识或规则不得进入生产链路。

## 5. 统一 version 策略
- 采用语义化版本（SemVer）：`major.minor.patch`。
- `major`：破坏性变更；`minor`：向后兼容新增；`patch`：修订。
- 规则执行需记录命中版本，支持历史追溯与结果复算。

## 6. 统一 status 生命周期
`draft -> parsed -> reviewed -> approved -> deprecated -> superseded`

- 默认仅 `approved` 可进入生产链路。
- `deprecated` 可查询不可默认命中。
- `superseded` 必须指向替代版本。

## 7. 向量索引策略
- 按知识包拆分向量索引（如 quantity_rules 索引、safety_rules 索引）。
- 检索时先按包过滤，再按项目上下文与权限过滤。
- 禁止加载未知来源向量索引。

## 8. 项目级知识策略（Overlay）
- 项目级知识仅允许存放在 `project_overlays`。
- Overlay 只能增量覆盖，不得改写通用基础知识原文。
- Overlay 需声明适用项目、有效期、审批人、关联基础知识版本。

## 9. 治理与验收
- 所有知识包变更必须经过 Acceptance Hub 的测试与审核门槛。
- 关键包（safety_rules / quantity_rules / technical_codes）必须有双人复核。
- 发布前必须验证：citation 完整、状态合规、版本可追溯。
