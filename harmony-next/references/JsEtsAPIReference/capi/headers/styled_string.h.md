# styled_string.h

#### 概述

在Native侧定义ArkUIText组件的文本样式。

**引用文件：** <arkui/styled_string.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：**[ArkUI_NativeModule](../../topics/system-services/ArkUI_NativeModule.md)

**相关示例：**[StyledStringSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/StyledStringSample)

#### 汇总

#### 结构体

名称typedef关键字描述[ArkUI_StyledString](../../topics/media/ArkUI_StyledString.md)ArkUI_StyledString定义文本组件支持的格式化字符串数据对象。

#### 函数

名称描述[ArkUI_StyledString* OH_ArkUI_StyledString_Create(OH_Drawing_TypographyStyle* style, OH_Drawing_FontCollection* collection)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_styledstring_create)创建指向ArkUI_StyledString对象的指针。[void OH_ArkUI_StyledString_Destroy(ArkUI_StyledString* handle)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_styledstring_destroy)释放被ArkUI_StyledString对象占据的内存。[void OH_ArkUI_StyledString_PushTextStyle(ArkUI_StyledString* handle, OH_Drawing_TextStyle* style)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_styledstring_pushtextstyle)将新的排版风格设置到当前格式化字符串样式栈顶。[void OH_ArkUI_StyledString_AddText(ArkUI_StyledString* handle, const char* content)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_styledstring_addtext)基于当前格式化字符串样式设置对应的文本内容。[void OH_ArkUI_StyledString_PopTextStyle(ArkUI_StyledString* handle)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_styledstring_poptextstyle)将当前格式化字符串对象中栈顶样式出栈。[OH_Drawing_Typography* OH_ArkUI_StyledString_CreateTypography(ArkUI_StyledString* handle)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_styledstring_createtypography)基于格式字符串对象创建指向OH_Drawing_Typography对象的指针，用于提前进行文本测算排版。[void OH_ArkUI_StyledString_AddPlaceholder(ArkUI_StyledString* handle, OH_Drawing_PlaceholderSpan* placeholder)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_styledstring_addplaceholder)设置占位符。[ArkUI_StyledString_Descriptor* OH_ArkUI_StyledString_Descriptor_Create(void)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_styledstring_descriptor_create)创建属性字符串数据对象。[void OH_ArkUI_StyledString_Descriptor_Destroy(ArkUI_StyledString_Descriptor* descriptor)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_styledstring_descriptor_destroy)释放被ArkUI_StyledString_Descriptor对象占据的内存。[int32_t OH_ArkUI_UnmarshallStyledStringDescriptor(uint8_t* buffer, size_t bufferSize, ArkUI_StyledString_Descriptor* descriptor)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_unmarshallstyledstringdescriptor)将包含属性字符串信息的字节数组反序列化为属性字符串。[int32_t OH_ArkUI_MarshallStyledStringDescriptor(uint8_t* buffer, size_t bufferSize, ArkUI_StyledString_Descriptor* descriptor, size_t* resultSize)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_marshallstyledstringdescriptor)将属性字符串信息序列化为字节数组。[const char* OH_ArkUI_ConvertToHtml(ArkUI_StyledString_Descriptor* descriptor)](#ZH-CN_TOPIC_0000002529445047__oh_arkui_converttohtml)将属性字符串信息转化成html。

#### 函数说明

#### OH_ArkUI_StyledString_Create()

```ets
ArkUI_StyledString* OH_ArkUI_StyledString_Create(OH_Drawing_TypographyStyle* style, OH_Drawing_FontCollection* collection)
```

**描述：**

创建指向ArkUI_StyledString对象的指针。

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_TypographyStyle](../../topics/graphics/OH_Drawing_TypographyStyle.md)* style指向OH_Drawing_TypographyStyle的指针，由[OH_Drawing_CreateTypographyStyle](drawing_text_typography.h.md#ZH-CN_TOPIC_0000002497606016__oh_drawing_createtypographystyle)获取。[OH_Drawing_FontCollection](../../topics/graphics/OH_Drawing_FontCollection.md)* collection指向OH_Drawing_FontCollection的指针，由[OH_Drawing_CreateFontCollection](drawing_font_collection.h.md)获取。

**返回：**

类型说明[ArkUI_StyledString](../../topics/media/ArkUI_StyledString.md)*创建指向ArkUI_StyledString对象的指针。如果对象返回空指针，表示创建失败，失败的原因是地址空间已满，或者是style，collection参数异常如空指针。

#### OH_ArkUI_StyledString_Destroy()

```ets
void OH_ArkUI_StyledString_Destroy(ArkUI_StyledString* handle)
```

**描述：**

释放被ArkUI_StyledString对象占据的内存。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_StyledString](../../topics/media/ArkUI_StyledString.md)* handle指向ArkUI_StyledString对象的指针。

#### OH_ArkUI_StyledString_PushTextStyle()

```ets
void OH_ArkUI_StyledString_PushTextStyle(ArkUI_StyledString* handle, OH_Drawing_TextStyle* style)
```

**描述：**

将新的排版风格设置到当前格式化字符串样式栈顶。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_StyledString](../../topics/media/ArkUI_StyledString.md)* handle指向ArkUI_StyledString对象的指针。[OH_Drawing_TextStyle](../../topics/graphics/OH_Drawing_TextStyle.md)* style指向OH_Drawing_TextStyle对象的指针。

