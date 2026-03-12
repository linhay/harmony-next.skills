# native_mediakeysession.h

#### 概述

定义Drm MediaKeySession API。提供以下功能：

 生成媒体密钥请求、处理媒体密钥响应、事件监听、获取内容保护级别、检查媒体密钥状态、删除媒体密钥等。

**引用文件：** <multimedia/drm_framework/native_mediakeysession.h>

**库：** libnative_drm.so

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

**相关模块：**[Drm](Drm.md)

#### 汇总

#### 结构体

名称typedef关键字描述[MediaKeySession_Callback](MediaKeySession_Callback.md)MediaKeySession_CallbackMediaKeySession_Callback结构体，用于监听密钥过期、密钥更改等事件，不返回媒体密钥会话实例，适用于单媒体密钥会话解密场景。[OH_MediaKeySession_Callback](OH_MediaKeySession_Callback.md)OH_MediaKeySession_CallbackOH_MediaKeySession_Callback结构体，用于监听密钥过期、密钥更改等事件，返回媒体密钥会话实例，适用多个媒体密钥会话解密场景。

#### 函数

名称typedef关键字描述[typedef Drm_ErrCode (*MediaKeySession_EventCallback)(DRM_EventType eventType, uint8_t *info,int32_t infoLen, char *extra)](#ZH-CN_TOPIC_0000002497445850__mediakeysession_eventcallback)MediaKeySession_EventCallbackMediaKeySession事件触发时将调用的回调，如密钥过期事件。[typedef Drm_ErrCode (*MediaKeySession_KeyChangeCallback)(DRM_KeysInfo *keysInfo, bool newKeysAvailable)](#ZH-CN_TOPIC_0000002497445850__mediakeysession_keychangecallback)MediaKeySession_KeyChangeCallback密钥变更时将调用回调。[typedef Drm_ErrCode (*OH_MediaKeySession_EventCallback)(MediaKeySession *mediaKeySession, DRM_EventType eventType,uint8_t *info, int32_t infoLen, char *extra)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_eventcallback)OH_MediaKeySession_EventCallback事件触发时将调用的回调。[typedef Drm_ErrCode (*OH_MediaKeySession_KeyChangeCallback)(MediaKeySession *mediaKeySession, DRM_KeysInfo *keysInfo, bool newKeysAvailable)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_keychangecallback)OH_MediaKeySession_KeyChangeCallback密钥变更时将调用的回调。[Drm_ErrCode OH_MediaKeySession_GenerateMediaKeyRequest(MediaKeySession *mediaKeySession, DRM_MediaKeyRequestInfo *info, DRM_MediaKeyRequest *mediaKeyRequest)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_generatemediakeyrequest)-生成媒体密钥请求。[Drm_ErrCode OH_MediaKeySession_ProcessMediaKeyResponse(MediaKeySession *mediaKeySession, uint8_t *response, int32_t responseLen, uint8_t *offlineMediaKeyId, int32_t *offlineMediaKeyIdLen)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_processmediakeyresponse)-处理媒体密钥请求响应。[Drm_ErrCode OH_MediaKeySession_CheckMediaKeyStatus(MediaKeySession *mediaKeySession, DRM_MediaKeyStatus *mediaKeyStatus)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_checkmediakeystatus)-检查媒体密钥状态。[Drm_ErrCode OH_MediaKeySession_ClearMediaKeys(MediaKeySession *mediaKeySession)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_clearmediakeys)-清除当前会话的媒体密钥。[Drm_ErrCode OH_MediaKeySession_GenerateOfflineReleaseRequest(MediaKeySession *mediaKeySession, uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen, uint8_t *releaseRequest,int32_t *releaseRequestLen)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_generateofflinereleaserequest)-生成离线媒体密钥释放请求。[Drm_ErrCode OH_MediaKeySession_ProcessOfflineReleaseResponse(MediaKeySession *mediaKeySession, uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen, uint8_t *releaseResponse,int32_t releaseResponseLen)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_processofflinereleaseresponse)-处理离线媒体密钥释放请求响应。[Drm_ErrCode OH_MediaKeySession_RestoreOfflineMediaKeys(MediaKeySession *mediaKeySession, uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_restoreofflinemediakeys)-恢复离线媒体密钥到当前会话。[Drm_ErrCode OH_MediaKeySession_GetContentProtectionLevel(MediaKeySession *mediaKeySession, DRM_ContentProtectionLevel *contentProtectionLevel)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_getcontentprotectionlevel)-获取会话的内容保护级别。[Drm_ErrCode OH_MediaKeySession_RequireSecureDecoderModule(MediaKeySession *mediaKeySession, const char *mimeType, bool *status)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_requiresecuredecodermodule)-是否需要安全解码。[Drm_ErrCode OH_MediaKeySession_SetMediaKeySessionCallback(MediaKeySession *mediaKeySession, MediaKeySession_Callback *callback)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_setmediakeysessioncallback)-设置MediaKeySession事件回调。[Drm_ErrCode OH_MediaKeySession_SetCallback(MediaKeySession *mediaKeySession, OH_MediaKeySession_Callback *callback)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_setcallback)-设置MediaKeySession事件回调。[Drm_ErrCode OH_MediaKeySession_Destroy(MediaKeySession *mediaKeySession)](#ZH-CN_TOPIC_0000002497445850__oh_mediakeysession_destroy)-销毁MediaKeySession实例。

#### 函数说明

#### MediaKeySession_EventCallback()

```ets
typedef  Drm_ErrCode (*MediaKeySession_EventCallback)(DRM_EventType eventType, uint8_t *info,int32_t infoLen, char *extra)
```

**描述**

MediaKeySession事件触发时将调用的回调，如密钥过期事件。

**起始版本：** 11

**参数：**

参数项描述[DRM_EventType](native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_eventtype) eventType事件类型。uint8_t *info从媒体密钥会话获取的事件信息。int32_t infoLen事件信息长度。char *extra从媒体密钥会话中获得的额外信息。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)错误码。

