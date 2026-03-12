# drawing_brush.h

#### 概述

文件中定义了与画刷相关的功能函数。

**相关示例：**[Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/HarmonyOS-feature-20251117/ArkGraphics2D/Drawing/NDKAPIDrawing)

**引用文件：** <native_drawing/drawing_brush.h>

**库：** libnative_drawing.so

**起始版本：** 8

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)OH_NativeColorSpaceManager声明色域管理对象，提供获取色域基础属性的能力。

#### 函数

名称描述[OH_Drawing_Brush* OH_Drawing_BrushCreate(void)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushcreate)用于创建一个画刷对象。[OH_Drawing_Brush* OH_Drawing_BrushCopy(OH_Drawing_Brush* brush)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushcopy)

创建一个画刷对象副本[OH_Drawing_Brush](OH_Drawing_Brush.md)，用于拷贝一个已有画刷对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_BrushDestroy(OH_Drawing_Brush* brush)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushdestroy)用于销毁画刷对象并回收该对象占有的内存。[bool OH_Drawing_BrushIsAntiAlias(const OH_Drawing_Brush* brush)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushisantialias)

用于获取画刷是否设置抗锯齿属性，如果为真则说明画刷会启用抗锯齿功能，在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_BrushSetAntiAlias(OH_Drawing_Brush* brush, bool antiAlias)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushsetantialias)

用于设置画刷的抗锯齿属性，设置为真则画刷在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[uint32_t OH_Drawing_BrushGetColor(const OH_Drawing_Brush* brush)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushgetcolor)

用于获取画刷的颜色属性，颜色属性描述了画刷填充图形时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_BrushSetColor(OH_Drawing_Brush* brush, uint32_t color)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushsetcolor)

用于设置画刷的颜色属性，颜色属性描述了画刷填充图形时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[uint8_t OH_Drawing_BrushGetAlpha(const OH_Drawing_Brush* brush)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushgetalpha)

获取画刷的透明度值。画刷在填充形状时透明通道会使用该值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_BrushSetAlpha(OH_Drawing_Brush* brush, uint8_t alpha)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushsetalpha)

为画刷设置透明度值。画刷在填充形状时透明通道会使用该值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_BrushSetShaderEffect(OH_Drawing_Brush* brush, OH_Drawing_ShaderEffect* shaderEffect)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushsetshadereffect)

为画刷设置着色器效果。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_BrushSetShadowLayer(OH_Drawing_Brush* brush, OH_Drawing_ShadowLayer* shadowLayer)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushsetshadowlayer)

为画刷设置阴影层，设置的阴影层效果当前仅在绘制文字时生效。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_BrushSetFilter(OH_Drawing_Brush* brush, OH_Drawing_Filter* filter)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushsetfilter)

为画刷设置滤波器[OH_Drawing_Filter](OH_Drawing_Filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_BrushGetFilter(OH_Drawing_Brush* brush, OH_Drawing_Filter* filter)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushgetfilter)

从画刷获取滤波器[OH_Drawing_Filter](OH_Drawing_Filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush、filter任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_BrushSetBlendMode(OH_Drawing_Brush* brush, OH_Drawing_BlendMode blendMode)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushsetblendmode)

为画刷设置一个混合器，该混合器实现了指定的混合模式枚举。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

blendMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[void OH_Drawing_BrushReset(OH_Drawing_Brush* brush)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushreset)

将画刷重置至初始状态，清空所有已设置的属性。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[OH_Drawing_ErrorCode OH_Drawing_BrushSetColor4f(OH_Drawing_Brush* brush, float a, float r, float g, float b,OH_NativeColorSpaceManager* colorSpaceManager)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushsetcolor4f)

设置画刷的颜色。颜色将被画刷用来填充形状。

 颜色采用浮点数表示的ARGB格式，色彩空间由[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)指定。

 如果colorSpaceManager为nullptr，使用SRGB（基于IEC 61966-2.1：1999的标准红绿蓝色彩空间）色彩空间作为默认值。

