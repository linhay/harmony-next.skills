[]()[]()

# DlpAntiPeep（防窥保护）

本模块提供窥视状态相关接口，应用根据窥视状态保护用户隐私，如拉起系统级蒙层遮盖窗口，非机主状态（即有非机主以外的人在注视屏幕）下不进行个性化推荐、隐藏浏览记录、支付记录、收藏记录等敏感信息。

**起始版本：**6.0.0(20)

[]()[]()

#### 导入模块

```ets
import { dlpAntiPeep } from '@kit.DeviceSecurityKit';
```

[]()[]()

#### DlpAntiPeepStatus

表示窥视状态的枚举。

**系统能力**：SystemCapability.Security.DlpAntiPeep

**起始版本：**6.0.0(20)

名称

值

说明

PASS

0

表示当前设备屏幕无人在窥视。

HIDE

1

表示有除机主以外的人在窥视设备屏幕。

[]()[]()

#### isDlpAntiPeepSwitchOn

isDlpAntiPeepSwitchOn(): Promise<boolean>

检查当前应用是否开启防窥保护。使用Promise异步回调。

**需要权限：**ohos.permission.DLP_GET_HIDE_STATUS

**系统能力****：**SystemCapability.Security.DlpAntiPeep

**起始版本：**6.0.0(20)

**返回值：**

类型

说明

Promise<boolean>

Promise对象，返回当前应用是否开启了防窥保护，true代表开启，false代表未开启，默认值为false。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/DlpAntiPeep（防窥保护） (devicesecurity-arktsapi-errcode-dlpantipeep).md)**。**

错误码ID

错误信息

201

Permission denied.

801

Capability not supported. Function on can not work correctly due to limited device capabilities.

1020600001

Internal error.

**示例：**

```ets
import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

try {
  let result = await dlpAntiPeep.isDlpAntiPeepSwitchOn();
  console.info(`isDlpAntiPeepSwitchOnsuccess.`);
} catch (err) {
  console.error(`isDlpAntiPeepSwitchOnfailed.`);
}
```

[]()[]()

#### on("dlpAntiPeep")

on(type: 'dlpAntiPeep', callback: Callback<DlpAntiPeepStatus>): void

订阅防窥保护通知。使用callback方式异步返回结果。

