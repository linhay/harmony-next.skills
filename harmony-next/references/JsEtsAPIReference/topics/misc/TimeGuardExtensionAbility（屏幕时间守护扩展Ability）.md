# TimeGuardExtensionAbility（屏幕时间守护扩展Ability）

TimeGuardExtensionAbility是屏幕时间守护扩展Ability，提供extension回调，支持开发者在策略管控生效和策略停止时执行特定逻辑，以及支持开发者用户授予应用权限和取消应用授权时执行特定逻辑。TimeGuardExtensionAbility继承自[ExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability)。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

**导入模块**

```ets
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
```

**属性**

模型约束： 属性仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | TimeGuardExtensionContext | 否 | 否 | TimeGuardExtensionContext上下文环境，继承自ExtensionContext。 |

**onStart**

onStart(strategyName: string): Promise<void>

应用所启动的策略管控生效时，执行该回调。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 时间管控策略名称。长度不超过64字符，仅支持字母、数字和下划线。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

示例：

```ets
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0;
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onStart(strategyName: string): Promise<void> {
    console.info('test --- onStart', strategyName, index++);
  }
```

**onStop**

onStop(strategyName: string): Promise<void>

应用所启动的策略管控效果结束时，执行该回调。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 时间管控策略名称。长度不超过64字符，仅支持字母、数字和下划线。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

示例：

```ets
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0;
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onStop(strategyName: string): Promise<void> {
    console.info('test --- onStop', strategyName, index++);
  }
```

**onUserAuthSwitchOn**

onUserAuthSwitchOn(): Promise<void>

当用户在“设置 > 健康使用设备 > 授权管理”中授予应用授权时，应用接收该回调。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

示例：

```ets
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0;
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onUserAuthSwitchOn(): Promise<void> {
    console.info('test --- onUserAuthSwitchOn', this.context, index++);
  }
```

**onUserAuthSwitchOff**

onUserAuthSwitchOff(): Promise<void>

当用户在“设置 > 健康使用设备 > 授权管理”中撤销应用授权时，应用接收该回调。使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

示例：

```ets
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0;
export default class EntryAbility extends TimeGuardExtensionAbility {
  async onUserAuthSwitchOff(): Promise<void> {
    console.info('test --- onUserAuthSwitchOff', this.context, index++);
  }
```