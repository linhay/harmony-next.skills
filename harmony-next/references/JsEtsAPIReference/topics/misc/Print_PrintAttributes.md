# Print_PrintAttributes

```ets
typedef struct {...} Print_PrintAttributes
```

#### 概述

表示打印属性结构体。

**起始版本：** 13

**相关模块：**[OH_Print](OH_Print.md)

所在头文件： [ohprint.h](ohprint.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Print_Range](Print_Range.md) pageRange | 打印范围。 |
| [Print_PageSize](Print_PageSize.md) pageSize | 打印纸张尺寸。 |
| [Print_Margin](Print_Margin.md) pageMargin | 打印边距。 |
| uint32_t copyNumber | 份数。 |
| uint32_t duplexMode | 双面模式。 |
| uint32_t colorMode | 色彩模式。 |
| bool isSequential | 顺序打印。 |
| bool isLandscape | 打印方向（是否横向）。 |
| bool hasOption | 打印选项标志。 |
| char options[256] | 打印选项。 |
