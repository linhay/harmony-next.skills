# native_avscreen_capture_errors.h

**概述**

声明用于运行屏幕录制过程中接口调用的错误码说明。

引用文件： <multimedia/player_framework/native_avscreen_capture_errors.h>

库： libnative_avscreen_capture.so

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

相关模块： [AVScreenCapture](AVScreenCapture.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVSCREEN_CAPTURE_ErrCode | OH_AVSCREEN_CAPTURE_ErrCode | 屏幕录制过程中产生的不同结果码。 |

**枚举类型说明**

**OH_AVSCREEN_CAPTURE_ErrCode**

```ets
enum OH_AVSCREEN_CAPTURE_ErrCode
```

描述

屏幕录制过程中产生的不同结果码。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| AV_SCREEN_CAPTURE_ERR_BASE = 0 | 接口调用错误返回的基础值。 |
| AV_SCREEN_CAPTURE_ERR_OK = AV_SCREEN_CAPTURE_ERR_BASE | 操作成功。 |
| AV_SCREEN_CAPTURE_ERR_NO_MEMORY = AV_SCREEN_CAPTURE_ERR_BASE + 1 | 内存不足。 |
| AV_SCREEN_CAPTURE_ERR_OPERATE_NOT_PERMIT = AV_SCREEN_CAPTURE_ERR_BASE + 2 | 不允许操作。 |
| AV_SCREEN_CAPTURE_ERR_INVALID_VAL = AV_SCREEN_CAPTURE_ERR_BASE + 3 | 无效参数。 |
| AV_SCREEN_CAPTURE_ERR_IO = AV_SCREEN_CAPTURE_ERR_BASE + 4 | 输入输出流异常。 |
| AV_SCREEN_CAPTURE_ERR_TIMEOUT = AV_SCREEN_CAPTURE_ERR_BASE + 5 | 网络超时。 |
| AV_SCREEN_CAPTURE_ERR_UNKNOWN = AV_SCREEN_CAPTURE_ERR_BASE + 6 | 未知错误。 |
| AV_SCREEN_CAPTURE_ERR_SERVICE_DIED = AV_SCREEN_CAPTURE_ERR_BASE + 7 | 媒体服务已终止。 |
| AV_SCREEN_CAPTURE_ERR_INVALID_STATE = AV_SCREEN_CAPTURE_ERR_BASE + 8 | 当前状态不支持此操作。 |
| AV_SCREEN_CAPTURE_ERR_UNSUPPORT = AV_SCREEN_CAPTURE_ERR_BASE + 9 | 不支持的接口。 |
| AV_SCREEN_CAPTURE_ERR_EXTEND_START = AV_SCREEN_CAPTURE_ERR_BASE + 100 | 预期之外的错误。 |