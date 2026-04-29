# Interface (AudioSessionManager)

音频会话管理。

在使用AudioSessionManager的接口之前，需先通过[getSessionManager](Interface (AudioManager).md#ZH-CN_TOPIC_0000002553361737__getsessionmanager12)获取AudioSessionManager实例。


- 本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 12开始支持。

#### 导入模块

```ets
import { audio } from '@kit.AudioKit';
```

#### activateAudioSession12+

activateAudioSession(strategy: AudioSessionStrategy): Promise<void>

激活音频会话。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategy | AudioSessionStrategy | 是 | 音频会话策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[Audio错误码]([Audio错误码](../../errors/Audio错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |
| 6800301 | System error. Returned by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let strategy: audio.AudioSessionStrategy = {
  concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS
};

audioSessionManager.activateAudioSession(strategy).then(() => {
  console.info('activateAudioSession SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### deactivateAudioSession12+

deactivateAudioSession(): Promise<void>

停用音频会话。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | System error. Returned by promise. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.deactivateAudioSession().then(() => {
  console.info('deactivateAudioSession SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`ERROR: ${err}`);
});
```

#### isAudioSessionActivated12+

isAudioSessionActivated(): boolean

检查音频会话是否已激活。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 音频会话是否处于激活状态。true表示已激活，false表示已停用。 |

**示例：**

```ets
let isActivated = audioSessionManager.isAudioSessionActivated();
```

#### on('audioSessionDeactivated')12+

on(type: 'audioSessionDeactivated', callback: Callback<AudioSessionDeactivatedEvent>): void

监听音频会话停用事件（当音频会话停用时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionDeactivated'，当音频会话停用时，触发该事件。 |
| callback | Callback<AudioSessionDeactivatedEvent> | 是 | 回调函数，返回音频会话停用原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters unspecified. 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ets
audioSessionManager.on('audioSessionDeactivated',
  (audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
  console.info(`reason of audioSessionDeactivated: ${audioSessionDeactivatedEvent.reason} `);
});
```

#### off('audioSessionDeactivated')12+

off(type: 'audioSessionDeactivated', callback?: Callback<AudioSessionDeactivatedEvent>): void

取消监听音频会话停用事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionDeactivated'，当取消监听音频会话停用事件时，触发该事件。 |
| callback | Callback<AudioSessionDeactivatedEvent> | 否 | 回调函数，返回音频会话停用原因。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ets
// 取消该事件的所有监听。
audioSessionManager.off('audioSessionDeactivated');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let audioSessionDeactivatedCallback = (audioSessionDeactivatedEvent: audio.AudioSessionDeactivatedEvent) => {
  console.info(`reason of audioSessionDeactivated: ${audioSessionDeactivatedEvent.reason} `);
};

audioSessionManager.on('audioSessionDeactivated', audioSessionDeactivatedCallback);

audioSessionManager.off('audioSessionDeactivated', audioSessionDeactivatedCallback);
```

#### set[AudioSessionScene](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__audiosessionscene20)20+

set[AudioSessionScene](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__audiosessionscene20)(scene: AudioSessionScene): void

设置音频会话场景参数。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scene | [AudioSessionScene](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__audiosessionscene20) | 是 | 音频会话场景。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
audioSessionManager.setAudioSessionScene(audio.AudioSessionScene.AUDIO_SESSION_SCENE_MEDIA);
```

#### on('audioSessionStateChanged')20+

on(type: 'audioSessionStateChanged', callback: Callback<AudioSessionStateChangedEvent>): void

监听音频会话状态变更事件（当音频会话焦点变更时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionStateChanged'，当音频会话状态变更时，触发该事件。 |
| callback | Callback<AudioSessionStateChangedEvent> | 是 | 回调函数，返回音频会话变更提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800102 | Allocate memory failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
audioSessionManager.on('audioSessionStateChanged', (audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
  console.info(`hint of audioSessionStateChanged: ${audioSessionStateChangedEvent.stateChangeHint} `);
});
```

#### off('audioSessionStateChanged')20+

off(type: 'audioSessionStateChanged', callback?: Callback<AudioSessionStateChangedEvent>): void

取消监听音频会话状态变更事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'audioSessionStateChanged'，当音频会话状态变更时，触发该事件。 |
| callback | Callback<AudioSessionStateChangedEvent> | 否 | 回调函数，返回音频会话变更提示信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
// 取消该事件的所有监听。
audioSessionManager.off('audioSessionStateChanged');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let audioSessionStateChangedCallback = (audioSessionStateChangedEvent: audio.AudioSessionStateChangedEvent) => {
  console.info(`hint of audioSessionStateChanged: ${audioSessionStateChangedEvent.stateChangeHint} `);
};

audioSessionManager.on('audioSessionStateChanged', audioSessionStateChangedCallback);

audioSessionManager.off('audioSessionStateChanged', audioSessionStateChangedCallback);
```

#### setDefaultOutputDevice20+

setDefaultOutputDevice(deviceType: [DeviceType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__devicetype)): Promise<void>

设置默认发声设备。使用Promise方式进行异步回调。


- 本接口适用于以下情况：当设置的[AudioSessionScene](Enums.md#ZH-CN_TOPIC_0000002553201785__audiosessionscene20)为VoIP场景时，激活AudioSession后立即生效。若[AudioSessionScene](Enums.md#ZH-CN_TOPIC_0000002553201785__audiosessionscene20)为非VoIP场景，激活AudioSession时不会生效，仅在启动播放的[StreamUsage](Enums.md#ZH-CN_TOPIC_0000002553201785__streamusage)为语音消息、VoIP语音通话或VoIP视频通话时才生效。支持听筒、扬声器和系统默认设备。

- 本接口允许在AudioSessionManager创建后随时调用，系统会记录应用设置的默认本机内置发声设备。但只有激活AudioSession后才能生效。应用启动播放时，若外接设备如蓝牙耳机或有线耳机已接入，系统优先从外接设备发声。否则，系统遵循应用设置的默认本机内置发声设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

设备行为差异： 当该接口在无听筒的设备上设置默认发声设备为听筒时，将继续从扬声器发声。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceType | [DeviceType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__devicetype) | 是 | 设备类型。 仅支持以下设备：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800102 | Allocate memory failed. Return by promise. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
  console.info('setDefaultOutputDevice Success!');
}).catch((err: BusinessError) => {
  console.error(`setDefaultOutputDevice Fail: ${err}`);
});
```

#### getDefaultOutputDevice20+

getDefaultOutputDevice(): [DeviceType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__devicetype)

获取通过[setDefaultOutputDevice](#ZH-CN_TOPIC_0000002522081820__setdefaultoutputdevice20)设置的默认发声设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceType](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__devicetype) | 设备类型。 仅支持以下设备：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800103 | Operation not permit at current state. Return by promise. |

**示例：**

```ets
let deviceType = audioSessionManager.getDefaultOutputDevice();
```

#### on('currentOutputDeviceChanged')20+

on(type: 'currentOutputDeviceChanged', callback: Callback<CurrentOutputDeviceChangedEvent>): void

监听当前输出设备变化事件（当前输出设备发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentOutputDeviceChanged'，当前输出设备变更时触发。 |
| callback | Callback<CurrentOutputDeviceChangedEvent> | 是 | 回调函数，返回当前输出设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800102 | Allocate memory failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
import { audio } from '@kit.AudioKit';

let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
  console.info(`reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} `);
};

audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);
```

#### off('currentOutputDeviceChanged')20+

off(type: 'currentOutputDeviceChanged', callback?: Callback<CurrentOutputDeviceChangedEvent>): void

取消监听当前输出设备的变化事件，并使用callback进行异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentOutputDeviceChanged'，当前输出设备发生变化时，触发该事件。 |
| callback | Callback<CurrentOutputDeviceChangedEvent> | 否 | 回调函数，用于返回当前输出设备变化的信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
// 取消该事件的所有监听。
audioSessionManager.off('currentOutputDeviceChanged');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
  console.info(`reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} `);
};

audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);

audioSessionManager.off('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);
```

#### getAvailableDevices21+

getAvailableDevices(deviceUsage: [DeviceUsage](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__deviceusage12)): AudioDeviceDescriptors

获取音频可选设备列表。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceUsage | [DeviceUsage](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__deviceusage12) | 是 | 音频设备类型（根据用途分类）。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AudioDeviceDescriptors](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605704__audiodevicedescriptors) | 返回设备列表。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data: audio.AudioDeviceDescriptors = audioSessionManager.getAvailableDevices(audio.DeviceUsage.MEDIA_OUTPUT_DEVICES);
  console.info('Succeeded in doing getAvailableDevices.');
} catch (err) {
  let error = err as BusinessError;
   console.error(`Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}`);
}
```

#### on('availableDeviceChange')21+

on(type: 'availableDeviceChange', deviceUsage: [DeviceUsage](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__deviceusage12), callback: Callback<DeviceChangeAction>): void

监听音频可选设备连接状态变化事件（当音频可选设备连接状态发生变化时触发）。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'availableDeviceChange'，当音频可选设备连接状态发生变化时，触发该事件。 |
| deviceUsage | [DeviceUsage](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__deviceusage12) | 是 | 音频设备类型（根据用途分类）。 |
| callback | Callback<DeviceChangeAction> | 是 | 回调函数，返回设备更新详情。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
audioSessionManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA_INPUT_DEVICES, (deviceChanged: audio.DeviceChangeAction) => {
  console.info('device change type : ' + deviceChanged.type);
  console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceRole);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceType);
});
```

#### off('availableDeviceChange')21+

off(type: 'availableDeviceChange', callback?: Callback<DeviceChangeAction>): void

取消监听音频可选设备连接状态变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'availableDeviceChange'，当取消监听音频可选设备连接变化事件时，触发该事件。 |
| callback | Callback<DeviceChangeAction> | 否 | 回调函数，返回可选设备更新详情。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
// 取消该事件的所有监听。
audioSessionManager.off('availableDeviceChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let availableDeviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
  console.info('device change type : ' + deviceChanged.type);
  console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceRole);
  console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceType);
};

audioSessionManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA_INPUT_DEVICES, availableDeviceChangeCallback);

audioSessionManager.off('availableDeviceChange', availableDeviceChangeCallback);
```

