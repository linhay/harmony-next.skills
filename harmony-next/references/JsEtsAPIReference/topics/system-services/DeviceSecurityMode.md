# DeviceSecurityMode

#### 概述

DeviceSecurityMode模块用于管理设备安全模式。

**系统能力：**SystemCapability.Security.SafetyDetect

**起始版本：**5.0.1(13)

#### 汇总

#### 文件

名称

描述

[device_security_mode.h](../../capi/headers/device_security_mode.h.md)

定义与设备安全模式相关的函数。

#### 类型定义

名称

描述

typedef enum [DSM_DeviceSecurityMode](#section1753134381213)[DSM_DeviceSecurityMode](#section17561511173514)

设备安全模式枚举类型定义。

#### 枚举

名称

描述

[DSM_DeviceSecurityMode](#section1753134381213) {

DSM_NORMAL_MODE = 0,

DSM_SECURE_SHIELD_MODE = 1

}

设备安全模式枚举值。

#### 函数

名称

描述

[DSM_DeviceSecurityMode](#section1753134381213)[HMS_DSM_GetDeviceSecurityMode()](#section556519812196)

查询当前设备安全模式。

#### 类型定义说明

#### DSM_DeviceSecurityMode

```ets
typedef enum DSM_DeviceSecurityMode DSM_DeviceSecurityMode
```

**描述**

设备安全模式枚举类型定义。

**起始版本：**5.0.1(13)

#### 枚举说明

#### DSM_DeviceSecurityMode

```ets
enum DSM_DeviceSecurityMode
```

**描述**

枚举设备安全模式。

**起始版本：**5.0.1(13)

枚举值

描述

DSM_NORMAL_MODE

一般模式，为设备默认的安全模式。

DSM_SECURE_SHIELD_MODE

坚盾守护模式，坚盾守护模式用于保护设备不被复杂网络攻击，此模式下部分网页的浏览功能和网络技术会受到限制。

#### 函数说明

#### HMS_DSM_GetDeviceSecurityMode()

```ets
DSM_DeviceSecurityMode HMS_DSM_GetDeviceSecurityMode(void)
```

**描述**

查询当前设备的安全模式。

**起始版本：**5.0.1(13)

**返回：**

返回结果参见枚举类型[DSM_DeviceSecurityMode](#section1753134381213)。