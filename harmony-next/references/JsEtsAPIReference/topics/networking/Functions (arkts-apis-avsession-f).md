[]()[]()

# Functions

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { avSession } from '@kit.AVSessionKit';
```

[]()[]()

#### avSession.createAVSession10+

createAVSession(context: Context, tag: string, type: AVSessionType): Promise<AVSession>

创建会话对象，一个应用进程仅允许存在一个会话，重复创建会失败，结果通过Promise异步回调方式返回。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明context[Context](../graphics/Context (FA模型的上下文基类).md)是需要使用UIAbilityContext，用于系统获取应用组件的相关信息。tagstring是会话的自定义名称。type[AVSessionType](Types (arkts-apis-avsession-t).md#ZH-CN_TOPIC_0000002497605764__avsessiontype10)是会话类型。

**返回值：**

类型说明Promise<[AVSession](../../types/interfaces/Interface (AVSession).md)>Promise对象。回调返回会话实例对象，可用于获取会话ID，以及设置元数据、播放状态，发送按键事件等操作。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.

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
            let currentAVSession: avSession.AVSession;
            let tag = "createNewSession";
            let context: Context = this.getUIContext().getHostContext() as Context;
            let sessionId: string;  // 供后续函数入参使用。

            avSession.createAVSession(context, tag, "audio").then(async (data: avSession.AVSession) => {
            currentAVSession = data;
            sessionId = currentAVSession.sessionId;
            console.info(`CreateAVSession : SUCCESS : sessionId = ${sessionId}`);
            }).catch((err: BusinessError) => {
            console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```

[]()[]()

#### avSession.createAVSession10+

createAVSession(context: Context, tag: string, type: AVSessionType, callback: AsyncCallback<AVSession>): void

创建会话对象，一个应用程序仅允许存在一个会话，重复创建会失败，结果通过callback异步回调方式返回。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明context[Context](../graphics/Context (FA模型的上下文基类).md)是需要使用UIAbilityContext，用于系统获取应用组件的相关信息。tagstring是会话的自定义名称。type[AVSessionType](Types (arkts-apis-avsession-t).md#ZH-CN_TOPIC_0000002497605764__avsessiontype10)是会话类型。callbackAsyncCallback<[AVSession](../../types/interfaces/Interface (AVSession).md)>是回调函数。回调返回会话实例对象，可用于获取会话ID，以及设置元数据、播放状态，发送按键事件等操作。

**错误码：**

以下错误码的详细介绍请参见[媒体会话管理错误码](../../errors/媒体会话管理错误码.md)。

错误码ID错误信息401parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.6600101Session service exception.

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
          let currentAVSession: avSession.AVSession;
          let tag = "createNewSession";
          let context: Context = this.getUIContext().getHostContext() as Context;
          let sessionId: string;  // 供后续函数入参使用。

          avSession.createAVSession(context, tag, "audio", async (err: BusinessError, data: avSession.AVSession) => {
            if (err) {
              console.error(`CreateAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
            } else {
              currentAVSession = data;
              sessionId = currentAVSession.sessionId;
              console.info(`CreateAVSession : SUCCESS : sessionId = ${sessionId}`);
            }
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

[]()[]()

#### avSession.getAVSession22+

getAVSession(context: Context): Promise<AVSession>

获取会话对象。使用Promise异步回调。

该接口可将当前进程已创建过的会话对象返回，如果没有创建过会话对象，当前接口会调用失败抛出异常。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**参数：**

参数名类型必填说明context[Context](../graphics/Context (FA模型的上下文基类).md)是需要使用UIAbilityContext，用于系统获取应用组件的相关信息。

**返回值：**

类型说明Promise<[AVSession](../../types/interfaces/Interface (AVSession).md)>Promise对象。回调返回会话实例对象，可用于获取会话ID、设置元数据及播放状态、发送按键事件等操作。

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
            let currentAVSession: avSession.AVSession;
            let context: Context = this.getUIContext().getHostContext() as Context;
            let sessionId: string;  // 供后续函数入参使用。
            let sessionTag: string;

            avSession.getAVSession(context).then(async (data: avSession.AVSession) => {
              currentAVSession = data;
              sessionId = currentAVSession.sessionId;
              sessionTag = currentAVSession.sessionTag;
              console.info(`GetAVSession : SUCCESS : sessionId=${sessionId}, sessionTag=${sessionTag}`);
            }).catch((err: BusinessError) => {
              console.error(`GetAVSession BusinessError: code: ${err.code}, message: ${err.message}`);
            });
          })
      }
    .width('100%')
    .height('100%')
  }
}
```