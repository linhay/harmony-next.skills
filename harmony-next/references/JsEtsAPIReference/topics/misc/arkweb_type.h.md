# arkweb_type.h

**概述**

提供ArkWeb在Native侧的公共类型定义。

引用文件： <web/arkweb_type.h>

库： libohweb.so

系统能力： SystemCapability.Web.Webview.Core

起始版本： 12

相关模块： [Web](Web.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkWeb_JavaScriptBridgeData | ArkWeb_JavaScriptBridgeData | 定义JavaScript Bridge数据的基础结构。 |
| ArkWeb_WebMessage* | ArkWeb_WebMessagePtr | Post Message数据结构体指针。 |
| ArkWeb_JavaScriptValue* | ArkWeb_JavaScriptValuePtr | JavaScript数据结构体指针。 |
| ArkWeb_WebMessagePort* | ArkWeb_WebMessagePortPtr | Post Message端口结构体指针。 |
| ArkWeb_JavaScriptObject | ArkWeb_JavaScriptObject | 注入的JavaScript结构体。 |
| ArkWeb_ProxyMethod | ArkWeb_ProxyMethod | 注入的Proxy方法通用结构体。 |
| ArkWeb_ProxyMethodWithResult | ArkWeb_ProxyMethodWithResult | 注入的Proxy方法通用结构体。 |
| ArkWeb_ProxyObject | ArkWeb_ProxyObject | 注入的Proxy对象通用结构体。 |
| ArkWeb_ProxyObjectWithResult | ArkWeb_ProxyObjectWithResult | 注入的Proxy对象通用结构体。 |
| ArkWeb_ControllerAPI | ArkWeb_ControllerAPI | Controller相关的Native API结构体。在调用接口前建议通过ARKWEB_MEMBER_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。Controller相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。 |
| ArkWeb_ComponentAPI | ArkWeb_ComponentAPI | Component相关的Native API结构体。 |
| ArkWeb_WebMessagePortAPI | ArkWeb_WebMessagePortAPI | Post Message相关的Native API结构体。在调用接口前建议通过ARKWEB_MEMBER_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。WebMessagePort相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。 |
| ArkWeb_WebMessageAPI | ArkWeb_WebMessageAPI | Post Message数据相关的Native API结构体。在调用接口前建议通过ARKWEB_MEMBER_MISSING校验该函数结构体是否有对应函数指针，避免SDK与设备ROM不匹配导致crash问题。WebMessage相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。 |
| ArkWeb_CookieManagerAPI | ArkWeb_CookieManagerAPI | 定义了ArkWeb的CookieManager接口。在调用接口之前，建议使用ARKWEB_MEMBER_MISSING检查函数结构体是否有对应的函数指针，避免SDK与设备ROM不匹配导致崩溃。CookieManager相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。 |
| ArkWeb_JavaScriptValueAPI | ArkWeb_JavaScriptValueAPI | 定义了ArkWeb的JavaScriptValue接口。在调用接口之前，建议使用ARKWEB_MEMBER_MISSING检查函数结构体是否有对应的函数指针，避免SDK与设备ROM不匹配导致崩溃。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkWeb_WebMessageType | ArkWeb_WebMessageType | Post Message数据类型。 |
| ArkWeb_JavaScriptValueType | ArkWeb_JavaScriptValueType | JavaScript数据类型。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*ArkWeb_OnJavaScriptCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* data, void* userData) | ArkWeb_OnJavaScriptCallback | 注入的JavaScript执行完成的回调。 |
| typedef void (*ArkWeb_OnJavaScriptProxyCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData) | ArkWeb_OnJavaScriptProxyCallback | Proxy方法被执行的回调。 |
| typedef ArkWeb_JavaScriptValuePtr (*ArkWeb_OnJavaScriptProxyCallbackWithResult)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData) | ArkWeb_OnJavaScriptProxyCallbackWithResult | Proxy方法被执行的回调。 |
| typedef void (*ArkWeb_OnComponentCallback)(const char* webTag, void* userData) | ArkWeb_OnComponentCallback | 组件事件通知相关的通用回调。 |
| typedef void (*ArkWeb_OnScrollCallback)(const char* webTag, void* userData, double x, double y) | ArkWeb_OnScrollCallback | 定义Web组件滚动时的回调函数的类型。 |
| typedef void (*ArkWeb_OnMessageEventHandler)(const char* webTag, const ArkWeb_WebMessagePortPtr port, const ArkWeb_WebMessagePtr message, void* userData) | ArkWeb_OnMessageEventHandler | 处理HTML发送过来的Post Message数据。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| ARKWEB_MEMBER_EXISTS(s, f) ((intptr_t) & ((s)->f) - (intptr_t)(s) + sizeof((s)->f) <= *reinterpret_cast<size_t*>(s)) | 检查结构体中是否存在该成员变量。 起始版本： 12 |
| ARKWEB_MEMBER_MISSING(s, f) (!ARKWEB_MEMBER_EXISTS(s, f) || !((s)->f)) | 当前结构体存在该成员变量则返回false，否则返回true 起始版本： 12 |

