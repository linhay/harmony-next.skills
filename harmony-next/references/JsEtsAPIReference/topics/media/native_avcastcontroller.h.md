# native_avcastcontroller.h

**概述**

提供播控控制器的定义。

引用文件： <multimedia/av_session/native_avcastcontroller.h>

库： libohavsession.so

系统能力： SystemCapability.Multimedia.AVSession.Core

起始版本： 23

相关模块： [OHAVSession](OHAVSession.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVCastController | OH_AVCastController | 播控控制器对象。使用OH_AVSession_CreateAVCastController方法创建指针。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_PlaybackStateChanged)(OH_AVCastController* avcastcontroller, OH_AVSession_AVPlaybackState* playbackState, void* userData) | OH_AVCastControllerCallback_PlaybackStateChanged | 播放状态改变的回调函数。 |
| typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_MediaItemChange)(OH_AVCastController* avcastcontroller, OH_AVSession_AVQueueItem* avQueueItem, void* userData) | OH_AVCastControllerCallback_MediaItemChange | 媒体项目变更的回调函数。 |
| typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_PlayNext)(OH_AVCastController* avcastcontroller, void* userData) | OH_AVCastControllerCallback_PlayNext | 播放下一首的回调函数。 |
| typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_PlayPrevious)(OH_AVCastController* avcastcontroller, void* userData) | OH_AVCastControllerCallback_PlayPrevious | 播放上一首的回调函数。 |
| typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_SeekDone)(OH_AVCastController* avcastcontroller, int32_t position, void* userData) | OH_AVCastControllerCallback_SeekDone | 搜索完成的回调函数。 |
| typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_EndOfStream)(OH_AVCastController* avcastcontroller, void* userData) | OH_AVCastControllerCallback_EndOfStream | 播放流结束的回调函数。 |
| typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_Error)(OH_AVCastController* avcastcontroller, void* userData, AVSession_ErrCode error) | OH_AVCastControllerCallback_Error | 播放错误的回调函数。 |
| AVSession_ErrCode OH_AVCastController_Destroy(OH_AVCastController* avcastcontroller) | - | 请求销毁播控控制器对象。 |
| AVSession_ErrCode OH_AVCastController_GetPlaybackState(OH_AVCastController* avcastcontroller, OH_AVSession_AVPlaybackState** playbackState) | - | 获取当前播放器的播放状态。不要单独释放playbackState指针。  当OH_AVCastController_Destroy被调用时播控控制器将被销毁。 |
| AVSession_ErrCode OH_AVCastController_RegisterPlaybackStateChangedCallback(OH_AVCastController* avcastcontroller, int32_t filter, OH_AVCastControllerCallback_PlaybackStateChanged callback, void* userData) | - | 请求注册播放状态改变的回调函数。 |
| AVSession_ErrCode OH_AVCastController_UnregisterPlaybackStateChangedCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlaybackStateChanged callback) | - | 请求取消注册播放状态改变的回调函数。 |
| AVSession_ErrCode OH_AVCastController_RegisterMediaItemChangedCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_MediaItemChange callback, void* userData) | - | 请求注册当前播放的媒体资源发生改变的回调函数。 |
| AVSession_ErrCode OH_AVCastController_UnregisterMediaItemChangedCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_MediaItemChange callback) | - | 请求取消注册当前播放的媒体资源发生改变的回调函数。 |
| AVSession_ErrCode OH_AVCastController_RegisterPlayNextCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayNext callback, void* userData) | - | 请求注册由远程端或媒体中心发送的播放下一首的回调函数。 |
| AVSession_ErrCode OH_AVCastController_UnregisterPlayNextCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayNext callback) | - | 请求取消注册由远程端或媒体中心发送的播放下一首的回调函数。 |
| AVSession_ErrCode OH_AVCastController_RegisterPlayPreviousCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayPrevious callback, void* userData) | - | 请求注册由远程端或媒体中心发送的播放上一首的回调函数。 |
| AVSession_ErrCode OH_AVCastController_UnregisterPlayPreviousCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayPrevious callback) | - | 请求取消注册由远程端或媒体中心发送的播放上一首的回调函数。 |
| AVSession_ErrCode OH_AVCastController_RegisterSeekDoneCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_SeekDone callback, void* userData) | - | 请求注册搜索完成的回调函数。 |
| AVSession_ErrCode OH_AVCastController_UnregisterSeekDoneCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_SeekDone callback) | - | 请求取消注册搜索完成的回调函数。 |
| AVSession_ErrCode OH_AVCastController_RegisterEndOfStreamCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_EndOfStream callback, void* userData) | - | 请求注册播放流结束的回调函数。 |
| AVSession_ErrCode OH_AVCastController_UnregisterEndOfStreamCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_EndOfStream callback) | - | 请求取消注册播放流结束的回调函数。 |
| AVSession_ErrCode OH_AVCastController_RegisterErrorCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_Error callback, void* userData) | - | 请求注册监听播放错误事件的回调函数。 |
| AVSession_ErrCode OH_AVCastController_UnregisterErrorCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_Error callback) | - | 请求取消注册监听播放错误事件的回调函数。 |
| AVSession_ErrCode OH_AVCastController_SendCommonCommand(OH_AVCastController* avcastcontroller, AVSession_AVCastControlCommandType* avCastControlcommand) | - | 请求发送普通命令到远程端。只支持发送播放、暂停、停止、播放下一首和播放上一首等命令。 |
| AVSession_ErrCode OH_AVCastController_SendSeekCommand(OH_AVCastController* avcastcontroller, int32_t seekTimeMS) | - | 请求向远程端发送搜索命令。 |
| AVSession_ErrCode OH_AVCastController_SendFastForwardCommand(OH_AVCastController* avcastcontroller, int32_t forwardTimeS) | - | 请求向远程端发送快进命令。 |
| AVSession_ErrCode OH_AVCastController_SendRewindCommand(OH_AVCastController* avcastcontroller, int32_t rewindTimeS) | - | 请求向远程端发送后退命令。 |
| AVSession_ErrCode OH_AVCastController_SendSetSpeedCommand(OH_AVCastController* avcastcontroller, AVSession_PlaybackSpeed speed) | - | 请求向远程端发送设置倍速命令。 |
| AVSession_ErrCode OH_AVCastController_SendVolumeCommand(OH_AVCastController* avcastcontroller, int32_t volume) | - | 请求向远程端发送音量控制命令。 |
| AVSession_ErrCode OH_AVCastController_Prepare(OH_AVCastController* avcastcontroller, OH_AVSession_AVQueueItem* avqueueItem) | - | 请求准备当前播放队列项，该操作是实现输出媒体信息展示的前置步骤。 |
| AVSession_ErrCode OH_AVCastController_Start(OH_AVCastController* avcastcontroller, OH_AVSession_AVQueueItem* avqueueItem) | - | 播放当前项目的请求，应该包含媒体资源，否则将播放失败。 |

