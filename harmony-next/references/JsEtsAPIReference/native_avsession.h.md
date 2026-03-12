# native_avsession.h

#### 概述

媒体会话定义，可用于设置元数据、播放状态信息等操作。

**引用文件：** <multimedia/av_session/native_avsession.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 13

**相关模块：**[OHAVSession](OHAVSession.md)

#### 汇总

#### 结构体

名称typedef关键字描述[AVSession_PlaybackPosition](AVSession_PlaybackPosition.md)AVSession_PlaybackPosition媒体播放位置的相关属性。[OH_AVSession](OH_AVSession.md)OH_AVSession播控会话对象定义。可以用OH_AVSession_Create创建一个会话对象。

#### 枚举

名称typedef关键字描述[AVSession_Type](#ZH-CN_TOPIC_0000002529285761__avsession_type)AVSession_Type会话类型。[AVSession_PlaybackState](#ZH-CN_TOPIC_0000002529285761__avsession_playbackstate)AVSession_PlaybackState媒体播放状态的相关属性。[AVSession_LoopMode](#ZH-CN_TOPIC_0000002529285761__avsession_loopmode)AVSession_LoopMode媒体播放循环模式。[AVSession_ControlCommand](#ZH-CN_TOPIC_0000002529285761__avsession_controlcommand)AVSession_ControlCommand播控命令。[AVSessionCallback_Result](#ZH-CN_TOPIC_0000002529285761__avsessioncallback_result)AVSessionCallback_Result回调执行的结果。

#### 函数

名称typedef关键字描述[typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnCommand)(OH_AVSession* session, AVSession_ControlCommand command, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_oncommand)OH_AVSessionCallback_OnCommand通用的执行播控命令的回调。[typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnFastForward)(OH_AVSession* session, uint32_t seekTime, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onfastforward)OH_AVSessionCallback_OnFastForward快进的回调。[typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnRewind)(OH_AVSession* session, uint32_t seekTime, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onrewind)OH_AVSessionCallback_OnRewind快退的回调。[typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnSeek)(OH_AVSession* session, uint64_t seekTime, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onseek)OH_AVSessionCallback_OnSeek进度调节的回调。[typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnSetLoopMode)(OH_AVSession* session, AVSession_LoopMode curLoopMode, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onsetloopmode)OH_AVSessionCallback_OnSetLoopMode设置循环模式的回调。[typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnToggleFavorite)(OH_AVSession* session, const char* assetId, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_ontogglefavorite)OH_AVSessionCallback_OnToggleFavorite收藏的回调。[AVSession_ErrCode OH_AVSession_Create(AVSession_Type sessionType, const char* sessionTag,const char* bundleName, const char* abilityName, OH_AVSession** avsession)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_create)-创建会话对象。[AVSession_ErrCode OH_AVSession_Destroy(OH_AVSession* avsession)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_destroy)-销毁会话对象。[AVSession_ErrCode OH_AVSession_Activate(OH_AVSession* avsession)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_activate)-激活会话。[AVSession_ErrCode OH_AVSession_Deactivate(OH_AVSession* avsession)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_deactivate)-取消激活媒体会话。[AVSession_ErrCode OH_AVSession_GetSessionType(OH_AVSession* avsession, AVSession_Type* sessionType)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_getsessiontype)-获取会话类型。[AVSession_ErrCode OH_AVSession_GetSessionId(OH_AVSession* avsession, const char** sessionId)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_getsessionid)-获取会话id。[AVSession_ErrCode OH_AVSession_SetAVMetadata(OH_AVSession* avsession, OH_AVMetadata* avmetadata)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_setavmetadata)-设置媒体元数据。[AVSession_ErrCode OH_AVSession_SetPlaybackState(OH_AVSession* avsession, AVSession_PlaybackState playbackState)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_setplaybackstate)-设置播放状态。[AVSession_ErrCode OH_AVSession_SetPlaybackPosition(OH_AVSession* avsession, AVSession_PlaybackPosition* playbackPosition)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_setplaybackposition)-设置播放位置。[AVSession_ErrCode OH_AVSession_SetFavorite(OH_AVSession* avsession, bool favorite)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_setfavorite)-设置收藏状态。[AVSession_ErrCode OH_AVSession_SetLoopMode(OH_AVSession* avsession, AVSession_LoopMode loopMode)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_setloopmode)-设置循环模式。[AVSession_ErrCode OH_AVSession_RegisterCommandCallback(OH_AVSession* avsession,AVSession_ControlCommand command, OH_AVSessionCallback_OnCommand callback, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_registercommandcallback)-注册通用播控的回调。[AVSession_ErrCode OH_AVSession_UnregisterCommandCallback(OH_AVSession* avsession, AVSession_ControlCommand command, OH_AVSessionCallback_OnCommand callback)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_unregistercommandcallback)-取消注册通用播控的回调。[AVSession_ErrCode OH_AVSession_RegisterForwardCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnFastForward callback, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_registerforwardcallback)-注册快进的回调。[AVSession_ErrCode OH_AVSession_UnregisterForwardCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnFastForward callback)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_unregisterforwardcallback)-取消注册快进的回调。[AVSession_ErrCode OH_AVSession_RegisterRewindCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnRewind callback, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_registerrewindcallback)-注册快退的回调。[AVSession_ErrCode OH_AVSession_UnregisterRewindCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnRewind callback)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_unregisterrewindcallback)-取消注册快退的回调。[AVSession_ErrCode OH_AVSession_RegisterSeekCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnSeek callback, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_registerseekcallback)-注册跳转的回调。[AVSession_ErrCode OH_AVSession_UnregisterSeekCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnSeek callback)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_unregisterseekcallback)-取消注册跳转的回调。[AVSession_ErrCode OH_AVSession_RegisterSetLoopModeCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnSetLoopMode callback, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_registersetloopmodecallback)-注册设置循环模式的回调。[AVSession_ErrCode OH_AVSession_UnregisterSetLoopModeCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnSetLoopMode callback)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_unregistersetloopmodecallback)-取消注册设置循环模式的回调。[AVSession_ErrCode OH_AVSession_RegisterToggleFavoriteCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnToggleFavorite callback, void* userData)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_registertogglefavoritecallback)-设置收藏的回调。[AVSession_ErrCode OH_AVSession_UnregisterToggleFavoriteCallback(OH_AVSession* avsession, OH_AVSessionCallback_OnToggleFavorite callback)](#ZH-CN_TOPIC_0000002529285761__oh_avsession_unregistertogglefavoritecallback)-取消设置收藏的回调。

#### 枚举类型说明

#### AVSession_Type

```ets
enum AVSession_Type
```

**描述**

会话类型。

**起始版本：** 13

枚举项描述SESSION_TYPE_AUDIO = 0音频。SESSION_TYPE_VIDEO = 1视频。SESSION_TYPE_VOICE_CALL = 2音频通话。SESSION_TYPE_VIDEO_CALL = 3视频通话。

#### AVSession_PlaybackState

```ets
enum AVSession_PlaybackState
```

**描述**

媒体播放状态的相关属性。

**起始版本：** 13

枚举项描述PLAYBACK_STATE_INITIAL = 0初始状态。PLAYBACK_STATE_PREPARING = 1准备状态。PLAYBACK_STATE_PLAYING = 2正在播放。PLAYBACK_STATE_PAUSED = 3暂停。PLAYBACK_STATE_FAST_FORWARDING = 4快进。PLAYBACK_STATE_REWINDED = 5快退。PLAYBACK_STATE_STOPPED = 6停止。PLAYBACK_STATE_COMPLETED = 7播放完成。PLAYBACK_STATE_RELEASED = 8释放。PLAYBACK_STATE_ERROR = 9错误。PLAYBACK_STATE_IDLE = 10空闲。PLAYBACK_STATE_BUFFERING = 11缓冲。PLAYBACK_STATE_MAX = 12最大状态。（当state为12时，返回错误码401）

#### AVSession_LoopMode

```ets
enum AVSession_LoopMode
```

**描述**

媒体播放循环模式。

**起始版本：** 13

枚举项描述LOOP_MODE_SEQUENCE = 0顺序播放。LOOP_MODE_SINGLE = 1单曲循环。LOOP_MODE_LIST = 2表单循环。LOOP_MODE_SHUFFLE = 3随机播放。LOOP_MODE_CUSTOM = 4自定义播放。

#### AVSession_ControlCommand

```ets
enum AVSession_ControlCommand
```

**描述**

播控命令。

**起始版本：** 13

枚举项描述CONTROL_CMD_INVALID = -1无效控制命令。CONTROL_CMD_PLAY = 0播放命令。CONTROL_CMD_PAUSE = 1暂停命令。CONTROL_CMD_STOP = 2停止命令。CONTROL_CMD_PLAY_NEXT = 3播放下一首命令。CONTROL_CMD_PLAY_PREVIOUS = 4播放上一首命令。

#### AVSessionCallback_Result

```ets
enum AVSessionCallback_Result
```

**描述**

回调执行的结果。

**起始版本：** 13

枚举项描述AVSESSION_CALLBACK_RESULT_SUCCESS = 0执行成功。AVSESSION_CALLBACK_RESULT_FAILURE = -1执行失败。

#### 函数说明

#### OH_AVSessionCallback_OnCommand()

```ets
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnCommand)(OH_AVSession* session,AVSession_ControlCommand command, void* userData)
```

**描述**

通用的执行播控命令的回调。

**起始版本：** 13

#### OH_AVSessionCallback_OnFastForward()

```ets
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnFastForward)(OH_AVSession* session,uint32_t seekTime, void* userData)
```

**描述**

快进的回调。

**起始版本：** 13

#### OH_AVSessionCallback_OnRewind()

```ets
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnRewind)(OH_AVSession* session,uint32_t seekTime, void* userData)
```

**描述**

快退的回调。

**起始版本：** 13

#### OH_AVSessionCallback_OnSeek()

```ets
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnSeek)(OH_AVSession* session,uint64_t seekTime, void* userData)
```

**描述**

进度调节的回调。

**起始版本：** 13

#### OH_AVSessionCallback_OnSetLoopMode()

```ets
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnSetLoopMode)(OH_AVSession* session,AVSession_LoopMode curLoopMode, void* userData)
```

**描述**

设置循环模式的回调。

**起始版本：** 13

#### OH_AVSessionCallback_OnToggleFavorite()

```ets
typedef AVSessionCallback_Result (*OH_AVSessionCallback_OnToggleFavorite)(OH_AVSession* session,const char* assetId, void* userData)
```

**描述**

收藏的回调。

**起始版本：** 13

#### OH_AVSession_Create()

```ets
AVSession_ErrCode OH_AVSession_Create(AVSession_Type sessionType, const char* sessionTag,const char* bundleName, const char* abilityName, OH_AVSession** avsession)
```

**描述**

创建会话对象。

**起始版本：** 13

**参数：**

参数项描述[AVSession_Type](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__avsession_type) sessionType会话类型[AVSession_Type](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__avsession_type)。const char* sessionTag会话标签。const char* bundleName创建会话的包名。const char* abilityName创建会话的ability名。[OH_AVSession](OH_AVSession.md)** avsession返回的媒体会话对象。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数sessionType无效。

 2.参数sessionTag为nullptr。

 3.参数bundleName为nullptr。

 4.参数abilityName为nullptr。

 5.参数avsession为nullptr。

#### OH_AVSession_Destroy()

```ets
AVSession_ErrCode OH_AVSession_Destroy(OH_AVSession* avsession)
```

**描述**

销毁会话对象。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_INVALID_PARAMETER：参数avsession为nullptr。

#### OH_AVSession_Activate()

```ets
AVSession_ErrCode OH_AVSession_Activate(OH_AVSession* avsession)
```

**描述**

激活会话。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_INVALID_PARAMETER：参数avsession为nullptr。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

#### OH_AVSession_Deactivate()

```ets
AVSession_ErrCode OH_AVSession_Deactivate(OH_AVSession* avsession)
```

**描述**

取消激活媒体会话。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_INVALID_PARAMETER：参数avsession为nullptr。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

#### OH_AVSession_GetSessionType()

```ets
AVSession_ErrCode OH_AVSession_GetSessionType(OH_AVSession* avsession, AVSession_Type* sessionType)
```

**描述**

获取会话类型。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[AVSession_Type](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__avsession_type)* sessionType返回的会话类型。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常，获取session type错误。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数sessionType为nullptr。

#### OH_AVSession_GetSessionId()

```ets
AVSession_ErrCode OH_AVSession_GetSessionId(OH_AVSession* avsession, const char** sessionId)
```

**描述**

获取会话id。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。const char** sessionId返回的会话类型id。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数sessionId为nullptr。

#### OH_AVSession_SetAVMetadata()

```ets
AVSession_ErrCode OH_AVSession_SetAVMetadata(OH_AVSession* avsession, OH_AVMetadata* avmetadata)
```

**描述**

设置媒体元数据。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVMetadata](OH_AVMetadataStruct.md)* avmetadata设置媒体元数据信息。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数avmetadata为nullptr。

