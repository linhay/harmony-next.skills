# atomicService（融合场景化API）

本模块为开发者提供获取系统信息、系统设置、关注组件等能力。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.atomicservice

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { atomicService } from '@kit.ScenarioFusionKit';
```

#### SystemSettingInfo

该类提供获取系统设置属性的对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.atomicservice

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

bluetoothEnabled

boolean

否

是

蓝牙系统开关。“true”表示开关已打开，“false”表示开关已关闭。

locationEnabled

boolean

否

是

地理位置的系统开关。“true”表示开关已打开，“false”表示开关已关闭。

wifiEnabled

boolean

否

是

Wi-Fi 的系统开关。“true”表示开关已打开，“false”表示开关已关闭。

deviceOrientation

string

否

是

设备当前显示的方向。“portrait”表示竖屏，“landscape”表示横屏。

#### SystemInfo

该类提供获取系统信息属性的对象。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.atomicservice

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

brand

string

否

是

设备品牌名称。

deviceModel

string

否

是

设备类型。

 说明：

返回值中如果出现特殊字符，需要进行转义。

screenWidth

number

否

是

屏幕的宽度，单位px。

screenHeight

number

否

是

屏幕的高度，单位px。

statusBarHeight

number

否

是

状态栏的高度，单位px。

screenSafeArea

[window.AvoidArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i#avoidarea7)

否

是

竖屏正方向下的安全区域。

language

string

否

是

系统语言。

osFullName

string

否

是

系统版本。

fontSizeSetting

number

否

是

显示设备逻辑像素的密度，代表物理像素与逻辑像素的缩放系数，计算方式为：

该参数为浮点数，受[densityDPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)范围限制，取值范围在[0.5，4.0]。一般取值1.0、3.0等，实际取值取决于不同设备提供的[densityDPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)。

sdkApiVersion

number

否

是

系统软件API版本。

bluetoothEnabled

boolean

否

是

蓝牙系统开关。“true”表示开关已打开，“false”表示开关已关闭。

locationEnabled

boolean

否

是

地理位置的系统开关。“true”表示开关已打开，“false”表示开关已关闭。

wifiEnabled

boolean

否

是

Wi-Fi 的系统开关。“true”表示开关已打开，“false”表示开关已关闭。

deviceOrientation

string

否

是

设备当前显示的方向。“portrait”表示竖屏，“landscape”表示横屏。

theme

[ColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-environment-variables#colormode)

否

是

深浅色模式，可选值为：

- ColorMode.LIGHT：浅色模式；

- ColorMode.DARK：深色模式。

windowWidth

number

否

是

可使用窗口宽度，单位px，该参数应为整数。

windowHeight

number

否

是

可使用窗口高度，单位px，该参数应为整数。

#### FollowResult

该枚举定义了关注结果的类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.1(21)

名称

值

说明

SUCCESS

0

关注成功。

FAILED

1

关注失败。

#### FollowComponentParams

获取关注组件的参数。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.1(21)

名称

类型

只读

可选

说明

pubId

string

否

否

服务号ID。从华为开发者联盟服务号管理页面获取，长度限制1~64位字符。

channelId

string

否

是

渠道ID。长度限制0~32位字符，只能是数字或字母。用于识别组件关注的来源渠道。

offset

[Position](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#position) | [Edges](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#edges12) | [LocalizedEdges](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#localizededges12)

否

是

组件放置位置，基于屏幕中心点的位置偏移。

默认值：{ x: 0, y: 300 }

#### FollowComponentCallback

关注组件的回调接口。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.1(21)

名称

类型

只读

可选

说明

onFollowComplete

AsyncCallback<[FollowCompleteResult](#section163417717564)>

否

否

回调函数。当关注操作成功，err为undefined，data为获取到的FollowCompleteResult；否则为错误对象。

#### FollowCompleteResult

该接口定义了关注组件关注结果的返回体。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.atomicservice

**起始版本：**6.0.1(21)

名称

类型

只读

可选

说明

code

[FollowResult](#section16831162003419)

否

否

关注组件返回结果。关注成功：FollowResult.SUCCESS，关注失败：FollowResult.FAILED。

#### SystemInfoType

type SystemInfoType = 'brand' | 'deviceModel' | 'screenWidth' | 'screenHeight' | 'statusBarHeight'

| 'screenSafeArea' | 'language' | 'osFullName' | 'fontSizeSetting' | 'sdkApiVersion' | 'bluetoothEnabled'

| 'locationEnabled' | 'wifiEnabled' | 'deviceOrientation' | 'theme' | 'windowWidth' | 'windowHeight'

系统信息属性取值类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：**对于5.0.0(12)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、Wearable、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

类型

说明

'brand'

设备品牌名称。

'deviceModel'

设备类型。

'screenWidth'

屏幕的宽度。

'screenHeight'

屏幕的高度。

'statusBarHeight'

状态栏的高度。

'screenSafeArea'

竖屏正方向下的安全区域。

'language'

系统语言。

'osFullName'

系统版本。

'fontSizeSetting'

显示设备逻辑像素的密度，代表物理像素与逻辑像素的缩放系数，计算方式为：

该参数为浮点数，受[densityDPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)范围限制，取值范围在[0.5，4.0]。一般取值1.0、3.0等，实际取值取决于不同设备提供的[densityDPI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#display)。

'sdkApiVersion'

系统软件API版本。

'bluetoothEnabled'

蓝牙系统开关。

'locationEnabled'

地理位置的系统开关。

'wifiEnabled'

Wi-Fi 的系统开关。

'deviceOrientation'

设备当前显示的方向。

'theme'

系统主题（深色、浅色模式）。

'windowWidth'

可使用窗口宽度。

'windowHeight'

可使用窗口高度。

#### SystemSettingType

type SystemSettingType = 'bluetoothEnabled' | 'locationEnabled' | 'wifiEnabled' | 'deviceOrientation'

系统设置属性取值类型。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：**对于5.0.0(12)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、Wearable、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

类型

说明

'bluetoothEnabled'

蓝牙系统开关。

'locationEnabled'

地理位置的系统开关。

'wifiEnabled'

Wi-Fi 的系统开关。

'deviceOrientation'

设备当前显示的方向。

#### getSystemInfoSync

getSystemInfoSync(properties?: Array<SystemInfoType>): SystemInfo

调用该方法获取设备、网络状态、屏幕、语言、主题等系统信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：**对于5.0.0(12)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、Wearable、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

properties

Array<[SystemInfoType](#section994220537517)>

否

获取设备、网络状态、屏幕、语言、主题等系统信息的请求对象。

 说明：

- 使用5.0.1(13)及以上版本时不需要配置Wi-Fi权限、蓝牙权限。
- 获取Wi-Fi信息需要配置权限ohos.permission.GET_WIFI_INFO。
- 获取蓝牙开启状态需要配置权限ohos.permission.ACCESS_BLUETOOTH。
- 获取用户程序访问控制权限可参考[程序访问控制管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9)。
- 定位信息不支持在TV设备上获取。

在多线程中调用getSystemInfoSync接口时，请勿获取theme、windowWidth、windowHeight、statusBarHeight和screenSafeArea的信息，可能会导致程序崩溃。

**返回值：**

类型

说明

[SystemInfo](#section6926144111527)

返回[SystemInfo](#section6926144111527)对象。

 说明：

getSystemInfoSync接口不支持获取windowWidth、windowHeight、statusBarHeight和screenSafeArea属性，如需获取可使用[getSystemInfo](#section17779133174510)接口。

**示例：**

```ets
import { atomicService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let stateArray: Array<atomicService.SystemInfoType> =
  ['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'language', 'osFullName', 'fontSizeSetting',
    'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation', 'theme'];
try {
  let data = atomicService.getSystemInfoSync(stateArray);
  hilog.info(0x0000, 'testTag', 'succeeded in getting system info');
  let brand: string | undefined = data.brand;
  let deviceModel: string | undefined = data.deviceModel;
  let screenWidth: number | undefined = data.screenWidth;
  let screenHeight: number | undefined = data.screenHeight;
  let language: string | undefined = data.language;
  let osFullName: string | undefined = data.osFullName;
  let fontSizeSetting: number | undefined = data.fontSizeSetting;
  let sdkApiVersion: number | undefined = data.sdkApiVersion;
  let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
  let wifiEnabled: boolean | undefined = data.wifiEnabled;
  let locationEnabled: boolean | undefined = data.locationEnabled;
  let deviceOrientation: string | undefined = data.deviceOrientation;
  let theme: ColorMode | undefined = data.theme;
} catch (error) {
  hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
}
```

#### getSystemInfo

getSystemInfo(properties?: Array<SystemInfoType>): Promise<SystemInfo>

调用该方法获取设备、网络状态、屏幕、语言、主题等系统信息，使用Promise异步回调。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：**对于5.0.0(12)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、Wearable、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

properties

Array<[SystemInfoType](#section994220537517)>

否

获取设备、网络状态、屏幕、语言、主题等系统信息的请求对象。

 说明：

- 使用5.0.1(13)及以上版本时不需要配置Wi-Fi权限、蓝牙权限。
- 获取Wi-Fi信息需要配置权限ohos.permission.GET_WIFI_INFO。
- 获取蓝牙开启状态需要配置权限ohos.permission.ACCESS_BLUETOOTH。
- 获取用户程序访问控制权限可参考[程序访问控制管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9)。
- 定位信息不支持在TV设备上获取。

在多线程中调用getSystemInfo接口时，请勿获取theme、windowWidth、windowHeight、statusBarHeight和screenSafeArea的信息，可能会导致程序崩溃。

**返回值：**

类型

说明

Promise<[SystemInfo](#section6926144111527)>

Promise对象，返回[SystemInfo](#section6926144111527)对象。

**示例：**

```ets
import { atomicService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let stateArray: Array<atomicService.SystemInfoType> =
  ['brand', 'deviceModel', 'screenWidth', 'screenHeight', 'statusBarHeight', 'screenSafeArea', 'language', 'osFullName',
    'fontSizeSetting', 'sdkApiVersion', 'bluetoothEnabled', 'wifiEnabled', 'locationEnabled', 'deviceOrientation',
    'theme', 'windowWidth', 'windowHeight'];
try {
  atomicService.getSystemInfo(stateArray).then((data: atomicService.SystemInfo) => {
    hilog.info(0x0000, 'testTag', 'succeeded in getting system info asynchronously');
    let brand: string | undefined = data.brand;
    let deviceModel: string | undefined = data.deviceModel;
    let screenWidth: number | undefined = data.screenWidth;
    let screenHeight: number | undefined = data.screenHeight;
    let statusBarHeight: number | undefined = data.statusBarHeight;
    let screenSafeArea: window.AvoidArea | undefined = data.screenSafeArea;
    let language: string | undefined = data.language;
    let osFullName: string | undefined = data.osFullName;
    let fontSizeSetting: number | undefined = data.fontSizeSetting;
    let sdkApiVersion: number | undefined = data.sdkApiVersion;
    let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
    let wifiEnabled: boolean | undefined = data.wifiEnabled;
    let locationEnabled: boolean | undefined = data.locationEnabled;
    let deviceOrientation: string | undefined = data.deviceOrientation;
    let theme: ColorMode | undefined = data.theme;
    let windowWidth: number | undefined = data.windowWidth;
    let windowHeight: number | undefined = data.windowHeight;
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Promise error: %{public}d %{public}s', error.code, error.message);
  })
} catch (error) {
  hilog.error(0x0000, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
}
```

#### getSystemSetting

getSystemSetting(properties?: Array<SystemSettingType>): SystemSettingInfo

调用该方法获取系统设置属性，包括蓝牙、位置、Wi-Fi状态和设备方向信息。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：**对于5.0.0(12)版本，该接口在Phone、Tablet、2in1中可正常调用，在其他设备类型中返回801错误码。对于5.1.0(18)及之后版本，该接口在Phone、Tablet、2in1、Wearable、TV中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

properties

Array<[SystemSettingType](#section11423195912475)>

否

获取蓝牙、定位、Wi-Fi开关，以及设备方向等系统信息的请求对象。

 说明：

- 使用5.0.1(13)及以上版本时不需要配置Wi-Fi权限、蓝牙权限。
- 获取Wi-Fi信息需要配置权限ohos.permission.GET_WIFI_INFO。
- 获取蓝牙开启状态需要配置权限ohos.permission.ACCESS_BLUETOOTH。
- 获取用户程序访问控制权限可参考[程序访问控制管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9)。
- 定位信息不支持在TV设备上获取。

**返回值：**

类型

说明

[SystemSettingInfo](#section53111326141919)

返回[SystemSettingInfo](#section53111326141919)对象。

**示例：**

```ets
import { atomicService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let stateArray: Array<atomicService.SystemSettingType> =
  ['bluetoothEnabled', 'locationEnabled', 'deviceOrientation', 'wifiEnabled'];
try {
  let data = atomicService.getSystemSetting(stateArray);
  hilog.info(0x0000, 'testTag', 'succeeded in getting system setting info');
  let bluetoothEnabled: boolean | undefined = data.bluetoothEnabled;
  let locationEnabled: boolean | undefined = data.locationEnabled;
  let deviceOrientation: string | undefined = data.deviceOrientation;
  let wifiEnabled: boolean | undefined = data.wifiEnabled;
} catch (error) {
  hilog.error(0x0001, 'testTag', 'failReason: %{public}d %{public}s', error.code, error.message);
}
```

#### showFollowComponent

showFollowComponent(ctx: UIContext, params: FollowComponentParams, callback: FollowComponentCallback): Promise<void>

调用该方法展示关注组件。

**模型约束：**此接口仅可在Stage模型下使用。

**元服务API：**从版本6.0.1(21)开始，该接口支持在元服务中使用。

**系统能力****：**SystemCapability.AtomicserviceComponent.atomicservice

**设备行为差异：**该接口在Phone、Tablet中可正常调用，在其他设备类型中返回801错误码。

**起始版本：**6.0.1(21)

**参数：**

参数名

类型

必填

说明

ctx

[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-api#uicontext)

是

UIContext实例对象。

params

[FollowComponentParams](#section1881114501476)

是

关注组件的参数。

callback

[FollowComponentCallback](#section137361343174413)

是

回调函数。callback返回关注的结果。

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回结果。

**错误码：**

错误码ID

错误信息

[801](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal#section801-该设备不支持此api)

Capability not supported.

[1009601001](../../errors/ArkTS API错误码.md#section310313457116)

Invalid service account id.

[1009601002](../../errors/ArkTS API错误码.md#section182327351133)

The user has not logged in with HUAWEI ID.

[1009601003](../../errors/ArkTS API错误码.md#section1710114369396)

Request server failed.

[1009601004](../../errors/ArkTS API错误码.md#section12303893910)

Network connection error.

[1009601005](../../errors/ArkTS API错误码.md#section17511740104712)

Other error.

**示例：**

```ets
import { atomicService } from '@kit.ScenarioFusionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  aboutToAppear(): void {
    // 一键关注组件。
    // pubId: 服务号id，此处以官方小助手服务号id为例。
    const pubId: string = '0cca1c645526449fb89d4a83e3bc25df';
    // channelId：渠道id，长度限制32，只能是数字或字母组成; offset：设置关注组件的位置坐标。
    const params: atomicService.FollowComponentParams =
      { pubId: pubId, channelId: '', offset: { x: 0, y: 300 } };
    // 点击关注按钮的关注结果回调。
    const callbacks: atomicService.FollowComponentCallback = {
      onFollowComplete: (err, result) => {
        if (err) {
          // 错误日志处理。
          hilog.error(0x0000, "testTag", "error: %{public}d %{public}s", err.code, err.message);
          return;
        }
        hilog.info(0x0000, "testTag", "follow result: %{public}d", result.code);
        if (result.code === atomicService.FollowResult.SUCCESS) {
          hilog.info(0x0000, "testTag", "follow succeeded handle");
        } else {
          hilog.info(0x0000, "testTag", "follow failed handle");
        }
      }
    }
    // 展示关注组件。
    atomicService.showFollowComponent(this.getUIContext(), params, callbacks).catch((error: BusinessError<void>) => {
      hilog.error(0x0000, 'testTag', 'showFollowComponent failReason: %{public}d %{public}s:', error.code,
        error.message);
    })
  }

  build() {
  }
}
```