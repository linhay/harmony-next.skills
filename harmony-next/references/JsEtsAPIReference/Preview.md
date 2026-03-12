# Preview

#### 概述

Preview Kit（文件预览服务）为应用提供便捷的文件快速预览服务。应用可以通过Preview Kit提供的预览API，快速启动预览界面，实现对各类文件的预览。

其中C API接口主要提供了文件打开加速功能，支持应用通过预加载机制提前加载文件，缩短用户打开文件时间，给用户提供流畅顺滑的爽感体验。

详见[文件打开加速开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-openfileboost)。

**起始版本：** 5.0.3(15)

#### 汇总

#### 文件

名称

描述

[open_file_boost.h](open_file_boost.h.md)

声明打开文件加速的API集合。

[preview_kit.h](preview_kit.h.md)

声明Preview Kit所包含的所有头文件。

#### 宏定义

名称

描述

[MAX_BUFFER_LENGTH](Preview.md#ZH-CN_TOPIC_0000002263162277__gaa8a8ed5c9e057542ff818fde39a94f07) 1024

沙箱路径最大长度1024。

#### 类型定义

名称

描述

typedef [OpenFileBoost_AppState](Preview.md#ZH-CN_TOPIC_0000002263162277__gafae4452b9e410d76236258ec57e0af62)(*[HMS_OpenFileBoost_QueryAppState](Preview.md#ZH-CN_TOPIC_0000002263162277__ga8de1d5d3db37e7701a91f24a56dee641)) (void)

该函数在调用[HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b)推荐文件之前先调用，用于向app查询当前是否允许推荐文件给app。比如，如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，app返回特定枚举值拒绝预加载。

typedef [OpenFileBoost_CbErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga773c6beb8645cfe54e1ce7eab67b8161)(*[HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b)) (void* fileInfo)

系统预测用户可能打开的文件，并通过该回调函数通知app，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知app取消某些文件的预加载。

#### 枚举

名称

描述

[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc) {

OPEN_FILE_BOOST_SUCCESS = 0,

OPEN_FILE_BOOST_PERMISSION_NOT_GRANTED = 201,

OPEN_FILE_BOOST_INVALID_PARAM = 401,

OPEN_FILE_BOOST_INTERNAL_ERROR = 1017200001,

OPEN_FILE_BOOST_INSUFFICIENT_BUFFER = 1017200002,

OPEN_FILE_BOOST_SERVICE_UNAVAILABLE = 1017200003,

OPEN_FILE_BOOST_NO_MEMORY = 1017200004

}

文件打开加速的错误码定义。

[OpenFileBoost_CbErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga773c6beb8645cfe54e1ce7eab67b8161) {

OPEN_FILE_BOOST_CALLBACK_SUCCESS = 0,

OPEN_FILE_BOOST_CALLBACK_FAILURE = 1017210000

}

回调函数[HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b)的错误码定义，它用于app向系统返回回调函数执行结果。

[OpenFileBoost_AppState](Preview.md#ZH-CN_TOPIC_0000002263162277__gafae4452b9e410d76236258ec57e0af62) {

OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD = 0,

OPEN_FILE_BOOST_APP_STATE_REJECT_PRELOAD = 1,

OPEN_FILE_BOOST_APP_STATE_FOREVER_REJECT_PRELOAD = 2

}

app状态，用于指示app当前允许、拒绝或永久拒绝系统推荐预加载文件。

#### 函数

名称

描述

[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)[HMS_OpenFileBoost_GetFdFromPreloadFileInfo](Preview.md#ZH-CN_TOPIC_0000002263162277__ga13429f2e33ddd0805274b46223a3f5b3) (void* fileInfo, int32_t* fd)

获取文件描述符信息。

[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)[HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo](Preview.md#ZH-CN_TOPIC_0000002263162277__ga16b482acdc9b56ebd8d01efed6875e95) (void* fileInfo, char* sandboxPath, int32_t pathLen)

获取沙箱路径信息。

[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)[HMS_OpenFileBoost_RegisterFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga0ff9ab52e40e265bc90a9cca779d0fd1) ([HMS_OpenFileBoost_QueryAppState](Preview.md#ZH-CN_TOPIC_0000002263162277__ga8de1d5d3db37e7701a91f24a56dee641) queryAppState, [HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b) filePreload, [HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b) cancelFilePreload)

注册预加载回调。

[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)[HMS_OpenFileBoost_UnregisterFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__gafdef9962cc4c394dad2103bd8c773e90) (void)

取消注册预加载回调。

[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)[HMS_OpenFileBoost_NotifyPreloadHit](Preview.md#ZH-CN_TOPIC_0000002263162277__ga613e9855b8e471157a522ba19bac4d5e) (int32_t fd, char* sandboxPath, int32_t pathLen)

当用户打开预加载文件时，app调用该接口通知系统预加载命中，这将有助于提高预加载文件预测的准确性。

#### 宏定义说明

#### MAX_BUFFER_LENGTH

```ets
#define MAX_BUFFER_LENGTH   1024
```

**描述**

沙箱路径最大长度

**起始版本：** 5.0.3(15)

#### 类型定义说明

#### HMS_OpenFileBoost_OnFilePreload

```ets
typedef [OpenFileBoost_CbErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga773c6beb8645cfe54e1ce7eab67b8161)(*HMS_OpenFileBoost_OnFilePreload) (void* fileInfo)
```

**描述**

系统向应用推荐或取消推荐预加载文件的回调函数定义。系统预测用户可能打开的文件，并通过该回调函数通知app，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知app取消某些文件的预加载。

**起始版本：** 5.0.3(15)

**参数:**

名称

描述

fileInfo

预加载文件信息，app可以调用[HMS_OpenFileBoost_GetFdFromPreloadFileInfo](Preview.md#ZH-CN_TOPIC_0000002263162277__ga13429f2e33ddd0805274b46223a3f5b3)获取对应的文件描述符信息，然后调用[HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo](Preview.md#ZH-CN_TOPIC_0000002263162277__ga16b482acdc9b56ebd8d01efed6875e95)获取对应的沙箱路径信息。app应该在当前回调上下文中同步解析预加载文件，以便系统可以评估本次预加载文件的资源消耗。

**返回：**

函数执行结果，如果执行成功则返回OPEN_FILE_BOOST_CALLBACK_SUCCESS，如果失败则返回 OPEN_FILE_BOOST_CALLBACK_FAILURE。

#### HMS_OpenFileBoost_QueryAppState

```ets
typedef [OpenFileBoost_AppState](Preview.md#ZH-CN_TOPIC_0000002263162277__gafae4452b9e410d76236258ec57e0af62)(*HMS_OpenFileBoost_QueryAppState) (void)
```

**描述**

系统查询app状态的回调函数定义，该函数在调用[HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b)推荐文件之前先回调app。该函数用于系统向app查询当前是否允许推荐文件给app。比如，如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，app返回特定枚举值拒绝预加载。

**起始版本：** 5.0.3(15)

**返回：**

如果app允许推荐文件，应该返回OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD，系统接下来将调用[HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b)去推荐文件进行预加载。如果app拒绝此次推荐， 应该返回OPEN_FILE_BOOST_APP_STATE_REJECT_PRELOAD。如果app在本次注册期间不想再收到推荐，应该返回OPEN_FILE_BOOST_APP_STATE_FOREVER_REJECT_PRELOAD，然后尽快调用[HMS_OpenFileBoost_UnregisterFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__gafdef9962cc4c394dad2103bd8c773e90)来取消注册。

#### 枚举类型说明

#### OpenFileBoost_AppState

```ets
enum [OpenFileBoost_AppState](Preview.md#ZH-CN_TOPIC_0000002263162277__gafae4452b9e410d76236258ec57e0af62)
```

**描述**

app状态，用于指示app当前是否允许系统推荐预加载文件。

**起始版本：** 5.0.3(15)

枚举值

描述

****OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD

当前允许推荐预加载文件。

****OPEN_FILE_BOOST_APP_STATE_REJECT_PRELOAD

当前不允许推荐预加载文件。

****OPEN_FILE_BOOST_APP_STATE_FOREVER_REJECT_PRELOAD

这次注册期间永远不允许推荐预加载文件。

#### OpenFileBoost_CbErrCode

```ets
enum [OpenFileBoost_CbErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga773c6beb8645cfe54e1ce7eab67b8161)
```

**描述**

回调函数[HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b)的错误码定义，它用于app向系统返回回调函数执行结果。

**起始版本：** 5.0.3(15)

枚举值

描述

****OPEN_FILE_BOOST_CALLBACK_SUCCESS

回调函数执行成功。

****OPEN_FILE_BOOST_CALLBACK_FAILURE

回调函数执行失败。

#### OpenFileBoost_ErrCode

```ets
enum [OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)
```

**描述**

文件打开加速的错误码定义。

**起始版本：** 5.0.3(15)

枚举值

描述

****OPEN_FILE_BOOST_SUCCESS

成功。

****OPEN_FILE_BOOST_PERMISSION_NOT_GRANTED

未授权。

****OPEN_FILE_BOOST_INVALID_PARAM

无效输入参数。

****OPEN_FILE_BOOST_INTERNAL_ERROR

内部错误。

****OPEN_FILE_BOOST_INSUFFICIENT_BUFFER

传入的缓冲区的长度不足。

****OPEN_FILE_BOOST_SERVICE_UNAVAILABLE

服务不可用。

****OPEN_FILE_BOOST_NO_MEMORY

内存不足。

#### 函数说明

#### HMS_OpenFileBoost_GetFdFromPreloadFileInfo()

```ets
[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc) HMS_OpenFileBoost_GetFdFromPreloadFileInfo (void* fileInfo, int32_t* fd)
```

**描述**

获取文件描述符信息。

**起始版本：** 5.0.3(15)

**参数:**

名称

描述

fileInfo

系统向app推荐的预加载文件信息。

fd

输出参数，预加载文件的文件描述符信息。

**返回：**

函数执行结果，如果执行成功则返回OPEN_FILE_BOOST_SUCCESS，如果失败将返回具体错误码，详见[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)。

#### HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo()

```ets
[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc) HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo (void* fileInfo, char* sandboxPath, int32_t pathLen)
```

**描述**

获取沙箱路径信息。

**起始版本：** 5.0.3(15)

**参数:**

名称

描述

fileInfo

系统向app推荐的预加载文件信息。

sandboxPath

输出参数，预加载文件的沙箱路径信息，app应该传递一个指向一块有效内存区域的指针，系统将向其中填充 沙箱路径信息。

pathLen

用于填充沙箱路径的内存区域的长度。

**返回：**

函数执行结果，如果执行成功则返回OPEN_FILE_BOOST_SUCCESS， 如果传入的内存缓冲区太小，系统将返回 OPEN_FILE_BOOST_INSUFFICIENT_BUFFER，其他错误详见[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)。

#### HMS_OpenFileBoost_NotifyPreloadHit()

```ets
[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc) HMS_OpenFileBoost_NotifyPreloadHit (int32_t fd, char* sandboxPath, int32_t pathLen)
```

**描述**

当用户打开预加载文件时，app调用该接口通知系统预加载命中，这将有助于提高预加载文件预测的准确性。

**起始版本：** 5.0.3(15)

**参数:**

名称

描述

fd

命中文件的文件描述符信息。

sandboxPath

命中文件的沙箱路径。

pathLen

沙箱路径的长度。

**返回：**

函数执行结果，如果执行成功则返回OPEN_FILE_BOOST_SUCCESS，如果失败将返回具体错误码，详见[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)。

#### HMS_OpenFileBoost_RegisterFilePreload()

```ets
[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc) HMS_OpenFileBoost_RegisterFilePreload ([HMS_OpenFileBoost_QueryAppState](Preview.md#ZH-CN_TOPIC_0000002263162277__ga8de1d5d3db37e7701a91f24a56dee641) queryAppState, [HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b) filePreload, [HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b) cancelFilePreload)
```

**描述**

注册预加载回调。

**起始版本：** 5.0.3(15)

**参数:**

名称

描述

queryAppState

app状态查询回调函数，在通知预加载之前先调用该回调函数查询当前是否允许推荐预加载文件。

filePreload

文件预加载回调，系统预测用户可能打开的文件，并通过该回调函数通知调用者。

cancelFilePreload

取消文件预加载回调，比如系统可用内存不足时系统会通知调用方取消文件的预加载。

**返回：**

函数执行结果，如果执行成功则返回OPEN_FILE_BOOST_SUCCESS，如果失败将返回具体错误码，详见[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)。

#### HMS_OpenFileBoost_UnregisterFilePreload()

```ets
[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc) HMS_OpenFileBoost_UnregisterFilePreload (void)
```

**描述**

取消注册预加载回调。

**起始版本：** 5.0.3(15)

**返回：**

函数执行结果，如果执行成功则返回OPEN_FILE_BOOST_SUCCESS，如果失败将返回具体错误码，详见[OpenFileBoost_ErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga5716dcdf88f1609b3466aadc675a0efc)。