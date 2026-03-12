# NetworkBoost_HandoverStart

#### 概述

连接迁移开始信息。

**起始版本：** 5.1.0(18)

**相关模块：**[NetworkBoost](NetworkBoost.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [expires](NetworkBoost_HandoverStart.md#ZH-CN_TOPIC_0000002463535626__a405fb82f10e067f1dacd91e1eac02725)

连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。

[NetworkBoost_DataSpeedAction](NetworkBoost_DataSpeedAction.md)[dataSpeedAction](NetworkBoost_HandoverStart.md#ZH-CN_TOPIC_0000002463535626__a9ef2e94bd85d1dbe00f1a0021c4fc7b5)

老链路的发包建议。

#### 结构体成员变量说明

#### dataSpeedAction

```ets
[NetworkBoost_DataSpeedAction](NetworkBoost_DataSpeedAction.md) NetworkBoost_HandoverStart::dataSpeedAction
```

**描述**

老链路的发包建议。

#### expires

```ets
uint32_t NetworkBoost_HandoverStart::expires
```

**描述**

连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。