# ImageEffect_FilterDelegate

```ets
typedef struct ImageEffect_FilterDelegate {...} ImageEffect_FilterDelegate
```

**概述**

自定义滤镜回调函数结构体。

起始版本： 12

相关模块： [ImageEffect](ImageEffect.md)

所在头文件： [image_effect_filter.h](image_effect_filter.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| OH_EffectFilterDelegate_SetValue setValue | 参数设置函数指针。 |
| OH_EffectFilterDelegate_Render render | 滤镜渲染函数指针。 |
| OH_EffectFilterDelegate_Save save | 序列化效果器函数指针。 |
| OH_EffectFilterDelegate_Restore restore | 反序列化效果器函数指针。 |