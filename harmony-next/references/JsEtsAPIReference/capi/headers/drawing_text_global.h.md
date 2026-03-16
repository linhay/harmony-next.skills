# drawing_text_global.h

#### 概述

提供文本全局信息的相关接口，比如设置文本渲染高对比度模式等。

**引用文件：** <native_drawing/drawing_text_global.h>

**库：** libnative_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**相关模块：**[Drawing](../../topics/graphics/Drawing.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_Drawing_TextHighContrast](#ZH-CN_TOPIC_0000002497606014__oh_drawing_texthighcontrast)OH_Drawing_TextHighContrast文本渲染高对比度模式枚举。[OH_Drawing_TextUndefinedGlyphDisplay](#ZH-CN_TOPIC_0000002497606014__oh_drawing_textundefinedglyphdisplay)OH_Drawing_TextUndefinedGlyphDisplay显示未定义字形的方式。

#### 函数

名称描述[void OH_Drawing_SetTextHighContrast(OH_Drawing_TextHighContrast action)](#ZH-CN_TOPIC_0000002497606014__oh_drawing_settexthighcontrast)设置文本渲染高对比度模式。[void OH_Drawing_SetTextUndefinedGlyphDisplay(OH_Drawing_TextUndefinedGlyphDisplay undefinedGlyphDisplay)](#ZH-CN_TOPIC_0000002497606014__oh_drawing_settextundefinedglyphdisplay)控制未定义字形的呈现方式，影响此后渲染的所有文本。

#### 枚举类型说明

#### OH_Drawing_TextHighContrast

```ets
enum OH_Drawing_TextHighContrast
```

**描述**

文本渲染高对比度模式枚举。

**起始版本：** 20

枚举项描述TEXT_FOLLOW_SYSTEM_HIGH_CONTRAST跟随系统设置中的高对比度文字配置。TEXT_APP_DISABLE_HIGH_CONTRAST关闭APP的文本渲染高对比度配置，该模式的优先级要高于系统设置中的高对比度文字配置。TEXT_APP_ENABLE_HIGH_CONTRAST开启APP的文本渲染高对比度配置，该模式的优先级要高于系统设置中的高对比度文字配置。

#### OH_Drawing_TextUndefinedGlyphDisplay

```ets
enum OH_Drawing_TextUndefinedGlyphDisplay
```

**描述**

显示未定义字形的方式。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

枚举项描述TEXT_NO_GLYPH_USE_DEFAULT = 0使用字体文件中定义的默认字形（可能是空框、空白或自定义符号等）。TEXT_NO_GLYPH_USE_TOFU = 1始终使用豆腐块显示缺失的字形。

#### 函数说明

#### OH_Drawing_SetTextHighContrast()

```ets
void OH_Drawing_SetTextHighContrast(OH_Drawing_TextHighContrast action)
```

**描述**

设置文本渲染高对比度模式。

该接口设置后整个进程都会生效，进程内所有页面共用相同模式。

可调用此接口设置，也可通过系统设置界面中高对比度文字配置开关进行开启/关闭。使用此接口设置开启/关闭文本渲染高对比度配置的优先级高于系统开关设置。

该接口针对应用的文字自绘制场景不生效。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述[OH_Drawing_TextHighContrast](#ZH-CN_TOPIC_0000002497606014__oh_drawing_texthighcontrast) action表示文本渲染高对比度模式，为[OH_Drawing_TextHighContrast](#ZH-CN_TOPIC_0000002497606014__oh_drawing_texthighcontrast)类型的枚举值。

#### OH_Drawing_SetTextUndefinedGlyphDisplay()

```ets
void OH_Drawing_SetTextUndefinedGlyphDisplay(OH_Drawing_TextUndefinedGlyphDisplay undefinedGlyphDisplay)
```

**描述**

控制未定义字形的呈现方式，影响此后渲染的所有文本。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 20

**参数：**

参数项描述[OH_Drawing_TextUndefinedGlyphDisplay](#ZH-CN_TOPIC_0000002497606014__oh_drawing_textundefinedglyphdisplay) undefinedGlyphDisplay表示显示未定义字形的方式，为[OH_Drawing_TextUndefinedGlyphDisplay](#ZH-CN_TOPIC_0000002497606014__oh_drawing_textundefinedglyphdisplay)类型的枚举值。