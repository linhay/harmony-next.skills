# ImageEffect_FilterNames

```ets
typedef struct ImageEffect_FilterDelegate {...} ImageEffect_FilterNames
```

**概述**

滤镜名信息。

起始版本： 12

相关模块： [ImageEffect](ImageEffect.md)

所在头文件： [image_effect_filter.h](image_effect_filter.h.md)

**汇总**

**成员变量**

支持C++语言语法的声明如下：

| 名称 | 描述 |
| --- | --- |
| uint32_t size = 0 | 滤镜名个数。 |
| const char **nameList = nullptr | 滤镜名列表。 |

支持C语言语法的声明如下：

| 名称 | 描述 |
| --- | --- |
| uint32_t size | 滤镜名个数。 |
| const char **nameList | 滤镜名列表。 |

**成员函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_EffectFilterInfo *OH_EffectFilterInfo_Create() | OH_EffectFilterInfo_Create() | 创建OH_EffectFilterInfo实例，调用OH_EffectFilterInfo_Release进行资源释放。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| ImageEffect_ErrorCode OH_EffectFilterInfo_SetFilterName(OH_EffectFilterInfo *info, const char *name) | OH_EffectFilterInfo_SetFilterName() | 设置滤镜名。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| ImageEffect_ErrorCode OH_EffectFilterInfo_GetFilterName(OH_EffectFilterInfo *info, char **name) | OH_EffectFilterInfo_GetFilterName() | 获取滤镜名。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t size,ImageEffect_BufferType *bufferTypeArray) | OH_EffectFilterInfo_SetSupportedBufferTypes() | 设置滤镜所支持的内存类型。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t *size,ImageEffect_BufferType **bufferTypeArray) | OH_EffectFilterInfo_GetSupportedBufferTypes() | 获取滤镜所支持的内存类型。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedFormats(OH_EffectFilterInfo *info, uint32_t size,ImageEffect_Format *formatArray) | OH_EffectFilterInfo_SetSupportedFormats() | 设置滤镜所支持的像素格式。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedFormats(OH_EffectFilterInfo *info, uint32_t *size,ImageEffect_Format **formatArray) | OH_EffectFilterInfo_GetSupportedFormats() | 获取滤镜所支持的像素格式。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |
| ImageEffect_ErrorCode OH_EffectFilterInfo_Release(OH_EffectFilterInfo *info) | OH_EffectFilterInfo_Release() | 销毁OH_EffectFilterInfo实例。 起始版本： 12 系统能力： SystemCapability.Multimedia.ImageEffect.Core |

**成员函数说明**

**OH_EffectFilterInfo_Create()**

```ets
OH_EffectFilterInfo *OH_EffectFilterInfo_Create()
```

描述

创建OH_EffectFilterInfo实例，调用[OH_EffectFilterInfo_Release](ImageEffect_FilterNames.md#ZH-CN_TOPIC_0000002522082022__oh_effectfilterinfo_release)进行资源释放。

系统能力： SystemCapability.Multimedia.ImageEffect.Core

起始版本： 12

返回：

| 类型 | 说明 |
| --- | --- |
| OH_EffectFilterInfo | 返回一个指向OH_EffectFilterInfo实例的指针，创建失败时返回空指针。 |

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
| ImageEffect_ErrorCode | EFFECT_SUCCESS如果方法调用成功。  EFFECT_ERROR_PARAM_INVALID如果入参为空指针。 |

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
| ImageEffect_ErrorCode | EFFECT_SUCCESS如果方法调用成功。  EFFECT_ERROR_PARAM_INVALID如果入参为空指针。 |

**OH_EffectFilterInfo_SetSupportedBufferTypes()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t size,ImageEffect_BufferType *bufferTypeArray)
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
| ImageEffect_ErrorCode | EFFECT_SUCCESS如果方法调用成功。  EFFECT_ERROR_PARAM_INVALID如果入参为空指针。 |

**OH_EffectFilterInfo_GetSupportedBufferTypes()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t *size,ImageEffect_BufferType **bufferTypeArray)
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
| ImageEffect_ErrorCode | EFFECT_SUCCESS如果方法调用成功。  EFFECT_ERROR_PARAM_INVALID如果入参为空指针。 |

**OH_EffectFilterInfo_SetSupportedFormats()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedFormats(OH_EffectFilterInfo *info, uint32_t size,ImageEffect_Format *formatArray)
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
| ImageEffect_ErrorCode | EFFECT_SUCCESS如果方法调用成功。  EFFECT_ERROR_PARAM_INVALID如果入参为空指针。 |

**OH_EffectFilterInfo_GetSupportedFormats()**

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedFormats(OH_EffectFilterInfo *info, uint32_t *size,ImageEffect_Format **formatArray)
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
| ImageEffect_ErrorCode | EFFECT_SUCCESS如果方法调用成功。  EFFECT_ERROR_PARAM_INVALID如果入参为空指针。 |

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
| ImageEffect_ErrorCode | EFFECT_SUCCESS如果方法调用成功。  EFFECT_ERROR_PARAM_INVALID如果入参为空指针。 |