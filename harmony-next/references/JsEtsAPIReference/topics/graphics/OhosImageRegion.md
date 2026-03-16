# OhosImageRegion

```ets
struct OhosImageRegion {...}
```

#### 概述

定义图像源解码的范围选项。是[OhosImageDecodingOps](OhosImageDecodingOps.md)的成员变量。

**起始版本：** 10

**相关模块：**[Image](Image.md)

**所在头文件：**[image_source_mdk.h](../../capi/headers/image_source_mdk.h.md)

#### 汇总

#### 成员变量

名称描述int32_t x起始x坐标，用pixels表示。int32_t y起始y坐标，用pixels表示。int32_t width宽度范围，用pixels表示。int32_t height高度范围，用pixels表示。