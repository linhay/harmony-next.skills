# drawing_typeface.h

**概述**

文件中定义了与字形相关的功能函数。

不同的平台有自己的默认字形，也可以从ttf文件解析出三方指定字形，如宋体、黑体字形等。

引用文件： <native_drawing/drawing_typeface.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

相关模块： [Drawing](Drawing.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_Typeface* OH_Drawing_TypefaceCreateDefault(void) | 用于创建一个默认的字形对象。 |
| OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFile(const char* path, int index) | 通过文件创建一个字形对象。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFileWithArguments(const char* path,const OH_Drawing_FontArguments* fontArguments) | 从指定文件路径创建带有字型参数的字体对象。 如果字体对象不支持字型参数中描述的可变维度，此函数将会创建默认字型参数的字体对象。 在这种情况下，此函数将提供与OH_Drawing_TypefaceCreateFromFile相同的功能。 |
| OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromCurrent(const OH_Drawing_Typeface* current,const OH_Drawing_FontArguments* fontArguments) | 通过已存在的字体对象创建带有字型参数的字体对象。 |
| OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromStream(OH_Drawing_MemoryStream* memoryStream, int32_t index) | 通过内存流创建一个字形对象。如果内存流是无效的字体文件，返回空指针。内存流传入后，所有权转移，开发者不能再释放它。 本接口会产生错误码，可以通过OH_Drawing_ErrorCodeGet查看错误码的取值。 memoryStream为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。 |
| void OH_Drawing_TypefaceDestroy(OH_Drawing_Typeface* typeface) | 用于销毁字形对象并回收该对象占有的内存。 |
| OH_Drawing_FontArguments* OH_Drawing_FontArgumentsCreate(void) | 用于创建一个字型参数对象。字型参数用于创建带有自定义属性的字体对象。 |
| OH_Drawing_ErrorCode OH_Drawing_FontArgumentsAddVariation(OH_Drawing_FontArguments* fontArguments,const char* axis, float value) | 给字型参数对象添加可变维度。 |
| OH_Drawing_ErrorCode OH_Drawing_FontArgumentsDestroy(OH_Drawing_FontArguments* fontArguments) | 用于销毁一个字型参数对象。 |
| OH_Drawing_ErrorCode OH_Drawing_TypefaceIsBold(const OH_Drawing_Typeface* typeface, bool* isBold) | 检查字形是否为粗体。 |
| OH_Drawing_ErrorCode OH_Drawing_TypefaceIsItalic(const OH_Drawing_Typeface* typeface, bool* isItalic) | 检查字形是否为斜体。 |

**函数说明**

**OH_Drawing_TypefaceCreateDefault()**

```ets
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateDefault(void)
```

描述

用于创建一个默认的字形对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Typeface* | 返回一个指针，指针指向创建的字形对象。 |

**OH_Drawing_TypefaceCreateFromFile()**

```ets
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFile(const char* path, int index)
```

描述

通过文件创建一个字形对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* path | 指向文件路径的指针。 |
| int index | 文件索引。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Typeface* | 函数返回一个指针，指针指向创建的字形对象OH_Drawing_Typeface。 |

**OH_Drawing_TypefaceCreateFromFileWithArguments()**

```ets
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFileWithArguments(const char* path,const OH_Drawing_FontArguments* fontArguments)
```

描述

从指定文件路径创建带有字型参数的字体对象。

如果字体对象不支持字型参数中描述的可变维度，此函数将会创建默认字型参数的字体对象。

在这种情况下，此函数将提供与[OH_Drawing_TypefaceCreateFromFile](drawing_typeface.h.md#ZH-CN_TOPIC_0000002522082170__oh_drawing_typefacecreatefromfile)相同的功能。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* path | 指向字体对象所在文件路径的指针。 |
| const OH_Drawing_FontArguments* fontArguments | 指向字型参数对象OH_Drawing_FontArguments的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Typeface* | 函数返回一个指针，指针指向创建的字体对象OH_Drawing_Typeface。  如果返回的对象指针为空，则表示字体对象创建失败。失败的原因可能为：没有可用的内存、传入的文件路径对象指针或字型参数为空、传入的路径无效。 |

**OH_Drawing_TypefaceCreateFromCurrent()**

```ets
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromCurrent(const OH_Drawing_Typeface* current,const OH_Drawing_FontArguments* fontArguments)
```

描述

通过已存在的字体对象创建带有字型参数的字体对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Typeface* current | 指向字体对象OH_Drawing_Typeface的指针。 |
| const OH_Drawing_FontArguments* fontArguments | 指向字型参数对象OH_Drawing_FontArguments的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Typeface* | 函数返回一个指针，指针指向创建的字体对象OH_Drawing_Typeface。  如果返回的对象指针为空，则表示字体对象创建失败。失败的原因可能为：没有可用的内存、传入的文件路径对象指针或字型参数为空、传入的字体对象不支持字型参数对象中描述的可变维度。 |

**OH_Drawing_TypefaceCreateFromStream()**

```ets
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromStream(OH_Drawing_MemoryStream* memoryStream, int32_t index)
```

描述

通过内存流创建一个字形对象。如果内存流是无效的字体文件，返回空指针。内存流传入后，所有权转移，开发者不能再释放它。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002553362073__oh_drawing_errorcodeget)查看错误码的取值。

memoryStream为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_MemoryStream* memoryStream | 指向内存流对象OH_Drawing_MemoryStream的指针。 |
| int32_t index | 内存流索引。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Typeface* | 返回一个指针，指针指向创建的字形对象OH_Drawing_Typeface。 |

**OH_Drawing_TypefaceDestroy()**

```ets
void OH_Drawing_TypefaceDestroy(OH_Drawing_Typeface* typeface)
```

描述

用于销毁字形对象并回收该对象占有的内存。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Typeface* typeface | 指向字形对象的指针。 |

**OH_Drawing_FontArgumentsCreate()**

```ets
OH_Drawing_FontArguments* OH_Drawing_FontArgumentsCreate(void)
```

描述

用于创建一个字型参数对象。字型参数用于创建带有自定义属性的字体对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 13

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_FontArguments* | 返回一个指针，指针指向创建的字型参数对象。 |

**OH_Drawing_FontArgumentsAddVariation()**

```ets
OH_Drawing_ErrorCode OH_Drawing_FontArgumentsAddVariation(OH_Drawing_FontArguments* fontArguments,const char* axis, float value)
```

描述

给字型参数对象添加可变维度。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_FontArguments* fontArguments | 指向字型参数对象OH_Drawing_FontArguments的指针。 |
| const char* axis | 字型参数对象可变维度的标签，必须为4个ASCII字符。具体可支持的标签取决于加载的字体文件，如'wght'即为字重标签。 |
| float value | 可变维度标签对应的取值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数fontArguments或axis任意一个为NULL或者axis的长度不为4。 |

**OH_Drawing_FontArgumentsDestroy()**

```ets
OH_Drawing_ErrorCode OH_Drawing_FontArgumentsDestroy(OH_Drawing_FontArguments* fontArguments)
```

描述

用于销毁一个字型参数对象。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_FontArguments* fontArguments | 指向字型参数对象OH_Drawing_FontArguments的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行错误码。  返回OH_DRAWING_SUCCESS，表示执行成功。  返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数fontArguments为NULL。 |

**OH_Drawing_TypefaceIsBold()**

```ets
OH_Drawing_ErrorCode OH_Drawing_TypefaceIsBold(const OH_Drawing_Typeface* typeface, bool* isBold)
```

描述

检查字形是否为粗体。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Typeface* typeface | 指向字形对象OH_Drawing_Typeface的指针。 |
| bool* isBold | 表示字形是否为粗体。作为出参使用。true表示该字形是粗体，false表示该字形不是粗体。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 OH_DRAWING_SUCCESS，表示执行成功。 OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示typeface或isBold是空指针。 |

**OH_Drawing_TypefaceIsItalic()**

```ets
OH_Drawing_ErrorCode OH_Drawing_TypefaceIsItalic(const OH_Drawing_Typeface* typeface, bool* isItalic)
```

描述

检查字形是否为斜体。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_Typeface* typeface | 指向字形对象OH_Drawing_Typeface的指针。 |
| bool* isItalic | 表示字形是否为斜体。作为出参使用。true表示该字形是斜体，false表示该字形不是斜体。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数返回执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示typeface或isItalic是空指针。 |