#### selectMediaInputDevice21+

selectMediaInputDevice(inputAudioDevice: AudioDeviceDescriptor): Promise<void>

设置媒体输入设备。使用Promise异步回调。


- 本接口不适用于VoIP通话录音，即[SourceType](Enums.md#ZH-CN_TOPIC_0000002553201785__sourcetype8)为SOURCE_TYPE_VOICE_COMMUNICATION的场景不适用。

- 本接口调用前需要先调用[getAvailableDevices](#ZH-CN_TOPIC_0000002522081820__getavailabledevices21)接口查询到当前可用输入设备列表，从列表中选择输入设备。

- 当系统中存在其他更高优先级的应用录音流时，实际使用的输入设备会跟随其他高优先级应用所选的输入设备。

- 应用程序可以监听[currentInputDeviceChanged](#ZH-CN_TOPIC_0000002522081820__oncurrentinputdevicechanged21)事件来获得实际的输入设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputAudioDevice | AudioDeviceDescriptor | 是 | 媒体输入设备。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed, for example, the selected device does not exist. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let data: audio.AudioDeviceDescriptors = audioSessionManager.getAvailableDevices(audio.DeviceUsage.MEDIA_OUTPUT_DEVICES);
  console.info('Succeeded in doing getAvailableDevices.');

  if (data[0]) {
    audioSessionManager.selectMediaInputDevice(data[0]).then(() => {
      console.info('Succeeded in doing selectMediaInputDevice.');
    }).catch((selectErr: BusinessError) => {
      console.error(`Failed to selectMediaInputDevice. Code: ${selectErr.code}, message: ${selectErr.message}`);
    });
  }
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}`);
}
```

#### getSelectedMediaInputDevice21+

getSelectedMediaInputDevice(): AudioDeviceDescriptor

获得通过[selectMediaInputDevice](#ZH-CN_TOPIC_0000002522081820__selectmediainputdevice21)设置的媒体输入设备。如果没有设置，返回一个deviceType属性为INVALID的设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AudioDeviceDescriptor | 媒体输入设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let device: audio.AudioDeviceDescriptor = audioSessionManager.getSelectedMediaInputDevice();
  console.info('Succeeded in doing getSelectedMediaInputDevice.');
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to getSelectedMediaInputDevice. Code: ${error.code}, message: ${error.message}`);
}
```

#### clearSelectedMediaInputDevice21+

clearSelectedMediaInputDevice(): Promise<void>

清空通过[selectMediaInputDevice](#ZH-CN_TOPIC_0000002522081820__selectmediainputdevice21)设置的媒体输入设备。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

audioSessionManager.clearSelectedMediaInputDevice().then(() => {
  console.info('Succeeded in doing clearSelectedMediaInputDevice.');
}).catch((err: BusinessError) => {
  console.error(`Failed to clearSelectedMediaInputDevice. Code: ${err.code}, message: ${err.message}`);
});
```

#### set[BluetoothAndNearlinkPreferredRecordCategory](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__bluetoothandnearlinkpreferredrecordcategory21)21+

set[BluetoothAndNearlinkPreferredRecordCategory](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__bluetoothandnearlinkpreferredrecordcategory21)(category: BluetoothAndNearlinkPreferredRecordCategory): Promise<void>

设置在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。使用Promise异步回调。

- 应用程序可以在蓝牙或星闪连接之前设置此分类，系统将在设备连接时优先使用蓝牙或星闪进行录音。
- 当系统中存在其他更高优先级的应用录音流时，实际使用的输入设备会跟随其他高优先级应用所选的输入设备。

- 应用程序可以监听[currentInputDeviceChanged](#ZH-CN_TOPIC_0000002522081820__oncurrentinputdevicechanged21)事件来获得实际的输入设备。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| category | [BluetoothAndNearlinkPreferredRecordCategory](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__bluetoothandnearlinkpreferredrecordcategory21) | 是 | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const category = audio.BluetoothAndNearlinkPreferredRecordCategory.PREFERRED_LOW_LATENCY;
audioSessionManager.setBluetoothAndNearlinkPreferredRecordCategory(category).then(() => {
  console.info('Succeeded in doing setBluetoothAndNearlinkPreferredRecordCategory.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setBluetoothAndNearlinkPreferredRecordCategory. Code: ${err.code}, message: ${err.message}`);
});
```

#### get[BluetoothAndNearlinkPreferredRecordCategory](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__bluetoothandnearlinkpreferredrecordcategory21)21+

get[BluetoothAndNearlinkPreferredRecordCategory](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__bluetoothandnearlinkpreferredrecordcategory21)(): BluetoothAndNearlinkPreferredRecordCategory

获取通过[setBluetoothAndNearlinkPreferredRecordCategory](#ZH-CN_TOPIC_0000002522081820__setbluetoothandnearlinkpreferredrecordcategory21)设置的在使用蓝牙或星闪进行录音时的设备偏好分类。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BluetoothAndNearlinkPreferredRecordCategory](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__bluetoothandnearlinkpreferredrecordcategory21) | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let category: audio.BluetoothAndNearlinkPreferredRecordCategory = audioSessionManager.getBluetoothAndNearlinkPreferredRecordCategory();
  console.info('Succeeded in doing getBluetoothAndNearlinkPreferredRecordCategory.');
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to getBluetoothAndNearlinkPreferredRecordCategory. Code: ${error.code}, message: ${error.message}`);
}
```

#### on('currentInputDeviceChanged')21+

on(type: 'currentInputDeviceChanged', callback: Callback<CurrentInputDeviceChangedEvent>): void

监听当前输入设备变化事件（当前输入设备发生变化时触发）。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentInputDeviceChanged'，当前输入设备发生变化时，触发该事件。 |
| callback | Callback<CurrentInputDeviceChangedEvent> | 是 | 回调函数，返回当前输入设备信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800101 | Parameter verification failed. |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
import { audio } from '@kit.AudioKit';

let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
  console.info(`reason of currentInputDeviceChanged: ${currentInputDeviceChangedEvent.changeReason} `);
};

audioSessionManager.on('currentInputDeviceChanged', currentInputDeviceChangedCallback);
```

