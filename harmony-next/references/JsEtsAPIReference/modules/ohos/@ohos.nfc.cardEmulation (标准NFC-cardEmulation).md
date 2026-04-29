# @ohos.nfc.cardEmulation (标准NFC-cardEmulation)

本模块主要提供NFC卡模拟业务，包括判断支持哪种卡模拟类型，HCE卡模拟的业务实现等。

HCE(Host Card Emulation)，称为基于主机的卡模拟，表示不依赖安全单元芯片，应用程序模拟NFC卡片，可以通过NFC服务和NFC读卡器通信。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### HCE卡模拟和AID列表的声明定义

开发HCE卡模拟相关应用时，需要在应用的属性配置文件中，声明与NFC相关的属性值，比如，在module.json5文件中，声明下面属性值：

```ets
// 适用于除轻量级智能穿戴产品之外其它设备
{
  "module": {
    // 其他已声明的属性
    "abilities": [
      {
        // 其他已声明的属性
        "skills": [
          {
            "actions": [
              "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
            ]
          }
        ],
        "metadata": [
          {
            "name": "payment-aid",
            "value": "your payment aid"
          },
          {
            "name": "other-aid",
            "value": "your other aid"
          }
        ]
      }
    ],
    "requestPermissions": [
      {
        "name": "ohos.permission.NFC_CARD_EMULATION",
        // 必须要添加reason: card_emulation_reason
        "reason": "$string:card_emulation_reason"
      }
    ]
}
```

```ets
// 轻量级智能穿戴设备
{
  "module": {
    // 其他已声明的属性
    "abilities": [
      {
        // 其他已声明的属性
        "metaData": {
          "customizeData": [
            {
              "name": "paymentAid",
              "value": "A0000000041012"
            },
            {
              "name": "otherAid",
              "value": "A0000000041010"
            }
          ]
        },
        "skills": [
          {
            "entities": [
              "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
            ],
            "actions": [
              "ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"
            ]
          }
        ]
      }
    ],
    "reqPermissions": [
      {
        "name": "ohos.permission.NFC_CARD_EMULATION",
        // 必须要添加reason: card_emulation_reason
        "reason": "$string:card_emulation_reason",
        "usedScene":{
          "ability":[
            "FormAbility"
          ],
          "when":"always"
        }
      },
      {
        "name": "ohos.permission.NFC_TAG",
        // 必须要添加reason: card_emulation_reason
        "reason": "$string:card_emulation_reason",
        "usedScene":{
          "ability":[
            "FormAbility"
          ],
          "when":"always"
        }
    ]
}
```

1. 声明"actions"字段的内容填写，必须包含"ohos.nfc.cardemulation.action.HOST_APDU_SERVICE"，不能更改。
1. 声明aid（参考ISO/IEC 7816-4规范）时，name必须为payment-aid或者other-aid。填写错误会造成解析失败。
1. 声明权限时"requestPermissions"中的"name"字段的内容填写，必须是"ohos.permission.NFC_CARD_EMULATION"，不能更改。
1. 轻量级智能穿戴产品不同于其他设备，仅支持FA模型，属性配置和接口调用方式与其它设备有所区别，详见示例。

#### 导入模块

```ets
// 适用于除轻量级智能穿戴产品之外其它设备
import { cardEmulation } from '@kit.ConnectivityKit';
```

```ets
// 轻量级智能穿戴设备
import cardEmulation from '@ohos.nfc.cardEmulation';
```

#### FeatureType(deprecated)

定义不同的NFC卡模拟类型。


