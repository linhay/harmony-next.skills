# Interface (AVPlayer)

播放管理类，用于管理和播放媒体资源。在调用AVPlayer的方法前，需要先通过[createAVPlayer()](Functions.md#ZH-CN_TOPIC_0000002522082030__mediacreateavplayer9)构建一个AVPlayer实例。

在使用AVPlayer实例的方法时，建议开发者注册相关回调，主动获取当前状态变化。[on('stateChange')](#ZH-CN_TOPIC_0000002553201993__onstatechange9)：监听播放状态机AVPlayerState切换。[on('error')](#ZH-CN_TOPIC_0000002553201993__onerror9)：监听错误事件。

应用需要按照实际业务需求合理使用AVPlayer对象，按需创建并及时释放，避免持有过多AVPlayer实例导致内存消耗过大，否则在一定情况下可能导致系统终止应用。

Audio/Video播放demo可参考：[音频播放开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avplayer-for-playback)、[视频播放开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-playback)。


- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

- 本Interface首批接口从API version 9开始支持。

#### 导入模块

```ets
import { media } from '@kit.MediaKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

![image](public_sys-resources/zh-cn_image_0000002522246110.webp)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| url9+ | string | 否 | 是 | 媒体URL，只允许在idle状态下设置。 支持的视频格式(mp4、mpeg-ts、mkv)。 支持的音频格式(m4a、aac、mp3、ogg、wav、flac、amr、ape)。 支持路径示例： 1. fd类型播放：fd://xx。  2. http网络播放: http://xx。 3. https网络播放: https://xx。 4. hls网络播放路径：http://xx或者https://xx。 说明： - 设置网络播放路径，需声明权限：ohos.permission.INTERNET，相关错误码: [201](../../errors/通用错误码.md)。 - 从API version 11开始不支持webm。 - 将资源句柄（fd）传递给 AVPlayer 实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个 AVPlayer / AVMetadataExtractor / AVImageGenerator / AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致媒体播放器数据获取异常。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| fdSrc9+ | AVFileDescriptor | 否 | 是 | 媒体文件描述，只允许在idle状态下设置。 使用场景：应用中的媒体资源被连续存储在同一个文件中。 支持的视频格式（mp4、mpeg-ts、mkv）。 支持的音频格式（m4a、aac、mp3、ogg、wav、flac、amr、ape）。 使用示例： 假设一个连续存储的媒体文件： 视频1（地址偏移：0，字节长度:100）； 视频2（地址偏移：101，字节长度：50）； 视频3（地址偏移：151，字节长度：150）； 1. 播放视频1：AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; }。 2. 播放视频2：AVFileDescriptor { fd = 资源句柄; offset = 101; length = 50; }。 3. 播放视频3：AVFileDescriptor { fd = 资源句柄; offset = 151; length = 150; }。 假设是一个独立的媒体文件: 请使用src=fd://xx。 说明： 从API version 11开始不支持webm。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| dataSrc10+ | AVDataSrcDescriptor | 否 | 是 | 流式媒体资源描述，只允许在idle状态下设置。 使用场景：应用播放从远端下载到本地的文件，在应用未下载完整音视频资源时，提前播放已获取的资源数据。若将已获取的资源数据写入到本地文件中，同时从本地文件中读取数据，即可实现边播边缓存的能力。 支持的视频格式（mp4、mpeg-ts、mkv）。 支持的音频格式（m4a、aac、mp3、ogg、wav、flac、amr、ape）。 使用示例： 假设用户正在从远端服务器获取音视频媒体文件，希望下载到本地的同时播放已经下载好的部分： 1.用户需要获取媒体文件的总大小size（单位为字节），获取不到时设置为-1。 2.用户需要实现回调函数func用于填写数据，如果size = -1，则func形式为：func(buffer: ArrayBuffer, length: number)，此时播放器只会按照顺序获取数据；否则func形式为：func(buffer: ArrayBuffer, length: number, pos: number)，播放器会按需跳转并获取数据。 3.用户设置AVDataSrcDescriptor {fileSize = size, callback = func}。 注意事项： 如果播放的是mp4/m4a格式用户需要保证moov字段（媒体信息字段）在mdat字段（媒体数据字段）之前，或者moov之前的字段小于10M，否则会导致解析失败无法播放。 说明： 从API version 11开始不支持webm。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| surfaceId9+ | string | 否 | 是 | 视频窗口ID，默认无窗口。 仅支持在initialized状态下初始化。 初始化后可以在prepared/playing/paused/completed/stopped状态下重新设置，重新设置后视频播放将在新的窗口渲染。 使用场景：视频播放时的窗口渲染（纯音频播放时不涉及）。 使用示例： [通过XComponent创建surfaceId](../../topics/components/XComponent.md#ZH-CN_TOPIC_0000002529444889__getxcomponentsurfaceid9)。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| loop9+ | boolean | 否 | 否 | 视频循环播放属性，默认false，设置为true表示循环播放，动态属性。 只允许在prepared/playing/paused/completed状态下设置。 直播场景不支持loop设置。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| videoScaleType9+ | [VideoScaleType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__videoscaletype9) | 否 | 是 | 视频缩放模式，默认VIDEO_SCALE_TYPE_FIT，动态属性。 只允许在prepared/playing/paused/completed状态下设置。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| audioInterruptMode9+ | [audio.InterruptMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__interruptmode9) | 否 | 是 | 音频焦点模型，默认SHARE_MODE，动态属性。 只允许在prepared/playing/paused/completed状态下设置。 在第一次调用play()之前设置， 以便此后中断模式生效。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| audioRendererInfo10+ | audio.AudioRendererInfo | 否 | 是 | 设置音频渲染信息。若媒体源包含视频，则usage默认值为[STREAM_USAGE_MOVIE](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)，否则usage默认值为[STREAM_USAGE_MUSIC](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)。rendererFlags默认值为0。若默认usage不满足需求，则须主动配置audio.AudioRendererInfo。 只允许在initialized状态下设置。 在第一次调用prepare()之前设置，以便音频渲染器信息在之后生效。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| audioEffectMode10+ | [audio.AudioEffectMode](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__audioeffectmode10) | 否 | 是 | 设置音频音效模式，默认值为EFFECT_DEFAULT，动态属性。audioRendererInfo的usage变动时会恢复为默认值，只允许在prepared/playing/paused/completed状态下设置。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| state9+ | [AVPlayerState](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__avplayerstate9) | 是 | 否 | 音视频播放的状态，全状态有效，可查询参数。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| currentTime9+ | number | 是 | 否 | 视频的当前播放位置，单位为毫秒（ms），可查询参数。 返回为(-1)表示无效值，prepared/playing/paused/completed状态下有效。 直播场景默认返回(-1)。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| duration9+ | number | 是 | 否 | 视频时长，单位为毫秒（ms），可查询参数。 返回为(-1)表示无效值，prepared/playing/paused/completed状态下有效。 直播场景默认返回(-1)。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| width9+ | number | 是 | 否 | 视频宽，单位为像素（px），可查询参数。 返回为(0)表示无效值，prepared/playing/paused/completed状态下有效。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| height9+ | number | 是 | 否 | 视频高，单位为像素（px），可查询参数。 返回为(0)表示无效值，prepared/playing/paused/completed状态下有效。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |

#### on('stateChange')9+

on(type: 'stateChange', callback: On[AVPlayerState](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__avplayerstate9)ChangeHandle): void

监听播放状态机[AVPlayerState](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__avplayerstate9)切换的事件。

**元服务API：** 从API version 11 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 状态机切换事件回调类型，支持的事件：'stateChange'，用户操作和系统都会触发此事件。 |
| callback12+ | On[AVPlayerState](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__avplayerstate9)ChangeHandle | 是 | 状态机切换事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
    switch (state) {
      case 'idle':
        console.info('state idle called');
        break;
      case 'initialized':
        console.info('initialized prepared called');
        break;
      case 'prepared':
        console.info('state prepared called');
        break;
      case 'playing':
        console.info('state playing called');
        break;
      case 'paused':
        console.info('state paused called');
        break;
      case 'completed':
        console.info('state completed called');
        break;
      case 'stopped':
        console.info('state stopped called');
        break;
      case 'released':
        console.info('state released called');
        break;
      case 'error':
        console.info('state error called');
        break;
      default:
        console.info('unknown state :' + state);
        break;
    }
  });
}
```

#### off('stateChange')9+

off(type: 'stateChange', callback?: On[AVPlayerState](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__avplayerstate9)ChangeHandle): void

取消监听播放状态机[AVPlayerState](Types.md#ZH-CN_TOPIC_0000002553201997__avplayerstate9)切换的事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 状态机切换事件回调类型，取消注册的事件：'stateChange' |
| callback12+ | On[AVPlayerState](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__avplayerstate9)ChangeHandle | 否 | 状态机切换事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('stateChange');
}
```

#### on('error')9+

on(type: 'error', callback: ErrorCallback): void

监听[AVPlayer](Interface (AVPlayer).md)的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。如果此时[AVPlayerState](Types.md#ZH-CN_TOPIC_0000002553201997__avplayerstate9)也切至error状态，用户需要通过[reset()](#ZH-CN_TOPIC_0000002553201993__reset9)或者[release()](#ZH-CN_TOPIC_0000002553201993__release9)退出播放操作。若调用[reset()](#ZH-CN_TOPIC_0000002553201993__reset9)方法后，播放状态仍为error状态，建议直接调用[release()](#ZH-CN_TOPIC_0000002553201993__release9)方法，退出播放操作。

**元服务API：** 从API version 11 开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，支持的事件：'error'，用户操作和系统都会触发此事件。 |
| callback | ErrorCallback | 是 | 错误事件回调方法，使用播放器的过程中发生错误，会提供错误码ID和错误信息。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

在API version 9-13，针对网络、服务器等数据流异常，接口上报5400103；从API version 14开始，对应错误细化为错误码5411001-5411012。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/通用错误码.md) | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported. |
| 5400101 | No memory. |
| 5400102 | Operation not allowed. |
| 5400104 | Time out. |
| 5400105 | Service died. |
| 5400106 | Unsupported format. |
| 5410002 | Seek continuous unsupported. |
| 5411001 | IO can not find host. |
| 5411002 | IO connection timeout. |
| 5411003 | IO network abnormal. |
| 5411004 | IO network unavailable. |
| 5411005 | IO no permission. |
| 5411006 | IO request denied. |
| 5411007 | IO resource not found. |
| 5411008 | IO SSL client cert needed. |
| 5411009 | IO SSL connect fail. |
| 5411010 | IO SSL server cert untrusted. |
| 5411011 | IO unsupported request. |
| 5411012 | Http cleartext traffic is not permitted. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('error', (error: BusinessError) => {
    console.info('error happened,and error message is :' + error.message);
    console.info('error happened,and error code is :' + error.code);
  });
}
```

#### off('error')9+

off(type: 'error', callback?: ErrorCallback): void

取消监听播放的错误事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 错误事件回调类型，取消注册的事件：'error' |
| callback12+ | ErrorCallback | 否 | 错误事件回调方法，使用播放器的过程中发生错误，会提供错误码ID和错误信息。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('error');
}
```

#### setMediaSource12+

setMediaSource(src:MediaSource, strategy?: PlaybackStrategy): Promise<void>

流媒体预下载资源设置，下载url对应的流媒体数据，并暂存在内存中。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | MediaSource | 是 | 流媒体预下载媒体来源。 |
| strategy | PlaybackStrategy | 否 | 流媒体预下载播放策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
async function test(){
  let player = await media.createAVPlayer();
  let headers: Record<string, string> = {"User-Agent" : "User-Agent-Value"};
  let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://xxx",  headers);
  let playStrategy : media.PlaybackStrategy = {
    preferredWidth: 1,
    preferredHeight: 2,
    preferredBufferDuration: 3,
    preferredHdr: false,
    preferredBufferDurationForPlaying: 1,
    thresholdForAutoQuickPlay: 5
  };
  player.setMediaSource(mediaSource, playStrategy);
}
```

#### setPlaybackStrategy12+

setPlaybackStrategy(strategy: PlaybackStrategy): Promise<void>

设置播放策略，只能在initialized状态下调用。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | PlaybackStrategy | 是 | 播放策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { common } from '@kit.AbilityKit';

let player = await media.createAVPlayer();
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let fileDescriptor = await context.resourceManager.getRawFd('xxx.mp4');
player.fdSrc = fileDescriptor
let playStrategy : media.PlaybackStrategy = {
  preferredWidth: 1,
  preferredHeight: 2,
  preferredBufferDuration: 3,
  preferredHdr: false,
  mutedMediaType: media.MediaType.MEDIA_TYPE_AUD,
  preferredBufferDurationForPlaying: 1,
  thresholdForAutoQuickPlay: 5
};
player.setPlaybackStrategy(playStrategy);
```

#### setPlaybackRange18+

setPlaybackRange(startTimeMs: number, endTimeMs: number, mode?: [SeekMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__seekmode8)) : Promise<void>

设置播放区间，并通过指定的[SeekMode](Enums.md#ZH-CN_TOPIC_0000002522242030__seekmode8)跳转到区间开始位置。设置之后，只播放音视频文件设定区间内的内容。使用Promise异步回调。可在initialized/prepared/paused/stopped/completed状态下使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startTimeMs | number | 是 | 区间开始位置，单位ms，取值[0, duration)。可以设置-1值，系统将会从0位置开始播放。 |
| endTimeMs | number | 是 | 区间结束位置，单位ms，取值(startTimeMs, duration]。可以设置-1值，系统将会播放到资源末尾。 |
| mode | [SeekMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__seekmode8) | 否 | 支持SeekMode.SEEK_PREV_SYNC和SeekMode.SEEK_CLOSEST, 默认值: SeekMode.SEEK_PREV_SYNC。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.setPlaybackRange(0, 6000, media.SeekMode.SEEK_CLOSEST).then(() => {
    console.info('Succeeded setPlaybackRange');
  }).catch((err: BusinessError) => {
    console.error('Failed to setPlaybackRange' + err.message);
  });
}
```

#### prepare9+

prepare(callback: AsyncCallback<void>): void

准备播放音频/视频，需在[stateChange](#ZH-CN_TOPIC_0000002553201993__onstatechange9)事件成功触发至initialized状态后，才能调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 准备播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400106 | Unsupported format. Return by callback. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
  avPlayer.prepare((err: BusinessError) => {
    if (err) {
      console.error('Failed to prepare,error message is :' + err.message);
    } else {
      console.info('Succeeded in preparing');
    }
  });
}
```

#### prepare9+

prepare(): Promise<void>

准备播放音频/视频，需在[stateChange](#ZH-CN_TOPIC_0000002553201993__onstatechange9)事件成功触发至initialized状态后，才能调用。使用Promise异步回调。

如果应用使用到多个短视频频繁切换的场景，为了提升切换性能，可以考虑创建多个AVPlayer对象，提前准备下一个视频，详情参见[在线短视频流畅切换](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-smooth-switching)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5400106 | Unsupported format. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
  avPlayer.prepare().then(() => {
    console.info('Succeeded in preparing');
  }, (err: BusinessError) => {
    console.error('Failed to prepare,error message is :' + err.message);
  });
}
```

#### setMediaMuted12+

setMediaMuted(mediaType: [MediaType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__mediatype8), muted: boolean ): Promise<void>

设置音频静音/取消音频静音。使用Promise异步回调。

从API version 20开始，支持设置关闭视频画面/取消关闭视频画面。

只能在prepared/playing/paused/completed状态下调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaType | [MediaType](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__mediatype8) | 是 | 播放策略。 |
| muted | boolean | 是 | API version 12-19：仅支持设置音频播放策略，表示音频是否静音播放。true为静音播放，false为取消静音播放。 API version 20：增加支持设置视频播放策略，表示视频画面是否关闭。true为关闭画面，false为恢复画面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
  avPlayer.prepare().then(() => {
    console.info('Succeeded in preparing');
    avPlayer.setMediaMuted(media.MediaType.MEDIA_TYPE_AUD, true);
  }, (err: BusinessError) => {
    console.error('Failed to prepare,error message is :' + err.message);
  });
}
```

#### play9+

play(callback: AsyncCallback<void>): void

开始播放音视频资源，只能在prepared/paused/completed状态调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 开始播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/paused/completed状态后才能调用。
  avPlayer.play((err: BusinessError) => {
    if (err) {
      console.error('Failed to play,error message is :' + err.message);
    } else {
      console.info('Succeeded in playing');
    }
  });
}
```

