[]()[]()

# Interfaces (其他)

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### AVFileDescriptor9+

音视频文件资源描述，一种特殊资源的播放方式，使用场景：应用中的音频资源被连续存储在同一个文件中，需要根据偏移量和长度进行播放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称类型只读可选说明fdnumber否否资源句柄，通过[resourceManager.getRawFd](../../modules/ohos/@ohos.resourceManager (资源管理).md#ZH-CN_TOPIC_0000002497445338__getrawfd9)获取，也可以通过[fs.open](../../modules/ohos/@ohos.file.fs (文件管理).md#ZH-CN_TOPIC_0000002529445221__fsopen)获取。offsetnumber否是资源偏移量，默认值为0，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。lengthnumber否是资源长度，默认值为文件中从偏移量开始的剩余字节，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。[]()[]()

#### AVDataSrcDescriptor10+

音视频文件资源描述，用于DataSource播放方式，使用场景：应用在未获取完整音视频资源时，允许用户创建播放实例并开始播放，达到提前播放的目的。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

名称类型只读可选说明fileSizenumber否否待播放文件大小（字节），-1代表大小未知。如果fileSize设置为-1，播放模式类似于直播，不能进行seek及setSpeed操作，不能设置loop属性，因此不能重新播放。callback(buffer: ArrayBuffer, length: number, pos?: number) => number否否

用户设置的回调函数，用于填写数据。

- buffer: 表示被填写的内存，必选。

- length: 表示被填写内存的最大长度，必选。

- pos：表示填写的数据在资源文件中的位置，可选。当fileSize设置为-1时，该参数禁止被使用。

- 返回值，number类型，返回填充数据的长度。返回-1表示到达流的末尾，返回-2表示遇到不可恢复的错误。

[]()[]()

#### SubtitleInfo12+

外挂字幕信息，使用场景：订阅外挂字幕事件，回调返回外挂字幕详细信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称类型只读可选说明textstring否是字幕文本信息。startTimenumber否是显示当前字幕文本的开始时间（单位：毫秒）。durationnumber否是显示当前字幕文本的持续时间（单位：毫秒）。[]()[]()

#### SeiMessage18+

SEI信息内容，描述SEI信息的负载类型和数据。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称类型只读可选说明payloadTypenumber否否SEI信息的负载类型。payloadArrayBuffer否否SEI信息的负载数据。[]()[]()

#### MediaDescription8+

通过key-value方式获取媒体信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称类型只读可选说明[key: string]Object否是该键值对支持的key取值范围，请参考[MediaDescriptionKey](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__mediadescriptionkey8)；每个key值的Object类型和范围，请参考[MediaDescriptionKey](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__mediadescriptionkey8)对应Key值的说明。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

function printfItemDescription(obj: media.MediaDescription, key: string) {
  let property: Object = obj[key];
  console.info('audio key is ' + key); // 通过key值获取对应的value。key值具体可见MediaDescriptionKey。
  console.info('audio value is ' + property); //对应key值得value。其类型可为任意类型，具体key对应value的类型可参考MediaDescriptionKey。
}

let avPlayer: media.AVPlayer | undefined = undefined;
media.createAVPlayer((err: BusinessError, player: media.AVPlayer) => {
  if(player != null) {
    avPlayer = player;
    console.info(`Succeeded in creating AVPlayer`);
    avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
      if (arrList != null) {
        for (let i = 0; i < arrList.length; i++) {
          printfItemDescription(arrList[i], media.MediaDescriptionKey.MD_KEY_TRACK_TYPE);  //打印出每条轨道MD_KEY_TRACK_TYPE的值。
        }
      } else {
        console.error(`Failed to get TrackDescription, error:${error}`);
      }
    });
  } else {
    console.error(`Failed to create AVPlayer, error message:${err.message}`);
  }
});
```

[]()[]()

#### PlaybackInfo12+

通过key-value方式获取播放信息。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称类型只读可选说明[key: string]Object否是

该键值对支持的key取值范围，请参考[PlaybackInfoKey](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__playbackinfokey12)。

每个key值的Object类型和范围，请参考[PlaybackInfoKey](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__playbackinfokey12)。

[]()[]()

#### AVRecorderConfig9+

表示音视频录制的参数设置。

通过audioSourceType和videoSourceType区分纯音频录制、纯视频录制或音视频录制。纯音频录制时，仅需要设置audioSourceType；纯视频录制时，仅需要设置videoSourceType；音视频录制时，audioSourceType和videoSourceType均需要设置。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

名称类型只读可选说明audioSourceType[AudioSourceType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__audiosourcetype9)否是

选择录制的音频源类型。选择音频录制时必填。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

videoSourceType[VideoSourceType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__videosourcetype9)否是选择录制的视频源类型。选择视频录制时必填。profile[AVRecorderProfile](#ZH-CN_TOPIC_0000002497605902__avrecorderprofile9)否否

录制的profile，必要参数。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

urlstring否否

录制输出URL：fd://xx (fd number) ，必要参数。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

fileGenerationMode12+[FileGenerationMode](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__filegenerationmode12)否是创建媒体文件的模式，配合[on('photoAssetAvailable')](Interface (AVRecorder).md#ZH-CN_TOPIC_0000002529445863__onphotoassetavailable12)监听使用。rotation(deprecated)number否是

录制的视频旋转角度，mp4格式支持0、90、180和270，默认值为0。

从API version 6开始支持，从API version 12开始废弃。建议使用[AVMetadata](#ZH-CN_TOPIC_0000002497605902__avmetadata11).videoOrientation替代。

如果同时设置两个值，将会采用[AVMetadata](#ZH-CN_TOPIC_0000002497605902__avmetadata11).videoOrientation。

location(deprecated)[Location](#ZH-CN_TOPIC_0000002497605902__location)否是

录制的地理位置，默认不记录地理位置信息。

从API version 6开始支持，从API version 12开始废弃。建议使用 [AVMetadata](#ZH-CN_TOPIC_0000002497605902__avmetadata11).location。

如果同时设置两个值，将会采用[AVMetadata](#ZH-CN_TOPIC_0000002497605902__avmetadata11).location。

metadata12+[AVMetadata](#ZH-CN_TOPIC_0000002497605902__avmetadata11)否是设置元数据信息。详细内容请参考 [AVMetadata](#ZH-CN_TOPIC_0000002497605902__avmetadata11)。maxDuration18+number否是设置录制的最大时长，单位为秒，有效值取值范围[1, 2^31-1]，无效输入会重置为最大值。录制到达设定时长后，录制会自动停止，并通过stateChange回调录制状态，[AVRecorderState](../../topics/networking/Types (arkts-apis-media-t).md#ZH-CN_TOPIC_0000002529285893__avrecorderstate9) = 'stopped'，[StateChangeReason](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__statechangereason9) = BACKGROUND。[]()[]()

#### AVRecorderProfile9+

音视频录制的配置文件。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

名称类型只读可选说明audioBitratenumber否是

音频编码比特率，选择音频录制时必填。

支持范围：

- AAC编码格式支持比特率范围[32000, 500000]。

- G711-mulaw编码格式支持比特率大小：64000。

- MP3编码格式支持范围[8000, 16000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 320000]。

当使用MP3编码格式时，采样率和比特率的映射关系：

- 采样率使用16K以下时，对应比特率范围为[8000 - 64000]。

- 采样率使用16K~32K时对应的比特率范围为[8000, 160000]。

- 采样率使用32K以上时对应的比特率范围为[32000, 320000]。

- AMR_NB编码格式支持比特率范围[4750, 5150, 5900, 6700, 7400, 7950, 10200, 12200]。

- AMR_WB编码格式支持比特率范围[6600, 8850, 12650, 14250, 15850, 18250, 19850, 23050, 23850]。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

audioChannelsnumber否是

音频采集声道数，选择音频录制时必填。

- AAC编码格式支持范围[1, 8]。

- G711-mulaw编码格式支持大小：1。

- MP3编码格式支持范围[1, 2]。

- AMR-NB和AMR-WB编码格式支持大小：1。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

audioCodec[CodecMimeType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__codecmimetype8)否是

音频编码格式，选择音频录制时必填。

当前支持AUDIO_AAC、AUDIO_MP3、AUDIO_G711MU、AUDIO_AMR_NB和AUDIO_AMR_WB。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

aacProfile22+[AacProfile](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__aacprofile22)否是

音频编码扩展格式，默认为AAC_LC格式。

当前支持类型：AAC_LC、AAC_HE和AAC_HE_V2。

**元服务API：** 从API version 22 开始，该接口支持在元服务中使用。

audioSampleRatenumber否是

音频采样率，选择音频录制时必填。

支持范围：

- AAC编码支持采样率范围[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000]。

- G711-mulaw编码支持采样率大小：8000。

- MP3编码支持采样率范围[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000]。

- AMR_NB编码支持采样率大小：8000。

- AMR_WB编码支持采样率大小：16000。

可变比特率模式，码率仅作参考。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

fileFormat[ContainerFormatType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__containerformattype8)否否

文件的容器格式，必要参数。当前支持MP4、M4A、MP3、WAV、AMR、AAC封装格式，当前AAC音频封装默认为ADTS帧头格式。不支持在MP4封装格式下使用AUDIO_MP3编码格式。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

videoBitratenumber否是视频编码比特率，选择视频录制时必填，支持范围[10000, 100000000]。videoCodec[CodecMimeType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__codecmimetype8)否是视频编码格式，选择视频录制时必填。当前支持VIDEO_AVC和VIDEO_HEVC。videoFrameWidthnumber否是视频帧的宽，选择视频录制时必填，支持范围[176, 4096]。videoFrameHeightnumber否是视频帧的高，选择视频录制时必填，支持范围[144, 4096]。videoFrameRatenumber否是视频帧率，选择视频录制时必填，推荐范围[1, 60]。isHdr11+boolean否是HDR编码，选择视频录制时选填，isHdr默认为false，对应编码格式没有要求，isHdr为true时，对应的编码格式必须为video/hevc。enableTemporalScale12+boolean否是视频录制是否支持时域分层编码功能，选择视频录制时选填，enableTemporalScale默认为false。设置为true时，编码输出的码流中部分帧可以支持跳过不编码。enableBFrame20+boolean否是

视频录制是否启用B帧编码。true表示启用B帧编码（仅在视频编码格式为H.265且设备硬件支持的情况下生效），false表示不启用B帧编码。

该参数为视频录制场景下的可选项，默认值为false。

[]()[]()

#### 音频参数配置对照表

此处提供音频参数配置的对照表，每项的具体释义，可查看下述字段解释。

编码格式封装格式采样率比特率声道数AUDIO_AACMP4,M4A[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000][32000-500000][1-8]AUDIO_MP3MP3[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000]

- 采样率使用16000以下时，对应比特率范围为[8000, 16000, 32000, 40000, 48000, 56000, 64000]。

- 采样率使用16000~32000时对应的比特率范围为[8000, 16000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000]。

- 采样率使用32000以上时对应的比特率范围为[32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 320000]。

[1-2]AUDIO_G711MUWAV[8000][64000][1]AUDIO_AMR_NB18+AMR[8000][4750, 5150, 5900, 6700, 7400, 7950, 10200, 12200][1]AUDIO_AMR_WB18+AMR[16000][6600, 8850, 12650, 14250, 15850, 18250, 19850, 23050, 23850][1][]()[]()

#### Location

视频录制的地理位置。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称类型只读可选说明latitudenumber否否地理位置的纬度，取值范围为[-90, 90]。longitudenumber否否地理位置的经度，取值范围为[-180, 180]。[]()[]()

#### EncoderInfo11+

编码器和规格参数。

系统能力：SystemCapability.Multimedia.Media.AVRecorder

名称类型只读可选说明mimeType[CodecMimeType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__codecmimetype8)否否编码器MIME类型名称。typestring否否编码器类型，audio表示音频编码器，video表示视频编码器。bitRate[Range](#ZH-CN_TOPIC_0000002497605902__range11)否是比特率，包含该编码器的最大和最小值。frameRate[Range](#ZH-CN_TOPIC_0000002497605902__range11)否是视频帧率，包含帧率的最大和最小值，仅视频编码器拥有。width[Range](#ZH-CN_TOPIC_0000002497605902__range11)否是视频帧的宽度，包含宽度的最大和最小值，仅视频编码器拥有。height[Range](#ZH-CN_TOPIC_0000002497605902__range11)否是视频帧的高度，包含高度的最大和最小值，仅视频编码器拥有。channels[Range](#ZH-CN_TOPIC_0000002497605902__range11)否是音频采集声道数，包含声道数的最大和最小值，仅音频编码器拥有。sampleRateArray<number>否是音频采样率，包含所有可以使用的音频采样率值数组，具体数值依赖编码器类型，仅音频编码器拥有。[]()[]()

#### Range11+

表示一个类型的范围。

系统能力：SystemCapability.Multimedia.Media.AVRecorder

名称类型只读可选说明minnumber否否范围的最小值。maxnumber否否范围的最大值。[]()[]()

#### AVTranscoderConfig12+

表示视频转码的参数设置。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

名称类型只读可选说明audioBitratenumber否是

输出音频的码率，单位为比特率（bps），支持范围[1, 500000]。默认设置为48Kbps。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

audioCodec[CodecMimeType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__codecmimetype8)否是

输出音频的编码格式，当前仅支持AAC。默认设置为AAC。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

fileFormat[ContainerFormatType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__containerformattype8)否否

输出视频文件的封装格式，当前视频文件仅支持MP4。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

videoBitratenumber否是

输出视频的码率，单位为比特率（bps）。默认码率按输出视频的分辨率设置，[240p, 480P]默认码率值为1Mbps，(480P, 720P]默认码率值为2Mbps，(720P, 1080P]默认码率值为4Mbps，1080P及以上默认值为8Mbps。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

videoCodec[CodecMimeType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__codecmimetype8)否是

输出视频的编码格式，当前仅支持AVC和HEVC。若源视频编码格式为HEVC，则默认设置为HEVC，否则默认设置为AVC。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

videoFrameWidthnumber否是

输出视频帧的宽，单位为像素（px），支持范围[240, 3840]。默认设置为源视频帧的宽。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

videoFrameHeightnumber否是

输出视频帧的高，单位为像素（px），支持范围[240, 2160]。默认设置为源视频帧的高。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

enableBFrame20+boolean否是

转码使能B帧编码。true表示开启B帧编码，默认为不开启B帧编码。

B帧视频编码相关的约束和限制可以参考文档[B帧视频编码约束和限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding-b-frame#约束和限制)。如果当前不符合B帧视频编码的约束和限制，将忽略B帧，按不使能B帧进行编码。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

[]()[]()

#### AVMetadata11+

音视频元数据，包含各个元数据字段。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

名称类型只读可选说明albumstring否是专辑的标题。不支持AVRecorder设置该属性。albumArtiststring否是专辑的艺术家。不支持AVRecorder设置该属性。artiststring否是媒体资源的艺术家。不支持AVRecorder设置该属性。authorstring否是媒体资源的作者。不支持AVRecorder设置该属性。dateTimestring否是媒体资源的创建时间。不支持AVRecorder设置该属性。dateTimeFormatstring否是媒体资源的创建时间，按YYYY-MM-DD HH:mm:ss格式输出。不支持AVRecorder设置该属性。composerstring否是媒体资源的作曲家。不支持AVRecorder设置该属性。durationstring否是媒体资源的时长。不支持AVRecorder设置该属性。genrestring否是媒体资源的类型或体裁。hasAudiostring否是媒体资源是否包含音频。不支持AVRecorder设置该属性。hasVideostring否是媒体资源是否包含视频。不支持AVRecorder设置该属性。mimeTypestring否是媒体资源的mime类型。不支持AVRecorder设置该属性。trackCountstring否是媒体资源的轨道数量。不支持AVRecorder设置该属性。sampleRatestring否是音频的采样率，单位为赫兹（Hz）。不支持AVRecorder设置该属性。titlestring否是媒体资源的标题。当前版本为只读参数。不支持AVRecorder设置该属性。videoHeightstring否是视频的高度，单位为像素（px）。不支持AVRecorder设置该属性。videoWidthstring否是视频的宽度，单位为像素（px）。不支持AVRecorder设置该属性。videoOrientationstring否是视频的旋转方向，单位为度（°）。hdrType12+[HdrType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__hdrtype12)否是媒体资源的HDR类型。不支持AVRecorder设置该属性。location12+[Location](#ZH-CN_TOPIC_0000002497605902__location)否是视频的地理位置信息。customInfo12+Record<string, string>否是从moov.meta.list 获取的自定义参数键值映射。tracks20+Array<[MediaDescription](#ZH-CN_TOPIC_0000002497605902__mediadescription8)>否是媒体资源的轨道信息。不支持AVRecorder设置该属性。[]()[]()

#### AVMetadata.tracks支持的MediaDescriptionKey8+说明

AVMetadata.tracks支持的[MediaDescriptionKey](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__mediadescriptionkey8)的范围如下：

名称值适用的轨道类型MD_KEY_TRACK_INDEX'track_index'全部MD_KEY_TRACK_TYPE'track_type'全部MD_KEY_CODEC_MIME'codec_mime'音频、视频MD_KEY_WIDTH'width'视频MD_KEY_HEIGHT'height'视频MD_KEY_FRAME_RATE'frame_rate'视频MD_KEY_AUD_CHANNEL_COUNT'channel_count'音频MD_KEY_AUD_SAMPLE_RATE'sample_rate'音频MD_KEY_HDR_TYPE12+'hdr_type'视频MD_KEY_ORIGINAL_WIDTH21+'original_width'视频MD_KEY_ORIGINAL_HEIGHT21+'original_height'视频MD_KEY_BITRATE'bitrate'音频、视频（从API version 21开始，AVMetadata.tracks支持该值获取。）MD_KEY_AUD_SAMPLE_DEPTH12+'sample_depth'音频（从API version 21开始，AVMetadata.tracks支持该值获取。）[]()[]()

#### PixelMapParams12+

获取视频缩略图时，输出缩略图的格式参数。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

名称类型只读可选说明widthnumber否是输出的缩略图宽度。应保证大于0且不大于原始视频宽度。否则返回的缩略图不会进行缩放。heightnumber否是输出的缩略图高度。应保证大于0且不大于原始视频高度。否则返回的缩略图不会进行缩放。[]()[]()

#### OutputSize20+

用于获取视频缩略图时，来定义输出图像大小。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

名称类型只读可选说明widthnumber否是

输出的缩略图宽度。

- 如果该值小于0，宽度是视频的原始宽度。

- 如果值为0或未分配任何值，缩放比例同高度比例。

- 如果宽度和高度均未分配任意值，则输出原始视频帧的宽度和高度。

heightnumber否是

输出的缩略图高度。

- 如果该值小于0，高度是视频的原始高度。

- 如果值为0或未分配任何值，缩放比例同宽度比例。

- 如果宽度和高度均未分配任意值，则输出原始视频帧的宽度和高度。

[]()[]()

#### MediaStream19+

媒体流数据信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称类型只读可选说明urlstring否否媒体资源链接，当前仅支持http或者https。widthnumber否否媒体资源视频宽像素值。未知时可以填0，此时将无法通过[PlaybackStrategy](#ZH-CN_TOPIC_0000002497605902__playbackstrategy12)优选匹配。heightnumber否否媒体资源视频高像素值。未知时可以填0，此时将无法通过[PlaybackStrategy](#ZH-CN_TOPIC_0000002497605902__playbackstrategy12)优选匹配。bitratenumber否否媒体资源码率值，单位bps。[]()[]()

#### MediaSourceLoader18+

用于定义媒体数据加载器，需要应用程序对其进行实现。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称类型只读可选说明open[SourceOpenCallback](../../topics/networking/Types (arkts-apis-media-t).md#ZH-CN_TOPIC_0000002529285893__sourceopencallback18)否否由应用程序实现的回调函数，用于处理资源打开请求。read[SourceReadCallback](../../topics/networking/Types (arkts-apis-media-t).md#ZH-CN_TOPIC_0000002529285893__sourcereadcallback18)否否由应用程序实现的回调函数，用于处理资源读取请求。close[SourceCloseCallback](../../topics/networking/Types (arkts-apis-media-t).md#ZH-CN_TOPIC_0000002529285893__sourceclosecallback18)否否由应用程序实现的回调函数，用于处理资源关闭请求。

**示例：**

```ets
import HashMap from '@ohos.util.HashMap';

