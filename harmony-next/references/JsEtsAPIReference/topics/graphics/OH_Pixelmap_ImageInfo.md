# OH_Pixelmap_ImageInfo

```ets
struct OH_Pixelmap_ImageInfo
```

#### 概述

OH_Pixelmap_ImageInfo是native层封装的图像像素信息结构体，保存图像像素的宽高、行跨距、像素格式、是否是HDR。

创建OH_Pixelmap_ImageInfo对象使用[OH_PixelmapImageInfo_Create](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_create)函数。

释放OH_Pixelmap_ImageInfo对象使用[OH_PixelmapImageInfo_Release](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_release)函数。

OH_Pixelmap_ImageInfo结构体内容和操作方式如下：

字段类型字段名称字段描述操作函数函数描述uint32_twidth图片宽[OH_PixelmapImageInfo_GetWidth](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getwidth)获取图片宽。uint32_theight图片高[OH_PixelmapImageInfo_GetHeight](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getheight)获取图片高。uint32_trowStride行跨距[OH_PixelmapImageInfo_GetRowStride](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getrowstride)获取行跨距。int32_tpixelFormat像素格式[OH_PixelmapImageInfo_GetPixelFormat](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getpixelformat)获取像素格式。int32_talphaType透明度类型[OH_PixelmapImageInfo_GetAlphaType](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getalphatype)获取透明度类型。boolisHdr是否为高动态范围的信息[OH_PixelmapImageInfo_GetDynamicRange](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getdynamicrange)获取Pixelmap是否为高动态范围的信息。

**起始版本：** 12

**相关模块：**[Image_NativeModule](Image_NativeModule.md)

**所在头文件：**[pixelmap_native.h](../../capi/headers/pixelmap_native.h.md)