# external_window.h

#### 概述

定义获取和使用NativeWindow的相关函数。

**引用文件：** <native_window/external_window.h>

**库：** libnative_window.so

**起始版本：** 8

**相关模块：**[NativeWindow](NativeWindow.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Region](Region.md)Region表示本地窗口OHNativeWindow需要更新内容的矩形区域（脏区）。[Rect](Rect.md)-如果rects是空指针nullptr，默认Buffer大小为脏区。[OHHDRMetaData](OHHDRMetaData.md)OHHDRMetaDataHDR元数据结构体定义。[OHExtDataHandle](OHExtDataHandle.md)OHExtDataHandle扩展数据句柄结构体定义。[OHIPCParcel](OHIPCParcel.md)OHIPCParcel提供对IPC序列化对象的访问功能。[NativeWindow](NativeWindow.md)OHNativeWindow提供对OHNativeWindow的访问功能。[NativeWindowBuffer](NativeWindowBuffer.md)OHNativeWindowBuffer提供对OHNativeWindowBuffer的访问功能。

#### 枚举

名称typedef关键字描述[NativeWindowOperation](#ZH-CN_TOPIC_0000002497606020__nativewindowoperation)NativeWindowOperationOH_NativeWindow_NativeWindowHandleOpt函数中的操作码。[OHScalingMode](#ZH-CN_TOPIC_0000002497606020__ohscalingmode)OHScalingMode缩放模式Scaling Mode。[OHScalingModeV2](#ZH-CN_TOPIC_0000002497606020__ohscalingmodev2)OHScalingModeV2渲染缩放模式枚举。[OHHDRMetadataKey](#ZH-CN_TOPIC_0000002497606020__ohhdrmetadatakey)OHHDRMetadataKey枚举HDR元数据关键字。[OHSurfaceSource](#ZH-CN_TOPIC_0000002497606020__ohsurfacesource)OHSurfaceSource本地窗口内容来源类型枚举。

#### 函数

名称描述[OHNativeWindow* OH_NativeWindow_CreateNativeWindow(void* pSurface)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_createnativewindow)

创建OHNativeWindow实例，每次调用都会产生一个新的OHNativeWindow实例。

说明：此接口不可用，可通过OH_NativeImage_AcquireNativeWindow创建，或通过XComponent创建。

[void OH_NativeWindow_DestroyNativeWindow(OHNativeWindow* window)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_destroynativewindow)

将OHNativeWindow对象的引用计数减1，当引用计数为0的时候，该OHNativeWindow对象会被析构掉。

本接口为非线程安全类型接口。

[OHNativeWindowBuffer* OH_NativeWindow_CreateNativeWindowBufferFromSurfaceBuffer(void* pSurfaceBuffer)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_createnativewindowbufferfromsurfacebuffer)

创建OHNativeWindowBuffer实例，每次调用都会产生一个新的OHNativeWindowBuffer实例。

说明：此接口不可用，使用OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer替代。

[OHNativeWindowBuffer* OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer(OH_NativeBuffer* nativeBuffer)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_createnativewindowbufferfromnativebuffer)

创建OHNativeWindowBuffer实例，每次调用都会产生一个新的OHNativeWindowBuffer实例。

本接口需要与[OH_NativeWindow_DestroyNativeWindowBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_destroynativewindowbuffer)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

[void OH_NativeWindow_DestroyNativeWindowBuffer(OHNativeWindowBuffer* buffer)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_destroynativewindowbuffer)

将OHNativeWindowBuffer对象的引用计数减1，当引用计数为0的时候，该OHNativeWindowBuffer对象会被析构掉。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_NativeWindowRequestBuffer(OHNativeWindow *window,OHNativeWindowBuffer **buffer, int *fenceFd)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowrequestbuffer)

通过OHNativeWindow对象申请一块OHNativeWindowBuffer，用以内容生产。

在调用本接口前，需要通过[SET_BUFFER_GEOMETRY](#ZH-CN_TOPIC_0000002497606020__nativewindowoperation)对OHNativeWindow设置宽高。

本接口需要与[OH_NativeWindow_NativeWindowFlushBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowflushbuffer)接口配合使用，否则内存会耗尽。

当fenceFd使用完，用户需要将其close。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_NativeWindowFlushBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer,int fenceFd, Region region)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowflushbuffer)

通过OHNativeWindow将生产好内容的OHNativeWindowBuffer放回到Buffer队列中，用以内容消费。

系统会将fenceFd关闭，无需用户close。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_GetLastFlushedBuffer(OHNativeWindow *window, OHNativeWindowBuffer **buffer,int *fenceFd, float matrix[16])](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_getlastflushedbuffer)从OHNativeWindow获取上次送回到buffer队列中的OHNativeWindowBuffer。[int32_t OH_NativeWindow_NativeWindowAbortBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowabortbuffer)

通过OHNativeWindow将之前申请出来的OHNativeWindowBuffer返还到Buffer队列中，供下次再申请。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_NativeWindowHandleOpt(OHNativeWindow *window, int code, ...)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowhandleopt)

设置/获取OHNativeWindow的属性，包括设置/获取宽高、内容格式等。

