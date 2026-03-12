# DataAbilityResult

定义DataAbility数据操作结果，通过[executeBatch](DataAbilityHelper.md#ZH-CN_TOPIC_0000002529284609__dataabilityhelperexecutebatch)操作数据库时，操作结果使用DataAbilityResult对象返回。

本接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此接口仅可在FA模型下使用。

#### 导入模块

```ets
import ability from '@ohos.ability.ability';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

名称类型只读可选说明uristring否是指示待处理的DataAbility。例：'dataability:///com.example.xxx.xxxx'。countnumber否是指示受操作影响的数据数量。

**示例：**

```ets
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import rdb from '@ohos.data.rdb';
import { BusinessError } from '@ohos.base';

// 批量执行数据库操作
function executeBatchOperation() {
    let dataAbilityUri = ('dataability:///com.example.myapplication.TestDataAbility');
    let DAHelper: ability.DataAbilityHelper;
    DAHelper = featureAbility.acquireDataAbilityHelper(dataAbilityUri);

    let valueBucket: rdb.ValuesBucket = {
        'name': 'DataAbilityHelperTest',
        'age': 24,
        'salary': 2024.20,
    };
    let predicateBackReferences = new Map<number, number>()
    predicateBackReferences.set(1, 1)

    let operations: Array<ability.DataAbilityOperation> = [
        {
            uri: dataAbilityUri,
            type: featureAbility.DataAbilityOperationType.TYPE_INSERT,
            valuesBucket: valueBucket,
            expectedCount: 1,
            predicatesBackReferences: predicateBackReferences,
            interrupted: true,
        },
        {
            uri: dataAbilityUri,
            type: featureAbility.DataAbilityOperationType.TYPE_INSERT,
            valuesBucket: valueBucket,
            expectedCount: 1,
            predicatesBackReferences: predicateBackReferences,
            interrupted: true,
        }
    ];
    try {
        DAHelper.executeBatch(dataAbilityUri, operations).then((data) => {
            for (let i = 0; i < data.length; i++) {
                let dataAbilityResult: ability.DataAbilityResult = data[i];
                console.log(`dataAbilityResult.uri: ${dataAbilityResult.uri}`);
                console.log(`dataAbilityResult.count: ${dataAbilityResult.count}`);
            }
        }).catch((err: BusinessError) => {
            console.error(`executeBatch error: ${JSON.stringify(err)}`);
        });
    } catch (err) {
        console.error(`executeBatch error: ${JSON.stringify(err as BusinessError)}`);
    }
}
```