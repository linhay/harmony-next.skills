# Interface (AVCastController)

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 10开始支持。

在投播建立后，调用[avSession.getAVCastController](Interface (AVSession).md#ZH-CN_TOPIC_0000002497605762__getavcastcontroller10)后，返回会话控制器实例。控制器可查看会话ID，并可完成对会话发送命令及事件，获取会话元数据，播放状态信息等操作。

#### 导入模块

```ets
import { avSession } from '@kit.AVSessionKit';
```

#### getAVPlaybackState10+

getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void

获取当前的远端播放状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)>是回调函数，返回远端播放状态。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.getAVPlaybackState((err: BusinessError, state: avSession.AVPlaybackState) => {
  if (err) {
    console.error(`getAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('getAVPlaybackState : SUCCESS');
  }
});
```

#### getAVPlaybackState10+

getAVPlaybackState(): Promise<AVPlaybackState>

获取当前的远端播放状态。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

类型说明Promise<[AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)>Promise对象。返回远端播放状态。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.getAVPlaybackState().then((state: avSession.AVPlaybackState) => {
  console.info('getAVPlaybackState : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`getAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getSupportedDecoders19+

getSupportedDecoders(): Promise<Array<DecoderType>>

获取当前远端设备的解码方式。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

类型说明Promise<Array<[DecoderType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__decodertype19)>>Promise对象。返回远端设备所支持的解码能力列表。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.getSupportedDecoders().then((decoderTypes: avSession.DecoderType[]) => {
  console.info(`getSupportedDecoders : SUCCESS : decoderTypes.length : ${decoderTypes.length}`);
  if (decoderTypes.length > 0 ) {
    console.info(`getSupportedDecoders : SUCCESS : decoderTypes[0] : ${decoderTypes[0]}`);
  }
}).catch((err: BusinessError) => {
  console.error(`getSupportedDecoders BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getRecommendedResolutionLevel19+

getRecommendedResolutionLevel(decoderType: DecoderType): Promise<ResolutionLevel>

通过传递解码方式，获取推荐的分辨率。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明decoderType[DecoderType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__decodertype19)是

设备所支持的解码格式。

设备所支持的解码格式包括：

'OH_AVCODEC_MIMETYPE_VIDEO_AVC'：VIDEO AVC，

'OH_AVCODEC_MIMETYPE_VIDEO_HEVC'：VIDEO HEVC，

'OH_AVCODEC_MIMETYPE_AUDIO_VIVID'：AUDIO AV3A。

**返回值：**

类型说明Promise<[ResolutionLevel](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__resolutionlevel19)>Promise对象。返回远端设备推荐的分辨率。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let decoderType = avSession.DecoderType.OH_AVCODEC_MIMETYPE_VIDEO_AVC;
aVCastController.getRecommendedResolutionLevel(decoderType).then((resolutionLevel: avSession.ResolutionLevel) => {
  console.info('getRecommendedResolutionLevel successfully');
}).catch((err: BusinessError) => {
  console.error(`getRecommendedResolutionLevel BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getSupportedHdrCapabilities19+

getSupportedHdrCapabilities(): Promise<Array<hdrCapability.HDRFormat>>

获取当前的远端设备所支持的HDR能力。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

类型说明Promise<Array<[hdrCapability.HDRFormat](../../modules/ohos/@ohos.graphics.hdrCapability (HDR能力).md#ZH-CN_TOPIC_0000002529445951__hdrformat)>>Promise对象。返回远端设备所支持的HDR能力。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import type hdrCapability from './@ohos.graphics.hdrCapability';

aVCastController.getSupportedHdrCapabilities().then((hdrFormats: hdrCapability.HDRFormat[]) => {
  console.info(`getSupportedHdrCapabilities : SUCCESS : hdrFormats.length : ${hdrFormats.length}`);
  if (hdrFormats.length > 0 ) {
    console.info(`getSupportedHdrCapabilities : SUCCESS : descriptors[0] : ${hdrFormats[0]}`);
  }
}).catch((err: BusinessError) => {
  console.error(`getSupportedHdrCapabilities BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getSupportedPlaySpeeds19+

getSupportedPlaySpeeds(): Promise<Array<number>>

获取当前的远端设备所支持倍速播放列表。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

类型说明Promise<Array<number>>Promise对象。返回远端设备所支持的倍速播放列表。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.getSupportedPlaySpeeds().then((nums: number[]) => {
  console.info(`getSupportedPlaySpeeds : SUCCESS : hdrFormats.length : ${nums.length}`);
  if (nums.length > 0 ) {
    console.info(`getSupportedPlaySpeeds : SUCCESS : descriptors[0] : ${nums[0]}`);
  }
}).catch((err: BusinessError) => {
  console.error(`getSupportedPlaySpeeds BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### sendControlCommand10+

sendControlCommand(command: AVCastControlCommand): Promise<void>

通过控制器发送命令到其对应的会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明command[AVCastControlCommand](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcastcontrolcommand10)是会话的相关命令和命令相关参数。

**返回值：**

类型说明Promise<void>Promise对象。当命令发送成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600105Invalid session command.6600109The remote connection is not established.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avCommand: avSession.AVCastControlCommand = {command:'play'};
aVCastController.sendControlCommand(avCommand).then(() => {
  console.info('SendControlCommand successfully');
}).catch((err: BusinessError) => {
  console.error(`SendControlCommand BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### sendControlCommand10+

sendControlCommand(command: AVCastControlCommand, callback: AsyncCallback<void>): void

通过会话控制器发送命令到其对应的会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明command[AVCastControlCommand](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcastcontrolcommand10)是会话的相关命令和命令相关参数。callbackAsyncCallback<void>是回调函数。当命令发送成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600105Invalid session command.6600109The remote connection is not established.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avCommand: avSession.AVCastControlCommand = {command:'play'};
aVCastController.sendControlCommand(avCommand, (err: BusinessError) => {
  if (err) {
    console.error(`SendControlCommand BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SendControlCommand successfully');
  }
});
```

#### sendCustomData20+

sendCustomData(data: Record<string, Object>): Promise<void>

发送私有数据到远端设备。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明dataRecord<string, Object>是

应用程序填充的自定义数据。

服务端仅解析key：string为'customData'，且Object为string类型的对象。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.sendCustomData({customData : "This is custom data"});
```

#### prepare10+

prepare(item: AVQueueItem, callback: AsyncCallback<void>): void

准备播放媒体资源，即进行播放资源的加载和缓冲。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明item[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)是播放列表中单项的相关属性。callbackAsyncCallback<void>是回调函数。当命令发送成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600109The remote connection is not established.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 设置播放参数，开始播放。
let playItem: avSession.AVQueueItem = {
  itemId: 0,
  description: {
    assetId: '12345',
    mediaType: 'AUDIO',
    mediaUri: 'http://resource1_address',
    mediaSize: 12345,
    startPosition: 0,
    duration: 0,
    artist: 'mysong',
    albumTitle: 'song1_title',
    albumCoverUri: "http://resource1_album_address",
    lyricUri: "http://resource1_lyric_address",
    appName: 'MyMusic'
  }
};
// 准备播放，这个不会触发真正的播放，会进行加载和缓冲。
aVCastController.prepare(playItem, (err: BusinessError) => {
  if (err) {
    console.error(`prepare BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('prepare successfully');
  }
});
```

#### prepare10+

prepare(item: AVQueueItem): Promise<void>

准备播放媒体资源，即进行播放资源的加载和缓冲。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明item[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)是播放列表中单项的相关属性。

**返回值：**

类型说明Promise<void>Promise对象。当命令发送成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600109The remote connection is not established.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 设置播放参数，开始播放。
let playItem: avSession.AVQueueItem = {
  itemId: 0,
  description: {
    assetId: '12345',
    mediaType: 'AUDIO',
    mediaUri: 'http://resource1_address',
    mediaSize: 12345,
    startPosition: 0,
    duration: 0,
    artist: 'mysong',
    albumTitle: 'song1_title',
    albumCoverUri: "http://resource1_album_address",
    lyricUri: "http://resource1_lyric_address",
    appName: 'MyMusic'
  }
};
// 准备播放，这个不会触发真正的播放，会进行加载和缓冲。
aVCastController.prepare(playItem).then(() => {
  console.info('prepare successfully');
}).catch((err: BusinessError) => {
  console.error(`prepare BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### start10+

start(item: AVQueueItem, callback: AsyncCallback<void>): void

启动播放某个媒体资源。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明item[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)是播放列表中单项的相关属性。callbackAsyncCallback<void>是回调函数。当命令发送成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600109The remote connection is not established.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 设置播放参数，开始播放。
let playItem: avSession.AVQueueItem = {
  itemId: 0,
  description: {
    assetId: '12345',
    mediaType: 'AUDIO',
    mediaUri: 'http://resource1_address',
    mediaSize: 12345,
    startPosition: 0,
    duration: 0,
    artist: 'mysong',
    albumTitle: 'song1_title',
    albumCoverUri: "http://resource1_album_address",
    lyricUri: "http://resource1_lyric_address",
    appName: 'MyMusic'
  }
};

// 启动播放。
aVCastController.start(playItem, (err: BusinessError) => {
  if (err) {
    console.error(`start BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('start successfully');
  }
});
```

#### start10+

start(item: AVQueueItem): Promise<void>

启动播放某个媒体资源。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明item[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)是播放列表中单项的相关属性。

**返回值：**

类型说明Promise<void>Promise对象。当命令发送成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600109The remote connection is not established.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 设置播放参数，开始播放。
let playItem: avSession.AVQueueItem = {
  itemId: 0,
  description: {
    assetId: '12345',
    mediaType: 'AUDIO',
    mediaUri: 'http://resource1_address',
    mediaSize: 12345,
    startPosition: 0,
    duration: 0,
    artist: 'mysong',
    albumTitle: 'song1_title',
    albumCoverUri: "http://resource1_album_address",
    lyricUri: "http://resource1_lyric_address",
    appName: 'MyMusic'
  }
};
// 启动播放。
aVCastController.start(playItem).then(() => {
  console.info('start successfully');
}).catch((err: BusinessError) => {
  console.error(`start BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getCurrentItem10+

getCurrentItem(callback: AsyncCallback<AVQueueItem>): void

获取当前投播的资源信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>是回调函数。当命令发送成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.getCurrentItem((err: BusinessError, value: avSession.AVQueueItem) => {
  if (err) {
    console.error(`getCurrentItem BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('getCurrentItem successfully');
  }
});
```

#### getCurrentItem10+

getCurrentItem(): Promise<AVQueueItem>

获取当前投播的资源信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

类型说明Promise<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>Promise对象，返回当前的播放资源，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.getCurrentItem().then((value: avSession.AVQueueItem) => {
  console.info('getCurrentItem successfully');
}).catch((err: BusinessError) => {
  console.error(`getCurrentItem BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getValidCommands11+

getValidCommands(callback: AsyncCallback<Array<AVCastControlCommandType>>): void

获取当前支持的命令。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[AVCastControlCommandType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avcastcontrolcommandtype10)>>是回调函数。返回当前支持的命令。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.getValidCommands((err: BusinessError, state: avSession.AVCastControlCommandType[]) => {
  if (err) {
    console.error(`getValidCommands BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('getValidCommands successfully');
  }
});
```

#### getValidCommands11+

getValidCommands(): Promise<Array<AVCastControlCommandType>>

获取当前支持的命令。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

类型说明Promise<Array<[AVCastControlCommandType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avcastcontrolcommandtype10)>>Promise对象，返回当前支持的命令。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.getValidCommands().then((state: avSession.AVCastControlCommandType[]) => {
  console.info('getValidCommands successfully');
}).catch((err: BusinessError) => {
  console.error(`getValidCommands BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### processMediaKeyResponse12+

processMediaKeyResponse(assetId: string, response: Uint8Array): Promise<void>

在线DRM资源投播时，处理许可证响应。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明assetIdstring是媒体ID。responseUint8Array是许可证响应。

**返回值：**

类型说明Promise<void>Promise对象，当处理许可证响应成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.

**示例：**

```ets
let keyRequestCallback: avSession.KeyRequestCallback = async(assetId: string, requestData: Uint8Array) => {
  // 根据assetId获取对应的DRM url。
  let drmUrl = 'http://license.xxx.xxx.com:8080/drmproxy/getLicense';
  // 从服务器获取许可证，需要开发者根据实际情况进行赋值。
  let licenseResponseData: Uint8Array = new Uint8Array();
  console.info(`Succeeded in get license by ${drmUrl}.`);
  aVCastController.processMediaKeyResponse(assetId, licenseResponseData);
}
```

#### release11+

release(callback: AsyncCallback<void>): void

销毁当前controller，结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当命令执行成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.release((err: BusinessError) => {
  if (err) {
    console.error(`release BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('release successfully');
  }
});
```

#### release11+

release(): Promise<void>

销毁当前controller。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

类型说明Promise<void>Promise对象，controller销毁成功，无结果返回，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.release().then(() => {
  console.info('release successfully');
}).catch((err: BusinessError) => {
  console.error(`release BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### on('playbackStateChange')10+

on(type: 'playbackStateChange', filter: Array<string> | 'all', callback: (state: AVPlaybackState) => void): void

设置播放状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'playbackStateChange'：当播放状态变化时，触发该事件。filterArray<string>|'all'是

'all' 表示关注播放状态所有字段变化；Array<string> 表示关注Array中的字段变化。

API version 20开始发生兼容变更，在API version 19及之前filter参数类型为：Array<keyof AVPlaybackState> | 'all'。

callback(state: [AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)) => void是回调函数，参数state是变化后的播放状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.on('playbackStateChange', 'all', (playbackState: avSession.AVPlaybackState) => {
  console.info(`on playbackStateChange state : ${playbackState.state}`);
});

let playbackFilter: Array<keyof avSession.AVPlaybackState> = ['state', 'speed', 'loopMode'];
aVCastController.on('playbackStateChange', playbackFilter, (playbackState: avSession.AVPlaybackState) => {
  console.info(`on playbackStateChange state : ${playbackState.state}`);
});
```

#### off('playbackStateChange')10+

off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void): void

取消播放状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'playbackStateChange'。callback(state: [AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)) => void否

回调函数，参数state是变化后的播放状态。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.off('playbackStateChange');
```

#### on('mediaItemChange')10+

on(type: 'mediaItemChange', callback: Callback<AVQueueItem>): void

设置投播当前播放媒体内容的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'mediaItemChange'：当播放的媒体内容变化时，触发该事件。callbackCallback<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>是回调函数，参数AVQueueItem是当前正在播放的媒体内容。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.on('mediaItemChange', (item: avSession.AVQueueItem) => {
  console.info(`on mediaItemChange state : ${item.itemId}`);
});
```

#### off('mediaItemChange')10+

off(type: 'mediaItemChange'): void

取消设置投播当前播放媒体内容事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'mediaItemChange'。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.off('mediaItemChange');
```

#### on('playNext')10+

on(type: 'playNext', callback: Callback<void>): void

设置播放下一首资源的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'playNext'：当播放下一首状态变化时，触发该事件。callbackCallback<void>是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.on('playNext', () => {
  console.info('on playNext');
});
```

#### off('playNext')10+

off(type: 'playNext'): void

取消设置播放下一首资源事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'playNext'。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.off('playNext');
```

#### on('playPrevious')10+

on(type: 'playPrevious', callback: Callback<void>): void

设置播放上一首资源的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'playPrevious'：当播放上一首状态变化时，触发该事件。callbackCallback<void>是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.on('playPrevious', () => {
  console.info('on playPrevious');
});
```

#### off('playPrevious')10+

off(type: 'playPrevious'): void

取消设置播放上一首资源事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'playPrevious'。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.off('playPrevious');
```

#### on('requestPlay')11+

on(type: 'requestPlay', callback: Callback<AVQueueItem>): void

设置请求播放的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'requestPlay'：当请求播放状态变化时，触发该事件。callbackCallback<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>是回调函数，参数AVQueueItem是当前正在播放的媒体内容。当监听事件注册成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.on('requestPlay', (item: avSession.AVQueueItem) => {
  console.info(`on requestPlay state : ${item.itemId}`);
});
```

#### off('requestPlay')11+

off(type: 'requestPlay', callback?: Callback<AVQueueItem>): void

取消设置请求播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'requestPlay'。callbackCallback<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>否回调函数，参数AVQueueItem是当前正在播放的媒体内容。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.off('requestPlay');
```

#### on('endOfStream')11+

on(type: 'endOfStream', callback: Callback<void>): void

设置播放结束的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'endOfStream'：当资源播放结束时，触发该事件。callbackCallback<void>是回调函数。当监听事件注册成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.on('endOfStream', () => {
  console.info('on endOfStream');
});
```

#### off('endOfStream')11+

off(type: 'endOfStream', callback?: Callback<void>): void

取消设置播放结束事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'endOfStream'。callbackCallback<void>否回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.off('endOfStream');
```

#### on('seekDone')10+

on(type: 'seekDone', callback: Callback<number>): void

设置seek结束的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'seekDone'：当seek结束时，触发该事件。callbackCallback<number>是回调函数，返回seek后播放的位置。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.on('seekDone', (pos: number) => {
  console.info(`on seekDone pos：${pos} `);
});
```

#### off('seekDone')10+

off(type: 'seekDone'): void

取消设置seek结束事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'seekDone'。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.off('seekDone');
```

#### on('validCommandChange')11+

on(type: 'validCommandChange', callback: Callback<Array<AVCastControlCommandType>>): void

会话支持的有效命令变化监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'validCommandChange'：当检测到会话的合法命令发生改变时，触发该事件。callbackCallback<Array<[AVCastControlCommandType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avcastcontrolcommandtype10)>>是回调函数。参数commands是有效命令的集合。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
aVCastController.on('validCommandChange', (validCommands: avSession.AVCastControlCommandType[]) => {
  console.info(`validCommandChange : SUCCESS : size : ${validCommands.length}`);
  console.info(`validCommandChange : SUCCESS : validCommands : ${validCommands.values()}`);
});
```

#### off('validCommandChange')11+

off(type: 'validCommandChange', callback?: Callback<Array<AVCastControlCommandType>>): void

取消会话有效命令变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'validCommandChange'。callbackCallback<Array<[AVCastControlCommandType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avcastcontrolcommandtype10)>>否

回调函数。参数commands是有效命令的集合。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
aVCastController.off('validCommandChange');
```

#### on('videoSizeChange')12+

on(type: 'videoSizeChange', callback: (width: number, height: number) => void): void

媒体控制器监听视频尺寸变化变化的事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

系统能力： SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'videoSizeChange'：当检测到会话的合法命令发生改变时，触发该事件。callback(width: number, height: number) => void是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.on('videoSizeChange', (width: number, height: number) => {
  console.info(`videoSizeChange : SUCCESS : size : ${width}, ${height}`);
});
```

#### off('videoSizeChange')12+

off(type: 'videoSizeChange'): void

取消视频尺寸事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

系统能力： SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'videoSizeChange'：当检测到会话的合法命令发生改变时，触发该事件。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.off('videoSizeChange');
```

#### on('error')10+

on(type: 'error', callback: ErrorCallback): void

监听远端播放器的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是错误事件回调类型，支持的事件：'error'，用户操作和系统都会触发此事件。callbackErrorCallback是错误事件回调方法：远端播放过程中发生的错误，会提供错误码ID和错误信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)、[媒体服务错误码](../../errors/Media错误码.md)以及[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.5400101No memory.5400102Operation not allowed.5400103I/O error.5400104Time out.5400105Service died.5400106Unsupport format.6600101Session service exception.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

aVCastController.on('error', (error: BusinessError) => {
  console.info(`error happened, error code: ${error.code}, error message : ${error.message}.`)
})
```

#### off('error')10+

off(type: 'error'): void

取消播放的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是错误事件回调类型，取消注册的事件：'error'。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)、[媒体服务错误码](../../errors/Media错误码.md)以及[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.5400101No memory.5400102Operation not allowed.5400103I/O error.5400104Time out.5400105Service died.5400106Unsupport format.6600101Session service exception.

**示例：**

```ets
aVCastController.off('error')
```

#### on('keyRequest')12+

on(type: 'keyRequest', callback: KeyRequestCallback): void

在线DRM资源投播时，设置许可证请求的事件监听。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'keyRequest'：当DRM资源播放需要许可证时，触发该事件。callback[KeyRequestCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__keyrequestcallback12)是回调函数，媒体资源及许可证请求数据。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
let keyRequestCallback: avSession.KeyRequestCallback = async(assetId: string, requestData: Uint8Array) => {
  console.info(`Succeeded in keyRequestCallback. assetId: ${assetId}, requestData: ${requestData}`);
}
aVCastController.on('keyRequest', keyRequestCallback);
```

#### off('keyRequest')12+

off(type: 'keyRequest', callback?: KeyRequestCallback): void

取消许可证请求事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持的事件是'keyRequest'。callback[KeyRequestCallback](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__keyrequestcallback12)否回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.

**示例：**

```ets
aVCastController.off('keyRequest');
```

#### on('castControlGenericError')13+

on(type: 'castControlGenericError', callback: ErrorCallback): void

监听投播通用错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是错误事件回调类型，支持的事件：'castControlGenericError'。callbackErrorCallback是投播通用错误事件回调方法。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.6611000The error code for cast control is unspecified.6611001An unspecified error occurs in the remote player.6611002The playback position falls behind the live window.6611003The process of cast control times out.6611004The runtime check failed.6611100Cross-device data transmission is locked.6611101The specified seek mode is not supported.6611102The position to seek to is out of the range of the media asset or the specified seek mode is not supported.6611103The specified playback mode is not supported.6611104The specified playback speed is not supported.6611105The action failed because either the media source device or the media sink device has been revoked.6611106The parameter is invalid, for example, the url is illegal to play.6611107Allocation of memory failed.6611108Operation is not allowed.

**示例：**

```ets
aVCastController.on('castControlGenericError', (error: BusinessError) => {
  console.info(`castControlGenericError happened, error code: ${error.code}, error message : ${error.message}.`)
})
```

#### off('castControlGenericError')13+

off(type: 'castControlGenericError', callback?: ErrorCallback): void

取消投播通用的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持的事件是'castControlGenericError'。callbackErrorCallback否回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

```ets
aVCastController.off('castControlGenericError');
```

#### on('castControlIoError')13+

on(type: 'castControlIoError', callback: ErrorCallback): void

监听投播输入/输出的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是错误事件回调类型，支持的事件：'castControlIoError'。callbackErrorCallback是投播输入/输出的错误事件回调方法。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.6612000An unspecified input/output error occurs.6612001Network connection failure.6612002Network timeout.6612003Invalid "Content-Type" HTTP header.6612004The HTTP server returns an unexpected HTTP response status code.6612005The file does not exist.6612006No permission is granted to perform the IO operation.6612007Access to cleartext HTTP traffic is not allowed by the app's network security configuration.6612008Reading data out of the data bound.6612100The media does not contain any contents that can be played.6612101The media cannot be read, for example, because of dust or scratches.6612102This resource is already in use.6612103The content using the validity interval has expired.6612104Using the requested content to play is not allowed.6612105The use of the allowed content cannot be verified.6612106The number of times this content has been used as requested has reached the maximum allowed number of uses.6612107An error occurs when sending packet from source device to sink device.

**示例：**

```ets
aVCastController.on('castControlIoError', (error: BusinessError) => {
  console.info(`castControlIoError happened, error code: ${error.code}, error message : ${error.message}.`)
})
```

#### off('castControlIoError')13+

off(type: 'castControlIoError', callback?: ErrorCallback): void

取消投播输入/输出的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持的事件是'castControlIoError'。callbackErrorCallback否回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

```ets
aVCastController.off('castControlIoError');
```

#### on('castControlParsingError')13+

on(type: 'castControlParsingError', callback: ErrorCallback): void

监听投播解析的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是错误事件回调类型，支持的事件：'castControlParsingError'。callbackErrorCallback是投播解析的错误事件回调方法。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.6613000Unspecified error related to content parsing.6613001Parsing error associated with media container format bit streams.6613002Parsing error associated with the media manifest.6613003An error occurs when attempting to extract a file with an unsupported media container format or an unsupported media container feature.6613004Unsupported feature in the media manifest.

**示例：**

```ets
aVCastController.on('castControlParsingError', (error: BusinessError) => {
  console.info(`castControlParsingError happened, error code: ${error.code}, error message : ${error.message}.`)
})
```

#### off('castControlParsingError')13+

off(type: 'castControlParsingError', callback?: ErrorCallback): void

取消投播解析的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持的事件是'castControlParsingError'。callbackErrorCallback否回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

```ets
aVCastController.off('castControlParsingError');
```

#### on('castControlDecodingError')13+

on(type: 'castControlDecodingError', callback: ErrorCallback): void

监听投播解码的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是错误事件回调类型，支持的事件：'castControlDecodingError'。callbackErrorCallback是投播解码的错误事件回调方法。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.6614000Unspecified decoding error.6614001Decoder initialization failed.6614002Decoder query failed.6614003Decoding the media samples failed.6614004The format of the content to decode exceeds the capabilities of the device.6614005The format of the content to decode is not supported.

**示例：**

```ets
aVCastController.on('castControlDecodingError', (error: BusinessError) => {
  console.info(`castControlDecodingError happened, error code: ${error.code}, error message : ${error.message}.`)
})
```

#### off('castControlDecodingError')13+

off(type: 'castControlDecodingError', callback?: ErrorCallback): void

取消投播解码的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持的事件是'castControlDecodingError'。callbackErrorCallback否回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

```ets
aVCastController.off('castControlDecodingError');
```

#### on('castControlAudioRendererError')13+

on(type: 'castControlAudioRendererError', callback: ErrorCallback): void

监听投播音频渲染器的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是错误事件回调类型，支持的事件：'castControlAudioRendererError'。callbackErrorCallback是投播音频渲染器的错误事件回调方法。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.6615000Unspecified errors related to the audio renderer.6615001Initializing the audio renderer failed.6615002The audio renderer fails to write data.

**示例：**

```ets
aVCastController.on('castControlAudioRendererError', (error: BusinessError) => {
  console.info(`castControlAudioRendererError happened, error code: ${error.code}, error message : ${error.message}.`)
})
```

#### off('castControlAudioRendererError')13+

off(type: 'castControlAudioRendererError', callback?: ErrorCallback): void

取消投播音频渲染器的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持的事件是'castControlAudioRendererError'。callbackErrorCallback否回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

```ets
aVCastController.off('castControlAudioRendererError');
```

#### on('castControlDrmError')13+

on(type: 'castControlDrmError', callback: ErrorCallback): void

监听投播drm的错误事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是错误事件回调类型，支持的事件：'castControlDrmError'。callbackErrorCallback是投播drm的错误事件回调方法。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.6616000Unspecified error related to DRM.6616001The chosen DRM protection scheme is not supported by the device.6616002Device provisioning failed.6616003The DRM-protected content to play is incompatible.6616004Failed to obtain a license.6616005The operation is disallowed by the license policy.6616006An error occurs in the DRM system.6616007The device has revoked DRM privileges.6616008The DRM license being loaded into the open DRM session has expired.6616100An error occurs when the DRM processes the key response.

**示例：**

```ets
aVCastController.on('castControlDrmError', (error: BusinessError) => {
  console.info(`castControlDrmError happened, error code: ${error.code}, error message : ${error.message}.`)
})
```

#### off('castControlDrmError')13+

off(type: 'castControlDrmError', callback?: ErrorCallback): void

取消投播drm的错误事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持的事件是'castControlDrmError'。callbackErrorCallback否回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)

错误码ID错误信息401Parameter check failed. 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

```ets
aVCastController.off('castControlDrmError');
```

#### on('customDataChange')20+

on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void

注册从远端设备发送的自定义数据的监听器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持'customDataChange'事件。媒体提供方发送自定义数据时触发。callbackCallback<Record<string, Object>>是回调函数，用于接收自定义数据。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
aVCastController.on('customDataChange', (callback) => {
    console.info(`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}`);
});
```

#### off('customDataChange')20+

off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void

取消对自定义数据的监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持的事件是'customDataChange'。callbackCallback<Record<string, Object>>否注册监听事件时的回调函数。该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.

**示例：**

```ets
aVCastController.off('customDataChange');
```