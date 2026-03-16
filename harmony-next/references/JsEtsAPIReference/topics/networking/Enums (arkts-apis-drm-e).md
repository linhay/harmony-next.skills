[]()[]()

# Enums

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### DrmErrorCode

枚举，错误码。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称值说明ERROR_UNKNOWN24700101未知错误。MAX_SYSTEM_NUM_REACHED24700103MediaKeySystem实例数量超过上限（64个）。MAX_SESSION_NUM_REACHED24700104MediaKeySession实例数量超过上限（64个）。SERVICE_FATAL_ERROR24700201DRM服务异常。[]()[]()

#### PreDefinedConfigName

枚举，预定义的配置属性。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称值说明CONFIG_DEVICE_VENDOR'vendor'插件厂商名，通过[getConfigurationString](../../types/interfaces/Interface (MediaKeySystem).md#ZH-CN_TOPIC_0000002497605826__getconfigurationstring)接口获取vendor对应配置值。CONFIG_DEVICE_VERSION'version'插件版本号，通过[getConfigurationString](../../types/interfaces/Interface (MediaKeySystem).md#ZH-CN_TOPIC_0000002497605826__getconfigurationstring)接口获取version对应配置值。CONFIG_DEVICE_DESCRIPTION'description'设备描述符，通过[getConfigurationString](../../types/interfaces/Interface (MediaKeySystem).md#ZH-CN_TOPIC_0000002497605826__getconfigurationstring)接口获取description对应配置值。CONFIG_DEVICE_ALGORITHMS'algorithms'支持的算法，通过[getConfigurationString](../../types/interfaces/Interface (MediaKeySystem).md#ZH-CN_TOPIC_0000002497605826__getconfigurationstring)接口获取algorithms对应配置值。CONFIG_DEVICE_UNIQUE_ID'deviceUniqueId'设备唯一标识，通过[getConfigurationByteArray](../../types/interfaces/Interface (MediaKeySystem).md#ZH-CN_TOPIC_0000002497605826__getconfigurationbytearray)接口获取deviceUniqueId对应配置值。CONFIG_SESSION_MAX'maxSessionNum'设备支持的最大会话数，通过[getConfigurationString](../../types/interfaces/Interface (MediaKeySystem).md#ZH-CN_TOPIC_0000002497605826__getconfigurationstring)接口获取maxSessionNum对应配置值。CONFIG_SESSION_CURRENT'currentSessionNum'当前会话数量，通过[getConfigurationString](../../types/interfaces/Interface (MediaKeySystem).md#ZH-CN_TOPIC_0000002497605826__getconfigurationstring)接口获取currentSessionNum对应配置值。[]()[]()

#### MediaKeyType

枚举，媒体密钥类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称值说明MEDIA_KEY_TYPE_OFFLINE0离线。MEDIA_KEY_TYPE_ONLINE1在线。[]()[]()

#### OfflineMediaKeyStatus

枚举，离线媒体密钥状态。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称值说明OFFLINE_MEDIA_KEY_STATUS_UNKNOWN0未知状态。OFFLINE_MEDIA_KEY_STATUS_USABLE1可用状态。OFFLINE_MEDIA_KEY_STATUS_INACTIVE2失活状态。[]()[]()

#### CertificateStatus

枚举，设备证书状态。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称值说明CERT_STATUS_PROVISIONED0设备已安装设备证书。CERT_STATUS_NOT_PROVISIONED1设备未安装设备证书。CERT_STATUS_EXPIRED2设备证书过期。CERT_STATUS_INVALID3设备证书无效。CERT_STATUS_UNAVAILABLE4设备证书不可用。[]()[]()

#### MediaKeyRequestType

枚举，媒体密钥请求类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称值说明MEDIA_KEY_REQUEST_TYPE_UNKNOWN0未知请求类型。MEDIA_KEY_REQUEST_TYPE_INITIAL1初始化请求。MEDIA_KEY_REQUEST_TYPE_RENEWAL2续订请求。MEDIA_KEY_REQUEST_TYPE_RELEASE3释放请求。MEDIA_KEY_REQUEST_TYPE_NONE4无请求。MEDIA_KEY_REQUEST_TYPE_UPDATE5更新请求。[]()[]()

#### ContentProtectionLevel

枚举，内容保护级别。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称值说明CONTENT_PROTECTION_LEVEL_UNKNOWN0未知内容保护级别。CONTENT_PROTECTION_LEVEL_SW_CRYPTO1软件内容保护级别。CONTENT_PROTECTION_LEVEL_HW_CRYPTO2硬件内容保护级别。CONTENT_PROTECTION_LEVEL_ENHANCED_HW3硬件增强内容保护级别。CONTENT_PROTECTION_LEVEL_MAX4最高内容保护级别。