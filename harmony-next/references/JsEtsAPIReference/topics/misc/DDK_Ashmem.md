# DDK_Ashmem

```ets
typedef struct DDK_Ashmem {...} DDK_Ashmem
```

#### 概述

定义通过接口**OH_DDK_CreateAshmem**创建的共享内存，共享内存的缓冲区提供更好的性能。

**起始版本：** 12

**相关模块：**[BaseDdk](BaseDdk.md)

**所在头文件：**[ddk_types.h](../../capi/headers/ddk_types.h.md)

#### 汇总

#### 成员变量

名称描述int32_t ashmemFd共享内存的文件描述符。const uint8_t* address缓存区地址。const uint32_t size缓存区大小。uint32_t offset已使用缓冲区的偏移量。默认值为0，表示没有偏移，缓冲区从指定地址开始。uint32_t bufferLength使用的缓冲区长度。默认情况下，该值等于size，表示使用整个缓冲区。uint32_t transferredLength传输数据的长度。