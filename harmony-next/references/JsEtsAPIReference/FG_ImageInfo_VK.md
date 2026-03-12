# FG_ImageInfo_VK

#### 概述

此结构体描述超帧输入输出图像信息。

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](GraphicsAccelerate.md)

#### 汇总

#### 成员变量

名称

描述

[FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)* [image](FG_ImageInfo_VK.md#ZH-CN_TOPIC_0000002385157854__af7d7acd5e8c8ea5968966fd5dae79c53)

超帧输入输出图像结构体[FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)对象的指针，该图像实例需要通过[HMS_FG_CreateImage_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga7733f097ea5f4ae4d2aa53d11d7e60ff)进行创建，通过[HMS_FG_DestroyImage_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gac850c7cd41a1aebaf9bcf943ebff372a)进行销毁。

[FG_ImageSync_VK](FG_ImageSync_VK.md)[initialSync](FG_ImageInfo_VK.md#ZH-CN_TOPIC_0000002385157854__ac14678edc22ab154772896a680f65038)

[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)执行前，该图像的同步状态。

[FG_ImageSync_VK](FG_ImageSync_VK.md)[finalSync](FG_ImageInfo_VK.md#ZH-CN_TOPIC_0000002385157854__ab14f8dc283ce6e769d0d598bc3c812a8)

[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)执行后，该图像的同步状态。

#### 结构体成员变量说明

#### finalSync

```ets
[FG_ImageSync_VK](FG_ImageSync_VK.md) FG_ImageInfo_VK::finalSync
```

**描述**

[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)执行后，该图像的同步状态。

#### image

```ets
[FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)* FG_ImageInfo_VK::image
```

**描述**

超帧输入输出图像结构体[FG_Image_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabd6ee9704e997ffc2792ad3c89847019)对象的指针，该图像实例需要通过[HMS_FG_CreateImage_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga7733f097ea5f4ae4d2aa53d11d7e60ff)进行创建，通过[HMS_FG_DestroyImage_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gac850c7cd41a1aebaf9bcf943ebff372a)进行销毁。

#### initialSync

```ets
[FG_ImageSync_VK](FG_ImageSync_VK.md) FG_ImageInfo_VK::initialSync
```

**描述**

[HMS_FG_Dispatch_VK](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga21f86a194e72e99dd54fd39080385a37)执行前，该图像的同步状态。