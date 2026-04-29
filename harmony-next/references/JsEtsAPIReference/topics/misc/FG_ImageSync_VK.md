# FG_ImageSync_VK

**概述**

此结构体描述超帧输入输出图像同步状态信息，用于创建超帧图像内存屏障。

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [frame_generation_vk.h](frame_generation_vk.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| VkAccessFlagBits accessMask | 内存访问类型的位掩码。 |
| VkImageLayout layout | 图像和图像子资源的内存布局。 |
| VkPipelineStageFlagBits stages | 管线阶段的位掩码。 |

**结构体成员变量说明**

**accessMask**

```ets
VkAccessFlagBits FG_ImageSync_VK::accessMask
```

描述

内存访问类型的位掩码。

**layout**

```ets
VkImageLayout FG_ImageSync_VK::layout
```

描述

图像和图像子资源的内存布局。

**stages**

```ets
VkPipelineStageFlagBits FG_ImageSync_VK::stages
```

描述

管线阶段的位掩码。