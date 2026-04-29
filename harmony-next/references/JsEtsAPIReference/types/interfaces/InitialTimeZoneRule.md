# InitialTimeZoneRule

```ets
typedef struct InitialTimeZoneRule {...} InitialTimeZoneRule
```

**概述**

起始时区规则。

起始版本： 22

相关模块： [i18n](i18n.md)

所在头文件： [timezone.h](timezone.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t rawOffset | 时区的原始偏移量。 |
| int32_t dstSavings | 夏令时的偏移量。 |