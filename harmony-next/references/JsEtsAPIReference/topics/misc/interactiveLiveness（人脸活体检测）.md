# interactiveLiveness（人脸活体检测）

人脸活体检测是指在一些身份验证场景中，确定对象真实生理特征的方法。

在人脸识别应用中，活体检测能实时捕捉人脸或者通过眨眼、张嘴、摇头、点头等组合动作，使用人脸关键点定位和人脸追踪等技术，验证用户是否为真实活体操作。可有效抵御照片、视频、面具、遮挡以及屏幕翻拍等常见的攻击手段，从而帮助用户甄别欺诈行为，保障用户的利益。

**起始版本：**5.0.0(12)

#### 导入模块

```ets
import { interactiveLiveness } from '@kit.VisionKit';
```

#### DetectionMode

检测模式的枚举值。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Component.LivenessDetect

**起始版本：**5.0.0(12)

名称

值

说明

SILENT_MODE

SILENT_MODE

表示静默活体检测模式，暂未支持。

INTERACTIVE_MODE

INTERACTIVE_MODE

表示动作活体检测模式。

#### ActionsNumber

人脸活体检测的动作检测个数的枚举值。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Component.LivenessDetect

**起始版本：**5.0.0(12)

名称

值

说明

ONE_ACTION

1

随机选择一个动作，暂未支持。

TWO_ACTION

2

随机选择两个动作，暂未支持。

THREE_ACTION

3

随机选择三个动作。

FOUR_ACTION

4

随机选择四个动作。

#### RouteRedirectionMode

人脸活体检测完成的路由跳转模式的枚举值。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Component.LivenessDetect

**起始版本：**5.0.0(12)

名称

值

**说明**

BACK_MODE

back

表示人脸活体检测完成后返回到上一页。

REPLACE_MODE

replace

表示人脸活体检测完跳转到成功或失败页面。

#### InteractiveLivenessConfig

人脸活体检测的配置项。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：**SystemCapability.AI.Component.LivenessDetect

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

isSilentMode

