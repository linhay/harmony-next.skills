# timezone.h

**概述**

提供获取时区信息的能力。

引用文件： <i18n/timezone.h>

库： libohi18n.so

系统能力： SystemCapability.Global.I18n

起始版本： 22

相关模块： [i18n](i18n.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| DateTimeRule | DateTimeRule | 时间日期规则。 |
| InitialTimeZoneRule | InitialTimeZoneRule | 起始时区规则。 |
| TimeArrayTimeZoneRule | TimeArrayTimeZoneRule | 起始时间戳数组定义的时区规则。 |
| AnnualTimeZoneRule | AnnualTimeZoneRule | 每年生效的时区规则。 |
| TimeZoneRules | TimeZoneRules | 完整的时区规则。 |
| TimeZoneRuleQuery | TimeZoneRuleQuery | 用于传入查询的信息，并接收查询的结果。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| DateRuleType | DateRuleType | 日期规则类型的枚举。 |
| TimeRuleType | TimeRuleType | 时间规则类型的枚举。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| MAX_YEAR_IN_ANNUAL_TIMEZONE_RULE 0x7fffffff | 每年生效时区规则的年份最大值。 起始版本： 22 |

**函数**

| 名称 | 描述 |
| --- | --- |
| I18n_ErrorCode OH_i18n_GetTimeZoneRules(const char* timeZoneID, TimeZoneRules* rules) | 通过时区ID，获取完整的时区规则。 |
| I18n_ErrorCode OH_i18n_GetFirstStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query) | 根据TimeArrayTimeZoneRule，获取时区规则的首次生效时间。 |
| I18n_ErrorCode OH_i18n_GetFirstStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query) | 根据AnnualTimeZoneRule，获取时区规则的首次生效时间。 |
| I18n_ErrorCode OH_i18n_GetFinalStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query) | 根据TimeArrayTimeZoneRule，获取时区规则的最后一次生效时间。 |
| I18n_ErrorCode OH_i18n_GetFinalStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query) | 根据AnnualTimeZoneRule，获取时区规则的最后一次生效时间。 |
| I18n_ErrorCode OH_i18n_GetNextStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query) | 根据TimeArrayTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。 |
| I18n_ErrorCode OH_i18n_GetNextStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query) | 根据AnnualTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。 |
| I18n_ErrorCode OH_i18n_GetPrevStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query) | 根据TimeArrayTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。 |
| I18n_ErrorCode OH_i18n_GetPrevStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query) | 根据AnnualTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。 |
| I18n_ErrorCode OH_i18n_GetStartTimeAt(TimeArrayTimeZoneRule* rule, int32_t index, double* result) | 根据TimeArrayTimeZoneRule，获取时区规则指定索引的起始时间。 |
| I18n_ErrorCode OH_i18n_GetStartInYear(AnnualTimeZoneRule* rule, int32_t year, TimeZoneRuleQuery* query) | 根据AnnualTimeZoneRule，获取时区规则在指定年份的生效时间。 |

**枚举类型说明**

**DateRuleType**

```ets
enum DateRuleType
```

描述

日期规则类型的枚举。

系统能力： SystemCapability.Global.I18n

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| DOM = 0 | 当月的第几天，以2025年为例，十月十六日为：十月的第十六天。 |
| DOW = 1 | 当月的第几个星期几，以2025年为例，十月十六日为：十月的第三个星期四。 |
| DOW_GEQ_DOM = 2 | 当月第几天之后的第一个星期几，以2025年为例，十月十六日为：十月第十三天/十四天/十五天之后的第一个星期四。 |
| DOW_LEQ_DOM = 3 | 当月第几天之前的最后一个星期几，以2025年为例，十月十六日为：十月第二十天之前的最后一个星期四。 |

**TimeRuleType**

```ets
enum TimeRuleType
```

描述

时间规则类型的枚举。

系统能力： SystemCapability.Global.I18n

起始版本： 22

| 枚举项 | 描述 |
| --- | --- |
| WALL_TIME = 0 | 本地时钟时间（不考虑时区偏移）。 |
| STANDARD_TIME = 1 | 本地标准时间（不考虑夏令时偏移）。 |
| UTC_TIME = 2 | 世界标准时间（UTC时间）。 |

**函数说明**

**OH_i18n_GetTimeZoneRules()**

```ets
I18n_ErrorCode OH_i18n_GetTimeZoneRules(const char* timeZoneID, TimeZoneRules* rules)
```

描述

通过时区ID，获取完整的时区规则。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* timeZoneID | 时区ID，例如“Asia/Shanghai”。 |
| TimeZoneRules* rules | 与时区ID对应的完整时区规则TimeZoneRules。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

