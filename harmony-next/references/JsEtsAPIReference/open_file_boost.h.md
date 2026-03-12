# open_file_boost.h

#### 概述

声明文件打开加速的API集合

**库：** libopen_file_boost.so

**系统能力：** SystemCapability.PCService.OpenFileBoost

**起始版本：** 5.0.3(15)

**相关模块：**[Preview](Preview.md)

#### 汇总

#### 宏定义

名称

描述

[MAX_BUFFER_LENGTH](Preview.md#ZH-CN_TOPIC_0000002263162277__gaa8a8ed5c9e057542ff818fde39a94f07) 1024

沙箱路径最大长度。

#### 类型定义

名称

描述

typedef [OpenFileBoost_AppState](Preview.md#ZH-CN_TOPIC_0000002263162277__gafae4452b9e410d76236258ec57e0af62)(*[HMS_OpenFileBoost_QueryAppState](Preview.md#ZH-CN_TOPIC_0000002263162277__ga8de1d5d3db37e7701a91f24a56dee641)) (void)

系统查询app状态的回调函数定义，该函数在调用[HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b)推荐文件之前先回调app。该函数用于系统向app查询当前是否允许推荐文件给app。如果应用处于前台焦点或者某些特殊状态，不适合预加载文件，app返回特定枚举值拒绝预加载。

typedef [OpenFileBoost_CbErrCode](Preview.md#ZH-CN_TOPIC_0000002263162277__ga773c6beb8645cfe54e1ce7eab67b8161)(*[HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b)) (void* fileInfo)

系统向应用推荐或取消推荐预加载文件的回调函数定义。 系统预测用户可能打开的文件，并通过该回调函数通知app，另外在某些场景下，比如当前系统可用内存不足，或者有其他文件更有可能被用户打开，则系统会通知app取消某些文件的预加载。

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

回调函数[HMS_OpenFileBoost_OnFilePreload](Preview.md#ZH-CN_TOPIC_0000002263162277__ga7cb236400dadbd94b0586c7f234ad23b)的错误码定义， 它用于app向系统返回回调函数执行结果。

[OpenFileBoost_AppState](Preview.md#ZH-CN_TOPIC_0000002263162277__gafae4452b9e410d76236258ec57e0af62) {

OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD = 0,

OPEN_FILE_BOOST_APP_STATE_REJECT_PRELOAD = 1,

OPEN_FILE_BOOST_APP_STATE_FOREVER_REJECT_PRELOAD = 2

}

app状态，用于指示app当前是否允许系统推荐预加载文件。

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