#### play9+

play(): Promise<void>

开始播放音视频资源，只能在prepared/paused/completed状态调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/paused/completed状态后才能调用。
  avPlayer.play().then(() => {
    console.info('Succeeded in playing');
  }, (err: BusinessError) => {
    console.error('Failed to play,error message is :' + err.message);
  });
}
```

#### pause9+

pause(callback: AsyncCallback<void>): void

暂停播放音视频资源，只能在playing状态调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 暂停播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至playing状态后才能调用。
  avPlayer.pause((err: BusinessError) => {
    if (err) {
      console.error('Failed to pause,error message is :' + err.message);
    } else {
      console.info('Succeeded in pausing');
    }
  });
}
```

#### pause9+

pause(): Promise<void>

暂停播放音视频资源，只能在playing状态调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至playing状态后才能调用。
  avPlayer.pause().then(() => {
    console.info('Succeeded in pausing');
  }, (err: BusinessError) => {
    console.error('Failed to pause,error message is :' + err.message);
  });
}
```

#### stop9+

stop(callback: AsyncCallback<void>): void

停止播放音视频资源，只能在prepared/playing/paused/completed状态调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 停止播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
  avPlayer.stop((err: BusinessError) => {
    if (err) {
      console.error('Failed to stop,error message is :' + err.message);
    } else {
      console.info('Succeeded in stopping');
    }
  });
}
```

