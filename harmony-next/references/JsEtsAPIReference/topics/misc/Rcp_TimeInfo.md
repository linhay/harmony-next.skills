# Rcp_TimeInfo

#### 概述

响应计时信息。

它将在[Rcp_Response.timeInfo](Rcp_Response.md#ZH-CN_TOPIC_0000002282446450__a57d437be63e686ada47b96b3126067d8)中被收集，[Rcp_TracingConfiguration.collectTimeInfo](Rcp_TracingConfiguration.md#ZH-CN_TOPIC_0000002317126029__aded07a3d27e7524e18362082264b9b94)决定是否收集它。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

double [totalTime](Rcp_TimeInfo.md#ZH-CN_TOPIC_0000002282549712__a61266aa883f6f7715bc5380c43c6ab28)

HTTP传输（包括名称解析、TCP连接等）的总时间（毫秒）。

double [nameLookUpTime](Rcp_TimeInfo.md#ZH-CN_TOPIC_0000002282549712__a61499e9621bab228bb6860af13090b68)

从开始到解析远程主机名所用的时间（以毫秒为单位）。

double [connectTime](Rcp_TimeInfo.md#ZH-CN_TOPIC_0000002282549712__a00f71c3e61958a61c5a95763460d53e9)

从开始到完成与远程主机（或代理）的连接的时间（以毫秒为单位）。

double [preTransferTime](Rcp_TimeInfo.md#ZH-CN_TOPIC_0000002282549712__ae1e72d2680d8edd395b1a80de8d24a39)

从开始到传输即将开始所花费的时间（以毫秒为单位）。

double [fileTime](Rcp_TimeInfo.md#ZH-CN_TOPIC_0000002282549712__aa2ace0fbac885a58100761269720d213)

从远程文件的上次修改时间开始的时间（以毫秒为单位）。

double [startTransferTime](Rcp_TimeInfo.md#ZH-CN_TOPIC_0000002282549712__ad2373fa86954f501efb5492858ca17f7)

从开始到接收到第一个字节所花费的时间（以毫秒为单位）。

double [redirectTime](Rcp_TimeInfo.md#ZH-CN_TOPIC_0000002282549712__a6050b0abb52990b0a0d01b49335a0d53)

所有重定向步骤（包括名称查找、连接等）所用的时间（毫秒）。

double [tlsHandshakeTime](Rcp_TimeInfo.md#ZH-CN_TOPIC_0000002282549712__ad4ecb9c4812a3f06edad569022a06ec1)

从开始到完成与远程主机（或代理）的TLS握手的时间（以毫秒为单位）。

#### 结构体成员变量说明

#### connectTime

```ets
double Rcp_TimeInfo::connectTime
```

**描述**

从开始到完成与远程主机（或代理）的连接时间（以毫秒为单位）。

#### fileTime

```ets
double Rcp_TimeInfo::fileTime
```

**描述**

从远程文件的上次修改时间开始的时间（以毫秒为单位）。

#### nameLookUpTime

```ets
double Rcp_TimeInfo::nameLookUpTime
```

**描述**

从开始到解析远程主机名所用的时间（以毫秒为单位）。

#### preTransferTime

```ets
double Rcp_TimeInfo::preTransferTime
```

**描述**

从开始到传输即将开始所花费的时间（以毫秒为单位）。

#### redirectTime

```ets
double Rcp_TimeInfo::redirectTime
```

**描述**

所有重定向步骤（包括名称查找、连接等）所用的时间（毫秒）。

#### startTransferTime

```ets
double Rcp_TimeInfo::startTransferTime
```

**描述**

从开始到接收到第一个字节所花费的时间（以毫秒为单位）。

#### tlsHandshakeTime

```ets
double Rcp_TimeInfo::tlsHandshakeTime
```

**描述**

从开始到完成与远程主机（或代理）的TLS握手的时间（以毫秒为单位）。

#### totalTime

```ets
double Rcp_TimeInfo::totalTime
```

**描述**

HTTP传输（包括名称解析、TCP连接等）的总时间（毫秒）。