#### OH_AVSession_SetPlaybackState()

```ets
AVSession_ErrCode OH_AVSession_SetPlaybackState(OH_AVSession* avsession,AVSession_PlaybackState playbackState)
```

**描述**

设置播放状态。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[AVSession_PlaybackState](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__avsession_playbackstate) playbackState播放状态。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数playbackState无效。

#### OH_AVSession_SetPlaybackPosition()

```ets
AVSession_ErrCode OH_AVSession_SetPlaybackPosition(OH_AVSession* avsession,AVSession_PlaybackPosition* playbackPosition)
```

**描述**

设置播放位置。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[AVSession_PlaybackPosition](AVSession_PlaybackPosition.md)* playbackPosition播放位置对象。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数playbackPosition为nullptr。

#### OH_AVSession_SetFavorite()

```ets
AVSession_ErrCode OH_AVSession_SetFavorite(OH_AVSession* avsession, bool favorite)
```

**描述**

设置收藏状态。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。bool favorite收藏状态，true表示收藏，false表示取消收藏。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：参数avsession为nullptr。

#### OH_AVSession_SetLoopMode()

```ets
AVSession_ErrCode OH_AVSession_SetLoopMode(OH_AVSession* avsession, AVSession_LoopMode loopMode)
```

**描述**

设置循环模式。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[AVSession_LoopMode](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__avsession_loopmode) loopMode循环模式。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数loopMode无效。

