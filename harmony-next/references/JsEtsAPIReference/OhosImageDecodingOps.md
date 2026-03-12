# OhosImageDecodingOps

```ets
struct OhosImageDecodingOps {...}
```

#### 概述

定义图像源解码选项。此选项给[OH_ImageSource_CreatePixelMap](image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createpixelmap)和[OH_ImageSource_CreatePixelMapList](image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createpixelmaplist)接口使用。

**起始版本：** 10

**相关模块：**[Image](Image.md)

**所在头文件：**[image_source_mdk.h](image_source_mdk.h.md)

#### 汇总

#### 成员变量

名称描述int8_t editable定义输出的像素位图是否可编辑。int32_t pixelFormat定义输出的像素格式。int32_t fitDensity定义解码目标的像素密度。uint32_t index定义ImageSource解码序号。uint32_t sampleSize定义解码样本大小选项。uint32_t rotate定义解码旋转选项。struct [OhosImageSize](OhosImageSize.md) size定义解码目标像素宽高的大小。struct [OhosImageRegion](OhosImageRegion.md) region定义ImageSource解码的像素范围。