#### stop9+

stop(): Promise<void>

停止播放音视频资源，只能在prepared/playing/paused/completed状态调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
  avPlayer.stop().then(() => {
    console.info('Succeeded in stopping');
  }, (err: BusinessError) => {
    console.error('Failed to stop,error message is :' + err.message);
  });
}
```

#### reset9+

reset(callback: AsyncCallback<void>): void

重置播放，只能在initialized/prepared/playing/paused/completed/stopped/error状态调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 重置播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized/prepared/playing/paused/completed/stopped/error状态后才能调用。
  avPlayer.reset((err: BusinessError) => {
    if (err) {
      console.error('Failed to reset,error message is :' + err.message);
    } else {
      console.info('Succeeded in resetting');
    }
  });
}
```

#### reset9+

reset(): Promise<void>

重置播放，只能在initialized/prepared/playing/paused/completed/stopped/error状态调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized/prepared/playing/paused/completed/stopped/error状态后才能调用。
  avPlayer.reset().then(() => {
    console.info('Succeeded in resetting');
  }, (err: BusinessError) => {
    console.error('Failed to reset,error message is :' + err.message);
  });
}
```

#### release9+

release(callback: AsyncCallback<void>): void

销毁播放资源，除released状态外，均可以调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 销毁播放的回调方法。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发除released以外的状态才能调用。
  avPlayer.release((err: BusinessError) => {
    if (err) {
      console.error('Failed to release,error message is :' + err.message);
    } else {
      console.info('Succeeded in releasing');
    }
  });
}
```

#### release9+

release(): Promise<void>

销毁播放资源，除released状态，都可以调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发除released以外的状态才能调用。
  avPlayer.release().then(() => {
    console.info('Succeeded in releasing');
  }, (err: BusinessError) => {
    console.error('Failed to release,error message is :' + err.message);
  });
}
```

#### getTrackDescription9+

getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void

获取音视频轨道信息，可以在prepared/playing/paused状态调用。获取所有音视轨道信息，应在数据加载回调后调用。使用callback方式异步获取返回值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<MediaDescription>> | 是 | 回调函数，当获取音视频轨道信息成功，err为undefined，data为获取到的MediaDescription数组；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by callback. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused状态后才能调用。
  avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
    if ((arrList) != null) {
      console.info('Succeeded in doing getTrackDescription');
    } else {
      console.error(`Failed to do getTrackDescription, error:${error}`);
    }
  });
}
```

#### getTrackDescription9+

getTrackDescription(): Promise<Array<MediaDescription>>

获取音视频轨道信息，可以在prepared/playing/paused状态调用。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<MediaDescription>> | Promise对象，返回音视频轨道信息MediaDescription数组。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused状态后才能调用。
  avPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
    console.info('Succeeded in getting TrackDescription');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get TrackDescription, error:${error}`);
  });
}
```

#### getSelectedTracks12+

getSelectedTracks(): Promise<Array<number>>

获取已选择的音视频轨道索引，可以在prepared/playing/paused状态调用。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<number>> | Promise对象，返回已选择音视频轨道索引数组。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused状态后才能调用。
  avPlayer.getSelectedTracks().then((arrList: Array<number>) => {
    console.info('Succeeded in getting SelectedTracks');
  }).catch((error: BusinessError) => {
    console.error(`Failed to get SelectedTracks, error:${error}`);
  });
}
```

#### getPlaybackInfo12+

getPlaybackInfo(): Promise<PlaybackInfo>

获取播放过程信息，可以在prepared/playing/paused状态调用。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PlaybackInfo> | Promise对象，返回播放器信息PlaybackInfo。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer | undefined = undefined;
let playbackInfo: media.PlaybackInfo | undefined = undefined;
media.createAVPlayer(async (err: BusinessError, player: media.AVPlayer) => {
  if (player != null) {
    avPlayer = player;
    console.info(`Succeeded in creating AVPlayer`);
    if (avPlayer) {
      try {
        playbackInfo = await avPlayer.getPlaybackInfo();
        console.info(`AVPlayer getPlaybackInfo = ${JSON.stringify(playbackInfo)}`); // 打印整个PlaybackInfo的值。
      } catch (error) {
        console.error(`error = ${error}`);
      }
  } else {
    console.error(`Failed to create AVPlayer, error message:${err.message}`);
  }
});
```

#### getPlaybackPosition18+

getPlaybackPosition(): number

获取当前播放位置，可以在prepared/playing/paused/completed状态调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前播放位置的时间，单位：毫秒（ms）。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
  avPlayer.prepare().then(() => {
    console.info('Succeeded in preparing');
    let playbackPosition: number = avPlayer.getPlaybackPosition();
    console.info(`AVPlayer getPlaybackPosition== ${playbackPosition}`);
  }, (err: BusinessError) => {
    console.error('Failed to prepare,error message is :' + err.message);
  });
}
```

**getCurrentPresentationTimestamp23+**

getCurrentPresentationTimestamp() : number

获取当前播放位置，可以在播放（playing）/暂停（paused）/完成（completed）状态调用。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

返回值：

| 类型 | 说明 |
| --- | --- |
| number | 返回当前播放位置的时间，单位：微秒（μs）。 |

错误码：

以下错误码的详细介绍请参见[Media错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized状态后才能调用。
  avPlayer.play().then(() => {
    console.info('Succeeded in playing');
    let currentPresentation: number = avPlayer.getCurrentPresentationTimestamp();
    console.info(`AVPlayer getCurrentPresentationTimestamp== ${currentPresentation}`);
  }, (err: BusinessError) => {
    console.error('Failed to prepare,error message is :' + err.message);
  });
}
```

#### selectTrack12+

selectTrack(index: number, mode?: [SwitchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__switchmode12)): Promise<void>

使用AVPlayer播放多音视频轨资源时，选择指定轨道播放，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 多音视频资源的轨道索引，可通过getTrackDescription接口获取当前资源的所有轨道信息MediaDescription。 |
| mode | [SwitchMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__switchmode12) | 否 | 切换视频轨道模式，默认为SMOOTH模式，仅在DASH协议网络流视频轨切换时生效，其他场景当前暂不支持。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

