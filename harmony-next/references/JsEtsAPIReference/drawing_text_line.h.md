# drawing_text_line.h

#### 概述

提供获取文本行内的字符位置、获取渲染单元信息和按行截断等功能。

**引用文件：** <native_drawing/drawing_text_line.h>

**库：** libnative_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 函数

名称typedef关键字描述[OH_Drawing_Array* OH_Drawing_TypographyGetTextLines(OH_Drawing_Typography* typography)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_typographygettextlines)-获取排版对象的文本行数组。文本行数组中包含一个或多个文本行对象。不再需要[OH_Drawing_Array](zh-cn_topic_0000002497446088.html)时，请使用[OH_Drawing_DestroyTextLines](drawing_text_line.h.md#ZH-CN_TOPIC_0000002497446034__oh_drawing_destroytextlines)接口释放该对象的指针。[void OH_Drawing_DestroyTextLines(OH_Drawing_Array* lines)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_destroytextlines)-释放文本行数组的内存。[void OH_Drawing_DestroyTextLine(OH_Drawing_TextLine* line)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_destroytextline)-释放单个文本行对象的内存。只能释放单独申请内存的文本行对象，不能释放文本行数组中的某一个文本行对象的内存。[OH_Drawing_TextLine* OH_Drawing_GetTextLineByIndex(OH_Drawing_Array* lines, size_t index)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_gettextlinebyindex)-获取文本行数组指定索引处的文本行对象。[double OH_Drawing_TextLineGetGlyphCount(OH_Drawing_TextLine* line)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinegetglyphcount)-获取文本行对象中字形的数量。[void OH_Drawing_TextLineGetTextRange(OH_Drawing_TextLine* line, size_t* start, size_t* end)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinegettextrange)-获取文本行对象中的文本在整个段落文本中的索引区间。[OH_Drawing_Array* OH_Drawing_TextLineGetGlyphRuns(OH_Drawing_TextLine* line)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinegetglyphruns)-获取文本行对象中的文本渲染单元数组。[void OH_Drawing_DestroyRuns(OH_Drawing_Array* runs)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_destroyruns)-释放文本渲染单元数组的内存。[OH_Drawing_Run* OH_Drawing_GetRunByIndex(OH_Drawing_Array* runs, size_t index)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_getrunbyindex)-获取文本渲染单元数组指定索引处的文本渲染单元对象。[void OH_Drawing_TextLinePaint(OH_Drawing_TextLine* line, OH_Drawing_Canvas* canvas, double x, double y)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinepaint)-在画布上以坐标点 (x, y) 为左上角位置绘制文本行。[OH_Drawing_TextLine* OH_Drawing_TextLineCreateTruncatedLine(OH_Drawing_TextLine* line, double width, int mode,const char* ellipsis)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinecreatetruncatedline)-创建一个截断的文本行对象。[double OH_Drawing_TextLineGetTypographicBounds(OH_Drawing_TextLine* line, double* ascent, double* descent,double* leading)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinegettypographicbounds)-

获取文本行对象的排版边界。文本行排版边界与排版字体、排版字号有关，与字符本身无关。

例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，排版边界就包括行首和末尾空格的边界。例如字符串为"j"或"E"，排版边界相同，即与字符本身无关。

[OH_Drawing_Rect* OH_Drawing_TextLineGetImageBounds(OH_Drawing_TextLine* line)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinegetimagebounds)-

获取文本行对象的图像边界。文本行图像边界与排版字体、排版字号、字符本身都有关，相当于视觉边界。

例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格,用户在界面上只能看到"a b"，图像边界即为不包括带行首和末尾空格的边界。

例如字符串为"j"或"E"，视觉边界不同，即与字符本身有关，"j"字符串的视觉边界宽度小于"E"字符串的视觉边界宽度，"j"字符串的视觉边界高度大于"E"字符串的视觉边界高度。

[double OH_Drawing_TextLineGetTrailingSpaceWidth(OH_Drawing_TextLine* line)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinegettrailingspacewidth)-获取文本行对象尾部空白字符的宽度。[int32_t OH_Drawing_TextLineGetStringIndexForPosition(OH_Drawing_TextLine* line, OH_Drawing_Point* point)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinegetstringindexforposition)-获取文本行对象中指定位置处的字符索引。[double OH_Drawing_TextLineGetOffsetForStringIndex(OH_Drawing_TextLine* line, int32_t index)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinegetoffsetforstringindex)-获取文本行对象中指定字符串索引处的偏移量。[typedef bool (*Drawing_CaretOffsetsCallback)(double offset, int32_t index, bool leadingEdge)](#ZH-CN_TOPIC_0000002497446034__drawing_caretoffsetscallback)Drawing_CaretOffsetsCallback用户自定义的回调函数。将文本行对象中每个字符的偏移量、索引值作为参数传递给用户自定义的回调函数。[void OH_Drawing_TextLineEnumerateCaretOffsets(OH_Drawing_TextLine* line, Drawing_CaretOffsetsCallback callback)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlineenumeratecaretoffsets)-枚举文本行对象中每个字符的偏移量和索引值，传递给用户自定义的回调函数，用户可以使用偏移量和索引值进行其他操作。[double OH_Drawing_TextLineGetAlignmentOffset(OH_Drawing_TextLine* line, double alignmentFactor, double alignmentWidth)](#ZH-CN_TOPIC_0000002497446034__oh_drawing_textlinegetalignmentoffset)-获取文本行对象根据对齐因子和对齐宽度计算对齐后所需的偏移量。

#### 函数说明

#### OH_Drawing_TypographyGetTextLines()

```ets
OH_Drawing_Array* OH_Drawing_TypographyGetTextLines(OH_Drawing_Typography* typography)
```

**描述**

获取排版对象的文本行数组。文本行数组中包含一个或多个文本行对象。不再需要[OH_Drawing_Array](OH_Drawing_Array.md)时，请使用[OH_Drawing_DestroyTextLines](drawing_text_line.h.md#ZH-CN_TOPIC_0000002497446034__oh_drawing_destroytextlines)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_Typography](OH_Drawing_Typography.md)* typography指向排版对象[OH_Drawing_Typography](OH_Drawing_Typography.md)的指针。

**返回：**

类型说明[OH_Drawing_Array](OH_Drawing_Array.md)*指向文本行数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针。

#### OH_Drawing_DestroyTextLines()

```ets
void OH_Drawing_DestroyTextLines(OH_Drawing_Array* lines)
```

**描述**

释放文本行数组的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_Array](OH_Drawing_Array.md)* lines指向文本行数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针。

#### OH_Drawing_DestroyTextLine()

```ets
void OH_Drawing_DestroyTextLine(OH_Drawing_TextLine* line)
```

**描述**

释放单个文本行对象的内存。只能释放单独申请内存的文本行对象，不能释放文本行数组中的某一个文本行对象的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。

#### OH_Drawing_GetTextLineByIndex()

```ets
OH_Drawing_TextLine* OH_Drawing_GetTextLineByIndex(OH_Drawing_Array* lines, size_t index)
```

**描述**

获取文本行数组指定索引处的文本行对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_Array](OH_Drawing_Array.md)* lines指向文本行数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针。size_t index指定的文本行数组的索引。

**返回：**

类型说明[OH_Drawing_TextLine](OH_Drawing_TextLine.md)*指向指定索引处的文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。

#### OH_Drawing_TextLineGetGlyphCount()

```ets
double OH_Drawing_TextLineGetGlyphCount(OH_Drawing_TextLine* line)
```

**描述**

获取文本行对象中字形的数量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。

**返回：**

类型说明double文本行对象中字形的数量。

#### OH_Drawing_TextLineGetTextRange()

```ets
void OH_Drawing_TextLineGetTextRange(OH_Drawing_TextLine* line, size_t* start, size_t* end)
```

**描述**

获取文本行对象中的文本在整个段落文本中的索引区间。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。size_t* start指向区间左侧端点索引的指针。size_t* end指向区间右侧端点索引的指针。

#### OH_Drawing_TextLineGetGlyphRuns()

```ets
OH_Drawing_Array* OH_Drawing_TextLineGetGlyphRuns(OH_Drawing_TextLine* line)
```

**描述**

获取文本行对象中的文本渲染单元数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。

**返回：**

类型说明[OH_Drawing_Array](OH_Drawing_Array.md)*指向文本渲染单元[OH_Drawing_Run](OH_Drawing_Run.md)数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针，不再需要[OH_Drawing_Array](OH_Drawing_Array.md)时，请使用[OH_Drawing_DestroyRuns](drawing_text_line.h.md#ZH-CN_TOPIC_0000002497446034__oh_drawing_destroyruns)释放该对象的指针。

#### OH_Drawing_DestroyRuns()

```ets
void OH_Drawing_DestroyRuns(OH_Drawing_Array* runs)
```

**描述**

释放文本渲染单元数组的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_Array](OH_Drawing_Array.md)* runs指向文本渲染单元[OH_Drawing_Run](OH_Drawing_Run.md)数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针。

#### OH_Drawing_GetRunByIndex()

```ets
OH_Drawing_Run* OH_Drawing_GetRunByIndex(OH_Drawing_Array* runs, size_t index)
```

**描述**

获取文本渲染单元数组指定索引处的文本渲染单元对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_Array](OH_Drawing_Array.md)* runs指向文本渲染单元[OH_Drawing_Run](OH_Drawing_Run.md)数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针。size_t index文本渲染单元数组的索引。

