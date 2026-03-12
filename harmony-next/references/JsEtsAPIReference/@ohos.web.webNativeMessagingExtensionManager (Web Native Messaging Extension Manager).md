# @ohos.web.webNativeMessagingExtensionManager (Web Native Messaging Extension Manager)

webNativeMessagingExtensionManager模块提供基于Web标准的消息扩展管理能力。

本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
```

#### ConnectionNativeInfo

表示Web原生消息连接的连接信息。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

名称类型只读可选说明connectionIdnumber否否连接ID。bundleNamestring否否Web原生消息扩展应用的包名。extensionOriginstring否否浏览器扩展的源URL。extensionPidnumber否否Web原生消息扩展的进程ID。

#### NmErrorCode

Native Messaging的错误列表。

**系统能力**：SystemCapability.Web.Webview.Core

名称值说明PERMISSION_DENY17100203Permission denied due to missing ohos.permission.WEB_NATIVE_MESSAGING.WANT_CONTENT_ERROR17100202The want content is invalid.INNER_ERROR17100201Inner error for native messaging.Error code:

#### WebExtensionConnectionCallback

#### onConnect

onConnect(connection: ConnectionNativeInfo): void

建立连接时的回调函数。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

参数名类型必填说明connection[ConnectionNativeInfo](#ZH-CN_TOPIC_0000002497605204__connectionnativeinfo)是连接信息。

**示例:**

```ets
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    try {
        let context: common.UIAbilityContext = this.context; // 获取UIAbilityContext
        let want:Want = {
          bundleName: 'com.example.app',
          abilityName: 'MyWebNativeMessageExtAbility',
          parameters: {
            'ohos.arkweb.messageReadPipe': { 'type': 'FD', 'value': 333 }, //假设此处为合法pipefd
            'ohos.arkweb.messageWritePipe': { 'type': 'FD', 'value': 444 }, //假设此处为合法pipefd
            'ohos.arkweb.extensionOrigin': 'chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/' //此处需要插件URI
          },
        };

        let callback: webNativeMessagingExtensionManager.WebExtensionConnectionCallback = {
            onConnect(connection) {
                console.info('onConnect, connectionId:' + connection.connectionId);
            },
            onDisconnect(connection) {
                console.info('onDisconnect');
            },
            onFailed(code, errMsg) {
                console.info(`onFailed, code:${code} errMsg:${errMsg}`);
            }
        };

        let connectionId = webNativeMessagingExtensionManager.connectNative(context, want, callback);
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`connectNative failed, code is ${code}, message is ${message}`);
    }
  }
}
```

#### onDisconnect

onDisconnect(connection: ConnectionNativeInfo): void

断开连接时的回调函数。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

参数名类型必填说明connection[ConnectionNativeInfo](#ZH-CN_TOPIC_0000002497605204__connectionnativeinfo)是连接信息。

**示例:**

```ets
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    try {
        let context: common.UIAbilityContext = this.context; // 获取UIAbilityContext
        let want:Want = {
          bundleName: 'com.example.app',
          abilityName: 'MyWebNativeMessageExtAbility',
          parameters: {
            'ohos.arkweb.messageReadPipe': { 'type': 'FD', 'value': 333 }, //假设此处为合法pipefd
            'ohos.arkweb.messageWritePipe': { 'type': 'FD', 'value': 444 }, //假设此处为合法pipefd
            'ohos.arkweb.extensionOrigin': 'chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/' //此处需要插件URI
          },
        };

        let callback: webNativeMessagingExtensionManager.WebExtensionConnectionCallback = {
            onConnect(connection) {
                console.info('onConnect, connectionId:' + connection.connectionId);
            },
            onDisconnect(connection) {
                console.info('onDisconnect');
            },
            onFailed(code, errMsg) {
                console.info(`onFailed, code:${code} errMsg:${errMsg}`);
            }
        };

        let connectionId = webNativeMessagingExtensionManager.connectNative(context, want, callback);
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`connectNative failed, code is ${code}, message is ${message}`);
    }
  }
}
```

#### onFailed

onFailed(code: NmErrorCode, errMsg: string): void

连接失败时的回调函数。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

参数名类型必填说明code[NmErrorCode](#ZH-CN_TOPIC_0000002497605204__nmerrorcode)是错误码。errMsgstring是错误码对应信息。

**示例:**

```ets
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    try {
        let context: common.UIAbilityContext = this.context; // 获取UIAbilityContext
        let want:Want = {
          bundleName: 'com.example.app',
          abilityName: 'MyWebNativeMessageExtAbility',
          parameters: {
            'ohos.arkweb.messageReadPipe': { 'type': 'FD', 'value': 333 }, //假设此处为合法pipefd
            'ohos.arkweb.messageWritePipe': { 'type': 'FD', 'value': 444 }, //假设此处为合法pipefd
            'ohos.arkweb.extensionOrigin': 'chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/' //此处需要插件URI
          },
        };

        let callback: webNativeMessagingExtensionManager.WebExtensionConnectionCallback = {
            onConnect(connection) {
                console.info('onConnect, connectionId:' + connection.connectionId);
            },
            onDisconnect(connection) {
                console.info('onDisconnect');
            },
            onFailed(code, errMsg) {
                console.info(`onFailed, code:${code} errMsg:${errMsg}`);
            }
        };

        let connectionId = webNativeMessagingExtensionManager.connectNative(context, want, callback);
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`connectNative failed, code is ${code}, message is ${message}`);
    }
  }
}
```

#### webNativeMessagingExtensionManager.connectNative

connectNative(context: UIAbilityContext, want: Want, callback: WebExtensionConnectionCallback): number

将当前Ability连接到指定的Web原生消息扩展Ability。

**需要权限**：ohos.permission.WEB_NATIVE_MESSAGING

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

参数名类型必填说明context[UIAbilityContext](UIAbilityContext.md)是Web原生消息扩展的上下文。want[Want](@ohos.app.ability.Want (Want).md)是启动Ability的want信息。callback[WebExtensionConnectionCallback](#ZH-CN_TOPIC_0000002497605204__webextensionconnectioncallback)是WebExtensionConnection状态的回调对象。

**返回值:**

类型说明number连接标识ID。

**错误码:**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)。

错误码ID错误信息801Capability not supported.

**示例:**

```ets
import { UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    try {
        let context: common.UIAbilityContext = this.context; // 获取UIAbilityContext
        let want:Want = {
          bundleName: 'com.example.app',
          abilityName: 'MyWebNativeMessageExtAbility',
          parameters: {
            'ohos.arkweb.messageReadPipe': { 'type': 'FD', 'value': 333 }, //假设此处为合法pipefd
            'ohos.arkweb.messageWritePipe': { 'type': 'FD', 'value': 444 }, //假设此处为合法pipefd
            'ohos.arkweb.extensionOrigin': 'chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/' //此处需要插件URI
          },
        };

        let callback: webNativeMessagingExtensionManager.WebExtensionConnectionCallback = {
            onConnect(connection) {
                console.info('onConnect, connectionId:' + connection.connectionId);
            },
            onDisconnect(connection) {
                console.info('onDisconnect');
            },
            onFailed(code, errMsg) {
                console.info(`onFailed, code:${code} errMsg:${errMsg}`);
            }
        };

        let connectionId = webNativeMessagingExtensionManager.connectNative(context, want, callback);
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`connectNative failed, code is ${code}, message is ${message}`);
    }
  }
}
```

#### webNativeMessagingExtensionManager.disconnectNative

disconnectNative(connectionId: number): Promise<void>

断开指定Web原生消息扩展连接。

**需要权限**：ohos.permission.WEB_NATIVE_MESSAGING

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

参数名类型必填说明connectionIdnumber是连接的标识ID。

**返回值:**

类型说明Promise<void>无返回结果的Promise对象。

**错误码:**

以下错误码详细介绍请参考[通用错误码](通用错误码.md)和[元能力子系统错误码](元能力子系统错误码.md)。

错误码ID错误信息201Permission verification failed.801Capability not supported.16000011The context does not exist.16000050Internal error. Possible causes: 1. Failed to connect to the system service; 2. The system service failed to communicate with dependency module.

**示例:**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { webNativeMessagingExtensionManager } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  async disconnect() {
    try {
        let connectionId = 1;
        // 假设之前已连接并获得connectionId
        await webNativeMessagingExtensionManager.disconnectNative(connectionId).then(() => {
            console.info('disconnectNative success');
        })
    } catch (err) {
      // 处理入参错误异常
      let code = (err as BusinessError).code;
      let message = (err as BusinessError).message;
      console.error(`disconnectNative failed, code is ${code}, message is ${message}`);
    }
  }
  onForeground() {
    this.disconnect();
  }
}
```