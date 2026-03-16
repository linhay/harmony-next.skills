# vibrator_type.h

#### 概述

为您提供标准的开放api，用于控制马达振动的启停

**引用文件：** <sensors/vibrator_type.h>

**库：** libohvibrator.z.so

**系统能力：** SystemCapability.Sensors.MiscDevice

**起始版本：** 11

**相关模块：**[Vibrator](../../topics/misc/Vibrator.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Vibrator_Attribute](../../topics/misc/Vibrator_Attribute.md)Vibrator_Attribute马达属性。[Vibrator_FileDescription](../../topics/misc/Vibrator_FileDescription.md)Vibrator_FileDescription振动文件描述。

#### 枚举

名称typedef关键字描述[Vibrator_ErrorCode](#ZH-CN_TOPIC_0000002529285639__vibrator_errorcode)Vibrator_ErrorCode为用户定义错误码。[Vibrator_Usage](#ZH-CN_TOPIC_0000002529285639__vibrator_usage)Vibrator_Usage振动优先级。

#### 枚举类型说明

#### Vibrator_ErrorCode

```ets
enum Vibrator_ErrorCode
```

**描述**

为用户定义错误码。

**起始版本：** 11

枚举项描述PERMISSION_DENIED = 201权限校验失败。PARAMETER_ERROR = 401参数检查失败，包括必选参数没有传入，参数类型错误等。UNSUPPORTED = 801该设备不支持此 API，通常用于在设备已支持该 SysCap 时，针对其少量的 API 的支持处理。DEVICE_OPERATION_FAILED = 14600101设备操作失败。

#### Vibrator_Usage

```ets
enum Vibrator_Usage
```

**描述**

振动优先级。

**起始版本：** 11

枚举项描述USAGE_UNKNOWN = 0未知场景USAGE_ALARM = 1报警USAGE_RING = 2铃声USAGE_NOTIFICATION = 3通知USAGE_COMMUNICATION = 4通信USAGE_TOUCH = 5触摸USAGE_MEDIA = 6媒体USAGE_PHYSICAL_FEEDBACK = 7物理反馈USAGE_SIMULATE_REALITY = 8模拟现实