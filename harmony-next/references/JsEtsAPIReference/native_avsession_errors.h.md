# native_avsession_errors.h

#### 概述

提供播控错误码的定义。

**引用文件：** <multimedia/av_session/native_avsession_errors.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 13

**相关模块：**[OHAVSession](OHAVSession.md)

#### 汇总

#### 枚举

名称typedef关键字描述[AVSession_ErrCode](#ZH-CN_TOPIC_0000002529445735__avsession_errcode)AVSession_ErrCode播控错误码。

#### 枚举类型说明

#### AVSession_ErrCode

```ets
enum AVSession_ErrCode
```

**描述**

播控错误码。

**起始版本：** 13

枚举项描述AV_SESSION_ERR_SUCCESS = 0操作成功。AV_SESSION_ERR_INVALID_PARAMETER = 401参数检查失败。AV_SESSION_ERR_SERVICE_EXCEPTION = 6600101会话服务端异常。AV_SESSION_ERR_CODE_SESSION_NOT_EXIST = 6600102会话不存在。AV_SESSION_ERR_CODE_COMMAND_INVALID = 6600105无效会话命令。AV_SESSION_ERR_CODE_SESSION_INACTIVE = 6600106会话未激活。AV_SESSION_ERR_CODE_MESSAGE_OVERLOAD = 6600107命令&消息过载。