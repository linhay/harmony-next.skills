# native_audio_common.h

#### 概述

声明音频公共基础数据结构。

 定义音频接口的公共返回值的类型。

**引用文件：** <ohaudio/native_audio_common.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 12

**相关模块：**[OHAudio](../../topics/media/OHAudio.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_AudioCommon_Result](#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)OH_AudioCommon_Result音频错误码。[OH_AudioScene](#ZH-CN_TOPIC_0000002497605712__oh_audioscene)OH_AudioScene定义音频场景。[OH_AudioRingerMode](#ZH-CN_TOPIC_0000002497605712__oh_audioringermode)OH_AudioRingerMode定义铃音模式。

#### 枚举类型说明

#### OH_AudioCommon_Result

```ets
enum OH_AudioCommon_Result
```

**描述**

音频错误码。

**起始版本：** 12

枚举项描述AUDIOCOMMON_RESULT_SUCCESS = 0操作成功。AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM = 6800101入参错误。AUDIOCOMMON_RESULT_ERROR_NO_MEMORY = 6800102无内存。AUDIOCOMMON_RESULT_ERROR_ILLEGAL_STATE = 6800103非法状态。AUDIOCOMMON_RESULT_ERROR_UNSUPPORTED = 6800104操作不支持。AUDIOCOMMON_RESULT_ERROR_TIMEOUT = 6800105操作超时。AUDIOCOMMON_RESULT_ERROR_STREAM_LIMIT = 6800201达到系统可支持的最大数量。AUDIOCOMMON_RESULT_ERROR_SYSTEM = 6800301系统通用错误。

#### OH_AudioScene

```ets
enum OH_AudioScene
```

**描述**

定义音频场景。

**起始版本：** 12

枚举项描述AUDIO_SCENE_DEFAULT = 0默认音频场景。AUDIO_SCENE_RINGING = 1响铃场景。AUDIO_SCENE_PHONE_CALL = 2电话场景。AUDIO_SCENE_VOICE_CHAT = 3语音聊天场景。

#### OH_AudioRingerMode

```ets
enum OH_AudioRingerMode
```

**描述**

定义铃音模式。

**起始版本：** 20

枚举项描述AUDIO_RINGER_MODE_SILENT = 0静音模式。AUDIO_RINGER_MODE_VIBRATE = 1振动模式。AUDIO_RINGER_MODE_NORMAL = 2响铃模式。