# AREngine_ClipPlaneDistance

**概述**

裁剪平面距离数据。

作为[HMS_AREngine_ARCamera_GetProjectionMatrix](AR Engine.md#ZH-CN_TOPIC_0000002553362039__hms_arengine_arcamera_getprojectionmatrix)接口输入。

起始版本： 5.0.0(12)

相关模块： [AR Engine](AR Engine.md)

所在头文件： [ar_engine_core.h](ar_engine_core.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| float near | OpenGL近裁剪平面距离，以m为单位。 |
| float far | OpenGL远裁剪平面距离，以m为单位。 |

**结构体成员变量说明**

**far**

```ets
float AREngine_ClipPlaneDistance::far
```

描述

OpenGL远裁剪平面距离，以m为单位。

**near**

```ets
float AREngine_ClipPlaneDistance::near
```

描述

OpenGL近裁剪平面距离，以m为单位。