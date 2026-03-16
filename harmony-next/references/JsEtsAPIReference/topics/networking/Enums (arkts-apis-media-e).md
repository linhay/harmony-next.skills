[]()[]()

# Enums

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### AVErrorCode9+

[媒体错误码](../../errors/Media错误码.md)类型枚举。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明AVERR_OK0表示操作成功。AVERR_NO_PERMISSION201表示无权限执行此操作。AVERR_INVALID_PARAMETER401表示传入入参无效。AVERR_UNSUPPORT_CAPABILITY801表示当前版本不支持该API能力。AVERR_NO_MEMORY5400101表示系统内存不足或服务数量达到上限。AVERR_OPERATE_NOT_PERMIT5400102表示当前状态不允许或无权执行此操作。AVERR_IO5400103表示数据流异常信息。AVERR_TIMEOUT5400104表示系统或网络响应超时。AVERR_SERVICE_DIED5400105表示服务进程死亡。AVERR_UNSUPPORT_FORMAT5400106表示不支持当前媒体资源的格式。AVERR_AUDIO_INTERRUPTED11+5400107表示音频焦点被抢占。AVERR_IO_HOST_NOT_FOUND14+5411001

表示解析或链接服务端地址错误。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_IO_CONNECTION_TIMEOUT14+5411002

表示网络连接超时。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_IO_NETWORK_ABNORMAL14+5411003

表示网络异常导致的数据或链路异常。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_IO_NETWORK_UNAVAILABLE14+5411004

表示网络被禁用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_IO_NO_PERMISSION14+5411005

表示无访问权限。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_IO_REQUEST_DENIED14+5411006

表示客户端请求参数错误或超出处理能力。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_IO_RESOURCE_NOT_FOUND14+5411007

表示无可用网络资源。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_IO_SSL_CLIENT_CERT_NEEDED14+5411008

表示服务端校验客户端证书失败。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_IO_SSL_CONNECTION_FAILED14+5411009

表示SSL连接失败。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_IO_SSL_SERVER_CERT_UNTRUSTED14+5411010

表示客户端校验服务端证书失败。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_IO_UNSUPPORTED_REQUEST14+5411011

表示网络协议的原因导致请求不受支持。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AVERR_SEEK_CONTINUOUS_UNSUPPORTED18+5410002

表示不支持SEEK_CONTINUOUS模式的seek。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

AVERR_SUPER_RESOLUTION_UNSUPPORTED18+5410003

表示不支持超分。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

AVERR_SUPER_RESOLUTION_NOT_ENABLED18+5410004

表示未使能超分。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

AVERR_PARAMETER_OUT_OF_RANGE20+5400108

表示参数超过取值范围。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### MediaType8+

媒体类型枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明MEDIA_TYPE_UNSUPPORTED20+-1

表示未支持的类型。

**元服务API：** 从API version 20 开始，该接口支持在元服务中使用。

MEDIA_TYPE_AUD0

表示音频。

**元服务API：** 从API version 11 开始，该接口支持在元服务中使用。

MEDIA_TYPE_VID1

表示视频。

**元服务API：** 从API version 11 开始，该接口支持在元服务中使用。

MEDIA_TYPE_SUBTITLE12+2

表示字幕。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

MEDIA_TYPE_ATTACHMENT20+3

表示附件信息（如嵌入的外部文件）。

**元服务API：** 从API version 20 开始，该接口支持在元服务中使用。

MEDIA_TYPE_DATA20+4

表示数据。

**元服务API：** 从API version 20 开始，该接口支持在元服务中使用。

MEDIA_TYPE_TIMED_METADATA20+5

表示带时间戳的元数据。

**元服务API：** 从API version 20 开始，该接口支持在元服务中使用。

MEDIA_TYPE_AUXILIARY20+6

表示辅助（轨道）信息。

**元服务API：** 从API version 20 开始，该接口支持在元服务中使用。

[]()[]()

#### CodecMimeType8+

Codec MIME类型枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明VIDEO_H263'video/h263'表示视频/h263类型。VIDEO_AVC'video/avc'

表示视频/avc类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

VIDEO_MPEG2'video/mpeg2'表示视频/mpeg2类型。VIDEO_MPEG4'video/mp4v-es'表示视频/mpeg4类型。VIDEO_VP8'video/x-vnd.on2.vp8'表示视频/vp8类型。VIDEO_HEVC11+'video/hevc'

表示视频/H265类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

AUDIO_AAC'audio/mp4a-latm'

表示音频/mp4a-latm类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

