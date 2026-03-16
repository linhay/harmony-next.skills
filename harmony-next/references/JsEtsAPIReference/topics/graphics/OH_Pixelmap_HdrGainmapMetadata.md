# OH_Pixelmap_HdrGainmapMetadata

```ets
typedef struct OH_Pixelmap_HdrGainmapMetadata {...} OH_Pixelmap_HdrGainmapMetadata
```

#### 概述

HDR_GAINMAP_METADATA关键字对应的gainmap相关元数据值，参考ISO 21496-1。

**起始版本：** 12

**相关模块：**[Image_NativeModule](Image_NativeModule.md)

**所在头文件：**[pixelmap_native.h](../../capi/headers/pixelmap_native.h.md)

#### 汇总

#### 成员变量

名称描述uint16_t writerVersion元数据编写器使用的版本。uint16_t miniVersion元数据解析需要理解的最小版本。uint8_t gainmapChannelNumGainmap的颜色通道数，值为3时RGB通道的元数据值不同，值为1时各通道元数据值相同。bool useBaseColorFlag是否使用基础图的色彩空间，参考ISO 21496-1。float baseHeadroom基础图提亮比，参考ISO 21496-1。float alternateHeadroom提取的可选择图像提亮比，参考ISO 21496-1。float gainmapMax[3]增强图像的最大值，参考ISO 21496-1。float gainmapMin[3]增强图像的最小值，参考ISO 21496-1。float gamma[3]gamma值，参考ISO 21496-1。float baselineOffset[3]基础图的偏移，参考ISO 21496-1。float alternateOffset[3]提取的可选择图像偏移量，参考ISO 21496-1。