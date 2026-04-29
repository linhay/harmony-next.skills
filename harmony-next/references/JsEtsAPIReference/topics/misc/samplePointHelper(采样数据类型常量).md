# samplePointHelper(采样数据类型常量)

本模块提供采样数据类型常量及数据模型。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { healthStore } from '@kit.HealthServiceKit';
```

此模块为healthStore子模块，需通过healthStore.samplePointHelper方式使用。

#### bloodOxygenSaturation

血氧数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 血氧数据类型。 |

#### Model

type Model = healthModels.BloodOxygenSaturation

血氧采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.BloodOxygenSaturation | 血氧采样数据模型。 |

#### Fields

type Fields = healthFields.BloodOxygenSaturation

血氧采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BloodOxygenSaturation | 血氧采样数据字段列表。 |

#### AggregateResult

type AggregateResult = healthModels.BloodOxygenSaturationAggregateResult

血氧采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.BloodOxygenSaturationAggregateResult | 血氧采样数据聚合统计结果模型 |

#### AggregateRequest

type AggregateRequest = healthModels.BloodOxygenSaturationAggregateRequest

血氧采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.BloodOxygenSaturationAggregateRequest | 血氧采样数据聚合统计请求模型 |

#### AggregateFields

type AggregateFields = healthFields.BloodOxygenSaturationAggregation

血氧采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BloodOxygenSaturationAggregation | 血氧采样数据支持的聚合统计字段列表。 |

#### bloodPressure

血压数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 血压数据类型。 |

#### Model

type Model = healthModels.BloodPressure

血压采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.BloodPressure | 血压采样数据模型。 |

#### Fields

type Fields = healthFields.BloodPressure

血压采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BloodPressure | 血压采样数据字段列表。 |

#### bodyTemperature

体温数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 体温数据类型。 |

#### Model

type Model = healthModels.BodyTemperature

体温采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.BodyTemperature | 体温采样数据模型。 |

#### Fields

type Fields = healthFields.BodyTemperature

体温采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BodyTemperature | 体温采样数据字段列表。 |

#### AggregateResult

type AggregateResult = healthModels.BodyTemperatureAggregateResult

体温采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.BodyTemperatureAggregateResult | 体温采样数据聚合统计结果模型。 |

#### AggregateRequest

type AggregateRequest = healthModels.BodyTemperatureAggregateRequest

体温采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.BodyTemperatureAggregateRequest | 体温采样数据聚合统计请求模型。 |

#### AggregateFields

type AggregateFields = healthFields.BodyTemperatureAggregation

体温采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.BodyTemperatureAggregation | 体温采样数据支持的聚合统计字段列表。 |

#### dailyActivities

日常活动数据类型常量及数据模型。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 日常活动数据类型。 |

#### Model

type Model = healthModels.DailyActivities

日常活动采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.DailyActivities | 日常活动采样数据模型。 |

#### Fields

type Fields = healthFields.DailyActivities

日常活动采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.DailyActivities | 日常活动采样数据字段列表。 |

#### AggregateResult

type AggregateResult = healthModels.DailyActivitiesAggregateResult

日常活动采样数据聚合统计结果模型。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.DailyActivitiesAggregateResult | 日常活动采样数据聚合结果模型。 |

#### AggregateRequest

type AggregateRequest = healthModels.DailyActivitiesAggregateRequest

日常活动采样数据聚合统计请求模型。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.DailyActivitiesAggregateRequest | 日常活动采样数据聚合请求模型。 |

#### AggregateFields

type AggregateFields = healthFields.DailyActivitiesAggregation

日常活动采样数据支持的聚合统计字段列表。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.DailyActivitiesAggregation | 日常活动采样数据支持的聚合统计字段列表。 |

#### emotion

情绪数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 情绪数据类型。 |

#### Model

type Model = healthModels.Emotion

情绪采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| healthModels.Emotion | 情绪采样数据模型。 |

#### Fields

type Fields = healthFields.Emotion

情绪采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| healthFields.Emotion | 情绪采样数据字段列表。 |

#### heartRate

动态心率数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 动态心率数据类型。 |

#### Model

type Model = healthModels.HeartRate

动态心率采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.HeartRate | 动态心率采样数据模型。 |

#### Fields

type Fields = healthFields.HeartRate

动态心率采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.HeartRate | 动态心率采样数据字段列表。 |

#### AggregateResult

type AggregateResult = healthModels.HeartRateAggregateResult

动态心率采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.HeartRateAggregateResult | 动态心率采样数据聚合统计结果模型。 |

#### AggregateRequest

type AggregateRequest = healthModels.HeartRateAggregateRequest

动态心率采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.HeartRateAggregateRequest | 动态心率采样数据聚合统计请求模型。 |

#### AggregateFields

type AggregateFields = healthFields.HeartRateAggregation

动态心率采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.HeartRateAggregation | 动态心率采样数据支持的聚合统计字段列表。 |

#### heartRateVariability

心率变异性数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 心率变异性数据类型。 |

#### Model

type Model = healthModels.HeartRateVariability

心率变异性采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| healthModels.HeartRateVariability | 心率变异性采样数据模型。 |

#### Fields

type Fields = healthFields.HeartRateVariability

心率变异性采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| healthFields.HeartRateVariability | 心率变异性采样数据字段列表。 |

#### height

身高数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 身高数据类型。 |

#### Model

type Model = healthModels.Height

身高采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Height | 身高采样数据模型。 |

#### Fields

type Fields = healthFields.Height

身高采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.Height | 身高采样数据字段列表。 |

#### restingHeartRate

静息心率数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 静息心率数据类型。 |

#### Model

type Model = healthModels.RestingHeartRate

静息心率采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.RestingHeartRate | 静息心率采样数据模型。 |

#### Fields

type Fields = healthFields.RestingHeartRate

静息心率采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RestingHeartRate | 静息心率采样数据字段列表。 |

#### AggregateResult

type AggregateResult = healthModels.RestingHeartRateAggregateResult

静息心率采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.RestingHeartRateAggregateResult | 静息心率采样数据聚合统计结果模型。 |

#### AggregateRequest

type AggregateRequest = healthModels.RestingHeartRateAggregateRequest

静息心率采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.RestingHeartRateAggregateRequest | 静息心率采样数据聚合统计请求模型。 |

#### AggregateFields

type AggregateFields = healthFields.RestingHeartRateAggregation

静息心率采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.RestingHeartRateAggregation | 静息心率采样数据支持的聚合统计字段列表。 |

#### skinTemperature

皮肤体温数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 皮肤体温数据类型。 |

#### Model

type Model = healthModels.SkinTemperature

皮肤体温采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.SkinTemperature | 皮肤体温采样数据模型。 |

#### Fields

type Fields = healthFields.SkinTemperature

皮肤体温采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SkinTemperature | 皮肤体温采样数据字段列表。 |

#### AggregateResult

type AggregateResult = healthModels.SkinTemperatureAggregateResult

皮肤体温采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.SkinTemperatureAggregateResult | 皮肤体温采样数据聚合统计结果模型。 |

#### AggregateRequest

type AggregateRequest = healthModels.SkinTemperatureAggregateRequest

皮肤体温采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.SkinTemperatureAggregateRequest | 皮肤体温采样数据聚合统计请求模型。 |

#### AggregateFields

type AggregateFields = healthFields.SkinTemperatureAggregation

皮肤体温采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.SkinTemperatureAggregation | 皮肤体温采样数据支持的聚合统计字段列表。 |

#### stress

压力数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 压力数据类型。 |

#### Model

type Model = healthModels.Stress

压力采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Stress | 压力采样数据模型。 |

#### Fields

type Fields = healthFields.Stress

压力采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.Stress | 压力采样数据字段列表。 |

#### AggregateResult

type AggregateResult = healthModels.StressAggregateResult

压力采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.StressAggregateResult | 压力采样数据聚合统计结果模型。 |

#### AggregateRequest

type AggregateRequest = healthModels.StressAggregateRequest

压力采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.StressAggregateRequest | 压力采样数据聚合统计请求模型。 |

#### AggregateFields

type AggregateFields = healthFields.StressAggregation

压力采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.StressAggregation | 压力采样数据支持的聚合统计字段列表。 |

#### weight

体重数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| DATA_TYPE | healthStore.DataType | 体重数据类型。 |

#### Model

type Model = healthModels.Weight

体重采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthModels.Weight | 体重采样数据模型。 |

#### Fields

type Fields = healthFields.Weight

体重采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| healthFields.Weight | 体重采样数据字段列表。 |