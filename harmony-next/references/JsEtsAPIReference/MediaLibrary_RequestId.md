# MediaLibrary_RequestId

```ets
typedef struct MediaLibrary_RequestId {...} MediaLibrary_RequestId
```

#### 概述

定义请求Id。

当请求媒体库资源时，会返回此类型。

请求Id可用于取消请求。

如果请求失败，值将全为零，如 "00000000-0000-0000-0000-000000000000"。

**起始版本：** 12

**相关模块：**[MediaAssetManager](MediaAssetManager.md)

**所在头文件：**[media_asset_base_capi.h](media_asset_base_capi.h.md)

#### 汇总

#### 成员变量

名称描述char requestId[UUID_STR_MAX_LENGTH]请求Id。