# Interface (AVSessionController)

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本Interface首批接口从API version 10开始支持。

AVSessionController控制器可查看会话ID，并可完成对会话发送命令及事件，获取会话元数据，播放状态信息等操作。

#### 导入模块

```ets
import { avSession } from '@kit.AVSessionKit';
```

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

名称类型只读可选说明sessionId10+string是否AVSessionController对象唯一的会话标识。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private AVSessionController?: avSession.AVSessionController;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {

    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio").then(async (data: avSession.AVSession) => {
      this.currentAVSession = data;
      this.sessionId = this.currentAVSession.sessionId;
      this.AVSessionController = await this.currentAVSession.getController();
      console.info('CreateAVSession :  SUCCESS :sessionId = ${this.sessionId}');
    }).catch((err: BusinessError) => {
      console.error(`CreateController BusinessError: code: ${err.code}, message: ${err.message}`);
    });
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

#### getAVPlaybackState10+

getAVPlaybackState(callback: AsyncCallback<AVPlaybackState>): void

获取当前的远端播放状态。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)>是回调函数，返回远端播放状态。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVPlaybackState((err: BusinessError, state: avSession.AVPlaybackState) => {
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

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<[AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)>Promise对象。返回远端播放状态。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVPlaybackState().then((state: avSession.AVPlaybackState) => {
  console.info('getAVPlaybackState : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`getAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getAVMetadata10+

getAVMetadata(): Promise<AVMetadata>

获取会话元数据。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<[AVMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avmetadata10)>Promise对象，返回会话元数据。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVMetadata().then((metadata: avSession.AVMetadata) => {
  console.info(`GetAVMetadata : SUCCESS : assetId : ${metadata.assetId}`);
}).catch((err: BusinessError) => {
  console.error(`GetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getAVMetadata10+

getAVMetadata(callback: AsyncCallback<AVMetadata>): void

获取会话元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avmetadata10)>是回调函数，返回会话元数据。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVMetadata((err: BusinessError, metadata: avSession.AVMetadata) => {
  if (err) {
    console.error(`GetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetAVMetadata : SUCCESS : assetId : ${metadata.assetId}`);
  }
});
```

#### getAVQueueTitle10+

getAVQueueTitle(): Promise<string>

获取当前会话播放列表的名称。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<string>Promise对象。返回播放列表名称。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueTitle().then((title: string) => {
  console.info(`GetAVQueueTitle : SUCCESS : title : ${title}`);
}).catch((err: BusinessError) => {
  console.error(`GetAVQueueTitle BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getAVQueueTitle10+

getAVQueueTitle(callback: AsyncCallback<string>): void

获取当前播放列表的名称。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<string>是回调函数，返回播放列表名称。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueTitle((err: BusinessError, title: string) => {
  if (err) {
    console.error(`GetAVQueueTitle BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetAVQueueTitle : SUCCESS : title : ${title}`);
  }
});
```

#### getAVQueueItems10+

getAVQueueItems(): Promise<Array<AVQueueItem>>

获取当前会话播放列表相关信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<Array<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>>Promise对象。返回播放列表队列。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueItems().then((items: avSession.AVQueueItem[]) => {
  console.info(`GetAVQueueItems : SUCCESS : length : ${items.length}`);
}).catch((err: BusinessError) => {
  console.error(`GetAVQueueItems BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getAVQueueItems10+

getAVQueueItems(callback: AsyncCallback<Array<AVQueueItem>>): void

获取当前播放列表相关信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>>是回调函数，返回播放列表队列。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVQueueItems((err: BusinessError, items: avSession.AVQueueItem[]) => {
  if (err) {
    console.error(`GetAVQueueItems BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetAVQueueItems : SUCCESS : length : ${items.length}`);
  }
});
```

#### skipToQueueItem10+

skipToQueueItem(itemId: number): Promise<void>

设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明itemIdnumber是播放列表单项的ID值，用以表示选中的播放列表单项。

**返回值：**

类型说明Promise<void>Promise对象。当播放列表单项ID设置成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let queueItemId = 0;
avsessionController.skipToQueueItem(queueItemId).then(() => {
  console.info('SkipToQueueItem successfully');
}).catch((err: BusinessError) => {
  console.error(`SkipToQueueItem BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### skipToQueueItem10+

skipToQueueItem(itemId: number, callback: AsyncCallback<void>): void

设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明itemIdnumber是播放列表单项的ID值，用以表示选中的播放列表单项。callbackAsyncCallback<void>是回调函数。当播放状态设置成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let queueItemId = 0;
avsessionController.skipToQueueItem(queueItemId, (err: BusinessError) => {
  if (err) {
    console.error(`SkipToQueueItem BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SkipToQueueItem successfully');
  }
});
```

#### getOutputDevice10+

getOutputDevice(): Promise<OutputDeviceInfo>

获取播放设备信息。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<[OutputDeviceInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__outputdeviceinfo10)>Promise对象，返回播放设备信息。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息600101Session service exception.600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getOutputDevice().then((deviceInfo: avSession.OutputDeviceInfo) => {
  console.info('GetOutputDevice : SUCCESS');
}).catch((err: BusinessError) => {
  console.error(`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getOutputDevice10+

getOutputDevice(callback: AsyncCallback<OutputDeviceInfo>): void

获取播放设备信息。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[OutputDeviceInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__outputdeviceinfo10)>是回调函数，返回播放设备信息。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息600101Session service exception.600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getOutputDevice((err: BusinessError, deviceInfo: avSession.OutputDeviceInfo) => {
  if (err) {
    console.error(`GetOutputDevice BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('GetOutputDevice : SUCCESS');
  }
});
```

#### sendAVKeyEvent10+

sendAVKeyEvent(event: KeyEvent): Promise<void>

发送按键事件到控制器对应的会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明event[KeyEvent](../../modules/ohos/@ohos.multimodalInput.keyEvent (按键输入事件).md)是按键事件。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.600101Session service exception.600102The session does not exist.600103The session controller does not exist.600105Invalid session command.600106The session is not activated.

**返回值：**

类型说明Promise<void>Promise对象。当事件发送成功，无返回结果，否则返回错误对象。

**示例：**

```ets
import { Key, KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyItem: Key = {code:0x49, pressedTime:2, deviceId:0};
let event:KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:[keyItem], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};

avsessionController.sendAVKeyEvent(event).then(() => {
  console.info('SendAVKeyEvent Successfully');
}).catch((err: BusinessError) => {
  console.error(`SendAVKeyEvent BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### sendAVKeyEvent10+

sendAVKeyEvent(event: KeyEvent, callback: AsyncCallback<void>): void

发送按键事件到会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明event[KeyEvent](../../modules/ohos/@ohos.multimodalInput.keyEvent (按键输入事件).md)是按键事件。callbackAsyncCallback<void>是回调函数。当事件发送成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.600101Session service exception.600102The session does not exist.600103The session controller does not exist.600105Invalid session command.600106The session is not activated.

**示例：**

```ets
import { Key, KeyEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

let keyItem: Key = {code:0x49, pressedTime:2, deviceId:0};
let event:KeyEvent = {id:1, deviceId:0, actionTime:1, screenId:1, windowId:1, action:2, key:keyItem, unicodeChar:0, keys:[keyItem], ctrlKey:false, altKey:false, shiftKey:false, logoKey:false, fnKey:false, capsLock:false, numLock:false, scrollLock:false};
avsessionController.sendAVKeyEvent(event, (err: BusinessError) => {
  if (err) {
    console.error(`SendAVKeyEvent BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SendAVKeyEvent Successfully');
  }
});
```

#### getLaunchAbility10+

getLaunchAbility(): Promise<WantAgent>

获取应用在会话中保存的WantAgent对象。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<[WantAgent](../../modules/ohos/@ohos.app.ability.wantAgent (WantAgent模块).md)>Promise对象，返回在[setLaunchAbility](Interface (AVSession).md#ZH-CN_TOPIC_0000002497605762__setlaunchability10)保存的对象，包括应用的相关属性信息，如bundleName，abilityName，deviceId等。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getLaunchAbility().then((agent: object) => {
  console.info(`GetLaunchAbility : SUCCESS : wantAgent : ${agent}`);
}).catch((err: BusinessError) => {
  console.error(`GetLaunchAbility BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getLaunchAbility10+

getLaunchAbility(callback: AsyncCallback<WantAgent>): void

获取应用在会话中保存的WantAgent对象。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[WantAgent](../../modules/ohos/@ohos.app.ability.wantAgent (WantAgent模块).md)>是回调函数。返回在[setLaunchAbility](Interface (AVSession).md#ZH-CN_TOPIC_0000002497605762__setlaunchability10)保存的对象，包括应用的相关属性信息，如bundleName，abilityName，deviceId等。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getLaunchAbility((err: BusinessError, agent: object) => {
  if (err) {
    console.error(`GetLaunchAbility BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetLaunchAbility : SUCCESS : wantAgent : ${agent}`);
  }
});
```

#### getRealPlaybackPositionSync10+

getRealPlaybackPositionSync(): number

获取当前播放位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明number时间节点，毫秒数。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
let time: number = avsessionController.getRealPlaybackPositionSync();
```

#### isActive10+

isActive(): Promise<boolean>

获取会话是否被激活。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<boolean>Promise对象，返回会话是否为激活状态，true表示被激活，false表示禁用。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.isActive().then((isActive: boolean) => {
  console.info(`IsActive : SUCCESS : isactive : ${isActive}`);
}).catch((err: BusinessError) => {
  console.error(`IsActive BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### isActive10+

isActive(callback: AsyncCallback<boolean>): void

判断会话是否被激活。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回会话是否为激活状态，true表示被激活，false表示禁用。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.isActive((err: BusinessError, isActive: boolean) => {
  if (err) {
    console.error(`IsActive BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`IsActive : SUCCESS : isactive : ${isActive}`);
  }
});
```

#### destroy10+

destroy(): Promise<void>

销毁当前控制器，销毁后当前控制器不可再用。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<void>Promise对象。当控制器销毁成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.destroy().then(() => {
  console.info('Destroy : SUCCESS ');
}).catch((err: BusinessError) => {
  console.error(`Destroy BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### destroy10+

destroy(callback: AsyncCallback<void>): void

销毁当前控制器，销毁后当前控制器不可再用。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当控制器销毁成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.destroy((err: BusinessError) => {
  if (err) {
    console.error(`Destroy BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Destroy : SUCCESS ');
  }
});
```

#### getValidCommands10+

getValidCommands(): Promise<Array<AVControlCommandType>>

获取会话支持的有效命令。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<Array<[AVControlCommandType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avcontrolcommandtype10)>>Promise对象。返回有效命令的集合。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getValidCommands().then((validCommands: avSession.AVControlCommandType[]) => {
  console.info(`GetValidCommands : SUCCESS : size : ${validCommands.length}`);
}).catch((err: BusinessError) => {
  console.error(`GetValidCommands BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getValidCommands10+

getValidCommands(callback: AsyncCallback<Array<AVControlCommandType>>): void

获取会话支持的有效命令。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[AVControlCommandType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avcontrolcommandtype10)>>是回调函数，返回有效命令的集合。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getValidCommands((err: BusinessError, validCommands: avSession.AVControlCommandType[]) => {
  if (err) {
    console.error(`GetValidCommands BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`GetValidCommands : SUCCESS : size : ${validCommands.length}`);
  }
});
```

#### sendControlCommand10+

sendControlCommand(command: AVControlCommand): Promise<void>

通过控制器发送命令到其对应的会话。结果通过Promise异步回调方式返回。

媒体控制方在使用sendControlCommand命令前，需要确保控制对应的媒体会话注册了对应的监听，注册媒体会话相关监听的方法请参见接口[on'play'](Interface (AVSession).md#ZH-CN_TOPIC_0000002497605762__onplay10)、[on'pause'](Interface (AVSession).md#ZH-CN_TOPIC_0000002497605762__onpause10)等。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明command[AVControlCommand](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcontrolcommand10)是会话的相关命令和命令相关参数。

**返回值：**

类型说明Promise<void>Promise对象。当命令发送成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.6600105Invalid session command.6600106The session is not activated.6600107Too many commands or events.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avCommand: avSession.AVControlCommand = {command:'play'};
avsessionController.sendControlCommand(avCommand).then(() => {
  console.info('SendControlCommand successfully');
}).catch((err: BusinessError) => {
  console.error(`SendControlCommand BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### sendControlCommand10+

sendControlCommand(command: AVControlCommand, callback: AsyncCallback<void>): void

通过会话控制器发送命令到其对应的会话。结果通过callback异步回调方式返回。

媒体控制方在使用sendControlCommand命令前，需要确保控制对应的媒体会话注册了对应的监听，注册媒体会话相关监听的方法请参见接口[on'play'](Interface (AVSession).md#ZH-CN_TOPIC_0000002497605762__onplay10)、[on'pause'](Interface (AVSession).md#ZH-CN_TOPIC_0000002497605762__onpause10)等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明command[AVControlCommand](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcontrolcommand10)是会话的相关命令和命令相关参数。callbackAsyncCallback<void>是回调函数。当命令发送成功，err为undefined，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.6600105Invalid session command.6600106The session is not activated.6600107Too many commands or events.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let avCommand: avSession.AVControlCommand = {command:'play'};
avsessionController.sendControlCommand(avCommand, (err: BusinessError) => {
  if (err) {
    console.error(`SendControlCommand BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('SendControlCommand successfully');
  }
});
```

#### sendCommonCommand10+

sendCommonCommand(command: string, args: Record<string, Object>): Promise<void>

通过会话控制器发送自定义控制命令到其对应的会话。结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明commandstring是需要设置的自定义控制命令的名称。argsRecord<string, Object>是

需要传递的控制命令键值对。

API version 20开始发生兼容变更，在API version 19及之前的版本args的参数类型为：{[key: string]: Object}。

参数args支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](../../modules/ohos/@ohos.app.ability.Want (Want).md)。

**返回值：**

类型说明Promise<void>Promise对象。当命令发送成功，无返回结果，否则返回错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.6600105Invalid session command.6600106The session is not activated.6600107Too many commands or events.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
let commandName = "my_command";
if (controller !== undefined) {
  (controller as avSession.AVSessionController).sendCommonCommand(commandName, {command : "This is my command"}).then(() => {
    console.info('SendCommonCommand successfully');
  }).catch((err: BusinessError) => {
    console.error(`SendCommonCommand BusinessError: code: ${err.code}, message: ${err.message}`);
  })
}
```

#### sendCommonCommand10+

sendCommonCommand(command: string, args: Record<string, Object>, callback: AsyncCallback<void>): void

通过会话控制器发送自定义命令到其对应的会话。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明commandstring是需要设置的自定义控制命令的名称。argsRecord<string, Object>是

需要传递的控制命令键值对。

API version 20开始发生兼容变更，在API version 19及之前的版本args的参数类型为：{[key: string]: Object}。

callbackAsyncCallback<void>是回调函数。当命令发送成功，err为undefined，否则返回错误对象。

参数args支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](../../modules/ohos/@ohos.app.ability.Want (Want).md)。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.6600105Invalid session command.6600106The session is not activated.6600107Too many commands or events.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
let commandName = "my_command";
if (controller !== undefined) {
  (controller as avSession.AVSessionController).sendCommonCommand(commandName, {command : "This is my command"}, (err: BusinessError) => {
    if (err) {
      console.error(`SendCommonCommand BusinessError: code: ${err.code}, message: ${err.message}`);
    }
  })
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

错误码ID错误信息6600101Session service exception.You are advised to:1.Scheduled retry.2.Destroy the current session or session controller and re-create it.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private controller: avSession.AVSessionController | undefined = undefined;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {
    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
      .then(async (data: avSession.AVSession) => {
        this.currentAVSession = data;
        this.sessionId = this.currentAVSession.sessionId;
        this.controller = await this.currentAVSession.getController();
        console.info(`CreateAVSession : SUCCESS :sessionId = ${this.sessionId}`);
      })
      .catch((err: BusinessError) => {
        console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
      });

    if (this.controller !== undefined) {
      (this.controller as avSession.AVSessionController).sendCustomData({ customData: "This is my data" })
    }
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

#### getExtras10+

getExtras(): Promise<Record<string, Object>>

获取媒体提供方设置的自定义媒体数据包。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<Record<string, Object>>

Promise对象，返回媒体提供方设置的自定义媒体数据包，数据包的内容与setExtras设置的内容完全一致。

API version 20开始发生兼容变更，在API version 19及之前的版本其返回值类型为：Promise<{[key: string]: Object}>。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.6600105Invalid session command.6600107Too many commands or events.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

@Entry
@Component
struct Index {
  private tag: string = "createNewSession";
  private sessionId: string = "";
  private controller: avSession.AVSessionController | undefined = undefined;
  private currentAVSession?: avSession.AVSession;
  context = this.getUIContext();

  aboutToAppear(): void {

    avSession.createAVSession(this.getUIContext().getHostContext(), this.tag, "audio")
      .then(async (data: avSession.AVSession) => {
        this.currentAVSession = data;
        this.sessionId = this.currentAVSession.sessionId;
        this.controller = await this.currentAVSession.getController();
        console.info(`CreateAVSession : SUCCESS :sessionId = ${this.sessionId}`);
      }).catch((err: BusinessError) => {
      console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
    });
    if (this.controller !== undefined) {
      (this.controller as avSession.AVSessionController).getExtras().then((extras) => {
        console.info(`getExtras : SUCCESS : ${extras}`);
      }).catch((err: BusinessError) => {
        console.error(`getExtras BusinessError: code: ${err.code}, message: ${err.message}`);
      });
    }
  }

  build() {
    Column() {
      Text('AVSession Demo')
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```

#### getExtras10+

getExtras(callback: AsyncCallback<Record<string, Object>>): void

获取媒体提供方设置的自定义媒体数据包。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<Record<string, Object>>是

回调函数，返回媒体提供方设置的自定义媒体数据包，数据包的内容与setExtras设置的内容完全一致。

API version 20开始发生兼容变更，在API version 19及之前的版本callback的参数类型为：AsyncCallback<{[key: string]: Object}>。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.6600105Invalid session command.6600107Too many commands or events.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).getExtras((err, extras) => {
    if (err) {
      console.error(`getExtras BusinessError: code: ${err.code}, message: ${err.message}`);
    } else {
      console.info(`getExtras : SUCCESS : ${extras}`);
    }
  });
}
```

#### getExtrasWithEvent18+

getExtrasWithEvent(extraEvent: string): Promise<ExtraInfo>

根据远端分布式事件类型，获取远端分布式媒体提供方设置的自定义媒体数据包。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明extraEventstring是

远端分布式事件类型。

当前支持的事件类型包括：

'AUDIO_GET_VOLUME'：获取远端设备音量，

'AUDIO_GET_AVAILABLE_DEVICES'：获取远端所有可连接设备，

'AUDIO_GET_PREFERRED_OUTPUT_DEVICE_FOR_RENDERER_INFO'：获取远端实际发声设备。

**返回值：**

类型说明Promise<[ExtraInfo](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__extrainfo18)>

Promise对象，返回远端分布式媒体提供方设置的自定义媒体数据包。

参数ExtraInfo支持的数据类型有：字符串、数字、布尔、对象、数组和文件描述符等，详细介绍请参见[@ohos.app.ability.Want(Want)](../../modules/ohos/@ohos.app.ability.Want (Want).md)。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.6600105Invalid session command.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let controller: avSession.AVSessionController | ESObject;
const COMMON_COMMAND_STRING_1 = 'AUDIO_GET_VOLUME';
const COMMON_COMMAND_STRING_2 = 'AUDIO_GET_AVAILABLE_DEVICES';
const COMMON_COMMAND_STRING_3 = 'AUDIO_GET_PREFERRED_OUTPUT_DEVICE_FOR_RENDERER_INFO';
if (controller !== undefined) {
  controller.getExtrasWithEvent(COMMON_COMMAND_STRING_1).then(() => {
    console.info(`${[COMMON_COMMAND_STRING_1]}`);
  }).catch((err: BusinessError) => {
    console.error(`getExtrasWithEvent failed with err: ${err.code}, ${err.message}`);
  })

  controller.getExtrasWithEvent(COMMON_COMMAND_STRING_2).then(() => {
    console.info(`${[COMMON_COMMAND_STRING_2]}`);
  }).catch((err: BusinessError) => {
    console.error(`getExtrasWithEvent failed with err: ${err.code}, ${err.message}`);
  })

  controller.getExtrasWithEvent(COMMON_COMMAND_STRING_3).then(() => {
    console.info(`${[COMMON_COMMAND_STRING_3]}`);
  }).catch((err: BusinessError) => {
    console.error(`getExtrasWithEvent failed with err: ${err.code}, ${err.message}`);
  })
}
```

#### on('metadataChange')10+

on(type: 'metadataChange', filter: Array<string> | 'all', callback: (data: AVMetadata) => void): void

设置元数据变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是

事件回调类型，支持事件'metadataChange'：当元数据需要更新时，触发该事件。

需要更新表示对应属性值被重新设置过，不论新值与旧值是否相同。

filterArray<string>|'all'是

'all'表示关注通话状态所有字段变化；Array<string>表示关注Array中的字段变化。

API version 20开始发生兼容变更，在API version 19及之前filter参数类型为：Array<keyof AVMetadata> | 'all'。

callback(data: [AVMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avmetadata10)) => void是回调函数，参数data是需要更新的元数据。只包含需要更新的元数据属性，不代表当前全量的元数据。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.on('metadataChange', 'all', (metadata: avSession.AVMetadata) => {
  console.info(`on metadataChange assetId : ${metadata.assetId}`);
});

avsessionController.on('metadataChange', ['assetId', 'title', 'description'], (metadata: avSession.AVMetadata) => {
  console.info(`on metadataChange assetId : ${metadata.assetId}`);
});
```

#### off('metadataChange')10+

off(type: 'metadataChange', callback?: (data: AVMetadata) => void): void

取消元数据变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'metadataChange'。callback(data: [AVMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avmetadata10)) => void否

回调函数，参数data是需要更新的元数据。只包含需要更新的元数据属性，并不代表当前全量的元数据。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('metadataChange');
```

#### on('playbackStateChange')10+

on(type: 'playbackStateChange', filter: Array<string> | 'all', callback: (state: AVPlaybackState) => void): void

设置播放状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是

事件回调类型，支持事件'playbackStateChange'，当播放状态需要更新时，触发该事件。

需要更新表示对应属性值被重新设置过，不论新值与旧值是否相同。

filterArray<string>|'all'是

'all'表示关注播放状态所有字段更新。

Array<string> 表示关注Array中的字段更新。

API version 20开始发生兼容变更，在API version 19及之前filter参数类型为：Array<keyof AVPlaybackstate> | 'all'。

callback(state: [AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)) => void是回调函数，参数state是需要更新的播放状态。只包含需要更新的播放状态属性，并不代表当前全量的播放状态。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.on('playbackStateChange', 'all', (playbackState: avSession.AVPlaybackState) => {
  console.info(`on playbackStateChange state : ${playbackState.state}`);
});

avsessionController.on('playbackStateChange', ['state', 'speed', 'loopMode'], (playbackState: avSession.AVPlaybackState) => {
  console.info(`on playbackStateChange state : ${playbackState.state}`);
});
```

#### off('playbackStateChange')10+

off(type: 'playbackStateChange', callback?: (state: AVPlaybackState) => void)

取消播放状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'playbackStateChange'。callback(state: [AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)) => void否

回调函数，参数state是需要更新的播放状态。只包含需要更新的播放状态属性，并不代表当前全量的播放状态。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('playbackStateChange');
```

#### on('callMetadataChange')11+

on(type: 'callMetadataChange', filter: Array<string> | 'all', callback: Callback<CallMetadata>): void

设置通话元数据变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'callMetadataChange'：当通话元数据变化时，触发该事件。filterArray<string>|'all'是

'all'表示关注通话元数据所有字段变化；Array<string> 表示关注Array中的字段变化。

API version 20开始发生兼容变更，在API version 19及之前filter参数类型为：Array<keyof CallMetadata> | 'all'。

callbackCallback<[CallMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__callmetadata11)>是回调函数，参数callmetadata是变化后的通话元数据。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.on('callMetadataChange', 'all', (callmetadata: avSession.CallMetadata) => {
  console.info(`on callMetadataChange state : ${callmetadata.name}`);
});

avsessionController.on('callMetadataChange', ['name'], (callmetadata: avSession.CallMetadata) => {
  console.info(`on callMetadataChange state : ${callmetadata.name}`);
});
```

#### off('callMetadataChange')11+

off(type: 'callMetadataChange', callback?: Callback<CallMetadata>): void

取消设置通话元数据变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'callMetadataChange'。callbackCallback<[CallMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__callmetadata11)>否

回调函数，参数calldata是变化后的通话原数据。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('callMetadataChange');
```

#### on('callStateChange')11+

on(type: 'callStateChange', filter: Array<string> | 'all', callback: Callback<AVCallState>): void

设置通话状态变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'callStateChange'：当通话状态变化时，触发该事件。filterArray<string>|'all'是

'all' 表示关注通话状态所有字段变化；Array<string>表示关注Array中的字段变化。

API version 20开始发生兼容变更，在API version 19及之前filter参数类型为：Array<keyof AVCallState> | 'all'。

callbackCallback<[AVCallState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcallstate11)>是回调函数，参数callstate是变化后的通话状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified.2.Incorrect parameter types.6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.on('callStateChange', 'all', (callstate: avSession.AVCallState) => {
  console.info(`on callStateChange state : ${callstate.state}`);
});

avsessionController.on('callStateChange', ['state'], (callstate: avSession.AVCallState) => {
  console.info(`on callStateChange state : ${callstate.state}`);
});
```

#### off('callStateChange')11+

off(type: 'callStateChange', callback?: Callback<AVCallState>): void

取消设置通话状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'callStateChange'。callbackCallback<[AVCallState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcallstate11)>否

回调函数，参数callstate是变化后的通话状态。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('callMetadataChange');
```

#### on('sessionDestroy')10+

on(type: 'sessionDestroy', callback: () => void): void

会话销毁的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'sessionDestroy'：当检测到会话销毁时，触发该事件）。callback() => void是回调函数。当监听事件注册成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.on('sessionDestroy', () => {
  console.info('on sessionDestroy : SUCCESS ');
});
```

#### off('sessionDestroy')10+

off(type: 'sessionDestroy', callback?: () => void): void

取消监听会话的销毁事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'sessionDestroy'。callback() => void否

回调函数。当监听事件取消成功，err为undefined，否则返回错误对象。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('sessionDestroy');
```

#### on('activeStateChange')10+

on(type: 'activeStateChange', callback: (isActive: boolean) => void): void

会话的激活状态的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'activeStateChange'：当检测到会话的激活状态发生改变时，触发该事件。callback(isActive: boolean) => void是回调函数。参数isActive表示会话是否被激活。true表示被激活，false表示禁用。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.on('activeStateChange', (isActive: boolean) => {
  console.info(`on activeStateChange : SUCCESS : isActive ${isActive}`);
});
```

#### off('activeStateChange')10+

off(type: 'activeStateChange', callback?: (isActive: boolean) => void): void

取消监听会话激活状态变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'activeStateChange'。callback(isActive: boolean) => void否

回调函数。参数isActive表示会话是否被激活。true表示被激活，false表示禁用。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('activeStateChange');
```

#### on('validCommandChange')10+

on(type: 'validCommandChange', callback: (commands: Array<AVControlCommandType>) => void): void

会话支持的有效命令变化监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'validCommandChange'：当检测到会话的合法命令发生改变时，触发该事件。callback(commands: Array<[AVControlCommandType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avcontrolcommandtype10)>) => void是回调函数。参数commands是有效命令的集合。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.on('validCommandChange', (validCommands: avSession.AVControlCommandType[]) => {
  console.info(`validCommandChange : SUCCESS : size : ${validCommands.length}`);
  console.info(`validCommandChange : SUCCESS : validCommands : ${validCommands.values()}`);
});
```

#### off('validCommandChange')10+

off(type: 'validCommandChange', callback?: (commands: Array<AVControlCommandType>) => void): void

取消监听会话有效命令变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'validCommandChange'。callback(commands: Array<[AVControlCommandType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avcontrolcommandtype10)>) => void否

回调函数。参数commands是有效命令的集合。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('validCommandChange');
```

#### on('outputDeviceChange')10+

on(type: 'outputDeviceChange', callback: (state: ConnectionState, device: OutputDeviceInfo) => void): void

设置播放设备变化的监听事件。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件为'outputDeviceChange'：当播放设备变化时，触发该事件）。callback(state: [ConnectionState](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__connectionstate10), device: [OutputDeviceInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__outputdeviceinfo10)) => void是回调函数，参数device是设备相关信息。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.on('outputDeviceChange', (state: avSession.ConnectionState, device: avSession.OutputDeviceInfo) => {
  console.info(`on outputDeviceChange state: ${state}, device : ${device}`);
});
```

#### off('outputDeviceChange')10+

off(type: 'outputDeviceChange', callback?: (state: ConnectionState, device: OutputDeviceInfo) => void): void

取消监听分布式设备变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'outputDeviceChange'。callback(state: [ConnectionState](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002529445729__connectionstate10), device: [OutputDeviceInfo](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__outputdeviceinfo10)) => void否

回调函数，参数device是设备相关信息。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('outputDeviceChange');
```

#### on('sessionEvent')10+

on(type: 'sessionEvent', callback: (sessionEvent: string, args: Record<String, Object>) => void): void

媒体控制器设置会话自定义事件变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'sessionEvent'：当会话事件变化时，触发该事件。callback(sessionEvent: string, args: Record<String, Object>) => void是

回调函数，sessionEvent为变化的会话事件名，args为事件的参数。

API version 20开始发生兼容变更，在API version 19及之前的版本callback的参数类型为：(sessionEvent: string, args: {[key: string]: Object}) => void。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).on('sessionEvent', (sessionEvent, args) => {
    console.info(`OnSessionEvent, sessionEvent is ${sessionEvent}, args: ${JSON.stringify(args)}`);
  });
}
```

#### off('sessionEvent')10+

off(type: 'sessionEvent', callback?: (sessionEvent: string, args: Record<String, Object>) => void): void

取消会话事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'sessionEvent'。callbacksessionEvent: string, args: Record<String, Object> => void否

回调函数，参数sessionEvent是变化的事件名，args为事件的参数。

API version 20开始发生兼容变更，在API version 19及之前的版本callback的参数类型为：(sessionEvent: string, args: {[key: string]: Object}) => void。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('sessionEvent');
```

#### on('queueItemsChange')10+

on(type: 'queueItemsChange', callback: (items: Array<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>) => void): void

媒体控制器设置会话自定义播放列表变化的监听器。

每个指令支持注册多个回调，如果需要只执行最新监听，需要先注销旧的监听，否则新旧监听都会触发回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'queueItemsChange'：当session修改播放列表时，触发该事件。callback(items: Array<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>) => void是回调函数，items为变化的播放列表。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.on('queueItemsChange', (items: avSession.AVQueueItem[]) => {
  console.info(`OnQueueItemsChange, items length is ${items.length}`);
});
```

#### off('queueItemsChange')10+

off(type: 'queueItemsChange', callback?: (items: Array<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>) => void): void

取消播放列表变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'queueItemsChange'。callback(items: Array<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>) => void否

回调函数，参数items是变化的播放列表。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('queueItemsChange');
```

#### on('queueTitleChange')10+

on(type: 'queueTitleChange', callback: (title: string) => void): void

媒体控制器设置会话自定义播放列表的名称变化的监听器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'queueTitleChange'：当session修改播放列表名称时，触发该事件。callback(title: string) => void是回调函数，title为变化的播放列表名称。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.on('queueTitleChange', (title: string) => {
  console.info(`queueTitleChange, title is ${title}`);
});
```

#### off('queueTitleChange')10+

off(type: 'queueTitleChange', callback?: (title: string) => void): void

取消播放列表名称变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'queueTitleChange'。callback(title: string) => void否

回调函数，参数items是变化的播放列表名称。

该参数为可选参数，若不填写该参数，则认为取消所有相关会话的事件监听。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('queueTitleChange');
```

#### on('extrasChange')10+

on(type: 'extrasChange', callback: (extras: Record<string, Object>) => void): void

媒体控制器设置自定义媒体数据包事件变化的监听器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持事件'extrasChange'：当媒体提供方设置自定义媒体数据包时，触发该事件。callback(extras: Record<string, Object>) => void是

回调函数，extras为媒体提供方新设置的自定义媒体数据包，该自定义媒体数据包与dispatchSessionEvent方法设置的数据包完全一致。

API version 20开始发生兼容变更，在API version 19及之前的版本callback的参数类型为：(extras: {[key: string]: Object}) => void。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).on('extrasChange', (extras) => {
    console.info(`Caught extrasChange event,the new extra is: ${JSON.stringify(extras)}`);
  });
}
```

#### off('extrasChange')10+

off(type: 'extrasChange', callback?: (extras: Record<string, Object>) => void): void

取消自定义媒体数据包变化事件监听。指定callback，可取消对应监听；未指定callback，取消所有事件监听。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明typestring是取消对应的监听事件，支持事件'extrasChange'。callback(extras: Record<string, Object>) => void否

注册监听事件时的回调函数。

该参数为可选参数，若不填写该参数，则认为取消会话所有与此事件相关的监听。

API version 20开始发生兼容变更，在API version 19及之前的版本callback的参数类型为：(extras: {[key: string]: Object}) => void。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('extrasChange');
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

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { avSession } from '@kit.AVSessionKit';

let tag: string = "createNewSession";
let sessionId: string = "";
let controller:avSession.AVSessionController | undefined = undefined;
avSession.createAVSession(context, tag, "audio").then(async (data:avSession.AVSession)=> {
  currentAVSession = data;
  sessionId = currentAVSession.sessionId;
  controller = await currentAVSession.getController();
  console.info(`CreateAVSession : SUCCESS :sessionId = ${sessionId}`);
}).catch((err: BusinessError) => {
  console.error(`CreateAVSession BusinessError:code: ${err.code}, message: ${err.message}`)
});
if (controller !== undefined) {
  (controller as avSession.AVSessionController).on('customDataChange', (callback) => {
    console.info(`Caught customDataChange event,the new callback is: ${JSON.stringify(callback)}`);
  });
}
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

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
avsessionController.off('customDataChange');
```

#### getAVPlaybackStateSync10+

getAVPlaybackStateSync(): AVPlaybackState;

使用同步方法获取当前会话的播放状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明[AVPlaybackState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avplaybackstate10)当前会话的播放状态。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let playbackState: avSession.AVPlaybackState = avsessionController.getAVPlaybackStateSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getAVPlaybackStateSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

#### getAVMetadataSync10+

getAVMetadataSync(): AVMetadata

使用同步方法获取会话元数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明[AVMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avmetadata10)会话元数据。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let metaData: avSession.AVMetadata = avsessionController.getAVMetadataSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getAVMetadataSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

#### getAVCallState11+

getAVCallState(): Promise<AVCallState>

获取通话状态数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<[AVCallState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcallstate11)>Promise对象，返回通话状态。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVCallState().then((callstate: avSession.AVCallState) => {
  console.info(`getAVCallState : SUCCESS : state : ${callstate.state}`);
}).catch((err: BusinessError) => {
  console.error(`getAVCallState BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getAVCallState11+

getAVCallState(callback: AsyncCallback<AVCallState>): void

获取通话状态数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[AVCallState](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avcallstate11)>是回调函数，返回通话状态。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getAVCallState((err: BusinessError, callstate: avSession.AVCallState) => {
  if (err) {
    console.error(`getAVCallState BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`getAVCallState : SUCCESS : state : ${callstate.state}`);
  }
});
```

#### getCallMetadata11+

getCallMetadata(): Promise<CallMetadata>

获取通话会话的元数据。结果通过Promise异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Promise<[CallMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__callmetadata11)>Promise对象，返回会话元数据。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getCallMetadata().then((calldata: avSession.CallMetadata) => {
  console.info(`getCallMetadata : SUCCESS : name : ${calldata.name}`);
}).catch((err: BusinessError) => {
  console.error(`getCallMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
});
```

#### getCallMetadata11+

getCallMetadata(callback: AsyncCallback<CallMetadata>): void

获取通话会话的元数据。结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[CallMetadata](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__callmetadata11)>是回调函数，返回会话元数据。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

avsessionController.getCallMetadata((err: BusinessError, calldata: avSession.CallMetadata) => {
  if (err) {
    console.error(`getCallMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`getCallMetadata : SUCCESS : name : ${calldata.name}`);
  }
});
```

#### getAVQueueTitleSync10+

getAVQueueTitleSync(): string

使用同步方法获取当前会话播放列表的名称。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明string当前会话播放列表名称。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentQueueTitle: string = avsessionController.getAVQueueTitleSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getAVQueueTitleSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

#### getAVQueueItemsSync10+

getAVQueueItemsSync(): Array<AVQueueItem>

使用同步方法获取当前会话播放列表相关信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Array<[AVQueueItem](Interfaces (其他).md#ZH-CN_TOPIC_0000002529285755__avqueueitem10)>当前会话播放列表队列。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentQueueItems: Array<avSession.AVQueueItem> = avsessionController.getAVQueueItemsSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getAVQueueItemsSync error, error code: ${error.code}, error message: ${error.message}`);
}
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

错误码ID错误信息6600101Session service exception.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let currentOutputDevice: avSession.OutputDeviceInfo = avsessionController.getOutputDeviceSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getOutputDeviceSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

#### isActiveSync10+

isActiveSync(): boolean

使用同步方法判断会话是否被激活。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明boolean会话是否为激活状态，true表示被激活，false表示禁用。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isActive: boolean = avsessionController.isActiveSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`isActiveSync error, error code: ${error.code}, error message: ${error.message}`);
}
```

#### getValidCommandsSync10+

getValidCommandsSync(): Array<AVControlCommandType>

使用同步方法获取会话支持的有效命令。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**返回值：**

类型说明Array<[AVControlCommandType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497605764__avcontrolcommandtype10)>会话支持的有效命令的集合。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息6600101Session service exception.6600102The session does not exist.6600103The session controller does not exist.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let validCommands: Array<avSession.AVControlCommandType> = avsessionController.getValidCommandsSync();
} catch (err) {
  let error = err as BusinessError;
  console.error(`getValidCommandsSync error, error code: ${error.code}, error message: ${error.message}`);
}
```