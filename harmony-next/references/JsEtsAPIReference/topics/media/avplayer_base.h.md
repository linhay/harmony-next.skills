# avplayer_base.h

**概述**

定义AVPlayer的结构体和枚举。

引用文件： <multimedia/player_framework/avplayer_base.h>

库： libavplayer.so

系统能力： SystemCapability.Multimedia.Media.AVPlayer

起始版本： 11

相关模块： [AVPlayer](AVPlayer.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| AVPlayerCallback | AVPlayerCallback | 包含了OH_AVPlayerOnInfo和OH_AVPlayerOnInfo回调函数指针的集合。应用需注册此结构体到OH_AVPlayer实例中，并处理回调上报的信息，保证AVPlayer的正常运行。(API12废弃) |
| OH_AVPlayer | OH_AVPlayer | 初始化AVPlayer。 |
| OH_AVSeiMessageArray | OH_AVSeiMessageArray | SEI消息数组。 |
| OH_AVPlaybackStrategy | OH_AVPlaybackStrategy | 音视频播放策略的结构体类型。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| AVPlayerState | AVPlayerState | 播放状态。 |
| AVPlayerSeekMode | AVPlayerSeekMode | 跳转模式。 |
| AVPlaybackSpeed | AVPlaybackSpeed | 播放速度。 |
| AVPlayerOnInfoType | AVPlayerOnInfoType | OnInfo类型。  可用于OH_AVPlayerOnInfoCallback和OH_AVPlayerOnInfo(已废弃)，用于表示收到的播放器信息类型。  从API 12开始，推荐用户使用OH_AVPlayerOnInfoCallback。不同的OnInfo类型，可获取到不同信息（infoBody），infoBody中包含key-value关系表，详见下述枚举值表。  使用API 11版本的开发者，需要使用旧接口。针对已废弃接口OH_AVPlayerOnInfo中使用的对应关系，可直接参考OH_AVPlayerOnInfo的API说明。 |
| AVPlayerBufferingType | AVPlayerBufferingType | 播放缓冲消息类型定义。 |
| AVPlayerTrackSwitchMode | AVPlayerTrackSwitchMode | 枚举轨道切换模式。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_AVPlayerOnInfo)(OH_AVPlayer *player, AVPlayerOnInfoType type, int32_t extra) | OH_AVPlayerOnInfo | 收到播放器消息时调用。(API12废弃) |
| typedef void (*OH_AVPlayerOnInfoCallback)(OH_AVPlayer player, AVPlayerOnInfoType type, OH_AVFormat infoBody, void *userData) | OH_AVPlayerOnInfoCallback | 收到播放器消息时被调用。如果应用成功设置该回调，则不会回调OH_AVPlayerOnInfo函数。 |
| typedef void (*OH_AVPlayerOnError)(OH_AVPlayer *player, int32_t errorCode, const char *errorMsg) | OH_AVPlayerOnError | 在API9以上的版本发生错误时调用。(API12废弃) |
| typedef void (*OH_AVPlayerOnErrorCallback)(OH_AVPlayer *player, int32_t errorCode, const char *errorMsg, void *userData) | OH_AVPlayerOnErrorCallback | 发生错误时被调用。如果应用成功设置该回调，则不会调用OH_AVPlayerOnError函数。 |
| typedef void (*OH_AVPlayerOnAmplitudeUpdateCallback)(OH_AVPlayer *player, double *amplitudes, uint32_t size, void *userData) | OH_AVPlayerOnAmplitudeUpdateCallback | 当计算出最大音频电平值时调用。 |
| typedef void (*OH_AVPlayerOnSeiMessageReceivedCallback)(OH_AVPlayer *player, OH_AVSeiMessageArray *message, int32_t playbackPosition, void *userData) | OH_AVPlayerOnSeiMessageReceivedCallback | 用于获取SEI消息的回调处理函数。在订阅SEI消息事件时使用，回调返回详细的SEI信息。 |

