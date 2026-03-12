# TimeArrayTimeZoneRule

```ets
typedef struct TimeArrayTimeZoneRule {...} TimeArrayTimeZoneRule
```

#### 概述

起始时间戳数组定义的时区规则。

**起始版本：** 22

**相关模块：**[i18n](i18n.md)

**所在头文件：**[timezone.h](timezone.h.md)

#### 汇总

#### 成员变量

名称描述char* name时区规则的名称。int32_t rawOffset时区的原始偏移量。int32_t dstSavings夏令时的偏移量。double* startTimes规则生效的起始时间戳数组。int32_t numStartTimes规则生效的起始时间戳数组的大小。[TimeRuleType](timezone.h.md#ZH-CN_TOPIC_0000002529285317__timeruletype) timeRuleType时间规则类型。