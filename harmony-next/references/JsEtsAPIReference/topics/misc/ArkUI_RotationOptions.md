# ArkUI_RotationOptions

```ets
typedef struct {...} ArkUI_RotationOptions
```

**概述**

定义组件转场时的旋转效果对象。

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_type.h](native_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| float x | 横向的旋转向量分量。 |
| float y | 纵向的旋转向量分量。 |
| float z | 竖向的旋转向量分量。 |
| float angle | 旋转角度。 |
| float centerX | 变换中心点x轴坐标，单位为vp。 |
| float centerY | 变换中心点y轴坐标，单位为vp。 |
| float centerZ | z轴锚点，即3D旋转中心点的z轴分量，单位为px。 |
| float perspective | 视距，即视点到z=0平面的距离，单位为px。 |