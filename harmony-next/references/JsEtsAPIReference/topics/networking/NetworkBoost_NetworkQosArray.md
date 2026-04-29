# [NetworkBoost_NetworkQos](NetworkBoost_NetworkQos.md)Array

#### 概述

网络质量变化的详细信息。

**起始版本：** 5.1.0(18)

**相关模块：**[NetworkBoost](NetworkBoost.md)

所在头文件： [network_boost_quality.h](network_boost_quality.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32_t [pathNum]([NetworkBoost_NetworkQos](NetworkBoost_NetworkQos.md)Array.md#ZH-CN_TOPIC_0000002496814645__a7881dde170513e4e1eb2f6030d224837) | 网络质量信息中的路径数量，取值范围 [1, 4]。 |
| NetworkBoost_NetworkQos [networkQos](NetworkBoost_NetworkQosArray.md#ZH-CN_TOPIC_0000002496814645__a85ba381b3f959459d2a832ab2b5e13ff) [[NETBOOST_MAX_PATH_NUM](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga7668e89aac2dea1d584a9ccacea33614)] | 多条路径的网络质量信息，每一项为一条路径的网络质量信息，取值范围 [0, pathNum-1]。 |

#### 结构体成员变量说明

#### [networkQos](NetworkBoost_NetworkQosArray.md#ZH-CN_TOPIC_0000002496814645__a85ba381b3f959459d2a832ab2b5e13ff)

```ets
[NetworkBoost_NetworkQos](NetworkBoost_NetworkQos.md) NetworkBoost_NetworkQosArray::networkQos[[NETBOOST_MAX_PATH_NUM](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga7668e89aac2dea1d584a9ccacea33614)]
```

**描述**

多条路径的网络质量信息，每一项为一条路径的网络质量信息，取值范围 [0, [pathNum](NetworkBoost_NetworkQosArray.md#ZH-CN_TOPIC_0000002496814645__a7881dde170513e4e1eb2f6030d224837)-1]。

#### [pathNum](NetworkBoost_NetworkQosArray.md#ZH-CN_TOPIC_0000002496814645__a7881dde170513e4e1eb2f6030d224837)

```ets
uint32_t NetworkBoost_NetworkQosArray::pathNum
```

**描述**

网络质量信息中的路径数量，取值范围 [1, 4]。
