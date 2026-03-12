# OhosImageReceiverInfo

```ets
struct OhosImageReceiverInfo {...}
```

#### 概述

定义ImageReceiver的相关信息。

**起始版本：** 10

**相关模块：**[Image](Image.md)

**所在头文件：**[image_receiver_mdk.h](image_receiver_mdk.h.md)

#### 汇总

#### 成员变量

名称描述int32_t width消费端接收图片时的默认图像宽度，用pixels表示。int32_t height消费端接收图片时的默认图像高度，用pixels表示。int32_t format通过接收器创建图像格式OHOS_IMAGE_FORMAT_JPEG。int32_t capicity图片缓存数量的最大值。该参数仅作为期望值，实际capacity由设备硬件决定。