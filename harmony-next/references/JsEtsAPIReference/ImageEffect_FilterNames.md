# ImageEffect_FilterNames

```ets
typedef struct ImageEffect_FilterDelegate {...} ImageEffect_FilterNames
```

#### 概述

滤镜名信息。

**起始版本：** 12

**相关模块：**[ImageEffect](ImageEffect.md)

**所在头文件：**[image_effect_filter.h](image_effect_filter.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t size = 0滤镜名个数。const char** nameList = nullptr滤镜名列表。

#### 成员函数

名称typedef关键字描述[OH_EffectFilterInfo *OH_EffectFilterInfo_Create()](#ZH-CN_TOPIC_0000002497605890__oh_effectfilterinfo_create)OH_EffectFilterInfo_Create()

创建OH_EffectFilterInfo实例，调用[OH_EffectFilterInfo_Release](ImageEffect_FilterNames.md#ZH-CN_TOPIC_0000002497605890__oh_effectfilterinfo_release)进行资源释放。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

[ImageEffect_ErrorCode OH_EffectFilterInfo_SetFilterName(OH_EffectFilterInfo *info, const char *name)](#ZH-CN_TOPIC_0000002497605890__oh_effectfilterinfo_setfiltername)OH_EffectFilterInfo_SetFilterName()

设置滤镜名。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

[ImageEffect_ErrorCode OH_EffectFilterInfo_GetFilterName(OH_EffectFilterInfo *info, char **name)](#ZH-CN_TOPIC_0000002497605890__oh_effectfilterinfo_getfiltername)OH_EffectFilterInfo_GetFilterName()

获取滤镜名。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

[ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t size,ImageEffect_BufferType *bufferTypeArray)](#ZH-CN_TOPIC_0000002497605890__oh_effectfilterinfo_setsupportedbuffertypes)OH_EffectFilterInfo_SetSupportedBufferTypes()

设置滤镜所支持的内存类型。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

[ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t *size,ImageEffect_BufferType **bufferTypeArray)](#ZH-CN_TOPIC_0000002497605890__oh_effectfilterinfo_getsupportedbuffertypes)OH_EffectFilterInfo_GetSupportedBufferTypes()

获取滤镜所支持的内存类型。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

[ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedFormats(OH_EffectFilterInfo *info, uint32_t size,ImageEffect_Format *formatArray)](#ZH-CN_TOPIC_0000002497605890__oh_effectfilterinfo_setsupportedformats)OH_EffectFilterInfo_SetSupportedFormats()

设置滤镜所支持的像素格式。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

[ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedFormats(OH_EffectFilterInfo *info, uint32_t *size,ImageEffect_Format **formatArray)](#ZH-CN_TOPIC_0000002497605890__oh_effectfilterinfo_getsupportedformats)OH_EffectFilterInfo_GetSupportedFormats()

获取滤镜所支持的像素格式。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

[ImageEffect_ErrorCode OH_EffectFilterInfo_Release(OH_EffectFilterInfo *info)](#ZH-CN_TOPIC_0000002497605890__oh_effectfilterinfo_release)OH_EffectFilterInfo_Release()

销毁OH_EffectFilterInfo实例。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

#### 成员函数说明

#### OH_EffectFilterInfo_Create()

```ets
OH_EffectFilterInfo *OH_EffectFilterInfo_Create()
```

**描述**

创建OH_EffectFilterInfo实例，调用[OH_EffectFilterInfo_Release](ImageEffect_FilterNames.md#ZH-CN_TOPIC_0000002497605890__oh_effectfilterinfo_release)进行资源释放。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**返回：**

类型说明[OH_EffectFilterInfo](OH_EffectFilterInfo.md)返回一个指向OH_EffectFilterInfo实例的指针，创建失败时返回空指针。

#### OH_EffectFilterInfo_SetFilterName()

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_SetFilterName(OH_EffectFilterInfo *info, const char *name)
```

**描述**

设置滤镜名。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

参数项描述[OH_EffectFilterInfo](OH_EffectFilterInfo.md) *info滤镜信息指针。const char *name滤镜名，例如：OH_EFFECT_BRIGHTNESS_FILTER。

**返回：**

类型说明[ImageEffect_ErrorCode](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)

[EFFECT_SUCCESS](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果方法调用成功。

[EFFECT_ERROR_PARAM_INVALID](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果入参为空指针。

#### OH_EffectFilterInfo_GetFilterName()

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_GetFilterName(OH_EffectFilterInfo *info, char **name)
```

**描述**

获取滤镜名。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

参数项描述[OH_EffectFilterInfo](OH_EffectFilterInfo.md) *info滤镜信息指针。char **name指向char数组的指针，返回滤镜名。

**返回：**

类型说明[ImageEffect_ErrorCode](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)

[EFFECT_SUCCESS](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果方法调用成功。

[EFFECT_ERROR_PARAM_INVALID](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果入参为空指针。

#### OH_EffectFilterInfo_SetSupportedBufferTypes()

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t size,ImageEffect_BufferType *bufferTypeArray)
```

**描述**

设置滤镜所支持的内存类型。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

参数项描述[OH_EffectFilterInfo](OH_EffectFilterInfo.md) *info滤镜信息指针。uint32_t size滤镜所支持内存类型[ImageEffect_BufferType](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_buffertype)个数。ImageEffect_BufferType *bufferTypeArray滤镜所支持内存类型[ImageEffect_BufferType](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_buffertype)数组。

**返回：**

类型说明[ImageEffect_ErrorCode](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)

[EFFECT_SUCCESS](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果方法调用成功。

[EFFECT_ERROR_PARAM_INVALID](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果入参为空指针。

#### OH_EffectFilterInfo_GetSupportedBufferTypes()

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedBufferTypes(OH_EffectFilterInfo *info, uint32_t *size,ImageEffect_BufferType **bufferTypeArray)
```

**描述**

获取滤镜所支持的内存类型。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

参数项描述[OH_EffectFilterInfo](OH_EffectFilterInfo.md) *info滤镜信息指针。uint32_t *size滤镜所支持内存类型[ImageEffect_BufferType](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_buffertype)个数。ImageEffect_BufferType **bufferTypeArray滤镜所支持内存类型[ImageEffect_BufferType](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_buffertype)数组。

**返回：**

类型说明[ImageEffect_ErrorCode](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)

[EFFECT_SUCCESS](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果方法调用成功。

[EFFECT_ERROR_PARAM_INVALID](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果入参为空指针。

#### OH_EffectFilterInfo_SetSupportedFormats()

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_SetSupportedFormats(OH_EffectFilterInfo *info, uint32_t size,ImageEffect_Format *formatArray)
```

**描述**

设置滤镜所支持的像素格式。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

参数项描述[OH_EffectFilterInfo](OH_EffectFilterInfo.md) *info滤镜信息指针。uint32_t size滤镜所支持像素格式[ImageEffect_Format](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_format)个数。ImageEffect_Format *formatArray滤镜所支持像素格式[ImageEffect_Format](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_format)数组。

**返回：**

类型说明[ImageEffect_ErrorCode](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)

[EFFECT_SUCCESS](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果方法调用成功。

[EFFECT_ERROR_PARAM_INVALID](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果入参为空指针。

#### OH_EffectFilterInfo_GetSupportedFormats()

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_GetSupportedFormats(OH_EffectFilterInfo *info, uint32_t *size,ImageEffect_Format **formatArray)
```

**描述**

获取滤镜所支持的像素格式。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

参数项描述[OH_EffectFilterInfo](OH_EffectFilterInfo.md) *info滤镜信息指针。uint32_t *size滤镜所支持像素格式[ImageEffect_Format](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_format)个数。ImageEffect_Format **formatArray滤镜所支持像素格式[ImageEffect_Format](image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__imageeffect_format)数组。

**返回：**

类型说明[ImageEffect_ErrorCode](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)

[EFFECT_SUCCESS](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果方法调用成功。

[EFFECT_ERROR_PARAM_INVALID](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果入参为空指针。

#### OH_EffectFilterInfo_Release()

```ets
ImageEffect_ErrorCode OH_EffectFilterInfo_Release(OH_EffectFilterInfo *info)
```

**描述**

销毁OH_EffectFilterInfo实例。

**系统能力：** SystemCapability.Multimedia.ImageEffect.Core

**起始版本：** 12

**参数：**

参数项描述[OH_EffectFilterInfo](OH_EffectFilterInfo.md) *info滤镜信息指针。

**返回：**

类型说明[ImageEffect_ErrorCode](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)

[EFFECT_SUCCESS](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果方法调用成功。

[EFFECT_ERROR_PARAM_INVALID](image_effect_errors.h.md#ZH-CN_TOPIC_0000002497605860__imageeffect_errorcode)如果入参为空指针。