# OH_Pixelmap_HdrMetadataValue

```ets
typedef struct OH_Pixelmap_HdrMetadataValue {...} OH_Pixelmap_HdrMetadataValue
```

#### 概述

Pixelmap使用的HDR元数据值，和OH_Pixelmap_HdrMetadataKey关键字相对应。用于[OH_PixelmapNative_SetMetadata](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_setmetadata)及[OH_PixelmapNative_GetMetadata](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getmetadata)，有相应[OH_Pixelmap_HdrMetadataKey](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmap_hdrmetadatakey)关键字作为入参时，设置或获取到本结构体中相对应的元数据类型的值。

**起始版本：** 12

**相关模块：**[Image_NativeModule](Image_NativeModule.md)

**所在头文件：**[pixelmap_native.h](pixelmap_native.h.md)

#### 汇总

#### 成员变量

名称描述[OH_Pixelmap_HdrMetadataType](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmap_hdrmetadatatype) typeHDR_METADATA_TYPE关键字对应的具体值。[OH_Pixelmap_HdrStaticMetadata](OH_Pixelmap_HdrStaticMetadata.md) staticMetadataHDR_STATIC_METADATA关键字对应的具体值。[OH_Pixelmap_HdrDynamicMetadata](OH_Pixelmap_HdrDynamicMetadata.md) dynamicMetadataHDR_DYNAMIC_METADATA关键字对应的具体值。[OH_Pixelmap_HdrGainmapMetadata](OH_Pixelmap_HdrGainmapMetadata.md) gainmapMetadataHDR_GAINMAP_METADATA关键字对应的具体值。