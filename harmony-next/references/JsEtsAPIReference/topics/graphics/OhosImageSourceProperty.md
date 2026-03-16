# OhosImageSourceProperty

```ets
struct OhosImageSourceProperty {...}
```

#### 概述

定义图像源属性键值字符串。此选项给[OH_ImageSource_GetImageProperty](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_getimageproperty)和[OH_ImageSource_ModifyImageProperty](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_modifyimageproperty)接口使用。

**起始版本：** 10

**相关模块：**[Image](Image.md)

**所在头文件：**[image_source_mdk.h](../../capi/headers/image_source_mdk.h.md)

#### 汇总

#### 成员变量

名称描述char* value = nullptr定义图像源属性键值字符串头地址。size_t size = 0定义图像源属性键值字符串大小。