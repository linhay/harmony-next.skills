[]()[]()

# Functions

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { audio } from '@kit.AudioKit';
```

[]()[]()

#### audio.getAudioManager

getAudioManager(): AudioManager

获取音频管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

类型说明[AudioManager](../../types/interfaces/Interface (AudioManager).md)音频管理器对象。

**示例：**

```ets
import { audio } from '@kit.AudioKit';

let audioManager = audio.getAudioManager();
```

[]()[]()

#### audio.createAudioRenderer8+

createAudioRenderer(options: AudioRendererOptions, callback: AsyncCallback<AudioRenderer>): void

获取音频渲染器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明options[AudioRendererOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-audio-i).md#ZH-CN_TOPIC_0000002497445724__audiorendereroptions8)是配置渲染器。callbackAsyncCallback<[AudioRenderer](../../types/interfaces/Interface (AudioRenderer).md)>是回调函数。当获取音频渲染器成功，err为undefined，data为获取到的音频渲染器对象；否则为错误对象。

**示例：**

```ets
import { audio } from '@kit.AudioKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};

let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};

let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

let audioRenderer: audio.AudioRenderer;

audio.createAudioRenderer(audioRendererOptions,(err, data) => {
  if (err) {
    console.error(`AudioRenderer Created: Error: ${err}`);
  } else {
    console.info('AudioRenderer Created: SUCCESS');
    audioRenderer = data;
  }
});
```

[]()[]()

#### audio.createAudioRenderer8+

createAudioRenderer(options: AudioRendererOptions): Promise<AudioRenderer>

获取音频渲染器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明options[AudioRendererOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-audio-i).md#ZH-CN_TOPIC_0000002497445724__audiorendereroptions8)是配置渲染器。

**返回值：**

类型说明Promise<[AudioRenderer](../../types/interfaces/Interface (AudioRenderer).md)>Promise对象，返回音频渲染器对象。

**示例：**

```ets
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};

let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};

let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

let audioRenderer: audio.AudioRenderer;

audio.createAudioRenderer(audioRendererOptions).then((data) => {
  audioRenderer = data;
  console.info('AudioFrameworkRenderLog: AudioRenderer Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRenderLog: AudioRenderer Created : ERROR : ${err}`);
});
```

[]()[]()

#### audio.createAudioCapturer8+

createAudioCapturer(options: AudioCapturerOptions, callback: AsyncCallback<AudioCapturer>): void

获取音频采集器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**需要权限：** ohos.permission.MICROPHONE

当设置Mic音频源（即[SourceType](Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__sourcetype8)为SOURCE_TYPE_MIC、SOURCE_TYPE_VOICE_RECOGNITION、SOURCE_TYPE_VOICE_COMMUNICATION、SOURCE_TYPE_VOICE_MESSAGE、SOURCE_TYPE_CAMCORDER）时需要该权限。

**参数：**

参数名类型必填说明options[AudioCapturerOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-audio-i).md#ZH-CN_TOPIC_0000002497445724__audiocaptureroptions8)是配置音频采集器。callbackAsyncCallback<[AudioCapturer](../../types/interfaces/Interface (AudioCapturer).md)>是

回调函数。当获取音频采集器成功，err为undefined，data为获取到的音频采集器对象；否则为错误对象。异常将返回error对象：

错误码6800301：表示参数校验异常、权限校验异常或系统处理异常（具体错误查看系统日志）。

错误码6800101：表示必选参数为空或参数类型错误。

**示例：**

```ets
import { audio } from '@kit.AudioKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
  capturerFlags: 0 // 音频采集器标志。
};

let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

let audioCapturer: audio.AudioCapturer;

audio.createAudioCapturer(audioCapturerOptions, (err, data) => {
  if (err) {
    console.error(`AudioCapturer Created : Error: ${err}`);
  } else {
    console.info('AudioCapturer Created : SUCCESS');
    audioCapturer = data;
  }
});
```

[]()[]()

#### audio.createAudioCapturer8+

createAudioCapturer(options: AudioCapturerOptions): Promise<AudioCapturer>

获取音频采集器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**需要权限：** ohos.permission.MICROPHONE

当设置Mic音频源（即[SourceType](Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__sourcetype8)为SOURCE_TYPE_MIC、SOURCE_TYPE_VOICE_RECOGNITION、SOURCE_TYPE_VOICE_COMMUNICATION、SOURCE_TYPE_VOICE_MESSAGE、SOURCE_TYPE_CAMCORDER）时需要该权限。

**参数：**

参数名类型必填说明options[AudioCapturerOptions](../../types/interfaces/Interfaces (其他) (arkts-apis-audio-i).md#ZH-CN_TOPIC_0000002497445724__audiocaptureroptions8)是配置音频采集器。

**返回值：**

类型说明Promise<[AudioCapturer](../../types/interfaces/Interface (AudioCapturer).md)>

Promise对象，成功将返回音频采集器对象，异常将返回error对象：

错误码6800301：表示参数校验异常、权限校验异常或系统处理异常（具体错误查看系统日志）。

错误码6800101：表示必选参数为空或参数类型错误。

**示例：**

```ets
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_2, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
  capturerFlags: 0 // 音频采集器标志。
};

let audioCapturerOptions:audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

let audioCapturer: audio.AudioCapturer;

audio.createAudioCapturer(audioCapturerOptions).then((data) => {
  audioCapturer = data;
  console.info('AudioCapturer Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`AudioCapturer Created : ERROR : ${err}`);
});
```

[]()[]()

#### audio.createAudioLoopback20+

createAudioLoopback(mode: AudioLoopbackMode): Promise<AudioLoopback>

创建音频返听器。使用Promise异步回调。

在使用createAudioLoopback接口之前，需先通过[isAudioLoopbackSupported](../../types/interfaces/Interface (AudioStreamManager).md#ZH-CN_TOPIC_0000002497445722__isaudioloopbacksupported20)查询系统返听能力。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**需要权限：** ohos.permission.MICROPHONE

**参数：**

参数名类型必填说明mode[AudioLoopbackMode](Enums (arkts-apis-audio-e).md#ZH-CN_TOPIC_0000002529285695__audioloopbackmode20)是音频返听模式。

**返回值：**

类型说明Promise<[AudioLoopback](../../types/interfaces/Interface (AudioLoopback).md)>Promise对象，成功将返回音频返听器对象，异常将返回error对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息201Permission denied.801Unsupported API.6800101Parameter verification failed.6800104Loopback mode is unsupported.

**示例：**

```ets
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let audioLoopback: audio.AudioLoopback;

audio.createAudioLoopback(audio.AudioLoopbackMode.HARDWARE).then((data) => {
  audioLoopback = data;
  console.info('AudioLoopback Created : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`AudioLoopback Created : ERROR : ${err}`);
});
```