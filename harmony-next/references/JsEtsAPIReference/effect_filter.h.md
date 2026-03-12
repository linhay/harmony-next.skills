# effect_filter.h

#### 概述

声明滤镜效果的接口。

**引用文件：** <native_effect/effect_filter.h>

**库：** libnative_effect.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**相关模块：**[effectKit](effectKit.md)

#### 汇总

#### 函数

名称描述[EffectErrorCode OH_Filter_CreateEffect(OH_PixelmapNative* pixelmap, OH_Filter** filter)](#ZH-CN_TOPIC_0000002529445981__oh_filter_createeffect)创建一个OH_Filter对象。[EffectErrorCode OH_Filter_Release(OH_Filter* filter)](#ZH-CN_TOPIC_0000002529445981__oh_filter_release)释放OH_Filter对象。[EffectErrorCode OH_Filter_Blur(OH_Filter* filter, float radius)](#ZH-CN_TOPIC_0000002529445981__oh_filter_blur)创建一个毛玻璃滤镜效果，然后添加到滤镜里面。[EffectErrorCode OH_Filter_BlurWithTileMode(OH_Filter* filter, float radius, EffectTileMode tileMode)](#ZH-CN_TOPIC_0000002529445981__oh_filter_blurwithtilemode)创建一个毛玻璃滤镜效果，然后添加到滤镜里面，支持着色器效果平铺模式选择。[EffectErrorCode OH_Filter_Brighten(OH_Filter* filter, float brightness)](#ZH-CN_TOPIC_0000002529445981__oh_filter_brighten)创建一个提亮效果并且添加到滤镜中。[EffectErrorCode OH_Filter_GrayScale(OH_Filter* filter)](#ZH-CN_TOPIC_0000002529445981__oh_filter_grayscale)创建一个灰度效果并且添加到滤镜中。[EffectErrorCode OH_Filter_Invert(OH_Filter* filter)](#ZH-CN_TOPIC_0000002529445981__oh_filter_invert)创建一个反色效果并且添加到滤镜中。[EffectErrorCode OH_Filter_SetColorMatrix(OH_Filter* filter, OH_Filter_ColorMatrix* matrix)](#ZH-CN_TOPIC_0000002529445981__oh_filter_setcolormatrix)通过矩阵创建一个自定义的效果并且添加到滤镜中。[EffectErrorCode OH_Filter_GetEffectPixelMap(OH_Filter* filter, OH_PixelmapNative** pixelmap)](#ZH-CN_TOPIC_0000002529445981__oh_filter_geteffectpixelmap)获取滤镜生成的位图。

#### 函数说明

#### OH_Filter_CreateEffect()

```ets
EffectErrorCode OH_Filter_CreateEffect(OH_PixelmapNative* pixelmap, OH_Filter** filter)
```

**描述**

创建一个OH_Filter对象。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md)* pixelmap创建滤镜的位图。[OH_Filter](OH_Filter.md)** filter用来接收滤镜的二级指针。

**返回：**

类型说明[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)返回结果参见状态码[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)。

#### OH_Filter_Release()

```ets
EffectErrorCode OH_Filter_Release(OH_Filter* filter)
```

**描述**

释放OH_Filter对象。

**起始版本：** 12

**参数：**

参数项描述[OH_Filter](OH_Filter.md)* filter被释放的对象指针。

**返回：**

类型说明[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)返回结果参见状态码[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)。

#### OH_Filter_Blur()

```ets
EffectErrorCode OH_Filter_Blur(OH_Filter* filter, float radius)
```

**描述**

创建一个毛玻璃滤镜效果，然后添加到滤镜里面。

**起始版本：** 12

**参数：**

参数项描述[OH_Filter](OH_Filter.md)* filter滤镜指针。float radius毛玻璃效果的模糊半径，单位为像素。

**返回：**

类型说明[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)返回结果参见状态码[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)。

#### OH_Filter_BlurWithTileMode()

```ets
EffectErrorCode OH_Filter_BlurWithTileMode(OH_Filter* filter, float radius, EffectTileMode tileMode)
```

**描述**

创建一个毛玻璃滤镜效果，然后添加到滤镜里面，支持着色器效果平铺模式选择。

**起始版本：** 14

**参数：**

参数项描述[OH_Filter](OH_Filter.md)* filter滤镜指针。float radius毛玻璃效果的模糊半径，单位为像素。[EffectTileMode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecttilemode) tileMode着色器效果平铺模式，支持可选的具体模式可见[EffectTileMode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecttilemode)枚举。

**返回：**

类型说明[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)

返回结果参见状态码[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)。

 操作成功则返回EFFECT_SUCCESS。

 无效参数则返回EFFECT_BAD_PARAMETER。

#### OH_Filter_Brighten()

```ets
EffectErrorCode OH_Filter_Brighten(OH_Filter* filter, float brightness)
```

**描述**

创建一个提亮效果并且添加到滤镜中。

**起始版本：** 12

**参数：**

参数项描述[OH_Filter](OH_Filter.md)* filter滤镜指针。float brightness提亮效果的亮度值，取值范围在0-1之间，取值为0时图像保持不变，取值为1时图像全白。

**返回：**

类型说明[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)返回结果参见状态码[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)。

#### OH_Filter_GrayScale()

```ets
EffectErrorCode OH_Filter_GrayScale(OH_Filter* filter)
```

**描述**

创建一个灰度效果并且添加到滤镜中。

**起始版本：** 12

**参数：**

参数项描述[OH_Filter](OH_Filter.md)* filter滤镜指针。

**返回：**

类型说明[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)返回结果参见状态码[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)。

#### OH_Filter_Invert()

```ets
EffectErrorCode OH_Filter_Invert(OH_Filter* filter)
```

**描述**

创建一个反色效果并且添加到滤镜中。

**起始版本：** 12

**参数：**

参数项描述[OH_Filter](OH_Filter.md)* filter滤镜指针。

**返回：**

类型说明[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)返回结果参见状态码[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)。

#### OH_Filter_SetColorMatrix()

```ets
EffectErrorCode OH_Filter_SetColorMatrix(OH_Filter* filter, OH_Filter_ColorMatrix* matrix)
```

**描述**

通过矩阵创建一个自定义的效果并且添加到滤镜中。

**起始版本：** 12

**参数：**

参数项描述[OH_Filter](OH_Filter.md)* filter滤镜指针。[OH_Filter_ColorMatrix](OH_Filter_ColorMatrix.md)* matrix用来创建滤镜的自定义矩阵[OH_Filter_ColorMatrix](OH_Filter_ColorMatrix.md)。

**返回：**

类型说明[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)返回结果参见状态码[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)。

#### OH_Filter_GetEffectPixelMap()

```ets
EffectErrorCode OH_Filter_GetEffectPixelMap(OH_Filter* filter, OH_PixelmapNative** pixelmap)
```

**描述**

获取滤镜生成的位图。

**起始版本：** 12

**参数：**

参数项描述[OH_Filter](OH_Filter.md)* filter用来创建位图的滤镜指针。[OH_PixelmapNative](OH_PixelmapNative.md)** pixelmap用来接收位图的二级指针。

**返回：**

类型说明[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)返回结果参见状态码[EffectErrorCode](effect_types.h.md#ZH-CN_TOPIC_0000002497606018__effecterrorcode)。