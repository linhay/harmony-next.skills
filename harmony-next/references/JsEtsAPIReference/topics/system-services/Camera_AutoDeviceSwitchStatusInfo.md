# Camera_AutoDeviceSwitchStatusInfo

```ets
typedef struct Camera_AutoDeviceSwitchStatusInfo {...} Camera_AutoDeviceSwitchStatusInfo
```

#### 概述

自动设备切换状态信息。

**起始版本：** 13

**相关模块：**[OH_Camera](../media/OH_Camera.md)

**所在头文件：**[camera.h](../../capi/headers/camera.h.md)

#### 汇总

#### 成员变量

名称描述bool isDeviceSwitched设备是否已切换，true表示已切换，false表示未切换。bool isDeviceCapabilityChanged设备功能是否改变，true表示已改变，false表示未改变。