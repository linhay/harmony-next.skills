# SoundPool (音频池)

音频池提供了短音频的加载、播放、音量设置、循环设置、停止播放、资源卸载等功能。

SoundPool需要和@ohos.multimedia.media配合使用，需要先通过[media.createSoundPool](../misc/Functions.md#ZH-CN_TOPIC_0000002529445861__mediacreatesoundpool10)完成音频池实例的创建。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
```

#### PlayParameters

表示音频池播放参数设置。

通过设置播放相关参数，来控制播放的音量，循环次数，播放优先级等参数。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

名称类型只读可选说明loopnumber否是

设置循环次数。

当loop≥0时，实际播放次数为loop+1。

 当loop＜0时，表示一直循环。

默认值：0，表示仅播放一次。

ratenumber否是设置音频播放的倍速，具体倍速范围参照[AudioRendererRate](../misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiorendererrate8)。默认值：0。leftVolumenumber否是设置左声道音量，设置范围（0.0, 1.0）。默认值：1.0。rightVolumenumber否是设置右声道音量，设置范围（0.0, 1.0）。（当前不支持左右分别设置，将以左声道音量为准）。默认值：1.0。prioritynumber否是音频流播放的优先级，0为最低优先级，数值越大优先级越高，通过相互比较大小确定播放优先级，设置范围为大于等于0的整数。默认值：0。

#### ErrorType20+

枚举，错误类型（用于区分错误发生阶段）。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

名称值说明LOAD_ERROR1表示加载资源时发生错误。PLAY_ERROR2表示播放资源时发生错误。

#### ErrorInfo20+

错误信息。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

名称类型只读可选说明errorCodeT否否错误码。errorCode的类型T为[BusinessError](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__businesserror)类型。errorType[ErrorType](#ZH-CN_TOPIC_0000002529445869__errortype20)否是表示错误发生阶段。soundIdnumber否是发生错误的资源ID，load方法能够获取soundId。streamIdnumber否是发生错误的音频流ID，play方法能够获取streamId。

#### SoundPool

音频池提供了系统声音的加载、播放、音量设置、循环设置、停止播放和资源卸载等功能，在调用SoundPool的接口前，需要先通过[media.createSoundPool](../misc/Functions.md#ZH-CN_TOPIC_0000002529445861__mediacreatesoundpool10)创建实例。

在使用SoundPool实例的方法时，建议开发者注册相关回调，主动获取当前状态变化。

- [on('loadComplete')](#ZH-CN_TOPIC_0000002529445869__onloadcomplete)：监听资源加载完成。
- [on('playFinishedWithStreamId')](#ZH-CN_TOPIC_0000002529445869__onplayfinishedwithstreamid18)：监听播放完成，同时返回播放结束的音频的streamId。
- [on('playFinished')](#ZH-CN_TOPIC_0000002529445869__onplayfinished)：监听播放完成。
- [on('error')](#ZH-CN_TOPIC_0000002529445869__onerror)：监听错误事件。
- [on('errorOccurred')](#ZH-CN_TOPIC_0000002529445869__onerroroccurred20)：监听错误事件，同时返回[errorInfo](#ZH-CN_TOPIC_0000002529445869__errorinfo20)。

#### load

load(uri: string, callback: AsyncCallback<number>): void

加载音频资源。使用callback方式异步获取资源ID，入参uri通过获取文件fd生成以"fd://"开头的文件描述字符串。

该方法不支持加载rawfile目录资源，需要通过[load(fd: number, offset: number, length: number, callback: AsyncCallback<number>): void](#ZH-CN_TOPIC_0000002529445869__load-2)或者[load(fd: number, offset: number, length: number): Promise<number>](#ZH-CN_TOPIC_0000002529445869__load-3)实现。

将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。

同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明uristring是音频文件的加载路径描述，一般以"fd://"开头的文件描述。callbackAsyncCallback<number>是异步音频资源加载返回的资源id，有效值大于0。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by callback.5400103I/O error. Return by callback.5400105Service died. Return by callback.

**示例：**

```ets
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let uri:string = "";
    let file: fileIo.File;
    // 获取fd的uri路径。
    fileIo.open('/test_01.mp3', fileIo.OpenMode.READ_ONLY).then((file_: fileIo.File) => {
      file = file_;
      console.info("file fd: " + file.fd);
      uri = 'fd://' + (file.fd).toString();
      soundPool.load(uri, (error: BusinessError, soundId_: number) => {
        if (error) {
          console.error(`Failed to load soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
        } else {
          console.info(`Succeeded in loading soundPool` + JSON.stringify(soundId_));
        }
      });
    }); // '/test_01.mp3' 作为样例，使用时需要传入文件对应路径。
  }
});
```

#### load

load(uri: string): Promise<number>

加载音频资源。使用Promise方式异步获取资源ID，入参uri通过获取文件fd生成以"fd://"开头的文件描述字符串。

该方法不支持加载rawfile目录资源，需要通过[load(fd: number, offset: number, length: number, callback: AsyncCallback<number>): void](#ZH-CN_TOPIC_0000002529445869__load-2)或者[load(fd: number, offset: number, length: number): Promise<number>](#ZH-CN_TOPIC_0000002529445869__load-3)实现。

将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。

同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明uristring是音频文件的加载路径描述，一般以"fd://"开头的文件描述。

**返回值：**

类型说明Promise<number>Promise对象，返回资源的id，有效值大于0。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by promise.5400103I/O error. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let uri:string = "";
    let soundID: number = 0;
    let file: fileIo.File;
    // 获取fd的uri路径。
    fileIo.open('/test_01.mp3', fileIo.OpenMode.READ_ONLY).then((file_: fileIo.File) => {
      file = file_;
      console.info("file fd: " + file.fd);
      uri = 'fd://' + (file.fd).toString();
      soundPool.load(uri).then((soundId: number) => {
        console.info('Succeeded in loading uri');
        soundID = soundId;
      }, (err: BusinessError) => {
        console.error('Failed to load soundPool and catch error is ' + err.message);
      });
    }); // '/test_01.mp3' 作为样例，使用时需要传入文件对应路径。
  }
});
```

#### load

load(fd: number, offset: number, length: number, callback: AsyncCallback<number>): void

加载音频资源。使用callback方式异步获取资源ID，入参可手动传入资源信息或通过读取应用内置资源自动获取。

将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。

同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明fdnumber是资源句柄，通过[resourceManager.getRawFd](../../modules/ohos/@ohos.resourceManager (资源管理).md#ZH-CN_TOPIC_0000002497445338__getrawfd9)获取。offsetnumber是资源偏移量，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。lengthnumber是资源长度，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。callbackAsyncCallback<number>是获取回调的soundID，有效值大于0。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by callback.5400103I/O error. Return by callback.5400105Service died. Return by callback.

**示例1：**

```ets
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let file: fileIo.File;
    let soundID: number = 0;
    let fileSize: number = 1; // 通过fileIo.stat()获取size值。
    let uri: string = "";
    // 获取fd的描述信息，test_01.mp3不是rawfile目录资源下面的音频。
    fileIo.open('/test_01.mp3', fileIo.OpenMode.READ_ONLY).then((file_: fileIo.File) => {
      file = file_;
      console.info("file fd: " + file.fd);
      uri = 'fd://' + (file.fd).toString();
      soundPool.load(file.fd, 0, fileSize, (error: BusinessError, soundId_: number) => {
        if (error) {
          console.error(`Failed to load soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
        } else {
          soundID = soundId_;
          console.info('Succeeded in loading soundId:' + soundId_);
        }
      });
    }); // '/test_01.mp3' 作为样例，使用时需要传入文件对应路径。
  }
});
```

**示例2：**

```ets
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

function create(context: Context) {
  // 创建soundPool实例。
  let soundPool: media.SoundPool;
  let audioRendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
    rendererFlags: 1
  }
  let soundID: number = 0;
  media.createSoundPool(5, audioRendererInfo, async (error: BusinessError, soundPool_: media.SoundPool) => {
    if (error) {
      console.error(`Failed to createSoundPool`);
      return;
    } else {
      soundPool = soundPool_;
      console.info(`Succeeded in createSoundPool`);
      // test_01.mp3为rawfile目录资源下面的音频。
      let fileDescriptor = await context.resourceManager.getRawFd('test_01.mp3');
      soundPool.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length, (error: BusinessError, soundId_: number) => {
        if (error) {
          console.error(`Failed to load soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
        } else {
          soundID = soundId_;
          console.info('Succeeded in loading soundId:' + soundId_);
        }
      });
    }
  });
}
```

#### load

load(fd: number, offset: number, length: number): Promise<number>

加载音频资源。使用Promise方式异步获取资源ID，入参可手动传入资源信息或通过读取应用内置资源自动获取。

将资源句柄（fd）或加载路径描述（uri）传递给音频池播放器之后，请不要通过该资源句柄或加载路径描述做其他读写操作，包括但不限于将同一个资源句柄或加载路径描述传递给多个音频池播放器。

同一时间通过同一个资源句柄或加载路径描述读写文件时存在竞争关系，将导致播放异常。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明fdnumber是资源句柄，通过[resourceManager.getRawFd](../../modules/ohos/@ohos.resourceManager (资源管理).md#ZH-CN_TOPIC_0000002497445338__getrawfd9)获取。offsetnumber是资源偏移量，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。lengthnumber是资源长度，需要基于预置资源的信息输入，非法值会造成音视频资源解析错误。

**返回值：**

类型说明Promise<number>Promise对象，返回soundID，有效值大于0。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by promise.5400103I/O error. Return by promise.5400105Service died. Return by promise.

**示例1：**

```ets
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let file: fileIo.File;
    let soundID: number = 0;
    let fileSize: number = 1; // 通过fileIo.stat()获取size值。
    let uri: string = "";
    // 获取fd的描述信息，test_01.mp3不是rawfile目录资源下面的音频。
    fileIo.open('/test_01.mp3', fileIo.OpenMode.READ_ONLY).then((file_: fileIo.File) => {
      file = file_;
      console.info("file fd: " + file.fd);
      uri = 'fd://' + (file.fd).toString();
      soundPool.load(file.fd, 0, fileSize).then((soundId: number) => {
        console.info('Succeeded in loading soundpool');
        soundID = soundId;
      }, (err: BusinessError) => {
        console.error('Failed to load soundpool and catch error is ' + err.message);
      });
    });
  }
});
```

**示例2：**

```ets
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';

function create(context: Context) {
  // 创建soundPool实例。
  let soundPool: media.SoundPool;
  let audioRendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
    rendererFlags: 1
  }
  let soundID: number = 0;
  media.createSoundPool(5, audioRendererInfo, async (error: BusinessError, soundPool_: media.SoundPool) => {
    if (error) {
      console.error(`Failed to createSoundPool`);
      return;
    } else {
      soundPool = soundPool_;
      console.info(`Succeeded in createSoundPool`);
      // test_01.mp3为rawfile目录资源下面的音频。
      let fileDescriptor = await context.resourceManager.getRawFd('test_01.mp3');
      soundPool.load(fileDescriptor.fd, fileDescriptor.offset, fileDescriptor.length).then((soundId: number) => {
        console.info('Succeeded in loading soundpool');
        soundID = soundId;
      }, (err: BusinessError) => {
        console.error('Failed to load soundpool and catch error is ' + err.message);
      });
    }
  });
}
```

#### play

play(soundID: number, params: PlayParameters, callback: AsyncCallback<number>): void

播放音频资源，获取音频流streamID。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明soundIDnumber是资源ID，通过load方法获取。params[PlayParameters](#ZH-CN_TOPIC_0000002529445869__playparameters)是play播放相关参数的设置。callbackAsyncCallback<number>是获取回调的音频流ID，有效值大于0。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback.5400102Operation not allowed. Return by callback.5400105Service died. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let soundID: number = 0;
    let streamID: number = 0;
    let playParameters: media.PlayParameters = {
      loop: 3, // 循环3次。
      rate: audio.AudioRendererRate.RENDER_RATE_NORMAL, // 正常倍速。
      leftVolume: 0.5, // range = 0.0-1.0
      rightVolume: 0.5, // range = 0.0-1.0
      priority: 0, // 最低优先级。
    }
    soundPool.play(soundID, playParameters, (error: BusinessError, streamId: number) => {
      if (error) {
        console.error(`Failed to play soundpool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        streamID = streamId;
        console.info('Succeeded in playing soundpool, streamId:' + streamId);
      }
    });
  }
});
```

#### play

play(soundID: number, callback: AsyncCallback<number>): void

使用默认参数播放音频资源，获取音频流streamID。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明soundIDnumber是资源ID，通过load方法获取。callbackAsyncCallback<number>是获取回调的音频流ID，有效值大于0。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback.5400102Operation not allowed. Return by callback.5400105Service died. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let soundID: number = 0;
    let streamID: number = 0;
    soundPool.play(soundID,  (error: BusinessError, streamId: number) => {
      if (error) {
        console.error(`Failed to play soundpool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        streamID = streamId;
        console.info('Succeeded in playing soundpool, streamId:' + streamId);
      }
    });
  }
});
```

#### play

play(soundID: number, params?: PlayParameters): Promise<number>

播放音频资源，获取音频流streamID。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明soundIDnumber是资源ID，通过load方法获取。params[PlayParameters](#ZH-CN_TOPIC_0000002529445869__playparameters)否play播放相关参数的设置。

**返回值：**

类型说明Promise<number>Promise对象，返回音频流ID，有效值大于0。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise.5400102Operation not allowed. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let soundID: number = 0;
    let streamID: number = 0;
    let playParameters: media.PlayParameters = {
      loop: 3, // 循环4次。
      rate: audio.AudioRendererRate.RENDER_RATE_NORMAL, // 正常倍速。
      leftVolume: 0.5, // range = 0.0-1.0。
      rightVolume: 0.5, // range = 0.0-1.0。
      priority: 0, // 最低优先级。
    }

    soundPool.play(soundID, playParameters).then((streamId: number) => {
      console.info('Succeeded in playing soundpool');
      streamID = streamId;
    },(err: BusinessError) => {
      console.error('Failed to play soundpool and catch error is ' + err.message);
    });
  }
});
```

