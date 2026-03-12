# DRM_Statistics

```ets
typedef struct DRM_Statistics {...} DRM_Statistics
```

#### 概述

MediaKeySystem的度量信息。

**起始版本：** 11

**相关模块：**[Drm](Drm.md)

**所在头文件：**[native_drm_common.h](native_drm_common.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t statisticsCount度量计数。char statisticsName[MAX_STATISTICS_COUNT][MAX_STATISTICS_NAME_LEN]度量信息名称集合。char statisticsDescription[MAX_STATISTICS_COUNT][MAX_STATISTICS_BUFFER_LEN]度量信息描述集合。