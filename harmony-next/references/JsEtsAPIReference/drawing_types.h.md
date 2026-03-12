# drawing_types.h

#### 概述

文件中定义了用于绘制2d图形的数据类型，包括画布、画笔、画刷、位图和路径。

**引用文件：** <native_drawing/drawing_types.h>

**库：** libnative_drawing.so

**起始版本：** 8

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_Drawing_Point2D](OH_Drawing_Point2D.md)OH_Drawing_Point2D定义一个二维的坐标点。[OH_Drawing_Point3D](OH_Drawing_Point3D.md)OH_Drawing_Point3D定义一个三维的坐标点。[OH_Drawing_Image_Info](OH_Drawing_Image_Info.md)OH_Drawing_Image_Info定义图片信息结构体。[OH_Drawing_RectStyle_Info](OH_Drawing_RectStyle_Info.md)OH_Drawing_RectStyle_Info定义矩形框样式结构体。[OH_Drawing_String](OH_Drawing_String.md)OH_Drawing_String采用UTF-16编码的字符串信息结构体。[OH_Drawing_Canvas](OH_Drawing_Canvas.md)OH_Drawing_Canvas定义为一块矩形的画布，可以结合画笔和画刷在上面绘制各种形状、图片和文字。[OH_Drawing_Pen](OH_Drawing_Pen.md)OH_Drawing_Pen定义为画笔，画笔用于描述绘制图形轮廓的样式和颜色。[OH_Drawing_Region](OH_Drawing_Region.md)OH_Drawing_Region定义一个区域，用于表示画布上的封闭区域，实现更精确的图形控制。[OH_Drawing_Brush](OH_Drawing_Brush.md)OH_Drawing_Brush定义为画刷，画刷用于描述填充图形的样式和颜色。[OH_Drawing_Path](OH_Drawing_Path.md)OH_Drawing_Path定义为路径，路径用于自定义各种形状。[OH_Drawing_Bitmap](OH_Drawing_Bitmap.md)OH_Drawing_Bitmap定义为位图，位图是一块内存，内存中包含了描述一张图片的像素数据。[OH_Drawing_Point](OH_Drawing_Point.md)OH_Drawing_Point定义一个点，用于描述坐标点。[OH_Drawing_PixelMap](OH_Drawing_PixelMap.md)OH_Drawing_PixelMap定义像素图，用于包装图像框架支持的真实像素图。[OH_Drawing_ColorSpace](OH_Drawing_ColorSpace.md)OH_Drawing_ColorSpace定义色彩空间，用于解释颜色信息。[OH_Drawing_PathEffect](OH_Drawing_PathEffect.md)OH_Drawing_PathEffect定义一个路径效果，用于影响描边路径。[OH_Drawing_Rect](OH_Drawing_Rect.md)OH_Drawing_Rect用于描述矩形。[OH_Drawing_RoundRect](OH_Drawing_RoundRect.md)OH_Drawing_RoundRect用于描述圆角矩形。[OH_Drawing_Matrix](OH_Drawing_Matrix.md)OH_Drawing_Matrix定义一个矩阵，用于描述坐标变换。[OH_Drawing_ShaderEffect](OH_Drawing_ShaderEffect.md)OH_Drawing_ShaderEffect定义一个着色器，用于描述绘制内容的源颜色。[OH_Drawing_ShadowLayer](OH_Drawing_ShadowLayer.md)OH_Drawing_ShadowLayer定义一个阴影层，用于描述绘制内容的阴影层。[OH_Drawing_Filter](OH_Drawing_Filter.md)OH_Drawing_Filter定义一个滤波器，用于存储颜色滤波器，蒙版滤波器和图像滤波器。[OH_Drawing_MaskFilter](OH_Drawing_MaskFilter.md)OH_Drawing_MaskFilter定义蒙版滤波器。[OH_Drawing_ColorFilter](OH_Drawing_ColorFilter.md)OH_Drawing_ColorFilter定义颜色滤波器，传入一个颜色并返回一个新的颜色。[OH_Drawing_Font](OH_Drawing_Font.md)OH_Drawing_Font用于描述字体。[OH_Drawing_FontFeatures](OH_Drawing_FontFeatures.md)OH_Drawing_FontFeatures用于描述字体特征容器。字体特征是字体内置的排版规则，控制字形显示。例如：连字、替代字形、上下标等。[OH_Drawing_MemoryStream](OH_Drawing_MemoryStream.md)OH_Drawing_MemoryStream用于描述内存流。[OH_Drawing_FontArguments](OH_Drawing_FontArguments.md)OH_Drawing_FontArguments用于描述字型参数。[OH_Drawing_Typeface](OH_Drawing_Typeface.md)OH_Drawing_Typeface用于描述字形。[OH_Drawing_TextBlob](OH_Drawing_TextBlob.md)OH_Drawing_TextBlob定义一个文本对象，表示将多个文本组合到一个不可变的容器中。每个文本行由字形和位置组成。[OH_Drawing_Image](OH_Drawing_Image.md)OH_Drawing_Image定义一个用于描述绘制二维像素数组的图片。[OH_Drawing_ImageFilter](OH_Drawing_ImageFilter.md)OH_Drawing_ImageFilter定义图像滤波器, 用于对构成图像像素的所有颜色位进行操作。[OH_Drawing_SamplingOptions](OH_Drawing_SamplingOptions.md)OH_Drawing_SamplingOptions定义一个采样选项，用于描述图片、位图等图像的采样方法。[OH_Drawing_TextBlobBuilder](OH_Drawing_TextBlobBuilder.md)OH_Drawing_TextBlobBuilder定义文本构建器，用于构建文本。[OH_Drawing_GpuContext](OH_Drawing_GpuContext.md)OH_Drawing_GpuContext定义图形处理器上下文，用于描述图形处理器后端上下文。[OH_Drawing_Surface](OH_Drawing_Surface.md)OH_Drawing_Surface定义surface，用于管理画布绘制的内容。[OH_Drawing_FontMgr](OH_Drawing_FontMgr.md)OH_Drawing_FontMgr定义字体管理类, 用于字体管理。[OH_Drawing_FontStyleSet](OH_Drawing_FontStyleSet.md)OH_Drawing_FontStyleSet定义字体样式集, 用于字体样式族匹配。[OH_Drawing_RecordCmdUtils](OH_Drawing_RecordCmdUtils.md)OH_Drawing_RecordCmdUtils定义指令录制工具，用于生成录制指令。[OH_Drawing_RecordCmd](OH_Drawing_RecordCmd.md)OH_Drawing_RecordCmd定义录制指令类, 用于存储录制指令的集合。[OH_Drawing_Array](OH_Drawing_Array.md)OH_Drawing_Array定义数组对象, 用于存储多个同类型对象。

