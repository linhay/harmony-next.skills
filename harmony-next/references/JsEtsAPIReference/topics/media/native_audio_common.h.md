# native_audio_common.h

**概述**

声明音频公共基础数据结构。

 定义音频接口的公共返回值的类型。

引用文件： <ohaudio/native_audio_common.h>

库： libohaudio.so

系统能力： SystemCapability.Multimedia.Audio.Core

起始版本： 12

相关模块： [OHAudio](OHAudio.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AudioCommon_Result | OH_AudioCommon_Result | 音频错误码。 |
| OH_AudioScene | OH_AudioScene | 定义音频场景。 |
| OH_AudioRingerMode | OH_AudioRingerMode | 定义铃音模式。 |

**枚举类型说明**

**OH_AudioCommon_Result**

```ets
enum OH_AudioCommon_Result
```

描述

音频错误码。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIOCOMMON_RESULT_SUCCESS = 0 | 操作成功。 |
| AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM = 6800101 | 入参错误。 |
| AUDIOCOMMON_RESULT_ERROR_NO_MEMORY = 6800102 | 无内存。 |
| AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE = 6800103 | 非法状态。 |
| AUDIOCOMMON_RESULT_ERROR_UNSUPPORTED = 6800104 | 操作不支持。 |
| AUDIOCOMMON_RESULT_ERROR_TIMEOUT = 6800105 | 操作超时。 |
| AUDIOCOMMON_RESULT_ERROR_STREAM_LIMIT = 6800201 | 达到系统可支持的最大数量。 |
| AUDIOCOMMON_RESULT_ERROR_SYSTEM = 6800301 | 系统通用错误。 |

**OH_AudioScene**

```ets
enum OH_AudioScene
```

描述

定义音频场景。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO_SCENE_DEFAULT = 0 | 默认音频场景。 |
| AUDIO_SCENE_RINGING = 1 | 响铃场景。 |
| AUDIO_SCENE_PHONE_CALL = 2 | 电话场景。 |
| AUDIO_SCENE_VOICE_CHAT = 3 | 语音聊天场景。 |

**OH_AudioRingerMode**

```ets
enum OH_AudioRingerMode
```

描述

定义铃音模式。

设备行为差异： 当该接口在无振动器件设备中被设置为振动模式时，将不会产生振动效果。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| AUDIO_RINGER_MODE_SILENT = 0 | 静音模式。 |
| AUDIO_RINGER_MODE_VIBRATE = 1 | 振动模式。 |
| AUDIO_RINGER_MODE_NORMAL = 2 | 响铃模式。 |