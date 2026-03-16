# arkweb_type.h

#### 概述

提供ArkWeb在Native侧的公共类型定义。

**引用文件：** <web/arkweb_type.h>

**库：** libohweb.so

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**相关模块：**[Web](../../topics/networking/web.md)

#### 汇总

#### 结构体

名称typedef关键字描述[ArkWeb_JavaScriptBridgeData](../../topics/networking/ArkWeb_JavaScriptBridgeData.md)ArkWeb_JavaScriptBridgeData定义JavaScript Bridge数据的基础结构。[ArkWeb_WebMessage*](../../topics/networking/ArkWeb_WebMessage_.md)ArkWeb_WebMessagePtrPost Message数据结构体指针。[ArkWeb_JavaScriptValue*](../../topics/networking/ArkWeb_JavaScriptValue_.md)ArkWeb_JavaScriptValuePtrJavaScript数据结构体指针。[ArkWeb_WebMessagePort*](../../topics/networking/ArkWeb_WebMessagePort_.md)ArkWeb_WebMessagePortPtrPost Message端口结构体指针。[ArkWeb_JavaScriptObject](../../topics/networking/ArkWeb_JavaScriptObject.md)ArkWeb_JavaScriptObject注入的JavaScript结构体。[ArkWeb_ProxyMethod](../../topics/networking/ArkWeb_ProxyMethod.md)ArkWeb_ProxyMethod注入的Proxy方法通用结构体。[ArkWeb_ProxyMethodWithResult](../../topics/networking/ArkWeb_ProxyMethodWithResult.md)ArkWeb_ProxyMethodWithResult注入的Proxy方法通用结构体。[ArkWeb_ProxyObject](../../topics/networking/ArkWeb_ProxyObject.md)ArkWeb_ProxyObject注入的Proxy对象通用结构体。[ArkWeb_ProxyObjectWithResult](../../topics/networking/ArkWeb_ProxyObjectWithResult.md)ArkWeb_ProxyObjectWithResult注入的Proxy对象通用结构体。[ArkWeb_ControllerAPI](../../topics/networking/ArkWeb_ControllerAPI.md)ArkWeb_ControllerAPIController相关的Native API结构体。在调用接口前建议通过ARKWEB_MEMBER_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。Controller相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。[ArkWeb_ComponentAPI](../../topics/components/ArkWeb_ComponentAPI.md)ArkWeb_ComponentAPIComponent相关的Native API结构体。[ArkWeb_WebMessagePortAPI](../../topics/networking/ArkWeb_WebMessagePortAPI.md)ArkWeb_WebMessagePortAPIPost Message相关的Native API结构体。在调用接口前建议通过ARKWEB_MEMBER_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。WebMessagePort相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。[ArkWeb_WebMessageAPI](../../topics/networking/ArkWeb_WebMessageAPI.md)ArkWeb_WebMessageAPIPost Message数据相关的Native API结构体。在调用接口前建议通过ARKWEB_MEMBER_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。WebMessage相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。[ArkWeb_CookieManagerAPI](../../topics/networking/ArkWeb_CookieManagerAPI.md)ArkWeb_CookieManagerAPI定义了ArkWeb的CookieManager接口。在调用接口之前，建议使用ARKWEB_MEMBER_MISSING检查函数结构体是否有对应的函数指针，避免SDK与设备ROM不匹配导致崩溃。CookieManager相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。[ArkWeb_JavaScriptValueAPI](../../topics/networking/ArkWeb_JavaScriptValueAPI.md)ArkWeb_JavaScriptValueAPI定义了ArkWeb的JavaScriptValue接口。在调用接口之前，建议使用ARKWEB_MEMBER_MISSING检查函数结构体是否有对应的函数指针，避免SDK与设备ROM不匹配导致崩溃。

#### 枚举

