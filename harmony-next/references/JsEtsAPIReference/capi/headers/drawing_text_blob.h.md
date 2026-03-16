# drawing_text_blob.h

#### 概述

文件中定义了与文字相关的功能函数。

**引用文件：** <native_drawing/drawing_text_blob.h>

**库：** libnative_drawing.so

**起始版本：** 11

**相关模块：**[Drawing](../../topics/graphics/Drawing.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_Drawing_RunBuffer](../../topics/graphics/OH_Drawing_RunBuffer.md)OH_Drawing_RunBuffer结构体用于描述一块内存，描述文字和位置信息。

#### 函数

名称描述[OH_Drawing_TextBlobBuilder* OH_Drawing_TextBlobBuilderCreate(void)](#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobbuildercreate)用于创建一个文本构造器对象。[OH_Drawing_TextBlob* OH_Drawing_TextBlobCreateFromText(const void* text, size_t byteLength,const OH_Drawing_Font* font, OH_Drawing_TextEncoding textEncoding)](#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobcreatefromtext)

使用文本创建一个文本对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

text、font任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

textEncoding不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[OH_Drawing_TextBlob* OH_Drawing_TextBlobCreateFromPosText(const void* text, size_t byteLength,OH_Drawing_Point2D* point2D, const OH_Drawing_Font* font, OH_Drawing_TextEncoding textEncoding)](#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobcreatefrompostext)

使用文本创建文本对象，文本对象中每个字符的坐标由OH_Drawing_Point2D数组中对应的坐标信息决定。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

text、point2D、font任意一个为NULL或byteLength等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

textEncoding不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[OH_Drawing_TextBlob* OH_Drawing_TextBlobCreateFromString(const char* str,const OH_Drawing_Font* font, OH_Drawing_TextEncoding textEncoding)](#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobcreatefromstring)

使用字符串创建文本对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

str、font任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

textEncoding不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

[void OH_Drawing_TextBlobGetBounds(OH_Drawing_TextBlob* textBlob, OH_Drawing_Rect* rect)](#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobgetbounds)

获取文本对象的边界范围。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

textBlob、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[uint32_t OH_Drawing_TextBlobUniqueID(const OH_Drawing_TextBlob* textBlob)](#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobuniqueid)

获取文本的标识符，该标识符是唯一的非零值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

textBlob为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[const OH_Drawing_RunBuffer* OH_Drawing_TextBlobBuilderAllocRunPos(OH_Drawing_TextBlobBuilder* textBlobBuilder,const OH_Drawing_Font* font, int32_t count, const OH_Drawing_Rect* rect)](#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobbuilderallocrunpos)

申请一块内存，用于存储文字和位置信息。返回的指针无需调用者管理，当调用[OH_Drawing_TextBlobBuilderMake](drawing_text_blob.h.md#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobbuildermake)后禁止使用。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

textBlobBuilder、font任意一个为NULL或者count小于等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[OH_Drawing_TextBlob* OH_Drawing_TextBlobBuilderMake(OH_Drawing_TextBlobBuilder* textBlobBuilder)](#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobbuildermake)

用于从文本构造器中创建文本对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

textBlobBuilder为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_TextBlobDestroy(OH_Drawing_TextBlob* textBlob)](#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobdestroy)用于销毁文本对象并回收该对象占有的内存。[void OH_Drawing_TextBlobBuilderDestroy(OH_Drawing_TextBlobBuilder* textBlobBuilder)](#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobbuilderdestroy)用于销毁文本构造器对象并回收该对象占有的内存。

#### 函数说明

#### OH_Drawing_TextBlobBuilderCreate()

```ets
OH_Drawing_TextBlobBuilder* OH_Drawing_TextBlobBuilderCreate(void)
```

**描述**

用于创建一个文本构造器对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

类型说明[OH_Drawing_TextBlobBuilder](../../topics/components/OH_Drawing_TextBlobBuilder.md)*函数会返回一个指针，指针指向创建的文本构造器对象。

#### OH_Drawing_TextBlobCreateFromText()

```ets
OH_Drawing_TextBlob* OH_Drawing_TextBlobCreateFromText(const void* text, size_t byteLength,const OH_Drawing_Font* font, OH_Drawing_TextEncoding textEncoding)
```

**描述**

使用文本创建一个文本对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

text、font任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

textEncoding不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述const void* text指向文本的指针。size_t byteLength文本的字节长度。const [OH_Drawing_Font](../../topics/graphics/OH_Drawing_Font.md)* font指向字体对象[OH_Drawing_Font](../../topics/graphics/OH_Drawing_Font.md)的指针。[OH_Drawing_TextEncoding](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_textencoding) textEncoding文本编码类型[OH_Drawing_TextEncoding](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_textencoding)。

**返回：**

类型说明[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)*函数返回一个指针，指针指向创建的文本对象[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)。

#### OH_Drawing_TextBlobCreateFromPosText()

```ets
OH_Drawing_TextBlob* OH_Drawing_TextBlobCreateFromPosText(const void* text, size_t byteLength,OH_Drawing_Point2D* point2D, const OH_Drawing_Font* font, OH_Drawing_TextEncoding textEncoding)
```

**描述**

使用文本创建文本对象，文本对象中每个字符的坐标由OH_Drawing_Point2D数组中对应的坐标信息决定。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

text、point2D、font任意一个为NULL或byteLength等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

textEncoding不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述const void* text指向文本的指针。size_t byteLength文本的字节长度。[OH_Drawing_Point2D](../../topics/graphics/OH_Drawing_Point2D.md)* point2D二维点[OH_Drawing_Point2D](../../topics/graphics/OH_Drawing_Point2D.md)数组首地址，数组个数由[OH_Drawing_FontCountText](drawing_font.h.md#ZH-CN_TOPIC_0000002529285991__oh_drawing_fontcounttext)计算结果决定。const [OH_Drawing_Font](../../topics/graphics/OH_Drawing_Font.md)* font指向字体对象[OH_Drawing_Font](../../topics/graphics/OH_Drawing_Font.md)的指针。[OH_Drawing_TextEncoding](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_textencoding) textEncoding文本编码类型[OH_Drawing_TextEncoding](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_textencoding)。

**返回：**

类型说明[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)*函数返回一个指针，指针指向创建的文本对象[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)。

#### OH_Drawing_TextBlobCreateFromString()

```ets
OH_Drawing_TextBlob* OH_Drawing_TextBlobCreateFromString(const char* str,const OH_Drawing_Font* font, OH_Drawing_TextEncoding textEncoding)
```

**描述**

使用字符串创建文本对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

str、font任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER；

textEncoding不在枚举范围内返回OH_DRAWING_ERROR_PARAMETER_OUT_OF_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述const char* str指向字符串的指针。const [OH_Drawing_Font](../../topics/graphics/OH_Drawing_Font.md)* font指向字体对象[OH_Drawing_Font](../../topics/graphics/OH_Drawing_Font.md)的指针。[OH_Drawing_TextEncoding](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_textencoding) textEncoding文本编码类型[OH_Drawing_TextEncoding](drawing_types.h.md#ZH-CN_TOPIC_0000002529286007__oh_drawing_textencoding)。

**返回：**

类型说明[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)*函数返回一个指针，指针指向创建的文本对象[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)。

#### OH_Drawing_TextBlobGetBounds()

```ets
void OH_Drawing_TextBlobGetBounds(OH_Drawing_TextBlob* textBlob, OH_Drawing_Rect* rect)
```

**描述**

获取文本对象的边界范围。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

textBlob、rect任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)* textBlob指向文本对象[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)的指针。[OH_Drawing_Rect](../../topics/graphics/OH_Drawing_Rect.md)* rect指向矩形对象[OH_Drawing_Rect](../../topics/graphics/OH_Drawing_Rect.md)的指针，开发者可调用[OH_Drawing_Rect](../../topics/graphics/OH_Drawing_Rect.md)接口创建。

#### OH_Drawing_TextBlobUniqueID()

```ets
uint32_t OH_Drawing_TextBlobUniqueID(const OH_Drawing_TextBlob* textBlob)
```

**描述**

获取文本的标识符，该标识符是唯一的非零值。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

textBlob为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述const [OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)* textBlob指向文本对象[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)的指针。

**返回：**

类型说明uint32_t返回文本对象的标识符。

#### OH_Drawing_TextBlobBuilderAllocRunPos()

```ets
const OH_Drawing_RunBuffer* OH_Drawing_TextBlobBuilderAllocRunPos(OH_Drawing_TextBlobBuilder* textBlobBuilder,const OH_Drawing_Font* font, int32_t count, const OH_Drawing_Rect* rect)
```

**描述**

申请一块内存，用于存储文字和位置信息。返回的指针无需调用者管理，当调用[OH_Drawing_TextBlobBuilderMake](drawing_text_blob.h.md#ZH-CN_TOPIC_0000002497446032__oh_drawing_textblobbuildermake)后禁止使用。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

textBlobBuilder、font任意一个为NULL或者count小于等于0时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_TextBlobBuilder](../../topics/components/OH_Drawing_TextBlobBuilder.md)* textBlobBuilder指向文本构造器对象的指针。const [OH_Drawing_Font](../../topics/graphics/OH_Drawing_Font.md)* font指向字体对象的指针。int32_t count文字的数量。const [OH_Drawing_Rect](../../topics/graphics/OH_Drawing_Rect.md)* rect文本的边界框，为NULL表示不设置边界框。

#### OH_Drawing_TextBlobBuilderMake()

```ets
OH_Drawing_TextBlob* OH_Drawing_TextBlobBuilderMake(OH_Drawing_TextBlobBuilder* textBlobBuilder)
```

**描述**

用于从文本构造器中创建文本对象。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

textBlobBuilder为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_TextBlobBuilder](../../topics/components/OH_Drawing_TextBlobBuilder.md)* textBlobBuilder指向文本构造器对象的指针。

**返回：**

类型说明[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)*返回一个指针，指针指向创建的文本对象。

#### OH_Drawing_TextBlobDestroy()

```ets
void OH_Drawing_TextBlobDestroy(OH_Drawing_TextBlob* textBlob)
```

**描述**

用于销毁文本对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_TextBlob](../../topics/graphics/OH_Drawing_TextBlob.md)* textBlob指向文本对象的指针。

#### OH_Drawing_TextBlobBuilderDestroy()

```ets
void OH_Drawing_TextBlobBuilderDestroy(OH_Drawing_TextBlobBuilder* textBlobBuilder)
```

**描述**

用于销毁文本构造器对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_TextBlobBuilder](../../topics/components/OH_Drawing_TextBlobBuilder.md)* textBlobBuilder指向文本构造器对象的指针。