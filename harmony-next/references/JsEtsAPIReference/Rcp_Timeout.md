# Rcp_Timeout

#### 概述

请求的超时配置。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [connectMs](Rcp_Timeout.md#ZH-CN_TOPIC_0000002317126021__a6fcc6e8da38cfb218ef9e534f30da218)

连接超时时间。默认值为60000毫秒。

uint32_t [transferMs](Rcp_Timeout.md#ZH-CN_TOPIC_0000002317126021__a096659a22ca66915119001cf5f76f3d9)

传输超时时间。默认值为60000毫秒。

#### 结构体成员变量说明

#### connectMs

```ets
uint32_t Rcp_Timeout::connectMs
```

**描述**

连接超时时间。默认值为60000毫秒。

#### transferMs

```ets
uint32_t Rcp_Timeout::transferMs
```

**描述**

传输超时时间。默认值为60000毫秒。