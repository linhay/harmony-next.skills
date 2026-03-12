# ImageProcessing_ColorSpaceInfo

```ets
typedef struct ImageProcessing_ColorSpaceInfo {...} ImageProcessing_ColorSpaceInfo
```

#### 概述

色彩空间信息，用于色彩空间转换能力查询。

**参考：**

[OH_ImageProcessing_IsColorSpaceConversionSupported](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_iscolorspaceconversionsupported), [OH_ImageProcessing_IsCompositionSupported](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_iscompositionsupported), [OH_ImageProcessing_IsDecompositionSupported](image_processing.h.md#ZH-CN_TOPIC_0000002529285851__oh_imageprocessing_isdecompositionsupported)

**起始版本：** 13

**相关模块：**[ImageProcessing](ImageProcessing.md)

**所在头文件：**[image_processing_types.h](image_processing_types.h.md)

#### 汇总

#### 成员变量

名称描述int32_t metadataType定义元数据类型，参考[OH_Pixelmap_HdrMetadataKey](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmap_hdrmetadatakey)。int32_t colorSpace定义色彩空间，参考[ColorSpaceName](native_color_space_manager.h.md#ZH-CN_TOPIC_0000002497605996__colorspacename)。int32_t pixelFormat定义像素格式，参考[PIXEL_FORMAT](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__pixel_format)。