let headers: Record<string, string> = {"User-Agent" : "User-Agent-Value"};
let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://xxx",  headers);
let uuid: number = 1;
let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();
let mediaSourceLoader: media.MediaSourceLoader = {
  open: (request: media.MediaSourceLoadingRequest) => {
    console.info(`Opening resource: ${request.url}`);
    // 成功打开资源，返回唯一的句柄, 保证uuid和request对应。
    uuid += 1;
    requests.set(uuid, request);
    return uuid;
  },
  read: (uuid: number, requestedOffset: number, requestedLength: number) => {
    console.info(`Reading resource with handle ${uuid}, offset: ${requestedOffset}, length: ${requestedLength}`);
    // 判断uuid是否合法、存储read请求，不要在read请求阻塞去推送数据和头信息。
  },
  close: (uuid: number) => {
    console.info(`Closing resource with handle ${uuid}`);
    // 清除当前uuid相关资源。
    requests.remove(uuid);
  }
};

mediaSource.setMediaResourceLoaderDelegate(mediaSourceLoader);
let playStrategy : media.PlaybackStrategy = {
  preferredBufferDuration: 20,
};

async function setupPlayer() {
  let player = await media.createAVPlayer();
  player.setMediaSource(mediaSource, playStrategy);
}
```

[]()[]()

#### PlaybackStrategy12+

播放策略。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称类型只读可选说明preferredWidthnumber否是

播放策略首选宽度，设置范围为大于0的整数，如1080，单位为像素（px）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

preferredHeightnumber否是

播放策略首选高度，设置范围为大于0的整数，如1920，单位为像素（px）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

preferredBufferDurationnumber否是

播放策略首选缓冲持续时间，单位为秒（s），取值范围[1, 20]。

具体使用方式可参考[在线视频播放卡顿优化实践](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-online-video-playback-lags-practice)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

preferredHdrboolean否是

表示播放策略是否为hdr。true表示是，false表示不是，默认为false。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

enableSuperResolution18+boolean否是

表示是否使能超分功能。true表示使能超分，false表示不使能超分，默认为false。

若不使能超分，则后续不能调用超分相关接口。若使能超分，则超分功能默认开启，默认目标分辨率为1920x1080，单位为像素。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

showFirstFrameOnPrepare17+boolean否是

播放策略true是Prepare之后显示视频起播首帧，false是Prepare之后不显示视频起播首帧，默认不显示。

**元服务API：** 从API version 17开始，该接口支持在元服务中使用。

mutedMediaType[MediaType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__mediatype8)否是

关闭输出的媒体类型。

API version 12-19，仅支持设置MediaType.MEDIA_TYPE_AUD。API version 20起，增加支持MediaType.MEDIA_TYPE_VID。

preferredAudioLanguage13+string否是

播放策略首选音轨语言。dash场景下应用可按需设置。非dash场景暂不支持，建议缺省。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

preferredSubtitleLanguage13+string否是

播放策略首选字幕语言。dash场景下应用可按需设置。非dash场景暂不支持，建议缺省。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

preferredBufferDurationForPlaying18+number否是

播放策略首选起播缓冲水线。当起播缓冲时间超过该值，开始播放。单位为秒（s），取值范围[0, 20]。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

thresholdForAutoQuickPlay18+number否是

智能追帧水线，单位为秒（s），取值应不小于2s，且需大于起播缓冲水线，默认设置为5s。

播放策略可以通过设置智能追帧水线来保证直播的实时性。flv直播场景下应用可按需设置，非flv直播场景暂不支持。网络状态的变化可能会导致播放器在某段时间内积压大量数据。播放器会定期检查当前播放时间与缓存中最新的帧时间戳之间的差值，当这个差值过大时，播放器将以1.2倍速开始智能追帧。[speedDone事件](Interface (AVPlayer).md#ZH-CN_TOPIC_0000002529285889__onspeeddone9)会回调特定值100，表示智能追帧开启成功。当差值小于起播缓冲水线时，则停止追帧并恢复到正常播放速度。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

keepDecodingOnMute20+boolean否是

表示在关闭视频媒体时解码器是否继续运行，用于方便快速打开媒体。目前仅支持视频。默认设置为false，表示当媒体关闭时，相应的解码器将停止运行以减少功耗。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### AVScreenCaptureStrategy20+

录屏策略。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

名称类型只读可选说明keepCaptureDuringCallboolean否是蜂窝通话时是否保持录屏。enableBFrameboolean否是

录屏是否使能B帧编码。true表示录屏文件使能B帧编码，false表示录屏文件禁用B帧编码，默认是false。

B帧视频编码相关的约束和限制可以参考文档[B帧视频编码约束和限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding-b-frame#约束和限制)。如果当前不符合B帧视频编码的约束和限制，则正常录制不含B帧的视频，不会返回错误。

[]()[]()

#### AVScreenCaptureRecordConfig12+

表示录屏参数配置。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

名称类型只读可选说明fdnumber否否录制输出的文件fd。frameWidthnumber否是录屏的视频宽度，默认屏幕宽度，根据不同屏幕默认值不同，单位px。frameHeightnumber否是录屏的视频高度，默认屏幕高度，根据不同屏幕默认值不同，单位px。videoBitratenumber否是录屏的视频比特率，默认10000000。audioSampleRatenumber否是录屏的音频采样率，内录的系统音和外录的麦克风都是用此采样率，默认48000，仅支持设置48000或16000。audioChannelCountnumber否是录屏的音频通道数，内录的系统音和外录的麦克风都是用此通道数，默认2声道，仅支持设置1或2声道。audioBitratenumber否是录屏的音频比特率，内录的系统音和外录的麦克风都是用此比特率，默认96000。preset[AVScreenCaptureRecordPreset](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__avscreencapturerecordpreset12)否是录屏使用的编码和封装格式，默认SCREEN_RECORD_PRESET_H264_AAC_MP4格式。displayId15+number否是指定录屏使用的屏幕，默认主屏幕。fillMode18+[AVScreenCaptureFillMode](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__avscreencapturefillmode18)否是录屏时视频流的填充模式。strategy20+[AVScreenCaptureStrategy](#ZH-CN_TOPIC_0000002497605902__avscreencapturestrategy20)否是录屏策略。[]()[]()

#### AudioRecorderConfig(deprecated)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorderConfig](#ZH-CN_TOPIC_0000002497605902__avrecorderconfig9)替代。

表示音频的录音配置。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

名称类型只读可选说明audioEncoder[AudioEncoder](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__audioencoderdeprecated)否是

音频编码格式，默认设置为AAC_LC。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用audioEncoderMime替代。

audioEncodeBitRatenumber否是

音频编码比特率，默认值为48000。

**说明：** 从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorderProfile](#ZH-CN_TOPIC_0000002497605902__avrecorderprofile9)中的audioBitrate替代。

audioSampleRatenumber否是

音频采集采样率，默认值为48000。

可变比特率模式，码率仅作参考。

**说明：** 从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorderProfile](#ZH-CN_TOPIC_0000002497605902__avrecorderprofile9)中的audioSampleRate替代。

numberOfChannelsnumber否是

音频采集声道数，默认值为2。

**说明：** 从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorderProfile](#ZH-CN_TOPIC_0000002497605902__avrecorderprofile9)中的audioChannels替代。

format[AudioOutputFormat](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__audiooutputformatdeprecated)否是

音频输出封装格式，默认设置为MPEG_4。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用fileFormat替代。

location[Location](#ZH-CN_TOPIC_0000002497605902__location)否是

音频采集的地理位置。

**说明：** 从API version 6开始支持，从API version 9开始废弃，建议使用[AVMetadata](#ZH-CN_TOPIC_0000002497605902__avmetadata11)中的location替代。

uristring否否

音频输出URI：fd://xx (fd number)

文件需要由调用者创建，并赋予适当的权限。

**说明：** 从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorderConfig](#ZH-CN_TOPIC_0000002497605902__avrecorderconfig9)中的url替代。

audioEncoderMime8+[CodecMimeType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__codecmimetype8)否是

容器编码格式。

**说明：** 从API version 8开始支持，从API version 9开始废弃，建议使用[AVRecorderProfile](#ZH-CN_TOPIC_0000002497605902__avrecorderprofile9)中的audioCodec替代。

fileFormat8+[ContainerFormatType](../../topics/networking/Enums (arkts-apis-media-e).md#ZH-CN_TOPIC_0000002497445922__containerformattype8)否是

音频编码格式。

**说明：** 从API version 8开始支持，从API version 9开始废弃，建议使用[AVRecorderProfile](#ZH-CN_TOPIC_0000002497605902__avrecorderprofile9)中的fileFormat替代。