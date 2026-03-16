# NativeChildProcess_FdList

```ets
typedef struct NativeChildProcess_FdList {...} NativeChildProcess_FdList
```

#### 概述

传递给子进程的文件描述符信息列表，文件描述符记录个数不能超过16个。

**起始版本：** 13

**相关模块：**[ChildProcess](../system-services/ChildProcess.md)

**所在头文件：**[native_child_process.h](../../capi/headers/native_child_process.h.md)

#### 汇总

#### 成员变量

名称描述struct [NativeChildProcess_Fd](../system-services/NativeChildProcess_Fd.md)* head子进程文件描述记录链表中的第一个记录。