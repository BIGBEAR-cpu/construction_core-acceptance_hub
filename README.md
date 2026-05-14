# Construction Core Foundation + Acceptance Hub

## 仓库定位
当前仓库为 **Core Foundation + Acceptance Hub** 代码仓库，用于沉淀可运行、可测试、可冻结的基础实现。

> 总控架构内容（历史 PR #1 / #3 / #4）已拆分至独立仓库，本仓库不再合入对应内容。

## P0.1 冻结目标
- 保持 FastAPI 后端最小可运行能力。
- 保持核心数据模型、示例规则、示例请求、基础测试可执行。
- 通过统一验收脚本执行环境检查与测试。

## 当前支持能力
- FastAPI 应用启动与健康检查。
- mock parse / normalize 数据流。
- 基于 `knowledge_base/rules` 的示例规则读取。
- 基础算量与审查服务接口联调（示例级）。

## 明确不支持
- 真实 PDF / DWG / RVT / IFC 解析。
- 生产级算量、审图、施工详图自动生成。
- 大规模规则库扩展与企业级知识中心能力。

## 安装依赖
```bash
pip install -r requirements.txt
```

## 启动服务
```bash
uvicorn backend.api.main:app --reload
```

## 运行测试
```bash
python -m pytest -q
```

## 一键检查
```bash
python scripts/check_all.py
```
