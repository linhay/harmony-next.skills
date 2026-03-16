# OpenGTX_NetworkInfo

#### 概述

此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](../graphics/GraphicsAccelerate.md)

#### 汇总

#### 成员变量

名称

描述

[OpenGTX_NetworkLatency](OpenGTX_NetworkLatency.md)[networkLatency](OpenGTX_NetworkInfo.md#ZH-CN_TOPIC_0000002385157862__a7630cf3cc694ba3d8ce1c7565d3c8860)

游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。

char* [networkServerIP](OpenGTX_NetworkInfo.md#ZH-CN_TOPIC_0000002385157862__a8a901843481e827a3799eb116744cf35)

游戏服务器的IP地址，字符长度范围[1,256]。

#### 结构体成员变量说明

#### networkLatency

```ets
[OpenGTX_NetworkLatency](OpenGTX_NetworkLatency.md) OpenGTX_NetworkInfo::networkLatency
```

**描述**

游戏中的网络延迟。 如果没有上下行时延，则设置为total（总时延）的值。将游戏总时延以0ms、50ms、100ms、150ms、200ms分为5个档位，当档位发生变化时，游戏应用通知OpenGTX。

#### networkServerIP

```ets
char* OpenGTX_NetworkInfo::networkServerIP
```

**描述**

游戏服务器的IP地址，字符长度范围[1,256]。