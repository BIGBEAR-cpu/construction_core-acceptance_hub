# DATA CONTRACTS（统一数据契约）v0.1

> 目标：定义跨模块必须统一的数据对象，保障接口兼容、审计可追溯、知识复用可治理。

## 全局字段规范（适用于多数模型）
- `source_ref`：来源引用标识（文件/页码/块/坐标/解析任务）
- `citation`：可读引用信息（规范条款、文档片段、来源 URI）
- `confidence`：0~1 的置信度
- `requires_review`：是否必须人工复核（布尔）
- `status`：统一状态机（如 draft/parsed/reviewed/approved/deprecated/superseded）

---

## 1) Project
- **用途**：统一工程项目上下文。
- **所属模块**：Core Foundation。
- **必须字段**：`project_id`, `name`, `region`, `stage`, `created_at`, `status`。
- **可选字段**：`owner`, `participants`, `tags`, `metadata`。
- **不允许滥用字段**：`metadata`（禁止塞入未建模核心业务字段）。
- **下游消费者**：全部模块。

## 2) DrawingFile
- **用途**：描述输入图纸文件。
- **所属模块**：Drawing Ingestion / Core Foundation。
- **必须字段**：`file_id`, `project_id`, `file_type`, `storage_uri`, `checksum`, `source_ref`, `status`。
- **可选字段**：`discipline`, `uploaded_by`, `uploaded_at`。
- **不允许滥用字段**：`storage_uri`（禁止写入临时本地路径作为长期引用）。
- **下游消费者**：Drawing Ingestion、Quantity、Weida、Detailing。

## 3) DrawingPage
- **用途**：描述图纸分页/图框级信息。
- **所属模块**：Drawing Ingestion。
- **必须字段**：`page_id`, `file_id`, `page_no`, `scale_hint`, `source_ref`, `status`。
- **可选字段**：`title`, `revision`, `bbox`。
- **不允许滥用字段**：`scale_hint`（禁止作为最终计量比例唯一依据）。
- **下游消费者**：Quantity、Review、Detailing。

## 4) Geometry
- **用途**：统一几何表达。
- **所属模块**：Core Foundation / Drawing Ingestion。
- **必须字段**：`geometry_id`, `type`, `coordinates`, `unit`, `source_ref`, `confidence`。
- **可选字段**：`transform`, `layer`, `properties`。
- **不允许滥用字段**：`properties`（禁止承载规则结论）。
- **下游消费者**：Quantity、Detailing、Quality。

## 5) DrawingElement
- **用途**：图元级结构化对象。
- **所属模块**：Drawing Ingestion。
- **必须字段**：`element_id`, `page_id`, `element_type`, `geometry_id`, `source_ref`, `confidence`, `status`。
- **可选字段**：`text`, `symbol`, `layer`, `attributes`。
- **不允许滥用字段**：`attributes`（禁止塞入跨模块标准字段）。
- **下游消费者**：Quantity、Weida、Detailing、Quality。

## 6) Component
- **用途**：工程构件标准对象。
- **所属模块**：Core Foundation。
- **必须字段**：`component_id`, `project_id`, `category`, `name`, `source_ref`, `status`。
- **可选字段**：`spec`, `material`, `geometry_refs`, `tags`。
- **不允许滥用字段**：`tags`（禁止替代分类体系）。
- **下游消费者**：Quantity、Weida、Detailing、Quality。

## 7) ComponentCandidate
- **用途**：待确认构件候选（AI/规则提取结果）。
- **所属模块**：Drawing Ingestion / Review。
- **必须字段**：`candidate_id`, `project_id`, `derived_from`, `confidence`, `requires_review`, `status`。
- **可选字段**：`proposed_component`, `reasons`, `citation`。
- **不允许滥用字段**：`reasons`（禁止写入无证据推断）。
- **下游消费者**：Review、Quantity、Weida。

## 8) Rule
- **用途**：可执行规则实体。
- **所属模块**：Knowledge & Rule Center。
- **必须字段**：`rule_id`, `rule_type`, `version`, `status`, `citation`, `effective_date`。
- **可选字段**：`scope`, `conditions`, `actions`, `priority`。
- **不允许滥用字段**：`scope`（禁止写成无限范围默认生效）。
- **下游消费者**：Quantity、Weida、Detailing、Quality。

## 9) KnowledgeItem
- **用途**：知识条目（规范条文、工法、模板、案例等）。
- **所属模块**：Knowledge & Rule Center。
- **必须字段**：`knowledge_id`, `package`, `title`, `version`, `status`, `citation`, `source_ref`。
- **可选字段**：`summary`, `keywords`, `embedding_ref`, `metadata`。
- **不允许滥用字段**：`embedding_ref`（禁止引用未知来源索引）。
- **下游消费者**：全部业务引擎。

## 10) SourceCitation
- **用途**：统一来源与引用对象。
- **所属模块**：Core Foundation / Knowledge Center。
- **必须字段**：`citation_id`, `source_type`, `source_ref`, `excerpt`, `locator`, `status`。
- **可选字段**：`uri`, `publisher`, `published_at`。
- **不允许滥用字段**：`excerpt`（禁止伪造原文、禁止无出处引用）。
- **下游消费者**：全部模块与审计系统。

## 11) ReviewIssue
- **用途**：人工审核问题单。
- **所属模块**：Acceptance Hub / Review Modules。
- **必须字段**：`issue_id`, `project_id`, `severity`, `description`, `source_ref`, `status`, `requires_review`。
- **可选字段**：`assignee`, `due_date`, `resolution`, `citation`。
- **不允许滥用字段**：`resolution`（禁止未复核即写“已解决”）。
- **下游消费者**：Acceptance Hub、业务引擎反馈回路。

## 12) QuantityItem
- **用途**：计量条目。
- **所属模块**：Quantity Takeoff Engine。
- **必须字段**：`quantity_item_id`, `component_id`, `measurement_type`, `value`, `unit`, `rule_id`, `confidence`, `status`。
- **可选字段**：`formula`, `source_ref`, `citation`, `requires_review`。
- **不允许滥用字段**：`value`（禁止混入未统一单位数据）。
- **下游消费者**：审计、报表、成本模块。

## 13) CalculationResult
- **用途**：计算结果汇总对象。
- **所属模块**：Quantity / Weida。
- **必须字段**：`result_id`, `project_id`, `result_type`, `inputs_ref`, `outputs`, `confidence`, `status`。
- **可选字段**：`warnings`, `requires_review`, `citation`。
- **不允许滥用字段**：`outputs`（禁止无 schema 的自由文本堆砌）。
- **下游消费者**：Review、Document Engine、Acceptance Hub。

## 14) QualityNote
- **用途**：质量验收与质量风险说明。
- **所属模块**：Quality Acceptance。
- **必须字段**：`note_id`, `project_id`, `category`, `description`, `citation`, `status`, `requires_review`。
- **可选字段**：`severity`, `suggestion`, `source_ref`, `attachments`。
- **不允许滥用字段**：`suggestion`（禁止输出超出资质边界的结论性意见）。
- **下游消费者**：Quality、Acceptance Hub、Document Engine。

---

## 统一字段重点约束
1. `source_ref`：必须可定位到原始证据（文件/页/区域/任务 ID）。
2. `citation`：必须可读、可回溯，禁止“无来源规则”。
3. `confidence`：AI 或规则推断必须给出数值置信度。
4. `requires_review`：低置信度、冲突规则、关键结论必须进入人工复核。
5. `status`：必须使用统一状态机，禁止自造语义冲突状态。
