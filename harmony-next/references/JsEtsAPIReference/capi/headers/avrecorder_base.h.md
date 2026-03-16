# avrecorder_base.h

#### 概述

定义了媒体AVRecorder的结构体和枚举。

**引用文件：** <multimedia/player_framework/avrecorder_base.h>

**库：** libavrecorder.so

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**相关模块：**[AVRecorder](../../topics/payment/AVRecorder.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVRecorder_Profile](../../topics/payment/OH_AVRecorder_Profile.md)OH_AVRecorder_Profile定义音视频录制的详细参数。[OH_AVRecorder](../../topics/payment/OH_AVRecorder.md)OH_AVRecorder初始化AVRecorder。[OH_AVRecorder_Location](../../topics/payment/OH_AVRecorder_Location.md)OH_AVRecorder_Location提供媒体资源的地理位置信息。[OH_AVRecorder_MetadataTemplate](../../topics/payment/OH_AVRecorder_MetadataTemplate.md)OH_AVRecorder_MetadataTemplate定义元数据的基本模板。[OH_AVRecorder_Metadata](../../topics/payment/OH_AVRecorder_Metadata.md)OH_AVRecorder_Metadata元数据信息数据结构。[OH_AVRecorder_Config](../../topics/payment/OH_AVRecorder_Config.md)OH_AVRecorder_Config提供媒体AVRecorder的配置定义。[OH_AVRecorder_Range](../../topics/payment/OH_AVRecorder_Range.md)OH_AVRecorder_Range表示类型的范围。[OH_AVRecorder_EncoderInfo](../../topics/payment/OH_AVRecorder_EncoderInfo.md)OH_AVRecorder_EncoderInfo提供编码器信息。

#### 枚举

名称typedef关键字描述[OH_AVRecorder_AudioSourceType](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_audiosourcetype)OH_AVRecorder_AudioSourceTypeAVRecorder的音频源类型。[OH_AVRecorder_VideoSourceType](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_videosourcetype)OH_AVRecorder_VideoSourceTypeAVRecorder的视频源类型。[OH_AVRecorder_CodecMimeType](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_codecmimetype)OH_AVRecorder_CodecMimeType编码器MIME类型。[OH_AVRecorder_ContainerFormatType](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_containerformattype)OH_AVRecorder_ContainerFormatType容器格式类型（容器格式类型的缩写是 CFT）。[OH_AVRecorder_State](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_state)OH_AVRecorder_StateAVRecorder状态。[OH_AVRecorder_StateChangeReason](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_statechangereason)OH_AVRecorder_StateChangeReasonAVRecorder状态变化的原因。[OH_AVRecorder_FileGenerationMode](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_filegenerationmode)OH_AVRecorder_FileGenerationMode创建录制文件的模式。

#### 函数

名称typedef关键字描述[typedef void (*OH_AVRecorder_OnStateChange)(OH_AVRecorder *recorder, OH_AVRecorder_State state, OH_AVRecorder_StateChangeReason reason, void *userData)](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_onstatechange)OH_AVRecorder_OnStateChange当录制状态发生变化时调用。[typedef void (*OH_AVRecorder_OnError)(OH_AVRecorder *recorder, int32_t errorCode, const char *errorMsg, void *userData)](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_onerror)OH_AVRecorder_OnError当录制过程中发生错误时调用。[typedef void (*OH_AVRecorder_OnUri)(OH_AVRecorder *recorder, OH_MediaAsset *asset, void *userData)](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_onuri)OH_AVRecorder_OnUri当录制在[OH_AVRecorder_FileGenerationMode](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_filegenerationmode).AVRECORDER_AUTO_CREATE_CAMERA_SCENE模式时调用。

#### 枚举类型说明

#### OH_AVRecorder_AudioSourceType

```ets
enum OH_AVRecorder_AudioSourceType
```

**描述**

AVRecorder的音频源类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