本接口为非线程安全类型接口。

[BufferHandle *OH_NativeWindow_GetBufferHandleFromNative(OHNativeWindowBuffer *buffer)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_getbufferhandlefromnative)

通过OHNativeWindowBuffer获取该buffer的BufferHandle指针。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_NativeObjectReference(void *obj)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectreference)

增加一个NativeObject的引用计数。

本接口需要与[OH_NativeWindow_NativeObjectUnreference](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectunreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_NativeObjectUnreference(void *obj)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectunreference)

减少一个NativeObject的引用计数，当引用计数减少为0时，该NativeObject将被析构掉。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_GetNativeObjectMagic(void *obj)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_getnativeobjectmagic)

获取NativeObject的MagicId。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_NativeWindowSetScalingMode(OHNativeWindow *window, uint32_t sequence,OHScalingMode scalingMode)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowsetscalingmode)设置OHNativeWindow的ScalingMode。[int32_t OH_NativeWindow_NativeWindowSetMetaData(OHNativeWindow *window, uint32_t sequence, int32_t size,const OHHDRMetaData *metaData)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowsetmetadata)设置OHNativeWindow的元数据。[int32_t OH_NativeWindow_NativeWindowSetMetaDataSet(OHNativeWindow *window, uint32_t sequence, OHHDRMetadataKey key,int32_t size, const uint8_t *metaData)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowsetmetadataset)设置OHNativeWindow的元数据集。[int32_t OH_NativeWindow_NativeWindowSetTunnelHandle(OHNativeWindow *window, const OHExtDataHandle *handle)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowsettunnelhandle)设置OHNativeWindow的TunnelHandle。[int32_t OH_NativeWindow_NativeWindowAttachBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowattachbuffer)

将OHNativeWindowBuffer添加进OHNativeWindow中。

本接口需要与[OH_NativeWindow_NativeWindowDetachBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowdetachbuffer)接口配合使用，否则会存在内存管理混乱问题。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_NativeWindowDetachBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowdetachbuffer)

将OHNativeWindowBuffer从OHNativeWindow中分离。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_GetSurfaceId(OHNativeWindow *window, uint64_t *surfaceId)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_getsurfaceid)

通过OHNativeWindow获取对应的surfaceId。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_CreateNativeWindowFromSurfaceId(uint64_t surfaceId, OHNativeWindow **window)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_createnativewindowfromsurfaceid)

通过surfaceId创建对应的OHNativeWindow。

本接口需要与[OH_NativeWindow_DestroyNativeWindow](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_destroynativewindow)接口配合使用，否则会存在内存泄露。

如果存在并发释放OHNativeWindow的情况，需要通过[OH_NativeWindow_NativeObjectReference](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectreference)和[OH_NativeWindow_NativeObjectUnreference](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectunreference)对OHNativeWindow进行引用计数加一和减一。

通过surfaceId获取的surface需要是在本进程中创建的，不能跨进程获取surface。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_NativeWindowSetScalingModeV2(OHNativeWindow* window, OHScalingModeV2 scalingMode)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowsetscalingmodev2)

设置OHNativeWindow的渲染缩放模式。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_GetLastFlushedBufferV2(OHNativeWindow *window, OHNativeWindowBuffer **buffer,int *fenceFd, float matrix[16])](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_getlastflushedbufferv2)

从OHNativeWindow获取上次送回到buffer队列中的OHNativeWindowBuffer,与OH_NativeWindow_GetLastFlushedBuffer的差异在于matrix不同。

本接口需要与[OH_NativeWindow_NativeObjectUnreference](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectunreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

[void OH_NativeWindow_SetBufferHold(OHNativeWindow *window)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_setbufferhold)启用单帧缓存机制，通过提前缓存一帧buffer并延迟显示，用于平滑帧率波动。[int32_t OH_NativeWindow_WriteToParcel(OHNativeWindow *window, OHIPCParcel *parcel)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_writetoparcel)

将窗口对象写入IPC序列化对象中。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_ReadFromParcel(OHIPCParcel *parcel, OHNativeWindow **window)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_readfromparcel)

从IPC序列化对象中读取窗口对象。

本接口将会创建一个OHNativeWindow，当窗口对象使用完，开发者需要与[OH_NativeWindow_DestroyNativeWindow](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_destroynativewindow)接口配合使用，否则会存在内存泄漏。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_SetColorSpace(OHNativeWindow *window, OH_NativeBuffer_ColorSpace colorSpace)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_setcolorspace)

为OHNativeWindow设置颜色空间属性。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_GetColorSpace(OHNativeWindow *window, OH_NativeBuffer_ColorSpace *colorSpace)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_getcolorspace)

获取OHNativeWindow颜色空间属性。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_SetMetadataValue(OHNativeWindow *window, OH_NativeBuffer_MetadataKey metadataKey,int32_t size, uint8_t *metadata)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_setmetadatavalue)

为OHNativeWindow设置元数据属性值。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_GetMetadataValue(OHNativeWindow *window, OH_NativeBuffer_MetadataKey metadataKey,int32_t *size, uint8_t **metadata)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_getmetadatavalue)

