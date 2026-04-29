# ABR_CameraData

**概述**

此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [abr_base.h](abr_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| ABR_Vector3 rotation | 相机变换的世界空间旋转欧拉角。 |
| ABR_Vector3 position | 相机变换的世界空间位移。 |

**结构体成员变量说明**

**position**

```ets
ABR_Vector3 ABR_CameraData::position
```

描述

相机变换的世界空间位移。

**rotation**

```ets
ABR_Vector3 ABR_CameraData::rotation
```

描述

相机变换的世界空间旋转欧拉角。