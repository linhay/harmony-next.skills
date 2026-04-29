# NetworkBoost_MultiPathQuotaInfo

**概述**

多网配额信息，包含配额次数信息和时长信息。

起始版本： 6.0.2(22)

相关模块： [NetworkBoost](NetworkBoost.md)

所在头文件： [network_boost_handover.h](network_boost_handover.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint16_t count | 配额次数信息。 |
| uint16_t duration | 配额时长信息，单位为s。 |

**结构体成员变量说明**

**count**

```ets
uint16_t NetworkBoost_MultiPathQuotaInfo::count
```

描述

配额次数信息。

**duration**

```ets
uint16_t NetworkBoost_MultiPathQuotaInfo::duration
```

描述

配额时长信息，单位为s。