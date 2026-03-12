# HiAppEvent_AppEventInfo

```ets
typedef struct HiAppEvent_AppEventInfo {...} HiAppEvent_AppEventInfo
```

#### 概述

单个事件信息，包含事件领域、事件名称、事件类型和事件携带的用json格式字符串表示的自定义参数列表。

**起始版本：** 12

**相关模块：**[HiAppEvent](HiAppEvent.md)

**所在头文件：**[hiappevent.h](hiappevent.h.md)

#### 汇总

#### 成员变量

名称描述const char* domain事件领域。const char* name事件名称。enum [EventType](hiappevent.h.md#ZH-CN_TOPIC_0000002497605668__eventtype) type事件类型。const char* paramsJson格式字符串类型的事件参数列表。