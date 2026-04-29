# JSVM_CompileProfile

```ets
typedef const struct {...} JSVM_CompileProfile
```

#### 概述

与JSVM_COMPILE_COMPILE_PROFILE一起传递的编译采样文件。

**起始版本：** 12

**相关模块：**[JSVM](JSVM.md)

所在头文件： [jsvm_types.h](jsvm_types.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| int *profile | 编译采样文件的指针。 |
| size_t length | 编译采样文件的大小。 |