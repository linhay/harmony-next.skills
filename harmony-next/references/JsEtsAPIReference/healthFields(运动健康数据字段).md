# healthFields(运动健康数据字段)

本模块提供运动健康数据字段列表。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { healthStore } from '@kit.HealthServiceKit';
```

此模块为healthStore子模块，需通过healthStore.healthFields方式使用。

#### AdventuresDetail

户外探险详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

markPoint

[MarkPoint](#section567919155513)[]

否

是

标记点采样详情列表，若未填写，默认为空。

altitude

[Altitude](#section271517115816)[]

否

是

海拔详情列表，若未填写，默认为空。

#### AdventuresSummary

户外探险统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

distance

[DistanceSummary](#section1931022758)

否

否

探险航点里程统计。

step

[StepSummary](#section1531683122019)

否

是

步数统计，若未填写，默认为空。

cadence

[CadenceSummary](#section517018141201)

否

是

步频统计，若未填写，默认为空。

altitude

[AltitudeSummary](#section5999164151119)

否

是

海拔统计，若未填写，默认为空。

#### Altitude

海拔详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

altitude

number

否

否

海拔。

单位：米

#### AltitudeSummary

海拔统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

max

number

否

否

最大值。

单位：米

min

number

否

否

最小值。

单位：米

avg

number

否

是

平均值，若未填写，默认为空。

单位：米

totalAscent

number

否

是

累计爬升，若未填写，默认为空。

单位：米

取值范围：[0, ∞)

totalDescent

number

否

是

累计下降，若未填写，默认为空。

单位：米

取值范围：[0, ∞)

#### BasketballDetail

篮球详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

jump

[Jump](#section2080454010485)[]

否

是

跳跃详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

#### BasketballFeature

篮球特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

overallScore

number

否

否

综合评分。

burstScore

number

否

是

爆发力得分，若未填写，默认为空。

jumpScore

number

否

是

弹跳滞空得分，若未填写，默认为空。

runScore

number

否

是

跑动得分，若未填写，默认为空。

breakthroughScore

number

否

是

突破移动得分，若未填写，默认为空。

sportIntensityScore

number

否

是

运动强度得分，若未填写，默认为空。

#### BasketballSummary

篮球统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

basketballFeature

[BasketballFeature](#section99689347364)

否

否

篮球特征数据。

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

jump

[JumpSummary](#section1775832805119)

否

否

跳跃统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

#### BiathlonDetail

冬季两项详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

#### BiathlonSummary

冬季两项统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

#### BloodOxygenSaturation

血氧采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

spo2

number

否

否

血氧饱和度。

单位：百分比

取值范围：(0, 100]。

#### BloodOxygenSaturationAggregation

血氧聚合统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

spo2

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'sum' | 'count'>

否

否

血氧饱和度聚合统计。

#### BloodPressure

血压采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

bloodPressureSystolic

number

否

否

收缩压，即高压。

单位：mmHg

取值范围： (0, ∞)

bloodPressureDiastolic

number

否

否

舒张压，即低压。

单位：mmHg

取值范围： (0, ∞)

sphygmus

number

否

是

脉搏，若未填写，默认为空。

单位：次/分钟

取值范围： (0, ∞)

measurementAnomalyFlag

number

否

是

测量异常事件，若未填写，默认为空。

取值范围： (0, ∞)

取值参考如下：

1：正常

2：测量时未和心脏平齐

3：测量时有轻微抖动

4：测量前没有至少5min休息

beforeMeasureActivity

number

否

是

测量前活动，若未填写，默认为空。

取值范围： (0, ∞)

取值参考如下：

1：剧烈运动

2：吸烟

3：进食

4：饮酒

5：喝咖啡

6：无活动

7：起床后

8：睡前

100：自定义

#### BodyTemperature

体温采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

bodyTemperature

number

否

否

体温。

单位：摄氏度

取值范围：[34, 42]。

#### BodyTemperatureAggregation

体温聚合统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

bodyTemperature

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'sum' | 'last'>

否

否

体温聚合统计。

#### BreathHoldingTestDetail

闭气测试详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

#### BreathHoldingTestFeature

闭气测试特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

diaphragmTime

number

否

否

横膈膜打点时间。

单位：秒

#### BreathHoldingTestSummary

闭气测试统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

breathHoldingTestFeature

[BreathHoldingTestFeature](#section236115121419)

否

否

闭气测试特征统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

#### BreathHoldingTrainDetail

闭气训练详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

#### BreathHoldingTrainFeature

闭气训练特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

breathTime

number

否

否

呼吸时间。

单位：秒

breathHoldingTime

number

否

否

闭气时间。

单位：秒

breathHoldingTrainRhythm

number

否

是

闭气训练节奏数，若未填写，默认为空。

单位：次

#### BreathHoldingTrainSummary

闭气训练统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

breathHoldingTrainFeature

[BreathHoldingTrainFeature](#section1359857181417)

否

否

闭气训练特征统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

#### Cadence

步频详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

cadence

number

否

否

步频。

单位：步数/分钟

取值范围：[0, ∞)

#### CadenceSummary

步频统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

单位：步数/分钟

取值范围：[0, ∞)

max

number

否

否

最大值。

单位：步数/分钟

取值范围：[0, ∞)

min

number

否

是

最小值，若未填写，默认为空。

单位：步数/分钟

取值范围：[0, ∞)

#### CalorieSummary

卡路里统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

totalCalories

number

否

否

卡路里总和。

单位：卡

取值范围：(0, ∞)

#### CyclingDetail

骑行详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

pedalingCadence

[PedalingCadence](#section15378151813915)[]

否

是

踏频详情列表，若未填写，默认为空。

power

[Power](#section154582103406)[]

否

是

功率详情列表，若未填写，默认为空。

location

[Location](#section1970034063415)[]

否

是

位置详情列表，若未填写，默认为空。

altitude

[Altitude](#section271517115816)[]

否

是

海拔详情列表，若未填写，默认为空。

resistance

[Resistance](#section17695193744217)[]

否

是

阻力详情列表，若未填写，默认为空。

#### CyclingSummary

骑行统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

distance

[DistanceSummary](healthFields(运动健康数据字段).md#section1931022758)

否

否

距离统计。

calorie

[CalorieSummary](#section10820034172215)

否

否

热量统计。

speed

[SpeedSummary](#section4460144920180)

否

否

速度统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

resistance

[ResistanceSummary](#section969783754212)

否

是

阻力统计，若未填写，默认为空。

pedalingCadence

[PedalingCadenceSummary](#section17379171873917)

否

是

踏频统计，若未填写，默认为空。

power

[PowerSummary](#section6460410194012)

否

是

功率统计，若未填写，默认为空。

altitude

[AltitudeSummary](#section5999164151119)

否

是

海拔统计，若未填写，默认为空。

location

[LocationSummary](#section20701154013341)

否

是

位置统计，若未填写，默认为空。

#### DailyActivities

日常活动采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

step

number

否

否

步数。

单位：步

取值范围：[0, 500)

calorie

number

否

否

热量。

单位：卡

取值范围：[0, 65536)

distance

number

否

否

距离。

单位：米

取值范围：[0, ∞)

duration

number

否

是

时长，若未填写，默认为空。

单位：分钟

取值范围：0 或 1

status

number

否

是

状态（走、跑、骑、爬等），若未填写，默认为空。

取值范围：

2： 登山

3： 骑行

4： 跑步

5：走路

9：游泳

10：健身

13：站立

isIntensity

number

否

是

是否中高强度，若未填写，默认为空。

取值范围：

0：否

1：是

climbHighAltitude

number

否

是

爬高海拔差（支持正负），若未填写，默认为空。

单位：米

isStand

number

否

是

是否站立（一个小时有活动记录，就标志这个小时的第一分钟为1），若未填写，默认为空。

取值范围：

0：否

1：是

#### DailyActivitiesAggregation

日常活动聚合统计数据字段列表。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

step

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'max' | 'min' | 'avg' | 'last' | 'count'>

否

否

步数聚合统计。

calorie

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'max' | 'min' | 'avg' | 'last' | 'count'>

否

否

卡路里聚合统计。

distance

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'max' | 'min' | 'avg' | 'last' | 'count'>

否

否

距离聚合统计。

climbHighAltitude

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'max' | 'min' | 'avg' | 'last' | 'count'>

否

否

爬高海拔差聚合统计。

isIntensity

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'max' | 'min' | 'avg' | 'last' | 'count'>

否

否

中高强度聚合统计。

isStand

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'max' | 'min' | 'avg' | 'last' | 'count'>

否

否

站立聚合统计。

#### DistanceSummary

距离统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

totalDistance

number

否

否

距离统计。

单位：米

取值范围：(0, ∞)

#### DivingDepth

潜水深度详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

depth

number

否

否

潜水深度。

单位：米

#### DivingDepthSummary

潜水深度统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

单位：米

取值范围：[0, ∞)

max

number

否

否

最大值。

单位：米

取值范围：[0, ∞)

#### DivingDetail

自由潜水详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

divingDepth

[DivingDepth](#section1089615015267)[]

否

是

潜水深度详情列表，若未填写，默认为空。

waterTemperature

[WaterTemperature](#section8976102914494)[]

否

是

水温详情列表，若未填写，默认为空。

#### DivingFeature

自由潜水特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

divingTime

number

否

否

潜水时间。

单位：秒

divingCount

number

否

否

潜水次数。

divingMode

number

否

否

潜水模式。

取值参考如下：

0：自由潜水

1：休闲水肺潜水

2：技术水肺潜水

3：仪表潜水

maxUnderwaterTime

number

否

是

单次水下最长时间，若未填写，默认为空。

单位：秒

underwaterTime

number

否

是

水下时间，若未填写，默认为空。

单位：秒

noFlyTime

number

否

是

禁飞时间，若未填写，默认为空。

单位：小时

waterType

number

否

是

水体类型，若未填写，默认为空。

取值参考如下：

0：自定义

1：淡水

2：海水

waterDensity

number

否

是

水密度，若未填写，默认为空。

单位：千克/升

maxAscentSpeed

number

否

是

最大上升速度，若未填写，默认为空。

单位：米/秒

maxDescentSpeed

number

否

是

最大下降速度，若未填写，默认为空。

单位：米/秒

#### DivingSummary

自由潜水统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

divingFeature

[DivingFeature](#section141695571417)

否

否

自由潜水特征数据。

location

[LocationSummary](#section20701154013341)

否

是

位置统计，若未填写，默认为空。

divingDepth

[DivingDepthSummary](#section10170184225917)

否

是

潜水深度统计，若未填写，默认为空。

waterTemperature

[WaterTemperatureSummary](#section16704161419471)

否

是

水温统计，若未填写，默认为空。

#### EllipticalDetail

椭圆机详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

pedalingCadence

[PedalingCadence](#section15378151813915)[]

否

是

脚踏节奏详情列表，若未填写，默认为空。

power

[Power](#section154582103406)[]

否

是

功率详情列表，若未填写，默认为空。

cadence

[Cadence[]](#section625153911153)

否

是

步频详情列表，若未填写，默认为空。

#### EllipticalSummary

椭圆机统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

distance

[DistanceSummary](#section1931022758)

否

是

距离统计，若未填写，默认为空。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

speed

[SpeedSummary](#section4460144920180)

否

是

速度统计，若未填写，默认为空。

step

[StepSummary](#section1531683122019)

否

是

步数统计，若未填写，默认为空。

cadence

[CadenceSummary](#section517018141201)

否

是

步频统计，若未填写，默认为空。

resistance

[ResistanceSummary](#section969783754212)

否

是

阻力统计，若未填写，默认为空。

pedalingCadence

[PedalingCadenceSummary](#section17379171873917)

否

是

脚踏节奏统计，若未填写，默认为空。

power

[PowerSummary](#section6460410194012)

否

是

功率统计，若未填写，默认为空。

#### Emotion

情绪采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

**名称**

**类型**

只读

可选

**说明**

emotionStatus

number

否

否

情绪状态。

取值范围：[0, 100)

当前运动健康App仅展示以下值：

1：不愉悦

2：平静

3：愉悦

#### ExerciseHeartRate

运动心率详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

bpm

number

否

否

运动心率详情。

单位：次/分钟

取值范围：(0, 255)

#### ExerciseHeartRateSummary

运动心率统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

单位：次/分钟

取值范围：[0, ∞)

max

number

否

否

最大值。

单位：次/分钟

取值范围：[0, ∞)

min

number

否

是

最小值，若未填写，默认为空。

单位：次/分钟

取值范围：[0, ∞)

#### GolfCourseModelDetail

高尔夫场地模式详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

altitude

[Altitude](#section271517115816)[]

否

是

海拔详情列表，若未填写，默认为空。

#### GolfCourseModelFeature

高尔夫场地模式特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

golfSwingCount

number

否

否

总挥杆数。

courseId

number

否

否

球场名称id。

holes

number

否

否

球洞个数。

branchId1

number

否

是

上半场分层id，若未填写，默认为空。

branchId2

number

否

是

下半场分层id，若未填写，默认为空。

gir

number

否

是

上果岭率，若未填写，默认为空。

doubleEagle

number

否

是

信天翁，若未填写，默认为空。

eagle

number

否

是

老鹰球，若未填写，默认为空。

birdie

number

否

是

小鸟球，若未填写，默认为空。

par

number

否

是

标准杆，若未填写，默认为空。

bogey

number

否

是

柏忌，若未填写，默认为空。

doubleBogey

number

否

是

双柏忌，若未填写，默认为空。

putts

number

否

是

总推杆，若未填写，默认为空。

avgPutts

number

否

是

平均推杆，若未填写，默认为空。

par3

number

否

是

标准3杆洞平均杆，若未填写，默认为空。

par4

number

否

是

标准4杆洞平均杆，若未填写，默认为空。

par5

number

否

是

标准5杆洞平均杆，若未填写，默认为空。

fairwayHits

number

否

是

球道命中数，若未填写，默认为空。

fairwayLeft

number

否

是

球道左曲数，若未填写，默认为空。

fairwayRight

number

否

是

球道右曲数，若未填写，默认为空。

avgHandicap

number

否

是

平均杆差，若未填写，默认为空。

bestHandicap

number

否

是

最佳杆差，若未填写，默认为空。

totalHandicap

number

否

是

总杆差，若未填写，默认为空。

#### GolfCourseModelSummary

高尔夫场地模式统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

golfCourseModelFeature

[GolfCourseModelFeature](#section192811952216)

否

否

高尔夫场地模式特征数据。

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

step

[StepSummary](#section1531683122019)

否

否

步数统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

distance

[DistanceSummary](#section1931022758)

否

是

距离统计，若未填写，默认为空。

cadence

[CadenceSummary](#section517018141201)

否

是

步频统计，若未填写，默认为空。

altitude

[AltitudeSummary](#section5999164151119)

否

是

海拔统计，若未填写，默认为空。

#### GolfPracticeDetail

高尔夫练习场模式详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

#### GolfPracticeFeature

高尔夫练习场模式特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

golfSwingCount

number

否

否

总挥杆数。

golfSwingSpeed

number

否

是

平均挥杆速度，若未填写，默认为空。

单位：厘米/秒

golfMaxSwingSpeed

number

否

是

最大挥杆速度，若未填写，默认为空。

单位：厘米/秒

golfSwingTempo

number

否

是

平均挥杆节奏（平均上杆时间/平均下杆时间），若未填写，默认为空。

golfDownSwingTime

number

否

是

平均下杆时间，若未填写，默认为空。

单位：毫秒

golfBackSwingTime

number

否

是

平均上杆时间，若未填写，默认为空。

单位：毫秒

#### GolfPracticeSummary

高尔夫练习场模式统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

golfPracticeFeature

[GolfPracticeFeature](#section1940192124016)

否

否

高尔夫练习场模式特征数据。

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

#### HeartRate

动态心率采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

bpm

number

否

否

动态心率。

单位：次/分钟

取值范围：[0, ∞)

#### HeartRateAggregation

动态心率聚合统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

bpm

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'avg' | 'sum' | 'count'>

否

否

动态心率聚合统计。

#### HeartRateVariability

心率变异性采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

**名称**

**类型**

只读

可选

**说明**

heartRateVariabilityRMSSD

number

否

否

心率变异性。

单位：毫秒

取值范围：(0, 200]

#### Height

身高采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

height

number

否

否

身高。

单位：厘米

#### Jump

跳跃详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

jumpHeight

number

否

否

纵跃高度。

单位：米

passageDuration

number

否

否

滞空时间。

单位：毫秒

#### JumpingRopeDetail

跳绳详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

skipSpeed

[SkipSpeed](#section22171238115)[]

否

是

跳跃速度详情列表，若未填写，默认为空。

#### JumpingRopeFeature

跳绳特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

skipNum

number

否

否

跳绳个数。

取值范围：[0, ∞)

interruptions

number

否

是

中断次数，若未填写，默认为空。

取值范围：[0, ∞)

longestStreak

number

否

是

最多连跳，若未填写，默认为空。

取值范围：[0, ∞)

doubleUnders

number

否

是

双摇个数，若未填写，默认为空。

取值范围：[0, ∞)

tripleUnders

number

否

是

三摇个数，若未填写，默认为空。

取值范围：[0, ∞)

#### JumpingRopeSummary

跳绳统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

jumpingRopeFeature

[JumpingRopeFeature](#section584042781213)

否

否

跳绳特征数据。

calorie

[CalorieSummary](#section10820034172215)

否

否

热量统计。

skipSpeed

[SkipSpeedSummary](#section162181823141115)

否

否

跳跃速度统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

#### JumpSummary

跳跃统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

jumpTimes

number

否

否

跳跃次数。

maxJumpHeight

number

否

是

最大跳跃高度，若未填写，默认为空。

单位：米

maxPassageDuration

number

否

是

最大滞空时间，若未填写，默认为空。

单位：毫秒

#### Location

位置详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

latitude

number

否

否

纬度。

单位：度

取值范围：[-90, 90]

longitude

number

否

否

经度。

单位：度

取值范围：[-180, 180]

#### LocationSummary

位置统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

coordinate

string

否

否

坐标系。

取值参考如下：

'GCJ02'

'WGS84'

'BD09'

startLat

number

否

是

起始点纬度，若未填写，默认为空。

单位：度

取值范围：[-90, 90]

endLat

number

否

是

结束点纬度，若未填写，默认为空。

单位：度

取值范围：[-90, 90]

startLon

number

否

是

起始点经度，若未填写，默认为空。

单位：度

取值范围：[-180, 180]

endLon

number

否

是

结束点经度，若未填写，默认为空。

单位：度

取值范围：[-180, 180]

#### MarkPoint

标记点采样数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

sn

number

否

否

序号。

type

number

否

否

标记点类型。

取值参考如下：

0：通用

1：起始

2：营地

3：向左

4：向右

5：直行

6：危险

7：野兽

8：医疗

9：水流

10：补给

11：桥梁

12：避险

13：山顶

14：房屋

254：终点

255：自动标记点

longitude

number

否

否

经度。

单位：度

latitude

number

否

否

纬度。

单位：度

mode

number

否

否

标记方式。

取值参考如下：

0：自动

1：手动

color

number

否

是

颜色，若未填写，默认为空。

取值参考如下：

0：橙色

1：红色

2：蓝色

3：黄色

4：灰色

5：绿色

255：自动标记点颜色

#### MountainHikeDetail

登山详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

location

[Location](#section1970034063415)[]

否

是

位置详情列表，若未填写，默认为空。

altitude

[Altitude](#section271517115816)[]

否

是

海拔详情列表，若未填写，默认为空。

#### MountainHikeSummary

登山统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

distance

[DistanceSummary](#section1931022758)

否

否

距离统计。

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

step

[StepSummary](#section1531683122019)

否

是

步数统计，若未填写，默认为空。

altitude

[AltitudeSummary](#section5999164151119)

否

是

海拔统计，若未填写，默认为空。

#### OpenWaterSwimDetail

开放水域游泳详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

location

[Location](#section1970034063415)[]

否

是

位置详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

swimStrokeRate

[SwimStrokeRate](#section19131136178)[]

否

是

划水频率详情列表，若未填写，默认为空。

swolf

[Swolf](#section8730142115192)[]

否

是

SWOLF详情列表，若未填写，默认为空。

#### OpenWaterSwimFeature

开放水域游泳特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

pullTimes

number

否

否

划水次数。

swimmingStroke

number

否

是

主泳姿，若未填写，默认为空。

取值参考如下：

1：蛙泳

2：自由泳

3：蝶泳

4：仰泳

5：混合泳

#### OpenWaterSwimSummary

开放水域游泳统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

openWaterSwimFeature

[OpenWaterSwimFeature](#section16771166230)

否

否

开放水域游泳特征数据。

distance

[DistanceSummary](#section1931022758)

否

否

距离统计。

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

swimStrokeRate

[SwimStrokeRateSummary](#section2087653613188)

否

是

划水频率统计，若未填写，默认为空。

swolf

[SwolfSummary](#section4125715154316)

否

是

SWOLF统计，若未填写，默认为空。

#### PedalingCadence

踏频详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

rpm

number

否

否

踏频详情。

单位：转/分钟

取值范围：[0, ∞)

#### PedalingCadenceSummary

踏频统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

单位：转/分钟

取值范围：[0, ∞)

max

number

否

否

最大值。

单位：转/分钟

取值范围：[0, ∞)

min

number

否

是

最小值，若未填写，默认为空。

单位：转/分钟

取值范围：[0, ∞)

#### PoolSwimDetail

泳池游泳详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

swimStrokeRate

[SwimStrokeRate](#section19131136178)[]

否

是

划水频率详情列表，若未填写，默认为空。

swolf

[Swolf](#section8730142115192)[]

否

是

SWOLF详情列表，若未填写，默认为空。

#### PoolSwimFeature

泳池游泳特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

pullTimes

number

否

否

划水次数。

tripTimes

number

否

否

趟数。

poolLength

number

否

是

泳池长度，若未填写，默认为空。

单位：米

swimmingStroke

number

否

是

主泳姿，若未填写，默认为空。

取值参考如下：

1：蛙泳

2：自由泳

3：蝶泳

4：仰泳

5：混合泳

#### PoolSwimSummary

泳池游泳统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

poolSwimFeature

[PoolSwimFeature](#section11868111541212)

否

否

泳池游泳特征数据。

distance

[DistanceSummary](#section1931022758)

否

否

距离统计。

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

speed

[SpeedSummary](#section4460144920180)

否

是

速度统计，若未填写，默认为空。

swimStrokeRate

[SwimStrokeRateSummary](#section2087653613188)

否

是

划水频率统计，若未填写，默认为空。

swolf

[SwolfSummary](#section4125715154316)

否

是

SWOLF统计，若未填写，默认为空。

#### Power

功率详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

power

number

否

否

功率详情。

单位：瓦

取值范围：[0, ∞)

#### PowerSummary

功率统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

单位：瓦

取值范围：[0, ∞)

max

number

否

否

最大值。

单位：瓦

取值范围：[0, ∞)

min

number

否

是

最小值，若未填写，默认为空。

单位：瓦

取值范围：[0, ∞)

#### QuantitySummary

统计基类数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

取值范围：[0, ∞)

max

number

否

否

最大值。

取值范围：[0, ∞)

min

number

否

是

最小值，若未填写，默认为空。

取值范围：[0, ∞)

#### Resistance

阻力详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

resLevel

number

否

否

阻力等级。

取值范围：[1, 100]

#### ResistanceSummary

阻力统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

resLv1LowerLimit

number

否

否

阻力区间1下限。

取值范围：[1, 100]

resLv2LowerLimit

number

否

否

阻力区间2下限。

取值范围：[1, 100]

resLv3LowerLimit

number

否

否

阻力区间3下限。

取值范围：[1, 100]

resLv4LowerLimit

number

否

否

阻力区间4下限。

取值范围：[1, 100]

resLv5LowerLimit

number

否

否

阻力区间5下限。

取值范围：[1, 100]

resLv5UpperLimit

number

否

否

阻力区间5上限。

取值范围：[1, 100]

resLv1Duration

number

否

否

在阻力区间1内运动时长。

单位：分钟

取值范围：[0, ∞)

resLv2Duration

number

否

否

在阻力区间2内运动时长。

单位：分钟

取值范围：[0, ∞)

resLv3Duration

number

否

否

在阻力区间3内运动时长。

单位：分钟

取值范围：[0, ∞)

resLv4Duration

number

否

否

在阻力区间4内运动时长。

单位：分钟

取值范围：[0, ∞)

resLv5Duration

number

否

否

在阻力区间5内运动时长。

单位：分钟

取值范围：[0, ∞)

maxRes

number

否

是

设备可设置的最大阻力级别，若未填写，默认为空。

取值范围：[1, 100]

minRes

number

否

是

设备可设置的最小阻力级别，若未填写，默认为空。

取值范围：[1, 100]

#### RestingHeartRate

静息心率数据字段列表.

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

restBpm

number

否

否

静息心率。

单位：次/分钟

取值范围：[0, ∞)

#### RestingHeartRateAggregation

静息心率聚合统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

restBpm

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'sum' | 'count' | 'max' | 'min' | 'avg'>

否

否

静息心率聚合统计。

#### RowerDetail

划船机详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

power

[Power](#section154582103406)[]

否

是

功率详情列表，若未填写，默认为空。

resistance

[Resistance](#section17695193744217)[]

否

是

阻力详情列表，若未填写，默认为空。

strokeRate

[StrokeRate](#section20396141712117)[]

否

是

桨频详情列表，若未填写，默认为空。

#### RowerFeature

划船机特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

strokesNum

number

否

否

累计桨次。

#### RowerSummary

划船机统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

rowerFeature

[RowerFeature](#section13153171111333)

否

否

划船机特征数据。

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

distance

[DistanceSummary](#section1931022758)

否

是

距离统计，若未填写，默认为空。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

speed

[SpeedSummary](#section4460144920180)

否

是

速度统计，若未填写，默认为空。

resistance

[ResistanceSummary](#section969783754212)

否

是

阻力统计，若未填写，默认为空。

power

[PowerSummary](#section6460410194012)

否

是

功率统计，若未填写，默认为空。

strokeRate

[StrokeRateSummary](#section167731953151312)

否

是

桨频统计，若未填写，默认为空。

#### RowingDetail

赛艇详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

strokeRate

[StrokeRate](#section20396141712117)[]

否

是

桨频详情列表，若未填写，默认为空。

#### RowingFeature

赛艇特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

strokesNum

number

否

否

累计桨次。

#### RowingSummary

赛艇统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

rowingFeature

[RowingFeature](#section45351858172920)

否

否

赛艇特征数据。

calorie

[CalorieSummary](#section10820034172215)

否

否

卡路里统计。

distance

[DistanceSummary](#section1931022758)

否

是

距离统计，若未填写，默认为空。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

strokeRate

[StrokeRateSummary](#section167731953151312)

否

是

桨频统计，若未填写，默认为空。

#### RunningDetail

跑步详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

cadence

[Cadence](#section625153911153)[]

否

是

步频详情列表，若未填写，默认为空。

runningForm

[RunningForm](#section1668116459594)[]

否

是

跑姿详情列表，若未填写，默认为空。

location

[Location](#section1970034063415)[]

否

是

位置详情列表，若未填写，默认为空。

altitude

[Altitude](#section271517115816)[]

否

是

海拔详情列表，若未填写，默认为空。

#### RunningFeature

跑步特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avgPace

number

否

否

平均配速。

取值范围：[0, ∞)

单位：秒/公里

bestPace

number

否

否

最快配速。

取值范围：[0, ∞)

单位：秒/公里

paceMap

[healthStore.PaceValueType](healthStore(运动健康数据服务).md#section1842384565915)

否

是

每公里的配速，若未填写，默认为空。单位：秒/公里

例如

'1.0':407.945

'2.0':473.98846

'2.170':473.98846

最后不满一公里的部分，按比例换算为整公里的配速存入。

partTimeMap

[healthStore.PaceValueType](healthStore(运动健康数据服务).md#section1842384565915)

否

是

公制分段数据表（key：公里，value：秒），若未填写，默认为空。

其中公里保留到小数点后4位。

Value是一个累积到当前公里的时间如：

- '1.0':3.0
- '2.0':6.0

- '3.0':9.0
- '21.0975':7020.0

- '42.195':18000.0

其中，21.0975，42.195分别为半马和全马的距离（仅半马全马key值小数点后不为0）。

#### RunningForm

跑姿详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

groundContactTime

number

否

否

触地时间。

单位：毫秒

取值范围：[0, 5000]

groundImpactAcceleration

number

否

是

着地冲击，若未填写，默认为空。

单位：g（重力加速度）

取值范围：[0, 50]

swingAngle

number

否

是

摆动角度，若未填写，默认为空。

单位：度

取值范围：[0, 360]

eversionExcursion

number

否

是

外翻幅度，若未填写，默认为空。

单位：度

取值范围：[-100, 100]

hangTime

number

否

是

腾空时间，若未填写，默认为空。

单位：毫秒

取值范围：[0, 500]

groundHangTimeRate

number

否

是

触地腾空比，若未填写，默认为空。

取值范围：[0, 500]

foreFootStrikePattern

number

否

是

触地方式中的前脚掌触地次数，若未填写，默认为空。

取值范围：[0, 100]

hindFootStrikePattern

number

否

是

触地方式中的后脚掌触地次数，若未填写，默认为空。

取值范围：[0, 100]

wholeFootStrikePattern

number

否

是

触地方式中的全脚掌触地次数，若未填写，默认为空。

取值范围：[0, 100]

impactPeak

number

否

是

触地峰值，若未填写，默认为空。

单位：BW（体重倍数）

取值范围：[0, 10]

verticalOscillation

number

否

是

垂直振幅，若未填写，默认为空。

单位：厘米

取值范围：[0, 25.6]

verticalRatio

number

否

是

垂直步幅比，若未填写，默认为空。

单位：百分比

取值范围：[0, 100]

gcTimeBalance

number

否

是

左右触地平衡，若未填写，默认为空。

单位：百分比（返回数据为左脚的触地平衡，右脚需自行计算，二者之和为100%）

取值范围：[0, 100]

#### RunningFormSummary

跑姿统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avgGroundContactTime

number

否

否

平均触地时间。

单位：毫秒

取值范围：[0, 5000]

avgGroundImpactAcceleration

number

否

是

平均着地冲击，若未填写，默认为空。

单位：g（重力加速度）

avgSwingAngle

number

否

是

平均摆动角度，若未填写，默认为空。

单位：度

avgEversionExcursion

number

否

是

平均外翻幅度，若未填写，默认为空。

单位：度

avgHangTime

number

否

是

平均腾空时间，若未填写，默认为空。

单位：毫秒

avgGroundHangTimeRate

number

否

是

平均触地腾空比，若未填写，默认为空。

foreFootStrikePattern

number

否

是

触地方式中的前脚掌触地次数，若未填写，默认为空。

hindFootStrikePattern

number

否

是

触地方式中的后脚掌触地次数，若未填写，默认为空。

wholeFootStrikePattern

number

否

是

触地方式中的全脚掌触地次数，若未填写，默认为空。

avgImpactPeak

number

否

是

平均触地峰值，若未填写，默认为空。

单位：BW（体重倍数）

avgVerticalImpactRate

number

否

是

平均冲击负载率，若未填写，默认为空。

单位：BW/S

avgVerticalOscillation

number

否

是

平均垂直振幅，若未填写，默认为空。

单位：厘米

avgVerticalRatio

number

否

是

平均垂直步幅比，若未填写，默认为空。

单位：百分比

avgGcTimeBalance

number

否

是

平均左右触地平衡，若未填写，默认为空。

单位：百分比（返回数据为左脚的触地平衡，右脚需自行计算，二者之和为100%）

#### RunningSummary

跑步统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

distance

[DistanceSummary](healthFields(运动健康数据字段).md#section1931022758)

否

否

距离统计。

calorie

[CalorieSummary](#section10820034172215)

否

否

热量统计。

speed

[SpeedSummary](#section4460144920180)

否

否

速度统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

step

[StepSummary](#section1531683122019)

否

是

步数统计，若未填写，默认为空。

cadence

[CadenceSummary](#section517018141201)

否

是

步频统计，若未填写，默认为空。

altitude

[AltitudeSummary](#section5999164151119)

否

是

海拔统计，若未填写，默认为空。

location

[LocationSummary](#section20701154013341)

否

是

位置统计，若未填写，默认为空。

runningForm

[RunningFormSummary](#section09431418413)

否

是

跑姿统计，若未填写，默认为空。

runningFeature

[RunningFeature](#section543218206545)

否

是

跑步特征数据，若未填写，默认为空。

#### ScubaDivingDetail

水肺潜水详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

divingDepth

[DivingDepth](#section1089615015267)[]

否

是

潜水深度详情列表，若未填写，默认为空。

waterTemperature

[WaterTemperature](#section8976102914494)[]

否

是

水温详情列表，若未填写，默认为空。

#### ScubaDivingFeature

水肺潜水特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

divingTime

number

否

否

潜水时间。

单位：秒

divingCount

number

否

否

潜水次数。

divingMode

number

否

否

潜水模式。

取值参考如下：

0：自由潜水

1：休闲水肺潜水

2：技术水肺潜水

3：仪表潜水

maxUnderwaterTime

number

否

是

单次水下最长时间，若未填写，默认为空。

单位：秒

underwaterTime

number

否

是

水下时间，若未填写，默认为空。

单位：秒

noFlyTime

number

否

是

禁飞时间，若未填写，默认为空。

单位：小时

cns

number

否

是

CNS(中枢神经系统毒性等级)，若未填写，默认为空。

等级：

一：0%-79%

二：80%-99%

三：大于等于100%

otu

number

否

是

OTU(氧气毒性单元)，若未填写，默认为空。

等级：

一：0-249

二：250-299

三：大于等于300

waterType

number

否

是

水体类型，若未填写，默认为空。

取值参考如下：

0：自定义

1：淡水

2：海水

waterDensity

number

否

是

水密度，若未填写，默认为空。

单位：千克/升

maxAscentSpeed

number

否

是

最大上升速度，若未填写，默认为空。

单位：米/秒

maxDescentSpeed

number

否

是

最大下降速度，若未填写，默认为空。

单位：米/秒

#### ScubaDivingSummary

水肺潜水统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

scubaDivingFeature

[ScubaDivingFeature](#section1968101417267)

否

否

水肺潜水特征数据。

location

[LocationSummary](#section20701154013341)

否

是

位置统计，若未填写，默认为空。

divingDepth

[DivingDepthSummary](#section10170184225917)

否

是

潜水深度统计，若未填写，默认为空。

waterTemperature

[WaterTemperatureSummary](#section16704161419471)

否

是

水温统计，若未填写，默认为空。

#### SkiingDetail

滑雪详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

location

[Location](#section1970034063415)[]

否

是

位置详情列表，若未填写，默认为空。

altitude

[Altitude](#section271517115816)[]

否

是

海拔详情列表，若未填写，默认为空。

#### SkiingFeature

滑雪特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

tripTimes

number

否

否

趟数。

maxSlopePercent

number

否

是

滑雪最大坡度百分比，若未填写，默认为空。

maxSlopeDegree

number

否

是

滑雪最大坡，若未填写，默认为空。

单位：度

totalTime

number

否

是

滑行时间，若未填写，默认为空。

单位：毫秒

totalDistance

number

否

是

滑行距离，若未填写，默认为空。

单位：米

#### SkiingSummary

滑雪统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

distance

[DistanceSummary](#section1931022758)

否

否

距离统计。

calorie

[CalorieSummary](#section10820034172215)

否

否

热量统计。

skiingFeature

[SkiingFeature](#section13822749155616)

否

否

滑雪特征数据。

altitude

[AltitudeSummary](#section5999164151119)

否

是

海拔统计，若未填写，默认为空。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

#### SkinTemperature

皮肤体温详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

skinTemperature

number

否

否

皮肤温度。

单位：摄氏度

取值范围：[20, 42]

#### SkinTemperatureAggregation

皮肤体温聚合统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

skinTemperature

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'sum' | 'last'>

否

否

皮肤体温聚合统计。

#### SkipSpeed

跳绳速度详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

skipSpeed

number

否

否

跳绳速度详情。

单位：个/分钟

取值范围：[0, ∞)

#### SkipSpeedSummary

跳绳速度统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

单位：个/分钟

取值范围：[0, ∞)

max

number

否

否

最大值。

单位：个/分钟

取值范围：[0, ∞)

min

number

否

是

最小值，若未填写，默认为空。

单位：个/分钟

取值范围：[0, ∞)

#### SledDetail

滑雪橇详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

#### SledSummary

滑雪橇统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

calorie

[CalorieSummary](#section10820034172215)

否

否

热量统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

#### Sleep

夜间睡眠数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

fallAsleepTime

number

否

否

分期睡眠最早入睡时间点。

单位：毫秒

取值范围：[0, ∞)

wakeupTime

number

否

否

分期睡眠最晚出睡时间点。

单位：毫秒

取值范围：[0, ∞)

duration

number

否

否

夜间/普通睡眠时长（不含零星小睡时长）。

单位：秒

取值范围：[0, ∞)

bedTime

number

否

是

最早上床时间点，若未填写，默认为空。

取值范围：[0, ∞)

risingTime

number

否

是

最晚起床时间点，若未填写，默认为空。

取值范围：[0, ∞)

prepareSleepTime

number

否

是

准备入睡时间点，若未填写，默认为空。

单位：毫秒

取值范围：[0, ∞)

shallowDuration

number

否

是

浅睡时长，若未填写，默认为空。

单位：秒

取值范围：[0, ∞)

deepDuration

number

否

是

深睡时长，若未填写，默认为空。

单位：秒

取值范围：[0, ∞)

dreamDuration

number

否

是

REM时长，若未填写，默认为空。

单位：秒

取值范围：[0, ∞)

wakeDuration

number

否

是

清醒时长，若未填写，默认为空。

单位：秒

取值范围：[0, ∞)

wakeCount

number

否

是

清醒次数，若未填写，默认为空。

取值范围：[0, ∞)

onBedDuration

number

否

是

卧床时长，若未填写，默认为空。

单位：秒

取值范围：[0, ∞)

recordDuration

number

否

是

睡眠记录时长，若未填写，默认为记录结束时间减去开始时间。

单位：秒

取值范围：[0, ∞)

sleepEfficiency

number

否

是

睡眠效率，若未填写，默认为空。

取值范围：[0, 100]

sleepScore

number

否

是

睡眠得分，若未填写，默认为空。

取值范围：[0, 100]

deepSleepContinuity

number

否

是

深睡连续性，若未填写，默认为空。

取值范围：[0, 100]

respiratoryQualityScore

number

否

是

呼吸质量分，若未填写，默认为空。

取值范围：[0, 100]

turnOverCount

number

否

是

翻身次数，若未填写，默认为空。

取值范围：[0, ∞)

sleepEndReason

number

否

是

睡眠结束原因，若未填写，默认为空。

取值范围：[0, ∞)

取值参考如下：

0：手动结束睡眠监测

1：自动结束睡眠监测

2：中断睡眠监测

3：电量过低结束

sleepSymptoms

string

否

是

睡眠症状，若未填写，默认为空。

sleepType

number

否

是

睡眠数据类型。

取值范围：

1：科学睡眠

2：普通睡眠

3：手动输入睡眠

4：手机记录睡眠

未设置时，默认值为2。

#### SleepDetail

睡眠详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

sleepSegment

[SleepSegment](#section5465143561710)[]

否

是

睡眠状态采样列表，若未填写，默认设置覆盖全部睡眠时间的详情，睡眠状态值为7。

#### SleepNap

零星小睡数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

noonDuration

number

否

否

午睡时长(零星小睡）。

单位：秒

取值范围：[0, ∞)

noonRecordDuration

number

否

是

零星小睡记录时长，若未填写，默认为记录结束时间减去开始时间。

单位：秒

取值范围：[0, ∞)

#### SleepSegment

睡眠状态采样数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

sleepStatus

number

否

否

睡眠状态。

取值范围：

0：未知

1：深睡

2：浅睡

3：REM

4：清醒

5：午睡（零星小睡）

6：卧床

7：睡眠（手工）

endTime

number

否

否

结束时间。

单位：毫秒

取值范围：[0, ∞)

#### SnowboardingDetail

单板滑雪详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

location

[Location](#section1970034063415)[]

否

是

位置详情列表，若未填写，默认为空。

altitude

[Altitude](#section271517115816)[]

否

是

海拔详情列表，若未填写，默认为空。

#### SnowboardingFeature

单板滑雪特征数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

tripTimes

number

否

否

趟数。

maxSlopePercent

number

否

是

滑雪最大坡度百分比，若未填写，默认为空。

maxSlopeDegree

number

否

是

滑雪最大坡，若未填写，默认为空。

单位：度

totalTime

number

否

是

滑行时间，若未填写，默认为空。

单位：毫秒

totalDistance

number

否

是

滑行距离，若未填写，默认为空。

单位：米

#### SnowboardingSummary

单板滑雪统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

distance

[DistanceSummary](#section1931022758)

否

否

距离统计。

calorie

[CalorieSummary](#section10820034172215)

否

否

热量统计。

snowboardingFeature

[SnowboardingFeature](#section1874516534612)

否

否

单板滑雪特征数据。

altitude

[AltitudeSummary](#section5999164151119)

否

是

海拔统计，若未填写，默认为空。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

#### Speed

速度详情数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

speed

number

否

否

速度详情。

单位：米/秒

取值范围：[0, ∞)

#### SpeedSummary

速度统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

单位：米/秒

取值范围：[0, ∞)

max

number

否

否

最大值。

单位：米/秒

取值范围：[0, ∞)

min

number

否

是

最小值，若未填写，默认为空。

单位：米/秒

取值范围：[0, ∞)

#### SportsDetail

通用详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

#### SportsSummary

通用统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

calorie

[CalorieSummary](#section10820034172215)

否

否

热量统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

#### StepSummary

步数统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

totalSteps

number

否

否

步数总值。

取值范围：(0, ∞)

#### Stress

压力采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

stressScore

number

否

否

压力得分。

取值范围：[1, 99]

#### StressAggregation

压力得分聚合统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

stressScore

Omit<[AggregateMetrics](healthStore(运动健康数据服务).md#section023015433412), 'sum'>

否

否

压力得分聚合统计。

#### StrokeRate

桨频采样数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

spm

number

否

否

桨频。

单位：次/分钟

#### StrokeRateSummary

桨频统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

单位：次/分钟

取值范围: [0, ∞)

max

number

否

否

最大值。

单位：次/分钟

取值范围: [0, ∞)

#### SwimStrokeRate

划水频率采样数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

spm

number

否

否

游泳划水频率。

单位：次/分钟

#### SwimStrokeRateSummary

划水频率统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

单位：次/分钟

取值范围: [0, ∞)

#### Swolf

SWOLF采样数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

swolf

number

否

否

SWOLF.

#### SwolfSummary

SWOLF统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

avg

number

否

否

平均值。

取值范围: [0, ∞)

max

number

否

否

最大值。

取值范围: [0, ∞)

min

number

否

是

最小值，若未填写，默认为空。

取值范围: [0, ∞)

#### WalkingDetail

健走详情数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

exerciseHeartRate

[ExerciseHeartRate](#section1011218571967)[]

否

是

运动心率详情列表，若未填写，默认为空。

speed

[Speed](#section10458134951817)[]

否

是

速度详情列表，若未填写，默认为空。

cadence

[Cadence](#section625153911153)[]

否

是

步频详情列表，若未填写，默认为空。

location

[Location](#section1970034063415)[]

否

是

位置详情列表，若未填写，默认为空。

altitude

[Altitude](#section271517115816)[]

否

是

海拔详情列表，若未填写，默认为空。

#### WalkingSummary

健走统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

distance

[DistanceSummary](healthFields(运动健康数据字段).md#section1931022758)

否

否

距离统计。

calorie

[CalorieSummary](#section10820034172215)

否

否

热量统计。

speed

[SpeedSummary](#section4460144920180)

否

否

速度统计。

exerciseHeartRate

[ExerciseHeartRateSummary](#section61131157564)

否

是

运动心率统计，若未填写，默认为空。

step

[StepSummary](#section1531683122019)

否

是

步数统计，若未填写，默认为空。

cadence

[CadenceSummary](#section517018141201)

否

是

步频统计，若未填写，默认为空。

altitude

[AltitudeSummary](#section5999164151119)

否

是

海拔统计，若未填写，默认为空。

location

[LocationSummary](#section20701154013341)

否

是

位置统计，若未填写，默认为空。

#### WaterTemperature

水温采样数据字段列表，继承[healthStore.SequencePoint](healthStore(运动健康数据服务).md#section244154911570)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

temperature

number

否

否

温度。

单位：摄氏度

#### WaterTemperatureSummary

水温统计数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

max

number

否

否

最大值。

单位：摄氏度

取值范围: [0, ∞)

min

number

否

是

最小值，若未填写，默认为空。

单位：摄氏度

取值范围: [0, ∞)

#### Weight

体重采样数据字段列表。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

bodyWeight

number

否

否

体重。

单位：千克

取值范围：[0.1, 500]

bmi

number

否

是

身体质量指数，若未填写，默认为空。

单位：千克/平方米

取值范围：[1,200]

bodyFat

number

否

是

体脂量，若未填写，默认为空。

单位：千克

取值范围：[0, 500]

bodyFatRate

number

否

是

体脂率，若未填写，默认为空。

单位：百分比

取值范围：[0, 100]

muscleMass

number

否

是

肌肉量，若未填写，默认为空。

单位：千克

取值范围：[0.1, 150]

basalMetabolism

number

否

是

基础代谢，若未填写，默认为空。

单位：千卡/天

取值范围：[0, ∞)

moisture

number

否

是

水分量，若未填写，默认为空。

单位：千克

取值范围：[0, 500]

moistureRate

number

否

是

水分率，若未填写，默认为空。

单位：百分比

取值范围：[0, 100]

visceralFatLevel

number

否

是

内脏脂肪等级，若未填写，默认为空。

取值范围：[1, 59]

boneSalt

number

否

是

骨盐量，若未填写，默认为空。

单位：千克

取值范围：[0.5, 5]

proteinRate

number

否

是

蛋白质率，若未填写，默认为空。

单位：百分比

取值范围：[0, 100]

bodyScore

number

否

是

身体得分，若未填写，默认为空。

单位：百分比

取值范围：[0, 100]

bodyAge

number

否

是

身体年龄，若未填写，默认为空。

取值范围：[5, 99]

skeletalMuscleMass

number

否

是

骨骼肌量，若未填写，默认为空。

单位：千克

取值范围：[1, 150]

impedance

number

否

是

阻抗。

单位：欧姆

取值范围：[0.1, 100000]