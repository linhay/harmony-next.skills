# OH_NativeBundle_ApplicationInfo

```ets
typedef struct {...} OH_NativeBundle_ApplicationInfo
```

#### 概述

应用包信息数据结构，包含应用包名和应用指纹信息。

**起始版本：** 9

**相关模块：**[Native_Bundle](../misc/Native_Bundle.md)

**所在头文件：**[native_interface_bundle.h](../../capi/headers/native_interface_bundle.h.md)

#### 汇总

#### 成员变量

名称描述char* bundleName应用包名。char* fingerprint应用的指纹信息，由签名证书通过SHA-256算法计算哈希值生成。使用的签名证书发生变化时，该字段也会发生变化。