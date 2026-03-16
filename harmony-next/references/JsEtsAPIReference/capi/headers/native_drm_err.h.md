# native_drm_err.h

#### 概述

定义DRM错误码。

**引用文件：** <multimedia/drm_framework/native_drm_err.h>

**库：** libnative_drm.so

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

**相关模块：**[Drm](../../topics/misc/Drm.md)

#### 汇总

#### 枚举

名称typedef关键字描述[Drm_ErrCode](#ZH-CN_TOPIC_0000002497605830__drm_errcode)Drm_ErrCodeDRM错误码。

#### 枚举类型说明

#### Drm_ErrCode

```ets
enum Drm_ErrCode
```

**描述**

DRM错误码。

**系统能力：** SystemCapability.Multimedia.Drm.Core

**起始版本：** 11

枚举项描述DRM_ERR_OK = 0操作成功完成。DRM_CAPI_ERR_BASE = 24700500基础错误。DRM_ERR_NO_MEMORY = DRM_CAPI_ERR_BASE + 1内存不足。DRM_ERR_OPERATION_NOT_PERMITTED = DRM_CAPI_ERR_BASE + 2不支持的操作。DRM_ERR_INVALID_VAL = DRM_CAPI_ERR_BASE + 3无效参数。DRM_ERR_IO = DRM_CAPI_ERR_BASE + 4IO错误。DRM_ERR_TIMEOUT = DRM_CAPI_ERR_BASE + 5网络超时。DRM_ERR_UNKNOWN = DRM_CAPI_ERR_BASE + 6未知错误。DRM_ERR_SERVICE_DIED = DRM_CAPI_ERR_BASE + 7drm服务死亡。DRM_ERR_INVALID_STATE = DRM_CAPI_ERR_BASE + 8无效的操作状态。DRM_ERR_UNSUPPORTED = DRM_CAPI_ERR_BASE + 9不支持的操作。DRM_ERR_MAX_SYSTEM_NUM_REACHED = DRM_CAPI_ERR_BASE + 10MediaKeySystem最大实例数。DRM_ERR_MAX_SESSION_NUM_REACHED = DRM_CAPI_ERR_BASE + 11MediaKeySession最大实例数。DRM_ERR_EXTEND_START = DRM_CAPI_ERR_BASE + 100扩展错误。