# OH_PackingOptions

```ets
typedef struct OH_PackingOptions OH_PackingOptions
```

#### 概述

OH_PackingOptions是native层封装的图像编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

创建PackingOptions结构体的对象使用[OH_PackingOptions_Create](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptions_create)函数。

释放OH_PackingOptions对象使用[OH_PackingOptions_Release](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptions_release)函数。

OH_PackingOptions结构体内容和操作方式如下：

字段类型字段名称字段描述操作函数函数描述Image_MimeTypemimeTypeMIME类型[OH_PackingOptions_GetMimeType](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptions_getmimetype)获取MIME类型。Image_MimeTypemimeTypeMIME类型[OH_PackingOptions_SetMimeType](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptions_setmimetype)设置MIME类型。uint32_tquality编码质量[OH_PackingOptions_GetQuality](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptions_getquality)获取编码质量。uint32_tquality编码质量[OH_PackingOptions_SetQuality](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptions_setquality)设置编码质量。int32_tdesiredDynamicRange图片动态范围[OH_PackingOptions_GetDesiredDynamicRange](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptions_getdesireddynamicrange)获取编码时期望的图片动态范围。int32_tdesiredDynamicRange图片动态范围[OH_PackingOptions_SetDesiredDynamicRange](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptions_setdesireddynamicrange)设置编码时期望的图片动态范围。

**起始版本：** 12

**相关模块：**[Image_NativeModule](../graphics/Image_NativeModule.md)

**所在头文件：**[image_packer_native.h](../../capi/headers/image_packer_native.h.md)