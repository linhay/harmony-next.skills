# BufferHandle

```ets
typedef struct {...} BufferHandle
```

#### 概述

缓冲区句柄，用于对缓冲区的信息传递和获取。句柄包含了缓冲区的文件描述符、尺寸、格式、用途、虚拟地址、共享内存键、物理地址、自定义数据。

**起始版本：** 8

**相关模块：**[NativeWindow](NativeWindow.md)

**所在头文件：**[buffer_handle.h](buffer_handle.h.md)

#### 汇总

#### 成员变量

名称描述int32_t fd缓冲区文件描述符，若不支持则为-1。int32_t width缓冲区内存的宽度，单位为像素。int32_t stride缓冲区内存的步幅，单位为字节。int32_t height缓冲区内存的高度，单位为像素。int32_t size缓冲区内存的大小，单位为字节。int32_t format缓冲区内存的格式，取值具体可见[OH_NativeBuffer_Format](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_format)枚举值。uint64_t usage缓冲区内存的用途，按位标志位，取值具体可见[OH_NativeBuffer_Format](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_format)枚举值。void* virAddr缓冲区内存的虚拟地址。int32_t key缓冲区共享内存键值。uint64_t phyAddr缓冲区内存的物理地址。uint32_t reserveFds额外数据的文件描述符数量。uint32_t reserveInts额外数据的整型值数量。int32_t reserve[0]额外数据。