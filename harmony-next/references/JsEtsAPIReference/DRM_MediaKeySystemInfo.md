# DRM_MediaKeySystemInfo

```ets
typedef struct DRM_MediaKeySystemInfo {...} DRM_MediaKeySystemInfo
```

#### 概述

加密媒体内容的DRM信息。

**起始版本：** 11

**相关模块：**[Drm](Drm.md)

**所在头文件：**[native_drm_common.h](native_drm_common.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t psshCountPSSH计数。[DRM_PsshInfo](DRM_PsshInfo.md) psshInfo[MAX_PSSH_INFO_COUNT]PSSH信息。