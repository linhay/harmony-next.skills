# Camera_OcclusionDetectionResult

```ets
typedef struct {...} Camera_OcclusionDetectionResult
```

**概述**

相机镜头遮挡、脏污检测结果。

起始版本： 23

相关模块： [OH_Camera](OH_Camera.md)

所在头文件： [camera.h](camera.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| bool isCameraOccluded | 检查相机镜头是否被遮挡。true表示被遮挡，false表示未被遮挡。 |
| bool isCameraLensDirty | 检查相机相机镜头是否有脏污。true表示有脏污，false表示没有脏污。 |