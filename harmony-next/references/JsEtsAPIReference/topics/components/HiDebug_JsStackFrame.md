# HiDebug_JsStackFrame

```ets
typedef struct HiDebug_JsStackFrame {...} HiDebug_JsStackFrame
```

#### 概述

js栈帧内容的定义。

**起始版本：** 20

**相关模块：**[HiDebug](../misc/HiDebug.md)

**所在头文件：**[hidebug_type.h](../../capi/headers/hidebug_type.h.md)

#### 汇总

#### 成员变量

名称描述uint64_t relativePc相对pc地址。当前pc相对于其所在的映射区域（如可执行文件或共享库）起始地址的偏移量。int32_t line代码所在的行号。当前栈帧对应的代码位于文件的具体行位置。int32_t column代码所在的列号。当前栈帧对应的代码在指定行的具体列位置。const char* mapName映射名称。当前栈帧所属的映射区域的名称。const char* functionName函数名称。当前栈帧对应的函数的名称。const char* urlURL地址。当前栈帧对应代码的文件的URL，无论是本地文件路径还是远程服务器上的文件地址，通过该URL能找到对应的代码文件。const char* packageName包名。当前栈帧对应的代码所属包的名称。