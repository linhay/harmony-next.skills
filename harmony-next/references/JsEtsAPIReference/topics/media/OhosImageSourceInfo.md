# OhosImageSourceInfo

```ets
struct OhosImageSourceInfo {...}
```

**概述**

定义图像源信息，由[OH_ImageSource_GetImageInfo](image_source_mdk.h.md#ZH-CN_TOPIC_0000002553361909__oh_imagesource_getimageinfo)获取。

起始版本： 10

相关模块： [Image](Image.md)

所在头文件： [image_source_mdk.h](image_source_mdk.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t pixelFormat | 图像源像素格式，由OH_ImageSource_CreateFromUri、OH_ImageSource_CreateFromFd和OH_ImageSource_CreateFromData设置。 |
| int32_t colorSpace | 图像源色彩空间。 |
| int32_t alphaType | 图像源透明度类型。 |
| int32_t density | 图像源密度，由OH_ImageSource_CreateFromUri、OH_ImageSource_CreateFromFd和OH_ImageSource_CreateFromData设置。 |
| struct OhosImageSize size | 图像源像素宽高的大小。 |