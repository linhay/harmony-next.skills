# image_processing.h

#### 概述

声明图片处理函数。提供图片处理能力，包括色彩空间转换，元数据生成及图片缩放。

**引用文件：** <multimedia/video_processing_engine/image_processing.h>

**库：** libimage_processing.so

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**起始版本：** 13

**相关模块：**[ImageProcessing](../../topics/graphics/ImageProcessing.md)

#### 汇总

#### 函数

名称描述[ImageProcessing_ErrorCode OH_ImageProcessing_InitializeEnvironment(void)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_initializeenvironment)

初始化图片处理模块的全局环境。

此函数为非必需函数。通常此函数在主进程启动时被调用，用于图片处理模块的全局环境初始化并可以减少[OH_ImageProcessing_Create](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_create)的耗时。调用[OH_ImageProcessing_DeinitializeEnvironment](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_deinitializeenvironment)进行全局环境反初始化。可用于检查设备GPU是否正常工作。

[ImageProcessing_ErrorCode OH_ImageProcessing_DeinitializeEnvironment(void)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_deinitializeenvironment)

反初始化图片处理模块的全局环境。

如果[OH_ImageProcessing_InitializeEnvironment](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_initializeenvironment)被调用，则此函数为必需函数。通常此函数在主进程准备退出时被调用，用于反初始化图片处理模块的全局环境（由[OH_ImageProcessing_InitializeEnvironment](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_initializeenvironment)接口初始化）。如果此时存在图片处理实例，则不应调用此函数。如果[OH_ImageProcessing_InitializeEnvironment](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_initializeenvironment)未被调用，则不应调用此函数。

[bool OH_ImageProcessing_IsColorSpaceConversionSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo, const ImageProcessing_ColorSpaceInfo* destinationImageInfo)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_iscolorspaceconversionsupported)查询是否支持当前图片色彩空间转换能力。[bool OH_ImageProcessing_IsCompositionSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo, const ImageProcessing_ColorSpaceInfo* sourceGainmapInfo,const ImageProcessing_ColorSpaceInfo* destinationImageInfo)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_iscompositionsupported)查询是否支持HDR双层图片转换为HDR单层图片。[bool OH_ImageProcessing_IsDecompositionSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo, const ImageProcessing_ColorSpaceInfo* destinationImageInfo, const ImageProcessing_ColorSpaceInfo* destinationGainmapInfo)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_isdecompositionsupported)查询是否支持HDR单层图片转换为HDR双层图片。[bool OH_ImageProcessing_IsMetadataGenerationSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_ismetadatagenerationsupported)查询是否支持图片元数据生成能力。[ImageProcessing_ErrorCode OH_ImageProcessing_Create(OH_ImageProcessing** imageProcessor, int32_t type)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_create)创建一个图片处理模块实例。[ImageProcessing_ErrorCode OH_ImageProcessing_Destroy(OH_ImageProcessing* imageProcessor)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_destroy)销毁当前图片处理模块实例。[ImageProcessing_ErrorCode OH_ImageProcessing_SetParameter(OH_ImageProcessing* imageProcessor, const OH_AVFormat* parameter)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_setparameter)设置图片处理模块参数。通过特定参数键添加参数。[ImageProcessing_ErrorCode OH_ImageProcessing_GetParameter(OH_ImageProcessing* imageProcessor, OH_AVFormat* parameter)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_getparameter)获取图片处理模块参数。通过特定参数键获取参数。[ImageProcessing_ErrorCode OH_ImageProcessing_ConvertColorSpace(OH_ImageProcessing* imageProcessor, OH_PixelmapNative* sourceImage, OH_PixelmapNative* destinationImage)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_convertcolorspace)实现单层图片间转换。此函数包括HDR图片到SDR图片的色彩空间转换，SDR图片到HDR图片的色彩空间转换，SDR图片到SDR图片的色彩空间转换和HDR图片的色彩空间转换。[ImageProcessing_ErrorCode OH_ImageProcessing_Compose(OH_ImageProcessing* imageProcessor, OH_PixelmapNative* sourceImage, OH_PixelmapNative* sourceGainmap, OH_PixelmapNative* destinationImage)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_compose)实现HDR双层图片到HDR单层图片的转换。此函数通过输入图片与输入Gainmap生成输出图片。[ImageProcessing_ErrorCode OH_ImageProcessing_Decompose(OH_ImageProcessing* imageProcessor, OH_PixelmapNative* sourceImage, OH_PixelmapNative* destinationImage, OH_PixelmapNative* destinationGainmap)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_decompose)实现HDR单层图片到HDR双层图片的转换。此函数通过输入图片生成输出图片和输出Gainmap。[ImageProcessing_ErrorCode OH_ImageProcessing_GenerateMetadata(OH_ImageProcessing* imageProcessor, OH_PixelmapNative* sourceImage)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_generatemetadata)生成HDR图片元数据。此函数为HDR图片生成元数据。[ImageProcessing_ErrorCode OH_ImageProcessing_EnhanceDetail(OH_ImageProcessing* imageProcessor, OH_PixelmapNative* sourceImage, OH_PixelmapNative* destinationImage)](#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_enhancedetail)进行图片清晰度/细节增强。此函数根据输入图片和输出图片预设的尺寸，对源图片进行必要的缩放操作生成目标图片，并提供了多种缩放方法以平衡性能和图像质量。

#### 函数说明

#### OH_ImageProcessing_InitializeEnvironment()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_InitializeEnvironment(void)
```

**描述**

初始化图片处理模块的全局环境。

此函数为非必需函数。通常此函数在主进程启动时被调用，用于图片处理模块的全局环境初始化并可以减少[OH_ImageProcessing_Create](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_create)的耗时。调用[OH_ImageProcessing_DeinitializeEnvironment](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_deinitializeenvironment)进行全局环境反初始化。可用于检查设备GPU是否正常工作。

**起始版本：** 13

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)如果初始化成功，则返回IMAGE_PROCESSING_SUCCESS，否则返回IMAGE_PROCESSING_ERROR_INITIALIZE_FAILED。

#### OH_ImageProcessing_DeinitializeEnvironment()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_DeinitializeEnvironment(void)
```

**描述**

反初始化图片处理模块的全局环境。

如果[OH_ImageProcessing_InitializeEnvironment](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_initializeenvironment)被调用，则此函数为必需函数。通常此函数在主进程准备退出时被调用，用于反初始化图片处理模块的全局环境（由[OH_ImageProcessing_InitializeEnvironment](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_initializeenvironment)接口初始化）。如果此时存在图片处理实例，则不应调用此函数。如果[OH_ImageProcessing_InitializeEnvironment](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_initializeenvironment)未被调用，则不应调用此函数。

**起始版本：** 13

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)

