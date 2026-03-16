# drawing_color_filter.h

#### 概述

声明与绘图模块中的颜色滤波器对象相关的函数。

**引用文件：** <native_drawing/drawing_color_filter.h>

**库：** libnative_drawing.so

**起始版本：** 11

**相关模块：**[Drawing](../../topics/graphics/Drawing.md)

#### 汇总

#### 函数

名称描述[OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateBlendMode(uint32_t color, OH_Drawing_BlendMode blendMode)](#ZH-CN_TOPIC_0000002529285989__oh_drawing_colorfiltercreateblendmode)创建具有混合模式的颜色滤波器。[OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateCompose(OH_Drawing_ColorFilter* outerColorFilter,OH_Drawing_ColorFilter* innerColorFilter)](#ZH-CN_TOPIC_0000002529285989__oh_drawing_colorfiltercreatecompose)

将两个颜色滤波器合成一个新的颜色滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

outerColorFilter、innerColorFilter任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateMatrix(const float matrix[20])](#ZH-CN_TOPIC_0000002529285989__oh_drawing_colorfiltercreatematrix)

创建具有5x4颜色矩阵的颜色滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateLinearToSrgbGamma(void)](#ZH-CN_TOPIC_0000002529285989__oh_drawing_colorfiltercreatelineartosrgbgamma)创建一个从线性颜色空间转换到SRGB颜色空间的颜色滤波器。[OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateSrgbGammaToLinear(void)](#ZH-CN_TOPIC_0000002529285989__oh_drawing_colorfiltercreatesrgbgammatolinear)创建颜色滤波器将RGB颜色通道应用于SRGB的伽玛曲线。[OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateLuma(void)](#ZH-CN_TOPIC_0000002529285989__oh_drawing_colorfiltercreateluma)创建一个颜色滤波器将其输入的亮度值乘以透明度通道，并将红色、绿色和蓝色通道设置为零。[OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateLighting(uint32_t mulColor, uint32_t addColor)](#ZH-CN_TOPIC_0000002529285989__oh_drawing_colorfiltercreatelighting)创建一个光照颜色滤波器，此滤波器会将RGB通道的颜色值乘以一种颜色值并加上另一种颜色值，计算结果会被限制在0到255范围内。[void OH_Drawing_ColorFilterDestroy(OH_Drawing_ColorFilter* colorFilter)](#ZH-CN_TOPIC_0000002529285989__oh_drawing_colorfilterdestroy)销毁颜色滤波器对象，并收回该对象占用的内存。

#### 函数说明

#### OH_Drawing_ColorFilterCreateBlendMode()

```ets
OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateBlendMode(uint32_t color, OH_Drawing_BlendMode blendMode)
```

**描述**

创建具有混合模式的颜色滤波器。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述uint32_t color表示颜色，是一个32位（ARGB）变量。[OH_Drawing_BlendMode](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_blendmode) blendMode表示混合模式。支持可选的混合模式具体可见[OH_Drawing_BlendMode](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_blendmode)枚举。

**返回：**

类型说明[OH_Drawing_ColorFilter](../../topics/graphics/OH_Drawing_ColorFilter.md)*返回创建的颜色滤波器对象的指针。

#### OH_Drawing_ColorFilterCreateCompose()

```ets
OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateCompose(OH_Drawing_ColorFilter* outerColorFilter,OH_Drawing_ColorFilter* innerColorFilter)
```

**描述**

将两个颜色滤波器合成一个新的颜色滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

outerColorFilter、innerColorFilter任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_ColorFilter](../../topics/graphics/OH_Drawing_ColorFilter.md)* outerColorFilter指向颜色滤波器对象一的指针。[OH_Drawing_ColorFilter](../../topics/graphics/OH_Drawing_ColorFilter.md)* innerColorFilter指向颜色滤波器对象二的指针。

**返回：**

类型说明[OH_Drawing_ColorFilter](../../topics/graphics/OH_Drawing_ColorFilter.md)*返回创建的颜色滤波器对象的指针。

#### OH_Drawing_ColorFilterCreateMatrix()

```ets
OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateMatrix(const float matrix[20])
```

**描述**

创建具有5x4颜色矩阵的颜色滤波器。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

matrix为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述matrix表示矩阵，以长度为20的浮点数组表示。

**返回：**

类型说明[OH_Drawing_ColorFilter](../../topics/graphics/OH_Drawing_ColorFilter.md)*返回创建的颜色滤波器对象的指针。

#### OH_Drawing_ColorFilterCreateLinearToSrgbGamma()

```ets
OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateLinearToSrgbGamma(void)
```

**描述**

创建一个从线性颜色空间转换到SRGB颜色空间的颜色滤波器。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

类型说明[OH_Drawing_ColorFilter](../../topics/graphics/OH_Drawing_ColorFilter.md)*返回创建的颜色滤波器对象的指针。

#### OH_Drawing_ColorFilterCreateSrgbGammaToLinear()

```ets
OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateSrgbGammaToLinear(void)
```

**描述**

创建颜色滤波器将RGB颜色通道应用于SRGB的伽玛曲线。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

类型说明[OH_Drawing_ColorFilter](../../topics/graphics/OH_Drawing_ColorFilter.md)*返回创建的颜色滤波器对象的指针。

#### OH_Drawing_ColorFilterCreateLuma()

```ets
OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateLuma(void)
```

**描述**

创建一个颜色滤波器将其输入的亮度值乘以透明度通道，并将红色、绿色和蓝色通道设置为零。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

类型说明[OH_Drawing_ColorFilter](../../topics/graphics/OH_Drawing_ColorFilter.md)*返回创建的颜色滤波器对象的指针。

#### OH_Drawing_ColorFilterCreateLighting()

```ets
OH_Drawing_ColorFilter* OH_Drawing_ColorFilterCreateLighting(uint32_t mulColor, uint32_t addColor)
```

**描述**

创建一个光照颜色滤波器，此滤波器会将RGB通道的颜色值乘以一种颜色值并加上另一种颜色值，计算结果会被限制在0到255范围内。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述uint32_t mulColor用来乘法运算的颜色值。uint32_t addColor用来加法运算的颜色值。

**返回：**

类型说明[OH_Drawing_ColorFilter](../../topics/graphics/OH_Drawing_ColorFilter.md)*返回创建的颜色滤波器对象的指针。

#### OH_Drawing_ColorFilterDestroy()

```ets
void OH_Drawing_ColorFilterDestroy(OH_Drawing_ColorFilter* colorFilter)
```

**描述**

销毁颜色滤波器对象，并收回该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_ColorFilter](../../topics/graphics/OH_Drawing_ColorFilter.md)* colorFilter表示指向颜色滤波器对象的指针。