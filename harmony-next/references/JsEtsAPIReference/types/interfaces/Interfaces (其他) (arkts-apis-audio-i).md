[]()[]()

# Interfaces (其他)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### AudioStreamInfo8+

音频流信息。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称类型只读可选说明samplingRate[AudioSamplingRate](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiosamplingrate8)否否音频文件的采样率。channels[AudioChannel](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiochannel8)否否音频文件的通道数。sampleFormat[AudioSampleFormat](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiosampleformat8)否否音频采样格式。encodingType[AudioEncodingType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audioencodingtype8)否否音频编码格式。channelLayout11+[AudioChannelLayout](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiochannellayout11)否是音频声道布局，默认值为0x0。[]()[]()

#### AudioRendererInfo8+

音频渲染器信息。

名称类型只读可选说明content[ContentType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__contenttypedeprecated)否是

音频内容类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

API version 8、9为必填参数，从API version 10开始为可选参数，默认值为CONTENT_TYPE_UNKNOWN。

从API version 7开始支持，从API version 10开始废弃，建议使用[StreamUsage](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__streamusage)替代。

usage[StreamUsage](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__streamusage)否否

音频流使用类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

rendererFlagsnumber否否

播放流行为标志。

设置为0即可。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

volumeMode19+[AudioVolumeMode](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiovolumemode19)否是

音频的音量模式。默认值为SYSTEM_GLOBAL。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

[]()[]()

#### AudioRendererOptions8+

音频渲染器选项信息。

