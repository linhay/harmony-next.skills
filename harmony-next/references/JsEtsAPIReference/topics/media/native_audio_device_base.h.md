# native_audio_device_base.h

**概述**

定义音频设备参数的类型以及获取每个设备参数的接口。

库： libohaudio.so

引用文件： <ohaudio/native_audio_device_base.h>

系统能力： SystemCapability.Multimedia.Audio.Core

起始版本： 12

相关模块： [OHAudio](OHAudio.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioDeviceDescriptorArray | OH_AudioDeviceDescriptorArray | 声明音频设备描述符数组。 |
| OH_AudioDeviceDescriptor | OH_AudioDeviceDescriptor | 声明音频设备描述符。该实例用于获取更多音频设备详细信息属性。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioDevice_ChangeType | OH_AudioDevice_ChangeType | 定义音频设备更改类型。 |
| OH_AudioDevice_Role | OH_AudioDevice_Role | 定义音频设备角色。 |
| OH_AudioDevice_Type | OH_AudioDevice_Type | 定义音频设备类型。 |
| OH_AudioDevice_Flag | OH_AudioDevice_Flag | 定义音频设备标志。 |
| OH_AudioDevice_Usage | OH_AudioDevice_Usage | 定义可获取的设备种类。 |
| OH_AudioDevice_BlockStatus | OH_AudioDevice_BlockStatus | 声明音频设备的堵塞状态。默认情况下，音频设备被视为未堵塞。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceRole(OH_AudioDeviceDescriptor *audioDeviceDescriptor, OH_AudioDevice_Role *deviceRole) | 查询目标音频设备描述符的设备角色。 |
| OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceType(OH_AudioDeviceDescriptor *audioDeviceDescriptor, OH_AudioDevice_Type *deviceType) | 查询目标音频设备描述符的设备类型。 |
| OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceId(OH_AudioDeviceDescriptor *audioDeviceDescriptor, uint32_t *id) | 查询目标音频设备描述符的设备id。 |
| OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceName(OH_AudioDeviceDescriptor *audioDeviceDescriptor, char **name) | 查询目标音频设备描述符的设备名称。 |
| OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceAddress(OH_AudioDeviceDescriptor *audioDeviceDescriptor, char **address) | 查询目标音频设备描述符的设备地址。 |
| OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceSampleRates(OH_AudioDeviceDescriptor *audioDeviceDescriptor, uint32_t **sampleRates, uint32_t *size) | 查询目标音频设备描述符的采样率数组。 |
| OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceChannelCounts(OH_AudioDeviceDescriptor *audioDeviceDescriptor, uint32_t **channelCounts, uint32_t *size) | 查询目标音频设备描述符的设备通道计数数组。 |
| OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceDisplayName(OH_AudioDeviceDescriptor *audioDeviceDescriptor, char **displayName) | 查询目标音频设备描述符的显示名称。 |
| OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceEncodingTypes(OH_AudioDeviceDescriptor *audioDeviceDescriptor, OH_AudioStream_EncodingType **encodingTypes, uint32_t *size) | 查询目标音频设备描述符的编码类型数组。 |

**枚举类型说明**

**OH_AudioDevice_ChangeType**

```ets
enum OH_AudioDevice_ChangeType
```

描述

定义音频设备更改类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO_DEVICE_CHANGE_TYPE_CONNECT = 0 | 设备连接。 |
| AUDIO_DEVICE_CHANGE_TYPE_DISCONNECT = 1 | 设备断开。 |

**OH_AudioDevice_Role**

```ets
enum OH_AudioDevice_Role
```

描述

定义音频设备角色。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO_DEVICE_ROLE_INPUT = 1 | 输入设备。 |
| AUDIO_DEVICE_ROLE_OUTPUT = 2 | 输出设备。 |

**OH_AudioDevice_Type**

```ets
enum OH_AudioDevice_Type
```

描述

定义音频设备类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO_DEVICE_TYPE_INVALID = 0 | 无效设备。 |
| AUDIO_DEVICE_TYPE_EARPIECE = 1 | 内置听筒。 |
| AUDIO_DEVICE_TYPE_SPEAKER = 2 | 内置扬声器。 |
| AUDIO_DEVICE_TYPE_WIRED_HEADSET = 3 | 带话筒的耳机。 |
| AUDIO_DEVICE_TYPE_WIRED_HEADPHONES = 4 | 无话筒的耳机。 |
| AUDIO_DEVICE_TYPE_BLUETOOTH_SCO = 7 | 使用面向同步连接链路（SCO）的蓝牙设备。 |
| AUDIO_DEVICE_TYPE_BLUETOOTH_A2DP = 8 | 使用高级音频分布模式（A2DP）的蓝牙设备。 |
| AUDIO_DEVICE_TYPE_MIC = 15 | 内置麦克风。 |
| AUDIO_DEVICE_TYPE_USB_HEADSET = 22 | USB音频耳机。 |
| AUDIO_DEVICE_TYPE_DISPLAY_PORT = 23 | 显示端口（DisplayPort）设备。 |
| AUDIO_DEVICE_TYPE_REMOTE_CAST = 24 | 音频被系统应用投送到其他远程的设备。 |
| AUDIO_DEVICE_TYPE_USB_DEVICE = 25 | USB设备（不包含USB耳机）。 起始版本： 18 |
| AUDIO_DEVICE_TYPE_ACCESSORY = 26 | 附件设备，如遥控器上的麦克风。 起始版本： 19 |
| AUDIO_DEVICE_TYPE_HDMI = 27 | HDMI设备（例如HDMI、ARC、eARC等）。 起始版本： 19 |
| AUDIO_DEVICE_TYPE_LINE_DIGITAL = 28 | 有线数字设备（例如S/PDIF等）。 起始版本： 19 |
| AUDIO_DEVICE_TYPE_HEARING_AID = 30 | 助听器设备。 起始版本： 20 |
| AUDIO_DEVICE_TYPE_NEARLINK = 31 | 星闪设备。 起始版本： 20 |
| AUDIO_DEVICE_TYPE_DEFAULT = 1000 | 默认设备类型。 |

**OH_AudioDevice_Flag**

```ets
enum OH_AudioDevice_Flag
```

描述

定义音频设备标志。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO_DEVICE_FLAG_NONE = 0 | 无设备。 |
| AUDIO_DEVICE_FLAG_OUTPUT = 1 | 输出设备。 |
| AUDIO_DEVICE_FLAG_INPUT = 2 | 输入设备。 |
| AUDIO_DEVICE_FLAG_ALL = 3 | 所有设备。 |

**OH_AudioDevice_Usage**

```ets
enum OH_AudioDevice_Usage
```

描述

定义可获取的设备种类。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO_DEVICE_USAGE_MEDIA_OUTPUT = 1 | 媒体输出设备。 |
| AUDIO_DEVICE_USAGE_MEDIA_INPUT = 2 | 媒体输入设备。 |
| AUDIO_DEVICE_USAGE_MEDIA_ALL = 3 | 所有媒体设备。 |
| AUDIO_DEVICE_USAGE_CALL_OUTPUT = 4 | 通话输出设备。 |
| AUDIO_DEVICE_USAGE_CALL_INPUT = 8 | 通话输入设备。 |
| AUDIO_DEVICE_USAGE_CALL_ALL = 12 | 所有通话设备。 |

**OH_AudioDevice_BlockStatus**

```ets
enum OH_AudioDevice_BlockStatus
```

描述

声明音频设备的堵塞状态。默认情况下，音频设备被视为未堵塞。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| AUDIO_DEVICE_UNBLOCKED = 0 | 音频设备未被堵塞。 |
| AUDIO_DEVICE_BLOCKED = 1 | 音频设备被堵塞。 |

**函数说明**

**OH_AudioDeviceDescriptor_GetDeviceRole()**

```ets
OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceRole(OH_AudioDeviceDescriptor *audioDeviceDescriptor,OH_AudioDevice_Role *deviceRole)
```

描述

查询目标音频设备描述符的设备角色。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioDeviceDescriptor *audioDeviceDescriptor | 音频设备描述符。通过 OH_AudioRoutingManager_GetDevices 或者OH_AudioRoutingManager_OnDeviceChangedCallback获取。 |
| OH_AudioDevice_Role *deviceRole | 设备角色指针。将设置设备角色值的变量，指向OH_AudioDevice_Role。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS或AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM。 |

**OH_AudioDeviceDescriptor_GetDeviceType()**

```ets
OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceType(OH_AudioDeviceDescriptor *audioDeviceDescriptor,OH_AudioDevice_Type *deviceType)
```

描述

查询目标音频设备描述符的设备类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioDeviceDescriptor *audioDeviceDescriptor | 音频设备描述符。通过 OH_AudioRoutingManager_GetDevices 或者OH_AudioRoutingManager_OnDeviceChangedCallback获取。 |
| OH_AudioDevice_Type *deviceType | 设备类型指针。将设置设备类型值的变量，指向OH_AudioDevice_Type。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS或AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM。 |

**OH_AudioDeviceDescriptor_GetDeviceId()**

```ets
OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceId(OH_AudioDeviceDescriptor *audioDeviceDescriptor,uint32_t *id)
```

描述

查询目标音频设备描述符的设备id。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioDeviceDescriptor *audioDeviceDescriptor | 音频设备描述符。通过 OH_AudioRoutingManager_GetDevices 或者OH_AudioRoutingManager_OnDeviceChangedCallback获取。 |
| uint32_t *id | 设备id指针，将设置设备角色值的变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS 或 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM。 |

**OH_AudioDeviceDescriptor_GetDeviceName()**

```ets
OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceName(OH_AudioDeviceDescriptor *audioDeviceDescriptor,char **name)
```

描述

查询目标音频设备描述符的设备名称。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioDeviceDescriptor *audioDeviceDescriptor | 音频设备描述符。通过 OH_AudioRoutingManager_GetDevices 或者OH_AudioRoutingManager_OnDeviceChangedCallback获取。 |
| char **name | 设备名称指针，将设置设备名称值的变量。 不要单独释放音频设备名称指针，而是调用OH_AudioRoutingManager_ReleaseDevices，以便在不再使用时释放所有DeviceDescriptor数组。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS或AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM。 |

**OH_AudioDeviceDescriptor_GetDeviceAddress()**

```ets
OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceAddress(OH_AudioDeviceDescriptor *audioDeviceDescriptor,char **address)
```

描述

查询目标音频设备描述符的设备地址。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioDeviceDescriptor *audioDeviceDescriptor | 音频设备描述符。通过 OH_AudioRoutingManager_GetDevices 或者OH_AudioRoutingManager_OnDeviceChangedCallback获取。 |
| char **address | 设备MAC地址指针，将设置设备MAC地址值的变量。 不要单独释放音频设备MAC地址指针，而是调用OH_AudioRoutingManager_ReleaseDevices，以便在不再使用时释放所有DeviceDescriptor数组。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS或AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM。 |

**OH_AudioDeviceDescriptor_GetDeviceSampleRates()**

```ets
OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceSampleRates(OH_AudioDeviceDescriptor *audioDeviceDescriptor,uint32_t **sampleRates, uint32_t *size)
```

描述

查询目标音频设备描述符的采样率数组。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioDeviceDescriptor *audioDeviceDescriptor | 音频设备描述符。通过 OH_AudioRoutingManager_GetDevices 或者OH_AudioRoutingManager_OnDeviceChangedCallback获取。 |
| uint32_t **sampleRates | 设置采样率数组值的数组指针变量。 不要单独释放音频设备采样率指针，而是调用OH_AudioRoutingManager_ReleaseDevices，以便在不再使用时释放所有DeviceDescriptor数组。 |
| uint32_t *size | 设置采样率大小值的指针变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS或AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM。 |

**OH_AudioDeviceDescriptor_GetDeviceChannelCounts()**

```ets
OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceChannelCounts(OH_AudioDeviceDescriptor *audioDeviceDescriptor,uint32_t **channelCounts, uint32_t *size)
```

描述

查询目标音频设备描述符的设备通道计数数组。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioDeviceDescriptor *audioDeviceDescriptor | 音频设备描述符。通过 OH_AudioRoutingManager_GetDevices 或者OH_AudioRoutingManager_OnDeviceChangedCallback获取。 |
| uint32_t **channelCounts | 数组指针变量，该变量将设置通道计数数组值。 不要单独释放音频设备通道数指针，而是调用OH_AudioRoutingManager_ReleaseDevices，以便在不再使用时释放所有DeviceDescriptor数组。 |
| uint32_t *size | 设置通道计数大小值的指针变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS或AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM。 |

**OH_AudioDeviceDescriptor_GetDeviceDisplayName()**

```ets
OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceDisplayName(OH_AudioDeviceDescriptor *audioDeviceDescriptor,char **displayName)
```

描述

查询目标音频设备描述符的显示名称。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioDeviceDescriptor *audioDeviceDescriptor | 音频设备描述符。通过 OH_AudioRoutingManager_GetDevices 或者OH_AudioRoutingManager_OnDeviceChangedCallback获取。 |
| char **displayName | 设置显示名称值的指针变量。 不要单独释放音频设备显示名称指针，而是调用OH_AudioRoutingManager_ReleaseDevices，以便在不再使用时释放所有DeviceDescriptor数组。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS或AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM。 |

**OH_AudioDeviceDescriptor_GetDeviceEncodingTypes()**

```ets
OH_AudioCommon_Result OH_AudioDeviceDescriptor_GetDeviceEncodingTypes(OH_AudioDeviceDescriptor *audioDeviceDescriptor,OH_AudioStream_EncodingType **encodingTypes, uint32_t *size)
```

描述

查询目标音频设备描述符的编码类型数组。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_AudioDeviceDescriptor *audioDeviceDescriptor | 音频设备描述符。通过 OH_AudioRoutingManager_GetDevices 或者OH_AudioRoutingManager_OnDeviceChangedCallback获取。 |
| OH_AudioStream_EncodingType **encodingTypes | 音频设备编码类型，指向OH_AudioStream_EncodingType。 不要单独释放音频设备编码类型指针，而是调用OH_AudioRoutingManager_ReleaseDevices，以便在不再使用时释放所有DeviceDescriptor数组。 |
| uint32_t *size | 设置编码类型大小值的指针变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_AudioCommon_Result | AUDIOCOMMON_RESULT_SUCCESS或AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM。 |