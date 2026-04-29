# graphic_error_code.h

**概述**

定义错误码。

引用文件： <native_window/graphic_error_code.h>

库： libnative_window.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeWindow

起始版本： 12

相关模块： [NativeWindow](NativeWindow.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OHNativeErrorCode | OHNativeErrorCode | 接口错误码说明（仅用于查询）。 |

**枚举类型说明**

**OHNativeErrorCode**

```ets
enum OHNativeErrorCode
```

描述

接口错误码说明（仅用于查询）。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| NATIVE_ERROR_OK = 0 | 成功。 |
| NATIVE_ERROR_MEM_OPERATION_ERROR = 30001000 | 内存操作错误。 起始版本： 15 |
| NATIVE_ERROR_INVALID_ARGUMENTS = 40001000 | 入参无效。 |
| NATIVE_ERROR_NO_PERMISSION = 40301000 | 无权限操作。 |
| NATIVE_ERROR_NO_BUFFER = 40601000 | 无空闲可用的buffer。 |
| NATIVE_ERROR_NO_CONSUMER = 41202000 | 消费端不存在。 |
| NATIVE_ERROR_NOT_INIT = 41203000 | 未初始化。 |
| NATIVE_ERROR_CONSUMER_CONNECTED = 41206000 | 消费端已经被连接。 |
| NATIVE_ERROR_BUFFER_STATE_INVALID = 41207000 | buffer状态不符合预期。 |
| NATIVE_ERROR_BUFFER_IN_CACHE = 41208000 | buffer已在缓存队列中。 |
| NATIVE_ERROR_BUFFER_QUEUE_FULL = 41209000 | 队列已满。 |
| NATIVE_ERROR_BUFFER_NOT_IN_CACHE = 41210000 | buffer不在缓存队列中。 |
| NATIVE_ERROR_CONSUMER_DISCONNECTED = 41211000 | 消费端已经被断开连接。 |
| NATIVE_ERROR_CONSUMER_NO_LISTENER_REGISTERED = 41212000 | 消费端未注册listener回调函数。 |
| NATIVE_ERROR_UNSUPPORTED = 50102000 | 当前设备或平台不支持。 |
| NATIVE_ERROR_UNKNOWN = 50002000 | 未知错误，请查看日志。 |
| NATIVE_ERROR_HDI_ERROR = 50007000 | HDI接口调用失败。 |
| NATIVE_ERROR_BINDER_ERROR = 50401000 | 跨进程通信失败。 |
| NATIVE_ERROR_EGL_STATE_UNKNOWN = 60001000 | egl环境状态异常。 |
| NATIVE_ERROR_EGL_API_FAILED = 60002000 | egl接口调用失败。 |