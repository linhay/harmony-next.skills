# vibrator.h

**概述**

为您提供标准的开放api，用于控制马达振动的启停。

引用文件： <sensors/vibrator.h>

库： libohvibrator.z.so

系统能力： SystemCapability.Sensors.MiscDevice

起始版本： 11

相关模块： [Vibrator](Vibrator.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t OH_Vibrator_PlayVibration(int32_t duration, Vibrator_Attribute attribute) | 控制马达在指定时间内持续振动。 |
| int32_t OH_Vibrator_PlayVibrationCustom(Vibrator_FileDescription fileDescription, Vibrator_Attribute vibrateAttribute) | 播放自定义振动序列。 |
| int32_t OH_Vibrator_Cancel() | 停止马达振动。 |

**函数说明**

**OH_Vibrator_PlayVibration()**

```ets
int32_t OH_Vibrator_PlayVibration(int32_t duration, Vibrator_Attribute attribute)
```

描述

控制马达在指定时间内持续振动。

需要权限： ohos.permission.VIBRATE

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t duration | - 振动时长，单位：毫秒。 |
| Vibrator_Attribute attribute | - 振动属性，请参考VibrateAttribute。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功，则返回0；否则返回非零值。请参阅 Vibrator_ErrorCode。 |

**OH_Vibrator_PlayVibrationCustom()**

```ets
int32_t OH_Vibrator_PlayVibrationCustom(Vibrator_FileDescription fileDescription, Vibrator_Attribute vibrateAttribute)
```

描述

播放自定义振动序列。

需要权限： ohos.permission.VIBRATE

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Vibrator_FileDescription fileDescription | - 自定义振动效果文件描述符，请参阅 Vibrator_FileDescription。 |
| Vibrator_Attribute vibrateAttribute | - 振动属性，请参阅 Vibrator_Attribute。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功，则返回0；否则返回非零值。请参阅 Vibrator_ErrorCode。 |

**OH_Vibrator_Cancel()**

```ets
int32_t OH_Vibrator_Cancel()
```

描述

停止马达振动。

需要权限： ohos.permission.VIBRATE

起始版本： 11

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功，则返回0；否则返回非零值。请参阅 Vibrator_ErrorCode。 |