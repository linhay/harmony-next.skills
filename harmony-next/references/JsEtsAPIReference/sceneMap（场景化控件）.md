# sceneMap（场景化控件）

本模块提供地图场景化控件功能，包括地点详情展示控件、地点选取控件和区划选择控件。

**起始版本：**4.1.0(11)

#### 导入模块

```ets
import { sceneMap } from '@kit.MapKit';
```

#### queryLocation

queryLocation(context: common.UIAbilityContext, options: LocationQueryOptions): Promise<void>

根据提供的参数拉起地点详情展示控件。使用Promise异步回调。

- 此函数必须在ArkUI页面上下文中调用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)或[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)所对应的context。

options

[LocationQueryOptions](#section971194972117)

是

查询地点详情参数。

**返回值：**

类型

说明

Promise<void>

Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

1002600001

System internal error.

1002600002

Failed to connect to the Map Kit server.

1002600003

App authentication failed.

1002600004

The Map permission is not enabled.

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let queryLocationOptions: sceneMap.LocationQueryOptions = { siteId: "922207154068557824" };
sceneMap.queryLocation(this.getUIContext().getHostContext() as common.UIAbilityContext, queryLocationOptions)
  .then(() => {
    console.info("QueryLocation", "Succeeded in querying location.");
  })
  .catch((err: BusinessError) => {
    console.error("QueryLocation", `Failed to query Location, code: ${err.code}, message: ${err.message}`);
  });
```

#### chooseLocation

chooseLocation(context: common.UIAbilityContext, options: LocationChoosingOptions): Promise<LocationChoosingResult>

根据提供的参数拉起地点选取控件。使用Promise异步回调。

- 此函数必须在ArkUI页面上下文中调用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：**4.1.0(11)

**参数：**

**参数名**

**类型**

必填

**说明**

context

common.[UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)或[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)所对应的context。

options

[LocationChoosingOptions](#section1313113517227)

是

地点选取参数。

**返回值：**

类型

说明

Promise<[LocationChoosingResult](#section0471517192216)>

Promise对象，返回[LocationChoosingResult](#section0471517192216)。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

1002600001

System internal error.

1002600002

Failed to connect to the Map Kit server.

1002600003

App authentication failed.

1002600004

The Map permission is not enabled.

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let locationChoosingOptions: sceneMap.LocationChoosingOptions = {
  location: { latitude: 39.92194051376904, longitude: 116.3971836796932 },
  searchEnabled: true,
  showNearbyPoi: true
};
sceneMap.chooseLocation(this.getUIContext().getHostContext() as common.UIAbilityContext, locationChoosingOptions)
  .then((data) => {
    console.info("ChooseLocation", "Succeeded in choosing location.");
  })
  .catch((err: BusinessError) => {
    console.error("ChooseLocation", `Failed to choose Location, code: ${err.code}, message: ${err.message}`);
  });
```

#### selectDistrict

selectDistrict(context: common.Context, options: DistrictSelectOptions): Promise<DistrictSelectResult>

根据提供的参数调出区划选择页面。使用Promise异步回调。

- 此函数必须在ArkUI页面上下文中调用。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

**参数名**

**类型**

必填

**说明**

context

[common.Context](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context)

是

[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)或[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability)所对应的context。

options

[DistrictSelectOptions](#section17211958161110)

是

区划选择页面初始选项。

**返回值：**

类型

说明

Promise<[DistrictSelectResult](#section3745121172118)>

Promise对象，返回[DistrictSelectResult](#section3745121172118)。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid input parameter.

1002600001

System internal error.

1002600002

Failed to connect to the Map Kit server.

1002600003

App authentication failed.

1002600004

The Map permission is not enabled.

1002600012

The country code is not supported.

801

Capability not supported. Failed to call the API due to limited device capabilities.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let districtSelectOptions: sceneMap.DistrictSelectOptions = {
  countryCode: "CN"
};
sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
  console.info("SelectDistrict", "Succeeded in selecting district.");
}).catch((err: BusinessError) => {
  console.error("SelectDistrict", `Failed to select district, code: ${err.code}, message: ${err.message}`);
});
```

#### LocationQueryOptions

查询地点详情的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

siteId

string

否

是

地点详情页的地点ID。

siteId可通过[MapEventManager](MapEventManager.md)中[on](MapEventManager.md#section0279247143911)(type: 'poiClick', callback: Callback<[mapCommon.Poi](mapCommon（地图属性模型）.md#section1155919456273)>)方法获取。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

language

string

否

是

语言，请参见[地图Picker支持语言](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-language#section167751124121111)，如果未设置，默认使用系统语言。异常值按默认值处理。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

location

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

是

地图中心点坐标。如果没有siteId，使用location查询地点详情。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

name

string

否

是

地点的名称。如果没有siteId，使用name作为location的名称标注。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

address

string

否

是

地点的地址。如果没有siteId，使用address作为location的地址标注。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

showBusiness

boolean

否

是

是否显示商业信息（如打车），默认值为true。

- true：显示
- false：不显示

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

 说明：

版本4.1.0(11)~5.1.1(19)为预留字段，从版本6.0.0(20)开始使用。

themeColor

[CustomColors](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme#customcolors)

否

是

自定义主题颜色对象，默认为brand（品牌色）。

**起始版本：**5.0.3(15)

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

cancelCallback

Callback<void>

否

是

回调函数。无返回结果的回调函数。地点详情控件关闭事件回调。

**起始版本：**5.0.3(15)

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

transitionDuration

number

否

是

转场动效时间，默认值：-1，取值范围[0, Number.MAX_VALUE），异常值将按照默认值-1处理，保持[interpolatingSpring](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve#curvesinterpolatingspring10)(0.5, 1, 328, 36)。2in1设备当前不显示转场动效，该配置不生效。

**起始版本：**6.0.2(22)

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

以下两组参数，至少传入其中一组，如果都传入，以siteId为主。

- siteId
- location、name

**示例：**

```ets
let queryLocationOptions: sceneMap.LocationQueryOptions = { siteId: "922207154068557824" };
```

#### LocationChoosingOptions

地点选取的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

location

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

是

地图中心点坐标。

如果参数未传，使用设备当前位置作为中心点；如果未获取到设备当前位置，默认以故宫博物院为中心点。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

language

string

否

是

语言，请参见[地图Picker支持语言](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-language#section167751124121111)，如果未设置，默认使用系统语言。异常值按默认值处理。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

poiTypes

Array<string>

否

是

指定需要展示的POI类别。取值范围参见[HwLocationType](POI类型值.md#section1662744719618)。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

searchEnabled

boolean

否

是

是否展示搜索控件，默认值为false，异常值按默认值处理。

- true：展示
- false：不展示

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

showNearbyPoi

boolean

否

是

是否展示附近POI，默认值为false，异常值按默认值处理。

- true：展示
- false：不展示

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

snapshotEnabled

boolean

否

是

是否返回映射快照，默认值为false。

- true：返回
- false：不返回

**起始版本：**5.0.0(12)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

themeColor

[CustomColors](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme#customcolors)

否

是

自定义主题颜色对象，默认为brand（品牌色）。

**起始版本：**5.0.3(15)

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

cancelCallback

Callback<void>

否

是

回调函数。无返回结果的回调函数。地点选取控件关闭事件回调。

**起始版本：**5.0.3(15)

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

transitionDuration

number

否

是

转场动效时间，默认值：-1，取值范围[0, Number.MAX_VALUE），异常值将按照默认值-1处理，保持[interpolatingSpring](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve#curvesinterpolatingspring10)(0.5, 1, 328, 36)。2in1设备当前不显示转场动效，该配置不生效。

**起始版本：**6.0.2(22)

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**示例：**

```ets
let locationChoosingOptions: sceneMap.LocationChoosingOptions = {
  location: {latitude: 39.9, longitude: 116.4},
  language: "en"
};
```

#### LocationChoosingResult

地点选取的返回结果。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：**4.1.0(11)

**名称**

**类型**

只读

可选

**说明**

siteId

string

否

是

选点的地点ID。如果选点非POI，则不返回。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

location

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

否

选点的坐标点。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

name

string

否

是

选点的POI名称。如果选点非POI，则返回的name值为"标记点"。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

address

string

否

否

选点地址。

**元服务API：**从版本4.1.0(11)开始，该接口支持在元服务中使用。

addressComponent

[site.AddressComponent](site（地点搜索）.md#section1652881563212)

否

是

选点地址的详细信息。

**起始版本：**5.0.0(12)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

zoom

number

否

否

选点地址的缩放层级，取值范围：[2, 20]，超出按边界值处理。

**起始版本：**5.0.0(12)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

snapshot

[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

否

是

地图快照。

**起始版本：**5.0.0(12)

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

#### DistrictSelectOptions

区划选择页面初始选项。

**模型约束：**此接口仅可在Stage模型下使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

countryCode

string

否

是

查询指定国家或地区的行政区划，国家或地区码必须符合ISO 3166-1 alpha-2规则。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

language

string

否

是

设置页面语言，请参见[地图Picker支持语言](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-language#section167751124121111)，如果未设置，默认使用系统语言。异常值按默认值处理。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

address

string

否

是

指定地址查询。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

themeColor

[CustomColors](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme#customcolors)

否

是

自定义主题颜色对象，默认为brand（品牌色）。

**起始版本：**5.0.3(15)

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

subWindowEnabled

boolean

否

是

是否在子窗口中显示区划选择，默认值为false。

- true：在子窗口中显示
- false：不在子窗口中显示

**起始版本：**5.0.3(15)

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

cancelCallback

Callback<void>

否

是

回调函数。无返回结果的回调函数。区划选择控件关闭事件回调。

**起始版本：**5.0.3(15)

**元服务API：**从版本5.0.3(15)开始，该接口支持在元服务中使用。

transitionDuration

number

否

是

转场动效时间，默认值：-1，取值范围[0, Number.MAX_VALUE），异常值将按照默认值-1处理，保持[interpolatingSpring](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve#curvesinterpolatingspring10)(0.5, 1, 328, 36)。当subWindowEnabled为true时该配置不生效。

**起始版本：**6.0.2(22)

**元服务API：**从版本6.0.2(22)开始，该接口支持在元服务中使用。

**示例：**

```ets
let districtSelectOptions: sceneMap.DistrictSelectOptions = {
  countryCode: "CN",
  language:"zh",
  address: "河南"
};
```

#### DistrictSelectResult

区划选择请求的结果。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

districts

Array<[District](#section1818842852518)>

否

否

所选行政区划的级别信息。

addressDescription

string

否

是

返回所选行政区划的地址信息。

#### District

行政区划信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.Map.Core

**设备行为差异：**该接口在phone、tablet和2in1设备上可以正常使用，在其他设备中返回801错误码。

**起始版本：**5.0.0(12)

**名称**

**类型**

只读

可选

**说明**

siteId

string

否

是

区划的地点ID。

name

string

否

是

区划的名称。

location

[mapCommon.LatLng](mapCommon（地图属性模型）.md#section20691173773810)

否

是

区划的坐标点

adminLevel

string

否

是

区划级别，分国家、省份、城市、区/县和街道五个区划级别。

 说明：

国家：COUNTRY

省份：ADMINISTRATIVE_AREA_LEVEL_1

城市：ADMINISTRATIVE_AREA_LEVEL_2

区/县：ADMINISTRATIVE_AREA_LEVEL_3

街道：ADMINISTRATIVE_AREA_LEVEL_4

adminCode

string

否

是

[行政区划码](城市码及区划代码表.md)。

 说明：

接口返回的行政区划码覆盖中国大陆及港澳地区，包括省份、城市、区/县、乡镇/街道等层级，文档附录中仅提供部分城市行政区划码示例。

cityCode

string

否

是

[城市码](城市码及区划代码表.md)。

countryCode

string

否

是

国家/地区码。