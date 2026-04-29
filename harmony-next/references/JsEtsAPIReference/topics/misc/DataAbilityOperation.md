# DataAbilityOperation

定义DataAbility数据操作方式，可以作为[executeBatch](DataAbilityHelper.md#ZH-CN_TOPIC_0000002553360489__dataabilityhelperexecutebatch)的入参，操作数据库的信息。

  ![image](public_sys-resources/note_3.0-zh-cn.webp)

本接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此接口仅可在FA模型下使用。

**导入模块**

```ets
import ability from '@ohos.ability.ability';
```

**属性**

系统能力：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uri | string | 否 | 否 | 指示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx'。 |
| type | featureAbility.DataAbilityOperationType | 否 | 否 | 指示数据操作类型。 |
| valuesBucket | rdb.ValuesBucket | 否 | 是 | 指示要操作的数据值。 |
| valueBackReferences | rdb.ValuesBucket | 否 | 是 | 指示包含一组键值对的valuesBucket对象。 |
| predicates | dataAbility.DataAbilityPredicates | 否 | 是 | 指示要设置的筛选条件。如果此参数为空，则操作所有数据记录。 |
| predicatesBackReferences | Map<number, number> | 否 | 是 | 指示用作谓词中筛选条件的反向引用。 |
| interrupted | boolean | 否 | 是 | 指示是否可以中断批处理操作。true表示可以中断批处理操作，false表示不可中断批处理操作。 |
| expectedCount | number | 否 | 是 | 指示要更新或删除的预期行数。 |