枚举项描述AVRECORDER_DEFAULT = 0默认音频源类型。AVRECORDER_MIC = 1麦克风音频源类型。AVRECORDER_VOICE_RECOGNITION = 2语音识别场景的音频源。AVRECORDER_VOICE_COMMUNICATION = 7语音通话场景的音频源。AVRECORDER_VOICE_MESSAGE = 10短语音消息的音频源。AVRECORDER_CAMCORDER = 13相机录像的音频源。

#### OH_AVRecorder_VideoSourceType

```ets
enum OH_AVRecorder_VideoSourceType
```

**描述**

AVRecorder的视频源类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

枚举项描述AVRECORDER_SURFACE_YUV = 0原始数据Surface。AVRECORDER_SURFACE_ES = 1ES数据Surface。

#### OH_AVRecorder_CodecMimeType

```ets
enum OH_AVRecorder_CodecMimeType
```

**描述**

编码器MIME类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

枚举项描述AVRECORDER_VIDEO_AVC = 2H.264 编码器MIME类型。AVRECORDER_AUDIO_AAC = 3AAC 编码器MIME类型。AVRECORDER_AUDIO_MP3 = 4mp3 编码器MIME类型。AVRECORDER_AUDIO_G711MU = 5G711-mulaw 编码器MIME类型。AVRECORDER_VIDEO_MPEG4 = 6MPEG4 编码器MIME类型。AVRECORDER_VIDEO_HEVC = 8H.265 编码器MIME类型。AVRECORDER_AUDIO_AMR_NB = 9AMR_NB 编解码器MIME类型。AVRECORDER_AUDIO_AMR_WB = 10AMR_WB 编解码器MIME类型。

#### OH_AVRecorder_ContainerFormatType

```ets
enum OH_AVRecorder_ContainerFormatType
```

**描述**

容器格式类型（容器格式类型的缩写是 CFT）。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

枚举项描述AVRECORDER_CFT_MPEG_4 = 2视频容器格式类型mp4。AVRECORDER_CFT_MPEG_4A = 6音频容器格式类型m4a。AVRECORDER_CFT_AMR = 8音频容器格式类型amr。AVRECORDER_CFT_MP3 = 9音频容器格式类型mp3。AVRECORDER_CFT_WAV = 10音频容器格式类型wav。AVRECORDER_CFT_AAC = 11

音频容器格式类型aac（带ADTS头）。

**起始版本：** 20

#### OH_AVRecorder_State

```ets
enum OH_AVRecorder_State
```

**描述**

AVRecorder状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

