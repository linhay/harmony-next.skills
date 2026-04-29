# PushExtensionAbility（推送扩展Ability）

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

推送扩展Ability目前为预留能力，暂未开放使用。若您的应用有拉起应用的子进程，在子进程中自行处理业务的诉求，请参考[发送语音播报消息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-send-extend-noti#开发步骤)。

PushExtensionAbility为推送扩展Ability，提供获取场景化消息数据和生命周期销毁的回调。有如下约束：

-

PushExtensionAbility为独立子进程，轻量级，不允许唤醒主进程。

-

不允许调用通知API、卡片API、窗口API、弹窗API、实况窗API。

-

生命周期根据场景受控，默认小于10秒，超过10秒子进程生命周期结束。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

起始版本： 4.0.0(10)

**导入模块**

```ets
import { PushExtensionAbility } from '@kit.PushKit';
```

**属性**

模型约束： 属性仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该属性在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该属性在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该属性在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | PushExtensionContext | 否 | 否 | PushExtensionAbility的上下文环境，继承自ExtensionContext。 |

**onReceiveMessage**

onReceiveMessage(payload: pushCommon.PushPayload): void

应用先继承PushExtensionAbility后接收场景化消息的接口。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| payload | pushCommon.PushPayload | 是 | 场景化消息数据。 |

示例：

```ets
import { PushExtensionAbility, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 此处以TestExtAbility继承PushExtensionAbility为例
export default class TestExtAbility extends PushExtensionAbility {
  onReceiveMessage(payload: pushCommon.PushPayload): void {
    hilog.info(0x0000, 'testTag', 'TestExtAbility onReceiveMessage');
  }
```

**onDestroy**

onDestroy(): void

当PushExtensionAbility生命周期结束时，会执行该回调，建议在该方法中执行资源清理等操作。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

示例：

```ets
import { PushExtensionAbility } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 此处以TestExtAbility继承PushExtensionAbility为例
export default class TestExtAbility extends PushExtensionAbility {
  onDestroy(): void {
    hilog.info(0x0000, 'testTag', 'TestExtAbility onDestroy');
  }
```