[OH_Drawing_ErrorCode OH_Drawing_BrushGetAlphaFloat(const OH_Drawing_Brush* brush, float* a)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushgetalphafloat)获取画刷颜色的透明度值。[OH_Drawing_ErrorCode OH_Drawing_BrushGetRedFloat(const OH_Drawing_Brush* brush, float* r)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushgetredfloat)获取画刷颜色的红色分量。[OH_Drawing_ErrorCode OH_Drawing_BrushGetGreenFloat(const OH_Drawing_Brush* brush, float* g)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushgetgreenfloat)获取画刷颜色的绿色分量。[OH_Drawing_ErrorCode OH_Drawing_BrushGetBlueFloat(const OH_Drawing_Brush* brush, float* b)](#ZH-CN_TOPIC_0000002529445961__oh_drawing_brushgetbluefloat)获取画刷颜色的蓝色分量。

#### 函数说明

#### OH_Drawing_BrushCreate()

```ets
OH_Drawing_Brush* OH_Drawing_BrushCreate(void)
```

**描述**

用于创建一个画刷对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

类型说明[OH_Drawing_Brush](OH_Drawing_Brush.md)*函数会返回一个指针，指针指向创建的画刷对象。

#### OH_Drawing_BrushCopy()

```ets
OH_Drawing_Brush* OH_Drawing_BrushCopy(OH_Drawing_Brush* brush)
```

**描述**

创建一个画刷对象副本[OH_Drawing_Brush](OH_Drawing_Brush.md)，用于拷贝一个已有画刷对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象的指针。

**返回：**

类型说明[OH_Drawing_Brush](OH_Drawing_Brush.md)*函数会返回一个指针，指针指向创建的画刷对象副本[OH_Drawing_Brush](OH_Drawing_Brush.md)。如果对象返回NULL，表示创建失败；可能的原因是可用内存为空，或者是brush为NULL。

#### OH_Drawing_BrushDestroy()

```ets
void OH_Drawing_BrushDestroy(OH_Drawing_Brush* brush)
```

**描述**

用于销毁画刷对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象的指针。

#### OH_Drawing_BrushIsAntiAlias()

```ets
bool OH_Drawing_BrushIsAntiAlias(const OH_Drawing_Brush* brush)
```

**描述**

用于获取画刷是否设置抗锯齿属性，如果为真则说明画刷会启用抗锯齿功能，在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述const [OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象的指针。

**返回：**

类型说明bool函数返回画刷对象是否设置抗锯齿属性，返回真则设置了抗锯齿，返回假则没有设置抗锯齿。

#### OH_Drawing_BrushSetAntiAlias()

```ets
void OH_Drawing_BrushSetAntiAlias(OH_Drawing_Brush* brush, bool antiAlias)
```

**描述**

用于设置画刷的抗锯齿属性，设置为真则画刷在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象的指针。bool antiAlias真为抗锯齿，假则不做抗锯齿处理。

#### OH_Drawing_BrushGetColor()

```ets
uint32_t OH_Drawing_BrushGetColor(const OH_Drawing_Brush* brush)
```

**描述**

用于获取画刷的颜色属性，颜色属性描述了画刷填充图形时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述const [OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象的指针。

**返回：**

类型说明uint32_t函数返回一个描述颜色的32位（ARGB）变量。

#### OH_Drawing_BrushSetColor()

```ets
void OH_Drawing_BrushSetColor(OH_Drawing_Brush* brush, uint32_t color)
```

**描述**

用于设置画刷的颜色属性，颜色属性描述了画刷填充图形时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象的指针。uint32_t color描述颜色的32位（ARGB）变量。

#### OH_Drawing_BrushGetAlpha()

```ets
uint8_t OH_Drawing_BrushGetAlpha(const OH_Drawing_Brush* brush)
```

**描述**

获取画刷的透明度值。画刷在填充形状时透明通道会使用该值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述const [OH_Drawing_Brush](OH_Drawing_Brush.md)* brush表示指向画刷对象的指针。

**返回：**

类型说明uint8_t返回一个8位变量，用于表示透明度值。

#### OH_Drawing_BrushSetAlpha()

```ets
void OH_Drawing_BrushSetAlpha(OH_Drawing_Brush* brush, uint8_t alpha)
```

**描述**

为画刷设置透明度值。画刷在填充形状时透明通道会使用该值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象的指针。uint8_t alpha表示要设置的透明度值，是一个8位变量。

#### OH_Drawing_BrushSetShaderEffect()

```ets
void OH_Drawing_BrushSetShaderEffect(OH_Drawing_Brush* brush, OH_Drawing_ShaderEffect* shaderEffect)
```

**描述**

为画刷设置着色器效果。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象的指针。[OH_Drawing_ShaderEffect](OH_Drawing_ShaderEffect.md)* shaderEffect表示指向着色器对象的指针，为NULL表示清空画刷的着色器效果。

#### OH_Drawing_BrushSetShadowLayer()

```ets
void OH_Drawing_BrushSetShadowLayer(OH_Drawing_Brush* brush, OH_Drawing_ShadowLayer* shadowLayer)
```

**描述**

为画刷设置阴影层，设置的阴影层效果当前仅在绘制文字时生效。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象的指针。[OH_Drawing_ShadowLayer](OH_Drawing_ShadowLayer.md)* shadowLayer表示指向阴影层的指针，为NULL表示清空画刷的阴影层效果。

#### OH_Drawing_BrushSetFilter()

```ets
void OH_Drawing_BrushSetFilter(OH_Drawing_Brush* brush, OH_Drawing_Filter* filter)
```

**描述**

为画刷设置滤波器[OH_Drawing_Filter](OH_Drawing_Filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象的指针。[OH_Drawing_Filter](OH_Drawing_Filter.md)* filter表示指向滤波器对象的指针，为NULL表示清空画刷滤波器。

#### OH_Drawing_BrushGetFilter()

```ets
void OH_Drawing_BrushGetFilter(OH_Drawing_Brush* brush, OH_Drawing_Filter* filter)
```

**描述**

从画刷获取滤波器[OH_Drawing_Filter](OH_Drawing_Filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush、filter任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象[OH_Drawing_Brush](OH_Drawing_Brush.md)的指针。[OH_Drawing_Filter](OH_Drawing_Filter.md)* filter表示指向滤波器对象[OH_Drawing_Filter](OH_Drawing_Filter.md)的指针。

#### OH_Drawing_BrushSetBlendMode()

```ets
void OH_Drawing_BrushSetBlendMode(OH_Drawing_Brush* brush, OH_Drawing_BlendMode blendMode)
```

**描述**

为画刷设置一个混合器，该混合器实现了指定的混合模式枚举。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

blendMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象[OH_Drawing_Brush](OH_Drawing_Brush.md)的指针。[OH_Drawing_BlendMode](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_blendmode) blendMode混合模式枚举类型[OH_Drawing_BlendMode](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_blendmode)。

#### OH_Drawing_BrushReset()

```ets
void OH_Drawing_BrushReset(OH_Drawing_Brush* brush)
```

**描述**

将画刷重置至初始状态，清空所有已设置的属性。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

brush为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Brush](OH_Drawing_Brush.md)* brush指向画刷对象[OH_Drawing_Brush](OH_Drawing_Brush.md)的指针。

#### OH_Drawing_BrushSetColor4f()

```ets
OH_Drawing_ErrorCode OH_Drawing_BrushSetColor4f(OH_Drawing_Brush* brush, float a, float r, float g, float b,OH_NativeColorSpaceManager* colorSpaceManager)
```

**描述**

设置画刷的颜色。颜色将被画刷用来填充形状。

 颜色采用浮点数表示的ARGB格式，色彩空间由[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)指定。

 如果colorSpaceManager为nullptr，使用SRGB（基于IEC 61966-2.1：1999的标准红绿蓝色彩空间）色彩空间作为默认值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述OH_Drawing_Brush* brush表示指向[OH_Drawing_Brush](OH_Drawing_Brush.md)对象的指针。float a表示颜色中的透明度值，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。float r表示颜色中的红色分量，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。float g表示颜色中的绿色分量，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。float b表示颜色中的蓝色分量，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)* colorSpaceManager表示指向[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)对象的指针。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行结果。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数brush为NULL。

#### OH_Drawing_BrushGetAlphaFloat()

```ets
OH_Drawing_ErrorCode OH_Drawing_BrushGetAlphaFloat(const OH_Drawing_Brush* brush, float* a)
```

**描述**

获取画刷颜色的透明度值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_Brush](OH_Drawing_Brush.md)* brush表示指向[OH_Drawing_Brush](OH_Drawing_Brush.md)对象的指针。float* a表示颜色的透明度，范围为0.0 ~ 1.0的浮点数。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行结果。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数brush或a为NULL。

#### OH_Drawing_BrushGetRedFloat()

```ets
OH_Drawing_ErrorCode OH_Drawing_BrushGetRedFloat(const OH_Drawing_Brush* brush, float* r)
```

**描述**

获取画刷颜色的红色分量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_Brush](OH_Drawing_Brush.md)* brush表示指向[OH_Drawing_Brush](OH_Drawing_Brush.md)对象的指针。float* r表示颜色中的红色分量，范围为0.0 ~ 1.0的浮点数。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行结果。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数brush或r为NULL。

#### OH_Drawing_BrushGetGreenFloat()

```ets
OH_Drawing_ErrorCode OH_Drawing_BrushGetGreenFloat(const OH_Drawing_Brush* brush, float* g)
```

**描述**

获取画刷颜色的绿色分量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_Brush](OH_Drawing_Brush.md)* brush表示指向[OH_Drawing_Brush](OH_Drawing_Brush.md)对象的指针。float* g表示颜色中的绿色分量，范围为0.0 ~ 1.0的浮点数。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行结果。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数brush或g为NULL。

#### OH_Drawing_BrushGetBlueFloat()

```ets
OH_Drawing_ErrorCode OH_Drawing_BrushGetBlueFloat(const OH_Drawing_Brush* brush, float* b)
```

**描述**

获取画刷颜色的蓝色分量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_Brush](OH_Drawing_Brush.md)* brush表示指向[OH_Drawing_Brush](OH_Drawing_Brush.md)对象的指针。float* b表示颜色中的蓝色分量，范围为0.0 ~ 1.0的浮点数。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行结果。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数brush或b为NULL。