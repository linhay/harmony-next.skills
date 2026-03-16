# OH_IPC_MessageOption

```ets
typedef struct {...} OH_IPC_MessageOption
```

#### 概述

IPC消息选项定义。

**起始版本：** 12

**相关模块：**[OHIPCRemoteObject](OHIPCRemoteObject.md)

**所在头文件：**[ipc_cremote_object.h](../../capi/headers/ipc_cremote_object.h.md)

#### 汇总

#### 成员变量

名称描述OH_IPC_RequestMode mode消息请求模式。uint32_t timeoutRPC预留参数，该参数对IPC无效。void* reserved保留参数，必须为空