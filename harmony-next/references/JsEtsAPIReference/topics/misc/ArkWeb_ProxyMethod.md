# ArkWeb_ProxyMethod

```ets
typedef struct {...} ArkWeb_ProxyMethod
```

**概述**

注入的Proxy方法通用结构体。

起始版本： 12

相关模块： [Web](Web.md)

所在头文件： [arkweb_type.h](arkweb_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| const char* methodName | 注入的方法名。 |
| ArkWeb_OnJavaScriptProxyCallback callback | Proxy方法执行的回调。 |
| void* userData | 需要在回调中携带的自定义数据。 |