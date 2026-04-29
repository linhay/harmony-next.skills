# native_drm_common.h

**概述**

定义DRM数据类型。

引用文件： <multimedia/drm_framework/native_drm_common.h>

库： libnative_drm.so

系统能力： SystemCapability.Multimedia.Drm.Core

起始版本： 11

相关模块： [Drm](Drm.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| DRM_MediaKeyRequestInfo | DRM_MediaKeyRequestInfo | 媒体密钥请求信息。 |
| DRM_MediaKeyRequest | DRM_MediaKeyRequest | 媒体密钥请求。 |
| DRM_Statistics | DRM_Statistics | MediaKeySystem的度量信息。 |
| DRM_OfflineMediakeyIdArray | DRM_OfflineMediakeyIdArray | 离线媒体密钥ID数组。 |
| DRM_KeysInfo | DRM_KeysInfo | 媒体密钥信息。 |
| DRM_MediaKeyStatus | DRM_MediaKeyStatus | 媒体密钥状态。 |
| DRM_PsshInfo | DRM_PsshInfo | DRM内容保护系统专用头（Protection System Specific Header）信息。 |
| DRM_MediaKeySystemInfo | DRM_MediaKeySystemInfo | 加密媒体内容的DRM信息。 |
| DRM_MediaKeySystemDescription | DRM_MediaKeySystemDescription | DRM解决方案名称及其UUID的列表。 |
| MediaKeySystem | MediaKeySystem | MediaKeySystem结构。 |
| MediaKeySession | MediaKeySession | MediaKeySession结构。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| DRM_EventType | DRM_EventType | 监听事件类型。 |
| DRM_ContentProtectionLevel | DRM_ContentProtectionLevel | 内容保护级别。 |
| DRM_MediaKeyType | DRM_MediaKeyType | 媒体密钥类型。 |
| DRM_MediaKeyRequestType | DRM_MediaKeyRequestType | 媒体密钥请求类型。 |
| DRM_OfflineMediaKeyStatus | DRM_OfflineMediaKeyStatus | 离线媒体密钥状态。 |
| DRM_CertificateStatus | DRM_CertificateStatus | 设备DRM证书状态。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*DRM_MediaKeySystemInfoCallback)(DRM_MediaKeySystemInfo *mediaKeySystemInfo) | DRM_MediaKeySystemInfoCallback | 应用为从媒体源获取DRM信息而设置的回调。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| MAX_MEDIA_KEY_REQUEST_OPTION_COUNT 16 | 媒体密钥请求可选数据的最大数量。 起始版本： 11 |
| MAX_MEDIA_KEY_REQUEST_OPTION_NAME_LEN 64 | 媒体密钥请求可选数据名称的最大长度。 起始版本： 11 |
| MAX_MEDIA_KEY_REQUEST_OPTION_DATA_LEN 128 | 媒体密钥请求可选数据的最大长度。 起始版本： 11 |
| MAX_INIT_DATA_LEN 2048 | 媒体密钥请求初始化数据的最大长度。 起始版本： 11 |
| MAX_MIMETYPE_LEN 64 | 媒体mimetype的最大长度。 起始版本： 11 |
| MAX_MEDIA_KEY_REQUEST_DATA_LEN 8192 | 媒体密钥请求数据的最大长度。 起始版本： 11 |
| MAX_DEFAULT_URL_LEN 2048 | URL最大长度。 起始版本： 11 |
| MAX_STATISTICS_COUNT 10 | 度量记录的最大数量。 起始版本： 11 |
| MAX_STATISTICS_NAME_LEN 64 | 度量记录名称的最大长度。 起始版本： 11 |
| MAX_STATISTICS_BUFFER_LEN 256 | 度量记录缓冲区的最大长度。 起始版本： 11 |
| MAX_OFFLINE_MEDIA_KEY_ID_COUNT 512 | 离线媒体密钥标识的最大数量。 起始版本： 11 |
| MAX_OFFLINE_MEDIA_KEY_ID_LEN 64 | 离线媒体密钥标识的最大长度。 起始版本： 11 |
| MAX_KEY_INFO_COUNT 64 | 密钥信息的最大数量。 起始版本： 11 |
| MAX_KEY_ID_LEN 16 | 密钥标识的最大长度。 起始版本： 11 |
| MAX_KEY_STATUS_VALUE_LEN 128 | 密钥状态值的最大长度。 起始版本： 11 |
| MAX_MEDIA_KEY_STATUS_COUNT 64 | 媒体密钥状态的最大数量。 起始版本： 11 |
| MAX_MEDIA_KEY_STATUS_NAME_LEN 64 | 媒体密钥状态名称的最大长度。 起始版本： 11 |
| MAX_MEDIA_KEY_STATUS_VALUE_LEN 256 | 媒体密钥状态值的最大长度。 起始版本： 11 |
| DRM_UUID_LEN 16 | DRM解决方案的UUID长度。 起始版本： 11 |
| MAX_PSSH_DATA_LEN 2048 | PSSH（Protected System Specific Header）信息的最大长度。 起始版本： 11 |
| MAX_PSSH_INFO_COUNT 8 | PSSH（Protected System Specific Header）信息的最大数量。 起始版本： 11 |
| MAX_MEDIA_KEY_SYSTEM_NAME_LEN 128 | MediaKeySystem名称的最大长度。 起始版本： 12 |
| MAX_MEDIA_KEY_SYSTEM_NUM 8 | MediaKeySystem的最大数量。 起始版本： 12 |

