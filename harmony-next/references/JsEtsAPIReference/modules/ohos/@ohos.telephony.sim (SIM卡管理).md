# @ohos.telephony.sim (SIM卡管理)

SIM卡管理模块提供了SIM卡管理的基础能力，包括获取指定卡槽SIM卡的ISO国家码、归属PLMN号、服务提供商名称、SIM卡状态、卡类型、是否插卡、是否激活等。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { sim } from '@kit.TelephonyKit';
```

#### sim.isSimActive7+

isSimActive(slotId: number, callback: AsyncCallback<boolean>): void

获取指定卡槽SIM卡是否激活。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<boolean>是

回调函数。返回指定卡槽是否激活。

- true:激活。

- false：未激活。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.isSimActive(0, (err: BusinessError, data: boolean) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.isSimActive7+

isSimActive(slotId: number): Promise<boolean>

获取指定卡槽SIM卡是否激活。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<boolean>

以Promise形式返回指定卡槽是否激活。

- true:激活。

- false：未激活。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.isSimActive(0).then((data: boolean) => {
    console.info(`isSimActive success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isSimActive failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.isSimActiveSync10+

isSimActiveSync(slotId: number): boolean

获取指定卡槽SIM卡是否激活。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明boolean

返回指定卡槽是否激活。

- true:激活。

- false：未激活。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

let isSimActive: boolean = sim.isSimActiveSync(0);
console.info(`the sim is active:` + isSimActive);
```

#### sim.getDefaultVoiceSlotId7+

getDefaultVoiceSlotId(callback: AsyncCallback<number>): void

获取默认语音业务的卡槽ID。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是

回调函数。

- 0：卡槽1。

- 1：卡槽2。

- -1：未设置或服务不可用。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSlotId((err: BusinessError, data: number) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.getDefaultVoiceSlotId7+

getDefaultVoiceSlotId(): Promise<number>

获取默认语音业务的卡槽ID。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

类型说明Promise<number>

以Promise形式返回默认语音业务的卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

- -1：未设置或服务不可用。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSlotId().then((data: number) => {
    console.info(`getDefaultVoiceSlotId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultVoiceSlotId failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.hasOperatorPrivileges7+

hasOperatorPrivileges(slotId: number, callback: AsyncCallback<boolean>): void

检查应用(调用者)是否已被授予运营商权限。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<boolean>是

回调函数。 返回检查应用(调用者)是否已被授予运营商权限。

- true:授权。

