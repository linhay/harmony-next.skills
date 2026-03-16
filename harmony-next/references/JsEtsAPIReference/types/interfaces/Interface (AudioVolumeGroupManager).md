# Interface (AudioVolumeGroupManager)

管理音频组音量。

在使用AudioVolumeGroupManager的接口之前，需先通过[getVolumeGroupManager](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getvolumegroupmanager9)获取AudioVolumeGroupManager实例。

- 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 9开始支持。

#### 导入模块

```ets
import { audio } from '@kit.AudioKit';
```

#### getVolume(deprecated)

getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的音量。使用callback异步回调。

从API version 9开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。callbackAsyncCallback<number>是回调函数。当获取指定流的音量成功，err为undefined，data为获取到的指定流的音量；否则为错误对象。指定流的音量等级范围可通过[getMinVolume](#ZH-CN_TOPIC_0000002529285693__getminvolumedeprecated)和[getMaxVolume](#ZH-CN_TOPIC_0000002529285693__getmaxvolumedeprecated)获取。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the volume. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the volume is obtained.');
});
```

#### getVolume(deprecated)

getVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的音量。使用Promise异步回调。

从API version 9开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。

**返回值：**

类型说明Promise<number>Promise对象，返回指定流的音量。指定流的音量等级范围可通过[getMinVolume](#ZH-CN_TOPIC_0000002529285693__getminvolumedeprecated)和[getMaxVolume](#ZH-CN_TOPIC_0000002529285693__getmaxvolumedeprecated)获取。

**示例：**

```ets
audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Promise returned to indicate that the volume is obtained ${value}.`);
});
```

#### getVolumeSync(deprecated)

getVolumeSync(volumeType: AudioVolumeType): number

获取指定流的音量。同步返回结果。

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。

**返回值：**

类型说明number返回指定流的音量。指定流的音量等级范围可通过[getMinVolume](#ZH-CN_TOPIC_0000002529285693__getminvolumedeprecated)和[getMaxVolume](#ZH-CN_TOPIC_0000002529285693__getmaxvolumedeprecated)获取。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(`Indicate that the volume is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the volume, error ${error}.`);
}
```

#### getMinVolume(deprecated)

getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最小音量。使用callback异步回调。

从API version 9开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。callbackAsyncCallback<number>是回调函数。当获取指定流的最小音量成功，err为undefined，data为获取到的指定流的最小音量；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getMinVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the minimum volume. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the minimum volume is obtained. ${value}`);
});
```

#### getMinVolume(deprecated)

getMinVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最小音量。使用Promise异步回调。

从API version 9开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。

**返回值：**

类型说明Promise<number>Promise对象，返回最小音量。

**示例：**

```ets
audioVolumeGroupManager.getMinVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Promised returned to indicate that the minimum volume is obtained ${value}.`);
});
```

#### getMinVolumeSync(deprecated)

getMinVolumeSync(volumeType: AudioVolumeType): number

获取指定流的最小音量。同步返回结果。

从API version 10开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。

**返回值：**

类型说明number返回最小音量。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getMinVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(`Indicate that the minimum volume is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the minimum volume, error ${error}.`);
}
```

#### getMaxVolume(deprecated)

getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最大音量。使用callback异步回调。

从API version 9开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。callbackAsyncCallback<number>是回调函数。当获取指定流的最大音量成功，err为undefined，data为获取到的指定流的最大音量；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getMaxVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to obtain the maximum volume. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the maximum volume is obtained. ${value}`);
});
```

#### getMaxVolume(deprecated)

getMaxVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最大音量。使用Promise异步回调。

从API version 9开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。

**返回值：**

类型说明Promise<number>Promise对象，返回最大音量大小。

**示例：**

```ets
audioVolumeGroupManager.getMaxVolume(audio.AudioVolumeType.MEDIA).then((data: number) => {
  console.info('Promised returned to indicate that the maximum volume is obtained.');
});
```

#### getMaxVolumeSync(deprecated)

getMaxVolumeSync(volumeType: AudioVolumeType): number

获取指定流的最大音量。同步返回结果。

从API version 10开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。

**返回值：**

类型说明number返回最大音量大小。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getMaxVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(`Indicate that the maximum volume is obtained. ${value}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the maximum volume, error ${error}.`);
}
```

