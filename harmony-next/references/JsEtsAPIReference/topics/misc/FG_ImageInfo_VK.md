# FG_ImageInfo_VK

**概述**

此结构体描述超帧输入输出图像信息。

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [frame_generation_vk.h](frame_generation_vk.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| FG_Image_VK* image | 超帧输入输出图像结构体FG_Image_VK对象的指针，该图像实例需要通过HMS_FG_CreateImage_VK进行创建，通过HMS_FG_DestroyImage_VK进行销毁。 |
| FG_ImageSync_VK initialSync | HMS_FG_Dispatch_VK执行前，该图像的同步状态。 |
| FG_ImageSync_VK finalSync | HMS_FG_Dispatch_VK执行后，该图像的同步状态。 |

**结构体成员变量说明**

**finalSync**

```ets
FG_ImageSync_VK FG_ImageInfo_VK::finalSync
```

描述

[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002522242234__hms_fg_dispatch_vk)执行后，该图像的同步状态。

**image**

```ets
FG_Image_VK* FG_ImageInfo_VK::image
```

描述

超帧输入输出图像结构体[FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002522242234__fg_image_vk)对象的指针，该图像实例需要通过[HMS_FG_CreateImage_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002522242234__hms_fg_createimage_vk)进行创建，通过[HMS_FG_DestroyImage_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002522242234__hms_fg_destroyimage_vk)进行销毁。

**initialSync**

```ets
FG_ImageSync_VK FG_ImageInfo_VK::initialSync
```

描述

[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002522242234__hms_fg_dispatch_vk)执行前，该图像的同步状态。