#### OH_AVSession_RegisterCommandCallback()

```ets
AVSession_ErrCode OH_AVSession_RegisterCommandCallback(OH_AVSession* avsession,AVSession_ControlCommand command, OH_AVSessionCallback_OnCommand callback, void* userData)
```

**描述**

注册通用播控的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[AVSession_ControlCommand](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__avsession_controlcommand) command播控的控制命令。[OH_AVSessionCallback_OnCommand](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_oncommand) callback控制命令的回调。void* userData指向通过回调函数传递的应用数据指针。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_CODE_COMMAND_INVALID：控制命令无效。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_UnregisterCommandCallback()

```ets
AVSession_ErrCode OH_AVSession_UnregisterCommandCallback(OH_AVSession* avsession,AVSession_ControlCommand command, OH_AVSessionCallback_OnCommand callback)
```

**描述**

取消注册通用播控的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[AVSession_ControlCommand](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__avsession_controlcommand) command播控的控制命令。[OH_AVSessionCallback_OnCommand](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_oncommand) callback控制命令的回调。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_CODE_COMMAND_INVALID：控制命令无效。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_RegisterForwardCallback()

```ets
AVSession_ErrCode OH_AVSession_RegisterForwardCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnFastForward callback, void* userData)
```

**描述**

注册快进的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVSessionCallback_OnFastForward](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onfastforward) callback快进命令的回调。void* userData指向通过回调函数传递的应用数据指针。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_UnregisterForwardCallback()