#### MediaKeySession_KeyChangeCallback()

```ets
typedef  Drm_ErrCode (*MediaKeySession_KeyChangeCallback)(DRM_KeysInfo *keysInfo, bool newKeysAvailable)
```

**描述**

密钥变更时将调用回调。

**起始版本：** 11

**参数：**

参数项描述[DRM_KeysInfo](DRM_KeysInfo.md) *keysInfo密钥信息。bool newKeysAvailable新密钥是否可用。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：参数检查失败。

#### OH_MediaKeySession_EventCallback()

```ets
typedef Drm_ErrCode (*OH_MediaKeySession_EventCallback)(MediaKeySession *mediaKeySession, DRM_EventType eventType,uint8_t *info, int32_t infoLen, char *extra)
```

**描述**

事件触发时将调用的回调。

**起始版本：** 12

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySession会话实例。[DRM_EventType](native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_eventtype) eventType事件类型。uint8_t *info事件信息。int32_t infoLen事件信息长度。char *extra增量信息。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)错误码。

#### OH_MediaKeySession_KeyChangeCallback()

```ets
typedef Drm_ErrCode (*OH_MediaKeySession_KeyChangeCallback)(MediaKeySession *mediaKeySession, DRM_KeysInfo *keysInfo,bool newKeysAvailable)
```

**描述**

密钥变更时将调用的回调。

**起始版本：** 12

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySession媒体密钥会话实例。[DRM_KeysInfo](DRM_KeysInfo.md) *keysInfo密钥信息。bool newKeysAvailable新密钥是否可用，true表示可用，false表示不可用。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：参数检查失败。

#### OH_MediaKeySession_GenerateMediaKeyRequest()

```ets
Drm_ErrCode OH_MediaKeySession_GenerateMediaKeyRequest(MediaKeySession *mediaKeySession,DRM_MediaKeyRequestInfo *info, DRM_MediaKeyRequest *mediaKeyRequest)
```

**描述**

生成媒体密钥请求。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。[DRM_MediaKeyRequestInfo](DRM_MediaKeyRequestInfo.md) *info媒体密钥请求信息。[DRM_MediaKeyRequest](DRM_MediaKeyRequest.md) *mediaKeyRequest媒体密钥请求。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效，或输入参数info为空指针，或输入参数mediaKeyRequest为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySession_ProcessMediaKeyResponse()

```ets
Drm_ErrCode OH_MediaKeySession_ProcessMediaKeyResponse(MediaKeySession *mediaKeySession,uint8_t *response, int32_t responseLen, uint8_t *offlineMediaKeyId, int32_t *offlineMediaKeyIdLen)
```

**描述**

处理媒体密钥请求响应。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。uint8_t *response媒体密钥请求响应。int32_t responseLen媒体密钥请求响应长度。uint8_t *offlineMediaKeyId离线媒体密钥标识。int32_t *offlineMediaKeyIdLen离线媒体密钥标识的长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效，或其它指针类型输入参数为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySession_CheckMediaKeyStatus()

```ets
Drm_ErrCode OH_MediaKeySession_CheckMediaKeyStatus(MediaKeySession *mediaKeySession,DRM_MediaKeyStatus *mediaKeyStatus)
```

**描述**

检查媒体密钥状态。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。[DRM_MediaKeyStatus](DRM_MediaKeyStatus.md) *mediaKeyStatus媒体密钥状态。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效，或输入参数mediaKeyStatus为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySession_ClearMediaKeys()

```ets
Drm_ErrCode OH_MediaKeySession_ClearMediaKeys(MediaKeySession *mediaKeySession)
```

**描述**

