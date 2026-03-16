[]()[]()

# OH_PixelmapNative

```ets
struct OH_PixelmapNative
```

[]()[]()

#### 概述

OH_PixelmapNative结构体是native层封装的图像解码后无压缩的位图格式结构体。

函数创建OH_PixelmapNative使用[OH_PixelmapNative_CreatePixelmap](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createpixelmap)函数，默认采用BGRA_8888格式处理数据。

释放OH_PixelmapNative对象使用[OH_PixelmapNative_Release](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_release)函数。

OH_PixelmapNative结构体内容和操作方式如下：

字段类型字段名称字段描述操作函数函数描述uint8_tdata图像像素数据[OH_PixelmapNative_ReadPixels](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_readpixels)读取图像像素数据，结果写入ArrayBuffer里。uint8_tdata图像像素数据[OH_PixelmapNative_WritePixels](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_writepixels)读取缓冲区中的图片数据，结果写入PixelMap中。OH_Pixelmap_ImageInfoimageInfo图像像素信息[OH_PixelmapNative_GetImageInfo](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getimageinfo)获取图像像素信息。floatalphaRate透明度[OH_PixelmapNative_Opacity](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_opacity)通过设置透明比率来让PixelMap达到对应的透明效果。float, float,scaleX, scaleYscaleX沿X轴缩放比例、scaleY沿Y轴缩放比例[OH_PixelmapNative_Scale](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_scale)根据输入的宽高对图片进行缩放。float, floatx, yx平移量、y平移量[OH_PixelmapNative_Translate](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_translate)根据输入的坐标对图片进行位置变换。floatangle旋转角度[OH_PixelmapNative_Rotate](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_rotate)根据输入的角度对图片进行旋转。bool, boolshouldFilpHorizontally, shouldFilpVertically是否水平翻转、是否垂直翻转[OH_PixelmapNative_Flip](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_flip)根据输入的条件对图片进行翻转。Image_Regionregion裁剪区间[OH_PixelmapNative_Crop](../../capi/headers/pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_crop)根据输入的尺寸对图片进行裁剪。

**起始版本：** 12

**相关模块：**[Image_NativeModule](Image_NativeModule.md)

**所在头文件：**[pixelmap_native.h](../../capi/headers/pixelmap_native.h.md)