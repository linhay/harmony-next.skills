# ArkWeb_JavaScriptObject

```ets
typedef struct {...} ArkWeb_JavaScriptObject
```

**概述**

注入的JavaScript结构体。

起始版本： 12

相关模块： [Web](Web.md)

所在头文件： [arkweb_type.h](arkweb_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| const uint8_t* buffer | 注入的JavaScript代码。 |
| size_t size | JavaScript代码长度。 |
| ArkWeb_OnJavaScriptCallback callback | JavaScript执行完成的回调。 |
| void* userData | 需要在回调中携带的自定义数据。 |