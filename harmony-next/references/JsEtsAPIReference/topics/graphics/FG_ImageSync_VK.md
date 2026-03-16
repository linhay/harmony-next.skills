# FG_ImageSync_VK

#### 概述

此结构体描述超帧输入输出图像同步状态信息，用于创建超帧图像内存屏障。

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](GraphicsAccelerate.md)

#### 汇总

#### 成员变量

名称

描述

VkAccessFlagBits [accessMask](FG_ImageSync_VK.md#ZH-CN_TOPIC_0000002418797133__a196de1506cbe6e3d50af409137f0c2ba)

内存访问类型的位掩码。

VkImageLayout [layout](FG_ImageSync_VK.md#ZH-CN_TOPIC_0000002418797133__a57ec08087e997e91c937dc30e0a26602)

图像和图像子资源的内存布局。

VkPipelineStageFlagBits [stages](FG_ImageSync_VK.md#ZH-CN_TOPIC_0000002418797133__af1041077c16e8d64f809d5fb42a615e0)

管线阶段的位掩码。

#### 结构体成员变量说明

#### accessMask

```ets
VkAccessFlagBits FG_ImageSync_VK::accessMask
```

**描述**

内存访问类型的位掩码。

#### layout

```ets
VkImageLayout FG_ImageSync_VK::layout
```

**描述**

图像和图像子资源的内存布局。

#### stages

```ets
VkPipelineStageFlagBits FG_ImageSync_VK::stages
```

**描述**

管线阶段的位掩码。