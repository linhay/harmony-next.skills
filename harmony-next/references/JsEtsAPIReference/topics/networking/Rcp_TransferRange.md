# Rcp_TransferRange

**概述**

HTTP传输范围。该设置将转换为HTTP Range标头。具有范围标头的HTTP请求要求服务器仅发送回HTTP响应的一部分。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int64_t from | 传输起始位置。 |
| bool hasZeroFrom | 是否从零开始。 |
| int64_t to | 传输结束位置。 |
| bool hasZeroTo | 是否以零结束。 |
| struct Rcp_TransferRange * next | 链式存储。指向下一个Rcp_TransferRange。 |

**结构体成员变量说明**

**from**

```ets
int64_t Rcp_TransferRange::from
```

描述

传输起始位置。

**hasZeroFrom**

```ets
bool Rcp_TransferRange::hasZeroFrom
```

描述

请求范围是否从零开始。

**hasZeroTo**

```ets
bool Rcp_TransferRange::hasZeroTo
```

描述

是否以零结束。

**next**

```ets
struct Rcp_TransferRange* Rcp_TransferRange::next
```

描述

链式存储。指向下一个[Rcp_TransferRange](Rcp_TransferRange.md#ZH-CN_TOPIC_0000002522081564__rcp_transferrange)。

**to**

```ets
int64_t Rcp_TransferRange::to
```

描述

传输结束位置。