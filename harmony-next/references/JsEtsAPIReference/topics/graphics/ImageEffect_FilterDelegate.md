# ImageEffect_FilterDelegate

```ets
typedef struct ImageEffect_FilterDelegate {...} ImageEffect_FilterDelegate
```

#### 概述

自定义滤镜回调函数结构体。

**起始版本：** 12

**相关模块：**[ImageEffect](ImageEffect.md)

**所在头文件：**[image_effect_filter.h](../../capi/headers/image_effect_filter.h.md)

#### 汇总

#### 成员变量

名称描述[OH_EffectFilterDelegate_SetValue](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__oh_effectfilterdelegate_setvalue) setValue参数设置函数指针。[OH_EffectFilterDelegate_Render](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__oh_effectfilterdelegate_render) render滤镜渲染函数指针。[OH_EffectFilterDelegate_Save](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__oh_effectfilterdelegate_save) save序列化效果器函数指针。[OH_EffectFilterDelegate_Restore](../../capi/headers/image_effect_filter.h.md#ZH-CN_TOPIC_0000002497445880__oh_effectfilterdelegate_restore) restore反序列化效果器函数指针。