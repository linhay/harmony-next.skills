[]()[]()

# Interfaces (其他)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### AVCastControlCommand10+

投播控制器接受的命令的对象描述。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

名称类型只读可选说明command[AVCastControlCommandType](../../topics/networking/Types (arkts-apis-avsession-t).md#ZH-CN_TOPIC_0000002497605764__avcastcontrolcommandtype10)否否命令。每种命令对应的参数不同，具体的对应关系可查阅[AVCastControlCommandType](../../topics/networking/Types (arkts-apis-avsession-t).md#ZH-CN_TOPIC_0000002497605764__avcastcontrolcommandtype10)。parameter[media.PlaybackSpeed](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__playbackspeed8) | number | string | [LoopMode](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__loopmode10)否是命令对应的参数。[]()[]()

#### CastDisplayInfo12+

扩展屏投播显示设备相关属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

名称类型只读可选说明idnumber否否投播显示设备的ID，该参数应为整数。namestring否否投播显示设备的名称。state[CastDisplayState](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__castdisplaystate12)否否投播显示设备状态。widthnumber否否投播显示设备的屏幕宽度，单位为px，该参数应为整数。heightnumber否否投播显示设备的屏幕高度，单位为px，该参数应为整数。[]()[]()

#### AVMetadata10+

媒体元数据的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明assetIdstring否否

媒体ID。歌曲的唯一标识，由应用自定义。该属性发生变化则其他元数据属性都将被刷新。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

titlestring否是

标题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

artiststring否是

艺术家。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

authorstring否是

专辑作者。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

avQueueName12+string否是歌单（歌曲列表）名称。avQueueId11+string否是歌单（歌曲列表）唯一标识Id。avQueueImage11+[image.PixelMap](Interface (PixelMap).md) | string否是

歌单（歌曲列表）封面图。

图片的像素数据或者图片路径地址（本地路径或网络路径）。应用通过setAVMetadata设置图片数据。

- 设置的数据类型为PixelMap时，通过getAVMetadata获取的将为PixelMap。

- 设置为url图片路径，获取的为url图片路径。

albumstring否是

专辑名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

writerstring否是

词作者。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

composerstring否是作曲者。durationnumber否是

媒体时长，单位毫秒（ms）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

mediaImage[image.PixelMap](Interface (PixelMap).md) | string否是

图片的像素数据或者图片路径地址(本地路径或网络路径)。应用通过setAVMetadata设置图片数据。

- 设置的数据类型为PixelMap时，通过getAVMetadata获取的将为PixelMap。

- 设置为url图片路径，获取的为url图片路径。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

bundleIcon18+[image.PixelMap](Interface (PixelMap).md)是是应用图标图片的像素数据。只读类型，不从应用侧设置。publishDateDate否是发行日期。subtitlestring否是

子标题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

descriptionstring否是

媒体描述。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

lyricstring否是

媒体歌词内容。应用需将歌词内容拼接为一个字符串传入。

字符串长度需<40960字节。

**说明：** 系统支持简单版的LRC格式（Simple LRC format）的歌词文本内容。当传入的歌词内容不规范（例如：出现重复的时间戳等），将导致解析失败，并在系统中显示异常。

singleLyricText17+string否是

单条媒体歌词内容。应用需将歌词内容拼接为一个字符串传入（不包含时间戳）。

字符串长度<40960字节。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

previousAssetIdstring否是

上一首媒体ID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

nextAssetIdstring否是

下一首媒体ID。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

filter11+number否是

当前session支持的协议，默认为TYPE_CAST_PLUS_STREAM。具体取值参考[ProtocolType](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__protocoltype11)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

drmSchemes12+Array<string>否是当前session支持的DRM方案，取值为DRM方案uuid。skipIntervals11+[SkipIntervals](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__skipintervals11)否是快进快退支持的时间间隔。默认为SECONDS_15，即15秒。displayTags11+number否是媒体资源的金标类型，取值参考[DisplayTag](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__displaytag11)。[]()[]()

#### AVMediaDescription10+

播放列表媒体元数据的相关属性。

名称类型只读可选说明assetIdstring否否

播放列表媒体ID。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

titlestring否是

播放列表媒体标题。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

subtitlestring否是

播放列表媒体子标题。在使用了cast+协议的音频投播场景下，暂不支持使用该属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

descriptionstring否是

播放列表媒体描述的文本。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

mediaImage[image.PixelMap](Interface (PixelMap).md) | string否是

播放列表媒体图片像素数据。在使用了cast+协议的音频投播场景下，暂不支持使用该属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

extrasRecord<string, Object>否是

播放列表媒体额外字段。

**说明：**

从API version 20开始参数类型变更为Record<string, Object>，API version 19及之前的版本extras的参数类型为：{[key: string]: Object}，无需适配仍可使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

mediaUristring否是

播放列表媒体URI。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

mediaTypestring否是

播放列表媒体类型。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

mediaSizenumber否是

播放列表媒体的大小。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

albumTitlestring否是

播放列表媒体专辑标题。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

albumCoverUristring否是

播放列表媒体专辑封面URI。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

lyricContentstring否是

播放列表媒体歌词内容。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

lyricUristring否是

播放列表媒体歌词URI。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

artiststring否是

播放列表媒体专辑作者。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

fdSrc[media.AVFileDescriptor](Interfaces (其他) (arkts-apis-media-i).md#ZH-CN_TOPIC_0000002497605902__avfiledescriptor9)否是

播放列表媒体本地文件的句柄。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

dataSrc12+[media.AVDataSrcDescriptor](Interfaces (其他) (arkts-apis-media-i).md#ZH-CN_TOPIC_0000002497605902__avdatasrcdescriptor10)否是

播放列表数据源描述。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

pcmSrc20+boolean否是

播放列表是否使用PCM数据源。true表示使用PCM数据源，false表示不使用PCM数据源。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

drmScheme12+string否是

播放列表媒体支持的DRM方案，由uuid表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

durationnumber否是

播放列表媒体播放时长。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

startPositionnumber否是

播放列表媒体起始播放位置。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

creditsPositionnumber否是

播放列表媒体的片尾播放位置。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

appNamestring否是

播放列表提供的应用的名字。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

displayTags11+number否是

媒体资源的金标类型，取值参考[DisplayTag](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__displaytag11)。在使用了cast+协议的音频投播场景下，暂不支持使用该属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

launchClientData20+string否是

投播过程中应用程序向接收方发送的自定义数据。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### AVQueueItem10+

播放列表中单项的相关属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明itemIdnumber否否播放列表中单项的ID。description[AVMediaDescription](#ZH-CN_TOPIC_0000002529285755__avmediadescription10)否是播放列表中单项的媒体元数据。[]()[]()

#### AVPlaybackState10+

媒体播放状态的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明state[PlaybackState](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__playbackstate10)否是

播放状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

speednumber否是

播放倍速。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

position[PlaybackPosition](#ZH-CN_TOPIC_0000002529285755__playbackposition10)否是

播放位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

bufferedTimenumber否是

缓冲时间。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

loopMode[LoopMode](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__loopmode10)否是

循环模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

isFavoriteboolean否是

表示是否收藏。true表示收藏，false表示不收藏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

activeItemIdnumber否是

正在播放的媒体Id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

volumenumber否是

正在播放的媒体音量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

maxVolume11+number否是

最大音量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

muted11+boolean否是

当前是否是静音状态。true表示是，false表示不是。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

duration11+number否是当前媒体资源的时长。videoWidth11+number否是

媒体资源的视频宽度，单位为像素（px）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

videoHeight11+number否是

媒体资源的视频高度，单位为像素（px）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

extrasRecord<string, Object>否是

自定义媒体数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

[]()[]()

#### PlaybackPosition10+

媒体播放位置的相关属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明elapsedTimenumber否否已用时间，单位毫秒（ms）。updateTimenumber否否更新时间，单位毫秒（ms）。[]()[]()

#### CallMetadata11+

通话会话元数据相关属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明namestring否是来电人姓名（别名）。phoneNumberstring否是来电电话号码。avatar[image.PixelMap](Interface (PixelMap).md)否是来电人头像。[]()[]()

#### AVCallState11+

通话状态相关属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明state[CallState](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__callstate11)否否当前通话状态。mutedboolean否否表示通话mic是否静音。 true表示是静音，false表示不是静音。[]()[]()

#### DeviceInfo10+

播放设备的相关信息。

名称类型只读可选说明castCategory[AVCastCategory](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__avcastcategory10)否否

投播的类别。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

deviceIdstring否否

播放设备的ID。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

deviceNamestring否否

播放设备的名称。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

deviceTypeDeviceType否否

播放设备的类型。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

supportedProtocols11+number否是

播放设备支持的协议。默认为TYPE_LOCAL。具体取值参考[ProtocolType](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__protocoltype11)。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

supportedDrmCapabilities12+Array<string>否是

播放设备支持的DRM能力。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

manufacturer13+string否是

播放设备生产厂家。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

modelName13+string否是

播放设备型号名称。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

audioCapabilities20+[AudioCapabilities](#ZH-CN_TOPIC_0000002529285755__audiocapabilities20)否是

播放设备支持的音频能力。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

supportedPullClients20+Array<number>否是

支持拉端客户端的ID集合（只有支持4K投播的设备会返回此字段）。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### OutputDeviceInfo10+

播放设备的相关信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明devicesArray<[DeviceInfo](#ZH-CN_TOPIC_0000002529285755__deviceinfo10)>否否播放设备的集合。[]()[]()

#### AVControlCommand10+

会话接受的命令的对象描述。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明command[AVControlCommandType](../../topics/networking/Types (arkts-apis-avsession-t).md#ZH-CN_TOPIC_0000002497605764__avcontrolcommandtype10)否否

命令（不同命令对应不同参数）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

parameter[LoopMode](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__loopmode10) | string | number否是

命令对应的参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

commandInfo22+[CommandInfo](#ZH-CN_TOPIC_0000002529285755__commandinfo22)否是命令信息。[]()[]()

#### AVCastPickerOptions14+

拉起的投播半模态窗口相关属性。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

名称类型只读可选说明sessionType[AVSessionType](../../topics/networking/Types (arkts-apis-avsession-t).md#ZH-CN_TOPIC_0000002497605764__avsessiontype10)否是

会话类型，默认值为audio。

当前仅支持audio、video会话类型。如果传入voice_call、video_call，将按照传入默认值audio处理。

[]()[]()

#### AudioCapabilities20+

表示投播设备支持的音频能力。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

名称类型只读可选说明streamInfosArray<[audio.AudioStreamInfo](Interfaces (其他) (arkts-apis-audio-i).md#ZH-CN_TOPIC_0000002497445724__audiostreaminfo8)>是否音频能力参数的列表。[]()[]()

#### CommandInfo22+

定义要发送到会话的命令信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明callerBundleNamestring否是调用方应用包名。callerModuleNamestring否是调用方应用模块名。callerDeviceIdstring否是调用方设备ID。callerType[CallerType](../../topics/networking/Enums (arkts-apis-avsession-e).md#ZH-CN_TOPIC_0000002529445729__callertype22)否是调用方来源。