#### stop

stop(streamID: number, callback: AsyncCallback<void>): void

停止播放音频资源。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明streamIDnumber是音频流ID，通过play方法获取。callbackAsyncCallback<void>是异步音频池stop的回调方法。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback.5400102Operation not allowed. Return by callback.5400105Service died. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let streamID: number = 0;
    // 先调用play方法给拿到对应的streamID。
    soundPool.stop(streamID, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to stop soundpool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        console.info('Succeeded in stopping soundpool');
      }
    })
  }
});
```

#### stop

stop(streamID: number): Promise<void>

停止streamID对应的音频播放。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明streamIDnumber是音频流ID，通过play方法获取。

**返回值：**

类型说明Promise<void>Promise方式返回，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise.5400102Operation not allowed. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let streamID: number = 0;
    // 先调用play方法给拿到对应的streamID。
    soundPool.stop(streamID).then(() => {
      console.info('Succeeded in stopping soundpool');
    }, (err: BusinessError) => {
      console.error('Failed to stop soundpool and catch error is ' + err.message);
    });
  }
});
```

#### setLoop

setLoop(streamID: number, loop: number, callback: AsyncCallback<void>): void;

设置循环模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明streamIDnumber是音频流ID，通过play方法获取。loopnumber是

设置循环次数。

