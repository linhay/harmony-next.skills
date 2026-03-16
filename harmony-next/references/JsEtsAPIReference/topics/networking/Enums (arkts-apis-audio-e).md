[]()[]()

# Enums

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### AudioVolumeType

表示音频音量类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

名称值说明VOICE_CALL8+0语音电话。RINGTONE2铃声。MEDIA3媒体。ALARM10+4闹钟。ACCESSIBILITY10+5无障碍。VOICE_ASSISTANT8+9语音助手。[]()[]()

#### InterruptMode9+

表示焦点模型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

名称值说明SHARE_MODE0共享焦点模式。INDEPENDENT_MODE1独立焦点模式。[]()[]()

#### DeviceFlag

表示音频设备类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称值说明OUTPUT_DEVICES_FLAG1输出设备。INPUT_DEVICES_FLAG2输入设备。ALL_DEVICES_FLAG3所有设备。[]()[]()

#### DeviceUsage12+

表示音频设备类型的枚举（根据用途分类）。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称值说明MEDIA_OUTPUT_DEVICES1媒体输出设备。MEDIA_INPUT_DEVICES2媒体输入设备。ALL_MEDIA_DEVICES3所有媒体设备。CALL_OUTPUT_DEVICES4通话输出设备。CALL_INPUT_DEVICES8通话输入设备。ALL_CALL_DEVICES12所有通话设备。[]()[]()

#### DeviceRole

表示设备角色的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称值说明INPUT_DEVICE1输入设备角色。OUTPUT_DEVICE2输出设备角色。[]()[]()

#### DeviceType

表示设备类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称值说明INVALID0

无效设备。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

EARPIECE1

听筒。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SPEAKER2

扬声器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

WIRED_HEADSET3

有线耳机，带麦克风。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

WIRED_HEADPHONES4

有线耳机，不带麦克风。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

BLUETOOTH_SCO7

蓝牙设备SCO（Synchronous Connection Oriented）连接。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

BLUETOOTH_A2DP8

蓝牙设备A2DP（Advanced Audio Distribution Profile）连接。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

MIC15

麦克风。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

USB_HEADSET22

USB耳机，带麦克风。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

DISPLAY_PORT12+23

DisplayPort（显示接口，简称DP），用于外接扩展设备。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

REMOTE_CAST12+24

音频被系统应用投送到其他的远程设备。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

USB_DEVICE18+25USB设备（不包含USB耳机）。HDMI19+27HDMI设备（例如HDMI、ARC、eARC等）。LINE_DIGITAL19+28有线数字设备（例如S/PDIF等）。REMOTE_DAUDIO18+29

分布式设备。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

HEARING_AID20+30助听器设备。NEARLINK20+31星闪设备。SYSTEM_PRIVATE22+200系统私有设备（由于该设备在系统中属于私有设备，因此应用程序可以忽略该设备）。DEFAULT9+1000

默认设备类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

[]()[]()

#### BluetoothAndNearlinkPreferredRecordCategory21+

表示在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明PREFERRED_NONE0无指定设备偏好。PREFERRED_DEFAULT1更偏好使用蓝牙或星闪录音，是否使用低延迟或高质量录音取决于系统。PREFERRED_LOW_LATENCY2更偏好使用蓝牙或星闪低延迟模式进行录音。PREFERRED_HIGH_QUALITY3更偏好使用蓝牙或星闪高质量模式进行录音。[]()[]()

#### CommunicationDeviceType9+

表示用于通信的可用设备类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

名称值说明SPEAKER2扬声器。[]()[]()

#### AudioRingMode

表示铃声模式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

名称值说明RINGER_MODE_SILENT0静音模式。RINGER_MODE_VIBRATE1震动模式。RINGER_MODE_NORMAL2响铃模式。[]()[]()

#### AudioSampleFormat8+

表示音频采样格式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明SAMPLE_FORMAT_INVALID-1无效格式。SAMPLE_FORMAT_U80无符号8位整数。SAMPLE_FORMAT_S16LE1带符号的16位整数，小尾数。SAMPLE_FORMAT_S24LE2

带符号的24位整数，小尾数。

由于系统限制，该采样格式仅部分设备支持，请根据实际情况使用。

SAMPLE_FORMAT_S32LE3

带符号的32位整数，小尾数。

由于系统限制，该采样格式仅部分设备支持，请根据实际情况使用。

