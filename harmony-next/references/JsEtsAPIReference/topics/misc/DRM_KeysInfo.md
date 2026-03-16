# DRM_KeysInfo

```ets
typedef struct DRM_KeysInfo {...} DRM_KeysInfo
```

#### 概述

媒体密钥信息。

**起始版本：** 11

**相关模块：**[Drm](Drm.md)

**所在头文件：**[native_drm_common.h](../../capi/headers/native_drm_common.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t keysInfoCount钥匙计数。uint8_t keyId[MAX_KEY_INFO_COUNT][MAX_KEY_ID_LEN]密钥ID集合。char statusValue[MAX_KEY_INFO_COUNT][MAX_KEY_STATUS_VALUE_LEN]关键状态值。