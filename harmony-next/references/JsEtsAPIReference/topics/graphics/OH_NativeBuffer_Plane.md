# OH_NativeBuffer_Plane

```ets
typedef struct {...} OH_NativeBuffer_Plane
```

**概述**

单个图像平面格式信息。

起始版本： 12

相关模块： [OH_NativeBuffer](OH_NativeBuffer.md)

所在头文件： [native_buffer.h](native_buffer.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint64_t offset | 图像平面的偏移量，单位为Byte。 |
| uint32_t rowStride | 从图像一行的第一个值到下一行的第一个值的距离，单位为Byte。 |
| uint32_t columnStride | 从图像一列的第一个值到下一列的第一个值的距离，单位为Byte。 |