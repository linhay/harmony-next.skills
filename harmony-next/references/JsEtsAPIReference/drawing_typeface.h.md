# drawing_typeface.h

#### 概述

文件中定义了与字形相关的功能函数。

不同的平台有自己的默认字形，也可以从ttf文件解析出三方指定字形，如宋体、黑体字形等。

**引用文件：** <native_drawing/drawing_typeface.h>

**库：** libnative_drawing.so

**起始版本：** 11

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 函数

名称描述[OH_Drawing_Typeface* OH_Drawing_TypefaceCreateDefault(void)](#ZH-CN_TOPIC_0000002497446036__oh_drawing_typefacecreatedefault)用于创建一个默认的字形对象。[OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFile(const char* path, int index)](#ZH-CN_TOPIC_0000002497446036__oh_drawing_typefacecreatefromfile)

通过文件创建一个字形对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFileWithArguments(const char* path,const OH_Drawing_FontArguments* fontArguments)](#ZH-CN_TOPIC_0000002497446036__oh_drawing_typefacecreatefromfilewitharguments)

从指定文件路径创建带有字型参数的字体对象。

如果字体对象不支持字型参数中描述的可变维度，此函数将会创建默认字型参数的字体对象。

在这种情况下，此函数将提供与[OH_Drawing_TypefaceCreateFromFile](drawing_typeface.h.md#ZH-CN_TOPIC_0000002497446036__oh_drawing_typefacecreatefromfile)相同的功能。

[OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromCurrent(const OH_Drawing_Typeface* current,const OH_Drawing_FontArguments* fontArguments)](#ZH-CN_TOPIC_0000002497446036__oh_drawing_typefacecreatefromcurrent)通过已存在的字体对象创建带有字型参数的字体对象。[OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromStream(OH_Drawing_MemoryStream* memoryStream, int32_t index)](#ZH-CN_TOPIC_0000002497446036__oh_drawing_typefacecreatefromstream)

通过内存流创建一个字形对象。如果内存流是无效的字体文件，返回空指针。内存流传入后，所有权转移，开发者不能再释放它。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

memoryStream为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_TypefaceDestroy(OH_Drawing_Typeface* typeface)](#ZH-CN_TOPIC_0000002497446036__oh_drawing_typefacedestroy)用于销毁字形对象并回收该对象占有的内存。[OH_Drawing_FontArguments* OH_Drawing_FontArgumentsCreate(void)](#ZH-CN_TOPIC_0000002497446036__oh_drawing_fontargumentscreate)用于创建一个字型参数对象。字型参数用于创建带有自定义属性的字体对象。[OH_Drawing_ErrorCode OH_Drawing_FontArgumentsAddVariation(OH_Drawing_FontArguments* fontArguments,const char* axis, float value)](#ZH-CN_TOPIC_0000002497446036__oh_drawing_fontargumentsaddvariation)给字型参数对象添加可变维度。[OH_Drawing_ErrorCode OH_Drawing_FontArgumentsDestroy(OH_Drawing_FontArguments* fontArguments)](#ZH-CN_TOPIC_0000002497446036__oh_drawing_fontargumentsdestroy)用于销毁一个字型参数对象。

#### 函数说明

#### OH_Drawing_TypefaceCreateDefault()

```ets
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateDefault(void)
```

**描述**

用于创建一个默认的字形对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

类型说明[OH_Drawing_Typeface](OH_Drawing_Typeface.md)*返回一个指针，指针指向创建的字形对象。

#### OH_Drawing_TypefaceCreateFromFile()

```ets
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFile(const char* path, int index)
```

**描述**

通过文件创建一个字形对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述const char* path指向文件路径的指针。int index文件索引。

**返回：**

类型说明[OH_Drawing_Typeface](OH_Drawing_Typeface.md)*函数返回一个指针，指针指向创建的字形对象[OH_Drawing_Typeface](OH_Drawing_Typeface.md)。

#### OH_Drawing_TypefaceCreateFromFileWithArguments()

```ets
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFileWithArguments(const char* path,const OH_Drawing_FontArguments* fontArguments)
```

**描述**

从指定文件路径创建带有字型参数的字体对象。

如果字体对象不支持字型参数中描述的可变维度，此函数将会创建默认字型参数的字体对象。

在这种情况下，此函数将提供与[OH_Drawing_TypefaceCreateFromFile](drawing_typeface.h.md#ZH-CN_TOPIC_0000002497446036__oh_drawing_typefacecreatefromfile)相同的功能。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

参数项描述const char* path指向字体对象所在文件路径的指针。const [OH_Drawing_FontArguments](OH_Drawing_FontArguments.md)* fontArguments指向字型参数对象[OH_Drawing_FontArguments](OH_Drawing_FontArguments.md)的指针。

**返回：**

类型说明[OH_Drawing_Typeface](OH_Drawing_Typeface.md)*

函数返回一个指针，指针指向创建的字体对象[OH_Drawing_Typeface](OH_Drawing_Typeface.md)。

 如果返回的对象指针为空，则表示字体对象创建失败。失败的原因可能为：没有可用的内存、传入的文件路径对象指针或字型参数为空、传入的路径无效。

#### OH_Drawing_TypefaceCreateFromCurrent()

```ets
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromCurrent(const OH_Drawing_Typeface* current,const OH_Drawing_FontArguments* fontArguments)
```

**描述**

通过已存在的字体对象创建带有字型参数的字体对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

参数项描述const [OH_Drawing_Typeface](OH_Drawing_Typeface.md)* current指向字体对象[OH_Drawing_Typeface](OH_Drawing_Typeface.md)的指针。const [OH_Drawing_FontArguments](OH_Drawing_FontArguments.md)* fontArguments指向字型参数对象[OH_Drawing_FontArguments](OH_Drawing_FontArguments.md)的指针。

**返回：**

类型说明[OH_Drawing_Typeface](OH_Drawing_Typeface.md)*

函数返回一个指针，指针指向创建的字体对象[OH_Drawing_Typeface](OH_Drawing_Typeface.md)。

 如果返回的对象指针为空，则表示字体对象创建失败。失败的原因可能为：没有可用的内存、传入的文件路径对象指针或字型参数为空、传入的字体对象不支持字型参数对象中描述的可变维度。

#### OH_Drawing_TypefaceCreateFromStream()

```ets
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromStream(OH_Drawing_MemoryStream* memoryStream, int32_t index)
```

**描述**

通过内存流创建一个字形对象。如果内存流是无效的字体文件，返回空指针。内存流传入后，所有权转移，开发者不能再释放它。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

memoryStream为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_MemoryStream](OH_Drawing_MemoryStream.md)* memoryStream指向内存流对象[OH_Drawing_MemoryStream](OH_Drawing_MemoryStream.md)的指针。int32_t index内存流索引。

**返回：**

类型说明[OH_Drawing_Typeface](OH_Drawing_Typeface.md)*返回一个指针，指针指向创建的字形对象[OH_Drawing_Typeface](OH_Drawing_Typeface.md)。

#### OH_Drawing_TypefaceDestroy()

```ets
void OH_Drawing_TypefaceDestroy(OH_Drawing_Typeface* typeface)
```

**描述**

用于销毁字形对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_Typeface](OH_Drawing_Typeface.md)* typeface指向字形对象的指针。

#### OH_Drawing_FontArgumentsCreate()

```ets
OH_Drawing_FontArguments* OH_Drawing_FontArgumentsCreate(void)
```

**描述**

用于创建一个字型参数对象。字型参数用于创建带有自定义属性的字体对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**返回：**

类型说明[OH_Drawing_FontArguments](OH_Drawing_FontArguments.md)*返回一个指针，指针指向创建的字型参数对象。

#### OH_Drawing_FontArgumentsAddVariation()

```ets
OH_Drawing_ErrorCode OH_Drawing_FontArgumentsAddVariation(OH_Drawing_FontArguments* fontArguments,const char* axis, float value)
```

**描述**

给字型参数对象添加可变维度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

参数项描述[OH_Drawing_FontArguments](OH_Drawing_FontArguments.md)* fontArguments指向字型参数对象[OH_Drawing_FontArguments](OH_Drawing_FontArguments.md)的指针。const char* axis字型参数对象可变维度的标签，必须为4个ASCII字符。具体可支持的标签取决于加载的字体文件，如'wght'即为字重标签。float value可变维度标签对应的取值。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行错误码。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数fontArguments或axis任意一个为NULL或者axis的长度不为4。

#### OH_Drawing_FontArgumentsDestroy()

```ets
OH_Drawing_ErrorCode OH_Drawing_FontArgumentsDestroy(OH_Drawing_FontArguments* fontArguments)
```

**描述**

用于销毁一个字型参数对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

参数项描述[OH_Drawing_FontArguments](OH_Drawing_FontArguments.md)* fontArguments指向字型参数对象[OH_Drawing_FontArguments](OH_Drawing_FontArguments.md)的指针。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数返回执行错误码。

 返回OH_DRAWING_SUCCESS，表示执行成功。

 返回OH_DRAWING_ERROR_INVALID_PARAMETER，表示参数fontArguments为NULL。