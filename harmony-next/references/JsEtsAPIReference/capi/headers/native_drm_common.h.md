# native_drm_common.h

#### 概述

定义DRM数据类型。

**引用文件：** <multimedia/drm_framework/native_drm_common.h>

**库：** libnative_drm.so

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

**相关模块：**[Drm](../../topics/misc/Drm.md)

#### 汇总

#### 结构体

名称typedef关键字描述[DRM_MediaKeyRequestInfo](../../topics/media/DRM_MediaKeyRequestInfo.md)DRM_MediaKeyRequestInfo媒体密钥请求信息。[DRM_MediaKeyRequest](../../topics/media/DRM_MediaKeyRequest.md)DRM_MediaKeyRequest媒体密钥请求。[DRM_Statistics](../../topics/misc/DRM_Statistics.md)DRM_StatisticsMediaKeySystem的度量信息。[DRM_OfflineMediakeyIdArray](../../topics/graphics/DRM_OfflineMediakeyIdArray.md)DRM_OfflineMediakeyIdArray离线媒体密钥ID数组。[DRM_KeysInfo](../../topics/misc/DRM_KeysInfo.md)DRM_KeysInfo媒体密钥信息。[DRM_MediaKeyStatus](../../topics/media/DRM_MediaKeyStatus.md)DRM_MediaKeyStatus媒体密钥状态。[DRM_PsshInfo](../../topics/misc/DRM_PsshInfo.md)DRM_PsshInfoDRM内容保护系统专用头（Protection System Specific Header）信息。[DRM_MediaKeySystemInfo](../../topics/system-services/DRM_MediaKeySystemInfo.md)DRM_MediaKeySystemInfo加密媒体内容的DRM信息。[DRM_MediaKeySystemDescription](../../topics/system-services/DRM_MediaKeySystemDescription.md)DRM_MediaKeySystemDescriptionDRM解决方案名称及其UUID的列表。[MediaKeySystem](../../topics/system-services/MediaKeySystem.md)MediaKeySystemMediaKeySystem结构。[MediaKeySession](../../topics/media/MediaKeySession.md)MediaKeySessionMediaKeySession结构。

#### 枚举

