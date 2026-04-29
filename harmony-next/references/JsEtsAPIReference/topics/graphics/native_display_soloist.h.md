# native_display_soloist.h

**概述**

定义获取和使用NativeDisplaySoloist的相关函数。

引用文件： <native_display_soloist/native_display_soloist.h>

库： libnative_display_soloist.so

系统能力： SystemCapability.Graphic.Graphic2D.HyperGraphicManager

起始版本： 12

相关模块： [NativeDisplaySoloist](NativeDisplaySoloist.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| DisplaySoloist_ExpectedRateRange | DisplaySoloist_ExpectedRateRange | 提供期望帧率范围结构体。 |
| OH_DisplaySoloist | OH_DisplaySoloist | 提供OH_DisplaySoloist结构体声明。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_DisplaySoloist_FrameCallback)(long long timestamp, long long targetTimestamp, void* data) | OH_DisplaySoloist_FrameCallback | OH_DisplaySoloist回调函数类型。 |
| OH_DisplaySoloist* OH_DisplaySoloist_Create(bool useExclusiveThread) | - | 创建一个OH_DisplaySoloist实例，每次调用都会产生一个新的实例。 |
| int32_t OH_DisplaySoloist_Destroy(OH_DisplaySoloist* displaySoloist) | - | 销毁OH_DisplaySoloist实例并回收对象占用的内存。 |
| int32_t OH_DisplaySoloist_Start(OH_DisplaySoloist* displaySoloist, OH_DisplaySoloist_FrameCallback callback, void* data) | - | 设置每帧回调函数，每次VSync信号到来时启动每帧回调。 |
| int32_t OH_DisplaySoloist_Stop(OH_DisplaySoloist* displaySoloist) | - | 停止请求下一次VSync信号，并停止调用回调函数callback。 |
| int32_t OH_DisplaySoloist_SetExpectedFrameRateRange(OH_DisplaySoloist* displaySoloist, DisplaySoloist_ExpectedRateRange* range) | - | 设置VSync期望帧率范围。 |

**函数说明**

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

**OH_DisplaySoloist_Create()**

```ets
OH_DisplaySoloist* OH_DisplaySoloist_Create(bool useExclusiveThread)
```

描述

创建一个OH_DisplaySoloist实例，每次调用都会产生一个新的实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| bool useExclusiveThread | 表示此OH_DisplaySoloist实例是否是独占线程。true表示独占一个线程，false表示共享线程。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_DisplaySoloist* | 返回一个指向OH_DisplaySoloist实例的指针，如果返回空表示执行失败，可能的原因是内存不足。 |

**OH_DisplaySoloist_Destroy()**

```ets
int32_t OH_DisplaySoloist_Destroy(OH_DisplaySoloist* displaySoloist)
```

描述

销毁OH_DisplaySoloist实例并回收对象占用的内存。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DisplaySoloist* displaySoloist | 一个指向OH_DisplaySoloist实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回值为0表示执行成功，-1表示执行失败。 |

**OH_DisplaySoloist_Start()**

```ets
int32_t OH_DisplaySoloist_Start(OH_DisplaySoloist* displaySoloist, OH_DisplaySoloist_FrameCallback callback, void* data)
```

描述

设置每帧回调函数，每次VSync信号到来时启动每帧回调。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DisplaySoloist* displaySoloist | 一个指向OH_DisplaySoloist实例的指针。 |
| OH_DisplaySoloist_FrameCallback callback | 表示下一次VSync信号到来时执行的回调函数类型。 |
| void* data | 一个指向用户自定义数据结构的指针，类型是void。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回值为0表示执行成功，-1表示执行失败。 |

**OH_DisplaySoloist_Stop()**

```ets
int32_t OH_DisplaySoloist_Stop(OH_DisplaySoloist* displaySoloist)
```

描述

停止请求下一次VSync信号，并停止调用回调函数callback。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DisplaySoloist* displaySoloist | 一个指向OH_DisplaySoloist实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回值为0表示执行成功，-1表示执行失败。 |

**OH_DisplaySoloist_SetExpectedFrameRateRange()**

```ets
int32_t OH_DisplaySoloist_SetExpectedFrameRateRange(OH_DisplaySoloist* displaySoloist, DisplaySoloist_ExpectedRateRange* range)
```

描述

设置VSync期望帧率范围。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DisplaySoloist* displaySoloist | 一个指向OH_DisplaySoloist实例的指针。 |
| DisplaySoloist_ExpectedRateRange* range | 一个指向期望帧率范围DisplaySoloist_ExpectedRateRange实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回值为0表示执行成功，-1表示执行失败。 |