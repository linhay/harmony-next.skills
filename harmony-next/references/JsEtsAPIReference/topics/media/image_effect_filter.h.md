# image_effect_filter.h

**概述**

声明滤镜相关接口。

 开发者可以通过滤镜的接口快速实现基本的效果处理，也可以将滤镜添加到效果器中，组合成滤镜链串联执行。系统提供了如“亮度”、“裁剪”等基本的效果处理滤镜。

引用文件： <multimedia/image_effect/image_effect_filter.h>

库： libimage_effect.so

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

相关模块： [ImageEffect](ImageEffect.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ImageEffect_DataValue | ImageEffect_DataValue | 数据值联合体。 |
| ImageEffect_Any | ImageEffect_Any | 参数结构体。 |
| ImageEffect_FilterNames | ImageEffect_FilterNames | 滤镜名信息。 |
| ImageEffect_FilterDelegate | ImageEffect_FilterDelegate | 自定义滤镜回调函数结构体。 |
| ImageEffect_Region | ImageEffect_Region | 图像区域结构体。 |
| ImageEffect_Size | ImageEffect_Size | 图像尺寸结构体。 |
| OH_EffectFilter | OH_EffectFilter | 定义滤镜结构类型。 |
| OH_EffectFilterInfo | OH_EffectFilterInfo | 定义滤镜信息结构体。 |
| OH_EffectBufferInfo | OH_EffectBufferInfo | 定义图像信息。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ImageEffect_DataType | ImageEffect_DataType | 数据类型枚举值。 |
| ImageEffect_Format | ImageEffect_Format | 像素格式枚举值。 |
| ImageEffect_BufferType | ImageEffect_BufferType | 内存类型枚举值。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| OH_EFFECT_BRIGHTNESS_FILTER "Brightness" | 亮度滤镜，对应的参数为OH_EFFECT_FILTER_INTENSITY_KEY，参数类型为EFFECT_DATA_TYPE_FLOAT。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| OH_EFFECT_CONTRAST_FILTER "Contrast" | 对比度滤镜，对应的参数为OH_EFFECT_FILTER_INTENSITY_KEY，参数类型为EFFECT_DATA_TYPE_FLOAT。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| OH_EFFECT_CROP_FILTER "Crop" | 裁剪滤镜，对应的参数为OH_EFFECT_FILTER_REGION_KEY，参数类型为EFFECT_DATA_TYPE_PTR，参数值为结构体 ImageEffect_Region。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| OH_EFFECT_FILTER_INTENSITY_KEY "FilterIntensity" | 强度参数。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| OH_EFFECT_FILTER_REGION_KEY "FilterRegion" | 图像区域参数。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_EffectFilterInfo *OH_EffectFilterInfo_Create() | - | 创建OH_EffectFilterInfo实例，调用OH_EffectFilterInfo_Release进行资源释放。 |
| ImageEffect_ErrorCode OH_EffectFilterInfo_SetFilterName(OH_EffectFilterInfo *info, const char *name) | - | 设置滤镜名。 |
| ImageEffect_ErrorCode OH_EffectFilterInfo_GetFilterName(OH_EffectFilterInfo *info, char **name) | - | 获取滤镜名。 |
| ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t size, ImageEffect_BufferType *bufferTypeArray) | - | 设置滤镜所支持的内存类型。 |
| ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t *size, ImageEffect_BufferType **bufferTypeArray) | - | 获取滤镜所支持的内存类型。 |
| ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedFormats(OH_EffectFilterInfo *info, uint32_t size, ImageEffect_Format *formatArray) | - | 设置滤镜所支持的像素格式。 |
| ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedFormats(OH_EffectFilterInfo *info, uint32_t *size, ImageEffect_Format **formatArray) | - | 获取滤镜所支持的像素格式。 |
| ImageEffect_ErrorCode OH_EffectFilterInfo_Release(OH_EffectFilterInfo *info) | - | 销毁OH_EffectFilterInfo实例。 |
| OH_EffectBufferInfo *OH_EffectBufferInfo_Create() | - | 创建OH_EffectBufferInfo实例，调用OH_EffectBufferInfo_Release进行资源释放。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_SetAddr(OH_EffectBufferInfo *info, void *addr) | - | 设置图像内存地址。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_GetAddr(OH_EffectBufferInfo *info, void **addr) | - | 获取图像内存地址。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_SetWidth(OH_EffectBufferInfo *info, int32_t width) | - | 设置图像宽度。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_GetWidth(OH_EffectBufferInfo *info, int32_t *width) | - | 获取图像宽度。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_SetHeight(OH_EffectBufferInfo *info, int32_t height) | - | 设置图像高度。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_GetHeight(OH_EffectBufferInfo *info, int32_t *height) | - | 获取图像高度。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_SetRowSize(OH_EffectBufferInfo *info, int32_t rowSize) | - | 设置图像每一行的字节数。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_GetRowSize(OH_EffectBufferInfo *info, int32_t *rowSize) | - | 获取图像每一行的字节数。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_SetEffectFormat(OH_EffectBufferInfo *info, ImageEffect_Format format) | - | 设置图像的像素格式。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_GetEffectFormat(OH_EffectBufferInfo *info, ImageEffect_Format *format) | - | 获取图像的像素格式。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_SetTextureId(OH_EffectBufferInfo *info, int32_t textureId) | - | 设置OH_EffectBufferInfo的图像的textureId。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_GetTextureId(OH_EffectBufferInfo *info, int32_t *textureId) | - | 从OH_EffectBufferInfo中获取图像的textureId。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_Release(OH_EffectBufferInfo *info) | - | 销毁OH_EffectBufferInfo实例。 |
| typedef bool (*OH_EffectFilterDelegate_SetValue)(OH_EffectFilter *filter, const char *key, const ImageEffect_Any *value) | OH_EffectFilterDelegate_SetValue | 自定义滤镜设置参数的回调函数，用于开发者校验参数及参数值。 |
| typedef void (*OH_EffectFilterDelegate_PushData)(OH_EffectFilter *filter, OH_EffectBufferInfo *info) | OH_EffectFilterDelegate_PushData | 自定义滤镜传递图像信息到下一级滤镜的函数指针。需要在OH_EffectFilterDelegate_Render的回调中主动调用该函数指针。 |
| typedef bool (*OH_EffectFilterDelegate_Render)(OH_EffectFilter *filter, OH_EffectBufferInfo *info, OH_EffectFilterDelegate_PushData pushData) | OH_EffectFilterDelegate_Render | 自定义滤镜渲染图像的回调函数。 |
| typedef bool (*OH_EffectFilterDelegate_Save)(OH_EffectFilter *filter, char **info) | OH_EffectFilterDelegate_Save | 自定义滤镜序列化的回调函数，按照JSON格式进行滤镜序列化处理。 |
| typedef OH_EffectFilter *(*OH_EffectFilterDelegate_Restore)(const char *info) | OH_EffectFilterDelegate_Restore | 自定义滤镜反序列化的回调函数。 |
| OH_EffectFilter *OH_EffectFilter_Create(const char *name) | - | 创建OH_EffectFilter实例，调用OH_EffectFilter_Release进行资源释放。 |
| ImageEffect_ErrorCode OH_EffectFilter_SetValue(OH_EffectFilter *filter, const char *key, const ImageEffect_Any *value) | - | 设置滤镜参数。 |
| ImageEffect_ErrorCode OH_EffectFilter_GetValue(OH_EffectFilter *filter, const char *key, ImageEffect_Any *value) | - | 获取滤镜参数。 |
| ImageEffect_ErrorCode OH_EffectFilter_Register(const OH_EffectFilterInfo *info, const ImageEffect_FilterDelegate *delegate) | - | 注册自定义滤镜。 |
| ImageEffect_FilterNames *OH_EffectFilter_LookupFilters(const char *key) | - | 查询满足条件的滤镜。 |
| void OH_EffectFilter_ReleaseFilterNames() | - | 释放滤镜名内存资源。 |
| ImageEffect_ErrorCode OH_EffectFilter_LookupFilterInfo(const char *name, OH_EffectFilterInfo *info) | - | 查询滤镜信息。 |
| ImageEffect_ErrorCode OH_EffectFilter_Render(OH_EffectFilter *filter, OH_PixelmapNative *inputPixelmap, OH_PixelmapNative *outputPixelmap) | - | 执行图像渲染。 |
| ImageEffect_ErrorCode OH_EffectFilter_RenderWithTextureId(OH_EffectFilter *filter, int32_t inputTextureId, int32_t outputTextureId, int32_t colorSpace) | - | 使用纹理标识渲染滤镜效果。该函数不支持相同的输入和输出图像。 |
| ImageEffect_ErrorCode OH_EffectFilter_Release(OH_EffectFilter *filter) | - | 销毁OH_EffectFilter实例。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_SetTimestamp(OH_EffectBufferInfo *info, int64_t timestamp) | - | 设置滤镜时间戳。 |
| ImageEffect_ErrorCode OH_EffectBufferInfo_GetTimestamp(OH_EffectBufferInfo *info, int64_t *timestamp) | - | 获取滤镜时间戳。 |

