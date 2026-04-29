# arkweb_interface.h

**概述**

提供ArkWeb在Native侧获取API的接口，及基础Native API类型。

引用文件： <web/arkweb_interface.h>

库： libohweb.so

系统能力： SystemCapability.Web.Webview.Core

起始版本： 12

相关模块： [Web](Web.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkWeb_AnyNativeAPI | ArkWeb_AnyNativeAPI | 定义基础Native API类型。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkWeb_NativeAPIVariantKind | ArkWeb_NativeAPIVariantKind | 定义Native API的类型枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| ArkWeb_AnyNativeAPI* OH_ArkWeb_GetNativeAPI(ArkWeb_NativeAPIVariantKind type) | 根据传入的API类型，获取对应的Native API结构体。 |
| bool OH_ArkWeb_RegisterScrollCallback(const char* webTag, ArkWeb_OnScrollCallback callback, void* userData) | 注册滚动事件回调。 |

**枚举类型说明**

**ArkWeb_NativeAPIVariantKind**

```ets
enum ArkWeb_NativeAPIVariantKind
```

描述：

定义Native API的类型枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| ARKWEB_NATIVE_COMPONENT | component相关API类型。 |
| ARKWEB_NATIVE_CONTROLLER | controller相关API类型。 |
| ARKWEB_NATIVE_WEB_MESSAGE_PORT | webMessagePort相关API类型。 |
| ARKWEB_NATIVE_WEB_MESSAGE | webMessage相关API类型。 |
| ARKWEB_NATIVE_COOKIE_MANAGER | cookieManager相关API类型。 |
| ARKWEB_NATIVE_JAVASCRIPT_VALUE | JavaScriptValue相关接口类型。 起始版本： 18 |

**函数说明**

**OH_ArkWeb_GetNativeAPI()**

```ets
ArkWeb_AnyNativeAPI* OH_ArkWeb_GetNativeAPI(ArkWeb_NativeAPIVariantKind type)
```

描述：

根据传入的API类型，获取对应的Native API结构体。

系统能力： SystemCapability.Web.Webview.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkWeb_NativeAPIVariantKind type | ArkWeb支持的Native API类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkWeb_AnyNativeAPI* | 根据传入的API类型，返回对应的Native API结构体指针，结构体第一个成员为当前结构体的大小。 |

**OH_ArkWeb_RegisterScrollCallback()**

```ets
bool OH_ArkWeb_RegisterScrollCallback(const char* webTag, ArkWeb_OnScrollCallback callback, void* userData)
```

描述

设置组件滚动时的回调函数。

系统能力： SystemCapability.Web.Webview.Core

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* webTag | Web组件的名称。 |
| ArkWeb_OnScrollCallback callback | 页面滚动时的回调函数。 |
| void* userData | 用户自定义的数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 如果回调设置成功，则返回true，否则返回false。 |