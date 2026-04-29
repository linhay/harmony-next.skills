# Rcp_ConnectionConfiguration

#### 概述

连接配置。

**起始版本：** 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| long [maxConnectionsPerHost](Rcp_ConnectionConfiguration.md#ZH-CN_TOPIC_0000002317039109__a5273114606602cb32197e705f42c0c25) | 每台主机的最大连接数。 |
| long [maxTotalConnections](Rcp_ConnectionConfiguration.md#ZH-CN_TOPIC_0000002317039109__af47d008692230fe5416caf4bde5223f6) | 最大总连接数。 |
| long [maxCacheConnections](Rcp_ConnectionConfiguration.md#ZH-CN_TOPIC_0000002317039109__ab1fe96a2cdfaf5451716b3efd60ea4fe) | 最大缓存连接数。 |

#### 结构体成员变量说明

#### [maxCacheConnections](Rcp_ConnectionConfiguration.md#ZH-CN_TOPIC_0000002317039109__ab1fe96a2cdfaf5451716b3efd60ea4fe)

```ets
long Rcp_ConnectionConfiguration::maxCacheConnections
```

**描述**

最大缓存连接数。

#### [maxConnectionsPerHost](Rcp_ConnectionConfiguration.md#ZH-CN_TOPIC_0000002317039109__a5273114606602cb32197e705f42c0c25)

```ets
long Rcp_ConnectionConfiguration::maxConnectionsPerHost
```

**描述**

每台主机的最大连接数。

#### [maxTotalConnections](Rcp_ConnectionConfiguration.md#ZH-CN_TOPIC_0000002317039109__af47d008692230fe5416caf4bde5223f6)

```ets
long Rcp_ConnectionConfiguration::maxTotalConnections
```

**描述**

最大总连接数。范围由long决定。
