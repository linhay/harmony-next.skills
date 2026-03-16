# native_buffer.h

#### 概述

定义获取和使用NativeBuffer的相关函数。

**引用文件：** <native_buffer/native_buffer.h>

**库：** libnative_buffer.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**相关模块：**[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_NativeBuffer_Config](../../topics/misc/OH_NativeBuffer_Config.md)OH_NativeBuffer_ConfigOH_NativeBuffer的属性配置，用于申请新的OH_NativeBuffer实例或查询现有实例的相关属性。[OH_NativeBuffer_Plane](../../topics/misc/OH_NativeBuffer_Plane.md)OH_NativeBuffer_Plane单个图像平面格式信息。[OH_NativeBuffer_Planes](../../topics/misc/OH_NativeBuffer_Planes.md)OH_NativeBuffer_PlanesOH_NativeBuffer的图像平面格式信息。[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md)OH_NativeBuffer提供OH_NativeBuffer结构体声明。

#### 枚举

名称typedef关键字描述[OH_NativeBuffer_Usage](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_usage)OH_NativeBuffer_UsageOH_NativeBuffer的用途。[OH_NativeBuffer_ColorGamut](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_colorgamut)OH_NativeBuffer_ColorGamutOH_NativeBuffer的色域。

#### 函数

名称描述[OH_NativeBuffer* OH_NativeBuffer_Alloc(const OH_NativeBuffer_Config* config)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_alloc)

通过OH_NativeBuffer_Config创建OH_NativeBuffer实例，每次调用都会产生一个新的OH_NativeBuffer实例。

本接口需要与[OH_NativeBuffer_Unreference](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_Reference(OH_NativeBuffer *buffer)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_reference)

将OH_NativeBuffer对象的引用计数加1。

本接口需要与[OH_NativeBuffer_Unreference](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_Unreference(OH_NativeBuffer *buffer)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unreference)

将OH_NativeBuffer对象的引用计数减1，当引用计数为0的时候，该NativeBuffer对象会被析构掉。

本接口为非线程安全类型接口。

[void OH_NativeBuffer_GetConfig(OH_NativeBuffer buffer, OH_NativeBuffer_Config config)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_getconfig)

用于获取OH_NativeBuffer的属性。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_Map(OH_NativeBuffer *buffer, void **virAddr)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_map)

将OH_NativeBuffer对应的ION内存映射到进程空间。

本接口需要与[OH_NativeBuffer_Unmap](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unmap)接口配合使用。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_Unmap(OH_NativeBuffer *buffer)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unmap)

将OH_NativeBuffer对应的ION内存从进程空间移除。

本接口为非线程安全类型接口。

[uint32_t OH_NativeBuffer_GetSeqNum(OH_NativeBuffer *buffer)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_getseqnum)

获取OH_NativeBuffer的序列号。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_SetColorSpace(OH_NativeBuffer *buffer, OH_NativeBuffer_ColorSpace colorSpace)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_setcolorspace)

为OH_NativeBuffer设置颜色空间属性。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_MapPlanes(OH_NativeBuffer *buffer, void **virAddr, OH_NativeBuffer_Planes *outPlanes)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_mapplanes)

将OH_NativeBuffer对应的多通道ION内存映射到进程空间。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_FromNativeWindowBuffer(OHNativeWindowBuffer *nativeWindowBuffer, OH_NativeBuffer **buffer)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_fromnativewindowbuffer)

将OHNativeWindowBuffer实例转换为OH_NativeBuffer实例。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_GetColorSpace(OH_NativeBuffer *buffer, OH_NativeBuffer_ColorSpace *colorSpace)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_getcolorspace)

获取OH_NativeBuffer颜色空间属性。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_SetMetadataValue(OH_NativeBuffer *buffer, OH_NativeBuffer_MetadataKey metadataKey,int32_t size, uint8_t *metadata)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_setmetadatavalue)

为OH_NativeBuffer设置元数据属性值。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_GetMetadataValue(OH_NativeBuffer *buffer, OH_NativeBuffer_MetadataKey metadataKey,int32_t *size, uint8_t **metadata)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_getmetadatavalue)

获取OH_NativeBuffer元数据属性值。

本接口为非线程安全类型接口。

