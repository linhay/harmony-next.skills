# Interface (AudioRenderer)

提供音频渲染的相关接口。

在使用AudioRenderer的接口之前，需先通过[createAudioRenderer](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529285689__audiocreateaudiorenderer8)获取AudioRenderer实例。

- 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 8开始支持。

#### 导入模块

```ets
import { audio } from '@kit.AudioKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

名称类型只读可选说明state8+[AudioState](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiostate8)是否音频渲染器的状态。

**示例：**

```ets
import { audio } from '@kit.AudioKit';

let state: audio.AudioState = audioRenderer.state;
```

#### getRendererInfo8+

getRendererInfo(callback: AsyncCallback<AudioRendererInfo>): void

获取当前创建的音频渲染器信息。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<[AudioRendererInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiorendererinfo8)>是回调函数。当获取音频渲染器的信息成功，err为undefined，data为获取到的音频渲染器的信息；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRendererInfo((err: BusinessError, audioRendererInfo: audio.AudioRendererInfo) => {
  if (err) {
    console.error(`Failed to get renderer info. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.`);
  }
});
```

#### getRendererInfo8+

getRendererInfo(): Promise<AudioRendererInfo>

获取当前创建的音频渲染器信息。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<[AudioRendererInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiorendererinfo8)>Promise对象，返回音频渲染器信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRendererInfo().then((audioRendererInfo: audio.AudioRendererInfo) => {
  console.info(`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get renderer info. Code: ${err.code}, message: ${err.message}`);
});
```

#### getRendererInfoSync10+

getRendererInfoSync(): AudioRendererInfo

获取当前创建的音频渲染器信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明[AudioRendererInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiorendererinfo8)返回音频渲染器信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioRendererInfo = audioRenderer.getRendererInfoSync();
  console.info(`Succeeded in getting renderer info, AudioRendererInfo: ${JSON.stringify(audioRendererInfo)}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get renderer info. Code: ${error.code}, message: ${error.message}`);
}
```

#### getStreamInfo8+

getStreamInfo(callback: AsyncCallback<AudioStreamInfo>): void

获取音频流信息。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<[AudioStreamInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiostreaminfo8)>是回调函数。当获取音频流信息成功，err为undefined，data为获取到的音频流信息；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getStreamInfo((err: BusinessError, streamInfo: audio.AudioStreamInfo) => {
  console.info('Renderer GetStreamInfo:');
  console.info(`Renderer sampling rate: ${streamInfo.samplingRate}`);
  console.info(`Renderer channel: ${streamInfo.channels}`);
  console.info(`Renderer format: ${streamInfo.sampleFormat}`);
  console.info(`Renderer encoding type: ${streamInfo.encodingType}`);
});
```

#### getStreamInfo8+

getStreamInfo(): Promise<AudioStreamInfo>

获取音频流信息。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<[AudioStreamInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiostreaminfo8)>Promise对象，返回音频流信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getStreamInfo().then((streamInfo: audio.AudioStreamInfo) => {
  console.info('Renderer GetStreamInfo:');
  console.info(`Renderer sampling rate: ${streamInfo.samplingRate}`);
  console.info(`Renderer channel: ${streamInfo.channels}`);
  console.info(`Renderer format: ${streamInfo.sampleFormat}`);
  console.info(`Renderer encoding type: ${streamInfo.encodingType}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### getStreamInfoSync10+

getStreamInfoSync(): AudioStreamInfo

