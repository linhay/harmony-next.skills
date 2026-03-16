# DRM_MediaKeyStatus

```ets
typedef struct DRM_MediaKeyStatus {...} DRM_MediaKeyStatus
```

#### 概述

媒体密钥状态。

**起始版本：** 11

**相关模块：**[Drm](../misc/Drm.md)

**所在头文件：**[native_drm_common.h](../../capi/headers/native_drm_common.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t statusCount状态计数。char statusName[MAX_MEDIA_KEY_STATUS_COUNT][MAX_MEDIA_KEY_STATUS_NAME_LEN]状态名数组。char statusValue[MAX_MEDIA_KEY_STATUS_COUNT][MAX_MEDIA_KEY_STATUS_VALUE_LEN]状态值数组。