# DRM_MediaKeyRequest

```ets
typedef struct DRM_MediaKeyRequest {...} DRM_MediaKeyRequest
```

#### 概述

媒体密钥请求。

**起始版本：** 11

**相关模块：**[Drm](../misc/Drm.md)

**所在头文件：**[native_drm_common.h](../../capi/headers/native_drm_common.h.md)

#### 汇总

#### 成员变量

名称描述[DRM_MediaKeyRequestType](../../capi/headers/native_drm_common.h.md#ZH-CN_TOPIC_0000002529445793__drm_mediakeyrequesttype) type媒体密钥请求类型。int32_t dataLen媒体密钥请求数据长度。uint8_t data[MAX_MEDIA_KEY_REQUEST_DATA_LEN]发送到媒体密钥服务器的媒体密钥请求数据。char defaultUrl[MAX_DEFAULT_URL_LEN]媒体密钥服务器URL。