#### off('currentInputDeviceChanged')21+

off(type: 'currentInputDeviceChanged', callback?: Callback<CurrentInputDeviceChangedEvent>): void

取消监听当前输入设备的变化事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'currentInputDeviceChanged'，当前输入设备发生变化时，触发该事件。 |
| callback | Callback<CurrentInputDeviceChangedEvent> | 否 | 回调函数，用于返回当前输入设备变化的信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800301 | Audio client call audio service error, System error. |

**示例：**

```ets
// 取消该事件的所有监听。
audioSessionManager.off('currentInputDeviceChanged');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
  console.info(`reason of currentInputDeviceChanged: ${currentInputDeviceChangedEvent.changeReason} `);
};

audioSessionManager.on('currentInputDeviceChanged', currentInputDeviceChangedCallback);

audioSessionManager.off('currentInputDeviceChanged', currentInputDeviceChangedCallback);
```

**enableMuteSuggestionWhenMixWithOthers23+**

enableMuteSuggestionWhenMixWithOthers(enable: boolean): void

启用混音播放下接收静音播放建议通知功能。

通常，当使用混音模式时，如果其他应用同时播放音频，会和其他应用进行混音播放。但在某些场景下（如游戏或广播），应用自身会通过静音自身的音频以给用户提供更好的体验。

