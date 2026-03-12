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

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

血氧数据类型。

#### Model

type Model = healthModels.BloodOxygenSaturation

血氧采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.BloodOxygenSaturation](healthModels(运动健康数据模型).md#section4460144920180)

血氧采样数据模型。

#### Fields

type Fields = healthFields.BloodOxygenSaturation

血氧采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.BloodOxygenSaturation](healthFields(运动健康数据字段).md#section445762631310)

血氧采样数据字段列表。

#### AggregateResult

type AggregateResult = healthModels.BloodOxygenSaturationAggregateResult

血氧采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.BloodOxygenSaturationAggregateResult](healthModels(运动健康数据模型).md#section597231954018)

血氧采样数据聚合统计结果模型

#### AggregateRequest

type AggregateRequest = healthModels.BloodOxygenSaturationAggregateRequest

血氧采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.BloodOxygenSaturationAggregateRequest](healthModels(运动健康数据模型).md#section362414246403)

血氧采样数据聚合统计请求模型

#### AggregateFields

type AggregateFields = healthFields.BloodOxygenSaturationAggregation

血氧采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.BloodOxygenSaturationAggregation](healthFields(运动健康数据字段).md#section1669661225716)

血氧采样数据支持的聚合统计字段列表。

#### bloodPressure

血压数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

血压数据类型。

#### Model

type Model = healthModels.BloodPressure

血压采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.BloodPressure](healthModels(运动健康数据模型).md#section3682114103016)

血压采样数据模型。

#### Fields

type Fields = healthFields.BloodPressure

血压采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.BloodPressure](healthFields(运动健康数据字段).md#section757514113583)

血压采样数据字段列表。

#### bodyTemperature

体温数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

体温数据类型。

#### Model

type Model = healthModels.BodyTemperature

体温采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.BodyTemperature](healthModels(运动健康数据模型).md#section163973109173)

体温采样数据模型。

#### Fields

type Fields = healthFields.BodyTemperature

体温采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.BodyTemperature](healthFields(运动健康数据字段).md#section169357517159)

体温采样数据字段列表。

#### AggregateResult

type AggregateResult = healthModels.BodyTemperatureAggregateResult

体温采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.BodyTemperatureAggregateResult](healthModels(运动健康数据模型).md#section6662725124415)

体温采样数据聚合统计结果模型。

#### AggregateRequest

type AggregateRequest = healthModels.BodyTemperatureAggregateRequest

体温采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.BodyTemperatureAggregateRequest](healthModels(运动健康数据模型).md#section3663325204419)

体温采样数据聚合统计请求模型。

#### AggregateFields

type AggregateFields = healthFields.BodyTemperatureAggregation

体温采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.BodyTemperatureAggregation](healthFields(运动健康数据字段).md#section0126118114915)

体温采样数据支持的聚合统计字段列表。

#### dailyActivities

日常活动数据类型常量及数据模型。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

日常活动数据类型。

#### Model

type Model = healthModels.DailyActivities

日常活动采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.DailyActivities](healthModels(运动健康数据模型).md#section1950102725213)

日常活动采样数据模型。

#### Fields

type Fields = healthFields.DailyActivities

日常活动采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.DailyActivities](healthFields(运动健康数据字段).md#section19505904120)

日常活动采样数据字段列表。

#### AggregateResult

type AggregateResult = healthModels.DailyActivitiesAggregateResult

日常活动采样数据聚合统计结果模型。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.DailyActivitiesAggregateResult](healthModels(运动健康数据模型).md#section197361850135310)

日常活动采样数据聚合结果模型。

#### AggregateRequest

type AggregateRequest = healthModels.DailyActivitiesAggregateRequest

日常活动采样数据聚合统计请求模型。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.DailyActivitiesAggregateRequest](healthModels(运动健康数据模型).md#section96562416465)

日常活动采样数据聚合请求模型。

#### AggregateFields

type AggregateFields = healthFields.DailyActivitiesAggregation

日常活动采样数据支持的聚合统计字段列表。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.DailyActivitiesAggregation](healthFields(运动健康数据字段).md#section21520371218)

日常活动采样数据支持的聚合统计字段列表。

#### emotion

情绪数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

情绪数据类型。

#### Model

type Model = healthModels.Emotion

情绪采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

类型

**说明**

[healthModels.Emotion](healthModels(运动健康数据模型).md#section1360442913818)

情绪采样数据模型。

#### Fields

type Fields = healthFields.Emotion

情绪采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

类型

**说明**

[healthFields.Emotion](healthFields(运动健康数据字段).md#section19971754101817)

情绪采样数据字段列表。

#### heartRate

动态心率数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

动态心率数据类型。

#### Model

type Model = healthModels.HeartRate

动态心率采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.HeartRate](healthModels(运动健康数据模型).md#section158575417544)

动态心率采样数据模型。

#### Fields

type Fields = healthFields.HeartRate

动态心率采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.HeartRate](healthFields(运动健康数据字段).md#section370919372088)

动态心率采样数据字段列表。

#### AggregateResult

type AggregateResult = healthModels.HeartRateAggregateResult

动态心率采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.HeartRateAggregateResult](healthModels(运动健康数据模型).md#section1618986154718)

动态心率采样数据聚合统计结果模型。

#### AggregateRequest

type AggregateRequest = healthModels.HeartRateAggregateRequest

动态心率采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.HeartRateAggregateRequest](healthModels(运动健康数据模型).md#section419015624713)

动态心率采样数据聚合统计请求模型。

#### AggregateFields

type AggregateFields = healthFields.HeartRateAggregation

动态心率采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.HeartRateAggregation](healthFields(运动健康数据字段).md#section16703114311507)

动态心率采样数据支持的聚合统计字段列表。

#### heartRateVariability

心率变异性数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

心率变异性数据类型。

#### Model

type Model = healthModels.HeartRateVariability

心率变异性采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

类型

**说明**

[healthModels.HeartRateVariability](healthModels(运动健康数据模型).md#section476295519419)

心率变异性采样数据模型。

#### Fields

type Fields = healthFields.HeartRateVariability

心率变异性采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

类型

**说明**

[healthFields.HeartRateVariability](healthFields(运动健康数据字段).md#section19727135714284)

心率变异性采样数据字段列表。

#### height

身高数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

身高数据类型。

#### Model

type Model = healthModels.Height

身高采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.Height](healthModels(运动健康数据模型).md#section53612024115018)

身高采样数据模型。

#### Fields

type Fields = healthFields.Height

身高采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.Height](healthFields(运动健康数据字段).md#section8653722114617)

身高采样数据字段列表。

#### restingHeartRate

静息心率数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

静息心率数据类型。

#### Model

type Model = healthModels.RestingHeartRate

静息心率采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.RestingHeartRate](healthModels(运动健康数据模型).md#section15611411402)

静息心率采样数据模型。

#### Fields

type Fields = healthFields.RestingHeartRate

静息心率采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.RestingHeartRate](healthFields(运动健康数据字段).md#section126714462018)

静息心率采样数据字段列表。

#### AggregateResult

type AggregateResult = healthModels.RestingHeartRateAggregateResult

静息心率采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.RestingHeartRateAggregateResult](healthModels(运动健康数据模型).md#section179020215478)

静息心率采样数据聚合统计结果模型。

#### AggregateRequest

type AggregateRequest = healthModels.RestingHeartRateAggregateRequest

静息心率采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.RestingHeartRateAggregateRequest](healthModels(运动健康数据模型).md#section690314211475)

静息心率采样数据聚合统计请求模型。

#### AggregateFields

type AggregateFields = healthFields.RestingHeartRateAggregation

静息心率采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.RestingHeartRateAggregation](healthFields(运动健康数据字段).md#section11821829192414)

静息心率采样数据支持的聚合统计字段列表。

#### skinTemperature

皮肤体温数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

皮肤体温数据类型。

#### Model

type Model = healthModels.SkinTemperature

皮肤体温采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.SkinTemperature](healthModels(运动健康数据模型).md#section20161955257)

皮肤体温采样数据模型。

#### Fields

type Fields = healthFields.SkinTemperature

皮肤体温采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.SkinTemperature](healthFields(运动健康数据字段).md#section1987717196217)

皮肤体温采样数据字段列表。

#### AggregateResult

type AggregateResult = healthModels.SkinTemperatureAggregateResult

皮肤体温采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.SkinTemperatureAggregateResult](healthModels(运动健康数据模型).md#section196931933174713)

皮肤体温采样数据聚合统计结果模型。

#### AggregateRequest

type AggregateRequest = healthModels.SkinTemperatureAggregateRequest

皮肤体温采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.SkinTemperatureAggregateRequest](healthModels(运动健康数据模型).md#section17694123374713)

皮肤体温采样数据聚合统计请求模型。

#### AggregateFields

type AggregateFields = healthFields.SkinTemperatureAggregation

皮肤体温采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.SkinTemperatureAggregation](healthFields(运动健康数据字段).md#section140143554319)

皮肤体温采样数据支持的聚合统计字段列表。

#### stress

压力数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

压力数据类型。

#### Model

type Model = healthModels.Stress

压力采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.Stress](healthModels(运动健康数据模型).md#section91515324419)

压力采样数据模型。

#### Fields

type Fields = healthFields.Stress

压力采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.Stress](healthFields(运动健康数据字段).md#section1199164115227)

压力采样数据字段列表。

#### AggregateResult

type AggregateResult = healthModels.StressAggregateResult

压力采样数据聚合统计结果模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.StressAggregateResult](healthModels(运动健康数据模型).md#section9313947104710)

压力采样数据聚合统计结果模型。

#### AggregateRequest

type AggregateRequest = healthModels.StressAggregateRequest

压力采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.StressAggregateRequest](healthModels(运动健康数据模型).md#section2031411477477)

压力采样数据聚合统计请求模型。

#### AggregateFields

type AggregateFields = healthFields.StressAggregation

压力采样数据支持的聚合统计字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.StressAggregation](healthFields(运动健康数据字段).md#section58707765616)

压力采样数据支持的聚合统计字段列表。

#### weight

体重数据类型常量及数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

#### 常量

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

名称

类型

说明

DATA_TYPE

[healthStore.DataType](healthStore(运动健康数据服务).md#section136147472298)

体重数据类型。

#### Model

type Model = healthModels.Weight

体重采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthModels.Weight](healthModels(运动健康数据模型).md#section82991615171110)

体重采样数据模型。

#### Fields

type Fields = healthFields.Weight

体重采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthFields.Weight](healthFields(运动健康数据字段).md#section1534182411503)

体重采样数据字段列表。