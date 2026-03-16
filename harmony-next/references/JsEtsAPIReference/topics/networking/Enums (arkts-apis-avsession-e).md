[]()[]()

# Enums

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### ProtocolType11+

远端设备支持的协议类型的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

名称值说明TYPE_LOCAL11+0

本地设备，包括设备本身的内置扬声器或音频插孔、A2DP 设备。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

TYPE_CAST_PLUS_STREAM11+2

Cast+的Stream模式。表示媒体正在其他设备上展示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

TYPE_DLNA12+4

DLNA协议。表示媒体正在其他设备上展示。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

TYPE_CAST_PLUS_AUDIO20+8

PCM模式。表示媒体正在其他设备上展示。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

[]()[]()

#### CastDisplayState12+

投播显示设备状态的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

名称值说明STATE_OFF1设备断开，扩展屏不再显示内容。STATE_ON2设备连接成功，扩展屏可用。[]()[]()

#### CallerType22+

表示调用方来源类型的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称值说明TYPE_CAST"cast"调用方来自投播。TYPE_BLUETOOTH"bluetooth"调用方来自蓝牙。TYPE_APP"app"调用方来自应用。TYPE_NEARLINK"nearlink"

调用方来自星闪。

**模型约束：** 此接口仅可在Stage模型下使用。

[]()[]()

#### ConnectionState10+

连接状态枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称值说明STATE_CONNECTING0设备连接中。STATE_CONNECTED1设备连接成功。STATE_DISCONNECTED6设备断开连接。[]()[]()

#### CallState11+

表示通话状态的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称值说明CALL_STATE_IDLE0空闲状态。CALL_STATE_INCOMING1来电。CALL_STATE_ACTIVE2接通。CALL_STATE_DIALING3响铃。CALL_STATE_WAITING4等待接通。CALL_STATE_HOLDING5保持。CALL_STATE_DISCONNECTING6挂断。[]()[]()

#### DisplayTag11+

枚举，表示当前媒体资源的金标，即应用媒体音源的特殊类型标识。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称值说明TAG_AUDIO_VIVID1AUDIO VIVID[]()[]()

#### DecoderType19+

枚举，设备所支持的解码格式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

名称值说明OH_AVCODEC_MIMETYPE_VIDEO_AVC"video/avc"VIDEO AVCOH_AVCODEC_MIMETYPE_VIDEO_HEVC"video/hevc"VIDEO HEVCOH_AVCODEC_MIMETYPE_AUDIO_VIVID"audio/av3a"AUDIO AV3A[]()[]()

#### ResolutionLevel19+

枚举，设备所支持的分辨率。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

名称值说明RESOLUTION_480P0分辨率为480P(640*480 dpi)。RESOLUTION_720P1分辨率为720P(1280*720 dpi)。RESOLUTION_1080P2分辨率为1080P(1920*1080 dpi)。RESOLUTION_2K3分辨率为2k(2560*1440 dpi)。RESOLUTION_4K4分辨率为4k(4096*3840 dpi)。[]()[]()

#### AVCastCategory10+

投播的类别枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

名称值说明CATEGORY_LOCAL0本地播放，默认播放设备，声音从本机或者连接的蓝牙耳机设备出声。CATEGORY_REMOTE1远端播放，远端播放设备，声音从其他设备发出声音或者画面。[]()[]()

#### DeviceType10+

播放设备的类型枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

名称值说明DEVICE_TYPE_LOCAL0

本地播放类型。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

DEVICE_TYPE_BLUETOOTH10

蓝牙设备。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

DEVICE_TYPE_TV2

电视。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

DEVICE_TYPE_SMART_SPEAKER3

音箱设备。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

[]()[]()

#### LoopMode10+

表示媒体播放循环模式的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称值说明LOOP_MODE_SEQUENCE0顺序播放。LOOP_MODE_SINGLE1单曲循环。LOOP_MODE_LIST2表单循环。LOOP_MODE_SHUFFLE3随机播放。LOOP_MODE_CUSTOM11+4自定义播放。[]()[]()

#### PlaybackState10+

表示媒体播放状态的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称值说明PLAYBACK_STATE_INITIAL0初始状态。PLAYBACK_STATE_PREPARE1播放准备状态。PLAYBACK_STATE_PLAY2正在播放。PLAYBACK_STATE_PAUSE3暂停。PLAYBACK_STATE_FAST_FORWARD4快进。PLAYBACK_STATE_REWIND5快退。PLAYBACK_STATE_STOP6停止。PLAYBACK_STATE_COMPLETED7播放完成。PLAYBACK_STATE_RELEASED8释放。PLAYBACK_STATE_ERROR9错误。PLAYBACK_STATE_IDLE11+10空闲。PLAYBACK_STATE_BUFFERING11+11缓冲。[]()[]()

#### AVSessionErrorCode10+

会话发生错误时的错误码。

名称值说明ERR_CODE_SERVICE_EXCEPTION6600101

会话服务端异常。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

ERR_CODE_SESSION_NOT_EXIST6600102

会话不存在。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

ERR_CODE_CONTROLLER_NOT_EXIST6600103

会话控制器不存在。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

ERR_CODE_REMOTE_CONNECTION_ERR6600104

远端会话连接失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

ERR_CODE_COMMAND_INVALID6600105

无效会话命令。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

ERR_CODE_SESSION_INACTIVE6600106

会话未激活。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

ERR_CODE_MESSAGE_OVERLOAD6600107