当loop≥0时，实际播放次数为loop+1。

 当loop＜0时，表示一直循环。

callbackAsyncCallback<void>是异步setLoop的回调方法。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback.5400102Operation not allowed. Return by callback.5400105Service died. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let streamID: number = 0;
    // 先通过调用play方法获取到对应的streamID。
    // 设置循环2次。
    soundPool.setLoop(streamID, 2, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to setLoop soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        console.info('Succeeded in setLoopping soundpool, streamID:' + streamID);
      }
    });
  }
});
```

#### setLoop

setLoop(streamID: number, loop: number): Promise<void>

设置循环模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明streamIDnumber是音频流ID，通过play方法获取。loopnumber是

设置循环次数。

当loop≥0时，实际播放次数为loop+1。

 当loop＜0时，表示一直循环。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise.5400102Operation not allowed. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let streamID: number = 0;
    // 先通过调用play方法获取到对应的streamID。
    // 设置循环1次。
    soundPool.setLoop(streamID, 1).then(() => {
      console.info('Succeeded in setLoopping soundpool, streamID:' + streamID);
    }).catch((err: BusinessError) => {
      console.error('Failed to setLoop soundPool and catch error is ' + err.message);
    });
  }
});
```

#### setPriority

setPriority(streamID: number, priority: number, callback: AsyncCallback<void>): void

