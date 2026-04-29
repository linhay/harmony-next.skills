# ArkUI_ScaleOptions

```ets
typedef struct {...} ArkUI_ScaleOptions
```

**概述**

定义组件转场时的缩放效果对象。

起始版本： 12

相关模块： [ArkUI_NativeModule](ArkUI_NativeModule.md)

所在头文件： [native_type.h](native_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| float x | 横向放大倍数（或缩小比例）。 |
| float y | 纵向放大倍数（或缩小比例）。 |
| float z | 当前为二维显示，该参数无效 。 |
| float centerX | 变换中心点x轴坐标，单位为vp。 |
| float centerY | 变换中心点y轴坐标，单位为vp。 |