# Rcp_IpAddress

**概述**

指定静态DNS规则使用的IP地址组。用于[Rcp_StaticDnsRuleItem](Rcp_StaticDnsRuleItem.md)。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char ipAddress [RCP_IP_MAX_LEN] | IP地址。 |
| struct Rcp_IpAddress * next | 链式存储。指向下一个Rcp_IpAddress。 |

**结构体成员变量说明**

**ipAddress**

```ets
char Rcp_IpAddress::ipAddress[RCP_IP_MAX_LEN]
```

描述

ip地址。

**next**

```ets
struct Rcp_IpAddress* Rcp_IpAddress::next
```

描述

链式存储。指向下一个[Rcp_IpAddress](Rcp_IpAddress.md#ZH-CN_TOPIC_0000002522241546__rcp_ipaddress)。