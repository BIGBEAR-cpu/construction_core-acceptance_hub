# MODULE DEPENDENCY MAP（模块依赖图）v0.1

## 1. 主链路（数据生产链）
```text
Source Files (PDF/DXF/CAD/BIM)
    -> Drawing Ingestion
        -> Common Drawing Data
            -> Quantity Takeoff Engine
            -> Weida Plan Engine
            -> Detailing Engine
            -> Quality/Review Modules
```

## 2. 知识规则链
```text
Knowledge & Rule Center
    -> Quantity Rules
    -> Weida Rules
    -> Detailing Rules
    -> Quality Rules
```

## 3. 验收治理链
```text
All Subprojects
    -> Acceptance Hub
        -> Test Report / Review Report
        -> Stage Freeze (P0.1 / P1.1 / ...)
        -> Merge Decision
```

## 4. 强制依赖约束
1. 子项目只能依赖 Core Foundation 的公共契约，不得绕过。
2. 子项目不得私自定义与公共模型冲突的核心实体。
3. 知识库访问必须经 Knowledge & Rule Center，不得各自维护独立生产知识源。
4. 项目级特殊规则仅可作为 overlay 叠加，不得污染通用知识包。
5. 接口升级必须遵循版本化策略，且在 Acceptance Hub 通过后方可生效。

## 5. 推荐依赖方向
- `Core Foundation`：被依赖，不反向依赖业务引擎。
- `Knowledge & Rule Center`：被业务引擎读取，不直接调用业务引擎。
- `Business Engines`：消费 Common Drawing Data + Knowledge/Rules，输出业务结果。
- `Acceptance Hub`：横向治理所有模块，不承载业务算法。
