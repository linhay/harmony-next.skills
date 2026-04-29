# OH_Drawing_LineMetrics

```ets
typedef struct OH_Drawing_LineMetrics {...} OH_Drawing_LineMetrics
```

#### 概述

文字行位置信息。

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

所在头文件： [drawing_text_typography.h](drawing_text_typography.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| double ascender | 文字相对于基线以上取绝对值后的高度。 |
| double descender | 文字相对于基线以下取绝对值后的高度。 |
| double capHeight | 大写字母的高度。 |
| double xHeight | 小写字母的高度。 |
| double width | 文字宽度。 |
| double height | 行高。 |
| double x | 文字左端到容器左端距离，左对齐为0，右对齐为容器宽度减去行文字宽度。 |
| double y | 文字上端到容器上端高度，第一行为0，第二行为第一行高度。 |
| size_t startIndex | 行起始位置字符索引。 |
| size_t endIndex | 行结束位置字符索引。 |
| [OH_Drawing_Font_Metrics](OH_Drawing_Font_Metrics.md) firstCharMetrics | 第一个字的度量信息。 |
