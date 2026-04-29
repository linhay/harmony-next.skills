# NativeChildProcess_Args

```ets
typedef struct {...} NativeChildProcess_Args
```

**概述**

传递给子进程的参数。

起始版本： 13

相关模块： [ChildProcess](ChildProcess.md)

所在头文件： [native_child_process.h](native_child_process.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char* entryParams | 入口参数，大小不能超过150KB。 |
| struct NativeChildProcess_FdList fdList | 传递给子进程的文件描述符信息列表。 |