**函数说明**

**OH_AVCastControllerCallback_PlaybackStateChanged()**

```ets
typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_PlaybackStateChanged)(OH_AVCastController* avcastcontroller, OH_AVSession_AVPlaybackState* playbackState, void* userData)
```

描述

播放状态改变的回调函数。

起始版本： 23

**OH_AVCastControllerCallback_MediaItemChange()**

```ets
typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_MediaItemChange)(OH_AVCastController* avcastcontroller, OH_AVSession_AVQueueItem* avQueueItem, void* userData)
```

描述

媒体项目变更的回调函数。

起始版本： 23

**OH_AVCastControllerCallback_PlayNext()**

```ets
typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_PlayNext)(OH_AVCastController* avcastcontroller, void* userData)
```

描述

播放下一首的回调函数。

起始版本： 23

**OH_AVCastControllerCallback_PlayPrevious()**

```ets
typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_PlayPrevious)(OH_AVCastController* avcastcontroller, void* userData)
```

描述

播放上一首的回调函数。

起始版本： 23

**OH_AVCastControllerCallback_SeekDone()**

```ets
typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_SeekDone)(OH_AVCastController* avcastcontroller, int32_t position, void* userData)
```

描述

搜索完成的回调函数。

起始版本： 23

**OH_AVCastControllerCallback_EndOfStream()**

```ets
typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_EndOfStream)(OH_AVCastController* avcastcontroller, void* userData)
```

描述

播放流结束的回调函数。

起始版本： 23

**OH_AVCastControllerCallback_Error()**

```ets
typedef AVSessionCallback_Result(*OH_AVCastControllerCallback_Error)(OH_AVCastController* avcastcontroller, void* userData, AVSession_ErrCode error)
```

描述

播放错误的回调函数。

起始版本： 23

**OH_AVCastController_Destroy()**

```ets
AVSession_ErrCode OH_AVCastController_Destroy(OH_AVCastController* avcastcontroller)
```

描述

请求销毁播控控制器对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：参数avcastcontroller为nullptr。 |

**OH_AVCastController_GetPlaybackState()**

```ets
AVSession_ErrCode OH_AVCastController_GetPlaybackState(OH_AVCastController* avcastcontroller, OH_AVSession_AVPlaybackState** playbackState)
```

描述