```ets
AVSession_ErrCode OH_AVSession_UnregisterForwardCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnFastForward callback)
```

**描述**

取消注册快进的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVSessionCallback_OnFastForward](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onfastforward) callback快进命令的回调。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_RegisterRewindCallback()

```ets
AVSession_ErrCode OH_AVSession_RegisterRewindCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnRewind callback, void* userData)
```

**描述**

注册快退的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVSessionCallback_OnRewind](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onrewind) callback快退命令的回调。void* userData指向通过回调函数传递的应用数据指针。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_UnregisterRewindCallback()

```ets
AVSession_ErrCode OH_AVSession_UnregisterRewindCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnRewind callback)
```

**描述**

取消注册快退的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVSessionCallback_OnRewind](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onrewind) callback快退命令的回调。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_RegisterSeekCallback()

```ets
AVSession_ErrCode OH_AVSession_RegisterSeekCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnSeek callback, void* userData)
```

**描述**

注册跳转的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVSessionCallback_OnSeek](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onseek) callback跳转命令的回调。void* userData指向通过回调函数传递的应用数据指针。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_UnregisterSeekCallback()

```ets
AVSession_ErrCode OH_AVSession_UnregisterSeekCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnSeek callback)
```

**描述**

取消注册跳转的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVSessionCallback_OnSeek](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onseek) callback跳转命令的回调。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_RegisterSetLoopModeCallback()

