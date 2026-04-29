# constant（星闪公共常量定义）

本模块提供了共用的一些常量定义。

起始版本： 5.0.1(13)

**导入模块**

```ets
import { constant } from '@kit.NearLinkKit';
```

**PairingState**

表示和远端设备的配对状态，为枚举值。

系统能力： SystemCapability.Communication.NearLink.Core

起始版本： 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAIRING_STATE_NONE | 1 | 表示未配对。 |
| PAIRING_STATE_PAIRING | 2 | 表示配对中。 |
| PAIRING_STATE_PAIRED | 3 | 表示已配对。 |

**ConnectionState**

表示和远端设备的连接状态，为枚举值。

系统能力： SystemCapability.Communication.NearLink.Core

起始版本： 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE_CONNECTING | 0 | 表示正在连接。 |
| STATE_CONNECTED | 1 | 表示已连接。 |
| STATE_DISCONNECTING | 2 | 表示正在断连。 |
| STATE_DISCONNECTED | 3 | 表示已断连。 |

**DeviceClass**

表示设备类型，为枚举值。

系统能力： SystemCapability.Communication.NearLink.Core

起始版本： 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE_UNCATEGORIZED | 0x000100 | 未分类设备。 |
| DEVICE_PHONE | 0x000200 | 电话。 |
| DEVICE_SMARTPHONE | 0x000201 | 智能手机。 |
| DEVICE_COMPUTER | 0x000300 | 计算机。 |
| DEVICE_LAPTOP | 0x000301 | 笔记本电脑。 |
| DEVICE_TABLET | 0x000302 | 平板。 |
| DEVICE_ALL_IN_ONE_COMPUTER | 0x000303 | 2in1。 |
| DEVICE_MINI_PC | 0x000304 | 迷你PC。 |
| DEVICE_WATCH | 0x000400 | 手表。 |
| DEVICE_SMART_WATCH | 0x000401 | 智能手表。 |
| DEVICE_HUMAN_INTERFACE | 0x000500 | 人机接口。 |
| DEVICE_KEYBOARD | 0x000501 | 键盘。 |
| DEVICE_MOUSE | 0x000502 | 鼠标。 |
| DEVICE_HANDLE | 0x000503 | 手柄。 |
| DEVICE_STYLUS | 0x000504 | 手写笔。 |
| DEVICE_TOUCHPAD | 0x000505 | 触摸板。 |
| DEVICE_AUDIO_PLAYBACK | 0x000600 | 音频播放器。 |
| DEVICE_SMART_SPEAKER | 0x000601 | 智能扬声器。 |
| DEVICE_ECHO_WALL | 0x000602 | 回音设备。 |
| DEVICE_AUDIO_CAPTURE | 0x000700 | 录音器。 |
| DEVICE_KARAOKE_MICROPHONE | 0x000701 | 卡拉OK麦克风。 |
| DEVICE_LAPEL_MICROPHONE | 0x000702 | 佩戴式话筒。 |
| DEVICE_WEARABLE_AUDIO | 0x000800 | 穿戴音频设备。 |
| DEVICE_IN_EAR_EARPHONE | 0x000801 | 入耳式耳机。 |
| DEVICE_HEADSET | 0x000802 | 头戴式受话器。 |
| DEVICE_OVER_EAR_HEADPHONE | 0x000803 | 头戴式耳机。 |
| DEVICE_NECKBAND_EARPHONE | 0x000804 | 颈带式耳机。 |
| DEVICE_PERSONAL_CARE | 0x000900 | 个人护理。 |
| DEVICE_INTELLIGENT_TOOTHBRUSH | 0x000901 | 智能牙刷。 |
| DEVICE_SMART_CUP | 0x000902 | 智能杯。 |
| DEVICE_INTELLIGENT_SHAVER | 0x000903 | 智能剃刀。 |
| DEVICE_HVAC | 0x000A00 | 空调HVAC(Ventilating and Air Conditioning)。 |
| DEVICE_AIR_PURIFIER | 0x000A01 | 空气净化器。 |
| DEVICE_HUMIDIFIER | 0x000A02 | 加湿器。 |
| DEVICE_AIR_CIRCULATION_FAN | 0x000A03 | 空气循环风机。 |
| DEVICE_ELECTRIC_RIDE | 0x000B00 | 电动骑行工具。 |
| DEVICE_ELECTRIC_SCOOTER | 0x000B01 | 电动滑板车。 |
| DEVICE_ELECTRIC_BICYCLE | 0x000B02 | 电动自行车。 |
| DEVICE_LIGHT_FITTING | 0x000C00 | 灯具配件。 |
| DEVICE_SMART_TABLE_LAMP | 0x000C01 | 智能台灯。 |
| DEVICE_REMOTE_CONTROL | 0x000D00 | 远程控制设备。 |
| DEVICE_TV_REMOTE_CONTROL | 0x000D01 | 电视遥控器。 |
| DEVICE_IMAGING | 0x000E00 | 成像设备。 |
| DEVICE_SMART_TV | 0x000E01 | 智能TV。 |
| DEVICE_IP_CAMERA | 0x000E02 | 网络摄像机。 |
| DEVICE_SCREEN_CASTER | 0x000E03 | 投影仪。 |
| DEVICE_NETWORKING | 0x000F00 | 网络设备。 |
| DEVICE_IOT_GATEWAY | 0x000F01 | 物联网网关。 |
| DEVICE_ACCESS_CONTROL | 0x001000 | 门禁设备。 |
| DEVICE_INTELLIGENT_LOCK | 0x001001 | 智能锁。 |
| DEVICE_SMART_KEY | 0x001002 | 智键设备。 |
| DEVICE_VEHICLE_KEY | 0x001003 | 车钥匙。 起始版本： 5.1.0(18) |
| DEVICE_VEHICLE_LOCK | 0x001004 | 车锁。 起始版本： 5.1.0(18) |

**AcbState**

表示和远端设备的逻辑链路连接状态，为枚举值。

系统能力： SystemCapability.Communication.NearLink.Core

起始版本： 5.1.0(18)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISCONNECTED | 0 | 表示已断连。 |
| CONNECTED | 1 | 表示已连接。 |
| ENCRYPTED | 2 | 表示已加密。 |