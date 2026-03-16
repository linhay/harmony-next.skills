# Interface (AVTranscoder)

- 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 12开始支持。

视频转码管理类，用于视频转码。在调用AVTranscoder的方法前，需要先通过[createAVTranscoder()](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529445861__mediacreateavtranscoder12)构建一个AVTranscoder实例。

视频转码demo可参考：[视频转码开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avtranscoder-for-transcodering)

#### 导入模块

```ets
import { media } from '@kit.MediaKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

名称类型只读可选说明fdSrc12+[AVFileDescriptor](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605902__avfiledescriptor9)否否

源媒体文件描述，通过该属性设置数据源。

**使用示例**：

假设一个连续存储的媒体文件，地址偏移：0，字节长度：100。其文件描述为AVFileDescriptor{ fd = 资源句柄; offset = 0; length = 100; }。

**说明：**

- 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

fdDst12+number否否

目标媒体文件描述，通过该属性设置数据输出。在创建AVTranscoder实例后，必须设置fdSrc和fdDst属性。

**说明：**

- 将资源句柄（fd）传递给AVTranscoder实例之后，请不要通过该资源句柄做其他读写操作，包括但不限于将同一个资源句柄传递给多个AVPlayer/AVMetadataExtractor/AVImageGenerator/AVTranscoder。同一时间通过同一个资源句柄读写文件时存在竞争关系，将导致视频转码数据获取异常。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

#### prepare12+

prepare(config: AVTranscoderConfig): Promise<void>

异步方式进行视频转码的参数设置。通过Promise获取返回值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

参数名类型必填说明config[AVTranscoderConfig](Interfaces (其他).md#ZH-CN_TOPIC_0000002497605902__avtranscoderconfig12)是配置视频转码的相关参数。 当config中设置的目标视频分辨率宽videoFrameWidth大于原视频的宽或目标视频分辨率高videoFrameHeight大于原视频的高时，会上报错误码401。

**返回值：**

类型说明Promise<void>异步视频转码prepare方法的Promise返回值。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401The parameter check failed. Return by promise.5400102Operation not allowed. Return by promise.5400103IO error. Return by promise.5400105Service died. Return by promise.5400106Unsupported format. Returned by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  // 配置参数以实际硬件设备支持的范围为准。
  let avTranscoderConfig: media.AVTranscoderConfig = {
    audioBitrate : 200000,
    audioCodec : media.CodecMimeType.AUDIO_AAC,
    fileFormat : media.ContainerFormatType.CFT_MPEG_4,
    videoBitrate : 3000000,
    videoCodec : media.CodecMimeType.VIDEO_AVC,
  };

  avTranscoder.prepare(avTranscoderConfig).then(() => {
    console.info('prepare success');
  }).catch((err: BusinessError) => {
    console.error('prepare failed and catch error is ' + err.message);
  });
}
```

#### start12+

start(): Promise<void>

异步方式开始视频转码。通过Promise获取返回值。

