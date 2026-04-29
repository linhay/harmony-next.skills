# DisplaySoloist_ExpectedRateRange

```ets
typedef struct {...} DisplaySoloist_ExpectedRateRange
```

**概述**

提供期望帧率范围结构体。

起始版本： 12

相关模块： [NativeDisplaySoloist](NativeDisplaySoloist.md)

所在头文件： [native_display_soloist.h](native_display_soloist.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t min | 期望帧率范围最小值，取值范围为[0,120]。 |
| int32_t max | 期望帧率范围最大值，取值范围为[0,120]。 |
| int32_t expected | 期望帧率，取值范围为[0,120]。 |

**成员函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_DisplaySoloist_FrameCallback)(long long timestamp, long long targetTimestamp, void* data) | OH_DisplaySoloist_FrameCallback() | OH_DisplaySoloist回调函数类型。 起始版本： 12 |

**成员函数说明**

**OH_DisplaySoloist_FrameCallback()**

```ets
typedef void (*OH_DisplaySoloist_FrameCallback)(long long timestamp, long long targetTimestamp, void* data)
```

描述

OH_DisplaySoloist回调函数类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| long long timestamp | 当前帧VSync时间戳。 |
| long long targetTimestamp | 预期的下一帧VSync时间戳。 |
| void* data | 用户自定义数据。 |