获取OHNativeWindow元数据属性值。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_CleanCache(OHNativeWindow *window)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_cleancache)

清理OHNativeWindow中的OHNativeWindowBuffer缓存。

使用该接口清理缓存前，需确保已通过[OH_NativeWindow_NativeWindowRequestBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowrequestbuffer)接口成功申请OHNativeWindowBuffer。

本接口为非线程安全类型接口。

[int32_t OH_NativeWindow_PreAllocBuffers(OHNativeWindow *window, uint32_t allocBufferCnt)](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_preallocbuffers)

通过OHNativeWindow对象提前申请多块OHNativeWindowBuffer，用以内容生产。

在调用本接口前，需要通过[OH_NativeWindow_NativeWindowHandleOpt](external_window.h.md#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowhandleopt)对OHNativeWindow设置宽高。

本接口为非线程安全类型接口。

#### 枚举类型说明

#### NativeWindowOperation

```ets
enum NativeWindowOperation
```

**描述**

OH_NativeWindow_NativeWindowHandleOpt函数中的操作码。

**起始版本：** 8

枚举项描述SET_BUFFER_GEOMETRY设置本地窗口缓冲区几何图形，函数中的可变参数是[输入] int32_t width，[输入] int32_t height。GET_BUFFER_GEOMETRY获取本地窗口缓冲区几何图形，函数中的可变参数是[输出] int32_t height，[输出] int32_t width。GET_FORMAT获取本地窗口缓冲区格式，函数中的可变参数是[输出] int32_tformat，取值具体可见[OH_NativeBuffer_Format](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_format)枚举值。SET_FORMAT设置本地窗口缓冲区格式，函数中的可变参数是[输入] int32_t format，取值具体可见[OH_NativeBuffer_Format](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_format)枚举值。GET_USAGE获取本地窗口读写方式，函数中的可变参数是[输出] uint64_tusage，取值具体可见[OH_NativeBuffer_Usage](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_usage)枚举值。SET_USAGE设置本地窗口缓冲区读写方式，函数中的可变参数是[输入] uint64_t usage，取值具体可见[OH_NativeBuffer_Usage](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_usage)枚举值。SET_STRIDE

设置本地窗口缓冲区步幅，函数中的可变参数是[输入] int32_t stride。

**废弃版本：** 16

GET_STRIDE

获取本地窗口缓冲区步幅，函数中的可变参数是[输出] int32_t *stride。

**废弃版本：** 16

**替代方案：** 使用[OH_NativeWindow_GetBufferHandleFromNative](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_getbufferhandlefromnative)接口获取BufferHandle实例，从[BufferHandle](zh-cn_topic_0000002529286029.html)实例中获取stride值。

SET_SWAP_INTERVAL设置本地窗口缓冲区交换间隔，函数中的可变参数是[输入] int32_t interval。GET_SWAP_INTERVAL获取本地窗口缓冲区交换间隔，函数中的可变参数是[输出] int32_tinterval。SET_TIMEOUT设置请求本地窗口请求缓冲区的超时等待时间，未手动设置时默认值为3000毫秒，函数中的可变参数是[输入] int32_t timeout, 单位为毫秒。GET_TIMEOUT获取请求本地窗口请求缓冲区的超时等待时间，未手动设置时默认值为3000毫秒，函数中的可变参数是[输出] int32_t timeout，单位为毫秒。SET_COLOR_GAMUT设置本地窗口缓冲区色彩空间，函数中的可变参数是[输入] int32_t colorGamut，取值具体可见[OH_NativeBuffer_ColorGamut](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_colorgamut)枚举值。GET_COLOR_GAMUT获取本地窗口缓冲区色彩空间，函数中的可变参数是[输出] int32_tcolorGamut，取值具体可见[OH_NativeBuffer_ColorGamut](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_colorgamut)枚举值。SET_TRANSFORM设置本地窗口缓冲区变换，函数中的可变参数是[输入] int32_t transform，取值具体可见[OH_NativeBuffer_TransformType](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_transformtype)枚举值。GET_TRANSFORM获取本地窗口缓冲区变换，函数中的可变参数是[输出] int32_t transform，取值具体可见[OH_NativeBuffer_TransformType](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_transformtype)枚举值。SET_UI_TIMESTAMP设置本地窗口缓冲区UI时间戳，函数中的可变参数是[输入] uint64_t uiTimestamp。GET_BUFFERQUEUE_SIZE

获取内存队列大小，函数中的可变参数是[输出] int32_t *size。

**起始版本：** 12

SET_SOURCE_TYPE

设置本地窗口内容来源，函数中的可变参数是[输入] int32_t sourceType，取值具体可见[OHSurfaceSource](#ZH-CN_TOPIC_0000002497606020__ohsurfacesource)枚举值。

**起始版本：** 12

GET_SOURCE_TYPE

获取本地窗口内容来源，函数中的可变参数是[输出] int32_t *sourceType，取值具体可见[OHSurfaceSource](#ZH-CN_TOPIC_0000002497606020__ohsurfacesource)枚举值。

**起始版本：** 12

SET_APP_FRAMEWORK_TYPE

设置本地窗口应用框架名称，函数中的可变参数是[输入] char* frameworkType，最大支持64字节。

**起始版本：** 12

GET_APP_FRAMEWORK_TYPE

获取本地窗口应用框架名称，函数中的可变参数是[输出] char* frameworkType。

**起始版本：** 12

SET_HDR_WHITE_POINT_BRIGHTNESS

设置HDR白点亮度，函数中的可变参数是[输入] float brightness。取值范围为[0.0f, 1.0f]。

**起始版本：** 12

SET_SDR_WHITE_POINT_BRIGHTNESS

设置SDR白点亮度，函数中的可变参数是[输入] float brightness。取值范围为[0.0f, 1.0f]。

**起始版本：** 12

SET_DESIRED_PRESENT_TIMESTAMP = 24

设置本地窗口缓冲区期望上屏时间的时间戳。

 当且仅当RenderService为本地窗口的消费者时，该时间戳生效

本操作执行后需要配合调用[OH_NativeWindow_NativeWindowFlushBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowflushbuffer)生效。

生产者下一次放入队列的buffer，达到该期望上屏时间后，才会被RenderService消费并上屏。

如果buffer队列中存在多个生产者放入的buffer，都设置了desiredPresentTimestamp并已达到期望上屏时间，则较早入队的buffer将被消费者丢弃回队列。

如果期望上屏时间大于消费者提供的时间 1 秒以上，则该期望上屏时间戳将被忽略。

 函数中的可变参数是[输入] int64_t desiredPresentTimestamp，取值范围大于0，应由std::chrono::steady_clock标准库时钟生成，且单位为纳秒。

**起始版本：** 13

#### OHScalingMode

```ets
enum OHScalingMode
```

**描述**

缩放模式Scaling Mode。

**起始版本：** 9

**废弃版本：** 10

**替代接口：**[OHScalingModeV2](#ZH-CN_TOPIC_0000002497606020__ohscalingmodev2)

枚举项描述OH_SCALING_MODE_FREEZE = 0在接收到窗口大小的缓冲区之前，不可以更新窗口内容。OH_SCALING_MODE_SCALE_TO_WINDOW缓冲区在二维中缩放以匹配窗口大小。OH_SCALING_MODE_SCALE_CROP缓冲区被统一缩放，使得缓冲区的较小尺寸与窗口大小匹配。OH_SCALING_MODE_NO_SCALE_CROP窗口被裁剪为缓冲区裁剪矩形的大小，裁剪矩形之外的像素被视为完全透明。

#### OHScalingModeV2

```ets
enum OHScalingModeV2
```

**描述**

渲染缩放模式枚举。

**起始版本：** 12

枚举项描述OH_SCALING_MODE_FREEZE_V2 = 0冻结窗口，在接收到和窗口大小相等的缓冲区之前，窗口内容不进行更新。OH_SCALING_MODE_SCALE_TO_WINDOW_V2缓冲区进行拉伸缩放以匹配窗口大小。OH_SCALING_MODE_SCALE_CROP_V2缓冲区按原比例缩放，使得缓冲区的较小边与窗口匹配，较长边超出窗口部分被视为透明。OH_SCALING_MODE_NO_SCALE_CROP_V2按窗口大小将缓冲区裁剪，裁剪矩形之外的像素被视为完全透明。OH_SCALING_MODE_SCALE_FIT_V2

缓冲区按原比例缩放。优先显示所有缓冲区内容。如果比例与窗口比例不同，用背景颜色填充窗口的未填充区域。

模拟器不支持该模式。

#### OHHDRMetadataKey

```ets
enum OHHDRMetadataKey
```

**描述**

枚举HDR元数据关键字。

**起始版本：** 9

**废弃版本：** 10

枚举项描述OH_METAKEY_RED_PRIMARY_X = 0红基色X坐标。OH_METAKEY_RED_PRIMARY_Y = 1,红基色Y坐标。OH_METAKEY_GREEN_PRIMARY_X = 2,绿基色X坐标。OH_METAKEY_GREEN_PRIMARY_Y = 3,绿基色Y坐标。OH_METAKEY_BLUE_PRIMARY_X = 4,蓝基色X坐标。OH_METAKEY_BLUE_PRIMARY_Y = 5,蓝基色Y坐标。OH_METAKEY_WHITE_PRIMARY_X = 6,白点X坐标。OH_METAKEY_WHITE_PRIMARY_Y = 7,白点Y坐标。OH_METAKEY_MAX_LUMINANCE = 8,最大的光亮度。OH_METAKEY_MIN_LUMINANCE = 9,最小的光亮度。OH_METAKEY_MAX_CONTENT_LIGHT_LEVEL = 10,最大的内容亮度水平。OH_METAKEY_MAX_FRAME_AVERAGE_LIGHT_LEVEL = 11,最大的帧平均亮度水平。OH_METAKEY_HDR10_PLUS = 12,HDR10 Plus。OH_METAKEY_HDR_VIVID = 13,Vivid。

#### OHSurfaceSource

```ets
enum OHSurfaceSource
```

**描述**

本地窗口内容来源类型枚举。

**起始版本：** 12

枚举项描述OH_SURFACE_SOURCE_DEFAULT = 0窗口内容默认来源。OH_SURFACE_SOURCE_UI窗口内容来自于UI。OH_SURFACE_SOURCE_GAME窗口内容来自于游戏。OH_SURFACE_SOURCE_CAMERA窗口内容来自于相机。OH_SURFACE_SOURCE_VIDEO窗口内容来自于视频。

#### 函数说明

#### OH_NativeWindow_CreateNativeWindow()

```ets
OHNativeWindow* OH_NativeWindow_CreateNativeWindow(void* pSurface)
```

**描述**

创建OHNativeWindow实例，每次调用都会产生一个新的OHNativeWindow实例。

说明：此接口不可用，可通过[OH_NativeImage_AcquireNativeWindow](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_acquirenativewindow)创建，或通过XComponent创建。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**废弃版本：** 从API version 12开始废弃，不再提供替代接口。

**参数：**

参数项描述void* pSurface一个指向生产者ProduceSurface的指针，类型为sptr<OHOS::Surface>。

**返回：**

类型说明[OHNativeWindow](NativeWindow.md)*返回一个指针，指向OHNativeWindow的结构体实例。

#### OH_NativeWindow_DestroyNativeWindow()

```ets
void OH_NativeWindow_DestroyNativeWindow(OHNativeWindow* window)
```

**描述**

将OHNativeWindow对象的引用计数减1，当引用计数为0的时候，该OHNativeWindow对象会被析构掉。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md)* window一个OHNativeWindow的结构体实例的指针。

#### OH_NativeWindow_CreateNativeWindowBufferFromSurfaceBuffer()

```ets
OHNativeWindowBuffer* OH_NativeWindow_CreateNativeWindowBufferFromSurfaceBuffer(void* pSurfaceBuffer)
```

**描述**

创建OHNativeWindowBuffer实例，每次调用都会产生一个新的OHNativeWindowBuffer实例。

说明：此接口不可用，使用[OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_createnativewindowbufferfromnativebuffer)替代。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**废弃版本：** 12

**替代接口：**[OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_createnativewindowbufferfromnativebuffer)

**参数：**

参数项描述void* pSurfaceBuffer一个指向生产者buffer的指针，类型为sptr[OHOS::SurfaceBuffer](OHOS::SurfaceBuffer)。

**返回：**

类型说明OHNativeWindowBuffer*返回一个指针，指向OHNativeWindowBuffer的结构体实例。

#### OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer()

```ets
OHNativeWindowBuffer* OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer(OH_NativeBuffer* nativeBuffer)
```

**描述**

创建OHNativeWindowBuffer实例，每次调用都会产生一个新的OHNativeWindowBuffer实例。

本接口需要与[OH_NativeWindow_DestroyNativeWindowBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_destroynativewindowbuffer)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 11

**参数：**

参数项描述OH_NativeBuffer* nativeBuffer一个指向OH_NativeBuffer的指针。

**返回：**

类型说明OHNativeWindowBuffer*返回一个指针，指向OHNativeWindowBuffer的结构体实例。

#### OH_NativeWindow_DestroyNativeWindowBuffer()

```ets
void OH_NativeWindow_DestroyNativeWindowBuffer(OHNativeWindowBuffer* buffer)
```

**描述**

将OHNativeWindowBuffer对象的引用计数减1，当引用计数为0的时候，该OHNativeWindowBuffer对象会被析构掉。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

参数项描述[OHNativeWindowBuffer](NativeWindowBuffer.md)* buffer一个OHNativeWindowBuffer的结构体实例的指针。

#### OH_NativeWindow_NativeWindowRequestBuffer()

```ets
int32_t OH_NativeWindow_NativeWindowRequestBuffer(OHNativeWindow *window,OHNativeWindowBuffer **buffer, int *fenceFd)
```

**描述**

通过OHNativeWindow对象申请一块OHNativeWindowBuffer，用以内容生产。

在调用本接口前，需要通过[SET_BUFFER_GEOMETRY](#ZH-CN_TOPIC_0000002497606020__nativewindowoperation)对OHNativeWindow设置宽高。

本接口需要与[OH_NativeWindow_NativeWindowFlushBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowflushbuffer)接口配合使用，否则内存会耗尽。

当fenceFd使用完，用户需要将其close。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。[OHNativeWindowBuffer](NativeWindowBuffer.md) **buffer

一个指向OHNativeWindowBuffer指针的指针（二级指针）。

通过OH_NativeWindow_GetBufferHandleFromNative可获取BufferHandle结构体，访问缓冲区内存。

int *fenceFd

一个文件描述符句柄，用于GPU/CPU同步：不同取值及含义如下：

- 返回≥0：缓冲区正被GPU使用，需要等待文件描述符fenceFd就绪。

- 返回-1：缓冲区可直接使用。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_NativeWindowFlushBuffer()

```ets
int32_t OH_NativeWindow_NativeWindowFlushBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer,int fenceFd, Region region)
```

**描述**

通过OHNativeWindow将生产好内容的OHNativeWindowBuffer放回到Buffer队列中，用以内容消费。

系统会将fenceFd关闭，无需用户close。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。[OHNativeWindowBuffer](NativeWindowBuffer.md) *buffer一个OHNativeWindowBuffer的结构体实例的指针。int fenceFd

一个文件描述符句柄，用以同步时序。不同取值及含义如下：

- -1：CPU渲染完成，无需同步时序。

- ≥0：从GPU同步对象转换（如EGL的eglDupNativeFenceFDANDROID），对端需要通过此fenceFd同步时序。

[Region](Region.md) region一个Region结构体，表示一块脏区域，该区域有内容更新。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_GetLastFlushedBuffer()

```ets
int32_t OH_NativeWindow_GetLastFlushedBuffer(OHNativeWindow *window, OHNativeWindowBuffer **buffer,int *fenceFd, float matrix[16])
```

**描述**

从OHNativeWindow获取上次送回到buffer队列中的OHNativeWindowBuffer。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 11

**废弃版本：** 从API version 12开始废弃。

**替代接口：**[OH_NativeWindow_GetLastFlushedBufferV2](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_getlastflushedbufferv2)

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。[OHNativeWindowBuffer](NativeWindowBuffer.md) **buffer一个OHNativeWindowBuffer结构体指针的指针。int *fenceFd一个文件描述符的指针。matrix表示检索到的44变换矩阵。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_NativeWindowAbortBuffer()

```ets
int32_t OH_NativeWindow_NativeWindowAbortBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer)
```

**描述**

通过OHNativeWindow将之前申请出来的OHNativeWindowBuffer返还到Buffer队列中，供下次再申请。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。[OHNativeWindowBuffer](NativeWindowBuffer.md) *buffer一个OHNativeWindowBuffer的结构体实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_NativeWindowHandleOpt()

```ets
int32_t OH_NativeWindow_NativeWindowHandleOpt(OHNativeWindow *window, int code, ...)
```

**描述**

设置/获取OHNativeWindow的属性，包括设置/获取宽高、内容格式等。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。int code表示操作码，详见[NativeWindowOperation](#ZH-CN_TOPIC_0000002497606020__nativewindowoperation)。...可变参数，必须与操作码对应的数据类型保持一致，且入参数量严格按照操作码提示传入，否则会存在未定义行为。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_GetBufferHandleFromNative()

```ets
BufferHandle *OH_NativeWindow_GetBufferHandleFromNative(OHNativeWindowBuffer *buffer)
```

**描述**

通过OHNativeWindowBuffer获取该buffer的BufferHandle指针。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

参数项描述[OHNativeWindowBuffer](NativeWindowBuffer.md) *buffer一个OHNativeWindowBuffer的结构体实例的指针。

**返回：**

类型说明[BufferHandle](BufferHandle.md)BufferHandle 返回一个指针，指向[BufferHandle](BufferHandle.md)的结构体实例。

#### OH_NativeWindow_NativeObjectReference()

```ets
int32_t OH_NativeWindow_NativeObjectReference(void *obj)
```

**描述**

增加一个NativeObject的引用计数。

本接口需要与[OH_NativeWindow_NativeObjectUnreference](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectunreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

参数项描述void *obj一个OHNativeWindow或者OHNativeWindowBuffer的结构体实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_NativeObjectUnreference()

```ets
int32_t OH_NativeWindow_NativeObjectUnreference(void *obj)
```

**描述**

减少一个NativeObject的引用计数，当引用计数减少为0时，该NativeObject将被析构掉。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

参数项描述void *obj一个OHNativeWindow或者OHNativeWindowBuffer的结构体实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_GetNativeObjectMagic()

```ets
int32_t OH_NativeWindow_GetNativeObjectMagic(void *obj)
```

**描述**

获取NativeObject的MagicId。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 8

**参数：**

参数项描述void *obj一个OHNativeWindow或者OHNativeWindowBuffer的结构体实例的指针。

**返回：**

类型说明int32_tMagicId 返回值为魔鬼数字，每个NativeObject唯一。

#### OH_NativeWindow_NativeWindowSetScalingMode()

```ets
int32_t OH_NativeWindow_NativeWindowSetScalingMode(OHNativeWindow *window, uint32_t sequence,OHScalingMode scalingMode)
```

**描述**

设置OHNativeWindow的ScalingMode。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃。

**替代接口：**[OH_NativeWindow_NativeWindowSetScalingModeV2](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowsetscalingmodev2)

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。uint32_t sequence生产缓冲区的序列。[OHScalingMode](#ZH-CN_TOPIC_0000002497606020__ohscalingmode) scalingMode枚举值OHScalingMode。

**返回：**

类型说明int32_t返回值为0表示执行成功。

#### OH_NativeWindow_NativeWindowSetMetaData()

```ets
int32_t OH_NativeWindow_NativeWindowSetMetaData(OHNativeWindow *window, uint32_t sequence, int32_t size,const OHHDRMetaData *metaData)
```

**描述**

设置OHNativeWindow的元数据。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃，不再提供替代接口。

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。uint32_t sequence生产缓冲区的序列。int32_t sizeOHHDRMetaData数组的大小。metaData指向OHHDRMetaData数组的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功。

#### OH_NativeWindow_NativeWindowSetMetaDataSet()

```ets
int32_t OH_NativeWindow_NativeWindowSetMetaDataSet(OHNativeWindow *window, uint32_t sequence, OHHDRMetadataKey key,int32_t size, const uint8_t *metaData)
```

**描述**

设置OHNativeWindow的元数据集。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃，不再提供替代接口。

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。uint32_t sequence生产缓冲区的序列。[OHHDRMetadataKey](#ZH-CN_TOPIC_0000002497606020__ohhdrmetadatakey) key枚举值OHHDRMetadataKey。int32_t sizeuint8_t向量的大小。metaDate指向uint8_t向量的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功。

#### OH_NativeWindow_NativeWindowSetTunnelHandle()

```ets
int32_t OH_NativeWindow_NativeWindowSetTunnelHandle(OHNativeWindow *window, const OHExtDataHandle *handle)
```

**描述**

设置OHNativeWindow的TunnelHandle。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 9

**废弃版本：** 从API version 10开始废弃，不再提供替代接口。

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。const [OHExtDataHandle](OHExtDataHandle.md) *handle指向OHExtDataHandle的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功。

#### OH_NativeWindow_NativeWindowAttachBuffer()

```ets
int32_t OH_NativeWindow_NativeWindowAttachBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer)
```

**描述**

将OHNativeWindowBuffer添加进OHNativeWindow中。

本接口需要与[OH_NativeWindow_NativeWindowDetachBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowdetachbuffer)接口配合使用，否则会存在内存管理混乱问题。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。[OHNativeWindowBuffer](NativeWindowBuffer.md) *buffer一个OHNativeWindowBuffer的结构体实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_NativeWindowDetachBuffer()

```ets
int32_t OH_NativeWindow_NativeWindowDetachBuffer(OHNativeWindow *window, OHNativeWindowBuffer *buffer)
```

**描述**

将OHNativeWindowBuffer从OHNativeWindow中分离。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。[OHNativeWindowBuffer](NativeWindowBuffer.md) *buffer一个OHNativeWindowBuffer的结构体实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_GetSurfaceId()

```ets
int32_t OH_NativeWindow_GetSurfaceId(OHNativeWindow *window, uint64_t *surfaceId)
```

**描述**

通过OHNativeWindow获取对应的surfaceId。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。uint64_t *surfaceId一个surface对应ID的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_CreateNativeWindowFromSurfaceId()

```ets
int32_t OH_NativeWindow_CreateNativeWindowFromSurfaceId(uint64_t surfaceId, OHNativeWindow **window)
```

**描述**

通过surfaceId创建对应的OHNativeWindow。

本接口需要与[OH_NativeWindow_DestroyNativeWindow](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_destroynativewindow)接口配合使用，否则会存在内存泄露。

如果存在并发释放OHNativeWindow的情况，需要通过[OH_NativeWindow_NativeObjectReference](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectreference)和[OH_NativeWindow_NativeObjectUnreference](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectunreference)对OHNativeWindow进行引用计数加一和减一。

通过surfaceId获取的surface需要是在本进程中创建的，不能跨进程获取surface。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述uint64_t surfaceId一个surface对应的ID。[OHNativeWindow](NativeWindow.md) **window一个OHNativeWindow的结构体实例的二级指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_NativeWindowSetScalingModeV2()

```ets
int32_t OH_NativeWindow_NativeWindowSetScalingModeV2(OHNativeWindow* window, OHScalingModeV2 scalingMode)
```

**描述**

设置OHNativeWindow的渲染缩放模式。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md)* window一个OHNativeWindow的结构体实例的指针。[OHScalingModeV2](#ZH-CN_TOPIC_0000002497606020__ohscalingmodev2) scalingMode一个OHScalingModeV2类型的枚举值。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_GetLastFlushedBufferV2()

```ets
int32_t OH_NativeWindow_GetLastFlushedBufferV2(OHNativeWindow *window, OHNativeWindowBuffer **buffer,int *fenceFd, float matrix[16])
```

**描述**

从OHNativeWindow获取上次送回到buffer队列中的OHNativeWindowBuffer,与OH_NativeWindow_GetLastFlushedBuffer的差异在于matrix不同。

本接口需要与[OH_NativeWindow_NativeObjectUnreference](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectunreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个OHNativeWindow的结构体实例的指针。[OHNativeWindowBuffer](NativeWindowBuffer.md) **buffer一个OHNativeWindowBuffer结构体指针的指针。int *fenceFd一个文件描述符的指针。matrix表示检索到的44变换矩阵。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_SetBufferHold()

```ets
void OH_NativeWindow_SetBufferHold(OHNativeWindow *window)
```

**描述**

启用单帧缓存机制，通过提前缓存一帧buffer并延迟显示，用于平滑帧率波动。

启用后，系统会预留一帧buffer作为缓冲，该帧会延迟一个显示周期才上屏。当后续渲染出现超长帧或帧间不均匀时，可使用该缓存帧填补空白，减少画面卡顿。

建议在预知即将出现渲染高峰前提前调用，以建立缓冲保护；缓存仅生效一次，被消费后自动失效，如需持续保护需重新调用本接口。

适用于游戏、动画、复杂UI渲染等对帧率稳定性要求较高的场景，但会引入一帧显示延迟（比如，在60hz的刷新率下，会延迟16.6ms上屏显示），不建议在高交互实时场景中使用。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个[OHNativeWindow](NativeWindow.md)的结构体实例的指针。

#### OH_NativeWindow_WriteToParcel()

```ets
int32_t OH_NativeWindow_WriteToParcel(OHNativeWindow *window, OHIPCParcel *parcel)
```

**描述**

将窗口对象写入IPC序列化对象中。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个指向[OHNativeWindow](NativeWindow.md)的结构体实例的指针。[OHIPCParcel](OHIPCParcel.md) *parcel一个指向[OHIPCParcel](OHIPCParcel.md)的结构体实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_ReadFromParcel()

```ets
int32_t OH_NativeWindow_ReadFromParcel(OHIPCParcel *parcel, OHNativeWindow **window)
```

**描述**

从IPC序列化对象中读取窗口对象。

本接口将会创建一个OHNativeWindow，当窗口对象使用完，开发者需要与[OH_NativeWindow_DestroyNativeWindow](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_destroynativewindow)接口配合使用，否则会存在内存泄漏。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHIPCParcel](OHIPCParcel.md) *parcel一个指向[OHIPCParcel](OHIPCParcel.md)的结构体实例的指针。[OHNativeWindow](NativeWindow.md) **window一个指向[OHNativeWindow](NativeWindow.md)的结构体实例的二级指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_SetColorSpace()

```ets
int32_t OH_NativeWindow_SetColorSpace(OHNativeWindow *window, OH_NativeBuffer_ColorSpace colorSpace)
```

**描述**

为OHNativeWindow设置颜色空间属性。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个指向[OHNativeWindow](NativeWindow.md)的结构体实例的指针。[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace) colorSpace为OHNativeWindow设置的颜色空间，其值从[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace)获取。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_GetColorSpace()

```ets
int32_t OH_NativeWindow_GetColorSpace(OHNativeWindow *window, OH_NativeBuffer_ColorSpace *colorSpace)
```

**描述**

获取OHNativeWindow颜色空间属性。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个指向[OHNativeWindow](NativeWindow.md)的结构体实例的指针。[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace) *colorSpace为OHNativeWindow设置的颜色空间，其值从[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace)获取。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_SetMetadataValue()

```ets
int32_t OH_NativeWindow_SetMetadataValue(OHNativeWindow *window, OH_NativeBuffer_MetadataKey metadataKey,int32_t size, uint8_t *metadata)
```

**描述**

为OHNativeWindow设置元数据属性值。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个指向[OHNativeWindow](NativeWindow.md)的结构体实例的指针。[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey) metadataKeyWindow的元数据类型，其值从[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey)获取。int32_t sizeuint8_t向量的大小，其取值范围见[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey)。metaDate指向uint8_t向量的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_GetMetadataValue()

```ets
int32_t OH_NativeWindow_GetMetadataValue(OHNativeWindow *window, OH_NativeBuffer_MetadataKey metadataKey,int32_t *size, uint8_t **metadata)
```

**描述**

获取OHNativeWindow元数据属性值。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个指向[OHNativeWindow](NativeWindow.md)的结构体实例的指针。[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey) metadataKeyWindow的元数据类型，其值从[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey)获取。int32_t *sizeuint8_t向量的大小，其取值范围见[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey)。metaDate指向uint8_t向量的二级指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_CleanCache()

```ets
int32_t OH_NativeWindow_CleanCache(OHNativeWindow *window)
```

**描述**

清理OHNativeWindow中的OHNativeWindowBuffer缓存。

使用该接口清理缓存前，需确保已通过[OH_NativeWindow_NativeWindowRequestBuffer](#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowrequestbuffer)接口成功申请OHNativeWindowBuffer。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 19

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个指向[OHNativeWindow](NativeWindow.md)的结构体实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeWindow_PreAllocBuffers()

```ets
int32_t OH_NativeWindow_PreAllocBuffers(OHNativeWindow *window, uint32_t allocBufferCnt)
```

**描述**

通过OHNativeWindow对象提前申请多块OHNativeWindowBuffer，用以内容生产。

在调用本接口前，需要通过[OH_NativeWindow_NativeWindowHandleOpt](external_window.h.md#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowhandleopt)对OHNativeWindow设置宽高。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeWindow

**起始版本：** 22

**参数：**

参数项描述[OHNativeWindow](NativeWindow.md) *window一个指向OHNativeWindow的结构体实例的指针。uint32_t allocBufferCnt提前申请buffer的数量。当allocBufferCnt大于bufferQueueSize时，只能提前申请bufferQueueSize数量的buffer。bufferQueueSize可以通过[OH_NativeWindow_NativeWindowHandleOpt](external_window.h.md#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativewindowhandleopt)获取。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。