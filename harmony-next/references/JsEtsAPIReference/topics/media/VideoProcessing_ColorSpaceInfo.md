# VideoProcessing_ColorSpaceInfo

```ets
typedef struct VideoProcessing_ColorSpaceInfo {...} VideoProcessing_ColorSpaceInfo
```

**概述**

视频颜色空间信息数据结构。

参考： [OH_VideoProcessing_IsColorSpaceConversionSupported](video_processing.h.md#ZH-CN_TOPIC_0000002522242050__oh_videoprocessing_iscolorspaceconversionsupported)

起始版本： 12

相关模块： [VideoProcessing](VideoProcessing.md)

所在头文件： [video_processing_types.h](video_processing_types.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t metadataType | 视频元数据类型，参考OH_NativeBuffer_MetadataType。 |
| int32_t colorSpace | 视频颜色空间类型，参考OH_NativeBuffer_ColorSpace。 |
| int32_t pixelFormat | 视频像素格式，参考OH_NativeBuffer_Format。 |