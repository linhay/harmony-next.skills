[]()[]()

# Functions

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { media } from '@kit.MediaKit';
```

[]()[]()

#### media.createAVPlayer9+

createAVPlayer(callback: AsyncCallback<AVPlayer>): void

创建音视频播放实例。使用callback异步回调。

- 推荐单个应用创建的音视频播放实例（即音频、视频、音视频三类相加）不超过16个。
- 应用需要按照实际业务需求合理使用AVPlayer对象，按需创建并及时释放，避免持有过多AVPlayer实例导致内存消耗过大，否则在一定情况下可能导致系统终止应用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVPlayer](../../types/interfaces/Interface (AVPlayer).md)>是回调函数。异步返回AVPlayer实例，失败时返回null。可用于音视频播放。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer;
media.createAVPlayer((error: BusinessError, video: media.AVPlayer) => {
  if (video != null) {
    avPlayer = video;
    console.info('Succeeded in creating AVPlayer');
  } else {
    console.error(`Failed to create AVPlayer, error message:${error.message}`);
  }
});
```

[]()[]()

#### media.createAVPlayer9+

createAVPlayer(): Promise<AVPlayer>

异步方式创建音视频播放实例。使用Promise异步回调。

- 推荐单个应用创建的音视频播放实例（即音频、视频、音视频三类相加）不超过16个。
- 应用需要按照实际业务需求合理使用AVPlayer对象，按需创建并及时释放，避免持有过多AVPlayer实例导致内存消耗过大，否则在一定情况下可能导致系统终止应用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**返回值：**

类型说明Promise<[AVPlayer](../../types/interfaces/Interface (AVPlayer).md)>Promise对象。异步返回AVPlayer实例，失败时返回null。可用于音视频播放。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avPlayer: media.AVPlayer;
media.createAVPlayer().then((video: media.AVPlayer) => {
  if (video != null) {
    avPlayer = video;
    console.info('Succeeded in creating AVPlayer');
  } else {
    console.error('Failed to create AVPlayer');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVPlayer, error message:${error.message}`);
});
```

[]()[]()

#### media.createAVRecorder9+

createAVRecorder(callback: AsyncCallback<AVRecorder>): void

创建音视频录制实例。使用callback异步回调。

应用可创建多个音视频录制实例，但由于设备共用音频通路，一个设备仅能有一个实例进行音频录制。创建第二个实例录制音频时，将会因为音频通路冲突导致创建失败。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVRecorder](../../types/interfaces/Interface (AVRecorder).md)>是回调函数，返回AVRecorder实例，失败时返回null。可用于录制音视频媒体。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let avRecorder: media.AVRecorder;

media.createAVRecorder((error: BusinessError, recorder: media.AVRecorder) => {
  if (recorder != null) {
    avRecorder = recorder;
    console.info('Succeeded in creating AVRecorder');
  } else {
    console.error(`Failed to create AVRecorder, error message:${error.message}`);
  }
});
```

[]()[]()

#### media.createAVRecorder9+

createAVRecorder(): Promise<AVRecorder>

创建音视频录制实例。使用Promise异步回调。

应用可创建多个音视频录制实例，但由于设备共用音频通路，一个设备仅能有一个实例进行音频录制。创建第二个实例录制音频时，将会因为音频通路冲突导致创建失败。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**返回值：**

类型说明Promise<[AVRecorder](../../types/interfaces/Interface (AVRecorder).md)>Promise对象，返回AVRecorder实例，失败时返回null。可用于录制音视频媒体。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let avRecorder: media.AVRecorder;
media.createAVRecorder().then((recorder: media.AVRecorder) => {
  if (recorder != null) {
    avRecorder = recorder;
    console.info('Succeeded in creating AVRecorder');
  } else {
    console.error('Failed to create AVRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVRecorder, error message:${error.message}`);
});
```

[]()[]()

#### media.createAVTranscoder12+

createAVTranscoder(): Promise<AVTranscoder>

创建视频转码实例。使用Promise异步回调。

可创建的视频转码实例不能超过2个。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

类型说明Promise<[AVTranscoder](../../types/interfaces/Interface (AVTranscoder).md)>Promise对象。异步返回AVTranscoder实例，失败时返回null。可用于视频转码。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avTranscoder: media.AVTranscoder | undefined = undefined;
media.createAVTranscoder().then((transcoder: media.AVTranscoder) => {
  if (transcoder != null) {
    avTranscoder = transcoder;
    console.info('Succeeded in creating AVTranscoder');
  } else {
    console.error('Failed to create AVTranscoder');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVTranscoder, error message:${error.message}`);
});
```

[]()[]()

#### media.createAVMetadataExtractor11+

createAVMetadataExtractor(callback: AsyncCallback<AVMetadataExtractor>): void

创建AVMetadataExtractor实例。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVMetadataExtractor](../../types/interfaces/Interface (AVMetadataExtractor).md)>是回调函数。当创建AVMetadataExtractor实例成功，err为undefined，data为获取到的AVMetadataExtractor实例，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Returned by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avMetadataExtractor: media.AVMetadataExtractor;
media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
  if (extractor != null) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
  } else {
    console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
  }
});
```

