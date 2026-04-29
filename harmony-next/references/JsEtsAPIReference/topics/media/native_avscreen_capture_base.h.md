# native_avscreen_capture_base.h

**概述**

声明用于运行屏幕录制通用的结构体、字符常量、枚举。

引用文件： <multimedia/player_framework/native_avscreen_capture_base.h>

库： libnative_avscreen_capture.so

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

相关模块： [AVScreenCapture](AVScreenCapture.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioCaptureInfo | OH_AudioCaptureInfo | 音频采样信息。  当audioSampleRate和audioChannels同时为0时，忽略该类型音频相关参数，不录制该类型音频数据。 |
| OH_AudioEncInfo | OH_AudioEncInfo | 音频编码信息。 |
| OH_AudioInfo | OH_AudioInfo | 音频信息。  同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采样参数需要相同。 |
| OH_VideoCaptureInfo | OH_VideoCaptureInfo | 视频录制信息。当videoFrameWidth和videoFrameHeight同时为0时，忽略视频相关参数不录制屏幕数据。 |
| OH_VideoEncInfo | OH_VideoEncInfo | 视频编码参数。 |
| OH_VideoInfo | OH_VideoInfo | 视频信息。 |
| OH_RecorderInfo | OH_RecorderInfo | 录制文件信息。 |
| OH_AVScreenCaptureConfig | OH_AVScreenCaptureConfig | 屏幕录制配置参数。 |
| OH_AVScreenCaptureCallback | OH_AVScreenCaptureCallback | OH_AVScreenCapture中所有异步回调函数指针的集合。将该结构体的实例注册到OH_AVScreenCapture实例中，并处理回调上报的信息，以保证OH_AVScreenCapture的正常运行。  从API version 12开始，推荐使用接口OH_AVScreenCapture_OnError、OH_AVScreenCapture_OnBufferAvailable替代。 |
| OH_Rect | OH_Rect | 定义录屏界面的宽高以及画面信息。 |
| OH_AudioBuffer | OH_AudioBuffer | 定义了音频数据的大小、类型、时间戳等配置信息。 |
| OH_AVScreenCaptureHighlightConfig | OH_AVScreenCaptureHighlightConfig | 表示高亮边框的样式，包括高亮边框的模式、边框宽度和边框颜色。 |
| OH_NativeBuffer | OH_NativeBuffer | 提供录屏的视频原始码流类。 |
| OH_AVScreenCapture | OH_AVScreenCapture | 通过OH_AVScreenCapture可以获取视频与音频的原始码流。 |
| OH_AVScreenCapture_ContentFilter | OH_AVScreenCapture_ContentFilter | 通过OH_AVScreenCapture_ContentFilter过滤音视频内容。 |
| OH_AVScreenCapture_CaptureStrategy | OH_AVScreenCapture_CaptureStrategy | 通过OH_AVScreenCapture_CaptureStrategy设置录屏策略。 |
| OH_AVScreenCapture_UserSelectionInfo | OH_AVScreenCapture_UserSelectionInfo | 通过OH_AVScreenCapture_UserSelectionInfo获取用户在授权界面（选择界面）选择的参数。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_CaptureMode | OH_CaptureMode | 枚举，表示屏幕录制的不同模式。 |
| OH_AudioCaptureSourceType | OH_AudioCaptureSourceType | 枚举，表示屏幕录制时的音频源类型。 |
| OH_AudioCodecFormat | OH_AudioCodecFormat | 枚举，表示音频编码格式。 |
| OH_VideoCodecFormat | OH_VideoCodecFormat | 枚举，表示视频编码格式。 |
| OH_DataType | OH_DataType | 枚举，表示屏幕录制流的数据格式。 |
| OH_VideoSourceType | OH_VideoSourceType | 枚举，表示视频源格式。当前仅支持RGBA格式。 |
| OH_ContainerFormatType | OH_ContainerFormatType | 枚举，表示屏幕录制生成的文件类型。 |
| OH_AVScreenCaptureStateCode | OH_AVScreenCaptureStateCode | 枚举，表示状态码。 |
| OH_AVScreenCaptureBufferType | OH_AVScreenCaptureBufferType | 枚举，表示buffer类型。 |
| OH_AVScreenCaptureFilterableAudioContent | OH_AVScreenCaptureFilterableAudioContent | 枚举，表示可过滤的音频类型。 |
| OH_AVScreenCaptureContentChangedEvent | OH_AVScreenCaptureContentChangedEvent | 枚举，表示录屏内容变更事件。 |
| OH_AVScreenCapture_FillMode | OH_AVScreenCapture_FillMode | 图像填充模式。 |
| OH_ScreenCaptureHighlightMode | OH_ScreenCaptureHighlightMode | 枚举，表示屏幕录制高亮边框的模式。 |
| OH_CapturePickerMode | OH_CapturePickerMode | 枚举，表示Picker显示模式。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_AVScreenCaptureOnError)(OH_AVScreenCapture *capture, int32_t errorCode) | OH_AVScreenCaptureOnError | 当OH_AVScreenCapture实例运行出错时，将调用函数指针。  从API version 12开始，推荐使用接口OH_AVScreenCapture_OnError替代。 |
| typedef void (*OH_AVScreenCaptureOnAudioBufferAvailable)(OH_AVScreenCapture *capture, bool isReady, OH_AudioCaptureSourceType type) | OH_AVScreenCaptureOnAudioBufferAvailable | 当OH_AVScreenCapture实例操作期间音频缓存区可用时，将调用函数指针。  从API version 12开始，推荐使用接口OH_AVScreenCapture_OnBufferAvailable替代。 |
| typedef void (*OH_AVScreenCaptureOnVideoBufferAvailable)(OH_AVScreenCapture *capture, bool isReady) | OH_AVScreenCaptureOnVideoBufferAvailable | 当OH_AVScreenCapture实例操作期间视频缓存区可用时，将调用函数指针。  从API version 12开始，推荐使用接口OH_AVScreenCapture_OnBufferAvailable替代。 |
| typedef void (*OH_AVScreenCapture_OnStateChange)(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureStateCode stateCode, void *userData) | OH_AVScreenCapture_OnStateChange | 当OH_AVScreenCapture实例操作期间发生状态变更时，将调用函数指针。 |
| typedef void (*OH_AVScreenCapture_OnError)(OH_AVScreenCapture *capture, int32_t errorCode, void *userData) | OH_AVScreenCapture_OnError | 当OH_AVScreenCapture实例操作期间发生错误时，将调用函数指针。 |
| typedef void (*OH_AVScreenCapture_OnBufferAvailable)(OH_AVScreenCapture *capture, OH_AVBuffer *buffer, OH_AVScreenCaptureBufferType bufferType, int64_t timestamp, void *userData) | OH_AVScreenCapture_OnBufferAvailable | 当OH_AVScreenCapture实例操作期间音频或视频缓存区可用时，将调用该函数指针。 |
| typedef void (*OH_AVScreenCapture_OnDisplaySelected)(OH_AVScreenCapture *capture, uint64_t displayId, void *userData) | OH_AVScreenCapture_OnDisplaySelected | 当录屏事件开始时，将调用函数指针。 |
| typedef void (*OH_AVScreenCapture_OnCaptureContentChanged)(OH_AVScreenCapture* capture, OH_AVScreenCaptureContentChangedEvent event, OH_Rect* area, void *userData) | OH_AVScreenCapture_OnCaptureContentChanged | 当OH_AVScreenCapture实例操作期间录屏内容变化时，将调用函数指针。 |
| typedef void (*OH_AVScreenCapture_OnUserSelected)(OH_AVScreenCapture* capture, OH_AVScreenCapture_UserSelectionInfo* selections, void *userData) | OH_AVScreenCapture_OnUserSelected | 当用户在授权界面（选择界面）选择参数时，功能接口将参数返回给应用程序。 |

