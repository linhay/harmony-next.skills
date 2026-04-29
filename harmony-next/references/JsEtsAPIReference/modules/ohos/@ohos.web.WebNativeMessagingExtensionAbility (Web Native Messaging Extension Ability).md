# @ohos.web.WebNativeMessagingExtensionAbility (Web Native Messaging Extension Ability)

WebNativeMessagingExtensionAbility为开发者提供Web原生消息通信的能力，继承自ExtensionAbility。

本模块首批接口从API version 21开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { WebNativeMessagingExtensionAbility } from '@kit.ArkWeb';
```

#### WebNativeMessagingExtensionAbility

为开发者提供Web原生消息通信能力，继承自ExtensionAbility。

#### 属性

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | WebNativeMessagingExtensionContext | 否 | 否 | Web原生信息通信上下文。 |

#### onConnectNative

onConnectNative(info: ConnectionInfo): void

Web原生信息连接建立时回调此方法。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | ConnectionInfo | 是 | 连接信息对象。 |

**示例:**

```ets
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onConnectNative(info: ConnectionInfo): void {
    console.info('Web Native connection established!');
    console.info(`Connection ID: ${info.connectionId}`);
    console.info(`Caller bundle: ${info.bundleName}`);
    // 在此处处理连接建立后的业务逻辑
  }
```

#### onDisconnectNative

onDisconnectNative(info: ConnectionInfo): void

Web原生信息连接断开时回调此方法。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | ConnectionInfo | 是 | 连接信息对象。 |

**示例:**

```ets
import { WebNativeMessagingExtensionAbility, ConnectionInfo } from '@kit.ArkWeb';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onDisconnectNative(info: ConnectionInfo): void {
    console.info('Web Native connection closed!');
    console.info(`Connection ID: ${info.connectionId}`);
    // 在此处处理连接断开后的清理工作
}
```

#### onDestroy

onDestroy(): void

WebNativeMessagingExtensionAbility销毁时回调。

**系统能力:** SystemCapability.Web.Webview.Core

**模型约束:** 此接口仅可在Stage模型下使用。

**示例:**

```ets
import { WebNativeMessagingExtensionAbility } from '@kit.ArkWeb';

export class MyWebNativeMessagingExtension extends WebNativeMessagingExtensionAbility {
  onDestroy(): void {
    console.info('WebNativeMessagingExtensionAbility is about to be destroyed!');
    // 在此处释放资源或者执行清理操作
  }
```

#### ConnectionInfo

Web原生消息连接的信息对象。

**系统能力:** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| connectionId | number | 否 | 否 | 连接的唯一标识符。 |
| bundleName | string | 否 | 否 | 调用方的应用包名。 |
| extensionOrigin | string | 否 | 否 | 调用方扩展的原始URL。 |
| fdRead | number | 否 | 否 | 用于读取数据的管道文件描述符。 |
| fdWrite | number | 否 | 否 | 用于写入数据的管道文件描述符。 |