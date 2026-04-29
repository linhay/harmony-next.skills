# drawing_text_run.h

**概述**

提供字体渲染单元的相关接口，比如绘制功能、获取排版边界功能等。

引用文件： <native_drawing/drawing_text_run.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

相关模块： [Drawing](Drawing.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_Array* OH_Drawing_GetRunStringIndices(OH_Drawing_Run* run, int64_t start, int64_t length) | 获取渲染单元指定范围内字形的字符索引数组，该索引是相对于整个段落的偏移。 |
| uint64_t OH_Drawing_GetRunStringIndicesByIndex(OH_Drawing_Array* stringIndices, size_t index) | 获取字符索引数组中指定下标的字符索引值。 |
| void OH_Drawing_DestroyRunStringIndices(OH_Drawing_Array* stringIndices) | 释放字形的字符索引数组对象指针。 |
| void OH_Drawing_GetRunStringRange(OH_Drawing_Run* run, uint64_t* location, uint64_t* length) | 获取渲染单元生成字形的字符范围。 |
| float OH_Drawing_GetRunTypographicBounds(OH_Drawing_Run* run, float* ascent, float* descent, float* leading) | 获取渲染单元的排版边界。文本排版边界与字符本身无关，与排版字号和字体有关。 |
| void OH_Drawing_RunPaint(OH_Drawing_Canvas* canvas, OH_Drawing_Run* run, double x, double y) | 在画布上绘制渲染单元包含的文本。 |
| OH_Drawing_Rect* OH_Drawing_GetRunImageBounds(OH_Drawing_Run* run) | 获取渲染单元的图像边界，文本图像边界与字符本身有关，相当于视觉边界。 |
| void OH_Drawing_DestroyRunImageBounds(OH_Drawing_Rect* rect) | 释放渲染单元图像边界对象指针。 |
| OH_Drawing_Array* OH_Drawing_GetRunGlyphs(OH_Drawing_Run* run, int64_t start, int64_t length) | 获取渲染单元指定范围内的字形数组。 |
| uint16_t OH_Drawing_GetRunGlyphsByIndex(OH_Drawing_Array* glyphs, size_t index) | 根据索引获取渲染单元单个字形。 |
| void OH_Drawing_DestroyRunGlyphs(OH_Drawing_Array* glyphs) | 释放渲染单元字形数组对象指针。 |
| OH_Drawing_Array* OH_Drawing_GetRunPositions(OH_Drawing_Run* run, int64_t start, int64_t length) | 获取渲染单元指定范围内字形的位置。 |
| OH_Drawing_Point* OH_Drawing_GetRunPositionsByIndex(OH_Drawing_Array* positions, size_t index) | 根据索引获取渲染单元中单个字形位置。 |
| void OH_Drawing_DestroyRunPositions(OH_Drawing_Array* positions) | 释放渲染单元字形位置数组对象指针。 |
| uint32_t OH_Drawing_GetRunGlyphCount(OH_Drawing_Run* run) | 获取渲染单元字形数量。 |
| OH_Drawing_Font* OH_Drawing_GetRunFont(OH_Drawing_Run* run) | 获取渲染单元字体对象。 |
| OH_Drawing_TextDirection OH_Drawing_GetRunTextDirection(OH_Drawing_Run* run) | 获取渲染单元文本方向。 |
| OH_Drawing_Array* OH_Drawing_GetRunGlyphAdvances(OH_Drawing_Run* run, uint32_t start, uint32_t length) | 获取渲染单元字形宽度数组。 |
| OH_Drawing_Point* OH_Drawing_GetRunGlyphAdvanceByIndex(OH_Drawing_Array* advances, size_t index) | 根据索引获取渲染单元中单个字形宽度。 |
| void OH_Drawing_DestroyRunGlyphAdvances(OH_Drawing_Array* advances) | 释放渲染单元字形宽度数组对象的指针。 |

**函数说明**

**OH_Drawing_GetRunStringIndices()**

```ets
OH_Drawing_Array* OH_Drawing_GetRunStringIndices(OH_Drawing_Run* run, int64_t start, int64_t length)
```

描述

获取渲染单元指定范围内字形的字符索引数组，该索引是相对于整个段落的偏移。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |
| int64_t start | 渲染单元内指定的开始位置，传入负数时该方法返回空指针。 |
| int64_t length | 渲染单元内指定的长度，length为0时获取渲染单元的所有字符索引数组，length小于0时该方法返回空指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Array* | 返回字形的字符索引数组，不再需要OH_Drawing_Array时，请使用OH_Drawing_DestroyRunStringIndices接口释放该对象的指针。 |

**OH_Drawing_GetRunStringIndicesByIndex()**

```ets
uint64_t OH_Drawing_GetRunStringIndicesByIndex(OH_Drawing_Array* stringIndices, size_t index)
```

描述

获取字符索引数组中指定下标的字符索引值。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* stringIndices | 字符索引数组。 |
| size_t index | 渲染单元字形的字符索引数组下标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint64_t | 返回渲染单元单个字形的字符索引。 |

**OH_Drawing_DestroyRunStringIndices()**

```ets
void OH_Drawing_DestroyRunStringIndices(OH_Drawing_Array* stringIndices)
```

描述

释放字形的字符索引数组对象指针。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* stringIndices | 字符索引数组。 |

**OH_Drawing_GetRunStringRange()**

```ets
void OH_Drawing_GetRunStringRange(OH_Drawing_Run* run, uint64_t* location, uint64_t* length)
```

描述

获取渲染单元生成字形的字符范围。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |
| uint64_t* location | 表示渲染单元字形的字符范围的开始位置，该位置是相对于整个段落的偏移。 |
| uint64_t* length | 表示渲染单元字符范围的长度。 |

**OH_Drawing_GetRunTypographicBounds()**

```ets
float OH_Drawing_GetRunTypographicBounds(OH_Drawing_Run* run, float* ascent, float* descent, float* leading)
```

描述

获取渲染单元的排版边界。文本排版边界与字符本身无关，与排版字号和字体有关。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |
| float* ascent | 渲染单元中最高字符到基准线的距离。 |
| float* descent | 渲染单元中最低字符到基准线的距离。 |
| float* leading | 渲染单元行间距。 |

返回：

| 类型 | 说明 |
| --- | --- |
| float | 返回渲染单元排版宽度。 |

**OH_Drawing_RunPaint()**

```ets
void OH_Drawing_RunPaint(OH_Drawing_Canvas* canvas, OH_Drawing_Run* run, double x, double y)
```

描述

在画布上绘制渲染单元包含的文本。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Canvas* canvas | 指向画布OH_Drawing_Canvas对象的指针。 |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |
| double x | 渲染单元x坐标。 |
| double y | 渲染单元y坐标。 |

**OH_Drawing_GetRunImageBounds()**

```ets
OH_Drawing_Rect* OH_Drawing_GetRunImageBounds(OH_Drawing_Run* run)
```

描述

获取渲染单元的图像边界，文本图像边界与字符本身有关，相当于视觉边界。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Rect* | 返回指向渲染单元图像边界OH_Drawing_Rect对象的指针，不再需要OH_Drawing_Rect时，请使用OH_Drawing_DestroyRunImageBounds接口释放该对象的指针。 |

**OH_Drawing_DestroyRunImageBounds()**

```ets
void OH_Drawing_DestroyRunImageBounds(OH_Drawing_Rect* rect)
```

描述

释放渲染单元图像边界对象指针。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Rect* rect | 指向渲染单元图像边界OH_Drawing_Rect对象的指针。 |

**OH_Drawing_GetRunGlyphs()**

```ets
OH_Drawing_Array* OH_Drawing_GetRunGlyphs(OH_Drawing_Run* run, int64_t start, int64_t length)
```

描述

获取渲染单元指定范围内的字形数组。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |
| int64_t start | 渲染单元内指定的开始位置，传入负数时该方法返回空指针。 |
| int64_t length | 渲染单元内指定的长度，length为0时获取渲染单元的所有字符索引，length小于0时该方法返回空指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Array* | 返回指向渲染单元字形数组OH_Drawing_Array对象的指针，不再需要OH_Drawing_Array时，请使用OH_Drawing_DestroyRunGlyphs接口释放该对象的指针。 |

**OH_Drawing_GetRunGlyphsByIndex()**

```ets
uint16_t OH_Drawing_GetRunGlyphsByIndex(OH_Drawing_Array* glyphs, size_t index)
```

描述

根据索引获取渲染单元单个字形。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* glyphs | 指向渲染单元字形数组OH_Drawing_Array对象的指针。 |
| size_t index | 渲染单元字形数组下标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint16_t | 渲染单元单个字形。 |

**OH_Drawing_DestroyRunGlyphs()**

```ets
void OH_Drawing_DestroyRunGlyphs(OH_Drawing_Array* glyphs)
```

描述

释放渲染单元字形数组对象指针。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* glyphs | 指向渲染单元字形数组OH_Drawing_Array对象的指针。 |

**OH_Drawing_GetRunPositions()**

```ets
OH_Drawing_Array* OH_Drawing_GetRunPositions(OH_Drawing_Run* run, int64_t start, int64_t length)
```

描述

获取渲染单元指定范围内字形的位置。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |
| int64_t start | 渲染单元内指定的开始位置，传入负数时该方法返回空指针。 |
| int64_t length | 渲染单元内指定的长度，length为0时获取渲染单元的所有字符索引，length小于0时该方法返回空指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Array* | 返回指向渲染单元字形位置数组OH_Drawing_Array对象的指针，不再需要OH_Drawing_Array时，请使用OH_Drawing_DestroyRunPositions接口释放该对象的指针。 |

**OH_Drawing_GetRunPositionsByIndex()**

```ets
OH_Drawing_Point* OH_Drawing_GetRunPositionsByIndex(OH_Drawing_Array* positions, size_t index)
```

描述

根据索引获取渲染单元中单个字形位置。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* positions | 指向渲染单元字形位置数组OH_Drawing_Array对象的指针。 |
| size_t index | 渲染单元字形位置数组下标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Point* | 返回指向渲染单元单个字形位置OH_Drawing_Point对象的指针。 |

**OH_Drawing_DestroyRunPositions()**

```ets
void OH_Drawing_DestroyRunPositions(OH_Drawing_Array* positions)
```

描述

释放渲染单元字形位置数组对象指针。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* positions | 指向渲染单元字形位置数组OH_Drawing_Array对象的指针。 |

**OH_Drawing_GetRunGlyphCount()**

```ets
uint32_t OH_Drawing_GetRunGlyphCount(OH_Drawing_Run* run)
```

描述

获取渲染单元字形数量。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 返回渲染单元字形数量。 |

**OH_Drawing_GetRunFont()**

```ets
OH_Drawing_Font* OH_Drawing_GetRunFont(OH_Drawing_Run* run)
```

描述

获取渲染单元字体对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Font* | 返回指向渲染单元字体OH_Drawing_Font对象的指针，不再需要OH_Drawing_Font时，请使用OH_Drawing_FontDestroy接口释放该对象的指针。 |

**OH_Drawing_GetRunTextDirection()**

```ets
OH_Drawing_TextDirection OH_Drawing_GetRunTextDirection(OH_Drawing_Run* run)
```

描述

获取渲染单元文本方向。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_TextDirection | 返回渲染单元的文本方向。0为TEXT_DIRECTION_RTL，方向为从右到左；1为TEXT_DIRECTION_LTR，方向为从左到右，具体可见OH_Drawing_TextDirection枚举。 |

**OH_Drawing_GetRunGlyphAdvances()**

```ets
OH_Drawing_Array* OH_Drawing_GetRunGlyphAdvances(OH_Drawing_Run* run, uint32_t start, uint32_t length)
```

描述

获取渲染单元字形宽度数组。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Run* run | 指向渲染单元OH_Drawing_Run对象的指针。 |
| uint32_t start | 渲染单元内指定的开始位置，传入负数时该方法返回空指针。 |
| uint32_t length | 渲染单元内指定的长度，如果length是0表示从start开始获取到渲染单元结束，length小于0时该方法返回空指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Array* | 返回指向渲染单元字形宽度数组OH_Drawing_Array对象的指针，不再需要OH_Drawing_Array时，请使用OH_Drawing_DestroyRunGlyphAdvances接口释放该对象的指针。 |

**OH_Drawing_GetRunGlyphAdvanceByIndex()**

```ets
OH_Drawing_Point* OH_Drawing_GetRunGlyphAdvanceByIndex(OH_Drawing_Array* advances, size_t index)
```

描述

根据索引获取渲染单元中单个字形宽度。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* advances | 指向渲染单元字形宽度数组OH_Drawing_Array对象的指针。 |
| size_t index | 渲染单元字形宽度数组的下标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Point* | 返回指向渲染单元单个字形宽度OH_Drawing_Point对象的指针。其中，OH_Drawing_Point对象的x值代表渲染单元单个字形宽度，y值为保留字段，默认返回0。 |

**OH_Drawing_DestroyRunGlyphAdvances()**

```ets
void OH_Drawing_DestroyRunGlyphAdvances(OH_Drawing_Array* advances)
```

描述

释放渲染单元字形宽度数组对象的指针。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* advances | 指向渲染单元字形宽度数组OH_Drawing_Array对象的指针。 |