获取音频流信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明[AudioStreamInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiostreaminfo8)返回音频流信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let streamInfo: audio.AudioStreamInfo = audioRenderer.getStreamInfoSync();
  console.info(`Renderer sampling rate: ${streamInfo.samplingRate}`);
  console.info(`Renderer channel: ${streamInfo.channels}`);
  console.info(`Renderer format: ${streamInfo.sampleFormat}`);
  console.info(`Renderer encoding type: ${streamInfo.encodingType}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

#### getAudioStreamId9+

getAudioStreamId(callback: AsyncCallback<number>): void

获取音频流id。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当获取音频流id成功，err为undefined，data为获取到的音频流id；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioStreamId((err: BusinessError, streamId: number) => {
  console.info(`Renderer GetStreamId: ${streamId}`);
});
```

#### getAudioStreamId9+

getAudioStreamId(): Promise<number>

获取音频流id。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<number>Promise对象，返回音频流id。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioStreamId().then((streamId: number) => {
  console.info(`Renderer getAudioStreamId: ${streamId}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### getAudioStreamIdSync10+

getAudioStreamIdSync(): number

获取音频流id。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明number返回音频流id。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let streamId: number = audioRenderer.getAudioStreamIdSync();
  console.info(`Renderer getAudioStreamIdSync: ${streamId}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

#### setAudioEffectMode10+

setAudioEffectMode(mode: AudioEffectMode, callback: AsyncCallback<void>): void

设置当前音效模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明mode[AudioEffectMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audioeffectmode10)是音效模式。callbackAsyncCallback<void>是回调函数。当设置当前音效模式成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setAudioEffectMode(audio.AudioEffectMode.EFFECT_DEFAULT, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set params');
  } else {
    console.info('Callback invoked to indicate a successful audio effect mode setting.');
  }
});
```

#### setAudioEffectMode10+

setAudioEffectMode(mode: AudioEffectMode): Promise<void>

设置当前音效模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明mode[AudioEffectMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audioeffectmode10)是音效模式。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setAudioEffectMode(audio.AudioEffectMode.EFFECT_DEFAULT).then(() => {
  console.info('setAudioEffectMode SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### getAudioEffectMode10+

getAudioEffectMode(callback: AsyncCallback<AudioEffectMode>): void

获取当前音效模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<[AudioEffectMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audioeffectmode10)>是回调函数。当获取当前音效模式成功，err为undefined，data为获取到的当前音效模式；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioEffectMode((err: BusinessError, effectMode: audio.AudioEffectMode) => {
  if (err) {
    console.error('Failed to get params');
  } else {
    console.info(`getAudioEffectMode: ${effectMode}`);
  }
});
```

#### getAudioEffectMode10+

getAudioEffectMode(): Promise<AudioEffectMode>

获取当前音效模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<[AudioEffectMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audioeffectmode10)>Promise对象，返回当前音效模式。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioEffectMode().then((effectMode: audio.AudioEffectMode) => {
  console.info(`getAudioEffectMode: ${effectMode}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### start8+

start(callback: AsyncCallback<void>): void

启动音频渲染器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是

回调函数。当启动音频渲染器成功，err为undefined，否则为错误对象。异常将返回error对象：

错误码6800301：表示包含状态检查异常、焦点抢占失败、系统处理异常（具体错误查看系统日志）。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.start((err: BusinessError) => {
  if (err) {
    console.error('Renderer start failed.');
  } else {
    console.info('Renderer start success.');
  }
});
```

#### start8+

start(): Promise<void>

启动音频渲染器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<void>

Promise对象，成功表示启动音频渲染器成功。异常将返回error对象：

错误码6800301：表示包含状态检查异常、焦点抢占失败、系统处理异常（具体错误查看系统日志）。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.start().then(() => {
  console.info('Renderer started');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### pause8+

pause(callback: AsyncCallback<void>): void

暂停音频渲染。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当暂停渲染成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.pause((err: BusinessError) => {
  if (err) {
    console.error('Renderer pause failed');
  } else {
    console.info('Renderer paused.');
  }
});
```

#### pause8+

pause(): Promise<void>

暂停音频渲染。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.pause().then(() => {
  console.info('Renderer paused');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### drain8+

drain(callback: AsyncCallback<void>): void

检查缓冲区是否已被耗尽。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当检查缓冲区是否已被耗尽成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.drain((err: BusinessError) => {
  if (err) {
    console.error('Renderer drain failed');
  } else {
    console.info('Renderer drained.');
  }
});
```

#### drain8+

drain(): Promise<void>

检查缓冲区是否已被耗尽。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.drain().then(() => {
  console.info('Renderer drained successfully');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### flush11+

flush(): Promise<void>

清空缓冲区（[AudioState](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiostate8)为STATE_RUNNING、STATE_PAUSED、STATE_STOPPED状态下可用）。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800103Operation not permit at current state. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.flush().then(() => {
  console.info('Renderer flushed successfully');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### stop8+

stop(callback: AsyncCallback<void>): void

停止音频渲染。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当停止渲染成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.stop((err: BusinessError) => {
  if (err) {
    console.error('Renderer stop failed');
  } else {
    console.info('Renderer stopped.');
  }
});
```

#### stop8+

stop(): Promise<void>

停止音频渲染。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.stop().then(() => {
  console.info('Renderer stopped successfully');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### release8+

release(callback: AsyncCallback<void>): void

释放音频渲染器。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当释放音频渲染器成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.release((err: BusinessError) => {
  if (err) {
    console.error('Renderer release failed');
  } else {
    console.info('Renderer released.');
  }
});
```

#### release8+

release(): Promise<void>

释放音频渲染器。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.release().then(() => {
  console.info('Renderer released successfully');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### getAudioTime8+

getAudioTime(callback: AsyncCallback<number>): void

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当获取时间戳成功，err为undefined，data为获取到的时间戳；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioTime((err: BusinessError, timestamp: number) => {
  console.info(`Current timestamp: ${timestamp}`);
});
```

#### getAudioTime8+

getAudioTime(): Promise<number>

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<number>Promise对象，返回时间戳。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioTime().then((timestamp: number) => {
  console.info(`Current timestamp: ${timestamp}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### getAudioTimeSync10+

getAudioTimeSync(): number

获取当前播放位置的时间戳（从1970年1月1日开始），单位为纳秒。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明number返回时间戳。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let timestamp: number = audioRenderer.getAudioTimeSync();
  console.info(`Current timestamp: ${timestamp}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

#### getAudioTimestampInfo19+

getAudioTimestampInfo(): Promise<AudioTimestampInfo>

获取输出音频流时间戳和位置信息，适配倍速接口。使用Promise异步回调。

获取输出音频流时间戳和位置信息，通常用于进行音画同步对齐。

注意，当实际播放位置（framePosition）为0时，时间戳（timestamp）是固定值，直到流真正跑起来时才会更新。当调用Flush接口时实际播放位置也会被重置。

当音频流路由（route）变化时，例如设备变化或者输出类型变化时，播放位置也会被重置，但此时时间戳仍会持续增长。推荐当实际播放位置和时间戳的变化稳定后再使用该接口获取的值。该接口适配倍速接口，例如当播放速度设置为2倍时，播放位置的增长速度也会返回为正常的2倍。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<[AudioTimestampInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiotimestampinfo19)>Promise对象，返回音频流时间戳和当前数据帧位置信息。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800103Operation not permit at current state.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getAudioTimestampInfo().then((audioTimestampInfo: audio.AudioTimestampInfo) => {
  console.info(`Current timestamp: ${audioTimestampInfo.timestamp}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### getAudioTimestampInfoSync19+

getAudioTimestampInfoSync(): AudioTimestampInfo

获取音频流时间戳和当前数据帧位置信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明[AudioTimestampInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiotimestampinfo19)返回音频流时间戳和当前数据帧位置信息。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800103Operation not permit at current state.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioTimestampInfo: audio.AudioTimestampInfo = audioRenderer.getAudioTimestampInfoSync();
  console.info(`Current timestamp: ${audioTimestampInfo.timestamp}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

#### getBufferSize8+

getBufferSize(callback: AsyncCallback<number>): void

获取音频渲染器的最小缓冲区大小。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当获取音频渲染器的最小缓冲区大小成功，err为undefined，data为获取到的最小缓冲区大小；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let bufferSize: number;

audioRenderer.getBufferSize((err: BusinessError, data: number) => {
  if (err) {
    console.error('getBufferSize error');
  } else {
    console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
    bufferSize = data;
  }
});
```

#### getBufferSize8+

getBufferSize(): Promise<number>

获取音频渲染器的最小缓冲区大小。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<number>Promise对象，返回缓冲区大小。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let bufferSize: number;

audioRenderer.getBufferSize().then((data: number) => {
  console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
  bufferSize = data;
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}`);
});
```

#### getBufferSizeSync10+

getBufferSizeSync(): number

获取音频渲染器的最小缓冲区大小。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明number返回缓冲区大小。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let bufferSize: number = 0;

try {
  bufferSize = audioRenderer.getBufferSizeSync();
  console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${bufferSize}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${error}`);
}
```

#### setSpeed11+

setSpeed(speed: number): void

设置播放倍速。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明speednumber是设置播放的倍速值（倍速范围：0.25-4.0）。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
audioRenderer.setSpeed(1.5);
```

#### getSpeed11+

getSpeed(): number

获取播放倍速。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明number返回播放的倍速值。

**示例：**

```ets
let speed = audioRenderer.getSpeed();
```

#### setInterruptMode9+

setInterruptMode(mode: InterruptMode): Promise<void>

设置应用的焦点模型。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

参数名类型必填说明mode[InterruptMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__interruptmode9)是焦点模型。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let mode = 0;

audioRenderer.setInterruptMode(mode).then(() => {
  console.info('setInterruptMode Success!');
}).catch((err: BusinessError) => {
  console.error(`setInterruptMode Fail: ${err}`);
});
```

#### setInterruptMode9+

setInterruptMode(mode: InterruptMode, callback: AsyncCallback<void>): void

设置应用的焦点模型。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

参数名类型必填说明mode[InterruptMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__interruptmode9)是焦点模型。callbackAsyncCallback<void>是回调函数。当设置应用的焦点模型成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let mode = 1;

audioRenderer.setInterruptMode(mode, (err: BusinessError) => {
  if(err){
    console.error(`setInterruptMode Fail: ${err}`);
  }
  console.info('setInterruptMode Success!');
});
```

#### setInterruptModeSync10+

setInterruptModeSync(mode: InterruptMode): void

设置应用的焦点模型。同步设置。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

参数名类型必填说明mode[InterruptMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__interruptmode9)是焦点模型。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  audioRenderer.setInterruptModeSync(0);
  console.info('setInterruptMode Success!');
} catch (err) {
  let error = err as BusinessError;
  console.error(`setInterruptMode Fail: ${error}`);
}
```

#### setVolume9+

setVolume(volume: number): Promise<void>

设置音频流的音量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明volumenumber是音量值范围为[0.0, 1.0]。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setVolume(0.5).then(() => {
  console.info('setVolume Success!');
}).catch((err: BusinessError) => {
  console.error(`setVolume Fail: ${err}`);
});
```

#### setVolume9+

setVolume(volume: number, callback: AsyncCallback<void>): void

设置音频流的音量。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明volumenumber是音量值范围为[0.0, 1.0]。callbackAsyncCallback<void>是回调函数。当设置应用的音量成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setVolume(0.5, (err: BusinessError) => {
  if(err){
    console.error(`setVolume Fail: ${err}`);
    return;
  }
  console.info('setVolume Success!');
});
```

#### getVolume12+

getVolume(): number

获取音频流的音量。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明number返回音量大小，音量值范围为[0.0, 1.0]。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getVolume();
  console.info(`Indicate that the volume is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume, error ${error}.`);
}
```

#### getMinStreamVolume10+

getMinStreamVolume(callback: AsyncCallback<number>): void

获取音频流的最小音量。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当获取音频流的最小音量成功，err为undefined，data为获取到的应用基于音频流的最小音量（音量范围[0, 1]）；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMinStreamVolume((err: BusinessError, minVolume: number) => {
  if (err) {
    console.error(`getMinStreamVolume error: ${err}`);
  } else {
    console.info(`getMinStreamVolume Success! ${minVolume}`);
  }
});
```

#### getMinStreamVolume10+

getMinStreamVolume(): Promise<number>

获取音频流的最小音量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<number>Promise对象，返回音频流最小音量（音量范围[0, 1]）。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMinStreamVolume().then((value: number) => {
  console.info(`Get min stream volume Success! ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Get min stream volume Fail: ${err}`);
});
```

#### getMinStreamVolumeSync10+

getMinStreamVolumeSync(): number

获取音频流的最小音量。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明number返回音频流最小音量（音量范围[0, 1]）。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getMinStreamVolumeSync();
  console.info(`Get min stream volume Success! ${value}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get min stream volume Fail: ${error}`);
}
```

#### getMaxStreamVolume10+

getMaxStreamVolume(callback: AsyncCallback<number>): void

获取音频流的最大音量。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当获取音频流的最大音量成功，err为undefined，data为获取到的应用基于音频流的最大音量（音量范围[0, 1]）；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMaxStreamVolume((err: BusinessError, maxVolume: number) => {
  if (err) {
    console.error(`getMaxStreamVolume Fail: ${err}`);
  } else {
    console.info(`getMaxStreamVolume Success! ${maxVolume}`);
  }
});
```

#### getMaxStreamVolume10+

getMaxStreamVolume(): Promise<number>

获取音频流的最大音量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<number>Promise对象，返回音频流最大音量（音量范围[0, 1]）。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getMaxStreamVolume().then((value: number) => {
  console.info(`Get max stream volume Success! ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Get max stream volume Fail: ${err}`);
});
```

#### getMaxStreamVolumeSync10+

getMaxStreamVolumeSync(): number

获取音频流的最大音量。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明number返回音频流最大音量（音量范围[0, 1]）。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getMaxStreamVolumeSync();
  console.info(`Get max stream volume Success! ${value}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get max stream volume Fail: ${error}`);
}
```

#### getUnderflowCount10+

getUnderflowCount(callback: AsyncCallback<number>): void

获取当前播放音频流的欠载音频帧数量。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。当获取当前播放音频流的欠载音频帧数量成功，err为undefined，data为获取到的当前播放音频流的欠载音频帧数量；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getUnderflowCount((err: BusinessError, underflowCount: number) => {
  if (err) {
    console.error(`getUnderflowCount Fail: ${err}`);
  } else {
    console.info(`getUnderflowCount Success! ${underflowCount}`);
  }
});
```

#### getUnderflowCount10+

getUnderflowCount(): Promise<number>

获取当前播放音频流的欠载音频帧数量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<number>Promise对象，返回音频流的欠载音频帧数量。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getUnderflowCount().then((value: number) => {
  console.info(`Get underflow count Success! ${value}`);
}).catch((err: BusinessError) => {
  console.error(`Get underflow count Fail: ${err}`);
});
```

#### getUnderflowCountSync10+

getUnderflowCountSync(): number

获取当前播放音频流的欠载音频帧数量，同步返回数据。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明number返回音频流的欠载音频帧数量。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioRenderer.getUnderflowCountSync();
  console.info(`Get underflow count Success! ${value}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get underflow count Fail: ${error}`);
}
```

#### getCurrentOutputDevices10+

getCurrentOutputDevices(callback: AsyncCallback<AudioDeviceDescriptors>): void

获取音频流输出设备信息。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

参数名类型必填说明callbackAsyncCallback<[AudioDeviceDescriptors](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)>是回调函数。当获取音频流输出设备信息成功，err为undefined，data为获取到的音频流输出设备信息；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getCurrentOutputDevices((err: BusinessError, deviceInfo: audio.AudioDeviceDescriptors) => {
  if (err) {
    console.error(`getCurrentOutputDevices Fail: ${err}`);
  } else {
    for (let i = 0; i < deviceInfo.length; i++) {
      console.info(`DeviceInfo id: ${deviceInfo[i].id}`);
      console.info(`DeviceInfo type: ${deviceInfo[i].deviceType}`);
      console.info(`DeviceInfo role: ${deviceInfo[i].deviceRole}`);
      console.info(`DeviceInfo name: ${deviceInfo[i].name}`);
      console.info(`DeviceInfo address: ${deviceInfo[i].address}`);
      console.info(`DeviceInfo samplerate: ${deviceInfo[i].sampleRates[0]}`);
      console.info(`DeviceInfo channelcount: ${deviceInfo[i].channelCounts[0]}`);
      console.info(`DeviceInfo channelmask: ${deviceInfo[i].channelMasks[0]}`);
    }
  }
});
```

#### getCurrentOutputDevices10+

getCurrentOutputDevices(): Promise<AudioDeviceDescriptors>

获取音频流输出设备信息。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

类型说明Promise<[AudioDeviceDescriptors](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)>Promise对象，返回音频流的输出设备信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getCurrentOutputDevices().then((deviceInfo: audio.AudioDeviceDescriptors) => {
  for (let i = 0; i < deviceInfo.length; i++) {
    console.info(`DeviceInfo id: ${deviceInfo[i].id}`);
    console.info(`DeviceInfo type: ${deviceInfo[i].deviceType}`);
    console.info(`DeviceInfo role: ${deviceInfo[i].deviceRole}`);
    console.info(`DeviceInfo name: ${deviceInfo[i].name}`);
    console.info(`DeviceInfo address: ${deviceInfo[i].address}`);
    console.info(`DeviceInfo samplerate: ${deviceInfo[i].sampleRates[0]}`);
    console.info(`DeviceInfo channelcount: ${deviceInfo[i].channelCounts[0]}`);
    console.info(`DeviceInfo channelmask: ${deviceInfo[i].channelMasks[0]}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Get current output devices Fail: ${err}`);
});
```

#### getCurrentOutputDevicesSync10+

getCurrentOutputDevicesSync(): AudioDeviceDescriptors

获取音频流输出设备信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

类型说明[AudioDeviceDescriptors](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)返回音频流的输出设备信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let deviceInfo: audio.AudioDeviceDescriptors = audioRenderer.getCurrentOutputDevicesSync();
  for (let i = 0; i < deviceInfo.length; i++) {
    console.info(`DeviceInfo id: ${deviceInfo[i].id}`);
    console.info(`DeviceInfo type: ${deviceInfo[i].deviceType}`);
    console.info(`DeviceInfo role: ${deviceInfo[i].deviceRole}`);
    console.info(`DeviceInfo name: ${deviceInfo[i].name}`);
    console.info(`DeviceInfo address: ${deviceInfo[i].address}`);
    console.info(`DeviceInfo samplerate: ${deviceInfo[i].sampleRates[0]}`);
    console.info(`DeviceInfo channelcount: ${deviceInfo[i].channelCounts[0]}`);
    console.info(`DeviceInfo channelmask: ${deviceInfo[i].channelMasks[0]}`);
  }
} catch (err) {
  let error = err as BusinessError;
  console.error(`Get current output devices Fail: ${error}`);
}
```

#### setChannelBlendMode11+

setChannelBlendMode(mode: ChannelBlendMode): void

设置单双声道混合模式。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明mode[ChannelBlendMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__channelblendmode11)是声道混合模式类型。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.6800103Operation not permit at current state.

**示例：**

```ets
let mode = audio.ChannelBlendMode.MODE_DEFAULT;

audioRenderer.setChannelBlendMode(mode);
console.info(`BlendMode: ${mode}`);
```

#### setVolumeWithRamp11+

setVolumeWithRamp(volume: number, duration: number): void

在指定时间范围内设置音量渐变模式。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明volumenumber是渐变目标音量值，音量范围为[0.0, 1.0]。durationnumber是渐变持续时间，单位为ms。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
let volume = 0.5;
let duration = 1000;

audioRenderer.setVolumeWithRamp(volume, duration);
console.info(`setVolumeWithRamp: ${volume}`);
```

#### setSilentModeAndMixWithOthers12+

setSilentModeAndMixWithOthers(on: boolean): void

设置静音并发播放模式。

当设置为true，打开静音并发播放模式，系统将让此音频流静音播放，并且不会打断其他音频流。设置为false，将关闭静音并发播放，音频流可根据系统焦点策略抢占焦点。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明onboolean是打开/关闭静音并发播放模式。true表示设置当前播放的音频流静音播放，并且不会打断其它音频流播放。false表示取消当前播放的音频流静音播放，音频流可根据系统焦点策略抢占焦点。

**示例：**

```ets
audioRenderer.setSilentModeAndMixWithOthers(true);
```

#### getSilentModeAndMixWithOthers12+

getSilentModeAndMixWithOthers(): boolean

获取静音并发播放模式。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明boolean静音并发播放模式状态。返回true表示打开，返回false表示关闭。

**示例：**

```ets
let on = audioRenderer.getSilentModeAndMixWithOthers();
```

#### setDefaultOutputDevice12+

setDefaultOutputDevice(deviceType: DeviceType): Promise<void>

设置默认发声设备。使用Promise异步回调。

- 本接口仅适用于[StreamUsage](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)为语音消息、VoIP语音通话或者VoIP视频通话的场景，支持听筒、扬声器和系统默认设备。
- 本接口允许在AudioRenderer创建后随时调用，系统会记录应用设置的默认本机内置发声设备。应用启动播放时，若外接设备如蓝牙耳机或有线耳机已接入，系统优先从外接设备发声；否则，系统遵循应用设置的默认本机内置发声设备。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明deviceType[DeviceType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__devicetype)是

设备类型。

仅支持以下设备：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.6800103Operation not permit at current state.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 本接口允许在AudioRenderer创建以后的任何时间被调用。
// 未播放时调用，系统会记录应用设置的默认本机内置发声设备，当应用启动播放时从设置的默认本机内置发声设备发声。
// 正在播放时调用，在没有外接设备如蓝牙耳机/有线耳机，系统会立即切换到设置的默认本机内置发声设备发声；否则系统会先记录应用设置的默认本机内置发声设备，等外接设备移除后再切换到设置的默认本机内置发声设备发声。
audioRenderer.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('setDefaultOutputDevice Success!');
}).catch((err: BusinessError) => {
  console.error(`setDefaultOutputDevice Fail: ${err}`);
});
```

#### on('audioInterrupt')9+

on(type: 'audioInterrupt', callback: Callback<InterruptEvent>): void

监听音频中断事件（当音频焦点发生变化时触发）。使用callback异步回调。

AudioRenderer对象在start事件时获取焦点，在pause、stop等事件时释放焦点，无需开发者主动申请。

调用此方法后，如果AudioRenderer对象获取焦点失败或发生中断事件（如被其他音频打断等），会收到[InterruptEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__interruptevent9)。建议应用根据InterruptEvent的信息进行进一步处理。更多信息请参阅文档[音频焦点和音频会话介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-concurrency)。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'audioInterrupt'，当音频焦点状态发生变化时，触发该事件。callbackCallback<[InterruptEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__interruptevent9)>是回调函数，返回中断事件信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
import { audio } from '@kit.AudioKit';

let isPlaying: boolean = false; // 标识符，表示是否正在渲染。
let isDucked: boolean = false; // 标识符，表示是否被降低音量。

audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent) => {
  // 在发生音频打断事件时，audioRenderer收到interruptEvent回调，此处根据其内容做相应处理。
  // 1. 可选：读取interruptEvent.forceType的类型，判断系统是否已强制执行相应操作。
  // 注意：默认焦点策略下，INTERRUPT_HINT_RESUME为INTERRUPT_SHARE类型，其余hintType均为INTERRUPT_FORCE类型。因此对forceType可不做判断。
  // 2. 必选：读取interruptEvent.hintType的类型，做出相应的处理。
  if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
    // 音频焦点事件已由系统强制执行，应用需更新自身状态及显示内容等。
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
        // 音频流已被暂停，临时失去焦点，待可重获焦点时会收到resume对应的interruptEvent。
        console.info('Force paused. Update playing status and stop writing');
        isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_STOP:
        // 音频流已被停止，永久失去焦点，若想恢复渲染，需用户主动触发。
        console.info('Force stopped. Update playing status and stop writing');
        isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_DUCK:
        // 音频流已被降低音量渲染。
        console.info('Force ducked. Update volume status');
        isDucked = true; // 简化处理，代表应用更新音量状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
        // 音频流已被恢复正常音量渲染。
        console.info('Force unducked. Update volume status');
        isDucked = false; // 简化处理，代表应用更新音量状态的若干操作。
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
    // 音频焦点事件需由应用进行操作，应用可以自主选择如何处理该事件，建议应用遵从InterruptHint提示处理。
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_RESUME:
        // 建议应用继续渲染（说明音频流此前被强制暂停，临时失去焦点，现在可以恢复渲染）。
        // 由于INTERRUPT_HINT_RESUME操作需要应用主动执行，系统无法强制，故INTERRUPT_HINT_RESUME事件一定为INTERRUPT_SHARE类型。
        console.info('Resume force paused renderer or ignore');
        // 若选择继续渲染，需在此处主动执行开始渲染的若干操作。
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  }
});
```

#### off('audioInterrupt')18+

off(type: 'audioInterrupt', callback?: Callback<InterruptEvent>): void

取消监听音频中断事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'audioInterrupt'，当取消监听音频中断事件时，触发该事件。callbackCallback<[InterruptEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__interruptevent9)>否回调函数，返回中断事件信息。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
// 取消该事件的所有监听。
audioRenderer.off('audioInterrupt');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let isPlaying: boolean; // 标识符，表示是否正在渲染。
let isDucked: boolean; // 标识符，表示是否被降低音量。

let audioInterruptCallback = (interruptEvent: audio.InterruptEvent) => {
  // 在发生音频打断事件时，audioRenderer收到interruptEvent回调，此处根据其内容做相应处理。
  // 1. 可选：读取interruptEvent.forceType的类型，判断系统是否已强制执行相应操作。
  // 注意：默认焦点策略下，INTERRUPT_HINT_RESUME为INTERRUPT_SHARE类型，其余hintType均为INTERRUPT_FORCE类型。因此对forceType可不做判断。
  // 2. 必选：读取interruptEvent.hintType的类型，做出相应的处理。
  if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_FORCE) {
    // 音频焦点事件已由系统强制执行，应用需更新自身状态及显示内容等。
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
        // 音频流已被暂停，临时失去焦点，待可重获焦点时会收到resume对应的interruptEvent。
        console.info('Force paused. Update playing status and stop writing');
        isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_STOP:
        // 音频流已被停止，永久失去焦点，若想恢复渲染，需用户主动触发。
        console.info('Force stopped. Update playing status and stop writing');
        isPlaying = false; // 简化处理，代表应用切换至暂停状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_DUCK:
        // 音频流已被降低音量渲染。
        console.info('Force ducked. Update volume status');
        isDucked = true; // 简化处理，代表应用更新音量状态的若干操作。
        break;
      case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
        // 音频流已被恢复正常音量渲染。
        console.info('Force unducked. Update volume status');
        isDucked = false; // 简化处理，代表应用更新音量状态的若干操作。
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  } else if (interruptEvent.forceType == audio.InterruptForceType.INTERRUPT_SHARE) {
    // 音频焦点事件需由应用进行操作，应用可以自主选择如何处理该事件，建议应用遵从InterruptHint提示处理。
    switch (interruptEvent.hintType) {
      case audio.InterruptHint.INTERRUPT_HINT_RESUME:
        // 建议应用继续渲染（说明音频流此前被强制暂停，临时失去焦点，现在可以恢复渲染）。
        // 由于INTERRUPT_HINT_RESUME操作需要应用主动执行，系统无法强制，故INTERRUPT_HINT_RESUME事件一定为INTERRUPT_SHARE类型。
        console.info('Resume force paused renderer or ignore');
        // 若选择继续渲染，需在此处主动执行开始渲染的若干操作。
        break;
      default:
        console.info('Invalid interruptEvent');
        break;
    }
  }
};

audioRenderer.on('audioInterrupt', audioInterruptCallback);

audioRenderer.off('audioInterrupt', audioInterruptCallback);
```

#### on('markReach')8+

on(type: 'markReach', frame: number, callback: Callback<number>): void

监听标记到达事件（当渲染的帧数到达frame参数的值时触发，仅调用一次）。使用callback异步回调。

如果将frame设置为100，当渲染帧数到达第100帧时，系统将上报信息。

**系统能力:** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'markReach'，当渲染的帧数到达frame参数的值时，触发该事件。framenumber是触发事件的帧数。该值必须大于0。callbackCallback<number>是回调函数，返回frame参数的值。

**示例：**

```ets
audioRenderer.on('markReach', 1000, (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
});
```

#### off('markReach')8+

off(type: 'markReach', callback?: Callback<number>): void

取消监听标记到达事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'markReach'，当取消监听标记到达事件时，触发该事件。callback18+Callback<number>否回调函数，返回frame参数的值。

**示例：**

```ets
// 取消该事件的所有监听。
audioRenderer.off('markReach');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let markReachCallback = (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
};

audioRenderer.on('markReach', 1000, markReachCallback);

audioRenderer.off('markReach', markReachCallback);
```

#### on('periodReach')8+

on(type: 'periodReach', frame: number, callback: Callback<number>): void

监听标记到达事件（每当渲染的帧数达到frame参数的值时触发，即按周期上报信息）。使用callback异步回调。

如果将frame设置为10，每渲染10帧数据均会上报信息（例如：第10帧、第20帧、第30帧......）。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'periodReach'，当渲染的帧数达到frame参数的值时，触发该事件。framenumber是触发事件的帧数。该值必须大于 0。callbackCallback<number>是回调函数，返回frame参数的值。

**示例：**

```ets
audioRenderer.on('periodReach', 1000, (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
});
```

#### off('periodReach')8+

off(type: 'periodReach', callback?: Callback<number>): void

取消监听标记到达事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'periodReach'，当取消监听标记到达事件时，触发该事件。callback18+Callback<number>否回调函数，返回frame参数的值。

**示例：**

```ets
// 取消该事件的所有监听。
audioRenderer.off('periodReach');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let periodReachCallback = (position: number) => {
  if (position == 1000) {
    console.info('ON Triggered successfully');
  }
};

audioRenderer.on('periodReach', 1000, periodReachCallback);

audioRenderer.off('periodReach', periodReachCallback);
```

#### on('stateChange')8+

on(type: 'stateChange', callback: Callback<AudioState>): void

监听状态变化事件（当AudioRenderer的状态发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'stateChange'，当AudioRenderer的状态发生变化时，触发该事件。callbackCallback<[AudioState](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiostate8)>是回调函数，返回当前音频的状态。

**示例：**

```ets
audioRenderer.on('stateChange', (state: audio.AudioState) => {
  if (state == 1) {
    console.info('audio renderer state is: STATE_PREPARED');
  }
  if (state == 2) {
    console.info('audio renderer state is: STATE_RUNNING');
  }
});
```

#### off('stateChange')18+

off(type: 'stateChange', callback?: Callback<AudioState>): void

取消监听到达标记事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'stateChange'，当取消监听到达标记事件时，触发该事件。callbackCallback<[AudioState](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiostate8)>否回调函数，返回当前音频的状态。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
// 取消该事件的所有监听。
audioRenderer.off('stateChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let stateChangeCallback = (state: audio.AudioState) => {
  if (state == 1) {
    console.info('audio renderer state is: STATE_PREPARED');
  }
  if (state == 2) {
    console.info('audio renderer state is: STATE_RUNNING');
  }
};

audioRenderer.on('stateChange', stateChangeCallback);

audioRenderer.off('stateChange', stateChangeCallback);
```

#### on('outputDeviceChange')10+

on(type: 'outputDeviceChange', callback: Callback<AudioDeviceDescriptors>): void

监听音频输出设备变化事件（当音频输出设备发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'outputDeviceChange'，当音频输出设备发生变化时，触发该事件。callbackCallback<[AudioDeviceDescriptors](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)>是回调函数，返回当前音频流的输出设备描述信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
audioRenderer.on('outputDeviceChange', (deviceInfo: audio.AudioDeviceDescriptors) => {
  console.info(`DeviceInfo id: ${deviceInfo[0].id}`);
  console.info(`DeviceInfo name: ${deviceInfo[0].name}`);
  console.info(`DeviceInfo address: ${deviceInfo[0].address}`);
});
```

#### off('outputDeviceChange')10+

off(type: 'outputDeviceChange', callback?: Callback<AudioDeviceDescriptors>): void

取消监听音频输出设备变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'outputDeviceChange'，当取消监听音频输出设备变化事件时，触发该事件。callbackCallback<[AudioDeviceDescriptors](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors)>否回调函数，返回当前音频流的输出设备描述信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
// 取消该事件的所有监听。
audioRenderer.off('outputDeviceChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let outputDeviceChangeCallback = (deviceInfo: audio.AudioDeviceDescriptors) => {
  console.info(`DeviceInfo id: ${deviceInfo[0].id}`);
  console.info(`DeviceInfo name: ${deviceInfo[0].name}`);
  console.info(`DeviceInfo address: ${deviceInfo[0].address}`);
};

audioRenderer.on('outputDeviceChange', outputDeviceChangeCallback);

audioRenderer.off('outputDeviceChange', outputDeviceChangeCallback);
```

#### on('outputDeviceChangeWithInfo')11+

on(type: 'outputDeviceChangeWithInfo', callback: Callback<AudioStreamDeviceChangeInfo>): void

监听音频流输出设备变化及原因事件（当音频输出设备发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'outputDeviceChangeWithInfo'，当音频输出设备发生变化时，触发该事件。callbackCallback<[AudioStreamDeviceChangeInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiostreamdevicechangeinfo11)>是回调函数，返回当前音频流的输出设备描述信息及变化原因。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
audioRenderer.on('outputDeviceChangeWithInfo', (deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
  console.info(`DeviceInfo id: ${deviceChangeInfo.devices[0].id}`);
  console.info(`DeviceInfo name: ${deviceChangeInfo.devices[0].name}`);
  console.info(`DeviceInfo address: ${deviceChangeInfo.devices[0].address}`);
  console.info(`Device change reason: ${deviceChangeInfo.changeReason}`);
});
```

#### off('outputDeviceChangeWithInfo')11+

off(type: 'outputDeviceChangeWithInfo', callback?: Callback<AudioStreamDeviceChangeInfo>): void

取消监听音频流输出设备变化及原因事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'outputDeviceChangeWithInfo'，当取消监听音频流输出设备变化及原因事件时，触发该事件。callbackCallback<[AudioStreamDeviceChangeInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiostreamdevicechangeinfo11)>否回调函数，返回当前音频流的输出设备描述信息及变化原因。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
// 取消该事件的所有监听。
audioRenderer.off('outputDeviceChangeWithInfo');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let outputDeviceChangeWithInfoCallback = (deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
  console.info(`DeviceInfo id: ${deviceChangeInfo.devices[0].id}`);
  console.info(`DeviceInfo name: ${deviceChangeInfo.devices[0].name}`);
  console.info(`DeviceInfo address: ${deviceChangeInfo.devices[0].address}`);
  console.info(`Device change reason: ${deviceChangeInfo.changeReason}`);
};

audioRenderer.on('outputDeviceChangeWithInfo', outputDeviceChangeWithInfoCallback);

audioRenderer.off('outputDeviceChangeWithInfo', outputDeviceChangeWithInfoCallback);
```

#### on('writeData')11+

on(type: 'writeData', callback: AudioRendererWriteDataCallback): void

监听音频数据写入回调事件（当需要写入音频数据时触发），使用 callback 方式返回结果。

回调函数仅用来写入音频数据，请勿在回调函数中调用AudioRenderer相关接口。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'writeData'，当需要写入音频数据时，触发该事件。callback[AudioRendererWriteDataCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605704__audiorendererwritedatacallback12)是

回调函数，入参代表应用接收待写入的数据缓冲区。

API version 11 不支持返回回调结果，从 API version 12 开始支持返回回调结果[AudioDataCallbackResult](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiodatacallbackresult12)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import {fileIo as fs} from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

class Options {
  offset?: number;
  length?: number;
}

let bufferSize: number = 0;
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.cacheDir;
// 此处仅作示例，实际使用时需要将文件替换为应用要播放的PCM文件。
let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
let writeDataCallback = (buffer: ArrayBuffer) => {
  let options: Options = {
    offset: bufferSize,
    length: buffer.byteLength
  };

  try {
    fs.readSync(file.fd, buffer, options);
    bufferSize += buffer.byteLength;
    // API version 11 不支持返回回调结果，从 API version 12 开始支持返回回调结果。
    return audio.AudioDataCallbackResult.VALID;
  } catch (error) {
    console.error('Error reading file:', error);
    // API version 11 不支持返回回调结果，从 API version 12 开始支持返回回调结果。
    return audio.AudioDataCallbackResult.INVALID;
  }
};

audioRenderer.on('writeData', writeDataCallback);
audioRenderer.start().then(() => {
  console.info('Renderer started');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### off('writeData')11+

off(type: 'writeData', callback?: AudioRendererWriteDataCallback): void

取消监听音频数据写入回调事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'writeData'，当取消监听音频数据写入回调事件时，触发该事件。callback[AudioRendererWriteDataCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605704__audiorendererwritedatacallback12)否

回调函数，入参代表应用接收待写入的数据缓冲区。

API version 11 不支持返回回调结果，从 API version 12 开始支持返回回调结果[AudioDataCallbackResult](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiodatacallbackresult12)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
// 取消该事件的所有监听。
audioRenderer.off('writeData');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let writeDataCallback = (data: ArrayBuffer) => {
    console.info(`write data: ${data}`);
};

audioRenderer.on('writeData', writeDataCallback);

audioRenderer.off('writeData', writeDataCallback);
```

#### write(deprecated)

write(buffer: ArrayBuffer, callback: AsyncCallback<number>): void

写入缓冲区。使用callback异步回调。

从API version 8开始支持，从API version 11开始废弃，建议使用[on('writeData')](#ZH-CN_TOPIC_0000002497445720__onwritedata11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明bufferArrayBuffer是要写入缓冲区的数据。callbackAsyncCallback<number>是回调函数。当写入缓冲区成功，err为undefined，data为获取到的写入的字节数；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

let bufferSize: number;
class Options {
  offset?: number;
  length?: number;
}
audioRenderer.getBufferSize().then((data: number)=> {
  console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
  bufferSize = data;
  console.info(`Buffer size: ${bufferSize}`);
  // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let path = context.cacheDir;
  // 此处仅作示例，实际使用时需要将文件替换为应用要播放的PCM文件。
  let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
  let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
  fs.stat(filePath).then(async (stat: fs.Stat) => {
    let buf = new ArrayBuffer(bufferSize);
    let len = stat.size % bufferSize == 0 ? Math.floor(stat.size / bufferSize) : Math.floor(stat.size / bufferSize + 1);
    for (let i = 0;i < len; i++) {
      let options: Options = {
        offset: i * bufferSize,
        length: bufferSize
      };
      await fs.read(file.fd, buf, options);
      await new Promise((resolve,reject)=>{
        audioRenderer.write(buf,(err: BusinessError, writeSize: number)=>{
          if(err){
            reject(err)
          }else{
            resolve(writeSize)
          }
        })
      })
    }
  });
  }).catch((err: BusinessError) => {
    console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}`);
});
```

#### write(deprecated)

write(buffer: ArrayBuffer): Promise<number>

写入缓冲区。使用Promise异步回调。

从API version 8开始支持，从API version 11开始废弃，建议使用[on('writeData')](#ZH-CN_TOPIC_0000002497445720__onwritedata11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明bufferArrayBuffer是要写入缓冲区的数据。

**返回值：**

类型说明Promise<number>Promise对象，返回写入的字节数。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';

let bufferSize: number;
class Options {
  offset?: number;
  length?: number;
}
audioRenderer.getBufferSize().then((data: number) => {
  console.info(`AudioFrameworkRenderLog: getBufferSize: SUCCESS ${data}`);
  bufferSize = data;
  console.info(`BufferSize: ${bufferSize}`);
  // 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let path = context.cacheDir;
  // 此处仅作示例，实际使用时需要将文件替换为应用要播放的PCM文件。
  let filePath = path + '/StarWars10s-2C-48000-4SW.pcm';
  let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
  fs.stat(filePath).then(async (stat: fs.Stat) => {
    let buf = new ArrayBuffer(bufferSize);
    let len = stat.size % bufferSize == 0 ? Math.floor(stat.size / bufferSize) : Math.floor(stat.size / bufferSize + 1);
    for (let i = 0;i < len; i++) {
      let options: Options = {
        offset: i * bufferSize,
        length: bufferSize
      };
      await fs.read(file.fd, buf, options);
      try{
        await audioRenderer.write(buf);
      } catch(err) {
        let error = err as BusinessError;
        console.error(`audioRenderer.write err: ${error}`);
      }
    }
  });
}).catch((err: BusinessError) => {
  console.error(`AudioFrameworkRenderLog: getBufferSize: ERROR: ${err}`);
});
```

#### setRenderRate(deprecated)

setRenderRate(rate: AudioRendererRate, callback: AsyncCallback<void>): void

设置音频渲染速率。使用callback异步回调。

从API version 8开始支持，从API version 11开始废弃，建议使用[setSpeed](#ZH-CN_TOPIC_0000002497445720__setspeed11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明rate[AudioRendererRate](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiorendererrate8)是渲染的速率。callbackAsyncCallback<void>是回调函数。当设置音频渲染速率成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setRenderRate(audio.AudioRendererRate.RENDER_RATE_NORMAL, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set params');
  } else {
    console.info('Callback invoked to indicate a successful render rate setting.');
  }
});
```

#### setRenderRate(deprecated)

setRenderRate(rate: AudioRendererRate): Promise<void>

设置音频渲染速率。使用Promise异步回调。

从API version 8开始支持，从API version 11开始废弃，建议使用[setSpeed](#ZH-CN_TOPIC_0000002497445720__setspeed11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明rate[AudioRendererRate](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiorendererrate8)是渲染的速率。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.setRenderRate(audio.AudioRendererRate.RENDER_RATE_NORMAL).then(() => {
  console.info('setRenderRate SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### getRenderRate(deprecated)

getRenderRate(callback: AsyncCallback<AudioRendererRate>): void

获取音频渲染速率。使用callback异步回调。

从API version 8开始支持，从API version 11开始废弃，建议使用[getSpeed](#ZH-CN_TOPIC_0000002497445720__getspeed11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明callbackAsyncCallback<[AudioRendererRate](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiorendererrate8)>是回调函数。当获取当前渲染速率成功，err为undefined，data为获取到的当前渲染速率；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRenderRate((err: BusinessError, renderRate: audio.AudioRendererRate) => {
  console.info(`getRenderRate: ${renderRate}`);
});
```

#### getRenderRate(deprecated)

getRenderRate(): Promise<AudioRendererRate>

获取音频渲染速率。使用Promise异步回调。

从API version 8开始支持，从API version 11开始废弃，建议使用[getSpeed](#ZH-CN_TOPIC_0000002497445720__getspeed11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明Promise<[AudioRendererRate](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiorendererrate8)>Promise对象，返回渲染速率。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioRenderer.getRenderRate().then((renderRate: audio.AudioRendererRate) => {
  console.info(`getRenderRate: ${renderRate}`);
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### getRenderRateSync(deprecated)

getRenderRateSync(): AudioRendererRate

获取音频渲染速率。同步返回结果。

从API version 10开始支持，从API version 11开始废弃，建议使用[getSpeed](#ZH-CN_TOPIC_0000002497445720__getspeed11)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明[AudioRendererRate](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiorendererrate8)返回渲染速率。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let renderRate: audio.AudioRendererRate = audioRenderer.getRenderRateSync();
  console.info(`getRenderRate: ${renderRate}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`ERROR: ${error}`);
}
```

#### setLoudnessGain20+

setLoudnessGain(loudnessGain: number): Promise<void>

设置播放响度。使用Promise异步回调。

- 该接口仅支持类型为[STREAM_USAGE_MUSIC](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)、[STREAM_USAGE_MOVIE](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)或[STREAM_USAGE_AUDIOBOOK](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)的音频流。
- 该接口不支持高清通路的响度设置。
- 由于音频框架与硬件之间存在缓冲区，响度调节实际生效存在延迟，时长取决于缓冲区长度。
- 建议在不同音频开始播放前预先设置响度，以实现最佳均衡效果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

参数名类型必填说明loudnessGainnumber是设置播放的响度值，单位为dB，响度范围为[-90.0, 24.0]。默认值为0.0dB。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.6800104

Operation is not supported on this renderer, e.g. the stream usage of this renderer is not one of [STREAM_USAGE_MUSIC](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage),

[STREAM_USAGE_MOVIE](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage), or [STREAM_USAGE_AUDIOBOOK](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage), or this renderer is routed through the high-resolution playback path.

**示例：**

```ets
audioRenderer.setLoudnessGain(1.0);
```

#### getLoudnessGain20+

getLoudnessGain(): number

获取播放响度。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

类型说明number返回播放的响度值。

**示例：**

```ets
let loudnessGain = audioRenderer.getLoudnessGain();
```