**枚举类型说明**

**OH_CaptureMode**

```ets
enum OH_CaptureMode
```

描述

枚举，表示屏幕录制的不同模式。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_CAPTURE_HOME_SCREEN = 0 | 录制主屏幕。 |
| OH_CAPTURE_SPECIFIED_SCREEN = 1 | 录制指定屏幕。 |
| OH_CAPTURE_SPECIFIED_WINDOW = 2 | 录制指定窗口。 |
| OH_CAPTURE_INVAILD = -1 | 无效模式。 |

**OH_AudioCaptureSourceType**

```ets
enum OH_AudioCaptureSourceType
```

描述

枚举，表示屏幕录制时的音频源类型。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_SOURCE_INVALID = -1 | 无效音频源。 |
| OH_SOURCE_DEFAULT = 0 | 默认音频源，默认为麦克风。 |
| OH_MIC = 1 | 麦克风录制的外部音频流。 |
| OH_ALL_PLAYBACK = 2 | 系统播放的所有内部音频流。 |
| OH_APP_PLAYBACK = 3 | 指定应用播放的内部音频流。 |

**OH_AudioCodecFormat**

```ets
enum OH_AudioCodecFormat
```

描述

枚举，表示音频编码格式。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_AUDIO_DEFAULT = 0 | 默认音频编码，默认为AAC_LC。 |
| OH_AAC_LC = 3 | AAC_LC音频编码。 |
| OH_AUDIO_CODEC_FORMAT_BUTT | 无效格式。 |

