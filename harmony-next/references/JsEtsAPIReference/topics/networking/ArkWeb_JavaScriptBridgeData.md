# ArkWeb_JavaScriptBridgeData

```ets
typedef struct {...} ArkWeb_JavaScriptBridgeData
```

#### 概述

定义JavaScript Bridge数据的基础结构。

**起始版本：** 12

**相关模块：**[Web](web.md)

**所在头文件：**[arkweb_type.h](../../capi/headers/arkweb_type.h.md)

#### 汇总

#### 成员变量

名称描述const uint8_t* buffer指向传输数据的指针。仅支持前端传入String和ArrayBuffer类型，其余类型会被json序列化后，以String类型传递。size_t size传输数据的长度。