```ets
AVSession_ErrCode OH_AVSession_RegisterSetLoopModeCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnSetLoopMode callback, void* userData)
```

**描述**

注册设置循环模式的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVSessionCallback_OnSetLoopMode](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onsetloopmode) callback设置循环模式命令的回调。void* userData指向通过回调函数传递的应用数据指针。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_UnregisterSetLoopModeCallback()

```ets
AVSession_ErrCode OH_AVSession_UnregisterSetLoopModeCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnSetLoopMode callback)
```

**描述**

取消注册设置循环模式的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVSessionCallback_OnSetLoopMode](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_onsetloopmode) callback设置循环模式命令的回调。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_RegisterToggleFavoriteCallback()

```ets
AVSession_ErrCode OH_AVSession_RegisterToggleFavoriteCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnToggleFavorite callback, void* userData)
```

**描述**

设置收藏的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVSessionCallback_OnToggleFavorite](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_ontogglefavorite) callback设置收藏命令的回调。void* userData指向通过回调函数传递的应用数据指针。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。

#### OH_AVSession_UnregisterToggleFavoriteCallback()

```ets
AVSession_ErrCode OH_AVSession_UnregisterToggleFavoriteCallback(OH_AVSession* avsession,OH_AVSessionCallback_OnToggleFavorite callback)
```

**描述**

取消设置收藏的回调。

**起始版本：** 13

**参数：**

参数项描述[OH_AVSession](OH_AVSession.md)* avsession媒体会话对象。[OH_AVSessionCallback_OnToggleFavorite](native_avsession.h.md#ZH-CN_TOPIC_0000002529285761__oh_avsessioncallback_ontogglefavorite) callback设置收藏命令的回调。

**返回：**

类型说明[AVSession_ErrCode](native_avsession_errors.h.md#ZH-CN_TOPIC_0000002529445735__avsession_errcode)

AV_SESSION_ERR_SUCCESS：函数执行成功。

 AV_SESSION_ERR_SERVICE_EXCEPTION：会话服务异常。

 AV_SESSION_ERR_INVALID_PARAMETER：

 1.参数avsession为nullptr。

 2.参数callback为nullptr。