async function  test(){
  let avPlayer: media.AVPlayer = await media.createAVPlayer();
  let audioTrackIndex: Object = 0;
  avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
    if (arrList != null) {
      for (let i = 0; i < arrList.length; i++) {
        if (i != 0) {
          // 获取音频轨道列表。
          audioTrackIndex = arrList[i][media.MediaDescriptionKey.MD_KEY_TRACK_INDEX];
        }
    } else {
      console.error(`Failed to get TrackDescription, error:${error}`);
    }
  });

  // 选择其中一个音频轨道。
  avPlayer.selectTrack(parseInt(audioTrackIndex.toString()));
}
```

#### deselectTrack12+

deselectTrack(index: number): Promise<void>

使用AVPlayer播放多音轨视频时取消指定音视频轨道播放，使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 多音视频资源的轨道索引，来自getTrackDescription接口所获取的轨道信息MediaDescription。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer = await media.createAVPlayer();
let audioTrackIndex: Object = 0;
avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
  if (arrList != null) {
    for (let i = 0; i < arrList.length; i++) {
      if (i != 0) {
        // 获取音频轨道列表。
        audioTrackIndex = arrList[i][media.MediaDescriptionKey.MD_KEY_TRACK_INDEX];
      }
  } else {
    console.error(`Failed to get TrackDescription, error:${error}`);
  }
});

// 选择其中一个音频轨道。
avPlayer.selectTrack(parseInt(audioTrackIndex.toString()));
// 取消选择上次选中的音频轨道，并恢复到默认音频轨道。
avPlayer.deselectTrack(parseInt(audioTrackIndex.toString()));
```

#### setDecryptionConfig11+

setDecryptionConfig(mediaKeySession: drm.MediaKeySession, secureVideoPath: boolean): void

设置解密配置。当收到[mediaKeySystemInfoUpdate事件](#ZH-CN_TOPIC_0000002553201993__onmediakeysysteminfoupdate11)时，需根据事件上报的信息创建相关配置并设置解密配置，否则无法播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mediaKeySession | drm.MediaKeySession | 是 | 解密会话 |
| secureVideoPath | boolean | 是 | 安全视频通路，true表示选择安全视频通路，false表示选择非安全视频通路 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

关于drm模块的示例具体可见[@ohos.multimedia.drm](模块描述.md)。

```ets
import { drm } from '@kit.DrmKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 创建MediaKeySystem系统。
  let keySystem:drm.MediaKeySystem = drm.createMediaKeySystem('com.wiseplay.drm');
  // 创建MediaKeySession解密会话。
  let keySession:drm.MediaKeySession = keySystem.createMediaKeySession(drm.ContentProtectionLevel.CONTENT_PROTECTION_LEVEL_SW_CRYPTO);
  // 生成许可证请求、设置许可证响应等。
  // 安全视频通路标志。
  let secureVideoPath:boolean = false;
  // 设置解密配置。
  avPlayer.setDecryptionConfig(keySession, secureVideoPath);
}
```

#### getMediaKeySystemInfos11+

getMediaKeySystemInfos(): Array<drm.MediaKeySystemInfo>

获取当前播放的媒体资源的MediaKeySystemInfo。需要在[mediaKeySystemInfoUpdate事件](#ZH-CN_TOPIC_0000002553201993__onmediakeysysteminfoupdate11)触发成功后才能调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<drm.MediaKeySystemInfo> | MediaKeySystemInfo数组，MediaKeySystemInfo具有uuid和pssh两个属性。当返回值为undefined时，表示mediaKeySystemInfoUpdate事件未触发。 |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在mediaKeySystemInfoUpdate事件触发成功后才能调用。
  const infos = avPlayer.getMediaKeySystemInfos();
  console.info('GetMediaKeySystemInfos count: ' + infos.length);
  for (let i = 0; i < infos.length; i++) {
    console.info('GetMediaKeySystemInfos uuid: ' + infos[i]["uuid"]);
    console.info('GetMediaKeySystemInfos pssh: ' + infos[i]["pssh"]);
  }
```

#### seek9+

seek(timeMs: number, mode?:[SeekMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__seekmode8)): void

跳转到指定播放位置，只能在prepared/playing/paused/completed状态调用，可以通过[seekDone事件](#ZH-CN_TOPIC_0000002553201993__onseekdone9)确认是否生效。


直播场景不支持seek。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为[0, duration]。 当模式为SEEK_CONTINUOUS时，可以取值-1，表示SEEK_CONTINUOUS模式结束。 |
| mode | [SeekMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__seekmode8) | 否 | 基于视频I帧的跳转模式，默认为SEEK_PREV_SYNC模式，仅在视频资源播放时设置。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  let seekTime: number = 1000;
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
  avPlayer.seek(seekTime, media.SeekMode.SEEK_PREV_SYNC);
}
```

```ets
async function  test(){
  // SEEK_CONTINUOUS 可以结合Slider的onChange回调方法进行对应处理，当slideMode为Moving时，触发拖动过程的SeekContinuous。
  let avPlayer = await media.createAVPlayer();
  let slideMovingTime: number = 2000;
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
  avPlayer.seek(slideMovingTime, media.SeekMode.SEEK_CONTINUOUS);

  // 当slideMode为End时，调用seek(-1, media.SeekMode.SEEK_CONTINUOUS)结束seek。
  avPlayer.seek(-1, media.SeekMode.SEEK_CONTINUOUS);
}
```

#### isSeekContinuousSupported18+

isSeekContinuousSupported() : boolean

查询媒体源是否支持以SEEK_CONTINUOUS模式[SeekMode](Enums.md#ZH-CN_TOPIC_0000002522242030__seekmode8)进行[seek](#ZH-CN_TOPIC_0000002553201993__seek9)，在prepared/playing/paused/completed状态调用返回实际值，其余状态调用返回false。对于不支持SEEK_CONTINUOUS模式进行seek的设备，返回false。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 媒体源是否支持以SEEK_CONTINUOUS模式进行seek。true表示支持，false表示不支持。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
  let isSupported = avPlayer.isSeekContinuousSupported();
}
```

#### on('seekDone')9+

on(type: 'seekDone', callback: Callback<number>): void

监听seek生效的事件。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | seek生效的事件回调类型，支持的事件：'seekDone'，除SEEK_CONTINUOUS外的[SeekMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__seekmode8)每次调用seek后都会回调此事件。 |
| callback | Callback<number> | 是 | 回调函数。seek生效的事件回调方法，只会上报用户请求的time位置。 视频播放：[SeekMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__seekmode8)会造成实际跳转位置与用户设置产生偏差，精准位置需要通过currentTime获取，事件回调的time仅代表完成用户某一次请求。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('seekDone', (seekDoneTime:number) => {
    console.info('seekDone called,and seek time is:' + seekDoneTime);
  });
}
```

#### off('seekDone')9+

off(type: 'seekDone', callback?: Callback<number>): void

取消监听seek生效的事件。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | seek生效的事件回调类型，取消注册的事件：'seekDone'。 |
| callback12+ | Callback<number> | 否 | 回调函数。seek生效的事件回调方法，只会上报用户请求的time位置。 视频播放：[SeekMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__seekmode8)会造成实际跳转位置与用户设置产生偏差，精准位置需要通过currentTime获取，事件回调的time仅代表完成用户某一次请求。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('seekDone');
}
```

#### setSpeed9+

setSpeed(speed: [PlaybackSpeed](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__playbackspeed8)): void

设置倍速模式，只能在prepared/playing/paused/completed状态调用，可以通过[speedDone事件](#ZH-CN_TOPIC_0000002553201993__onspeeddone9)确认是否生效。


直播场景不支持setSpeed。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | [PlaybackSpeed](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__playbackspeed8) | 是 | 指定播放倍速模式。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
  avPlayer.setSpeed(media.PlaybackSpeed.SPEED_FORWARD_2_00_X);
}
```

#### on('speedDone')9+

on(type: 'speedDone', callback: Callback<number>): void

监听setSpeed生效的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setSpeed生效的事件回调类型，支持的事件：'speedDone'，每次调用setSpeed后都会回调此事件。 |
| callback | Callback<number> | 是 | 回调函数。当setSpeed成功，上报生效的倍速模式，具体见[PlaybackSpeed](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__playbackspeed8)。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('speedDone', (speed:number) => {
    console.info('speedDone called,and speed value is:' + speed);
  });
}
```

#### off('speedDone')9+

off(type: 'speedDone', callback?: Callback<number>): void

取消监听setSpeed生效的事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setSpeed生效的事件回调类型，取消注册的事件：'speedDone'。 |
| callback12+ | Callback<number> | 否 | 回调函数。当setSpeed成功，上报生效的倍速模式，具体见[PlaybackSpeed](../enums/Enums.md#ZH-CN_TOPIC_0000002497445922__playbackspeed8)。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('speedDone');
}
```

