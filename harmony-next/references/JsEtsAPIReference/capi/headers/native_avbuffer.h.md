# native_avbuffer.h

#### 概述

声明了媒体数据结构AVBuffer的函数接口。

**引用文件：** <multimedia/player_framework/native_avbuffer.h>

**库：** libnative_media_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**相关模块：**[Core](../../topics/misc/Core.md)

**相关示例：**[AVCodec](https://gitcode.com/HarmonyOS/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVBuffer](../../topics/misc/OH_AVBuffer.md)OH_AVBuffer为媒体内存接口定义native层对象。[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md)OH_NativeBuffer为图形内存接口定义native层对象。

#### 函数

名称描述[OH_AVBuffer *OH_AVBuffer_Create(int32_t capacity)](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_create)创建OH_AVBuffer实例。需要注意的是，返回值指向的创建OH_AVBuffer的实例需要开发者主动调用接口释放，请参阅[OH_AVBuffer_Destroy](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_destroy)。[OH_AVErrCode OH_AVBuffer_Destroy(OH_AVBuffer *buffer)](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_destroy)释放OH_AVBuffer实例指针的资源，同一个buffer不允许重复销毁。[OH_AVErrCode OH_AVBuffer_GetBufferAttr(OH_AVBuffer *buffer, OH_AVCodecBufferAttr *attr)](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_getbufferattr)获取数据缓冲区的pts、size、offset、flags高频属性参数。[OH_AVErrCode OH_AVBuffer_SetBufferAttr(OH_AVBuffer *buffer, const OH_AVCodecBufferAttr *attr)](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_setbufferattr)设置数据缓冲区的pts、size、offset、flags高频属性参数。[OH_AVFormat *OH_AVBuffer_GetParameter(OH_AVBuffer *buffer)](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_getparameter)获取除基础属性外的其他参数，信息在OH_AVFormat中承载。需要注意的是，返回值指向的创建OH_AVFormat的实例需要开发者主动释放，请参阅[OH_AVFormat_Destroy](native_avformat.h.md#ZH-CN_TOPIC_0000002497445762__oh_avformat_destroy)。[OH_AVErrCode OH_AVBuffer_SetParameter(OH_AVBuffer *buffer, const OH_AVFormat *format)](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_setparameter)设置除基础属性外的其他参数，信息在OH_AVFormat中承载。[uint8_t *OH_AVBuffer_GetAddr(OH_AVBuffer *buffer)](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_getaddr)获取数据缓冲区的虚拟地址。[int32_t OH_AVBuffer_GetCapacity(OH_AVBuffer *buffer)](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_getcapacity)获取数据缓冲区的容量（字节数）。[OH_NativeBuffer *OH_AVBuffer_GetNativeBuffer(OH_AVBuffer *buffer)](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_getnativebuffer)获取OH_NativeBuffer实例的指针。需要注意的是，返回值指向的创建OH_NativeBuffer的实例需要开发者主动调用接口释放，请参阅[OH_NativeBuffer_Unreference](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unreference)。

#### 函数说明

#### OH_AVBuffer_Create()

```ets
OH_AVBuffer *OH_AVBuffer_Create(int32_t capacity)
```

**描述**

创建OH_AVBuffer实例。需要注意的是，返回值指向的创建OH_AVBuffer的实例需要开发者主动调用接口释放，请参阅[OH_AVBuffer_Destroy](#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_destroy)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

参数项描述int32_t capacity创建内存的大小，单位字节。

**返回：**

类型说明[OH_AVBuffer](../../topics/misc/OH_AVBuffer.md) *

如果创建成功，则返回OH_AVBuffer实例的指针，如果失败，则返回NULL。

 可能的失败原因：

 1.capacity <= 0。

 2.出现内部错误，系统没有资源等。

#### OH_AVBuffer_Destroy()

```ets
OH_AVErrCode OH_AVBuffer_Destroy(OH_AVBuffer *buffer)
```

**描述**

释放OH_AVBuffer实例指针的资源，同一个buffer不允许重复销毁。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

参数项描述[OH_AVBuffer](../../topics/misc/OH_AVBuffer.md) *buffer指向OH_AVBuffer实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：操作成功。

 AV_ERR_INVALID_VAL：输入的buffer为空指针或者buffer格式校验失败。

 AV_ERR_OPERATE_NOT_PERMIT：输入的buffer不是用户创建的。

#### OH_AVBuffer_GetBufferAttr()

```ets
OH_AVErrCode OH_AVBuffer_GetBufferAttr(OH_AVBuffer *buffer, OH_AVCodecBufferAttr *attr)
```

**描述**

获取数据缓冲区的pts、size、offset、flags高频属性参数。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

参数项描述[OH_AVBuffer](../../topics/misc/OH_AVBuffer.md) *buffer指向OH_AVBuffer实例的指针。[OH_AVCodecBufferAttr](../../topics/misc/OH_AVCodecBufferAttr.md) *attr指向OH_AVCodecBufferAttr实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：操作成功。

 AV_ERR_INVALID_VAL：可能的原因：

 1. 输入的buffer或attr为空指针。

 2. buffer结构校验失败。

#### OH_AVBuffer_SetBufferAttr()

```ets
OH_AVErrCode OH_AVBuffer_SetBufferAttr(OH_AVBuffer *buffer, const OH_AVCodecBufferAttr *attr)
```

**描述**

设置数据缓冲区的pts、size、offset、flags高频属性参数。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

参数项描述[OH_AVBuffer](../../topics/misc/OH_AVBuffer.md) *buffer指向OH_AVBuffer实例的指针。[const OH_AVCodecBufferAttr](../../topics/misc/OH_AVCodecBufferAttr.md) *attr指向OH_AVCodecBufferAttr实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：操作成功。

 AV_ERR_INVALID_VAL：可能的原因：

 1. 输入的buffer或attr为空指针。

 2. buffer结构校验失败。

 3. 输入buffer中内存的size或offset是无效值。

#### OH_AVBuffer_GetParameter()

```ets
OH_AVFormat *OH_AVBuffer_GetParameter(OH_AVBuffer *buffer)
```

**描述**

获取除基础属性外的其他参数，信息在OH_AVFormat中承载。需要注意的是，返回值指向的创建OH_AVFormat的实例需要开发者主动释放，请参阅[OH_AVFormat_Destroy](native_avformat.h.md#ZH-CN_TOPIC_0000002497445762__oh_avformat_destroy)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

参数项描述[OH_AVBuffer](../../topics/misc/OH_AVBuffer.md) *buffer指向OH_AVBuffer实例的指针。

**返回：**

类型说明[OH_AVFormat](../../topics/misc/OH_AVFormat.md) *

AV_ERR_OK：操作成功。

 AV_ERR_INVALID_VAL：可能的原因：

 1. 输入的buffer为空指针。

 2. 输入buffer的meta为空指针。

 3. buffer结构校验失败。

#### OH_AVBuffer_SetParameter()

```ets
OH_AVErrCode OH_AVBuffer_SetParameter(OH_AVBuffer *buffer, const OH_AVFormat *format)
```

**描述**

设置除基础属性外的其他参数，信息在OH_AVFormat中承载。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

参数项描述[OH_AVBuffer](../../topics/misc/OH_AVBuffer.md) *buffer指向OH_AVBuffer实例的指针。[const OH_AVFormat](../../topics/misc/OH_AVFormat.md) *format指向OH_AVFormat实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：操作成功。

 AV_ERR_INVALID_VAL：可能的原因：

 1. 输入的buffer或format为空指针。

 2. 输入buffer的meta为空指针。

 3. buffer结构校验失败。

#### OH_AVBuffer_GetAddr()

```ets
uint8_t *OH_AVBuffer_GetAddr(OH_AVBuffer *buffer)
```

**描述**

获取数据缓冲区的虚拟地址。

不同场景下，对是否可以获取虚拟地址的支持情况不同，请见表格：

**编码：**

模式填充数据的方式是否可以获取虚拟地址Surface模式OnNeedInputBuffer输入×Surface模式OnNewOutputBuffer输出√Buffer模式OnNeedInputBuffer输入√Buffer模式OnNewOutputBuffer输出√

**解码：**

模式填充数据的方式是否可以获取虚拟地址Surface模式OnNeedInputBuffer输入√Surface模式OnNewOutputBuffer输出×Buffer模式OnNeedInputBuffer输入√Buffer模式OnNewOutputBuffer输出√

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

参数项描述[OH_AVBuffer](../../topics/misc/OH_AVBuffer.md) *buffer指向OH_AVBuffer实例的指针。

**返回：**

类型说明uint8_t *

如果成功，则返回数据缓冲区的虚拟地址，如果失败，则返回NULL。

 可能的失败原因：

 1.输入的buffer为空指针。

 2.OH_AVBuffer结构校验失败。

 3.出现内部错误。

#### OH_AVBuffer_GetCapacity()

```ets
int32_t OH_AVBuffer_GetCapacity(OH_AVBuffer *buffer)
```

**描述**

获取数据缓冲区的容量（字节数）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

参数项描述[OH_AVBuffer](../../topics/misc/OH_AVBuffer.md) *buffer指向OH_AVBuffer实例的指针。

**返回：**

类型说明int32_t

如果成功，则返回数据缓冲区的容量，如果失败，则返回-1。

 可能的失败原因：

 1.输入的buffer为空指针。

 2.OH_AVBuffer结构校验失败。

 3.出现内部错误。

#### OH_AVBuffer_GetNativeBuffer()

```ets
OH_NativeBuffer *OH_AVBuffer_GetNativeBuffer(OH_AVBuffer *buffer)
```

**描述**

获取OH_NativeBuffer实例的指针。需要注意的是，返回值指向的创建OH_NativeBuffer的实例需要开发者主动调用接口释放，请参阅[OH_NativeBuffer_Unreference](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_unreference)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 11

**参数：**

参数项描述[OH_AVBuffer](../../topics/misc/OH_AVBuffer.md) *buffer指向OH_AVBuffer实例的指针。

**返回：**

类型说明[OH_NativeBuffer](../../topics/misc/OH_NativeBuffer.md) *

如果成功，则返回OH_NativeBuffer实例的指针，如果失败，则返回NULL。

 可能的失败原因：

 1.输入的buffer为空指针。

 2.OH_AVBuffer结构校验失败。

 3.出现内部错误。