名称typedef关键字描述[ArkWeb_WebMessageType](#ZH-CN_TOPIC_0000002529445189__arkweb_webmessagetype)ArkWeb_WebMessageTypePost Message数据类型。[ArkWeb_JavaScriptValueType](#ZH-CN_TOPIC_0000002529445189__arkweb_javascriptvaluetype)ArkWeb_JavaScriptValueTypeJavaScript数据类型。

#### 函数

名称typedef关键字描述[typedef void (*ArkWeb_OnJavaScriptCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* data, void* userData)](#ZH-CN_TOPIC_0000002529445189__arkweb_onjavascriptcallback)ArkWeb_OnJavaScriptCallback注入的JavaScript执行完成的回调。[typedef void (*ArkWeb_OnJavaScriptProxyCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)](#ZH-CN_TOPIC_0000002529445189__arkweb_onjavascriptproxycallback)ArkWeb_OnJavaScriptProxyCallbackProxy方法被执行的回调。[typedef ArkWeb_JavaScriptValuePtr (*ArkWeb_OnJavaScriptProxyCallbackWithResult)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)](#ZH-CN_TOPIC_0000002529445189__arkweb_onjavascriptproxycallbackwithresult)ArkWeb_OnJavaScriptProxyCallbackWithResultProxy方法被执行的回调。[typedef void (*ArkWeb_OnComponentCallback)(const char* webTag, void* userData)](#ZH-CN_TOPIC_0000002529445189__arkweb_oncomponentcallback)ArkWeb_OnComponentCallback组件事件通知相关的通用回调。[typedef void (*ArkWeb_OnScrollCallback)(const char* webTag, void* userData, double x, double y)](#ZH-CN_TOPIC_0000002529445189__arkweb_onscrollcallback)ArkWeb_OnScrollCallback定义Web组件滚动时的回调函数的类型。[typedef void (*ArkWeb_OnMessageEventHandler)(const char* webTag, const ArkWeb_WebMessagePortPtr port, const ArkWeb_WebMessagePtr message, void* userData)](#ZH-CN_TOPIC_0000002529445189__arkweb_onmessageeventhandler)ArkWeb_OnMessageEventHandler处理HTML发送过来的Post Message数据。

#### 宏定义

名称描述ARKWEB_MEMBER_EXISTS(s, f) ((intptr_t) & ((s)->f) - (intptr_t)(s) + sizeof((s)->f) <= *reinterpret_cast<size_t*>(s))

检查结构体中是否存在该成员变量。

**起始版本：** 12

ARKWEB_MEMBER_MISSING(s, f) (!ARKWEB_MEMBER_EXISTS(s, f) || !((s)->f))

当前结构体存在该成员变量则返回false，否则返回true

**起始版本：** 12

#### 枚举类型说明

#### ArkWeb_WebMessageType

```ets
enum ArkWeb_WebMessageType
```

**描述**

Post Message数据类型。

**起始版本：** 12

枚举项描述ARKWEB_NONE = 0错误数据。ARKWEB_STRING字符串数据类型。ARKWEB_BUFFER字节流数据类型。

#### ArkWeb_JavaScriptValueType

```ets
enum ArkWeb_JavaScriptValueType
```

**描述**

JavaScript数据类型。

**起始版本：** 18

枚举项描述ARKWEB_JAVASCRIPT_NONE = 0错误数据。ARKWEB_JAVASCRIPT_STRING字符串数据类型。ARKWEB_JAVASCRIPT_BOOLbool数据类型。

#### 函数说明

#### ArkWeb_OnJavaScriptCallback()

```ets
typedef void (*ArkWeb_OnJavaScriptCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* data, void* userData)
```

**描述**

注入的JavaScript执行完成的回调。

**起始版本：** 12

**参数：**

参数项描述const char* webTagWeb组件名称。const [ArkWeb_JavaScriptBridgeData](../../topics/networking/ArkWeb_JavaScriptBridgeData.md)* dataJavaScriptBridge数据。void* userData用户自定义的数据。

#### ArkWeb_OnJavaScriptProxyCallback()

```ets
typedef void (*ArkWeb_OnJavaScriptProxyCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)
```

**描述**

Proxy方法被执行的回调。

**起始版本：** 12

**参数：**

参数项描述const char* webTagWeb组件名称。const [ArkWeb_JavaScriptBridgeData](../../topics/networking/ArkWeb_JavaScriptBridgeData.md)* dataArray数组数据。size_t arraySize数组大小。void* userData用户自定义的数据。

#### ArkWeb_OnJavaScriptProxyCallbackWithResult()

```ets
typedef ArkWeb_JavaScriptValuePtr (*ArkWeb_OnJavaScriptProxyCallbackWithResult)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)
```

**描述**

Proxy方法被执行的回调。

**起始版本：** 18

**参数：**

参数项描述const char* webTagWeb组件名称。const [ArkWeb_JavaScriptBridgeData](../../topics/networking/ArkWeb_JavaScriptBridgeData.md)* dataArray数组数据。size_t arraySize数组大小。void* userData用户自定义的数据。

#### ArkWeb_OnComponentCallback()

```ets
typedef void (*ArkWeb_OnComponentCallback)(const char* webTag, void* userData)
```

**描述**

组件事件通知相关的通用回调。

**起始版本：** 12

**参数：**

参数项描述const char* webTagWeb组件名称。void* userData用户自定义的数据。

#### ArkWeb_OnScrollCallback()

```ets
typedef void (*ArkWeb_OnScrollCallback)(const char* webTag, void* userData, double x, double y)
```

**描述**

定义Web组件滚动时的回调函数的类型。

**起始版本：** 18

**参数：**

参数项描述const char* webTagWeb组件名称。void* userData用户自定义的数据。double xX轴滚动偏移。double yY轴滚动偏移。

#### ArkWeb_OnMessageEventHandler()

```ets
typedef void (*ArkWeb_OnMessageEventHandler)(const char* webTag, const ArkWeb_WebMessagePortPtr port, const ArkWeb_WebMessagePtr message, void* userData)
```

**描述**

处理HTML发送过来的Post Message数据。

**起始版本：** 12

**参数：**

参数项描述const char* webTagWeb组件名称。const [ArkWeb_WebMessagePortPtr](../../topics/networking/ArkWeb_WebMessagePort_.md) portPost Message端口。const [ArkWeb_WebMessagePtr](../../topics/networking/ArkWeb_WebMessage_.md) messagePost Message数据。void* userData用户自定义数据。