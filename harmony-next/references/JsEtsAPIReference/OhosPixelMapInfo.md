# OhosPixelMapInfo

```ets
struct OhosPixelMapInfo {...}
```

#### 概述

用于定义PixelMap的相关信息。

**起始版本：** 8

**废弃版本：** 10

**相关模块：**[Image](Image.md)

**所在头文件：**[image_pixel_map_napi.h](image_pixel_map_napi.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t width图片的宽，用pixels表示。uint32_t height图片的高，用pixels表示。uint32_t rowSize

图片在内存中，每行所占的字节数。

DMA内存为图片的宽 * 每个像素字节数 + 每行末尾填充字节数；其他内存为图片的宽 * 每个像素字节数。

int32_t pixelFormat

Pixel的格式，取值范围：

0：未知格式。

2：格式为RGB_565。

3：格式为RGBA_8888。

4：格式为BGRA_8888。

5：格式为RGB_888。

6：格式为ALPHA_8。

7：格式为RGBA_F16。

8：格式为NV21。

9：格式为NV12。