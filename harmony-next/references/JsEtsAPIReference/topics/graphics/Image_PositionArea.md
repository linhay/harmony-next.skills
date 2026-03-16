# Image_PositionArea

```ets
typedef struct Image_PositionArea {...} Image_PositionArea
```

#### 概述

要读取或写入的图像像素区域。

**起始版本：** 22

**相关模块：**[Image_NativeModule](Image_NativeModule.md)

**所在头文件：**[image_common.h](../../capi/headers/image_common.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t *pixels读取或写入的图像像素数据。仅支持BRGA_8888格式的数据。size_t pixelsSize图像像素数据的长度（单位：字节）。uint32_t offset数据读取或写入的偏移量（单位：字节）。uint32_t stride区域的跨距，即区域中每行像素所占的空间（单位：字节）。stride >= region.size.width * 4。[Image_Region](Image_Region.md) region读取或写入的区域。区域宽度加X坐标不能大于原图的宽度，区域高度加Y坐标不能大于原图的高度。