#### setPlaybackRate20+

setPlaybackRate(rate: number): void

设置倍速模式。只能在prepared/playing/paused/completed状态调用，取值范围是[0.125, 4.0]，可以通过[playbackRateDone](#ZH-CN_TOPIC_0000002553201993__onplaybackratedone20)事件确认是否生效。


直播场景不支持setPlaybackRate。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rate | number | 是 | 指定播放倍速速率，取值范围为[0.125, 4.0]。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400108 | The parameter check failed, parameter value out of range. |
| 5400102 | Operation not allowed，if invalid state or live stream. |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
  avPlayer.setPlaybackRate(2.0);
}
```

**getPlaybackRate23+**

getPlaybackRate(): Promise<number>

获取当前播放器的播放速率。使用Promise异步回调。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回播放倍速速率。 |

示例：

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.getPlaybackRate().then((rate: number) => {
    console.info('Succeeded getPlaybackRate' + rate);
  });
}
```

#### on('playbackRateDone')20+

on(type: 'playbackRateDone', callback: OnPlaybackRateDone): void

监听[setPlaybackRate](#ZH-CN_TOPIC_0000002553201993__setplaybackrate20)生效的事件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setPlaybackRate生效的事件回调类型，支持的事件：'playbackRateDone'，每次调用setPlaybackRate后都会回调此事件。 |
| callback | OnPlaybackRateDone | 是 | setPlaybackRate生效的事件回调方法，上报设置后的播放速率。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('playbackRateDone', (rate:number) => {
    console.info('playbackRateDone called,and rate value is:' + rate);
  });
}
```

#### off('playbackRateDone')20+

off(type: 'playbackRateDone', callback?: OnPlaybackRateDone): void

取消监听[setPlaybackRate](#ZH-CN_TOPIC_0000002553201993__setplaybackrate20)生效的事件。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setPlaybackRate生效的事件回调类型，取消注册的事件：'playbackRateDone'。 |
| callback | OnPlaybackRateDone | 否 | setPlaybackRate生效的事件回调方法，上报设置后的播放速率。如填写该参数，则仅取消注册此回调方法，否则取消注册playbackRateDone事件的所有回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('playbackRateDone');
}
```

#### setBitrate9+

setBitrate(bitrate: number): void

设置比特率，以播放所指定比特率的流媒体资源，当前仅对HLS/DASH协议网络流有效。默认情况下，AVPlayer会根据网络连接速度选择合适的比特率。只能在prepared/playing/paused/completed状态调用，可以通过[bitrateDone](#ZH-CN_TOPIC_0000002553201993__onbitratedone9)事件确认是否生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bitrate | number | 是 | 指定比特率，须通过availableBitrates事件获得当前HLS/DASH协议网络流可用的比特率列表，如果用户指定的比特率不在此列表中，则播放器将从可用比特率列表中选择最接近的比特率。如果通过availableBitrates事件获得的比特率列表长度为0，则不支持指定比特率，也不会产生bitrateDone回调。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  let bitrate: number = 96000;
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
  avPlayer.setBitrate(bitrate);
}
```

#### on('bitrateDone')9+

on(type: 'bitrateDone', callback: Callback<number>): void

监听setBitrate生效的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setBitrate生效的事件回调类型，支持的事件：'bitrateDone'，每次调用setBitrate后都会回调此事件。 |
| callback | Callback<number> | 是 | setBitrate生效的事件回调方法，上报生效的比特率。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('bitrateDone', (bitrate:number) => {
    console.info('bitrateDone called,and bitrate value is:' + bitrate);
  });
}
```

#### off('bitrateDone')9+

off(type: 'bitrateDone', callback?: Callback<number>): void

取消监听setBitrate生效的事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setBitrate生效的事件回调类型，取消注册的事件：'bitrateDone'。 |
| callback12+ | Callback<number> | 否 | setBitrate生效的事件回调方法，上报生效的比特率。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('bitrateDone');
}
```

#### on('availableBitrates')9+

on(type: 'availableBitrates', callback: Callback<Array<number>>): void

监听HLS/DASH协议网络流可用的比特率列表，只会在切换prepared状态后上报。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | HLS/DASH协议网络流可用比特率上报事件回调类型，支持的事件：'availableBitrates'，只会在prepared之后上报一次。 |
| callback | Callback<Array<number>> | 是 | HLS/DASH协议网络流可用比特率上报事件回调方法，使用数组存放支持的比特率。如果数组长度为0，则不支持指定比特率。 |

**示例：**

```ets
async function  test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('availableBitrates', (bitrates: Array<number>) => {
    console.info('availableBitrates called,and availableBitrates length is:' + bitrates.length);
  });
}
```

#### off('availableBitrates')9+

off(type: 'availableBitrates', callback?: Callback<Array<number>>): void

取消监听HLS/DASH协议网络流可用的比特率列表，调用[prepare](#ZH-CN_TOPIC_0000002553201993__prepare9)后，上报此事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | HLS/DASH协议网络流可用比特率上报事件回调类型，取消注册的事件：'availableBitrates'。 |
| callback12+ | Callback<Array<number>> | 否 | HLS/DASH协议网络流可用比特率上报事件回调方法，使用数组存放支持的比特率。如果数组长度为0，则不支持指定比特率。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('availableBitrates');
}
```

#### on('mediaKeySystemInfoUpdate')11+

on(type: 'mediaKeySystemInfoUpdate', callback: Callback<Array<drm.MediaKeySystemInfo>>): void

监听mediaKeySystemInfoUpdate事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 版权保护信息更新上报事件回调类型，支持的事件：'mediaKeySystemInfoUpdate'，当播放内容的版权保护信息更新时上报事件。 |
| callback | Callback<Array<drm.MediaKeySystemInfo>> | 是 | 版权保护信息更新上报事件回调方法，上报MediaKeySystemInfo数组。 |

**示例：**

```ets
import { drm } from '@kit.DrmKit';

async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('mediaKeySystemInfoUpdate', (mediaKeySystemInfo: Array<drm.MediaKeySystemInfo>) => {
    for (let i = 0; i < mediaKeySystemInfo.length; i++) {
      console.info('mediaKeySystemInfoUpdate happened uuid: ' + mediaKeySystemInfo[i]["uuid"]);
      console.info('mediaKeySystemInfoUpdate happened pssh: ' + mediaKeySystemInfo[i]["pssh"]);
    }
  });
}
```

#### off('mediaKeySystemInfoUpdate')11+

off(type: 'mediaKeySystemInfoUpdate', callback?: Callback<Array<drm.MediaKeySystemInfo>>): void;

取消监听mediaKeySystemInfoUpdate事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 版权保护信息更新上报事件回调类型，取消注册的事件：'mediaKeySystemInfoUpdate'。 |
| callback | Callback<Array<drm.MediaKeySystemInfo>> | 否 | 版权保护信息更新上报事件回调方法，上报版权保护信息数组。如填写该参数，则仅取消注册此回调方法，否则取消注册mediaKeySystemInfoUpdate事件的所有回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('mediaKeySystemInfoUpdate');
}
```

#### setLoudnessGain21+

setLoudnessGain(loudnessGain: number): Promise<void>

设置播放器的响度。调用该接口后，响度增益立即生效。使用Promise异步回调。

- 当播放处于prepared/playing/paused/completed/stopped状态时，可调用该接口。

- 调用此接口时，需确保已设置音频渲染信息AVPlayer.audioRendererInfo，audioRendererInfo的usage参数必须是[STREAM_USAGE_MUSIC](Enums.md#ZH-CN_TOPIC_0000002553201785__streamusage)、[STREAM_USAGE_MOVIE](Enums.md#ZH-CN_TOPIC_0000002553201785__streamusage)、[STREAM_USAGE_AUDIOBOOK](Enums.md#ZH-CN_TOPIC_0000002553201785__streamusage)其中之一。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| loudnessGain | number | 是 | 设置播放器的响度值，单位为dB，响度范围为[-90.0, 24.0]。默认值为0.0dB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. e.g. The function is called in an incorrect state, or the stream usage of audioRendererInfo is not one of [STREAM_USAGE_MUSIC](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage), STREAM_USAGE_MOVIE or [STREAM_USAGE_AUDIOBOOK](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage). |
| 5400105 | Service died. |
| 5400108 | Parameter check failed. Returned by promise. |

**示例：**

```ets
import { audio } from '@kit.AudioKit';

async function test(){
  let avPlayer = await media.createAVPlayer();

  let loudnessGain: number = 1.0;
  avPlayer.audioRendererInfo = {
    usage: audio.StreamUsage.STREAM_USAGE_MOVIE,
    rendererFlags: 0
  }
  avPlayer.setLoudnessGain(loudnessGain);
}
```

#### setVolume9+

setVolume(volume: number): void

设置媒体播放音量，只能在prepared/playing/paused/completed状态调用，可以通过[volumeChange事件](#ZH-CN_TOPIC_0000002553201993__onvolumechange9)确认是否生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| volume | number | 是 | 指定的相对音量大小，取值范围为[0.00-1.00]，1表示最大音量，即100%。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  let volume: number = 1.0;
  avPlayer.setVolume(volume);
}
```

#### on('volumeChange')9+

on(type: 'volumeChange', callback: Callback<number>): void

监听setVolume生效的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setVolume生效的事件回调类型，支持的事件：'volumeChange'，每次调用setVolume后都会回调此事件。 |
| callback | Callback<number> | 是 | setVolume生效的事件回调方法，上报生效的媒体音量。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('volumeChange', (vol: number) => {
    console.info('volumeChange called,and new volume is :' + vol);
  });
}
```

#### off('volumeChange')9+

off(type: 'volumeChange', callback?: Callback<number>): void

取消监听setVolume生效的事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | setVolume生效的事件回调类型，取消注册的事件：'volumeChange'。 |
| callback12+ | Callback<number> | 否 | setVolume生效的事件回调方法，上报生效的媒体音量。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('volumeChange');
}
```

#### on('endOfStream')9+

on(type: 'endOfStream', callback: Callback<void>): void

监听资源播放至结尾的事件；如果用户设置[loop](#ZH-CN_TOPIC_0000002553201993__属性)=true，播放会跳转至开头重播；如果用户没有设置loop，会通过[stateChange](#ZH-CN_TOPIC_0000002553201993__onstatechange9)上报completed状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 资源播放至结尾的事件回调类型，支持的事件：'endOfStream'，当播放至结尾时会上报此事件。 |
| callback | Callback<void> | 是 | 资源播放至结尾的事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('endOfStream', () => {
    console.info('endOfStream called');
  });
}
```

#### off('endOfStream')9+

off(type: 'endOfStream', callback?: Callback<void>): void

取消监听资源播放至结尾的事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 资源播放至结尾的事件回调类型，取消注册的事件：'endOfStream'。 |
| callback12+ | Callback<void> | 否 | 资源播放至结尾的事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('endOfStream');
}
```

#### on('timeUpdate')9+

on(type: 'timeUpdate', callback: Callback<number>): void

监听资源播放当前时间，单位为毫秒（ms），用于刷新进度条当前位置，默认间隔100ms时间上报，因用户操作（seek）产生的时间变化会立刻上报。

- 直播场景不支持timeUpdate上报。
- 操作（seek）时必须等待seekdone结束才能根据timeUpdate来更新进度条。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 时间更新的回调类型，支持的事件：'timeUpdate'。 |
| callback | Callback<number> | 是 | 回调函数。返回当前时间。 |

**示例1：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('timeUpdate', (time:number) => {
    console.info('timeUpdate called,and new time is :' + time);
  });
}
```

**示例2：**

```ets
async function test() {
  let avPlayer = await media.createAVPlayer();

  let isSeeking = false;    // 标记是否正在seek。
  let seekTargetTime = 0;   // 记录目标时间（单位：毫秒）。

  // 1.监听seekDone：确认跳转完成。
  avPlayer.on('seekDone', (seekDoneTime: number) => {
    console.info('seekDone called, and seek time is: ' + seekDoneTime);
    isSeeking = false;
    seekTargetTime = seekDoneTime; // 可选：记录最终定位时间。
  });

  // 2.监听timeUpdate：只在seekDone后才更新进度。
  avPlayer.on('timeUpdate', (time: number) => {
    // 关键逻辑：只有seekDone之后才允许更新进度条。
    if (isSeeking) {
      console.info('seek in progress, ignore timeUpdate');
      return; // 忽略seek期间的timeUpdate。
    }

    // 真正的播放进度更新（seekDone后才生效）。
    console.info('timeUpdate: ' + time + ' ms');
    // 此处进行进度条更新。
  });

  // 3.模拟seek操作。
  let seekTime: number = 1000;
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至prepared/playing/paused/completed状态后才能调用。
  avPlayer.seek(seekTime, media.SeekMode.SEEK_PREV_SYNC); // 单位：毫秒。
  isSeeking = true; // 标记正在seek。
}
```

#### off('timeUpdate')9+

off(type: 'timeUpdate', callback?: Callback<number>): void

取消监听资源播放当前时间。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 时间更新的回调类型，取消注册的事件：'timeUpdate'。 |
| callback12+ | Callback<number> | 否 | 回调函数。返回当前时间。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('timeUpdate');
}
```

#### on('durationUpdate')9+

on(type: 'durationUpdate', callback: Callback<number>): void

监听资源播放资源的时长，单位为毫秒（ms），用于刷新进度条长度，默认只在prepared上报一次，同时允许一些特殊码流刷新多次时长。


直播场景不支持durationUpdate上报。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 时长更新的回调类型，支持的事件：'durationUpdate'。 |
| callback | Callback<number> | 是 | 回调函数。返回资源时长。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('durationUpdate', (duration: number) => {
    console.info('durationUpdate called,new duration is :' + duration);
  });
}
```

#### off('durationUpdate')9+

off(type: 'durationUpdate', callback?: Callback<number>): void

取消监听资源播放资源的时长。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 时长更新的回调类型，取消注册的事件：'durationUpdate'。 |
| callback12+ | Callback<number> | 否 | 回调函数。返回资源时长。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('durationUpdate');
}
```

#### on('bufferingUpdate')9+

on(type: 'bufferingUpdate', callback: [OnBufferingUpdateHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onbufferingupdatehandler12)): void

订阅音视频缓存更新事件，仅网络播放支持该订阅事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 播放缓存事件回调类型，支持的事件：'bufferingUpdate'。 |
| callback | [OnBufferingUpdateHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onbufferingupdatehandler12) | 是 | 播放缓存事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
    console.info('bufferingUpdate called,and infoType value is:' + infoType + ', value is :' + value);
  });
}
```

#### off('bufferingUpdate')9+

off(type: 'bufferingUpdate', callback?: [OnBufferingUpdateHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onbufferingupdatehandler12)): void

取消监听音视频缓存更新事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 播放缓存事件回调类型，取消注册的事件：'bufferingUpdate'。 |
| callback | [OnBufferingUpdateHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onbufferingupdatehandler12) | 否 | 播放缓存事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('bufferingUpdate');
}
```

#### on('startRenderFrame')9+

on(type: 'startRenderFrame', callback: Callback<void>): void

订阅视频播放开始首帧渲染的更新事件，仅视频播放支持该订阅事件，该事件仅代表播放服务将第一帧画面送显示模块，实际效果依赖显示服务渲染性能。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放开始首帧渲染事件回调类型，支持的事件：'startRenderFrame'。 |
| callback | Callback<void> | 是 | 视频播放开始首帧渲染事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('startRenderFrame', () => {
    console.info('startRenderFrame called');
  });
}
```

#### off('startRenderFrame')9+

off(type: 'startRenderFrame', callback?: Callback<void>): void

取消监听视频播放开始首帧渲染的更新事件。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放开始首帧渲染事件回调类型，取消注册的事件：'startRenderFrame'。 |
| callback12+ | Callback<void> | 否 | 视频播放开始首帧渲染事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('startRenderFrame');
}
```

#### on('videoSizeChange')9+

on(type: 'videoSizeChange', callback: [OnVideoSizeChangeHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onvideosizechangehandler12)): void

监听视频播放宽高变化事件，仅视频播放支持该订阅事件，默认只在prepared状态上报一次，但HLS协议码流会在切换分辨率时上报。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放宽高变化事件回调类型，支持的事件：'videoSizeChange'。 |
| callback | [OnVideoSizeChangeHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onvideosizechangehandler12) | 是 | 视频播放宽高变化事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('videoSizeChange', (width: number, height: number) => {
    console.info('videoSizeChange called,and width is:' + width + ', height is :' + height);
  });
}
```

#### off('videoSizeChange')9+

off(type: 'videoSizeChange', callback?: [OnVideoSizeChangeHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onvideosizechangehandler12)): void

取消监听视频播放宽高变化事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 视频播放宽高变化事件回调类型，取消注册的事件：'videoSizeChange'。 |
| callback12+ | [OnVideoSizeChangeHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onvideosizechangehandler12) | 否 | 视频播放宽高变化事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('videoSizeChange');
}
```

#### on('audioInterrupt')9+

on(type: 'audioInterrupt', callback: Callback<audio.InterruptEvent>): void

监听音频焦点变化事件，多个音视频资源同时播放时，会根据音频焦点模型[audio.InterruptMode](Enums.md#ZH-CN_TOPIC_0000002553201785__interruptmode9)触发此事件。应用需根据不同焦点变化事件作相应处理。具体可参考[处理音频焦点事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-concurrency)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 音频焦点变化事件回调类型，支持的事件：'audioInterrupt'。 |
| callback | Callback<audio.InterruptEvent> | 是 | 音频焦点变化事件回调方法。 |

**示例：**

```ets
import { audio } from '@kit.AudioKit';

async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('audioInterrupt', (info: audio.InterruptEvent) => {
    console.info('audioInterrupt called,and InterruptEvent info is:' + info);
  });
}
```

#### off('audioInterrupt')9+

off(type: 'audioInterrupt', callback?: Callback<audio.InterruptEvent>): void

取消监听音频焦点变化事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 音频焦点变化事件回调类型，取消注册的事件：'audioInterrupt'。 |
| callback12+ | Callback<audio.InterruptEvent> | 否 | 音频焦点变化事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('audioInterrupt');
}
```

#### on('audioOutputDeviceChangeWithInfo')11+

on(type: 'audioOutputDeviceChangeWithInfo', callback: Callback<audio.AudioStreamDeviceChangeInfo>): void

订阅监听音频流输出设备变化及原因，使用callback方式返回结果。

在订阅此监听时，建议参考[响应输出设备变更时合理暂停](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-change)自行实现设备连接或者断开时的播放器行为。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'audioOutputDeviceChangeWithInfo'。 |
| callback | Callback<audio.AudioStreamDeviceChangeInfo> | 是 | 回调函数，返回当前音频流的输出设备描述信息及变化原因。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
import { audio } from '@kit.AudioKit';

async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('audioOutputDeviceChangeWithInfo', (data: audio.AudioStreamDeviceChangeInfo) => {
    console.info(`${JSON.stringify(data)}`);
  });
}
```

#### off('audioOutputDeviceChangeWithInfo')11+

off(type: 'audioOutputDeviceChangeWithInfo', callback?: Callback<audio.AudioStreamDeviceChangeInfo>): void

取消订阅监听音频流输出设备变化及原因，使用callback方式返回结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'audioOutputDeviceChangeWithInfo'。 |
| callback | Callback<audio.AudioStreamDeviceChangeInfo> | 否 | 回调函数，返回当前音频流的输出设备描述信息及变化原因。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('audioOutputDeviceChangeWithInfo');
}
```

#### addSubtitleFromFd12+

addSubtitleFromFd(fd: number, offset?: number, length?: number): Promise<void>

依据fd为视频添加外挂字幕，当前仅支持与视频资源同时设置（在avplayer设置fdSrc视频资源后设置外挂字幕）。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fd | number | 是 | 资源句柄，通过resourceManager.getRawFd获取。 |
| offset | number | 否 | 资源偏移量，需要基于预置资源的信息输入，非法值会造成字幕频资源解析错误，默认值:0。 |
| length | number | 否 | 资源长度，默认值为文件中从偏移量开始的剩余字节，需要基于预置资源的信息输入，非法值会造成字幕频资源解析错误，默认值:0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
import { common } from '@kit.AbilityKit'

let avPlayer = await media.createAVPlayer();
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let fileDescriptor = await context.resourceManager.getRawFd('xxx.srt');

avPlayer.addSubtitleFromFd(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length);
```

#### addSubtitleFromUrl12+

addSubtitleFromUrl(url: string): Promise<void>

依据url为视频添加外挂字幕，当前仅支持与视频资源同时设置（在avplayer设置fdSrc视频资源后设置外挂字幕）。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | 外挂字幕文件地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | The parameter check failed. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |

**示例：**

```ets
async function test(){
  let fdUrl:string = 'http://xxx.xxx.xxx/xx/index.srt';
  let avPlayer: media.AVPlayer = await media.createAVPlayer();
  avPlayer.addSubtitleFromUrl(fdUrl);
}
```

#### on('subtitleUpdate')12+

on(type: 'subtitleUpdate', callback: Callback<SubtitleInfo>): void

订阅获取外挂字幕的事件，当有外挂字幕时，会通过订阅的回调方法通知用户。用户只能订阅一个外挂字幕事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'subtitleUpdate'。 |
| callback | Callback<SubtitleInfo> | 是 | 外挂字幕事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('subtitleUpdate', async (info: media.SubtitleInfo) => {
    if (info) {
      let text = (!info.text) ? '' : info.text
      let startTime = (!info.startTime) ? 0 : info.startTime
      let duration = (!info.duration) ? 0 : info.duration
      console.info('subtitleUpdate info: text=' + text + ' startTime=' + startTime +' duration=' + duration);
    } else {
      console.info('subtitleUpdate info is null');
    }
  });
}
```

#### off('subtitleUpdate')12+

off(type: 'subtitleUpdate', callback?: Callback<SubtitleInfo>): void

取消订阅获取外挂字幕的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'subtitleUpdate'。 |
| callback | Callback<SubtitleInfo> | 否 | 取消外挂字幕事件的回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('subtitleUpdate');
}
```

#### on('trackChange')12+

on(type: 'trackChange', callback: [OnTrackChangeHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__ontrackchangehandler12)): void

订阅获取轨道变更的事件，当播放的轨道变更时，会通过订阅的回调方法通知用户。用户只能订阅一个轨道变更事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'trackChange'。 |
| callback | [OnTrackChangeHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__ontrackchangehandler12) | 是 | 轨道变更事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('trackChange', (index: number, isSelect: boolean) => {
    console.info('trackChange info: index=' + index + ' isSelect=' + isSelect);
  });
}
```

#### off('trackChange')12+

off(type: 'trackChange', callback?: [OnTrackChangeHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__ontrackchangehandler12)): void

取消订阅获取轨道变更的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'trackChange'。 |
| callback | [OnTrackChangeHandler](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__ontrackchangehandler12) | 否 | 取消轨道变更事件的回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('trackChange');
}
```

#### on('trackInfoUpdate')12+

on(type: 'trackInfoUpdate', callback: Callback<Array<MediaDescription>>): void

订阅获取轨道信息更新的事件，当播放的轨道有更新时，会通过订阅的回调方法通知用户。用户只能订阅一个轨道变更事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'trackInfoUpdate'。 |
| callback | Callback<Array<MediaDescription>> | 是 | 轨道信息更新事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('trackInfoUpdate', (info: Array<media.MediaDescription>) => {
    if (info) {
      for (let i = 0; i < info.length; i++) {
        let propertyIndex: Object = info[i][media.MediaDescriptionKey.MD_KEY_TRACK_INDEX];
        let propertyType: Object = info[i][media.MediaDescriptionKey.MD_KEY_TRACK_TYPE];
        console.info('track info: index=' + propertyIndex + ' tracktype=' + propertyType);
      }
    } else {
      console.info('track info is null');
    }
  });
}
```

#### off('trackInfoUpdate')12+

off(type: 'trackInfoUpdate', callback?: Callback<Array<MediaDescription>>): void

取消订阅获取轨道信息更新的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'trackInfoUpdate'。 |
| callback | Callback<Array<MediaDescription>> | 否 | 取消轨道信息更新事件的回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('trackInfoUpdate');
}
```

#### on('amplitudeUpdate')13+

on(type: 'amplitudeUpdate', callback: Callback<Array<number>>): void

订阅音频最大电平值，音频资源播放时定时上报。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'amplitudeUpdate'。 |
| callback | Callback<Array<number>> | 是 | 音频最大电平值更新事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('amplitudeUpdate', (value: Array<number>) => {
    console.info(`amplitudeUpdate called,and amplitudeUpdate = ${value}`);
  });
}
```

#### off('amplitudeUpdate')13+

off(type: 'amplitudeUpdate', callback?: Callback<Array<number>>): void

取消订阅获取音频最大电平值事件。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'amplitudeUpdate'。 |
| callback | Callback<Array<number>> | 否 | 取消音频最大电平值更新事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('amplitudeUpdate');
}
```

#### on('seiMessageReceived')18+

on(type: 'seiMessageReceived', payloadTypes: Array<number>, callback: [OnSeiMessageHandle](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onseimessagehandle18)): void

订阅获取SEI信息事件，仅适用于HTTP-FLV直播，视频流中包含SEI信息时上报。需在prepare之前订阅，当用户重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'seiMessageReceived'。 |
| payloadTypes | Array<number> | 是 | SEI信息的订阅负载类型数组。当前仅支持负载类型为5，即payloadType = 5。 |
| callback | [OnSeiMessageHandle](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onseimessagehandle18) | 是 | 用于监听SEI信息事件的回调函数，接收订阅的负载类型。 |

**示例：**

```ets
import { util } from '@kit.ArkTS';

async function test(){
  let avPlayer = await media.createAVPlayer();

  avPlayer.on('seiMessageReceived', [5], (messages: Array<media.SeiMessage>, playbackPosition?: number) =>
  {
    console.info('seiMessageReceived playbackPosition ' + playbackPosition);

    for (let key = 0; key < messages.length; key++) {
      console.info('seiMessageReceived messages payloadType ' + messages[key].payloadType + ' payload size ' + messages[key].payload.byteLength);

      let textDecoder = util.TextDecoder.create("utf-8",{ignoreBOM: true});
      let ab = messages[key]?.payload?.slice(16, messages[key].payload.byteLength);
      let result: Uint8Array = new Uint8Array(ab);
      let retStr: string = textDecoder.decodeToString(result);
      console.info('seiMessageReceived messages payload ' + retStr);
    }
  });
}
```

#### off('seiMessageReceived')18+

off(type: 'seiMessageReceived', payloadTypes?: Array<number>, callback?: [OnSeiMessageHandle](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onseimessagehandle18)): void

取消订阅获取SEI信息事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'seiMessageReceived'。 |
| payloadTypes | Array<number> | 否 | SEI信息的订阅负载类型。 |
| callback | [OnSeiMessageHandle](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onseimessagehandle18) | 否 | 用于监听SEI信息事件的回调函数，接收订阅的负载类型。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('seiMessageReceived');
}
```

#### setSuperResolution18+

setSuperResolution(enabled: boolean) : Promise<void>

动态开启/关闭超分算法，可在 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' 状态下调用。使用Promise异步回调。

在调用[prepare()](#ZH-CN_TOPIC_0000002553201993__prepare9)前先通过[PlaybackStrategy](Interfaces (其他).md#ZH-CN_TOPIC_0000002553361955__playbackstrategy12)使能超分。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 表示是否开启超分。true表示开启超分，false表示关闭超分。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400102 | Operation not allowed. Return by promise. |
| 5410003 | Super-resolution not supported. Return by promise. |
| 5410004 | Missing enable super-resolution feature in PlaybackStrategy. Return by promise. |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized/prepared/playing/paused/completed/stopped状态后才能调用。
  avPlayer.setSuperResolution(true);
}
```

#### setVideoWindowSize18+

setVideoWindowSize(width: number, height: number) : Promise<void>

动态设置超分算法的输出分辨率。可在 'initialized' | 'prepared' | 'playing' | 'paused' | 'completed' | 'stopped' 状态下调用。使用Promise异步回调。

输入参数须在320x320~1920x1080范围内，单位为像素。

在调用[prepare()](#ZH-CN_TOPIC_0000002553201993__prepare9)前先通过[PlaybackStrategy](Interfaces (其他).md#ZH-CN_TOPIC_0000002553361955__playbackstrategy12)使能超分。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 超分算法的目标输出视频宽度，取值范围为[320-1920]，单位为像素。 |
| height | number | 是 | 超分算法的目标输出视频高度，取值范围为[320-1080]，单位为像素。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[媒体错误码](Media错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Return by promise. |
| 5400102 | Operation not allowed. Return by promise. |
| 5410003 | Super-resolution not supported. Return by promise. |
| 5410004 | Missing enable super-resolution feature in PlaybackStrategy. Return by promise. |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  // 此处仅为示意，实际开发中需要在stateChange事件成功触发至initialized/prepared/playing/paused/completed/stopped状态后才能调用。
  avPlayer.setVideoWindowSize(1920, 1080);
}
```

#### on('superResolutionChanged')18+

on(type:'superResolutionChanged', callback: [OnSuperResolutionChanged](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onsuperresolutionchanged-18)): void

订阅监听超分算法开启/关闭事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'superResolutionChanged'，当超分算法开启/关闭状态变化时，触发该事件。 |
| callback | [OnSuperResolutionChanged](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onsuperresolutionchanged-18) | 是 | 超分开关事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.on('superResolutionChanged', (enabled: boolean) => {
    console.info('superResolutionChanged called, and enabled is:' + enabled);
  });
}
```

#### off('superResolutionChanged')18+

off(type:'superResolutionChanged', callback?: [OnSuperResolutionChanged](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onsuperresolutionchanged-18)): void

取消监听超分算法开启/关闭事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为：'superResolutionChanged'，当超分算法开启/关闭状态变化时，触发该事件。 |
| callback | [OnSuperResolutionChanged](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002529285893__onsuperresolutionchanged-18) | 否 | 超分开关事件回调方法。 |

**示例：**

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.off('superResolutionChanged');
}
```

**getPlaybackStatisticMetrics23+**

getPlaybackStatisticMetrics(): Promise<PlaybackMetrics>

获取当前播放器的统计指标信息，可以在准备（prepared）/播放（playing）/暂停（paused）/完成（completed）/停止（stopped）状态调用。使用Promise异步回调。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<PlaybackMetrics> | Promise对象，返回当前播放器的指标信息PlaybackMetrics。 |

示例：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer | undefined = undefined;
let playbackMetrics: media.PlaybackMetrics | undefined = undefined;
media.createAVPlayer(async (err: BusinessError, player: media.AVPlayer) => {
  if (player != null) {
    avPlayer = player;
    console.info(`Succeeded in creating AVPlayer`);
    if (avPlayer) {
      try {
        playbackMetrics = await avPlayer.getPlaybackStatisticMetrics();
        console.info(`AVPlayer getPlaybackStatisticMetrics = ${JSON.stringify(playbackMetrics)}`); // 打印整个playbackMetrics的值。
      } catch (error) {
        console.error(`error = ${error}`);
      }
  } else {
    console.error(`Failed to create AVPlayer, error message:${err.message}`);
  }
});
```

**onMetricsEvent23+**

onMetricsEvent(callback: Callback<Array<AVMetricsEvent>>): void

订阅播放过程中的指标事件。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<Array<AVMetricsEvent>> | 是 | 上报的指标事件信息的方法。使用callback异步回调。 |

示例：

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.onMetricsEvent((info: Array<media.AVMetricsEvent>) => {
    if (info) {
      for (let i = 0; i < info.length; i++) {
        console.info('metrics info: index=' + i + ' info=' + JSON.stringify(info));
      }
    } else {
      console.info('metrics info is null');
    }
  });
}
```

**offMetricsEvent23+**

offMetricsEvent(callback?: Callback<Array<AVMetricsEvent>>): void

取消订阅播放过程中的指标事件。

系统能力： SystemCapability.Multimedia.Media.AVPlayer

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<Array<AVMetricsEvent>> | 否 | 上报的指标事件信息的方法。使用callback异步回调。 |

示例：

```ets
async function test(){
  let avPlayer = await media.createAVPlayer();
  avPlayer.offMetricsEvent();
}
```