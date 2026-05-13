# Common Drawing Data

统一结构由 `ParsedDrawingResult` 表达。

关键字段：
- `drawing_file.source_type`: 预留 `PDF/DXF/DWG/IFC/RVT`。
- `pages[]`: 页面级容器。
- `elements[]`: 通用图元（墙线/门窗等）。
- `text_annotations[]`、`dimension_annotations[]`、`grid_lines[]`。
- `component_candidates[]`: 构件候选。
- `source_ref`: 来源追溯（文件、页码、图层、原始对象 ID）。
- `confidence`: 识别置信度（0~1）。
- `geometry.geometry_type`: `point/line/polyline/polygon/circle/arc/bbox`。
