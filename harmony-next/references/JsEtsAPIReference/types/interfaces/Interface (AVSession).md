# Interface (AVSession)

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 10开始支持。

调用[avSession.createAVSession](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002497445782__avsessioncreateavsession10)后，返回会话的实例，可以获得会话ID，完成设置元数据，播放状态信息等操作。

#### 导入模块

```ets
import { avSession } from '@kit.AVSessionKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明sessionId10+string是否

AVSession对象唯一的会话标识。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

sessionType10+[AVSessionType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avsessiontype10)是否

AVSession会话类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

sessionTag22+string是否

AVSession会话的自定义标签信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**示例：**

```ets
let sessionId: string = currentAVSession.sessionId;
let sessionType: avSession.AVSessionType = currentAVSession.sessionType;
```

#### setAVMetadata10+

setAVMetadata(data: AVMetadata): Promise<void>

设置会话元数据。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明data[AVMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avmetadata10)是会话元数据。

**返回值：**

类型说明Promise<void>Promise对象。当元数据设置成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let metadata: avSession.AVMetadata = {
  assetId: "121278",
  title: "lose yourself",
  artist: "Eminem",
  author: "ST",
  album: "Slim shady",
  writer: "ST",
  composer: "ST",
  duration: 2222,
  mediaImage: "https://www.example.com/example.jpg",
  subtitle: "8 Mile",
  description: "Rap",
  // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
  // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n
  lyric: "lrc格式歌词内容",
  // singleLyricText字段存储单条歌词文本，不包含时间戳。
  // 例如："单条歌词内容"。
  singleLyricText: "单条歌词内容",
  previousAssetId: "121277",
  nextAssetId: "121279"
};
currentAVSession.setAVMetadata(metadata).then(() => {
  console.info('SetAVMetadata successfully');
}).catch((err: BusinessError) => {
  console.error(`SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### setAVMetadata10+

setAVMetadata(data: AVMetadata, callback: AsyncCallback<void>): void

