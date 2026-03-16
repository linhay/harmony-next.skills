# OhosImageSourceInfo

```ets
struct OhosImageSourceInfo {...}
```

#### 概述

定义图像源信息，由[OH_ImageSource_GetImageInfo](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_getimageinfo)获取。

**起始版本：** 10

**相关模块：**[Image](Image.md)

**所在头文件：**[image_source_mdk.h](../../capi/headers/image_source_mdk.h.md)

#### 汇总

#### 成员变量

名称描述int32_t pixelFormat图像源像素格式，由[OH_ImageSource_CreateFromUri](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createfromuri)、[OH_ImageSource_CreateFromFd](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createfromfd)和[OH_ImageSource_CreateFromData](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createfromdata)设置。int32_t colorSpace图像源色彩空间。int32_t alphaType图像源透明度类型。int32_t density图像源密度，由[OH_ImageSource_CreateFromUri](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createfromuri)、[OH_ImageSource_CreateFromFd](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createfromfd)和[OH_ImageSource_CreateFromData](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createfromdata)设置。struct [OhosImageSize](OhosImageSize.md) size图像源像素宽高的大小。