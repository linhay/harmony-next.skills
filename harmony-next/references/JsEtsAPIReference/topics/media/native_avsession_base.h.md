# native_avsession_base.h

**概述**

声明avsession基本信息。

引用文件： <multimedia/av_session/native_avsession_base.h>

库： libohavsession.so

系统能力： SystemCapability.Multimedia.AVSession.Core

起始版本： 23

相关模块： [OHAVSession](OHAVSession.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| AVSession_Type | AVSession_Type | 会话类型枚举。 |
| AVSession_PlaybackState | AVSession_PlaybackState | 媒体播放状态的相关属性枚举。 |
| AVSession_LoopMode | AVSession_LoopMode | 定义媒体播放循环模式。 |
| AVSession_ControlCommand | AVSession_ControlCommand | 播控命令枚举。 |
| AVMetadata_SkipIntervals | AVMetadata_SkipIntervals | 定义快进或快退的时间间隔。 |
| AVMetadata_DisplayTag | AVMetadata_DisplayTag | 当前媒体资源的金标枚举，即应用媒体音源的特殊类型标识。 |
| AVSession_ConnectionState | AVSession_ConnectionState | 设备连接状态枚举。 |
| AVSession_AVCastCategory | AVSession_AVCastCategory | 表示不同播放场景的投播类别枚举。 |
| AVSession_DeviceType | AVSession_DeviceType | 设备类型枚举。 |
| AVSession_ProtocolType | AVSession_ProtocolType | 协议类型枚举。 |
| AVSession_AVCastControlCommandType | AVSession_AVCastControlCommandType | 命令类型枚举。 |
| AVSession_PlaybackSpeed | AVSession_PlaybackSpeed | 播放倍速类型枚举。 |
| AVSession_PlaybackFilter | AVSession_PlaybackFilter | 播放状态过滤器枚举。 |

**枚举类型说明**

**AVSession_Type**

```ets
enum AVSession_Type
```

描述

会话类型枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| SESSION_TYPE_AUDIO = 0 | 音频会话类型（指媒体类音频，如音乐）。 |
| SESSION_TYPE_VIDEO = 1 | 视频会话类型（指媒体类投屏视频）。 |
| SESSION_TYPE_VOICE_CALL = 2 | 音频通话会话类型（指人机交互相关的音频，如语音助手）。 |
| SESSION_TYPE_VIDEO_CALL = 3 | 视频通话会话类型（指视频电话）。 |
| SESSION_TYPE_PHOTO = 4 | 相片会话类型。 |

**AVSession_PlaybackState**

```ets
enum AVSession_PlaybackState
```

描述

媒体播放状态的相关属性枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| PLAYBACK_STATE_INITIAL = 0 | 初始状态。 |
| PLAYBACK_STATE_PREPARING = 1 | 准备播放状态。表示媒体资源还未处于可播放状态。 |
| PLAYBACK_STATE_PLAYING = 2 | 正在播放状态。 |
| PLAYBACK_STATE_PAUSED = 3 | 暂停播放状态。 |
| PLAYBACK_STATE_FAST_FORWARDING = 4 | 快进状态。 |
| PLAYBACK_STATE_REWINDED = 5 | 快退状态。 |
| PLAYBACK_STATE_STOPPED = 6 | 停止状态。 |
| PLAYBACK_STATE_COMPLETED = 7 | 播放完成状态。 |
| PLAYBACK_STATE_RELEASED = 8 | 释放状态。 |
| PLAYBACK_STATE_ERROR = 9 | 错误状态。 |
| PLAYBACK_STATE_IDLE = 10 | 空闲状态。 |
| PLAYBACK_STATE_BUFFERING = 11 | 缓冲状态。 |
| PLAYBACK_STATE_MAX = 12 | 最大状态（当状态值为12时，返回错误码401）。 |

**AVSession_LoopMode**

```ets
enum AVSession_LoopMode
```

描述

定义媒体播放循环模式。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| LOOP_MODE_SEQUENCE = 0 | 按顺序播放。 |
| LOOP_MODE_SINGLE = 1 | 单曲循环。 |
| LOOP_MODE_LIST = 2 | 按表单循环。 |
| LOOP_MODE_SHUFFLE = 3 | 随机播放。 |
| LOOP_MODE_CUSTOM = 4 | 自定义播放。 |

**AVSession_ControlCommand**

```ets
enum AVSession_ControlCommand
```

描述

播控命令枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| CONTROL_CMD_INVALID = -1 | 无效控制命令。 |
| CONTROL_CMD_PLAY = 0 | 播放命令。 |
| CONTROL_CMD_PAUSE = 1 | 暂停命令。 |
| CONTROL_CMD_STOP = 2 | 停止命令。 |
| CONTROL_CMD_PLAY_NEXT = 3 | 播放下一首命令。 |
| CONTROL_CMD_PLAY_PREVIOUS = 4 | 播放上一首命令。 |

**AVMetadata_SkipIntervals**

```ets
enum AVMetadata_SkipIntervals
```

描述

定义快进或快退的时间间隔。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| SECONDS_10 = 10 | 时间间隔为10秒。 |
| SECONDS_15 = 15 | 时间间隔为15秒。 |
| SECONDS_30 = 30 | 时间间隔为30秒。 |

**AVMetadata_DisplayTag**

```ets
enum AVMetadata_DisplayTag
```

描述

当前媒体资源的金标枚举，即应用媒体音源的特殊类型标识。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| AVSESSION_DISPLAYTAG_AUDIO_VIVID = 1 | 高清音频。 |

**AVSession_ConnectionState**

```ets
enum AVSession_ConnectionState
```

描述

设备连接状态枚举。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| STATE_CONNECTING = 0 | 表示设备正处于连接状态。 |
| STATE_CONNECTED = 1 | 表示设备处于已连接状态。 |
| STATE_DISCONNECTED = 6 | 表示设备已处于断开默认连接的状态。 |

**AVSession_AVCastCategory**

```ets
enum AVSession_AVCastCategory
```

描述

表示不同播放场景的投播类别枚举。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| CATEGORY_LOCAL = 0 | 默认投播类别是本地。默认投屏类型为本地。媒体本地路由支持内置扬声器、音频插孔、A2DP（Advanced Audio Distribution Profile）设备。 |
| CATEGORY_REMOTE = 1 | 远程类别。表示媒体正在远程设备上展示，应用需要一个OH_AVCastController来控制远程播放。 |

**AVSession_DeviceType**

```ets
enum AVSession_DeviceType
```

描述

设备类型枚举。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| DEVICE_TYPE_LOCAL = 0 | 一种设备类型，标识音频路由为设备自身的内置扬声器或音频插孔。 |
| DEVICE_TYPE_TV = 2 | 一种设备类型，标识音频路由为电视端。 |
| DEVICE_TYPE_SMART_SPEAKER = 3 | 一种设备类型，标识音频路由为智能音箱端。 |
| DEVICE_TYPE_BLUETOOTH = 10 | 一种设备类型，标识音频路由为蓝牙设备端。 |

**AVSession_ProtocolType**

```ets
enum AVSession_ProtocolType
```

描述

协议类型枚举。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| TYPE_LOCAL = 0 | 默认为本地设备。包括设备本身的内置扬声器或音频插孔，A2DP（Advanced Audio Distribution Profile）设备。 |
| TYPE_CAST_PLUS_STREAM = 2 | Cast+的Stream模式。表示媒体正在其他设备上展示，应用需要一个AVCastController来控制远程播放。 |
| TYPE_DLNA = 4 | DLNA（DIGITAL LIVING NETWORK ALLIANCE）协议。表示设备支持DLNA协议，应用需要一个AVCastController来控制远程播放。 |
| TYPE_CAST_PLUS_AUDIO = 8 | 表示该设备支持高清晰度的音频投播，以获得更好的音质。 |

**AVSession_AVCastControlCommandType**

```ets
enum AVSession_AVCastControlCommandType
```

描述

命令类型枚举。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| CAST_CONTROL_CMD_PLAY = 0 | 播放命令。 |
| CAST_CONTROL_CMD_PAUSE = 1 | 暂停命令。 |
| CAST_CONTROL_CMD_STOP = 2 | 停止命令。 |
| CAST_CONTROL_CMD_PLAY_NEXT = 3 | 下一首命令。 |
| CAST_CONTROL_CMD_PLAY_PREVIOUS = 4 | 上一首命令。 |
| CAST_CONTROL_CMD_FAST_FORWARD = 5 | 快进命令。 |
| CAST_CONTROL_CMD_REWIND = 6 | 快退命令。 |
| CAST_CONTROL_CMD_SEEK = 7 | 跳转某一节点命令。 |
| CAST_CONTROL_CMD_SET_VOLUME = 8 | 设置音量命令。 |
| CAST_CONTROL_CMD_SET_SPEED = 9 | 设置播放倍速命令。 |

**AVSession_PlaybackSpeed**

```ets
enum AVSession_PlaybackSpeed
```

描述

播放倍速类型枚举。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| SPEED_FORWARD_0_75_X = 0 | 以正常播速的0.75倍速播放视频。 |
| SPEED_FORWARD_1_00_X = 1 | 以正常播速（1.00x）播放视频。 |
| SPEED_FORWARD_1_25_X = 2 | 以正常播速的1.25倍速播放视频。 |
| SPEED_FORWARD_1_75_X = 3 | 以正常播速的1.75倍速播放视频。 |
| SPEED_FORWARD_2_00_X = 4 | 以正常播速的2倍速播放视频。 |
| SPEED_FORWARD_0_50_X = 5 | 以正常播速的0.5倍速播放视频。 |
| SPEED_FORWARD_1_50_X = 6 | 以正常播速的1.5倍速播放视频。 |

**AVSession_PlaybackFilter**

```ets
enum AVSession_PlaybackFilter
```

描述

播放状态过滤器枚举。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| FILTER_STATE = 1 << 0 | 过滤出状态。 |
| FILTER_POSITION = 1 << 1 | 过滤出位置。 |
| FILTER_SPEED = 1 << 2 | 过滤出倍速。 |
| FILTER_VOLUME = 1 << 3 | 过滤出音量。 |