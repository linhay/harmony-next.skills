# DRM_PsshInfo

```ets
typedef struct DRM_PsshInfo {...} DRM_PsshInfo
```

**概述**

DRM内容保护系统专用头（Protection System Specific Header）信息。

起始版本： 11

相关模块： [Drm](Drm.md)

所在头文件： [native_drm_common.h](native_drm_common.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint8_t uuid[DRM_UUID_LEN] | UUID的PSSH信息。 |
| int32_t dataLen | PSSH数据长度。 |
| uint8_t data[MAX_PSSH_DATA_LEN] | PSSH数据。 |