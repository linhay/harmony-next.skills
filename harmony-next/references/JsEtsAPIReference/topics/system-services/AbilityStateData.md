# AbilityStateData

AbilityStateData是Ability状态信息的数据结构。使用[on](../../modules/ohos/@ohos.app.ability.appManager (应用管理).md#ZH-CN_TOPIC_0000002497444628__appmanageronapplicationstate14)注册生命周期变化监听后，可以通过[ApplicationStateObserver](ApplicationStateObserver.md)的onAbilityStateChanged回调的入参获取该数据结构。

本模块首批接口从API version 14开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { appManager } from '@kit.AbilityKit';
```

#### AbilityStateData

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

名称类型只读可选说明pidnumber否否进程ID。bundleNamestring否否应用Bundle名称。abilityNamestring否否Ability名称。uidnumber否否所属应用程序的UID。statenumber否否

Ability状态。

- [Stage模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#stage模型)：[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)的状态参见[UIAbility状态](#ZH-CN_TOPIC_0000002497444642__uiability状态)；[ExtensionAbility](../../modules/ohos/@ohos.app.ability.ExtensionAbility (扩展能力基类).md)的状态参见[ExtensionAbility状态](#ZH-CN_TOPIC_0000002497444642__extensionability状态)；[UIExtensionAbility](../../modules/ohos/@ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件).md)的状态参见[UIExtensionAbility状态](#ZH-CN_TOPIC_0000002497444642__uiextensionability状态)。

- [FA模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#fa模型)：参见[Ability状态](#ZH-CN_TOPIC_0000002497444642__ability状态)。

moduleNamestring否否Ability所属的模块名称。abilityTypenumber否否[Ability类型](#ZH-CN_TOPIC_0000002497444642__ability类型)：[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)或[ExtensionAbility](../../modules/ohos/@ohos.app.ability.ExtensionAbility (扩展能力基类).md)等。isAtomicServiceboolean否否

判断Ability所属应用是否为元服务。

true: 是元服务。

false: 不是元服务。

appCloneIndexnumber否是应用包的[分身](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-clone)索引标识。

#### UIAbility状态

值状态说明0ABILITY_STATE_CREATEUIAbility正在创建中。1ABILITY_STATE_READYUIAbility已创建完成。2ABILITY_STATE_FOREGROUNDUIAbility处于前台。3ABILITY_STATE_FOCUSUIAbility已获得焦点。4ABILITY_STATE_BACKGROUNDUIAbility处于后台。5ABILITY_STATE_TERMINATEDUIAbility已经销毁。

#### ExtensionAbility状态

值状态说明0EXTENSION_STATE_CREATEExtensionAbility正在创建中。1EXTENSION_STATE_READYExtensionAbility已创建完成。2EXTENSION_STATE_CONNECTEDExtensionAbility已与客户端建立连接。3EXTENSION_STATE_DISCONNECTEDExtensionAbility与客户端断开连接。4EXTENSION_STATE_TERMINATEDExtensionAbility已经销毁。

#### UIExtensionAbility状态

值状态说明0ABILITY_STATE_CREATEUIExtensionAbility正在创建中。1ABILITY_STATE_READYUIExtensionAbility已创建完成。2ABILITY_STATE_FOREGROUNDUIExtensionAbility处于前台。4ABILITY_STATE_BACKGROUNDUIExtensionAbility处于后台。5ABILITY_STATE_TERMINATEDUIExtensionAbility已经销毁。

#### Ability状态

值状态说明0ABILITY_STATE_CREATEAbility正在创建中。1ABILITY_STATE_READYAbility已创建完成。2ABILITY_STATE_FOREGROUNDAbility处于前台。3ABILITY_STATE_FOCUSAbility已获得焦点。4ABILITY_STATE_BACKGROUNDAbility处于后台。5ABILITY_STATE_TERMINATEDAbility已经销毁。7ABILITY_STATE_CONNECTED后台服务已被客户端连接。8ABILITY_STATE_DISCONNECTED后台服务与客户端断开连接。

#### Ability类型

值状态说明0UNKNOWN未知类型。（系统错误）1PAGEUI界面类型的Ability，即[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)。2SERVICE后台服务类型的Ability。（FA模型）3DATA数据类型的Ability。（FA模型）4FORM卡片类型的Ability。（FA模型）5EXTENSION扩展类型的Ability。（Stage模型）