**返回：**

类型说明[OH_Drawing_Run](OH_Drawing_Run.md)*指向指定索引处的文本渲染单元对象[OH_Drawing_Run](OH_Drawing_Run.md)的指针。

#### OH_Drawing_TextLinePaint()

```ets
void OH_Drawing_TextLinePaint(OH_Drawing_TextLine* line, OH_Drawing_Canvas* canvas, double x, double y)
```

**描述**

在画布上以坐标点 (x, y) 为左上角位置绘制文本行。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。[OH_Drawing_Canvas](OH_Drawing_Canvas.md)* canvas指向绘制的目标画布[OH_Drawing_Canvas](OH_Drawing_Canvas.md)。double x绘制的左上角位置的横坐标，单位为物理像素px。double y绘制的左上角位置的纵坐标，单位为物理像素px。

#### OH_Drawing_TextLineCreateTruncatedLine()

```ets
OH_Drawing_TextLine* OH_Drawing_TextLineCreateTruncatedLine(OH_Drawing_TextLine* line, double width, int mode,const char* ellipsis)
```

**描述**

创建一个截断的文本行对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。double width截断后的行宽度。int mode截断的类型，取值对应为 [OH_Drawing_EllipsisModal](drawing_text_typography.h.md#ZH-CN_TOPIC_0000002497606016__oh_drawing_ellipsismodal) 枚举，当前仅支持头部截断ELLIPSIS_MODAL_HEAD和尾部截断ELLIPSIS_MODAL_TAIL。const char* ellipsis截断的标记字符串。

**返回：**

类型说明[OH_Drawing_TextLine](OH_Drawing_TextLine.md)*返回指向截断的文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)指针。

