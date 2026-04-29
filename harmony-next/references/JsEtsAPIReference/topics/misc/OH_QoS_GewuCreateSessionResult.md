# OH_QoS_GewuCreateSessionResult

```ets
typedef struct { ... } OH_QoS_GewuCreateSessionResult
```

#### 概述

OH_QoS_GewuCreateSession()接口的返回结果，成功时返回创建的 session，失败时 error 会置为对应的错误码 。

**起始版本：** 20

**相关模块：**[QoS](QoS.md)

所在头文件： [qos.h](qos.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH_QoS_GewuSession](qos.h.md#ZH-CN_TOPIC_0000002497605598__变量) session | 创建出来的会话句柄 |
| [OH_QoS_GewuErrorCode](qos.h.md#ZH-CN_TOPIC_0000002497605598__oh_qos_gewuerrorcode) error | 错误码- 创建会话成功返回OH_QOS_GEWU_OK。- 由于没有足够的内存而创建会话失败返回OH_QOS_GEWU_NOMEM。 |