名称typedef关键字描述[DRM_EventType](#ZH-CN_TOPIC_0000002529445793__drm_eventtype)DRM_EventType监听事件类型。[DRM_ContentProtectionLevel](#ZH-CN_TOPIC_0000002529445793__drm_contentprotectionlevel)DRM_ContentProtectionLevel内容保护级别。[DRM_MediaKeyType](#ZH-CN_TOPIC_0000002529445793__drm_mediakeytype)DRM_MediaKeyType媒体密钥类型。[DRM_MediaKeyRequestType](#ZH-CN_TOPIC_0000002529445793__drm_mediakeyrequesttype)DRM_MediaKeyRequestType媒体密钥请求类型。[DRM_OfflineMediaKeyStatus](#ZH-CN_TOPIC_0000002529445793__drm_offlinemediakeystatus)DRM_OfflineMediaKeyStatus离线媒体密钥状态。[DRM_CertificateStatus](#ZH-CN_TOPIC_0000002529445793__drm_certificatestatus)DRM_CertificateStatus设备DRM证书状态。

#### 函数

名称typedef关键字描述[typedef void (*DRM_MediaKeySystemInfoCallback)(DRM_MediaKeySystemInfo *mediaKeySystemInfo)](#ZH-CN_TOPIC_0000002529445793__drm_mediakeysysteminfocallback)DRM_MediaKeySystemInfoCallback应用为从媒体源获取DRM信息而设置的回调。

#### 宏定义

名称描述MAX_MEDIA_KEY_REQUEST_OPTION_COUNT 16

媒体密钥请求可选数据的最大数量。

**起始版本：** 11

MAX_MEDIA_KEY_REQUEST_OPTION_NAME_LEN 64

媒体密钥请求可选数据名称的最大长度。

**起始版本：** 11

MAX_MEDIA_KEY_REQUEST_OPTION_DATA_LEN 128

媒体密钥请求可选数据的最大长度。

**起始版本：** 11

MAX_INIT_DATA_LEN 2048

媒体密钥请求初始化数据的最大长度。

**起始版本：** 11

MAX_MIMETYPE_LEN 64

媒体mimetype的最大长度。

**起始版本：** 11

MAX_MEDIA_KEY_REQUEST_DATA_LEN 8192

媒体密钥请求数据的最大长度。

**起始版本：** 11

MAX_DEFAULT_URL_LEN 2048

URL最大长度。

**起始版本：** 11

MAX_STATISTICS_COUNT 10

度量记录的最大数量。

**起始版本：** 11

MAX_STATISTICS_NAME_LEN 64

度量记录名称的最大长度。

**起始版本：** 11

MAX_STATISTICS_BUFFER_LEN 256

度量记录缓冲区的最大长度。

**起始版本：** 11

MAX_OFFLINE_MEDIA_KEY_ID_COUNT 512

离线媒体密钥标识的最大数量。

**起始版本：** 11

MAX_OFFLINE_MEDIA_KEY_ID_LEN 64

离线媒体密钥标识的最大长度。

**起始版本：** 11

MAX_KEY_INFO_COUNT 64

密钥信息的最大数量。

**起始版本：** 11

MAX_KEY_ID_LEN 16

密钥标识的最大长度。

**起始版本：** 11

MAX_KEY_STATUS_VALUE_LEN 128

密钥状态值的最大长度。

**起始版本：** 11

MAX_MEDIA_KEY_STATUS_COUNT 64

媒体密钥状态的最大数量。

**起始版本：** 11

MAX_MEDIA_KEY_STATUS_NAME_LEN 64

媒体密钥状态名称的最大长度。

**起始版本：** 11

MAX_MEDIA_KEY_STATUS_VALUE_LEN 256

媒体密钥状态值的最大长度。

**起始版本：** 11

DRM_UUID_LEN 16

DRM解决方案的UUID长度。

**起始版本：** 11

MAX_PSSH_DATA_LEN 2048

PSSH（Protected System Specific Header）信息的最大长度。

**起始版本：** 11

MAX_PSSH_INFO_COUNT 8

PSSH（Protected System Specific Header）信息的最大数量。

**起始版本：** 11

MAX_MEDIA_KEY_SYSTEM_NAME_LEN 128

MediaKeySystem名称的最大长度。

**起始版本：** 12

MAX_MEDIA_KEY_SYSTEM_NUM 8

MediaKeySystem的最大数量。

**起始版本：** 12

#### 枚举类型说明

#### DRM_EventType

```ets
enum DRM_EventType
```

**描述**

监听事件类型。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

枚举项描述EVENT_DRM_BASE = 200DRM基础事件。EVENT_PROVISION_REQUIRED = 201设备证书请求事件。EVENT_KEY_REQUIRED = 202密钥请求事件。EVENT_KEY_EXPIRED = 203密钥过期事件。EVENT_VENDOR_DEFINED = 204DRM解决方案自定义事件。EVENT_EXPIRATION_UPDATE = 206密钥过期更新事件。

#### DRM_ContentProtectionLevel

```ets
enum DRM_ContentProtectionLevel
```

**描述**

内容保护级别。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

枚举项描述CONTENT_PROTECTION_LEVEL_UNKNOWN = 0未知级别。CONTENT_PROTECTION_LEVEL_SW_CRYPTO软件安全级别。CONTENT_PROTECTION_LEVEL_HW_CRYPTO硬件安全级别。CONTENT_PROTECTION_LEVEL_ENHANCED_HW_CRYPTO硬件增强级别。CONTENT_PROTECTION_LEVEL_MAX最大安全级别。

#### DRM_MediaKeyType

```ets
enum DRM_MediaKeyType
```

**描述**

媒体密钥类型。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

枚举项描述MEDIA_KEY_TYPE_OFFLINE = 0离线。MEDIA_KEY_TYPE_ONLINE在线。

#### DRM_MediaKeyRequestType

```ets
enum DRM_MediaKeyRequestType
```

**描述**

媒体密钥请求类型。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

枚举项描述MEDIA_KEY_REQUEST_TYPE_UNKNOWN = 0未知请求类型。MEDIA_KEY_REQUEST_TYPE_INITIAL初始化请求。MEDIA_KEY_REQUEST_TYPE_RENEWAL续订请求。MEDIA_KEY_REQUEST_TYPE_RELEASE释放请求。MEDIA_KEY_REQUEST_TYPE_NONE无请求。MEDIA_KEY_REQUEST_TYPE_UPDATE更新请求。

#### DRM_OfflineMediaKeyStatus

```ets
enum DRM_OfflineMediaKeyStatus
```

**描述**

离线媒体密钥状态。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

枚举项描述OFFLINE_MEDIA_KEY_STATUS_UNKNOWN = 0未知状态。OFFLINE_MEDIA_KEY_STATUS_USABLE可用状态。OFFLINE_MEDIA_KEY_STATUS_INACTIVE失活状态。

#### DRM_CertificateStatus

```ets
enum DRM_CertificateStatus
```

**描述**

设备DRM证书状态。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

枚举项描述CERT_STATUS_PROVISIONED = 0设备已安装设备DRM证书。CERT_STATUS_NOT_PROVISIONED设备未安装设备DRM证书或证书状态异常。CERT_STATUS_EXPIRED设备DRM证书过期。CERT_STATUS_INVALID设备DRM证书无效。CERT_STATUS_UNAVAILABLE设备DRM证书不可用。

#### 函数说明

#### DRM_MediaKeySystemInfoCallback()

```ets
typedef void (*DRM_MediaKeySystemInfoCallback)(DRM_MediaKeySystemInfo *mediaKeySystemInfo)
```

**描述**

应用为从媒体源获取DRM信息而设置的回调。

**起始版本：** 11

**参数：**

参数项描述[DRM_MediaKeySystemInfo](../../topics/system-services/DRM_MediaKeySystemInfo.md) *mediaKeySystemInfo从媒体源获取的DRM信息。