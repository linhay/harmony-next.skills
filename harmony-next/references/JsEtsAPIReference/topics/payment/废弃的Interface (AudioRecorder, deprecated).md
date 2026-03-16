# 废弃的Interface (AudioRecorder, deprecated)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder](../../types/interfaces/Interface (AVRecorder).md)替代。

音频录制管理类，用于录制音频媒体。在调用AudioRecorder的方法前，需要先通过[createAudioRecorder()](../misc/Functions.md#ZH-CN_TOPIC_0000002529445861__mediacreateaudiorecorderdeprecated) 构建一个AudioRecorder实例。

#### 导入模块

```ets
import { media } from '@kit.MediaKit';
```

#### prepare(deprecated)

prepare(config: AudioRecorderConfig): void

录音准备。

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.prepare](../../types/interfaces/Interface (AVRecorder).md#ZH-CN_TOPIC_0000002529445863__prepare9)替代。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

参数名类型必填说明config[AudioRecorderConfig](../../types/interfaces/Interfaces (其他).md#ZH-CN_TOPIC_0000002497605902__audiorecorderconfigdeprecated)是配置录音的相关参数，包括音频输出URI、编码格式、采样率、声道数、输出格式等。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息201permission denied

**示例：**

```ets
let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://1',       // 文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130},
};
audioRecorder.on('prepare', () => {    //设置'prepare'事件回调。
  console.info('prepare called');
});
audioRecorder.prepare(audioRecorderConfig);
```

#### start(deprecated)

start(): void

开始录制，需在'prepare'事件成功触发后，才能调用start方法。

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.start](../../types/interfaces/Interface (AVRecorder).md#ZH-CN_TOPIC_0000002529445863__start9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ets
audioRecorder.on('start', () => {    //设置'start'事件回调。
  console.info('audio recorder start called');
});
audioRecorder.start();
```

#### pause(deprecated)

pause():void

暂停录制，需要在'start'事件成功触发后，才能调用pause方法。

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.pause](../../types/interfaces/Interface (AVRecorder).md#ZH-CN_TOPIC_0000002529445863__pause9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ets
audioRecorder.on('pause', () => {    //设置'pause'事件回调。
  console.info('audio recorder pause called');
});
audioRecorder.pause();
```

#### resume(deprecated)

resume():void

恢复录制，需要在'pause'事件成功触发后，才能调用resume方法。

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.resume](../../types/interfaces/Interface (AVRecorder).md#ZH-CN_TOPIC_0000002529445863__resume9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ets
audioRecorder.on('resume', () => {    //设置'resume'事件回调。
  console.info('audio recorder resume called');
});
audioRecorder.resume();
```

#### stop(deprecated)

stop(): void

停止录音。

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.stop](../../types/interfaces/Interface (AVRecorder).md#ZH-CN_TOPIC_0000002529445863__stop9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ets
audioRecorder.on('stop', () => {    //设置'stop'事件回调。
  console.info('audio recorder stop called');
});
audioRecorder.stop();
```

#### release(deprecated)

release(): void

释放录音资源。

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.release](../../types/interfaces/Interface (AVRecorder).md#ZH-CN_TOPIC_0000002529445863__release9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ets
audioRecorder.on('release', () => {    //设置'release'事件回调。
  console.info('audio recorder release called');
});
audioRecorder.release();
audioRecorder = undefined;
```

#### reset(deprecated)

reset(): void

重置录音。

进行重置录音之前，需要先调用stop()停止录音。重置录音之后，需要调用prepare()设置录音参数项，才能再次进行录音。

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.reset](../../types/interfaces/Interface (AVRecorder).md#ZH-CN_TOPIC_0000002529445863__reset9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ets
audioRecorder.on('reset', () => {    //设置'reset'事件回调。
  console.info('audio recorder reset called');
});
audioRecorder.reset();
```

#### on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')(deprecated)

on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void

开始订阅音频录制事件。

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.on('stateChange')](../../types/interfaces/Interface (AVRecorder).md#ZH-CN_TOPIC_0000002529445863__onstatechange9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

参数名类型必填说明typestring是

录制事件回调类型，支持的事件包括：'prepare' | 'start' | 'pause' | ’resume‘ | 'stop' | 'release' | 'reset'。

- 'prepare' ：完成prepare调用，音频录制参数设置完成，触发该事件。

- 'start' ：完成start调用，音频录制开始，触发该事件。

- 'pause': 完成pause调用，音频暂停录制，触发该事件。

- 'resume': 完成resume调用，音频恢复录制，触发该事件。

- 'stop' ：完成stop调用，音频停止录制，触发该事件。

- 'release' ：完成release调用，音频释放录制资源，触发该事件。

- 'reset'：完成reset调用，音频重置为初始状态，触发该事件。

callback()=>void是录制事件回调方法。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let audioRecorder: media.AudioRecorder = media.createAudioRecorder();  // 创建一个音频录制实例。
let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://xx',  // 文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130}
};
audioRecorder.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
  console.error(`audio error called, error: ${error}`);
});
audioRecorder.on('prepare', () => {  // 设置'prepare'事件回调。
  console.info('prepare called');
  audioRecorder.start();  // 开始录制，并触发'start'事件回调。
});
audioRecorder.on('start', () => {  // 设置'start'事件回调。
  console.info('audio recorder start called');
});
audioRecorder.on('pause', () => {  // 设置'pause'事件回调。
  console.info('audio recorder pause called');
});
audioRecorder.on('resume', () => {  // 设置'resume'事件回调。
  console.info('audio recorder resume called');
});
audioRecorder.on('stop', () => {  // 设置'stop'事件回调。
  console.info('audio recorder stop called');
});
audioRecorder.on('release', () => {  // 设置'release'事件回调。
  console.info('audio recorder release called');
});
audioRecorder.on('reset', () => {  // 设置'reset'事件回调。
  console.info('audio recorder reset called');
});
audioRecorder.prepare(audioRecorderConfig)  // 设置录制参数 ，并触发'prepare'事件回调。
```

#### on('error')(deprecated)

on(type: 'error', callback: ErrorCallback): void

开始订阅音频录制错误事件，当上报error错误事件后，用户需处理error事件，退出录制操作。

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.on('error')](../../types/interfaces/Interface (AVRecorder).md#ZH-CN_TOPIC_0000002529445863__onerror9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

参数名类型必填说明typestring是

录制错误事件回调类型'error'。

- 'error'：音频录制过程中发生错误，触发该事件。

callback[ErrorCallback](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)是录制错误事件回调方法。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 22050,
  audioSampleRate : 22050,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://xx',   // 文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130}
};
audioRecorder.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
  console.error(`audio error called, error: ${error}`);
});
audioRecorder.prepare(audioRecorderConfig);  // prepare不设置参数，触发'error'事件。
```