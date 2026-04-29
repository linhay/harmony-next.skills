# OH_PixelmapNative

```ets
struct OH_PixelmapNative
```

**概述**

OH_PixelmapNative结构体是native层封装的图像解码后无压缩的位图格式结构体。

函数创建OH_PixelmapNative使用[OH_PixelmapNative_CreatePixelmap](pixelmap_native.h.md#ZH-CN_TOPIC_0000002522241982__oh_pixelmapnative_createpixelmap)函数，默认采用BGRA_8888格式处理数据。

释放OH_PixelmapNative对象使用[OH_PixelmapNative_Release](pixelmap_native.h.md#ZH-CN_TOPIC_0000002522241982__oh_pixelmapnative_release)函数。

OH_PixelmapNative结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint8_t | data | 图像像素数据 | OH_PixelmapNative_ReadPixels | 读取图像像素数据，结果写入ArrayBuffer里。 |
| uint8_t | data | 图像像素数据 | OH_PixelmapNative_WritePixels | 读取缓冲区中的图片数据，结果写入PixelMap中。 |
| OH_Pixelmap_ImageInfo | imageInfo | 图像像素信息 | OH_PixelmapNative_GetImageInfo | 获取图像像素信息。 |
| float | alphaRate | 透明度 | OH_PixelmapNative_Opacity | 通过设置透明比率来让PixelMap达到对应的透明效果。 |
| float, float, | scaleX, scaleY | scaleX沿X轴缩放比例、scaleY沿Y轴缩放比例 | OH_PixelmapNative_Scale | 根据输入的宽高对图片进行缩放。 |
| float, float | x, y | x平移量、y平移量 | OH_PixelmapNative_Translate | 根据输入的坐标对图片进行位置变换。 |
| float | angle | 旋转角度 | OH_PixelmapNative_Rotate | 根据输入的角度对图片进行旋转。 |
| bool, bool | shouldFlipHorizontally, shouldFlipVertically | 是否水平翻转图像、是否垂直翻转图像。 | OH_PixelmapNative_Flip | 根据输入的条件对图片进行翻转。 |
| Image_Region | region | 裁剪区间 | OH_PixelmapNative_Crop | 根据输入的尺寸对图片进行裁剪。 |

起始版本： 12

相关模块： [Image_NativeModule](Image_NativeModule.md)

所在头文件： [pixelmap_native.h](pixelmap_native.h.md)