#### 枚举

名称typedef关键字描述[OH_Drawing_ColorFormat](#ZH-CN_TOPIC_0000002529286007__oh_drawing_colorformat)OH_Drawing_ColorFormat用于描述位图像素的存储格式。[OH_Drawing_AlphaFormat](#ZH-CN_TOPIC_0000002529286007__oh_drawing_alphaformat)OH_Drawing_AlphaFormat用于描述位图像素的透明度分量。[OH_Drawing_BlendMode](#ZH-CN_TOPIC_0000002529286007__oh_drawing_blendmode)OH_Drawing_BlendMode

混合模式枚举。混合模式的操作会为两种颜色（源色、目标色）生成一种新的颜色。

这些操作在红、绿、蓝3个颜色通道上是相同的（透明度有另外的处理规则）。

对于这些，我们使用透明度通道作为示例，而不是单独命名每个通道。为简洁起见，我们使用以下缩写：

s : source，源的缩写。

d : destination，目标的缩写。

sa : source alpha，源透明度的缩写。

da : destination alpha，目标透明度的缩写。

计算结果用如下缩写表示：

r : 如果4个通道的计算方式相同，用r表示。

ra : 如果只操作透明度通道，用ra表示。

rc : 如果操作3个颜色通道，用rc表示。

[OH_Drawing_TextEncoding](#ZH-CN_TOPIC_0000002529286007__oh_drawing_textencoding)OH_Drawing_TextEncoding文本编码类型枚举。

#### 枚举类型说明

#### OH_Drawing_ColorFormat

```ets
enum OH_Drawing_ColorFormat
```

**描述**

用于描述位图像素的存储格式。

**起始版本：** 8

枚举项描述COLOR_FORMAT_UNKNOWN未知格式。COLOR_FORMAT_ALPHA_8每个像素用一个8位的量表示，8个比特位表示透明度。COLOR_FORMAT_RGB_565每个像素用一个16位的量表示，高位到低位依次是5个比特位表示红，6个比特位表示绿，5个比特位表示蓝。COLOR_FORMAT_ARGB_4444每个像素用一个16位的量表示，高位到低位依次是4个比特位表示透明度，4个比特位表示红，4个比特位表示绿，4个比特位表示蓝。COLOR_FORMAT_RGBA_8888每个像素用一个32位的量表示，高位到低位依次是8个比特位表示透明度，8个比特位表示红，8个比特位表示绿，8个比特位表示蓝。COLOR_FORMAT_BGRA_8888每个像素用一个32位的量表示，高位到低位依次是8个比特位表示蓝，8个比特位表示绿，8个比特位表示红，8个比特位表示透明度。

#### OH_Drawing_AlphaFormat

```ets
enum OH_Drawing_AlphaFormat
```

**描述**

用于描述位图像素的透明度分量。

**起始版本：** 8

枚举项描述ALPHA_FORMAT_UNKNOWN未知格式。ALPHA_FORMAT_OPAQUE位图无透明度。ALPHA_FORMAT_PREMUL每个像素的颜色组件由透明度分量预先乘以。ALPHA_FORMAT_UNPREMUL每个像素的颜色组件未由透明度分量预先乘以。

#### OH_Drawing_BlendMode

```ets
enum OH_Drawing_BlendMode
```

**描述**

混合模式枚举。混合模式的操作会为两种颜色（源色、目标色）生成一种新的颜色。

这些操作在红、绿、蓝3个颜色通道上是相同的（透明度有另外的处理规则）。

对于这些，我们使用透明度通道作为示例，而不是单独命名每个通道。为简洁起见，我们使用以下缩写：

s : source，源的缩写。

d : destination，目标的缩写。

sa : source alpha，源透明度的缩写。

da : destination alpha，目标透明度的缩写。

计算结果用如下缩写表示：

r : 如果4个通道的计算方式相同，用r表示。

ra : 如果只操作透明度通道，用ra表示。

rc : 如果操作3个颜色通道，用rc表示。

**起始版本：** 11

枚举项描述BLEND_MODE_CLEAR清除模式，r = 0。BLEND_MODE_SRCr = s（result的4个通道，都等于source的4个通道，即结果等于源。）BLEND_MODE_DSTr = d（result的4个通道，都等于destination的4个通道，即结果等于目标。）BLEND_MODE_SRC_OVERr = s + (1 - sa) * d。BLEND_MODE_DST_OVERr = d + (1 - da) * s。BLEND_MODE_SRC_INr = s * da。BLEND_MODE_DST_INr = d * sa。BLEND_MODE_SRC_OUTr = s * (1 - da)。BLEND_MODE_DST_OUTr = d * (1 - sa)。BLEND_MODE_SRC_ATOPr = s * da + d * (1 - sa)。BLEND_MODE_DST_ATOPr = d * sa + s * (1 - da)。BLEND_MODE_XORr = s * (1 - da) + d * (1 - sa)。BLEND_MODE_PLUSr = min(s + d, 1)。BLEND_MODE_MODULATEr = s * d。BLEND_MODE_SCREEN滤色模式，r = s + d - s * d。BLEND_MODE_OVERLAY叠加模式。BLEND_MODE_DARKEN变暗模式，rc = s + d - max(s * da, d * sa), ra = s + (1 - sa) * d。BLEND_MODE_LIGHTEN变亮模式，rc = s + d - min(s * da, d * sa), ra = s + (1 - sa) * d。BLEND_MODE_COLOR_DODGE颜色减淡模式。BLEND_MODE_COLOR_BURN颜色加深模式。BLEND_MODE_HARD_LIGHT强光模式。BLEND_MODE_SOFT_LIGHT柔光模式。BLEND_MODE_DIFFERENCE差值模式，rc = s + d - 2 * (min(s * da, d * sa)), ra = s + (1 - sa) * d。BLEND_MODE_EXCLUSION排除模式，rc = s + d - two(s * d), ra = s + (1 - sa) * d。BLEND_MODE_MULTIPLY正片叠底，r = s * (1 - da) + d * (1 - sa) + s * d。BLEND_MODE_HUE色相模式。BLEND_MODE_SATURATION饱和度模式。BLEND_MODE_COLOR颜色模式。BLEND_MODE_LUMINOSITY亮度模式。

#### OH_Drawing_TextEncoding

```ets
enum OH_Drawing_TextEncoding
```

**描述**

文本编码类型枚举。

**起始版本：** 12

枚举项描述TEXT_ENCODING_UTF8单字节，表示UTF-8或ASCII。TEXT_ENCODING_UTF16双字节，表示大部分Unicode。TEXT_ENCODING_UTF32四字节，表示所有Unicode。TEXT_ENCODING_GLYPH_ID双字节，表示字形索引。