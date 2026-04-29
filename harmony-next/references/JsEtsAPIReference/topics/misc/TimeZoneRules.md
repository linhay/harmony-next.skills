# TimeZoneRules

```ets
typedef struct TimeZoneRules {...} TimeZoneRules
```

#### 概述

完整的时区规则。

**起始版本：** 22

**相关模块：**[i18n](i18n.md)

所在头文件： [timezone.h](timezone.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [InitialTimeZoneRule](../../types/interfaces/InitialTimeZoneRule.md) initial | 起始时区规则。 |
| [TimeArrayTimeZoneRule*](TimeArrayTimeZoneRule.md) timeArrayRules | 起始时间戳数组定义的时区规则数组。 |
| [AnnualTimeZoneRule*](AnnualTimeZoneRule.md) annualRules | 每年生效的时区规则数组。 |
| size_t numTimeArrayRules | 起始时间戳数组定义的时区规则数组的大小。 |
| size_t numAnnualRules | 每年生效的时区规则数组的大小。 |
