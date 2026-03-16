# oh_pasteboard_err_code.h

#### 概述

声明剪贴板框架错误码信息。

**引用文件：** <database/pasteboard/oh_pasteboard_err_code.h>

**库：** libpasteboard.so

**系统能力：** SystemCapability.MiscServices.Pasteboard

**起始版本：** 13

**相关模块：**[Pasteboard](../../topics/payment/Pasteboard.md)

#### 汇总

#### 枚举

名称typedef关键字描述[PASTEBOARD_ErrCode](#ZH-CN_TOPIC_0000002529285523__pasteboard_errcode)PASTEBOARD_ErrCode错误码信息。

#### 枚举类型说明

#### PASTEBOARD_ErrCode

```ets
enum PASTEBOARD_ErrCode
```

**描述：**

错误码信息。

**起始版本：** 13

枚举项描述ERR_OK = 0执行成功。ERR_PERMISSION_ERROR = 201权限校验失败。ERR_INVALID_PARAMETER = 401非法参数。ERR_DEVICE_NOT_SUPPORTED = 801设备能力不支持。ERR_INNER_ERROR = 12900000内部错误。ERR_BUSY = 12900003系统忙。ERR_PASTEBOARD_COPY_FILE_ERROR = 12900007

文件拷贝失败。

 起始版本: 15

ERR_PASTEBOARD_PROGRESS_START_ERROR = 12900008

拉起进度显示失败。

 起始版本: 15

ERR_PASTEBOARD_PROGRESS_ABNORMAL = 12900009

进度显示异常。

 起始版本: 15

ERR_PASTEBOARD_GET_DATA_FAILED = 12900010

获取剪贴数据失败。

 起始版本: 15