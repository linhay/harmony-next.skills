# FG_ResolutionInfo

#### 概述

此结构体描述超帧输入输出图像的分辨率。

**起始版本：** 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [frame_generation_base.h](frame_generation_base.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FG_Dimension2D](FG_Dimension2D.md) [inputColorResolution](FG_ResolutionInfo.md#ZH-CN_TOPIC_0000002385317774__af99a47a1f71f8c13d8f5dff8ac02d137) | 真实渲染帧颜色缓冲区分辨率。 |
| FG_Dimension2D [inputDepthStencilResolution](FG_ResolutionInfo.md#ZH-CN_TOPIC_0000002385317774__a0938887b43f2d9353d836a95c1ce0c81) | 真实渲染帧深度模板缓冲区分辨率。当设置成0时, 系统中会默认使用inputColorResolution作为真实帧深度模板缓冲区分辨率。 |
| FG_Dimension2D [outputColorResolution](FG_ResolutionInfo.md#ZH-CN_TOPIC_0000002385317774__a69fd8491d75c622c2a21bc0278278965) | 预测帧缓冲区分辨率。当设置成0时, 系统中会默认使用inputColorResolution作为预测帧缓冲区分辨率。 |

#### 结构体成员变量说明

#### [inputColorResolution](FG_ResolutionInfo.md#ZH-CN_TOPIC_0000002385317774__af99a47a1f71f8c13d8f5dff8ac02d137)

```ets
[FG_Dimension2D](FG_Dimension2D.md) FG_ResolutionInfo::inputColorResolution
```

**描述**

真实渲染帧颜色缓冲区分辨率。

#### [inputDepthStencilResolution](FG_ResolutionInfo.md#ZH-CN_TOPIC_0000002385317774__a0938887b43f2d9353d836a95c1ce0c81)

```ets
[FG_Dimension2D](FG_Dimension2D.md) FG_ResolutionInfo::inputDepthStencilResolution
```

**描述**

真实渲染帧深度模板缓冲区分辨率。当设置成0时, 系统中会默认使用[inputColorResolution](#ZH-CN_TOPIC_0000002553202209__inputcolorresolution)作为真实帧深度模板缓冲区分辨率。

#### [outputColorResolution](FG_ResolutionInfo.md#ZH-CN_TOPIC_0000002385317774__a69fd8491d75c622c2a21bc0278278965)

```ets
[FG_Dimension2D](FG_Dimension2D.md) FG_ResolutionInfo::outputColorResolution
```

**描述**

预测帧缓冲区分辨率。当设置成0时, 系统中会默认使用[inputColorResolution](#ZH-CN_TOPIC_0000002553202209__inputcolorresolution)作为预测帧缓冲区分辨率。
