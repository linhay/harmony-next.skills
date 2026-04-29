# drawing_text_font_descriptor.h

**概述**

定义了字体信息的相关接口，比如获取字体信息，查找指定字体等。

引用文件： <native_drawing/drawing_text_font_descriptor.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 14

相关模块： [Drawing](Drawing.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Drawing_SystemFontType | OH_Drawing_SystemFontType | 字体类型的枚举。 |
| OH_Drawing_FontFullDescriptorAttributeId | OH_Drawing_FontFullDescriptorAttributeId | 字体描述符属性的枚举。不同类型的字体描述符属性，请使用对应类型的接口获取属性。如字体描述符属性FULL_DESCRIPTOR_ATTR_I_WEIGHT为int类型，需使用OH_Drawing_GetFontFullDescriptorAttributeInt接口获取其属性值。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Drawing_FontDescriptor* OH_Drawing_MatchFontDescriptors(OH_Drawing_FontDescriptor* desc, size_t* num) | 获取与指定字体描述符匹配的所有系统字体描述符，其中OH_Drawing_FontDescriptor的path字段不作为有效的匹配字段，其余字段不是默认值时生效。 如果参数desc的所有字段都是默认值，则获取所有系统字体描述符。 如果匹配失败，返回NULL。不再需要OH_Drawing_FontDescriptor时，请使用OH_Drawing_DestroyFontDescriptors接口释放该对象的指针。 |
| void OH_Drawing_DestroyFontDescriptors(OH_Drawing_FontDescriptor* descriptors, size_t num) | 释放字体描述符OH_Drawing_FontDescriptor数组。 |
| OH_Drawing_FontDescriptor* OH_Drawing_GetFontDescriptorByFullName(const OH_Drawing_String* fullName,OH_Drawing_SystemFontType fontType) | 根据字体名称和字体类型获取指定的字体描述符，支持系统字体、风格字体和用户已安装字体。 字体描述符是描述字体特征的一种数据结构，它包含了定义字体外观和属性的详细信息。 |
| OH_Drawing_Array* OH_Drawing_GetSystemFontFullNamesByType(OH_Drawing_SystemFontType fontType) | 根据字体类型获取对应字体的字体名称数组。 |
| const OH_Drawing_String* OH_Drawing_GetSystemFontFullNameByIndex(OH_Drawing_Array* fullNameArray, size_t index) | 在字体名称数组中通过索引获取对应位置的字体名称。 |
| void OH_Drawing_DestroySystemFontFullNames(OH_Drawing_Array* fullNameArray) | 释放通过字体类型获取的对应字体的字体名称数组占用的内存。 |
| OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorsFromStream(const void* data, size_t size) | 根据原始二进制数据获取字体描述符数组。 |
| OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorsFromPath(const char* path) | 根据字体文件路径获取字体描述符数组。 |
| const OH_Drawing_FontFullDescriptor* OH_Drawing_GetFontFullDescriptorByIndex(OH_Drawing_Array* descriptorArray, size_t index) | 在字体描述符数组中通过索引获取对应的字体描述符。 |
| void OH_Drawing_DestroyFontFullDescriptors(OH_Drawing_Array* descriptorArray) | 释放字体描述符数组占用的内存。 |
| OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeInt(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, int* value) | 获取int类型字体描述符的属性。 |
| OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeBool(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, bool* value) | 获取bool类型字体描述符的属性。 |
| OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeString(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, OH_Drawing_String* str) | 获取OH_Drawing_String类型字体描述符的属性。 |
| OH_Drawing_ErrorCode OH_Drawing_GetFontUnicodeArrayFromFile(const char* fontSrc, uint32_t index, int32_t** unicodeArray, int32_t* arrayLength) | 从字体文件中获取unicode码。 |
| OH_Drawing_ErrorCode OH_Drawing_GetFontUnicodeArrayFromBuffer(uint8_t* fontBuffer, size_t length, uint32_t index, int32_t** unicodeArray, int32_t* arrayLength) | 从字体字节流缓存中获取unicode码。 |
| uint32_t OH_Drawing_GetFontCountFromFile(const char* fontSrc) | 获取字体文件中包含的字体数量。 |
| uint32_t OH_Drawing_GetFontCountFromBuffer(uint8_t* fontBuffer, size_t length) | 获取字体缓存数据中包含的字体数量。 |
| OH_Drawing_String* OH_Drawing_GetFontPathsByType(OH_Drawing_SystemFontType fontType, size_t* pathCount) | 获取指定字体类型的所有字体文件路径。 |

**枚举类型说明**

**OH_Drawing_SystemFontType**

```ets
enum OH_Drawing_SystemFontType
```

描述

字体类型的枚举。

起始版本： 14

| 枚举项 | 描述 |
| --- | --- |
| ALL = 1 << 0 | 所有字体类型。 |
| GENERIC = 1 << 1 | 系统字体类型。 |
| STYLISH = 1 << 2 | 风格字体类型 |
| INSTALLED = 1 << 3 | 用户已安装字体类型。 |
| CUSTOMIZED = 1 << 4 | 自定义字体类型。  起始版本： 18 |

**OH_Drawing_FontFullDescriptorAttributeId**

```ets
enum OH_Drawing_FontFullDescriptorAttributeId
```

描述

字体描述符属性的枚举。不同类型的字体描述符属性，请使用对应类型的接口获取属性。如字体描述符属性FULL_DESCRIPTOR_ATTR_I_WEIGHT为int类型，需使用[OH_Drawing_GetFontFullDescriptorAttributeInt](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002522242164__oh_drawing_getfontfulldescriptorattributeint)接口获取其属性值。

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| FULL_DESCRIPTOR_ATTR_S_PATH = 0 | 字体文件的路径，OH_Drawing_String类型。 |
| FULL_DESCRIPTOR_ATTR_S_POSTSCRIPT_NAME = 1 | 唯一标识字体的名称，OH_Drawing_String类型。 |
| FULL_DESCRIPTOR_ATTR_S_FULL_NAME = 2 | 字体的名称，OH_Drawing_String类型。 |
| FULL_DESCRIPTOR_ATTR_S_FAMILY_NAME = 3 | 字体家族的名称，OH_Drawing_String类型。 |
| FULL_DESCRIPTOR_ATTR_S_SUB_FAMILY_NAME = 4 | 子字体家族的名称，OH_Drawing_String类型。 |
| FULL_DESCRIPTOR_ATTR_I_WEIGHT = 5 | 字体的字重，int类型。 |
| FULL_DESCRIPTOR_ATTR_I_WIDTH = 6 | 字体的宽窄风格属性，int类型。 |
| FULL_DESCRIPTOR_ATTR_I_ITALIC = 7 | 字体是否倾斜，int类型。1表示字体倾斜，0表示字体非倾斜。 |
| FULL_DESCRIPTOR_ATTR_B_MONO = 8 | 字体是否紧凑，bool类型。true表示字体紧凑，false表示字体非紧凑。 |
| FULL_DESCRIPTOR_ATTR_B_SYMBOLIC = 9 | 字体是否支持符号字体，bool类型。true表示支持符号字体，false表示不支持符号字体。 |
| FULL_DESCRIPTOR_ATTR_S_LOCAL_POSTSCRIPT_NAME = 10 | 根据系统语言配置提取字体唯一标识的名称。 起始版本： 23 |
| FULL_DESCRIPTOR_ATTR_S_LOCAL_FULL_NAME = 11 | 根据系统语言配置提取字体全名。 起始版本： 23 |
| FULL_DESCRIPTOR_ATTR_S_LOCAL_FAMILY_NAME = 12 | 根据系统语言配置提取字体家族名称。 起始版本： 23 |
| FULL_DESCRIPTOR_ATTR_S_LOCAL_SUB_FAMILY_NAME = 13 | 根据系统语言配置提取子字体家族名称。 起始版本： 23 |
| FULL_DESCRIPTOR_ATTR_S_VERSION = 14 | 字体版本。 起始版本： 23 |
| FULL_DESCRIPTOR_ATTR_S_MANUFACTURE = 15 | 字体制造商信息。 起始版本： 23 |
| FULL_DESCRIPTOR_ATTR_S_COPYRIGHT = 16 | 字体版权信息。 起始版本： 23 |
| FULL_DESCRIPTOR_ATTR_S_TRADEMARK = 17 | 字体商标信息。 起始版本： 23 |
| FULL_DESCRIPTOR_ATTR_S_LICENSE = 18 | 字体许可证信息。 起始版本： 23 |
| FULL_DESCRIPTOR_ATTR_I_INDEX = 21 | 字体索引。 起始版本： 23 |

**函数说明**

**OH_Drawing_MatchFontDescriptors()**

```ets
OH_Drawing_FontDescriptor* OH_Drawing_MatchFontDescriptors(OH_Drawing_FontDescriptor* desc, size_t* num)
```

描述

获取与指定字体描述符匹配的所有系统字体描述符，其中[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)的path字段不作为有效的匹配字段，其余字段不是默认值时生效。

如果参数desc的所有字段都是默认值，则获取所有系统字体描述符。

如果匹配失败，返回NULL。不再需要[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)时，请使用[OH_Drawing_DestroyFontDescriptors](drawing_text_font_descriptor.h.md#ZH-CN_TOPIC_0000002522242164__oh_drawing_destroyfontdescriptors)接口释放该对象的指针。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_FontDescriptor* desc | 指针。 建议使用OH_Drawing_CreateFontDescriptor获得有效的OH_Drawing_FontDescriptor实例。 如果自己创建OH_Drawing_FontDescriptor实例，请确保不用于匹配的字段是默认值。 |
| size_t* num | 表示返回值数组的成员个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_FontDescriptor* | OH_Drawing_FontDescriptor数组，释放时请使用OH_Drawing_DestroyFontDescriptors。 |

**OH_Drawing_DestroyFontDescriptors()**

```ets
void OH_Drawing_DestroyFontDescriptors(OH_Drawing_FontDescriptor* descriptors, size_t num)
```

描述

释放字体描述符[OH_Drawing_FontDescriptor](OH_Drawing_FontDescriptor.md)数组。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_FontDescriptor* descriptors | 数组。 |
| size_t num | OH_Drawing_FontDescriptor数组的成员个数。 |

**OH_Drawing_GetFontDescriptorByFullName()**

```ets
OH_Drawing_FontDescriptor* OH_Drawing_GetFontDescriptorByFullName(const OH_Drawing_String* fullName,OH_Drawing_SystemFontType fontType)
```

描述

根据字体名称和字体类型获取指定的字体描述符，支持系统字体、风格字体和用户已安装字体。

字体描述符是描述字体特征的一种数据结构，它包含了定义字体外观和属性的详细信息。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_String* fullName | 表示指向字体名称字符串OH_Drawing_String的指针。 |
| OH_Drawing_SystemFontType fontType | 表示字体类型的枚举值OH_Drawing_SystemFontType。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_FontDescriptor* | 指向字体描述符对象OH_Drawing_FontDescriptor的指针，不再需要OH_Drawing_FontDescriptor时，请使用OH_Drawing_DestroyFontDescriptor接口释放该对象的指针。 |

**OH_Drawing_GetSystemFontFullNamesByType()**

```ets
OH_Drawing_Array* OH_Drawing_GetSystemFontFullNamesByType(OH_Drawing_SystemFontType fontType)
```

描述

根据字体类型获取对应字体的字体名称数组。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_SystemFontType fontType | 表示字体类型的枚举值OH_Drawing_SystemFontType。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Array* | 返回对应字体类型的字体名称数组OH_Drawing_Array的指针，不再需要OH_Drawing_Array时，请使用OH_Drawing_DestroySystemFontFullNames接口释放该对象的指针。 |

**OH_Drawing_GetSystemFontFullNameByIndex()**

```ets
const OH_Drawing_String* OH_Drawing_GetSystemFontFullNameByIndex(OH_Drawing_Array* fullNameArray, size_t index)
```

描述

在字体名称数组中通过索引获取对应位置的字体名称。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* fullNameArray | 表示字体名称数组OH_Drawing_Array的指针。 |
| size_t index | 数组的索引。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const OH_Drawing_String* | 返回对应索引的字体名称OH_Drawing_String的指针。 |

**OH_Drawing_DestroySystemFontFullNames()**

```ets
void OH_Drawing_DestroySystemFontFullNames(OH_Drawing_Array* fullNameArray)
```

描述

释放通过字体类型获取的对应字体的字体名称数组占用的内存。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* fullNameArray | 表示字体名称数组OH_Drawing_Array的指针。 |

**OH_Drawing_GetFontFullDescriptorsFromStream()**

```ets
OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorsFromStream(const void* data, size_t size)
```

描述

根据原始二进制数据获取字体描述符数组。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const void* data | 指向原始二进制字体数据缓冲区的指针。 |
| size_t size | 以字节为单位的字体数据缓冲区的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Array* | 返回指向对应字体文件的字体描述符数组OH_Drawing_Array的指针，不再需要OH_Drawing_Array时，请使用OH_Drawing_DestroyFontFullDescriptors接口释放该对象的指针。 如果因数据格式无效或解析错误导致操作失败，返回NULL。 |

**OH_Drawing_GetFontFullDescriptorsFromPath()**

```ets
OH_Drawing_Array* OH_Drawing_GetFontFullDescriptorsFromPath(const char* path)
```

描述

根据字体文件路径获取字体描述符数组。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* path | 需要查询的字体文件的路径。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_Array* | 返回指向对应字体文件的字体描述符数组OH_Drawing_Array的指针，不再需要OH_Drawing_Array时，请使用OH_Drawing_DestroyFontFullDescriptors接口释放该对象的指针。 如果字体文件未找到、字体文件路径无效、字体文件无权限或者文件非字体格式，返回NULL。 |

**OH_Drawing_GetFontFullDescriptorByIndex()**

```ets
const OH_Drawing_FontFullDescriptor* OH_Drawing_GetFontFullDescriptorByIndex(OH_Drawing_Array* descriptorArray, size_t index)
```

描述

在字体描述符数组中通过索引获取对应的字体描述符。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* descriptorArray | 表示指向字体描述符数组OH_Drawing_Array的指针。 |
| size_t index | 数组的索引，索引值从0开始。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const OH_Drawing_FontFullDescriptor* | 返回指向指定索引处字体描述符对象OH_Drawing_FontFullDescriptor的指针。 如果索引超出范围或数组无效，则返回NULL。 |

**OH_Drawing_DestroyFontFullDescriptors()**

```ets
void OH_Drawing_DestroyFontFullDescriptors(OH_Drawing_Array* descriptorArray)
```

描述

释放字体描述符数组占用的内存。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_Array* descriptorArray | 表示指向字体描述符数组OH_Drawing_Array的指针。 |

**OH_Drawing_GetFontFullDescriptorAttributeInt()**

```ets
OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeInt(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, int* value)
```

描述

获取int类型字体描述符的属性。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_FontFullDescriptor* descriptor | 指向字体描述符对象OH_Drawing_FontFullDescriptor的指针。 |
| OH_Drawing_FontFullDescriptorAttributeId id | 字体描述符属性id。从OH_Drawing_FontFullDescriptorAttributeId中可获取字体描述符属性。 |
| int* value | 指向int类型属性的指针。作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数descriptor或者value为空指针。 返回OH_DRAWING_ERROR_ATTRIBUTE_ID_MISMATCH，表示传入属性id与调用函数不匹配。 |

**OH_Drawing_GetFontFullDescriptorAttributeBool()**

```ets
OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeBool(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, bool* value)
```

描述

获取bool类型字体描述符的属性。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_FontFullDescriptor* descriptor | 指向字体描述符对象OH_Drawing_FontFullDescriptor的指针。 |
| OH_Drawing_FontFullDescriptorAttributeId id | 字体描述符属性id。从OH_Drawing_FontFullDescriptorAttributeId中可获取字体描述符属性。 |
| bool* value | 指向bool类型属性的指针。作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数descriptor或者value为空指针。 返回OH_DRAWING_ERROR_ATTRIBUTE_ID_MISMATCH，表示传入属性id与调用函数不匹配。 |

**OH_Drawing_GetFontFullDescriptorAttributeString()**

```ets
OH_Drawing_ErrorCode OH_Drawing_GetFontFullDescriptorAttributeString(const OH_Drawing_FontFullDescriptor* descriptor, OH_Drawing_FontFullDescriptorAttributeId id, OH_Drawing_String* str)
```

描述

获取[OH_Drawing_String](OH_Drawing_String.md)类型字体描述符的属性。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

如果不再需要OH_Drawing_String时，调用方需要手动释放OH_Drawing_String结构体内部的strData成员。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Drawing_FontFullDescriptor* descriptor | 指向字体描述符对象OH_Drawing_FontFullDescriptor的指针。 |
| OH_Drawing_FontFullDescriptorAttributeId id | 字体描述符属性id。从OH_Drawing_FontFullDescriptorAttributeId中可获取字体描述符属性。 |
| OH_Drawing_String* str | 指向OH_Drawing_String类型属性的指针。作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示参数descriptor或者str为空指针。 返回OH_DRAWING_ERROR_ATTRIBUTE_ID_MISMATCH，表示传入属性id与调用函数不匹配。 |

**OH_Drawing_GetFontUnicodeArrayFromFile()**

```ets
OH_Drawing_ErrorCode OH_Drawing_GetFontUnicodeArrayFromFile(const char* fontSrc, uint32_t index, int32_t** unicodeArray, int32_t* arrayLength)
```

描述

从字体文件中获取unicode码。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* fontSrc | 字体文件路径。 |
| uint32_t index | ttc/otc文件中字体的索引，非ttc/otc文件需设置为0。 |
| int32_t** unicodeArray | 出参，用于接收unicode码数组，当不需要时，使用free()释放。 |
| int32_t* arrayLength | 出参，用于接收unicode码数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示字体路径非法或不是字体文件。 |

**OH_Drawing_GetFontUnicodeArrayFromBuffer()**

```ets
OH_Drawing_ErrorCode OH_Drawing_GetFontUnicodeArrayFromBuffer(uint8_t* fontBuffer, size_t length, uint32_t index, int32_t** unicodeArray, int32_t* arrayLength)
```

描述

从字体字节流缓存中获取unicode码。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| uint8_t* fontBuffer | 字体文件数据。 |
| size_t length | 字体文件数据长度。 |
| uint32_t index | ttc/otc文件中字体的索引，非ttc/otc文件需设置为0。 |
| int32_t** unicodeArray | 出参，用于接收unicode码数组，当不需要时，使用free()释放。 |
| int32_t* arrayLength | 出参，用于接收unicode码数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_ErrorCode | 函数执行结果。 返回OH_DRAWING_SUCCESS，表示执行成功。 返回OH_DRAWING_ERROR_INCORRECT_PARAMETER，表示缓存数据非法或缓存数据不是字体文件数据。 |

**OH_Drawing_GetFontCountFromFile()**

```ets
uint32_t OH_Drawing_GetFontCountFromFile(const char* fontSrc)
```

描述

获取字体文件中包含的字体数量。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* fontSrc | 字体文件路径。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 字体数量。 |

**OH_Drawing_GetFontCountFromBuffer()**

```ets
uint32_t OH_Drawing_GetFontCountFromBuffer(uint8_t* fontBuffer, size_t length)
```

描述

获取字体缓存数据中包含的字体数量。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| uint8_t* fontBuffer | 字体缓存数据。 |
| size_t length | 字体数据长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 字体数量。 |

**OH_Drawing_GetFontPathsByType()**

```ets
OH_Drawing_String* OH_Drawing_GetFontPathsByType(OH_Drawing_SystemFontType fontType, size_t* pathCount)
```

描述

获取指定字体类型的所有字体文件路径。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_SystemFontType fontType | 系统字体类型对象 OH_Drawing_SystemFontType 的枚举。 |
| size_t* pathCount | 返回的字体路径列表的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Drawing_String* | 返回一个字体路径对象OH_Drawing_String列表。不再需要时，请使用free释放该对象指针以及每个OH_Drawing_String对象内部持有的指针。 |