**枚举类型说明**

**ArkWeb_WebMessageType**

```ets
enum ArkWeb_WebMessageType
```

描述

Post Message数据类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKWEB_NONE = 0 | 错误数据。 |
| ARKWEB_STRING | 字符串数据类型。 |
| ARKWEB_BUFFER | 字节流数据类型。 |

**ArkWeb_JavaScriptValueType**

```ets
enum ArkWeb_JavaScriptValueType
```

描述

JavaScript数据类型。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| ARKWEB_JAVASCRIPT_NONE = 0 | 错误数据。 |
| ARKWEB_JAVASCRIPT_STRING | 字符串数据类型。 |
| ARKWEB_JAVASCRIPT_BOOL | bool数据类型。 |

**函数说明**

**ArkWeb_OnJavaScriptCallback()**

```ets
typedef void (*ArkWeb_OnJavaScriptCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* data, void* userData)
```

描述

注入的JavaScript执行完成的回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件名称。 |
| const ArkWeb_JavaScriptBridgeData* data | JavaScriptBridge数据。 |
| void* userData | 用户自定义的数据。 |

**ArkWeb_OnJavaScriptProxyCallback()**

```ets
typedef void (*ArkWeb_OnJavaScriptProxyCallback)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)
```

描述

Proxy方法被执行的回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件名称。 |
| const ArkWeb_JavaScriptBridgeData* dataArray | 数组数据。 |
| size_t arraySize | 数组大小。 |
| void* userData | 用户自定义的数据。 |

**ArkWeb_OnJavaScriptProxyCallbackWithResult()**

```ets
typedef ArkWeb_JavaScriptValuePtr (*ArkWeb_OnJavaScriptProxyCallbackWithResult)(const char* webTag, const ArkWeb_JavaScriptBridgeData* dataArray, size_t arraySize, void* userData)
```

描述

Proxy方法被执行的回调。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件名称。 |
| const ArkWeb_JavaScriptBridgeData* dataArray | 数组数据。 |
| size_t arraySize | 数组大小。 |
| void* userData | 用户自定义的数据。 |

**ArkWeb_OnComponentCallback()**

```ets
typedef void (*ArkWeb_OnComponentCallback)(const char* webTag, void* userData)
```

描述

组件事件通知相关的通用回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件名称。 |
| void* userData | 用户自定义的数据。 |

**ArkWeb_OnScrollCallback()**

```ets
typedef void (*ArkWeb_OnScrollCallback)(const char* webTag, void* userData, double x, double y)
```

描述

定义Web组件滚动时的回调函数的类型。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件名称。 |
| void* userData | 用户自定义的数据。 |
| double x | X轴滚动偏移。 |
| double y | Y轴滚动偏移。 |

**ArkWeb_OnMessageEventHandler()**

```ets
typedef void (*ArkWeb_OnMessageEventHandler)(const char* webTag, const ArkWeb_WebMessagePortPtr port, const ArkWeb_WebMessagePtr message, void* userData)
```

描述

处理HTML发送过来的Post Message数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件名称。 |
| const ArkWeb_WebMessagePortPtr port | Post Message端口。 |
| const ArkWeb_WebMessagePtr message | Post Message数据。 |
| void* userData | 用户自定义数据。 |