设置音频流播放的优先级。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明streamIDnumber是音频流ID，通过play方法获取。prioritynumber是优先级，0表示最低优先级。设置范围为大于等于0的整数。callbackAsyncCallback<void>是异步音频池setPriority方法的回调方法。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback.5400102Operation not allowed. Return by callback.5400105Service died. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let streamID: number = 0;
    // 先调用play方法获取到对应资源的streamID。
    // 给对应的streamID资源设置优先级为1。
    soundPool.setPriority(streamID, 1, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to setPriority soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        console.info('Succeeded in setPriority soundpool, streamID:' + streamID);
      }
    });
  }
});
```

#### setPriority

setPriority(streamID: number, priority: number): Promise<void>

设置音频流优先级。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明streamIDnumber是音频流ID，通过play方法获取。prioritynumber是优先级，0表示最低优先级。设置范围为大于等于0的整数。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise.5400102Operation not allowed. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let streamID: number = 0;
    // 先调用play方法获取到对应资源的streamID。
    // 给对应的streamID资源设置优先级为1。

    soundPool.setPriority(streamID, 1).then(() => {
      console.info('Succeeded in setPriority soundpool');
    }, (err: BusinessError) => {
      console.error('Failed to setPriority soundPool and catch error is ' + err.message);
    });
  }
});
```

