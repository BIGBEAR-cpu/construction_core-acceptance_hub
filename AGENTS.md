# AGENTS

## 项目定位
AI Construction Detailing Engine 是施工端 AI 工程生产系统。

## 当前项目范围
- midasW
- 超危大工程文档自动输出
- AI 自动计量

## 后续公共模块规划
- construction_core
- acceptance_hub
- evidence_chain
- review_engine

## 核心规则
1. 禁止编造规范条文、公式、定额、真实工程数据。
2. 所有关键输出必须保留 `SourceCitation` 或 `EvidenceLink`。
3. 计算逻辑必须程序化实现，不能由 LLM 编造计算结果。
4. 图纸输出必须有校验器和 golden sample。
5. 工程量结果必须包含：规则依据、表达式、单位和 `need_review` 状态。
6. 文档输出必须包含：来源、计算、质量、合规附录。
7. 所有改动必须配套测试。
8. 禁止大规模重构已有项目，除非任务明确要求。
9. 优先小步提交、小步 PR。

## 协作分工
- 本地 Trae/GLM：负责代码实现。
- DeepSeek：负责审核。
- GPT 网页：负责总裁判。
- Codex Web：负责关键 PR 和复杂重构。

## 安全与数据要求
- 不要上传真实工程资料、密钥、大型 CAD/BIM 文件。

## 交付要求
- 每个任务完成后必须输出开发报告。