SAMPLE_FORMAT_F32LE9+4

带符号的32位浮点数，小尾数。

由于系统限制，该采样格式仅部分设备支持，请根据实际情况使用。

[]()[]()

#### AudioErrors9+

表示音频错误码的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明ERROR_INVALID_PARAM6800101无效入参。ERROR_NO_MEMORY6800102分配内存失败。ERROR_ILLEGAL_STATE6800103状态不支持。ERROR_UNSUPPORTED6800104参数选项不支持。ERROR_TIMEOUT6800105处理超时。ERROR_STREAM_LIMIT6800201音频流数量达到限制。ERROR_SYSTEM6800301系统处理异常。[]()[]()

#### AudioChannel8+

表示音频声道的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明CHANNEL_11单声道。CHANNEL_22双声道。CHANNEL_311+3三声道。CHANNEL_411+4四声道。CHANNEL_511+5五声道。CHANNEL_611+6六声道。CHANNEL_711+7七声道。CHANNEL_811+8八声道。CHANNEL_911+9九声道。CHANNEL_1011+10十声道。CHANNEL_1211+12十二声道。CHANNEL_1411+14十四声道。CHANNEL_1611+16十六声道。[]()[]()

#### AudioSamplingRate8+

表示音频采样率的枚举（具体设备支持的采样率规格会存在差异）。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明SAMPLE_RATE_80008000采样率为8000。SAMPLE_RATE_1102511025采样率为11025。SAMPLE_RATE_1200012000采样率为12000。SAMPLE_RATE_1600016000采样率为16000。SAMPLE_RATE_2205022050采样率为22050。SAMPLE_RATE_2400024000采样率为24000。SAMPLE_RATE_3200032000采样率为32000。SAMPLE_RATE_4410044100采样率为44100。SAMPLE_RATE_4800048000采样率为48000。SAMPLE_RATE_6400064000采样率为64000。SAMPLE_RATE_8820012+88200采样率为88200。SAMPLE_RATE_9600096000采样率为96000。SAMPLE_RATE_17640012+176400采样率为176400。SAMPLE_RATE_19200012+192000采样率为192000。[]()[]()

#### AudioEncodingType8+

表示音频编码类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明ENCODING_TYPE_INVALID-1无效。ENCODING_TYPE_RAW0PCM编码。[]()[]()

#### AudioChannelLayout11+

