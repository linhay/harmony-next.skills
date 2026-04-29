# ArkUI_AttributeItem

```ets
typedef struct {...} ArkUI_AttributeItem
```

**概述**

定义[setAttribute](ArkUI_NativeNodeAPI_1.md#ZH-CN_TOPIC_0000002522081074__setattribute)函数通用入参结构。各个属性设置接口可选择使用其中的成员变量来存储特定类型的参数数据。

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_node.h](native_node.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| const ArkUI_NumberValue* value | 数字类型数组，用于存储数字数组类型的参数。 |
| int32_t size | 数字类型数组大小，配合变量value使用，value数组的长度。 |
| const char* string | 字符串类型，用于存储字符串类型的参数。 |
| void* object | 对象类型，用于存储对象类型的参数。 |