**OH_i18n_GetFirstStartFromTimeArrayTimeZoneRule()**

```ets
I18n_ErrorCode OH_i18n_GetFirstStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

描述

根据TimeArrayTimeZoneRule，获取时区规则的首次生效时间。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| TimeArrayTimeZoneRule* rule | 起始时间戳数组定义的时区规则TimeArrayTimeZoneRule。 |
| TimeZoneRuleQuery* query | 用于传入查询的信息，并接收查询的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

**OH_i18n_GetFirstStartFromAnnualTimeZoneRule()**

```ets
I18n_ErrorCode OH_i18n_GetFirstStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

描述

根据AnnualTimeZoneRule，获取时区规则的首次生效时间。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| AnnualTimeZoneRule* rule | 每年生效的时区规则AnnualTimeZoneRule。 |
| TimeZoneRuleQuery* query | 用于传入查询的信息，并接收查询的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

**OH_i18n_GetFinalStartFromTimeArrayTimeZoneRule()**

```ets
I18n_ErrorCode OH_i18n_GetFinalStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

描述

根据TimeArrayTimeZoneRule，获取时区规则的最后一次生效时间。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| TimeArrayTimeZoneRule* rule | 起始时间戳数组定义的时区规则TimeArrayTimeZoneRule。 |
| TimeZoneRuleQuery* query | 用于传入查询的信息，并接收查询的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

**OH_i18n_GetFinalStartFromAnnualTimeZoneRule()**

```ets
I18n_ErrorCode OH_i18n_GetFinalStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

描述

根据AnnualTimeZoneRule，获取时区规则的最后一次生效时间。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| AnnualTimeZoneRule* rule | 每年生效的时区规则AnnualTimeZoneRule。 |
| TimeZoneRuleQuery* query | 用于传入查询的信息，并接收查询的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

**OH_i18n_GetNextStartFromTimeArrayTimeZoneRule()**

```ets
I18n_ErrorCode OH_i18n_GetNextStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

描述

根据TimeArrayTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| TimeArrayTimeZoneRule* rule | 起始时间戳数组定义的时区规则TimeArrayTimeZoneRule。 |
| TimeZoneRuleQuery* query | 用于传入查询的信息，并接收查询的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

**OH_i18n_GetNextStartFromAnnualTimeZoneRule()**

```ets
I18n_ErrorCode OH_i18n_GetNextStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

描述

根据AnnualTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| AnnualTimeZoneRule* rule | 每年生效的时区规则AnnualTimeZoneRule。 |
| TimeZoneRuleQuery* query | 用于传入查询的信息，并接收查询的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

**OH_i18n_GetPrevStartFromTimeArrayTimeZoneRule()**

```ets
I18n_ErrorCode OH_i18n_GetPrevStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

描述

根据TimeArrayTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| TimeArrayTimeZoneRule* rule | 起始时间戳数组定义的时区规则TimeArrayTimeZoneRule。 |
| TimeZoneRuleQuery* query | 用于传入查询的信息，并接收查询的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

**OH_i18n_GetPrevStartFromAnnualTimeZoneRule()**

```ets
I18n_ErrorCode OH_i18n_GetPrevStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

描述

根据AnnualTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| AnnualTimeZoneRule* rule | 每年生效的时区规则AnnualTimeZoneRule。 |
| TimeZoneRuleQuery* query | 用于传入查询的信息，并接收查询的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

**OH_i18n_GetStartTimeAt()**

```ets
I18n_ErrorCode OH_i18n_GetStartTimeAt(TimeArrayTimeZoneRule* rule, int32_t index, double* result)
```

描述

根据TimeArrayTimeZoneRule，获取时区规则指定索引的起始时间。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| TimeArrayTimeZoneRule* rule | 起始时间戳数组定义的时区规则TimeArrayTimeZoneRule。 |
| int32_t index | 起始时间的索引。 |
| double* result | 规则生效的起始时间。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

**OH_i18n_GetStartInYear()**

```ets
I18n_ErrorCode OH_i18n_GetStartInYear(AnnualTimeZoneRule* rule, int32_t year, TimeZoneRuleQuery* query)
```

描述

根据AnnualTimeZoneRule，获取时区规则在指定年份的生效时间。

系统能力： SystemCapability.Global.I18n

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| AnnualTimeZoneRule* rule | 每年生效的时区规则AnnualTimeZoneRule。 |
| int32_t year | 查询的年份。 |
| TimeZoneRuleQuery* query | 用于传入查询的信息，并接收查询的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| I18n_ErrorCode | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |