# walletPass（Pass卡片能力）

本模块提供接入钱包服务的能力。

起始版本： 5.0.0(12)

**导入模块**

```ets
import { walletPass } from '@kit.WalletKit';
```

**WalletPassClient**

钱包卡券的功能入口类，与钱包卡券有关的所有方法从此处接入。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

**constructor**

constructor(context: common.UIAbilityContext)

构造函数。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext | 是 | UIAbility上下文。 |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);

  build() {
    // your application UI
  }
```

**queryPassDeviceInfo**

queryPassDeviceInfo(passStr: string): Promise<string>

查询当前设备唯一标识及设备能力，用于关联已开通的云侧卡券，同时开卡过程可指定目标设备标识，提升安全性。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、targetDeviceType。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - targetDeviceType：目标设备类型。取值如下 - phone：手机 - wear：穿戴 - all：手机+穿戴 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在数组类型的JSON String中，并通过该参数传出。 key包括deviceType、passDeviceId、deviceModel、passCapabilityVersion、deviceModelNumber、deviceCapabilities。 - deviceType：设备类型。取值如下 - phone：手机 - wear：穿戴 - passDeviceId：账号/设备联合标识符。 - deviceModel：设备名，用于展示可开通的设备名称。 - passCapabilityVersion：WalletKit开放能力版本号，用于版本兼容处理，初始为 1。 - deviceModelNumber：设备型号编码，用于获取匹配的标定数据。 - deviceCapabilities：能力集，同步返回是否支持NFC/BLE/UWB/SLE - NFC：0200 - NFC+BLE：0201 - UWB：0202 - SLE：0203 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected |
| 1010220003 | Pass service is temporarily unavailable. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200010 | Network connection error. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private passType: string = '';
  private targetDeviceType: string = '';

  async queryPassDeviceInfo() {
    let passStr = JSON.stringify({
      passType: this.passType,
      targetDeviceType: this.targetDeviceType
    });
    this.walletPassClient.queryPassDeviceInfo(passStr).then((result: string) => {
      console.info(`Succeeded in querying passDeviceInfo, result:${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to query passDeviceInfo, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**canAddPass**

canAddPass(passStr: string): Promise<string>

检查当前设备是否支持添加卡券，返回结果码。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、targetDeviceType。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - targetDeviceType：目标设备类型。取值如下 - phone: 手机 - wear：穿戴 - all：手机+穿戴 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在数组类型的JSON String中，并通过该参数传出。 key包括passType、deviceType、passDeviceId、deviceModel、result。 - passType：服务号 - deviceType：设备类型。取值如下 - phone：手机 - wear：穿戴 - passDeviceId：账号/设备联合标识符。 - deviceModel：设备名，用于展示可开通的设备名称。 - result：结果码。取值如下 0：支持添加 1：ROM版本过低 2：钱包版本过低 3：ROM版本和钱包版本均过低 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200004 | The device does not support this card. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200009 | The chip space is full, and no more cards can be added. |
| 1010200010 | Network connection error. |
| 1010220002 | The card already exists in the specified device. |
| 1010220003 | Pass service is temporarily unavailable. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200015 | This card is not available for a child account. |
| 1010200016 | This card is not available for the current country or region. |
| 1010220005 | The number of cards has reached the upper limit. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private passType: string = '';
  private targetDeviceType: string = '';

  async canAddPass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      targetDeviceType: this.targetDeviceType
    });
    this.walletPassClient.canAddPass(passStr).then((result: string) => {
      console.info(`Succeeded in checking addPass, result:${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to check addPass, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**initWalletEnvironment**

initWalletEnvironment(passStr: string): Promise<void>

初始化钱包开通卡券的同意协议或是登录账号，引导用户跳转钱包完成应用初始化。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括targetDeviceType。 - targetDeviceType：目标设备类型。取值如下 - phone: 手机 - wear：穿戴 - all：手机+穿戴 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200002 | Wallet app not found. |
| 1010200005 | The operation was canceled by the user. |
| 1010200011 | Failed to initialize the environment. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200017 | The Wallet app was closed by the user. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private targetDeviceType: string = '';

  async initWalletEnvironment() {
    let passStr = JSON.stringify({
      targetDeviceType: this.targetDeviceType
    });
    this.walletPassClient.initWalletEnvironment(passStr).then(() => {
      console.info(`Succeeded in initiating walletEnvironment`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to initiate walletEnvironment, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**addPass**

addPass(passStr: string): Promise<string>

用户主动发起开卡时，跳转钱包应用，携带开卡JWE数据，开通卡券到钱包并激活。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括jweContent。 - jweContent：生成JWE数据章节生成的开卡签名数据包。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。 key包括passType、serialNumber、deviceType、passDeviceId。 - passType： 开通的卡片服务号 。 - serialNumber： 开通的 Pass 卡片唯一标识 。 - deviceType：开卡设备的类型。取值如下 - phone: 手机 - wear：穿戴 - all：手机+穿戴 - passDeviceId： 开卡设备的帐号/设备联合标识符。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200002 | Wallet app not found. |
| 1010200004 | The device does not support this card. |
| 1010200005 | The operation was canceled by the user. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200009 | The chip space is full, and no more cards can be added. |
| 1010200012 | Duplicate request. |
| 1010220002 | The card already exists in the specified device. |
| 1010220003 | Pass service is temporarily unavailable. |
| 1010220401 | Failed to add the card because the signature verification failed. |
| 1010220402 | Failed to add the card because the data decryption failed. |
| 1010220403 | Failed to add the card because the instance ID does not exist. |
| 1010220404 | Failed to add the card because the instance ID has been used. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200015 | This card is not available for a child account. |
| 1010200016 | This card is not available for the current country or region. |
| 1010200017 | The Wallet app was closed by the user. |
| 1010220005 | The number of cards has reached the upper limit. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private jweContent: string = '';

  async addPass() {
    let passStr = JSON.stringify({
      jweContent: this.jweContent
    });
    this.walletPassClient.addPass(passStr).then((result: string) => {
      console.info(`Succeeded in adding pass, result:${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to add pass, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**queryPass**

queryPass(passStr: string): Promise<string>

检查当前设备卡券的开通情况。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、serialNumber。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - serialNumber：申请钥匙卡片时定义的卡券唯一标识。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在数组类型的JSON String中，并通过该参数传出。 key包括passType、serialNumber、deviceType、passDeviceId、deviceModel、cardStatus。 - passType：服务号 - serialNumber：卡券唯一标识 - deviceType：设备类型。取值如下 - phone：手机 - wear：穿戴 - passDeviceId：账号/设备联合标识符。 - deviceModel：设备名，用于展示可开通的设备名称。 - cardStatus：卡片状态 。取值如下 0：可用 1：不可用 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200003 | The environment of the wallet is not ready. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010220501 | No card that meets the search criteria is found. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private passType: string = '';
  private serialNumber: string = '';

  async queryPass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.queryPass(passStr).then((result: string) => {
      console.info(`Succeeded in querying pass, result: ${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to query pass, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**viewPass**

viewPass(passStr: string): Promise<void>

跳转钱包查看已开通的卡券详情页。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、serialNumber。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - serialNumber：申请钥匙卡片时定义的卡券唯一标识。 |

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

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private passType: string = '';
  private serialNumber: string = '';

  async viewPass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    try {
      await this.walletPassClient.viewPass(passStr);
      console.info(`Succeeded in viewing pass`);
    } catch (err) {
      console.error(`Failed to view pass, code:${err.code}, message:${err.message}`);
    }

  build() {
    // your application UI
  }
```

**updatePass**

updatePass(passStr: string): Promise<string>

卡券更新（预留接口，暂不提供具体功能）。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、serialNumber。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - serialNumber：申请钥匙卡片时定义的卡券唯一标识。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。 key包括result。 - result：卡券更新结果0，全部更新完成后返回操作成功。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200005 | The operation was canceled by the user. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010220003 | Pass service is temporarily unavailable. |
| 1010220004 | The card does not exist in the specified device. |
| 1010220701 | Failed to update the card because no update is detected. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200010 | Network connection error. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private passType: string = '';
  private serialNumber: string = '';

  async updatePass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.updatePass(passStr).then((result: string) => {
      console.info(`Succeeded in updating pass,result: ${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to update pass, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**deletePass**

deletePass(passStr: string): Promise<string>

卡券删除（预留接口，暂不提供具体功能）。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| passStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、serialNumber。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - serialNumber：申请钥匙卡片时定义的卡券唯一标识。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。 key包括result。 - result：卡券删除结果0，全部删除完成后返回操作成功。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200005 | The operation was canceled by the user. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200012 | Duplicate request. |
| 1010220003 | Pass service is temporarily unavailable. |
| 1010220004 | The card does not exist in the specified device. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |
| 1010200010 | Network connection error. |
| 1010220801 | Failed to delete the card because the signature verification failed. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private passType: string = '';
  private serialNumber: string = '';

  async deletePass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.deletePass(passStr).then((result: string) => {
      console.info(`Succeeded in deleting pass, result: ${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to delete pass, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**queryICCEConnectionState**

queryICCEConnectionState(rkeStr: string): Promise<string>

查询车控连接状态。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rkeStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、serialNumber。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - serialNumber：申请钥匙卡片时定义的卡券唯一标识。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。 key包括deviceType、passDeviceId、deviceModel、connectionState、authState。 - deviceType：设备类型。取值如下 - phone：手机 - wear：穿戴 - passDeviceId：账号/设备联合标识符。 - deviceModel：设备名，用于展示可开通的设备名称。 - connectionState：连接状态。取值如下 0：异常状态 1：正在连接 2：连接成功 3：未连接 4：连接超时 10：未配对 11：配对中 12：已配对 - authState：认证状态。取值如下 0：未认证/认证失败 1：认证成功 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010220004 | The card does not exist in the specified device. |
| 1010220006 | Bluetooth permission is not granted. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private passType: string = '';
  private serialNumber: string = '';

  async queryICCEConnectionState() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.queryICCEConnectionState(passStr).then((result: string) => {
      console.info(`Succeeded in querying ICCEConnectionState, result: ${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to query ICCEConnectionState, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**startICCEConnection**

startICCEConnection(rkeStr: string): Promise<string>

车控连接。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rkeStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、serialNumber。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - serialNumber：申请钥匙卡片时定义的卡券唯一标识。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。 key包括result、deviceType、passDeviceId、deviceModel、connectionState、authState、reasonCode。 result：认证状态。取值如下 0：已配对已连接 1：已配对未连接 2：未配对 deviceType：设备类型。取值如下 phone：手机 wear：穿戴 passDeviceId：账号/设备联合标识符。 deviceModel：设备名，用于展示可开通的设备名称。 connectionState：连接状态。取值如下 0：异常状态 1：正在连接 2：连接成功 3：未连接 4：连接超时 10：未配对 11：配对中 12：已配对 authState：认证状态。取值如下 0：未认证/认证失败 1：认证成功 reasonCode：异常原因码，只有result为2时才会返回。取值如下 1：表侧星闪开关未开启 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200005 | The operation was canceled by the user. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200010 | Network connection error. |
| 1010200012 | Duplicate request. |
| 1010221001 | Connection failed because the pairing code is not obtained. |
| 1010220004 | The card does not exist in the specified device. |
| 1010220006 | Bluetooth permission is not granted. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private passType: string = '';
  private serialNumber: string = '';

  async startICCEConnection() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.startICCEConnection(passStr).then((result: string) => {
      console.info(`Succeeded in starting ICCEConnection, result: ${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to start ICCEConnection, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**registerICCEListener**

registerICCEListener(rkeStr: string, eventNotifyListener: rpc.RemoteObject): Promise<string>

注册监听。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rkeStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、registerName。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - registerName：注册监听的应用名称，一般为包名。 |
| eventNotifyListener | rpc.RemoteObject | 是 | 回调事件，rpc.RemoteObject格式。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。 key包括result。 result：注册成功结果0。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010221101 | Registration failed because of duplicate register name. |
| 1010200012 | Duplicate request. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

class ICCECallBack extends rpc.RemoteObject {
  constructor() {
    super('ICCECallBack');
  }

  async onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption): Promise<boolean> {
    // processing after receiving communication data
    let codeInt = data.readInt();
    return true;
  }

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private callback: rpc.RemoteObject | null = null;
  private passType: string = '';
  private registerName: string = '';

  async registerICCEListener() {
    let passStr = JSON.stringify({
      passType: this.passType,
      registerName: this.registerName
    });
    this.callback = new ICCECallBack();
    this.walletPassClient.registerICCEListener(passStr, this.callback).then((result: string) => {
      console.info(`Succeeded in registering ICCEListener, result: ${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to register ICCEListener, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**unregisterICCEListener**

unregisterICCEListener(rkeStr: string): Promise<string>

解注册监听。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rkeStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、registerName。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - registerName：注册监听的应用名称，一般为包名。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。 key包括result。 result：解注册成功结果0。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010221201 | The registration may have been unregistered before. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private callback: rpc.RemoteObject | null = null;
  private passType: string = '';
  private registerName: string = '';

  async unregisterICCEListener() {
    let passStr = JSON.stringify({
      passType: this.passType,
      registerName: this.registerName
    });

    this.walletPassClient.unregisterICCEListener(passStr).then((result: string) => {
      console.info(`Succeeded in unregistering ICCEListener, result: ${result}`);
      this.callback = null;
    }).catch((err: BusinessError) => {
      console.error(`Failed to unregister ICCEListener, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```

**sendICCERKEMessage**

sendICCERKEMessage(rkeStr: string): Promise<string>

发送车控指令。

使用Promise异步回调。

不支持多线程调用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Payment.Wallet

起始版本： 5.0.0(12)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rkeStr | string | 是 | 要求JSON String格式，传入的字段以key-value的形式设置在JSON String中，并通过该参数传入。 key包括passType、serialNumber、rkeCommand、encryptFlag、directionFlag。 - passType：创建Wallet Kit服务时注册的服务号，需要开发者到华为AGC网站申请。 - serialNumber：申请钥匙卡片时定义的卡券唯一标识。 - rkeCommand：请求指令。 - encryptFlag：加密指示位。取值如下 0：不加密 1：需要基于通道会话秘钥加密 - directionFlag：方向指示位。取值如下 0：上报结果 1：发送指令 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，JSON String格式，传出的字段以key-value的形式设置在JSON String中，并通过该参数传出。 key包括deviceType、passDeviceId、deviceModel、result。 - deviceType：设备类型。取值如下 - phone：手机 - wear：穿戴 - passDeviceId：账号/设备联合标识符。 - deviceModel：设备名，用于展示可开通的设备名称。 - result：车控发起结果，发送至车辆后立即返回。取值如下 - 0：发送成功 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 1010200001 | No permission to access the Wallet APIs. |
| 1010200002 | Wallet app not found. |
| 1010200006 | The device's remote paired watch cannot be connected. |
| 1010200012 | Duplicate request. |
| 1010220004 | The card does not exist in the specified device. |
| 1010220006 | Bluetooth permission is not granted. |
| 1010221301 | Failed to send the RKE message because of a connection failure. |
| 1010221302 | Failed to send the RKE message because of an authentication failure. |
| 1010200013 | Operation failed because of an internal error. |
| 1010200014 | The Wallet APIs can be called by the device owner only. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  private serialNumber: string = '';
  private passType: string = '';
  private rkeCommand: string = '';

  async sendICCERKEMessage() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber,
      rkeCommand: this.rkeCommand,
      encryptFlag: '0',
      directionFlag: '1'
    });
    this.walletPassClient.sendICCERKEMessage(passStr).then((result: string) => {
      console.info(`Succeeded in sending ICCERKEMessage, result: ${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to send ICCERKEMessage, code:${err.code}, message:${err.message}`);
    })
  }

  build() {
    // your application UI
  }
```