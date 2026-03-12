# OH_ImageSource_Info

```ets
struct OH_ImageSource_Info
```

#### 概述

OH_ImageSource_Info是native层封装的ImageSource信息结构体，OH_ImageSource_Info结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

创建OH_ImageSource_Info对象使用[OH_ImageSourceInfo_Create](image_source_native.h.md#ZH-CN_TOPIC_0000002497445874__oh_imagesourceinfo_create)函数。

释放OH_ImageSource_Info对象使用[OH_ImageSourceInfo_Release](image_source_native.h.md#ZH-CN_TOPIC_0000002497445874__oh_imagesourceinfo_release)函数。

OH_ImageSource_Info结构体内容和操作方式如下：

字段类型字段名称字段描述操作函数函数描述uint32_twidth图片宽度[OH_ImageSourceInfo_GetWidth](image_source_native.h.md#ZH-CN_TOPIC_0000002497445874__oh_imagesourceinfo_getwidth)获取图片的宽。uint32_theight图片高度[OH_ImageSourceInfo_GetHeight](image_source_native.h.md#ZH-CN_TOPIC_0000002497445874__oh_imagesourceinfo_getheight)获取图片的高。boolisHdr是否为高动态范围的信息[OH_ImageSourceInfo_GetDynamicRange](image_source_native.h.md#ZH-CN_TOPIC_0000002497445874__oh_imagesourceinfo_getdynamicrange)获取图片是否为高动态范围的信息。

**起始版本：** 13

**相关模块：**[Image_NativeModule](Image_NativeModule.md)

**所在头文件：**[image_source_native.h](image_source_native.h.md)