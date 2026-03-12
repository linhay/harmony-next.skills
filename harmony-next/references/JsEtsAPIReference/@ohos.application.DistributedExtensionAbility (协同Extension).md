# @ohos.application.DistributedExtensionAbility (协同Extension)

DistributedExtensionAbility模块提供分布式相关扩展能力，提供分布式创建、销毁、连接的生命周期回调。

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { DistributedExtensionAbility} from '@kit.DistributedServiceKit';
```

#### DistributedExtensionAbility

#### 属性

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称类型只读可选说明contextDistributedExtensionContext否否DistributedExtension的上下文环境，继承自ExtensionContext。

#### onCreate

onCreate(want: Want): void

Extension生命周期回调，在创建时回调，执行初始化业务逻辑操作。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明want[Want](@ohos.app.ability.Want (Want).md)是当前Extension相关的Want类型信息，包括ability名称、bundle名称等。

**示例：**

```ets
import { Want } from '@kit.AbilityKit';
import { DistributedExtensionAbility } from '@kit.DistributedServiceKit';

export default class DistributedExtension extends DistributedExtensionAbility {
  onCreate(want: Want) {
    console.info(`DistributedExtension Create ok`);
    console.info(`DistributedExtension on Create want: ${JSON.stringify(want)}`);
    console.info(`DistributedExtension Create end`);
  }
}
```

#### onCollaborate

onCollaborate(wantParam: Record <string, Object>) : AbilityConstant.CollaborateResult

多设备协作场景下返回协作结果的回调。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明wantParamRecord <string, Object>是want相关参数，仅支持key值取"ohos.extra.param.key.supportCollaborateIndex"。通过该key值可以获取到调用方传输的数据并进行相应的处理。

**返回值：**

类型说明[AbilityConstant.CollaborateResult](@ohos.app.ability.AbilityConstant (Ability相关常量).md#ZH-CN_TOPIC_0000002497604576__collaborateresult18)协同方应用是否接受协同。

**示例**

```ets
import { abilityConnectionManager, DistributedExtensionAbility } from '@kit.DistributedServiceKit';
import { AbilityConstant } from '@kit.AbilityKit';

export default class DistributedExtension extends DistributedExtensionAbility {
  onCollaborate(wantParam: Record<string, Object>) {
    console.info(`DistributedExtension onCollabRequest Accept to the result of Ability collaborate`);
    let sessionId = -1;
    const collaborationValues = wantParam["CollaborationValues"] as abilityConnectionManager.CollaborationValues;
    if (collaborationValues == undefined) {
      return sessionId;
    }
    console.info(`onCollab, collaborationValues: ${JSON.stringify(collaborationValues)}`);
    return AbilityConstant.CollaborateResult.ACCEPT;
  }
}
```

#### onDestroy

onDestroy(): void

Extension生命周期回调，在销毁时回调，执行资源清理等操作。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**示例：**

```ets
import { DistributedExtensionAbility } from '@kit.DistributedServiceKit';

export default class DistributedExtension extends DistributedExtensionAbility {
  onDestroy() {
    console.info('DistributedExtension onDestroy ok');
  }
}
```