# arkweb_error_code.h

#### 概述

声明ArkWeb NDK接口异常错误码。

**引用文件：** <web/arkweb_error_code.h>

**库：** libohweb.so

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**相关模块：**[Web](Web.md)

#### 汇总

#### 枚举

名称typedef关键字描述[ArkWeb_ErrorCode](#ZH-CN_TOPIC_0000002529445187__arkweb_errorcode)ArkWeb_ErrorCode定义ArkWeb NDK接口异常错误码。[ArkWeb_BlanklessErrorCode](#ZH-CN_TOPIC_0000002529445187__arkweb_blanklesserrorcode)ArkWeb_BlanklessErrorCode定义无白屏加载的异常错误码。

#### 枚举类型说明

#### ArkWeb_ErrorCode

```ets
enum ArkWeb_ErrorCode
```

**描述：**

定义ArkWeb NDK接口异常错误码。

**起始版本：** 12

枚举项描述ARKWEB_SUCCESS = 0成功。ARKWEB_INIT_ERROR = 17100001初始化失败。ARKWEB_ERROR_UNKNOWN = 17100100未知错误。ARKWEB_INVALID_PARAM = 17100101参数无效。ARKWEB_SCHEME_REGISTER_FAILED = 17100102注册scheme的配置失败，应该在创建ArkWeb之前注册。ARKWEB_INVALID_URL = 17100103无效的URL。ARKWEB_INVALID_COOKIE_VALUE = 17100104无效的cookie值。ARKWEB_LIBRARY_OPEN_FAILURE = 17100105

打开动态链接库失败。

**起始版本：** 15

ARKWEB_LIBRARY_SYMBOL_NOT_FOUND = 17100106

动态链接库中找不到所需的符号。

**起始版本：** 15

ARKWEB_COOKIE_MANAGER_NOT_INITIALIZED = 17100107

CookieManager未初始化。

**起始版本：** 20

ARKWEB_COOKIE_MANAGER_INITIALIZE_FAILED = 17100108

CookieManager初始化失败。

**起始版本：** 20

ARKWEB_COOKIE_SAVE_FAILED = 17100109

保存cookie失败。

**起始版本：** 20

#### ArkWeb_BlanklessErrorCode

```ets
enum ArkWeb_BlanklessErrorCode
```

**描述：**

定义无白屏加载的异常错误码。

**起始版本：** 20

枚举项描述ARKWEB_BLANKLESS_SUCCESS = 0成功。ARKWEB_BLANKLESS_ERR_UNKNOWN = -1未知错误，内部状态错误等。ARKWEB_BLANKLESS_ERR_INVALID_ARGS = -2参数不合法。ARKWEB_BLANKLESS_ERR_CONTROLLER_NOT_INITED = -3WebViewController未绑定组件。ARKWEB_BLANKLESS_ERR_KEY_NOT_MATCH = -4未匹配到key值，对于OH_NativeArkWeb_SetBlanklessLoadingWithKey需与OH_NativeArkWeb_GetBlanklessInfoWithKey配套使用并且key值一致，否则返回该错误码。ARKWEB_BLANKLESS_ERR_SIGNIFICANT_CHANGE = -5当相似度较低时，系统会判定为跳变太大，OH_NativeArkWeb_SetBlanklessLoadingWithKey接口启用插帧不成功。ARKWEB_BLANKLESS_ERR_DEVICE_NOT_SUPPORT = 801该设备不适用于此功能。