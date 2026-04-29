# DateTimeRule

```ets
typedef struct DateTimeRule {...} DateTimeRule
```

#### 概述

时间日期规则。

**起始版本：** 22

**相关模块：**[i18n](i18n.md)

所在头文件： [timezone.h](timezone.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32_t month | 月份。 |
| int32_t dayOfMonth | 当月的第几天。 |
| int32_t dayOfWeek | 当周的第几天。 |
| int32_t weekInMonth | 当月的第几周。 |
| int32_t millisInDay | 从当天凌晨0点开始到当前时间的毫秒值。 |
| [DateRuleType](timezone.h.md#ZH-CN_TOPIC_0000002529285317__dateruletype) dateRuleType | 日期规则类型。 |
| [TimeRuleType](timezone.h.md#ZH-CN_TOPIC_0000002529285317__timeruletype) timeRuleType | 时间规则类型。 |
