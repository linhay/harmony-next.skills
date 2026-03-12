# OhosImageSourceSupportedFormat

```ets
struct OhosImageSourceSupportedFormat {...}
```

#### 概述

定义图像源支持的格式字符串。此选项给[OhosImageSourceSupportedFormatList](OhosImageSourceSupportedFormatList.md)和[OH_ImageSource_GetSupportedFormats](image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_getsupportedformats)接口使用。

**起始版本：** 10

**相关模块：**[Image](Image.md)

**所在头文件：**[image_source_mdk.h](image_source_mdk.h.md)

#### 汇总

#### 成员变量

名称描述char* format = nullptr图像源支持的格式字符串头地址。size_t size = 0图像源支持的格式字符串大小。