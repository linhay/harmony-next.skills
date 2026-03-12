# DisplaySoloist_ExpectedRateRange

```ets
typedef struct {...} DisplaySoloist_ExpectedRateRange
```

#### 概述

提供期望帧率范围结构体。

**起始版本：** 12

**相关模块：**[NativeDisplaySoloist](NativeDisplaySoloist.md)

**所在头文件：**[native_display_soloist.h](native_display_soloist.h.md)

#### 汇总

#### 成员变量

名称描述int32_t min期望帧率范围最小值，取值范围为[0,120]。int32_t max期望帧率范围最大值，取值范围为[0,120]。int32_t expected期望帧率，取值范围为[0,120]。

#### 成员函数

名称typedef关键字描述[typedef void (*OH_DisplaySoloist_FrameCallback)(long long timestamp, long long targetTimestamp, void* data)](#ZH-CN_TOPIC_0000002497446046__oh_displaysoloist_framecallback)OH_DisplaySoloist_FrameCallback()

OH_DisplaySoloist回调函数类型。

**起始版本：** 12

#### 成员函数说明

#### OH_DisplaySoloist_FrameCallback()

```ets
typedef void (*OH_DisplaySoloist_FrameCallback)(long long timestamp, long long targetTimestamp, void* data)
```

**描述**

OH_DisplaySoloist回调函数类型。

**起始版本：** 12

**参数：**

参数项描述long long timestamp当前帧VSync时间戳。long long targetTimestamp预期的下一帧VSync时间戳。void* data用户自定义数据。