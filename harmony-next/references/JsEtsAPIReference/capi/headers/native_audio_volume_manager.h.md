# native_audio_volume_manager.h

#### 概述

声明音频音量管理器接口。

 该文件接口用于创建AudioVolumeManager。

**引用文件：** <ohaudio/native_audio_volume_manager.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

**相关模块：**[OHAudio](../../topics/media/OHAudio.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md)OH_AudioVolumeManager声明音频音量管理器。音频音量管理器提供多种函数，供开发人员获取系统音量信息。

#### 函数

名称typedef关键字描述[typedef void (*OH_AudioVolumeManager_OnStreamVolumeChangeCallback)(void *userData, OH_AudioStream_Usage usage, int32_t volumeLevel, bool updateUi)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_onstreamvolumechangecallback)OH_AudioVolumeManager_OnStreamVolumeChangeCallback音量变化回调函数的原型定义，用于传递给[OH_AudioVolumeManager_RegisterStreamVolumeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_registerstreamvolumechangecallback)。[typedef void (*OH_AudioVolumeManager_OnRingerModeChangeCallback)(void *userData, OH_AudioRingerMode ringerMode)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_onringermodechangecallback)OH_AudioVolumeManager_OnRingerModeChangeCallback铃声模式变化回调函数的原型定义，用于传递给[OH_AudioVolumeManager_RegisterRingerModeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_registerringermodechangecallback)。[OH_AudioCommon_Result OH_AudioManager_GetAudioVolumeManager(OH_AudioVolumeManager **volumeManager)](#ZH-CN_TOPIC_0000002529285703__oh_audiomanager_getaudiovolumemanager)-使用音量管理器相关功能，首先需要获取音量管理器实例。[OH_AudioCommon_Result OH_AudioVolumeManager_GetMaxVolumeByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, int32_t *maxVolumeLevel)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_getmaxvolumebyusage)-获取指定用途类型音频流的最大音量等级。[OH_AudioCommon_Result OH_AudioVolumeManager_GetMinVolumeByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, int32_t *minVolumeLevel)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_getminvolumebyusage)-获取指定用途类型音频流的最小音量等级。[OH_AudioCommon_Result OH_AudioVolumeManager_GetVolumeByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, int32_t *volumeLevel)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_getvolumebyusage)-获取指定用途类型音频流的系统音量等级。[OH_AudioCommon_Result OH_AudioVolumeManager_IsMuteByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, bool *muted)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_ismutebyusage)-检查指定用途类型的音频流是否处于静音状态。[OH_AudioCommon_Result OH_AudioVolumeManager_RegisterStreamVolumeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, OH_AudioVolumeManager_OnStreamVolumeChangeCallback callback, void *userData)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_registerstreamvolumechangecallback)-注册音频流音量修改回调函数。[OH_AudioCommon_Result OH_AudioVolumeManager_UnregisterStreamVolumeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioVolumeManager_OnStreamVolumeChangeCallback callback)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_unregisterstreamvolumechangecallback)-取消注册音频流音量修改回调函数。[OH_AudioCommon_Result OH_AudioVolumeManager_GetRingerMode(OH_AudioVolumeManager *volumeManager, OH_AudioRingerMode *ringerMode)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_getringermode)-获取当前铃声模式。[OH_AudioCommon_Result OH_AudioVolumeManager_RegisterRingerModeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioVolumeManager_OnRingerModeChangeCallback callback, void *userData)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_registerringermodechangecallback)-注册铃声模式切换回调函数。[OH_AudioCommon_Result OH_AudioVolumeManager_UnregisterRingerModeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioVolumeManager_OnRingerModeChangeCallback callback)](#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_unregisterringermodechangecallback)-取消注册铃声模式切换回调函数。

#### 函数说明

#### OH_AudioVolumeManager_OnStreamVolumeChangeCallback()

```ets
typedef void (*OH_AudioVolumeManager_OnStreamVolumeChangeCallback)(void *userData, OH_AudioStream_Usage usage, int32_t volumeLevel, bool updateUi)
```

**描述**

音量变化回调函数的原型定义，用于传递给[OH_AudioVolumeManager_RegisterStreamVolumeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_registerstreamvolumechangecallback)。

**起始版本：** 20

**参数：**

参数项描述void *userData用户自定义数据指针。[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage) usage对应音量被调整的流的用途类型。int32_t volumeLevel修改后的音量。bool updateUi是否在UI界面显示音量变化。true表示显示，false表示不显示。

#### OH_AudioVolumeManager_OnRingerModeChangeCallback()

```ets
typedef void (*OH_AudioVolumeManager_OnRingerModeChangeCallback)(void *userData, OH_AudioRingerMode ringerMode)
```

**描述**

铃声模式变化回调函数的原型定义，用于传递给[OH_AudioVolumeManager_RegisterRingerModeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_registerringermodechangecallback)。

**起始版本：** 20

**参数：**

参数项描述void *userData用户自定义数据指针。[OH_AudioRingerMode](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audioringermode) ringerMode切换后的铃声模式。

#### OH_AudioManager_GetAudioVolumeManager()

```ets
OH_AudioCommon_Result OH_AudioManager_GetAudioVolumeManager(OH_AudioVolumeManager **volumeManager)
```

**描述**

使用音量管理器相关功能，首先需要获取音量管理器实例。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md) **volumeManager指向OH_AudioVolumeManager用于接收创建的音量管理器实例。

