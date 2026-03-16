# Print_PrintAttributes

```ets
typedef struct {...} Print_PrintAttributes
```

#### 概述

打印属性结构体。

**起始版本：** 13

**相关模块：**[OH_Print](OH_Print.md)

**所在头文件：**[ohprint.h](../../capi/headers/ohprint.h.md)

#### 汇总

#### 成员变量

名称描述[Print_Range](Print_Range.md) pageRange打印范围。[Print_PageSize](Print_PageSize.md) pageSize打印尺寸。[Print_Margin](../media/Print_Margin.md) pageMargin打印边距。uint32_t copyNumber打印份数。uint32_t duplexMode单双面。uint32_t colorMode彩色。bool isSequential顺序打印。bool isLandscape横纵向。bool hasOption打印选项标识位。char options[256]打印选项。