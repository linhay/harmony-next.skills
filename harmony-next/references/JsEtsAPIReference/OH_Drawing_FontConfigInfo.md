# OH_Drawing_FontConfigInfo

```ets
typedef struct OH_Drawing_FontConfigInfo {...} OH_Drawing_FontConfigInfo
```

#### 概述

系统字体配置信息结构体。

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

**所在头文件：**[drawing_text_typography.h](drawing_text_typography.h.md)

#### 汇总

#### 成员变量

名称描述size_t fontDirSize系统字体文件路径数量。size_t fontGenericInfoSize通用字体集列表数量。size_t fallbackGroupSize备用字体集列表数量。char** fontDirSet系统字体文件路径列表。[OH_Drawing_FontGenericInfo](OH_Drawing_FontGenericInfo.md)* fontGenericInfoSet通用字体集列表。[OH_Drawing_FontFallbackGroup](OH_Drawing_FontFallbackGroup.md)* fallbackGroupSet备用字体集列表。