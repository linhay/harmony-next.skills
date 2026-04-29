# Camera_ConcurrentInfo

```ets
typedef struct Camera_ConcurrentInfo {...} Camera_ConcurrentInfo
```

#### 概述

相机并发能力信息。

**起始版本：** 18

**相关模块：**[OH_Camera](OH_Camera.md)

所在头文件： [camera.h](camera.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Camera_Device](Camera_Device.md) camera | 相机实例。 |
| [Camera_ConcurrentType](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_concurrenttype) type | 相机并发状态。 |
| [Camera_SceneMode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_scenemode)* sceneModes | 相机并发支持的模式。 |
| [Camera_OutputCapability](Camera_OutputCapability.md)* outputCapabilities | 相机输出能力集。 |
| uint32_t modeAndCapabilitySize | 相机输出能力集大小。 |
