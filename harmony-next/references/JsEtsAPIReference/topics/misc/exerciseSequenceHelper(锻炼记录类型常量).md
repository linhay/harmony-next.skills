# exerciseSequenceHelper(锻炼记录类型常量)

本模块提供锻炼记录数据类型常量及数据模型。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { healthStore } from '@kit.HealthServiceKit';
```

此模块为healthStore子模块，需通过healthStore.exerciseSequenceHelper方式使用。

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 锻炼记录数据类型。 |

#### adventures

户外探险数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 户外探险子数据类型。 |

#### Model

type Model = healthModels.Adventures

户外探险锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Adventures | 户外探险锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.AdventuresSummary

户外探险统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.AdventuresSummary | 户外探险统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.AdventuresDetail

户外探险详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.AdventuresDetail | 户外探险详情数据字段列表。 |

#### basketball

篮球数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 篮球子数据类型。 |

#### Model

type Model = healthModels.Basketball

篮球锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Basketball | 篮球锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.BasketballSummary

篮球统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BasketballSummary | 篮球统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.BasketballDetail

篮球详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BasketballDetail | 篮球详情数据字段列表。 |

#### biathlon

冬季两项数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 冬季两项子数据类型。 |

#### Model

type Model = healthModels.Biathlon

冬季两项锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Biathlon | 冬季两项锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.BiathlonSummary

冬季两项统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BiathlonSummary | 冬季两项统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.BiathlonDetail

冬季两项详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BiathlonDetail | 冬季两项详情数据字段列表。 |

#### bmx

BMX自行车数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | BMX自行车子数据类型。 |

#### Model

type Model = healthModels.Bmx

BMX自行车锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Bmx | BMX自行车锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.CyclingSummary

BMX自行车统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.CyclingSummary | BMX自行车统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.CyclingDetail

BMX自行车详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.CyclingDetail | BMX自行车详情数据字段列表。 |

#### breathHoldingTest

闭气测试数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 闭气测试子数据类型。 |

#### Model

type Model = healthModels.BreathHoldingTest

闭气测试锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.BreathHoldingTest | 闭气测试锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.BreathHoldingTestSummary

闭气测试统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BreathHoldingTestSummary | 闭气测试统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.BreathHoldingTestDetail

闭气测试详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BreathHoldingTestDetail | 闭气测试详情数据字段列表。 |

#### breathHoldingTrain

闭气训练数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 闭气训练子数据类型。 |

#### Model

type Model = healthModels.BreathHoldingTrain

闭气训练锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.BreathHoldingTrain | 闭气训练锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.BreathHoldingTrainSummary

闭气训练统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BreathHoldingTrainSummary | 闭气训练统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.BreathHoldingTrainDetail

闭气训练详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BreathHoldingTrainDetail | 闭气训练详情数据字段列表。 |

#### cycling

户外骑行数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 户外骑行子数据类型。 |

#### Model

type Model = healthModels.Cycling

户外骑行锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Cycling | 户外骑行锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.CyclingSummary

户外骑行统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.CyclingSummary | 户外骑行统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.CyclingDetail

户外骑行详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.CyclingDetail | 户外骑行详情数据字段列表。 |

#### diving

自由潜水数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 自由潜水子数据类型。 |

#### Model

type Model = healthModels.Diving

自由潜水锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Diving | 自由潜水锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.DivingSummary

自由潜水统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.DivingSummary | 自由潜水统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.DivingDetail

自由潜水详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.DivingDetail | 自由潜水详情数据字段列表。 |

#### elliptical

椭圆机数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 椭圆机子数据类型。 |

#### Model

type Model = healthModels.Elliptical

椭圆机锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Elliptical | 椭圆机锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.EllipticalSummary

椭圆机统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.EllipticalSummary | 椭圆机统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.EllipticalDetail

椭圆机详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.EllipticalDetail | 椭圆机详情数据字段列表。 |

#### golfCourseModel

高尔夫场地模式数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 高尔夫场地模式子数据类型。 |

#### Model

type Model = healthModels.GolfCourseModel

高尔夫场地模式锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.GolfCourseModel | 高尔夫场地模式锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.GolfCourseModelSummary

高尔夫场地模式统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.GolfCourseModelSummary | 高尔夫场地模式统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.GolfCourseModelDetail

高尔夫场地模式详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.GolfCourseModelDetail | 高尔夫场地模式详情数据字段列表。 |

#### golfPractice

高尔夫练习场模式数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 高尔夫练习场模式子数据类型。 |

#### Model

type Model = healthModels.GolfPractice

高尔夫练习场模式锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.GolfPractice | 高尔夫练习场模式锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.GolfPracticeSummary

高尔夫练习场模式统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.GolfPracticeSummary | 高尔夫练习场模式统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.GolfPracticeDetail

高尔夫练习场模式详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.GolfPracticeDetail | 高尔夫练习场模式详情数据字段列表。 |

#### hiking

徒步数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 徒步子数据类型。 |

#### Model

type Model = healthModels.Hiking

徒步锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Hiking | 徒步锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.WalkingSummary

徒步统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.WalkingSummary | 徒步统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.WalkingDetail

徒步详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.WalkingDetail | 徒步详情数据字段列表。 |

#### indoorCycling

室内骑行数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 室内骑行子数据类型。 |

#### Model

type Model = healthModels.IndoorCycling

室内骑行锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.IndoorCycling | 室内骑行锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.CyclingSummary

室内骑行统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.CyclingSummary | 室内骑行统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.CyclingDetail

室内骑行详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.CyclingDetail | 室内骑行详情数据字段列表。 |

#### indoorRunning

室内跑步数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 室内跑步子数据类型。 |

#### Model

type Model = healthModels.IndoorRunning

室内跑步锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.IndoorRunning | 室内跑步锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.RunningSummary

室内跑步统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RunningSummary | 室内跑步统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.RunningDetail

室内跑步详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RunningDetail | 室内跑步详情数据字段列表。 |

#### indoorWalking

室内步行数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 室内步行子数据类型。 |

#### Model

type Model = healthModels.IndoorWalking

室内步行锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.IndoorWalking | 室内步行锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.WalkingSummary

室内步行统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.WalkingSummary | 室内步行统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.WalkingDetail

室内步行详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.WalkingDetail | 室内步行详情数据字段列表。 |

#### jumpingRope

跳绳数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 跳绳子数据类型。 |

#### Model

type Model = healthModels.JumpingRope

跳绳锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.JumpingRope | 跳绳锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.JumpingRopeSummary

跳绳统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.JumpingRopeSummary | 跳绳统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.JumpingRopeDetail

跳绳详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.JumpingRopeDetail | 跳绳详情数据字段列表。 |

#### mountainHike

登山数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 登山子数据类型。 |

#### Model

type Model = healthModels.MountainHike

登山锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.MountainHike | 登山锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.MountainHikeSummary

登山统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.MountainHikeSummary | 登山统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.MountainHikeDetail

登山详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.MountainHikeDetail | 登山详情数据字段列表。 |

#### openWaterSwim

开放水域游泳数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 开放水域游泳子数据类型。 |

#### Model

type Model = healthModels.OpenWaterSwim

开放水域游泳锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.OpenWaterSwim | 开放水域游泳锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.OpenWaterSwimSummary

开放水域游泳统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.OpenWaterSwimSummary | 开放水域游泳统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.OpenWaterSwimDetail

开放水域游泳详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.OpenWaterSwimDetail | 开放水域游泳详情数据字段列表。 |

#### poolSwim

泳池游泳数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 泳池游泳子数据类型。 |

#### Model

type Model = healthModels.PoolSwim

泳池游泳锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.PoolSwim | 泳池游泳锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.PoolSwimSummary

泳池游泳统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.PoolSwimSummary | 泳池游泳统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.PoolSwimDetail

泳池游泳详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.PoolSwimDetail | 泳池游泳详情数据字段列表。 |

#### rower

划船机数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 划船机子数据类型。 |

#### Model

type Model = healthModels.Rower

划船机锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Rower | 划船机锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.RowerSummary

划船机统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RowerSummary | 划船机统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.RowerDetail

划船机详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RowerDetail | 划船机详情数据字段列表。 |

#### rowing

赛艇数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 赛艇子数据类型。 |

#### Model

type Model = healthModels.Rowing

赛艇锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Rowing | 赛艇锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.RowingSummary

赛艇统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RowingSummary | 赛艇统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.RowingDetail

赛艇详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RowingDetail | 赛艇详情数据字段列表。 |

#### running

户外跑步数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 户外跑步子数据类型。 |

#### Model

type Model = healthModels.Running

户外跑步锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Running | 户外跑步锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.RunningSummary

户外跑步统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RunningSummary | 户外跑步统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.RunningDetail

户外跑步详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RunningDetail | 户外跑步详情数据字段列表。 |

#### scubaDiving

水肺潜水数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 水肺潜水子数据类型。 |

#### Model

type Model = healthModels.ScubaDiving

水肺潜水锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.ScubaDiving | 水肺潜水锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.ScubaDivingSummary

水肺潜水统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.ScubaDivingSummary | 水肺潜水统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.ScubaDivingDetail

水肺潜水详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.ScubaDivingDetail | 水肺潜水详情数据字段列表。 |

#### skiing

滑雪数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 滑雪子数据类型。 |

#### Model

type Model = healthModels.Skiing

滑雪锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Skiing | 滑雪锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.SkiingSummary

滑雪统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SkiingSummary | 滑雪统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.SkiingDetail

滑雪详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SkiingDetail | 滑雪详情数据字段列表。 |

#### sled

滑雪橇数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 滑雪橇子数据类型。 |

#### Model

type Model = healthModels.Sled

滑雪橇锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Sled | 滑雪橇锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.SledSummary

滑雪橇统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SledSummary | 滑雪橇统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.SledDetail

滑雪橇详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SledDetail | 滑雪橇详情数据字段列表。 |

#### snowboarding

单板滑雪数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 单板滑雪子数据类型。 |

#### Model

type Model = healthModels.Snowboarding

单板滑雪锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Snowboarding | 单板滑雪锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.SnowboardingSummary

单板滑雪统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SnowboardingSummary | 单板滑雪统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.SnowboardingDetail

单板滑雪详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SnowboardingDetail | 单板滑雪详情数据字段列表。 |

#### spinning

动感单车数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 动感单车子数据类型。 |

#### Model

type Model = healthModels.Spinning

动感单车锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Spinning | 动感单车锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.CyclingSummary

动感单车统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.CyclingSummary | 动感单车统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.CyclingDetail

动感单车详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.CyclingDetail | 动感单车详情数据字段列表。 |

#### sports

其他运动数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| AEROBICS | healthStore.SubDataType | 健美操 |
| AIR_WALKER | healthStore.SubDataType | 漫步机 |
| ARCHERY | healthStore.SubDataType | 射箭 |
| BADMINTON | healthStore.SubDataType | 羽毛球 |
| BALLET | healthStore.SubDataType | 芭蕾舞 |
| BASEBALL | healthStore.SubDataType | 棒球 |
| BEACH_SOCCER | healthStore.SubDataType | 沙滩足球 |
| BEACH_VOLLEYBALL | healthStore.SubDataType | 沙滩排球 |
| BELLY_DANCE | healthStore.SubDataType | 肚皮舞 |
| BODY_COMBAT | healthStore.SubDataType | 搏击操 |
| BOWLING | healthStore.SubDataType | 保龄球 |
| BOXING | healthStore.SubDataType | 拳击 |
| BUNGEE_JUMPING | healthStore.SubDataType | 蹦极 |
| CANOEING | healthStore.SubDataType | 皮划艇 |
| CORE_TRAINING | healthStore.SubDataType | 核心训练 |
| CRICKET | healthStore.SubDataType | 板球 |
| CROSS_COUNTRY_SKIING | healthStore.SubDataType | 越野滑雪 |
| CROSS_FIT | healthStore.SubDataType | Cross fit |
| CURLING | healthStore.SubDataType | 冰壶 |
| DANCE | healthStore.SubDataType | 舞蹈 |
| DARTS | healthStore.SubDataType | 飞镖 |
| DODGE_BALL | healthStore.SubDataType | 躲避球 |
| DRAGON_BOAT | healthStore.SubDataType | 龙舟 |
| DRIFTING | healthStore.SubDataType | 漂流 |
| ESPORTS | healthStore.SubDataType | 电子竞技 |
| FENCING | healthStore.SubDataType | 击剑 |
| FISHING | healthStore.SubDataType | 钓鱼 |
| FREE_SPARRING | healthStore.SubDataType | 自由搏击 |
| FREE_TRAINING | healthStore.SubDataType | 自由训练 |
| FRISBEE | healthStore.SubDataType | 飞盘 |
| FUNCTIONAL_TRAINING | healthStore.SubDataType | 功能性训练 |
| GATEBALL | healthStore.SubDataType | 门球 |
| HANDBALL | healthStore.SubDataType | 手球 |
| HIIT | healthStore.SubDataType | HIIT |
| HOCKEY | healthStore.SubDataType | 曲棍球 |
| HORSE_RIDING | healthStore.SubDataType | 骑马 |
| HULA_HOOP | healthStore.SubDataType | 呼啦圈 |
| HUNTING | healthStore.SubDataType | 对战游戏 |
| ICE_HOCKEY | healthStore.SubDataType | 冰球 |
| JAZZ_DANCE | healthStore.SubDataType | 爵士舞 |
| KARATE | healthStore.SubDataType | 空手道 |
| KENDO | healthStore.SubDataType | 剑道 |
| KITE_FLYING | healthStore.SubDataType | 放风筝 |
| LATIN_DANCE | healthStore.SubDataType | 拉丁舞 |
| MARTIAL_ARTS | healthStore.SubDataType | 武术 |
| MOTORBOAT | healthStore.SubDataType | 摩托艇 |
| OBSTACLE_RACE | healthStore.SubDataType | 障碍赛 |
| ORIENTEERING | healthStore.SubDataType | 定向越野 |
| PADEL | healthStore.SubDataType | 笼式网球 |
| PARACHUTE | healthStore.SubDataType | 跳伞 |
| PARALLEL_BARS | healthStore.SubDataType | 双杠 |
| PARKOUR | healthStore.SubDataType | 跑酷 |
| PHYSICAL_TRAINING | healthStore.SubDataType | 体能训练 |
| PILATES | healthStore.SubDataType | 普拉提 |
| PLAYGROUND_RACE | healthStore.SubDataType | 操场赛跑 |
| PLAZA_DANCING | healthStore.SubDataType | 广场舞 |
| POOL | healthStore.SubDataType | 台球 |
| RACING_CAR | healthStore.SubDataType | 赛车 |
| ROCK_CLIMBING | healthStore.SubDataType | 攀岩 |
| ROLLER_SKATING | healthStore.SubDataType | 轮滑 |
| RUGBY | healthStore.SubDataType | 橄榄球 |
| SAILBOAT | healthStore.SubDataType | 帆船 |
| SENSE_SPORT | healthStore.SubDataType | 体感运动 |
| SEPAKTAKRAW | healthStore.SubDataType | 藤球 |
| SHUTTLECOCK | healthStore.SubDataType | 毽球 |
| SINGLE_BAR | healthStore.SubDataType | 单杠 |
| SKATEBOARD | healthStore.SubDataType | 滑板 |
| SKATING | healthStore.SubDataType | 滑冰 |
| SNOWMOBILE | healthStore.SubDataType | 雪地摩托 |
| SOCCER | healthStore.SubDataType | 足球 |
| SOFTBALL | healthStore.SubDataType | 垒球 |
| SQUASH | healthStore.SubDataType | 壁球 |
| STAIR_CLIMBING | healthStore.SubDataType | 爬楼 |
| STEPPER | healthStore.SubDataType | 踏步机 |
| STREET_DANCE | healthStore.SubDataType | 街舞 |
| STRENGTH_TRAINING | healthStore.SubDataType | 力量训练 |
| SUP | healthStore.SubDataType | 桨板冲浪 |
| SURFING | healthStore.SubDataType | 冲浪 |
| SWINGING | healthStore.SubDataType | 秋千 |
| TABLE_TENNIS | healthStore.SubDataType | 乒乓球 |
| TAEKWONDO | healthStore.SubDataType | 跆拳道 |
| TAI_CHI | healthStore.SubDataType | 太极拳 |
| TENNIS | healthStore.SubDataType | 网球 |
| TRIATHLON | healthStore.SubDataType | 铁人三项 |
| TUG_OF_WAR | healthStore.SubDataType | 拔河 |
| VOLLEYBALL | healthStore.SubDataType | 排球 |
| YOGA | healthStore.SubDataType | 瑜伽 |

#### Model

type Model = healthModels.Sports

通用锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Sports | 通用锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.SportsSummary

通用统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SportsSummary | 通用统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.SportsDetail

通用详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SportsDetail | 通用详情数据字段列表。 |

#### trailRunning

越野跑数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 越野跑子数据类型。 |

#### Model

type Model = healthModels.TrailRunning

越野跑锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.TrailRunning | 越野跑锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.RunningSummary

越野跑统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RunningSummary | 越野跑统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.RunningDetail

越野跑详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RunningDetail | 越野跑详情数据字段列表。 |

#### walking

户外步行数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| EXERCISE_TYPE | healthStore.SubDataType | 户外步行子数据类型。 |

#### Model

type Model = healthModels.Walking

户外步行锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Walking | 户外步行锻炼记录数据模型。 |

#### SummaryFields

type SummaryFields = healthFields.WalkingSummary

户外步行统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.WalkingSummary | 户外步行统计数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.WalkingDetail

户外步行详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.WalkingDetail | 户外步行详情数据字段列表。 |