# native_avplaybackstate.h

**概述**

提供播放状态的定义。

引用文件： <multimedia/av_session/native_avplaybackstate.h>

库： libohavsession.so

系统能力： SystemCapability.Multimedia.AVSession.Core

起始版本： 23

相关模块： [OHAVSession](OHAVSession.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| AVSession_PlaybackPosition | AVSession_PlaybackPosition | 播放位置的定义。 |
| OH_AVSession_AVPlaybackState | OH_AVSession_AVPlaybackState | 播控播放状态的对象。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| AVSession_ErrCode OH_AVSession_GetPlaybackState(OH_AVSession_AVPlaybackState* playbackState, AVSession_PlaybackState* state) | 获取播放的状态。 |
| AVSession_ErrCode OH_AVSession_GetPlaybackPosition(OH_AVSession_AVPlaybackState* playbackState, AVSession_PlaybackPosition* position) | 获取播放状态的位置。 |
| AVSession_ErrCode OH_AVSession_GetPlaybackSpeed(OH_AVSession_AVPlaybackState* playbackState, int32_t* speed) | 获取播放状态的倍速。 |
| AVSession_ErrCode OH_AVSession_GetPlaybackVolume(OH_AVSession_AVPlaybackState* playbackState, int32_t* volume) | 获取播放状态的音量值。 |

**函数说明**

**OH_AVSession_GetPlaybackState()**

```ets
AVSession_ErrCode OH_AVSession_GetPlaybackState(OH_AVSession_AVPlaybackState* playbackState, AVSession_PlaybackState* state)
```

描述

获取播放的状态。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVPlaybackState* playbackState | 表示播放状态实例对象。 |
| AVSession_PlaybackState* state | 指针变量将返回播放状态值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_INVALID_PARAMETER 参数验证失败原因如下：  1. 参数playbackState为nullptr。  2. 参数state为nullptr。 |

**OH_AVSession_GetPlaybackPosition()**

```ets
AVSession_ErrCode OH_AVSession_GetPlaybackPosition(OH_AVSession_AVPlaybackState* playbackState, AVSession_PlaybackPosition* position)
```

描述

获取播放状态的位置。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVPlaybackState* playbackState | 表示播放状态实例对象。 |
| AVSession_PlaybackPosition* position | 指针变量将返回播放位置值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_INVALID_PARAMETER 参数验证失败原因如下：  1. 参数playbackState为nullptr。  2. 参数position为nullptr。 |

**OH_AVSession_GetPlaybackSpeed()**

```ets
AVSession_ErrCode OH_AVSession_GetPlaybackSpeed(OH_AVSession_AVPlaybackState* playbackState, int32_t* speed)
```

描述

获取播放状态的倍速。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVPlaybackState* playbackState | 表示播放状态实例对象。 |
| int32_t* speed | 指针变量将返回播放倍速值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_INVALID_PARAMETER 参数验证失败原因如下：  1. 参数playbackState为nullptr。  2. 参数speed为nullptr。 |

**OH_AVSession_GetPlaybackVolume()**

```ets
AVSession_ErrCode OH_AVSession_GetPlaybackVolume(OH_AVSession_AVPlaybackState* playbackState, int32_t* volume)
```

描述

获取播放状态的音量值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVSession_AVPlaybackState* playbackState | 表示播放状态实例对象。 |
| int32_t* volume | 指针变量将返回播放音量值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| AVSession_ErrCode | AV_SESSION_ERR_SUCCESS：函数执行成功。  AV_SESSION_ERR_INVALID_PARAMETER 参数验证失败原因如下：  1. 参数playbackState为nullptr。  2. 参数volume为nullptr。 |