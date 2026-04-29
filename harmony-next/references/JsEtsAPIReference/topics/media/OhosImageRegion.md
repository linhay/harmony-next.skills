# OhosImageRegion

```ets
struct OhosImageRegion {...}
```

**概述**

定义图像源解码的范围选项。是[OhosImageDecodingOps](OhosImageDecodingOps.md)的成员变量。

起始版本： 10

相关模块： [Image](Image.md)

所在头文件： [image_source_mdk.h](image_source_mdk.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t x | 起始x坐标，用pixels表示。 |
| int32_t y | 起始y坐标，用pixels表示。 |
| int32_t width | 宽度范围，用pixels表示。 |
| int32_t height | 高度范围，用pixels表示。 |