**变量**

| 名称 | 描述 |
| --- | --- |
| const char * OH_PLAYER_STATE | 获取播放状态的关键字，对应值类型是int32_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_STATE_CHANGE_REASON | 获取播放状态变更原因的关键字，对应值类型是int32_t。  1：用户操作触发；2：系统变更触发。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_VOLUME | 获取音量的关键字，对应值类型是float。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_BITRATE_ARRAY | 获取比特率列表的关键字，对应值类型是uint8_t字节数组。通过该关键字获取信息时：  需要先使用uint8_t类型指针变量保存比特率列表，使用size_t类型变量保存字节数组长度。  然后分配若干个uint32_t类型的存储空间，接收将uint8_t字节数组转换为uint32_t类型比特率整数值。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_AUDIO_INTERRUPT_TYPE | 获取音频打断类型的关键字，对应值类型是int32_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_AUDIO_INTERRUPT_FORCE | 获取音频打断FORCE类型的关键字，对应值类型是int32_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_AUDIO_INTERRUPT_HINT | 获取音频打断HINT类型的关键字，对应值类型是int32_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_AUDIO_DEVICE_CHANGE_REASON | 获取音频设备变更原因的关键字，对应值类型是int32_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_BUFFERING_TYPE | 获取缓冲更新消息类型的关键字，对应值类型是AVPlayerBufferingType。  通过该关键字获取信息时，需要先使用int32_t类型变量保存结果，再转换为AVPlayerBufferingType类型。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_BUFFERING_VALUE | 获取缓冲更新消息数值的关键字，对应值类型是int32_t，参见AVPlayerBufferingType。  当缓冲更新消息类型是AVPLAYER_BUFFERING_PERCENT、AVPLAYER_BUFFERING_CACHED_DURATION时有效。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_SEEK_POSITION | 获取Seek后播放进度的关键字，对应值类型是int32_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_PLAYBACK_SPEED | 获取播放倍速信息的关键字, 对应值类型是AVPlaybackSpeed。  通过该关键字获取信息时，需要先使用int32_t类型变量保存结果，再转换为AVPlaybackSpeed类型。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_PLAYBACK_RATE | 获取有效播放速率的关键字，对应值类型是浮点数。 起始版本： 20 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_BITRATE | 获取比特率信息的关键字，对应值类型是uint32_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_CURRENT_POSITION | 获取播放进度信息的关键字，对应值类型是int32_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_DURATION | 获取媒体资源时长信息的关键字，对应值类型是int64_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_VIDEO_WIDTH | 获取视频宽度信息的关键字，对应值类型是int32_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_VIDEO_HEIGHT | 获取视频高度信息的关键字，对应值类型是int32_t。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_MESSAGE_TYPE | 获取播放器消息信息的关键字，对应值类型是int32_t。  1：视频帧开始渲染。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_IS_LIVE_STREAM | 获取媒体资源是否为直播类型信息的关键字，对应值类型是int32_t。  1：直播。 起始版本： 12 系统能力： SystemCapability.Multimedia.Media.AVPlayer |
| const char * OH_PLAYER_MD_KEY_HAS_VIDEO | 获取媒体资源是否包含视频轨信息的关键字，对应值类型int32_t。  1：包含视频轨，0：不包含视频轨。 起始版本： 22 |
| const char * OH_PLAYER_MD_KEY_HAS_AUDIO | 获取媒体资源是否包含音频轨信息的关键字，对应值类型int32_t。  1：包含音频轨，0：不包含音频轨。 起始版本： 22 |
| const char * OH_PLAYER_MD_KEY_HAS_SUBTITLE | 获取媒体资源是否包含字幕轨信息的关键字，对应值类型int32_t。  1：包含字幕轨，0：不包含字幕轨。 起始版本： 22 |
| const char * OH_PLAYER_MD_KEY_TRACK_INDEX | 获取媒体资源轨道下标信息的关键字，对应值类型int32_t。 起始版本： 22 |
| const char * OH_PLAYER_SEI_PAYLOAD_TYPE | SEI 消息中表示负载类型的关键字。 起始版本： 23 |
| const char * OH_PLAYER_SEI_PAYLOAD_CONTENT | SEI 消息中表示负载内容的关键字。 起始版本： 23 |
| const char * OH_PLAYER_SUPER_RESOLUTION_ENABLE_STATE | 超分辨率功能启用状态关键字，值类型为int32_t。值为1表示已启用，0表示未启用；用于超分辨率状态变化时的信息回调。 起始版本： 23 |
| const char * OH_PLAYER_TRACH_CHANGE_INFO_TRACK_INDEX | 轨道切换信息中表示轨道索引的关键字，值类型为int32_t。 起始版本： 23 |
| const char * OH_PLAYER_TRACH_CHANGE_INFO_TRACK_SELECTED | 轨道切换信息中表示轨道是否被选中的标志关键字，值类型为int32_t。 起始版本： 23 |
| const char * OH_PLAYER_SUBTITLE_UPDATE_INFO_DURATION | 字幕更新信息中表示持续时间的关键字，值类型为int32_t。 起始版本： 23 |
| const char * OH_PLAYER_SUBTITLE_UPDATE_INFO_START_TIME | 字幕更新信息中表示起始时间的关键字，值类型为int32_t。 起始版本： 23 |
| const char * OH_PLAYER_SUBTITLE_UPDATE_INFO_TEXT | 字幕更新信息中表示字幕文本内容的关键字，值类型为字符串（string）。 起始版本： 23 |
| const char * OH_PLAYER_SERVER_IP_ADDRESS | 播放信息中表示服务器IP地址的关键字。 起始版本： 23 |
| const char * OH_PLAYER_IS_DOWNLOADING | 播放信息中表示当前是否处于下载状态的关键字。 起始版本： 23 |
| const char * OH_PLAYER_BUFFER_DURATION | 播放信息中表示缓冲区时长的关键字。 起始版本： 23 |
| const char * OH_PLAYER_DOWNLOAD_RATE | 播放信息中表示当前下载速率的关键字，下载速率的单位为比特率（bps）。 起始版本： 23 |
| const char * OH_PLAYER_AVG_DOWNLOAD_RATE | 播放信息中表示平均下载速率的关键字，下载速率的单位为比特率（bps）。 起始版本： 23 |
| const char * OH_MEDIA_EVENT_INFO_PREPARE_DURATION | 获取统计指标信息中的准备时长的关键字，对应值类型为uint32_t，单位为毫秒。 起始版本： 23 |
| const char * OH_MEDIA_EVENT_INFO_RESOURCE_CONNECTION_DURATION | 获取统计指标信息中的资源链接建立时长的关键字，对应值类型为uint32_t，单位为毫秒。 起始版本： 23 |
| const char * OH_MEDIA_EVENT_INFO_FIRST_FRAME_DECAPSULATION_DURATION | 获取统计指标信息中的首帧解封装时长的关键字，对应值类型为uint32_t，单位为毫秒。 起始版本： 23 |
| const char * OH_MEDIA_EVENT_INFO_TOTAL_PLAYING_TIME | 获取统计指标信息中的累计播放时长的关键字，对应值类型为uint32_t，单位为毫秒。 起始版本： 23 |
| const char * OH_MEDIA_EVENT_INFO_DOWNLOAD_REQUEST_COUNT | 获取统计指标信息中的媒体资源加载请求累计次数的关键字，对应值类型为uint32_t。 起始版本： 23 |
| const char * OH_MEDIA_EVENT_INFO_DOWNLOAD_TOTAL_TIME | 获取统计指标信息中的媒体资源加载总时长的关键字，对应值类型为uint32_t，单位为毫秒。 起始版本： 23 |
| const char * OH_MEDIA_EVENT_INFO_DOWNLOAD_TOTAL_SIZE | 获取统计指标信息中的已加载媒体资源累计字节数的关键字，对应值类型为int64_t。 起始版本： 23 |
| const char * OH_MEDIA_EVENT_INFO_STALLING_COUNT | 获取统计指标信息中的累计卡顿次数的关键字，对应值类型为uint32_t。 起始版本： 23 |
| const char * OH_MEDIA_EVENT_INFO_TOTAL_STALLING_TIME | 获取统计指标信息中的累计卡顿时长的关键字，对应值类型为uint32_t，单位为毫秒。 起始版本： 23 |