表示音频文件声道布局类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明CH_LAYOUT_UNKNOWN0x0未知声道布局。CH_LAYOUT_MONO0x4声道布局为MONO。CH_LAYOUT_STEREO0x3声道布局为STEREO。CH_LAYOUT_STEREO_DOWNMIX0x60000000声道布局为STEREO-DOWNMIX。CH_LAYOUT_2POINT10xB声道布局为2.1。CH_LAYOUT_3POINT00x103声道布局为3.0。CH_LAYOUT_SURROUND0x7声道布局为SURROUND。CH_LAYOUT_3POINT10xF声道布局为3.1。CH_LAYOUT_4POINT00x107声道布局为4.0。CH_LAYOUT_QUAD0x33声道布局为QUAD。CH_LAYOUT_QUAD_SIDE0x603声道布局为QUAD-SIDE。CH_LAYOUT_2POINT0POINT20x3000000003声道布局为2.0.2。CH_LAYOUT_AMB_ORDER1_ACN_N3D0x100000000001声道排序为ACN_N3D（根据ITU标准）的一阶FOA文件。CH_LAYOUT_AMB_ORDER1_ACN_SN3D0x100000001001声道排序为ACN_SN3D（根据ITU标准）的一阶FOA文件。CH_LAYOUT_AMB_ORDER1_FUMA0x100000000101声道排序为FUMA（根据ITU标准）的一阶FOA文件。CH_LAYOUT_4POINT10x10F声道布局为4.1。CH_LAYOUT_5POINT00x607声道布局为5.0。CH_LAYOUT_5POINT0_BACK0x37声道布局为5.0-BACK。CH_LAYOUT_2POINT1POINT20x300000000B声道布局为2.1.2。CH_LAYOUT_3POINT0POINT20x3000000007声道布局为3.0.2。CH_LAYOUT_5POINT10x60F声道布局为5.1。CH_LAYOUT_5POINT1_BACK0x3F声道布局为5.1-BACK。CH_LAYOUT_6POINT00x707声道布局为6.0。CH_LAYOUT_HEXAGONAL0x137声道布局为HEXAGONAL。CH_LAYOUT_3POINT1POINT20x500F声道布局为3.1.2。CH_LAYOUT_6POINT0_FRONT0x6C3声道布局为6.0-FRONT。CH_LAYOUT_6POINT10x70F声道布局为6.1。CH_LAYOUT_6POINT1_BACK0x13F声道布局为6.1-BACK。CH_LAYOUT_6POINT1_FRONT0x6CB声道布局为6.1-FRONT。CH_LAYOUT_7POINT00x637声道布局为7.0。CH_LAYOUT_7POINT0_FRONT0x6C7声道布局为7.0-FRONT。CH_LAYOUT_7POINT10x63F声道布局为7.1。CH_LAYOUT_OCTAGONAL0x737声道布局为OCTAGONAL。CH_LAYOUT_5POINT1POINT20x300000060F声道布局为5.1.2。CH_LAYOUT_7POINT1_WIDE0x6CF声道布局为7.1-WIDE。CH_LAYOUT_7POINT1_WIDE_BACK0xFF声道布局为7.1-WIDE-BACK。CH_LAYOUT_AMB_ORDER2_ACN_N3D0x100000000002声道排序为ACN_N3D（根据ITU标准）的二阶HOA文件。CH_LAYOUT_AMB_ORDER2_ACN_SN3D0x100000001002声道排序为ACN_SN3D（根据ITU标准）的二阶HOA文件。CH_LAYOUT_AMB_ORDER2_FUMA0x100000000102声道排序为FUMA（根据ITU标准）的二阶HOA文件。CH_LAYOUT_5POINT1POINT40x2D60F声道布局为5.1.4。CH_LAYOUT_7POINT1POINT20x300000063F声道布局为7.1.2。CH_LAYOUT_7POINT1POINT40x2D63F声道布局为7.1.4。CH_LAYOUT_10POINT20x180005737声道布局为10.2。CH_LAYOUT_9POINT1POINT40x18002D63F声道布局为9.1.4。CH_LAYOUT_9POINT1POINT60x318002D63F声道布局为9.1.6。CH_LAYOUT_HEXADECAGONAL0x18003F737声道布局为HEXADECAGONAL。CH_LAYOUT_AMB_ORDER3_ACN_N3D0x100000000003声道排序为ACN_N3D（根据ITU标准）的三阶HOA文件。CH_LAYOUT_AMB_ORDER3_ACN_SN3D0x100000001003声道排序为ACN_SN3D（根据ITU标准）的三阶HOA文件。CH_LAYOUT_AMB_ORDER3_FUMA0x100000000103声道排序为FUMA（根据ITU标准）的三阶HOA文件。[]()[]()

#### StreamUsage

表示播放音频流类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明STREAM_USAGE_UNKNOWN0

未知类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_MEDIA(deprecated)1

媒体。

从API version 7开始支持，从API version 10开始废弃，建议使用该枚举中的STREAM_USAGE_MUSIC、STREAM_USAGE_MOVIE、STREAM_USAGE_GAME或STREAM_USAGE_AUDIOBOOK替代。

STREAM_USAGE_MUSIC10+1

音乐。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_VOICE_COMMUNICATION2

VoIP语音通话（该流类型起播时，会触发开启3A算法）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_VOICE_ASSISTANT9+3

语音播报。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_ALARM10+4

闹钟。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_VOICE_MESSAGE10+5

语音消息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_NOTIFICATION_RINGTONE(deprecated)6

通知铃声。

从API version 7开始支持，从API version 10开始废弃，建议使用该枚举中的STREAM_USAGE_RINGTONE替代。

STREAM_USAGE_RINGTONE10+6

铃声。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_NOTIFICATION10+7

通知音。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_ACCESSIBILITY10+8

无障碍。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_MOVIE10+10

电影或视频。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_GAME10+11

游戏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_AUDIOBOOK10+12

有声读物（包括听书、相声、评书）、听新闻、播客等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_NAVIGATION10+13

导航。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

STREAM_USAGE_VIDEO_COMMUNICATION12+17

VoIP视频通话（该流类型起播时，会触发开启3A算法）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

[]()[]()

#### AudioState8+

