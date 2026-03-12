# OH_ImageNative

```ets
typedef struct OH_ImageNative OH_ImageNative
```

#### 概述

为图像接口定义native层图像对象的别名。

此结构体内容不可直接操作，采用函数调用方式操作具体字段，结构体内容和操作方式如下：

字段类型字段名称字段描述操作函数函数描述Image_SizeimageSize图像大小[OH_ImageNative_GetImageSize](image_native.h.md#ZH-CN_TOPIC_0000002529285843__oh_imagenative_getimagesize)获取 OH_ImageNative 对象的 Image_Size 信息。uint32_ttypes组件类型，用于描述图像颜色分量。[OH_ImageNative_GetComponentTypes](image_native.h.md#ZH-CN_TOPIC_0000002529285843__oh_imagenative_getcomponenttypes)获取 OH_ImageNative 对象的组件列表信息。OH_NativeBuffernativeBuffer组件缓冲区[OH_ImageNative_GetByteBuffer](image_native.h.md#ZH-CN_TOPIC_0000002529285843__oh_imagenative_getbytebuffer)获取 OH_ImageNative 对象中某个组件类型所对应的缓冲区。size_tbufferSize缓冲区的大小[OH_ImageNative_GetBufferSize](image_native.h.md#ZH-CN_TOPIC_0000002529285843__oh_imagenative_getbuffersize)获取 OH_ImageNative 对象中某个组件类型所对应的缓冲区的大小。int32_trowStride像素行宽[OH_ImageNative_GetRowStride](image_native.h.md#ZH-CN_TOPIC_0000002529285843__oh_imagenative_getrowstride)获取 OH_ImageNative 对象中某个组件类型所对应的像素行宽。int32_tpixelStride像素大小[OH_ImageNative_GetPixelStride](image_native.h.md#ZH-CN_TOPIC_0000002529285843__oh_imagenative_getpixelstride)获取 OH_ImageNative 对象中某个组件类型所对应的像素大小。

释放OH_ImageNative对象使用[OH_ImageNative_Release](image_native.h.md#ZH-CN_TOPIC_0000002529285843__oh_imagenative_release)函数。

**起始版本：** 12

**相关模块：**[Image_NativeModule](Image_NativeModule.md)

**所在头文件：**[image_native.h](image_native.h.md)