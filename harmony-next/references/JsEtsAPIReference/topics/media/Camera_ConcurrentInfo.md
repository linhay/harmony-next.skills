# Camera_ConcurrentInfo

```ets
typedef struct Camera_ConcurrentInfo {...} Camera_ConcurrentInfo
```

#### 概述

相机并发能力信息。

**起始版本：** 18

**相关模块：**[OH_Camera](OH_Camera.md)

**所在头文件：**[camera.h](../../capi/headers/camera.h.md)

#### 汇总

#### 成员变量

名称描述[Camera_Device](../system-services/Camera_Device.md) camera相机实例。[Camera_ConcurrentType](../../capi/headers/camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_concurrenttype) type相机并发状态。[Camera_SceneMode](../../capi/headers/camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_scenemode)* sceneModes相机并发支持的模式。[Camera_OutputCapability](../system-services/Camera_OutputCapability.md)* outputCapabilities相机输出能力集。uint32_t modeAndCapabilitySize相机输出能力集大小。