如果反初始化成功，则返回IMAGE_PROCESSING_SUCCESS。

如果存在图片处理实例未被销毁或[OH_ImageProcessing_InitializeEnvironment](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_initializeenvironment)接口未被调用，则返回IMAGE_PROCESSING_ERROR_OPERATION_NOT_PERMITTED。

#### OH_ImageProcessing_IsColorSpaceConversionSupported()

```ets
bool OH_ImageProcessing_IsColorSpaceConversionSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo,const ImageProcessing_ColorSpaceInfo* destinationImageInfo)
```

**描述**

查询是否支持当前图片色彩空间转换能力。

**起始版本：** 13

**参数：**

参数项描述const [ImageProcessing_ColorSpaceInfo](../../topics/graphics/ImageProcessing_ColorSpaceInfo.md)* sourceImageInfo指向输入图片色彩空间信息的指针。const [ImageProcessing_ColorSpaceInfo](../../topics/graphics/ImageProcessing_ColorSpaceInfo.md)* destinationImageInfo指向输出图片色彩空间信息的指针，

**返回：**

类型说明bool

如果支持当前色彩空间转换，返回true。

如果不支持当前色彩空间转换，返回false。

#### OH_ImageProcessing_IsCompositionSupported()

```ets
bool OH_ImageProcessing_IsCompositionSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo,const ImageProcessing_ColorSpaceInfo* sourceGainmapInfo,const ImageProcessing_ColorSpaceInfo* destinationImageInfo)
```

**描述**

查询是否支持HDR双层图片转换为HDR单层图片。

**起始版本：** 13

**参数：**

参数项描述const [ImageProcessing_ColorSpaceInfo](../../topics/graphics/ImageProcessing_ColorSpaceInfo.md)* sourceImageInfo指向输入图片色彩空间信息的指针。const [ImageProcessing_ColorSpaceInfo](../../topics/graphics/ImageProcessing_ColorSpaceInfo.md)* sourceGainmapInfo指向输入Gainmap色彩空间信息的指针。const [ImageProcessing_ColorSpaceInfo](../../topics/graphics/ImageProcessing_ColorSpaceInfo.md)* destinationImageInfo指向输出图片色彩空间信息的指针。

**返回：**

类型说明bool

如果支持HDR双层图片转换HDR单层图片能力，返回true。

如果不支持此能力，返回false。

#### OH_ImageProcessing_IsDecompositionSupported()

