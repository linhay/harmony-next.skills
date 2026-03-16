# Interface (AudioVolumeManager)

音量管理。

在使用AudioVolumeManager的接口之前，需先通过[getVolumeManager](Interface (AudioManager).md#ZH-CN_TOPIC_0000002497605698__getvolumemanager9)获取AudioVolumeManager实例。

- 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 9开始支持。

#### 导入模块

```ets
import { audio } from '@kit.AudioKit';
```

#### getVolumeGroupManager9+

getVolumeGroupManager(groupId: number, callback: AsyncCallback<AudioVolumeGroupManager>): void

获取音频组音量管理器实例。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明groupIdnumber是音量组id，默认使用DEFAULT_VOLUME_GROUP_ID。callbackAsyncCallback<[AudioVolumeGroupManager](Interface (AudioVolumeGroupManager).md)>是回调函数。当获取音频组音量管理器实例成功，err为undefined，data为获取到的音频组音量管理器实例；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let groupId: number = audio.DEFAULT_VOLUME_GROUP_ID;

audioVolumeManager.getVolumeGroupManager(groupId, (err: BusinessError, value: audio.AudioVolumeGroupManager) => {
  if (err) {
    console.error(`Failed to getVolumeGroupManager. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in doing getVolumeGroupManager.');
});
```

#### getVolumeGroupManager9+

getVolumeGroupManager(groupId: number): Promise<AudioVolumeGroupManager>

获取音频组音量管理器实例。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明groupIdnumber是音量组id，默认使用DEFAULT_VOLUME_GROUP_ID。

**返回值：**

类型说明Promise< [AudioVolumeGroupManager](Interface (AudioVolumeGroupManager).md) >Promise对象，返回音频组音量管理器实例。

**示例：**

```ets
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

let groupId: number = audio.DEFAULT_VOLUME_GROUP_ID;

audioVolumeManager.getVolumeGroupManager(groupId).then((audioVolumeGroupManager: audio.AudioVolumeGroupManager) => {
  console.info('Succeeded in doing getVolumeGroupManager.');
}).catch((err: BusinessError) => {
  console.error(`Failed to getVolumeGroupManager. Code: ${err.code}, message: ${err.message}`);
});
```

#### getVolumeGroupManagerSync10+

getVolumeGroupManagerSync(groupId: number): AudioVolumeGroupManager

获取音频组音量管理器实例。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明groupIdnumber是音量组id，默认使用DEFAULT_VOLUME_GROUP_ID。

**返回值：**

类型说明[AudioVolumeGroupManager](Interface (AudioVolumeGroupManager).md)音频组音量管理器实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioVolumeGroupManager: audio.AudioVolumeGroupManager = audioVolumeManager.getVolumeGroupManagerSync(audio.DEFAULT_VOLUME_GROUP_ID);
  console.info(`Get audioVolumeGroupManager success.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get audioVolumeGroupManager, error: ${error}`);
}
```

#### getAppVolumePercentage19+

getAppVolumePercentage(): Promise<number>

获取应用的音量（范围为0到100）。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

类型说明Promise<number>Promise对象，返回应用的音量。

**示例：**

```ets
import { audio } from '@kit.AudioKit';

audioVolumeManager.getAppVolumePercentage().then((value: number) => {
  console.info(`app volume is ${value}.`);
});
```

#### setAppVolumePercentage19+

setAppVolumePercentage(volume: number): Promise<void>

设置应用的音量（范围为0到100）。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumenumber是要设置的音量值。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.6800301Crash or blocking occurs in system process.

**示例：**

```ets
import { audio } from '@kit.AudioKit';

audioVolumeManager.setAppVolumePercentage(20).then(() => {
  console.info(`set app volume success.`);
});
```

#### on('volumeChange')(deprecated)

on(type: 'volumeChange', callback: Callback<VolumeEvent>): void

监听系统音量变化事件（当系统音量发生变化时触发）。使用callback异步回调。

从API version 12开始支持，从API version 20开始废弃，建议使用[on('streamVolumeChange')](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__onstreamvolumechange20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'volumeChange'，当系统音量发生变化时，触发该事件。callbackCallback<[VolumeEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__volumeevent9)>是回调函数，返回变化后的音量信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
audioVolumeManager.on('volumeChange', (volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
});
```

#### off('volumeChange')(deprecated)

off(type: 'volumeChange', callback?: Callback<VolumeEvent>): void

取消监听系统音量变化事件。使用callback异步回调。

从API version 12开始支持，从API version 20开始废弃，建议使用[off('streamVolumeChange')](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__offstreamvolumechange20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'volumeChange'，当取消监听系统音量变化事件时，触发该事件。callbackCallback<[VolumeEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__volumeevent9)>否回调函数，返回变化后的音量信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters missing; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
// 取消该事件的所有监听。
audioVolumeManager.off('volumeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let volumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
};

audioVolumeManager.on('volumeChange', volumeChangeCallback);

audioVolumeManager.off('volumeChange', volumeChangeCallback);
```

#### on('appVolumeChange')19+

on(type: 'appVolumeChange', callback: Callback<VolumeEvent>): void

监听当前应用应用级音量变化事件（当应用级音量发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'appVolumeChange'，当应用级音量发生变化时，触发该事件。callbackCallback<[VolumeEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__volumeevent9)>是回调函数，返回变化后的音量信息。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
audioVolumeManager.on('appVolumeChange', (volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
});
```

#### off('appVolumeChange')19+

off(type: 'appVolumeChange', callback?: Callback<VolumeEvent>): void

取消监听当前应用应用级音量变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'appVolumeChange'，当取消监听当前应用应用级音量变化事件时，触发该事件。callbackCallback<[VolumeEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__volumeevent9)>否回调函数，返回变化后的音量信息。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
// 取消该事件的所有监听。
audioVolumeManager.off('appVolumeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let appVolumeChangeCallback = (volumeEvent: audio.VolumeEvent) => {
  console.info(`VolumeType of stream: ${volumeEvent.volumeType} `);
  console.info(`Volume level: ${volumeEvent.volume} `);
  console.info(`Whether to updateUI: ${volumeEvent.updateUi} `);
};

audioVolumeManager.on('appVolumeChange', appVolumeChangeCallback);

audioVolumeManager.off('appVolumeChange', appVolumeChangeCallback);
```

#### getVolumeByStream20+

getVolumeByStream(streamUsage: StreamUsage): number

获取指定音频流的音量。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明streamUsage[StreamUsage](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)是需要获取音量值的音频流。

**返回值：**

类型说明number音量值。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
// 获取指定音频流的音量值。
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit'

try {
  let volume : number = audio.getAudioManager().getVolumeManager().getVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
  console.info(`Obtains the volume of a stream success.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtains the volume of a stream, error: ${error}`);
}
```

#### getMinVolumeByStream20+

getMinVolumeByStream(streamUsage: StreamUsage): number

获取指定音频流的最小音量。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明streamUsage[StreamUsage](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)是需要获取的最小音量值的音频流。

**返回值：**

类型说明number音量值。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
// 获取指定音频流的最小音量。
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit'

try {
  let volume : number = audio.getAudioManager().getVolumeManager().getMinVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
  console.info(`Obtains the minimum volume allowed for a stream success.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtains the minimum volume allowed for a stream, error: ${error}`);
}
```

#### getMaxVolumeByStream20+

getMaxVolumeByStream(streamUsage: StreamUsage): number

获取指定音频流的最大音量。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明streamUsage[StreamUsage](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)是需要获取的最大音量值的音频流。

**返回值：**

类型说明number音量值。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
// 获取指定音频流的最大音量。
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit'

try {
  let volume : number = audio.getAudioManager().getVolumeManager().getMaxVolumeByStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
  console.info(`Obtains the maximum volume allowed for a stream success.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtains the maximum volume allowed for a stream, error: ${error}`);
}
```

#### isSystemMutedForStream20+

isSystemMutedForStream(streamUsage: StreamUsage): boolean

检查指定音频流是否静音。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明streamUsage[StreamUsage](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)是检查是否为静音的音频流。

**返回值：**

类型说明boolean音频流是否为静音状态，true表示音频流已静音，false表示音频流未静音。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
// 检查指定音频流是否静音。
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit'

try {
  let isMuted : boolean = audio.getAudioManager().getVolumeManager().isSystemMutedForStream(audio.StreamUsage.STREAM_USAGE_MUSIC);
  console.info(`Checks whether the system is muted based on the stream success.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to checks whether the system is muted based on the stream, error: ${error}`);
}
```

#### getVolumeInUnitOfDbByStream20+

getVolumeInUnitOfDbByStream(streamUsage: StreamUsage, volumeLevel: number, device: DeviceType): number

获取系统通过音频流、音量等级和设备类型计算出的音量db值。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明streamUsage[StreamUsage](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)是音频流。volumeLevelnumber是音量值等级。device[DeviceType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__devicetype)是设备类型。

**返回值：**

类型说明number音频流的音量db值。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
// 获取系统通过音频流、音量等级和设备类型计算出的音量db值。
import { BusinessError } from '@kit.BasicServicesKit';
import { audio } from '@kit.AudioKit'

try {
  let volumeInDb : number = audio.getAudioManager().getVolumeManager().getVolumeInUnitOfDbByStream(audio.StreamUsage.STREAM_USAGE_MUSIC, 5, audio.DeviceType.SPEAKER);
  console.info(`Gets the volume db value that system calculate by volume stream, volume level and device type.
 success.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to gets the volume db value that system calculate by volume stream, volume level and device type., error: ${error}`);
}
```

#### on('streamVolumeChange')20+

 on(type: 'streamVolumeChange', streamUsage: StreamUsage, callback: Callback<StreamVolumeEvent>): void

监听系统音频流音量变化事件（当系统音频流音量发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'streamVolumeChange'，当系统音量发生变化时，触发该事件。streamUsage[StreamUsage](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__streamusage)是音频流使用类型。callbackCallback<[StreamVolumeEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__streamvolumeevent20)>是回调函数，返回变化后的音量信息。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC, (streamVolumeEvent: audio.StreamVolumeEvent) => {
  console.info(`StreamUsage of stream: ${streamVolumeEvent.streamUsage} `);
  console.info(`Volume level: ${streamVolumeEvent.volume} `);
  console.info(`Whether to updateUI: ${streamVolumeEvent.updateUi} `);
});
```

#### off('streamVolumeChange')20+

off(type: 'streamVolumeChange', callback?: Callback<StreamVolumeEvent>): void

取消监听系统音频流音量变化事件（当系统音频流音量发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'volumeChange'，当取消监听系统音量变化事件时，触发该事件。callbackCallback<[StreamVolumeEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__streamvolumeevent20)>否回调函数，返回变化后的音量信息。

**示例：**

```ets
// 取消该事件的所有监听。
audioVolumeManager.off('streamVolumeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let streamVolumeChangeCallback = (streamVolumeEvent: audio.StreamVolumeEvent) => {
  console.info(`StreamUsage of stream: ${streamVolumeEvent.streamUsage} `);
  console.info(`Volume level: ${streamVolumeEvent.volume} `);
  console.info(`Whether to updateUI: ${streamVolumeEvent.updateUi} `);
};

audioVolumeManager.on('streamVolumeChange', audio.StreamUsage.STREAM_USAGE_MUSIC, streamVolumeChangeCallback);

audioVolumeManager.off('streamVolumeChange', streamVolumeChangeCallback);
```