#### isMute(deprecated)

isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

获取指定音量流静音状态。使用callback异步回调。

从API version 9开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。callbackAsyncCallback<boolean>是回调函数。当获取指定音量流静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMute(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to obtain the mute status. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the mute status of the stream is obtained ${value}.`);
});
```

#### isMute(deprecated)

isMute(volumeType: AudioVolumeType): Promise<boolean>

获取指定音量流是否被静音。使用Promise异步回调。

从API version 9开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示静音；返回false表示非静音。

**示例：**

```ets
audioVolumeGroupManager.isMute(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(`Promise returned to indicate that the mute status of the stream is obtained ${value}.`);
});
```

#### isMuteSync(deprecated)

isMuteSync(volumeType: AudioVolumeType): boolean

获取指定音量流是否被静音。同步返回结果。

从API version 10开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。

**返回值：**

类型说明boolean流静音状态。返回true表示静音，返回false表示非静音。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioVolumeGroupManager.isMuteSync(audio.AudioVolumeType.MEDIA);
  console.info(`Indicate that the mute status of the stream is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the mute status of the stream, error ${error}.`);
}
```

#### getRingerMode9+

getRingerMode(callback: AsyncCallback<AudioRingMode>): void

获取铃声模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明callbackAsyncCallback<[AudioRingMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audioringmode)>是回调函数。当获取铃声模式成功，err为undefined，data为获取到的铃声模式；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getRingerMode((err: BusinessError, value: audio.AudioRingMode) => {
  if (err) {
    console.error(`Failed to obtain the ringer mode. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the ringer mode is obtained ${value}.`);
});
```

#### getRingerMode9+

getRingerMode(): Promise<AudioRingMode>

获取铃声模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

类型说明Promise<[AudioRingMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audioringmode)>Promise对象，返回系统的铃声模式。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getRingerMode().then((value: audio.AudioRingMode) => {
  console.info(`Promise returned to indicate that the ringer mode is obtained ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getRingerMode. Code: ${err.code}, message: ${err.message}`);
});
```

#### getRingerModeSync10+

getRingerModeSync(): AudioRingMode

获取铃声模式。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

类型说明[AudioRingMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audioringmode)返回系统的铃声模式。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: audio.AudioRingMode = audioVolumeGroupManager.getRingerModeSync();
  console.info(`Indicate that the ringer mode is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the ringer mode, error ${error}.`);
}
```

#### on('ringerModeChange')9+

on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void

监听铃声模式变化事件（当[铃声模式](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audioringmode)发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'ringerModeChange'，当铃声模式发生变化时，触发该事件。callbackCallback<[AudioRingMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audioringmode)>是回调函数，返回变化后的铃音模式。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
audioVolumeGroupManager.on('ringerModeChange', (ringerMode: audio.AudioRingMode) => {
  console.info(`Updated ringermode: ${ringerMode}`);
});
```

#### off('ringerModeChange')18+

off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void

取消监听铃声模式变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'ringerModeChange'，当取消监听铃声模式变化事件时，触发该事件。callbackCallback<[AudioRingMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audioringmode)>否回调函数，返回变化后的铃音模式。

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息6800101Parameter verification failed.

**示例：**

```ets
// 取消该事件的所有监听。
audioVolumeGroupManager.off('ringerModeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let ringerModeChangeCallback = (ringerMode: audio.AudioRingMode) => {
  console.info(`Updated ringermode: ${ringerMode}`);
};

audioVolumeGroupManager.on('ringerModeChange', ringerModeChangeCallback);

