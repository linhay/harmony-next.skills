# drawing_sampling_options.h

#### 概述

文件中定义了与采样相关的功能函数。用于图片或者纹理等图像的采样。

**引用文件：** <native_drawing/drawing_sampling_options.h>

**库：** libnative_drawing.so

**起始版本：** 12

**相关模块：**[Drawing](../../topics/graphics/Drawing.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_Drawing_FilterMode](#ZH-CN_TOPIC_0000002497446030__oh_drawing_filtermode)OH_Drawing_FilterMode过滤模式枚举。[OH_Drawing_MipmapMode](#ZH-CN_TOPIC_0000002497446030__oh_drawing_mipmapmode)OH_Drawing_MipmapMode多级渐远纹理模式枚举。

#### 函数

名称描述[OH_Drawing_SamplingOptions* OH_Drawing_SamplingOptionsCreate(OH_Drawing_FilterMode filterMode,OH_Drawing_MipmapMode mipmapMode)](#ZH-CN_TOPIC_0000002497446030__oh_drawing_samplingoptionscreate)

创建一个采样选项对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

mipmapMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[OH_Drawing_SamplingOptions* OH_Drawing_SamplingOptionsCopy(OH_Drawing_SamplingOptions* samplingOptions)](#ZH-CN_TOPIC_0000002497446030__oh_drawing_samplingoptionscopy)

创建一个采样选项对象副本[OH_Drawing_SamplingOptions](../../topics/graphics/OH_Drawing_SamplingOptions.md)，用于拷贝一个已有采样选项对象。

 本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

 samplingOptions为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_SamplingOptionsDestroy(OH_Drawing_SamplingOptions* samplingOptions)](#ZH-CN_TOPIC_0000002497446030__oh_drawing_samplingoptionsdestroy)销毁采样选项对象并回收该对象占有内存。

#### 枚举类型说明

#### OH_Drawing_FilterMode

```ets
enum OH_Drawing_FilterMode
```

**描述**

过滤模式枚举。

**起始版本：** 12

枚举项描述FILTER_MODE_NEAREST邻近过滤模式。FILTER_MODE_LINEAR线性过滤模式。

#### OH_Drawing_MipmapMode

```ets
enum OH_Drawing_MipmapMode
```

**描述**

多级渐远纹理模式枚举。

**起始版本：** 12

枚举项描述MIPMAP_MODE_NONE忽略多级渐远纹理级别。MIPMAP_MODE_NEAREST邻近多级渐远级别采样。MIPMAP_MODE_LINEAR两个邻近多级渐远纹理之间，线性插值采样。

#### 函数说明

#### OH_Drawing_SamplingOptionsCreate()

```ets
OH_Drawing_SamplingOptions* OH_Drawing_SamplingOptionsCreate(OH_Drawing_FilterMode filterMode,OH_Drawing_MipmapMode mipmapMode)
```

**描述**

创建一个采样选项对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

mipmapMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_FilterMode](#ZH-CN_TOPIC_0000002497446030__oh_drawing_filtermode) filterMode过滤采样模式[OH_Drawing_FilterMode](drawing_sampling_options.h.md#ZH-CN_TOPIC_0000002497446030__oh_drawing_filtermode)。[OH_Drawing_MipmapMode](#ZH-CN_TOPIC_0000002497446030__oh_drawing_mipmapmode) mipmapMode多级渐远纹理采样模式[OH_Drawing_MipmapMode](drawing_sampling_options.h.md#ZH-CN_TOPIC_0000002497446030__oh_drawing_mipmapmode)。

**返回：**

类型说明[OH_Drawing_SamplingOptions](../../topics/graphics/OH_Drawing_SamplingOptions.md)*函数会返回一个指针，指针指向创建的采样选项对象[OH_Drawing_SamplingOptions](../../topics/graphics/OH_Drawing_SamplingOptions.md)。

#### OH_Drawing_SamplingOptionsCopy()

```ets
OH_Drawing_SamplingOptions* OH_Drawing_SamplingOptionsCopy(OH_Drawing_SamplingOptions* samplingOptions)
```

**描述**

创建一个采样选项对象副本[OH_Drawing_SamplingOptions](../../topics/graphics/OH_Drawing_SamplingOptions.md)，用于拷贝一个已有采样选项对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

samplingOptions为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述[OH_Drawing_SamplingOptions](../../topics/graphics/OH_Drawing_SamplingOptions.md)* samplingOptions指向采样选项对象[OH_Drawing_SamplingOptions](../../topics/graphics/OH_Drawing_SamplingOptions.md)的指针。

**返回：**

类型说明OH_Drawing_SamplingOptions*函数会返回一个指针，指针指向创建的采样选项对象副本[OH_Drawing_SamplingOptions](../../topics/graphics/OH_Drawing_SamplingOptions.md)。如果对象返回NULL，表示创建失败；可能的原因是可用内存为空，或者是samplingOptions为NULL。

#### OH_Drawing_SamplingOptionsDestroy()

```ets
void OH_Drawing_SamplingOptionsDestroy(OH_Drawing_SamplingOptions* samplingOptions)
```

**描述**

销毁采样选项对象并回收该对象占有内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_SamplingOptions](../../topics/graphics/OH_Drawing_SamplingOptions.md)* samplingOptions指向采样选项对象[OH_Drawing_SamplingOptions](../../topics/graphics/OH_Drawing_SamplingOptions.md)的指针。