设置会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明data[AVMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avmetadata10)是会话元数据。callbackAsyncCallback<void>是回调函数。当元数据设置成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let metadata: avSession.AVMetadata = {
  assetId: "121278",
  title: "lose yourself",
  artist: "Eminem",
  author: "ST",
  album: "Slim shady",
  writer: "ST",
  composer: "ST",
  duration: 2222,
  mediaImage: "https://www.example.com/example.jpg",
  subtitle: "8 Mile",
  description: "Rap",
  // LRC中有两类元素：一种是时间标签+歌词，一种是ID标签。
  // 例如：[00:25.44]xxx\r\n[00:26.44]xxx\r\n
  lyric: "lrc格式歌词内容",
  // singleLyricText字段存储单条歌词文本，不包含时间戳。
  // 例如："单条歌词内容"。
  singleLyricText: "单条歌词内容",
  previousAssetId: "121277",
  nextAssetId: "121279"
};
currentAVSession.setAVMetadata(metadata, (err: BusinessError) => {
  if (err) {
    console.error(`SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SetAVMetadata successfully');
  }
});
```

#### setCallMetadata11+

setCallMetadata(data: CallMetadata): Promise<void>

设置通话会话元数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明data[CallMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__callmetadata11)是通话会话元数据。

**返回值：**

类型说明Promise<void>Promise对象。当通话元数据设置成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height('100%')
  }
}

class CallManager {
  private currentAVSession: avSession.AVSession | null = null;

  async setCallMetadata() {
    try {
      let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
      let imageSource = await image.createImageSource(value.buffer);
      let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
      let calldata: avSession.CallMetadata = {
        name: "xiaoming",
        phoneNumber: "111xxxxxxxx",
        avatar: imagePixel
      };
      await this.currentAVSession?.setCallMetadata(calldata);
      console.info('setCallMetadata successfully');
    } catch (err) {
      if (err) {
        console.error('setCallMetadata BusinessError: code: ${err.code}, message: ${err.message}');
      } else {
        console.error('setCallMetadata Error: ${err}')
      }
    }
  }
}
```

#### setCallMetadata11+

setCallMetadata(data: CallMetadata, callback: AsyncCallback<void>): void

设置通话会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明data[CallMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__callmetadata11)是通话会话元数据。callbackAsyncCallback<void>是回调函数。当通话元数据设置成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Hello World')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
    }
    .width('100%')
    .height('100%')
  }
}

class CallManager {
  private currentAVSession: avSession.AVSession | null = null;

  async setCallMetadata() {
    try {
      let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
      let imageSource = await image.createImageSource(value.buffer);
      let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
      let calldata: avSession.CallMetadata = {
        name: "xiaoming",
        phoneNumber: "111xxxxxxxx",
        avatar: imagePixel
      };
      this.currentAVSession?.setCallMetadata(calldata, (err: BusinessError) => {
        if (err) {
          console.error('setCallMetadata BusinessError: code: ${err.code}, message: ${err.message}');
        } else {
          console.info("setCallMetadata successfully");
        }
      });
    }catch (syncErr) {
      console.error('Syncronous operation failed: ${syncErr}');
    }
  }
}
```

#### setAVCallState11+

setAVCallState(state: AVCallState): Promise<void>

设置通话状态。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明state[AVCallState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcallstate11)是通话状态。

**返回值：**

类型说明Promise<void>Promise对象。当通话元数据设置成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let calldata: avSession.AVCallState = {
  state: avSession.CallState.CALL_STATE_ACTIVE,
  muted: false
};
currentAVSession.setAVCallState(calldata).then(() => {
  console.info('setAVCallState successfully');
}).catch((err: BusinessError) => {
  console.error(`setAVCallState BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### setAVCallState11+

setAVCallState(state: AVCallState, callback: AsyncCallback<void>): void

设置通话状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明state[AVCallState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcallstate11)是通话状态。callbackAsyncCallback<void>是回调函数。当通话元数据设置成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avcalldata: avSession.AVCallState = {
  state: avSession.CallState.CALL_STATE_ACTIVE,
  muted: false
};
currentAVSession.setAVCallState(avcalldata, (err: BusinessError) => {
  if (err) {
    console.error(`setAVCallState BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('setAVCallState successfully');
  }
});
```

#### setAVPlaybackState10+

setAVPlaybackState(state: AVPlaybackState): Promise<void>

设置会话播放状态。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明state[AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)是会话播放状态，包括状态、倍数、循环模式等信息。

**返回值：**

类型说明Promise<void>Promise对象。当播放状态设置成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let playbackState: avSession.AVPlaybackState = {
  state:avSession.PlaybackState.PLAYBACK_STATE_PLAY,
  speed: 1.0,
  position:{elapsedTime:10, updateTime:(new Date()).getTime()},
  bufferedTime:1000,
  loopMode:avSession.LoopMode.LOOP_MODE_SINGLE,
  isFavorite:true
};
currentAVSession.setAVPlaybackState(playbackState).then(() => {
  console.info('SetAVPlaybackState successfully');
}).catch((err: BusinessError) => {
  console.error(`SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### setAVPlaybackState10+

setAVPlaybackState(state: AVPlaybackState, callback: AsyncCallback<void>): void

设置会话播放状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明state[AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)是会话播放状态，包括状态、倍数、循环模式等信息。callbackAsyncCallback<void>是回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let PlaybackState: avSession.AVPlaybackState = {
  state:avSession.PlaybackState.PLAYBACK_STATE_PLAY,
  speed: 1.0,
  position:{elapsedTime:10, updateTime:(new Date()).getTime()},
  bufferedTime:1000,
  loopMode:avSession.LoopMode.LOOP_MODE_SINGLE,
  isFavorite:true
};
currentAVSession.setAVPlaybackState(PlaybackState, (err: BusinessError) => {
  if (err) {
    console.error(`SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SetAVPlaybackState successfully');
  }
});
```

#### setLaunchAbility10+

setLaunchAbility(ability: WantAgent): Promise<void>

设置一个WantAgent用于拉起会话的Ability。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明ability[WantAgent](../../modules/ohos/@ohos.app.ability.wantAgent (WantAgent模块).md)是应用的相关属性信息，如bundleName，abilityName，deviceId等。

**返回值：**

类型说明Promise<void>Promise对象。当Ability设置成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// WantAgentInfo对象。
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: "deviceId",
      bundleName: "com.example.myapplication",
      abilityName: "EntryAbility",
      action: "action1",
      entities: ["entity1"],
      type: "MIMETYPE",
      uri: "key = {true,true,false}",
      parameters:
        {
          mykey0: 2222,
          mykey1: [1, 2, 3],
          mykey2: "[1, 2, 3]",
          mykey3: "ssssssssssssssssssssssssss",
          mykey4: [false, true, false],
          mykey5: ["qqqqq", "wwwwww", "aaaaaaaaaaaaaaaaa"],
          mykey6: true
        }
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITIES,
  requestCode: 0,
  wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
}

wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
  currentAVSession.setLaunchAbility(agent).then(() => {
    console.info('SetLaunchAbility successfully');
  }).catch((err: BusinessError) => {
    console.error(`SetLaunchAbility BusinessError: code: ${err.code}, message: ${err.message}`);
  });
});
```

#### setLaunchAbility10+

setLaunchAbility(ability: WantAgent, callback: AsyncCallback<void>): void

设置一个WantAgent用于拉起会话的Ability。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明ability[WantAgent](../../modules/ohos/@ohos.app.ability.wantAgent (WantAgent模块).md)是应用的相关属性信息，如bundleName，abilityName，deviceId等。callbackAsyncCallback<void>是回调函数。当Ability设置成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// WantAgentInfo对象。
let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      deviceId: "deviceId",
      bundleName: "com.example.myapplication",
      abilityName: "EntryAbility",
      action: "action1",
      entities: ["entity1"],
      type: "MIMETYPE",
      uri: "key = {true,true,false}",
      parameters:
        {
          mykey0: 2222,
          mykey1: [1, 2, 3],
          mykey2: "[1, 2, 3]",
          mykey3: "ssssssssssssssssssssssssss",
          mykey4: [false, true, false],
          mykey5: ["qqqqq", "wwwwww", "aaaaaaaaaaaaaaaaa"],
          mykey6: true
        }
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITIES,
  requestCode: 0,
  wantAgentFlags:[wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
}

wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
  currentAVSession.setLaunchAbility(agent, (err: BusinessError) => {
    if (err) {
      console.error(`SetLaunchAbility BusinessError: code: ${err.code}, message: ${err.message}`);
    } else {
      console.info('SetLaunchAbility successfully');
    }
  });
});
```

#### dispatchSessionEvent10+

dispatchSessionEvent(event: string, args: Record<string, Object>): Promise<void>

媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容，结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明eventstring是需要设置的会话事件的名称。argsRecord<string, Object>是

需要传递的会话事件内容。

API version 20开始发生兼容变更，在API version 19及之前的版本args的参数类型为：{[key: string]: Object}。

参数args支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](../../modules/ohos/@ohos.app.ability.Want (Want).md)。

**返回值：**

类型说明Promise<void>Promise对象。当事件设置成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
              if (err) {
                console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
              } else {
                currentAVSession = data;
                let eventName = "dynamic_lyric";
                if (currentAVSession !== undefined) {
                  (currentAVSession as avSession.AVSession).dispatchSessionEvent(eventName, {lyric : "This is lyric"}).then(() => {
                    console.info('dispatchSessionEvent successfully');
                  }).catch((err: BusinessError) => {
                    console.error(`dispatchSessionEvent BusinessError: code: ${err.code}, message: ${err.message}`);
                  })
                }
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### dispatchSessionEvent10+

dispatchSessionEvent(event: string, args: Record<string, Object>, callback: AsyncCallback<void>): void

媒体提供方设置一个会话内自定义事件，包括事件名和键值对形式的事件内容，结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明eventstring是需要设置的会话事件的名称。argsRecord<string, Object>是

需要传递的会话事件内容。

API version 20开始发生兼容变更，在API version 19及之前的版本args的参数类型为：{[key: string]: Object}。

callbackAsyncCallback<void>是回调函数。当会话事件设置成功，err为undefined，否则返回错误对象。

参数args支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](../../modules/ohos/@ohos.app.ability.Want (Want).md)。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
              if (err) {
                console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
              } else {
                currentAVSession = data;
                let eventName: string = "dynamic_lyric";
                if (currentAVSession !== undefined) {
                  (currentAVSession as avSession.AVSession).dispatchSessionEvent(eventName, {lyric : "This is lyric"}, (err: BusinessError) => {
                    if (err) {
                      console.error(`dispatchSessionEvent BusinessError: code: ${err.code}, message: ${err.message}`);
                    }
                  })
                }
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### setAVQueueItems10+

setAVQueueItems(items: Array<AVQueueItem>): Promise<void>

设置媒体播放列表。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明itemsArray<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>是播放列表单项的队列，用以表示播放列表。

**返回值：**

类型说明Promise<void>Promise对象。当播放列表设置成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
interface ExtrasType {
  extras: string;
}

@Entry
@Component
struct Index {
  build() {
    Column() {
    }
  }
}

let currentAVSession: avSession.AVSession;

async function setAVQueueItems() {
  try {
    let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
    let imageSource = await image.createImageSource(value.buffer);
    let imagePixel = await imageSource.createPixelMap({desiredSize:{width: 150, height: 150}});
    let queueItemDescription_1: avSession.AVMediaDescription = {
      assetId: '001',
      title: 'music_name',
      subtitle: 'music_sub_name',
      description: 'music_description',
      mediaImage : imagePixel,
      extras: {extras:'any'}
    };
    let queueItem_1: avSession.AVQueueItem = {
      itemId: 1,
      description: queueItemDescription_1
    } as avSession.AVQueueItem;
    let queueItemDescription_2: avSession.AVMediaDescription = {
      assetId: '002',
      title: 'music_name',
      subtitle: 'music_sub_name',
      description: 'music_description',
      mediaImage: imagePixel,
      extras: {extras:'any'}
    };
    let queueItem_2: avSession.AVQueueItem = {
      itemId: 2,
      description: queueItemDescription_2
    } as avSession.AVQueueItem;
    let queueItemsArray: avSession.AVQueueItem[] = [queueItem_1, queueItem_2];
    currentAVSession.setAVQueueItems(queueItemsArray).then(() => {
      console.info('SetAVQueueItems successfully');
    }).catch((err: BusinessError) => {
      console.error(`SetAVQueueItems BusinessError: code: ${err.code}, message: ${err.message}`);
    });
  } catch (err) {
    if (err) {
      console.error(`ImageSource or PixelMap create Error: code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

#### setAVQueueItems10+

setAVQueueItems(items: Array<AVQueueItem>, callback: AsyncCallback<void>): void

设置媒体播放列表。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明itemsArray<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>是播放列表单项的队列，用以表示播放列表。callbackAsyncCallback<void>是回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit'

interface ExtrasType {
  extras: string;
}

@Entry
@Component
struct Index {
  build() {
    Column() {
    }
  }
}

let currentAVSession: avSession.AVSession;

async function setAVQueueItems() {
  try {
    let value = await resourceManager.getSysResourceManager().getRawFileContent('IMAGE_URI');
    let imageSource = await image.createImageSource(value.buffer);
    let imagePixel = await imageSource.createPixelMap({ desiredSize: { width: 150, height: 150 } });
    let queueItemDescription_1: avSession.AVMediaDescription = {
      assetId: '001',
      title: 'music_name',
      subtitle: 'music_sub_name',
      description: 'music_description',
      mediaImage: imagePixel,
      extras: { extras: 'any' }
    };
    let queueItem_1: avSession.AVQueueItem = {
      itemId: 1,
      description: queueItemDescription_1
    };
    let queueItemDescription_2: avSession.AVMediaDescription = {
      assetId: '002',
      title: 'music_name',
      subtitle: 'music_sub_name',
      description: 'music_description',
      mediaImage: imagePixel,
      extras: { extras: 'any' }
    };
    let queueItem_2: avSession.AVQueueItem = {
      itemId: 2,
      description: queueItemDescription_2
    };
    let queueItemsArray: avSession.AVQueueItem[] = [queueItem_1, queueItem_2];
    currentAVSession.setAVQueueItems(queueItemsArray, (err: BusinessError) => {
      if (err) {
        console.error(`SetAVQueueItems BusinessError: code: ${err.code}, message: ${err.message}`);
      } else {
        console.info('SetAVQueueItems successfully');
      }
    });
  } catch (err) {
    if (err) {
      console.error(`ImageSource or PixelMap create Error: code: ${err.code}, message: ${err.message}`);
    }
  }
}
```

#### setAVQueueTitle10+

setAVQueueTitle(title: string): Promise<void>

设置媒体播放列表名称。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明titlestring是播放列表的名称。

**返回值：**

类型说明Promise<void>Promise对象。当播放列表设置成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let queueTitle = 'QUEUE_TITLE';
currentAVSession.setAVQueueTitle(queueTitle).then(() => {
  console.info('SetAVQueueTitle successfully');
}).catch((err: BusinessError) => {
  console.error(`SetAVQueueTitle BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### setAVQueueTitle10+

setAVQueueTitle(title: string, callback: AsyncCallback<void>): void

设置媒体播放列表名称。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明titlestring是播放列表名称字段。callbackAsyncCallback<void>是回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let queueTitle = 'QUEUE_TITLE';
currentAVSession.setAVQueueTitle(queueTitle, (err: BusinessError) => {
  if (err) {
    console.error(`SetAVQueueTitle BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SetAVQueueTitle successfully');
  }
});
```

#### setExtras10+

setExtras(extras: Record<string, Object>): Promise<void>

媒体提供方设置键值对形式的自定义媒体数据包，结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明extrasRecord<string, Object>是

需要传递的自定义媒体数据包键值对。

API version 20开始发生兼容变更，在API version 19及之前的版本args的参数类型为：{[key: string]: Object}。

参数extras支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](../../modules/ohos/@ohos.app.ability.Want (Want).md)。

**返回值：**

类型说明Promise<void>Promise对象。当自定义媒体数据包设置成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(() => {
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
              if (err) {
                console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
              } else {
                currentAVSession = data;
                if (currentAVSession !== undefined) {
                  (currentAVSession as avSession.AVSession).setExtras({extras : "This is custom media packet"}).then(() => {
                      console.info('setExtras successfully');
                  }).catch((err: BusinessError) => {
                      console.error(`setExtras BusinessError: code: ${err.code}, message: ${err.message}`);
                  })
                }
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### setExtras10+

setExtras(extras: {[key: string]: Object}, callback: AsyncCallback<void>): void

媒体提供方设置键值对形式的自定义媒体数据包，结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明extras{[key: string]: Object}是需要传递的自定义媒体数据包键值对。callbackAsyncCallback<void>是回调函数。当自定义媒体数据包设置成功，err为undefined，否则返回错误对象。

参数extras支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](../../modules/ohos/@ohos.app.ability.Want (Want).md)。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
              if (err) {
                console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
              } else {
                currentAVSession = data;
                if (currentAVSession !== undefined) {
                  (currentAVSession as avSession.AVSession).setExtras({extras : "This is custom media packet"}, (err: BusinessError) => {
                    if (err) {
                      console.error(`setExtras BusinessError: code: ${err.code}, message: ${err.message}`);
                    }
                  })
                }
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### sendCustomData20+

sendCustomData(data: Record<string, Object>): Promise<void>

发送私有数据到远端设备。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明dataRecord<string, Object>是应用程序填充的自定义数据。服务端仅解析key为'customData'，且Object为string类型的对象。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
            if (err) {
                console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
            } else {
                currentAVSession = data;
            }
            });
            if (currentAVSession !== undefined) {
            (currentAVSession as avSession.AVSession).sendCustomData({customData : "This is custom data"}).then(() => {
                console.info('sendCustomData successfully');
            }).catch((err: BusinessError) => {
                console.error(`sendCustomData BusinessError: code: ${err.code}, message: ${err.message}`);
            })
            }
          })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### getController10+

getController(): Promise<AVSessionController>

获取本会话对应的控制器。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<[AVSessionController](Interface (AVSessionController).md)>Promise对象。返回会话控制器。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';
  build() {
    Column() {
      Text(this.message)
        .onClick(async ()=>{
          try {
            let context: Context = this.getUIContext().getHostContext() as Context;
            let currentAVSession: avSession.AVSession = await avSession.createAVSession(context, 'SESSION_NAME', 'audio');
            let avSessionController: avSession.AVSessionController;
            currentAVSession.getController().then((avController: avSession.AVSessionController) => {
              avSessionController = avController;
              console.info(`GetController : SUCCESS : sessionid : ${avSessionController.sessionId}`);
            }).catch((err: BusinessError) => {
              console.error(`GetController BusinessError: code: ${err.code}, message: ${err.message}`);
            });
          } catch (err) {
            if (err) {
              console.error(`AVSession create Error: ${JSON.stringify(err)}`);
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### getController10+

getController(callback: AsyncCallback<AVSessionController>): void

获取本会话相应的控制器。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVSessionController](Interface (AVSessionController).md)>是回调函数。返回会话控制器。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { avSession } from '@kit.AVSessionKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
      Text(this.message)
        .onClick(async () => {
          try {
            let context: Context = this.getUIContext().getHostContext() as Context;
            let currentAVSession: avSession.AVSession = await avSession.createAVSession(context, 'SESSION_NAME', 'audio');
            let avsessionController: avSession.AVSessionController;
            currentAVSession.getController((err: BusinessError, avcontroller: avSession.AVSessionController) => {
              if (err) {
                console.error(`GetController BusinessError: code: ${err.code}, message: ${err.message}`);
              } else {
                avsessionController = avcontroller;
                console.info(`GetController : SUCCESS : sessionid : ${avsessionController.sessionId}`);
              }
            });
          } catch (err) {
            if (err) {
              console.error(`AVSession create Error: code: ${err.code}, message: ${err.message}`);
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

#### getAVCastController10+

getAVCastController(): Promise<AVCastController>

设备建立连接后，获取投播控制器。结果通过Promise异步回调方式返回。如果 avsession 未处于投播状态，则控制器将返回 null。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

类型说明Promise<[AVCastController](Interface (AVCastController).md)>Promise对象。返回投播控制器实例。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600102The session does not exist.6600109The remote connection is not established.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let aVCastController: avSession.AVCastController;
currentAVSession.getAVCastController().then((avcontroller: avSession.AVCastController) => {
  aVCastController = avcontroller;
  console.info('getAVCastController : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`getAVCastController BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getAVCastController10+

getAVCastController(callback: AsyncCallback<AVCastController>): void

设备建立连接后，获取投播控制器。结果通过callback异步回调方式返回。如果 avsession 未处于投播状态，则控制器将返回 null。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVCastController](Interface (AVCastController).md)>是回调函数，返回投播控制器实例。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600102The session does not exist.6600109The remote connection is not established.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let aVCastController: avSession.AVCastController;
currentAVSession.getAVCastController((err: BusinessError, avcontroller: avSession.AVCastController) => {
  if (err) {
    console.error(`getAVCastController BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    aVCastController = avcontroller;
    console.info('getAVCastController : SUCCESS');
  }
});
```

#### getOutputDevice10+

getOutputDevice(): Promise<OutputDeviceInfo>

通过会话获取播放设备信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<[OutputDeviceInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__outputdeviceinfo10)>Promise对象。返回播放设备信息。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.getOutputDevice().then((outputDeviceInfo: avSession.OutputDeviceInfo) => {
  console.info(`GetOutputDevice : SUCCESS : devices length : ${outputDeviceInfo.devices.length}`);
}).catch((err: BusinessError) => {
  console.error(`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}`);
})
```

#### getOutputDevice10+

getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void

通过会话获取播放设备相关信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[OutputDeviceInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__outputdeviceinfo10)>是回调函数，返回播放设备信息。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.getOutputDevice((err: BusinessError, outputDeviceInfo: avSession.OutputDeviceInfo) => {
  if (err) {
    console.error(`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetOutputDevice : SUCCESS : devices length : ${outputDeviceInfo.devices.length}`);
  }
});
```

#### activate10+

activate(): Promise<void>

激活会话，激活后可正常使用会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<void>Promise对象。当会话激活成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.activate().then(() => {
  console.info('Activate : SUCCESS ');
}).catch((err: BusinessError) => {
  console.error(`Activate BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### activate10+

activate(callback: AsyncCallback<void>): void

激活会话，激活后可正常使用会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当会话激活成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.activate((err: BusinessError) => {
  if (err) {
    console.error(`Activate BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Activate : SUCCESS ');
  }
});
```

#### deactivate10+

deactivate(): Promise<void>

禁用当前会话的功能，可通过[activate](#ZH-CN_TOPIC_0000002497605762__activate10)恢复。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<void>Promise对象。当禁用会话成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.deactivate().then(() => {
  console.info('Deactivate : SUCCESS ');
}).catch((err: BusinessError) => {
  console.error(`Deactivate BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### deactivate10+

deactivate(callback: AsyncCallback<void>): void

禁用当前会话。结果通过callback异步回调方式返回。

禁用当前会话的功能，可通过[activate](#ZH-CN_TOPIC_0000002497605762__activate10)恢复。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当禁用会话成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.deactivate((err: BusinessError) => {
  if (err) {
    console.error(`Deactivate BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Deactivate : SUCCESS ');
  }
});
```

#### destroy10+

destroy(): Promise<void>

销毁当前会话，使当前会话完全失效。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<void>Promise对象。当会话销毁成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.destroy().then(() => {
  console.info('Destroy : SUCCESS ');
}).catch((err: BusinessError) => {
  console.error(`Destroy BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### destroy10+

destroy(callback: AsyncCallback<void>): void

销毁当前会话，使当前会话完全失效。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当会话销毁成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.destroy((err: BusinessError) => {
  if (err) {
    console.error(`Destroy BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Destroy : SUCCESS ');
  }
});
```

#### on('play')10+

on(type: 'play', callback: () => void): void

设置播放命令监听事件。注册该监听，说明应用支持播放指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'play'，当播放命令被发送到会话时，触发该事件回调。callback() => void是回调函数。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('play', () => {
  console.info('on play entry');
});
```

#### onPlay22+

onPlay(callback: Callback<CommandInfo>): void

设置播放命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackCallback<[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)>是回调函数。当监听事件注册成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.onPlay((info: CommandInfo) => {
  console.info('on play entry');
});
```

#### on('pause')10+

on(type: 'pause', callback: () => void): void

设置暂停命令监听事件。注册该监听，说明应用支持暂停指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'pause'，当暂停命令被发送到会话时，触发该事件回调。callback() => void是回调函数。当监听事件注册成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('pause', () => {
  console.info('on pause entry');
});
```

#### on('stop')10+

on(type:'stop', callback: () => void): void

设置停止命令监听事件。注册该监听，说明应用支持停止指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件是'stop'，当停止命令被发送到会话时，触发该事件回调。callback() => void是回调函数。当监听事件注册成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('stop', () => {
  console.info('on stop entry');
});
```

#### on('playNext')10+

on(type:'playNext', callback: () => void): void

设置播放下一首命令监听事件。注册该监听，说明应用支持下一首指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件是'playNext'，当播放下一首命令被发送到会话时，触发该事件回调。callback() => void是回调函数。当监听事件注册成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('playNext', () => {
  console.info('on playNext entry');
});
```

#### onPlayNext22+

onPlayNext(callback: Callback<CommandInfo>): void

设置播放下一首命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackCallback<[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)>是回调函数。当监听事件注册成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.onPlayNext((info: CommandInfo) => {
  console.info('on playNext entry');
});
```

#### on('playPrevious')10+

on(type:'playPrevious', callback: () => void): void

设置播放上一首命令监听事件。注册该监听，说明应用支持上一首指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件是'playPrevious'，当播放上一首命令被发送到会话时，触发该事件回调。callback() => void是回调函数。当监听事件注册成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('playPrevious', () => {
  console.info('on playPrevious entry');
});
```

#### onPlayPrevious22+

onPlayPrevious(callback: Callback<CommandInfo>): void

设置播放上一首命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackCallback<[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)>是回调函数。当监听事件注册成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.onPlayPrevious((info: CommandInfo) => {
  console.info('on playPrevious entry');
});
```

#### on('fastForward')10+

on(type: 'fastForward', callback: (time?: number) => void): void

设置快进命令监听事件。注册该监听，说明应用支持快进指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件是 'fastForward'，当快进命令被发送到会话时，触发该事件回调。callback(time?: number) => void是回调函数。参数time是时间节点，单位为秒。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('fastForward', (time?: number) => {
  console.info('on fastForward entry');
});
```

#### onFastForward22+

onFastForward(callback: TwoParamCallback<number, CommandInfo>): void

设置快进命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的快进时间参数，以及对应的[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackTwoParamCallback<number, [CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)>是回调函数。用于处理'fastForward'操作。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.onFastForward((time: number, info: CommandInfo) => {
  console.info('on fastForward entry');
});
```

#### on('rewind')10+

on(type:'rewind', callback: (time?: number) => void): void

设置快退命令监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件是'rewind'，当快退命令被发送到会话时，触发该事件回调。callback(time?: number) => void是回调函数。参数time是时间节点，单位为秒。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('rewind', (time?: number) => {
  console.info('on rewind entry');
});
```

#### onRewind22+

onRewind(callback: TwoParamCallback<number, CommandInfo>): void

设置快退命令监听事件。使用callback异步回调。

应用将通过回调接收控制器发送的快退时间参数，以及对应的[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackTwoParamCallback<number, [CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)>是回调函数。用于处理'rewind'操作。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.onRewind((time: number, info: CommandInfo) => {
  console.info('on rewind entry');
});
```

#### on('playWithAssetId')20+

on(type:'playWithAssetId', callback: Callback<string>): void

设置指定资源id进行播放的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件是'playWithAssetId'，当指定资源id进行播放时，触发该事件回调。callbackCallback<string>是回调函数。参数assetId是媒体id。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
let playWithAssetIdCallback = (assetId: string) => {
  console.info(`on playWithAssetId entry,  assetId = ${assetId}`);
}
currentAVSession.on('playWithAssetId', playWithAssetIdCallback);
```

#### off('playWithAssetId')20+

off(type: 'playWithAssetId', callback?: Callback<string>): void

取消指定资源id进行播放的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'playWithAssetId'。callbackCallback<string>否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。参数assetId是媒体id。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('playWithAssetId');
```

#### on('seek')10+

on(type: 'seek', callback: (time: number) => void): void

设置跳转节点监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'seek'：当跳转节点命令被发送到会话时，触发该事件。callback(time: number) => void是回调函数。参数time是时间节点，单位为毫秒。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('seek', (time: number) => {
  console.info(`on seek entry time : ${time}`);
});
```

#### on('setSpeed')10+

on(type: 'setSpeed', callback: (speed: number) => void): void

设置播放速率的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'setSpeed'：当设置播放速率的命令被发送到会话时，触发该事件。callback(speed: number) => void是回调函数。参数speed是播放倍速。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('setSpeed', (speed: number) => {
  console.info(`on setSpeed speed : ${speed}`);
});
```

#### on('setLoopMode')10+

on(type: 'setLoopMode', callback: (mode: LoopMode) => void): void

设置循环模式的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'setLoopMode'：当设置循环模式的命令被发送到会话时，触发该事件。callback(mode: [LoopMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__loopmode10)) => void是回调函数。参数mode是循环模式。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('setLoopMode', (mode: avSession.LoopMode) => {
  console.info(`on setLoopMode mode : ${mode}`);
});
```

#### on('setTargetLoopMode')18+

on(type: 'setTargetLoopMode', callback: Callback<LoopMode>): void

设置目标循环模式的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是

事件回调类型，支持事件'setTargetLoopMode'。

- 'setTargetLoopMode'：当设置目标循环模式的命令被发送到会话时，触发该事件。

callbackCallback<[LoopMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__loopmode10)>是回调函数。参数表示目标循环模式。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('setTargetLoopMode', (mode: avSession.LoopMode) => {
  console.info(`on setTargetLoopMode mode : ${mode}`);
});
```

#### on('toggleFavorite')10+

on(type: 'toggleFavorite', callback: (assetId: string) => void): void

设置是否收藏的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'toggleFavorite'：当是否收藏的命令被发送到会话时，触发该事件。callback(assetId: string) => void是回调函数。参数assetId是媒体ID。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('toggleFavorite', (assetId: string) => {
  console.info(`on toggleFavorite mode : ${assetId}`);
});
```

#### on('skipToQueueItem')10+

on(type: 'skipToQueueItem', callback: (itemId: number) => void): void

设置播放列表其中某项被选中的监听事件，session端可以选择对这个单项歌曲进行播放。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'skipToQueueItem'：当播放列表选中单项的命令被发送到会话时，触发该事件。callback(itemId: number) => void是回调函数。参数itemId是选中的播放列表项的ID。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('skipToQueueItem', (itemId: number) => {
  console.info(`on skipToQueueItem id : ${itemId}`);
});
```

#### on('handleKeyEvent')10+

on(type: 'handleKeyEvent', callback: (event: KeyEvent) => void): void

设置蓝牙/有线等外设接入的按键输入事件的监听，监听多媒体按键事件中播放、暂停、上下一首、快进、快退的指令。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'handleKeyEvent'：当按键事件被发送到会话时，触发该事件。callback(event: [KeyEvent](../../modules/ohos/@ohos.multimodalInput.keyEvent (按键输入事件).md)) => void是回调函数。参数event是按键事件。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { KeyEvent } from '@kit.InputKit';

currentAVSession.on('handleKeyEvent', (event: KeyEvent) => {
  console.info(`on handleKeyEvent event : ${event}`);
});
```

#### on('outputDeviceChange')10+

on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void

设置播放设备变化的监听事件。应用接入[系统投播组件](../../modules/ohos/@ohos.multimedia.avCastPicker (投播组件).md)，当用户通过组件切换设备时，会收到设备切换的回调。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'outputDeviceChange'：当播放设备变化时，触发该事件。callback(state: [ConnectionState](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__connectionstate10), device: [OutputDeviceInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__outputdeviceinfo10)) => void是

回调函数，参数device是设备相关信息。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('outputDeviceChange', (state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
  console.info(`on outputDeviceChange device : ${device}`);
});
```

#### on('commonCommand')10+

on(type: 'commonCommand', callback: (command: string, args: Record<string, Object>) => void): void

设置自定义控制命令变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'commonCommand'：当自定义控制命令变化时，触发该事件。callback(command: string, args: Record<string, Object>) => void是

回调函数，command为变化的自定义控制命令名，args为自定义控制命令的参数，参数内容与[sendCommonCommand](Interface (AVSessionController).md#ZH-CN_TOPIC_0000002497445784__sendcommoncommand10)方法设置的参数内容完全一致。

API version 20开始发生兼容变更，在API version 19及之前的版本callback的参数类型为：(command :string, args:{[key: string]: Object}) => void。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';
@Entry
@Component
struct Index {
  @State message: string = 'hello world';

  build() {
    Column() {
        Text(this.message)
          .onClick(()=>{
            let currentAVSession: avSession.AVSession | undefined = undefined;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;

            avSession.createAVSession(context, tag, "audio", (err: BusinessError, data: avSession.AVSession) => {
              if (err) {
                console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
              } else {
                currentAVSession = data;
                if (currentAVSession !== undefined) {
                  (currentAVSession as avSession.AVSession).on('commonCommand', (commonCommand, args) => {
                      console.info(`OnCommonCommand, the command is ${commonCommand}, args: ${JSON.stringify(args)}`);
                  });
                }
              }
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```

#### off('play')10+

off(type: 'play', callback?: () => void): void

取消会话播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'play'。callback() => void否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('play');
```

#### offPlay22+

offPlay(callback?: Callback<CommandInfo>): void

取消会话播放事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackCallback<[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)>否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.offPlay();
```

#### off('pause')10+

off(type: 'pause', callback?: () => void): void

取消会话暂停事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'pause'。callback() => void否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('pause');
```

#### off('stop')10+

off(type: 'stop', callback?: () => void): void

取消会话停止事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'stop'。callback() => void否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('stop');
```

#### off('playNext')10+

off(type: 'playNext', callback?: () => void): void

取消会话播放下一首事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是 'playNext'。callback() => void否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('playNext');
```

#### offPlayNext22+

offPlayNext(callback?: Callback<CommandInfo>): void

取消会话播放下一首事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackCallback<[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)>否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.offPlayNext();
```

#### off('playPrevious')10+

off(type: 'playPrevious', callback?: () => void): void

取消会话播放上一首事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'playPrevious'。callback() => void否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('playPrevious');
```

#### offPlayPrevious22+

offPlayPrevious(callback?: Callback<CommandInfo>): void

取消会话播放上一首事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackCallback<[CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)>否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.offPlayPrevious();
```

#### off('fastForward')10+

off(type: 'fastForward', callback?: () => void): void

取消会话快进事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'fastForward'。callback() => void否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('fastForward');
```

#### offFastForward22+

offFastForward(callback?: TwoParamCallback<number, CommandInfo>): void

取消会话快进事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackTwoParamCallback<number, [CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)>否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.offFastForward();
```

#### off('rewind')10+

off(type: 'rewind', callback?: () => void): void

取消会话快退事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'rewind'。callback() => void否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('rewind');
```

#### offRewind22+

offRewind(callback?: TwoParamCallback<number, CommandInfo>): void

取消会话快退事件监听。使用callback异步回调。

指定callback，取消对应监听；未指定callback，则取消所有事件监听。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackTwoParamCallback<number, [CommandInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__commandinfo22)>否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.offRewind();
```

#### off('seek')10+

off(type: 'seek', callback?: (time: number) => void): void

取消跳转节点事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持关闭事件'seek'。callback(time: number) => void否

回调函数，参数time是时间节点，单位为毫秒。

当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('seek');
```

#### off('setSpeed')10+

off(type: 'setSpeed', callback?: (speed: number) => void): void

取消播放速率变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持关闭事件'setSpeed'。callback(speed: number) => void否

回调函数，参数speed是播放倍速。

当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('setSpeed');
```

#### off('setLoopMode')10+

off(type: 'setLoopMode', callback?: (mode: LoopMode) => void): void

取消循环模式变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持关闭事件'setLoopMode'。callback(mode: [LoopMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__loopmode10)) => void否

回调函数，参数mode是循环模式。

- 当监听事件取消成功，err为undefined，否则返回错误对象。

- 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('setLoopMode');
```

#### off('setTargetLoopMode')18+

off(type: 'setTargetLoopMode', callback?: Callback<LoopMode>): void

取消目标循环模式变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持关闭事件'setTargetLoopMode'。callbackCallback<[LoopMode](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__loopmode10)>否

回调函数，参数表示目标循环模式。

- 当监听事件取消成功，err为undefined，否则返回错误对象。

- 该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('setTargetLoopMode');
```

#### off('toggleFavorite')10+

off(type: 'toggleFavorite', callback?: (assetId: string) => void): void

取消是否收藏的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持关闭事件'toggleFavorite'。callback(assetId: string) => void否

回调函数，参数assetId是媒体ID。

当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('toggleFavorite');
```

#### off('skipToQueueItem')10+

off(type: 'skipToQueueItem', callback?: (itemId: number) => void): void

取消播放列表单项选中的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持关闭事件'skipToQueueItem'。callback(itemId: number) => void否

回调函数，参数itemId是播放列表单项ID。

当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('skipToQueueItem');
```

#### off('handleKeyEvent')10+

off(type: 'handleKeyEvent', callback?: (event: KeyEvent) => void): void

取消按键事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持关闭事件'handleKeyEvent'。callback(event: [KeyEvent](../../modules/ohos/@ohos.multimodalInput.keyEvent (按键输入事件).md)) => void否

回调函数，参数event是按键事件。

当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('handleKeyEvent');
```

#### off('outputDeviceChange')10+

off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void

取消播放设备变化的事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持关闭事件'outputDeviceChange'。callback(state: [ConnectionState](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__connectionstate10), device: [OutputDeviceInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__outputdeviceinfo10)) => void否

回调函数，参数device是设备相关信息。

当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('outputDeviceChange');
```

#### off('commonCommand')10+

off(type: 'commonCommand', callback?: (command: string, args: Record<string, Object>) => void): void

取消自定义控制命令的变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'commonCommand'。callback(command: string, args: Record<string, Object>) => void否

回调函数，参数command是变化的自定义控制命令名，args为自定义控制命令的参数。

该参数为可选参数，若不填写该参数，则认为取消所有对command事件的监听。

API version 20开始发生兼容变更，在API version 19及之前的版本callback的参数类型为：(command: string, args:{[key: string]: Object}) => void。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('commonCommand');
```

#### on('answer')11+

on(type: 'answer', callback: Callback<void>): void

设置通话接听的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'answer'：当通话接听时，触发该事件。callbackCallback<void>是回调函数。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('answer', () => {
  console.info('on call answer');
});
```

#### off('answer')11+

off(type: 'answer', callback?: Callback<void>): void

取消通话接听事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'answer'。callbackCallback<void>否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('answer');
```

#### on('hangUp')11+

on(type: 'hangUp', callback: Callback<void>): void

设置通话挂断的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'hangUp'：当通话挂断时，触发该事件。callbackCallback<void>是回调函数。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('hangUp', () => {
  console.info('on call hangUp');
});
```

#### off('hangUp')11+

off(type: 'hangUp', callback?: Callback<void>): void

取消通话挂断事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'hangUp'。callbackCallback<void>否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('hangUp');
```

#### on('toggleCallMute')11+

on(type: 'toggleCallMute', callback: Callback<void>): void

设置通话静音的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'toggleCallMute'：当通话静音或解除静音时，触发该事件。callbackCallback<void>是回调函数。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('toggleCallMute', () => {
  console.info('on call toggleCallMute');
});
```

#### off('toggleCallMute')11+

off(type: 'toggleCallMute', callback?: Callback<void>): void

取消通话静音事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'toggleCallMute'。callbackCallback<void>否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('toggleCallMute');
```

#### on('castDisplayChange')12+

on(type: 'castDisplayChange', callback: Callback<CastDisplayInfo>): void

设置扩展屏投播显示设备变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'castDisplayChange'：当扩展屏投播显示设备变化时触发事件。callbackCallback<[CastDisplayInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__castdisplayinfo12)>是回调函数。参数是扩展屏投播显示设备信息。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
let castDisplay: avSession.CastDisplayInfo;
currentAVSession.on('castDisplayChange', (display: avSession.CastDisplayInfo) => {
    if (display.state === avSession.CastDisplayState.STATE_ON) {
        castDisplay = display;
        console.info(`Succeeded in castDisplayChange display : ${display.id} ON`);
    } else if (display.state === avSession.CastDisplayState.STATE_OFF){
        console.info(`Succeeded in castDisplayChange display : ${display.id} OFF`);
    }
});
```

#### off('castDisplayChange')12+

 off(type: 'castDisplayChange', callback?: Callback<CastDisplayInfo>): void

取消扩展屏投播显示设备变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'castDisplayChange'。callbackCallback<[CastDisplayInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__castdisplayinfo12)>否回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('castDisplayChange');
```

#### stopCasting10+

stopCasting(callback: AsyncCallback<void>): void

结束投播。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当命令发送成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600109The remote connection is not established.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.stopCasting((err: BusinessError) => {
  if (err) {
    console.error(`stopCasting BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('stopCasting successfully');
  }
});
```

#### stopCasting10+

stopCasting(): Promise<void>

结束投播。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**返回值：**

类型说明Promise<void>Promise对象。当成功结束投播，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600109The remote connection is not established.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

currentAVSession.stopCasting().then(() => {
  console.info('stopCasting successfully');
}).catch((err: BusinessError) => {
  console.error(`stopCasting BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getOutputDeviceSync10+

getOutputDeviceSync(): OutputDeviceInfo

使用同步方法获取当前输出设备信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明[OutputDeviceInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__outputdeviceinfo10)当前输出设备信息。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentOutputDevice: avSession.OutputDeviceInfo = currentAVSession.getOutputDeviceSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getOutputDeviceSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

#### getAllCastDisplays12+

getAllCastDisplays(): Promise<Array<CastDisplayInfo>>

获取当前系统中所有支持扩展屏投播的显示设备。通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**返回值：**

类型说明Promise<Array<[CastDisplayInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__castdisplayinfo12)>>Promise对象，返回当前系统中所有支持扩展屏投播的显示设备。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let castDisplay: avSession.CastDisplayInfo;
currentAVSession.getAllCastDisplays().then((data: Array< avSession.CastDisplayInfo >) => {
    if (data.length >= 1) {
       castDisplay = data[0];
     }
   }).catch((err: BusinessError) => {
     console.error(`Failed to getAllCastDisplay. Code: ${err.code}, message: ${err.message}`);
   });
```

#### on('playFromAssetId')(deprecated)

on(type:'playFromAssetId', callback: (assetId: number) => void): void

设置媒体id播放监听事件。

从 API version 11 开始支持，从 API version 20 开始废弃。建议使用[on('playWithAssetId')](#ZH-CN_TOPIC_0000002497605762__onplaywithassetid20)设置媒体id播放监听事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件是'playFromAssetId'，当媒体id播放时，触发该事件回调。callback(assetId: number) => void是回调函数。参数assetId是媒体id。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('playFromAssetId', (assetId: number) => {
  console.info('on playFromAssetId entry');
});
```

#### off('playFromAssetId')(deprecated)

off(type: 'playFromAssetId', callback?: (assetId: number) => void): void

取消媒体id播放事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

从 API version 11 开始支持，从 API version 20 开始废弃。建议使用[off('playWithAssetId')](#ZH-CN_TOPIC_0000002497605762__offplaywithassetid20)取消媒体id播放事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是关闭对应的监听事件，支持的事件是'playFromAssetId'。callback(assetId: number) => void否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。参数assetId是媒体id。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('playFromAssetId');
```

#### on('customDataChange')20+

on(type: 'customDataChange', callback: Callback<Record<string, Object>>): void

注册从远程设备发送的自定义数据的监听器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'customDataChange'，当媒体提供方发送自定义数据时，触发该事件。callbackCallback<Record<string, Object>>是回调函数，用于接收自定义数据。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it.6600102The session does not exist.

**示例：**

```ets
currentAVSession.on('customDataChange', (callback) => {
    console.info(`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}`);
});
```

#### off('customDataChange')20+

off(type: 'customDataChange', callback?: Callback<Record<string, Object>>): void

取消自定义数据监听。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持的事件是'customDataChange'。callbackCallback<Record<string, Object>>否注册监听事件时的回调函数。该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it.6600102The session does not exist.

**示例：**

```ets
currentAVSession.off('customDataChange');
```