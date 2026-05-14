# SYSTEM BOUNDARY（系统边界）v0.1

## 1) Core Foundation
**负责：**
- 公共数据模型（Project、DrawingElement、Rule、ReviewIssue 等）
- API 契约与字段语义规范
- `source_ref`、`citation`、`confidence`、`requires_review`、`status` 的统一定义
- 验收标准、阶段冻结策略、跨项目验收入口

**不负责：**
- 真实 PDF/CAD/BIM 的解析实现
- 完整计量规则库与业务算法
- 危大专项方案生成业务实现

## 2) Knowledge & Rule Center
**负责：**
- 统一知识 schema、知识包与规则包
- 版本（version）与状态（status）治理
- 引用（citation）与来源追溯
- 按包发布、检索与审计支持

**不负责：**
- 直接执行业务生成（计量计算、方案编写、详图出图）

## 3) Drawing Ingestion
**负责：**
- PDF/DXF/CAD/BIM 到 Common Drawing Data 的解析转换
- 页面、图元、构件候选等结构化中间数据产出

**不负责：**
- 工程量计算
- 规范合规判断
- 危大专项方案生成

## 4) Quantity Takeoff Engine
**负责：**
- 工程量计算
- 规则匹配
- 定额推荐
- 审计导出

**不负责：**
- 原始图纸解析

## 5) Weida Plan Engine
**负责：**
- 危大/超危大判定
- 专项方案生成
- 计算辅助
- 合规检查
- Word 导出

**不负责：**
- 计量定额体系实现

## 6) Detailing Engine
**负责：**
- 构造节点建议
- 标准详图匹配
- 施工节点建议

**不负责：**
- 完整施工方案生成

## 7) Acceptance Hub
**负责：**
- 测试报告与审核报告
- 验收标准执行
- 阶段冻结（P0.1/P1.1 等）
- 合并决策（通过/拒绝/退回）

## 8) 边界原则
- 模块边界以“职责单一 + 契约清晰”为原则。
- 跨模块能力仅通过公共契约与版本化接口交互。
- 禁止以“临时脚本”绕过统一模型和验收流程。
