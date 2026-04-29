# device_security_mode.h

**概述**

文件中定义了与设备安全模式相关的函数。

引用文件： <DeviceSecurityKit/device_security_mode.h>

库： libdevice_security_mode.z.so

系统能力： SystemCapability.Security.SafetyDetect

起始版本： 5.0.1(13)

相关模块： [DeviceSecurityMode](DeviceSecurityMode.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum DSM_DeviceSecurityMode DSM_DeviceSecurityMode | 设备安全模式枚举类型定义。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| DSM_DeviceSecurityMode { DSM_NORMAL_MODE = 0, DSM_SECURE_SHIELD_MODE = 1 } | 设备安全模式枚举值。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| DSM_DeviceSecurityMode HMS_DSM_GetDeviceSecurityMode() | 查询当前设备安全模式。 |