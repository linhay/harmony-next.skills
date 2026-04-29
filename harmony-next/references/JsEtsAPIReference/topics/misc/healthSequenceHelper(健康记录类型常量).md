# healthSequenceHelper(健康记录类型常量)

本模块提供健康记录数据类型常量及数据模型。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { healthStore } from '@kit.HealthServiceKit';
```

此模块为healthStore子模块，需通过healthStore.healthSequenceHelper方式使用。

#### sleepRecord

夜间睡眠数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 夜间睡眠数据类型。 |

#### Model

type Model = healthModels.SleepRecord

夜间睡眠健康记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.SleepRecord | 夜间睡眠健康记录数据模型。 |

#### Fields

type Fields = healthFields.Sleep

夜间睡眠健康记录数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.Sleep | 夜间睡眠健康记录数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.SleepDetail

睡眠详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SleepDetail | 睡眠详情数据字段列表。 |

#### sleepNapRecord

零星小睡数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 零星小睡数据类型。 |

#### Model

type Model = healthModels.SleepNapRecord

零星小睡健康记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.SleepNapRecord | 零星小睡健康记录数据模型。 |

#### Fields

type Fields = healthFields.SleepNap

零星小睡健康记录数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SleepNap | 零星小睡健康记录数据字段列表。 |

#### DetailFields

type DetailFields = healthFields.SleepDetail

睡眠详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SleepDetail | 睡眠详情数据字段列表。 |