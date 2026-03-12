# OH_NativeVSync_ExpectedRateRange

```ets
typedef struct {...} OH_NativeVSync_ExpectedRateRange
```

#### 概述

期望帧率范围结构体。

**起始版本：** 20

**相关模块：**[NativeVsync](NativeVsync.md)

**所在头文件：**[native_vsync.h](native_vsync.h.md)

#### 汇总

#### 成员变量

名称描述int32_t min帧率范围的最小帧率。int32_t max帧率范围的最大帧率。int32_t expected帧率范围的期望帧率。

#### 成员函数

名称typedef关键字描述[typedef void (*OH_NativeVSync_FrameCallback)(long long timestamp, void *data)](#ZH-CN_TOPIC_0000002497446058__oh_nativevsync_framecallback)OH_NativeVSync_FrameCallback()

VSync回调函数类型。

**起始版本：** 9

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

#### 成员函数说明

#### OH_NativeVSync_FrameCallback()

```ets
typedef void (*OH_NativeVSync_FrameCallback)(long long timestamp, void *data)
```

**描述**

VSync回调函数类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 9

**参数：**

参数项描述long long timestampVSync使用CLOCK_MONOTONIC获取的系统时间戳, 单位为纳秒。void *data用户自定义数据。