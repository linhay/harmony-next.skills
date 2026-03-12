# native_mediakeysystem.h

#### 概述

定义Drm MediaKeySystem API。提供以下功能：

查询是否支持特定的drm、创建媒体密钥会话、获取和设置配置、获取统计信息、获取内容保护级别、生成提供请求、处理提供响应、事件监听、获取内容防护级别、管理离线媒体密钥等。

**引用文件：** <multimedia/drm_framework/native_mediakeysystem.h>

**库：** libnative_drm.so

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

**相关模块：**[Drm](Drm.md)

#### 汇总

#### 函数

名称typedef关键字描述[typedef Drm_ErrCode (*MediaKeySystem_Callback)(DRM_EventType eventType, uint8_t *info, int32_t infoLen, char *extra)](#ZH-CN_TOPIC_0000002529285821__mediakeysystem_callback)MediaKeySystem_CallbackMediaKeySystem事件触发时将调用的回调，不返回MediaKeySystem实例，适用于单个MediaKeySystem场景。[typedef Drm_ErrCode (*OH_MediaKeySystem_Callback)(MediaKeySystem *mediaKeySystem, DRM_EventType eventType, uint8_t *info, int32_t infoLen, char *extra)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_callback)OH_MediaKeySystem_CallbackMediaKeySystem事件触发时将调用的回调，返回MediaKeySystem实例，适用于多个MediaKeySystem场景。[Drm_ErrCode OH_MediaKeySystem_SetCallback(MediaKeySystem *mediaKeySystem, OH_MediaKeySystem_Callback callback)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_setcallback)-设置MediaKeySystem事件回调。[Drm_ErrCode OH_MediaKeySystem_GetMediaKeySystems(DRM_MediaKeySystemDescription *infos, uint32_t *count)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_getmediakeysystems)-获取设备支持的DRM解决方案的名称和唯一标识的列表。[bool OH_MediaKeySystem_IsSupported(const char *name)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_issupported)-查询设备是否支持对应的DRM解决方案。[bool OH_MediaKeySystem_IsSupported2(const char *name, const char *mimeType)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_issupported2)-查询设备是否支持对应的DRM解决方案名称及媒体类型。[bool OH_MediaKeySystem_IsSupported3(const char *name, const char *mimeType, DRM_ContentProtectionLevel contentProtectionLevel)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_issupported3)-查询设备是否支持对应的DRM解决方案、媒体类型、内容保护级别。[Drm_ErrCode OH_MediaKeySystem_Create(const char *name, MediaKeySystem **mediaKeySystem)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_create)-创建MediaKeySystem实例。[Drm_ErrCode OH_MediaKeySystem_SetConfigurationString(MediaKeySystem *mediaKeySystem, const char *configName, const char *value)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_setconfigurationstring)-设置字符串类型的配置属性。[Drm_ErrCode OH_MediaKeySystem_GetConfigurationString(MediaKeySystem *mediaKeySystem, const char *configName, char *value, int32_t valueLen)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_getconfigurationstring)-获取字符串类型配置属性值。[Drm_ErrCode OH_MediaKeySystem_SetConfigurationByteArray(MediaKeySystem *mediaKeySystem, const char *configName, uint8_t *value, int32_t valueLen)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_setconfigurationbytearray)-设置字符数组类型的配置属性值。[Drm_ErrCode OH_MediaKeySystem_GetConfigurationByteArray(MediaKeySystem *mediaKeySystem, const char *configName, uint8_t *value, int32_t *valueLen)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_getconfigurationbytearray)-获取字符数组类型配置属性值。[Drm_ErrCode OH_MediaKeySystem_GetStatistics(MediaKeySystem *mediaKeySystem, DRM_Statistics *statistics)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_getstatistics)-获取度量记录。[Drm_ErrCode OH_MediaKeySystem_GetMaxContentProtectionLevel(MediaKeySystem *mediaKeySystem, DRM_ContentProtectionLevel *contentProtectionLevel)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_getmaxcontentprotectionlevel)-获取设备支持的最大内容保护级别。[Drm_ErrCode OH_MediaKeySystem_SetMediaKeySystemCallback(MediaKeySystem *mediaKeySystem, MediaKeySystem_Callback callback)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_setmediakeysystemcallback)-设置MediaKeySystem事件回调。[Drm_ErrCode OH_MediaKeySystem_CreateMediaKeySession(MediaKeySystem *mediaKeySystem, DRM_ContentProtectionLevel *level, MediaKeySession **mediaKeySession)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_createmediakeysession)-创建MediaKeySession会话实例。[Drm_ErrCode OH_MediaKeySystem_GenerateKeySystemRequest(MediaKeySystem *mediaKeySystem, uint8_t *request, int32_t *requestLen, char *defaultUrl, int32_t defaultUrlLen)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_generatekeysystemrequest)-生成设备DRM证书请求。[Drm_ErrCode OH_MediaKeySystem_ProcessKeySystemResponse(MediaKeySystem *mediaKeySystem, uint8_t *response, int32_t responseLen)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_processkeysystemresponse)-处理设备DRM证书请求响应。[Drm_ErrCode OH_MediaKeySystem_GetOfflineMediaKeyIds(MediaKeySystem *mediaKeySystem, DRM_OfflineMediakeyIdArray *offlineMediaKeyIds)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_getofflinemediakeyids)-获取离线媒体密钥标识列表，媒体密钥标识用于对离线媒体密钥的管理。[Drm_ErrCode OH_MediaKeySystem_GetOfflineMediaKeyStatus(MediaKeySystem *mediaKeySystem, uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen, DRM_OfflineMediaKeyStatus *status)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_getofflinemediakeystatus)-获取离线媒体密钥状态。[Drm_ErrCode OH_MediaKeySystem_ClearOfflineMediaKeys(MediaKeySystem *mediaKeySystem, uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_clearofflinemediakeys)-按id清除离线媒体密钥。[Drm_ErrCode OH_MediaKeySystem_GetCertificateStatus(MediaKeySystem *mediaKeySystem, DRM_CertificateStatus *certStatus)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_getcertificatestatus)-获取设备DRM证书状态。[Drm_ErrCode OH_MediaKeySystem_Destroy(MediaKeySystem *mediaKeySystem)](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_destroy)-销毁MediaKeySystem实例。

#### 函数说明

#### MediaKeySystem_Callback()

```ets
typedef  Drm_ErrCode (*MediaKeySystem_Callback)(DRM_EventType eventType, uint8_t *info,int32_t infoLen, char *extra)
```

**描述**

MediaKeySystem事件触发时将调用的回调，不返回MediaKeySystem实例，适用于单个MediaKeySystem场景。

**起始版本：** 11

**参数：**

参数项描述[DRM_EventType](native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_eventtype) eventType事件类型。uint8_t *info事件信息。int32_t infoLen事件信息长度。char *extra增量信息。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数无效。

#### OH_MediaKeySystem_Callback()

```ets
typedef Drm_ErrCode (*OH_MediaKeySystem_Callback)(MediaKeySystem *mediaKeySystem, DRM_EventType eventType,uint8_t *info, int32_t infoLen, char *extra)
```

**描述**

MediaKeySystem事件触发时将调用的回调，返回MediaKeySystem实例，适用于多个MediaKeySystem场景。

**起始版本：** 12

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。[DRM_EventType](native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_eventtype) eventType事件类型。uint8_t *info事件信息。int32_t infoLen事件信息长度。char *extra增量信息。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数无效。

#### OH_MediaKeySystem_SetCallback()

```ets
Drm_ErrCode OH_MediaKeySystem_SetCallback(MediaKeySystem *mediaKeySystem, OH_MediaKeySystem_Callback callback)
```

**描述**

设置MediaKeySystem事件回调。

**起始版本：** 12

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。[OH_MediaKeySystem_Callback](#ZH-CN_TOPIC_0000002529285821__oh_mediakeysystem_callback) callback回调函数。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效。

#### OH_MediaKeySystem_GetMediaKeySystems()

```ets
Drm_ErrCode OH_MediaKeySystem_GetMediaKeySystems(DRM_MediaKeySystemDescription *infos, uint32_t *count)
```

**描述**

获取设备支持的DRM解决方案的名称和唯一标识的列表。

**起始版本：** 12

**参数：**

参数项描述[DRM_MediaKeySystemDescription](DRM_MediaKeySystemDescription.md) *infosDRM解决方案名称和唯一标识的列表。uint32_t *countDRM解决方案名称和唯一标识的列表长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：可能原因：

 1.输入参数infos为空指针或输入参数count为空指针。

 2.输入参数infos长度不足。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_IsSupported()

```ets
bool OH_MediaKeySystem_IsSupported(const char *name)
```

**描述**

查询设备是否支持对应的DRM解决方案。

**起始版本：** 11

**参数：**

参数项描述const char *nameDRM解决方案名称。

**返回：**

类型说明bool表示是否支持指定DRM解决方案。true表示支持，false表示不支持。

#### OH_MediaKeySystem_IsSupported2()

```ets
bool OH_MediaKeySystem_IsSupported2(const char *name, const char *mimeType)
```

**描述**

查询设备是否支持对应的DRM解决方案名称及媒体类型。

**起始版本：** 11

**参数：**

参数项描述const char *nameDRM解决方案名称。const char *mimeType媒体类型，支持的媒体类型取决于DRM解决方案，如：video/avc、video/hev。

**返回：**

类型说明bool表示是否支持指定DRM解决方案及媒体类型。true表示支持，false表示不支持。

#### OH_MediaKeySystem_IsSupported3()

```ets
bool OH_MediaKeySystem_IsSupported3(const char *name, const char *mimeType,DRM_ContentProtectionLevel contentProtectionLevel)
```

**描述**

查询设备是否支持对应的DRM解决方案、媒体类型、内容保护级别。

**起始版本：** 11

**参数：**

参数项描述const char *nameDRM解决方案名称。const char *mimeType媒体类型，支持的媒体类型取决于DRM解决方案，如：video/avc、video/hev。[DRM_ContentProtectionLevel](native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_contentprotectionlevel) contentProtectionLevel内容保护级别。

**返回：**

类型说明bool表示是否支持指定DRM解决方案，媒体类型以及内容保护级别。true表示支持，false表示不支持。

#### OH_MediaKeySystem_Create()

```ets
Drm_ErrCode OH_MediaKeySystem_Create(const char *name, MediaKeySystem **mediaKeySystem)
```

**描述**

创建MediaKeySystem实例。

**起始版本：** 11

**参数：**

参数项描述const char *nameDRM解决方案名称。[MediaKeySystem](MediaKeySystem.md) **mediaKeySystemMediaKeySystem实例。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：可能原因：

 1.输入参数name为空指针或长度为0。

 2.输入参数mediaKeySystem为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

DRM_ERR_SERVICE_DIED：服务死亡。

DRM_ERR_MAX_SYSTEM_NUM_REACHED：已创建的MediaKeySystem数量达到最大限制(64个)。

#### OH_MediaKeySystem_SetConfigurationString()

```ets
Drm_ErrCode OH_MediaKeySystem_SetConfigurationString(MediaKeySystem *mediaKeySystem,const char *configName, const char *value)
```

**描述**

设置字符串类型的配置属性。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。const char *configName字符串类型配置属性名，不能为空，具体支持的属性名由设备上DRM解决方案决定。const char *value字符串类型配置属性值，不能为空，具体支持的属性值由设备上DRM解决方案决定。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，输入参数configName为空指针，或输入参数value为空指针。

#### OH_MediaKeySystem_GetConfigurationString()

```ets
Drm_ErrCode OH_MediaKeySystem_GetConfigurationString(MediaKeySystem *mediaKeySystem,const char *configName, char *value, int32_t valueLen)
```

**描述**

获取字符串类型配置属性值。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。const char *configName字符串类型配置名。char *value字符串类型配置值。int32_t valueLen字符串类型配置值长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，输入参数configName为空指针，或输入参数value为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_SetConfigurationByteArray()

```ets
Drm_ErrCode OH_MediaKeySystem_SetConfigurationByteArray(MediaKeySystem *mediaKeySystem,const char *configName, uint8_t *value, int32_t valueLen)
```

**描述**

设置字符数组类型的配置属性值。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。const char *configName字符数组类型配置属性名，不能为空，具体支持的属性名由设备上DRM解决方案决定。uint8_t *value字符数组类型配置属性值，不能为空，具体支持的属性值由设备上DRM解决方案决定。int32_t valueLen字符数组类型配置属性值长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，输入参数configName为空指针，或输入参数value为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_GetConfigurationByteArray()

```ets
Drm_ErrCode OH_MediaKeySystem_GetConfigurationByteArray(MediaKeySystem *mediaKeySystem,const char *configName, uint8_t *value, int32_t *valueLen)
```

**描述**

获取字符数组类型配置属性值。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。const char *configName字符数组类型配置属性名称，不能为空，具体支持的属性名由设备上DRM解决方案决定。uint8_t *value字符数组类型配置属性。int32_t *valueLen字符数组类型配置属性长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，输入参数configName为空指针，输入参数value为空指针，或valueLen为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_GetStatistics()

```ets
Drm_ErrCode OH_MediaKeySystem_GetStatistics(MediaKeySystem *mediaKeySystem, DRM_Statistics *statistics)
```

**描述**

获取度量记录。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。[DRM_Statistics](DRM_Statistics.md) *statistics度量记录。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数statistics为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_GetMaxContentProtectionLevel()

```ets
Drm_ErrCode OH_MediaKeySystem_GetMaxContentProtectionLevel(MediaKeySystem *mediaKeySystem,DRM_ContentProtectionLevel *contentProtectionLevel)
```

**描述**

获取设备支持的最大内容保护级别。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。[DRM_ContentProtectionLevel](native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_contentprotectionlevel) *contentProtectionLevel内容保护级别。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数contentProtectionLevel为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_SetMediaKeySystemCallback()

```ets
Drm_ErrCode OH_MediaKeySystem_SetMediaKeySystemCallback(MediaKeySystem *mediaKeySystem,MediaKeySystem_Callback callback)
```

**描述**

设置MediaKeySystem事件回调。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。[MediaKeySystem_Callback](#ZH-CN_TOPIC_0000002529285821__mediakeysystem_callback) callback回调函数。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效。

#### OH_MediaKeySystem_CreateMediaKeySession()

```ets
Drm_ErrCode OH_MediaKeySystem_CreateMediaKeySession(MediaKeySystem *mediaKeySystem,DRM_ContentProtectionLevel *level, MediaKeySession **mediaKeySession)
```

**描述**

创建MediaKeySession会话实例。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。[DRM_ContentProtectionLevel](native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_contentprotectionlevel) *level内容保护级别。[MediaKeySession](MediaKeySession.md) **mediaKeySessionMediaKeySession实例。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数level超出合理范围，或mediaKeySession为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

DRM_ERR_SERVICE_DIED：服务死亡。

DRM_ERR_MAX_SESSION_NUM_REACHED：当前MediaKeySystem已创建的MediaKeySession数量达到最大限制(64个)。

#### OH_MediaKeySystem_GenerateKeySystemRequest()

```ets
Drm_ErrCode OH_MediaKeySystem_GenerateKeySystemRequest(MediaKeySystem *mediaKeySystem, uint8_t *request,int32_t *requestLen, char *defaultUrl, int32_t defaultUrlLen)
```

**描述**

生成设备DRM证书请求。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。uint8_t *request设备DRM证书请求。int32_t *requestLen设备DRM证书请求的长度。char *defaultUrl设备DRM证书服务的URL。int32_t defaultUrlLen设备DRM证书服务的URL长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，或其它指针类型输入参数为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_ProcessKeySystemResponse()

```ets
Drm_ErrCode OH_MediaKeySystem_ProcessKeySystemResponse(MediaKeySystem *mediaKeySystem,uint8_t *response, int32_t responseLen)
```

**描述**

处理设备DRM证书请求响应。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。uint8_t *response设备DRM证书请求响应。int32_t responseLen设备DRM证书请求响应长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数response为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_GetOfflineMediaKeyIds()

```ets
Drm_ErrCode OH_MediaKeySystem_GetOfflineMediaKeyIds(MediaKeySystem *mediaKeySystem,DRM_OfflineMediakeyIdArray *offlineMediaKeyIds)
```

**描述**

获取离线媒体密钥标识列表，媒体密钥标识用于对离线媒体密钥的管理。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。[DRM_OfflineMediakeyIdArray](DRM_OfflineMediakeyIdArray.md) *offlineMediaKeyIds离线媒体密钥的媒体密钥标识列表。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数offlineMediaKeyIds为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_GetOfflineMediaKeyStatus()

```ets
Drm_ErrCode OH_MediaKeySystem_GetOfflineMediaKeyStatus(MediaKeySystem *mediaKeySystem,uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen, DRM_OfflineMediaKeyStatus *status)
```

**描述**

获取离线媒体密钥状态。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。uint8_t *offlineMediaKeyId离线媒体密钥标识。int32_t offlineMediaKeyIdLen离线媒体密钥标识长度。[DRM_OfflineMediaKeyStatus](native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_offlinemediakeystatus) *status媒体密钥状态。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，或其它指针类型输入参数为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_ClearOfflineMediaKeys()

```ets
Drm_ErrCode OH_MediaKeySystem_ClearOfflineMediaKeys(MediaKeySystem *mediaKeySystem,uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen)
```

**描述**

按id清除离线媒体密钥。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。uint8_t *offlineMediaKeyId离线媒体密钥标识。int32_t offlineMediaKeyIdLen离线媒体密钥标识长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数offlineMediaKeyId为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_GetCertificateStatus()

```ets
Drm_ErrCode OH_MediaKeySystem_GetCertificateStatus(MediaKeySystem *mediaKeySystem,DRM_CertificateStatus *certStatus)
```

**描述**

获取设备DRM证书状态。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。[DRM_CertificateStatus](native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_certificatestatus) *certStatus设备DRM证书状态值。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效，或输入参数certStatus为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySystem_Destroy()

```ets
Drm_ErrCode OH_MediaKeySystem_Destroy(MediaKeySystem *mediaKeySystem)
```

**描述**

销毁MediaKeySystem实例。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySystem](MediaKeySystem.md) *mediaKeySystemMediaKeySystem实例。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySystem为空指针或无效。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。