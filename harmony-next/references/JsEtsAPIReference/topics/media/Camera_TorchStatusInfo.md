# Camera_TorchStatusInfo

```ets
typedef struct Camera_TorchStatusInfo {...} Camera_TorchStatusInfo
```

#### 概述

手电筒状态信息。

**起始版本：** 12

**相关模块：**[OH_Camera](OH_Camera.md)

所在头文件： [camera.h](camera.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool isTorchAvailable | 手电筒是否可用，true表示可用，false表示不可用。 |
| bool isTorchActive | 手电筒是否激活，true表示激活，false表示未激活。 |
| float torchLevel | 手电筒亮度等级。取值范围为[0,1]，越靠近1，亮度越大。 |