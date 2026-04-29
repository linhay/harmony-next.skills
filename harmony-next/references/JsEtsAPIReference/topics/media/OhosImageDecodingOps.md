# OhosImageDecodingOps

```ets
struct OhosImageDecodingOps {...}
```

**概述**

定义图像源解码选项。此选项给[OH_ImageSource_CreatePixelMap](image_source_mdk.h.md#ZH-CN_TOPIC_0000002553361909__oh_imagesource_createpixelmap)和[OH_ImageSource_CreatePixelMapList](image_source_mdk.h.md#ZH-CN_TOPIC_0000002553361909__oh_imagesource_createpixelmaplist)接口使用。

起始版本： 10

相关模块： [Image](Image.md)

所在头文件： [image_source_mdk.h](image_source_mdk.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int8_t editable | 定义输出的像素位图是否可编辑。 |
| int32_t pixelFormat | 定义输出的像素格式。 |
| int32_t fitDensity | 定义解码目标的像素密度。 |
| uint32_t index | 定义ImageSource解码序号。 |
| uint32_t sampleSize | 定义解码样本大小选项。 |
| uint32_t rotate | 定义解码旋转选项。 |
| struct OhosImageSize size | 定义解码目标像素宽高的大小。 |
| struct OhosImageRegion region | 定义ImageSource解码的像素范围。 |