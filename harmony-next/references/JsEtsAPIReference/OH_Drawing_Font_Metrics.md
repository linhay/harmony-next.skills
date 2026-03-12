# OH_Drawing_Font_Metrics

```ets
typedef struct OH_Drawing_Font_Metrics {...} OH_Drawing_Font_Metrics
```

#### 概述

定义字体度量信息的结构体。

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

**所在头文件：**[drawing_font.h](drawing_font.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t flags指示哪些度量是有效的。float top字符最高点到基线的最大距离。float ascent字符最高点到基线的推荐距离。float descent字符最低点到基线的推荐距离。float bottom字符最低点到基线的最大距离。float leading行间距。float avgCharWidth平均字符宽度，如果未知则为零。float maxCharWidth最大字符宽度，如果未知则为零。float xMin任何字形边界框原点左侧的最大范围，通常为负值；不推荐使用可变字体。float xMax任何字形边界框原点右侧的最大范围，通常为负值；不推荐使用可变字体。float xHeight小写字母的高度，如果未知则为零，通常为负数。float capHeight大写字母的高度，如果未知则为零，通常为负数。float underlineThickness下划线粗细。float underlinePosition表示下划线的位置，即从基线到文字下方笔画顶部的垂直距离，通常为正值。float strikeoutThickness删除线粗细。float strikeoutPosition表示删除线的位置，即从基线到文字上方笔画底部的垂直距离，通常为负值。