# native_vsync.h

#### 概述

定义获取和使用NativeVsync的相关函数。

**引用文件：** <native_vsync/native_vsync.h>

**库：** libnative_vsync.so

**起始版本：** 9

**相关模块：**[NativeVsync](../../topics/misc/NativeVsync.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_NativeVSync_ExpectedRateRange](../../topics/misc/OH_NativeVSync_ExpectedRateRange.md)OH_NativeVSync_ExpectedRateRange期望帧率范围结构体。[OH_NativeVSync](../../topics/misc/OH_NativeVSync.md)OH_NativeVSync提供OH_NativeVSync结构体声明。

#### 函数

名称typedef关键字描述[typedef void (*OH_NativeVSync_FrameCallback)(long long timestamp, void *data)](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_framecallback)OH_NativeVSync_FrameCallbackVSync回调函数类型。[OH_NativeVSync* OH_NativeVSync_Create(const char* name, unsigned int length)](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_create)-

创建一个OH_NativeVSync实例，每次调用都会产生一个新的实例。

本接口需要与[OH_NativeVSync_Destroy](native_vsync.h.md#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_destroy)接口配合使用，否则会存在内存泄露。

[OH_NativeVSync* OH_NativeVSync_Create_ForAssociatedWindow(uint64_t windowID, const char* name, unsigned int length)](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_create_forassociatedwindow)-

创建一个和窗口绑定的OH_NativeVSync实例，每次调用都会产生一个新的实例。

使用本接口创建出来的OH_NativeVSync实例的实际vsync周期与系统vsync周期不完全一致，系统会根据窗口的状态对实际vsync周期进行调整。

[void OH_NativeVSync_Destroy(OH_NativeVSync* nativeVsync)](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_destroy)-

销毁OH_NativeVSync实例。

销毁后的OH_NativeVSync指针不能再继续使用，否则会有野指针问题，尤其需要注意多线程并发时对于OH_NativeVSync指针的管理。

[int OH_NativeVSync_RequestFrame(OH_NativeVSync* nativeVsync, OH_NativeVSync_FrameCallback callback, void* data)](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_requestframe)-

请求下一次vsync信号，当信号到来时，调用回调函数callback。

如果在同一帧内中多次调用此接口，则只会触发最后一个回调。

如果此接口与[OH_NativeVSync_RequestFrameWithMultiCallback](native_vsync.h.md#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_requestframewithmulticallback)接口在同一帧内被调用，则此接口的功能不会生效。

[int OH_NativeVSync_RequestFrameWithMultiCallback(OH_NativeVSync* nativeVsync, OH_NativeVSync_FrameCallback callback, void* data)](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_requestframewithmulticallback)-

请求下一次vsync信号，当信号到来时，调用回调函数callback。

如果在同一帧内中多次调用此接口，每一次传入的callback都会被执行。

[int OH_NativeVSync_GetPeriod(OH_NativeVSync* nativeVsync, long long* period)](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_getperiod)-

获取vsync周期。

vsync周期是在每次使用OH_NativeVSync_RequestFrame接口请求vsync信号后收到OH_NativeVSync_FrameCallback回调的时候才会更新。

首次使用该接口获取vsync周期之前，需要先使用OH_NativeVSync_RequestFrame接口请求vsync信号，在收到OH_NativeVSync_FrameCallback回调之后，才可以通过该接口获取到vsync周期。

[int OH_NativeVSync_DVSyncSwitch(OH_NativeVSync* nativeVsync, bool enable)](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_dvsyncswitch)-

启用DVSync以提高自绘制动画场景的流畅性。

DVSync是Decoupled VSync的缩写，它是一种与硬件VSync解耦的帧时序管理策略。

DVSync通过提前发送带有未来时间戳的VSync信号驱动后续动画帧的提前绘制，这些帧会被帧缓冲队列缓存；DVSync通过缓存的帧减少未来可能发生的丢帧，进而提高动画场景的流畅性。

因为DVSync需要占用空闲的自绘制帧缓冲用于缓存提前绘制的动画帧，用户需要确保至少有一个空闲的帧缓冲区，否则不建议启用此功能。

启用DVSync后，用户需要正确响应提前发送的VSync信号，并在前一个VSync对应的动画帧完成后再请求下一个VSync，且自绘制帧需要携带与VSync一致的时间戳。

在动画结束之后，用户需要关闭DVSync。

在不支持DVSync的平台或者如果有另一个应用程序已经启用了DVSync，则当前的启用操作将不会生效，应用程序仍将收到正常的VSync信号。

[int OH_NativeVSync_SetExpectedFrameRateRange(OH_NativeVSync* nativeVsync, OH_NativeVSync_ExpectedRateRange* range)](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_setexpectedframeraterange)-设置VSync期望帧率以及期望帧率的范围。

#### 函数说明

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

#### OH_NativeVSync_Create()

```ets
OH_NativeVSync* OH_NativeVSync_Create(const char* name, unsigned int length)
```

**描述**

创建一个OH_NativeVSync实例，每次调用都会产生一个新的实例。

本接口需要与[OH_NativeVSync_Destroy](native_vsync.h.md#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_destroy)接口配合使用，否则会存在内存泄露。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 9

**参数：**

参数项描述const char* name表示一个名字，与创建的OH_NativeVSync实例关联。unsigned int lengthname的长度（字符数）。

**返回：**

类型说明[OH_NativeVSync](../../topics/misc/OH_NativeVSync.md)*返回一个指向OH_NativeVSync实例的指针。

#### OH_NativeVSync_Create_ForAssociatedWindow()

```ets
OH_NativeVSync* OH_NativeVSync_Create_ForAssociatedWindow(uint64_t windowID, const char* name, unsigned int length)
```

**描述**

创建一个和窗口绑定的OH_NativeVSync实例，每次调用都会产生一个新的实例。

使用本接口创建出来的OH_NativeVSync实例的实际vsync周期与系统vsync周期不完全一致，系统会根据窗口的状态对实际vsync周期进行调整。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 14

**参数：**

参数项描述uint64_t windowID表示窗口ID，窗口子进程索引标识符，可以通过[OH_NativeWindow_GetSurfaceId](external_window.h.md#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_getsurfaceid)接口获取。const char* name表示一个名称，与创建的OH_NativeVSync实例关联。unsigned int lengthname的长度（字符数）。

**返回：**

类型说明[OH_NativeVSync](../../topics/misc/OH_NativeVSync.md)*返回一个指向OH_NativeVSync实例的指针。

#### OH_NativeVSync_Destroy()

```ets
void OH_NativeVSync_Destroy(OH_NativeVSync* nativeVsync)
```

**描述**

销毁OH_NativeVSync实例。

销毁后的OH_NativeVSync指针不能再继续使用，否则会有野指针问题，尤其需要注意多线程并发时对于OH_NativeVSync指针的管理。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 9

**参数：**

参数项描述[OH_NativeVSync](../../topics/misc/OH_NativeVSync.md)* nativeVsync一个指向OH_NativeVSync实例的指针。

#### OH_NativeVSync_RequestFrame()

```ets
int OH_NativeVSync_RequestFrame(OH_NativeVSync* nativeVsync, OH_NativeVSync_FrameCallback callback, void* data)
```

**描述**

请求下一次vsync信号，当信号到来时，调用回调函数callback。

如果在同一帧内中多次调用此接口，则只会触发最后一个回调。

如果此接口与[OH_NativeVSync_RequestFrameWithMultiCallback](native_vsync.h.md#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_requestframewithmulticallback)接口在同一帧内被调用，则此接口的功能不会生效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 9

**参数：**

参数项描述[OH_NativeVSync](../../topics/misc/OH_NativeVSync.md)* nativeVsync一个指向OH_NativeVSync实例的指针。[OH_NativeVSync_FrameCallback](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_framecallback) callback一个OH_NativeVSync_FrameCallback类型的函数指针，当下一次vsync信号到来时会被调用。void* data一个指向用户自定义数据结构的指针，类型是void。

**返回：**

类型说明int返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeVSync_RequestFrameWithMultiCallback()

```ets
int OH_NativeVSync_RequestFrameWithMultiCallback(OH_NativeVSync* nativeVsync, OH_NativeVSync_FrameCallback callback, void* data)
```

**描述**

请求下一次vsync信号，当信号到来时，调用回调函数callback。

如果在同一帧内中多次调用此接口，每一次传入的callback都会被执行。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 12

**参数：**

参数项描述[OH_NativeVSync](../../topics/misc/OH_NativeVSync.md)* nativeVsync一个指向OH_NativeVSync实例的指针。[OH_NativeVSync_FrameCallback](#ZH-CN_TOPIC_0000002529286009__oh_nativevsync_framecallback) callback一个OH_NativeVSync_FrameCallback类型的函数指针，当下一次vsync信号到来时会被调用。void* data一个指向用户自定义数据结构的指针，类型是void。

**返回：**

类型说明int返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeVSync_GetPeriod()

```ets
int OH_NativeVSync_GetPeriod(OH_NativeVSync* nativeVsync, long long* period)
```

**描述**

获取vsync周期。

vsync周期是在每次使用OH_NativeVSync_RequestFrame接口请求vsync信号后收到OH_NativeVSync_FrameCallback回调的时候才会更新。

首次使用该接口获取vsync周期之前，需要先使用OH_NativeVSync_RequestFrame接口请求vsync信号，在收到OH_NativeVSync_FrameCallback回调之后，才可以通过该接口获取到vsync周期。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 10

**参数：**

参数项描述[OH_NativeVSync](../../topics/misc/OH_NativeVSync.md)* nativeVsync一个指向OH_NativeVSync实例的指针。long long* period表示vsync周期，作为出参使用。

**返回：**

类型说明int返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeVSync_DVSyncSwitch()

```ets
int OH_NativeVSync_DVSyncSwitch(OH_NativeVSync* nativeVsync, bool enable)
```

**描述**

启用DVSync以提高自绘制动画场景的流畅性。

DVSync是Decoupled VSync的缩写，它是一种与硬件VSync解耦的帧时序管理策略。

DVSync通过提前发送带有未来时间戳的VSync信号驱动后续动画帧的提前绘制，这些帧会被帧缓冲队列缓存；DVSync通过缓存的帧减少未来可能发生的丢帧，进而提高动画场景的流畅性。

因为DVSync需要占用空闲的自绘制帧缓冲用于缓存提前绘制的动画帧，用户需要确保至少有一个空闲的帧缓冲区，否则不建议启用此功能。

启用DVSync后，用户需要正确响应提前发送的VSync信号，并在前一个VSync对应的动画帧完成后再请求下一个VSync，且自绘制帧需要携带与VSync一致的时间戳。

在动画结束之后，用户需要关闭DVSync。

在不支持DVSync的平台或者如果有另一个应用程序已经启用了DVSync，则当前的启用操作将不会生效，应用程序仍将收到正常的VSync信号。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 14

**参数：**

参数项描述[OH_NativeVSync](../../topics/misc/OH_NativeVSync.md)* nativeVsync一个指向OH_NativeVSync实例的指针。bool enable表示打开或者关闭DVSync，true表示打开，false表示关闭。

**返回：**

类型说明int返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeVSync_SetExpectedFrameRateRange()

```ets
int OH_NativeVSync_SetExpectedFrameRateRange(OH_NativeVSync* nativeVsync, OH_NativeVSync_ExpectedRateRange* range)
```

**描述**

设置VSync期望帧率及其范围。实际帧率可能因系统功耗、性能和硬件规格等限制而与设置的期望值不一致。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeVsync

**起始版本：** 20

**参数：**

参数项描述[OH_NativeVSync](../../topics/misc/OH_NativeVSync.md)* nativeVsync指向[OH_NativeVSync](../../topics/misc/OH_NativeVSync.md)实例的指针。[OH_NativeVSync_ExpectedRateRange](../../topics/misc/OH_NativeVSync_ExpectedRateRange.md)* range

指向[OH_NativeVSync_ExpectedRateRange](../../topics/misc/OH_NativeVSync_ExpectedRateRange.md)实例的指针。

有效的期望帧率范围为：0 <= 最小值 <= 期望帧率 <= 最大值 <= 144。

期望帧率为0时，表示取消设置期望帧率。

此指针需开发者自行管理生命周期。

**返回：**

类型说明int返回值为0表示成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。