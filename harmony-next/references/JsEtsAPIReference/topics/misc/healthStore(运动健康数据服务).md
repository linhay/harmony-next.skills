# healthStore(运动健康数据服务)

本模块提供运动健康数据服务。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { healthStore } from '@kit.HealthServiceKit';
```

#### AggregateMetrics

type AggregateMetrics = Partial<Record<[AggregateMetricScope](#ZH-CN_TOPIC_0000002522082354__aggregatemetricscope), number>>

聚合策略。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| max | number | 否 | 是 | 最大值聚合，若未填写，则不查询此聚合类型。 |
| min | number | 否 | 是 | 最小值聚合，若未填写，则不查询此聚合类型。 |
| avg | number | 否 | 是 | 平均值聚合，若未填写，则不查询此聚合类型。 |
| sum | number | 否 | 是 | 累计值聚合，若未填写，则不查询此聚合类型。 |
| last | number | 否 | 是 | 最新值聚合，若未填写，则不查询此聚合类型。 |
| count | number | 否 | 是 | 计数聚合，若未填写，则不查询此聚合类型。 |

#### AggregateMetricScope

type AggregateMetricScope = 'max' | 'min' | 'avg' | 'sum' | 'last' | 'count'

聚合策略类型。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| 'max' | 统计最大值。 |
| 'min' | 统计最小值。 |
| 'avg' | 统计平均值。 |
| 'sum' | 统计累计值。 |
| 'last' | 统计最新值。 |
| 'count' | 计数。 |

#### AggregateRequest

AggregateRequest<T extends Record<string, [AggregateMetrics](#ZH-CN_TOPIC_0000002522082354__aggregatemetrics)> = Record<string, [AggregateMetrics](#ZH-CN_TOPIC_0000002522082354__aggregatemetrics)>>

聚合查询请求类，继承Omit<[DataReadRequest](#ZH-CN_TOPIC_0000002522082354__datareadrequest), 'startTime' | 'endTime'>。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataType | DataType | 否 | 否 | 聚合查询的数据类型。 |
| metrics | Partial<Record<keyof T, AggregateMetricScope[]>> | 否 | 否 | 聚合策略。 |
| groupBy | GroupOption | 否 | 否 | 聚合分组选项。 |

#### AggregateResult

AggregateResult<T extends Record<string, [AggregateMetrics](#ZH-CN_TOPIC_0000002522082354__aggregatemetrics)> = Record<string, [AggregateMetrics](#ZH-CN_TOPIC_0000002522082354__aggregatemetrics)>>

聚合查询结果类，继承Omit<[SampleDataBase](#ZH-CN_TOPIC_0000002522082354__sampledatabase), 'dataSourceId'>。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fields | Pick<T, keyof T> | 否 | 否 | 聚合查询字段。 |

#### AppInfo

应用信息类。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 是 | 调用方的应用包名，若未填写，默认为调用方包名。 |
| appId | string | 是 | 是 | 调用方的应用的OAuth 2.0客户端ID(client_id)，若未填写，默认为调用方client_id。 |
| appName | string | 是 | 是 | 调用方的应用名称，长度小于256字节。首次若未填写，默认为'CoreServiceExtAbility'，更新需要调用updateDataSource接口。 |
| version | string | 是 | 是 | 调用方的应用版本信息，长度小于256字节。首次若未填写，默认为空，更新需要调用updateDataSource接口。 |

#### AuthorizationBase

授权信息基类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| readDataTypes | DataType[] | 否 | 否 | 读数据类型。 |
| writeDataTypes | DataType[] | 否 | 否 | 写数据类型。 |

#### AuthorizationRequest

授权请求参数类型，继承[AuthorizationBase](#ZH-CN_TOPIC_0000002522082354__authorizationbase)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| readDataTypes | DataType[] | 否 | 否 | 读数据类型。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| writeDataTypes | DataType[] | 否 | 否 | 写数据类型。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| scopes | string[] | 否 | 是 | 非数据类型权限，使用scope授权，请参见OAuth权限，若未填写，默认为空。 起始版本： 5.1.0(18) 元服务API： 从版本5.1.0(18)开始，该接口支持在元服务中使用。 |

#### AuthorizationResponse

授权响应返回类型，继承[AuthorizationBase](#ZH-CN_TOPIC_0000002522082354__authorizationbase)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| readDataTypes | DataType[] | 否 | 否 | 授权成功的读数据类型，其对应权限在应用申请权限和用户授权权限的交集中。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| writeDataTypes | DataType[] | 否 | 否 | 授权成功的写数据类型，其对应权限在应用申请权限和用户授权权限的交集中。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| scopes | string[] | 否 | 是 | 非数据类型权限，使用scope授权，请参见OAuth权限，若未填写，默认为空。 起始版本： 5.1.0(18) 元服务API： 从版本5.1.0(18)开始，该接口支持在元服务中使用。 |

#### DataReadRequest

读取请求参数基类，继承[DataRequest](#ZH-CN_TOPIC_0000002522082354__datarequest)。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| count | number | 否 | 是 | 读取数据的条数，若未填写，默认为无条数限制。 取值范围：[1, ∞) |
| offset | number | 否 | 是 | 相对于当前位置的偏移，若未填写，默认为0，无偏移。 |
| sortOrder | SortOrder | 否 | 是 | 排序顺序，若未填写，默认为升序。 |

#### DataRequest

请求参数基类。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startLocalDate | string | 否 | 否 | 数据的开始本地日期，格式'MM/DD/YYYY'。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| endLocalDate | string | 否 | 否 | 数据的结束本地日期，格式'MM/DD/YYYY'。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| startTime | number | 否 | 否 | 请求的开始时间，Unix时间戳，以毫秒为单位。 该参数在Wearable设备上暂不生效，仅支持返回最新一条数据。 取值范围：(0, ∞) |
| endTime | number | 否 | 否 | 请求的结束时间，Unix时间戳，以毫秒为单位。 该参数在Wearable设备上暂不生效，仅支持返回最新一条数据。 取值范围：(0, ∞) |
| dataSourceOptions | DataSourceOptions | 否 | 是 | 请求关联的数据源信息，若未填写，默认为无数据源限制。 |

#### DataSource

数据源。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataSourceId | string | 是 | 否 | 数据源的标识，由平台生成，无法更改，长度小于256字节。 |
| deviceInfo | DeviceInfo | 是 | 是 | 设备信息，若未填写，默认为空。 |
| appInfo | AppInfo | 是 | 是 | 应用信息，若未填写，默认为调用方应用信息。 |

#### DataSourceBase

type DataSourceBase = Omit<DataSource, 'dataSourceId'>

数据源的基类，用于插入数据源。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceInfo | DeviceInfo | 是 | 是 | 设备信息，若未填写，默认为空。 |
| appInfo | AppInfo | 是 | 是 | 应用信息，若未填写，默认为调用方应用信息。 |

#### DataSourceOptions

数据源选项类，用于查询和删除。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataSourceId | string | 否 | 是 | 数据源的标识，由平台生成，无法更改，若未填写，默认为空。 |
| deviceUniqueId | string | 否 | 是 | 设备的UniqueId，若未填写，默认为空。 |
| appBundleName | string | 否 | 是 | 应用包名，若未填写，默认为空。 |
| appId | string | 否 | 是 | 应用的OAuth 2.0客户端ID(client_id)，若未填写，默认为空。 |

#### DataSourceReadRequest

读取数据源请求。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataSourceId | string | 否 | 是 | 数据源的唯一标识（dataSourceId与bundleName、deviceUniqueId不能同时填写）。 |
| bundleName | string | 否 | 是 | 应用包名（仅当未填写dataSourceId时可填写）。 |
| deviceUniqueId | string | 否 | 是 | 设备UniqueId（仅当未填写dataSourceId时可填写）。 |

#### DataType

定义数据类型的类，每个数据类型字段都有唯一的id来标识。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 是 | 否 | 数据类型唯一标识值。 |
| name | string | 是 | 是 | 数据类型的名称，若未填写，默认匹配id对应的名称。 |

#### DeviceCategory

设备类型枚举对象。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MANUAL_INPUT | '000' | 手动输入。 |
| SMART_PHONE | '00E' | 手机。 |
| WEARABLE_WATCH | '06D' | 手表。 |
| WEARABLE_BAND | '06E' | 手环。 |
| SMART_HEADPHONES | '082' | 智能耳机。 |
| HDK_WEIGHT_SCALE | '0CB' | 体脂秤。 |
| HDK_BLOOD_SUGAR_MONITOR | '086' | 血糖仪。 |
| HDK_BLOOD_PRESSURE_MONITOR | '02B' | 血压计。 |
| HDK_HEART_RATE_MONITOR | '088' | 心率计。 |
| HDK_THERMOMETER | '0B3' | 体温计。 |
| HDK_BLOOD_OXYGEN_MONITOR | '0B4' | 血氧仪。 |
| HDK_ROPE_SKIPPING | '095' | 跳绳。 |
| HDK_TREADMILL | '08F' | 跑步机。 |
| HDK_EXERCISE_BIKE | '0BF' | 动感单车。 |
| HDK_ROWING_MACHINE | '0C1' | 划船机。 |
| HDK_ELLIPTICAL_MACHINE | '0C0' | 椭圆机。 |
| HDK_WALKING_MACHINE | '092' | 漫步机。 |
| SPORTS_GENIE | 'A12' | 跑姿监测设备。 |

#### DeviceInfo

设备信息类。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniqueId | string | 是 | 否 | 设备UniqueId，唯一标识，长度小于256字节。 |
| udid | string | 是 | 是 | 设备udid，若未填写，默认为空。 |
| name | string | 是 | 是 | 设备名称，长度小于256字节。(插入数据源时必填) |
| category | DeviceCategory | 是 | 是 | 设备类型，需与productId匹配。(插入数据源时必填) |
| productId | string | 是 | 是 | 生态设备的华为全场景产品ID，需与category匹配，长度小于256字节。(插入数据源时必填) 例如手动输入场景： category: DeviceCategory.MANUAL_INPUT productId: '0062' |
| model | string | 是 | 是 | 设备的型号名称，若未填写，默认为空。 |
| manufacturer | string | 是 | 是 | 设备的制造商信息，若未填写，默认为空。 |
| mac | string | 是 | 是 | 设备mac地址，若未填写，默认为空。 |
| sn | string | 是 | 是 | 设备sn地址，若未填写，默认为空。 |
| hardwareVersion | string | 是 | 是 | 设备硬件版本，若未填写，默认为空。 |
| softwareVersion | string | 是 | 是 | 设备软件版本，若未填写，默认为空。 |
| firmwareVersion | string | 是 | 是 | 设备固件版本，若未填写，默认为空。 |

#### ExerciseSequence

ExerciseSequence<K extends Record<string, [ExerciseSummary](#ZH-CN_TOPIC_0000002522082354__exercisesummary)> = Record<string, [ExerciseSummary](#ZH-CN_TOPIC_0000002522082354__exercisesummary)>,DK extends Record<string, [SequencePoint](#ZH-CN_TOPIC_0000002522082354__sequencepoint)[]> = Record<string, [SequencePoint](#ZH-CN_TOPIC_0000002522082354__sequencepoint)[]>>

锻炼记录数据类，继承[SampleDataBase](#ZH-CN_TOPIC_0000002522082354__sampledatabase)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| exerciseType | SubDataType | 否 | 否 | 锻炼记录子数据类型。 |
| duration | number | 否 | 是 | 锻炼时长，单位毫秒，若未填写，默认为结束时间减去开始时间。 取值范围：(0, ∞) |
| summaries | Pick<K, keyof K> | 否 | 否 | 统计数据，锻炼记录关联的统计数据类型参考exerciseSequenceHelper定义的模型。 |
| details | Pick<DK, keyof DK> | 否 | 是 | 详情数据，锻炼记录关联的详情数据类型参考exerciseSequenceHelper定义的模型，若未填写，默认为空。 |

#### ExerciseSequenceDeleteRequest

删除锻炼记录请求类，继承Omit<[DataRequest](#ZH-CN_TOPIC_0000002522082354__datarequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| exerciseType | SubDataType | SubDataType[] | null | 否 | 否 | 锻炼记录子数据类型。若为空时，删除所有类型。 |

#### ExerciseSequenceReadRequest

ExerciseSequenceReadRequest<DK extends Record<string, [SequencePoint](#ZH-CN_TOPIC_0000002522082354__sequencepoint)[]> = Record<string, [SequencePoint](#ZH-CN_TOPIC_0000002522082354__sequencepoint)[]>>

读取锻炼记录请求类，继承Omit<[DataReadRequest](#ZH-CN_TOPIC_0000002522082354__datareadrequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| exerciseType | SubDataType | SubDataType[] | null | 否 | 否 | 锻炼记录子数据类型，为空时查询所有类型。 |
| readOptions | SequenceReadOptions<DK> | 否 | 是 | 详情数据选项，若未填写，默认为不查询详情数据。 |

#### ExerciseSummary

锻炼记录统计数据类。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| [P: string] | HealthValueType | PaceValueType | 否 | 否 | 统计数据字段。 |

#### GroupOption

聚合分组选项。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| unitType | GroupUnitType | 否 | 否 | 聚合策略（分组单元）。 |
| duration | number | 否 | 是 | 每个分组的单元数量，若未填写，默认为1，每个分组仅有一个单元，当前按天聚合只支持duration为1。 |

#### GroupUnitType

聚合策略（分组单元）枚举对象。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DAY | 3 | 按天聚合。 |

#### HealthSequence

HealthSequence<K extends Record<string, [HealthValueType](#ZH-CN_TOPIC_0000002522082354__healthvaluetype)> = Record<string, [HealthValueType](#ZH-CN_TOPIC_0000002522082354__healthvaluetype)>,DK extends Record<string, [SequencePoint](#ZH-CN_TOPIC_0000002522082354__sequencepoint)[]> = Record<string, [SequencePoint](#ZH-CN_TOPIC_0000002522082354__sequencepoint)[]>>

健康记录数据类，继承[SampleDataBase](#ZH-CN_TOPIC_0000002522082354__sampledatabase)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| summaries | Pick<K, keyof K> | 否 | 否 | 统计数据，健康记录关联的统计数据类型参考healthSequenceHelper定义的模型。 |
| details | Pick<DK, keyof DK> | 否 | 是 | 详情数据，健康记录关联的详情数据类型参考healthSequenceHelper定义的模型，若未填写，默认为空。 |

#### HealthSequenceDeleteRequest

删除健康记录请求类，继承Omit<[DataRequest](#ZH-CN_TOPIC_0000002522082354__datarequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| healthSequenceDataType | DataType | DataType[] | 否 | 否 | 健康数据类型。 |

#### HealthSequenceReadRequest

HealthSequenceReadRequest<DK extends Record<string, [SequencePoint](#ZH-CN_TOPIC_0000002522082354__sequencepoint)[]> = Record<string, [SequencePoint](#ZH-CN_TOPIC_0000002522082354__sequencepoint)[]>>

读取健康记录请求类，继承Omit<[DataReadRequest](#ZH-CN_TOPIC_0000002522082354__datareadrequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| healthSequenceDataType | DataType | DataType[] | 否 | 否 | 健康数据类型。 |
| readOptions | SequenceReadOptions<DK> | 否 | 是 | 详情数据选项，若未填写，默认为不查询详情数据。 |

#### HealthValueType

type HealthValueType = number | string | boolean | undefined

运动健康数据值类型。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| boolean | 表示值类型为布尔类型，可取true或false，具体含义以实际使用场景为准。 |
| undefined | 表示值类型为undefined，取值为空。 起始版本： 6.0.1(21) |

#### PaceValueType

type PaceValueType = Record<string, number>

配速数据类型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| Record<string, number> | 配速数据字段。 |

#### SampleDataBase

健康数据基类。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataType | DataType | 否 | 否 | 数据类型。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| dataSourceId | string | 否 | 否 | 数据源唯一标识值。 |
| localDate | string | 否 | 否 | 数据的本地日期，格式'MM/DD/YYYY'。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| startTime | number | 否 | 否 | 数据开始时间，Unix时间戳，以毫秒为单位。 取值范围：(0, ∞) 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| endTime | number | 否 | 否 | 数据结束时间，Unix时间戳，以毫秒为单位。 取值范围：(0, ∞) 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| timeZone | string | 否 | 否 | 数据所在的时区，格式为+0800。 元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。 |
| modifiedTime | number | 否 | 否 | 创建或修改时间，Unix时间戳，以毫秒为单位。 取值范围：(0, ∞) |

#### SamplePoint

SamplePoint<K extends Record<string, [HealthValueType](#ZH-CN_TOPIC_0000002522082354__healthvaluetype)> = Record<string, [HealthValueType](#ZH-CN_TOPIC_0000002522082354__healthvaluetype)>>

数据采样点，继承[SampleDataBase](#ZH-CN_TOPIC_0000002522082354__sampledatabase)。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fields | Pick<K, keyof K> | 否 | 否 | 数据的字段，数据类型对应的字段参考samplePointHelper定义的模型。 |

#### SamplePointDeleteRequest

type SamplePointDeleteRequest = UnixTimeBasedDataDeleteRequest

删除数据采样点请求类型，继承Omit<[DataRequest](#ZH-CN_TOPIC_0000002522082354__datarequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataType | DataType | DataType[] | 否 | 否 | 待删除的数据类型。 |

#### SamplePointReadRequest

SamplePointReadRequest<FK extends Record<string, [HealthValueType](#ZH-CN_TOPIC_0000002522082354__healthvaluetype)> = Record<string, [HealthValueType](#ZH-CN_TOPIC_0000002522082354__healthvaluetype)>>

读取数据采样点请求类，继承Omit<[DataReadRequest](#ZH-CN_TOPIC_0000002522082354__datareadrequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| samplePointDataType | DataType| DataType[] | 否 | 否 | 查询的数据类型。 |
| fields | Partial<Pick<FK, keyof FK>> | 否 | 是 | 要读取的字段列表，若samplePointDataType参数为数组，fields字段不能设置，数据类型对应的字段参考samplePointHelper定义的模型。若为空，则用于读取所有字段。 |

#### SequencePoint

运动健康数据详情点。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| startTime | number | 否 | 否 | 数据开始时间，Unix时间戳，以毫秒为单位。 取值范围：(0, ∞) |
| [P: string] | HealthValueType | 否 | 否 | 详情数据点字段。 |

#### SequenceReadOptions

SequenceReadOptions<DK extends Record<string, [SequencePoint](#ZH-CN_TOPIC_0000002522082354__sequencepoint)[]> = Record<string, [SequencePoint](#ZH-CN_TOPIC_0000002522082354__sequencepoint)[]>>

读取运动健康记录详情数据选项类。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| withDetails | boolean | 否 | 是 | 是否读取全部详情。true为读取全部详情，false为不读取详情，若未填写，则withPartialDetails参数生效。 |
| withPartialDetails | (keyof DK)[] | 否 | 是 | 读取部分详情数据类型（若需要读取部分详情，withDetails参数不能填写），锻炼记录与健康记录关联的详情数据类型分别参考exerciseSequenceHelper与healthSequenceHelper定义的模型。 |

#### SequenceValueType

type SequenceValueType = number | string | boolean | object

运动健康数据值类型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| boolean | 表示值类型为布尔类型，可取true或false，具体含义以实际使用场景为准。 |
| object | 表示值类型为对象，可取任意值。 |

#### SortOrder

结果排序类型枚举对象。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ASC | 0 | 升序。 |
| DESC | 1 | 降序。 |

#### SubDataType

type SubDataType = DataType

子数据类型。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | number | 是 | 否 | 子数据类型唯一标识值。 |
| name | string | 是 | 是 | 子数据类型的名称，若未填写，默认匹配id对应的名称。 |

#### UnixTimeBasedDataDeleteRequest

基于Unix时间戳的删除请求基类，继承Omit<[DataRequest](#ZH-CN_TOPIC_0000002522082354__datarequest), 'startLocalDate' | 'endLocalDate'>。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataType | DataType | DataType[] | 否 | 否 | 待删除的数据类型。 |

#### healthStore.init

init(context: common.Context): Promise<void>

Health Service初始化接口，使用Promise异步方式，其他接口调用前需先初始化，仅首次调用需要。

该接口从API 19 Release开始，支持Wearable设备开发。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.Context | 是 | 上下文，目前只支持UIAbility或UIExtensionAbility的上下文环境。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthStore.init(this.getUIContext().getHostContext());
  hilog.info(0x0000, 'testTag', 'Succeeded in initing.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.insertDataSource

insertDataSource(dataSource: DataSourceBase): Promise<string>

插入指定的数据源，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataSource | DataSourceBase | 是 | 构造的数据源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回数据源唯一标识符（dataSourceId）。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let dataSource: healthStore.DataSourceBase = {
  deviceInfo: {
    uniqueId: 'test',
    name: 'test', // 插入数据源时此字段必填
    category: healthStore.DeviceCategory.WEARABLE_BAND, // 插入数据源时此字段必填
    productId: '0554', // 插入数据源时此字段必填
    model: 'lotana',
    manufacturer: 'HUAWEI',
    mac: 'testDeviceMac',
    sn: 'testDeviceSn',
    hardwareVersion: '1',
    softwareVersion: '2',
    firmwareVersion: '3',
    udid: ''
  }

try {
  const dataSourceId = await healthStore.insertDataSource(dataSource);
  hilog.info(0x0000, 'testTag', `Succeeded in inserting dataSource, the dataSourceId is ${dataSourceId}.`);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to insert dataSource. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.readDataSource

readDataSource(request: DataSourceReadRequest): Promise<DataSource[]>

读取数据源，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | DataSourceReadRequest | 是 | 读取数据源请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DataSource[]> | Promise对象，返回DataSource数组。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let readSourceRequest: healthStore.DataSourceReadRequest = {
  deviceUniqueId: 'testudidupdate'
}

try {
  let dataSources = await healthStore.readDataSource(readSourceRequest);
  dataSources.forEach((dataSource) => {
    hilog.info(0x0000, 'testTag', `Succeeded in reading dataSource, the dataSourceId is ${dataSource.dataSourceId}.`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read dataSource. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.updateDataSource

updateDataSource(dataSource: DataSource): Promise<void>

更新数据源，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataSource | DataSource | 是 | 待更新的数据源。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let newDataSource: healthStore.DataSource = {
  deviceInfo: {
    uniqueId: 'test',
    name: 'test',
    category: healthStore.DeviceCategory.WEARABLE_BAND,
    productId: '0554',
    model: 'lotana',
    manufacturer: 'HUAWEI',
    mac: 'testDeviceMac',
    sn: 'testDeviceSn',
    hardwareVersion: '1',
    softwareVersion: '2',
    firmwareVersion: '3',
    // 修改udid
    udid: 'updateudid'
  },
  // 此处dataSourceId值为开发步骤插入数据源时，返回的dataSourceId
  dataSourceId: 'xxx'
}

try {
  await healthStore.updateDataSource(newDataSource);
  hilog.info(0x0000, 'testTag', 'Succeeded in updating dataSource.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to update dataSource. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.saveData

saveData(sampleData: SamplePoint[] | SamplePoint): Promise<void>

保存数据采样点，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sampleData | SamplePoint[] | SamplePoint | 是 | 单个数据采样点或数据采样点数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let samplePoint: healthStore.SamplePoint = {
  dataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
  startTime: 1698633801000,
  endTime: 1698633801000,
  localDate: '10/30/2023',
  timeZone: '+0800',
  modifiedTime: 1698633801000,
  // insertDataSource插入数据源接口返回的DataSourceId
  dataSourceId: 'xxx',
  fields: {
    bodyTemperature: 39
  }

try {
  await healthStore.saveData(samplePoint);
  hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to save data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.saveData

saveData(exerciseSequence: ExerciseSequence[] | ExerciseSequence): Promise<void>

保存锻炼记录数据，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exerciseSequence | ExerciseSequence[] | ExerciseSequence | 是 | 单个锻炼记录或锻炼记录数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 构造跑步记录
const startTime = 1698040800000; // 2023-10-23 14:00:00
const endTime = 1698042600000; // 2023-10-23 14:30:00

const runningSequence: healthStore.exerciseSequenceHelper.running.Model = {
  dataType: healthStore.exerciseSequenceHelper.DATA_TYPE,
  // insertDataSource插入数据源接口返回的DataSourceId
  dataSourceId: 'xxx',
  startTime: startTime, // 2023-10-23 14:00:00
  endTime: endTime, // 2023-10-23 14:30:00
  localDate: '10/23/2023',
  timeZone: '+0800',
  modifiedTime: new Date().getTime(),
  exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
  duration: 1800000,
  summaries: {
    distance: {
      totalDistance: 2000
    },
    calorie: {
      totalCalories: 20
    },
    speed: {
      avg: 5,
      max: 6
    }
  },
  details: {
    exerciseHeartRate: [
      {
        startTime: startTime,
        bpm: 88
      },
      {
        startTime: startTime + 5000,
        bpm: 89
      }
    ],
    speed: [
      {
        startTime: startTime,
        speed: 2.5
      },
      {
        startTime: startTime + 5000,
        speed: 2.3
      }
    ],
    altitude: [
      {
        startTime: startTime,
        altitude: 100
      },
      {
        startTime: startTime + 5000,
        altitude: 101
      }
    ]
  }
};
try {
  await healthStore.saveData(runningSequence);
  hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to save data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.saveData

saveData(healthSequence: HealthSequence[] | HealthSequence): Promise<void>

保存健康记录数据，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| healthSequence | HealthSequence[] | HealthSequence | 是 | 单个健康记录或健康记录数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let healthSequence: healthStore.healthSequenceHelper.sleepRecord.Model = {
  summaries: {
    fallAsleepTime: 1695740400000, // 2023-09-26 23:00:00
    wakeupTime: 1695769200000, // 2023-09-27 7:00:00
    sleepScore: 80,
    wakeCount: 2,
    sleepType: 1,
    shallowDuration: 14400,
    deepDuration: 7200,
    dreamDuration: 7200,
    wakeDuration: 0,
    duration: 28800
  },
  dataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
  // insertDataSource插入数据源接口返回的DataSourceId
  dataSourceId: 'xxx',
  localDate: '09/26/2023',
  startTime: 1695740400000,
  endTime: 1695769200000,
  timeZone: '+0800',
  modifiedTime: 1695769200000,
  details: {
    sleepSegment: [
      {
        startTime: 1695740400000, // 2023-09-26 23:00:00
        endTime: 1695747600000, // 2023-09-27 01:00:00
        sleepStatus: 2
      },
      {
        startTime: 1695747600000, // 2023-09-27 01:00:00
        endTime: 1695754800000, // 2023-09-27 03:00:00
        sleepStatus: 1
      },
      {
        startTime: 1695754800000, // 2023-09-27 03:00:00
        endTime: 1695762000000, // 2023-09-27 05:00:00
        sleepStatus: 3
      },
      {
        startTime: 1695762000000, // 2023-09-27 05:00:00
        endTime: 1695769200000, // 2023-09-27 07:00:00
        sleepStatus: 2
      }
    ]
  }
try {
  await healthStore.saveData(healthSequence);
  hilog.info(0x0000, 'testTag', 'Succeeded in saving data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to save data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.readData

readData<T extends SamplePoint>(request: SamplePointReadRequest): Promise<T[]>

读取数据采样点，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | SamplePointReadRequest | 是 | 读取数据采样点请求，查询时间跨度范围为31天。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | Promise对象，T继承SamplePoint，返回数据采样点数组。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let samplePointReadRequest: healthStore.SamplePointReadRequest = {
  samplePointDataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
  startTime: 1698633801000,
  endTime: 1698633801000,
  fields: {
    bodyTemperature: 39
}

try {
  let samplePoints = await healthStore.readData(samplePointReadRequest);
  samplePoints.forEach((samplePoint) => {
    hilog.info(0x0000, 'testTag', `Succeeded in reading data, the bodyTemperature is ${samplePoint.fields.bodyTemperature}.`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.readData

readData<T extends ExerciseSequence>(request: ExerciseSequenceReadRequest): Promise<T[]>

读取锻炼记录数据，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | ExerciseSequenceReadRequest | 是 | 读取锻炼记录请求，查询时间跨度范围为31天。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | Promise对象，T继承ExerciseSequence，返回锻炼记录数组。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 查询跑步记录
const startTime = 1698040800000; // 2023-10-23 14:00:00
const endTime = 1698042600000; // 2023-10-23 14:30:00

const sequenceReadRequest: healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
  startTime: startTime,
  endTime: endTime,
  exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
  count: 1,
  sortOrder: 1,
  readOptions: {
    withPartialDetails: ['exerciseHeartRate', 'altitude']
 }
};
try {
  const runningSequences = await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
  hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
  runningSequences.forEach((runningSequence) => {
    hilog.info(0x0000, 'testTag', `the start time is ${runningSequence.startTime}.`);
    hilog.info(0x0000, 'testTag', `the end time is ${runningSequence.endTime}.`);
    Object.keys(runningSequence.summaries).forEach((key) => {
      Object.keys(runningSequence.summaries[key]).forEach((fieldName) => {
        hilog.info(0x0000, 'testTag', `the summaries of ${key} field ${fieldName} is ${runningSequence.summaries[key][fieldName]}.`);
      });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.readData

readData<T extends HealthSequence>(request: HealthSequenceReadRequest): Promise<T[]>

读取健康记录数据，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | HealthSequenceReadRequest | 是 | 读取健康记录请求，查询时间跨度范围为31天。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | Promise对象，T继承HealthSequence，返回健康记录数组。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
  healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
  startTime: 1695740400000,
  endTime: 1695769200000,
  readOptions: {
    withDetails: true
  }
try {
  const healthSequences = await healthStore.readData(healthSequenceReadRequest);

  hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
  healthSequences.forEach((healthSequence) => {
    hilog.info(0x0000, 'testTag', `the start time is ${healthSequence.startTime}.`);
    hilog.info(0x0000, 'testTag', `the end time is ${healthSequence.endTime}.`);
    Object.keys(healthSequence.summaries).forEach((key) => {
      hilog.info(0x0000, 'testTag', `the summaries of ${key} is ${healthSequence.summaries[key]}.`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.deleteData

deleteData(request: SamplePointDeleteRequest | SamplePointDeleteRequest[]): Promise<void>

删除数据采样点，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | SamplePointDeleteRequest | SamplePointDeleteRequest[] | 是 | 删除数据采样点请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let samplePointDeleteRequest: healthStore.SamplePointDeleteRequest = {
  dataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
  startTime: 1698633801000,
  endTime: 1698633801000
}

try {
  await healthStore.deleteData(samplePointDeleteRequest);
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.deleteData

deleteData(request: ExerciseSequenceDeleteRequest | ExerciseSequenceDeleteRequest[]): Promise<void>

删除锻炼记录数据，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | ExerciseSequenceDeleteRequest | ExerciseSequenceDeleteRequest[] | 是 | 删除锻炼记录请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let exerciseSequenceDeleteRequest: healthStore.ExerciseSequenceDeleteRequest= {
  exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE,
  startTime: 1698633801000,
  endTime: 1698633801000
}
try {
  await healthStore.deleteData(exerciseSequenceDeleteRequest);
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.deleteData

deleteData(request: HealthSequenceDeleteRequest | HealthSequenceDeleteRequest[]): Promise<void>

删除健康记录数据，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | HealthSequenceDeleteRequest | HealthSequenceDeleteRequest[] | 是 | 删除健康记录请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const healthSequenceDeleteRequest: healthStore.HealthSequenceDeleteRequest = {
  healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
  startTime: 1695740400000,
  endTime: 1695769200000
}
try {
  await healthStore.deleteData(healthSequenceDeleteRequest);
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.deleteData

deleteData(samplePoint: SamplePoint | SamplePoint[]): Promise<void>

删除指定数据采样点，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| samplePoint | SamplePoint | SamplePoint[] | 是 | 单个数据采样点或数据采样点数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let samplePointReadRequest: healthStore.SamplePointReadRequest = {
    samplePointDataType: healthStore.samplePointHelper.bodyTemperature.DATA_TYPE,
    startTime: 1698633801000,
    endTime: 1698633801000
  }
  let samplePoints: healthStore.SamplePoint[] = await healthStore.readData(samplePointReadRequest);
  for (let index = 0; index < samplePoints.length; index++) {
    const samplePoint = samplePoints[index];
    await healthStore.deleteData(samplePoint);
  }
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.deleteData

deleteData(exerciseSequence: ExerciseSequence | ExerciseSequence[]): Promise<void>

删除指定锻炼记录数据，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| exerciseSequence | ExerciseSequence | ExerciseSequence[] | 是 | 单个锻炼记录或锻炼记录数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 删除跑步
try {
  const sequenceReadRequest: healthStore.ExerciseSequenceReadRequest<healthStore.exerciseSequenceHelper.running.DetailFields> = {
    startTime: 1698040800000,
    endTime: 1698042600000,
    exerciseType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE
  };
  const runningSequences = await healthStore.readData<healthStore.exerciseSequenceHelper.running.Model>(sequenceReadRequest);
  for (let index = 0; index < runningSequences.length; index++) {
    const runningSequence = runningSequences[index];
    await healthStore.deleteData(runningSequence);
  }
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.deleteData

deleteData(healthSequence: HealthSequence | HealthSequence[]): Promise<void>

删除指定健康记录数据，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| healthSequence | HealthSequence | HealthSequence[] | 是 | 单个健康记录或健康记录数组。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let healthSequenceReadRequest: healthStore.HealthSequenceReadRequest = {
    healthSequenceDataType: healthStore.healthSequenceHelper.sleepRecord.DATA_TYPE,
    startTime: 1695740400000,
    endTime: 1695769200000
  }
  const healthSequences = await healthStore.readData(healthSequenceReadRequest);
  for (let index = 0; index < healthSequences.length; index++) {
    const healthSequence = healthSequences[index];
    await healthStore.deleteData(healthSequence);
  }
  hilog.info(0x0000, 'testTag', 'Succeeded in deleting data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to delete data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.aggregateData

aggregateData<T extends AggregateResult>(request: AggregateRequest | AggregateRequest[]): Promise<T[]>

聚合查询，使用Promise异步方式。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[1002700001](../../errors/ArkTS API错误码.md#section153755119333)错误码。

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | AggregateRequest | AggregateRequest[] | 是 | 聚合统计查询请求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T[]> | Promise对象，T继承AggregateResult，返回聚合查询结果数组。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let aggregateRequest: healthStore.AggregateRequest<healthStore.samplePointHelper.dailyActivities.AggregateFields> = {
  dataType: healthStore.samplePointHelper.dailyActivities.DATA_TYPE,
  metrics: {
    step: ['sum'],
    calorie: ['sum'],
    distance: ['sum'],
    climbHighAltitude:['sum'],
    isIntensity: ['sum'],
    isStand: ['sum']
 },
  groupBy: {
    unitType: 3,
    duration: 0
  },
  startLocalDate: '10/30/2023',
  endLocalDate: '10/30/2023'
}

try {
  const aggregateResults = await healthStore.aggregateData<healthStore.samplePointHelper.dailyActivities.AggregateResult>(aggregateRequest);

  hilog.info(0x0000, 'testTag', 'Succeeded in reading data.');
  aggregateResults.forEach((aggregateResult) => {
    hilog.info(0x0000, 'testTag', `the start time is ${aggregateResult.startTime}.`);
    hilog.info(0x0000, 'testTag', `the end time is ${aggregateResult.endTime}.`);
    Object.keys(aggregateResult.fields).forEach((fieldName) => {
      hilog.info(0x0000, 'testTag', `the sum of ${fieldName} is ${aggregateResult.fields[fieldName].sum}.`);
    });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.requestAuthorizations

requestAuthorizations(context: common.UIAbilityContext, request: AuthorizationRequest): Promise<AuthorizationResponse>

用户授权，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext | 是 | UIAbility上下文。 |
| request | AuthorizationRequest | 是 | 授权请求参数，确保授权参数中的权限已在申请运动健康服务时勾选。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AuthorizationResponse> | Promise对象，返回授权响应结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)，其他错误码请参见[华为账号服务ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common } from '@kit.AbilityKit';

let authorizationParameter: healthStore.AuthorizationRequest = {
  readDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE],
  writeDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE]
}

try {
  let authorizationResponse = await healthStore.requestAuthorizations(this.getUIContext().getHostContext() as common.UIAbilityContext, authorizationParameter);

  hilog.info(0x0000, 'testTag', 'Succeeded in requesting authorization.');
  authorizationResponse.writeDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', `grantedWriteDataType is : ${dataType.name}`);
  });
  authorizationResponse.readDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', `grantedReadDataTypes is : ${dataType.name}`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to request authorization. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.getAuthorizations

getAuthorizations(request: AuthorizationRequest): Promise<AuthorizationResponse>

查询权限，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | AuthorizationRequest | 是 | 查询权限请求参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<AuthorizationResponse> | Promise对象，返回查询权限结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [401](../../errors/ArkTS API错误码.md#section1598111146271) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let queryAuthorizationRequest: healthStore.AuthorizationRequest = {
  readDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE],
  writeDataTypes: [healthStore.exerciseSequenceHelper.DATA_TYPE, healthStore.samplePointHelper.heartRate.DATA_TYPE]
}

try {
  let queryAuthorizationResponse = await healthStore.getAuthorizations(queryAuthorizationRequest);

  hilog.info(0x0000, 'testTag', 'Succeeded in getting authorization.');
  queryAuthorizationResponse.writeDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', `grantedWriteDataType is : ${dataType.name}`);
  });
  queryAuthorizationResponse.readDataTypes.forEach(dataType => {
    hilog.info(0x0000, 'testTag', `grantedReadDataTypes is : ${dataType.name}`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to get authorization. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.cancelAuthorizations

cancelAuthorizations(): Promise<void>

用户取消授权，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)，其他错误码请参见[华为账号服务ArkTS错误码](ArkTS错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthStore.cancelAuthorizations();
  hilog.info(0x0000, 'testTag', 'Succeeded in canceling authorization.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to cancel authorization. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.syncAll

syncAll(): Promise<void>

用户主动触发数据同步，使用Promise异步方式。

**系统能力：**SystemCapability.Health.HealthStore

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在Wearable中返回[801](../../errors/ArkTS API错误码.md#section14722630151713)错误码。

**起始版本：**5.1.0(18)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errors/ArkTS API错误码.md#section383228112410) | Permission verification failed. |
| [801](../../errors/ArkTS API错误码.md#section14722630151713) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [1002700001](../../errors/ArkTS API错误码.md#section153755119333) | System internal error. |
| [1002700002](../../errors/ArkTS API错误码.md#section1210612513414) | Database processing error. |
| [1002701001](../../errors/ArkTS API错误码.md#section140917121405) | Network error. The network is unavailable. |
| [1002702001](../../errors/ArkTS API错误码.md#section673773124213) | Account error. The user has not logged in with HUAWEI ID. |
| [1002702002](../../errors/ArkTS API错误码.md#section1283610451436) | Account error. Failed to obtain account information with HUAWEI ID. |
| [1002703001](../../errors/ArkTS API错误码.md#section9390213122310) | User privacy is not agreed. |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthStore.syncAll();
  hilog.info(0x0000, 'testTag', 'Succeeded in synchronizing data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to synchronize data. Code: ${err.code}, message: ${err.message}`);
}
```

#### healthStore.on('serviceDie')

on(type: 'serviceDie', callback: Callback<void>): void

订阅Health Service Kit进程销毁通知，使用Callback异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | Health Service Kit进程状态的回调类型，支持的事件为：'serviceDie'，当Health Service Kit进程销毁时，触发该事件。 |
| callback | Callback<void> | 是 | 无返回结果的回调函数。 |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

healthStore.on('serviceDie', () => {
  hilog.info(0x0000, 'testTag', 'Succeeded in monitoring the process death.');
});
```

#### healthStore.off('serviceDie')

off(type: 'serviceDie', callback?: Callback<void>): void

取消订阅Health Service Kit进程销毁通知，使用Callback异步回调。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：**SystemCapability.Health.HealthStore

**起始版本：**5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | Health Service Kit进程状态的回调类型，支持的事件为：'serviceDie'，当Health Service Kit进程销毁时，触发该事件。 |
| callback | Callback<void> | 否 | 无返回结果的回调函数。 - callback为空：取消所有callback回调。 - callback非空：取消指定的callback回调。 |


上述接口调用前，需先使用[init](#ZH-CN_TOPIC_0000002522082354__healthstoreinit)方法进行初始化。

**示例：**

```ets
import { healthStore } from '@kit.HealthServiceKit';

healthStore.off('serviceDie');
```