# drawing_memory_stream.h

#### 概述

文件中定义了与内存流相关的功能函数。

**引用文件：** <native_drawing/drawing_memory_stream.h>

**库：** libnative_drawing.so

**起始版本：** 12

**相关模块：**[Drawing](../../topics/graphics/Drawing.md)

#### 汇总

#### 函数

名称描述[OH_Drawing_MemoryStream* OH_Drawing_MemoryStreamCreate(const void* data, size_t length, bool copyData)](#ZH-CN_TOPIC_0000002529285995__oh_drawing_memorystreamcreate)

创建一个内存流对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

data为NULL或者length等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_MemoryStreamDestroy(OH_Drawing_MemoryStream* memoryStream)](#ZH-CN_TOPIC_0000002529285995__oh_drawing_memorystreamdestroy)销毁内存流对象并回收该对象占有内存。

#### 函数说明

#### OH_Drawing_MemoryStreamCreate()

```ets
OH_Drawing_MemoryStream* OH_Drawing_MemoryStreamCreate(const void* data, size_t length, bool copyData)
```

**描述**

创建一个内存流对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

data为NULL或者length等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述const void* data数据段。size_t length数据段长度。bool copyData是否拷贝数据。true表示内存流对象会拷贝一份数据段数据，false表示内存流对象直接使用数据段数据，不拷贝。

**返回：**

类型说明[OH_Drawing_MemoryStream](../../topics/graphics/OH_Drawing_MemoryStream.md)*函数会返回一个指针，指针指向创建的内存流对象[OH_Drawing_MemoryStream](../../topics/graphics/OH_Drawing_MemoryStream.md)。

#### OH_Drawing_MemoryStreamDestroy()

```ets
void OH_Drawing_MemoryStreamDestroy(OH_Drawing_MemoryStream* memoryStream)
```

**描述**

销毁内存流对象并回收该对象占有内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_MemoryStream](../../topics/graphics/OH_Drawing_MemoryStream.md)* memoryStream指向内存流对象[OH_Drawing_MemoryStream](../../topics/graphics/OH_Drawing_MemoryStream.md)的指针。