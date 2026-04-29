# Http_PerformanceTiming

```ets
typedef struct Http_PerformanceTiming {...} Http_PerformanceTiming
```

#### 概述

HTTP响应时间信息，会在[Http_Response]([Http_Response](Http_Response.md#ZH-CN_TOPIC_0000002497605476__成员变量).md#ZH-CN_TOPIC_0000002553201471__成员变量)中收集。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

所在头文件： [net_http_type.h](net_http_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| double dnsTiming | 从request请求到DNS解析完成的耗时，包含域名解析，TCP连接等流程耗时。 |
| double tcpTiming | 从request请求到TCP连接完成的耗时。 |
| double tlsTiming | 从request请求到TLS连接完成的耗时。 |
| double firstSendTiming | 从request请求到开始发送第一个字节的耗时。 |
| double firstReceiveTiming | 从request请求到接收到第一个字节的耗时。 |
| double totalFinishTiming | 从request请求到完成请求的耗时。 |
| double redirectTiming | 从request请求到完成所有重定向步骤的耗时。 |