**枚举类型说明**

**DRM_EventType**

```ets
enum DRM_EventType
```

描述

监听事件类型。

系统能力： SystemCapability.Multimedia.Drm.Core

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| EVENT_DRM_BASE = 200 | DRM基础事件。 |
| EVENT_PROVISION_REQUIRED = 201 | 设备证书请求事件。 |
| EVENT_KEY_REQUIRED = 202 | 密钥请求事件。 |
| EVENT_KEY_EXPIRED = 203 | 密钥过期事件。 |
| EVENT_VENDOR_DEFINED = 204 | DRM解决方案自定义事件。 |
| EVENT_EXPIRATION_UPDATE = 206 | 密钥过期更新事件。 |

**DRM_ContentProtectionLevel**

```ets
enum DRM_ContentProtectionLevel
```

描述

内容保护级别。

系统能力： SystemCapability.Multimedia.Drm.Core

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| CONTENT_PROTECTION_LEVEL_UNKNOWN = 0 | 未知级别。 |
| CONTENT_PROTECTION_LEVEL_SW_CRYPTO | 软件安全级别。 |
| CONTENT_PROTECTION_LEVEL_HW_CRYPTO | 硬件安全级别。 |
| CONTENT_PROTECTION_LEVEL_ENHANCED_HW_CRYPTO | 硬件增强级别。 |
| CONTENT_PROTECTION_LEVEL_MAX | 最大安全级别。 |

**DRM_MediaKeyType**

```ets
enum DRM_MediaKeyType
```

描述

媒体密钥类型。

系统能力： SystemCapability.Multimedia.Drm.Core

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| MEDIA_KEY_TYPE_OFFLINE = 0 | 离线。 |
| MEDIA_KEY_TYPE_ONLINE | 在线。 |

**DRM_MediaKeyRequestType**

```ets
enum DRM_MediaKeyRequestType
```

描述

媒体密钥请求类型。

系统能力： SystemCapability.Multimedia.Drm.Core

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| MEDIA_KEY_REQUEST_TYPE_UNKNOWN = 0 | 未知请求类型。 |
| MEDIA_KEY_REQUEST_TYPE_INITIAL | 初始化请求。 |
| MEDIA_KEY_REQUEST_TYPE_RENEWAL | 续订请求。 |
| MEDIA_KEY_REQUEST_TYPE_RELEASE | 释放请求。 |
| MEDIA_KEY_REQUEST_TYPE_NONE | 无请求。 |
| MEDIA_KEY_REQUEST_TYPE_UPDATE | 更新请求。 |

**DRM_OfflineMediaKeyStatus**

```ets
enum DRM_OfflineMediaKeyStatus
```

描述

离线媒体密钥状态。

系统能力： SystemCapability.Multimedia.Drm.Core

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| OFFLINE_MEDIA_KEY_STATUS_UNKNOWN = 0 | 未知状态。 |
| OFFLINE_MEDIA_KEY_STATUS_USABLE | 可用状态。 |
| OFFLINE_MEDIA_KEY_STATUS_INACTIVE | 失活状态。 |

**DRM_CertificateStatus**

```ets
enum DRM_CertificateStatus
```

描述

设备DRM证书状态。

系统能力： SystemCapability.Multimedia.Drm.Core

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| CERT_STATUS_PROVISIONED = 0 | 设备已安装设备DRM证书。 |
| CERT_STATUS_NOT_PROVISIONED | 设备未安装设备DRM证书或证书状态异常。 |
| CERT_STATUS_EXPIRED | 设备DRM证书过期。 |
| CERT_STATUS_INVALID | 设备DRM证书无效。 |
| CERT_STATUS_UNAVAILABLE | 设备DRM证书不可用。 |

**函数说明**

**DRM_MediaKeySystemInfoCallback()**

```ets
typedef void (*DRM_MediaKeySystemInfoCallback)(DRM_MediaKeySystemInfo *mediaKeySystemInfo)
```

描述

应用为从媒体源获取DRM信息而设置的回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| DRM_MediaKeySystemInfo *mediaKeySystemInfo | 从媒体源获取的DRM信息。 |