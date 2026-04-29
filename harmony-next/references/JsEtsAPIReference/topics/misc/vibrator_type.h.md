# vibrator_type.h

**概述**

为您提供标准的开放api，用于控制马达振动的启停

引用文件： <sensors/vibrator_type.h>

库： libohvibrator.z.so

系统能力： SystemCapability.Sensors.MiscDevice

起始版本： 11

相关模块： [Vibrator](Vibrator.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Vibrator_Attribute | Vibrator_Attribute | 马达属性。 |
| Vibrator_FileDescription | Vibrator_FileDescription | 振动文件描述。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Vibrator_ErrorCode | Vibrator_ErrorCode | 为用户定义错误码。 |
| Vibrator_Usage | Vibrator_Usage | 振动优先级。 |

**枚举类型说明**

**Vibrator_ErrorCode**

```ets
enum Vibrator_ErrorCode
```

描述

为用户定义错误码。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| PERMISSION_DENIED = 201 | 权限校验失败。 |
| PARAMETER_ERROR = 401 | 参数检查失败，包括必选参数没有传入，参数类型错误等。 |
| UNSUPPORTED = 801 | 该设备不支持此 API，通常用于在设备已支持该 SysCap 时，针对其少量的 API 的支持处理。 |
| DEVICE_OPERATION_FAILED = 14600101 | 设备操作失败。 |

**Vibrator_Usage**

```ets
enum Vibrator_Usage
```

描述

振动优先级。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| VIBRATOR_USAGE_UNKNOWN = 0 | 未知场景 |
| VIBRATOR_USAGE_ALARM = 1 | 报警 |
| VIBRATOR_USAGE_RING = 2 | 铃声 |
| VIBRATOR_USAGE_NOTIFICATION = 3 | 通知 |
| VIBRATOR_USAGE_COMMUNICATION = 4 | 通信 |
| VIBRATOR_USAGE_TOUCH = 5 | 触摸 |
| VIBRATOR_USAGE_MEDIA = 6 | 媒体 |
| VIBRATOR_USAGE_PHYSICAL_FEEDBACK = 7 | 物理反馈 |
| VIBRATOR_USAGE_SIMULATED_REALITY = 8 | 模拟现实 |