# Image_NativeModule

#### 概述

提供图片处理的相关能力，包括图片编解码、从Native层获取图片数据等。

使用该模块的接口，无需通过JS接口导入，可直接使用NDK完成功能开发。

开发者可根据实际的开发需求，参考对应的开发指南及样例：

- [使用Image_NativeModule完成图片解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-c)
- [使用Image_NativeModule完成多图对象解码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-source-picture-c)
- [使用Image_NativeModule完成图片接收](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-receiver-c)
- [使用Image_NativeModule完成位图操作](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pixelmap-c)
- [使用Image_NativeModule完成图片编码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-packer-c)
- [使用Image_NativeModule完成多图对象编码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/image-packer-picture-c)

**起始版本：** 12

#### 文件汇总

名称描述[image_common.h](../../capi/headers/image_common.h.md)声明图像接口使用的公共枚举和结构体。[image_native.h](../../capi/headers/image_native.h.md)声明图像的剪辑矩形、大小和组件数据的接口函数。[image_packer_native.h](../../capi/headers/image_packer_native.h.md)图片编码API。[image_receiver_native.h](../../capi/headers/image_receiver_native.h.md)声明从native层获取图片数据的方法。[image_source_native.h](../../capi/headers/image_source_native.h.md)图片解码API。[picture_native.h](../../capi/headers/picture_native.h.md)提供获取picture数据和信息的API。[pixelmap_native.h](../../capi/headers/pixelmap_native.h.md)访问Pixelmap的API。