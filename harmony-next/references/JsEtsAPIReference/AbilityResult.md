# AbilityResult

定义UIAbility被拉起并退出后返回给调用方的结果码和数据。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

[Stage模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#stage模型)下：

```ets
import { common } from '@kit.AbilityKit';
```

[FA模型](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology#fa模型)下：

```ets
import ability from '@ohos.ability.ability';
```

#### 使用说明

Stage模型下：可以通过[startAbilityForResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__startabilityforresult)获取被拉起的UIAbility退出后返回的AbilityResult对象，被startAbilityForResult拉起的UIAbility对象可以通过[terminateSelfWithResult](UIAbilityContext.md#ZH-CN_TOPIC_0000002497604628__terminateselfwithresult)返回AbilityResult对象。

FA模型下：可以通过[startAbilityForResult](@ohos.ability.featureAbility (FeatureAbility模块).md#ZH-CN_TOPIC_0000002529444565__featureabilitystartabilityforresult7)获取被拉起的UIAbility退出后返回的AbilityResult对象，被startAbilityForResult拉起的UIAbility对象可以通过[terminateSelfWithResult](@ohos.ability.featureAbility (FeatureAbility模块).md#ZH-CN_TOPIC_0000002529444565__featureabilityterminateselfwithresult7)返回AbilityResult对象。

#### 属性

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityBase

名称类型只读可选说明resultCodenumber否否

目标方的UIAbility被拉起并退出后，目标方返回给拉起方的结果码。

- 正常情况下，返回目标方传递的结果码。

- 异常情况下，返回-1。

want[Want](@ohos.app.ability.Want (Want).md)否是表示UIAbility被拉起并退出后返回的数据。