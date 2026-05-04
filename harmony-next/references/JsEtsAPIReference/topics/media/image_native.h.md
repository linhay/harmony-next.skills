# image_native.h

**概述**

声明图像的剪辑矩形、大小和组件数据的接口函数。

引用文件： <multimedia/image_framework/image/image_native.h>

库： libohimage.so

系统能力： SystemCapability.Multimedia.Image.Core

起始版本： 12

相关模块： [Image_NativeModule](Image_NativeModule.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_ImageBufferData | OH_ImageBufferData | OH_ImageBufferData是native层封装的图像数据结构体。 |
| OH_ImageNative | OH_ImageNative | 为图像接口定义native层图像对象的别名。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| Image_ErrorCode OH_ImageNative_GetImageSize(OH_ImageNative *image, Image_Size *size) | 获取Native OH_ImageNative对象的Image_Size信息。 |
| Image_ErrorCode OH_ImageNative_GetComponentTypes(OH_ImageNative *image, uint32_t **types, size_t *typeSize) | 获取Native OH_ImageNative对象的组件列表信息。 |
| Image_ErrorCode OH_ImageNative_GetByteBuffer(OH_ImageNative *image, uint32_t componentType, OH_NativeBuffer **nativeBuffer) | 获取Native OH_ImageNative对象中某个组件类型所对应的缓冲区。 |
| Image_ErrorCode OH_ImageNative_GetBufferSize(OH_ImageNative *image, uint32_t componentType, size_t *size) | 获取Native OH_ImageNative对象中某个组件类型所对应的缓冲区的大小。 |
| Image_ErrorCode OH_ImageNative_GetRowStride(OH_ImageNative *image, uint32_t componentType, int32_t *rowStride) | 获取Native OH_ImageNative对象中某个组件类型所对应的像素行宽。 |
| Image_ErrorCode OH_ImageNative_GetPixelStride(OH_ImageNative *image, uint32_t componentType, int32_t *pixelStride) | 获取Native OH_ImageNative对象中某个组件类型所对应的像素大小。 |
| Image_ErrorCode OH_ImageNative_GetTimestamp(OH_ImageNative *image, int64_t *timestamp) | 获取Native OH_ImageNative对象中的时间戳信息。 |
| Image_ErrorCode OH_ImageNative_Release(OH_ImageNative *image) | 释放Native OH_ImageNative对象。 |
| Image_ErrorCode OH_ImageNative_GetColorSpace(OH_ImageNative *image, int32_t *colorSpaceName) | 获取图像OH_ImageNative对象中的色彩空间。 |
| Image_ErrorCode OH_ImageNative_GetFormat(OH_ImageNative *image, OH_NativeBuffer_Format *format) | 获取图像OH_ImageNative对象中的图像格式。 |
| Image_ErrorCode OH_ImageNative_GetBufferData(OH_ImageNative *image, OH_ImageBufferData *imageBufferData) | 获取图像OH_ImageNative对象中的图像缓冲区数据对象。 |

**函数说明**

**OH_ImageNative_GetImageSize()**

```ets
Image_ErrorCode OH_ImageNative_GetImageSize(OH_ImageNative *image, Image_Size *size)
```

描述

获取Native [OH_ImageNative](OH_ImageNative.md)对象的[Image_Size](Image_Size.md)信息。

如果OH_ImageNative对象所存储的是相机预览流数据，即YUV图像数据，那么获取到的Image_Size中的宽高分别对应YUV图像的宽高；如果OH_ImageNative对象所存储的是相机拍照流数据，即JPEG图像，由于已经是编码后的数据，Image_Size中的宽等于JPEG数据大小，高等于1。

OH_ImageNative对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId传给相机的previewOutput还是captureOutput。相机预览与拍照最佳实践请参考[预览流二次处理(C/C++)](../../guides/预览流二次处理（C-C++）.md)与[拍照(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting)。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |
| Image_Size *size | 表示作为获取结果的Image_Size对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 IMAGE_UNKNOWN_ERROR：未知原因错误。 |

**OH_ImageNative_GetComponentTypes()**

```ets
Image_ErrorCode OH_ImageNative_GetComponentTypes(OH_ImageNative *image,uint32_t **types, size_t *typeSize)
```

描述

获取Native [OH_ImageNative](OH_ImageNative.md)对象的组件列表信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |
| uint32_t **types | 表示作为获取结果的组件类型列表对象的指针。由于不确定组件个数，需要调用该接口两次：第一次传入types参数为NULL，获取组件个数typeSize；第二次根据typeSize给types申请对应内存，获取组件类型列表。 |
| size_t *typeSize | 表示作为获取结果的组件列表中，元素个数的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageNative_GetByteBuffer()**

```ets
Image_ErrorCode OH_ImageNative_GetByteBuffer(OH_ImageNative *image,uint32_t componentType, OH_NativeBuffer **nativeBuffer)
```

描述

获取Native [OH_ImageNative](OH_ImageNative.md)对象中某个组件类型所对应的缓冲区。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |
| uint32_t componentType | 表示组件的类型。通过OH_ImageNative_GetComponentTypes接口获取。 |
| OH_NativeBuffer **nativeBuffer | 表示作为获取结果的OH_NativeBuffer缓冲区对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageNative_GetBufferSize()**

```ets
Image_ErrorCode OH_ImageNative_GetBufferSize(OH_ImageNative *image,uint32_t componentType, size_t *size)
```

描述

获取Native [OH_ImageNative](OH_ImageNative.md)对象中某个组件类型所对应的缓冲区的大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |
| uint32_t componentType | 表示组件的类型。通过OH_ImageNative_GetComponentTypes接口获取。 |
| size_t *size | 表示作为获取结果的缓冲区大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageNative_GetRowStride()**

```ets
Image_ErrorCode OH_ImageNative_GetRowStride(OH_ImageNative *image,uint32_t componentType, int32_t *rowStride)
```

描述

获取Native [OH_ImageNative](OH_ImageNative.md)对象中某个组件类型所对应的像素行宽。

读取相机预览流数据时，需要考虑按stride进行读取，具体用法参考[预览流二次处理(C/C++)](../../guides/预览流二次处理（C-C++）.md)。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |
| uint32_t componentType | 表示组件的类型。通过OH_ImageNative_GetComponentTypes接口获取。 |
| int32_t *rowStride | 表示作为获取结果的像素行宽的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageNative_GetPixelStride()**

```ets
Image_ErrorCode OH_ImageNative_GetPixelStride(OH_ImageNative *image,uint32_t componentType, int32_t *pixelStride)
```

描述

获取Native [OH_ImageNative](OH_ImageNative.md)对象中某个组件类型所对应的像素大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |
| uint32_t componentType | 表示组件的类型。通过OH_ImageNative_GetComponentTypes接口获取。 |
| int32_t *pixelStride | 表示作为获取结果的像素大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageNative_GetTimestamp()**

```ets
Image_ErrorCode OH_ImageNative_GetTimestamp(OH_ImageNative *image, int64_t *timestamp)
```

描述

获取Native [OH_ImageNative](OH_ImageNative.md)对象中的时间戳信息。时间戳以纳秒为单位，通常是单调递增的。

时间戳的具体含义和基准取决于图像的生产者，在相机预览/拍照场景，生产者就是相机。来自不同生产者的图像的时间戳可能有不同的含义和基准，因此可能无法进行比较。

如果要获取某张照片的生成时间，可以通过[OH_ImageSourceNative_GetImageProperty](image_source_native.h.md#ZH-CN_TOPIC_0000002522081986__oh_imagesourcenative_getimageproperty)接口读取相关的EXIF信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |
| int64_t *timestamp | 表示作为获取结果的时间戳信息的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageNative_Release()**

```ets
Image_ErrorCode OH_ImageNative_Release(OH_ImageNative *image)
```

描述

释放Native [OH_ImageNative](OH_ImageNative.md)对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageNative_GetColorSpace()**

```ets
Image_ErrorCode OH_ImageNative_GetColorSpace(OH_ImageNative *image, int32_t *colorSpaceName)
```

描述

获取图像OH_ImageNative对象中的色彩空间。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |
| int32_t *colorSpaceName | 表示图像色彩空间的指针，colorSpaceName的对应色彩空间请参考ColorSpaceName。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageNative_GetFormat()**

```ets
Image_ErrorCode OH_ImageNative_GetFormat(OH_ImageNative *image, OH_NativeBuffer_Format *format)
```

描述

获取图像OH_ImageNative对象中的图像格式。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |
| OH_NativeBuffer_Format *format | 表示图像格式的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageNative_GetBufferData()**

```ets
Image_ErrorCode OH_ImageNative_GetBufferData(OH_ImageNative *image, OH_ImageBufferData *imageBufferData)
```

描述

获取图像OH_ImageNative对象中的图像缓冲区数据对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageNative *image | 表示OH_ImageNative native对象的指针。 |
| OH_ImageBufferData *imageBufferData | 表示图像缓冲区数据对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |