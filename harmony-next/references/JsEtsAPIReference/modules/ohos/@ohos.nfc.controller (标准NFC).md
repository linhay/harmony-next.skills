# @ohos.nfc.controller (标准NFC)

本模块主要用于管理NFC状态，包括打开和关闭NFC，读取NFC的状态等。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### **导入模块**

```ets
import { nfcController } from '@kit.ConnectivityKit';
```

#### NfcState

定义不同的NFC状态值。

**系统能力：** SystemCapability.Communication.NFC.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE_OFF | 1 | NFC已关闭状态。 |
| STATE_TURNING_ON | 2 | NFC正在打开状态。 |
| STATE_ON | 3 | NFC已打开状态。 |
| STATE_TURNING_OFF | 4 | NFC正在关闭状态。 |

#### nfcController.isNfcAvailable(deprecated)

isNfcAvailable(): boolean

查询设备是否有NFC能力。


从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[canIUse("SystemCapability.Communication.NFC.Core")](Init.md#ZH-CN_TOPIC_0000002553202571__caniuse)替代。

**系统能力：** SystemCapability.Communication.NFC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 设备具备NFC能力， false: 设备不具备NFC能力。 |

#### nfcController.openNfc(deprecated)

openNfc(): boolean

打开NFC开关。


从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[enableNfc](#ZH-CN_TOPIC_0000002522081450__nfccontrollerenablenfc9)替代。

**需要权限：** ohos.permission.MANAGE_SECURE_SETTINGS（该权限仅系统应用可申请）

**系统能力：** SystemCapability.Communication.NFC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 打开NFC成功， false: 打开NFC失败。 |

#### nfcController.enableNfc9+

enableNfc(): void

打开NFC开关，该接口只能被系统应用调用。

**需要权限：** ohos.permission.MANAGE_SECURE_SETTINGS（该权限仅系统应用可申请）

**系统能力：** SystemCapability.Communication.NFC.Core

**错误码：**

以下错误码的详细介绍请参见[NFC错误码]([NFC错误码](../../errors/NFC错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100101 | The NFC state is abnormal in the service. |

#### nfcController.closeNfc(deprecated)

closeNfc(): boolean

关闭NFC开关。


从 API version 7 开始支持，从 API version 9 开始废弃，建议使用[disableNfc](#ZH-CN_TOPIC_0000002522081450__nfccontrollerdisablenfc9)替代。

**需要权限：** ohos.permission.MANAGE_SECURE_SETTINGS（该权限仅系统应用可申请）

**系统能力：** SystemCapability.Communication.NFC.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 关闭NFC成功， false: 关闭NFC失败。 |

#### nfcController.disableNfc9+

disableNfc(): void

关闭NFC开关，该接口只能被系统应用调用。

**需要权限：** ohos.permission.MANAGE_SECURE_SETTINGS（该权限仅系统应用可申请）

**系统能力：** SystemCapability.Communication.NFC.Core

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3100101 | The NFC state is abnormal in the service. |

#### nfcController.isNfcOpen

isNfcOpen(): boolean

查询NFC是否打开。

**系统能力：** SystemCapability.Communication.NFC.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: NFC是打开的， false: NFC是关闭的。 |

#### nfcController.getNfcState

getNfcState(): [NfcState](#ZH-CN_TOPIC_0000002522081450__nfcstate)

查询NFC状态。

**系统能力：** SystemCapability.Communication.NFC.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| NfcState | NFC状态值，详细请见NfcState枚举值。 |

#### nfcController.on('nfcStateChange')

on(type: 'nfcStateChange', callback: Callback<[NfcState](#ZH-CN_TOPIC_0000002522081450__nfcstate)>): void

注册NFC开关状态事件，获取NFC状态的变化通知。使用callback异步回调。

**系统能力：** SystemCapability.Communication.NFC.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"nfcStateChange"字符串。 |
| callback | Callback<NfcState> | 是 | 回调函数，返回NFC状态的枚举值。 |

#### nfcController.off('nfcStateChange')

off(type: 'nfcStateChange', callback?: Callback<[NfcState](#ZH-CN_TOPIC_0000002522081450__nfcstate)>): void

取消NFC开关状态事件的注册，取消后NFC状态变化时，就不会再收到Callback的通知。使用callback异步回调。

**系统能力：** SystemCapability.Communication.NFC.Core

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"nfcStateChange"字符串。 |
| callback | Callback<NfcState> | 否 | NFC状态改变回调函数，可以空缺不填。如果callback不填，将取消注册该事件关联的所有回调函数。 |

**示例**

```ets
import { nfcController } from '@kit.ConnectivityKit';

// 注册回调以接收nfc状态更改通知
nfcController.on("nfcStateChange", (nfcState : number)=> {
  console.info("nfcController on callback nfcState: " + nfcState);
});

// 打开nfc需要权限: ohos.permission.MANAGE_SECURE_SETTINGS（此权限仅系统应用可申请）
if (!nfcController.isNfcOpen()) {
  // 从api9开始,使用'enableNfc'打开nfc
  try {
    nfcController.enableNfc();
    console.info("nfcController enableNfc success");
  } catch (businessError) {
    console.error("nfcController enableNfc businessError: " + businessError);
  }
} else {
  console.info("nfcController NFC has been opened");
}

// 关闭nfc需要权限: ohos.permission.MANAGE_SECURE_SETTINGS（此权限仅系统应用可申请）
if (nfcController.isNfcOpen()) {
  // 从api9开始,使用'disableNfc'关闭nfc
  try {
    nfcController.disableNfc();
    console.info("nfcController disableNfc success");
  } catch (businessError) {
    console.error("nfcController disableNfc businessError: " + businessError);
  }
} else {
  console.info("nfcController NFC has been closed");
}

// 取消注册回调
nfcController.off("nfcStateChange");
```