# OH_Drawing_FontFallbackGroup

```ets
typedef struct OH_Drawing_FontFallbackGroup {...} OH_Drawing_FontFallbackGroup
```

#### 概述

备用字体集信息结构体。

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

**所在头文件：**[drawing_text_typography.h](drawing_text_typography.h.md)

#### 汇总

#### 成员变量

名称描述char* groupName备用字体集所对应的字体集名称，如果值为空，表示可以使用备用字体集列表集所有的字体。size_t fallbackInfoSize备用字体集数量。[OH_Drawing_FontFallbackInfo](OH_Drawing_FontFallbackInfo.md)* fallbackInfoSet备用字体字体集列表。