# ArkWeb_ProxyMethodWithResult

```ets
typedef struct {...} ArkWeb_ProxyMethodWithResult
```

#### 概述

注入的Proxy方法通用结构体。

**起始版本：** 18

**相关模块：**[Web](web.md)

**所在头文件：**[arkweb_type.h](../../capi/headers/arkweb_type.h.md)

#### 汇总

#### 成员变量

名称描述const char* methodName注入的方法名。[ArkWeb_OnJavaScriptProxyCallbackWithResult](../../capi/headers/arkweb_type.h.md#ZH-CN_TOPIC_0000002529445189__arkweb_onjavascriptproxycallbackwithresult) callbackProxy方法执行的回调。void* userData需要在回调中携带的自定义数据。