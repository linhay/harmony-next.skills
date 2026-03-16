# Rcp_StaticDnsRule

#### 概述

静态DNS规则。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](../misc/RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_StaticDnsRuleItem](../components/Rcp_StaticDnsRuleItem.md)[staticDnsRule](Rcp_StaticDnsRule.md#ZH-CN_TOPIC_0000002282446410__a614d54045bd4f35aa4b35206a5d16709)

单个静态DNS规则。

struct [Rcp_StaticDnsRule](Rcp_StaticDnsRule.md) * [next](Rcp_StaticDnsRule.md#ZH-CN_TOPIC_0000002282446410__a892fbba45d597be89398929e8936b027)

链式存储。指向下一个[Rcp_StaticDnsRule](Rcp_StaticDnsRule.md)的指针。

#### 结构体成员变量说明

#### next

```ets
struct [Rcp_StaticDnsRule](Rcp_StaticDnsRule.md)* Rcp_StaticDnsRule::next
```

**描述**

链式存储。指向下一个[Rcp_StaticDnsRule](Rcp_StaticDnsRule.md)的指针。

#### staticDnsRule

```ets
[Rcp_StaticDnsRuleItem](../components/Rcp_StaticDnsRuleItem.md) Rcp_StaticDnsRule::staticDnsRule
```

**描述**

单个静态DNS规则。