需要[prepare()](#ZH-CN_TOPIC_0000002497445920__prepare12)事件成功触发后，才能调用start方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

类型说明Promise<void>异步开始视频转码方法的Promise返回值。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by promise.5400103IO error. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.start().then(() => {
    console.info('start AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('start AVTranscoder failed and catch error is ' + err.message);
  });
}
```

#### pause12+

pause(): Promise<void>

异步方式暂停视频转码。通过Promise获取返回值。

需要[start()](#ZH-CN_TOPIC_0000002497445920__start12)事件成功触发后，才能调用pause方法，可以通过调用[resume()](#ZH-CN_TOPIC_0000002497445920__resume12)接口来恢复转码。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

类型说明Promise<void>异步暂停视频转码方法的Promise返回值。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by promise.5400103IO error. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.pause().then(() => {
    console.info('pause AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('pause AVTranscoder failed and catch error is ' + err.message);
  });
}
```

#### resume12+

resume(): Promise<void>

异步方式恢复视频转码。通过Promise获取返回值。

需要在[pause()](#ZH-CN_TOPIC_0000002497445920__pause12)事件成功触发后，才能调用resume方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

类型说明Promise<void>异步恢复视频转码方法的Promise返回值。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by promise.5400103IO error. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.resume().then(() => {
    console.info('resume AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('resume AVTranscoder failed and catch error is ' + err.message);
  });
}
```

#### cancel12+

cancel(): Promise<void>

异步方式取消视频转码。通过Promise获取返回值。

需要在[prepare()](#ZH-CN_TOPIC_0000002497445920__prepare12)、[start()](#ZH-CN_TOPIC_0000002497445920__start12)、[pause()](#ZH-CN_TOPIC_0000002497445920__pause12)或[resume()](#ZH-CN_TOPIC_0000002497445920__resume12)事件成功触发后，才能调用cancel方法。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

类型说明Promise<void>异步取消视频转码方法的Promise返回值。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by promise.5400103IO error. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.cancel().then(() => {
    console.info('cancel AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('cancel AVTranscoder failed and catch error is ' + err.message);
  });
}
```

#### release12+

release(): Promise<void>

异步方式释放视频转码资源。通过Promise获取返回值。

释放视频转码资源之后，该AVTranscoder实例不能再进行任何操作。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**返回值：**

类型说明Promise<void>异步释放视频转码资源方法的Promise返回值。

**错误码：**

以下错误码的详细介绍请参见[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息5400102Operation not allowed. Return by promise.5400105Service died. Return by promise.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.release().then(() => {
    console.info('release AVTranscoder success');
  }).catch((err: BusinessError) => {
    console.error('release AVTranscoder failed and catch error is ' + err.message);
  });
}
```

#### on('progressUpdate')12+

on(type:'progressUpdate', callback: Callback<number>):void

注册转码进度更新事件，并通过注册的回调方法通知开发者。开发者只能注册一个进度更新事件的回调方法，当开发者重复注册时，以最后一次注册的回调接口为准。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

参数名类型必填说明typestring是进度更新事件回调类型，支持的事件：'progressUpdate'，在转码过程中系统会自动触发此事件。callback[Callback<number>](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__callback)是进度更新事件回调方法，progress: number，表示当前转码进度。

**示例：**

```ets
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.on('progressUpdate', (progress: number) => {
    console.info('avTranscoder progressUpdate = ' + progress);
  });
}
```

#### off('progressUpdate')12+

off(type:'progressUpdate', callback?: Callback<number>): void

取消注册转码进度更新事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

参数名类型必填说明typestring是进度更新事件回调类型，支持的事件：'progressUpdate'。callback[Callback<number>](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__callback)否已注册的进度更新事件回调。由于当前回调注册时，仅会保留最后一次注册的回调，建议此参数缺省。

**示例：**

```ets
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.off('progressUpdate');
}
```

#### on('error')12+

on(type: 'error', callback: ErrorCallback): void

注册AVtranscoder的错误事件，该事件仅用于错误提示。如果AVTranscoder上报error事件，开发者需要通过[release()](#ZH-CN_TOPIC_0000002497445920__release12)退出转码操作。

开发者只能订阅一个错误事件的回调方法，当开发者重复订阅时，以最后一次订阅的回调接口为准。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

参数名类型必填说明typestring是

转码错误事件回调类型'error'。

- 'error'：录制过程中发生错误，触发该事件。

callback[ErrorCallback](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)是转码错误事件回调方法。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体错误码](../../errors/Media错误码.md)。

错误码ID错误信息401The parameter check failed.801Capability not supported.5400101No memory.5400102Operation not allowed.5400103I/O error.5400104Time out.5400105Service died.5400106Unsupported format.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.on('error', (err: BusinessError) => {
    console.info('case avTranscoder.on(error) called, errMessage is ' + err.message);
  });
}
```

#### off('error')12+

off(type:'error', callback?: ErrorCallback): void

取消注册转码错误事件，取消后不再接收到AVTranscoder的错误事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

参数名类型必填说明typestring是

转码错误事件回调类型'error'。

- 'error'：转码过程中发生错误，触发该事件。

callback[ErrorCallback](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__errorcallback)否错误事件回调方法。

**示例：**

```ets
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.off('error');
}
```

#### on('complete')12+

on(type: 'complete', callback: Callback<void>): void

注册转码完成事件，并通过注册的回调方法通知开发者。开发者只能注册一个进度更新事件的回调方法，当开发者重复注册时，以最后一次注册的回调接口为准。

当AVTranscoder上报complete事件时，当前转码操作已完成，开发者需要通过[release()](#ZH-CN_TOPIC_0000002497445920__release12)退出转码操作。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

参数名类型必填说明typestring是完成事件回调类型，支持的事件：'complete'，在转码过程中系统会自动触发此事件。callback[Callback<void>](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__callback)是完成事件回调方法。

**示例：**

```ets
import { media } from '@kit.MediaKit';

async function test() {
  let avTranscoder: media.AVTranscoder | undefined = undefined;
  // 创建转码实例。
  avTranscoder = await media.createAVTranscoder();
  avTranscoder.on('complete', async () => {
    console.info('avTranscoder complete');
    if (avTranscoder != undefined) {
      // 开发者须在此监听转码完成事件。
      // 须等待avTranscoder.release()释放转码实例之后，再对转码后的文件进行转发、上传、转存等处理。
      await avTranscoder.release();
      avTranscoder = undefined;
    }
  });
}
```

#### off('complete')12+

off(type:'complete', callback?: Callback<void>): void

取消注册转码完成事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**参数：**

参数名类型必填说明typestring是转码完成事件回调类型，支持的事件：'complete'。callback[Callback<void>](../../modules/ohos/@ohos.base (公共回调信息).md#ZH-CN_TOPIC_0000002497445536__callback)否完成事件回调方法。

**示例：**

```ets
import { media } from '@kit.MediaKit';

async function test() {
  // 创建转码实例。
  let avTranscoder = await media.createAVTranscoder();
  avTranscoder.off('complete');
}
```