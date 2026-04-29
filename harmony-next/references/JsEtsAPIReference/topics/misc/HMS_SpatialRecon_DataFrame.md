# HMS_SpatialRecon_DataFrame

```ets
typedef struct HMS_SpatialRecon_DataFrame {...} HMS_SpatialRecon_DataFrame
```

**概述**

定义HMS（Huawei Mobile Services）空间重建数据帧的结构体，包含用于空间重建的相机内参、姿态信息、时间戳和图像数据。

起始版本： 6.1.0(23)

相关模块： [SpatialRecon](SpatialRecon.md)

所在头文件： [spatial_recon_interface.h](spatial_recon_interface.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| float focalX = 0.0f | X轴方向的焦距，单位：px。 |
| float focalY = 0.0f | Y轴方向的焦距，单位：px。 |
| float principalX = 0.0f | 主点X坐标（光心），单位：px。 |
| float principalY = 0.0f | 主点Y坐标（光心），单位：px。 |
| float distortionCoef[8] | 失真参数 [k1, k2, p1, p2, k3, k4, k5, k6]。 |
| int32_t imageWidth = 0.0f | 图像的宽度，单位：px。 |
| int32_t imageHeight = 0.0f | 图像的高度，单位：px。 |
| float position[3] | 相机在3D空间中的位置 [x, y, z]。 |
| float rotation[4] | 相机旋转，表示为四元数 [x, y, z, w]。 |
| int64_t timestamp = 0 | 帧捕获的时间戳，单位：ns。 |
| uint8_t *imageData = 0 | 指向原始图像像素数据的指针。 |
| HMS_SpatialReconImageDataFormat format = SPATIAL_RECON_IMAGEDATA_FORMAT_RGB | 图像数据的格式/编码。 |