**枚举类型说明**

**ImageEffect_DataType**

```ets
enum ImageEffect_DataType
```

描述

数据类型枚举值。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| EFFECT_DATA_TYPE_UNKNOWN = 0 | 未定义类型。 |
| EFFECT_DATA_TYPE_INT32 = 1 | 整形。 |
| EFFECT_DATA_TYPE_FLOAT = 2 | 单精度浮点型。 |
| EFFECT_DATA_TYPE_DOUBLE = 3 | 双精度浮点型。 |
| EFFECT_DATA_TYPE_CHAR = 4 | 字节类型。 |
| EFFECT_DATA_TYPE_LONG = 5 | 长整型。 |
| EFFECT_DATA_TYPE_BOOL = 6 | 布尔类型。 |
| EFFECT_DATA_TYPE_PTR = 7 | 指针类型。 |

**ImageEffect_Format**

```ets
enum ImageEffect_Format
```

描述

像素格式枚举值。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| EFFECT_PIXEL_FORMAT_UNKNOWN = 0 | 未定义类型。 |
| EFFECT_PIXEL_FORMAT_RGBA8888 = 1 | RGBA8888类型。 |
| EFFECT_PIXEL_FORMAT_NV21 = 2 | NV21类型。 |
| EFFECT_PIXEL_FORMAT_NV12 = 3 | NV12类型。 |
| EFFECT_PIXEL_FORMAT_RGBA1010102 = 4 | 10bit RGBA类型。 |
| EFFECT_PIXEL_FORMAT_YCBCR_P010 = 5 | 10bit YCBCR420类型。 |
| EFFECT_PIXEL_FORMAT_YCRCB_P010 = 6 | 10bit YCRCB420类型。 |

