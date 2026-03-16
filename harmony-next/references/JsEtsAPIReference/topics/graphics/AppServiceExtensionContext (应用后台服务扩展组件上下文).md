# AppServiceExtensionContext (应用后台服务扩展组件上下文)

AppServiceExtensionContext模块是[AppServiceExtensionAbility](../../modules/ohos/@ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件).md)的上下文环境，继承自[ExtensionContext](ExtensionContext.md)。

AppServiceExtensionContext提供了连接、断开ServiceExtensionAbility（系统应用后台服务扩展组件）的能力，以及AppServiceExtensionAbility终止自身的能力。这里的ServiceExtensionAbility只能由系统应用开发，支持三方应用连接。

- 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
- 本模块接口仅可在Stage模型下使用。
- 本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

#### 导入模块

```ets
import { common } from '@kit.AbilityKit';
```

#### 使用说明

在使用AppServiceExtensionContext的功能前，需要通过AppServiceExtensionAbility子类实例获取。

**示例：**

```ets
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';

export default class AppServiceExtension extends AppServiceExtensionAbility {
  onCreate(want: Want) {
    let context = this.context; // 获取AppServiceExtensionContext
  }
}
```

#### AppServiceExtensionContext

#### startAbility

startAbility(want: Want, options?: StartOptions): Promise<void>

启动UIAbility。仅支持在主线程调用。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明want[Want](../../modules/ohos/@ohos.app.ability.Want (Want).md)是Want类型参数，传入需要启动的Ability的信息，如Ability名称、Bundle名称等。options[StartOptions](../../modules/ohos/@ohos.app.ability.StartOptions (startAbility的可选参数).md)否启动Ability所携带的参数。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息201The application does not have permission to call the interface.16000001The specified ability does not exist.16000002Incorrect ability type.16000004Cannot start an invisible component.16000005The specified process does not have the permission.16000008The crowdtesting application expires.16000009An ability cannot be started or stopped in Wukong mode.16000010The call with the continuation and prepare continuation flag is forbidden.16000011The context does not exist.16000012The application is controlled.16000013The application is controlled by EDM.16000019No matching ability is found.16000050Internal error.16000055Installation-free timed out.16000071App clone is not supported.16000072App clone or multi-instance is not supported.16000073The app clone index is invalid.16000076The app instance key is invalid.16000077The number of app instances reaches the limit.16000078The multi-instance is not supported.16000079The APP_INSTANCE_KEY cannot be specified.16000080Creating a new instance is not supported.

**示例：**

```ets
import { AppServiceExtensionAbility, Want, StartOptions } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAppServiceExtensionAbility extends AppServiceExtensionAbility {
  onCreate(want: Want) {
    let wantInfo: Want = {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    };
    let options: StartOptions = {
      displayId: 0
    };

    try {
      this.context.startAbility(wantInfo, options)
        .then(() => {
          // 执行正常业务
          console.info('startAbility succeed');
        })
        .catch((err: BusinessError) => {
          // 处理业务逻辑错误
          console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
        });
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`startAbility failed, code is ${code}, message is ${message}`);
    }
  }
}
```

#### connectServiceExtensionAbility

connectServiceExtensionAbility(want: Want, callback: ConnectOptions): number

将当前AppServiceExtensionAbility连接到一个ServiceExtensionAbility，通过返回的proxy与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。仅支持在主线程调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明want[Want](../../modules/ohos/@ohos.app.ability.Want (Want).md)是Want类型参数，传入需要连接的Ability的信息，如Ability名称，Bundle名称等。callback[ConnectOptions](../misc/ConnectOptions.md)是ConnectOptions类型的回调函数，返回服务连接成功、连接失败、断开的信息。

**返回值：**

类型说明number返回连接id，客户端可以通过[disconnectServiceExtensionAbility](#ZH-CN_TOPIC_0000002497604622__disconnectserviceextensionability)传入该连接id来断开连接。

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息16000001The specified ability does not exist.16000002Incorrect ability type.16000004Cannot start an invisible component.16000005The specified process does not have the permission.16000006Cross-user operations are not allowed.16000008The crowdtesting application expires.16000011The context does not exist.16000050Internal error.

**示例：**

```ets
import { AppServiceExtensionAbility, Want, common } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let commRemote: rpc.IRemoteObject | null = null; // 断开连接时需要释放
const TAG: string = '[AppServiceExtensionAbility]';

export default class AppServiceExtension extends AppServiceExtensionAbility {
  connection: number = 0;

  onCreate(localWant: Want) {
    let want: Want = {
      bundleName: 'com.example.myapp',
      abilityName: 'MyAbility'
    };
    let callback: common.ConnectOptions = {
      onConnect(elementName, remote) {
        commRemote = remote;
        hilog.info(0x0000, TAG, '----------- onConnect -----------');
      },
      onDisconnect(elementName) {
        hilog.info(0x0000, TAG, '----------- onDisconnect -----------');
      },
      onFailed(code) {
        hilog.error(0x0000, TAG, '----------- onFailed -----------');
      }
    };

    try {
      this.connection = this.context.connectServiceExtensionAbility(want, callback);
    } catch (paramError) {
      commRemote = null;
      // 处理入参错误异常
      hilog.error(0x0000, TAG, `error.code: ${(paramError as BusinessError).code}, error.message: ${(paramError as BusinessError).message}`);
    }
  }

  onDestroy(): void {
    this.context.disconnectServiceExtensionAbility(this.connection).then(() => {
      commRemote = null;
      // 执行正常业务
      hilog.info(0x0000, TAG, '----------- disconnectServiceExtensionAbility success -----------');
    })
      .catch((error: BusinessError) => {
        commRemote = null;
        // 处理业务逻辑错误
        hilog.error(0x0000, TAG, `disconnectServiceExtensionAbility failed, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }
}
```

#### disconnectServiceExtensionAbility

disconnectServiceExtensionAbility(connection: number): Promise<void>

将AppServiceExtensionAbility与已连接的ServiceExtensionAbility断开连接。仅支持在主线程调用。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明connectionnumber是在[connectServiceExtensionAbility](#ZH-CN_TOPIC_0000002497604622__connectserviceextensionability)中返回的连接id。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息16000011The context does not exist.16000050Internal error.

**示例：**

参见[connectServiceExtensionAbility](#ZH-CN_TOPIC_0000002497604622__connectserviceextensionability)。

#### terminateSelf

terminateSelf(): Promise<void>

销毁AppServiceExtensionAbility自身。仅支持在主线程调用。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息16000009An ability cannot be started or stopped in Wukong mode.16000011The context does not exist.16000050Internal error.

**示例：**

```ets
import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = '[AppServiceExtensionAbility]';

export default class AppServiceExtension extends AppServiceExtensionAbility {
  onCreate(want: Want) {
    this.context.terminateSelf().then(() => {
      // 执行正常业务
      hilog.info(0x0000, TAG, '----------- terminateSelf succeed -----------');
    }).catch((error: BusinessError) => {
      // 处理业务逻辑错误
      hilog.error(0x0000, TAG, `terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}`);
    });
  }
}
```