**枚举类型说明**

**AVPlayerState**

```ets
enum AVPlayerState
```

描述

播放状态。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| AV_IDLE = 0 | 空闲 |
| AV_INITIALIZED = 1 | 初始化 |
| AV_PREPARED = 2 | 准备 |
| AV_PLAYING = 3 | 播放 |
| AV_PAUSED = 4 | 暂停 |
| AV_STOPPED = 5 | 停止 |
| AV_COMPLETED = 6 | 结束 |
| AV_RELEASED = 7 | 释放 |
| AV_ERROR = 8 | 错误 |

**AVPlayerSeekMode**

```ets
enum AVPlayerSeekMode
```

描述

跳转模式。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| AV_SEEK_NEXT_SYNC = 0 | 同步到时间点之后的关键帧。 |
| AV_SEEK_PREVIOUS_SYNC | 同步到时间点之前的关键帧。 |
| AV_SEEK_CLOSEST = 2 | 同步到距离指定时间点最近的帧。 起始版本： 12 |
| AV_SEEK_CONTINUOUS = 3 | 连续拖动模式下的跳转（seek）。该模式可提供更流畅的拖拽体验，但要求设备支持对当前流执行连续跳转。在调用连续跳转前，请先检查是否支持，参见OH_AVPlayer_IsSeekContinuousSupported。 起始版本： 23 |