**ImageEffect_BufferType**

```ets
enum ImageEffect_BufferType
```

描述

内存类型枚举值。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| EFFECT_BUFFER_TYPE_UNKNOWN = 0 | 未定义类型。 |
| EFFECT_BUFFER_TYPE_PIXEL = 1 | 像素图类型。 |
| EFFECT_BUFFER_TYPE_TEXTURE = 2 | 纹理类型。 |

**函数说明**

**OH_EffectFilterInfo_Create()**

```ets
OH_EffectFilterInfo *OH_EffectFilterInfo_Create()
```

描述

创建OH_EffectFilterInfo实例，调用[OH_EffectFilterInfo_Release](#ZH-CN_TOPIC_0000002522081992__oh_effectfilterinfo_release)进行资源释放。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| OH_EffectFilterInfo * | 返回一个指向OH_EffectFilterInfo实例的指针，创建失败时返回空指针。 |

**OH_EffectFilterInfo_SetFilterName()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_SetFilterName(OH_EffectFilterInfo *info, const char *name)
```

描述

设置滤镜名。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilterInfo *info | 滤镜信息指针。 |
| const char *name | 滤镜名，例如：OH_EFFECT_BRIGHTNESS_FILTER。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectFilterInfo_GetFilterName()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_GetFilterName(OH_EffectFilterInfo *info, char **name)
```

描述

获取滤镜名。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilterInfo *info | 滤镜信息指针。 |
| char **name | 指向char数组的指针，返回滤镜名。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectFilterInfo_SetSupportedBufferTypes()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t size, ImageEffect_BufferType *bufferTypeArray)
```

描述

设置滤镜所支持的内存类型。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilterInfo *info | 滤镜信息指针。 |
| uint32_t size | 滤镜所支持内存类型ImageEffect_BufferType个数。 |
| ImageEffect_BufferType *bufferTypeArray | 滤镜所支持内存类型ImageEffect_BufferType数组。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectFilterInfo_GetSupportedBufferTypes()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t *size, ImageEffect_BufferType **bufferTypeArray)
```