```ets
bool OH_ImageProcessing_IsDecompositionSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo,const ImageProcessing_ColorSpaceInfo* destinationImageInfo,const ImageProcessing_ColorSpaceInfo* destinationGainmapInfo)
```

**描述**

查询是否支持HDR单层图片转换为HDR双层图片。

**起始版本：** 13

**参数：**

参数项描述const [ImageProcessing_ColorSpaceInfo](../../topics/graphics/ImageProcessing_ColorSpaceInfo.md)* sourceImageInfo指向输入图片色彩空间信息的指针。const [ImageProcessing_ColorSpaceInfo](../../topics/graphics/ImageProcessing_ColorSpaceInfo.md)* destinationImageInfo指向输出图片色彩空间信息的指针。const [ImageProcessing_ColorSpaceInfo](../../topics/graphics/ImageProcessing_ColorSpaceInfo.md)* destinationGainmapInfo指向输出Gainmap色彩空间信息的指针。

**返回：**

类型说明bool

如果支持HDR单层图片转换为HDR双层图片能力，返回true。

如果不支持此能力，返回false。

#### OH_ImageProcessing_IsMetadataGenerationSupported()

```ets
bool OH_ImageProcessing_IsMetadataGenerationSupported(const ImageProcessing_ColorSpaceInfo* sourceImageInfo)
```

**描述**

查询是否支持图片元数据生成能力。

**起始版本：** 13

**参数：**

参数项描述const [ImageProcessing_ColorSpaceInfo](../../topics/graphics/ImageProcessing_ColorSpaceInfo.md)* sourceImageInfo指向输入图片色彩空间信息的指针。

**返回：**

类型说明bool

如果支持图片元数据生成能力，返回true。

如果不支持此能力，返回false。

#### OH_ImageProcessing_Create()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_Create(OH_ImageProcessing** imageProcessor, int32_t type)
```

**描述**

创建一个图片处理模块实例。

**起始版本：** 13

**参数：**

参数项描述[OH_ImageProcessing](../../topics/graphics/OH_ImageProcessing.md)** imageProcessor输出参数。指针*imageProcessor指向一个新的图片处理对象。指针*imageProcessor在传递前必须是一个空指针。int32_t type使用IMAGE_PROCESSING_TYPE_XXX来指定图片处理类型。此实例的类型在创建后不能更改。

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)

如果创建成功，则返回IMAGE_PROCESSING_SUCCESS。

当指定的图片处理类型不支持时，返回IMAGE_PROCESSING_ERROR_UNSUPPORTED_PROCESSING，例如如果不支持图片元数据生成能力，则返回不支持该处理类型。

当创建失败时，返回IMAGE_PROCESSING_ERROR_CREATE_FAILED。

当该实例为空或指向该实例的指针为空时，返回IMAGE_PROCESSING_ERROR_INVALID_INSTANCE。

当指定的图片处理类型无效时，返回IMAGE_PROCESSING_ERROR_INVALID_PARAMETER。

#### OH_ImageProcessing_Destroy()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_Destroy(OH_ImageProcessing* imageProcessor)
```

**描述**

销毁当前图片处理模块实例。

**起始版本：** 13

**参数：**

参数项描述[OH_ImageProcessing](../../topics/graphics/OH_ImageProcessing.md)* imageProcessor指向图片处理模块实例的指针。当实例被销毁时，建议该指针设置为空。

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)

如果销毁成功，则返回IMAGE_PROCESSING_SUCCESS。

当该实例为空或该实例不是图片处理模块实例时，返回IMAGE_PROCESSING_ERROR_INVALID_INSTANCE。

#### OH_ImageProcessing_SetParameter()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_SetParameter(OH_ImageProcessing* imageProcessor,const OH_AVFormat* parameter)
```

**描述**

设置图片处理模块参数。通过特定参数键添加参数。

**起始版本：** 13

**参数：**

参数项描述[OH_ImageProcessing](../../topics/graphics/OH_ImageProcessing.md)* imageProcessor指向图片处理模块实例的指针。const [OH_AVFormat](../../topics/misc/OH_AVFormat.md)* parameter图片处理参数。

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)

如果设置参数成功，则返回IMAGE_PROCESSING_SUCCESS。

当该实例为空或该实例不是图片处理模块实例时，返回IMAGE_PROCESSING_ERROR_INVALID_INSTANCE。

当参数为空时，返回IMAGE_PROCESSING_ERROR_INVALID_PARAMETER。

当部分参数无效时，返回IMAGE_PROCESSING_ERROR_INVALID_VALUE，例如参数包含不支持的参数键或值。

当内存分配失败时，返回IMAGE_PROCESSING_ERROR_NO_MEMORY。

#### OH_ImageProcessing_GetParameter()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_GetParameter(OH_ImageProcessing* imageProcessor,OH_AVFormat* parameter)
```

