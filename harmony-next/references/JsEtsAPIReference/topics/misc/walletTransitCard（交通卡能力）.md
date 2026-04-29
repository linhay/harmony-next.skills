# walletTransitCard（交通卡能力）

本模块提供接入钱包交通卡服务的能力。

起始版本： 5.0.0(12)

**导入模块**

```ets
import { walletTransitCard } from '@kit.WalletKit';
```

**TransitCardClient**

钱包交通卡的功能入口类，与钱包卡券有关的所有方法从此处接入。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

**constructor**

constructor(context: common.UIAbilityContext, callerId: string)

构造函数。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext | 是 | UIAbility上下文。 |
| callerId | string | 是 | 接口调用方ID，调用方联系钱包运营申请交通卡服务时获取，仅对受邀应用开放申请。 |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';

@Entry
@Component
struct Index {
  private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

  build() {
    // your application UI
  }
```

**getCardMetadataInDevice**

getCardMetadataInDevice(specifiedDeviceType: DeviceType, callerToken?: string): Promise<CardMetadataInDevice[]>

获取当前设备中可开卡和已经开通的交通卡信息，包含设备信息和设备支持的卡的元数据。 在没有eSE的情况下，将返回一个空数组。 如果设备没有支持的卡，则无法在阵列中添加设备的CardMetadataInDevice。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| specifiedDeviceType | DeviceType | 是 | 指定设备的枚举值。 |
| callerToken | string | 否 | 小程序在微信、支付宝等中的鉴权token，要求使用JWT格式生成。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<CardMetadataInDevice[]> | Promise对象，返回一个CardMetadataInDevice元数据数组，包含设备信息和卡的元数据。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010210701 | Failed to verify the caller token. |
| 1010210702 | Failed to get the metadata of the cards. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

  async getCardMetadataInDevice() {
    this.transitCardClient.getCardMetadataInDevice(walletTransitCard.DeviceType.DEVICE_PHONE).then((result) => {
      console.info(`Succeeded in getting cardMetadataInDevice`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to get CardMetadataInDevice, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**getTransitCardInfo**

getTransitCardInfo(logicalCardNumber: string, specifiedDeviceId: string, callerToken?: string): Promise<TransitCardInfo>

查询指定的cardNumber交通卡信息。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| logicalCardNumber | string | 是 | 指定卡的卡号，要求使用getCardMetadataInDevice 返回的 CardMetadataInDevice 中的CardMetadata 对应的logicalCardNumber。 |
| specifiedDeviceId | string | 是 | 存在该卡的设备的ID，要求使用getCardMetadataInDevice 返回的CardMetadataInDevice 对应的deviceId。 |
| callerToken | string | 否 | 小程序在微信、支付宝等中的鉴权token，要求使用JWT格式生成。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<TransitCardInfo> | Promise对象，返回cardNumber指定卡的详细信息。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010210101 | The card status is not correct. |
| 1010210119 | Failed to read the card data. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010210102 | Failed to verify the caller token. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

  async getTransitCardInfo() {
    // number of the enabled traffic card returned by the getCardMetadataInDevice interface
    const logicalCardNumber = 'logicalCardNumber';
    // the specifiedDeviceId returned by the getCardMetadataInDevice interface
    const specifiedDeviceId = 'specifiedDeviceId';
    // JWT token for authentication in applications such as WeChat and Alipay
    const callerToken= 'callerToken';
    this.transitCardClient.getTransitCardInfo(logicalCardNumber, specifiedDeviceId, callerToken).then((result) => {
      console.info(`Succeeded in getting TransitCardInfo`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to get TransitCardInfo, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**canAddTransitCard**

canAddTransitCard(issuerId: string, specifiedDeviceId: string): Promise<string>

判断issuerId在当前设备中是否可以开卡，返回一个令牌字符串，指示是否可以在指定设备的钱包中添加issuerId指定的卡。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| issuerId | string | 是 | 城市的一种交通卡产品的ID，要求使用 getCardMetadataInDevice 返回的 CardMetadataInDevice中的 CardMetadata 对应的issuerId。 |
| specifiedDeviceId | string | 是 | 存在该卡的设备的ID，要求使用 getCardMetadataInDevice 返回的 CardMetadataInDevice对应的deviceId。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回一个用于添加卡片的token令牌。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200007 | The OS version is too old. Please upgrade the OS version. |
| 1010200008 | The wallet version is too old. |
| 1010200009 | The chip space is full, and no more cards can be added. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200016 | This card is not available for the current country or region. |
| 1010210201 | The device does not support adding the card specified by issuerId. |
| 1010210202 | A card conflicting with the specified card already exists in the device. |
| 1010210203 | The specified card already exists. |
| 1010210204 | The card addition service is temporarily offline. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

  async canAddTransitCard() {
    // the issuerId returned by the getCardMetadataInDevice interface
    const issuerId = 'issuerId';
    // the specifiedDeviceId returned by the getCardMetadataInDevice interface
    const specifiedDeviceId = 'specifiedDeviceId';
    this.transitCardClient.canAddTransitCard(issuerId, specifiedDeviceId).then((result) => {
      console.info(`Succeeded in canning AddTransitCard`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to can AddTransitCard, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**setupWalletEnvironment**

setupWalletEnvironment(): Promise<void>

设置Wallet应用程序的environment。当开发者从另一个api得到1010200003错误代码时，你应该调用这个api来设置Wallet应用。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 1010200002 | Wallet app not found. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200011 | Failed to initialize the environment. |
| 1010200017 | The Wallet app was closed by the user. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

  async setupWalletEnvironment() {
    this.transitCardClient.setupWalletEnvironment().then(() => {
      console.info(`Succeeded in setting up WalletEnvironment`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to setup WalletEnvironment, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**addTransitCard**

addTransitCard(addCardOpaqueData: string, serverOrderId: string): Promise<CardMetadata>

将指定的卡添加到钱包中，并返回CardMetadata。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| addCardOpaqueData | string | 是 | 开卡令牌，要求使用canAddTransitCard接口返回的字符串。 |
| serverOrderId | string | 是 | 开卡订单ID，要求是加卡业务在服务商后台服务器上生成的订单ID。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<CardMetadata> | Promise对象，返回添加的卡片数据。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010210301 | The card adding conditions are not met. The order can be refunded to end the card addition process. |
| 1010200016 | This card is not available for the current country or region. |
| 1010200017 | The Wallet app was closed by the user. |
| 1010210319 | Failed to add the card. |
| 1010210302 | Failed to confirm the order. The order can be refunded to end the card addition process. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

  async addTransitCard() {
    // order ID generated after payment in a developer's app, which is implemented by the developer
    let serverOrderId = 'serverOrderId';
    // the addCardOpaqueData returned by the canAddTransitCard interface
    let addCardOpaqueData = 'addCardOpaqueData';
    this.transitCardClient.addTransitCard(addCardOpaqueData, serverOrderId).then((result) => {
      console.info(`Succeeded in adding TransitCard`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to add TransitCard, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**rechargeTransitCard**

rechargeTransitCard(logicalCardNumber: string, specifiedDeviceId: string, serverOrderId: string): Promise<number>

交通卡充值接口，根据支付订单号serverOrderId为指定的logicalCardNumber交通卡进行充值，充值完成后返回当前余额。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| logicalCardNumber | string | 是 | 卡的序列号，要求使用getCardMetadataInDevice返回的CardMetadataInDevice中的CardMetadata对应的logicalCardNumber。 |
| specifiedDeviceId | string | 是 | 存在该卡的设备的ID，要求使用getCardMetadataInDevice返回的CardMetadataInDevice对应的deviceId。 |
| serverOrderId | string | 是 | 卡充值订单ID，要求是余额充值业务在服务商后台服务器上生成的订单ID。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回新的交通卡余额。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010210401 | The specified card does not exist. |
| 1010210402 | The status of the specified card is incorrect. |
| 1010210419 | Failed to recharge the card. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010210403 | Failed to confirm the order. The order can be refunded to end the recharging process. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

  async rechargeTransitCard() {
    // number of the enabled traffic card returned by the getCardMetadataInDevice interface
    const logicalCardNumber = 'logicalCardNumber';
    // the specifiedDeviceId returned by the getCardMetadataInDevice interface
    const specifiedDeviceId = 'specifiedDeviceId';
    // order ID generated after payment in a developer's app, which is implemented by the developer
    const serverOrderId = 'serverOrderId';
    this.transitCardClient.rechargeTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then((result) => {
      console.info(`Succeeded in recharging TransitCard`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to recharge TransitCard, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**updateTransitCard**

updateTransitCard(logicalCardNumber: string, specifiedDeviceId: string, serverOrderId: string): Promise<void>

更新交通卡信息，根据支付订单号serverOrderId为指定的logicalCardNumber交通卡进行数据更新。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| logicalCardNumber | string | 是 | 指定卡的卡号，要求使用getCardMetadataInDevice返回的CardMetadataInDevice中的CardMetadata对应的logicalCardNumber。 |
| specifiedDeviceId | string | 是 | 卡所在的设备ID，要求使用getCardMetadataInDevice返回的CardMetadataInDevice对应的deviceId。 |
| serverOrderId | string | 是 | 更新卡信息订单ID，要求是卡数据更新服务在服务提供商后台服务器上生成的订单ID。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010210501 | The specified card does not exist. |
| 1010210502 | The status of the specified card is incorrect. |
| 1010210503 | Failed to confirm the order. |
| 1010210519 | Failed to update the card data. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

  async updateTransitCard() {
    // number of the enabled traffic card returned by the getCardMetadataInDevice interface
    const logicalCardNumber = 'logicalCardNumber';
    // the specifiedDeviceId returned by the getCardMetadataInDevice interface
    const specifiedDeviceId = 'specifiedDeviceId';
    // order ID generated after payment in a developer's app, which is implemented by the developer
    const serverOrderId = 'serverOrderId';
    this.transitCardClient.updateTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then(() => {
      console.info(`Succeeded in updating TransitCard`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to update TransitCard, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**deleteTransitCard**

deleteTransitCard(logicalCardNumber: string, specifiedDeviceId: string, serverOrderId: string): Promise<void>

删除交通卡，根据支付订单号serverOrderId为指定的logicalCardNumber交通卡进行删卡。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| logicalCardNumber | string | 是 | 指定卡的卡号，要求使用getCardMetadataInDevice返回的CardMetadataInDevice中的CardMetadata对应的logicalCardNumber。 |
| specifiedDeviceId | string | 是 | 卡所在的设备ID，要求使用getCardMetadataInDevice返回的CardMetadataInDevice对应的deviceId。 |
| serverOrderId | string | 是 | 删卡订单id，要求是服务提供商的后端服务器上为删卡业务生成的订单id。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Parameter verification failed. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200013 | Operation failed because of an internal error. |
| 1010210619 | Failed to delete the card. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010210601 | Failed to confirm the order. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletTransitCard } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private transitCardClient: walletTransitCard.TransitCardClient = new walletTransitCard.TransitCardClient(this.getUIContext().getHostContext() as common.UIAbilityContext, 'callerId');

  async deleteTransitCard() {
    // number of the enabled traffic card returned by the getCardMetadataInDevice interface
    const logicalCardNumber = 'logicalCardNumber';
    // the specifiedDeviceId returned by the getCardMetadataInDevice interface
    const specifiedDeviceId = 'specifiedDeviceId';
    // order ID generated after payment in a developer's app, which is implemented by the developer
    const serverOrderId = 'serverOrderId';
    this.transitCardClient.deleteTransitCard(logicalCardNumber, specifiedDeviceId, serverOrderId).then(() => {
      console.info(`Succeeded in deleting TransitCard`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to delete TransitCard, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**CardMetadata**

描述卡的元数据信息。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| issuerId | string | 否 | 否 | 交通卡产品的id |
| aid | string | 否 | 否 | SE芯片中卡的小程序应用程序ID。 |
| logicalCardNumber | string | 否 | 是 | 卡的序列号。仅当设备中存在转接卡时会存在。 |
| cardNumber | string | 否 | 是 | 显示卡号（30个字符以内），如果该卡存在于设备中则会返回 |
| balance | number | 否 | 是 | 卡的余额（如果设备中存在卡） |

**CardMetadataInDevice**

设备的接口和设备支持的卡元数据。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 设备ID，开发者使用。 |
| deviceType | DeviceType | 否 | 否 | 设备的类型 |
| displayName | string | 否 | 否 | 要显示的设备名称 |
| cardMetadata | CardMetadata[] | 否 | 否 | 设备支持的卡的数据。 |

**TransitCardInfo**

交通卡信息。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cardNumber | string | 否 | 否 | 显示卡号 |
| customCardData | string | 否 | 是 | 服务提供商的自定义卡数据。json数据结构如下。 - balance：卡余额，单位分。 - expireDate：卡片过期时间。 - metroStatus：地铁刷卡进出站状态，其他交通卡不涉及。  - 1：已进站  - 2：已出站  - 3：未知 - records：交易记录，包括充值和消费两种类型。records包括以下字段。  - type：记录类型 。1：充值 ；2：消费  - amount：交易金额。单位：分。  - transDate：交易时间。  - transactionNo：交易序号。 |

**DeviceType**

设备类型的枚举。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE_PHONE | 0 | 手机设备类型 |
| DEVICE_WATCH | 1 | 穿戴手表设备类型 |