- false：未授权。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasOperatorPrivileges(0, (err: BusinessError, data: boolean) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.hasOperatorPrivileges7+

hasOperatorPrivileges(slotId: number): Promise<boolean>

检查应用(调用者)是否已被授予运营商权限。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<boolean>以Promise形式返回检查应用(调用者)是否已被授予运营商权限。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasOperatorPrivileges(0).then((data: boolean) => {
    console.info(`hasOperatorPrivileges success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`hasOperatorPrivileges failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getISOCountryCodeForSim

getISOCountryCodeForSim(slotId: number, callback: AsyncCallback<string>): void

获取指定卡槽SIM卡的ISO国家码。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<string>是回调函数。返回国家码，例如：CN(中国)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getISOCountryCodeForSim(0, (err: BusinessError, data: string) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.getISOCountryCodeForSim

getISOCountryCodeForSim(slotId: number): Promise<string>

获取指定卡槽SIM卡的ISO国家码。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<string>以Promise形式返回获取指定卡槽SIM卡的ISO国家码。例如：CN(中国)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getISOCountryCodeForSim(0).then((data: string) => {
    console.info(`getISOCountryCodeForSim success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getISOCountryCodeForSim failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getISOCountryCodeForSimSync10+

getISOCountryCodeForSimSync(slotId: number): string

获取指定卡槽SIM卡的ISO国家码。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明string返回获取指定卡槽SIM卡的ISO国家码。例如：CN(中国)。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

let countryCode: string = sim.getISOCountryCodeForSimSync(0);
console.info(`the country ISO is:` + countryCode);
```

#### sim.getSimOperatorNumeric

getSimOperatorNumeric(slotId: number, callback: AsyncCallback<string>): void

获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<string>是回调函数。返回指定卡槽SIM卡的归属PLMN号。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimOperatorNumeric(0, (err: BusinessError, data: string) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.getSimOperatorNumeric

getSimOperatorNumeric(slotId: number): Promise<string>

获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<string>以Promise形式返回获取指定卡槽SIM卡的归属PLMN号。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimOperatorNumeric(0).then((data: string) => {
    console.info(`getSimOperatorNumeric success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimOperatorNumeric failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getSimOperatorNumericSync10+

getSimOperatorNumericSync(slotId: number): string

获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明string返回获取指定卡槽SIM卡的归属PLMN号。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

let numeric: string = sim.getSimOperatorNumericSync(0);
console.info(`the sim operator numeric is:` + numeric);
```

#### sim.getSimSpn

getSimSpn(slotId: number, callback: AsyncCallback<string>): void

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<string>是回调函数。返回指定卡槽SIM卡的SPN。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimSpn(0, (err: BusinessError, data: string) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.getSimSpn

getSimSpn(slotId: number): Promise<string>

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<string>以Promise形式返回获取指定卡槽SIM卡的SPN。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimSpn(0).then((data: string) => {
    console.info(`getSimSpn success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimSpn failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getSimSpnSync10+

getSimSpnSync(slotId: number): string

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明string返回获取指定卡槽SIM卡的SPN。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

let spn: string = sim.getSimSpnSync(0);
console.info(`the sim card spn is:` + spn);
```

#### sim.getSimState

getSimState(slotId: number, callback: AsyncCallback<SimState>): void

获取指定卡槽的SIM卡状态。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<[SimState](#ZH-CN_TOPIC_0000002529445457__simstate)>是回调函数。参考[SimState](#ZH-CN_TOPIC_0000002529445457__simstate)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimState(0, (err: BusinessError, data: sim.SimState) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.getSimState

getSimState(slotId: number): Promise<SimState>

获取指定卡槽的SIM卡状态。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<[SimState](#ZH-CN_TOPIC_0000002529445457__simstate)>以Promise形式返回获取指定卡槽的SIM卡状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimState(0).then((data: sim.SimState) => {
    console.info(`getSimState success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimState failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getSimStateSync10+

getSimStateSync(slotId: number): SimState

获取指定卡槽的SIM卡状态。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明[SimState](#ZH-CN_TOPIC_0000002529445457__simstate)返回获取指定卡槽的SIM卡状态。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

let simState: sim.SimState = sim.getSimStateSync(0);
console.info(`The sim state is:` + simState);
```

#### sim.getCardType7+

getCardType(slotId: number, callback: AsyncCallback<CardType>): void

获取指定卡槽SIM卡的卡类型。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<[CardType](#ZH-CN_TOPIC_0000002529445457__cardtype7)>是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getCardType(0, (err: BusinessError, data: sim.CardType) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.getCardType7+

getCardType(slotId: number): Promise<CardType>

获取指定卡槽SIM卡的卡类型。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<[CardType](#ZH-CN_TOPIC_0000002529445457__cardtype7)>以Promise形式返回指定卡槽SIM卡的卡类型。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getCardType(0).then((data: sim.CardType) => {
    console.info(`getCardType success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getCardType failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getCardTypeSync10+

getCardTypeSync(slotId: number): CardType

获取指定卡槽SIM卡的卡类型。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明[CardType](#ZH-CN_TOPIC_0000002529445457__cardtype7)返回指定卡槽SIM卡的卡类型。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

let cardType: sim.CardType = sim.getCardTypeSync(0);
console.info(`the card type is:` + cardType);
```

#### sim.hasSimCard7+

hasSimCard(slotId: number, callback: AsyncCallback<boolean>): void

获取指定卡槽SIM卡是否插卡。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<boolean>是

回调返回指定卡槽是否插卡。

- true:插卡。

- false：未插卡。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasSimCard(0, (err: BusinessError, data: boolean) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.hasSimCard7+

hasSimCard(slotId: number): Promise<boolean>

获取指定卡槽SIM卡是否插卡。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<boolean>

以Promise形式返回指定卡槽是否插卡。

- true:插卡。

- false：未插卡。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.hasSimCard(0).then((data: boolean) => {
    console.info(`hasSimCard success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`hasSimCard failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.hasSimCardSync10+

hasSimCardSync(slotId: number): boolean

获取指定卡槽SIM卡是否插卡。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明boolean

返回指定卡槽是否插卡。

- true:插卡。

- false：未插卡。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

let hasSimCard: boolean = sim.hasSimCardSync(0);
console.info(`has sim card: ` + hasSimCard);
```

#### sim.getSimAccountInfo10+

getSimAccountInfo(slotId: number, callback: AsyncCallback<IccAccountInfo>): void

获取SIM卡帐户信息。使用callback异步回调。

**需要权限**：ohos.permission.GET_TELEPHONY_STATE

获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<[IccAccountInfo](#ZH-CN_TOPIC_0000002529445457__iccaccountinfo10)>是回调函数。返回指定卡槽SIM卡的帐户信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.8301002The SIM card failed to read or update data.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAccountInfo(0, (err:BusinessError , data: sim.IccAccountInfo) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.getSimAccountInfo10+

getSimAccountInfo(slotId: number): Promise<IccAccountInfo>

获取SIM卡帐户信息。使用Promise异步回调。

**需要权限**：ohos.permission.GET_TELEPHONY_STATE

获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<[IccAccountInfo](#ZH-CN_TOPIC_0000002529445457__iccaccountinfo10)>以Promise形式返回指定卡槽SIM卡的帐户信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.8301002The SIM card failed to read or update data.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimAccountInfo(0).then((data: sim.IccAccountInfo) => {
    console.info(`getSimAccountInfo success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSimAccountInfo failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getActiveSimAccountInfoList10+

getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void

获取激活SIM卡帐户信息列表。使用callback异步回调。

**需要权限**：ohos.permission.GET_TELEPHONY_STATE

获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明callbackAsyncCallback<Array<[IccAccountInfo](#ZH-CN_TOPIC_0000002529445457__iccaccountinfo10)>>是回调函数。返回激活SIM卡帐户信息列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getActiveSimAccountInfoList((err: BusinessError, data: Array<sim.IccAccountInfo>) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.getMaxSimCount7+

getMaxSimCount(): number

获取卡槽数量。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

类型说明number卡槽数量。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

console.info("Result: "+ sim.getMaxSimCount());
```

#### sim.getActiveSimAccountInfoList10+

getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>

获取激活SIM卡帐户信息列表。使用Promise异步回调。

**需要权限**：ohos.permission.GET_TELEPHONY_STATE

获取ICCID和号码信息时需要GET_TELEPHONY_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

类型说明Promise<Array<[IccAccountInfo](#ZH-CN_TOPIC_0000002529445457__iccaccountinfo10)>>以Promise形式返回激活卡槽SIM卡的帐户信息列表。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getActiveSimAccountInfoList().then((data: Array<sim.IccAccountInfo>) => {
    console.info(`getActiveSimAccountInfoList success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getActiveSimAccountInfoList failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getOpKey9+

getOpKey(slotId: number, callback: AsyncCallback<string>): void

获取指定卡槽中SIM卡的opkey。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<string>是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

try {
    sim.getOpKey(0, (err: BusinessError, data: string) => {
    if (err) {
      console.error("getOpKey failed, err: " + JSON.stringify(err));
    } else {
      console.info('getOpKey successfully, data: ' + JSON.stringify(data));
    }
  });
} catch (err) {
  console.error("getOpKey err: " + JSON.stringify(err));
}
```

#### sim.getOpKey9+

getOpKey(slotId: number): Promise<string>

获取指定卡槽中SIM卡的opkey。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<string>以Promise形式返回指定卡槽中SIM卡的opkey。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getOpKey(0).then((data: string) => {
    console.info(`getOpKey success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getOpKey failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getOpKeySync10+

getOpKeySync(slotId: number): string

获取指定卡槽中SIM卡的opkey。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明string返回指定卡槽中SIM卡的opkey。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

let data: string = sim.getOpKeySync(0);
console.info(`getOpKey success, promise: data->${JSON.stringify(data)}`);
```

#### sim.getOpName9+

getOpName(slotId: number, callback: AsyncCallback<string>): void

获取指定卡槽中SIM卡的OpName。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<string>是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

try {
    sim.getOpName(0, (err: BusinessError, data: string) => {
    if (err) {
      console.error("getOpName failed, err: " + JSON.stringify(err));
    } else {
      console.info('getOpName successfully, data: ' + JSON.stringify(data));
    }
  });
} catch (err) {
  console.error("getOpName err: " + JSON.stringify(err));
}
```

#### sim.getOpName9+

getOpName(slotId: number): Promise<string>

获取指定卡槽中SIM卡的OpName。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<string>以Promise形式返回指定卡槽中SIM卡的OpName。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.801Capability not supported.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getOpName(0).then((data: string) => {
    console.info(`getOpName success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getOpName failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getOpNameSync10+

getOpNameSync(slotId: number): string

获取指定卡槽中SIM卡的OpName。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明string返回指定卡槽中SIM卡的OpName。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

let data: string = sim.getOpNameSync(0);
console.info(`getOpName success, promise: data->${JSON.stringify(data)}`);
```

#### sim.getDefaultVoiceSimId10+

getDefaultVoiceSimId(callback: AsyncCallback<number>): void

获取默认语音业务的SIM卡ID。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是

回调函数。

与SIM卡绑定，从1开始递增。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.8301001SIM card is not activated.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getDefaultVoiceSimId((err: BusinessError, data: number) => {
    console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.getDefaultVoiceSimId10+

getDefaultVoiceSimId(): Promise<number>

获取默认语音业务的SIM卡ID。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

类型说明Promise<number>

以Promise形式返回默认语音业务的SIM卡ID。

与SIM卡绑定，从1开始递增。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300004No SIM card found.8300999Unknown error.8301001SIM card is not activated.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

let promise = sim.getDefaultVoiceSimId();
promise.then((data: number) => {
    console.info(`getDefaultVoiceSimId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultVoiceSimId failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getSimLabel20+

getSimLabel(slotId: number, callback: AsyncCallback<SimLabel>): void

查看卡槽ID和SIM卡的对应关系：- 卡槽1对应SIM卡1或SIM卡2- 卡槽2对应SIM卡2或ESIMX

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<[SimLabel](#ZH-CN_TOPIC_0000002529445457__simlabel20)>是回调函数。获取SIM卡标签信息。

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimLabel(0, (err: BusinessError, data: sim.SimLabel) => {
  console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sim.getSimLabel20+

getSimLabel(slotId: number): Promise<SimLabel>

获取SIM卡的标签信息。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<[SimLabel](#ZH-CN_TOPIC_0000002529445457__simlabel20) >回调函数。获取SIM卡标签信息。

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { sim } from '@kit.TelephonyKit';

sim.getSimLabel(0).then((data: sim.SimLabel) => {
  console.info(`getSimLabel success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getSimState failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sim.getSimLabelSync20+

getSimLabelSync(slotId: number): SimLabel

通过传入SIM卡槽的ID，获取对应的SIM卡标签。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明[SimLabel](#ZH-CN_TOPIC_0000002529445457__simlabel20)SIM卡标签。

**示例：**

```ets
import { sim } from '@kit.TelephonyKit';

let simLabel: sim.SimLabel = sim.getSimLabelSync(0);
console.info(`The sim state is:` + simLabel);
```

#### SimType20+

SIM卡类型的枚举。

**系统能力**：SystemCapability.Telephony.CoreService

名称值说明PSIM0实体SIM卡。ESIM1电子SIM卡。

#### SimLabel20+

SIM卡标签。

**系统能力**：SystemCapability.Telephony.CoreService

名称类型只读可选说明simType[SimType](#ZH-CN_TOPIC_0000002529445457__simtype20)否否表示SIM卡类型的枚举。indexnumber否否SIM卡的唯一标识索引值。

#### SimState

SIM卡状态。

**系统能力**：SystemCapability.Telephony.CoreService

名称值说明SIM_STATE_UNKNOWN0SIM卡状态未知，即无法获取准确的状态。SIM_STATE_NOT_PRESENT1表示SIM卡处于not present状态，即卡槽中没有插入SIM卡。SIM_STATE_LOCKED2表示SIM卡处于locked状态，即SIM卡被PIN、PUK或网络锁锁定。SIM_STATE_NOT_READY3表示SIM卡处于not ready状态，即SIM卡在位但无法正常工作。SIM_STATE_READY4表示SIM卡处于ready状态，即SIM卡在位且工作正常。SIM_STATE_LOADED5表示SIM卡处于loaded状态，即SIM卡在位且所有卡文件加载完毕。

#### CardType7+

卡类型。

**系统能力**：SystemCapability.Telephony.CoreService

名称值说明UNKNOWN_CARD-1未知类型。SINGLE_MODE_SIM_CARD10单SIM卡。SINGLE_MODE_USIM_CARD20单USIM卡。SINGLE_MODE_RUIM_CARD30单RUIM卡。DUAL_MODE_CG_CARD40双卡模式C+G。CT_NATIONAL_ROAMING_CARD41中国电信内部漫游卡。CU_DUAL_MODE_CARD42中国联通双模卡。DUAL_MODE_TELECOM_LTE_CARD43双模式电信LTE卡。DUAL_MODE_UG_CARD50双模式UG卡。SINGLE_MODE_ISIM_CARD8+60单一ISIM卡类型。

#### IccAccountInfo10+

Icc帐户信息。

**系统能力**：SystemCapability.Telephony.CoreService

名称类型只读可选说明simIdnumber否否SIM卡ID。slotIndexnumber否否卡槽ID。isEsimboolean否否

标记卡是否是eSim。

- true:是eSim。

- false：不是eSim。

isActiveboolean否否

卡是否被激活。

- true:激活。

- false：未激活。

iccIdstring否否ICCID号码。showNamestring否否SIM卡显示名称。showNumberstring否否SIM卡显示号码。