#### OH_Drawing_TextLineGetTypographicBounds()

```ets
double OH_Drawing_TextLineGetTypographicBounds(OH_Drawing_TextLine* line, double* ascent, double* descent,double* leading)
```

**描述**

获取文本行对象的排版边界。文本行排版边界与排版字体、排版字号有关，与字符本身无关。

例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格，排版边界就包括行首和末尾空格的边界。例如字符串为"j"或"E"，排版边界相同，即与字符本身无关。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。height = ascent + descent + leading。double* ascent指向文本行对象上升高度的指针。double* descent指向文本行对象下降高度的指针。double* leading指向文本行对象行间距的指针。

**返回：**

类型说明double排版边界的总宽度。

#### OH_Drawing_TextLineGetImageBounds()

```ets
OH_Drawing_Rect* OH_Drawing_TextLineGetImageBounds(OH_Drawing_TextLine* line)
```

**描述**

获取文本行对象的图像边界。文本行图像边界与排版字体、排版字号、字符本身都有关，相当于视觉边界。

例如字符串为" a b "，'a'字符前面有1个空格，'b'字符后面有1个空格,用户在界面上只能看到"a b"，图像边界即为不包括带行首和末尾空格的边界。

例如字符串为"j"或"E"，视觉边界不同，即与字符本身有关，"j"字符串的视觉边界宽度小于"E"字符串的视觉边界宽度，"j"字符串的视觉边界高度大于"E"字符串的视觉边界高度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。

**返回：**