#### setRate

setRate(streamID: number, rate: audio.AudioRendererRate, callback: AsyncCallback<void>): void

设置音频流播放速率。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明streamIDnumber是音频流ID，通过play方法获取。rate[audio.AudioRendererRate](../misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiorendererrate8)是音频rate相关参数。callbackAsyncCallback<void>是异步音频池setRate方法的回调方法。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback.5400102Operation not allowed. Return by callback.5400105Service died. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let streamID: number = 0;
    let selectedAudioRendererRate: audio.AudioRendererRate = audio.AudioRendererRate.RENDER_RATE_NORMAL; // 默认正常速率
    // 先调用play方法获取到对应资源的streamID。
    soundPool.setRate(streamID, selectedAudioRendererRate, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to setRate soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        console.info('Succeeded in setRate success, streamID:' + streamID);
      }
    })
  }
});
```

#### setRate

setRate(streamID: number, rate: audio.AudioRendererRate): Promise<void>

设置音频流的播放速率。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明streamIDnumber是音频流ID，通过play方法获取。rate[audio.AudioRendererRate](../misc/Enums.md#ZH-CN_TOPIC_0000002529285695__audiorendererrate8)是音频rate相关参数。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise.5400102Operation not allowed. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let streamID: number = 0;
    let selectedAudioRendererRate: audio.AudioRendererRate = audio.AudioRendererRate.RENDER_RATE_NORMAL; // 默认正常速率
    // 先调用play方法获取到对应资源的streamID。
    soundPool.setRate(streamID, selectedAudioRendererRate).then(() => {
      console.info('Succeeded in setRate soundpool');
    }, (err: BusinessError) => {
      console.error('Failed to setRate soundpool and catch error is ' + err.message);
    });
  }
});
```

#### setVolume

setVolume(streamID: number, leftVolume: number, rightVolume: number, callback: AsyncCallback<void>): void

设置音频流播放音量。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明streamIDnumber是音频流ID，通过play方法获取。leftVolumenumber是左声道音量，设置范围为0.0-1.0之间。rightVolumenumber是右声道音量，设置范围为0.0-1.0之间，当前右声道设置无效，以左声道为准。callbackAsyncCallback<void>是异步音频池setVolume方法的回调方法。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by callback.5400102Operation not allowed. Return by callback.5400105Service died. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let streamID: number = 0;
    // 先调用play方法获取到对应资源的streamID。
    // 设置音量为0.5。
    soundPool.setVolume(streamID, 0.5, 0.5, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to setVolume soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        console.info('Succeeded in setVolume soundpool, streamID:' + streamID);
      }
    })
  }
});
```

#### setVolume

setVolume(streamID: number, leftVolume: number, rightVolume: number): Promise<void>

设置音频流的播放音量。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明streamIDnumber是音频流ID，通过play方法获取。leftVolumenumber是左声道音量，设置范围为0.0-1.0之间。rightVolumenumber是右声道音量，设置范围为0.0-1.0之间，当前右声道设置无效，以左声道为准。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. Return by promise.5400102Operation not allowed. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let streamID: number = 0;
    // 先调用play方法获取到对应资源的streamID。

    soundPool.setVolume(streamID, 0.5, 0.5).then(() => {
      console.info('Succeeded in setVolume soundpool');
    }, (err: BusinessError) => {
      console.error('Failed to setVolume soundPool and catch error is ' + err.message);
    });
  }
});
```

