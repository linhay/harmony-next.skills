# VideoProcessing_ColorSpaceInfo

```ets
typedef struct VideoProcessing_ColorSpaceInfo {...} VideoProcessing_ColorSpaceInfo
```

#### 概述

视频颜色空间信息数据结构。

**参考：**[OH_VideoProcessing_IsColorSpaceConversionSupported](../../capi/headers/video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_iscolorspaceconversionsupported)

**起始版本：** 12

**相关模块：**[VideoProcessing](../system-services/VideoProcessing.md)

**所在头文件：**[video_processing_types.h](../../capi/headers/video_processing_types.h.md)

#### 汇总

#### 成员变量

名称描述int32_t metadataType视频元数据类型，参考[OH_NativeBuffer_MetadataType](../../capi/headers/buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatatype)。int32_t colorSpace视频颜色空间类型，参考[OH_NativeBuffer_ColorSpace](../../capi/headers/buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace)。int32_t pixelFormat视频像素格式，参考[OH_NativeBuffer_Format](../../capi/headers/buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_format)。