如果启用此功能，当订阅音频会话状态更改事件后静音建议和取消静音建议提示将通过[AudioSessionStateChangedEvent](Interfaces (其他).md#ZH-CN_TOPIC_0000002522241818__audiosessionstatechangedevent20)回调发送。收到静音建议表示其他应用程序开始播放音频，且播放的音频和本应用的音频不能混音。

此功能仅支持已设置[AudioSessionScene](Enums.md#ZH-CN_TOPIC_0000002553201785__audiosessionscene20)并激活模式模式为CONCURRENCY_MIX_WITH_OTHERS的音频会话使用。并且仅在激活音频会话期间生效一次，每次激活音频会话前都必须重新启用。

详细说明请参考[启用混音播放下静音建议通知](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-session-management#启用混音播放下静音建议通知)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Audio.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用混音播放下接收静音播放建议通知功能。true表示启用，false表示不启用。 |

错误码：

以下错误码的详细介绍请参见[Audio错误码](Audio错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 6800103 | Function is called without setting [AudioSessionScene](../enums/Enums.md#ZH-CN_TOPIC_0000002529285695__audiosessionscene20) or called after audio session activation. |
| 6800301 | Audio client call audio service error, system internal error. |

示例：

```ets
audio.getAudioManager().getSessionManager().enableMuteSuggestionWhenMixWithOthers(true);
```

**isOtherMediaPlaying23+**

isOtherMediaPlaying(): boolean

检查是否有其他应用正在播放MUSIC、MOVIE、AUDIOBOOK、GAME四种媒体类型的音频，已激活媒体类型的音频会话也将会被检查。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Multimedia.Audio.Core

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | 是否有其他应用正在播放媒体类型的音频。true表示有，false表示没有。 |

示例：

```ets
let isExistence = audioSessionManager.isOtherMediaPlaying();
```