#### OH_ArkUI_StyledString_AddText()

```ets
void OH_ArkUI_StyledString_AddText(ArkUI_StyledString* handle, const char* content)
```

**描述：**

基于当前格式化字符串样式设置对应的文本内容。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_StyledString](../../topics/media/ArkUI_StyledString.md)* handle指向ArkUI_StyledString对象的指针。const char* content指向文本内容的指针。

#### OH_ArkUI_StyledString_PopTextStyle()

```ets
void OH_ArkUI_StyledString_PopTextStyle(ArkUI_StyledString* handle)
```

**描述：**

将当前格式化字符串对象中栈顶样式出栈。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_StyledString](../../topics/media/ArkUI_StyledString.md)* handle指向ArkUI_StyledString对象的指针。

#### OH_ArkUI_StyledString_CreateTypography()

```ets
OH_Drawing_Typography* OH_ArkUI_StyledString_CreateTypography(ArkUI_StyledString* handle)
```

**描述：**

基于格式字符串对象创建指向OH_Drawing_Typography对象的指针，用于提前进行文本测算排版。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_StyledString](../../topics/media/ArkUI_StyledString.md)* handle指向ArkUI_StyledString对象的指针。

**返回：**

类型说明[OH_Drawing_Typography](../../topics/graphics/OH_Drawing_Typography.md)*指向OH_Drawing_Typography对象的指针。如果对象返回空指针，表示创建失败，失败的原因可能是handle参数异常如空指针。

#### OH_ArkUI_StyledString_AddPlaceholder()

```ets
void OH_ArkUI_StyledString_AddPlaceholder(ArkUI_StyledString* handle, OH_Drawing_PlaceholderSpan* placeholder)
```

**描述：**

设置占位符。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_StyledString](../../topics/media/ArkUI_StyledString.md)* handle指向ArkUI_StyledString对象的指针。[OH_Drawing_PlaceholderSpan](../../topics/components/OH_Drawing_PlaceholderSpan.md)* placeholder指向OH_Drawing_PlaceholderSpan对象的指针。

#### OH_ArkUI_StyledString_Descriptor_Create()

```ets
ArkUI_StyledString_Descriptor* OH_ArkUI_StyledString_Descriptor_Create(void)
```

**描述：**

创建属性字符串数据对象。

**起始版本：** 14

**返回：**

类型说明[ArkUI_StyledString_Descriptor](../../topics/media/ArkUI_StyledString_Descriptor.md)*指向ArkUI_StyledString_Descriptor对象的指针。

#### OH_ArkUI_StyledString_Descriptor_Destroy()

```ets
void OH_ArkUI_StyledString_Descriptor_Destroy(ArkUI_StyledString_Descriptor* descriptor)
```

**描述：**

释放被ArkUI_StyledString_Descriptor对象占据的内存。

**起始版本：** 14

**参数：**

参数项描述[ArkUI_StyledString_Descriptor](../../topics/media/ArkUI_StyledString_Descriptor.md)* descriptor指向ArkUI_StyledString_Descriptor对象的指针。

#### OH_ArkUI_UnmarshallStyledStringDescriptor()

```ets
int32_t OH_ArkUI_UnmarshallStyledStringDescriptor(uint8_t* buffer, size_t bufferSize, ArkUI_StyledString_Descriptor* descriptor)
```

**描述：**

将包含属性字符串信息的字节数组反序列化为属性字符串。

**起始版本：** 14

**参数：**

参数项描述uint8_t* buffer待反序列化的字节数组。size_t bufferSize字节数组长度。[ArkUI_StyledString_Descriptor](../../topics/media/ArkUI_StyledString_Descriptor.md)* descriptor指向ArkUI_StyledString_Descriptor对象的指针。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_MarshallStyledStringDescriptor()

```ets
int32_t OH_ArkUI_MarshallStyledStringDescriptor(uint8_t* buffer, size_t bufferSize, ArkUI_StyledString_Descriptor* descriptor, size_t* resultSize)
```

**描述：**

将属性字符串信息序列化为字节数组。

**起始版本：** 14

**参数：**

参数项描述uint8_t* buffer字节数组，用于存储属性字符串序列化后的数据。size_t bufferSize字节数组长度。[ArkUI_StyledString_Descriptor](../../topics/media/ArkUI_StyledString_Descriptor.md)* descriptor指向ArkUI_StyledString_Descriptor对象的指针。size_t* resultSize属性字符串转换后的字节数组实际长度。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

[ARKUI_ERROR_CODE_INVALID_STYLED_STRING](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 无效的属性字符串。

#### OH_ArkUI_ConvertToHtml()

```ets
const char* OH_ArkUI_ConvertToHtml(ArkUI_StyledString_Descriptor* descriptor)
```

**描述：**

将属性字符串信息转化成html。

**起始版本：** 14

**参数：**

参数项描述[ArkUI_StyledString_Descriptor](../../topics/media/ArkUI_StyledString_Descriptor.md)* descriptor指向ArkUI_StyledString_Descriptor对象的指针。

**返回：**

类型说明const char*html。该指针由内部管理，在OH_ArkUI_StyledString_Descriptor_Destroy()时释放。