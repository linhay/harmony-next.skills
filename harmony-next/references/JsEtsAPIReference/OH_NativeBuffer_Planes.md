# OH_NativeBuffer_Planes

```ets
typedef struct OH_NativeBuffer_Planes {...} OH_NativeBuffer_Planes
```

#### 概述

OH_NativeBuffer的图像平面格式信息。

**起始版本：** 12

**相关模块：**[OH_NativeBuffer](OH_NativeBuffer.md)

**所在头文件：**[native_buffer.h](native_buffer.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t planeCount不同平面的数量。[OH_NativeBuffer_Plane](OH_NativeBuffer_Plane.md) planes[4]图像平面格式信息数组。