**OH_VideoCodecFormat**

```ets
enum OH_VideoCodecFormat
```

描述

枚举，表示视频编码格式。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_VIDEO_DEFAULT = 0 | 默认视频编码，默认为H.264。 |
| OH_H264 = 2 | H.264。 |
| OH_H265 = 4 | H.265/HEVC。 |
| OH_MPEG4 = 6 | MPEG4。 |
| OH_VP8 = 8 | VP8。 |
| OH_VP9 = 10 | VP9。 |
| OH_VIDEO_CODEC_FORMAT_BUTT | 无效格式。 |

**OH_DataType**

```ets
enum OH_DataType
```

描述

枚举，表示屏幕录制流的数据格式。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_ORIGINAL_STREAM = 0 | 原始流格式，如YUV/RGBA/PCM等。 |
| OH_ENCODED_STREAM = 1 | 编码格式，如H264/AAC等。当前版本暂不支持。 |
| OH_CAPTURE_FILE = 2 | 保存文件格式，支持mp4。 |
| OH_INVAILD = -1 | 无效格式。 |

**OH_VideoSourceType**

```ets
enum OH_VideoSourceType
```

描述

枚举，表示视频源格式。当前仅支持RGBA格式。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_VIDEO_SOURCE_SURFACE_YUV = 0 | YUV格式。当前版本暂不支持。 |
| OH_VIDEO_SOURCE_SURFACE_ES | raw格式。当前版本暂不支持。 |
| OH_VIDEO_SOURCE_SURFACE_RGBA | RGBA格式。 |
| OH_VIDEO_SOURCE_BUTT | 无效格式。 |

**OH_ContainerFormatType**

```ets
enum OH_ContainerFormatType
```

描述

枚举，表示屏幕录制生成的文件类型。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| CFT_MPEG_4A = 0 | 音频格式 m4a。 |
| CFT_MPEG_4 = 1 | 视频格式 mp4。 |

**OH_AVScreenCaptureStateCode**

```ets
enum OH_AVScreenCaptureStateCode
```

描述

枚举，表示状态码。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| OH_SCREEN_CAPTURE_STATE_STARTED = 0 | 已开始录屏。 |
| OH_SCREEN_CAPTURE_STATE_CANCELED = 1 | 已取消录屏。 |
| OH_SCREEN_CAPTURE_STATE_STOPPED_BY_USER = 2 | 已停止录屏。 |
| OH_SCREEN_CAPTURE_STATE_INTERRUPTED_BY_OTHER = 3 | 录屏被其他录屏中断。 |
| OH_SCREEN_CAPTURE_STATE_STOPPED_BY_CALL = 4 | 录屏被通话中断。 |
| OH_SCREEN_CAPTURE_STATE_MIC_UNAVAILABLE = 5 | 麦克风不可用。 |
| OH_SCREEN_CAPTURE_STATE_MIC_MUTED_BY_USER = 6 | 麦克风被静音。 |
| OH_SCREEN_CAPTURE_STATE_MIC_UNMUTED_BY_USER = 7 | 麦克风被取消静音。 |
| OH_SCREEN_CAPTURE_STATE_ENTER_PRIVATE_SCENE = 8 | 进入隐私界面。 |
| OH_SCREEN_CAPTURE_STATE_EXIT_PRIVATE_SCENE = 9 | 隐私界面退出。 |
| OH_SCREEN_CAPTURE_STATE_STOPPED_BY_USER_SWITCHES = 10 | 系统用户切换，录屏中断。 |

**OH_AVScreenCaptureBufferType**

```ets
enum OH_AVScreenCaptureBufferType
```