枚举项描述AVRECORDER_IDLE = 0空闲状态。此时可以调用[OH_AVRecorder_Prepare](avrecorder.h.md#ZH-CN_TOPIC_0000002529445879__oh_avrecorder_prepare)方法设置录制参数，进入AVRECORDER_PREPARED状态。AVRECORDER_PREPARED = 1准备状态。参数设置完成，此时可以调用[OH_AVRecorder_Start](avrecorder.h.md#ZH-CN_TOPIC_0000002529445879__oh_avrecorder_start)方法开始录制，进入AVRECORDER_STARTED状态。AVRECORDER_STARTED = 2

启动状态。正在录制，此时可以调用[OH_AVRecorder_Pause](avrecorder.h.md#ZH-CN_TOPIC_0000002529445879__oh_avrecorder_pause)方法暂停录制，进入AVRECORDER_PAUSED状态。

也可以调用[OH_AVRecorder_Stop](avrecorder.h.md#ZH-CN_TOPIC_0000002529445879__oh_avrecorder_stop)方法结束录制，进入AVRECORDER_STOPPED状态。

AVRECORDER_PAUSED = 3

暂停状态。此时可以调用[OH_AVRecorder_Resume](avrecorder.h.md#ZH-CN_TOPIC_0000002529445879__oh_avrecorder_resume)方法继续录制，进入AVRECORDER_STARTED状态。

也可以调用[OH_AVRecorder_Stop](avrecorder.h.md#ZH-CN_TOPIC_0000002529445879__oh_avrecorder_stop)方法结束录制，进入AVRECORDER_STOPPED状态。

AVRECORDER_STOPPED = 4停止状态。此时可以调用[OH_AVRecorder_Prepare](avrecorder.h.md#ZH-CN_TOPIC_0000002529445879__oh_avrecorder_prepare)方法设置录制参数，重新进入AVRECORDER_PREPARED状态。AVRECORDER_RELEASED = 5释放状态。录制资源释放，此时不能再进行任何操作。在任何其他状态下，均可以通过调用[OH_AVRecorder_Release](avrecorder.h.md#ZH-CN_TOPIC_0000002529445879__oh_avrecorder_release)方法进入AVRECORDER_RELEASED状态。AVRECORDER_ERROR = 6

错误状态。当AVRecorder实例发生不可逆错误，会转换至当前状态。

切换至AVRECORDER_ERROR状态时会伴随[OH_AVRecorder_OnError](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_onerror)事件，该事件会上报详细错误原因。

在AVRECORDER_ERROR状态时，用户需要调用[OH_AVRecorder_Reset](avrecorder.h.md#ZH-CN_TOPIC_0000002529445879__oh_avrecorder_reset)方法重置AVRecorder实例，或者调用[OH_AVRecorder_Release](avrecorder.h.md#ZH-CN_TOPIC_0000002529445879__oh_avrecorder_release)方法释放资源。

#### OH_AVRecorder_StateChangeReason

```ets
enum OH_AVRecorder_StateChangeReason
```

**描述**

AVRecorder状态变化的原因。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

枚举项描述AVRECORDER_USER = 0用户操作导致的状态变化。AVRECORDER_BACKGROUND = 1后台操作导致的状态变化。

#### OH_AVRecorder_FileGenerationMode

```ets
enum OH_AVRecorder_FileGenerationMode
```

**描述**

创建录制文件的模式。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

枚举项描述AVRECORDER_APP_CREATE = 0由应用自行在沙箱中创建媒体文件。AVRECORDER_AUTO_CREATE_CAMERA_SCENE = 1由系统创建媒体文件，当前仅在相机录制场景下生效。

#### 函数说明

#### OH_AVRecorder_OnStateChange()

```ets
typedef void (*OH_AVRecorder_OnStateChange)(OH_AVRecorder *recorder,OH_AVRecorder_State state, OH_AVRecorder_StateChangeReason reason, void *userData)
```

**描述**

当录制状态发生变化时调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

参数项描述[OH_AVRecorder](../../topics/payment/OH_AVRecorder.md) *recorderOH_AVRecorder实例的指针。[OH_AVRecorder_State](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_state) state表示录制器状态。[OH_AVRecorder_StateChangeReason](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_statechangereason) reason录制器状态变化的原因。void *userData用户特定数据的指针。

#### OH_AVRecorder_OnError()

```ets
typedef void (*OH_AVRecorder_OnError)(OH_AVRecorder *recorder, int32_t errorCode, const char *errorMsg,void *userData)
```

**描述**

当录制过程中发生错误时调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

参数项描述[OH_AVRecorder](../../topics/payment/OH_AVRecorder.md) *recorderOH_AVRecorder实例的指针。int32_t errorCode错误码，详细说明请参见[AVErrorCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)。const char *errorMsg错误信息。void *userData用户特定数据的指针。

#### OH_AVRecorder_OnUri()

```ets
typedef void (*OH_AVRecorder_OnUri)(OH_AVRecorder *recorder, OH_MediaAsset *asset, void *userData)
```

**描述**

当录制在[OH_AVRecorder_FileGenerationMode](#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_filegenerationmode).AVRECORDER_AUTO_CREATE_CAMERA_SCENE模式下时调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

参数项描述[OH_AVRecorder](../../topics/payment/OH_AVRecorder.md) *recorderOH_AVRecorder实例的指针。[OH_MediaAsset](../../topics/media/OH_MediaAsset.md) *assetOH_MediaAsset实例的指针。void *userData用户特定数据的指针。