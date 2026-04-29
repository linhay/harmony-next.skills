# drawing_text_declaration.h

**概述**

提供2d 绘制文本相关的数据结构声明

引用文件： <native_drawing/drawing_text_declaration.h>

库： libnative_drawing.so

系统能力： SystemCapability.Graphic.Graphic2D.NativeDrawing

起始版本： 8

相关模块： [Drawing](Drawing.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Drawing_FontCollection | OH_Drawing_FontCollection | 用于加载字体。 |
| OH_Drawing_Typography | OH_Drawing_Typography | 用于管理排版的布局和显示等。 |
| OH_Drawing_TextStyle | OH_Drawing_TextStyle | 用于管理字体颜色、装饰等。 |
| OH_Drawing_TypographyStyle | OH_Drawing_TypographyStyle | 用于管理排版风格，如文字方向等。 |
| OH_Drawing_LineTypography | OH_Drawing_LineTypography | 用于从一段文字中提取单行数据进行排版。 |
| OH_Drawing_TypographyCreate | OH_Drawing_TypographyCreate | 用于创建OH_Drawing_Typography。 |
| OH_Drawing_TextBox | OH_Drawing_TextBox | 用于接收文本框的矩形大小、方向和数量大小。 |
| OH_Drawing_PositionAndAffinity | OH_Drawing_PositionAndAffinity | 用于接收字体的位置和亲和性。 |
| OH_Drawing_Range | OH_Drawing_Range | 用于接收字体的起始位置和结束位置。 |
| OH_Drawing_TextShadow | OH_Drawing_TextShadow | 用于管理文本阴影。 |
| OH_Drawing_FontParser | OH_Drawing_FontParser | 用来解析系统字体文件。 |
| OH_Drawing_TextTab | OH_Drawing_TextTab | 用于管理文本制表符。 |
| OH_Drawing_TextLine | OH_Drawing_TextLine | 用于管理文本行。 |
| OH_Drawing_Run | OH_Drawing_Run | 用于管理文本渲染单元。 |
| OH_Drawing_FontFullDescriptor | OH_Drawing_FontFullDescriptor | 用于描述字体的详细信息，即字体描述符。 |