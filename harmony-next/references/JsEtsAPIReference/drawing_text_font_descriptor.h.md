# drawing_text_font_descriptor.h

#### 概述

定义了字体信息的相关接口，比如获取字体信息，查找指定字体等。

**引用文件：** <native_drawing/drawing_text_font_descriptor.h>

**库：** libnative_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_Drawing_SystemFontType](#ZH-CN_TOPIC_0000002529445977__oh_drawing_systemfonttype)OH_Drawing_SystemFontType字体类型的枚举。[OH_Drawing_FontFullDescriptorAttributeId](#ZH-CN_TOPIC_0000002529445977__oh_drawing_fontfulldescriptorattributeid)OH_Drawing_FontFullDescriptorAttributeId字体描述符属性的枚举。不同类型的字体描述符属性，请使用对应类型的接口获取属性。如字体描述符属性FULL_DESCRIPTOR_ATTR_I_WEIGHT为int类型，需使用[OH_Drawing_GetFontFullDescriptorAttributeInt](zh-cn_topic_0000002529445977.html#ZH-CN_TOPIC_0000002529445977__oh_drawing_getfontfulldescriptorattributeint)接口获取其属性值。

#### 函数

名称描述[OH_Drawing_FontDescriptor* OH_Drawing_MatchFontDescriptors(OH_Drawing_FontDescriptor* desc, size_t* num)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_matchfontdescriptors)

获取与指定字体描述符匹配的所有系统字体描述符，其中[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)的path字段不作为有效的匹配字段，其余字段不是默认值时生效。

如果参数desc的所有字段都是默认值，则获取所有系统字体描述符。

如果匹配失败，返回NULL。不再需要[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)时，请使用[OH_Drawing_DestroyFontDescriptors](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_destroyfontdescriptors)接口释放该对象的指针。

[void OH_Drawing_DestroyFontDescriptors(OH_Drawing_FontDescriptor* descriptors, size_t num)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_destroyfontdescriptors)释放字体描述符[OH_Drawing_FontDescriptor](zh-cn_topic_0000002529445993.html)数组。[OH_Drawing_FontDescriptor* OH_Drawing_GetFontDescriptorByFullName(const OH_Drawing_String* fullName,OH_Drawing_SystemFontType fontType)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_getfontdescriptorbyfullname)

根据字体名称和字体类型获取指定的字体描述符，支持系统字体、风格字体和用户已安装字体。

字体描述符是描述字体特征的一种数据结构，它包含了定义字体外观和属性的详细信息。

[OH_Drawing_Array* OH_Drawing_GetSystemFontFullNamesByType(OH_Drawing_SystemFontType fontType)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_getsystemfontfullnamesbytype)根据字体类型获取对应字体的字体名称数组。[const OH_Drawing_String* OH_Drawing_GetSystemFontFullNameByIndex(OH_Drawing_Array* fullNameArray, size_t index)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_getsystemfontfullnamebyindex)在字体名称数组中通过索引获取对应位置的字体名称。[void OH_Drawing_DestroySystemFontFullNames(OH_Drawing_Array* fullNameArray)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_destroysystemfontfullnames)释放通过字体类型获取的对应字体的字体名称数组占用的内存。[OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorsFromStream(const void* data, size_t size)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_getfontfulldescriptorsfromstream)根据原始二进制数据获取字体描述符数组。[OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorsFromPath(const char* path)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_getfontfulldescriptorsfrompath)根据字体文件路径获取字体描述符数组。[const OH_Drawing_FontFullDescriptor* OH_Drawing_GetFontFullDescriptorByIndex(OH_Drawing_Array* descriptorArray, size_t index)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_getfontfulldescriptorbyindex)在字体描述符数组中通过索引获取对应的字体描述符。[void OH_Drawing_DestroyFontFullDescriptors(OH_Drawing_Array* descriptorArray)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_destroyfontfulldescriptors)释放字体描述符数组占用的内存。[OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeInt(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, int* value)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_getfontfulldescriptorattributeint)获取int类型字体描述符的属性。[OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeBool(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, bool* value)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_getfontfulldescriptorattributebool)获取bool类型字体描述符的属性。[OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeString(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, OH_Drawing_String* str)](#ZH-CN_TOPIC_0000002529445977__oh_drawing_getfontfulldescriptorattributestring)获取[OH_Drawing_String](zh-cn_topic_0000002529286027.html)类型字体描述符的属性。

#### 枚举类型说明

#### OH_Drawing_SystemFontType

```ets
enum OH_Drawing_SystemFontType
```

**描述**

字体类型的枚举。

**起始版本：** 14

枚举项描述ALL = 1 << 0所有字体类型。GENERIC = 1 << 1系统字体类型。STYLISH = 1 << 2风格字体类型INSTALLED = 1 << 3用户已安装字体类型。CUSTOMIZED = 1 << 4

自定义字体类型。

**起始版本：** 18

#### OH_Drawing_FontFullDescriptorAttributeId

```ets
enum OH_Drawing_FontFullDescriptorAttributeId
```

**描述**

字体描述符属性的枚举。不同类型的字体描述符属性，请使用对应类型的接口获取属性。如字体描述符属性FULL_DESCRIPTOR_ATTR_I_WEIGHT为int类型，需使用[OH_Drawing_GetFontFullDescriptorAttributeInt](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_getfontfulldescriptorattributeint)接口获取其属性值。

**起始版本：** 22

枚举项描述FULL_DESCRIPTOR_ATTR_S_PATH = 0字体文件的路径，[OH_Drawing_String](OH_Drawing_String.md)类型。FULL_DESCRIPTOR_ATTR_S_POSTSCRIPT_NAME = 1唯一标识字体的名称，[OH_Drawing_String](OH_Drawing_String.md)类型。FULL_DESCRIPTOR_ATTR_S_FULL_NAME = 2字体的名称，[OH_Drawing_String](OH_Drawing_String.md)类型。FULL_DESCRIPTOR_ATTR_S_FAMILY_NAME = 3字体家族的名称，[OH_Drawing_String](OH_Drawing_String.md)类型。FULL_DESCRIPTOR_ATTR_S_SUB_FAMILY_NAME = 4子字体家族的名称，[OH_Drawing_String](OH_Drawing_String.md)类型。FULL_DESCRIPTOR_ATTR_I_WEIGHT = 5字体的字重，int类型。FULL_DESCRIPTOR_ATTR_I_WIDTH = 6字体的宽窄风格属性，int类型。FULL_DESCRIPTOR_ATTR_I_ITALIC = 7字体是否倾斜，int类型。1表示字体倾斜，0表示字体非倾斜。FULL_DESCRIPTOR_ATTR_B_MONO = 8字体是否紧凑，bool类型。true表示字体紧凑，false表示字体非紧凑。FULL_DESCRIPTOR_ATTR_B_SYMBOLIC = 9字体是否支持符号字体，bool类型。true表示支持符号字体，false表示不支持符号字体。

#### 函数说明

#### OH_Drawing_MatchFontDescriptors()

```ets
OH_Drawing_FontDescriptor* OH_Drawing_MatchFontDescriptors(OH_Drawing_FontDescriptor* desc, size_t* num)
```

**描述**

获取与指定字体描述符匹配的所有系统字体描述符，其中[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)的path字段不作为有效的匹配字段，其余字段不是默认值时生效。

如果参数desc的所有字段都是默认值，则获取所有系统字体描述符。

如果匹配失败，返回NULL。不再需要[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)时，请使用[OH_Drawing_DestroyFontDescriptors](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_destroyfontdescriptors)接口释放该对象的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)* desc

指针。

建议使用[OH_Drawing_CreateFontDescriptor](drawing_text_typography.h.md#ZH-CN_TOPIC_0000002497606016__oh_drawing_createfontdescriptor)获得有效的[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)实例。

如果自己创建[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)实例，请确保不用于匹配的字段是默认值。

size_t* num表示返回值数组的成员个数。

**返回：**

类型说明[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)*[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)数组，释放时请使用[OH_Drawing_DestroyFontDescriptors](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_destroyfontdescriptors)。

#### OH_Drawing_DestroyFontDescriptors()

```ets
void OH_Drawing_DestroyFontDescriptors(OH_Drawing_FontDescriptor* descriptors, size_t num)
```

**描述**

释放字体描述符[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

参数项描述[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)* descriptors数组。size_t num[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)数组的成员个数。

#### OH_Drawing_GetFontDescriptorByFullName()

```ets
OH_Drawing_FontDescriptor* OH_Drawing_GetFontDescriptorByFullName(const OH_Drawing_String* fullName,OH_Drawing_SystemFontType fontType)
```

**描述**

根据字体名称和字体类型获取指定的字体描述符，支持系统字体、风格字体和用户已安装字体。

字体描述符是描述字体特征的一种数据结构，它包含了定义字体外观和属性的详细信息。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**参数：**

参数项描述const [OH_Drawing_String](OH_Drawing_String.md)* fullName表示指向字体名称字符串[OH_Drawing_String](OH_Drawing_String.md)的指针。[OH_Drawing_SystemFontType](#ZH-CN_TOPIC_0000002529445977__oh_drawing_systemfonttype) fontType表示字体类型的枚举值[OH_Drawing_SystemFontType](zh-cn_topic_0000002529445977.html#ZH-CN_TOPIC_0000002529445977__oh_drawing_systemfonttype)。

**返回：**

类型说明[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)*指向字体描述符对象[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)的指针，不再需要[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)时，请使用[OH_Drawing_DestroyFontDescriptor](drawing_text_typography.h.md#ZH-CN_TOPIC_0000002497606016__oh_drawing_destroyfontdescriptor)接口释放该对象的指针。

#### OH_Drawing_GetSystemFontFullNamesByType()

```ets
OH_Drawing_Array* OH_Drawing_GetSystemFontFullNamesByType(OH_Drawing_SystemFontType fontType)
```

**描述**

根据字体类型获取对应字体的字体名称数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**参数：**

参数项描述[OH_Drawing_SystemFontType](#ZH-CN_TOPIC_0000002529445977__oh_drawing_systemfonttype) fontType表示字体类型的枚举值[OH_Drawing_SystemFontType](zh-cn_topic_0000002529445977.html#ZH-CN_TOPIC_0000002529445977__oh_drawing_systemfonttype)。

**返回：**

类型说明[OH_Drawing_Array](OH_Drawing_Array.md)*返回对应字体类型的字体名称数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针，不再需要[OH_Drawing_Array](OH_Drawing_Array.md)时，请使用[OH_Drawing_DestroySystemFontFullNames](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_destroysystemfontfullnames)接口释放该对象的指针。

#### OH_Drawing_GetSystemFontFullNameByIndex()

```ets
const OH_Drawing_String* OH_Drawing_GetSystemFontFullNameByIndex(OH_Drawing_Array* fullNameArray, size_t index)
```

**描述**

在字体名称数组中通过索引获取对应位置的字体名称。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**参数：**

参数项描述[OH_Drawing_Array](OH_Drawing_Array.md)* fullNameArray表示字体名称数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针。size_t index数组的索引。

**返回：**

类型说明const [OH_Drawing_String](OH_Drawing_String.md)*返回对应索引的字体名称[OH_Drawing_String](OH_Drawing_String.md)的指针。

#### OH_Drawing_DestroySystemFontFullNames()

```ets
void OH_Drawing_DestroySystemFontFullNames(OH_Drawing_Array* fullNameArray)
```

**描述**

释放通过字体类型获取的对应字体的字体名称数组占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 14

**参数：**

参数项描述[OH_Drawing_Array](OH_Drawing_Array.md)* fullNameArray表示字体名称数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针。

#### OH_Drawing_GetFontFullDescriptorsFromStream()

```ets
OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorsFromStream(const void* data, size_t size)
```

**描述**

根据原始二进制数据获取字体描述符数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

参数项描述const void* data指向原始二进制字体数据缓冲区的指针。size_t size以字节为单位的字体数据缓冲区的大小。

**返回：**

类型说明[OH_Drawing_Array*](OH_Drawing_Array.md)

返回指向对应字体文件的字体描述符数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针，不再需要OH_Drawing_Array时，请使用[OH_Drawing_DestroyFontFullDescriptors](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_destroyfontfulldescriptors)接口释放该对象的指针。

如果因数据格式无效或解析错误导致操作失败，返回NULL。

#### OH_Drawing_GetFontFullDescriptorsFromPath()

```ets
OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorsFromPath(const char* path)
```

**描述**

根据字体文件路径获取字体描述符数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

参数项描述const char* path需要查询的字体文件的路径。

**返回：**

类型说明[OH_Drawing_Array*](OH_Drawing_Array.md)

返回指向对应字体文件的字体描述符数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针，不再需要OH_Drawing_Array时，请使用[OH_Drawing_DestroyFontFullDescriptors](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_destroyfontfulldescriptors)接口释放该对象的指针。

如果字体文件未找到、字体文件路径无效、字体文件无权限或者文件非字体格式，返回NULL。

#### OH_Drawing_GetFontFullDescriptorByIndex()

```ets
const OH_Drawing_FontFullDescriptor* OH_Drawing_GetFontFullDescriptorByIndex(OH_Drawing_Array* descriptorArray, size_t index)
```

**描述**

在字体描述符数组中通过索引获取对应的字体描述符。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

参数项描述[OH_Drawing_Array](OH_Drawing_Array.md)* descriptorArray表示指向字体描述符数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针。size_t index数组的索引，索引值从0开始。

**返回：**

类型说明const [OH_Drawing_FontFullDescriptor](OH_Drawing_FontFullDescriptor.md)*

返回指向指定索引处字体描述符对象[OH_Drawing_FontFullDescriptor](OH_Drawing_FontFullDescriptor.md)的指针。

如果索引超出范围或数组无效，则返回NULL。

#### OH_Drawing_DestroyFontFullDescriptors()

```ets
void OH_Drawing_DestroyFontFullDescriptors(OH_Drawing_Array* descriptorArray)
```

**描述**

释放字体描述符数组占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

参数项描述[OH_Drawing_Array](OH_Drawing_Array.md)* descriptorArray表示指向字体描述符数组[OH_Drawing_Array](OH_Drawing_Array.md)的指针。

#### OH_Drawing_GetFontFullDescriptorAttributeInt()

```ets
OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeInt(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, int* value)
```

**描述**

获取int类型字体描述符的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

参数项描述const [OH_Drawing_FontFullDescriptor](OH_Drawing_FontFullDescriptor.md)* descriptor指向字体描述符对象[OH_Drawing_FontFullDescriptor](OH_Drawing_FontFullDescriptor.md)的指针。[OH_Drawing_FontFullDescriptorAttributeId](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_fontfulldescriptorattributeid) id字体描述符属性id。从[OH_Drawing_FontFullDescriptorAttributeId](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_fontfulldescriptorattributeid)中可获取字体描述符属性。int* value指向int类型属性的指针。作为出参使用。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数执行结果。

返回OH_DRAWING_SUCCESS，表示执行成功。

返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数descriptor或者value为空指针。

返回OH_DRAWING_ERROR_ATTRIBUTE_ID_MISMATCH，表示传入属性id与调用函数不匹配。

#### OH_Drawing_GetFontFullDescriptorAttributeBool()

```ets
OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeBool(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, bool* value)
```

**描述**

获取bool类型字体描述符的属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

参数项描述const [OH_Drawing_FontFullDescriptor](OH_Drawing_FontFullDescriptor.md)* descriptor指向字体描述符对象[OH_Drawing_FontFullDescriptor](OH_Drawing_FontFullDescriptor.md)的指针。[OH_Drawing_FontFullDescriptorAttributeId](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_fontfulldescriptorattributeid) id字体描述符属性id。从[OH_Drawing_FontFullDescriptorAttributeId](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_fontfulldescriptorattributeid)中可获取字体描述符属性。bool* value指向bool类型属性的指针。作为出参使用。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数执行结果。

返回OH_DRAWING_SUCCESS，表示执行成功。

返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数descriptor或者value为空指针。

返回OH_DRAWING_ERROR_ATTRIBUTE_ID_MISMATCH，表示传入属性id与调用函数不匹配。

#### OH_Drawing_GetFontFullDescriptorAttributeString()

```ets
OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeString(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, OH_Drawing_String* str)
```

**描述**

获取[OH_Drawing_String](OH_Drawing_String.md)类型字体描述符的属性。

如果不再需要OH_Drawing_String时，调用方需要手动释放OH_Drawing_String结构体内部的strData成员。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 22

**参数：**

参数项描述const [OH_Drawing_FontFullDescriptor](OH_Drawing_FontFullDescriptor.md)* descriptor指向字体描述符对象[OH_Drawing_FontFullDescriptor](OH_Drawing_FontFullDescriptor.md)的指针。[OH_Drawing_FontFullDescriptorAttributeId](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_fontfulldescriptorattributeid) id字体描述符属性id。从[OH_Drawing_FontFullDescriptorAttributeId](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002529445977__oh_drawing_fontfulldescriptorattributeid)中可获取字体描述符属性。[OH_Drawing_String](OH_Drawing_String.md)* str指向OH_Drawing_String类型属性的指针。作为出参使用。

**返回：**

类型说明[OH_Drawing_ErrorCode](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcode)

函数执行结果。

返回OH_DRAWING_SUCCESS，表示执行成功。

返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数descriptor或者str为空指针。

返回OH_DRAWING_ERROR_ATTRIBUTE_ID_MISMATCH，表示传入属性id与调用函数不匹配。