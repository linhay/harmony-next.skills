# Rcp_DebugInfo

#### 概述

描述存储在[Rcp_Response](Rcp_Response.md)中的调试信息的结构。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

[Rcp_DebugEvent](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gadff9eaa1b517bf01defd1273b2eeddbc)[type](Rcp_DebugInfo.md#ZH-CN_TOPIC_0000002282549680__ab4ef1c46103e7faf4c65c188300c5c91)

调试事件类型。

[Rcp_Buffer](Rcp_Buffer.md)[data](Rcp_DebugInfo.md#ZH-CN_TOPIC_0000002282549680__aece86864dfc23ae47580444af9fcdb3c)

调试信息。

struct [Rcp_DebugInfo](Rcp_DebugInfo.md) * [next](Rcp_DebugInfo.md#ZH-CN_TOPIC_0000002282549680__ab51a791fac9a703013aa3b931dacdcdb)

链式存储。指向下一个[Rcp_DebugInfo](Rcp_DebugInfo.md)。

#### 结构体成员变量说明

#### data

```ets
[Rcp_Buffer](Rcp_Buffer.md) Rcp_DebugInfo::data
```

**描述**

调试信息。

#### next

```ets
struct [Rcp_DebugInfo](Rcp_DebugInfo.md)* Rcp_DebugInfo::next
```

**描述**

链式存储。指向下一个[Rcp_DebugInfo](Rcp_DebugInfo.md)。

#### type

```ets
[Rcp_DebugEvent](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__gadff9eaa1b517bf01defd1273b2eeddbc) Rcp_DebugInfo::type
```

**描述**

调试事件类型。