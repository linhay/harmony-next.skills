# OH_Drawing_StrutStyle

```ets
typedef struct OH_Drawing_StrutStyle {...} OH_Drawing_StrutStyle
```

#### 概述

用于描述支柱样式的结构体。支柱样式用于控制绘制文本时行之间的间距、基线对齐方式以及其他与行高相关的属性。

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

所在头文件： [drawing_text_typography.h](drawing_text_typography.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH_Drawing_FontWeight](drawing_text_typography.h.md#ZH-CN_TOPIC_0000002497606016__oh_drawing_fontweight) weight | 计算支柱时使用的字体粗细。 |
| [OH_Drawing_FontStyle](drawing_text_typography.h.md#ZH-CN_TOPIC_0000002497606016__oh_drawing_fontstyle) style | 计算支柱时使用的字体格式。 |
| double size | 逻辑像素中的上升加下降的大小。 |
| double heightScale | 行高缩放系数。 |
| bool heightOverride | 是否启用高度覆盖。true表示启用，false表示不启用。 |
| bool halfLeading | 半行距是否启用。true表示启用，false表示不启用。 |
| double leading | 以自定义行距应用于支柱的行距。 |
| bool forceStrutHeight | 是否所有行都将使用支柱的高度。true表示使用，false表示不使用。 |
| size_t familiesSize | 字体家族的数量。 |
| char** families | 计算支柱时使用的字体名称。 |
