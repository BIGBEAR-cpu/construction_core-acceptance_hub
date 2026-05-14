# P0 Acceptance（Core Foundation P0.1）

## 验收原则
- 必须记录真实执行命令与真实输出结论。
- **不允许伪造 PASS**。
- 依赖安装或外部环境问题导致无法完成时，统一标记为 `BLOCKED`。

## 真实验收命令
```bash
pip install -r requirements.txt
python -m pytest -q
python scripts/check_all.py
uvicorn backend.api.main:app --reload
```

## 最近一次执行记录（2026-05-14）

### 1) `pip install -r requirements.txt`
- 结果：`BLOCKED`
- 原因：当前环境访问包索引失败（`Tunnel connection failed: 403 Forbidden`），导致 `fastapi==0.115.0` 等依赖无法下载。

### 2) `python -m pytest -q`
- 结果：失败（非测试断言失败，属于依赖缺失）
- 通过数量：0
- 失败原因：`ModuleNotFoundError: No module named 'fastapi'` / `No module named 'pydantic'`。

### 3) `python scripts/check_all.py`
- 结果：失败
- 失败原因：在 `import backend.api.main:app` 阶段因缺少 `fastapi` 失败。

### 4) `uvicorn backend.api.main:app --reload`
- 结果：`BLOCKED`
- 原因：依赖未安装完成，服务无法启动。

## 通过标准（供后续复验）
- `pip install -r requirements.txt` 成功完成。
- `python -m pytest -q` 正常执行并输出通过用例数量。
- `python scripts/check_all.py` 返回码为 0。
- `uvicorn backend.api.main:app --reload` 正常启动并可访问健康检查接口。
