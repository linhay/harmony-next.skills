# image_processing_types.h

**概述**

图片处理的类型定义。

引用文件： <multimedia/video_processing_engine/image_processing_types.h>

库： libimage_processing.so

系统能力： SystemCapability.Multimedia.VideoProcessingEngine

起始版本： 13

相关模块： [ImageProcessing](ImageProcessing.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ImageProcessing_ColorSpaceInfo | ImageProcessing_ColorSpaceInfo | 色彩空间信息，用于色彩空间转换能力查询。 |
| OH_ImageProcessing | OH_ImageProcessing | 提供OH_ImageProcessing结构体声明。 定义了OH_ImageProcessing的空指针并调用OH_ImageProcessing_Create来创建图片处理实例。在创建实例之前，指针应为空。用户可以为不同的处理类型创建多个图片实例。 |
| OH_PixelmapNative | OH_PixelmapNative | 提供OH_PixelmapNative结构体声明。 |
| OH_AVFormat | OH_AVFormat | 提供OH_AVFormat结构体声明。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ImageDetailEnhancer_QualityLevel | ImageDetailEnhancer_QualityLevel | 质量级别，用于细节增强能力。 键参数的值IMAGE_DETAIL_ENHANCER_PARAMETER_KEY_QUALITY_LEVEL。 |
| ImageProcessing_ErrorCode | ImageProcessing_ErrorCode | 图片处理接口错误码说明。 |

**变量**

| 名称 | 描述 |
| --- | --- |
| const int32_t IMAGE_PROCESSING_TYPE_COLOR_SPACE_CONVERSION | 用于创建色彩空间转换的图片处理实例。 色彩空间转换包括单层HDR图片转换SDR图片，SDR图片之间的转换，以及SDR图片转换单层HDR图片，部分能力由厂商支持。使用OH_ImageProcessing_IsColorSpaceConversionSupported查询某种转换是否支持在单层图片之间进行。 起始版本： 13 参考：OH_ImageProcessing_Create |
| const int32_t IMAGE_PROCESSING_TYPE_COMPOSITION | 用于创建双层HDR图片转换单层HDR图片的图片处理实例。 包括从双层HDR图片转换为单层HDR图片的能力。部分能力由厂商支持。使用OH_ImageProcessing_IsCompositionSupported查询是否支持从双层HDR图片到单层HDR图片的转换。 起始版本： 13 参考：OH_ImageProcessing_Create |
| const int32_t IMAGE_PROCESSING_TYPE_DECOMPOSITION | 用于创建单层HDR图片转换双层HDR图片的图片处理实例。 包括从单层HDR图片转换为双层HDR图片的能力。部分能力由厂商支持。使用OH_ImageProcessing_IsDecompositionSupported查询是否支持从单层HDR图片到双层HDR图片的转换。 起始版本： 13 参考：OH_ImageProcessing_Create |
| const int32_t IMAGE_PROCESSING_TYPE_METADATA_GENERATION | 用于创建元数据生成的图片处理实例。 生成单层HDR图片的HDR Vivid元数据。该能力由厂商支持。如果不支持该能力，OH_ImageProcessing_Create将返回IMAGE_PROCESSING_ERROR_UNSUPPORTED_PROCESSING。 起始版本： 13 参考：OH_ImageProcessing_Create |
| const int32_t IMAGE_PROCESSING_TYPE_DETAIL_ENHANCER | 用于创建细节增强的图片处理实例。 按指定图像质量缩放或调整图片大小，或仅增强图像细节以在不更改分辨率的情况下渲染图片。 起始版本： 13 参考：OH_ImageProcessing_Create |
| const char * IMAGE_DETAIL_ENHANCER_PARAMETER_KEY_QUALITY_LEVEL | 用于设定图像细节增强的质量级别。 使用ImageDetailEnhancer_QualityLevel获取其值。使用OH_ImageProcessing_SetParameter设置质量级别。使用OH_ImageProcessing_GetParameter获取当前质量级别。 起始版本： 13 |

**枚举类型说明**

**ImageDetailEnhancer_QualityLevel**

```ets
enum ImageDetailEnhancer_QualityLevel
```

描述

质量级别，用于细节增强能力。

键参数的值IMAGE_DETAIL_ENHANCER_PARAMETER_KEY_QUALITY_LEVEL。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| IMAGE_DETAIL_ENHANCER_QUALITY_LEVEL_NONE | 无细节增强。 |
| IMAGE_DETAIL_ENHANCER_QUALITY_LEVEL_LOW | 细节增强质量较低，但速度较快。默认级别。 |
| IMAGE_DETAIL_ENHANCER_QUALITY_LEVEL_MEDIUM | 细节增强质量中等，速度介于低级别与高级别之间。 |
| IMAGE_DETAIL_ENHANCER_QUALITY_LEVEL_HIGH | 细节增强质量较高，但速度较慢。 |

参考：

[OH_ImageProcessing_SetParameter](image_processing.h.md#ZH-CN_TOPIC_0000002553361911__oh_imageprocessing_setparameter)，[OH_ImageProcessing_GetParameter](image_processing.h.md#ZH-CN_TOPIC_0000002553361911__oh_imageprocessing_getparameter)

**ImageProcessing_ErrorCode**

```ets
enum ImageProcessing_ErrorCode
```

描述

图片处理接口错误码说明。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| IMAGE_PROCESSING_SUCCESS | 成功。 |
| IMAGE_PROCESSING_ERROR_INVALID_PARAMETER = 401 | 输入参数无效。 在以下错误条件返回该错误码： 1. 输入或输出buffer无效，例如图片buffer为空。 2. 参数无效，例如参数为空。 3. 类型无效，例如在创建函数中传入的类型不存在。 |
| IMAGE_PROCESSING_ERROR_UNKNOWN = 29200001 | 未知错误，例如GPU计算失败或memcpy失败。 |
| IMAGE_PROCESSING_ERROR_INITIALIZE_FAILED | 全局环境初始化失败，例如GPU环境初始化失败。 |
| IMAGE_PROCESSING_ERROR_CREATE_FAILED | 创建图片处理实例失败，例如实例数量超过上限。 |
| IMAGE_PROCESSING_ERROR_PROCESS_FAILED | 处理图片buffer失败，例如处理超时。 |
| IMAGE_PROCESSING_ERROR_UNSUPPORTED_PROCESSING | 当前处理不支持，可以通过“OH_ImageProcessing_IsXXXSupported”接口查询是否支持该能力。 |
| IMAGE_PROCESSING_ERROR_OPERATION_NOT_PERMITTED | 无权限操作，可能由于状态不正确导致。 |
| IMAGE_PROCESSING_ERROR_NO_MEMORY | 内存不足。 |
| IMAGE_PROCESSING_ERROR_INVALID_INSTANCE | 无效的图片处理实例，可能由于实例为空导致。 |
| IMAGE_PROCESSING_ERROR_INVALID_VALUE | 输入值无效。 在以下错误条件下返回该错误码： 1. 输入或输出图片buffer无效，例如图片buffer的宽度（高度）过大或颜色空间不正确。 2. 参数无效，例如参数不包括有效信息，例如细节增强的质量级别不正确。 |