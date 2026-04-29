# drawing_register_font.h

**概述**

定义绘制模块中字体管理器相关的函数。

引用文件： <native_drawing/drawing_register_font.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

相关模块： [Drawing](Drawing.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| uint32_t OH_Drawing_RegisterFont(OH_Drawing_FontCollection*, const char* fontFamily, const char* familySrc) | 用于在字体管理器中注册自定义字体，支持的字体文件格式包含：ttf、otf。 |
| uint32_t OH_Drawing_RegisterFontBuffer(OH_Drawing_FontCollection*, const char* fontFamily, uint8_t* fontBuffer,size_t length) | 用于在字体管理器中注册字体缓冲区。 |
| uint32_t OH_Drawing_UnregisterFont(OH_Drawing_FontCollection* fontCollection, const char* fontFamily) | 通过字体家族名称取消注册自定义字体。  取消注册当前正在使用的字体可能导致文本渲染异常，包括乱码或字形缺失。  所有使用被取消注册的字体家族名称的排版对象都应该被销毁重建。 |
| uint32_t OH_Drawing_RegisterFontByIndex(OH_Drawing_FontCollection* fontCollection, const char* fontFamily, const char* familySrc, uint32_t index) | 使用ttc/otc文件注册自定义字体。 |
| uint32_t OH_Drawing_RegisterFontBufferByIndex(OH_Drawing_FontCollection* fontCollection, const char* fontFamily, uint8_t* fontBuffer, size_t length, uint32_t index) | 使用ttc/otc文件字节流注册字体。 |
| bool OH_Drawing_IsFontSupportedFromPath(const char* path) | 检查系统是否支持指定路径的字体格式。 |
| bool OH_Drawing_IsFontSupportedFromBuffer(uint8_t* data, size_t dataLength) | 检查系统是否支持缓冲区中指定的字体格式。 |

**函数说明**

**OH_Drawing_RegisterFont()**

```ets
uint32_t OH_Drawing_RegisterFont(OH_Drawing_FontCollection*, const char* fontFamily, const char* familySrc)
```

描述

用于在字体管理器中注册自定义字体，支持的字体文件格式包含：ttf、otf。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_FontCollection* | 指向OH_Drawing_FontCollection对象的指针。 |
| const char* fontFamily | 指需要注册的字体的字体名称。 |
| const char* familySrc | 指需要注册的字体文件的路径。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 返回错误代码，0为成功，1为文件不存在，2为打开文件失败，3为读取文件失败，4为寻找文件失败，5为获取大小失败，9文件损坏。 |

**OH_Drawing_RegisterFontBuffer()**

```ets
uint32_t OH_Drawing_RegisterFontBuffer(OH_Drawing_FontCollection*, const char* fontFamily, uint8_t* fontBuffer,size_t length)
```

描述

用于在字体管理器中注册字体缓冲区。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_FontCollection* | 指向OH_Drawing_FontCollection对象的指针。 |
| const char* fontFamily | 指需要注册的字体的字体名称。 |
| uint8_t* fontBuffer | 指需要注册的字体文件的缓冲区。 |
| size_t length | 指需要注册的字体文件的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 返回错误代码，0为成功，6为缓冲区大小为零，7为字体集合为空，9为文件损坏。 |

**OH_Drawing_UnregisterFont()**

```ets
uint32_t OH_Drawing_UnregisterFont(OH_Drawing_FontCollection* fontCollection, const char* fontFamily)
```

描述

通过字体家族名称取消注册自定义字体。

取消注册当前正在使用的字体可能导致文本渲染异常，包括乱码或字形缺失。

所有使用被取消注册的字体家族名称的排版对象都应该被销毁重建。

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_FontCollection* fontCollection | 指向OH_Drawing_FontCollection对象的指针。 |
| const char* fontFamily | 需要取消注册的字体家族名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 返回执行结果状态码，0为成功，8为入参不合法，1为取消注册失败。 |

**OH_Drawing_RegisterFontByIndex()**

```ets
uint32_t OH_Drawing_RegisterFontByIndex(OH_Drawing_FontCollection* fontCollection, const char* fontFamily, const char* familySrc, uint32_t index)
```

描述

使用ttc/otc文件注册自定义字体。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_FontCollection* fontCollection | 指向OH_Drawing_FontCollection对象的指针。 |
| const char* fontFamily | 需要注册的字体的字体名称。 |
| const char* familySrc | 需要注册的字体文件的路径。 |
| uint32_t index | 字体在ttc/otc文件中的索引，非ttc/otc格式文件需设置为0。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 函数执行结果。0为成功，1为文件不存在，2为打开文件失败，3为读取文件失败，4为寻找文件失败，5为获取大小失败，8为fontCollection为空，9为文件损坏。 |

**OH_Drawing_RegisterFontBufferByIndex()**

```ets
uint32_t OH_Drawing_RegisterFontBufferByIndex(OH_Drawing_FontCollection* fontCollection, const char* fontFamily, uint8_t* fontBuffer, size_t length, uint32_t index)
```

描述

使用ttc/otc文件字节流注册字体。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Drawing_FontCollection* fontCollection | 指向OH_Drawing_FontCollection对象的指针。 |
| const char* fontFamily | 需要注册的字体的字体名称。 |
| uint8_t* fontBuffer | 需要注册的字体文件的字节流数据。 |
| size_t length | 字节流数据长度 |
| uint32_t index | 字体在ttc/otc文件中的索引，非ttc/otc格式文件需设置为0。 |

返回：

| 类型 | 说明 |
| --- | --- |
| uint32_t | 函数执行结果。0为成功，6为字节流指针为空，7为字节流长度为0，8为fontCollection为空，9为文件损坏。 |

**OH_Drawing_IsFontSupportedFromPath()**

```ets
bool OH_Drawing_IsFontSupportedFromPath(const char* path)
```

描述

检查系统是否支持指定路径的字体格式。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* path | 字体文件的绝对路径。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持该字体则返回true；否则返回false。 |

**OH_Drawing_IsFontSupportedFromBuffer()**

```ets
bool OH_Drawing_IsFontSupportedFromBuffer(uint8_t* data, size_t dataLength)
```

描述

检查系统是否支持缓冲区中指定的字体格式。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| uint8_t* data | 包含字体数据的内存缓冲区的指针。 |
| size_t dataLength | 字体数据的大小（以字节为单位）。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持该字体则返回true；否则返回false。 |