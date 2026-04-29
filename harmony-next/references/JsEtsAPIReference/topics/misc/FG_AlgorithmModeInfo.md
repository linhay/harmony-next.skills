# FG_AlgorithmModeInfo

#### 概述

此结构体描述超帧算法模式信息。

**起始版本：** 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [frame_generation_base.h](frame_generation_base.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766) [predictionMode](FG_AlgorithmModeInfo.md#ZH-CN_TOPIC_0000002418916957__a7be414f9af27d0eba30f65b02fdb085d) | 超帧预测算法模式，支持内插模式和外插模式。 |
| [FG_MeMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8bd44b6bea12774dd2ee6014d696e7d1) [meMode](FG_AlgorithmModeInfo.md#ZH-CN_TOPIC_0000002418916957__a9849821d626bc06881e5ee9430c96b83) | 超帧运动估计算法模式，支持基础模式和增强模式。 |

#### 结构体成员变量说明

#### [meMode](FG_AlgorithmModeInfo.md#ZH-CN_TOPIC_0000002418916957__a9849821d626bc06881e5ee9430c96b83)

```ets
[FG_MeMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8bd44b6bea12774dd2ee6014d696e7d1) FG_AlgorithmModeInfo::meMode
```

**描述**

超帧运动估计算法模式，支持基础模式和增强模式。

#### [predictionMode](FG_AlgorithmModeInfo.md#ZH-CN_TOPIC_0000002418916957__a7be414f9af27d0eba30f65b02fdb085d)

```ets
[FG_PredictionMode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766) FG_AlgorithmModeInfo::predictionMode
```

**描述**

超帧预测算法模式，支持内插模式和外插模式。