表示音频状态的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明STATE_INVALID-1无效状态。STATE_NEW0创建新实例状态。STATE_PREPARED1准备状态。STATE_RUNNING2运行状态。STATE_STOPPED3停止状态。STATE_RELEASED4释放状态。STATE_PAUSED5暂停状态。[]()[]()

#### AudioEffectMode10+

表示音效模式的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称值说明EFFECT_NONE0关闭音效。EFFECT_DEFAULT1默认音效。[]()[]()

#### AudioRendererRate8+

表示音频渲染速度的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称值说明RENDER_RATE_NORMAL0正常速度。RENDER_RATE_DOUBLE12倍速。RENDER_RATE_HALF20.5倍速。[]()[]()

#### InterruptType

表示中断类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称值说明INTERRUPT_TYPE_BEGIN1音频播放中断事件开始。INTERRUPT_TYPE_END2音频播放中断事件结束。[]()[]()

#### InterruptForceType9+

表示音频打断类型的枚举。

当用户监听到音频中断（即收到[InterruptEvent](../../types/interfaces/Interfaces (其他) (arkts-apis-audio-i).md#ZH-CN_TOPIC_0000002497445724__interruptevent9)事件）时，获取此信息。

此类型表示音频打断是否已由系统强制执行，具体操作信息（如音频暂停、停止等）可通过[InterruptHint](#ZH-CN_TOPIC_0000002529285695__interrupthint)获取。关于音频打断策略的详细说明可参考文档[音频焦点和音频会话介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-concurrency)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称值说明INTERRUPT_FORCE0强制打断类型，即具体操作已由系统强制执行。INTERRUPT_SHARE1共享打断类型，即系统不执行具体操作，通过[InterruptHint](#ZH-CN_TOPIC_0000002529285695__interrupthint)建议并提示应用操作，应用可自行决策下一步处理方式。[]()[]()

#### InterruptHint

表示中断提示的枚举。

当用户监听到音频中断事件（即收到[InterruptEvent](../../types/interfaces/Interfaces (其他) (arkts-apis-audio-i).md#ZH-CN_TOPIC_0000002497445724__interruptevent9)事件）时，获取此信息。

此类型表示根据焦点策略，对音频流执行的具体操作（如暂停、调整音量等）。

可以结合InterruptEvent中的[InterruptForceType](#ZH-CN_TOPIC_0000002529285695__interruptforcetype9)信息，判断该操作是否已由系统强制执行。详情请参阅文档[音频焦点和音频会话介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-concurrency)。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称值说明INTERRUPT_HINT_NONE8+0

无提示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

INTERRUPT_HINT_RESUME1

提示音频恢复，应用可主动触发开始渲染或开始采集的相关操作。

此操作无法由系统强制执行，其对应的[InterruptForceType](#ZH-CN_TOPIC_0000002529285695__interruptforcetype9)一定为INTERRUPT_SHARE类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

INTERRUPT_HINT_PAUSE2

提示音频暂停，暂时失去音频焦点。

待焦点可用时，会收到INTERRUPT_HINT_RESUME事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

INTERRUPT_HINT_STOP3

提示音频停止，彻底失去音频焦点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

INTERRUPT_HINT_DUCK4

提示音频躲避开始，降低音量播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

INTERRUPT_HINT_UNDUCK8+5

提示音频躲避结束，恢复音量播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

INTERRUPT_HINT_MUTE20+6提示音频静音。INTERRUPT_HINT_UNMUTE20+7提示音频解除静音。[]()[]()

#### AudioVolumeMode19+

表示音量模式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

名称值说明SYSTEM_GLOBAL0系统级音量（默认模式）。APP_INDIVIDUAL1应用级音量。[]()[]()

#### AudioPrivacyType10+

表示对应播放音频流是否支持被其他应用录制的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

名称值说明PRIVACY_TYPE_PUBLIC0表示音频流可以被其他应用录制或屏幕投射，不包含隐私类型的流。PRIVACY_TYPE_PRIVATE1表示音频流不可以被其他应用录制或屏幕投射。PRIVACY_TYPE_SHARED21+2

表示音频流可以被其他应用录制或屏幕投射，包含隐私类型的流。

例如，在PRIVACY_TYPE_PUBLIC策略下，[STREAM_USAGE_VOICE_COMMUNICATION](#ZH-CN_TOPIC_0000002529285695__streamusage)类型音频流不会被其他应用录制或屏幕投射。

然而，在PRIVACY_TYPE_SHARED策略下，这些音频流将会允许被其他应用录制或屏幕投射。

[]()[]()

#### ChannelBlendMode11+

表示声道混合模式类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明MODE_DEFAULT0无声道混合。MODE_BLEND_LR1混合左右声道。MODE_ALL_LEFT2从左声道覆盖到右声道混合。MODE_ALL_RIGHT3从右声道覆盖到左声道混合。[]()[]()

#### AudioStreamDeviceChangeReason11+

表示流设备变更原因的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称值说明REASON_UNKNOWN0

未知原因。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

REASON_NEW_DEVICE_AVAILABLE1

新设备可用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

REASON_OLD_DEVICE_UNAVAILABLE2

旧设备不可用。报告此原因时，应考虑暂停音频播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

REASON_OVERRODE3

强选。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

REASON_SESSION_ACTIVATED20+4音频会话已激活。REASON_STREAM_PRIORITY_CHANGED20+5更高优先级的音频流出现导致的系统设备切换。[]()[]()

#### OutputDeviceChangeRecommendedAction20+

表示输出设备变更后推荐操作的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明DEVICE_CHANGE_RECOMMEND_TO_CONTINUE0推荐继续播放。DEVICE_CHANGE_RECOMMEND_TO_STOP1推荐停止播放。[]()[]()

#### DeviceChangeType

表示设备连接状态变化的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称值说明CONNECT0设备连接。DISCONNECT1断开设备连接。[]()[]()

#### DeviceBlockStatus13+

表示音频设备是否被堵塞的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称值说明UNBLOCKED0音频设备正常。BLOCKED1音频设备被堵塞。[]()[]()

#### SourceType8+

表示录制音频流类型的枚举。

名称值说明SOURCE_TYPE_INVALID-1

无效的音频源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

SOURCE_TYPE_MIC0

Mic音频源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

SOURCE_TYPE_VOICE_RECOGNITION9+1

语音识别源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

SOURCE_TYPE_PLAYBACK_CAPTURE(deprecated)2

播放音频流（内录）录制音频源。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

从API version 10开始支持，从API version 12开始废弃，建议使用[录屏接口AVScreenCapture](../misc/AVScreenCapture.md)替代。

SOURCE_TYPE_VOICE_COMMUNICATION7

语音通话场景的音频源（单独启动录制不会开启3A算法，需同时使用[STREAM_USAGE_VOICE_COMMUNICATION](#ZH-CN_TOPIC_0000002529285695__streamusage)或[STREAM_USAGE_VIDEO_COMMUNICATION](#ZH-CN_TOPIC_0000002529285695__streamusage)类型的AudioRender起播才会触发开启3A算法）。

**系统能力：** SystemCapability.Multimedia.Audio.Core

SOURCE_TYPE_VOICE_MESSAGE12+10

短语音消息的音频源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

SOURCE_TYPE_CAMCORDER13+13

录像的音频源。

**系统能力：** SystemCapability.Multimedia.Audio.Core

SOURCE_TYPE_UNPROCESSED14+14

麦克风纯净录音的音频源（系统不做任何算法处理）。

**系统能力：** SystemCapability.Multimedia.Audio.Core

SOURCE_TYPE_LIVE20+17

直播场景的音频源，在支持的设备上会提供系统回声消除能力。

**系统能力：** SystemCapability.Multimedia.Audio.Core

[]()[]()

#### AudioScene8+

表示音频场景的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

名称值说明AUDIO_SCENE_DEFAULT0默认音频场景。AUDIO_SCENE_RINGING12+1响铃模式。AUDIO_SCENE_PHONE_CALL12+2电话模式。AUDIO_SCENE_VOICE_CHAT3语音聊天模式。[]()[]()

#### AudioConcurrencyMode12+

表示音频并发模式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明CONCURRENCY_DEFAULT0默认使用系统策略。CONCURRENCY_MIX_WITH_OTHERS1和其他音频并发。CONCURRENCY_DUCK_OTHERS2压低其他音频的音量。CONCURRENCY_PAUSE_OTHERS3暂停其他音频。[]()[]()

#### AudioSessionDeactivatedReason12+

表示音频会话停用原因的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明DEACTIVATED_LOWER_PRIORITY0应用焦点被抢占。DEACTIVATED_TIMEOUT1音频会话等待超时。[]()[]()

#### AudioSessionScene20+

枚举音频会话场景。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明AUDIO_SESSION_SCENE_MEDIA0媒体音频会话场景。AUDIO_SESSION_SCENE_GAME1游戏音频会话场景。AUDIO_SESSION_SCENE_VOICE_COMMUNICATION2VoIP语音通话音频会话场景。[]()[]()

#### AudioSessionStateChangeHint20+

枚举用于音频会话状态变更提示。

当用户监听到音频会话状态变化事件（即收到[AudioSessionStateChangedEvent](../../types/interfaces/Interfaces (其他) (arkts-apis-audio-i).md#ZH-CN_TOPIC_0000002497445724__audiosessionstatechangedevent20)事件）时，获取相关信息。

此类型表示根据焦点策略对音频会话执行的操作，包括暂停、调整音量等。

详情请参阅文档[音频焦点和音频会话介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-concurrency)。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明AUDIO_SESSION_STATE_CHANGE_HINT_RESUME0提示音频会话恢复，应用可主动触发开始渲染等操作。AUDIO_SESSION_STATE_CHANGE_HINT_PAUSE1提示音频会话暂停，暂时失去音频焦点。当焦点再次可用时，会收到 AUDIO_SESSION_STATE_CHANGE_HINT_RESUME 事件。AUDIO_SESSION_STATE_CHANGE_HINT_STOP2提示音频会话因焦点被抢占而停止，彻底失去音频焦点。AUDIO_SESSION_STATE_CHANGE_HINT_TIME_OUT_STOP3提示音频会话因长时间无业务而被系统停止，导致失去音频焦点。AUDIO_SESSION_STATE_CHANGE_HINT_DUCK4提示音频会话躲避开始，降低音量播放。AUDIO_SESSION_STATE_CHANGE_HINT_UNDUCK5提示音频会话躲避结束，恢复音量播放。[]()[]()

#### AudioDataCallbackResult12+

表示音频数据回调结果的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明INVALID-1表示该回调数据无效。VALID0表示该回调数据有效。[]()[]()

#### ContentType(deprecated)

表示音频内容类型的枚举。

从API version 7开始支持，从API version 10开始废弃，建议使用[StreamUsage](#ZH-CN_TOPIC_0000002529285695__streamusage)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称值说明CONTENT_TYPE_UNKNOWN0未知类型。CONTENT_TYPE_SPEECH1语音。CONTENT_TYPE_MUSIC2音乐。CONTENT_TYPE_MOVIE3电影。CONTENT_TYPE_SONIFICATION4通知音。CONTENT_TYPE_RINGTONE8+5铃声。[]()[]()

#### ActiveDeviceType(deprecated)

表示活跃设备类型的枚举。

从API version 7开始支持，从API version 9开始废弃，建议使用[CommunicationDeviceType](#ZH-CN_TOPIC_0000002529285695__communicationdevicetype9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称值说明SPEAKER2扬声器。BLUETOOTH_SCO7蓝牙设备SCO（Synchronous Connection Oriented）连接。[]()[]()

#### InterruptActionType(deprecated)

表示中断事件返回类型的枚举。

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称值说明TYPE_ACTIVATED0表示触发焦点事件。TYPE_INTERRUPT1表示音频打断事件。[]()[]()

#### AudioLoopbackMode20+

表示返听模式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

名称值说明HARDWARE0表示硬件返听模式。[]()[]()

#### AudioLoopbackStatus20+

表示返听状态的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

名称值说明UNAVAILABLE_DEVICE-2表示返听由于输入\输出设备而不可用（如出声设备变更）。UNAVAILABLE_SCENE-1表示返听由于音频场景而不可用（如音频焦点、低时延管控）。AVAILABLE_IDLE0表示返听可用。AVAILABLE_RUNNING1表示返听运行中。[]()[]()

#### AudioLoopbackReverbPreset21+

表示返听混响模式的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

名称值说明ORIGINAL1保持原始混响，不进行任何增强。KTV2提供类似KTV的混响效果。THEATER3提供类似剧场的混响效果（默认的混响模式）。CONCERT4提供类似演唱会的混响效果。[]()[]()

#### AudioLoopbackEqualizerPreset21+

表示返听均衡器类型的枚举。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

名称值说明FLAT1保持原始声音，不进行均衡调节。FULL2使人声更饱满（默认的均衡器类型）。BRIGHT3使人声更明亮。