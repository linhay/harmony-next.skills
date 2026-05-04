# @ohos.identifier.oaid (开放匿名设备标识服务)

本模块提供开放匿名设备标识符（Open Anonymous Device Identifier, OAID，以下简称OAID）的获取和重置能力。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

使用获取开放匿名设备标识符接口，需[向用户申请授权](../../guides/向用户申请授权.md)（默认开启权限）：ohos.permission.APP_TRACKING_CONSENT。

#### 导入模块

```ets
import { identifier } from '@kit.AdsKit';
```

#### identifier.getOAID

getOAID(): Promise<string>

获取开放匿名设备标识符（OAID）。使用Promise异步回调。

**需要权限：** ohos.permission.APP_TRACKING_CONSENT

**系统能力：** SystemCapability.Advertising.OAID

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回开放匿名设备标识符（OAID）。 1.如应用已配置ohos.permission.APP_TRACKING_CONSENT权限，且“跨应用关联访问权限”为“允许”，则返回OAID。 2.如应用已配置ohos.permission.APP_TRACKING_CONSENT权限，且“跨应用关联访问权限”为“禁止”，则返回00000000-0000-0000-0000-000000000000。 3.如应用未配置ohos.permission.APP_TRACKING_CONSENT权限，则返回00000000-0000-0000-0000-000000000000。 |


设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

**错误码：**

以下错误码的详细介绍请参见[开放匿名设备标识服务错误码参考](开放匿名设备标识服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17300001 | System internal error. |

**示例：**

```ets
import { identifier } from '@kit.AdsKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

void identifier.getOAID().then((data: string) => {
  const oaid: string = data;
}).catch((error: BusinessError) => {
  hilog.info(0x0000, 'testTag', `Failed to get oaid. Code is ${error.code}, message is ${error.message}`);
});
```

#### identifier.getOAID

getOAID(callback: AsyncCallback<string>): void

获取开放匿名设备标识符（OAID）。使用callback异步回调。

**需要权限：** ohos.permission.APP_TRACKING_CONSENT

**系统能力：** SystemCapability.Advertising.OAID

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数，返回开放匿名设备标识符（OAID）。 1.如应用已配置ohos.permission.APP_TRACKING_CONSENT权限，且“跨应用关联访问权限”为“允许”，则返回OAID。 2.如应用已配置ohos.permission.APP_TRACKING_CONSENT权限，且“跨应用关联访问权限”为“禁止”，则返回00000000-0000-0000-0000-000000000000。 3.如应用未配置ohos.permission.APP_TRACKING_CONSENT权限，则返回00000000-0000-0000-0000-000000000000。 |


设置项“跨应用关联访问权限”在HarmonyOS NEXT Developer Beta5及更早版本名称为“应用跟踪访问权限”。

**错误码：**

以下错误码的详细介绍请参见[开放匿名设备标识服务错误码参考](开放匿名设备标识服务错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17300001 | System internal error. |

**示例：**

```ets
import { identifier } from '@kit.AdsKit';
import { BusinessError } from '@kit.BasicServicesKit';

identifier.getOAID((err: BusinessError, data: string) => {
  if (err.code) {
    return;
  }
  const oaid: string = data;
});
```