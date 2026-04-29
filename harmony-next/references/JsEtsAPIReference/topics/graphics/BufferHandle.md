# BufferHandle

```ets
typedef struct {...} BufferHandle
```

**概述**

缓冲区句柄，用于对缓冲区的信息传递和获取。句柄包含了缓冲区的文件描述符、尺寸、格式、用途、虚拟地址、共享内存键、物理地址、自定义数据。

起始版本： 8

相关模块： [NativeWindow](NativeWindow.md)

所在头文件： [buffer_handle.h](buffer_handle.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t fd | 缓冲区文件描述符，若不支持则为-1。 |
| int32_t width | 缓冲区内存的宽度，单位为像素。 |
| int32_t stride | 缓冲区内存的步幅，单位为字节。 |
| int32_t height | 缓冲区内存的高度，单位为像素。 |
| int32_t size | 缓冲区内存的大小，单位为字节。 |
| int32_t format | 缓冲区内存的格式，取值具体可见OH_NativeBuffer_Format枚举值。 |
| uint64_t usage | 缓冲区内存的用途，按位标志位，取值具体可见OH_NativeBuffer_Format枚举值。 |
| void* virAddr | 缓冲区内存的虚拟地址。 |
| int32_t key | 缓冲区共享内存键值。 |
| uint64_t phyAddr | 缓冲区内存的物理地址。 |
| uint32_t reserveFds | 额外数据的文件描述符数量。 |
| uint32_t reserveInts | 额外数据的整型值数量。 |
| int32_t reserve[0] | 额外数据。 |