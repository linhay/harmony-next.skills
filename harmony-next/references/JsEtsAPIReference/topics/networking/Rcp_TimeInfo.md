# Rcp_TimeInfo

**概述**

响应计时信息。

它将在[Rcp_Response.timeInfo](Rcp_Response.md#ZH-CN_TOPIC_0000002553361477__timeinfo)中被收集，[Rcp_TracingConfiguration.collectTimeInfo](Rcp_TracingConfiguration.md#ZH-CN_TOPIC_0000002522241558__collecttimeinfo)决定是否收集它。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| double totalTime | HTTP传输（包括名称解析、TCP连接等）的总时间（毫秒）。 |
| double nameLookUpTime | 从开始到解析远程主机名所用的时间（以毫秒为单位）。 |
| double connectTime | 从开始到完成与远程主机（或代理）的连接的时间（以毫秒为单位）。 |
| double preTransferTime | 从开始到传输即将开始所花费的时间（以毫秒为单位）。 |
| double fileTime | 从远程文件的上次修改时间开始的时间（以毫秒为单位）。 |
| double startTransferTime | 从开始到接收到第一个字节所花费的时间（以毫秒为单位）。 |
| double redirectTime | 所有重定向步骤（包括名称查找、连接等）所用的时间（毫秒）。 |
| double tlsHandshakeTime | 从开始到完成与远程主机（或代理）的TLS握手的时间（以毫秒为单位）。 |

**结构体成员变量说明**

**connectTime**

```ets
double Rcp_TimeInfo::connectTime
```

描述

从开始到完成与远程主机（或代理）的连接时间（以毫秒为单位）。

**fileTime**

```ets
double Rcp_TimeInfo::fileTime
```

描述

从远程文件的上次修改时间开始的时间（以毫秒为单位）。

**nameLookUpTime**

```ets
double Rcp_TimeInfo::nameLookUpTime
```

描述

从开始到解析远程主机名所用的时间（以毫秒为单位）。

**preTransferTime**

```ets
double Rcp_TimeInfo::preTransferTime
```

描述

从开始到传输即将开始所花费的时间（以毫秒为单位）。

**redirectTime**

```ets
double Rcp_TimeInfo::redirectTime
```

描述

所有重定向步骤（包括名称查找、连接等）所用的时间（毫秒）。

**startTransferTime**

```ets
double Rcp_TimeInfo::startTransferTime
```

描述

从开始到接收到第一个字节所花费的时间（以毫秒为单位）。

**tlsHandshakeTime**

```ets
double Rcp_TimeInfo::tlsHandshakeTime
```

描述

从开始到完成与远程主机（或代理）的TLS握手的时间（以毫秒为单位）。

**totalTime**

```ets
double Rcp_TimeInfo::totalTime
```

描述

HTTP传输（包括名称解析、TCP连接等）的总时间（毫秒）。