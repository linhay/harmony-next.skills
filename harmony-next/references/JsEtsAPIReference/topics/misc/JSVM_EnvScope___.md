# JSVM_EnvScope__*

```ets
typedef struct JSVM_EnvScope__* JSVM_EnvScope
```

#### 概述

表示用于控制附加到当前虚拟机实例的环境。只有当线程通过OH_JSVM_OpenEnvScope进入该环境的JSVM_EnvScope后，该环境才对线程的虚拟机实例可用。

**起始版本：** 11

**相关模块：**[JSVM](JSVM.md)

**所在头文件：**[jsvm_types.h](../../topics/misc/[jsvm_types.h](jsvm_types.h.md).md)
