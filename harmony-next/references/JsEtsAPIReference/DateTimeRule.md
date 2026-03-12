# DateTimeRule

```ets
typedef struct DateTimeRule {...} DateTimeRule
```

#### 概述

时间日期规则。

**起始版本：** 22

**相关模块：**[i18n](i18n.md)

**所在头文件：**[timezone.h](timezone.h.md)

#### 汇总

#### 成员变量

名称描述int32_t month月份。int32_t dayOfMonth当月的第几天。int32_t dayOfWeek当周的第几天。int32_t weekInMonth当月的第几周。int32_t millisInDay从当天凌晨0点开始到当前时间的毫秒值。[DateRuleType](timezone.h.md#ZH-CN_TOPIC_0000002529285317__dateruletype) dateRuleType日期规则类型。[TimeRuleType](timezone.h.md#ZH-CN_TOPIC_0000002529285317__timeruletype) timeRuleType时间规则类型。