名称类型只读可选说明streamInfo[AudioStreamInfo](#ZH-CN_TOPIC_0000002497445724__audiostreaminfo8)否否

音频流信息。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

rendererInfo[AudioRendererInfo](#ZH-CN_TOPIC_0000002497445724__audiorendererinfo8)否否

音频渲染器信息。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

privacyType10+[AudioPrivacyType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audioprivacytype10)否是

表示音频流是否可以被其他应用录制，默认值为0。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

[]()[]()

#### InterruptEvent9+

音频中断时，应用接收的中断事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称类型只读可选说明eventType[InterruptType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__interrupttype)否否音频中断事件类型，开始或是结束。forceType[InterruptForceType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__interruptforcetype9)否否操作是由系统强制执行或是由应用程序执行。hintType[InterruptHint](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__interrupthint)否否中断提示，用于提供中断事件的相关信息。[]()[]()

#### DeviceBlockStatusInfo13+

描述音频设备被堵塞状态和设备信息。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称类型只读可选说明blockStatus[DeviceBlockStatus](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__deviceblockstatus13)否否音频设备堵塞状态。devices[AudioDeviceDescriptors](../../topics/networking/Types (arkts-apis-audio-t).md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)否否设备信息。[]()[]()

#### AudioSessionStrategy12+

音频会话策略。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称类型只读可选说明concurrencyMode[AudioConcurrencyMode](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audioconcurrencymode12)否否音频并发模式。[]()[]()

#### AudioSessionDeactivatedEvent12+

音频会话停用事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称类型只读可选说明reason[AudioSessionDeactivatedReason](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiosessiondeactivatedreason12)否否音频会话停用原因。[]()[]()

#### AudioSessionStateChangedEvent20+

音频会话状态变更事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称类型只读可选说明stateChangeHint[AudioSessionStateChangeHint](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiosessionstatechangehint20)否否音频会话状态变更提示。[]()[]()

#### AudioRendererChangeInfo9+

描述音频渲染器更改信息。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称类型只读可选说明streamIdnumber是否音频流唯一id。rendererInfo[AudioRendererInfo](#ZH-CN_TOPIC_0000002497445724__audiorendererinfo8)是否音频渲染器信息。deviceDescriptors[AudioDeviceDescriptors](../../topics/networking/Types (arkts-apis-audio-t).md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)是否音频设备描述。[]()[]()

#### AudioCapturerChangeInfo9+

描述音频采集器更改信息。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

名称类型只读可选说明streamIdnumber是否音频流唯一id。capturerInfo[AudioCapturerInfo](#ZH-CN_TOPIC_0000002497445724__audiocapturerinfo8)是否音频采集器信息。deviceDescriptors[AudioDeviceDescriptors](../../topics/networking/Types (arkts-apis-audio-t).md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)是否音频设备信息。muted11+boolean是是音频采集器是否处于静音状态。true表示静音，false表示非静音。[]()[]()

#### AudioDeviceDescriptor

描述音频设备。

名称类型只读可选说明deviceRole[DeviceRole](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__devicerole)是否

设备角色。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

deviceType[DeviceType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__devicetype)是否

设备类型。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

id9+number是否

唯一的设备id。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

name9+string是否

设备名称。

如果是蓝牙设备，需要申请权限ohos.permission.USE_BLUETOOTH。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

address9+string是否

设备静态MAC地址。

如果是蓝牙设备，需要申请权限ohos.permission.USE_BLUETOOTH。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

sampleRates9+Array<number>是否

支持的采样率。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

channelCounts9+Array<number>是否

支持的通道数。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

channelMasks9+Array<number>是否

支持的通道掩码。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

displayName10+string是否

设备显示名。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

encodingTypes11+Array<[AudioEncodingType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audioencodingtype8)>是是

支持的编码类型。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

spatializationSupported18+boolean是是

设备是否支持空间音频。true表示支持空间音频，false表示不支持空间音频。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

model22+string是是

设备的具体型号类别。

**系统能力：** SystemCapability.Multimedia.Audio.Device

capabilities22+Array<[AudioStreamInfo](#ZH-CN_TOPIC_0000002497445724__audiostreaminfo8)>是是

设备支持的音频流能力。

**系统能力：** SystemCapability.Multimedia.Audio.Device

[]()[]()

#### VolumeEvent9+

音量改变时，应用接收到的事件。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

名称类型只读可选说明volumeType[AudioVolumeType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)否否音频音量类型。volumenumber否否音量等级，可设置范围通过调用getMinVolume和getMaxVolume方法获取。updateUiboolean否否是否在UI中显示音量变化。true表示显示，false表示不显示。volumeMode19+[AudioVolumeMode](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiovolumemode19)否是音频的音量模式。默认值为SYSTEM_GLOBAL。[]()[]()

#### MicStateChangeEvent9+

麦克风状态变化时，应用接收到的事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称类型只读可选说明muteboolean否否系统麦克风是否为静音状态。true表示静音，false表示非静音。[]()[]()

#### StreamVolumeEvent20+

音频流音量变化时，应用接收到的事件。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

名称类型只读可选说明streamUsage[StreamUsage](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__streamusage)否否音量发生变化的音频流。volumenumber否否音量值。updateUiboolean否否是否在UI上展示音量变化。true表示展示，false表示不展示。[]()[]()

#### DeviceChangeAction

描述设备连接状态变化和设备信息。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称类型只读可选说明type[DeviceChangeType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__devicechangetype)否否设备连接状态变化。deviceDescriptors[AudioDeviceDescriptors](../../topics/networking/Types (arkts-apis-audio-t).md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)否否设备信息。[]()[]()

#### AudioStreamDeviceChangeInfo11+

流设备变更时，应用接收到的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Device

名称类型只读可选说明devices[AudioDeviceDescriptors](../../topics/networking/Types (arkts-apis-audio-t).md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)否否设备信息。changeReason[AudioStreamDeviceChangeReason](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiostreamdevicechangereason11)否否流设备变更原因。[]()[]()

#### CurrentOutputDeviceChangedEvent20+

应用接收到输出设备的变更事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称类型只读可选说明devices[AudioDeviceDescriptors](../../topics/networking/Types (arkts-apis-audio-t).md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)否否设备信息。changeReason[AudioStreamDeviceChangeReason](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiostreamdevicechangereason11)否否设备变更原因。recommendedAction[OutputDeviceChangeRecommendedAction](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__outputdevicechangerecommendedaction20)否否设备变更后推荐的操作。[]()[]()

#### CurrentInputDeviceChangedEvent21+

应用接收到输入设备的变更事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称类型只读可选说明devices[AudioDeviceDescriptors](../../topics/networking/Types (arkts-apis-audio-t).md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)否否设备信息。changeReason[AudioStreamDeviceChangeReason](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audiostreamdevicechangereason11)否否设备变更原因。[]()[]()

#### AudioTimestampInfo19+

音频流时间戳和当前数据帧位置信息。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称类型只读可选说明framePosnumber是否当前播放或者录制的数据帧位置。timestampnumber是否播放或者录制到当前数据帧位置时对应的时间戳。[]()[]()

#### AudioCapturerInfo8+

描述音频采集器信息。

**系统能力：** SystemCapability.Multimedia.Audio.Core

名称类型只读可选说明source[SourceType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__sourcetype8)否否音源类型。capturerFlagsnumber否否

录制流行为标志。

设置为0即可。

[]()[]()

#### AudioCapturerOptions8+

音频采集器选项信息。

名称类型只读可选说明streamInfo[AudioStreamInfo](#ZH-CN_TOPIC_0000002497445724__audiostreaminfo8)否否

音频流信息。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

capturerInfo[AudioCapturerInfo](#ZH-CN_TOPIC_0000002497445724__audiocapturerinfo8)否否

音频采集器信息。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

playbackCaptureConfig(deprecated)[AudioPlaybackCaptureConfig](#ZH-CN_TOPIC_0000002497445724__audioplaybackcaptureconfigdeprecated)否是

音频内录的配置信息。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

 从API version 10开始支持，从API version 12开始废弃，建议使用[录屏接口AVScreenCapture](../../topics/misc/AVScreenCapture.md)替代。

[]()[]()

#### AudioInterrupt(deprecated)

音频监听事件传入的参数。

从API version 7开始支持，从API version 9开始废弃，无替代接口。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称类型只读可选说明streamUsage[StreamUsage](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__streamusage)否否音频流使用类型。contentType[ContentType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__contenttypedeprecated)否否音频打断媒体类型。pauseWhenDuckedboolean否否音频打断时是否可以暂停音频播放。true表示音频播放可以在音频打断期间暂停，false表示音频播放不可以在音频打断期间暂停。[]()[]()

#### CaptureFilterOptions(deprecated)

待录制的播放音频流的筛选信息。

从API version 10开始支持，从API version 12开始废弃，建议使用[录屏接口AVScreenCapture](../../topics/misc/AVScreenCapture.md)替代。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

名称类型只读可选说明usagesArray<[StreamUsage](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__streamusage)>否否

指定需要录制的音频播放流的StreamUsage类型。可同时指定0个或多个StreamUsage。Array为空时，默认录制StreamUsage为STREAM_USAGE_MUSIC、STREAM_USAGE_MOVIE、STREAM_USAGE_GAME和STREAM_USAGE_AUDIOBOOK的音频播放流。

在API version 10时，CaptureFilterOptions支持使用StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION，使用时需要申请权限ohos.permission.CAPTURE_VOICE_DOWNLINK_AUDIO，该权限仅系统应用可申请。

从API version 11开始，CaptureFilterOptions不再支持使用StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION，所以当前接口不再涉及此权限。

[]()[]()

#### AudioPlaybackCaptureConfig(deprecated)

音频内录的配置信息。

从API version 10开始支持，从API version 12开始废弃，建议使用[录屏接口AVScreenCapture](../../topics/misc/AVScreenCapture.md)替代。

**系统能力：** SystemCapability.Multimedia.Audio.PlaybackCapture

名称类型只读可选说明filterOptions[CaptureFilterOptions](#ZH-CN_TOPIC_0000002497445724__capturefilteroptionsdeprecated)否否需要录制的播放音频流的筛选信息。[]()[]()

#### InterruptAction(deprecated)

音频打断/获取焦点事件的回调方法。

从API version 7开始支持，从API version 9开始废弃，建议使用[InterruptEvent](#ZH-CN_TOPIC_0000002497445724__interruptevent9)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称类型只读可选说明actionType[InterruptActionType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__interruptactiontypedeprecated)否否事件返回类型。TYPE_ACTIVATED为焦点触发事件，TYPE_INTERRUPT为音频打断事件。type[InterruptType](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__interrupttype)否是打断事件类型。hint[InterruptHint](../../topics/networking/Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__interrupthint)否是打断事件提示。activatedboolean否是焦点获取/释放是否成功。true表示焦点获取/释放成功，false表示焦点获得/释放失败。