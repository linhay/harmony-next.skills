# VpnExtensionContext

VpnExtensionContext是VpnExtensionAbility的上下文环境，继承自[ExtensionContext](ExtensionContext.md)。

VpnExtensionContext可直接作为VpnExtension的上下文环境，提供允许访问特定于VpnExtensionAbility的资源的能力。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { VpnExtensionAbility } from '@kit.NetworkKit';
```

#### 使用说明

通过VpnExtensionAbility子类实例来获取。

```ets
import { VpnExtensionAbility, vpnExtension } from '@kit.NetworkKit';
import { Want } from '@kit.AbilityKit';

export default class MyVpnExtAbility extends VpnExtensionAbility {
  private vpnServerIp: string = 'xxx.xxx.x.x';
  private tunIp: string = 'x.x.x.x';
  private blockedAppName: string = 'xxxx';

  onCreate(want: Want) {
    let VpnConnection: vpnExtension.VpnConnection = vpnExtension.createVpnConnection(this.context);
    console.info("vpn createVpnConnection: " + JSON.stringify(VpnConnection));
  }
}
```

#### VpnExtensionAbility

三方VPN拓展能力。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

名称类型只读可选说明context[VpnExtensionContext](VpnExtensionContext.md)否否指定context。

#### onCreate

onCreate(want: Want): void

拓展VPN启动初始化的时候进行回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

参数名类型必填说明want[Want](../../modules/ohos/@ohos.app.ability.Want (Want).md)是指示要启动的信息。

#### onDestroy

onDestroy(): void

拓展VPN销毁之前进行回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在Stage模型下使用。