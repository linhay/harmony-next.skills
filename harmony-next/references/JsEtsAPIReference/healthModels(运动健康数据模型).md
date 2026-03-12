# healthModels(运动健康数据模型)

本模块提供运动健康数据模型。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { healthStore } from '@kit.HealthServiceKit';
```

此模块为healthStore子模块，需通过healthStore.healthModels方式使用。

#### Adventures

type Adventures = healthStore.ExerciseSequence<healthFields.AdventuresSummary, healthFields.AdventuresDetail>

户外探险锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.AdventuresSummary](healthFields(运动健康数据字段).md#section1679513731311), [healthFields.AdventuresDetail](healthFields(运动健康数据字段).md#section16124059161013)>

户外探险锻炼记录数据模型。

#### Basketball

type Basketball = healthStore.ExerciseSequence<healthFields.BasketballSummary, healthFields.BasketballDetail>

篮球锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.BasketballSummary](healthFields(运动健康数据字段).md#section10673222193111), [healthFields.BasketballDetail](healthFields(运动健康数据字段).md#section1351703362917)>

篮球锻炼记录数据模型。

#### Biathlon

type Biathlon = healthStore.ExerciseSequence<healthFields.BiathlonSummary, healthFields.BiathlonDetail>

冬季两项锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.BiathlonSummary](healthFields(运动健康数据字段).md#section17960123155119), [healthFields.BiathlonDetail](healthFields(运动健康数据字段).md#section16793944164419)>

冬季两项锻炼记录数据模型。

#### BloodOxygenSaturation

type BloodOxygenSaturation = healthStore.SamplePoint<healthFields.BloodOxygenSaturation>

血氧采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.BloodOxygenSaturation](healthFields(运动健康数据字段).md#section445762631310)>

血氧采样数据模型。

#### BloodOxygenSaturationAggregateRequest

type BloodOxygenSaturationAggregateRequest = healthStore.AggregateRequest<healthFields.BloodOxygenSaturationAggregation>

血氧采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateRequest](healthStore(运动健康数据服务).md#section599483722019)<[healthFields.BloodOxygenSaturationAggregation](healthFields(运动健康数据字段).md#section1669661225716)>

血氧采样数据聚合统计请求模型。

#### BloodOxygenSaturationAggregateResult

type BloodOxygenSaturationAggregateResult = healthStore.AggregateResult<healthFields.BloodOxygenSaturationAggregation>

血氧聚合结果数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateResult](healthStore(运动健康数据服务).md#section19656142151412)<[healthFields.BloodOxygenSaturationAggregation](healthFields(运动健康数据字段).md#section1669661225716)>

血氧聚合结果数据模型。

#### BloodPressure

type BloodPressure = healthStore.SamplePoint<healthFields.BloodPressure>

血压采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.BloodPressure](healthFields(运动健康数据字段).md#section757514113583)>

血压采样数据模型。

#### Bmx

type Bmx = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>

BMX自行车锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.CyclingSummary](healthFields(运动健康数据字段).md#section18131342132411), [healthFields.CyclingDetail](healthFields(运动健康数据字段).md#section1292902313238)>

BMX自行车锻炼记录数据模型。

#### BodyTemperature

type BodyTemperature = healthStore.SamplePoint<healthFields.BodyTemperature>

体温采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.BodyTemperature](healthFields(运动健康数据字段).md#section169357517159)>

体温采样数据模型。

#### BodyTemperatureAggregateRequest

type BodyTemperatureAggregateRequest = healthStore.AggregateRequest<healthFields.BodyTemperatureAggregation>

体温采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateRequest](healthStore(运动健康数据服务).md#section599483722019)<[healthFields.BodyTemperatureAggregation](healthFields(运动健康数据字段).md#section0126118114915)>

体温采样数据聚合统计请求模型。

#### BodyTemperatureAggregateResult

type BodyTemperatureAggregateResult = healthStore.AggregateResult<healthFields.BodyTemperatureAggregation>

体温聚合结果数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateResult](healthStore(运动健康数据服务).md#section19656142151412)<[healthFields.BodyTemperatureAggregation](healthFields(运动健康数据字段).md#section0126118114915)>

体温聚合结果数据模型。

#### BreathHoldingTest

type BreathHoldingTest = healthStore.ExerciseSequence<healthFields.BreathHoldingTestSummary, healthFields.BreathHoldingTestDetail>

闭气测试锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.BreathHoldingTestSummary](healthFields(运动健康数据字段).md#section12738114515162), [healthFields.BreathHoldingTestDetail](healthFields(运动健康数据字段).md#section187211129175913)>

闭气测试锻炼记录数据模型。

#### BreathHoldingTrain

type BreathHoldingTrain = healthStore.ExerciseSequence<healthFields.BreathHoldingTrainSummary, healthFields.BreathHoldingTrainDetail>

闭气训练锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.BreathHoldingTrainSummary](healthFields(运动健康数据字段).md#section12107151151615), [healthFields.BreathHoldingTrainDetail](healthFields(运动健康数据字段).md#section1169317427910)>

闭气训练锻炼记录数据模型。

#### Cycling

type Cycling = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>

户外骑行锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.CyclingSummary](healthFields(运动健康数据字段).md#section18131342132411), [healthFields.CyclingDetail](healthFields(运动健康数据字段).md#section1292902313238)>

户外骑行锻炼记录数据模型。

#### DailyActivities

type DailyActivities = healthStore.SamplePoint<healthFields.DailyActivities>

日常活动采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.DailyActivities](healthFields(运动健康数据字段).md#section19505904120)>

日常活动采样数据模型。

#### DailyActivitiesAggregateRequest

type DailyActivitiesAggregateRequest = healthStore.AggregateRequest<healthFields.DailyActivitiesAggregation>

日常活动采样数据聚合统计请求模型。

**元服务API**：从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateRequest](healthStore(运动健康数据服务).md#section599483722019)<[healthFields.DailyActivitiesAggregation](healthFields(运动健康数据字段).md#section21520371218)>

日常活动采样数据聚合统计请求模型。

#### DailyActivitiesAggregateResult

type DailyActivitiesAggregateResult = healthStore.AggregateResult<healthFields.DailyActivitiesAggregation>

日常活动聚合结果数据模型。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateResult](healthStore(运动健康数据服务).md#section19656142151412)<[healthFields.DailyActivitiesAggregation](healthFields(运动健康数据字段).md#section21520371218)>

日常活动聚合结果数据模型。

#### Diving

type Diving = healthStore.ExerciseSequence<healthFields.DivingSummary, healthFields.DivingDetail>

自由潜水锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.DivingSummary](healthFields(运动健康数据字段).md#section9861815141011), [healthFields.DivingDetail](healthFields(运动健康数据字段).md#section3831317111117)>

自由潜水锻炼记录数据模型。

#### Elliptical

type Elliptical = healthStore.ExerciseSequence<healthFields.EllipticalSummary, healthFields.EllipticalDetail>

椭圆机锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.EllipticalSummary](healthFields(运动健康数据字段).md#section161641514131415), [healthFields.EllipticalDetail](healthFields(运动健康数据字段).md#section593118391380)>

椭圆机锻炼记录数据模型。

#### Emotion

type Emotion = healthStore.SamplePoint<healthFields.Emotion>

情绪采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.Emotion](healthFields(运动健康数据字段).md#section19971754101817)>

情绪采样数据模型。

#### GolfCourseModel

type GolfCourseModel = healthStore.ExerciseSequence<healthFields.GolfCourseModelSummary, healthFields.GolfCourseModelDetail>

高尔夫场地模式锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.GolfCourseModelSummary](healthFields(运动健康数据字段).md#section639182623118), [healthFields.GolfCourseModelDetail](healthFields(运动健康数据字段).md#section2652134511912)>

高尔夫场地模式锻炼记录数据模型。

#### GolfPractice

type GolfPractice = healthStore.ExerciseSequence<healthFields.GolfPracticeSummary, healthFields.GolfPracticeDetail>

高尔夫练习场模式锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.GolfPracticeSummary](healthFields(运动健康数据字段).md#section10209195013439), [healthFields.GolfPracticeDetail](healthFields(运动健康数据字段).md#section16417153619382)>

高尔夫练习场模式锻炼记录数据模型。

#### HeartRate

type HeartRate = healthStore.SamplePoint<healthFields.HeartRate>

动态心率采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.HeartRate](healthFields(运动健康数据字段).md#section370919372088)>

动态心率采样数据模型。

#### HeartRateAggregateRequest

type HeartRateAggregateRequest = healthStore.AggregateRequest<healthFields.HeartRateAggregation>

动态心率采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateRequest](healthStore(运动健康数据服务).md#section599483722019)<[healthFields.HeartRateAggregation](healthFields(运动健康数据字段).md#section16703114311507)>

动态心率采样数据聚合统计请求模型。

#### HeartRateAggregateResult

type HeartRateAggregateResult = healthStore.AggregateResult<healthFields.HeartRateAggregation>

动态心率聚合结果数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateResult](healthStore(运动健康数据服务).md#section19656142151412)<[healthFields.HeartRateAggregation](healthFields(运动健康数据字段).md#section16703114311507)>

动态心率聚合结果数据模型。

#### HeartRateVariability

type HeartRateVariability = healthStore.SamplePoint<healthFields.HeartRateVariability>

心率变异性采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.HeartRateVariability](healthFields(运动健康数据字段).md#section19727135714284)>

心率变异性采样数据模型。

#### Height

type Height = healthStore.SamplePoint<healthFields.Height>

身高采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.Height](healthFields(运动健康数据字段).md#section8653722114617)>

身高采样数据模型。

#### Hiking

type Hiking = healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail>

徒步锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.WalkingSummary](healthFields(运动健康数据字段).md#section1532671232411), [healthFields.WalkingDetail](healthFields(运动健康数据字段).md#section57131952192319)>

徒步锻炼记录数据模型。

#### IndoorCycling

type IndoorCycling = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>

室内单车锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.CyclingSummary](healthFields(运动健康数据字段).md#section18131342132411), [healthFields.CyclingDetail](healthFields(运动健康数据字段).md#section1292902313238)>

室内单车锻炼记录数据模型。

#### IndoorRunning

type IndoorRunning = healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail>

室内跑步锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.RunningSummary](healthFields(运动健康数据字段).md#section13878173115011), [healthFields.RunningDetail](healthFields(运动健康数据字段).md#section8876931155019)>

室内跑步锻炼记录数据模型。

#### IndoorWalking

type IndoorWalking = healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail>

室内步行锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.WalkingSummary](healthFields(运动健康数据字段).md#section1532671232411), [healthFields.WalkingDetail](healthFields(运动健康数据字段).md#section57131952192319)>

室内步行锻炼记录数据模型。

#### JumpingRope

type JumpingRope = healthStore.ExerciseSequence<healthFields.JumpingRopeSummary, healthFields.JumpingRopeDetail>

跳绳锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.JumpingRopeSummary](healthFields(运动健康数据字段).md#section1247995013914), [healthFields.JumpingRopeDetail](healthFields(运动健康数据字段).md#section54772508914)>

跳绳锻炼记录数据模型。

#### MountainHike

type MountainHike = healthStore.ExerciseSequence<healthFields.MountainHikeSummary, healthFields.MountainHikeDetail>

登山锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.MountainHikeSummary](healthFields(运动健康数据字段).md#section173151241607), [healthFields.MountainHikeDetail](healthFields(运动健康数据字段).md#section74201810185820)>

登山锻炼记录数据模型。

#### OpenWaterSwim

type OpenWaterSwim = healthStore.ExerciseSequence<healthFields.OpenWaterSwimSummary, healthFields.OpenWaterSwimDetail>

开放水域游泳锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.OpenWaterSwimSummary](healthFields(运动健康数据字段).md#section6757113111619), [healthFields.OpenWaterSwimDetail](healthFields(运动健康数据字段).md#section1658118501949)>

开放水域游泳锻炼记录数据模型。

#### PoolSwim

type PoolSwim = healthStore.ExerciseSequence<healthFields.PoolSwimSummary, healthFields.PoolSwimDetail>

泳池游泳锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.PoolSwimSummary](healthFields(运动健康数据字段).md#section542225431315), [healthFields.PoolSwimDetail](healthFields(运动健康数据字段).md#section11261159108)>

泳池游泳锻炼记录数据模型。

#### RestingHeartRate

type RestingHeartRate = healthStore.SamplePoint<healthFields.RestingHeartRate>

静息心率采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.RestingHeartRate](healthFields(运动健康数据字段).md#section126714462018)>

静息心率采样数据模型。

#### RestingHeartRateAggregateRequest

type RestingHeartRateAggregateRequest = healthStore.AggregateRequest<healthFields.RestingHeartRateAggregation>

静息心率采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateRequest](healthStore(运动健康数据服务).md#section599483722019)<[healthFields.RestingHeartRateAggregation](healthFields(运动健康数据字段).md#section11821829192414)>

静息心率采样数据聚合统计请求模型。

#### RestingHeartRateAggregateResult

type RestingHeartRateAggregateResult = healthStore.AggregateResult<healthFields.RestingHeartRateAggregation>

静息心率聚合结果数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateResult](healthStore(运动健康数据服务).md#section19656142151412)<[healthFields.RestingHeartRateAggregation](healthFields(运动健康数据字段).md#section11821829192414)>

静息心率聚合结果数据模型。

#### Rower

type Rower = healthStore.ExerciseSequence<healthFields.RowerSummary, healthFields.RowerDetail>

划船机锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.RowerSummary](healthFields(运动健康数据字段).md#section1604202162518), [healthFields.RowerDetail](healthFields(运动健康数据字段).md#section958022142216)>

划船机锻炼记录数据模型。

#### Rowing

type Rowing = healthStore.ExerciseSequence<healthFields.RowingSummary, healthFields.RowingDetail>

赛艇锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.RowingSummary](healthFields(运动健康数据字段).md#section653019515312), [healthFields.RowingDetail](healthFields(运动健康数据字段).md#section4348954172819)>

赛艇锻炼记录数据模型。

#### Running

type Running = healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail>

户外跑步锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.RunningSummary](healthFields(运动健康数据字段).md#section13878173115011), [healthFields.RunningDetail](healthFields(运动健康数据字段).md#section8876931155019)>

户外跑步锻炼记录数据模型。

#### ScubaDiving

type ScubaDiving = healthStore.ExerciseSequence<healthFields.ScubaDivingSummary, healthFields.ScubaDivingDetail>

水肺潜水锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.ScubaDivingSummary](healthFields(运动健康数据字段).md#section318411033320), [healthFields.ScubaDivingDetail](healthFields(运动健康数据字段).md#section989110199238)>

水肺潜水锻炼记录数据模型。

#### Skiing

type Skiing = healthStore.ExerciseSequence<healthFields.SkiingSummary, healthFields.SkiingDetail>

滑雪锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.SkiingSummary](healthFields(运动健康数据字段).md#section37524095920), [healthFields.SkiingDetail](healthFields(运动健康数据字段).md#section1119141665514)>

滑雪锻炼记录数据模型。

#### SkinTemperature

type SkinTemperature = healthStore.SamplePoint<healthFields.SkinTemperature>

皮肤体温采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.SkinTemperature](healthFields(运动健康数据字段).md#section1987717196217)>

皮肤体温采样数据模型。

#### SkinTemperatureAggregateRequest

type SkinTemperatureAggregateRequest = healthStore.AggregateRequest<healthFields.SkinTemperatureAggregation>

皮肤体温采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateRequest](healthStore(运动健康数据服务).md#section599483722019)<[healthFields.SkinTemperatureAggregation](healthFields(运动健康数据字段).md#section140143554319)>

皮肤体温采样数据聚合统计请求模型。

#### SkinTemperatureAggregateResult

type SkinTemperatureAggregateResult = healthStore.AggregateResult<healthFields.SkinTemperatureAggregation>

皮肤体温聚合结果数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateResult](healthStore(运动健康数据服务).md#section19656142151412)<[healthFields.SkinTemperatureAggregation](healthFields(运动健康数据字段).md#section140143554319)>

皮肤体温聚合结果数据模型。

#### Sled

type Sled = healthStore.ExerciseSequence<healthFields.SledSummary, healthFields.SledDetail>

滑雪橇锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.SledSummary](healthFields(运动健康数据字段).md#section1652592714511), [healthFields.SledDetail](healthFields(运动健康数据字段).md#section14520143010413)>

滑雪橇锻炼记录数据模型。

#### SleepNapRecord

type SleepNapRecord = healthStore.HealthSequence<healthFields.SleepNap, healthFields.SleepDetail>

零星小睡健康记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.HealthSequence](healthStore(运动健康数据服务).md#section1038711561532)<[healthFields.SleepNap](healthFields(运动健康数据字段).md#section149051398168), [healthFields.SleepDetail](healthFields(运动健康数据字段).md#section16105838111514)>

零星小睡健康记录数据模型。

#### SleepRecord

type SleepRecord = healthStore.HealthSequence<healthFields.Sleep, healthFields.SleepDetail>

夜间睡眠健康记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.HealthSequence](healthStore(运动健康数据服务).md#section1038711561532)<[healthFields.Sleep](healthFields(运动健康数据字段).md#section11560114121214), [healthFields.SleepDetail](healthFields(运动健康数据字段).md#section16105838111514)>

夜间睡眠健康记录数据模型。

#### Snowboarding

type Snowboarding = healthStore.ExerciseSequence<healthFields.SnowboardingSummary, healthFields.SnowboardingDetail>

单板滑雪锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.SnowboardingSummary](healthFields(运动健康数据字段).md#section41271158985), [healthFields.SnowboardingDetail](healthFields(运动健康数据字段).md#section1593115514711)>

单板滑雪锻炼记录数据模型。

#### Spinning

type Spinning = healthStore.ExerciseSequence<healthFields.CyclingSummary, healthFields.CyclingDetail>

动感单车锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.CyclingSummary](healthFields(运动健康数据字段).md#section18131342132411), [healthFields.CyclingDetail](healthFields(运动健康数据字段).md#section1292902313238)>

动感单车锻炼记录数据模型。

#### Sports

type Sports = healthStore.ExerciseSequence<healthFields.SportsSummary, healthFields.SportsDetail>

通用锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.SportsSummary](healthFields(运动健康数据字段).md#section15586141212712), [healthFields.SportsDetail](healthFields(运动健康数据字段).md#section758116127273)>

通用锻炼记录数据模型。

#### Stress

type Stress = healthStore.SamplePoint<healthFields.Stress>

压力采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.Stress](healthFields(运动健康数据字段).md#section1199164115227)>

压力采样数据模型。

#### StressAggregateRequest

type StressAggregateRequest = healthStore.AggregateRequest<healthFields.StressAggregation>

压力采样数据聚合统计请求模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateRequest](healthStore(运动健康数据服务).md#section599483722019)<[healthFields.StressAggregation](healthFields(运动健康数据字段).md#section58707765616)>

压力采样数据聚合统计请求模型。

#### StressAggregateResult

type StressAggregateResult = healthStore.AggregateResult<healthFields.StressAggregation>

压力聚合结果数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.AggregateResult](healthStore(运动健康数据服务).md#section19656142151412)<[healthFields.StressAggregation](healthFields(运动健康数据字段).md#section58707765616)>

压力聚合结果数据模型。

#### TrailRunning

type TrailRunning = healthStore.ExerciseSequence<healthFields.RunningSummary, healthFields.RunningDetail>

越野跑锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.RunningSummary](healthFields(运动健康数据字段).md#section13878173115011), [healthFields.RunningDetail](healthFields(运动健康数据字段).md#section8876931155019)>

越野跑锻炼记录数据模型。

#### Walking

type Walking = healthStore.ExerciseSequence<healthFields.WalkingSummary, healthFields.WalkingDetail>

户外步行锻炼记录数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.ExerciseSequence](healthStore(运动健康数据服务).md#section17704373316)<[healthFields.WalkingSummary](healthFields(运动健康数据字段).md#section1532671232411), [healthFields.WalkingDetail](healthFields(运动健康数据字段).md#section57131952192319)>

户外步行锻炼数据模型记录。

#### Weight

type Weight = healthStore.SamplePoint<healthFields.Weight>

体重采样数据模型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

类型

**说明**

[healthStore.SamplePoint](healthStore(运动健康数据服务).md#section341712418323)<[healthFields.Weight](healthFields(运动健康数据字段).md#section1534182411503)>

体重采样数据模型。