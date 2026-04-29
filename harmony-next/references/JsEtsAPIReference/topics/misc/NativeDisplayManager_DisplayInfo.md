# NativeDisplayManager_DisplayInfo

```ets
typedef struct {...} NativeDisplayManager_DisplayInfo
```

#### 概述

显示设备的对象属性。

**起始版本：** 14

**相关模块：**[OH_DisplayManager](OH_DisplayManager.md)

所在头文件： [oh_display_info.h](oh_display_info.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32_t id | 显示设备的屏幕id号，为非负整数。 |
| char name[OH_DISPLAY_NAME_LENGTH + 1] | 显示设备的名称。 |
| bool isAlive | 显示设备是否启用：true表示设备启动，false表示设备未启用。 |
| int32_t width | 显示设备的屏幕宽度，单位为px，该参数应为非负整数。 |
| int32_t height | 显示设备的屏幕高度，单位为px，该参数应为非负整数。 |
| int32_t physicalWidth | 显示设备的物理宽度，单位为px，该参数应为非负整数。 |
| int32_t physicalHeight | 显示设备的物理高度，单位为px，该参数应为非负整数。 |
| uint32_t refreshRate | 显示设备的刷新率，单位为Hz，该参数应为非负整数。 |
| uint32_t availableWidth | 2in1设备上屏幕的可用区域宽度，单位为px，该参数为非负整数。 |
| uint32_t availableHeight | 2in1设备上屏幕的可用区域高度，单位为px，该参数为大于0的整数。 |
| float densityDPI | 显示设备屏幕的物理像素密度，表示每英寸上的像素点数。该参数为大于0的浮点数，单位为px。一般取值160.0、480.0等，实际能取到的值取决于不同设备设置里提供的可选值。 |
| float densityPixels | 显示设备逻辑像素的密度，代表物理像素与逻辑像素的缩放系数。该参数为大于0的浮点数，受densityDPI范围限制，取值范围在[0.5，4.0]。一般取值1.0、3.0等，实际取值取决于不同设备提供的densityDPI。 |
| float scaledDensity | 显示设备的显示字体的缩放因子。该参数为大于0的浮点数，通常与densityPixels相同。 |
| float xDPI | 显示设备x方向中每英寸屏幕的确切物理像素值，该参数为大于0的浮点数。 |
| float yDPI | 显示设备y方向中每英寸屏幕的确切物理像素值，该参数为大于0的浮点数。 |
| [NativeDisplayManager_Rotation](oh_display_info.h.md#ZH-CN_TOPIC_0000002529285077__nativedisplaymanager_rotation) rotation | 显示设备的屏幕顺时针旋转角度。 |
| [NativeDisplayManager_DisplayState](oh_display_info.h.md#ZH-CN_TOPIC_0000002529285077__nativedisplaymanager_displaystate) state | 显示设备的状态。 |
| [NativeDisplayManager_Orientation](oh_display_info.h.md#ZH-CN_TOPIC_0000002529285077__nativedisplaymanager_orientation) orientation | 表示屏幕当前显示的方向。 |
| [NativeDisplayManager_DisplayHdrFormat](NativeDisplayManager_DisplayHdrFormat.md)* hdrFormat | 显示设备支持的所有HDR格式。 |
| [NativeDisplayManager_DisplayColorSpace](NativeDisplayManager_DisplayColorSpace.md)* colorSpace | 显示设备支持的所有色域类型。 |
