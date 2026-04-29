# OhosPixelMapInfos

```ets
typedef struct OhosPixelMapInfos {...} OhosPixelMapInfos
```

**概述**

用于定义PixelMap的相关信息。

起始版本： 10

相关模块： [Image](Image.md)

所在头文件： [image_pixel_map_mdk.h](image_pixel_map_mdk.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t width | 图片的宽，用pixels表示。 |
| uint32_t height | 图片的高，用pixels表示。 |
| uint32_t rowSize | 图片在内存中，每行所占的字节数。 DMA内存为图片的宽 * 每个像素字节数 + 每行末尾填充字节数；其他内存为图片的宽 * 每个像素字节数。 |
| int32_t pixelFormat | Pixel的格式。 |