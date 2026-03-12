# Rcp_IpAddress

#### 概述

指定静态DNS规则使用的IP地址组。用于[Rcp_StaticDnsRuleItem](Rcp_StaticDnsRuleItem.md)。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

char [ipAddress](Rcp_IpAddress.md#ZH-CN_TOPIC_0000002317126041__a3f54f15797c4c306245e1d5bb282f300) [[RCP_IP_MAX_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaedd78171e1671e9ec89b59ecf6e96730)]

IP地址。

struct [Rcp_IpAddress](Rcp_IpAddress.md) * [next](Rcp_IpAddress.md#ZH-CN_TOPIC_0000002317126041__a73eede3d8fd7459aac9ef1d03512e276)

链式存储。指向下一个[Rcp_IpAddress](Rcp_IpAddress.md)。

#### 结构体成员变量说明

#### ipAddress

```ets
char Rcp_IpAddress::ipAddress[[RCP_IP_MAX_LEN](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gaedd78171e1671e9ec89b59ecf6e96730)]
```

**描述**

ip地址。

#### next

```ets
struct [Rcp_IpAddress](Rcp_IpAddress.md)* Rcp_IpAddress::next
```

**描述**

链式存储。指向下一个[Rcp_IpAddress](Rcp_IpAddress.md)。