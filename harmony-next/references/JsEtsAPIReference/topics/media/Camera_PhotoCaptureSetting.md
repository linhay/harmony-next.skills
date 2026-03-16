# Camera_PhotoCaptureSetting

```ets
typedef struct Camera_PhotoCaptureSetting {...} Camera_PhotoCaptureSetting
```

#### 概述

要设置的拍照捕获选项。

**起始版本：** 11

**相关模块：**[OH_Camera](OH_Camera.md)

**所在头文件：**[camera.h](../../capi/headers/camera.h.md)

#### 汇总

#### 成员变量

名称描述[Camera_QualityLevel](../../capi/headers/camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_qualitylevel) quality拍照图像质量。[Camera_ImageRotation](../../capi/headers/camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_imagerotation) rotation拍照旋转角度。[Camera_Location](Camera_Location.md)* location拍照位置。bool mirror

设置镜像拍照功能开关。

 true为打开，false为关闭，默认为false。