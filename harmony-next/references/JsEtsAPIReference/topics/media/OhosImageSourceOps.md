# OhosImageSourceOps

```ets
struct OhosImageSourceOps {...}
```

**概述**

定义图像源选项信息。此选项给[OH_ImageSource_CreateFromUri](image_source_mdk.h.md#ZH-CN_TOPIC_0000002553361909__oh_imagesource_createfromuri)、[OH_ImageSource_CreateFromFd](image_source_mdk.h.md#ZH-CN_TOPIC_0000002553361909__oh_imagesource_createfromfd)、[OH_ImageSource_CreateFromData](image_source_mdk.h.md#ZH-CN_TOPIC_0000002553361909__oh_imagesource_createfromdata)和[OH_ImageSource_CreateIncremental](image_source_mdk.h.md#ZH-CN_TOPIC_0000002553361909__oh_imagesource_createincremental)接口使用。

起始版本： 10

相关模块： [Image](Image.md)

所在头文件： [image_source_mdk.h](image_source_mdk.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t density | 图像源像素密度。 |
| int32_t pixelFormat | 图像源像素格式，通常用于描述YUV缓冲区。 |
| struct OhosImageSize size | 图像源像素宽高的大小。 |