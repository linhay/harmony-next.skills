# native_averrors.h

**概述**

媒体框架错误码。

引用文件： <multimedia/player_framework/native_averrors.h>

库： libnative_media_core.so

系统能力： SystemCapability.Multimedia.Media.Core

起始版本： 9

相关模块： [Core](Core.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVErrCode | OH_AVErrCode | 媒体框架错误码。 |

**枚举类型说明**

**OH_AVErrCode**

```ets
enum OH_AVErrCode
```

描述

媒体框架错误码。

系统能力： SystemCapability.Multimedia.Media.Core

起始版本： 9

| 枚举项 | 描述 |
| --- | --- |
| AV_ERR_OK = 0 | 操作成功。 |
| AV_ERR_NO_MEMORY = 1 | 无内存。 |
| AV_ERR_OPERATE_NOT_PERMIT = 2 | 操作不允许。 |
| AV_ERR_INVALID_VAL = 3 | 无效值。 |
| AV_ERR_IO = 4 | IO错误。 |
| AV_ERR_TIMEOUT = 5 | 超时错误。 |
| AV_ERR_UNKNOWN = 6 | 未知错误。 |
| AV_ERR_SERVICE_DIED = 7 | 服务死亡。 |
| AV_ERR_INVALID_STATE = 8 | 当前状态不支持此操作。 |
| AV_ERR_UNSUPPORT = 9 | 未支持的接口。 |
| AV_ERR_INPUT_DATA_ERROR = 10 | 输入数据错误。 起始版本： 12 |
| AV_ERR_UNSUPPORTED_FORMAT = 11 | 不支持的格式。 起始版本： 18 |
| AV_ERR_EXTEND_START = 100 | 扩展错误码初始值。 |
| AV_ERR_DRM_BASE = 200 | DRM起始错误码。 起始版本： 12 |
| AV_ERR_DRM_DECRYPT_FAILED = 201 | DRM解密失败。 起始版本： 12 |
| AV_ERR_VIDEO_BASE = 300 | 视频起始错误码。 起始版本： 12 |
| AV_ERR_VIDEO_UNSUPPORTED_COLOR_SPACE_CONVERSION = 301 | 视频不支持色彩空间转换。 起始版本： 12 |
| AV_ERR_IO_CANNOT_FIND_HOST = 5411001 | 无法找到主机，可能服务器地址错误。 起始版本： 14 |
| AV_ERR_IO_CONNECTION_TIMEOUT = 5411002 | 网络连接超时。 起始版本： 14 |
| AV_ERR_IO_NETWORK_ABNORMAL = 5411003 | 网络异常导致连接失败。 起始版本： 14 |
| AV_ERR_IO_NETWORK_UNAVAILABLE = 5411004 | 网络不可用导致连接失败。 起始版本： 14 |
| AV_ERR_IO_NO_PERMISSION = 5411005 | 无网络访问权限。 起始版本： 14 |
| AV_ERR_IO_NETWORK_ACCESS_DENIED = 5411006 | 客户端请求参数错误或超出处理能力。 起始版本： 14 |
| AV_ERR_IO_RESOURCE_NOT_FOUND = 5411007 | 无法找到可用网络资源。 起始版本： 14 |
| AV_ERR_IO_SSL_CLIENT_CERT_NEEDED = 5411008 | 由于未携带客户端证书、证书无效或过期导致服务器验证失败。 起始版本： 14 |
| AV_ERR_IO_SSL_CONNECT_FAIL = 5411009 | 由于未携带服务器证书、证书无效或过期导致客户端验证失败。 起始版本： 14 |
| AV_ERR_IO_SSL_SERVER_CERT_UNTRUSTED = 5411010 | SSL服务器证书不受信任。 起始版本： 14 |
| AV_ERR_IO_UNSUPPORTED_REQUEST = 5411011 | 网络协议不支持该请求。 起始版本： 14 |
| AV_ERR_IO_CLEARTEXT_NOT_PERMITTED = 5411012 | 不允许HTTP明文访问。 起始版本： 23 |
| AV_ERR_STREAM_CHANGED = 5410005 | 同步模式下流格式发生变更。可以通过调用接口OH_VideoEncoder_GetOutputDescription（视频编码）、OH_VideoDecoder_GetOutputDescription（视频解码）、OH_AudioCodec_GetOutputDescription（音频编解码）来获取更新后流的配置信息。 起始版本： 20 |
| AV_ERR_TRY_AGAIN_LATER = 5410006 | 同步模式下临时缓冲区查询失败，建议等待短暂间隔后重试操作。 起始版本： 20 |
| AV_ERR_SUPER_RESOLUTION_UNSUPPORTED = 5410003 | 该媒体源或者当前设备不支持超分。 起始版本： 23 |
| AV_ERR_SUPER_RESOLUTION_NOT_ENABLED = 5410004 | 未使能超分。 起始版本： 23 |