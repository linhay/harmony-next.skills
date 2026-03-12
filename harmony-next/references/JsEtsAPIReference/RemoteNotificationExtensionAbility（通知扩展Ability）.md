# RemoteNotificationExtensionAbility（通知扩展Ability）

RemoteNotificationExtensionAbility为通知扩展Ability，提供获取场景化消息数据和生命周期结束的回调。有如下约束：

- RemoteNotificationExtensionAbility为独立子进程，轻量级，不允许唤醒主进程。
- 不允许调用通知API、卡片API、窗口API、弹窗API、实况窗API。
- 生命周期根据场景受控，默认小于10秒，超过10秒子进程生命周期结束。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { RemoteNotificationExtensionAbility } from '@kit.PushKit';
```

#### 属性

**模型约束：**属性仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)及之后版本，该属性在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

名称

类型

只读

可选

说明

context

[RemoteNotificationExtensionContext](RemoteNotificationExtensionContext（通知扩展Context）.md)

否

否

RemoteNotificationExtensionAbility的上下文环境，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

#### onReceiveMessage

onReceiveMessage(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<pushCommon.RemoteNotificationContent>

应用继承RemoteNotificationExtensionAbility后接收通知扩展消息的接口，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

**参数：**

参数名

类型

必填

说明

remoteNotificationInfo

pushCommon.[RemoteNotificationInfo](pushCommon（推送服务公共信息）.md#section5154112615120)

是

通知扩展消息的数据。

**返回值：**

类型

说明

Promise<pushCommon.[RemoteNotificationContent](pushCommon（推送服务公共信息）.md#section155703491918)>

Promise对象，返回通知扩展消息的替换内容。

**示例****：**

```ets
import { RemoteNotificationExtensionAbility, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 此处以RemoteNotificationExtAbility继承RemoteNotificationExtensionAbility为例
export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
  async onReceiveMessage(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<pushCommon.RemoteNotificationContent> {
    hilog.info(0x0000, 'testTag', 'TestExtAbility onReceiveMessage');
    return {
      title: 'Default replace title.',
      text: 'Default replace text.',
      badgeNumber: 1,
      wantAgent: {
        abilityName: 'DemoAbility',
        parameters: {
          key: 'Default value'
        }
      }
    }
  }
}
```

#### onDestroy

onDestroy(): void

当RemoteNotificationExtensionAbility生命周期结束时，会执行该回调，建议在该方法中执行资源清理等操作。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Push.PushService

**设备行为差异**：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。

**起始版本：**4.1.0(11)

**示例****：**

```ets
import { RemoteNotificationExtensionAbility } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 此处以RemoteNotificationExtAbility继承RemoteNotificationExtensionAbility为例
export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
  onDestroy(): void {
    hilog.info(0x0000, 'testTag', 'RemoteNotificationExtAbility onDestroy.');
  }
}
```