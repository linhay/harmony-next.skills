# weatherService（天气数据服务）

本模块提供天气数据服务。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { weatherService } from '@kit.WeatherServiceKit';
```

#### weatherService.getWeather

getWeather(request: WeatherRequest): Promise<Weather>

天气数据获取接口，使用Promise异步回调。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

request

[WeatherRequest](#section1992347172717)

是

天气数据请求体。

**返回值：**

类型

说明

Promise<[Weather](#section157006480227)>

Promise对象，返回天气数据对象。

**错误码：**

以下错误码的详细介绍请参见天气服务[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

[1011900001](../../errors/ArkTS API错误码.md#section19421613172910)

Capability is not configured.

[1011900002](../../errors/ArkTS API错误码.md#section1210612513414)

The requested longitude and latitude grid point lacks data.

[1011900003](../../errors/ArkTS API错误码.md#section140917121405)

Network error.

[1011900004](../../errors/ArkTS API错误码.md#section673773124213)

System error.

**示例：**

```ets
// 引入
import { weatherService } from '@kit.WeatherServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getWeatherData() {
  // 初始化参数
  let request: weatherService.WeatherRequest = {
    location: {
      latitude: 22.62,
      longitude: 114.07
    },
    // 只请求需要的数据，不设置的话默认请求全量数据
    limitedDatasets: [weatherService.Dataset.CURRENT, weatherService.Dataset.ALERTS]
  }

  // 请求及错误处理
  try {
    let weather = await weatherService.getWeather(request);
    if (weather.current) {
      console.info('getWeather current temperature: ' + weather.current.temperature);
    }
    if (weather.alerts?.length) {
      console.info('getWeather alert: ' + weather.alerts[0].title);
    }
  } catch (err) {
    err = err as BusinessError;
    console.error(`getWeather failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

#### weatherService.getWeatherWithContext

getWeatherWithContext(context: common.Context, request: WeatherRequest): Promise<Weather>

根据调用方提供的上下文信息获取天气数据，使用Promise异步回调。

**元服务API：**从版本5.0.2(14)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.2(14)

**参数：**

**参数名**

**类型**

必填

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common#context)

是

上下文，目前只支持[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)或[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)的上下文环境。

request

[WeatherRequest](#section1992347172717)

是

天气数据请求体。

**返回值：**

类型

说明

Promise<[Weather](#section157006480227)>

Promise对象，返回天气数据对象。

**错误码：**

以下错误码的详细介绍请参见天气服务[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

[401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section401-参数检查失败)

Parameter error.

[1011900001](../../errors/ArkTS API错误码.md#section19421613172910)

Capability is not configured.

[1011900002](../../errors/ArkTS API错误码.md#section1210612513414)

The requested longitude and latitude grid point lacks data.

[1011900003](../../errors/ArkTS API错误码.md#section140917121405)

Network error.

[1011900004](../../errors/ArkTS API错误码.md#section673773124213)

System error.

**示例：**

```ets
// 引入
import { UIAbility } from '@kit.AbilityKit';
import { weatherService } from '@kit.WeatherServiceKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { taskpool } from '@kit.ArkTS';

@Concurrent
async function getWeatherData(context: common.Context) {
  let request: weatherService.WeatherRequest = {
    location: {
      latitude: 22.62,
      longitude: 114.07
    },
    // 只请求需要的数据，不设置的话默认请求全量数据
    limitedDatasets: [weatherService.Dataset.CURRENT, weatherService.Dataset.ALERTS]
  }

  // 请求及错误处理
  try {
    let weather = await weatherService.getWeatherWithContext(context, request);
    if (weather.current) {
      console.info('getWeatherWithContext current temperature: ' + weather.current.temperature);
    }
    if (weather.alerts?.length) {
      console.info('getWeatherWithContext alert: ' + weather.alerts[0].title);
    }
  } catch (err) {
    err = err as BusinessError;
    console.error(`getWeatherWithContext failed. Code: ${err.code}, message: ${err.message}`);
  }
}

function executeGetWeather(context: common.Context) {
  taskpool.execute(getWeatherData, context);
}

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    executeGetWeather(this.context);
  }
}
```

#### WeatherRequest

天气数据请求类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

location

[Location](#section188316932819)

否

否

位置信息。

limitedDatasets

[Dataset](#section83091727192814)[]

否

是

接口只返回列表中指定的数据类型，若未设置或数组为空，默认返回全量数据。

#### Location

位置信息。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

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

取值范围：[-90, 90]。

longitude

number

否

否

经度。

取值范围：[-180, 180]。

#### Weather

天气数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

current

[CurrentWeather](#section0966121642920)

否

是

实况天气，若设置了limitedDatasets且数组中不包含[Dataset](#section83091727192814).CURRENT，该字段不返回。

daily

[Forecast](#section1528522182918)<[DailyWeather](#section123711629162919)>

否

是

多日预报，若设置了limitedDatasets且数组中不包含[Dataset](#section83091727192814).DAILY，该字段不返回。

hourly

[Forecast](#section1528522182918)<[HourlyWeather](#section0211544202918)>

否

是

逐小时预报，若设置了limitedDatasets且数组中不包含[Dataset](#section83091727192814).HOURLY，该字段不返回。

minute

[Forecast](#section1528522182918)<[MinuteWeather](#section938117524293)>

否

是

分钟级降水预报，若设置了limitedDatasets且数组中不包含[Dataset](#section83091727192814).MINUTE，或者该区域短期无降水，该字段不返回。

alerts

[WeatherAlert](#section8376165133019)[]

否

是

天气预警，若设置了limitedDatasets且数组中不包含[Dataset](#section83091727192814).ALERTS，或者该区域当前无预警，该字段不返回。

indices

[WeatherIndex](#section1635416963019)[]

否

是

天气指数，若设置了limitedDatasets且数组中不包含[Dataset](#section83091727192814).INDICES，该字段不返回。

tides

[Tide](#section1082471633017)[]

否

是

潮汐，若设置了limitedDatasets且数组中不包含[Dataset](#section83091727192814).TIDES，或者该区域无潮汐站点，该字段不返回。

metadata

[WeatherMetadata](#section19686182312309)

否

否

天气数据元数据。

attributions

[WeatherAttribution](#section7105153453010)[]

否

否

天气数据的归因。

#### CurrentWeather

实况天气数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

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

单位：℃。

apparentTemperature

number

否

否

体感温度。

单位：℃。

humidity

number

否

否

相对湿度。

例如湿度为30%，本字段返回30。

pressure

number

否

否

地面气压。

单位：hPa。

pressureTrend

[PressureTrend](#section69911219313)

否

否

气压趋势。

wind

[Wind](#section2353114611314)

否

否

风力风向。

cloudCover

number

否

否

云量。

例如云量为30%，本字段返回30。

condition

[WeatherCondition](#section10699512153212)

否

否

天气现象。

uvIndex

[UVIndex](#section7981132253218)

否

否

紫外线指数。

aqi

[WeatherAqi](#section10621192719325)

否

是

空气质量。

visibility

number

否

否

能见度。

单位：km。

updateTime

Date

否

否

数据更新时间，UTC时间格式。

expirationTime

Date

否

否

数据失效时间，UTC时间格式。

summary

string

否

是

实况天气一句话描述。

#### Forecast<T>

预报类天气集合。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

forecast

T[]

否

否

预报数据集合。

updateTime

Date

否

否

数据更新时间，UTC时间格式。

expirationTime

Date

否

否

数据失效时间，UTC时间格式。

summary

string

否

是

预报数据一句话描述，只有分钟级降水预报会返回该字段。

#### DailyWeather

多日天气数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

date

Date

否

否

日期，精确到天，UTC时间格式。

highTemperature

number

否

否

高温。

单位：℃。

lowTemperature

number

否

否

低温。

单位：℃。

highApparentTemperature

number

否

否

体感温度高温。

单位：℃。

lowApparentTemperature

number

否

否

体感温度低温。

单位：℃。

uvIndex

[UVIndex](#section7981132253218)

否

否

紫外线指数。

aqi

[WeatherAqi](#section10621192719325)

否

是

空气质量。

visibility

number

否

否

能见度。

单位：km。

moon

[MoonEvents](#section1446317353338)

否

否

月出/月落时间，月相等信息。

sun

[SunEvents](#section1799124063311)

否

否

日出/日落时间。

daytimeForecast

[DayPartForecast](#section165511045173319)

否

否

白天天气数据。

overnightForecast

[DayPartForecast](#section165511045173319)

否

否

夜晚天气数据。

pressure

number

否

否

地面气压。

单位：hPa。

#### HourlyWeather

小时天气数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

date

Date

否

否

日期， 精确到小时，UTC时间格式。

temperature

number

否

否

温度。

单位：℃。

apparentTemperature

number

否

否

体感温度。

单位：℃。

humidity

number

否

否

相对湿度。

例如湿度为30%，本字段返回30。

wind

[Wind](#section2353114611314)

否

否

风力风向。

cloudCover

number

否

否

云量。

例如云量为30%，本字段返回30。

condition

[WeatherCondition](#section10699512153212)

否

否

天气现象。

uvIndex

[UVIndex](#section7981132253218)

否

否

紫外线等级。

aqi

[WeatherAqi](#section10621192719325)

否

是

空气质量。

visibility

number

否

否

能见度。

单位：km。

precipitationProbability

number

否

否

降水概率。

precipitationAmount

number

否

否

降水量。

单位：mm。

#### MinuteWeather

分钟级降水数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

date

Date

否

否

日期， 精确到分钟，UTC时间格式。

precipitation

[Precipitation](#section56681655183416)

否

否

降水类型。

precipitationIntensity

number

否

否

降水密度。

取值范围：[0, 1]。

#### WeatherAlert

天气预警信息类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

updateTime

Date

否

否

数据更新时间，UTC时间格式。

expirationTime

Date

否

否

数据失效时间，UTC时间格式。

id

string

否

否

预警id。

title

string

否

否

预警标题。

region

string

否

是

预警区域。

level

[AlertLevel](#section1696618143515)

否

否

预警等级。

levelDescription

string

否

否

预警等级描述。

type

[AlertType](#section162382144356)

否

否

预警类型。

typeDescription

string

否

否

预警类型描述。

content

string

否

否

预警正文。

guide

string

否

是

预警防御指南。

detailsUrl

string

否

是

预警详情链接。

source

string

否

否

预警来源。

icon

[resourceManager.Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#resource9)

否

是

预警图标。

#### WeatherIndex

天气指数数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

updateTime

Date

否

否

数据更新时间，UTC时间格式。

expirationTime

Date

否

否

数据失效时间，UTC时间格式。

type

[WeatherIndexType](#section13240134383517)

否

否

指数类型。

name

string

否

否

指数名称。

dailyItems

[DailyIndex](#section1130118559352)[]

否

否

每天的指数详情。

#### Tide

潮汐数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

updateTime

Date

否

否

数据更新时间，UTC时间格式。

expirationTime

Date

否

否

数据失效时间，UTC时间格式。

stationId

string

否

否

潮汐站点id。

stationName

string

否

否

潮汐站点名称。

hourlyTides

[HourlyTide](#section1911611318363)[]

否

否

小时潮汐数据。

#### WeatherMetadata

天气元数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

requestTime

Date

否

否

接口请求时间，UTC时间格式。

version

string

否

否

天气服务版本。

timeZone

string

否

是

接口请求目的地的时区。

#### WeatherAttribution

天气数据归因类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

serviceName

string

否

否

数据供应商名称。

legalPageUrl

string

否

否

归因页面链接。

#### Wind

风力风向数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

direction

[CompassDirection](#section415174943216)

否

否

风向。

speed

number

否

否

风速。

单位：km/h。

level

number

否

否

风力级别。

gustDirection

[CompassDirection](#section415174943216)

否

是

阵风风向。

gustSpeed

number

否

是

阵风风速。

单位：km/h。

gustLevel

number

否

是

阵风风力级别。

#### WeatherCondition

天气现象数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

type

[ConditionType](#section1715644153214)

否

否

天气现象类型。

icon

[resourceManager.Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#resource9)

否

否

天气现象图标。

description

string

否

否

天气现象描述。

#### UVIndex

紫外线指数数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

category

[ExposureCategory](#section34333283311)

否

否

紫外线暴露类别。

value

number

否

否

紫外线等级。

description

string

否

否

紫外线等级描述。

#### WeatherAqi

空气质量数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

no2

number

否

是

二氧化氮浓度。

单位：μg/m3。

o3

number

否

是

臭氧浓度。

单位：μg/m3。

pm10

number

否

是

PM10浓度。

单位：μg/m3。

pm25

number

否

是

PM2.5浓度。

单位：μg/m3。

so2

number

否

是

二氧化硫浓度。

单位：μg/m3。

co

number

否

是

一氧化碳浓度。

单位：μg/m3。

aqiValue

number

否

否

空气质量数值。

aqiCategory

[AqiCategory](#section13959324356)

否

否

空气质量类别。

aqiDescription

string

否

否

空气质量类别描述。

#### MoonEvents

月出/月落时间，月相等信息类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

moonrise

Date

否

否

月出时间，UTC时间格式。

moonset

Date

否

否

月落时间，UTC时间格式。

phase

[MoonPhase](#section1559611811347)

否

否

月相。

illuminatedFraction

number

否

是

月面照亮比例。

例如比例为30%，本字段返回30。

age

number

否

是

月龄。

#### MoonPhase

月相信息类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

type

[MoonPhaseType](#section01843323411)

否

否

月相类型。

description

string

否

否

月相描述。

icon

[resourceManager.Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#resource9)

否

否

月相图标。

#### SunEvents

日出/日落信息类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

sunrise

Date

否

否

日出时间，UTC时间格式。

sunset

Date

否

否

日落时间，UTC时间格式。

#### DayPartForecast

全天部分时段天气信息类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

wind

[Wind](#section2353114611314)

否

否

风力风向。

humidity

number

否

否

相对湿度。

例如湿度为30%，本字段返回30。

cloudCover

number

否

否

云量。

例如云量为30%，本字段返回30。

condition

[WeatherCondition](#section10699512153212)

否

否

天气现象。

precipitationProbability

number

否

否

降水概率。

precipitationAmount

number

否

否

降水量。

单位：mm。

rainfallProbability

number

否

是

降雨概率。

rainfallAmount

number

否

是

降雨量。

单位：mm。

snowfallProbability

number

否

是

降雪概率。

snowfallAmount

number

否

是

降雪量。

单位：mm。

#### DailyIndex

每天天气指数数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

date

Date

否

否

日期，精确到天，UTC时间格式。

level

number

否

否

指数级别。

levelDescription

string

否

否

指数级别描述。

content

string

否

否

指数内容。

#### HourlyTide

小时潮汐数据类。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

date

Date

否

否

日期，精确到小时，UTC时间格式。

category

[TideCategory](#section6932142214363)

否

是

潮汐类型。

height

number

否

否

潮汐高度。

单位：cm。

#### Dataset

数据集枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

CURRENT

0

实况天气。

DAILY

1

多日预报。

HOURLY

2

逐小时预报。

MINUTE

3

分钟级降水预报。

ALERTS

4

天气预警。

INDICES

5

天气指数。

TIDES

6

潮汐。

#### PressureTrend

气压趋势枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

UNDEFINED

0

未定义。

FALLING

1

下降。

RISING

2

上升。

STEADY

3

稳定。

#### ConditionType

天气现象类型枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

UNDEFINED

0

未定义

SUNNY

1

晴

MOSTLY_SUNNY

2

多云

PARTLY_SUNNY

3

多云

INTERMITTENT_CLOUDS

4

多云

HAZY_SUNSHINE

5

霾

MOSTLY_CLOUDY

6

多云

CLOUDY

7

多云

OVERCAST

8

阴

FOG

11

雾

SHOWERS

12

阵雨

MOSTLY_CLOUDY_WITH_SHOWERS

13

阵雨

PARTLY_SUNNY_WITH_SHOWERS

14

阵雨

T_STORMS

15

雷阵雨

MOSTLY_CLOUDY_WITH_T_STORMS

16

雷阵雨

PARTLY_SUNNY_WITH_T_STORMS

17

雷阵雨

RAIN

18

雨

FLURRIES

19

阵雪

MOSTLY_CLOUDY_WITH_FLURRIES

20

阵雪

PARTLY_SUNNY_WITH_FLURRIES

21

阵雪

SNOW

22

雪

MOSTLY_CLOUDY_WITH_SNOW

23

雪

ICE

24

雪

SLEET

25

雨夹雪

FREEZING_RAIN

26

雨

RAIN_AND_SNOW

29

雨夹雪

HOT

30

炎热

COLD

31

寒冷

WINDY

32

有风

CLEAR

33

晴

MOSTLY_CLEAR

34

多云

PARTLY_CLOUDY

35

多云

INTERMITTENT_CLOUDS_NIGHT

36

多云

HAZY_MOONLIGHT

37

霾

MOSTLY_CLOUDY_NIGHT

38

多云

PARTLY_CLOUDY_WITH_SHOWERS

39

阵雨

MOSTLY_CLOUDY_WITH_SHOWERS_NIGHT

40

阵雨

PARTLY_CLOUDY_WITH_T_STORMS

41

雷阵雨

MOSTLY_CLOUDY_WITH_T_STORMS_NIGHT

42

雷阵雨

MOSTLY_CLOUDY_WITH_FLURRIES_NIGHT

43

阵雪

MOSTLY_CLOUDY_WITH_SNOW_NIGHT

44

雪

THUNDERSHOWER_WITH_HAIL

45

冰雹

LIGHT_RAIN

46

小雨

MODERATE_RAIN

47

中雨

HEAVY_RAIN

48

大雨

STORM

49

暴雨

HEAVY_STORM

50

暴雨

SEVERE_STORM

51

特大暴雨

LIGHT_SNOW

52

阵雪

MODERATE_SNOW

53

中雪

HEAVY_SNOW

54

大雪

SNOWSTORM

55

暴雪

DUST_STORM

56

沙尘暴

LIGHT_TO_MODERATE_RAIN

57

中雨

MODERATE_TO_HEAVY_RAIN

58

大雨

HEAVY_RAIN_TO_STORM

59

暴雨

STORM_TO_HEAVY_STORM

60

暴雨

HEAVY_TO_SEVERE_STORM

61

特大暴雨

LIGHT_TO_MODERATE_SNOW

62

中雪

MODERATE_TO_HEAVY_SNOW

63

大雪

HEAVY_SNOW_TO_SNOWSTORM

64

暴雪

DUST

65

浮尘

SAND

66

扬沙

SANDSTORM

67

强沙尘暴

DENSE_FOGGY

68

雾

MODERATE_FOGGY

69

雾

MODERATE_HAZE

70

霾

HEAVY_HAZE

71

霾

SEVERE_HAZE

72

霾

HEAVY_FOGGY

73

雾

SEVERE_FOGGY

74

雾

OVERCAST_NIGHT

75

阴

BLOWING_SNOW

76

阵雪

#### CompassDirection

指针方向枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

UNDEFINED

0

未定义。

NORTH

1

北。

NORTH_EAST

2

东北。

EAST

3

东。

SOUTH_EAST

4

东南。

SOUTH

5

南。

SOUTH_WEST

6

西南。

WEST

7

西。

NORTH_WEST

8

西北。

#### ExposureCategory

紫外线暴露程度枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

UNDEFINED

0

未定义。

VERY_LOW

1

最弱。

LOW

2

弱。

MODERATE

3

中等。

HIGH

4

强。

VERY_HIGH

5

很强。

#### MoonPhaseType

月相类别枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

UNDEFINED

0

未定义。

NEW

1

新月。

WAXING_CRESCENT

2

娥眉月。

FIRST_QUARTER

3

上弦月。

WAXING_GIBBOUS

4

渐盈凸月。

FULL

5

满月。

WANING_GIBBOUS

6

渐盈凸月。

LAST_QUARTER

7

下弦月。

WANING_CRESCENT

8

残月。

#### Precipitation

降水类型枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

NONE

0

无降水。

HAIL

1

冰雹。

RAIN

2

雨。

SLEET

3

雨夹雪。

SNOW

4

雪。

#### AlertLevel

预警级别枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

BLUE

1

蓝色预警。

YELLOW

2

黄色预警。

ORANGE

3

橙色预警。

RED

4

红色预警。

OTHER

5

其他。

WHITE

6

白色预警。

BLACK

7

黑色预警。

#### AlertType

预警类型枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

TYPHOON

1

台风。

RAIN_STORM

2

暴雨

SNOW_STORM

3

暴雪。

COLD_WAVE

4

寒潮。

GALE

5

大风。

SAND_STORM

6

沙尘暴。

HEAT_WAVE

7

高温。

DROUGHT

8

干旱。

LIGHTNING

9

雷电。

HAIL

10

冰雹。

FROST

11

霜冻。

HEAVY_FOG

12

大雾。

HAZE

13

霾。

ROAD_ICING

14

道路结冰。

OTHER

15

其他。

THUNDER_AND_GALE

17

雷电大风。

FOREST_FIRE_RISK

18

森林火险。

COLD

19

寒冷。

DUST_HAZE

20

灰霾。

COOLING

21

降温。

ROAD_ICE_AND_SNOW

22

道路冰雪。

DRY_HOT_WIND

23

干热风。

HAZE_VERY_UNHEALTHY

24

空气重污染。

FROZEN

25

冰冻。

HEAVY_FOG_AT_SEA

26

海上大雾。

THUNDERSTORM_AND_GALE

27

雷暴大风。

CONTINUOUS_LOW_TEMPERATURE

28

持续低温。

THICK_DUST

29

浓浮尘。

TORNADO

30

龙卷风。

LOW_TEMPERATURE_FREEZE_INJURY

31

低温冻害。

GALE_AT_SEA

32

海上大风。

LOW_TEMPERATURE_FREEZING_RAIN_AND_SNOW

33

低温雨雪冰冻。

SEVERE_CONVECTION

34

强对流。

OZONE

35

臭氧。

HEAVY_SNOW

36

大雪。

HEAVY_RAINFALL

37

强降雨。

STRONG_COOLING

38

强降温。

SNOW_DISASTER

39

雪灾。

FOREST_GRASSLAND_FIRE_RISK

40

森林（草原）火险。

THUNDERSTORM

41

雷暴。

SEVERE_COLD

42

严寒。

SAND_DUST

43

沙尘。

THUNDERSTORM_AND_GALE_AT_SEA

44

海上雷雨大风。

LIGHTNING_AT_SEA

45

海上雷电。

TYPHOON_AT_SEA

46

海上台风。

LOW_TEMPERATURE

47

低温。

GEOLOGICAL_HAZARD

48

地质灾害。

GEOLOGICAL_HAZARD_AND_METEOROLOGICAL_RISK

49

地质灾害气象风险。

FLUSH_FLOOD

50

山洪。

GRASSLAND_FIRE_RISK

51

草原火险。

THUNDER_RAIN_AND_GALE

52

雷雨大风。

#### AqiCategory

空气质量类别枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

UNDEFINED

0

未定义。

EXCELLENT

1

优质。

GOOD

2

良。

SLIGHT

3

轻度污染。

MODERATE

4

中度污染。

HEAVY

5

重度污染。

SEVERE

6

严重污染。

#### WeatherIndexType

天气指数类型枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

UNDEFINED

0

未定义。

DRESSING

1

穿衣指数。

MOTION

2

运动指数。

COLD

3

感冒指数。

CAR_WASHING

4

洗车指数。

TOURISM

5

旅游指数。

SUN_PROTECTION

7

防晒指数。

FISHING

8

钓鱼指数。

MORNING_EXERCISE

10

晨练指数。

ALLERGY

24

过敏指数。

SKIING

31

滑雪指数。

STARGAZING

34

观星指数。

#### TideCategory

潮汐类别枚举。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Weather.Core

**设备行为差异：**对于API 17及之前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无法使用。对于API 18及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable中均可正常使用。

**起始版本：**5.0.0(12)

名称

值

说明

UNDEFINED

0

未定义。

HIGH

1

潮高。

LOW

2

潮低。