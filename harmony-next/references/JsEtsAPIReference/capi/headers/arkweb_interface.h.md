# arkweb_interface.h

#### 概述

提供ArkWeb在Native侧获取API的接口，及基础Native API类型。

**引用文件：** <web/arkweb_interface.h>

**库：** libohweb.so

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**相关模块：**[Web](../../topics/networking/web.md)

#### 汇总

#### 结构体

名称typedef关键字描述[ArkWeb_AnyNativeAPI](../../topics/networking/ArkWeb_AnyNativeAPI.md)ArkWeb_AnyNativeAPI定义基础Native API类型。

#### 枚举

名称typedef关键字描述[ArkWeb_NativeAPIVariantKind](#ZH-CN_TOPIC_0000002497605222__arkweb_nativeapivariantkind)ArkWeb_NativeAPIVariantKind定义Native API的类型枚举。

#### 函数

名称描述[ArkWeb_AnyNativeAPI* OH_ArkWeb_GetNativeAPI(ArkWeb_NativeAPIVariantKind type)](#ZH-CN_TOPIC_0000002497605222__oh_arkweb_getnativeapi)根据传入的API类型，获取对应的Native API结构体。[bool OH_ArkWeb_RegisterScrollCallback(const char* webTag, ArkWeb_OnScrollCallback callback, void* userData)](#ZH-CN_TOPIC_0000002497605222__oh_arkweb_registerscrollcallback)注册滚动事件回调。

#### 枚举类型说明

#### ArkWeb_NativeAPIVariantKind

```ets
enum ArkWeb_NativeAPIVariantKind
```

**描述：**

定义Native API的类型枚举。

**起始版本：** 12

枚举项描述ARKWEB_NATIVE_COMPONENTcomponent相关API类型。ARKWEB_NATIVE_CONTROLLERcontroller相关API类型。ARKWEB_NATIVE_WEB_MESSAGE_PORTwebMessagePort相关API类型。ARKWEB_NATIVE_WEB_MESSAGEwebMessage相关API类型。ARKWEB_NATIVE_COOKIE_MANAGERcookieManager相关API类型。ARKWEB_NATIVE_JAVASCRIPT_VALUE

JavaScriptValue相关接口类型。

**起始版本：** 18

#### 函数说明

#### OH_ArkWeb_GetNativeAPI()

```ets
ArkWeb_AnyNativeAPI* OH_ArkWeb_GetNativeAPI(ArkWeb_NativeAPIVariantKind type)
```

**描述：**

根据传入的API类型，获取对应的Native API结构体。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

参数项描述[ArkWeb_NativeAPIVariantKind](#ZH-CN_TOPIC_0000002497605222__arkweb_nativeapivariantkind) typeArkWeb支持的Native API类型。

**返回：**

类型说明[ArkWeb_AnyNativeAPI](../../topics/networking/ArkWeb_AnyNativeAPI.md)*根据传入的API类型，返回对应的Native API结构体指针，结构体第一个成员为当前结构体的大小。

#### OH_ArkWeb_RegisterScrollCallback()

```ets
bool OH_ArkWeb_RegisterScrollCallback(const char* webTag, ArkWeb_OnScrollCallback callback, void* userData)
```

**描述**

设置组件滚动时的回调函数。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 18

**参数：**

参数项描述const char* webTagWeb组件的名称。[ArkWeb_OnScrollCallback](arkweb_type.h.md#ZH-CN_TOPIC_0000002529445189__arkweb_onscrollcallback) callback页面滚动时的回调函数。void* userData用户自定义的数据。

**返回：**

类型说明bool如果回调设置成功，则返回true，否则返回false。