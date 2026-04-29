# HiDebug_StackFrame

```ets
typedef struct HiDebug_StackFrame {...} HiDebug_StackFrame
```

**概述**

栈帧内容的定义。

起始版本： 20

相关模块： [HiDebug](HiDebug.md)

所在头文件： [hidebug_type.h](hidebug_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| HiDebug_StackFrameType type | 当前栈的类型。 |
| struct HiDebug_JsStackFrame js | 由HiDebug_JsStackFrame定义的js栈帧内容。 |
| struct HiDebug_NativeStackFrame native | 由HiDebug_NativeStackFrame定义的native栈帧内容。 |