描述

枚举，表示buffer类型。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| OH_SCREEN_CAPTURE_BUFFERTYPE_VIDEO = 0 | 视频数据。 |
| OH_SCREEN_CAPTURE_BUFFERTYPE_AUDIO_INNER = 1 | 内录音频数据。 |
| OH_SCREEN_CAPTURE_BUFFERTYPE_AUDIO_MIC = 2 | 麦克风音频数据。 |

**OH_AVScreenCaptureFilterableAudioContent**

```ets
enum OH_AVScreenCaptureFilterableAudioContent
```

描述

枚举，表示可过滤的音频类型。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| OH_SCREEN_CAPTURE_NOTIFICATION_AUDIO = 0 | 通知音。 |
| OH_SCREEN_CAPTURE_CURRENT_APP_AUDIO = 1 | 应用自身声音。 |

**OH_AVScreenCaptureContentChangedEvent**

```ets
enum OH_AVScreenCaptureContentChangedEvent
```

描述

枚举，表示录屏内容变更事件。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| OH_SCREEN_CAPTURE_CONTENT_HIDE = 0 | 录屏内容变为隐藏。 |
| OH_SCREEN_CAPTURE_CONTENT_VISIBLE = 1 | 录屏内容变为可见。 |
| OH_SCREEN_CAPTURE_CONTENT_UNAVAILABLE = 2 | 录屏内容状态变化为不可用，如录屏窗口关闭。 |

**OH_AVScreenCapture_FillMode**

```ets
enum OH_AVScreenCapture_FillMode
```

描述

图像填充模式。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| OH_SCREENCAPTURE_FILLMODE_ASPECT_SCALE_FIT = 0 | 保持图像原始宽高比匹配目标图像大小，若比例不一致可能存在黑边。 |
| OH_SCREENCAPTURE_FILLMODE_SCALE_TO_FILL = 1 | 图像拉伸匹配目标图像大小，若比例不一致图像变形。 |

**OH_ScreenCaptureHighlightMode**

```ets
enum OH_ScreenCaptureHighlightMode
```

描述

枚举，表示屏幕录制高亮边框的模式。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| OH_HIGHLIGHT_MODE_CLOSED = 0 | 默认模式，用方形全包边框高亮显示录制区域。 |
| OH_HIGHLIGHT_MODE_CORNER_WRAP = 1 | 用四角包裹边框高亮显示录制区域。 |

**OH_CapturePickerMode**

```ets
enum OH_CapturePickerMode
```

描述

枚举，表示Picker显示模式。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| OH_CAPTURE_PICKER_MODE_WINDOW_ONLY = 0 | 仅显示窗口模式。 |
| OH_CAPTURE_PICKER_MODE_SCREEN_ONLY = 1 | 仅显示屏幕模式。 |
| OH_CAPTURE_PICKER_MODE_SCREEN_AND_WINDOW = 2 | 显示屏幕和窗口模式（默认模式）。 |

**函数说明**

**OH_AVScreenCaptureOnError()**

```ets
typedef void (*OH_AVScreenCaptureOnError)(OH_AVScreenCapture *capture, int32_t errorCode)
```

描述