[]()[]()

#### media.createAVMetadataExtractor11+

createAVMetadataExtractor(): Promise<AVMetadataExtractor>

创建AVMetadataExtractor实例。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**返回值：**

类型说明Promise<[AVMetadataExtractor](../../types/interfaces/Interface (AVMetadataExtractor).md)>Promise对象。异步返回元数据获取类对象（AVMetadataExtractor）。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Returned by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avMetadataExtractor: media.AVMetadataExtractor;
media.createAVMetadataExtractor().then((extractor: media.AVMetadataExtractor) => {
  if (extractor != null) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
  } else {
    console.error(`Failed to create AVMetadataExtractor`);
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVMetadataExtractor, error message:${error.message}`);
});
```

[]()[]()

#### media.createSoundPool10+

createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo, callback: AsyncCallback<SoundPool>): void

创建音频池实例。使用callback异步回调。

- API version 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。
- API version 18及API version 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明maxStreamsnumber是soundPool实例的最大播放的流数，设置范围为1-32的正整数。audioRenderInfo[audio.AudioRendererInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-audio-i).md#ZH-CN_TOPIC_0000002497445724__audiorendererinfo8)是音频播放参数信息。其中audioRenderInfo中的参数usage取值为STREAM_USAGE_UNKNOWN，STREAM_USAGE_MUSIC，STREAM_USAGE_MOVIE，STREAM_USAGE_AUDIOBOOK时，SoundPool播放短音时为混音模式，不会打断其他音频播放。SoundPool支持将rendererFlags设置为1用于低时延通路播放。callbackAsyncCallback<[SoundPool](../media/SoundPool (音频池).md)>是回调函数。异步返回SoundPool实例，失败时返回null。用于音频池实例的加载播放功能。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Return by callback.

**示例：**

```ets
import { audio } from '@kit.AudioKit';

let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage : audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags : 0
};

media.createSoundPool(5, audioRendererInfo, (error, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
  }
});
```

[]()[]()

#### media.createSoundPool10+

createSoundPool(maxStreams: number, audioRenderInfo: audio.AudioRendererInfo): Promise<SoundPool>

创建音频池实例。使用Promise异步回调。

- API version 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。
- API version 18及API version 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明maxStreamsnumber是soundPool实例的最大播放的流数，设置范围为1-32的正整数。audioRenderInfo[audio.AudioRendererInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-audio-i).md#ZH-CN_TOPIC_0000002497445724__audiorendererinfo8)是音频播放参数信息

**返回值：**

类型说明Promise<[SoundPool](../media/SoundPool (音频池).md)>Promise对象。异步返回SoundPool实例，失败时返回null。用于音频池实例的加载播放功能。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Return by promise.

**示例：**

```ets
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage : audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags : 0
};

media.createSoundPool(5, audioRendererInfo).then((soundpool_: media.SoundPool) => {
  if (soundpool_ != null) {
    soundPool = soundpool_;
    console.info('Succeeded in creating SoundPool');
  } else {
    console.error('Failed to create SoundPool');
  }
}, (error: BusinessError) => {
  console.error(`soundpool catchCallback, error message:${error.message}`);
});
```

[]()[]()

#### media.createAVScreenCaptureRecorder12+

createAVScreenCaptureRecorder(): Promise<AVScreenCaptureRecorder>

创建屏幕录制实例，使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**返回值：**

类型说明Promise<[AVScreenCaptureRecorder](../../types/interfaces/Interface (AVScreenCaptureRecorder).md)>Promise对象，返回AVScreenCaptureRecorder实例，失败时返回null。可用于进行屏幕录制。

**错误码：**

错误码ID错误信息5400101No memory. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avScreenCaptureRecorder: media.AVScreenCaptureRecorder;
media.createAVScreenCaptureRecorder().then((captureRecorder: media.AVScreenCaptureRecorder) => {
  if (captureRecorder != null) {
    avScreenCaptureRecorder = captureRecorder;
    console.info('Succeeded in createAVScreenCaptureRecorder');
  } else {
    console.error('Failed to createAVScreenCaptureRecorder');
  }
}).catch((error: BusinessError) => {
  console.error(`createAVScreenCaptureRecorder catchCallback, error message:${error.message}`);
});
```

[]()[]()

#### media.createAVImageGenerator12+

createAVImageGenerator(callback: AsyncCallback<AVImageGenerator>): void

创建AVImageGenerator实例。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVImageGenerator](../../types/interfaces/Interface (AVImageGenerator).md)>是回调函数。异步返回AVImageGenerator实例，失败时返回null。可用于获取视频缩略图。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Returned by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avImageGenerator: media.AVImageGenerator;
media.createAVImageGenerator((error: BusinessError, generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info('Succeeded in creating AVImageGenerator');
  } else {
    console.error(`Failed to create AVImageGenerator, error message:${error.message}`);
  }
});
```

[]()[]()

#### media.createAVImageGenerator12+

createAVImageGenerator(): Promise<AVImageGenerator>

创建AVImageGenerator对象。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**返回值：**

类型说明Promise<[AVImageGenerator](../../types/interfaces/Interface (AVImageGenerator).md)>Promise对象。异步返回AVImageGenerator实例，失败时返回null。可用于获取视频缩略图。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400101No memory. Returned by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avImageGenerator: media.AVImageGenerator;
media.createAVImageGenerator().then((generator: media.AVImageGenerator) => {
  if (generator != null) {
    avImageGenerator = generator;
    console.info('Succeeded in creating AVImageGenerator');
  } else {
    console.error('Failed to create AVImageGenerator');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create AVImageGenerator, error message:${error.message}`);
});
```

[]()[]()

#### media.createMediaSourceWithUrl12+

createMediaSourceWithUrl(url: string, headers?: Record<string, string>): MediaSource

创建流媒体预下载媒体来源实例方法。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

参数名类型必填说明urlstring是

- 流媒体预下载媒体来源url，支持的流媒体格式：HLS、HTTP-FLV、Dash、Https。

 - 本地m3u8的fd路径。

headersRecord<string, string>否支持流媒体预下载HttpHeader自定义。

**返回值：**

类型说明[MediaSource](../../types/interfaces/Interface (MediaSource).md)MediaSource返回值。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.5400101No memory.

**示例1：**

```ets
let headers: Record<string, string> = {"User-Agent" : "User-Agent-Value"};
let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://xxx",  headers);
```

**示例2：**

```ets
import { media } from "@kit.MediaKit";

async function test(context: Context){
    // this.getUIContext().getHostContext();
    let mgr = context?.resourceManager;
    if (!mgr) {
        return;
    }
    let fileDescriptor = await mgr.getRawFd("xxx.m3u8");

    let fd: string = fileDescriptor.fd.toString();
    let offset: string = fileDescriptor.offset.toString();
    let length: string = fileDescriptor.length.toString();
    let fdUrl: string = "fd://" + fd + "?offset=" + offset + "&size=" + length;

    let mediaSource: media.MediaSource = media.createMediaSourceWithUrl(fdUrl);
}
```

[]()[]()

#### media.createMediaSourceWithStreamData19+

createMediaSourceWithStreamData(streams: Array<MediaStream>): MediaSource

创建流媒体多码率媒体来源实例方法，当前仅支持HTTP-FLV协议格式多码率。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

参数名类型必填说明streamsArray<[MediaStream](../../types/interfaces/Interfaces (其他) (arkts-apis-media-i).md#ZH-CN_TOPIC_0000002497605902__mediastream19)>是可设置MediaStream数组，支持的流媒体格式：HTTP-FLV。

**返回值：**

类型说明[MediaSource](../../types/interfaces/Interface (MediaSource).md)返回MediaSource，用于媒体资源设置。

**示例：**

```ets
let streams : Array<media.MediaStream> = [];
streams.push({url: "http://xxx/480p.flv", width: 854, height: 480, bitrate: 800000});
streams.push({url: "http://xxx/720p.flv", width: 1280, height: 720, bitrate: 2000000});
streams.push({url: "http://xxx/1080p.flv", width: 1920, height: 1080, bitrate: 2000000});
let mediaSource : media.MediaSource = media.createMediaSourceWithStreamData(streams);
```

[]()[]()

#### media.createAudioPlayer(deprecated)

createAudioPlayer(): AudioPlayer

同步方式创建音频播放实例。

从API version 6开始支持，从API version 9开始废弃，建议使用[createAVPlayer](#ZH-CN_TOPIC_0000002529445861__mediacreateavplayer9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioPlayer

**返回值：**

类型说明[AudioPlayer](../media/废弃的Interface (AudioPlayer, deprecated).md)返回AudioPlayer类实例，失败时返回null。可用于音频播放、暂停、停止等操作。

**示例：**

```ets
let audioPlayer: media.AudioPlayer = media.createAudioPlayer();
```

[]()[]()

#### media.createVideoPlayer(deprecated)

createVideoPlayer(callback: AsyncCallback<VideoPlayer>): void

异步方式创建视频播放实例，通过注册回调函数获取返回值。

从API version 8开始支持，从API version 9开始废弃，建议使用[createAVPlayer](#ZH-CN_TOPIC_0000002529445861__mediacreateavplayer9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

参数名类型必填说明callbackAsyncCallback<[VideoPlayer](../media/废弃的Interface (VideoPlayer, deprecated).md)>是回调函数。创建VideoPlayer实例成功时，err为undefined，data为获取到的VideoPlayer实例，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
```

[]()[]()

#### media.createVideoPlayer(deprecated)

createVideoPlayer(): Promise<VideoPlayer>

异步方式创建视频播放实例，通过Promise获取返回值。

从API version 8开始支持，从API version 9开始废弃，建议使用[createAVPlayer](#ZH-CN_TOPIC_0000002529445861__mediacreateavplayer9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

类型说明Promise<[VideoPlayer](../media/废弃的Interface (VideoPlayer, deprecated).md)>Promise对象。异步返回VideoPlayer实例，失败时返回null。可用于管理和播放视频媒体。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer;
media.createVideoPlayer().then((video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error('Failed to create VideoPlayer');
  }
}).catch((error: BusinessError) => {
  console.error(`Failed to create VideoPlayer, error:${error}`);
});
```

[]()[]()

#### media.createAudioRecorder(deprecated)

createAudioRecorder(): AudioRecorder

创建音频录制的实例来控制音频的录制。

一台设备只允许创建一个录制实例。

从API version 6开始支持，从API version 9开始废弃，建议使用[createAVRecorder](#ZH-CN_TOPIC_0000002529445861__mediacreateavrecorder9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**返回值:**

类型说明[AudioRecorder](../payment/废弃的Interface (AudioRecorder, deprecated).md)返回AudioRecorder类实例，失败时返回null。可用于录制音频媒体。

**示例：**

```ets
let audioRecorder: media.AudioRecorder = media.createAudioRecorder();
```