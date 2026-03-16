# @ohos.web.WebNativeMessagingExtensionContext (Web Native Messaging Extension Context)

WebNativeMessagingExtensionContext是Web原生消息扩展的上下文, 继承自ExtensionContext。它提供了与WebNativeMessagingExtension通信消息的交互能力。

本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
```

#### WebNativeMessagingExtensionContext

WebNativeMessagingExtensionContext是Web原生消息扩展的上下文，包含所需交互能力。

#### startAbility

startAbility(want: Want, options?: StartOptions): Promise<void>

使用Promise异步回调启动Ability。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是表示需要启动的Ability的信息。options[StartOptions](@ohos.app.ability.StartOptions (startAbility的可选参数).md)否启动选项。

**返回值:**

类型说明Promise<void>无返回结果的Promise对象。

**错误码:**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息201The application does not have permission to call the interface.16000001The specified ability does not exist.16000002Incorrect ability type.16000004Cannot start an invisible component.16000005The specified process does not have the permission.16000008The crowdtesting application expires.16000009An ability cannot be started or stopped in Wukong mode.16000010The call with the continuation and prepare continuation flag is forbidden.16000011The context does not exist.16000012The application is controlled.16000013The application is controlled by EDM.16000019No matching ability is found.16000050Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module.16000055Installation-free timed out.16000071App clone is not supported.16000072App clone or multi-instance is not supported.16000073The app clone index is invalid.16000076The app instance key is invalid.16000077The number of app instances reaches the limit.16000078The multi-instance is not supported.16000079The APP_INSTANCE_KEY cannot be specified.16000080Creating a new instance is not supported.

**示例:**

```ets
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';
import { Want } from '@kit.AbilityKit';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const abilityWant: Want = {
    bundleName: 'com.example.mybundle',
    abilityName: 'MainAbility'
    };
    try {
        const context = this.context; // 获取 WebNativeMessagingExtensionContext 实例
        context.startAbility(abilityWant);
        console.info('Ability started successfully');
    } catch (err) {
        console.error(`Failed to start ability. Code: ${err.code}, Message: ${err.message}`);
    }
  }
}
```

#### terminateSelf

terminateSelf(): Promise<void>

销毁当前Web原生消息扩展。该方法返回一个Promise对象用于异步处理。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**返回值:**

类型说明Promise<void>无返回结果的Promise对象。

**错误码:**

以下错误码详细介绍请参考[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息16000009An ability cannot be started or stopped in Wukong mode.16000011The context does not exist.16000050Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module.

**示例:**

```ets
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    try {
        const context = this.context; // 获取 WebNativeMessagingExtensionContext 实例
        context.terminateSelf();
        console.info('Extension terminated successfully');
    } catch (err) {
        console.error(`Failed to terminate extension. Code: ${err.code}, Message: ${err.message}`);
    }
  }
}
```

#### stopNativeConnection

stopNativeConnection(connectionId: number): Promise<void>

停止指定的本地连接。使用Promise进行异步回调。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

参数名类型必填说明connectionIdnumber是要停止的连接ID。

**返回值:**

类型说明Promise<void>无返回结果的Promise对象。

**错误码:**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息201The application does not have permission to call the interface.16000011The context does not exist.16000050Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module.

**示例:**

```ets
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    const CONNECTION_ID = 12345; // 实际的连接 ID
    try {
        const context = this.context;// 获取 WebNativeMessagingExtensionContext 实例
        context.stopNativeConnection(CONNECTION_ID);
        console.info('Native connection stopped successfully');
    } catch (err) {
        console.error(`Failed to stop native connection. Code: ${err.code}, Message: ${err.message}`);
    }
  }
}
```