清除当前会话的媒体密钥。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySession_GenerateOfflineReleaseRequest()

```ets
Drm_ErrCode OH_MediaKeySession_GenerateOfflineReleaseRequest(MediaKeySession *mediaKeySession,uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen, uint8_t *releaseRequest,int32_t *releaseRequestLen)
```

**描述**

生成离线媒体密钥释放请求。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。uint8_t *offlineMediaKeyId离线媒体密钥标识。int32_t *releaseRequestLen离线媒体密钥标识长度。uint8_t *releaseRequest离线媒体密钥释放请求。int32_t *releaseRequestLen离线媒体密钥释放请求长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_NO_MEMORY：内存不足，内存分配失败。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效，或其它指针类型输入参数为空指针。

DRM_ERR_UNKNOWN：发生内部错误或设备上的DRM解决方案不支持离线媒体密钥释放，请查看日志详细信息。

#### OH_MediaKeySession_ProcessOfflineReleaseResponse()

```ets
Drm_ErrCode OH_MediaKeySession_ProcessOfflineReleaseResponse(MediaKeySession *mediaKeySession,uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen, uint8_t *releaseResponse,int32_t releaseResponseLen)
```

**描述**

处理离线媒体密钥释放请求响应。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。uint8_t *offlineMediaKeyId离线媒体密钥标识。int32_t offlineMediaKeyIdLen离线媒体密钥标识长度。uint8_t *releaseResponse媒体密钥释放请求响应。int32_t releaseResponseLen媒体密钥释放请求响应长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效，或其它指针类型输入参数为空指针。

DRM_ERR_UNKNOWN：发生内部错误或设备上的DRM解决方案不支持离线媒体密钥释放，请查看日志详细信息。

#### OH_MediaKeySession_RestoreOfflineMediaKeys()

```ets
Drm_ErrCode OH_MediaKeySession_RestoreOfflineMediaKeys(MediaKeySession *mediaKeySession,uint8_t *offlineMediaKeyId, int32_t offlineMediaKeyIdLen)
```

**描述**

恢复离线媒体密钥到当前会话。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。uint8_t *offlineMediaKeyId离线媒体密钥标识。int32_t offlineMediaKeyIdLen离线媒体密钥标识长度。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效，或其它指针类型输入参数为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySession_GetContentProtectionLevel()

```ets
Drm_ErrCode OH_MediaKeySession_GetContentProtectionLevel(MediaKeySession *mediaKeySession,DRM_ContentProtectionLevel *contentProtectionLevel)
```

**描述**

获取会话的内容保护级别。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。[DRM_ContentProtectionLevel](native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_contentprotectionlevel) *contentProtectionLevel内容保护级别。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效，或输入参数contentProtectionLevel为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySession_RequireSecureDecoderModule()

```ets
Drm_ErrCode OH_MediaKeySession_RequireSecureDecoderModule(MediaKeySession *mediaKeySession,const char *mimeType, bool *status)
```

**描述**

是否需要安全解码。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。const char *mimeType媒体类型，支持的媒体类型取决于DRM解决方案，如：video/avc、video/hev。bool *status安全解码模块状态。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效，或其它指针类型输入参数为空指针。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。

#### OH_MediaKeySession_SetMediaKeySessionCallback()

```ets
Drm_ErrCode OH_MediaKeySession_SetMediaKeySessionCallback(MediaKeySession *mediaKeySession,MediaKeySession_Callback *callback)
```

**描述**

设置MediaKeySession事件回调。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。[MediaKeySession_Callback](MediaKeySession_Callback.md) *callbackMediaKeySession的回调。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效，或输入参数callback为空指针。

#### OH_MediaKeySession_SetCallback()

```ets
Drm_ErrCode OH_MediaKeySession_SetCallback(MediaKeySession *mediaKeySession,OH_MediaKeySession_Callback *callback)
```

**描述**

设置MediaKeySession事件回调。

**起始版本：** 12

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。[OH_MediaKeySession_Callback](OH_MediaKeySession_Callback.md) *callbackMediaKeySession的回调。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效，或输入参数callback为空指针。

#### OH_MediaKeySession_Destroy()

```ets
Drm_ErrCode OH_MediaKeySession_Destroy(MediaKeySession *mediaKeySession)
```

**描述**

销毁MediaKeySession实例。

**起始版本：** 11

**参数：**

参数项描述[MediaKeySession](MediaKeySession.md) *mediaKeySessionMediaKeySession实例。

**返回：**

类型说明[Drm_ErrCode](native_drm_err.h.md#ZH-CN_TOPIC_0000002497605830__drm_errcode)

DRM_ERR_OK：执行成功。

DRM_ERR_INVALID_VAL：输入参数mediaKeySession为空指针或无效。

DRM_ERR_UNKNOWN：发生内部错误，请查看日志详细信息。