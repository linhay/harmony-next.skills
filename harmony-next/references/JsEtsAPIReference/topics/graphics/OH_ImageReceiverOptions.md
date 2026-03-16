# OH_ImageReceiverOptions

```ets
typedef struct OH_ImageReceiverOptions OH_ImageReceiverOptions
```

#### 概述

用于定义OH_ImageReceiverOptions数据类型名称。

OH_ImageReceiverOptions是native层封装的图片接收器选项设置器结构体，用于创建OH_ImageReceiverNative时传入设置参数。OH_ImageReceiverOptions结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

创建OH_ImageReceiverOptions对象使用[OH_ImageReceiverOptions_Create](../../capi/headers/image_receiver_native.h.md#ZH-CN_TOPIC_0000002497605854__oh_imagereceiveroptions_create)函数。

释放OH_ImageReceiverOptions对象使用[OH_ImageReceiverOptions_Release](../../capi/headers/image_receiver_native.h.md#ZH-CN_TOPIC_0000002497605854__oh_imagereceiveroptions_release)函数。

OH_ImageReceiverOptions结构体内容和操作方式如下：

字段类型字段名称字段描述操作函数函数描述Image_Sizesize图像大小[OH_ImageReceiverOptions_GetSize](../../capi/headers/image_receiver_native.h.md#ZH-CN_TOPIC_0000002497605854__oh_imagereceiveroptions_getsize)获取OH_ImageReceiverOptions对象的Image_Size。Image_Sizesize图像大小[OH_ImageReceiverOptions_SetSize](../../capi/headers/image_receiver_native.h.md#ZH-CN_TOPIC_0000002497605854__oh_imagereceiveroptions_setsize)设置OH_ImageReceiverOptions对象的Image_Size。int32_tcapacity图片缓存容量[OH_ImageReceiverOptions_GetCapacity](../../capi/headers/image_receiver_native.h.md#ZH-CN_TOPIC_0000002497605854__oh_imagereceiveroptions_getcapacity)获取OH_ImageReceiverOptions对象的图片缓存容量。int32_tcapacity图片缓存容量[OH_ImageReceiverOptions_SetCapacity](../../capi/headers/image_receiver_native.h.md#ZH-CN_TOPIC_0000002497605854__oh_imagereceiveroptions_setcapacity)设置OH_ImageReceiverOptions对象的图片缓存容量。

**起始版本：** 12

**相关模块：**[Image_NativeModule](Image_NativeModule.md)

**所在头文件：**[image_receiver_native.h](../../capi/headers/image_receiver_native.h.md)