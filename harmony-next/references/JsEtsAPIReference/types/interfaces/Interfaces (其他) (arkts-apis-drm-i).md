[]()[]()

# Interfaces (其他)

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### ProvisionRequest

设备证书请求。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称类型只读可选说明dataUint8Array否否设备证书请求数据。defaultURLstring否否Provision服务（设备证书请求服务）URL。[]()[]()

#### OptionsData

设备证书请求的可选数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称类型只读可选说明namestring否否可选数据名。valuestring否否可选数据值。[]()[]()

#### MediaKeyRequest

媒体密钥请求参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称类型只读可选说明mediaKeyRequestType[MediaKeyRequestType](../../topics/networking/Enums (arkts-apis-drm-e).md#ZH-CN_TOPIC_0000002529285817__mediakeyrequesttype)否否媒体密钥请求类型。dataUint8Array否否媒体密钥请求数据。defaultURLstring否否媒体密钥服务URL。[]()[]()

#### EventInfo

事件信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称类型只读可选说明infoUint8Array否否事件信息数据。extraInfostring否否事件扩展信息。[]()[]()

#### StatisticKeyValue

度量记录。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称类型只读可选说明namestring否否度量记录名。valuestring否否度量记录值。[]()[]()

#### MediaKeyStatus

媒体密钥状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称类型只读可选说明namestring否否媒体密钥状态名称（如媒体密钥过期时间、内容保护安全级别等）。valuestring否否媒体密钥状态值。[]()[]()

#### KeysInfo

媒体密钥中密钥信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称类型只读可选说明keyIdUint8Array否否媒体密钥标识。valuestring否否媒体密钥状态值。[]()[]()

#### MediaKeySystemInfo

加密媒体内容的DRM信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称类型只读可选说明uuidstring否否DRM内容保护系统的唯一标识。psshUint8Array否否DRM内容保护系统专用头（Protection System Specific Header）。[]()[]()

#### MediaKeySystemDescription12+

插件信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Drm.Core

名称类型只读可选说明namestring否否插件名称。uuidstring否否插件唯一标识码。