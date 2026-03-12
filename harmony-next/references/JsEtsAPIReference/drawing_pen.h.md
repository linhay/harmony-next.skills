# drawing_pen.h

#### 概述

文件中定义了与画笔相关的功能函数。

**相关示例：**[Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/HarmonyOS-feature-20251117/ArkGraphics2D/Drawing/NDKAPIDrawing)

**引用文件：** <native_drawing/drawing_pen.h>

**库：** libnative_drawing.so

**起始版本：** 8

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)OH_NativeColorSpaceManager声明色域管理对象，提供获取色域基础属性的能力。

#### 枚举

名称typedef关键字描述[OH_Drawing_PenLineCapStyle](#ZH-CN_TOPIC_0000002497446026__oh_drawing_penlinecapstyle)OH_Drawing_PenLineCapStyle枚举集合定义了画笔笔帽的样式，即画笔在绘制线段时，在线段头尾端点的样式。[OH_Drawing_PenLineJoinStyle](#ZH-CN_TOPIC_0000002497446026__oh_drawing_penlinejoinstyle)OH_Drawing_PenLineJoinStyle枚举集合定义了线条转角的样式，即画笔在绘制折线段时，在折线转角处的样式。

#### 函数

名称描述[OH_Drawing_Pen* OH_Drawing_PenCreate(void)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pencreate)用于创建一个画笔对象。[OH_Drawing_Pen* OH_Drawing_PenCopy(OH_Drawing_Pen* pen)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pencopy)

创建一个画笔对象副本[OH_Drawing_Pen](OH_Drawing_Pen.md)，用于拷贝一个已有画笔对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenDestroy(OH_Drawing_Pen* pen)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pendestroy)用于销毁画笔对象并回收该对象占有的内存。[bool OH_Drawing_PenIsAntiAlias(const OH_Drawing_Pen* pen)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_penisantialias)

用于获取画笔是否设置抗锯齿属性，如果为真则说明画笔会启用抗锯齿功能，在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetAntiAlias(OH_Drawing_Pen* pen, bool antiAlias)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetantialias)

用于设置画笔的抗锯齿属性，设置为真则画笔在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[uint32_t OH_Drawing_PenGetColor(const OH_Drawing_Pen* pen)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetcolor)

用于获取画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetColor(OH_Drawing_Pen* pen, uint32_t color)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetcolor)

用于设置画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[uint8_t OH_Drawing_PenGetAlpha(const OH_Drawing_Pen* pen)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetalpha)

获取画笔的透明度值。画笔在勾勒图形时透明通道会使用该值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetAlpha(OH_Drawing_Pen* pen, uint8_t alpha)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetalpha)

为画笔设置透明度值。画笔在勾勒图形时透明通道会使用该值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[float OH_Drawing_PenGetWidth(const OH_Drawing_Pen* pen)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetwidth)

用于获取画笔的厚度属性，厚度属性描述了画笔绘制图形轮廓的宽度。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetWidth(OH_Drawing_Pen* pen, float width)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetwidth)

用于设置画笔的厚度属性，厚度属性描述了画笔绘制图形轮廓的宽度。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[float OH_Drawing_PenGetMiterLimit(const OH_Drawing_Pen* pen)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetmiterlimit)

用于获取折线尖角的限制值，当画笔绘制一条折线，转角类型设置为尖角时，那么此时该属性用于限制出现尖角的长度范围，如果超出则平角显示，不超出依然为尖角。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetMiterLimit(OH_Drawing_Pen* pen, float miter)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetmiterlimit)

用于设置折线尖角的限制值，当画笔绘制一条折线，转角类型设置为尖角时，那么此时该属性用于限制出现尖角的长度范围，如果超出则平角显示，不超出依然为尖角。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[OH_Drawing_PenLineCapStyle OH_Drawing_PenGetCap(const OH_Drawing_Pen* pen)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetcap)

用于获取画笔笔帽的样式。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetCap(OH_Drawing_Pen* pen, OH_Drawing_PenLineCapStyle capStyle)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetcap)

