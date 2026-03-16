# OhosImageSourceSupportedFormatList

```ets
struct OhosImageSourceSupportedFormatList {...}
```

#### 概述

定义图像源支持的格式字符串列表。由[OH_ImageSource_GetSupportedFormats](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_getsupportedformats)获取。

**起始版本：** 10

**相关模块：**[Image](../graphics/Image.md)

**所在头文件：**[image_source_mdk.h](../../capi/headers/image_source_mdk.h.md)

#### 汇总

#### 成员变量

名称描述struct [OhosImageSourceSupportedFormat](../graphics/OhosImageSourceSupportedFormat.md)** supportedFormatList = nullptr图像源支持的格式字符串列表头地址。size_t size = 0图像源支持的格式字符串列表大小。