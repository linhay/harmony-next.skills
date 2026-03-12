# OhosImageSource

```ets
struct OhosImageSource {...}
```

#### 概述

定义图像源输入资源，每次仅接收一种类型。由[OH_ImageSource_CreateFromUri](image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createfromuri)、[OH_ImageSource_CreateFromFd](image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createfromfd)和[OH_ImageSource_CreateFromData](image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_createfromdata)获取。

**起始版本：** 10

**废弃版本：** 11

**相关模块：**[Image](Image.md)

**所在头文件：**[image_source_mdk.h](image_source_mdk.h.md)

#### 汇总

#### 成员变量

名称描述char* uri = nullptr图像源资源标识符，接受文件资源或者base64资源。size_t uriSize = 0图像源资源长度。int32_t fd = - 1图像源文件资源描述符。uint8_t* buffer = nullptr图像源缓冲区资源，接受格式化包缓冲区或者base64缓冲区。size_t bufferSize = 0图像源缓冲区资源大小。