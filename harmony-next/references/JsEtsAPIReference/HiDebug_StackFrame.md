# HiDebug_StackFrame

```ets
typedef struct HiDebug_StackFrame {...} HiDebug_StackFrame
```

#### 概述

栈帧内容的定义。

**起始版本：** 20

**相关模块：**[HiDebug](HiDebug.md)

**所在头文件：**[hidebug_type.h](hidebug_type.h.md)

#### 汇总

#### 成员变量

名称描述[HiDebug_StackFrameType](hidebug_type.h.md#ZH-CN_TOPIC_0000002529285663__hidebug_stackframetype) type当前栈的类型。struct [HiDebug_JsStackFrame](HiDebug_JsStackFrame.md) js由[HiDebug_JsStackFrame](HiDebug_JsStackFrame.md)定义的js栈帧内容。struct [HiDebug_NativeStackFrame](HiDebug_NativeStackFrame.md) native由[HiDebug_NativeStackFrame](HiDebug_NativeStackFrame.md)定义的native栈帧内容。