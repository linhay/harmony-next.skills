# SecurityAudit_Event

#### 概述

定义审计事件信息。

**起始版本：** 6.0.0(20)

**相关模块：**[SecurityAudit](SecurityAudit.md)

**所在头文件：**[security_audit.h](../../capi/headers/security_audit.h.md)

#### 汇总

#### 成员变量

名称

描述

int64_t [eventId](#ZH-CN_TOPIC_0000002514988501__zh-cn_topic_0000002382857565_a2601bc18ab6afae9e11dc9dc0074f87a)

审计事件ID。

const char * [metadata](#ZH-CN_TOPIC_0000002514988501__zh-cn_topic_0000002382857565_a1b4c390813d35ca2f1cd385517c6fc20)

集成了事件版本号、事件接收时间、设备ID和用户ID的json字符串。

const char * [content](#ZH-CN_TOPIC_0000002514988501__zh-cn_topic_0000002382857565_ab436f59837fd0ecf41248425172d39da)

事件内容。

#### 结构体成员变量说明

#### content

```ets
const char* SecurityAudit_Event::content
```

**描述**

事件内容。

#### eventId

```ets
int64_t SecurityAudit_Event::eventId
```

**描述**

审计事件ID。

#### metadata

```ets
const char* SecurityAudit_Event::metadata
```

**描述**

集成了事件版本号、事件接收时间、设备ID和用户ID的json字符串。