[int32_t OH_NativeBuffer_MapWaitFence(OH_NativeBuffer *buffer, int32_t fenceFd, void **virAddr)](#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_mapwaitfence)

将[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md)对应的ION内存映射到进程空间，永久阻塞传入的fenceFd。

如果接口返回OK，系统会将fenceFd关闭，无需用户close，否则，用户需要自行关闭fenceFd。

 本接口需要与[OH_NativeBuffer_Unmap](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unmap)接口配合使用。

本接口为非线程安全类型接口。

#### 枚举类型说明

#### OH_NativeBuffer_Usage

```ets
enum OH_NativeBuffer_Usage
```

**描述**

OH_NativeBuffer的用途。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 10

枚举项描述NATIVEBUFFER_USAGE_CPU_READ = (1ULL << 0)CPU可读。NATIVEBUFFER_USAGE_CPU_WRITE = (1ULL << 1)CPU可写。NATIVEBUFFER_USAGE_MEM_DMA = (1ULL << 3)直接内存访问缓冲区。NATIVEBUFFER_USAGE_MEM_MMZ_CACHE = (1ULL << 5)

媒体内存区域缓存。

**起始版本：** 20

NATIVEBUFFER_USAGE_HW_RENDER = (1ULL << 8)

GPU可写。

**起始版本：** 12

NATIVEBUFFER_USAGE_HW_TEXTURE = (1ULL << 9)

GPU可读。

**起始版本：** 12

NATIVEBUFFER_USAGE_CPU_READ_OFTEN = (1ULL << 16)

CPU可直接映射。

**起始版本：** 12

NATIVEBUFFER_USAGE_ALIGNMENT_512 = (1ULL << 18)

512字节对齐。

**起始版本：** 12

#### OH_NativeBuffer_ColorGamut

```ets
enum OH_NativeBuffer_ColorGamut
```

**描述**

OH_NativeBuffer的色域。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

枚举项描述NATIVEBUFFER_COLOR_GAMUT_NATIVE = 0默认色域格式。NATIVEBUFFER_COLOR_GAMUT_STANDARD_BT601 = 1Standard BT601色域格式。NATIVEBUFFER_COLOR_GAMUT_STANDARD_BT709 = 2Standard BT709色域格式。NATIVEBUFFER_COLOR_GAMUT_DCI_P3 = 3DCI P3色域格式。NATIVEBUFFER_COLOR_GAMUT_SRGB = 4SRGB色域格式。NATIVEBUFFER_COLOR_GAMUT_ADOBE_RGB = 5Adobe RGB色域格式。NATIVEBUFFER_COLOR_GAMUT_DISPLAY_P3 = 6Display P3色域格式。NATIVEBUFFER_COLOR_GAMUT_BT2020 = 7BT2020色域格式。NATIVEBUFFER_COLOR_GAMUT_BT2100_PQ = 8BT2100 PQ色域格式。NATIVEBUFFER_COLOR_GAMUT_BT2100_HLG = 9BT2100 HLG色域格式。NATIVEBUFFER_COLOR_GAMUT_DISPLAY_BT2020 = 10Display BT2020色域格式。

#### 函数说明

#### OH_NativeBuffer_Alloc()

```ets
OH_NativeBuffer* OH_NativeBuffer_Alloc(const OH_NativeBuffer_Config* config)
```

**描述**

通过OH_NativeBuffer_Config创建OH_NativeBuffer实例，每次调用都会产生一个新的OH_NativeBuffer实例。

本接口需要与[OH_NativeBuffer_Unreference](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

参数项描述const [OH_NativeBuffer_Config](../../topics/misc/OH_NativeBuffer_Config.md)* config一个指向OH_NativeBuffer_Config类型的指针。

**返回：**

类型说明OH_NativeBuffer*创建成功则返回一个指向OH_NativeBuffer结构体实例的指针，否则返回NULL。

#### OH_NativeBuffer_Reference()

```ets
int32_t OH_NativeBuffer_Reference(OH_NativeBuffer *buffer)
```

**描述**

将OH_NativeBuffer对象的引用计数加1。

本接口需要与[OH_NativeBuffer_Unreference](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unreference)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeBuffer_Unreference()

```ets
int32_t OH_NativeBuffer_Unreference(OH_NativeBuffer *buffer)
```

**描述**

将OH_NativeBuffer对象的引用计数减1，当引用计数为0的时候，该NativeBuffer对象会被析构掉。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeBuffer_GetConfig()

```ets
void OH_NativeBuffer_GetConfig(OH_NativeBuffer *buffer, OH_NativeBuffer_Config* config)
```

**描述**

用于获取OH_NativeBuffer的属性。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。[OH_NativeBuffer_Config](../../topics/misc/OH_NativeBuffer_Config.md)* config一个指向OH_NativeBuffer_Config的指针，用于接收OH_NativeBuffer的属性。

#### OH_NativeBuffer_Map()

```ets
int32_t OH_NativeBuffer_Map(OH_NativeBuffer *buffer, void **virAddr)
```

**描述**

将OH_NativeBuffer对应的ION内存映射到进程空间。

本接口需要与[OH_NativeBuffer_Unmap](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unmap)接口配合使用。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。void **virAddr一个二级指针，二级指针指向映射到当前进程的虚拟内存的地址。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeBuffer_Unmap()

```ets
int32_t OH_NativeBuffer_Unmap(OH_NativeBuffer *buffer)
```

**描述**

将OH_NativeBuffer对应的ION内存从进程空间移除。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeBuffer_GetSeqNum()

```ets
uint32_t OH_NativeBuffer_GetSeqNum(OH_NativeBuffer *buffer)
```

**描述**

获取OH_NativeBuffer的序列号。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 9

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。

**返回：**

类型说明uint32_t返回对应OH_NativeBuffer的唯一序列号。

#### OH_NativeBuffer_SetColorSpace()

```ets
int32_t OH_NativeBuffer_SetColorSpace(OH_NativeBuffer *buffer, OH_NativeBuffer_ColorSpace colorSpace)
```

**描述**

为OH_NativeBuffer设置颜色空间属性。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 11

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace) colorSpace为OH_NativeBuffer设置的颜色空间，其值从[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace)获取。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeBuffer_MapPlanes()

```ets
int32_t OH_NativeBuffer_MapPlanes(OH_NativeBuffer *buffer, void **virAddr, OH_NativeBuffer_Planes *outPlanes)
```

**描述**

将OH_NativeBuffer对应的多通道ION内存映射到进程空间。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。void **virAddr一个二级指针，二级指针指向映射到当前进程的虚拟内存的地址。[OH_NativeBuffer_Planes](../../topics/misc/OH_NativeBuffer_Planes.md) *outPlanes一个指向所有图像平面格式信息的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeBuffer_FromNativeWindowBuffer()

```ets
int32_t OH_NativeBuffer_FromNativeWindowBuffer(OHNativeWindowBuffer *nativeWindowBuffer, OH_NativeBuffer **buffer)
```

**描述**

将OHNativeWindowBuffer实例转换为OH_NativeBuffer实例。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**参数：**

参数项描述[OHNativeWindowBuffer](../../topics/misc/NativeWindowBuffer.md) *nativeWindowBuffer一个指向[OHNativeWindowBuffer](../../topics/misc/NativeWindowBuffer.md)实例的指针。[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) **buffer一个指向OH_NativeBuffer实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeBuffer_GetColorSpace()

```ets
int32_t OH_NativeBuffer_GetColorSpace(OH_NativeBuffer *buffer, OH_NativeBuffer_ColorSpace *colorSpace)
```

**描述**

获取OH_NativeBuffer颜色空间属性。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace) *colorSpace为[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md)设置的颜色空间，其值从[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace)获取。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeBuffer_SetMetadataValue()

