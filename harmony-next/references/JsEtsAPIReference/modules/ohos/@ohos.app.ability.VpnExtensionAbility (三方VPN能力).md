# @ohos.app.ability.VpnExtensionAbility (三方VPN能力)

VpnExtensionAbility模块提供三方VPN相关能力，提供三方VPN创建、销毁等生命周期回调。

-

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { VpnExtensionAbility } from '@kit.NetworkKit';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明context[VpnExtensionContext](../../topics/graphics/VpnExtensionContext.md)否否VpnExtension的上下文环境，继承自ExtensionContext。

#### VpnExtensionAbility.onCreate

onCreate(want: Want): void

在启动三方VPN进行初始化时回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数**：

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是指示要启动的信息。

**示例：**

```ets
import { VpnExtensionAbility } from '@kit.NetworkKit';
import { Want } from '@kit.AbilityKit';

class MyVpnExtAbility extends VpnExtensionAbility {
    onCreate(want: Want) {
       console.info('MyVpnExtAbility onCreate');
    }
}
```

#### VpnExtensionAbility.onDestroy

onDestroy(): void

VpnExtensionAbility生命周期回调，在销毁时回调，执行资源清理等操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**示例：**

```ets
import { VpnExtensionAbility } from '@kit.NetworkKit';

class MyVpnExtAbility extends VpnExtensionAbility {
    onDestroy() {
       console.info('MyVpnExtAbility onDestroy');
    }
}
```