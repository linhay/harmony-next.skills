# JSVM_ExtendedErrorInfo

```ets
typedef struct {...} JSVM_ExtendedErrorInfo
```

#### 概述

扩展的异常信息。

**起始版本：** 11

**相关模块：**[JSVM](JSVM.md)

**所在头文件：**[jsvm_types.h](../../capi/headers/jsvm_types.h.md)

#### 汇总

#### 成员变量

名称描述const char* errorMessageUTF-8编码的字符串，包含异常信息。void* engineReserved特定于VM的详细异常信息。目前尚未为任何VM实现此功能。uint32_t engineErrorCode特定于VM的异常代码。目前尚未为任何VM实现此功能。JSVM_Status errorCode源自最后一个异常的JSVM-API状态代码。