请在满足[开发前置条件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-dlpantipeep#section128161223011)后再调用此接口，避免无法触发防窥回调。

**需要权限：**ohos.permission.DLP_GET_HIDE_STATUS

**系统能力****：**SystemCapability.Security.DlpAntiPeep

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

type

'dlpAntiPeep'

是

表示需要订阅的事件'dlpAntiPeep'，取值为固定字符串'dlpAntiPeep'。

callback

Callback<[DlpAntiPeepStatus](#section11705111513)>

是

回调函数，返回调用结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/DlpAntiPeep（防窥保护） (devicesecurity-arktsapi-errcode-dlpantipeep).md)**。**

错误码ID

错误信息

201

Permission denied.

801

Capability not supported.

1020600001

Internal error.

**示例：**

```ets
import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

try {
  dlpAntiPeep.on('dlpAntiPeep', (dlpAntiPeepStatus: dlpAntiPeep.DlpAntiPeepStatus) => {
    console.info(`dlpAntiPeep.on success.`);
  });
} catch (error) {
  console.error(`dlpAntiPeep.on failed.`);
}
```

[]()[]()

#### off("dlpAntiPeep")

off(type: 'dlpAntiPeep', callback?: Callback<DlpAntiPeepStatus>): void

解订阅防窥保护通知。使用callback方式异步返回结果。

**需要权限：**ohos.permission.DLP_GET_HIDE_STATUS

**系统能力****：**SystemCapability.Security.DlpAntiPeep

**起始版本：**6.0.0(20)

**参数：**

参数名

类型

必填

说明

type

'dlpAntiPeep'

是

表示需要解订阅的事件'dlpAntiPeep'，取值为固定字符串'dlpAntiPeep'。

callback

Callback<[DlpAntiPeepStatus](#section11705111513)>

否

用于接收防窥保护通知的回调函数。如果传入了callback，则取消callback的订阅，否则取消所有callback的订阅。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/DlpAntiPeep（防窥保护） (devicesecurity-arktsapi-errcode-dlpantipeep).md)**。**

错误码ID

错误信息

201

Permission denied.

801

Capability not supported.

1020600001

Internal error.

**示例：**

```ets
import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

try {
  dlpAntiPeep.off('dlpAntiPeep', (dlpAntiPeepStatus: dlpAntiPeep.DlpAntiPeepStatus) => {
    console.info(`dlpAntiPeep.off success.`);
  });
} catch (error) {
  console.error(`dlpAntiPeep.off failed.`);
}
```

[]()[]()

#### getDlpAntiPeepInfo

getDlpAntiPeepInfo(): DlpAntiPeepStatus

获取当前应用的窥视状态。

**需要权限：**ohos.permission.DLP_GET_HIDE_STATUS

**系统能力****：**SystemCapability.Security.DlpAntiPeep

**起始版本：**6.0.0(20)

**返回值：**

类型

说明

[DlpAntiPeepStatus](#section11705111513)

表示窥视状态。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/DlpAntiPeep（防窥保护） (devicesecurity-arktsapi-errcode-dlpantipeep).md)**。**

错误码ID

错误信息

201

Permission denied.

801

Capability not supported. Function getDlpHideInfo can not work correctly due to limited device capabilities.

1020600001

Internal error.

**示例：**

```ets
import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

try {
  let dlpAntiPeepStatus = dlpAntiPeep.getDlpAntiPeepInfo();
  console.info(`getDlpHideInfo success.`);
} catch (err) {
  console.error(`getDlpHideInfo failed.`);
}
```

[]()[]()

#### passDlpAntiPeepInfo

passDlpAntiPeepInfo(): void

设置当前应用窥视状态为非窥视，后续[on("dlpAntiPeep")](#section1794633020274)接口回调函数返回的窥视状态、[getDlpAntiPeepInfo](#section11694411559)接口直接获取的窥视状态均为无人窥视屏幕。

若应用在生命周期内不再需要接受窥视状态，可直接调用[off("dlpAntiPeep")](#section142181149107)接口解注册，若仍想接受放通后的非窥视状态，则可以调用该接口。

请在满足[开发前置条件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-dlpantipeep#section128161223011)并调用[on("dlpAntiPeep")](#section1794633020274)接口注册后再调用该接口，可用于在应用注册的生命周期内将回调状态变更为非防窥状态，直到应用退出或设备锁屏。

**需要权限：**ohos.permission.DLP_GET_HIDE_STATUS

**系统能力****：**SystemCapability.Security.DlpAntiPeep

**起始版本：**6.0.0(20)

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/DlpAntiPeep（防窥保护） (devicesecurity-arktsapi-errcode-dlpantipeep).md)**。**

错误码ID

错误信息

201

Permission denied.

801

Capability not supported. Function passDlpHideInfo can not work correctly due to limited device capabilities.

1020600001

Internal error.

**示例：**

```ets
import { dlpAntiPeep } from '@kit.DeviceSecurityKit';

try {
  dlpAntiPeep.passDlpAntiPeepInfo();
  console.info(`passDlpAntiPeepInfo success.`);
} catch (err) {
  console.error(`passDlpAntiPeepInfo failed.`);
}
```

[]()[]()

#### setAntiPeepMaskLayer

setAntiPeepMaskLayer(windowId: number): Promise<void>

对指定窗口设置系统级蒙层，使用Promise异步回调。

该接口调用后会拉起蒙层，覆盖应用窗口，建议开发者在检测到窥视状态后调用一次即可，频繁调用可能对用户体验造成影响。

**需要权限：**ohos.permission.DLP_GET_HIDE_STATUS

**系统能力****：**SystemCapability.Security.DlpAntiPeep

**起始版本：**6.0.1(21)

**参数：**

参数名

类型

必填

说明

windowId

number

是

应用需要覆盖保护的窗口ID，该参数取值范围为大于0的整数。

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/DlpAntiPeep（防窥保护） (devicesecurity-arktsapi-errcode-dlpantipeep).md)**。**

错误码ID

错误信息

201

Permission denied.

801

Capability not supported.function setAntiPeepMaskLayer can not work correctly due to limited device capabilities.

1020600001

Internal error.

1020600002

The antipeep function is not enabled.

1020600003

The protected application is not displayed on the screen.

**示例：**

```ets
import { dlpAntiPeep } from '@kit.DeviceSecurityKit';
import { common } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let windowClass: window.Window;
try {
  windowClass = await window.getLastWindow(context);
} catch(err) {
  console.error('error', err.code, err.message);
  return;
}
let windowId: number;
try {
  windowId = windowClass.getWindowProperties().id;
} catch (err) {
  console.error('Failed to get window properties:', err);
  return;
}
try {
  await dlpAntiPeep.setAntiPeepMaskLayer(windowId);
} catch (err) {
  console.error(`setAntiPeepMaskLayer failed. error code is ${JSON.stringify(err)}`);
}
```