用于设置画笔笔帽样式。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

capStyle不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[OH_Drawing_PenLineJoinStyle OH_Drawing_PenGetJoin(const OH_Drawing_Pen* pen)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetjoin)

用于获取画笔绘制折线转角的样式。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetJoin(OH_Drawing_Pen* pen, OH_Drawing_PenLineJoinStyle joinStyle)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetjoin)

用于设置画笔绘制转角的样式。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

joinStyle不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[void OH_Drawing_PenSetShaderEffect(OH_Drawing_Pen* pen, OH_Drawing_ShaderEffect* shaderEffect)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetshadereffect)

设置画笔着色器效果。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetShadowLayer(OH_Drawing_Pen* pen, OH_Drawing_ShadowLayer* shadowLayer)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetshadowlayer)

设置画笔阴影层效果，设置的阴影层效果当前仅在绘制文字时生效。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetPathEffect(OH_Drawing_Pen* pen, OH_Drawing_PathEffect* pathEffect)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetpatheffect)

设置画笔路径效果。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetFilter(OH_Drawing_Pen* pen, OH_Drawing_Filter* filter)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetfilter)

设置画笔滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenGetFilter(OH_Drawing_Pen* pen, OH_Drawing_Filter* filter)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetfilter)

从画笔获取滤波器[OH_Drawing_Filter](OH_Drawing_Filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen、filter任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenSetBlendMode(OH_Drawing_Pen* pen, OH_Drawing_BlendMode blendMode)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetblendmode)

为画笔设置一个混合器，该混合器实现了指定的混合模式枚举。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

blendMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[bool OH_Drawing_PenGetFillPath(OH_Drawing_Pen* pen, const OH_Drawing_Path* src, OH_Drawing_Path* dst,const OH_Drawing_Rect* rect, const OH_Drawing_Matrix* matrix)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetfillpath)

获取使用画笔绘制的源路径轮廓，并用目标路径表示。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen、src、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_PenReset(OH_Drawing_Pen* pen)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_penreset)

将画笔重置至初始值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[OH_Drawing_ErrorCode OH_Drawing_PenSetColor4f(OH_Drawing_Pen* pen, float a, float r, float g, float b,OH_NativeColorSpaceManager* colorSpaceManager)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pensetcolor4f)

用于设置画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色。

 颜色采用浮点数表示的ARGB格式，色彩空间由[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)指定。

 如果colorSpaceManager为nullptr，使用SRGB（基于IEC 61966-2.1：1999的标准红绿蓝色彩空间）色彩空间作为默认值。

