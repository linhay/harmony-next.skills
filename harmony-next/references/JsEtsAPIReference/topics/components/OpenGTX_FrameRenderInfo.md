# OpenGTX_FrameRenderInfo

#### 概述

此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](../graphics/GraphicsAccelerate.md)

#### 汇总

#### 成员变量

名称

描述

[OpenGTX_Vector3](../misc/OpenGTX_Vector3.md)[mainCameraPosition](OpenGTX_FrameRenderInfo.md#ZH-CN_TOPIC_0000002385317790__aa3ca65cc999276260b31db3a4a5ec477)

主摄像头的位置。x, y, z的取值范围[-360,360]。

[OpenGTX_Vector3](../misc/OpenGTX_Vector3.md)[mainCameraRotate](OpenGTX_FrameRenderInfo.md#ZH-CN_TOPIC_0000002385317790__a089fb1579868141b741bcd6ee06b8f0b)

主摄像头的转动，包括偏航、俯仰、侧滚。 x, y, z的取值范围[-360,360]。

#### 结构体成员变量说明

#### mainCameraPosition

```ets
[OpenGTX_Vector3](../misc/OpenGTX_Vector3.md) OpenGTX_FrameRenderInfo::mainCameraPosition
```

**描述**

主摄像头的位置。

#### mainCameraRotate

```ets
[OpenGTX_Vector3](../misc/OpenGTX_Vector3.md) OpenGTX_FrameRenderInfo::mainCameraRotate
```

**描述**

主摄像头的转动，包括偏航、俯仰、侧滚。 x, y, z的取值范围[-360,360]。