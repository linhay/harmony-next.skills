# NDK 开发与 Node-API 指南

HarmonyOS NDK 基于 Node-API (napi) 提供 C++/ArkTS 跨语言交互能力。

## 1. 核心概念
*   **napi_env**：JS 引擎实例上下文。
*   **napi_value**：JS 对象在 C++ 侧的抽象表示。
*   **HandleScope**：管理 `napi_value` 生命周期，防止泄露。

## 2. ArkTS 与 C++ 互调流程

### C++ 侧实现
1.  **定义逻辑**：编写函数，使用 `napi_get_cb_info` 解析参数。
2.  **模块注册**：
    *   定义 `napi_module`。
    *   在 `Init` 中使用 `napi_define_properties` 导出接口。
    *   使用 `napi_module_register` 注册模块。

### 工程配置
*   **CMakeLists.txt**：
    *   使用 `add_library` 定义 SO。
    *   `target_link_libraries` 链接 `libace_napi.z.so`。
*   **build-profile.json5**：在 `externalNativeBuild` 中关联 CMake 路径。

### ArkTS 侧调用
```typescript
import nativeModule from 'libentry.so';
nativeModule.add(1, 2);
```

## 3. 常用接口参考
*   `napi_create_function`：创建 JS 函数。
*   `napi_get_cb_info`：获取 ArkTS 传入参数。
*   `napi_create_double` / `napi_create_string_utf8`：创建 JS 基础类型。
*   `napi_wrap`：将 C++ 对象绑定到 JS 对象。