[OH_Drawing_ErrorCode OH_Drawing_PenGetAlphaFloat(const OH_Drawing_Pen* pen, float* a)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetalphafloat)获取画笔颜色的透明度值。[OH_Drawing_ErrorCode OH_Drawing_PenGetRedFloat(const OH_Drawing_Pen* pen, float* r)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetredfloat)获取画笔颜色的红色分量。[OH_Drawing_ErrorCode OH_Drawing_PenGetGreenFloat(const OH_Drawing_Pen* pen, float* g)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetgreenfloat)获取画笔颜色的绿色分量。[OH_Drawing_ErrorCode OH_Drawing_PenGetBlueFloat(const OH_Drawing_Pen* pen, float* b)](#ZH-CN_TOPIC_0000002497446026__oh_drawing_pengetbluefloat)获取画笔颜色的蓝色分量。

#### 枚举类型说明

#### OH_Drawing_PenLineCapStyle

```ets
enum OH_Drawing_PenLineCapStyle
```

**描述**

枚举集合定义了画笔笔帽的样式，即画笔在绘制线段时，在线段头尾端点的样式。

**起始版本：** 8

枚举项描述LINE_FLAT_CAP没有笔帽样式，线条头尾端点处横切。LINE_SQUARE_CAP笔帽的样式为方框，线条的头尾端点处多出一个方框，方框宽度和线段一样宽，高度是线段厚度的一半。LINE_ROUND_CAP笔帽的样式为圆弧，线条的头尾端点处多出一个半圆弧，半圆的直径与线段厚度一致。

#### OH_Drawing_PenLineJoinStyle

```ets
enum OH_Drawing_PenLineJoinStyle
```

**描述**

枚举集合定义了线条转角的样式，即画笔在绘制折线段时，在折线转角处的样式。

**起始版本：** 8

枚举项描述LINE_MITER_JOIN转角类型为尖角，如果折线角度比较小，则尖角会很长，需要使用限制值（miter limit）进行限制。LINE_ROUND_JOIN转角类型为圆头。LINE_BEVEL_JOIN转角类型为平头。

#### 函数说明

#### OH_Drawing_PenCreate()

```ets
OH_Drawing_Pen* OH_Drawing_PenCreate(void)
```

**描述**

用于创建一个画笔对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

类型说明[OH_Drawing_Pen](OH_Drawing_Pen.md)*函数会返回一个指针，指针指向创建的画笔对象。

#### OH_Drawing_PenCopy()

```ets
OH_Drawing_Pen* OH_Drawing_PenCopy(OH_Drawing_Pen* pen)
```

**描述**

创建一个画笔对象副本[OH_Drawing_Pen](OH_Drawing_Pen.md)，用于拷贝一个已有画笔对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。

**返回：**

类型说明[OH_Drawing_Pen](OH_Drawing_Pen.md)*函数会返回一个指针，指针指向创建的画笔对象副本[OH_Drawing_Pen](OH_Drawing_Pen.md)。如果对象返回NULL，表示创建失败；可能的原因是可用内存为空，或者是pen为NULL。

#### OH_Drawing_PenDestroy()

```ets
void OH_Drawing_PenDestroy(OH_Drawing_Pen* pen)
```

**描述**

用于销毁画笔对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。

#### OH_Drawing_PenIsAntiAlias()

```ets
bool OH_Drawing_PenIsAntiAlias(const OH_Drawing_Pen* pen)
```

**描述**

用于获取画笔是否设置抗锯齿属性，如果为真则说明画笔会启用抗锯齿功能，在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。

**返回：**

类型说明bool函数返回画笔对象是否设置抗锯齿属性，返回真则设置了抗锯齿，返回假则没有设置抗锯齿。

#### OH_Drawing_PenSetAntiAlias()

```ets
void OH_Drawing_PenSetAntiAlias(OH_Drawing_Pen* pen, bool antiAlias)
```

**描述**

用于设置画笔的抗锯齿属性，设置为真则画笔在绘制图形时会对图形的边缘像素进行半透明的模糊处理。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。bool antiAlias真为抗锯齿，假则不做抗锯齿处理。

#### OH_Drawing_PenGetColor()

```ets
uint32_t OH_Drawing_PenGetColor(const OH_Drawing_Pen* pen)
```

**描述**

用于获取画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。

**返回：**

类型说明uint32_t函数返回一个描述颜色的32位（ARGB）变量。

#### OH_Drawing_PenSetColor()

```ets
void OH_Drawing_PenSetColor(OH_Drawing_Pen* pen, uint32_t color)
```

**描述**

用于设置画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色，用一个32位（ARGB）的变量表示。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。uint32_t color描述颜色的32位（ARGB）变量。

#### OH_Drawing_PenGetAlpha()

```ets
uint8_t OH_Drawing_PenGetAlpha(const OH_Drawing_Pen* pen)
```

**描述**

获取画笔的透明度值。画笔在勾勒图形时透明通道会使用该值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen表示指向画笔对象的指针。

**返回：**

类型说明uint8_t返回一个8比特的值表示透明度。

#### OH_Drawing_PenSetAlpha()

```ets
void OH_Drawing_PenSetAlpha(OH_Drawing_Pen* pen, uint8_t alpha)
```

**描述**

为画笔设置透明度值。画笔在勾勒图形时透明通道会使用该值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen表示指向画笔对象的指针。uint8_t alpha表示要设置的透明度值，是一个8比特的变量。

#### OH_Drawing_PenGetWidth()

```ets
float OH_Drawing_PenGetWidth(const OH_Drawing_Pen* pen)
```

**描述**

用于获取画笔的厚度属性，厚度属性描述了画笔绘制图形轮廓的宽度。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。

**返回：**

类型说明float函数返回画笔的厚度。

#### OH_Drawing_PenSetWidth()

```ets
void OH_Drawing_PenSetWidth(OH_Drawing_Pen* pen, float width)
```

**描述**

用于设置画笔的厚度属性，厚度属性描述了画笔绘制图形轮廓的宽度。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。float width描述画笔厚度的变量。

#### OH_Drawing_PenGetMiterLimit()

```ets
float OH_Drawing_PenGetMiterLimit(const OH_Drawing_Pen* pen)
```

**描述**

用于获取折线尖角的限制值，当画笔绘制一条折线，转角类型设置为尖角时，那么此时该属性用于限制出现尖角的长度范围，如果超出则平角显示，不超出依然为尖角。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。

**返回：**

类型说明float函数返回尖角的限制值。

#### OH_Drawing_PenSetMiterLimit()

```ets
void OH_Drawing_PenSetMiterLimit(OH_Drawing_Pen* pen, float miter)
```

**描述**

用于设置折线尖角的限制值，当画笔绘制一条折线，转角类型设置为尖角时，那么此时该属性用于限制出现尖角的长度范围，如果超出则平角显示，不超出依然为尖角。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。float miter描述尖角限制值的变量。

#### OH_Drawing_PenGetCap()

```ets
OH_Drawing_PenLineCapStyle OH_Drawing_PenGetCap(const OH_Drawing_Pen* pen)
```

**描述**

用于获取画笔笔帽的样式。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。

**返回：**

类型说明[OH_Drawing_PenLineCapStyle](#ZH-CN_TOPIC_0000002497446026__oh_drawing_penlinecapstyle)函数返回画笔笔帽样式。

#### OH_Drawing_PenSetCap()

```ets
void OH_Drawing_PenSetCap(OH_Drawing_Pen* pen, OH_Drawing_PenLineCapStyle capStyle)
```

**描述**

用于设置画笔笔帽样式。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

capStyle不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。[OH_Drawing_PenLineCapStyle](#ZH-CN_TOPIC_0000002497446026__oh_drawing_penlinecapstyle) capStyle描述画笔笔帽样式的变量。

#### OH_Drawing_PenGetJoin()

```ets
OH_Drawing_PenLineJoinStyle OH_Drawing_PenGetJoin(const OH_Drawing_Pen* pen)
```

**描述**

用于获取画笔绘制折线转角的样式。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。

**返回：**

类型说明[OH_Drawing_PenLineJoinStyle](#ZH-CN_TOPIC_0000002497446026__oh_drawing_penlinejoinstyle)函数返回折线转角的样式。

#### OH_Drawing_PenSetJoin()

```ets
void OH_Drawing_PenSetJoin(OH_Drawing_Pen* pen, OH_Drawing_PenLineJoinStyle joinStyle)
```

**描述**

用于设置画笔绘制转角的样式。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

joinStyle不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象的指针。[OH_Drawing_PenLineJoinStyle](#ZH-CN_TOPIC_0000002497446026__oh_drawing_penlinejoinstyle) joinStyle折线转角样式。

#### OH_Drawing_PenSetShaderEffect()

```ets
void OH_Drawing_PenSetShaderEffect(OH_Drawing_Pen* pen, OH_Drawing_ShaderEffect* shaderEffect)
```

**描述**

设置画笔着色器效果。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象[OH_Drawing_Pen](OH_Drawing_Pen.md)的指针。[OH_Drawing_ShaderEffect](OH_Drawing_ShaderEffect.md)* shaderEffect指向着色器对象[OH_Drawing_ShaderEffect](OH_Drawing_ShaderEffect.md)的指针，为NULL表示清空着色器效果。

#### OH_Drawing_PenSetShadowLayer()

```ets
void OH_Drawing_PenSetShadowLayer(OH_Drawing_Pen* pen, OH_Drawing_ShadowLayer* shadowLayer)
```

**描述**

设置画笔阴影层效果，设置的阴影层效果当前仅在绘制文字时生效。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象[OH_Drawing_Pen](OH_Drawing_Pen.md)的指针。[OH_Drawing_ShadowLayer](OH_Drawing_ShadowLayer.md)* shadowLayer指向阴影层对象[OH_Drawing_ShadowLayer](OH_Drawing_ShadowLayer.md)的指针，为NULL表示清空阴影层效果。

#### OH_Drawing_PenSetPathEffect()

```ets
void OH_Drawing_PenSetPathEffect(OH_Drawing_Pen* pen, OH_Drawing_PathEffect* pathEffect)
```

**描述**

设置画笔路径效果。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象[OH_Drawing_Pen](OH_Drawing_Pen.md)的指针。[OH_Drawing_PathEffect](OH_Drawing_PathEffect.md)* pathEffect指向路径效果对象[OH_Drawing_PathEffect](OH_Drawing_PathEffect.md)的指针，为NULL表示清空路径效果。

#### OH_Drawing_PenSetFilter()

```ets
void OH_Drawing_PenSetFilter(OH_Drawing_Pen* pen, OH_Drawing_Filter* filter)
```

**描述**

设置画笔滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象[OH_Drawing_Pen](OH_Drawing_Pen.md)的指针。[OH_Drawing_Filter](OH_Drawing_Filter.md)* filter指向滤波器[OH_Drawing_Filter](OH_Drawing_Filter.md)的指针，为NULL表示清空画笔滤波器。

#### OH_Drawing_PenGetFilter()

```ets
void OH_Drawing_PenGetFilter(OH_Drawing_Pen* pen, OH_Drawing_Filter* filter)
```

**描述**

从画笔获取滤波器[OH_Drawing_Filter](OH_Drawing_Filter.md)。滤波器是一个容器，可以承载蒙版滤波器和颜色滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen、filter任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象[OH_Drawing_Pen](OH_Drawing_Pen.md)的指针。[OH_Drawing_Filter](OH_Drawing_Filter.md)* filter指向滤波器对象[OH_Drawing_Filter](OH_Drawing_Filter.md)的指针。

#### OH_Drawing_PenSetBlendMode()

```ets
void OH_Drawing_PenSetBlendMode(OH_Drawing_Pen* pen, OH_Drawing_BlendMode blendMode)
```

**描述**

为画笔设置一个混合器，该混合器实现了指定的混合模式枚举。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

blendMode不在枚举范围内时返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象[OH_Drawing_Pen](OH_Drawing_Pen.md)的指针。[OH_Drawing_BlendMode](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_blendmode) blendMode混合模式枚举类型[OH_Drawing_BlendMode](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_blendmode)。

#### OH_Drawing_PenGetFillPath()

```ets
bool OH_Drawing_PenGetFillPath(OH_Drawing_Pen* pen, const OH_Drawing_Path* src, OH_Drawing_Path* dst,const OH_Drawing_Rect* rect, const OH_Drawing_Matrix* matrix)
```

**描述**

获取使用画笔绘制的源路径轮廓，并用目标路径表示。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen、src、dst任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象[OH_Drawing_Pen](OH_Drawing_Pen.md)的指针。const [OH_Drawing_Path](OH_Drawing_Path.md)* src指向源路径对象[OH_Drawing_Path](OH_Drawing_Path.md)的指针。[OH_Drawing_Path](OH_Drawing_Path.md)* dst指向目标路径对象[OH_Drawing_Path](OH_Drawing_Path.md)的指针。const [OH_Drawing_Rect](OH_Drawing_Rect.md)* rect指向矩形对象[OH_Drawing_Rect](OH_Drawing_Rect.md)的指针，推荐使用NULL。const [OH_Drawing_Matrix](OH_Drawing_Matrix.md)* matrix指向矩阵对象[OH_Drawing_Matrix](OH_Drawing_Matrix.md)的指针，推荐使用NULL, 默认是一个单位矩阵。

**返回：**

类型说明bool获取目标路径是否成功。true表示获取成功，false表示获取失败。

#### OH_Drawing_PenReset()

```ets
void OH_Drawing_PenReset(OH_Drawing_Pen* pen)
```

**描述**

将画笔重置至初始值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

pen为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Pen](OH_Drawing_Pen.md)* pen指向画笔对象[OH_Drawing_Pen](OH_Drawing_Pen.md)的指针。

#### OH_Drawing_PenSetColor4f()

```ets
OH_Drawing_ErrorCode OH_Drawing_PenSetColor4f(OH_Drawing_Pen* pen, float a, float r, float g, float b,OH_NativeColorSpaceManager* colorSpaceManager)
```

**描述**

用于设置画笔的颜色属性，颜色属性描述了画笔绘制图形轮廓时使用的颜色。

 颜色采用浮点数表示的ARGB格式，色彩空间由[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)指定。

 如果colorSpaceManager为nullptr，使用SRGB（基于IEC 61966-2.1：1999的标准红绿蓝色彩空间）色彩空间作为默认值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述OH_Drawing_Pen* pen表示指向[OH_Drawing_Pen](OH_Drawing_Pen.md)对象的指针。float a表示颜色中的透明度值，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。float r表示颜色中的红色分量，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。float g表示颜色中的绿色分量，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。float b表示颜色中的蓝色分量，用0.0 ~ 1.0之间的浮点数表示，大于1.0时，取1.0，小于0.0时，取0.0。[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)* colorSpaceManager表示指向[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)对象的指针。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行结果。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数pen为NULL。

#### OH_Drawing_PenGetAlphaFloat()

```ets
OH_Drawing_ErrorCode OH_Drawing_PenGetAlphaFloat(const OH_Drawing_Pen* pen, float* a)
```

**描述**

获取画笔颜色的透明度值。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen表示指向[OH_Drawing_Pen](OH_Drawing_Pen.md)对象的指针。float* a表示颜色中的透明度，范围为0.0 ~ 1.0的浮点数。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行结果。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数pen或a为NULL。

#### OH_Drawing_PenGetRedFloat()

```ets
OH_Drawing_ErrorCode OH_Drawing_PenGetRedFloat(const OH_Drawing_Pen* pen, float* r)
```

**描述**

获取画笔颜色的红色分量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen表示指向[OH_Drawing_Pen](OH_Drawing_Pen.md)对象的指针。float* r表示颜色中的红色分量，范围为0.0 ~ 1.0的浮点数。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行结果。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数pen或r为NULL。

#### OH_Drawing_PenGetGreenFloat()

```ets
OH_Drawing_ErrorCode OH_Drawing_PenGetGreenFloat(const OH_Drawing_Pen* pen, float* g)
```

**描述**

获取画笔颜色的绿色分量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen表示指向[OH_Drawing_Pen](OH_Drawing_Pen.md)对象的指针。float* g表示颜色中的绿色分量，范围为0.0 ~ 1.0的浮点数。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行结果。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数pen或g为NULL。

#### OH_Drawing_PenGetBlueFloat()

```ets
OH_Drawing_ErrorCode OH_Drawing_PenGetBlueFloat(const OH_Drawing_Pen* pen, float* b)
```

**描述**

获取画笔颜色的蓝色分量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述const [OH_Drawing_Pen](OH_Drawing_Pen.md)* pen表示指向[OH_Drawing_Pen](OH_Drawing_Pen.md)对象的指针。float* b表示颜色中的蓝色分量，范围为0.0 ~ 1.0的浮点数。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行结果。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数pen或b为NULL。