命令&消息过载。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

ERR_CODE_DEVICE_CONNECTION_FAILED6600108

设备连接失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

ERR_CODE_REMOTE_CONNECTION_NOT_EXIST6600109

远端会话不存在。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

ERR_CODE_CAST_CONTROL_UNSPECIFIED13+6611000

未被定义的投播错误码。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_REMOTE_ERROR13+6611001

远端播放器中发生不明错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_BEHIND_LIVE_WINDOW13+6611002

播放出现延迟。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_TIMEOUT13+6611003

投播控制进程超时。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_RUNTIME_CHECK_FAILED13+6611004

运行时检查失败。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_PLAYER_NOT_WORKING13+6611100

跨设备数据传输被锁定。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_SEEK_MODE_UNSUPPORTED13+6611101

不支持指定的查找模式。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_ILLEGAL_SEEK_TARGET13+6611102

要搜索的位置超出媒体的范围，或者不支持当前搜索模式。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_PLAY_MODE_UNSUPPORTED13+6611103

不支持指定的播放模式。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_PLAY_SPEED_UNSUPPORTED13+6611104

不支持指定的播放速度。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DEVICE_MISSING13+6611105

操作失败，因为媒体源设备或媒体接收器设备已被销毁。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_INVALID_PARAM13+6611106

该参数无效。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_NO_MEMORY13+6611107

内存分配失败。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_OPERATION_NOT_ALLOWED13+6611108

不被允许的操作。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_UNSPECIFIED13+6612000

未指定的输入/输出错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_NETWORK_CONNECTION_FAILED13+6612001

网络连接失败。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_NETWORK_CONNECTION_TIMEOUT13+6612002

网络连接超时。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_INVALID_HTTP_CONTENT_TYPE 13+6612003

无效的"Content-Type"。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_BAD_HTTP_STATUS13+6612004

HTTP服务器返回一个意外的HTTP响应状态码。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_FILE_NOT_FOUND13+6612005

文件不存在。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_NO_PERMISSION13+6612006

不允许执行输入/输出的IO操作。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_CLEARTEXT_NOT_PERMITTED13+6612007

应用的网络安全配置不允许访问明文HTTP流量。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_READ_POSITION_OUT_OF_RANGE13+6612008

从数据绑定中读取数据。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_NO_CONTENTS13+6612100

媒体中没有可播放的内容。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_READ_ERROR13+6612101

媒体无法读取。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_CONTENT_BUSY13+6612102

该资源正在使用中。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_CONTENT_EXPIRED13+6612103

输入/输出的IO请求内容已过期。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_USE_FORBIDDEN13+6612104

不允许播放请求内容。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_NOT_VERIFIED13+6612105

无法验证所允许的内容。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_EXHAUSTED_ALLOWED_USES13+6612106

此内容已达到允许的最大使用次数。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_IO_NETWORK_PACKET_SENDING_FAILED13+6612107

从源设备发送数据包到接收设备时出现错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_PARSING_UNSPECIFIED13+6613000

未指定的内容解析错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_PARSING_CONTAINER_MALFORMED13+6613001

媒体容器比特流的格式解析错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_PARSING_MANIFEST_MALFORMED13+6613002

媒体清单解析错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_PARSING_CONTAINER_UNSUPPORTED13+6613003

文件的媒体容器格式/媒体容器特性不被支持。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_PARSING_MANIFEST_UNSUPPORTED13+6613004

媒体清单中不支持的特性。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DECODING_UNSPECIFIED13+6614000

未指定的解码错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DECODING_INIT_FAILED13+6614001

解码器初始化失败。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DECODING_QUERY_FAILED13+6614002

解码器查询失败。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DECODING_FAILED13+6614003

媒体样本解码失败。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DECODING_FORMAT_EXCEEDS_CAPABILITIES13+6614004

设备的能力无法解码当前格式。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DECODING_FORMAT_UNSUPPORTED13+6614005

不支持的解码格式。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_AUDIO_RENDERER_UNSPECIFIED13+6615000

未指定的音频渲染器错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_AUDIO_RENDERER_INIT_FAILED 13+6615001

音频渲染器初始化失败。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_AUDIO_RENDERER_WRITE_FAILED13+6615002

音频渲染器写入数据失败。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DRM_UNSPECIFIED13+6616000

未指定的DRM相关错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DRM_SCHEME_UNSUPPORTED13+6616001

设备不支持所选择的DRM保护方案。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DRM_PROVISIONING_FAILED13+6616002

设备配置失败。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DRM_CONTENT_ERROR13+6616003

受DRM保护的内容无法播放。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DRM_LICENSE_ACQUISITION_FAILED13+6616004

获取许可证失败。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DRM_DISALLOWED_OPERATION13+6616005

许可证策略不允许该操作。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DRM_SYSTEM_ERROR13+6616006

DRM系统中发生错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DRM_DEVICE_REVOKED13+6616007

设备已撤销DRM权限。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DRM_LICENSE_EXPIRED13+6616008

加载中的DRM许可证已过期。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

ERR_CODE_CAST_CONTROL_DRM_PROVIDE_KEY_RESPONSE_ERROR13+6616100

DRM处理密钥响应时发生错误。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

[]()[]()

#### SkipIntervals11+

表示session支持的快进快退时间间隔的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称值说明SECONDS_1010时间为10秒。SECONDS_1515时间为15秒。SECONDS_3030时间为30秒。