从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[hasHceCapability](#ZH-CN_TOPIC_0000002553201411__cardemulationhashcecapability9)替代。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HCE | 0 | HCE 卡模拟。 |
| UICC | 1 | SIM 卡模拟。 |
| ESE | 2 | ESE 卡模拟。 |

#### CardType9+

定义卡模拟应用所使用的业务类型，是支付类型，还是其他类型。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAYMENT | "payment" | 卡模拟应用所使用的业务是支付类型。 |
| OTHER | "other" | 卡模拟应用所使用的业务是其他类型。 |

#### cardEmulation.isSupported(deprecated)

isSupported(feature: number): boolean

是否支持某种类型的卡模拟。


从 API version 6 开始支持，从 API version 9 开始废弃，建议使用[hasHceCapability](#ZH-CN_TOPIC_0000002553201411__cardemulationhashcecapability9)替代。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| feature | number | 是 | 卡模拟类型值，详细请见FeatureType枚举值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 支持该类型卡模拟， false: 不支持该类型卡模拟。 |

**示例：**

```ets
// 适用于除轻量级智能穿戴产品之外其它设备
import { cardEmulation } from '@kit.ConnectivityKit';

let isHceSupported: boolean = cardEmulation.isSupported(cardEmulation.FeatureType.HCE);
if (!isHceSupported) {
    console.info('this device is not supported for HCE, ignore it.');
}
```

```ets
// 适用于轻量化智能穿戴设备
import cardEmulation from '@ohos.nfc.cardEmulation';

let isHceSupported = cardEmulation.isSupported(cardEmulation.FeatureType.HCE);
if (!isHceSupported) {
    console.error('this device is not supported for HCE, ignore it.');
}
```

#### cardEmulation.hasHceCapability9+

hasHceCapability(): boolean

判断设备是否支持HCE卡模拟功能。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 支持HCE， false: 不支持HCE。 |

**错误码**：

以下错误码的详细介绍请参见[NFC错误码]([NFC错误码](../../errors/NFC错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```ets
// 适用于除轻量级智能穿戴产品之外其它设备
import { cardEmulation } from '@kit.ConnectivityKit';

let hasHceCap: boolean = cardEmulation.hasHceCapability();
if (!hasHceCap) {
    console.error('this device hasHceCapability false, ignore it.');
}
```

```ets
// 适用于轻量化智能穿戴设备
import cardEmulation from '@ohos.nfc.cardEmulation';

let hasHceCap = cardEmulation.hasHceCapability();
if (!hasHceCap) {
    console.error('this device hasHceCapability false, ignore it.');
}
```

#### cardEmulation.isDefaultService9+

isDefaultService(elementName: [ElementName](../../topics/misc/ElementName.md), type: CardType): boolean

判断指定的应用是否为指定业务类型的默认应用。

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](../../topics/misc/ElementName.md) | 是 | 所属应用声明NFC卡模拟能力的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。 |
| type | CardType | 是 | 卡模拟业务类型。目前只支持默认支付应用查询。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| boolean | true: 是默认支付应用， false: 不是默认支付应用。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
801Capability not supported.

**示例：**

```ets
// 适用于除轻量级智能穿戴产品之外其它设备
import { cardEmulation } from '@kit.ConnectivityKit';
import { bundleManager, Want } from '@kit.AbilityKit';

// 需要初始化 elementName、bundleName、abilityName，根据实际应用信息更改为正确的值
let elementName: bundleManager.ElementName = {
  bundleName: "com.example.myapplication",
  moduleName: "entry",
  abilityName: "EntryAbility"
};

let isDefaultService: boolean = cardEmulation.isDefaultService(elementName, cardEmulation.CardType.PAYMENT);
```

```ets
// 适用于轻量化智能穿戴设备
import cardEmulation from '@ohos.nfc.cardEmulation';

let appName = "com.example.testquestionlite";
let isDefaultService = cardEmulation.isDefaultService(appName, cardEmulation.CardType.PAYMENT);
```

#### HceService8+

提供HCE卡模拟的实现，主要包括接收对端读卡设备的APDU数据，并响应APDU数据到对端读卡设备。使用HCE相关接口前，必须先判断设备是否支持HCE卡模拟能力。

#### startHCE(deprecated)

startHCE(aidList: string[]): boolean

启动HCE业务功能。包括设置当前应用为前台优先，动态注册AID列表。


从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[start](#ZH-CN_TOPIC_0000002553201411__start9)替代。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| aidList | string[] | 是 | 动态注册卡模拟的AID列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 启动HCE功能或HCE已启动， false: 启动失败。 |

#### start9+

start(elementName: [ElementName](ElementName.md), aidList: string[]): void

启动HCE业务功能。包括设置当前应用为前台优先，动态注册AID列表。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](../../topics/misc/ElementName.md) | 是 | 所属应用声明NFC卡模拟能力的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。 |
| aidList | string[] | 是 | 动态注册卡模拟的AID列表，允许为空。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

#### stopHCE(deprecated)

stopHCE(): boolean

停止HCE业务功能。包括退出当前应用前台优先，释放动态注册的AID列表，释放hceCmd的订阅。


从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[stop](#ZH-CN_TOPIC_0000002553201411__stop9)替代。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true: 禁用HCE功能或HCE已禁用，false: 禁用失败。 |

**示例：**

示例请参见[on](#ZH-CN_TOPIC_0000002553201411__on8)接口的示例。

#### stop9+

stop(elementName: [ElementName](ElementName.md)): void

停止HCE业务功能。包括取消APDU数据接收的订阅，退出当前应用前台优先，释放动态注册的AID列表。应用程序需要在HCE卡模拟页面的onDestroy函数里调用该接口。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elementName | [ElementName](../../topics/misc/ElementName.md) | 是 | 所属应用声明NFC卡模拟能力的页面信息（至少包含bundleName、abilityName这两项的赋值），不可以为空。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

#### on8+

on(type: 'hceCmd', callback: AsyncCallback<number[]>): void

订阅回调，用于接收对端读卡设备发送的APDU数据，应用程序需要在HCE卡模拟页面的onCreate函数里面调用该订阅函数。使用callback异步回调。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要订阅的回调类型，固定填"hceCmd"字符串。 |
| callback | AsyncCallback<number[]> | 是 | 回调函数，返回的是符合APDU协议的数据，每个number十六进制表示，范围是0x00~0xFF。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |

**示例：**

```ets
// 适用于除轻量级智能穿戴产品之外其它设备
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cardEmulation } from '@kit.ConnectivityKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { ElementName } from './bundleManager/ElementName'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();
let element: ElementName;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onCreate');
    element = {
      bundleName: want.bundleName ?? '',
      abilityName: want.abilityName ?? '',
      moduleName: want.moduleName
    }
    const apduCallback: AsyncCallback<number[]> = (err, data) => {
      //处理数据和异常
      console.info("got apdu data");
    };
    hceService.on('hceCmd', apduCallback);
  }
  onDestroy() {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onDestroy');
    hceService.stop(element);
  }
  // 生命周期内的其它功能
}
```

**示例：**

```ets
// 适用于轻量级智能穿戴设备
import cardEmulation from '@ohos.nfc.cardEmulation';

let appName = "com.example.testquestionlite";

export default {
  data:{
    fontSize: '30px',
    fontColor: '#50609f',
    hide: 'show',
    headCon: appName,
    paymentAid: ["A0000000041010", "A0000000041012"]
  },
  onCreate() {
    console.info('onCreate');
  },
  onReady() {
    cardEmulation.hasHceCapability();
    cardEmulation.isDefaultService(appName, cardEmulation.CardType.PAYMENT);
    cardEmulation.isDefaultService(appName, cardEmulation.CardType.OTHER);
    let HceService = new cardEmulation.HceService();

    HceService.start(appName, this.paymentAid);
    HceService.on("hceCmd", (data) => {
      console.info('data:' + data);
      // 应用程序实际想要发送的数据， 此处仅做为示例
      let responseData = [0x1, 0x2];
      HceService.transmit(responseData, () => {
        console.info('sendResponse start');
      });
      console.info('sendResponse end');
    });
  },
  onDestroy() {
  }
  // 生命周期内的其它功能
}
```

#### off18+

off(type: 'hceCmd', callback?: AsyncCallback<number[]>): void

取消APDU数据接收的订阅。使用callback异步回调。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 要取消订阅的事件类型，固定填"hceCmd"字符串。 |
| callback | AsyncCallback<number[]> | 否 | 回调函数，返回的每个number十六进制表示，范围是0x00~0xFF。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```ets
// 适用于除轻量级智能穿戴产品之外其它设备
import { hilog } from '@kit.PerformanceAnalysisKit';
import { cardEmulation } from '@kit.ConnectivityKit';
import { AsyncCallback } from '@kit.BasicServicesKit';
import { ElementName } from './bundleManager/ElementName'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();
let element: ElementName;
const apduCallback: AsyncCallback<number[]> = (err, data) => {
  // 处理数据和异常
  console.info("AsyncCallback got apdu data");
};

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, param: AbilityConstant.LaunchParam) {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onCreate');
    element = {
      bundleName: want.bundleName ?? '',
      abilityName: want.abilityName ?? '',
      moduleName: want.moduleName
    }
    hceService.on('hceCmd', apduCallback);
  }
  onDestroy() {
    hilog.info(0x0000, 'testHce', '%{public}s', 'Ability onDestroy');
    hceService.off('hceCmd', apduCallback);
    hceService.stop(element);
  }
  // 生命周期内的其它功能
}
```

#### sendResponse(deprecated)

sendResponse(responseApdu: number[]): void

发送APDU数据到对端读卡设备。


从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[transmit](#ZH-CN_TOPIC_0000002553201411__transmit9)替代。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| responseApdu | number[] | 是 | 发送到对端读卡设备的符合APDU协议的数据，每个number十六进制表示，范围是0x00~0xFF。 |

#### transmit9+

transmit(response: number[]): Promise<void>

发送APDU数据到对端读卡设备，使用Promise异步回调。应用程序必须在[on](#ZH-CN_TOPIC_0000002553201411__on8)收到读卡设备发送的APDU数据后，才调用该接口响应数据。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | number[] | 是 | 发送到对端读卡设备的符合APDU协议的数据，每个number十六进制表示，范围是0x00~0xFF。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

**示例：**

```ets
// 适用于除轻量级智能穿戴产品之外其它设备
import { cardEmulation } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();

// 应用程序实际想要发送的数据， 此处仅做为示例
const responseData = [0x1, 0x2];
hceService.transmit(responseData).then(() => {
  // 处理 promise 的回调
  console.info("transmit Promise success.");
}).catch((err: BusinessError) => {
  console.error("transmit Promise error:", err);
});
```

```ets
// 适用于轻量级智能穿戴设备
import cardEmulation from '@ohos.nfc.cardEmulation';

let hceService = new cardEmulation.HceService();

// 应用程序实际想要发送的数据， 此处仅做为示例
let responseData = [0x1, 0x2];
hceService.transmit(responseData).then(() => {
  // 处理 promise 的回调
  console.info("transmit Promise success.");
});
console.info("transmit Promise end.");
```

#### transmit9+

transmit(response: number[], callback: AsyncCallback<void>): void

发送APDU数据到对端读卡设备，应用程序必须在[on](#ZH-CN_TOPIC_0000002553201411__on8)收到读卡设备发送的APDU数据后，才调用该接口响应数据。使用Callback异步回调。

**需要权限：** ohos.permission.NFC_CARD_EMULATION

**系统能力：** SystemCapability.Communication.NFC.CardEmulation

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| response | number[] | 是 | 发送到对端读卡设备的符合APDU协议的数据，每个number十六进制表示，范围是0x00~0xFF。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当发送APDU数据成功时，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[NFC错误码](NFC错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified. 2. Incorrect parameters types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3100301 | Card emulation running state is abnormal in service. |

**示例：**

```ets
// 适用于除轻量级智能穿戴产品之外其它设备
import { cardEmulation } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let hceService: cardEmulation.HceService = new cardEmulation.HceService();

// 应用程序实际想要发送的数据， 此处仅做为示例
try {
  const responseData = [0x1, 0x2];

  hceService.transmit(responseData, (err : BusinessError)=> {
    if (err) {
      console.error(`transmit AsyncCallback err Code: ${err.code}, message: ${err.message}`);
    } else {
      console.info("transmit AsyncCallback success.");
    }
  });
} catch (error) {
  console.error(`transmit AsyncCallback catch Code: ${(error as BusinessError).code}, ` +
    `message: ${(error as BusinessError).message}`);
}
```

```ets
// 适用于轻量级智能穿戴设备
import cardEmulation from '@ohos.nfc.cardEmulation';

let hceService = new cardEmulation.HceService();

// 应用程序实际想要发送的数据， 此处仅做为示例
let responseData = [0x1, 0x2];
hceService.transmit(responseData, () => {
  console.info("transmit Promise success.");
});
console.info("transmit Promise end.");
```