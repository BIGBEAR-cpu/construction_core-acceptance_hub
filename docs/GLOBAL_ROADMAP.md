# GLOBAL ROADMAP（全局路线图）v0.1

## P0：架构与底座奠基
- Core Foundation 搭建
- 公共数据模型基线
- mock drawing parse（明确为 mock）
- 示例规则与示例知识项
- 基础 API 契约
- 文档与测试骨架

## P0.1：工程化与冻结门槛（必须达成）
- 依赖安装可复现
- `pytest` 全量通过
- CI 流水线可运行
- `check_all` 通过
- 验收冻结（Acceptance Freeze）

## P1：首批真实能力接入
- DXF Basic Reader
- Knowledge Center P0
- 第一个真实业务包接入（建议先 Quantity 或 Weida）

## P1.1：跨模块一致性冻结（必须达成）
- DXF Reader 验收冻结
- Knowledge Center 验收冻结
- 计量 / 危大项目完成公共知识与公共数据适配

## P2：增强解析与审核能力
- PDF 解析能力接入
- 规则 DSL
- 人工审核工作台
- 更多知识包扩展
- 审核版导出门槛（未达门槛禁止生产导出）

## P3：企业级协同与治理
- 多项目协同
- 生产级权限体系
- 版本化知识发布机制
- 项目级知识 overlay 管理
- 企业级部署与运维策略

## 路线执行原则
- 每一阶段结束前必须通过 Acceptance Hub 冻结。
- 任何“看起来可用”的能力未达冻结门槛不得宣称完成。
- 文档状态、测试状态、代码状态必须一致。
