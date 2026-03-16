# OhosImageSourceUpdateData

```ets
struct OhosImageSourceUpdateData {...}
```

#### 概述

定义图像源更新数据选项，由[OH_ImageSource_UpdateData](../../capi/headers/image_source_mdk.h.md#ZH-CN_TOPIC_0000002529285849__oh_imagesource_updatedata)获取。

**起始版本：** 10

**相关模块：**[Image](Image.md)

**所在头文件：**[image_source_mdk.h](../../capi/headers/image_source_mdk.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t* buffer = nullptr图像源更新数据缓冲区。size_t bufferSize = 0图像源更新数据缓冲区大小。uint32_t offset = 0图像源更新数据缓冲区的开端。uint32_t updateLength = 0图像源更新数据缓冲区的更新数据长度。int8_t isCompleted = 0图像源更新数据在此节中完成。