[DetectionMode](#section143611912403)

否

否

表示的是人脸活体检测模式，默认动作活体检测模式。

INTERACTIVE_MODE表示动作活体检测模式。

actionsNum

[ActionsNumber](#section156871424104118)

否

是

表示动作活体检测的动作数量，数量范围3或4个，默认3个动作。随机生成，规则如下：

当actionsNum=3时，[眨眼，注视]组合中的动作元素不会同时存在并且相邻的动作元素不会相同。

当actionsNum=4时，眨眼动作元素有且仅有1次，注视动作元素最多出现1次，[眨眼，注视]组合中的动作元素不会相邻，相邻的动作元素不会相同。

该参数只有当isSilentMode是INTERACTIVE_MODE的时候有效。

successfulRouteUrl

string

否

是

表示人脸活体检测成功后跳转的页面路径。如果自定义界面，routeMode值为replace时生效。

如果不填，系统有默认的检测成功页面。

failedRouteUrl

string

否

是

表示人脸活体检测失败后跳转的页面路径。如果自定义界面，routeMode值为replace时生效。

如果不填，系统有默认的检测失败页面。

routeMode

[RouteRedirectionMode](#section6129163245310)

否

是

人脸活体检测完成后跳转模式。

challenge

string

否

是

挑战值。仅用于安全摄像头场景（对应[initializeAttestContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-taas-api#section166716269293)方法中的“userData”字段）的活体检测。

使用安全摄像头场景的前提需要[开通Device Security服务](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice)。

长度范围是[16,128]之间（challenge传空或者undefined表示不使用安全摄像头）。

安全摄像头目前支持的设备详情请查看[约束与限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-taas-securecamera#section104414218221)。

speechSwitch

boolean

否

是

语音播报的开关。

- true表示开启语音播报。
- false表示关闭语音播报。

默认开启语音播报。

isPrivacyMode

boolean

否

是

是否设置隐私模式。

- true：设置隐私模式。
- false：不设置隐私模式。

默认值为false。

 说明：

当设置隐私模式时，需要申请ohos.permission.PRIVACY_WINDOW权限。

**示例：**

```ets
import { interactiveLiveness } from '@kit.VisionKit';

let isSilentMode = "INTERACTIVE_MODE" as interactiveLiveness.DetectionMode;
let routeMode = "replace" as interactiveLiveness.RouteRedirectionMode;
let actionsNum = 3 as interactiveLiveness.ActionsNumber;
let routerOptions: interactiveLiveness.InteractiveLivenessConfig= {
  isSilentMode: isSilentMode,
  routeMode: routeMode,
  actionsNum: actionsNum,
  failedRouteUrl: "pages/FailPage",
  successfulRouteUrl: "pages/SuccessPage"
}
```

#### startLivenessDetection

startLivenessDetection(config: InteractiveLivenessConfig): Promise<boolean>

跳转到人脸活体检测页面的入口。使用Promise异步回调。

**需要权限：**ohos.permission.CAMERA

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.LivenessDetect

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

config

[InteractiveLivenessConfig](#section16532153115517)

是

跳转到人脸活体检测页面的配置项

**返回值：**

类型

说明

Promise<boolean>

Promise方式返回的结果，用于判断跳转到人脸活体检测页面是否成功。

- true表示跳转人脸活体检测页面成功。
- false表示跳转人脸活体检测页面失败。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

1008301002

Route switching failed.

**示例：**

```ets
import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let isSilentMode = "INTERACTIVE_MODE" as interactiveLiveness.DetectionMode;
let actionsNum = 3 as interactiveLiveness.ActionsNumber;
let routerOptions: interactiveLiveness.InteractiveLivenessConfig= {
  actionsNum: actionsNum,
  isSilentMode: isSilentMode
};

interactiveLiveness.startLivenessDetection(routerOptions).then((DetectState: boolean) => {
  hilog.info(0x0001, "LivenessCollectionIndex", `Succeeded in jumping.`);
}).catch((err: BusinessError) => {
  hilog.error(0x0001, "LivenessCollectionIndex", `Failed to jump. Code：${err.code}，message：${err.message}`);
})
```

#### startLivenessDetection

startLivenessDetection(config: InteractiveLivenessConfig, callback: AsyncCallback<InteractiveLivenessResult | undefined>): Promise<boolean>

跳转到人脸活体检测页面的入口。使用Promise异步回调获取跳转结果，使用callback回调获取检测结果。

**需要权限：**ohos.permission.CAMERA

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.LivenessDetect

**起始版本：**5.0.0(12)

**参数：**

参数名

类型

必填

说明

config

[InteractiveLivenessConfig](#section16532153115517)

是

跳转到人脸活体检测页面的配置项。

callback

[AsyncCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#asynccallback)<[InteractiveLivenessResult](#section173751154134515) | undefined>

是

回调函数，返回活体检测的结果。当前只适用于RouteRedirectionMode.BACK_MODE跳转模式。

**返回值：**

类型

说明

Promise<boolean>

Promise方式返回的结果，用于判断跳转到人脸活体检测页面是否成功。

- true表示跳转人脸活体检测页面成功。
- false表示跳转人脸活体检测页面失败。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied.

401

Parameter error.

1008301002

Route switching failed.

1008302000

Detection algorithm initialization.

1008302001

Detection timeout.

1008302002

Action mutual exclusion error.

1008302003

Continuity Check Failure.

1008302004

The test is not complete.

**示例：**

```ets
import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let isSilentMode = "INTERACTIVE_MODE" as interactiveLiveness.DetectionMode;
let actionsNum = 3 as interactiveLiveness.ActionsNumber;
let routerOptions: interactiveLiveness.InteractiveLivenessConfig= {
  actionsNum: actionsNum,
  isSilentMode: isSilentMode,
  routeMode: "back" as interactiveLiveness.RouteRedirectionMode
};

interactiveLiveness.startLivenessDetection(routerOptions, (err: BusinessError,
  result: interactiveLiveness.InteractiveLivenessResult | undefined) => { // 当路由跳转错误时，获取结果失败，result返回undefined
  if(err.code !== 0 && !result) { // 在发生错误如路由跳转失败/参数错误/权限被拒绝时，会抛出错误码，详见[ArkTS API错误码](../../errors/ArkTS API错误码.md)
    hilog.error(0x0001, "LivenessCollectionIndex", `Failed to detect. Code：${err.code}，message：${err.message}`);
    return;
  }
  hilog.info(0x0001, 'LivenessCollectionIndex', `Succeeded in detecting result：${result}`);
})
```

#### LivenessType

活体检测模式的枚举值。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.LivenessDetect

**起始版本：**5.0.0(12)

名称

值

说明

INTERACTIVE_LIVENESS

0

表示当前检测的结果是动作活体检测。

SILENT_LIVENESS

1

表示当前检测的结果是静默活体检测，暂未支持。

NOT_LIVENESS

2

表示当前检测的结果是非活体，跳转的是失败页面，不会返回错误信息。如果配置了失败页面或者back路由跳转，不建议有重新检测的场景。

#### InteractiveLivenessResult

返回人脸活体检测结果的相关参数。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.LivenessDetect

**起始版本：**5.0.0(12)

名称

类型

只读

可选

说明

livenessType

[LivenessType](#section15262164419435)

否

否

活体检测模式。

mPixelMap

[image.PixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)

否

是

检测成功后返回最具有活体特征的图片。

securedImageBuffer

ArrayBuffer

否

是

安全摄像头场景返回的安全流。

certificate

Array<string>

否

是

安全摄像头场景返回的证书链。

#### getInteractiveLivenessResult

getInteractiveLivenessResult(): Promise<InteractiveLivenessResult>

获取人脸活体检测的结果。使用Promise异步回调。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.AI.Component.LivenessDetect

**起始版本：**5.0.0(12)

**返回值：**

类型

说明

Promise<[InteractiveLivenessResult](#section173751154134515)>

Promise方式返回人脸活体检测的结果。成功会获取活体检测的方式和一张检测图片。失败获取错误码ID和描述信息。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

1008302000

Detection algorithm initialization.

1008302001

Detection timeout.

1008302002

Action mutual exclusion error.

1008302003

Continuity Check Failure.

1008302004

The test is not complete.

**示例：**

```ets
import { interactiveLiveness } from '@kit.VisionKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

interactiveLiveness.getInteractiveLivenessResult().then(data => {
  hilog.info(0x0001, "LivenessCollectionIndex", `Succeeded in detecting.`);
}).catch((err: BusinessError) => {
  hilog.error(0x0001, "LivenessCollectionIndex", `Failed to detect. Code：${err.code}，message：${err.message}`);
})
```

#### 动作说明

动作

描述

1

点头

2

张嘴

3

眨眼

4

左摇头

5

右摇头

6

注视