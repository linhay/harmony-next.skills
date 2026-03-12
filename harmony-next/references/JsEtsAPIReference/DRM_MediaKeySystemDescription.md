# DRM_MediaKeySystemDescription

```ets
typedef struct DRM_MediaKeySystemDescription {...} DRM_MediaKeySystemDescription
```

#### 概述

DRM解决方案名称及其UUID的列表。

**起始版本：** 12

**相关模块：**[Drm](Drm.md)

**所在头文件：**[native_drm_common.h](native_drm_common.h.md)

#### 汇总

#### 成员变量

名称描述char name[MAX_MEDIA_KEY_SYSTEM_NAME_LEN]DRM插件的名称。uint8_t uuid[DRM_UUID_LEN]UUID。