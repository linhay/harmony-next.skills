# graphic_error_code.h

#### 概述

定义错误码。

**引用文件：** <native_window/graphic_error_code.h>

**库：** libnative_window.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**相关模块：**[NativeWindow](NativeWindow.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OHNativeErrorCode](#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)OHNativeErrorCode接口错误码说明（仅用于查询）。

#### 枚举类型说明

#### OHNativeErrorCode

```ets
enum OHNativeErrorCode
```

**描述**

接口错误码说明（仅用于查询）。

**起始版本：** 12

枚举项描述NATIVE_ERROR_OK = 0成功。NATIVE_ERROR_MEM_OPERATION_ERROR = 30001000

内存操作错误。

**起始版本：** 15

NATIVE_ERROR_INVALID_ARGUMENTS = 40001000入参无效。NATIVE_ERROR_NO_PERMISSION = 40301000无权限操作。NATIVE_ERROR_NO_BUFFER = 40601000无空闲可用的buffer。NATIVE_ERROR_NO_CONSUMER = 41202000消费端不存在。NATIVE_ERROR_NOT_INIT = 41203000未初始化。NATIVE_ERROR_CONSUMER_CONNECTED = 41206000消费端已经被连接。NATIVE_ERROR_BUFFER_STATE_INVALID = 41207000buffer状态不符合预期。NATIVE_ERROR_BUFFER_IN_CACHE = 41208000buffer已在缓存队列中。NATIVE_ERROR_BUFFER_QUEUE_FULL = 41209000队列已满。NATIVE_ERROR_BUFFER_NOT_IN_CACHE = 41210000buffer不在缓存队列中。NATIVE_ERROR_CONSUMER_DISCONNECTED = 41211000消费端已经被断开连接。NATIVE_ERROR_CONSUMER_NO_LISTENER_REGISTERED = 41212000消费端未注册listener回调函数。NATIVE_ERROR_UNSUPPORTED = 50102000当前设备或平台不支持。NATIVE_ERROR_UNKNOWN = 50002000未知错误，请查看日志。NATIVE_ERROR_HDI_ERROR = 50007000HDI接口调用失败。NATIVE_ERROR_BINDER_ERROR = 50401000跨进程通信失败。NATIVE_ERROR_EGL_STATE_UNKNOWN = 60001000egl环境状态异常。NATIVE_ERROR_EGL_API_FAILED = 60002000egl接口调用失败。