#### unload

unload(soundID: number, callback: AsyncCallback<void>): void

卸载音频资源。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明soundIDnumber是资源ID，通过load方法获取。callbackAsyncCallback<void>是异步音频池unload方法的回调方法。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by callback.5400103I/O error. Return by callback.5400105Service died. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let soundID: number = 0;
    // 先调用load方法获取到对应资源的soundID。
    soundPool.unload(soundID, (error: BusinessError) => {
      if (error) {
        console.error(`Failed to unload soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        console.info('Succceeded in unload soundPool');
      }
    })
  }
});
```

#### unload

unload(soundID: number): Promise<void>

卸载音频资源。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明soundIDnumber是资源ID，通过load方法获取。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by promise.5400103I/O error. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    let soundID: number = 0;
    // 先调用load方法获取到对应资源的soundID。

    soundPool.unload(soundID).then(() => {
      console.info('Succceeded in unload soundPool');
    }, (err: BusinessError) => {
      console.error('Failed to unload soundPool and catch error is ' + err.message);
    });
  }
});
```

#### release

release(callback: AsyncCallback<void>): void

释放音频池实例。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是异步音频池release方法的回调方法。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400105Service died. Return by callback.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    soundPool.release((error: BusinessError) => {
      if (error) {
        console.error(`Failed to release soundPool: errCode is ${error.code}, errMessage is ${error.message}`);
      } else {
        console.info('Succeeded in releasing soundPool');
      }
    })
  }
});
```

#### release

release(): Promise<void>

释放音频池实例。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    soundPool.release().then(() => {
      console.info('Succeeded in releasing soundPool');
    }, (err: BusinessError) => {
      console.error('Failed to release soundPool and catch error is ' + err.message);
    });
  }
});
```

#### on('loadComplete')

on(type: 'loadComplete', callback: Callback<number>): void

音频池资源加载完成监听。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明typestring是支持的事件：'loadComplete'，对应的ID加载完成会触发此回调。callbackCallback<number>是对应资源加载完成的资源ID。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    soundPool.on('loadComplete', (soundId: number) => {
      console.info('Succeeded in loadComplete, soundId：' + soundId);
    })
  }
});
```

#### off('loadComplete')

off(type: 'loadComplete'): void

取消监听资源的加载完成。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明typestring是取消注册的事件：'loadComplete'。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    soundPool.off('loadComplete');
  }
});
```

#### on('playFinishedWithStreamId')18+

on(type: 'playFinishedWithStreamId', callback: Callback<number>): void

音频池资源播放完成监听，同时返回播放结束的音频的streamId。

当仅单独注册[on('playFinished')](#ZH-CN_TOPIC_0000002529445869__onplayfinished)事件回调或者[on('playFinishedWithStreamId')](#ZH-CN_TOPIC_0000002529445869__onplayfinishedwithstreamid18)事件回调时，当音频播放完成的时候，都会触发注册的回调。

当同时注册[on('playFinished')](#ZH-CN_TOPIC_0000002529445869__onplayfinished)事件回调和[on('playFinishedWithStreamId')](#ZH-CN_TOPIC_0000002529445869__onplayfinishedwithstreamid18)事件回调时，当音频播放完成的时候，仅会触发'playFinishedWithStreamId'事件回调，不会触发'playFinished'事件回调。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明typestring是支持的事件：'playFinishedWithStreamId'，音频流播放完成会触发此回调，并返回播放完成的音频的streamId。callbackCallback<number>是异步'playFinishedWithStreamId'的回调方法。返回播放完成的音频的streamId。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool_: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
  } else {
    soundPool_ = soundPool;
    console.info(`Succeeded in createSoundPool`);
    soundPool_.on('playFinishedWithStreamId', (streamId) => {
      console.info('The stream with streamId: ' + streamId + ' has finished playing.');
    });
  }
});
```

