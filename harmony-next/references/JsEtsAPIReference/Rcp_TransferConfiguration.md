# Rcp_TransferConfiguration

#### 概述

传输配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

bool [autoRedirect](Rcp_TransferConfiguration.md#ZH-CN_TOPIC_0000002317039145__a80c7d591979b9538f847a9d4bd2109a1)

是否自动遵循HTTP重定向响应。默认为True。

[Rcp_Timeout](Rcp_Timeout.md)[timeout](Rcp_TransferConfiguration.md#ZH-CN_TOPIC_0000002317039145__a9ffa3456e4f7e056eb93887091b7fb04)

超时配置。如果未设置此选项，将应用默认超时。

bool [assumesHTTP3Capable](Rcp_TransferConfiguration.md#ZH-CN_TOPIC_0000002317039145__ae5f8dd2f74c11b558e0aa6761feefbed)

是否假定目标服务器支持HTTP/3。默认值为false。

[Rcp_PathPreference](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9498d24addbd529f258fd6faacfd9c67)[pathPreference](Rcp_TransferConfiguration.md#ZH-CN_TOPIC_0000002317039145__a169a9f44d629000efe1e54ea953efcf1)

请求路径首选项。

#### 结构体成员变量说明

#### assumesHTTP3Capable

```ets
bool Rcp_TransferConfiguration::assumesHTTP3Capable
```

**描述**

是否假定目标服务器支持HTTP/3。默认值为false。

#### autoRedirect

```ets
bool Rcp_TransferConfiguration::autoRedirect
```

**描述**

是否自动遵循HTTP重定向响应。默认为True。

#### pathPreference

```ets
[Rcp_PathPreference](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga9498d24addbd529f258fd6faacfd9c67) Rcp_TransferConfiguration::pathPreference
```

**描述**

请求路径首选项。

#### timeout

```ets
[Rcp_Timeout](Rcp_Timeout.md) Rcp_TransferConfiguration::timeout
```

**描述**

超时配置。如果未设置此选项，将应用默认超时。如果已配置，则使用配置的超时时间。