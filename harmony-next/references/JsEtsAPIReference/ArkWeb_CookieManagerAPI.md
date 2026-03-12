# ArkWeb_CookieManagerAPI

```ets
typedef struct {...} ArkWeb_CookieManagerAPI
```

#### 概述

定义了ArkWeb的CookieManager接口。在调用接口之前，建议使用[ARKWEB_MEMBER_MISSING](arkweb_type.h.md#ZH-CN_TOPIC_0000002529445189__宏定义)检查函数结构体是否有对应的函数指针，避免SDK与设备ROM不匹配导致崩溃。CookieManager相关接口需在UI线程中调用OH_ArkWeb_GetNativeAPI方法获取。

**起始版本：** 12

**相关模块：**[Web](Web.md)

**所在头文件：**[arkweb_type.h](arkweb_type.h.md)

#### 汇总

#### 成员变量

名称描述size_t size结构体的大小。

#### 成员函数

名称描述[ArkWeb_ErrorCode (*fetchCookieSync)(const char* url, bool incognito, bool includeHttpOnly, char** cookieValue)](#ZH-CN_TOPIC_0000002529445201__fetchcookiesync)获取指定URL对应的cookie值。[ArkWeb_ErrorCode (*configCookieSync)(const char* url,const char* cookieValue, bool incognito, bool includeHttpOnly)](#ZH-CN_TOPIC_0000002529445201__configcookiesync)设置指定URL的cookie值。[bool (*existCookies)(bool incognito)](#ZH-CN_TOPIC_0000002529445201__existcookies)检查Cookie是否存在。[void (*clearAllCookiesSync)(bool incognito)](#ZH-CN_TOPIC_0000002529445201__clearallcookiessync)清除所有cookies。[void (*clearSessionCookiesSync)()](#ZH-CN_TOPIC_0000002529445201__clearsessioncookiessync)清除所有会话Cookies。

#### 成员函数说明

#### fetchCookieSync()

```ets
ArkWeb_ErrorCode (*fetchCookieSync)(const char* url, bool incognito, bool includeHttpOnly, char** cookieValue)
```

**描述：**

获取指定URL对应的cookie值。

**参数：**

参数项描述const char* url要获取的cookie所属的URL，建议使用完整的URL。bool incognitotrue表示获取隐私模式下webview的内存cookie, false表示获取非隐私模式下的cookie。bool includeHttpOnly如果为true，则标记为HTTP-Only属性的cookie也将包含在cookieValue中。char** cookieValue获取与URL对应的cookie值。

**返回：**

类型说明[ArkWeb_ErrorCode](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode)

返回值错误码。

[ARKWEB_SUCCESS](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode) 获取cookie成功。

[ARKWEB_INVALID_URL](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode) 设置的URL无效。

[ARKWEB_INVALID_PARAM](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode) cookieValue参数无效。

#### configCookieSync()

```ets
ArkWeb_ErrorCode (*configCookieSync)(const char* url,const char* cookieValue, bool incognito, bool includeHttpOnly)
```

**描述：**

设置指定URL的cookie值。

**参数：**

参数项描述const char* url指定cookie所属的URL，建议填写完整的URL。const char* cookieValue要设置的cookie的值。bool incognitotrue表示在隐私模式下设置对应URL的Cookie，false表示以非隐私模式设置对应URL的cookie。bool includeHttpOnly如果为true，则标记为HTTP-Only的cookie也可以被覆盖。

**返回：**

类型说明[ArkWeb_ErrorCode](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode)

返回值错误码。

[ARKWEB_SUCCESS](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode) 获取cookie成功。

[ARKWEB_INVALID_URL](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode) 设置的URL无效。

[ARKWEB_INVALID_PARAM](arkweb_error_code.h.md#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode) cookieValue参数无效。

#### existCookies()

```ets
bool (*existCookies)(bool incognito)
```

**描述：**

检查Cookie是否存在。

**参数：**

参数项描述bool incognitotrue表示隐私模式下是否存在cookie，false表示非隐私模式下是否存在cookie。

**返回：**

类型说明booltrue表示cookie存在，false表示cookie不存在。

#### clearAllCookiesSync()

```ets
void (*clearAllCookiesSync)(bool incognito)
```

**描述：**

清除所有cookies。

**参数：**

参数项描述bool incognitotrue表示清除隐私模式下的所有cookies，false表示清除非隐私模式下的所有cookies。

#### clearSessionCookiesSync()

```ets
void (*clearSessionCookiesSync)()
```

**描述：**

清除所有会话Cookies。