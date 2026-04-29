# FG_PerFrameExtendedCameraInfo

**概述**

此结构体描述相机扩展信息。当视图投影矩阵的平移分量非常大时，可以提供更加详细的相机信息以获得更加准确的超帧预测效果。

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [frame_generation_base.h](frame_generation_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| FG_Mat4x4 proj | 相机投影矩阵，即从视图空间到裁剪空间坐标系的转换矩阵。 |
| FG_Mat4x4 translatedInvViewProj | 平移视图投影矩阵的逆矩阵，即从裁剪空间到以相机为中心的世界空间坐标系的转换矩阵。 |
| FG_Mat4x4 translatedView | 平移视图矩阵，即从以相机为中心的世界空间到视图空间坐标系的转换矩阵。 |
| FG_Mat4x4 translatedViewProj | 平移视图投影矩阵，即从以相机为中心的世界空间到裁剪空间坐标系的转换矩阵。 |
| FG_Vec3D worldPosition | 相机世界空间坐标。 |

**结构体成员变量说明**

**proj**

```ets
FG_Mat4x4 FG_PerFrameExtendedCameraInfo::proj
```

描述

相机投影矩阵，即从视图空间到裁剪空间坐标系的转换矩阵。

**translatedInvViewProj**

```ets
FG_Mat4x4 FG_PerFrameExtendedCameraInfo::translatedInvViewProj
```

描述

平移视图投影矩阵的逆矩阵，即从裁剪空间到以相机为中心的世界空间坐标系的转换矩阵。

**translatedView**

```ets
FG_Mat4x4 FG_PerFrameExtendedCameraInfo::translatedView
```

描述

平移视图矩阵，即从以相机为中心的世界空间到视图空间坐标系的转换矩阵。

**translatedViewProj**

```ets
FG_Mat4x4 FG_PerFrameExtendedCameraInfo::translatedViewProj
```

描述

平移视图投影矩阵，即从以相机为中心的世界空间到裁剪空间坐标系的转换矩阵。

**worldPosition**

```ets
FG_Vec3D FG_PerFrameExtendedCameraInfo::worldPosition
```

描述

相机世界空间坐标。