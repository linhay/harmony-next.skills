# ImageProcessing_ColorSpaceInfo

```ets
typedef struct ImageProcessing_ColorSpaceInfo {...} ImageProcessing_ColorSpaceInfo
```

**概述**

色彩空间信息，用于色彩空间转换能力查询。

参考：

[OH_ImageProcessing_IsColorSpaceConversionSupported](image_processing.h.md#ZH-CN_TOPIC_0000002553361911__oh_imageprocessing_iscolorspaceconversionsupported), [OH_ImageProcessing_IsCompositionSupported](image_processing.h.md#ZH-CN_TOPIC_0000002553361911__oh_imageprocessing_iscompositionsupported), [OH_ImageProcessing_IsDecompositionSupported](image_processing.h.md#ZH-CN_TOPIC_0000002553361911__oh_imageprocessing_isdecompositionsupported)

起始版本： 13

相关模块： [ImageProcessing](ImageProcessing.md)

所在头文件： [image_processing_types.h](image_processing_types.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t metadataType | 定义元数据类型，参考OH_Pixelmap_HdrMetadataKey。 |
| int32_t colorSpace | 定义色彩空间，参考ColorSpaceName。 |
| int32_t pixelFormat | 定义像素格式，参考PIXEL_FORMAT。 |