**返回：**

类型说明[OH_AudioCommon_Result](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)

AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。

 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数volumeManager为nullptr。

#### OH_AudioVolumeManager_GetMaxVolumeByUsage()

```ets
OH_AudioCommon_Result OH_AudioVolumeManager_GetMaxVolumeByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, int32_t *maxVolumeLevel)
```

**描述**

获取指定用途类型音频流的最大音量等级。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md) *volumeManager指向OH_AudioVolumeManager用于接收创建的音量管理器实例。[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage) usage用于映射特定音量类型的音频流用途类型。int32_t *maxVolumeLevel用于接收返回的最大音量。

**返回：**

类型说明[OH_AudioCommon_Result](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)

AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。

 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数volumeManager或maxVolumeLevel为nullptr，或usage是无效值。

 AUDIOCOMMON_RESULT_ERROR_SYSTEM：系统处理错误。

#### OH_AudioVolumeManager_GetMinVolumeByUsage()

```ets
OH_AudioCommon_Result OH_AudioVolumeManager_GetMinVolumeByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, int32_t *minVolumeLevel)
```

**描述**

获取指定用途类型音频流的最小音量等级。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md) *volumeManager指向OH_AudioVolumeManager用于接收创建的音量管理器实例。[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage) usage用于映射特定音量类型的音频流用途类型。int32_t *minVolumeLevel用于接收返回的最小音量。

**返回：**

类型说明[OH_AudioCommon_Result](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)

AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。

 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数volumeManager或minVolumeLevel为nullptr，或usage是无效值。

 AUDIOCOMMON_RESULT_ERROR_SYSTEM：系统处理错误。

#### OH_AudioVolumeManager_GetVolumeByUsage()

```ets
OH_AudioCommon_Result OH_AudioVolumeManager_GetVolumeByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, int32_t *volumeLevel)
```

**描述**

获取指定用途类型音频流的系统音量等级。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md) *volumeManager指向OH_AudioVolumeManager用于接收创建的音量管理器实例。[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage) usage用于映射特定音量类型的音频流用途类型。int32_t *volumeLevel用于接收返回的系统音量。

**返回：**

类型说明[OH_AudioCommon_Result](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)

AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。

 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数volumeManager或volumeLevel为nullptr，或usage是无效值。

 AUDIOCOMMON_RESULT_ERROR_SYSTEM：系统处理错误。

#### OH_AudioVolumeManager_IsMuteByUsage()

```ets
OH_AudioCommon_Result OH_AudioVolumeManager_IsMuteByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, bool *muted)
```

**描述**

检查指定用途类型的音频流是否处于静音状态。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md) *volumeManager指向OH_AudioVolumeManager用于接收创建的音量管理器实例。[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage) usage用于映射特定音量类型的音频流用途类型。bool *muted用于接收返回的音频流是否静音。true表示静音，false表示未静音。

**返回：**

类型说明[OH_AudioCommon_Result](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)

AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。

 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数volumeManager或muted为nullptr，或usage是无效值。

 AUDIOCOMMON_RESULT_ERROR_SYSTEM：系统处理错误。

#### OH_AudioVolumeManager_RegisterStreamVolumeChangeCallback()

```ets
OH_AudioCommon_Result OH_AudioVolumeManager_RegisterStreamVolumeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, OH_AudioVolumeManager_OnStreamVolumeChangeCallback callback, void *userData)
```

**描述**

