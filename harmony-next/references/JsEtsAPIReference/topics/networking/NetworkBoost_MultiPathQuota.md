# NetworkBoost_MultiPathQuota

**概述**

应用配额信息，包含应用已使用配额信息和剩余配额信息。

起始版本： 6.0.2(22)

相关模块： [NetworkBoost](NetworkBoost.md)

所在头文件： [network_boost_handover.h](network_boost_handover.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| NetworkBoost_MultiPathQuotaInfo used | 应用已使用配额信息。 |
| NetworkBoost_MultiPathQuotaInfo remaining | 应用剩余使用配额信息。 |

**结构体成员变量说明**

**used**

```ets
NetworkBoost_MultiPathQuotaInfo NetworkBoost_MultiPathQuota::used
```

描述

表明应用已使用配额信息。

**remaining**

```ets
NetworkBoost_MultiPathQuotaInfo NetworkBoost_MultiPathQuota::remaining
```

描述

应用剩余使用配额信息。