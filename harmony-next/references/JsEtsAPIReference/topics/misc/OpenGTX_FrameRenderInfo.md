# OpenGTX_FrameRenderInfo

**概述**

此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [opengtx_base.h](opengtx_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| OpenGTX_Vector3 mainCameraPosition | 主摄像头的位置。x, y, z的取值范围[-360,360]。 |
| OpenGTX_Vector3 mainCameraRotate | 主摄像头的转动，包括偏航、俯仰、侧滚。 x, y, z的取值范围[-360,360]。 |

**结构体成员变量说明**

**mainCameraPosition**

```ets
OpenGTX_Vector3 OpenGTX_FrameRenderInfo::mainCameraPosition
```

描述

主摄像头的位置。

**mainCameraRotate**

```ets
OpenGTX_Vector3 OpenGTX_FrameRenderInfo::mainCameraRotate
```

描述

主摄像头的转动，包括偏航、俯仰、侧滚。 x, y, z的取值范围[-360,360]。