```ets
int32_t OH_NativeBuffer_SetMetadataValue(OH_NativeBuffer *buffer, OH_NativeBuffer_MetadataKey metadataKey,int32_t size, uint8_t *metadata)
```

**描述**

为OH_NativeBuffer设置元数据属性值。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey) metadataKey[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md)的元数据类型，其值从[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey)获取。int32_t sizeuint8_t向量的大小，其取值范围参考[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey)。uint8_t *metadata指向uint8_t向量的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeBuffer_GetMetadataValue()

```ets
int32_t OH_NativeBuffer_GetMetadataValue(OH_NativeBuffer *buffer, OH_NativeBuffer_MetadataKey metadataKey,int32_t *size, uint8_t **metadata)
```

**描述**

获取OH_NativeBuffer元数据属性值。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向OH_NativeBuffer实例的指针。[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey) metadataKey[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md)的元数据类型，其值从[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey)获取。int32_t *sizeuint8_t向量的大小，其取值范围参考[OH_NativeBuffer_MetadataKey](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey)。uint8_t **metadata指向uint8_t向量的二级指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeBuffer_MapWaitFence()

```ets
int32_t OH_NativeBuffer_MapWaitFence(OH_NativeBuffer *buffer, int32_t fenceFd, void **virAddr)
```

**描述**

将[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md)对应的ION内存映射到进程空间，永久阻塞传入的fenceFd。

如果接口返回OK，系统会将fenceFd关闭，无需用户close，否则，用户需要自行关闭fenceFd。

本接口需要与[OH_NativeBuffer_Unmap](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unmap)接口配合使用。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 22

**参数：**

参数项描述[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *buffer一个指向[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md)实例的指针。int32_t fenceFd指向文件描述符句柄，用于并发同步控制。void **virAddr一个二级指针，二级指针指向映射到当前进程的虚拟内存的地址。

**返回：**

类型说明int32_t

执行成功时返回NATIVE_ERROR_OK。

buffer，virAddr是空指针或fenceFd小于0时返回NATIVE_ERROR_INVALID_ARGUMENTS。

映射失败时返回NATIVE_ERROR_UNKNOWN。