类型说明[OH_Drawing_Rect](OH_Drawing_Rect.md)*指向文本行对象的图像边界[OH_Drawing_Rect](OH_Drawing_Rect.md)的指针，不再需要[OH_Drawing_Rect](OH_Drawing_Rect.md)时，请使用[OH_Drawing_RectDestroy](drawing_rect.h.md#ZH-CN_TOPIC_0000002497446028__oh_drawing_rectdestroy)接口释放该对象的指针。

#### OH_Drawing_TextLineGetTrailingSpaceWidth()

```ets
double OH_Drawing_TextLineGetTrailingSpaceWidth(OH_Drawing_TextLine* line)
```

**描述**

获取文本行对象尾部空白字符的宽度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。

**返回：**

类型说明double文本行对象尾部空白字符的宽度。

#### OH_Drawing_TextLineGetStringIndexForPosition()

```ets
int32_t OH_Drawing_TextLineGetStringIndexForPosition(OH_Drawing_TextLine* line, OH_Drawing_Point* point)
```

**描述**

获取文本行对象中指定位置处的字符索引。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。[OH_Drawing_Point](OH_Drawing_Point.md)* point指向要查找索引的位置[OH_Drawing_Point](OH_Drawing_Point.md)指针。

**返回：**

类型说明int32_t指定位置处的字符串索引。例如文本字符串为"abc"，"a"字符的索引为0，"b"字符的索引为1，"c"字符的索引为2。如果指定的位置在"a"字符处，则返回0。

#### OH_Drawing_TextLineGetOffsetForStringIndex()

```ets
double OH_Drawing_TextLineGetOffsetForStringIndex(OH_Drawing_TextLine* line, int32_t index)
```

**描述**

获取文本行对象中指定字符串索引处的偏移量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。int32_t index要获取偏移量的字符串索引。

**返回：**

类型说明double指定字符串索引处的偏移量。

#### Drawing_CaretOffsetsCallback()

```ets
typedef bool (*Drawing_CaretOffsetsCallback)(double offset, int32_t index, bool leadingEdge)
```

**描述**

用户自定义的回调函数。将文本行对象中每个字符的偏移量、索引值作为参数传递给用户自定义的回调函数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述double offset文本行对象中每个字符的偏移量。int32_t index文本行对象中每个字符的索引值。bool leadingEdge光标是否位于字符的前缘。true表示位于字符前缘，即偏移量不包含该字符宽度，false表示位于字符后缘，即偏移量包含该字符宽度。

**返回：**

类型说明bool表示是否停止调用该回调函数。true表示停止调用该回调函数，false表示继续调用该回调函数。

#### OH_Drawing_TextLineEnumerateCaretOffsets()

```ets
void OH_Drawing_TextLineEnumerateCaretOffsets(OH_Drawing_TextLine* line, Drawing_CaretOffsetsCallback callback)
```

**描述**

枚举文本行对象中每个字符的偏移量和索引值，传递给用户自定义的回调函数，用户可以使用偏移量和索引值进行其他操作。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。[Drawing_CaretOffsetsCallback](#ZH-CN_TOPIC_0000002497446034__drawing_caretoffsetscallback) callback用户自定义函数[Drawing_CaretOffsetsCallback](zh-cn_topic_0000002497446034.html#ZH-CN_TOPIC_0000002497446034__drawing_caretoffsetscallback)。

#### OH_Drawing_TextLineGetAlignmentOffset()

```ets
double OH_Drawing_TextLineGetAlignmentOffset(OH_Drawing_TextLine* line, double alignmentFactor, double alignmentWidth)
```

**描述**

获取文本行对象根据对齐因子和对齐宽度计算对齐后所需的偏移量。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_TextLine](OH_Drawing_TextLine.md)* line指向文本行对象[OH_Drawing_TextLine](OH_Drawing_TextLine.md)的指针。double alignmentFactor对齐因子，即对齐的程度。小于等于0.0表示左对齐，大于0.0小于0.5表示偏左对齐，0.5表示居中对齐，大于0.5小于1.0表示偏右对齐，大于等于1.0表示右对齐。double alignmentWidth对齐宽度，即最终偏移后的文本行对象右下角相对于起始位置的偏移值。如果指定对齐宽度小于文本行对象的实际宽度，则返回0。

**返回：**

类型说明double计算得到的对齐所需偏移量。