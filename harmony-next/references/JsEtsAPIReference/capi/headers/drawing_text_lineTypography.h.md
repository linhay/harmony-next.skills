# drawing_text_lineTypography.h

#### 概述

提供排版行相关的接口，比如获取指定位置处开始可以排版的字符个数等函数。

**引用文件：** <native_drawing/drawing_text_lineTypography.h>

**库：** libnative_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**相关模块：**[Drawing](../../topics/graphics/Drawing.md)

#### 汇总

#### 函数

名称描述[OH_Drawing_LineTypography* OH_Drawing_CreateLineTypography(OH_Drawing_TypographyCreate* handler)](#ZH-CN_TOPIC_0000002529286005__oh_drawing_createlinetypography)创建一个排版行对象[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)的指针，排版行对象保存着文本内容以及样式的载体，可以用于计算单行排版信息。[void OH_Drawing_DestroyLineTypography(OH_Drawing_LineTypography* lineTypography)](#ZH-CN_TOPIC_0000002529286005__oh_drawing_destroylinetypography)释放排版行对象[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)占用的内存。[size_t OH_Drawing_LineTypographyGetLineBreak(OH_Drawing_LineTypography* lineTypography,size_t startIndex, double width)](#ZH-CN_TOPIC_0000002529286005__oh_drawing_linetypographygetlinebreak)计算在限定排版宽度的情况下，从指定位置处开始可以排版的字符个数。[OH_Drawing_TextLine* OH_Drawing_LineTypographyCreateLine(OH_Drawing_LineTypography* lineTypography,size_t startIndex, size_t count)](#ZH-CN_TOPIC_0000002529286005__oh_drawing_linetypographycreateline)根据指定区间文本内容创建一个指向文本行对象[OH_Drawing_TextLine](../../topics/graphics/OH_Drawing_TextLine.md)的指针。

#### 函数说明

#### OH_Drawing_CreateLineTypography()

```ets
OH_Drawing_LineTypography* OH_Drawing_CreateLineTypography(OH_Drawing_TypographyCreate* handler)
```

**描述**

创建一个排版行对象[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)的指针，排版行对象保存着文本内容以及样式的载体，可以用于计算单行排版信息。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TypographyCreate](../../topics/graphics/OH_Drawing_TypographyCreate.md)* handler指向[OH_Drawing_TypographyCreate](../../topics/graphics/OH_Drawing_TypographyCreate.md)对象的指针，由[OH_Drawing_CreateTypographyHandler](drawing_text_typography.h.md#ZH-CN_TOPIC_0000002497606016__oh_drawing_createtypographyhandler)获取。

**返回：**

类型说明[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)*返回一个指向排版行对象[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)的指针。

#### OH_Drawing_DestroyLineTypography()

```ets
void OH_Drawing_DestroyLineTypography(OH_Drawing_LineTypography* lineTypography)
```

**描述**

释放排版行对象[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)* lineTypography指向排版行对象[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)的指针，由[OH_Drawing_CreateLineTypography](drawing_text_lineTypography.h.md#ZH-CN_TOPIC_0000002529286005__oh_drawing_createlinetypography)获取。

#### OH_Drawing_LineTypographyGetLineBreak()

```ets
size_t OH_Drawing_LineTypographyGetLineBreak(OH_Drawing_LineTypography* lineTypography,size_t startIndex, double width)
```

**描述**

计算在限定排版宽度的情况下，从指定位置处开始可以排版的字符个数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)* lineTypography指向排版行对象[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)的指针，由[OH_Drawing_CreateLineTypography](drawing_text_lineTypography.h.md#ZH-CN_TOPIC_0000002529286005__oh_drawing_createlinetypography)获取。size_t startIndex开始计算排版的起始位置（包括起始位置）。取值范围需要为[0,文本字符总数）的整数。double width换行宽度，大于0的浮点数，单位为物理像素px。

**返回：**

类型说明size_t返回在限定排版宽度的情况下，从指定位置处开始可以排版的字符总数，取值为整数。

#### OH_Drawing_LineTypographyCreateLine()

```ets
OH_Drawing_TextLine* OH_Drawing_LineTypographyCreateLine(OH_Drawing_LineTypography* lineTypography,size_t startIndex, size_t count)
```

**描述**

根据指定区间文本内容创建一个指向文本行对象[OH_Drawing_TextLine](../../topics/graphics/OH_Drawing_TextLine.md)的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)* lineTypography指向排版行对象[OH_Drawing_LineTypography](../../topics/graphics/OH_Drawing_LineTypography.md)的指针，由[OH_Drawing_CreateLineTypography](drawing_text_lineTypography.h.md#ZH-CN_TOPIC_0000002529286005__oh_drawing_createlinetypography)获取。size_t startIndex表示计算排版的起始位置，整数，取值范围为[0, 文本字符总数)。size_t count

表示从指定排版起始位置开始进行排版的字符个数，取值为[0,文本字符总数)的整数，startIndex和count之和不能大于文本字符总数。

可以先使用[OH_Drawing_LineTypographyGetLineBreak](drawing_text_lineTypography.h.md#ZH-CN_TOPIC_0000002529286005__oh_drawing_linetypographygetlinebreak)获得合理的可用于进行排版的字符总数。如果该值设置为0，则返回nullptr。

**返回：**

类型说明[OH_Drawing_TextLine](../../topics/graphics/OH_Drawing_TextLine.md)*返回一个指向文本行对象[OH_Drawing_TextLine](../../topics/graphics/OH_Drawing_TextLine.md)的指针。