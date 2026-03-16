# native_avmemory.h

#### 概述

声明了媒体数据结构AVMemory的定义。

**引用文件：** <multimedia/player_framework/native_avmemory.h>

**库：** libnative_media_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**相关模块：**[Core](../../topics/misc/Core.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVMemory](../../topics/misc/OH_AVMemory.md)OH_AVMemory为音视频内存接口定义native层对象。

#### 函数

名称描述[OH_AVMemory *OH_AVMemory_Create(int32_t size)](#ZH-CN_TOPIC_0000002529285733__oh_avmemory_create)创建OH_AVMemory实例的指针。[uint8_t *OH_AVMemory_GetAddr(struct OH_AVMemory *mem)](#ZH-CN_TOPIC_0000002529285733__oh_avmemory_getaddr)获取内存虚拟地址。[int32_t OH_AVMemory_GetSize(struct OH_AVMemory *mem)](#ZH-CN_TOPIC_0000002529285733__oh_avmemory_getsize)获取内存长度。[OH_AVErrCode OH_AVMemory_Destroy(struct OH_AVMemory *mem)](#ZH-CN_TOPIC_0000002529285733__oh_avmemory_destroy)释放OH_AVMemory实例指针的资源。

#### 函数说明

#### OH_AVMemory_Create()

```ets
OH_AVMemory *OH_AVMemory_Create(int32_t size)
```

**描述**

创建OH_AVMemory实例的指针。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 10

**废弃版本：** 11

**替代接口：**[OH_AVBuffer_Create](native_avbuffer.h.md#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_create)

**参数：**

参数项描述int32_t size创建内存的大小，单位字节。

**返回：**

类型说明[OH_AVMemory](../../topics/misc/OH_AVMemory.md) *

如果创建成功，返回OH_AVMemory实例的指针，如果失败，返回NULL。

 使用结束后需要通过OH_AVMemory_Destroy释放内存。

 可能的失败原因：

 1. size <= 0。

 2. 创建OH_AVMemory失败。

 3. OH_AVMemory内存分配失败。

#### OH_AVMemory_GetAddr()

```ets
uint8_t *OH_AVMemory_GetAddr(struct OH_AVMemory *mem)
```

**描述**

获取内存虚拟地址。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**废弃版本：** 11

**替代接口：**[OH_AVBuffer_GetAddr](native_avbuffer.h.md#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_getaddr)

**参数：**

参数项描述[struct OH_AVMemory](../../topics/misc/OH_AVMemory.md) *mem指向OH_AVMemory实例的指针。

**返回：**

类型说明uint8_t *

如果内存有效，返回内存的虚拟地址，如果内存无效，返回NULL。

 可能的失败原因：

 1. 输入mem为空指针。

 2. 输入mem参数结构校验失败。

 3. 输入mem中内存为空指针。

#### OH_AVMemory_GetSize()

```ets
int32_t OH_AVMemory_GetSize(struct OH_AVMemory *mem)
```

**描述**

获取内存长度。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**废弃版本：** 11

**替代接口：**[OH_AVBuffer_GetCapacity](native_avbuffer.h.md#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_getcapacity)

**参数：**

参数项描述[struct OH_AVMemory](../../topics/misc/OH_AVMemory.md) *mem指向OH_AVMemory实例的指针。

**返回：**

类型说明int32_t

如果内存有效，返回内存长度，如果内存无效，返回-1。

 可能的失败原因：

 1. 输入mem为空指针。

 2. 输入mem参数结构校验失败。

 3. 输入mem中内存为空指针。

#### OH_AVMemory_Destroy()

```ets
OH_AVErrCode OH_AVMemory_Destroy(struct OH_AVMemory *mem)
```

**描述**

释放OH_AVMemory实例指针的资源。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 10

**废弃版本：** 11

**替代接口：**[OH_AVBuffer_Destroy](native_avbuffer.h.md#ZH-CN_TOPIC_0000002529285731__oh_avbuffer_destroy)

**参数：**

参数项描述[struct OH_AVMemory](../../topics/misc/OH_AVMemory.md) *mem指向OH_AVMemory实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：释放成功。

 AV_ERR_INVALID_VAL：

 1. 输入mem为空指针。

 2. 输入mem参数结构校验失败。

 3. 输入mem不是开发者创建的。