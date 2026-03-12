# DataAbilityOperation

定义DataAbility数据操作方式，可以作为[executeBatch](DataAbilityHelper.md#ZH-CN_TOPIC_0000002529284609__dataabilityhelperexecutebatch)的入参，操作数据库的信息。

本接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此接口仅可在FA模型下使用。

#### 导入模块

```ets
import ability from '@ohos.ability.ability';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

名称类型只读可选说明uristring否否指示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx'。type[featureAbility.DataAbilityOperationType](@ohos.ability.featureAbility (FeatureAbility模块).md#ZH-CN_TOPIC_0000002529444565__dataabilityoperationtype7)否否指示数据操作类型。valuesBucket[rdb.ValuesBucket](Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)否是指示要操作的数据值。valueBackReferences[rdb.ValuesBucket](Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)否是指示包含一组键值对的valuesBucket对象。predicates[dataAbility.DataAbilityPredicates](@ohos.data.dataAbility (DataAbility谓词).md#ZH-CN_TOPIC_0000002497444700__dataabilitypredicates)否是指示要设置的筛选条件。如果此参数为空，则操作所有数据记录。predicatesBackReferencesMap<number, number>否是指示用作谓词中筛选条件的反向引用。interruptedboolean否是指示是否可以中断批处理操作。true表示可以中断批处理操作，false表示不可中断批处理操作。expectedCountnumber否是指示要更新或删除的预期行数。