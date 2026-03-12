# DRM_OfflineMediakeyIdArray

```ets
typedef struct DRM_OfflineMediakeyIdArray {...} DRM_OfflineMediakeyIdArray
```

#### 概述

离线媒体密钥ID数组。

**起始版本：** 11

**相关模块：**[Drm](Drm.md)

**所在头文件：**[native_drm_common.h](native_drm_common.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t idsCountID计数。int32_t idsLen[MAX_OFFLINE_MEDIA_KEY_ID_COUNT]ID长度集合。uint8_t ids[MAX_OFFLINE_MEDIA_KEY_ID_COUNT][MAX_OFFLINE_MEDIA_KEY_ID_LEN]ID数据集合。