描述

获取滤镜所支持的内存类型。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilterInfo *info | 滤镜信息指针。 |
| uint32_t *size | 滤镜所支持内存类型ImageEffect_BufferType个数。 |
| ImageEffect_BufferType **bufferTypeArray | 滤镜所支持内存类型ImageEffect_BufferType数组。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectFilterInfo_SetSupportedFormats()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedFormats(OH_EffectFilterInfo *info, uint32_t size, ImageEffect_Format *formatArray)
```

描述

设置滤镜所支持的像素格式。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilterInfo *info | 滤镜信息指针。 |
| uint32_t size | 滤镜所支持像素格式ImageEffect_Format个数。 |
| ImageEffect_Format *formatArray | 滤镜所支持像素格式ImageEffect_Format数组。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectFilterInfo_GetSupportedFormats()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedFormats(OH_EffectFilterInfo *info, uint32_t *size, ImageEffect_Format **formatArray)
```

描述

获取滤镜所支持的像素格式。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilterInfo *info | 滤镜信息指针。 |
| uint32_t *size | 滤镜所支持像素格式ImageEffect_Format个数。 |
| ImageEffect_Format **formatArray | 滤镜所支持像素格式ImageEffect_Format数组。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectFilterInfo_Release()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_Release(OH_EffectFilterInfo *info)
```

描述

销毁OH_EffectFilterInfo实例。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilterInfo *info | 滤镜信息指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_Create()**

```ets
OH_EffectBufferInfo *OH_EffectBufferInfo_Create()
```

描述

创建OH_EffectBufferInfo实例，调用[OH_EffectBufferInfo_Release](#ZH-CN_TOPIC_0000002522081992__oh_effectbufferinfo_release)进行资源释放。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| OH_EffectBufferInfo * | 返回一个指向OH_EffectBufferInfo实例的指针，创建失败时返回空指针。 |

**OH_EffectBufferInfo_SetAddr()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_SetAddr(OH_EffectBufferInfo *info, void *addr)
```

描述

设置图像内存地址。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| void *addr | 图像虚拟内存地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_GetAddr()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_GetAddr(OH_EffectBufferInfo *info, void **addr)
```

描述

获取图像内存地址。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| void **addr | 图像虚拟内存地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_SetWidth()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_SetWidth(OH_EffectBufferInfo *info, int32_t width)
```

描述

设置图像宽度。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| int32_t width | 图像宽度，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_GetWidth()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_GetWidth(OH_EffectBufferInfo *info, int32_t *width)
```

描述

获取图像宽度。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| int32_t *width | 图像宽度，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_SetHeight()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_SetHeight(OH_EffectBufferInfo *info, int32_t height)
```

描述

设置图像高度。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| int32_t height | 图像高度，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_GetHeight()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_GetHeight(OH_EffectBufferInfo *info, int32_t *height)
```

描述

获取图像高度。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| int32_t *height | 图像高度，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_SetRowSize()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_SetRowSize(OH_EffectBufferInfo *info, int32_t rowSize)
```

描述

设置图像每一行的字节数。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| int32_t rowSize | 图像每一行的字节数，单位：字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_GetRowSize()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_GetRowSize(OH_EffectBufferInfo *info, int32_t *rowSize)
```

描述

获取图像每一行的字节数。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| int32_t *rowSize | 图像每一行的字节数，单位：字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_SetEffectFormat()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_SetEffectFormat(OH_EffectBufferInfo *info, ImageEffect_Format format)
```

描述

设置图像的像素格式。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| ImageEffect_Format format | 图像像素格式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_GetEffectFormat()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_GetEffectFormat(OH_EffectBufferInfo *info, ImageEffect_Format *format)
```

描述

获取图像的像素格式。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| ImageEffect_Format *format | 图像像素格式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_SetTextureId()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_SetTextureId(OH_EffectBufferInfo *info, int32_t textureId)
```

描述

设置OH_EffectBufferInfo的图像的textureId。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | OH_EffectBufferInfo结构体实例指针。 |
| int32_t textureId | 图像纹理标识。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：参数缺失。 |