audioVolumeGroupManager.off('ringerModeChange', ringerModeChangeCallback);
```

#### isMicrophoneMute9+

isMicrophoneMute(callback: AsyncCallback<boolean>): void

获取麦克风静音状态。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。当获取麦克风静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMicrophoneMute((err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to obtain the mute status of the microphone. ${err}`);
    return;
  }
  console.info(`Callback invoked to indicate that the mute status of the microphone is obtained ${value}.`);
});
```

#### isMicrophoneMute9+

isMicrophoneMute(): Promise<boolean>

获取麦克风静音状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示麦克风被静音；返回false表示麦克风未被静音。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMicrophoneMute().then((value: boolean) => {
  console.info(`Promise returned to indicate that the mute status of the microphone is obtained ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to isMicrophoneMute. Code: ${err.code}, message: ${err.message}`);
});
```

#### isMicrophoneMuteSync10+

isMicrophoneMuteSync(): boolean

获取麦克风静音状态。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

类型说明boolean系统麦克风静音状态。返回true表示静音，返回false表示非静音。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioVolumeGroupManager.isMicrophoneMuteSync();
  console.info(`Indicate that the mute status of the microphone is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the mute status of the microphone, error ${error}.`);
}
```

#### on('micStateChange')9+

on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void

监听系统麦克风状态更改事件（当检测到系统麦克风状态发生改变时触发）。使用callback异步回调。

目前此订阅接口在单进程多AudioManager实例的使用场景下，仅最后一个实例的订阅生效，其他实例的订阅会被覆盖（即使最后一个实例没有进行订阅）。因此，推荐使用单一AudioManager实例进行开发。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'micStateChange'，当检测到系统麦克风状态发生改变时，触发该事件。callbackCallback<[MicStateChangeEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__micstatechangeevent9)>是回调函数，返回变更后的麦克风状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
audioVolumeGroupManager.on('micStateChange', (micStateChange: audio.MicStateChangeEvent) => {
  console.info(`Current microphone status is: ${micStateChange.mute} `);
});
```

#### off('micStateChange')12+

off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void

取消监听系统麦克风状态更改事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'micStateChange'，当取消监听系统麦克风状态更改事件时，触发该事件。callbackCallback<[MicStateChangeEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__micstatechangeevent9)>否回调函数，返回变更后的麦克风状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters missing; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
// 取消该事件的所有监听。
audioVolumeGroupManager.off('micStateChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let micStateChangeCallback = (micStateChange: audio.MicStateChangeEvent) => {
  console.info(`Current microphone status is: ${micStateChange.mute} `);
};

audioVolumeGroupManager.on('micStateChange', micStateChangeCallback);

audioVolumeGroupManager.off('micStateChange', micStateChangeCallback);
```

#### isVolumeUnadjustable10+

isVolumeUnadjustable(): boolean

获取固定音量模式开关状态，打开时进入固定音量模式，此时音量固定无法被调节。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

类型说明boolean固定音量模式开关状态。返回true表示固定音量模式，返回false表示非固定音量模式。

**示例：**

```ets
let volumeAdjustSwitch: boolean = audioVolumeGroupManager.isVolumeUnadjustable();
console.info(`Whether it is volume unadjustable: ${volumeAdjustSwitch}.`);
```

#### getSystemVolumeInDb(deprecated)

getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void

获取音量增益dB值。使用callback异步回调。

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。volumeLevelnumber是音量等级。device[DeviceType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__devicetype)是设备类型。callbackAsyncCallback<number>是回调函数。当获取音量增益dB值成功，err为undefined，data为获取到的音量增益dB值；否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed. Return by callback.6800301System error. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER, (err: BusinessError, dB: number) => {
  if (err) {
    console.error(`Failed to get the volume DB. ${err}`);
  } else {
    console.info(`Success to get the volume DB. ${dB}`);
  }
});
```

#### getSystemVolumeInDb(deprecated)

getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>

获取音量增益dB值。使用Promise异步回调。

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。volumeLevelnumber是音量等级。device[DeviceType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__devicetype)是设备类型。

**返回值：**