AUDIO_VORBIS'audio/vorbis'表示音频/vorbis类型。AUDIO_FLAC'audio/flac'表示音频/flac类型。AUDIO_MP312+'audio/mpeg'表示音频/mpeg类型。AUDIO_G711MU12+'audio/g711mu'表示音频/G711-mulaw类型。AUDIO_AMR_NB18+'audio/3gpp'表示音频/amr-nb类型。AUDIO_AMR_WB18+'audio/amr-wb'表示音频/amr-wb类型。[]()[]()

#### AacProfile22+

高级音频编码（AAC）类型枚举。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

名称值说明AAC_LC0表示 AAC Low-Complexity 类型。AAC_HE1表示 AAC Hight-Efficiency 类型。AAC_HE_V22表示 AAC Hight-Efficiency version 2 类型。[]()[]()

#### MediaDescriptionKey8+

媒体信息描述枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明MD_KEY_TRACK_INDEX'track_index'

表示轨道序号，其对应键值类型为number。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MD_KEY_TRACK_TYPE'track_type'

表示轨道类型，其对应键值类型为number，参考[MediaType](#ZH-CN_TOPIC_0000002497445922__mediatype8)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MD_KEY_CODEC_MIME'codec_mime'

表示codec_mime类型，其对应键值类型为string。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MD_KEY_DURATION'duration'

表示媒体时长，其对应键值类型为number，单位为毫秒（ms）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MD_KEY_BITRATE'bitrate'

表示比特率，其对应键值类型为number，单位为比特率（bps），值为undefined或0表示异常。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MD_KEY_WIDTH'width'

表示视频宽度，其对应键值类型为number，单位为像素（px）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MD_KEY_HEIGHT'height'

表示视频高度，其对应键值类型为number，单位为像素（px）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MD_KEY_FRAME_RATE'frame_rate'

表示视频帧率，其对应键值类型为number，单位为每100秒的帧数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MD_KEY_AUD_CHANNEL_COUNT'channel_count'

表示声道数，其对应键值类型为number。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MD_KEY_AUD_SAMPLE_RATE'sample_rate'

表示采样率，其对应键值类型为number，单位为赫兹（Hz）。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

MD_KEY_AUD_SAMPLE_DEPTH12+'sample_depth'

表示位深，其对应键值类型为number，单位为位（bit）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

MD_KEY_LANGUAGE12+'language'

表示字幕语言，其对应键值类型为string。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

MD_KEY_TRACK_NAME12+'track_name'

表示track名称，其对应键值类型为string。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

MD_KEY_HDR_TYPE12+'hdr_type'

表示视频轨类型，其对应键值类型为string。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

MD_KEY_ORIGINAL_WIDTH21+'original_width'

表示视频原始宽度，其对应键值类型为number，单位为像素（px）。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

MD_KEY_ORIGINAL_HEIGHT21+'original_height'

表示视频原始高度，其对应键值类型为number，单位为像素（px）。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

[]()[]()

#### PlaybackInfoKey12+

播放信息描述枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明SERVER_IP_ADDRESS'server_ip_address'表示服务器IP地址，其对应键值类型为string。AVG_DOWNLOAD_RATE'average_download_rate'表示平均下载速率，其对应键值类型为number，单位为比特率（bps）。DOWNLOAD_RATE'download_rate'表示1s的下载速率，其对应键值类型为number，单位为比特率（bps）。IS_DOWNLOADING'is_downloading'表示下载状态，1表示在下载状态，0表示非下载状态（下载完成），其对应键值类型为number。BUFFER_DURATION'buffer_duration'表示缓存数据的可播放时长，其对应键值类型为number，单位为秒（s）。[]()[]()

#### BufferingInfoType8+

缓存事件类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明BUFFERING_START1

表示开始缓冲。当上报BUFFERING_START时，播放器会暂停播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

BUFFERING_END2

表示结束缓冲。当上报BUFFERING_END时，播放器会恢复播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

BUFFERING_PERCENT3

表示缓冲百分比。可参考该事件感知缓冲进度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

CACHED_DURATION4

表示已缓冲数据预估可播放时长，单位为毫秒（ms）。缓冲区中的数据变化量大于500ms，上报一次。可参考该事件做进度条。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

[]()[]()

#### StateChangeReason9+

表示播放或录制实例状态机切换原因的枚举，伴随state一起上报。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明USER1表示用户行为造成的状态切换，由用户或客户端主动调用接口产生。BACKGROUND2表示后台系统行为造成的状态切换，比如应用未注册播控中心权限，退到后台时被系统强制暂停或停止。[]()[]()

#### SeekMode8+

视频播放的Seek模式枚举，可通过seek方法作为参数传递下去。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明SEEK_NEXT_SYNC0

表示跳转到指定时间点的下一个关键帧，建议向后快进的时候用这个枚举值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

SEEK_PREV_SYNC1

表示跳转到指定时间点的上一个关键帧，建议向前快进的时候用这个枚举值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

SEEK_CLOSEST12+2

表示跳转到距离指定时间点最近的帧，建议精准跳转进度的时候用这个枚举值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SEEK_CONTINUOUS18+3

该模式提供了一种画面平滑流畅变化的Seek体验，应用可以结合进度条控件持续调用Seek方法，AVPlayer根据Seek调用持续流畅地更新画面。

应用可以调用[isSeekContinuousSupported](../../types/interfaces/Interface (AVPlayer).md#ZH-CN_TOPIC_0000002529285889__isseekcontinuoussupported18)方法根据返回结果感知视频源是否支持该模式Seek。

对于不支持该Seek模式的视频源调用该模式Seek时，会上报AVERR_SEEK_CONTINUOUS_UNSUPPORTED错误([媒体错误码](#ZH-CN_TOPIC_0000002497445922__averrorcode9))，同时画面更新的流畅性会降低。

该Seek模式不会触发[seekDone事件](../../types/interfaces/Interface (AVPlayer).md#ZH-CN_TOPIC_0000002529285889__onseekdone9)。

当应用需要退出该模式下的Seek时，需要调用seek(-1, SeekMode.SEEK_CONTINUOUS)来结束该模式下的Seek。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

[]()[]()

#### SwitchMode12+

视频播放的selectTrack模式枚举，可通过selectTrack方法作为参数传递下去，当前仅DASH协议视频轨支持该扩展参数。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明SMOOTH0

表示切换后视频平滑播放，该模式切换存在延迟，不会立即生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SEGMENT1

表示切换后从当前分片开始位置播放，该模式立即切换，会有重复播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

CLOSEST2

表示从距离当前播放时间点最近的帧开始播放，该模式立即切换，切换后会卡住3到5s，然后恢复播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

[]()[]()

#### PlaybackSpeed8+

视频播放的倍速枚举，可通过setSpeed方法作为参数传递下去。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

名称值说明SPEED_FORWARD_0_75_X0

表示视频播放正常播速的0.75倍。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SPEED_FORWARD_1_00_X1

表示视频播放正常播速。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SPEED_FORWARD_1_25_X2

表示视频播放正常播速的1.25倍。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SPEED_FORWARD_1_75_X3

表示视频播放正常播速的1.75倍。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SPEED_FORWARD_2_00_X4

表示视频播放正常播速的2.00倍。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SPEED_FORWARD_0_50_X12+5

表示视频播放正常播速的0.50倍。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SPEED_FORWARD_1_50_X12+6

表示视频播放正常播速的1.50倍。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SPEED_FORWARD_3_00_X13+7

表示视频播放正常播速的3.00倍。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

SPEED_FORWARD_0_25_X12+8

表示视频播放正常播速的0.25倍。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

SPEED_FORWARD_0_125_X12+9

表示视频播放正常播速的0.125倍。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

[]()[]()

#### VideoScaleType9+

枚举，视频缩放模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

名称值说明VIDEO_SCALE_TYPE_FIT0默认比例类型，视频拉伸至与窗口等大。VIDEO_SCALE_TYPE_FIT_CROP1保持视频宽高比缩放至最短边填满窗口，长边超出窗口部分被裁剪。VIDEO_SCALE_TYPE_SCALED_ASPECT20+2

保持视频宽高比缩放至长边填满窗口，短边居中对齐，未填满部分留黑。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### AudioSourceType9+

表示视频录制中音频源类型的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

名称值说明AUDIO_SOURCE_TYPE_DEFAULT0默认的音频输入源类型。AUDIO_SOURCE_TYPE_MIC1

表示MIC的音频输入源。

**元服务API：** 从API version 12 开始，该接口支持在元服务中使用。

AUDIO_SOURCE_TYPE_VOICE_RECOGNITION12+2表示语音识别场景的音频源。AUDIO_SOURCE_TYPE_VOICE_COMMUNICATION12+7表示语音通话场景的音频源。AUDIO_SOURCE_TYPE_VOICE_MESSAGE12+10表示短语音消息的音频源。AUDIO_SOURCE_TYPE_CAMCORDER12+13表示相机录像的音频源。[]()[]()

#### VideoSourceType9+

表示视频录制中视频源类型的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

名称值说明VIDEO_SOURCE_TYPE_SURFACE_YUV0输入surface中携带的是raw data。VIDEO_SOURCE_TYPE_SURFACE_ES1输入surface中携带的是ES data。[]()[]()

#### ContainerFormatType8+

表示容器格式类型的枚举，缩写为CFT。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明CFT_MPEG_4'mp4'

视频的容器格式，MP4。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

CFT_MPEG_4A'm4a'

音频的容器格式，M4A。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

CFT_MP312+'mp3'音频的容器格式，MP3。CFT_WAV12+'wav'音频的容器格式，WAV。CFT_AMR18+'amr'音频的容器格式，AMR。CFT_AAC20+'aac'音频的容器格式，AAC。默认为ADTS帧头格式。[]()[]()

#### FileGenerationMode12+

表示创建媒体文件模式的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

名称值说明APP_CREATE0由应用自行在沙箱创建媒体文件。AUTO_CREATE_CAMERA_SCENE1由系统创建媒体文件，当前仅在相机录制场景下生效，会忽略应用设置的url。[]()[]()

#### HdrType12+

表示视频HDR类型的枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明AV_HDR_TYPE_NONE0表示无HDR类型。AV_HDR_TYPE_VIVID1表示为HDR VIVID类型。[]()[]()

#### AVImageQueryOptions12+

需要获取的缩略图时间点与视频帧的对应关系。

在获取视频缩略图时，传入的时间点与实际取得的视频帧所在时间点不一定相等，需要指定传入的时间点与实际取得的视频帧的时间关系。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

名称值说明AV_IMAGE_QUERY_NEXT_SYNC0表示选取传入时间点或之后的关键帧。AV_IMAGE_QUERY_PREVIOUS_SYNC1表示选取传入时间点或之前的关键帧。AV_IMAGE_QUERY_CLOSEST_SYNC2表示选取离传入时间点最近的关键帧。AV_IMAGE_QUERY_CLOSEST3表示选取离传入时间点最近的帧，该帧不一定是关键帧。[]()[]()

#### LoadingRequestError18+

枚举，数据加载过程中状态变化的原因。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明LOADING_ERROR_SUCCESS0由客户端返回，表示已经推送到资源末尾。LOADING_ERROR_NOT_READY1由客户端返回，表示资源尚未准备好可供访问。LOADING_ERROR_NO_RESOURCE2由客户端返回，表示请求的资源URL不存在。LOADING_ERROR_INVAID_HANDLE3由客户端返回，表示请求的资源句柄uuid无效。LOADING_ERROR_ACCESS_DENIED4由客户端返回，表示客户端没有权限请求该资源。LOADING_ERROR_ACCESS_TIMEOUT5由客户端返回，表示访问资源过程超时。LOADING_ERROR_AUTHORIZE_FAILED6由客户端返回，表示授权失败。[]()[]()

#### AVMimeTypes12+

媒体MIME类型，通过[setMimeType](../../types/interfaces/Interface (MediaSource).md#ZH-CN_TOPIC_0000002529285891__setmimetype12)设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明APPLICATION_M3U8application/m3u8表示m3u8本地文件。[]()[]()

#### AVScreenCaptureRecordPreset12+

进行屏幕录制时的编码、封装格式参数的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

名称值说明SCREEN_RECORD_PRESET_H264_AAC_MP40使用视频H264编码，音频AAC编码，MP4封装格式。SCREEN_RECORD_PRESET_H265_AAC_MP41使用视频H265编码，音频AAC编码，MP4封装格式。[]()[]()

#### AVScreenCaptureStateCode12+

屏幕录制的状态回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

名称值说明SCREENCAPTURE_STATE_STARTED0录屏已开始。SCREENCAPTURE_STATE_CANCELED1录屏被取消。SCREENCAPTURE_STATE_STOPPED_BY_USER2录屏被用户手动停止。SCREENCAPTURE_STATE_INTERRUPTED_BY_OTHER3录屏被其他录屏打断。SCREENCAPTURE_STATE_STOPPED_BY_CALL4录屏被来电打断。SCREENCAPTURE_STATE_MIC_UNAVAILABLE5录屏无法使用麦克风收音。SCREENCAPTURE_STATE_MIC_MUTED_BY_USER6麦克风被用户关闭。SCREENCAPTURE_STATE_MIC_UNMUTED_BY_USER7麦克风被用户打开。SCREENCAPTURE_STATE_ENTER_PRIVATE_SCENE8录屏进入隐私页面。SCREENCAPTURE_STATE_EXIT_PRIVATE_SCENE9录屏退出隐私页面。SCREENCAPTURE_STATE_STOPPED_BY_USER_SWITCHES10系统用户切换，录屏中断。[]()[]()

#### AVScreenCaptureFillMode18+

进行屏幕录制时视频填充模式的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

名称值说明PRESERVE_ASPECT_RATIO0保持与原始图像相同的宽高比例，即与物理屏幕宽高比例一致。SCALE_TO_FILL1进行图像拉伸填充，适配设置的宽度和高度。[]()[]()

#### PickerMode22+

表示屏幕录制Picker模式的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

名称值说明WINDOW_ONLY0仅显示窗口列表。SCREEN_ONLY1仅显示屏幕列表。SCREEN_AND_WINDOW2同时显示屏幕列表和窗口列表。[]()[]()

#### AudioEncoder(deprecated)

从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](#ZH-CN_TOPIC_0000002497445922__codecmimetype8)替代。

表示音频编码格式的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

名称值说明DEFAULT0

默认编码格式。

仅做接口定义，暂不支持使用。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](#ZH-CN_TOPIC_0000002497445922__codecmimetype8)中的AUDIO_AAC替代。

AMR_NB1

AMR-NB(Adaptive Multi Rate-Narrow Band Speech Codec) 编码格式。

仅做接口定义，暂不支持使用。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](#ZH-CN_TOPIC_0000002497445922__codecmimetype8)中的AUDIO_AMR_NB替代。

AMR_WB2

AMR-WB(Adaptive Multi Rate-Wide Band Speech Codec) 编码格式。

仅做接口定义，暂不支持使用。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](#ZH-CN_TOPIC_0000002497445922__codecmimetype8)中的AUDIO_AMR_WB替代。

AAC_LC3

AAC-LC（Advanced Audio Coding Low Complexity）编码格式。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](#ZH-CN_TOPIC_0000002497445922__codecmimetype8)中的AUDIO_AAC替代。

HE_AAC4

HE_AAC（High-Efficiency Advanced Audio Coding）编码格式。

仅做接口定义，暂不支持使用。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[CodecMimeType](#ZH-CN_TOPIC_0000002497445922__codecmimetype8)中的AUDIO_AAC替代。

[]()[]()

#### AudioOutputFormat(deprecated)

从API version 6开始支持，从API version 8 开始废弃，建议使用[ContainerFormatType](#ZH-CN_TOPIC_0000002497445922__containerformattype8)替代。

表示音频封装格式的枚举。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

名称值说明DEFAULT0

默认封装格式。

仅做接口定义，暂不支持使用。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议根据具体情况选择[ContainerFormatType](#ZH-CN_TOPIC_0000002497445922__containerformattype8)中的一项替代。

MPEG_42

封装为MPEG-4格式。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[ContainerFormatType](#ZH-CN_TOPIC_0000002497445922__containerformattype8)中的CFT_MPEG_4替代。

AMR_NB3

封装为AMR_NB格式。

仅做接口定义，暂不支持使用。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[ContainerFormatType](#ZH-CN_TOPIC_0000002497445922__containerformattype8)中的CFT_AMR，编码格式使用[CodecMimeType](#ZH-CN_TOPIC_0000002497445922__codecmimetype8)中的AUDIO_AMR_NB替代。

AMR_WB4

封装为AMR_WB格式。

仅做接口定义，暂不支持使用。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[ContainerFormatType](#ZH-CN_TOPIC_0000002497445922__containerformattype8)中的CFT_AMR，编码格式使用[CodecMimeType](#ZH-CN_TOPIC_0000002497445922__codecmimetype8)中的AUDIO_AMR_WB替代。

AAC_ADTS6

封装为ADTS（Audio Data Transport Stream）格式，是AAC音频的传输流格式。

**说明：** 从API version 6开始支持，从API version 8开始废弃，建议使用[ContainerFormatType](#ZH-CN_TOPIC_0000002497445922__containerformattype8)中的CFT_AAC替代。

[]()[]()

#### MediaErrorCode(deprecated)

媒体服务错误类型枚举。

从API version 8开始支持，从API version 11开始废弃，建议使用[媒体错误码](#ZH-CN_TOPIC_0000002497445922__averrorcode9)替代。

**系统能力：** SystemCapability.Multimedia.Media.Core

名称值说明MSERR_OK0表示操作成功。MSERR_NO_MEMORY1表示申请内存失败，系统可能无可用内存。MSERR_OPERATION_NOT_PERMIT2表示无权限执行此操作。MSERR_INVALID_VAL3表示传入入参无效。MSERR_IO4表示发生IO错误。MSERR_TIMEOUT5表示操作超时。MSERR_UNKNOWN6表示未知错误。MSERR_SERVICE_DIED7表示服务端失效。MSERR_INVALID_STATE8表示在当前状态下，不允许执行此操作。MSERR_UNSUPPORTED9表示在当前版本下，不支持此操作。