**描述**

获取图片处理模块参数。通过特定参数键获取参数。

**起始版本：** 13

**参数：**

参数项描述[OH_ImageProcessing](../../topics/graphics/OH_ImageProcessing.md)* imageProcessor指向图片处理模块实例的指针。[OH_AVFormat](../../topics/misc/OH_AVFormat.md)* parameter该图片处理模块实例使用的参数。

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)

如果获取参数成功，则返回IMAGE_PROCESSING_SUCCESS。

当该实例为空或该实例不是图片处理模块实例时，返回IMAGE_PROCESSING_ERROR_INVALID_INSTANCE。

当参数为空时，返回IMAGE_PROCESSING_ERROR_INVALID_PARAMETER。

#### OH_ImageProcessing_ConvertColorSpace()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_ConvertColorSpace(OH_ImageProcessing* imageProcessor,OH_PixelmapNative* sourceImage, OH_PixelmapNative* destinationImage)
```

**描述**

实现单层图片间转换。此函数包括HDR图片到SDR图片的色彩空间转换，SDR图片到HDR图片的色彩空间转换，SDR图片到SDR图片的色彩空间转换和HDR图片的色彩空间转换。

**起始版本：** 13

**参数：**

参数项描述[OH_ImageProcessing](../../topics/graphics/OH_ImageProcessing.md)* imageProcessor指向图片处理模块实例的指针。该实例应该由IMAGE_PROCESSING_TYPE_COLOR_SPACE_CONVERSION类型创建。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* sourceImage指向输入图片的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* destinationImage指向输出图片的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)

如果图片处理成功，则返回IMAGE_PROCESSING_SUCCESS。

当该实例为空或该实例不是图片处理模块实例时，返回IMAGE_PROCESSING_ERROR_INVALID_INSTANCE。

当图片为空时，返回IMAGE_PROCESSING_ERROR_INVALID_PARAMETER。

当图片的某些属性无效时，返回IMAGE_PROCESSING_ERROR_INVALID_VALUE，例如图片的色彩空间是不支持的。

当该图片处理不支持时，返回IMAGE_PROCESSING_ERROR_UNSUPPORTED_PROCESSING。

当该图片处理中返回错误时，返回IMAGE_PROCESSING_ERROR_PROCESS_FAILED。

当内存分配失败时，返回IMAGE_PROCESSING_ERROR_NO_MEMORY。

#### OH_ImageProcessing_Compose()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_Compose(OH_ImageProcessing* imageProcessor,OH_PixelmapNative* sourceImage, OH_PixelmapNative* sourceGainmap, OH_PixelmapNative* destinationImage)
```

**描述**

实现HDR双层图片到HDR单层图片的转换。此函数通过输入图片与输入Gainmap生成输出图片。

**起始版本：** 13

**参数：**

参数项描述[OH_ImageProcessing](../../topics/graphics/OH_ImageProcessing.md)* imageProcessor指向图片处理模块实例的指针。该实例应该由IMAGE_PROCESSING_TYPE_COMPOSITION类型创建。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* sourceImage指向输入图片的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* sourceGainmap指向输入Gainmap的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* destinationImage指向输出图片的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)

如果图片处理成功，则返回IMAGE_PROCESSING_SUCCESS。

当该实例为空或该实例不是图片处理模块实例时，返回IMAGE_PROCESSING_ERROR_INVALID_INSTANCE。

当图片为空时，返回IMAGE_PROCESSING_ERROR_INVALID_PARAMETER。

当图片的某些属性无效时，返回IMAGE_PROCESSING_ERROR_INVALID_VALUE，例如图片的色彩空间是不支持的。

当该图片处理不支持时，返回IMAGE_PROCESSING_ERROR_UNSUPPORTED_PROCESSING。

当该图片处理中返回错误时，返回IMAGE_PROCESSING_ERROR_PROCESS_FAILED。

当内存分配失败时，返回IMAGE_PROCESSING_ERROR_NO_MEMORY。

