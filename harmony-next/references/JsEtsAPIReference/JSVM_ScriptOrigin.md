# JSVM_ScriptOrigin

```ets
typedef struct {...} JSVM_ScriptOrigin
```

#### 概述

某段JavaScript代码的原始信息，如sourceMap路径、源文件名、源文件中的起始行/列号等。

**起始版本：** 12

**相关模块：**[JSVM](JSVM.md)

**所在头文件：**[jsvm_types.h](jsvm_types.h.md)

#### 汇总

#### 成员变量

名称描述const char* sourceMapUrlSourcemap 路径。const char* resourceName源文件名。size_t resourceLineOffset这段代码在源文件中的起始行号。size_t resourceColumnOffset这段代码在源文件中的起始列号。