**OH_EffectBufferInfo_GetTextureId()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_GetTextureId(OH_EffectBufferInfo *info, int32_t *textureId)
```

描述

从OH_EffectBufferInfo中获取图像的textureId。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | OH_EffectBufferInfo结构体实例指针。 |
| int32_t *textureId | 图像纹理标识。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：参数缺失。 |

**OH_EffectBufferInfo_Release()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_Release(OH_EffectBufferInfo *info)
```

描述

销毁OH_EffectBufferInfo实例。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectFilterDelegate_SetValue()**

```ets
typedef bool (*OH_EffectFilterDelegate_SetValue)(OH_EffectFilter *filter, const char *key, const ImageEffect_Any *value)
```

描述

自定义滤镜设置参数的回调函数，用于开发者校验参数及参数值。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilter *filter | 滤镜指针。 |
| const char *key | 滤镜参数。 |
| const ImageEffect_Any *value | 滤镜参数值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 参数有效时返回true，否则返回false。 |

**OH_EffectFilterDelegate_PushData()**

```ets
typedef void (*OH_EffectFilterDelegate_PushData)(OH_EffectFilter *filter, OH_EffectBufferInfo *info)
```

描述

自定义滤镜传递图像信息到下一级滤镜的函数指针。需要在[OH_EffectFilterDelegate_Render](#ZH-CN_TOPIC_0000002522081992__oh_effectfilterdelegate_render)的回调中主动调用该函数指针。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilter *filter | 滤镜指针。 |
| OH_EffectBufferInfo *info | 图像信息OH_EffectBufferInfo指针。 |

**OH_EffectFilterDelegate_Render()**

```ets
typedef bool (*OH_EffectFilterDelegate_Render)(OH_EffectFilter *filter, OH_EffectBufferInfo *info, OH_EffectFilterDelegate_PushData pushData)
```

描述

自定义滤镜渲染图像的回调函数。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilter *filter | 滤镜指针。 |
| OH_EffectBufferInfo *info | 图像信息OH_EffectBufferInfo指针。 |
| OH_EffectFilterDelegate_PushData pushData | 自定义滤镜传递图像信息到下一级滤镜的函数指针OH_EffectFilterDelegate_PushData。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 执行成功时返回true，否则返回false。 |

**OH_EffectFilterDelegate_Save()**

```ets
typedef bool (*OH_EffectFilterDelegate_Save)(OH_EffectFilter *filter, char **info)
```

描述

自定义滤镜序列化的回调函数，按照JSON格式进行滤镜序列化处理。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilter *filter | 滤镜指针。 |
| char **info | 指向char数组的指针，返回序列化JSON字符串。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 执行成功时返回true，否则返回false。 |

**OH_EffectFilterDelegate_Restore()**

```ets
typedef OH_EffectFilter *(*OH_EffectFilterDelegate_Restore)(const char *info)
```

描述

自定义滤镜反序列化的回调函数。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *info | 序列化JSON字符串。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_EffectFilter * | 执行成功时返回OH_EffectFilter实例，否则返回空指针。 |

**OH_EffectFilter_Create()**

```ets
OH_EffectFilter *OH_EffectFilter_Create(const char *name)
```

描述

创建OH_EffectFilter实例，调用[OH_EffectFilter_Release](#ZH-CN_TOPIC_0000002522081992__oh_effectfilter_release)进行资源释放。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *name | 滤镜名，例如：OH_EFFECT_BRIGHTNESS_FILTER。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_EffectFilter * | 返回一个指向OH_EffectFilter实例的指针，创建失败时返回空指针。 |

**OH_EffectFilter_SetValue()**

```ets
ImageEffect_ErrorCode OH_EffectFilter_SetValue(OH_EffectFilter *filter, const char *key, const ImageEffect_Any *value)
```

描述

设置滤镜参数。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilter *filter | 滤镜指针。 |
| const char *key | 滤镜参数，例如：OH_EFFECT_FILTER_INTENSITY_KEY。 |
| const ImageEffect_Any *value | 滤镜参数值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。  EFFECT_KEY_ERROR：参数无效。  EFFECT_PARAM_ERROR：参数值无效。 |

**OH_EffectFilter_GetValue()**

```ets
ImageEffect_ErrorCode OH_EffectFilter_GetValue(OH_EffectFilter *filter, const char *key, ImageEffect_Any *value)
```

描述

获取滤镜参数。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilter *filter | 滤镜指针。 |
| const char *key | 滤镜参数，例如：OH_EFFECT_FILTER_INTENSITY_KEY。 |
| ImageEffect_Any *value | 滤镜参数值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。  EFFECT_KEY_ERROR：参数无效。 |

**OH_EffectFilter_Register()**

```ets
ImageEffect_ErrorCode OH_EffectFilter_Register(const OH_EffectFilterInfo *info, const ImageEffect_FilterDelegate *delegate)
```

描述

注册自定义滤镜。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_EffectFilterInfo *info | 滤镜信息指针OH_EffectFilterInfo。 |
| const ImageEffect_FilterDelegate *delegate | 自定义滤镜回调函数ImageEffect_FilterDelegate。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectFilter_LookupFilters()**

```ets
ImageEffect_FilterNames *OH_EffectFilter_LookupFilters(const char *key)
```

描述

查询满足条件的滤镜。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *key | 查询条件，可根据“Default”关键词查询所有的滤镜。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_FilterNames * | 滤镜名列表。 |

**OH_EffectFilter_ReleaseFilterNames()**

```ets
void OH_EffectFilter_ReleaseFilterNames()
```

描述

释放滤镜名内存资源。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

**OH_EffectFilter_LookupFilterInfo()**

```ets
ImageEffect_ErrorCode OH_EffectFilter_LookupFilterInfo(const char *name, OH_EffectFilterInfo *info)
```

描述

查询滤镜信息。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *name | 滤镜名。 |
| OH_EffectFilterInfo *info | 滤镜信息指针OH_EffectFilterInfo。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针或其他无效值。 |

**OH_EffectFilter_Render()**

```ets
ImageEffect_ErrorCode OH_EffectFilter_Render(OH_EffectFilter *filter, OH_PixelmapNative *inputPixelmap, OH_PixelmapNative *outputPixelmap)
```

描述

执行图像渲染。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilter *filter | 滤镜指针。 |
| OH_PixelmapNative *inputPixelmap | 输入图像。 |
| OH_PixelmapNative *outputPixelmap | 输出图像。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectFilter_RenderWithTextureId()**

```ets
ImageEffect_ErrorCode OH_EffectFilter_RenderWithTextureId(OH_EffectFilter *filter, int32_t inputTextureId, int32_t outputTextureId, int32_t colorSpace)
```

描述

使用纹理标识渲染滤镜效果。该函数不支持相同的输入和输出图像。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilter *filter | OH_EffectFilter结构体实例指针。 |
| int32_t inputTextureId | 输入纹理标识。输入的纹理标识必须是有效的且绑定了GL_TEXTURE_2D类型的纹理。 |
| int32_t outputTextureId | 输出纹理标识，输入纹理标识必须是一个有效的纹理。  如果纹理标识未被绑定纹理图片，纹理标识会自动绑定GL_TEXTURE_2D类型；  如果纹理标识已经被绑定纹理且尺寸不合适，结果可能会被裁剪或部分填充到此纹理上。 |
| int32_t colorSpace | 图片对应的色彩空间。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：参数缺失。 |

**OH_EffectFilter_Release()**

```ets
ImageEffect_ErrorCode OH_EffectFilter_Release(OH_EffectFilter *filter)
```

描述

销毁OH_EffectFilter实例。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectFilter *filter | 滤镜指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_SetTimestamp()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_SetTimestamp(OH_EffectBufferInfo *info, int64_t timestamp)
```

描述

设置滤镜时间戳。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| int64_t timestamp | 图像帧数据的时间戳。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |

**OH_EffectBufferInfo_GetTimestamp()**

```ets
ImageEffect_ErrorCode OH_EffectBufferInfo_GetTimestamp(OH_EffectBufferInfo *info, int64_t *timestamp)
```

描述

获取滤镜时间戳。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_EffectBufferInfo *info | 图像信息指针。 |
| int64_t *timestamp | 图像帧数据的时间戳。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ImageEffect_ErrorCode | EFFECT_SUCCESS：方法调用成功。  EFFECT_ERROR_PARAM_INVALID：入参为空指针。 |