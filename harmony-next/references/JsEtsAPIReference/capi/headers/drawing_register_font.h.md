# drawing_register_font.h

#### 概述

定义绘制模块中字体管理器相关的函数。

**引用文件：** <native_drawing/drawing_register_font.h>

**库：** libnative_drawing.so

**起始版本：** 11

**相关模块：**[Drawing](../../topics/graphics/Drawing.md)

#### 汇总

#### 函数

名称描述[uint32_t OH_Drawing_RegisterFont(OH_Drawing_FontCollection*, const char* fontFamily, const char* familySrc)](#ZH-CN_TOPIC_0000002529445973__oh_drawing_registerfont)用于在字体管理器中注册自定义字体，支持的字体文件格式包含：ttf、otf。[uint32_t OH_Drawing_RegisterFontBuffer(OH_Drawing_FontCollection*, const char* fontFamily, uint8_t* fontBuffer,size_t length)](#ZH-CN_TOPIC_0000002529445973__oh_drawing_registerfontbuffer)用于在字体管理器中注册字体缓冲区。[uint32_t OH_Drawing_UnregisterFont(OH_Drawing_FontCollection* fontCollection, const char* fontFamily)](#ZH-CN_TOPIC_0000002529445973__oh_drawing_unregisterfont)

通过字体家族名称取消注册自定义字体。

 取消注册当前正在使用的字体可能导致文本渲染异常，包括乱码或字形缺失。

 所有使用被取消注册的字体家族名称的排版对象都应该被销毁重建。

#### 函数说明

#### OH_Drawing_RegisterFont()

```ets
uint32_t OH_Drawing_RegisterFont(OH_Drawing_FontCollection*, const char* fontFamily, const char* familySrc)
```

**描述**

用于在字体管理器中注册自定义字体，支持的字体文件格式包含：ttf、otf。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_FontCollection](../../topics/graphics/OH_Drawing_FontCollection.md)*指向[OH_Drawing_FontCollection](../../topics/graphics/OH_Drawing_FontCollection.md)对象的指针。const char* fontFamily指需要注册的字体的字体名称。const char* familySrc指需要注册的字体文件的路径。

**返回：**

类型说明uint32_t返回错误代码，0为成功，1为文件不存在，2为打开文件失败，3为读取文件失败，4为寻找文件失败，5为获取大小失败，9文件损坏。

#### OH_Drawing_RegisterFontBuffer()

```ets
uint32_t OH_Drawing_RegisterFontBuffer(OH_Drawing_FontCollection*, const char* fontFamily, uint8_t* fontBuffer,size_t length)
```

**描述**

用于在字体管理器中注册字体缓冲区。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

参数项描述[OH_Drawing_FontCollection](../../topics/graphics/OH_Drawing_FontCollection.md)*指向[OH_Drawing_FontCollection](../../topics/graphics/OH_Drawing_FontCollection.md)对象的指针。const char* fontFamily指需要注册的字体的字体名称。uint8_t* fontBuffer指需要注册的字体文件的缓冲区。size_t length指需要注册的字体文件的长度。

**返回：**

类型说明uint32_t返回错误代码，0为成功，6为缓冲区大小为零，7为字体集合为空，9为文件损坏。

#### OH_Drawing_UnregisterFont()

```ets
uint32_t OH_Drawing_UnregisterFont(OH_Drawing_FontCollection* fontCollection, const char* fontFamily)
```

**描述**

通过字体家族名称取消注册自定义字体。

取消注册当前正在使用的字体可能导致文本渲染异常，包括乱码或字形缺失。

所有使用被取消注册的字体家族名称的排版对象都应该被销毁重建。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述[OH_Drawing_FontCollection](../../topics/graphics/OH_Drawing_FontCollection.md)* fontCollection指向[OH_Drawing_FontCollection](../../topics/graphics/OH_Drawing_FontCollection.md)对象的指针。const char* fontFamily需要取消注册的字体家族名称。

**返回：**

类型说明uint32_t返回执行结果状态码，0为成功，8为入参不合法，1为取消注册失败。