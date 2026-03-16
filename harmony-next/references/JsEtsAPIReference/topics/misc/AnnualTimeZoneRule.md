# AnnualTimeZoneRule

```ets
typedef struct AnnualTimeZoneRule {...} AnnualTimeZoneRule
```

#### 概述

每年生效的时区规则。

**起始版本：** 22

**相关模块：**[i18n](i18n.md)

**所在头文件：**[timezone.h](../../capi/headers/timezone.h.md)

#### 汇总

#### 成员变量

名称描述char* name时区规则的名称。int32_t startYear时区规则生效的起始年份。int32_t endYear时区规则生效的终止年份。int32_t rawOffset时区的原始偏移量。int32_t dstSavings夏令时的偏移量。[DateTimeRule](DateTimeRule.md) dateTimeRule时间日期规则。