#### OH_ImageProcessing_Decompose()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_Decompose(OH_ImageProcessing* imageProcessor,OH_PixelmapNative* sourceImage, OH_PixelmapNative* destinationImage, OH_PixelmapNative* destinationGainmap)
```

**描述**

实现HDR单层图片到HDR双层图片的转换。此函数通过输入图片生成输出图片和输出Gainmap。

**起始版本：** 13

**参数：**

参数项描述[OH_ImageProcessing](../../topics/graphics/OH_ImageProcessing.md)* imageProcessor指向图片处理模块实例的指针。该实例应该由IMAGE_PROCESSING_TYPE_DECOMPOSITION类型创建。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* sourceImage指向输入图片的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* destinationImage指向输出图片的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* destinationGainmap指向输出Gainmap的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)

如果图片处理成功，则返回IMAGE_PROCESSING_SUCCESS。

当该实例为空或该实例不是图片处理模块实例时，返回IMAGE_PROCESSING_ERROR_INVALID_INSTANCE。

当图片为空时，返回IMAGE_PROCESSING_ERROR_INVALID_PARAMETER。

当图片的某些属性无效时，返回IMAGE_PROCESSING_ERROR_INVALID_VALUE，例如图片的色彩空间是不支持的。

当该图片处理不支持时，返回IMAGE_PROCESSING_ERROR_UNSUPPORTED_PROCESSING。

当该图片处理中返回错误时，返回IMAGE_PROCESSING_ERROR_PROCESS_FAILED。

当内存分配失败时，返回IMAGE_PROCESSING_ERROR_NO_MEMORY。

#### OH_ImageProcessing_GenerateMetadata()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_GenerateMetadata(OH_ImageProcessing* imageProcessor,OH_PixelmapNative* sourceImage)
```

**描述**

生成HDR图片元数据。此函数为HDR图片生成元数据。

**起始版本：** 13

**参数：**

参数项描述[OH_ImageProcessing](../../topics/graphics/OH_ImageProcessing.md)* imageProcessor指向图片处理模块实例的指针。该实例应该由IMAGE_PROCESSING_TYPE_METADATA_GENERATION类型创建。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* sourceImage指向输入图片的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)

如果图片处理成功，则返回IMAGE_PROCESSING_SUCCESS。

当该实例为空或该实例不是图片处理模块实例时，返回IMAGE_PROCESSING_ERROR_INVALID_INSTANCE。

当图片为空时，返回IMAGE_PROCESSING_ERROR_INVALID_PARAMETER。

当图片的某些属性无效时，返回IMAGE_PROCESSING_ERROR_INVALID_VALUE，例如图片的色彩空间是不支持的。

当该图片处理不支持时，返回IMAGE_PROCESSING_ERROR_UNSUPPORTED_PROCESSING。

当该图片处理中返回错误时，返回IMAGE_PROCESSING_ERROR_PROCESS_FAILED。

当内存分配失败时，返回IMAGE_PROCESSING_ERROR_NO_MEMORY。

#### OH_ImageProcessing_EnhanceDetail()

```ets
ImageProcessing_ErrorCode OH_ImageProcessing_EnhanceDetail(OH_ImageProcessing* imageProcessor,OH_PixelmapNative* sourceImage, OH_PixelmapNative* destinationImage)
```

**描述**

进行图片清晰度/细节增强。此函数根据输入图片和输出图片预设的尺寸，对源图片进行必要的缩放操作生成目标图片，并提供了多种缩放方法以平衡性能和图像质量。

**起始版本：** 13

**参数：**

参数项描述[OH_ImageProcessing](../../topics/graphics/OH_ImageProcessing.md)* imageProcessor指向图片处理模块实例的指针。该实例应该由IMAGE_PROCESSING_TYPE_DETAIL_ENHANCER类型创建。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* sourceImage指向输入图片的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)* destinationImage指向输出图片的指针，指向的OH_PixelmapNative需为DMA内存，具体情况请参考[PixelMap的内存类型介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-allocator-type#内存类型介绍)。

**返回：**

类型说明[ImageProcessing_ErrorCode](image_processing_types.h.md#ZH-CN_TOPIC_0000002529445825__imageprocessing_errorcode)

如果图片处理成功，则返回IMAGE_PROCESSING_SUCCESS。

当该实例为空或该实例不是图片处理模块实例时，返回IMAGE_PROCESSING_ERROR_INVALID_INSTANCE。

当图片为空时，返回IMAGE_PROCESSING_ERROR_INVALID_PARAMETER。

当图片的某些属性无效时，返回IMAGE_PROCESSING_ERROR_INVALID_VALUE，例如图片的色彩空间是不支持的。

当该图片处理不支持时，返回IMAGE_PROCESSING_ERROR_UNSUPPORTED_PROCESSING。

当该图片处理中返回错误时，返回IMAGE_PROCESSING_ERROR_PROCESS_FAILED。

当内存分配失败时，返回IMAGE_PROCESSING_ERROR_NO_MEMORY。