**AVPlaybackSpeed**

```ets
enum AVPlaybackSpeed
```

描述

播放速度。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| AV_SPEED_FORWARD_0_75_X | 0.75倍速播放。 |
| AV_SPEED_FORWARD_1_00_X | 正常播放。 |
| AV_SPEED_FORWARD_1_25_X | 1.25倍速播放。 |
| AV_SPEED_FORWARD_1_75_X | 1.75倍速播放。 |
| AV_SPEED_FORWARD_2_00_X | 2.0倍速播放。 |
| AV_SPEED_FORWARD_0_50_X | 0.5倍速播放。 起始版本： 12 |
| AV_SPEED_FORWARD_1_50_X | 1.5倍速播放。 起始版本： 12 |
| AV_SPEED_FORWARD_3_00_X | 3.0倍速播放。 起始版本： 13 |
| AV_SPEED_FORWARD_0_25_X | 0.25倍速播放。 起始版本： 13 |
| AV_SPEED_FORWARD_0_125_X | 0.125倍速播放。 起始版本： 13 |

**AVPlayerOnInfoType**

```ets
enum AVPlayerOnInfoType
```

描述

OnInfo类型。

 可用于OH_AVPlayerOnInfoCallback和OH_AVPlayerOnInfo(已废弃)，用于表示收到的播放器信息类型。

 从API version 12开始，推荐用户使用[OH_AVPlayerOnInfoCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002553361969__oh_avplayeroninfocallback)。不同的OnInfo类型，可获取到不同信息（infoBody），infoBody中包含key-value关系表，详见下述枚举值表。

 使用API version 11版本的开发者，需要使用旧接口。针对已废弃接口OH_AVPlayerOnInfo中使用的对应关系，可直接参考[OH_AVPlayerOnInfo](avplayer_base.h.md#ZH-CN_TOPIC_0000002553361969__oh_avplayeroninfo)的API说明。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| AV_INFO_TYPE_SEEKDONE = 0 | 跳转到对应播放位置时返回消息。  key为OH_PLAYER_SEEK_POSITION：取值类型int32_t。系统通过int32_t传递value，应用需通过int32_t获取。 |
| AV_INFO_TYPE_SPEEDDONE = 1 | 播放倍速设置完成时返回消息。  key为OH_PLAYER_PLAYBACK_SPEED：取值类型AVPlaybackSpeed。系统通过int32_t传递value，应用需先通过int32_t获取，再强制转为AVPlaybackSpeed。 |
| AV_INFO_TYPE_BITRATEDONE = 2 | 比特率设置完成时返回消息。  key为OH_PLAYER_BITRATE：取值类型uint32_t。系统通过int32_t传递value，应用需先通过int32_t获取，再强制为uint32_t。 |
| AV_INFO_TYPE_EOS = 3 | 播放完成时返回消息。 |
| AV_INFO_TYPE_STATE_CHANGE = 4 | 状态改变时返回消息。  key为OH_PLAYER_STATE：取值类型int32_t。系统通过int32_t传递value，应用需先通过int32_t获取，再强制转为AVPlayerState。  key为OH_PLAYER_STATE_CHANGE_REASON：取值类型int32_t。系统通过int32_t传递value，应用需通过int32_t获取。1：用户操作触发；2：系统变更触发。 |
| AV_INFO_TYPE_POSITION_UPDATE = 5 | 返回当前播放位置。  key为OH_PLAYER_CURRENT_POSITION：取值类型int32_t。系统通过int32_t传递value，应用需通过int32_t获取。 |
| AV_INFO_TYPE_MESSAGE = 6 | 视频开始渲染时返回消息。  key为OH_PLAYER_MESSAGE_TYPE：取值类型int32_t。系统通过int32_t传递value，应用需通过int32_t获取。1表示视频开始渲染。 |
| AV_INFO_TYPE_VOLUME_CHANGE = 7 | 音量改变时返回消息。  key为OH_PLAYER_VOLUME：取值类型float。系统通过float传递value，应用需通过float获取。取值范围[0.0, 1.0]。 |
| AV_INFO_TYPE_RESOLUTION_CHANGE = 8 | 首次获取视频大小或视频大小更新时返回消息。  key为OH_PLAYER_VIDEO_WIDTH 或 OH_PLAYER_VIDEO_HEIGHT：取值类型int32_t。系统通过int32_t传递value，应用需通过int32_t获取。 |
| AV_INFO_TYPE_BUFFERING_UPDATE = 9 | 返回多队列缓冲时间。  key为OH_PLAYER_BUFFERING_TYPE：取值类型AVPlayerBufferingType。系统通过int32_t传递value，应用需先通过int32_t获取，再强制转为AVPlayerBufferingType。  key为OH_PLAYER_BUFFERING_VALUE：取值类型int32_t。系统通过int32_t传递value，应用需通过int32_t获取。  当缓冲更新消息类型是AVPLAYER_BUFFERING_PERCENT、AVPLAYER_BUFFERING_CACHED_DURATION时有效，分别表示缓冲进度完成百分比、缓冲数据可播放时长。 |
| AV_INFO_TYPE_BITRATE_COLLECT = 10 | 上报HLS视频比特率列表消息。  key为OH_PLAYER_BITRATE_ARRAY：取值类型uint8_t字节数组。应用需要先使用uint8_t类型指针变量保存比特率列表，使用size_t类型变量保存字节数组长度。然后分配若干个uint32_t类型的存储空间，接收将uint8_t字节数组转换为uint32_t类型比特率整数值。 |
| AV_INFO_TYPE_INTERRUPT_EVENT = 11 | 音频焦点改变时返回消息。  取值类型int32_t。系统通过int32_t传递value，应用需通过int32_t获取。  key为：  OH_PLAYER_AUDIO_INTERRUPT_TYPE：取值1表示中断事件开始；2表示结束。  OH_PLAYER_AUDIO_INTERRUPT_FORCE：取值0表示强制打断，系统改变音频播放状态；1表示共享打断，应用改变音频播放状态。  OH_PLAYER_AUDIO_INTERRUPT_HINT：取值0表示NONE，无提示；1表示RESUME，提示音频恢复；2表示PAUSE，提示音频暂停暂时失去焦点；3表示STOP，提示音频停止；4表示DUCK，音频降低音量；5表示UNDUCK，音频恢复音量。 |
| AV_INFO_TYPE_DURATION_UPDATE = 12 | 返回播放时长。  key为OH_PLAYER_DURATION：取值类型int64_t。系统通过int64_t传递value，应用需通过int64_t获取。 |
| AV_INFO_TYPE_IS_LIVE_STREAM = 13 | 播放为直播流时返回消息。 key为OH_PLAYER_IS_LIVE_STREAM：取值类型int32_t。系统通过int32_t传递value，应用需通过int32_t获取。0表示非直播流，1表示直播流。 |
| AV_INFO_TYPE_TRACKCHANGE = 14 | 轨道改变时返回消息。 |
| AV_INFO_TYPE_TRACK_INFO_UPDATE = 15 | 轨道更新时返回消息。 |
| AV_INFO_TYPE_SUBTITLE_UPDATE = 16 | 字幕信息更新时返回消息。 |
| AV_INFO_TYPE_AUDIO_OUTPUT_DEVICE_CHANGE = 17 | 音频输出设备改变时返回消息。  key为OH_PLAYER_AUDIO_DEVICE_CHANGE_REASON：取值类型int32_t。系统通过int32_t传递value，应用需通过int32_t获取。 |
| AV_INFO_TYPE_PLAYBACK_RATE_DONE = 18 | 播放速率成功应用时返回消息。  key为OH_PLAYER_PLAYBACK_RATE：取值类型float。系统通过float传递value，应用通过float获取。 起始版本： 20 |
| AV_INFO_TYPE_SUPER_RESOLUTION_CHANGED = 19 | 超分辨率变化时返回消息。 起始版本： 23 |

**AVPlayerBufferingType**

```ets
enum AVPlayerBufferingType
```

描述

播放缓冲消息类型定义。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| AVPLAYER_BUFFERING_START = 1 | 缓冲开始消息。 |
| AVPLAYER_BUFFERING_END | 缓冲结束消息。 |
| AVPLAYER_BUFFERING_PERCENT | 缓冲执行进度百分比，取值范围：整数，[0, 100]。 |
| AVPLAYER_BUFFERING_CACHED_DURATION | 缓冲数据可播放时长，单位：毫秒。 |

**AVPlayerTrackSwitchMode**

```ets
enum AVPlayerTrackSwitchMode
```

描述

枚举轨道切换模式。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| AV_TRACK_SWITCH_MODE_SMOOTH = 0 | 平滑切换轨道。 |
| AV_TRACK_SWITCH_MODE_SEGMENT = 1 | 按片段切换轨道。 |
| AV_TRACK_SWITCH_MODE_CLOSEST = 2 | 切换到最接近的轨道。 |

**函数说明**

**OH_AVPlayerOnInfo()**

```ets
typedef void (*OH_AVPlayerOnInfo)(OH_AVPlayer *player, AVPlayerOnInfoType type, int32_t extra)
```

描述

收到播放器消息时调用。

信息类型（type）和信息（extra）的对应关系如表所示。

| 信息类型（type） | 对应的extra描述 |
| --- | --- |
| AV_INFO_TYPE_SEEKDONE | 跳转到对应播放位置时返回消息，extra表示跳转到的位置。 |
| AV_INFO_TYPE_SPEEDDONE | 播放倍速设置完成时返回消息，extra表示播放倍速信息，具体请参考AVPlaybackSpeed。 |
| AV_INFO_TYPE_BITRATEDONE | 比特率设置完成时返回消息，extra表示比特率信息。 |
| AV_INFO_TYPE_EOS | 播放完成时返回消息。 |
| AV_INFO_TYPE_STATE_CHANGE | 状态改变时返回消息，extra表示当前播放状态，具体请参见AVPlayerState。 |
| AV_INFO_TYPE_POSITION_UPDATE | 返回当前播放位置，extra表示当前位置。 |
| AV_INFO_TYPE_MESSAGE | 视频开始渲染时返回消息，extra表示视频首帧渲染。 |
| AV_INFO_TYPE_VOLUME_CHANGE | 音量改变时返回消息，此场景下extra未定义。 |
| AV_INFO_TYPE_RESOLUTION_CHANGE | 首次获取视频大小或视频大小更新时返回消息，此场景下extra未定义。 |
| AV_INFO_TYPE_BUFFERING_UPDATE | 返回多队列缓冲时间，extra表示视频时长。 |
| AV_INFO_TYPE_BITRATE_COLLECT | 上报HLS视频比特率列表消息。上报时每个比特率已经转化为uint8_t字节数组，使用者需要将uint8_t字节数组强制转换为uint32_t整型数组。 |
| AV_INFO_TYPE_INTERRUPT_EVENT | 音频焦点改变时返回消息，extra表示音频打断提示，具体请参见OH_AudioInterrupt_Hint，应用可决定是否根据打断提示作进一步处理。 |
| AV_INFO_TYPE_DURATION_UPDATE | 返回播放时长，extra表示视频时长。 |
| AV_INFO_TYPE_IS_LIVE_STREAM | 播放为直播流时返回消息，extra表示是否为直播流，0表示非直播流，1表示直播流。 |
| AV_INFO_TYPE_TRACKCHANGE | 轨道改变时返回消息，此场景extra未定义。 |
| AV_INFO_TYPE_TRACK_INFO_UPDATE | 轨道更新时返回消息，此场景extra未定义。 |
| AV_INFO_TYPE_SUBTITLE_UPDATE | 字幕信息更新时返回消息，此场景extra未定义。 |
| AV_INFO_TYPE_AUDIO_OUTPUT_DEVICE_CHANGE | 音频输出设备改变时返回消息，extra表示设备改变原因，具体请参见OH_AudioStream_DeviceChangeReason。 |

系统能力： SystemCapability.Multimedia.Media.AVPlayer

起始版本： 11

废弃版本： 12

替代接口： [OH_AVPlayerOnInfoCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002553361969__oh_avplayeroninfocallback)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVPlayer *player | 指向OH_AVPlayer实例的指针。 |
| AVPlayerOnInfoType type | 信息类型。类型为AVPlayerOnInfoType，与extra的对应关系可见方法描述。 |
| int32_t extra | 其他信息，如播放文件的开始时间位置。 |

**OH_AVPlayerOnInfoCallback()**

```ets
typedef void (*OH_AVPlayerOnInfoCallback)(OH_AVPlayer *player, AVPlayerOnInfoType type, OH_AVFormat* infoBody, void *userData)
```

描述

收到播放器消息时被调用。如果应用成功设置该回调，则不会回调OH_AVPlayerOnInfo函数。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVPlayer *player | 指向OH_AVPlayer实例的指针。 |
| AVPlayerOnInfoType type | 信息类型。具体请参见AVPlayerOnInfoType。 |
| OH_AVFormat* infoBody | 指向携带具体消息的指针，仅在该回调方法内有效。 |
| void *userData | 指向应用调用者设置该回调函数时提供的实例的指针。 |

**OH_AVPlayerOnError()**

```ets
typedef void (*OH_AVPlayerOnError)(OH_AVPlayer *player, int32_t errorCode, const char *errorMsg)
```

描述

在API version 9以上的版本发生错误时调用。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

起始版本： 11

废弃版本： 12

替代接口： [OH_AVPlayerOnErrorCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002553361969__oh_avplayeronerrorcallback)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVPlayer *player | 指向OH_AVPlayer实例的指针。 |
| int32_t errorCode | 错误码。  AV_ERR_NO_MEMORY：无内存，取值为1。  AV_ERR_OPERATE_NOT_PERMIT：操作不允许，取值为2。  AV_ERR_INVALID_VAL：无效值，取值为3。  AV_ERR_IO：IO错误，取值为4。  AV_ERR_TIMEOUT：超时错误，取值为5。  AV_ERR_UNKNOWN：未知错误，取值为6。  AV_ERR_SERVICE_DIED：服务死亡，取值为7。  AV_ERR_INVALID_STATE：当前状态不支持此操作，取值为8。  AV_ERR_UNSUPPORT：未支持的接口，取值为9。  AV_ERR_EXTEND_START：扩展错误码初始值，取值为100。 |
| const char *errorMsg | 错误消息。 |

**OH_AVPlayerOnErrorCallback()**

```ets
typedef void (*OH_AVPlayerOnErrorCallback)(OH_AVPlayer *player, int32_t errorCode, const char *errorMsg, void *userData)
```

描述

发生错误时被调用。如果应用成功设置该回调，则不会调用OH_AVPlayerOnError函数。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVPlayer *player | 指向OH_AVPlayer实例的指针。 |
| int32_t errorCode | 错误码。  AV_ERR_NO_MEMORY：无内存，取值为1。  AV_ERR_OPERATE_NOT_PERMIT：操作不允许，取值为2。  AV_ERR_INVALID_VAL：无效值，取值为3。  AV_ERR_IO：IO错误。API version 12-13取值为4；API version 14及以后，对应错误细化为错误码5411001~5411011。  AV_ERR_TIMEOUT：超时错误，取值为5。  AV_ERR_UNKNOWN：未知错误，取值为6。  AV_ERR_SERVICE_DIED：服务死亡，取值为7。  AV_ERR_INVALID_STATE：当前状态不支持此操作，取值为8。  AV_ERR_UNSUPPORT：未支持的接口，取值为9。  AV_ERR_EXTEND_START：扩展错误码初始值，取值为100。 |
| const char *errorMsg | 错误消息。 |
| void *userData | 原样返回用户设置回调时传入的userData数据。 |

**OH_AVPlayerOnAmplitudeUpdateCallback()**

```ets
typedef void (*OH_AVPlayerOnAmplitudeUpdateCallback)(OH_AVPlayer *player, double *amplitudes, uint32_t size, void *userData)
```

描述

当计算出最大音频电平值时调用。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVPlayer *player | 指向OH_AVPlayer实例的指针。 |
| double *amplitudes | 指向最大音频电平值数组的指针。注意：最大音频电平值数组会在回调后自动释放，如有需要，用户需自行拷贝数据以供后续使用。 |
| uint32_t size | 最大音频电平值数组的大小。 |
| void *userData | 指向用户特定数据的指针。 |

**OH_AVPlayerOnSeiMessageReceivedCallback()**

```ets
typedef void (*OH_AVPlayerOnSeiMessageReceivedCallback)(OH_AVPlayer *player, OH_AVSeiMessageArray *message, int32_t playbackPosition, void *userData)
```

描述

用于获取SEI消息的回调处理函数。在订阅SEI消息事件时使用，回调返回详细的SEI信息。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVPlayer *player | 指向OH_AVPlayer实例的指针。 |
| OH_AVSeiMessageArray *message | SEI消息数组。注意：SEI消息数组会在回调后自动释放，如有需要，用户需自行拷贝数据以供后续使用。 |
| int32_t playbackPosition | 播放位置。 |
| void *userData | 指向用户特定数据的指针。 |