类型说明Promise<number>Promise对象，返回对应的音量增益dB值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed. Return by promise.6800301System error. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER).then((value: number) => {
  console.info(`Success to get the volume DB. ${value}`);
}).catch((error: BusinessError) => {
  console.error(`Fail to adjust the system volume by step. ${error}`);
});
```

#### getSystemVolumeInDbSync(deprecated)

getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number

获取音量增益dB值。同步返回结果。

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](Interface (AudioVolumeManager).md#ZH-CN_TOPIC_0000002529445667__getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明volumeType[AudioVolumeType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiovolumetype)是音频音量类型。volumeLevelnumber是音量等级。device[DeviceType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529285695__devicetype)是设备类型。

**返回值：**

类型说明number返回对应的音量增益dB值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getSystemVolumeInDbSync(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER);
  console.info(`Success to get the volume DB. ${value}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Fail to adjust the system volume by step. ${error}`);
}
```

#### getMaxAmplitudeForInputDevice12+

getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>

获取输入设备音频流的最大电平值，取值范围为[0, 1]。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明inputDevice[AudioDeviceDescriptor](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiodevicedescriptor)是获取最大电平值的设备信息。

**返回值：**

类型说明Promise<number>Promise对象，返回对应设备的电平值，大小在[0, 1]之间。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed. Return by promise.6800301System error. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let capturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
  capturerFlags: 0 // 音频采集器标志。
};

audio.getAudioManager().getRoutingManager().getPreferredInputDeviceForCapturerInfo(capturerInfo).then((data) => {
  audioVolumeGroupManager.getMaxAmplitudeForInputDevice(data[0]).then((value) => {
    console.info(`max amplitude is: ${value}`);
  }).catch((err: BusinessError) => {
    console.error(`getMaxAmplitudeForInputDevice error. Code: ${err.code}, message: ${err.message}`);
  })
}).catch((err: BusinessError) => {
  console.error(`getPreferredInputDeviceForCapturerInfo error. Code: ${err.code}, message: ${err.message}`);
})
```

#### getMaxAmplitudeForOutputDevice12+

getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<number>

获取输出设备音频流的最大电平值，取值范围为[0, 1]。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明outputDevice[AudioDeviceDescriptor](Interfaces (其他).md#ZH-CN_TOPIC_0000002497445724__audiodevicedescriptor)是获取最大电平值的设备信息。

**返回值：**

类型说明Promise<number>Promise对象，返回对应设备的电平值，大小在[0, 1]之间。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[Audio错误码](../../errors/Audio错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.6800101Parameter verification failed. Return by promise.6800301System error. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let rendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};

audio.getAudioManager().getRoutingManager().getPreferOutputDeviceForRendererInfo(rendererInfo).then((data) => {
  audioVolumeGroupManager.getMaxAmplitudeForOutputDevice(data[0]).then((value) => {
    console.info(`max amplitude is: ${value}`);
  }).catch((err: BusinessError) => {
    console.error(`getMaxAmplitudeForOutputDevice error. Code: ${err.code}, message: ${err.message}`);
  })
}).catch((err: BusinessError) => {
  console.error(`getPreferOutputDeviceForRendererInfo error. Code: ${err.code}, message: ${err.message}`);
})
```

#### setMicrophoneMute(deprecated)

setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void

设置麦克风静音状态。使用callback异步回调。

从API version 9开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明muteboolean是是否设置麦克风为静音状态。true表示静音，false表示非静音。callbackAsyncCallback<void>是回调函数。当设置麦克风静音状态成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.setMicrophoneMute(true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to mute the microphone. ${err}`);
    return;
  }
  console.info('Callback invoked to indicate that the microphone is muted.');
});
```

#### setMicrophoneMute(deprecated)

setMicrophoneMute(mute: boolean): Promise<void>

设置麦克风静音状态。使用Promise异步回调。

从API version 9开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.MANAGE_AUDIO_CONFIG，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

参数名类型必填说明muteboolean是是否设置麦克风为静音状态。true表示静音，false表示非静音。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
audioVolumeGroupManager.setMicrophoneMute(true).then(() => {
  console.info('Promise returned to indicate that the microphone is muted.');
});
```