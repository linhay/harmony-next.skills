# ddk_types.h

#### 概述

提供基础DDK接口所使用的Base DDK类型，宏定义，枚举值和数据结构。

**引用文件：** <ddk/ddk_types.h>

**库：** libddk_base.z.so

**系统能力：** SystemCapability.Driver.DDK.Extension

**起始版本：** 12

**相关模块：**[BaseDdk](BaseDdk.md)

#### 汇总

#### 结构体

名称typedef关键字描述[DDK_Ashmem](DDK_Ashmem.md)DDK_Ashmem定义通过接口**OH_DDK_CreateAshmem**创建的共享内存，共享内存的缓冲区提供更好的性能。

#### 枚举

名称typedef关键字描述[DDK_RetCode](#ZH-CN_TOPIC_0000002497445630__ddk_retcode)DDK_RetCode枚举基本DDK中使用的错误代码。

#### 枚举类型说明

#### DDK_RetCode

```ets
enum DDK_RetCode
```

**描述**

枚举基本DDK中使用的错误代码。

**起始版本：** 12

枚举项描述DDK_SUCCESS = 0操作成功DDK_FAILURE = 28600001操作失败DDK_INVALID_PARAMETER = 28600002无效参数DDK_INVALID_OPERATION = 28600003无效操作DDK_NULL_PTR = 28600004空指针异常