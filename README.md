# AI Construction Detailing Engine (P0 Core Foundation)

## 项目目标
将 PDF / CAD / DXF / BIM 工程图纸转化为统一公共数据结构，并作为工程量计算、规则审核、施工详图生成、AI 解释的上游输入。

## 当前 P0 范围
- 建立 FastAPI 最小可运行后端。
- 建立核心模型与公共图纸数据模型。
- 建立示例规则库、服务层、示例数据、测试。
- 仅支持 mock 解析与基础规范化。

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
pytest
```

## 当前明确不支持
- 真实 DWG/RVT/IFC/PDF 解析。
- 复杂 AI 推理和专业级算量。
- 完整规范审图与全量定额库。

## 数据流
PDF / CAD / BIM Source → Drawing Ingestion → Common Drawing Data → Quantity / Review / Detailing