当OH_AVScreenCapture实例运行出错时，将调用函数指针。

 从API version 12开始，推荐使用接口[OH_AVScreenCapture_OnError](#ZH-CN_TOPIC_0000002553202013__oh_avscreencapture_onerror)替代。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVScreenCapture *capture | 指向OH_AVScreenCapture实例的指针。 |
| int32_t errorCode | 指定错误码。 |

**OH_AVScreenCaptureOnAudioBufferAvailable()**

```ets
typedef void (*OH_AVScreenCaptureOnAudioBufferAvailable)(OH_AVScreenCapture *capture, bool isReady, OH_AudioCaptureSourceType type)
```

描述

当OH_AVScreenCapture实例操作期间音频缓存区可用时，将调用函数指针。

 从API version 12开始，推荐使用接口[OH_AVScreenCapture_OnBufferAvailable](#ZH-CN_TOPIC_0000002553202013__oh_avscreencapture_onbufferavailable)替代。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVScreenCapture *capture | 指向OH_AVScreenCapture实例的指针。 |
| bool isReady | 音频缓存区是否可用。true表示音频缓存区可用，false表示音频缓存区不可用。 |
| OH_AudioCaptureSourceType type | 音频源类型。 |

**OH_AVScreenCaptureOnVideoBufferAvailable()**

```ets
typedef void (*OH_AVScreenCaptureOnVideoBufferAvailable)(OH_AVScreenCapture *capture, bool isReady)
```

描述

当OH_AVScreenCapture实例操作期间视频缓存区可用时，将调用函数指针。

 从API version 12开始，推荐使用接口[OH_AVScreenCapture_OnBufferAvailable](#ZH-CN_TOPIC_0000002553202013__oh_avscreencapture_onbufferavailable)替代。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVScreenCapture *capture | 指向OH_AVScreenCapture实例的指针。 |
| bool isReady | 视频缓存区是否可用。true表示视频缓存区可用，false表示视频缓存区不可用。 |

**OH_AVScreenCapture_OnStateChange()**

```ets
typedef void (*OH_AVScreenCapture_OnStateChange)(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureStateCode stateCode, void *userData)
```

描述

当OH_AVScreenCapture实例操作期间发生状态变更时，将调用函数指针。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| struct OH_AVScreenCapture *capture | 指向OH_AVScreenCapture实例的指针。 |
| OH_AVScreenCaptureStateCode stateCode | 指定状态码。 |
| void *userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

**OH_AVScreenCapture_OnError()**

```ets
typedef void (*OH_AVScreenCapture_OnError)(OH_AVScreenCapture *capture, int32_t errorCode, void *userData)
```

描述

当OH_AVScreenCapture实例操作期间发生错误时，将调用函数指针。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVScreenCapture *capture | 指向OH_AVScreenCapture实例的指针。 |
| int32_t errorCode | 指定错误码。 |
| void *userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

**OH_AVScreenCapture_OnBufferAvailable()**

```ets
typedef void (*OH_AVScreenCapture_OnBufferAvailable)(OH_AVScreenCapture *capture, OH_AVBuffer *buffer, OH_AVScreenCaptureBufferType bufferType, int64_t timestamp, void *userData)
```

描述

当OH_AVScreenCapture实例操作期间音频或视频缓存区可用时，将调用该函数指针。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVScreenCapture *capture | 指向OH_AVScreenCapture实例的指针。 |
| OH_AVBuffer *buffer | 指向OH_AVBuffer缓存区实例的指针，该回调方法执行结束返回后，数据缓存区不再有效。 |
| OH_AVScreenCaptureBufferType bufferType | 可用缓存区的数据类型。 |
| int64_t timestamp | 时间戳，单位纳秒。 |
| void *userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

**OH_AVScreenCapture_OnDisplaySelected()**

```ets
typedef void (*OH_AVScreenCapture_OnDisplaySelected)(OH_AVScreenCapture *capture, uint64_t displayId, void *userData)
```

描述

当录屏事件开始时，将调用函数指针。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVScreenCapture *capture | 指向OH_AVScreenCapture实例的指针。 |
| uint64_t displayId | 录屏屏幕的Id。 |
| void *userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

**OH_AVScreenCapture_OnCaptureContentChanged()**

```ets
typedef void (*OH_AVScreenCapture_OnCaptureContentChanged)(OH_AVScreenCapture* capture, OH_AVScreenCaptureContentChangedEvent event, OH_Rect* area, void *userData)
```

描述

当OH_AVScreenCapture实例操作期间录屏内容变化时，将调用函数指针。

系统能力： SystemCapability.Multimedia.Media.AVScreenCapture

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVScreenCapture* capture | 指向OH_AVScreenCapture实例的指针。 |
| OH_AVScreenCaptureContentChangedEvent event | 录屏内容变更事件。 |
| OH_Rect* area | 录屏内容可见时，对应位置信息。 |
| void *userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

**OH_AVScreenCapture_OnUserSelected()**

```ets
typedef void (*OH_AVScreenCapture_OnUserSelected)(OH_AVScreenCapture* capture, OH_AVScreenCapture_UserSelectionInfo* selections, void *userData)
```

描述

当用户在授权界面（选择界面）选择参数时，功能接口将参数返回给应用程序。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AVScreenCapture* capture | 指向OH_AVScreenCapture实例的指针。 |
| OH_AVScreenCapture_UserSelectionInfo* selections | 用户在授权界面选择的录制参数信息。 |
| void *userData | 指向用户数据的指针。 |