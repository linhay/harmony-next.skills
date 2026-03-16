[]()[]()

# Image

[]()[]()

#### 概述

提供image接口的访问。

开发者可根据实际的开发需求，参考对应的开发指南及样例：

- [图片解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-decoding-native)
- [图片编码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-encoding-native)
- [图像变换](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-transformation-native)
- [位图操作](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-pixelmap-operation-native)
- [图片接收](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-receiver-native)

**起始版本：** 8

[]()[]()

#### 文件汇总

名称描述[image_mdk.h](../../capi/headers/image_mdk.h.md)声明访问图像矩形、大小、格式和组件数据的函数。[image_mdk_common.h](../../capi/headers/image_mdk_common.h.md)声明图像常用的枚举值和结构体。[image_packer_mdk.h](../../capi/headers/image_packer_mdk.h.md)声明用于将图像编码到缓冲区或文件的api。可用于将像素数据编码到目标缓冲区或文件中。[image_pixel_map_mdk.h](../../capi/headers/image_pixel_map_mdk.h.md)声明可以锁定并访问pixelmap数据的方法，声明解锁的方法。[image_pixel_map_napi.h](../../capi/headers/image_pixel_map_napi.h.md)声明可以锁定并访问pixelmap数据的方法，声明解锁的方法。[image_receiver_mdk.h](../../capi/headers/image_receiver_mdk.h.md)声明从native层获取图片数据的方法。[image_source_mdk.h](../../capi/headers/image_source_mdk.h.md)声明将图片源解码成像素位图的方法。