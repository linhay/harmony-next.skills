# Camera_CaptureStartInfo

```ets
typedef struct Camera_CaptureStartInfo {...} Camera_CaptureStartInfo
```

#### 概述

拍照开始信息。

**起始版本：** 12

**相关模块：**[OH_Camera](../media/OH_Camera.md)

**所在头文件：**[camera.h](../../capi/headers/camera.h.md)

#### 汇总

#### 成员变量

名称描述int32_t captureId拍照id。int64_t time预估的单次拍照底层出sensor采集帧时间，如果上报-1，代表没有预估时间。