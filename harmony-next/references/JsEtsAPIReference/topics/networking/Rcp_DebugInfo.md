# Rcp_DebugInfo

**概述**

描述存储在[Rcp_Response](Rcp_Response.md)中的调试信息的结构。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| Rcp_DebugEventtype | 调试事件类型。 |
| Rcp_Bufferdata | 调试信息。 |
| struct Rcp_DebugInfo * next | 链式存储。指向下一个Rcp_DebugInfo。 |

**结构体成员变量说明**

**data**

```ets
Rcp_Buffer Rcp_DebugInfo::data
```

描述

调试信息。

**next**

```ets
struct Rcp_DebugInfo* Rcp_DebugInfo::next
```

描述

链式存储。指向下一个[Rcp_DebugInfo](Rcp_DebugInfo.md#ZH-CN_TOPIC_0000002522081544__rcp_debuginfo)。

**type**

```ets
Rcp_DebugEvent Rcp_DebugInfo::type
```

描述

调试事件类型。