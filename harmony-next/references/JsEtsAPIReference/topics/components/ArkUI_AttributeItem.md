# ArkUI_AttributeItem

```ets
typedef struct {...} ArkUI_AttributeItem
```

#### 概述

定义[setAttribute](ArkUI_NativeNodeAPI_1.md#ZH-CN_TOPIC_0000002497605120__setattribute)函数通用入参结构。

**起始版本：** 12

**相关模块：**[ArkUI_NativeModule](../system-services/ArkUI_NativeModule.md)

**所在头文件：**[native_node.h](../../capi/headers/native_node.h.md)

#### 汇总

#### 成员变量

名称描述const [ArkUI_NumberValue](../media/ArkUI_NumberValue.md)* value数字类型数组。int32_t size数字类型数组大小。const char* string字符串类型。void* object对象类型。