#### off('playFinishedWithStreamId')18+

off(type: 'playFinishedWithStreamId'): void

取消监听音频池资源播放完成。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明typestring是取消注册的事件：'playFinishedWithStreamId'。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool_: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
  } else {
    soundPool_ = soundPool;
    console.info(`Succeeded in createSoundPool`);
    soundPool_.off('playFinishedWithStreamId');
  }
});
```

#### on('playFinished')

on(type: 'playFinished', callback: Callback<void>): void

音频池资源播放完成监听。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明typestring是支持的事件：'playFinished'，音频流播放完成会触发此回调。callbackCallback<void>是异步'playFinished'的回调方法。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    soundPool.on('playFinished', () => {
      console.info('Succeeded in playFinished');
    });
  }
});
```

#### off('playFinished')

off(type: 'playFinished'): void

取消监听音频池资源播放完成。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明typestring是取消注册的事件：'playFinished'。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    soundPool.off('playFinished');
  }
});
```

#### on('error')

on(type: 'error', callback: ErrorCallback): void

监听[SoundPool](#ZH-CN_TOPIC_0000002529445869__soundpool)的错误事件，该事件仅用于错误提示。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明typestring是错误事件回调类型，支持的事件：'error'，用户操作和系统都会触发此事件。callbackErrorCallback是错误事件回调方法：使用播放器的过程中发生错误，会提供错误码ID和错误信息。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    soundPool.on('error', (error: BusinessError) => {
      console.error('error happened,and error message is :' + error.message);
      console.error('error happened,and error code is :' + error.code);
    })
  }
});
```

#### off('error')

off(type: 'error'): void

取消监听音频池的错误事件。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明typestring是错误事件回调类型，取消注册的事件：'error'。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    soundPool.off('error');
  }
});
```

#### on('errorOccurred')20+

on(type: 'errorOccurred', callback: Callback<ErrorInfo>): void

监听[SoundPool](#ZH-CN_TOPIC_0000002529445869__soundpool)的错误事件，并返回包含错误码、错误发生阶段、资源ID和音频流ID的[ErrorInfo](#ZH-CN_TOPIC_0000002529445869__errorinfo20)。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'errorOccurred'，当用户或系统操作导致错误，触发该事件。callbackCallback<[ErrorInfo](#ZH-CN_TOPIC_0000002529445869__errorinfo20)>是错误事件回调方法。在使用播放器的过程中发生错误时，提供错误信息[ErrorInfo](#ZH-CN_TOPIC_0000002529445869__errorinfo20)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    soundPool.on('errorOccurred', (errorInfo) => {
      console.error('error happened,and error message is :' + errorInfo.errorCode.message);
      console.error('error happened,and error code is :' + errorInfo.errorCode.code);
      console.error('error happened,and errorType is :' + errorInfo.errorType);
      console.error('error happened,and soundId is :' + errorInfo.soundId);
      console.error('error happened,and streamId is :' + errorInfo.streamId);
    })
  }
});
```

#### off('errorOccurred')20+

 off(type: 'errorOccurred', callback?: Callback<ErrorInfo>): void

取消监听音频池的错误事件。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**参数：**

参数名类型必填说明typestring是事件回调类型，取消注册的事件为'errorOccurred'。callbackCallback<[ErrorInfo](#ZH-CN_TOPIC_0000002529445869__errorinfo20)>否错误事件回调方法。在使用播放器的过程中发生错误时，提供错误信息[ErrorInfo](#ZH-CN_TOPIC_0000002529445869__errorinfo20)。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';

// 创建soundPool实例。
let soundPool: media.SoundPool;
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
  rendererFlags: 1
}
media.createSoundPool(5, audioRendererInfo, (error: BusinessError, soundPool_: media.SoundPool) => {
  if (error) {
    console.error(`Failed to createSoundPool`);
    return;
  } else {
    soundPool = soundPool_;
    console.info(`Succeeded in createSoundPool`);
    soundPool.off('errorOccurred');
  }
});
```