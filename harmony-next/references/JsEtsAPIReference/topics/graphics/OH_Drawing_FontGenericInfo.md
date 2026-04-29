# OH_Drawing_FontGenericInfo

```ets
typedef struct OH_Drawing_FontGenericInfo {...} OH_Drawing_FontGenericInfo
```

#### 概述

系统所支持的通用字体集信息结构体。

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

所在头文件： [drawing_text_typography.h](drawing_text_typography.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| char* familyName | 字体家族名。 |
| size_t aliasInfoSize | 别名字体列表的数量。 |
| size_t adjustInfoSize | 字重映射列表的数量。 |
| [OH_Drawing_FontAliasInfo](OH_Drawing_FontAliasInfo.md)* aliasInfoSet | 别名字体列表。 |
| [OH_Drawing_FontAdjustInfo](OH_Drawing_FontAdjustInfo.md)* adjustInfoSet | 字重映射列表。 |
