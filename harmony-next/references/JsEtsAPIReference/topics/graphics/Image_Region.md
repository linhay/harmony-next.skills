# Image_Region

```ets
struct Image_Region {...}
```

#### 概述

待解码的图像源区域结构体。

**起始版本：** 12

**相关模块：**[Image_NativeModule](Image_NativeModule.md)

**所在头文件：**[image_common.h](../../capi/headers/image_common.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t x区域横坐标，不能大于原图的宽度。uint32_t y区域纵坐标，不能大于原图的高度。uint32_t width输出图片的宽，单位：像素。uint32_t height输出图片的高，单位：像素。