注册音频流音量修改回调函数。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md) *volumeManager指向OH_AudioVolumeManager用于接收创建的音量管理器实例。[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage) usage监听用于映射特定音量类型的音频流用途类型。[OH_AudioVolumeManager_OnStreamVolumeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_onstreamvolumechangecallback) callback监听的音频流音量发生时，将调用此回调函数[OH_AudioVolumeManager_OnStreamVolumeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_onstreamvolumechangecallback)。void *userData用户自定义数据指针。

**返回：**

类型说明[OH_AudioCommon_Result](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)

AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。

 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数volumeManager、usage或callback为nullptr，或usage是无效值。

 AUDIOCOMMON_RESULT_ERROR_SYSTEM：系统处理错误。

#### OH_AudioVolumeManager_UnregisterStreamVolumeChangeCallback()

```ets
OH_AudioCommon_Result OH_AudioVolumeManager_UnregisterStreamVolumeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioVolumeManager_OnStreamVolumeChangeCallback callback)
```

**描述**

取消注册音频流音量修改回调函数。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md) *volumeManager指向OH_AudioVolumeManager用于接收创建的音量管理器实例。[OH_AudioVolumeManager_OnStreamVolumeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_onstreamvolumechangecallback) callback指向[OH_AudioVolumeManager_RegisterStreamVolumeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_registerstreamvolumechangecallback)传入的回调函数，用于取消注册。

**返回：**

类型说明[OH_AudioCommon_Result](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)

AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。

 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数volumeManager或callback为nullptr。

 AUDIOCOMMON_RESULT_ERROR_SYSTEM：系统处理错误。

#### OH_AudioVolumeManager_GetRingerMode()

```ets
OH_AudioCommon_Result OH_AudioVolumeManager_GetRingerMode(OH_AudioVolumeManager *volumeManager, OH_AudioRingerMode *ringerMode)
```

**描述**

获取当前铃声模式。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md) *volumeManager指向OH_AudioVolumeManager用于接收创建的音量管理器实例。[OH_AudioRingerMode](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audioringermode) *ringerMode用于接收返回的铃声模式。

**返回：**

类型说明[OH_AudioCommon_Result](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)

AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。

 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数volumeManager或ringerMode为nullptr。

 AUDIOCOMMON_RESULT_ERROR_SYSTEM：系统处理错误。

#### OH_AudioVolumeManager_RegisterRingerModeChangeCallback()

```ets
OH_AudioCommon_Result OH_AudioVolumeManager_RegisterRingerModeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioVolumeManager_OnRingerModeChangeCallback callback, void *userData)
```

**描述**

注册铃声模式切换回调函数。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md) *volumeManager指向OH_AudioVolumeManager用于接收创建的音量管理器实例。[OH_AudioVolumeManager_OnRingerModeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_onringermodechangecallback) callback监听的铃声模式发生切换时，将调用此回调函数[OH_AudioVolumeManager_OnRingerModeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_onringermodechangecallback)。void *userData用户自定义数据指针。

**返回：**

类型说明[OH_AudioCommon_Result](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)

AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。

 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数volumeManager或callback为nullptr。

 AUDIOCOMMON_RESULT_ERROR_SYSTEM：系统处理错误。

#### OH_AudioVolumeManager_UnregisterRingerModeChangeCallback()

```ets
OH_AudioCommon_Result OH_AudioVolumeManager_UnregisterRingerModeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioVolumeManager_OnRingerModeChangeCallback callback)
```

**描述**

取消注册铃声模式切换回调函数。

**起始版本：** 20

**参数：**

参数项描述[OH_AudioVolumeManager](../../topics/media/OH_AudioVolumeManager.md) *volumeManager指向OH_AudioVolumeManager用于接收创建的音量管理器实例。[OH_AudioVolumeManager_OnRingerModeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_onringermodechangecallback) callback指向[OH_AudioVolumeManager_RegisterRingerModeChangeCallback](native_audio_volume_manager.h.md#ZH-CN_TOPIC_0000002529285703__oh_audiovolumemanager_registerringermodechangecallback)传入的回调函数，用于取消注册。

**返回：**

类型说明[OH_AudioCommon_Result](native_audio_common.h.md#ZH-CN_TOPIC_0000002497605712__oh_audiocommon_result)

AUDIOCOMMON_RESULT_SUCCESS：函数执行成功。

 AUDIOCOMMON_RESULT_ERROR_INVALID_PARAM：参数volumeManager或callback为nullptr。

 AUDIOCOMMON_RESULT_ERROR_SYSTEM：系统处理错误。