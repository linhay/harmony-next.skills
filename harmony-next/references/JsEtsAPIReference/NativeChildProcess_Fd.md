# NativeChildProcess_Fd

```ets
typedef struct {...} NativeChildProcess_Fd
```

#### 概述

传递给子进程的文件描述符信息。

**起始版本：** 13

**相关模块：**[ChildProcess](ChildProcess.md)

**所在头文件：**[native_child_process.h](native_child_process.h.md)

#### 汇总

#### 成员变量

名称描述char* fdName文件描述符的键，最大长度为20字符。int32_t fd文件描述符的值。struct [NativeChildProcess_Fd](NativeChildProcess_Fd.md)* next下一个文件描述记录指针。