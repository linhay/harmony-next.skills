# OH_IPC_MessageOption

```ets
typedef struct {...} OH_IPC_MessageOption
```

#### 概述

IPC消息选项定义。

**起始版本：** 12

**相关模块：**[OHIPCRemoteObject](OHIPCRemoteObject.md)

所在头文件： [ipc_cremote_object.h](ipc_cremote_object.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| OH_IPC_RequestMode mode | 消息请求模式。 |
| uint32_t timeout | RPC预留参数，该参数对IPC无效。 |
| void* reserved | 保留参数，必须为空 |