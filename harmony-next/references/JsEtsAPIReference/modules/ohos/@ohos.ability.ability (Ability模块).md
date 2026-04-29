# @ohos.ability.ability (Ability模块)

Ability模块将二级模块API组织在一起方便开发者进行导出。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { ability } from '@kit.AbilityKit';
```

#### DataAbilityHelper

type DataAbilityHelper = [_DataAbilityHelper](../../topics/misc/DataAbilityHelper.md)

DataAbilityHelper二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_DataAbilityHelper](../../topics/misc/DataAbilityHelper.md) | DataAbilityHelper二级模块。 |

#### PacMap

type PacMap = [_PacMap](../../topics/misc/DataAbilityHelper.md#ZH-CN_TOPIC_0000002529284609__pacmap)

PacMap二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 类型 | 说明 |
| --- | --- |
| [_PacMap](../../topics/misc/DataAbilityHelper.md#ZH-CN_TOPIC_0000002529284609__pacmap) | DataAbilityHelper二级模块。 |

#### DataAbilityOperation

type DataAbilityOperation = [_DataAbilityOperation](../../topics/misc/DataAbilityOperation.md)

DataAbilityOperation二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_DataAbilityOperation](../../topics/misc/DataAbilityOperation.md) | DataAbilityOperation二级模块。 |

#### DataAbilityResult

type DataAbilityResult = [_DataAbilityResult](../../topics/misc/DataAbilityResult.md)

DataAbilityResult二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_DataAbilityResult](../../topics/misc/DataAbilityResult.md) | DataAbilityResult二级模块。 |

#### AbilityResult

type AbilityResult = [_AbilityResult](../../topics/misc/AbilityResult.md)

AbilityResult二级模块。

**系统能力**：SystemCapability.Ability.AbilityBase

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_AbilityResult](../../topics/misc/AbilityResult.md) | AbilityResult二级模块。 |

#### ConnectOptions

type ConnectOptions = [_ConnectOptions](../../topics/misc/ConnectOptions.md)

ConnectOptions二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_ConnectOptions](../../topics/misc/ConnectOptions.md) | ConnectOptions二级模块。 |

#### StartAbilityParameter

type StartAbilityParameter = [_StartAbilityParameter](../../topics/misc/StartAbilityParameter.md)

StartAbilityParameter二级模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

| 类型 | 说明 |
| --- | --- |
| [_StartAbilityParameter](../../topics/misc/StartAbilityParameter.md) | StartAbilityParameter二级模块。 |

**示例：**

```ets
import { ability } from '@kit.AbilityKit';

let dataAbilityHelper: ability.DataAbilityHelper;
let pacMap: ability.PacMap;
let dataAbilityOperation: ability.DataAbilityOperation;
let dataAbilityResult: ability.DataAbilityResult;
let abilityResult: ability.AbilityResult;
let connectOptions: ability.ConnectOptions;
let startAbilityParameter: ability.StartAbilityParameter;
```