# avplayer.h

#### 概述

定义avplayer接口。使用AVPlayer提供的Native API播放媒体源。

**引用文件：** <multimedia/player_framework/avplayer.h>

**库：** libavplayer.so

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**相关模块：**[AVPlayer](../../topics/misc/AVPlayer.md)

**相关示例：**[AVPlayerNDKVideo](https://gitcode.com/HarmonyOS/applications_app_samples/tree/master/code/DocsSample/Media/AVPlayer/AVPlayerNDK)

#### 汇总

#### 结构体

名称typedef关键字描述[MediaKeySession](../../topics/media/MediaKeySession.md)MediaKeySessionMediaKeySession类型。[DRM_MediaKeySystemInfo](../../topics/system-services/DRM_MediaKeySystemInfo.md)DRM_MediaKeySystemInfoDRM_MediaKeySystemInfo类型。

#### 函数

名称typedef关键字描述[typedef void (*Player_MediaKeySystemInfoCallback)(OH_AVPlayer player, DRM_MediaKeySystemInfo mediaKeySystemInfo)](#ZH-CN_TOPIC_0000002497445934__player_mediakeysysteminfocallback)Player_MediaKeySystemInfoCallback播放器DRM信息更新时调用。[OH_AVPlayer *OH_AVPlayer_Create(void)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_create)-

创建播放器。

 推荐单个应用创建的音视频播放器实例（即音频、视频、音视频三类相加）不超过16个。

[OH_AVErrCode OH_AVPlayer_SetURLSource(OH_AVPlayer *player, const char *url)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_seturlsource)-设置播放器的播放源。对应的源可以是http url。[OH_AVErrCode OH_AVPlayer_SetFDSource(OH_AVPlayer *player, int32_t fd, int64_t offset, int64_t size)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setfdsource)-设置播放器的媒体文件描述符来源。[OH_AVErrCode OH_AVPlayer_SetDataSource(OH_AVPlayer player, OH_AVDataSourceExt datasrc, void* userData)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setdatasource)-设置播放器的媒体源，该媒体源的数据由应用程序提供。[OH_AVErrCode OH_AVPlayer_Prepare(OH_AVPlayer *player)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_prepare)-

准备播放环境，异步缓存媒体数据。

 此函数必须在SetSource之后调用。

[OH_AVErrCode OH_AVPlayer_Play(OH_AVPlayer *player)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_play)-

开始播放。

 此函数必须在[OH_AVPlayer_Prepare](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_prepare)之后调用。

 如果播放器状态为<Prepared>，调用此函数开始播放。

[OH_AVErrCode OH_AVPlayer_Pause(OH_AVPlayer *player)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_pause)-暂停播放。[OH_AVErrCode OH_AVPlayer_Stop(OH_AVPlayer *player)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_stop)-停止播放。[OH_AVErrCode OH_AVPlayer_Reset(OH_AVPlayer *player)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_reset)-

将播放器恢复到初始状态。

 函数调用完成后，调用SetSource添加播放源。调用[OH_AVPlayer_Prepare](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_prepare)后，再调用[OH_AVPlayer_Play](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_play)重新开始播放。

[OH_AVErrCode OH_AVPlayer_Release(OH_AVPlayer *player)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_release)-

异步释放播放器资源。

 异步释放可以提升性能，但不能确保播放画面的SurfaceBuffer已释放。调用者需要确保播放画面窗口的生命周期安全。

[OH_AVErrCode OH_AVPlayer_ReleaseSync(OH_AVPlayer *player)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_releasesync)-

同步释放播放器资源。

 同步过程保证了播放画面的SurfaceBuffer释放，但该过程耗时较长，建议调用者自行设计异步机制。

[OH_AVErrCode OH_AVPlayer_SetVolume(OH_AVPlayer *player, float leftVolume, float rightVolume)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setvolume)-

设置播放器的音量。

 可以在播放或暂停的过程中使用。0表示无声音，1为原始值。

[OH_AVErrCode OH_AVPlayer_SetLoudnessGain(OH_AVPlayer *player, float loudnessGain)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setloudnessgain)-

设置播放器的响度。当播放处于prepared/playing/paused/completed/stopped状态时，可调用该接口。

 默认响度增益0.0dB。播放器流的usage参数必须是[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage).AUDIOSTREAM_USAGE_MUSIC，

[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage).AUDIOSTREAM_USAGE_MOVIE，[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage).AUDIOSTREAM_USAGE_AUDIOBOOK 之一。

 音频渲染器的延迟模式必须是[OH_AudioStream_LatencyMode](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_latencymode).AUDIOSTREAM_LATENCY_MODE_NORMAL。

 如果通过高分辨率管道播放，则不支持此操作。

[OH_AVErrCode OH_AVPlayer_Seek(OH_AVPlayer *player, int32_t mSeconds, AVPlayerSeekMode mode)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_seek)-

改变播放位置。

 此函数可以在播放或暂停时使用。

[OH_AVErrCode OH_AVPlayer_GetCurrentTime(OH_AVPlayer *player, int32_t *currentTime)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_getcurrenttime)-获取播放位置，精确到毫秒。[OH_AVErrCode OH_AVPlayer_GetVideoWidth(OH_AVPlayer *player, int32_t *videoWidth)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_getvideowidth)-获取视频宽度。[OH_AVErrCode OH_AVPlayer_GetVideoHeight(OH_AVPlayer *player, int32_t *videoHeight)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_getvideoheight)-获取视频高度。[OH_AVErrCode OH_AVPlayer_SetPlaybackSpeed(OH_AVPlayer *player, AVPlaybackSpeed speed)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setplaybackspeed)-根据指定的[AVPlaybackSpeed](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__avplaybackspeed)，设置播放器的播放速率。[OH_AVErrCode OH_AVPlayer_SetPlaybackRate(OH_AVPlayer *player, float rate)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setplaybackrate)-

在有效范围内，设置播放器的播放速率。

 支持的状态：已准备/正在播放/已暂停/已完成。

[OH_AVErrCode OH_AVPlayer_GetPlaybackSpeed(OH_AVPlayer *player, AVPlaybackSpeed *speed)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_getplaybackspeed)-获取当前播放器的播放速率。[OH_AVErrCode OH_AVPlayer_SetAudioRendererInfo(OH_AVPlayer *player, OH_AudioStream_Usage streamUsage)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setaudiorendererinfo)-设置player音频流类型。[OH_AVErrCode OH_AVPlayer_SetVolumeMode(OH_AVPlayer *player, OH_AudioStream_VolumeMode volumeMode)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setvolumemode)-设置player音频流音量模式。[OH_AVErrCode OH_AVPlayer_SetAudioInterruptMode(OH_AVPlayer *player, OH_AudioInterrupt_Mode interruptMode)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setaudiointerruptmode)-设置player音频流的打断模式。[OH_AVErrCode OH_AVPlayer_SetAudioEffectMode(OH_AVPlayer *player, OH_AudioStream_AudioEffectMode effectMode)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setaudioeffectmode)-设置player音频流的音效模式。[OH_AVErrCode OH_AVPlayer_SelectBitRate(OH_AVPlayer *player, uint32_t bitRate)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_selectbitrate)-

设置hls播放器使用的码率。仅对HLS协议网络流有效。

 默认情况下，播放器会根据网络连接情况选择合适的码率和速度。

 通过INFO_TYPE_BITRATE_COLLECT上报有效码率链表，设置并选择指定的码率，选择小于且最接近的码率。准备好后，读取以查询当前选择的比特率。

[OH_AVErrCode OH_AVPlayer_SetVideoSurface(OH_AVPlayer *player, OHNativeWindow *window)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setvideosurface)-

设置播放画面窗口。

 此函数必须在SetSource之后，Prepare之前调用。

[OH_AVErrCode OH_AVPlayer_GetDuration(OH_AVPlayer *player, int32_t *duration)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_getduration)-获取媒体文件的总时长，精确到毫秒。[OH_AVErrCode OH_AVPlayer_GetState(OH_AVPlayer *player, AVPlayerState *state)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_getstate)-获取当前播放状态。[bool OH_AVPlayer_IsPlaying(OH_AVPlayer *player)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_isplaying)-判断播放器是否在播放。[bool OH_AVPlayer_IsLooping(OH_AVPlayer *player)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_islooping)-判断是否循环播放。[OH_AVErrCode OH_AVPlayer_SetLooping(OH_AVPlayer *player, bool loop)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setlooping)-设置循环播放。[OH_AVErrCode OH_AVPlayer_SetPlayerCallback(OH_AVPlayer *player, AVPlayerCallback callback)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setplayercallback)-

设置播放器回调函数。

 由于通过此方法设置的信息监听回调函数[OH_AVPlayerOnInfo](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeroninfo)和错误监听回调函数[OH_AVPlayerOnError](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeronerror)可以传递的信息有限，也不便于应用区分多个播放器实例。

 从API version 12开始，应使用[OH_AVPlayer_SetOnInfoCallback](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setoninfocallback)、[OH_AVPlayer_SetOnErrorCallback](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setonerrorcallback)接口分别设置信息监听回调函数[OH_AVPlayerOnInfoCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeroninfocallback)和错误监听回调函数[OH_AVPlayerOnErrorCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeronerrorcallback)。

[OH_AVErrCode OH_AVPlayer_SelectTrack(OH_AVPlayer *player, int32_t index)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_selecttrack)-

选择音频或字幕轨道。

 默认播放第一个带数据的音轨，不播放字幕轨迹。

 设置生效后，原音轨将失效。请设置字幕处于准备/播放/暂停/完成状态，并将音轨设置为准备状态。

[OH_AVErrCode OH_AVPlayer_DeselectTrack(OH_AVPlayer *player, int32_t index)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_deselecttrack)-取消选择当前音频或字幕轨道。[OH_AVErrCode OH_AVPlayer_GetCurrentTrack(OH_AVPlayer *player, int32_t trackType, int32_t *index)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_getcurrenttrack)-获取当前有效的轨道索引。请将状态设置为准备/正在播放/暂停/完成。[OH_AVErrCode OH_AVPlayer_SetMediaKeySystemInfoCallback(OH_AVPlayer *player, Player_MediaKeySystemInfoCallback callback)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setmediakeysysteminfocallback)-设置播放器媒体密钥系统信息回调的方法。[OH_AVErrCode OH_AVPlayer_GetMediaKeySystemInfo(OH_AVPlayer *player, DRM_MediaKeySystemInfo *mediaKeySystemInfo)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_getmediakeysysteminfo)-获取媒体密钥系统信息以创建媒体密钥会话。[OH_AVErrCode OH_AVPlayer_SetDecryptionConfig(OH_AVPlayer *player, MediaKeySession *mediaKeySession, bool secureVideoPath)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setdecryptionconfig)-设置解密信息。[OH_AVErrCode OH_AVPlayer_SetOnInfoCallback(OH_AVPlayer *player, OH_AVPlayerOnInfoCallback callback, void *userData)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setoninfocallback)-设置播放器消息回调监听函数。[OH_AVErrCode OH_AVPlayer_SetOnErrorCallback(OH_AVPlayer *player, OH_AVPlayerOnErrorCallback callback, void *userData)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setonerrorcallback)-设置播放器错误回调监听函数。[OH_AVFormat *OH_AVPlayer_GetMediaDescription(OH_AVPlayer *player)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_getmediadescription)-

获取播放器媒体源信息。设置完播放资源并且播放处于initialized/prepared/playing/paused/completed/stopped状态，可调用该接口。

 需要注意返回值OH_AVFormat指针对象的生命周期需要用户手动释放。

[OH_AVFormat *OH_AVPlayer_GetTrackDescription(OH_AVPlayer *player, uint32_t index)](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_gettrackdescription)-

通过索引下标获取播放器媒体源轨道信息。设置完播放资源并且播放处于initialized/prepared/playing/paused/completed/stopped状态，可调用该接口。

 需要注意返回值OH_AVFormat指针对象的生命周期需要用户手动释放。

#### 函数说明

#### Player_MediaKeySystemInfoCallback()

```ets
typedef void (*Player_MediaKeySystemInfoCallback)(OH_AVPlayer *player, DRM_MediaKeySystemInfo* mediaKeySystemInfo)
```

**描述**

播放器DRM信息更新时调用。

**起始版本：** 12

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[DRM_MediaKeySystemInfo](../../topics/system-services/DRM_MediaKeySystemInfo.md)* mediaKeySystemInfoDRM信息。

#### OH_AVPlayer_Create()

```ets
OH_AVPlayer *OH_AVPlayer_Create(void)
```

**描述**

创建播放器。

 推荐单个应用创建的音视频播放器实例（即音频、视频、音视频三类相加）不超过16个。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**返回：**

类型说明[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *

如果创建成功返回指向OH_AVPlayer实例的指针，否则返回空指针。

 可能的失败原因：

 1.PlayerFactory::CreatePlayer执行失败。

 2.new PlayerObject执行失败。

#### OH_AVPlayer_SetURLSource()

```ets
OH_AVErrCode OH_AVPlayer_SetURLSource(OH_AVPlayer *player, const char *url)
```

**描述**

设置播放器的播放源。对应的源可以是http url。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。const char *url播放源。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：设置成功。

 AV_ERR_INVALID_VAL：输入player为空指针，url为空或者player SetUrlSource执行失败。

#### OH_AVPlayer_SetFDSource()

```ets
OH_AVErrCode OH_AVPlayer_SetFDSource(OH_AVPlayer *player, int32_t fd, int64_t offset, int64_t size)
```

**描述**

设置播放器的媒体文件描述符来源。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。int32_t fd媒体源的文件描述符。int64_t offset媒体源在文件描述符中的偏移量。int64_t size表示媒体源的大小。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：fd设置成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player SetFdSource执行失败。

#### OH_AVPlayer_SetDataSource()

```ets
OH_AVErrCode OH_AVPlayer_SetDataSource(OH_AVPlayer *player, OH_AVDataSourceExt* datasrc, void* userData)
```

**描述**

设置播放器的媒体源，该媒体源的数据由应用程序提供。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 21

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。OH_AVDataSourceExt* datasrc指向自定义媒体数据的指针。void* userData用户传入的句柄，用于回调中传入。userData若为空，不支持AVPlayer的多实例播放。

**返回：**

类型说明OH_AVErrCode

AV_ERR_OK：设置成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者输入datasrc为空指针。

#### OH_AVPlayer_Prepare()

```ets
OH_AVErrCode OH_AVPlayer_Prepare(OH_AVPlayer *player)
```

**描述**

准备播放环境，异步缓存媒体数据。

 此函数必须在SetSource之后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player Prepare执行失败。

#### OH_AVPlayer_Play()

```ets
OH_AVErrCode OH_AVPlayer_Play(OH_AVPlayer *player)
```

**描述**

开始播放。

 此函数必须在[OH_AVPlayer_Prepare](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_prepare)之后调用。

 如果播放器状态为<Prepared>，调用此函数开始播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player Play执行失败。

#### OH_AVPlayer_Pause()

```ets
OH_AVErrCode OH_AVPlayer_Pause(OH_AVPlayer *player)
```

**描述**

暂停播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player Pause执行失败。

#### OH_AVPlayer_Stop()

```ets
OH_AVErrCode OH_AVPlayer_Stop(OH_AVPlayer *player)
```

**描述**

停止播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player Stop执行失败。

#### OH_AVPlayer_Reset()

```ets
OH_AVErrCode OH_AVPlayer_Reset(OH_AVPlayer *player)
```

**描述**

将播放器恢复到初始状态。

 函数调用完成后，调用SetSource添加播放源。调用[OH_AVPlayer_Prepare](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_prepare)后，再调用[OH_AVPlayer_Play](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_play)重新开始播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player Reset执行失败。

#### OH_AVPlayer_Release()

```ets
OH_AVErrCode OH_AVPlayer_Release(OH_AVPlayer *player)
```

**描述**

异步释放播放器资源。

 异步释放可以提升性能，但不能确保播放画面的SurfaceBuffer已释放。调用者需要确保播放画面窗口的生命周期安全。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player Release执行失败。

#### OH_AVPlayer_ReleaseSync()

```ets
OH_AVErrCode OH_AVPlayer_ReleaseSync(OH_AVPlayer *player)
```

**描述**

同步释放播放器资源。

 同步过程保证了播放画面的SurfaceBuffer释放，但该过程耗时较长，建议调用者自行设计异步机制。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player ReleaseSync执行失败。

#### OH_AVPlayer_SetVolume()

```ets
OH_AVErrCode OH_AVPlayer_SetVolume(OH_AVPlayer *player, float leftVolume, float rightVolume)
```

**描述**

设置播放器的音量。

 可以在播放或暂停的过程中使用。0表示无声音，1为原始值。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。float leftVolume要设置的左声道目标音量。float rightVolume要设置的右声道目标音量。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置音量。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player SetVolume执行失败。

#### OH_AVPlayer_SetLoudnessGain()

```ets
OH_AVErrCode OH_AVPlayer_SetLoudnessGain(OH_AVPlayer *player, float loudnessGain)
```

**描述**

设置播放器的响度。当播放处于prepared/playing/paused/completed/stopped状态时，可调用该接口。

 默认响度增益0.0dB。播放器流的usage参数必须是[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage).AUDIOSTREAM_USAGE_MUSIC，

[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage).AUDIOSTREAM_USAGE_MOVIE，[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage).AUDIOSTREAM_USAGE_AUDIOBOOK 之一。

 音频渲染器的延迟模式必须是[OH_AudioStream_LatencyMode](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_latencymode).AUDIOSTREAM_LATENCY_MODE_NORMAL。

 如果通过高分辨率管道播放，则不支持此操作。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 21

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。float loudnessGain设置播放器的响度值，单位为dB，响度范围为[-90.0, 24.0]。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置响度。

 AV_ERR_INVALID_VAL：输入player为空指针，或者输入的loudnessGain是无效参数。

 AV_ERR_INVALID_STATE：函数在不正常的状态下调用，或者audioRendererInfo的usage参数不是[StreamUsage](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage).STREAM_USAGE_MUSIC，

[StreamUsage](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage).STREAM_USAGE_MOVIE ，[StreamUsage](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage).STREAM_USAGE_AUDIOBOOK 之一。

 AV_ERR_SERVICE_DIED：系统错误。

#### OH_AVPlayer_Seek()

```ets
OH_AVErrCode OH_AVPlayer_Seek(OH_AVPlayer *player, int32_t mSeconds, AVPlayerSeekMode mode)
```

**描述**

改变播放位置。

 此函数可以在播放或暂停时使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。int32_t mSeconds播放目标位置，精确到毫秒。[AVPlayerSeekMode](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__avplayerseekmode) mode播放器的跳转模式。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player Seek执行失败。

#### OH_AVPlayer_GetCurrentTime()

```ets
OH_AVErrCode OH_AVPlayer_GetCurrentTime(OH_AVPlayer *player, int32_t *currentTime)
```

**描述**

获取播放位置，精确到毫秒。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。int32_t *currentTime播放位置。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功获取当前播放位置。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player GetCurrentTime执行失败。

#### OH_AVPlayer_GetVideoWidth()

```ets
OH_AVErrCode OH_AVPlayer_GetVideoWidth(OH_AVPlayer *player, int32_t *videoWidth)
```

**描述**

获取视频宽度。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。int32_t *videoWidth视频宽度。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功获取视频宽度。

 AV_ERR_INVALID_VAL：输入player为空指针。

#### OH_AVPlayer_GetVideoHeight()

```ets
OH_AVErrCode OH_AVPlayer_GetVideoHeight(OH_AVPlayer *player, int32_t *videoHeight)
```

**描述**

获取视频高度。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。int32_t *videoHeight视频高度。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功获取视频高度。

 AV_ERR_INVALID_VAL：输入player为空指针。

#### OH_AVPlayer_SetPlaybackSpeed()

```ets
OH_AVErrCode OH_AVPlayer_SetPlaybackSpeed(OH_AVPlayer *player, AVPlaybackSpeed speed)
```

**描述**

根据指定的[AVPlaybackSpeed](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__avplaybackspeed)，设置播放器的播放速率。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[AVPlaybackSpeed](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__avplaybackspeed) speed速率模式。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置播放速率。

 AV_ERR_INVALID_VAL：输入player为空指针。

#### OH_AVPlayer_SetPlaybackRate()

```ets
OH_AVErrCode OH_AVPlayer_SetPlaybackRate(OH_AVPlayer *player, float rate)
```

**描述**

在有效范围内，设置播放器的播放速率。

 支持的状态：已准备/正在播放/已暂停/已完成。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 20

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。float rate播放速率，有效范围是0.125~4。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置播放速率。

 AV_ERR_OPERATE_NOT_PERMIT：如果在不支持的状态下调用或在直播期间调用。

 AV_ERR_INVALID_VAL：输入player为空指针，或者速率超出范围。

#### OH_AVPlayer_GetPlaybackSpeed()

```ets
OH_AVErrCode OH_AVPlayer_GetPlaybackSpeed(OH_AVPlayer *player, AVPlaybackSpeed *speed)
```

**描述**

获取当前播放器的播放速率。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[AVPlaybackSpeed](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__avplaybackspeed) *speed速率模式。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功获取播放速率。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player GetPlaybackSpeed执行失败。

#### OH_AVPlayer_SetAudioRendererInfo()

```ets
OH_AVErrCode OH_AVPlayer_SetAudioRendererInfo(OH_AVPlayer *player, OH_AudioStream_Usage streamUsage)
```

**描述**

设置player音频流类型。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[OH_AudioStream_Usage](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_usage) streamUsageplayer音频流设置的类型。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置音频流类型。

 AV_ERR_INVALID_VAL：输入player为空指针或者streamUsage值无效。

#### OH_AVPlayer_SetVolumeMode()

```ets
OH_AVErrCode OH_AVPlayer_SetVolumeMode(OH_AVPlayer *player, OH_AudioStream_VolumeMode volumeMode)
```

**描述**

设置player音频流音量模式。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 18

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[OH_AudioStream_VolumeMode](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_volumemode) volumeMode指定音频流音量模式。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置音频流音量模式。

 AV_ERR_INVALID_VAL： 输入player为空指针或者volumeMode值无效。

 AV_ERR_INVALID_STATE：函数在无效状态下调用，应先处于准备状态。

 AV_ERR_SERVICE_DIED：系统错误。

#### OH_AVPlayer_SetAudioInterruptMode()

```ets
OH_AVErrCode OH_AVPlayer_SetAudioInterruptMode(OH_AVPlayer *player, OH_AudioInterrupt_Mode interruptMode)
```

**描述**

设置player音频流的打断模式。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[OH_AudioInterrupt_Mode](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiointerrupt_mode) interruptModeplayer音频流使用的打断模式。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置音频流的打断模式。

 AV_ERR_INVALID_VAL：输入player为空指针，或者interruptMode值无效。

#### OH_AVPlayer_SetAudioEffectMode()

```ets
OH_AVErrCode OH_AVPlayer_SetAudioEffectMode(OH_AVPlayer *player, OH_AudioStream_AudioEffectMode effectMode)
```

**描述**

设置player音频流的音效模式。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[OH_AudioStream_AudioEffectMode](native_audiostream_base.h.md#ZH-CN_TOPIC_0000002529445679__oh_audiostream_audioeffectmode) effectModeplayer音频流使用的音效模式。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置音频流的音效模式。

 AV_ERR_INVALID_VAL：输入player为空指针，或者effectMode值无效。

#### OH_AVPlayer_SelectBitRate()

```ets
OH_AVErrCode OH_AVPlayer_SelectBitRate(OH_AVPlayer *player, uint32_t bitRate)
```

**描述**

设置hls播放器使用的码率。仅对HLS协议网络流有效。

 默认情况下，播放器会根据网络连接情况选择合适的码率和速度。

 通过INFO_TYPE_BITRATE_COLLECT上报有效码率链表，设置并选择指定的码率，选择小于且最接近的码率。准备好后，读取以查询当前选择的比特率。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。uint32_t bitRate码率，单位为bps。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置码率。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player SelectBitRate执行失败。

#### OH_AVPlayer_SetVideoSurface()

```ets
OH_AVErrCode OH_AVPlayer_SetVideoSurface(OH_AVPlayer *player, OHNativeWindow *window)
```

**描述**

设置播放画面窗口。

 此函数必须在SetSource之后，Prepare之前调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。OHNativeWindow *window指向OHNativeWindow实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置播放画面窗口。

 AV_ERR_INVALID_VAL：输入player为空指针，输入window为空指针或者player SetVideoSurface执行失败。

#### OH_AVPlayer_GetDuration()

```ets
OH_AVErrCode OH_AVPlayer_GetDuration(OH_AVPlayer *player, int32_t *duration)
```

**描述**

获取媒体文件的总时长，精确到毫秒。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。int32_t *duration媒体文件的总时长。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功获取媒体文件时长。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player GetDuration执行失败。

#### OH_AVPlayer_GetState()

```ets
OH_AVErrCode OH_AVPlayer_GetState(OH_AVPlayer *player, AVPlayerState *state)
```

**描述**

获取当前播放状态。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[AVPlayerState](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__avplayerstate) *state当前播放状态。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功获取当前播放状态。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player GetState执行失败。

#### OH_AVPlayer_IsPlaying()

```ets
bool OH_AVPlayer_IsPlaying(OH_AVPlayer *player)
```

**描述**

判断播放器是否在播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。

**返回：**

类型说明bool如果正在播放，则返回true；如果不在播放或者输入player为空指针则返回false。

#### OH_AVPlayer_IsLooping()

```ets
bool OH_AVPlayer_IsLooping(OH_AVPlayer *player)
```

**描述**

判断是否循环播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。

**返回：**

类型说明bool如果是循环播放，则返回true；如果不是循环播放或者输入player为空指针则返回false。

#### OH_AVPlayer_SetLooping()

```ets
OH_AVErrCode OH_AVPlayer_SetLooping(OH_AVPlayer *player, bool loop)
```

**描述**

设置循环播放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。bool loop循环播放开关。true表示开启循环播放，false表示关闭循环播放。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置循环播放。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player SetLooping执行失败。

#### OH_AVPlayer_SetPlayerCallback()

```ets
OH_AVErrCode OH_AVPlayer_SetPlayerCallback(OH_AVPlayer *player, AVPlayerCallback callback)
```

**描述**

设置播放器回调函数。

 由于通过此方法设置的信息监听回调函数[OH_AVPlayerOnInfo](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeroninfo)和错误监听回调函数[OH_AVPlayerOnError](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeronerror)可以传递的信息有限，也不便于应用区分多个播放器实例。

 从API version 12开始，应使用[OH_AVPlayer_SetOnInfoCallback](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setoninfocallback)、[OH_AVPlayer_SetOnErrorCallback](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setonerrorcallback)接口分别设置信息监听回调函数[OH_AVPlayerOnInfoCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeroninfocallback)和错误监听回调函数[OH_AVPlayerOnErrorCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeronerrorcallback)。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**废弃版本：** 12

**替代接口：**[OH_AVPlayer_SetOnInfoCallback](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setoninfocallback)、[OH_AVPlayer_SetOnErrorCallback](#ZH-CN_TOPIC_0000002497445934__oh_avplayer_setonerrorcallback)

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[AVPlayerCallback](../../topics/misc/AVPlayerCallback.md) callback回调对象指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功设置播放器回调。

 AV_ERR_INVALID_VAL：输入player为空指针，callback.onInfo或onError为空，或者player SetPlayerCallback执行失败。

#### OH_AVPlayer_SelectTrack()

```ets
OH_AVErrCode OH_AVPlayer_SelectTrack(OH_AVPlayer *player, int32_t index)
```

**描述**

选择音频或字幕轨道。

 默认播放第一个带数据的音轨，不播放字幕轨迹。

 设置生效后，原音轨将失效。请设置字幕处于准备/播放/暂停/完成状态，并将音轨设置为准备状态。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。int32_t index索引。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player SelectTrack执行失败。

#### OH_AVPlayer_DeselectTrack()

```ets
OH_AVErrCode OH_AVPlayer_DeselectTrack(OH_AVPlayer *player, int32_t index)
```

**描述**

取消选择当前音频或字幕轨道。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。int32_t index索引。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player DeselectTrack执行失败。

#### OH_AVPlayer_GetCurrentTrack()

```ets
OH_AVErrCode OH_AVPlayer_GetCurrentTrack(OH_AVPlayer *player, int32_t trackType, int32_t *index)
```

**描述**

获取当前有效的轨道索引。请将状态设置为准备/正在播放/暂停/完成。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 11

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。int32_t trackType媒体类型。0：音频，1：视频。int32_t *index索引。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：成功获取轨道索引。

 AV_ERR_INVALID_VAL：输入player为空指针，或者player GetCurrentTrack执行失败。

#### OH_AVPlayer_SetMediaKeySystemInfoCallback()

```ets
OH_AVErrCode OH_AVPlayer_SetMediaKeySystemInfoCallback(OH_AVPlayer *player, Player_MediaKeySystemInfoCallback callback)
```

**描述**

设置播放器媒体密钥系统信息回调的方法。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[Player_MediaKeySystemInfoCallback](#ZH-CN_TOPIC_0000002497445934__player_mediakeysysteminfocallback) callback对象指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针，callback为空指针，player SetDrmSystemInfoCallback，

 SetDrmSystemInfoCallback或SetDrmSystemInfoCallback执行失败。

#### OH_AVPlayer_GetMediaKeySystemInfo()

```ets
OH_AVErrCode OH_AVPlayer_GetMediaKeySystemInfo(OH_AVPlayer *player, DRM_MediaKeySystemInfo *mediaKeySystemInfo)
```

**描述**

获取媒体密钥系统信息以创建媒体密钥会话。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[DRM_MediaKeySystemInfo](../../topics/system-services/DRM_MediaKeySystemInfo.md) *mediaKeySystemInfo媒体密钥系统信息。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针或者内存不足。

#### OH_AVPlayer_SetDecryptionConfig()

```ets
OH_AVErrCode OH_AVPlayer_SetDecryptionConfig(OH_AVPlayer *player, MediaKeySession *mediaKeySession, bool secureVideoPath)
```

**描述**

设置解密信息。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[MediaKeySession](../../topics/media/MediaKeySession.md) *mediaKeySession具有解密功能的媒体密钥会话实例。bool secureVideoPath是否需要安全解码器。true表示需要安全解码器，false表示不需要安全解码器。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入player为空指针或者player SetDecryptionConfig执行失败。

#### OH_AVPlayer_SetOnInfoCallback()

```ets
OH_AVErrCode OH_AVPlayer_SetOnInfoCallback(OH_AVPlayer *player, OH_AVPlayerOnInfoCallback callback, void *userData)
```

**描述**

设置播放器消息回调监听函数。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[OH_AVPlayerOnInfoCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeroninfocallback) callback执行回调监听函数的指针，空指针表示取消设置播放器消息回调监听。void *userData指向应用调用者设置的实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_NO_MEMORY：内存分配失败。

 AV_ERR_INVALID_VAL： 输入player为空指针或者函数执行失败。

#### OH_AVPlayer_SetOnErrorCallback()

```ets
OH_AVErrCode OH_AVPlayer_SetOnErrorCallback(OH_AVPlayer *player, OH_AVPlayerOnErrorCallback callback, void *userData)
```

**描述**

设置播放器错误回调监听函数。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 12

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。[OH_AVPlayerOnErrorCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeronerrorcallback) callback执行回调监听函数的指针，空指针表示取消设置播放器错误回调监听。void *userData指向应用调用者设置的实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_NO_MEMORY：内存分配失败。

 AV_ERR_INVALID_VAL： 输入player为空指针或者函数执行失败。

#### OH_AVPlayer_GetMediaDescription()

```ets
OH_AVFormat *OH_AVPlayer_GetMediaDescription(OH_AVPlayer *player)
```

**描述**

获取播放器媒体源信息。设置完播放资源并且播放处于initialized/prepared/playing/paused/completed/stopped状态，可调用该接口。

 需要注意返回值OH_AVFormat指针对象的生命周期需要用户手动释放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 22

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。

**返回：**

类型说明[OH_AVFormat](../../topics/misc/OH_AVFormat.md) *

执行成功返回播放器媒体信息，否则返回nullptr。

 可能故障原因：

 1. 传入player指针不合法。

 2. 设置的播放资源不合法。

#### OH_AVPlayer_GetTrackDescription()

```ets
OH_AVFormat *OH_AVPlayer_GetTrackDescription(OH_AVPlayer *player, uint32_t index)
```

**描述**

通过索引下标获取播放器媒体源轨道信息。设置完播放资源并且播放处于initialized/prepared/playing/paused/completed/stopped状态，可调用该接口。

 需要注意返回值OH_AVFormat指针对象的生命周期需要用户手动释放。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 22

**参数：**

参数项描述[OH_AVPlayer](../../topics/misc/OH_AVPlayer.md) *player指向OH_AVPlayer实例的指针。uint32_t index轨道索引下标。

**返回：**

类型说明[OH_AVFormat](../../topics/misc/OH_AVFormat.md) *

执行成功按索引下标返回轨道信息，否则返回nullptr。

 可能故障原因：

 1. 传入player指针不合法。

 2. 设置的播放资源不合法。

 3. 轨道索引下标超出播放源文件数组界限。