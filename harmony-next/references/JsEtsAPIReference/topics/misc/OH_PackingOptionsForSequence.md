# OH_PackingOptionsForSequence

```ets
typedef struct OH_PackingOptionsForSequence OH_PackingOptionsForSequence
```

#### 概述

OH_PackingOptionsForSequence是native层封装的图像序列编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

创建OH_PackingOptionsForSequence结构体的对象使用[OH_PackingOptionsForSequence_Create](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptionsforsequence_create)函数。

释放OH_PackingOptionsForSequence对象使用[OH_PackingOptionsForSequence_Release](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptionsforsequence_release)函数。

字段类型字段名称字段描述操作函数函数描述uint32_tframeCount帧数[OH_PackingOptionsForSequence_GetFrameCount](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptionsforsequence_getframecount)获取编码时指定的帧数。uint32_tframeCount帧数[OH_PackingOptionsForSequence_SetFrameCount](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptionsforsequence_setframecount)设置编码时指定的帧数。int32_t *delayTimeList延迟时间数组[OH_PackingOptionsForSequence_GetDelayTimeList](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptionsforsequence_getdelaytimelist)获取编码时图片的延迟时间数组。int32_t *delayTimeList延迟时间数组[OH_PackingOptionsForSequence_SetDelayTimeList](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptionsforsequence_setdelaytimelist)设置编码时图片的延迟时间数组。uint32_t *disposalTypes帧数[OH_PackingOptionsForSequence_GetDisposalTypes](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptionsforsequence_getdisposaltypes)设置编码时图片的过渡帧模式数组。uint32_t *disposalTypes帧数[OH_PackingOptionsForSequence_SetDisposalTypes](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptionsforsequence_setdisposaltypes)设置编码时图片的过渡帧模式数组。uint32_tloopCount帧数[OH_PackingOptionsForSequence_GetLoopCount](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptionsforsequence_getloopcount)获取编码时图片循环播放次数。uint32_tloopCount帧数[OH_PackingOptionsForSequence_SetLoopCount](../../capi/headers/image_packer_native.h.md#ZH-CN_TOPIC_0000002529445817__oh_packingoptionsforsequence_setloopcount)设置编码时图片循环播放次数，取值范围为[0，65535]，0表示无限循环；若无此字段，则表示不循环播放。

**起始版本：** 18

**相关模块：**[Image_NativeModule](../graphics/Image_NativeModule.md)

**所在头文件：**[image_packer_native.h](../../capi/headers/image_packer_native.h.md)