获取当前播放器的播放状态。不要单独释放playbackState指针。当[OH_AVCastController_Destroy](native_avcastcontroller.h.md#ZH-CN_TOPIC_0000002553201855__oh_avcastcontroller_destroy)被调用时播控控制器将被销毁。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVSession_AVPlaybackState** playbackState | 返回的播放状态。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数playbackState为nullptr。 |

**OH_AVCastController_RegisterPlaybackStateChangedCallback()**

```ets
AVSession_ErrCode OH_AVCastController_RegisterPlaybackStateChangedCallback(OH_AVCastController* avcastcontroller, int32_t filter, OH_AVCastControllerCallback_PlaybackStateChanged callback, void* userData)
```

描述

请求注册播放状态改变的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| int32_t filter | 通过播放状态的过滤器AVSession_PlaybackFilter来决定需要包含在回调中的参数。 |
| OH_AVCastControllerCallback_PlaybackStateChanged callback | 要注册的回调函数。 |
| void* userData | 由用户传递的用户数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。  3. 参数filter是无效的。 |

**OH_AVCastController_UnregisterPlaybackStateChangedCallback()**

```ets
AVSession_ErrCode OH_AVCastController_UnregisterPlaybackStateChangedCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlaybackStateChanged callback)
```

描述

请求取消注册播放状态改变的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_PlaybackStateChanged callback | 要取消注册的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_RegisterMediaItemChangedCallback()**

```ets
AVSession_ErrCode OH_AVCastController_RegisterMediaItemChangedCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_MediaItemChange callback, void* userData)
```

描述

请求注册当前播放的媒体资源发生改变的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_MediaItemChange callback | 要注册的回调函数。 |
| void* userData | 由用户传递的用户数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_UnregisterMediaItemChangedCallback()**

```ets
AVSession_ErrCode OH_AVCastController_UnregisterMediaItemChangedCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_MediaItemChange callback)
```

描述

请求取消注册当前播放的媒体资源发生改变的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_MediaItemChange callback | 要取消注册的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_RegisterPlayNextCallback()**

```ets
AVSession_ErrCode OH_AVCastController_RegisterPlayNextCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayNext callback, void* userData)
```

描述

请求注册由远程端或媒体中心发送的播放下一首的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_PlayNext callback | 要注册的回调函数。 |
| void* userData | 由用户传递的用户数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_UnregisterPlayNextCallback()**

```ets
AVSession_ErrCode OH_AVCastController_UnregisterPlayNextCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayNext callback)
```

描述

请求取消注册由远程端或媒体中心发送的播放下一首的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_PlayNext callback | 要取消注册的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_RegisterPlayPreviousCallback()**

```ets
AVSession_ErrCode OH_AVCastController_RegisterPlayPreviousCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayPrevious callback, void* userData)
```

描述

请求注册由远程端或媒体中心发送的播放上一首的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_PlayPrevious callback | 要注册的回调函数。 |
| void* userData | 由用户传递的用户数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_UnregisterPlayPreviousCallback()**

```ets
AVSession_ErrCode OH_AVCastController_UnregisterPlayPreviousCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_PlayPrevious callback)
```

描述

请求取消注册由远程端或媒体中心发送的播放上一首的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_PlayPrevious callback | 要取消注册的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_RegisterSeekDoneCallback()**

```ets
AVSession_ErrCode OH_AVCastController_RegisterSeekDoneCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_SeekDone callback, void* userData)
```

描述

请求注册搜索完成的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_SeekDone callback | 要注册的回调函数。 |
| void* userData | 由用户传递的用户数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_UnregisterSeekDoneCallback()**

```ets
AVSession_ErrCode OH_AVCastController_UnregisterSeekDoneCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_SeekDone callback)
```

描述

请求取消注册搜索完成的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_SeekDone callback | 要取消注册的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_RegisterEndOfStreamCallback()**

```ets
AVSession_ErrCode OH_AVCastController_RegisterEndOfStreamCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_EndOfStream callback, void* userData)
```

描述

请求注册播放流结束的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_EndOfStream callback | 要注册的回调函数。 |
| void* userData | 由用户传递的用户数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_UnregisterEndOfStreamCallback()**

```ets
AVSession_ErrCode OH_AVCastController_UnregisterEndOfStreamCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_EndOfStream callback)
```

描述

请求取消注册播放流结束的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_EndOfStream callback | 要取消注册的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_RegisterErrorCallback()**

```ets
AVSession_ErrCode OH_AVCastController_RegisterErrorCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_Error callback, void* userData)
```

描述

请求注册监听播放错误事件的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_Error callback | 要注册的回调函数。 |
| void* userData | 由用户传递的用户数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_UnregisterErrorCallback()**

```ets
AVSession_ErrCode OH_AVCastController_UnregisterErrorCallback(OH_AVCastController* avcastcontroller, OH_AVCastControllerCallback_Error callback)
```

描述

请求取消注册监听播放错误事件的回调函数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVCastControllerCallback_Error callback | 要取消注册的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数callback为nullptr。 |

**OH_AVCastController_SendCommonCommand()**

```ets
AVSession_ErrCode OH_AVCastController_SendCommonCommand(OH_AVCastController* avcastcontroller, AVSession_AVCastControlCommandType* avCastControlcommand)
```

描述

请求发送普通命令到远程端。只支持发送播放、暂停、停止、播放下一首和播放上一首等命令。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| AVSession_AVCastControlCommandType* avCastControlcommand | 控制命令。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：参数avcastcontroller为nullptr。  AV_SESSION_ERR_CODE_COMMAND_INVALID：参数avCastControlcommand是无效的。  AV_SESSION_ERR_CODE_REMOTE_CONNECTION_NOT_EXIST：远程连接未建立。 |

**OH_AVCastController_SendSeekCommand()**

```ets
AVSession_ErrCode OH_AVCastController_SendSeekCommand(OH_AVCastController* avcastcontroller, int32_t seekTimeMS)
```

描述

请求向远程端发送搜索命令。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| int32_t seekTimeMS | 寻找时间。单位为毫秒。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数seekTimeMS是无效的。  AV_SESSION_ERR_CODE_REMOTE_CONNECTION_NOT_EXIST：远程连接未建立。 |

**OH_AVCastController_SendFastForwardCommand()**

```ets
AVSession_ErrCode OH_AVCastController_SendFastForwardCommand(OH_AVCastController* avcastcontroller, int32_t forwardTimeS)
```

描述

请求向远程端发送快进命令。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| int32_t forwardTimeS | 快进时间。单位为秒。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数forwardTimeS是无效的。  AV_SESSION_ERR_CODE_REMOTE_CONNECTION_NOT_EXIST：远程连接未建立。 |

**OH_AVCastController_SendRewindCommand()**

```ets
AVSession_ErrCode OH_AVCastController_SendRewindCommand(OH_AVCastController* avcastcontroller, int32_t rewindTimeS)
```

描述

请求向远程端发送后退命令。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| int32_t rewindTimeS | 后退时间。单位为秒。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数rewindTimeS是无效的。  AV_SESSION_ERR_CODE_REMOTE_CONNECTION_NOT_EXIST：远程连接未建立。 |

**OH_AVCastController_SendSetSpeedCommand()**

```ets
AVSession_ErrCode OH_AVCastController_SendSetSpeedCommand(OH_AVCastController* avcastcontroller, AVSession_PlaybackSpeed speed)
```

描述

请求向远程端发送设置倍速命令。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| AVSession_PlaybackSpeed speed | 倍速控制命令。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数speed是无效的。  AV_SESSION_ERR_CODE_REMOTE_CONNECTION_NOT_EXIST：远程连接未建立。 |

**OH_AVCastController_SendVolumeCommand()**

```ets
AVSession_ErrCode OH_AVCastController_SendVolumeCommand(OH_AVCastController* avcastcontroller, int32_t volume)
```

描述

请求向远程端发送音量控制命令。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| int32_t volume | 音量控制。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数volume是无效的。  AV_SESSION_ERR_CODE_REMOTE_CONNECTION_NOT_EXIST：远程连接未建立。 |

**OH_AVCastController_Prepare()**

```ets
AVSession_ErrCode OH_AVCastController_Prepare(OH_AVCastController* avcastcontroller, OH_AVSession_AVQueueItem* avqueueItem)
```

描述

请求准备当前播放队列项，该操作是实现输出媒体信息展示的前置步骤。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVSession_AVQueueItem* avqueueItem | 音视频队列项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数avqueueItem为nullptr。  AV_SESSION_ERR_CODE_REMOTE_CONNECTION_NOT_EXIST：远程连接未建立。 |

**OH_AVCastController_Start()**

```ets
AVSession_ErrCode OH_AVCastController_Start(OH_AVCastController* avcastcontroller, OH_AVSession_AVQueueItem* avqueueItem)
```

描述

播放当前项目的请求，应该包含媒体资源，否则将播放失败。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVCastController* avcastcontroller | 播控控制器的实例对象。 |
| OH_AVSession_AVQueueItem* avqueueItem | 音视频队列项。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_SERVICE_EXCEPTION：服务器内部错误。  AV_SESSION_ERR_INVALID_PARAMETER：  1. 参数avcastcontroller为nullptr。  2. 参数avqueueItem为nullptr。 |