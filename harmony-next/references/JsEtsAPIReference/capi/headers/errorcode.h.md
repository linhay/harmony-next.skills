# errorcode.h

#### 概述

提供国际化接口返回的错误码。

**引用文件：** <i18n/errorcode.h>

**库：** libohi18n.so

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**相关模块：**[i18n](../../topics/misc/i18n.md)

#### 汇总

#### 枚举

名称typedef关键字描述[I18n_ErrorCode](#ZH-CN_TOPIC_0000002529445291__i18n_errorcode)I18n_ErrorCode国际化错误码。

#### 枚举类型说明

#### I18n_ErrorCode

```ets
enum I18n_ErrorCode
```

**描述**

国际化错误码。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

枚举项描述SUCCESS = 0成功。ERROR_INVALID_PARAMETER = 8900001传入参数无效。UNEXPECTED_ERROR = 8900050预期之外的错误，例如内存错误。