# Camera_FrameShutterInfo

```ets
typedef struct Camera_FrameShutterInfo {...} Camera_FrameShutterInfo
```

#### 概述

帧快门回调信息。

**起始版本：** 11

**相关模块：**[OH_Camera](../media/OH_Camera.md)

**所在头文件：**[camera.h](../../capi/headers/camera.h.md)

#### 汇总

#### 成员变量

名称描述int32_t captureId捕获id。uint64_t timestamp帧的时间戳，单位毫秒。