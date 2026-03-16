# @ohos.telephony.radio (网络搜索)

网络搜索模块提供管理网络搜索的一些基础功能，包括获取当前接入的CS域和PS域无线接入技术、获取网络状态、获取当前选网模式、获取注册网络所在国家的ISO国家码、获取主卡所在卡槽的索引号、获取指定SIM卡槽对应的注册网络信号强度信息列表、获取运营商名称，判断当前设备是否支持NR(New Radio)、判断主卡的Radio是否打开等。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { radio } from '@kit.TelephonyKit';
```

#### radio.getRadioTech

getRadioTech(slotId: number, callback: AsyncCallback<[NetworkRadioTech](#ZH-CN_TOPIC_0000002529285483__networkradiotech11)>): void

获取当前接入的CS域和PS域无线接入技术。使用callback异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<[NetworkRadioTech](#ZH-CN_TOPIC_0000002529285483__networkradiotech11)>是回调函数。返回当前接入的CS域和PS域无线接入技术。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getRadioTech(slotId, (err: BusinessError, data: radio.NetworkRadioTech) => {
    if (err) {
        console.error(`getRadioTech failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.log(`getRadioTech success, callback: data->${JSON.stringify(data)}`);
});
```

#### radio.getRadioTech

getRadioTech(slotId: number): Promise<[NetworkRadioTech](#ZH-CN_TOPIC_0000002529285483__networkradiotech11)>

获取当前接入的CS域和PS域无线接入技术。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<[NetworkRadioTech](#ZH-CN_TOPIC_0000002529285483__networkradiotech11)>以Promise形式返回当前接入的CS域和PS域技术。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getRadioTech(slotId).then((data: radio.NetworkRadioTech) => {
    console.log(`getRadioTech success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getRadioTech failed, promise: err->${JSON.stringify(err)}`);
});
```

#### radio.getRadioTechSync18+

getRadioTechSync(slotId: number): [NetworkRadioTech](#ZH-CN_TOPIC_0000002529285483__networkradiotech11)

获取当前接入的CS域和PS域无线接入技术。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明[NetworkRadioTech](#ZH-CN_TOPIC_0000002529285483__networkradiotech11)返回当前接入的CS域和PS域技术。

**示例：**

```ets
let slotId: number = 0;
let networkRadioTech: radio.NetworkRadioTech = radio.getRadioTechSync(slotId);
console.info(`getRadioTechSync success, NetworkRadioTech->${JSON.stringify(networkRadioTech)}`);
```

#### radio.getNetworkState

getNetworkState(callback: AsyncCallback<NetworkState>): void

获取网络状态。使用callback异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明callbackAsyncCallback<[NetworkState](#ZH-CN_TOPIC_0000002529285483__networkstate)>是回调函数。返回当前网络状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

radio.getNetworkState((err: BusinessError, data: radio.NetworkState) => {
    if (err) {
        console.error(`getNetworkState failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.log(`getNetworkState success, callback: data->${JSON.stringify(data)}`);
});
```

#### radio.getNetworkState

getNetworkState(slotId: number, callback: AsyncCallback<NetworkState>): void

获取网络状态。使用callback异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<[NetworkState](#ZH-CN_TOPIC_0000002529285483__networkstate)>是回调函数。返回当前网络状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkState(slotId, (err: BusinessError, data: radio.NetworkState) => {
    if (err) {
        console.error(`getNetworkState failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.log(`getNetworkState success, callback: data->${JSON.stringify(data)}`);
});
```

#### radio.getNetworkState

getNetworkState(slotId?: number): Promise<NetworkState>

获取网络状态。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber否

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

 未指定卡槽时，默认为卡槽1。

**返回值：**

类型说明Promise<[NetworkState](#ZH-CN_TOPIC_0000002529285483__networkstate)>以Promise形式返回网络状态。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkState(slotId).then((data: radio.NetworkState) => {
    console.log(`getNetworkState success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getNetworkState failed, promise: err->${JSON.stringify(err)}`);
});
```

#### radio.getNetworkSelectionMode

getNetworkSelectionMode(slotId: number, callback: AsyncCallback<NetworkSelectionMode>): void

获取当前选网模式。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<[NetworkSelectionMode](#ZH-CN_TOPIC_0000002529285483__networkselectionmode)>是回调函数。返回当前选网模式。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkSelectionMode(slotId, (err: BusinessError, data: radio.NetworkSelectionMode) => {
    if (err) {
        console.error(`getNetworkSelectionMode failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.log(`getNetworkSelectionMode success, callback: data->${JSON.stringify(data)}`);
});
```

#### radio.getNetworkSelectionMode

getNetworkSelectionMode(slotId: number): Promise<NetworkSelectionMode>

获取当前选网模式。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<[NetworkSelectionMode](#ZH-CN_TOPIC_0000002529285483__networkselectionmode)>以Promise形式返回当前选网模式。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkSelectionMode(slotId).then((data: radio.NetworkSelectionMode) => {
    console.log(`getNetworkSelectionMode success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getNetworkSelectionMode failed, promise: err->${JSON.stringify(err)}`);
});
```

#### radio.getISOCountryCodeForNetwork7+

getISOCountryCodeForNetwork(slotId: number, callback: AsyncCallback<string>): void

获取注册网络所在国家的ISO国家码。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<string>是回调函数。返回国家码，例如：CN(中国)。如果设备没有注册任何网络，接口返回空字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getISOCountryCodeForNetwork(slotId, (err: BusinessError, data: string) => {
    if (err) {
        console.error(`getISOCountryCodeForNetwork failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.log(`getISOCountryCodeForNetwork success, callback: data->${JSON.stringify(data)}`);
});
```

#### radio.getISOCountryCodeForNetwork7+

getISOCountryCodeForNetwork(slotId: number): Promise<string>

获取注册网络所在国家的ISO国家码。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<string>以Promise形式返回注册网络所在国家的ISO国家码，例如CN(中国)。如果设备没有注册任何网络，接口返回空字符串。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getISOCountryCodeForNetwork(slotId).then((data: string) => {
    console.log(`getISOCountryCodeForNetwork success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getISOCountryCodeForNetwork failed, promise: err->${JSON.stringify(err)}`);
});
```

#### radio.getISOCountryCodeForNetworkSync10+

getISOCountryCodeForNetworkSync(slotId: number): string

获取注册网络所在国家的ISO国家码。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明string返回注册网络所在国家的ISO国家码，例如CN(中国)。如果设备没有注册任何网络，接口返回空字符串。

**示例：**

```ets
let slotId: number = 0;
let countryISO: string = radio.getISOCountryCodeForNetworkSync(slotId);
console.log(`the country ISO is:` + countryISO);
```

#### radio.getPrimarySlotId7+

getPrimarySlotId(callback: AsyncCallback<number>): void

获取主卡所在卡槽的索引号。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是回调函数。返回主卡所在卡槽的索引号。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

radio.getPrimarySlotId((err: BusinessError, data: number) => {
    if (err) {
        console.error(`getPrimarySlotId failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.log(`getPrimarySlotId success, callback: data->${JSON.stringify(data)}`);
});
```

#### radio.getPrimarySlotId7+

getPrimarySlotId(): Promise<number>

获取主卡所在卡槽的索引号。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

类型说明Promise<number>以Promise形式返回获取设备主卡所在卡槽的索引号的结果。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

radio.getPrimarySlotId().then((data: number) => {
    console.log(`getPrimarySlotId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getPrimarySlotId failed, promise: err->${JSON.stringify(err)}`);
});
```

#### radio.getSignalInformation7+

getSignalInformation(slotId: number, callback: AsyncCallback<Array<SignalInformation>>): void

获取指定SIM卡槽对应的注册网络信号强度信息列表。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<Array<[SignalInformation](#ZH-CN_TOPIC_0000002529285483__signalinformation)>>是回调函数，返回从[SignalInformation](#ZH-CN_TOPIC_0000002529285483__signalinformation)中派生出的子类对象的数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getSignalInformation(slotId, (err: BusinessError, data: Array<radio.SignalInformation>) => {
    if (err) {
        console.error(`getSignalInformation failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.log(`getSignalInformation success, callback: data->${JSON.stringify(data)}`);
});
```

#### radio.getSignalInformation7+

getSignalInformation(slotId: number): Promise<Array<SignalInformation>>

获取指定SIM卡槽对应的注册网络信号强度信息列表。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<Array<[SignalInformation](#ZH-CN_TOPIC_0000002529285483__signalinformation)>>以Promise形式返回网络信号强度[SignalInformation](#ZH-CN_TOPIC_0000002529285483__signalinformation)子类对象的数组。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getSignalInformation(slotId).then((data: Array<radio.SignalInformation>) => {
    console.log(`getSignalInformation success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSignalInformation failed, promise: err->${JSON.stringify(err)}`);
});
```

#### radio.getSignalInformationSync10+

getSignalInformationSync(slotId: number): Array<SignalInformation>

获取指定SIM卡槽对应的注册网络信号强度信息列表。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Array<[SignalInformation](#ZH-CN_TOPIC_0000002529285483__signalinformation)>返回网络信号强度[SignalInformation](#ZH-CN_TOPIC_0000002529285483__signalinformation)子类对象的数组。

**示例：**

```ets
let slotId: number = 0;
let signalInfo: Array<radio.SignalInformation> = radio.getSignalInformationSync(slotId);
console.log(`signal information size is:` + signalInfo.length);
```

#### radio.isNrSupported8+(deprecated)

isNrSupported(): boolean

判断当前设备是否支持NR(New Radio)。

从 API version 7开始支持，从API version 9开始废弃。建议使用[isNRSupported](#ZH-CN_TOPIC_0000002529285483__radioisnrsupported9)替代。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

类型说明boolean

- true：支持。

- false：不支持。

**示例：**

```ets
let result: boolean = radio.isNrSupported();
console.log("Result: "+ result);
```

#### radio.isNrSupported(deprecated)

isNrSupported(slotId: number): boolean

判断当前设备是否支持NR(New Radio)。

从 API version 8开始支持，从API version 9开始废弃。建议使用[isNRSupported](#ZH-CN_TOPIC_0000002529285483__radioisnrsupported9-1)替代。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明boolean

- true：支持。

- false：不支持。

**示例：**

```ets
let slotId: number = 0;
let result: boolean = radio.isNrSupported(slotId);
console.log("Result: "+ result);
```

#### radio.isNRSupported9+

isNRSupported(): boolean

判断当前设备是否支持NR(New Radio)。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

类型说明boolean

- true：支持。

- false：不支持。

**示例：**

```ets
let result: boolean = radio.isNRSupported();
console.log("Result: "+ result);
```

#### radio.isNRSupported9+

isNRSupported(slotId: number): boolean

判断当前设备是否支持NR(New Radio)。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明boolean

- true：支持。

- false：不支持。

**示例：**

```ets
let slotId: number = 0;
let result: boolean = radio.isNRSupported(slotId);
console.log("Result: "+ result);
```

#### radio.isRadioOn7+

isRadioOn(callback: AsyncCallback<boolean>): void

判断主卡的Radio是否打开。使用callback异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是

回调函数。返回主卡的Radio状态。

- true：Radio打开。

- false：Radio关闭。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

radio.isRadioOn((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isRadioOn failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.log(`isRadioOn success, callback: data->${JSON.stringify(data)}`);
});
```

#### radio.isRadioOn7+

isRadioOn(slotId: number, callback: AsyncCallback<boolean>): void

判断指定卡槽位的Radio是否打开。使用callback异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<boolean>是

回调函数。返回指定卡槽的Radio状态。

- true：Radio打开。

- false：Radio关闭。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.isRadioOn(slotId, (err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isRadioOn failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.log(`isRadioOn success, callback: data->${JSON.stringify(data)}`);
});
```

#### radio.isRadioOn7+

isRadioOn(slotId?: number): Promise<boolean>

判断Radio是否打开。使用Promise异步回调。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber否

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

如果不指定slotId，默认判断主卡Radio是否打开

**返回值：**

类型说明Promise<boolean>

以Promise形式返回判断Radio是否打开的结果。

- true：Radio打开。

- false：Radio关闭。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.isRadioOn(slotId).then((data: boolean) => {
    console.log(`isRadioOn success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isRadioOn failed, promise: err->${JSON.stringify(err)}`);
});
```

#### radio.getOperatorName7+

getOperatorName(slotId: number, callback: AsyncCallback<string>): void

获取运营商名称。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

callbackAsyncCallback<string>是回调函数，返回运营商名称。例如：中国移动。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getOperatorName(slotId, (err: BusinessError, data: string) => {
    if (err) {
        console.error(`getOperatorName failed, callback: err->${JSON.stringify(err)}`);
        return;
    }
    console.log(`getOperatorName success, callback: data->${JSON.stringify(data)}`);
});
```

#### radio.getOperatorName7+

getOperatorName(slotId: number): Promise<string>

获取运营商名称。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明Promise<string>以Promise形式返回运营商名称。例如：中国移动。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getOperatorName(slotId).then((data: string) => {
    console.log(`getOperatorName success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getOperatorName failed, promise: err->${JSON.stringify(err)}`);
});
```

#### radio.getOperatorNameSync10+

getOperatorNameSync(slotId: number): string

获取运营商名称。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

参数名类型必填说明slotIdnumber是

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。

**返回值：**

类型说明string返回运营商名称。例如：中国移动。

**示例：**

```ets
let slotId: number = 0;
let operatorName: string = radio.getOperatorNameSync(slotId);
console.log(`operator name is:` + operatorName);
```

#### NetworkRadioTech11+

网络中packet service (PS) 和 circuit service (CS) 无线接入技术。

**系统能力**：SystemCapability.Telephony.CoreService

名称类型只读可选说明psRadioTech[RadioTechnology](#ZH-CN_TOPIC_0000002529285483__radiotechnology)否否PS无线接入技术。csRadioTech[RadioTechnology](#ZH-CN_TOPIC_0000002529285483__radiotechnology)否否CS无线接入技术。

#### RadioTechnology

无线接入技术。

**系统能力**：SystemCapability.Telephony.CoreService

名称值说明RADIO_TECHNOLOGY_UNKNOWN0未知无线接入技术(RAT)。RADIO_TECHNOLOGY_GSM1无线接入技术GSM(Global System For Mobile Communication)。RADIO_TECHNOLOGY_1XRTT2无线接入技术1XRTT(Single-Carrier Radio Transmission Technology)。RADIO_TECHNOLOGY_WCDMA3无线接入技术WCDMA(Wideband Code Division Multiple Access)。RADIO_TECHNOLOGY_HSPA4无线接入技术HSPA(High Speed Packet Access)。RADIO_TECHNOLOGY_HSPAP5无线接入技术HSPAP(High Speed packet access (HSPA+) )。RADIO_TECHNOLOGY_TD_SCDMA6无线接入技术TD_SCDMA(TimeDivision-Synchronous Code Division Multiple Access)。RADIO_TECHNOLOGY_EVDO7无线接入技术EVDO(Evolution Data Only)。RADIO_TECHNOLOGY_EHRPD8无线接入技术EHRPD(Evolved High Rate Package Data)。RADIO_TECHNOLOGY_LTE9无线接入技术LTE(Long Term Evolution)。RADIO_TECHNOLOGY_LTE_CA10无线接入技术LTE_CA(Long Term Evolution_Carrier Aggregation)。RADIO_TECHNOLOGY_IWLAN11无线接入技术IWLAN(Industrial Wireless LAN)。RADIO_TECHNOLOGY_NR12无线接入技术NR(New Radio)。

#### SignalInformation

网络信号强度信息对象。

**系统能力**：SystemCapability.Telephony.CoreService

名称类型只读可选说明signalType[NetworkType](#ZH-CN_TOPIC_0000002529285483__networktype)否否网络信号强度类型。signalLevelnumber否否网络信号强度等级。dBm9+number否否网络信号强度。

#### NetworkType

网络类型。

**系统能力**：SystemCapability.Telephony.CoreService

名称值说明NETWORK_TYPE_UNKNOWN0未知网络类型。NETWORK_TYPE_GSM1网络类型为GSM(Global System For Mobile Communication)。NETWORK_TYPE_CDMA2网络类型为CDMA(Code Division Multiple Access)。NETWORK_TYPE_WCDMA3网络类型为WCDMA(Wideband Code Division Multiple Access)。NETWORK_TYPE_TDSCDMA4网络类型为TDSCDMA(TimeDivision-Synchronous Code Division Multiple Access)。NETWORK_TYPE_LTE5网络类型为LTE(Long Term Evolution)。NETWORK_TYPE_NR6网络类型为NR(New Radio)。

#### NetworkState

网络注册状态。

**系统能力**：SystemCapability.Telephony.CoreService

名称类型只读可选说明longOperatorNamestring否否注册网络的长运营商名称。shortOperatorNamestring否否注册网络的短运营商名称。plmnNumericstring否否注册网络的PLMN码。isRoamingboolean否否是否处于漫游状态。regState[RegState](#ZH-CN_TOPIC_0000002529285483__regstate)否否设备的网络注册状态。cfgTech8+[RadioTechnology](#ZH-CN_TOPIC_0000002529285483__radiotechnology)否否设备的无线接入技术。nsaState[NsaState](#ZH-CN_TOPIC_0000002529285483__nsastate)否否设备的NSA网络注册状态。isCaActiveboolean否否CA的状态。isEmergencyboolean否否此设备是否只允许拨打紧急呼叫。

#### RegState

网络注册状态。

**系统能力**：SystemCapability.Telephony.CoreService

名称值说明REG_STATE_NO_SERVICE0设备不能使用任何服务，包括数据业务、短信、通话等。REG_STATE_IN_SERVICE1设备可以正常使用服务，包括数据业务、短信、通话等。REG_STATE_EMERGENCY_CALL_ONLY2设备只能使用紧急呼叫业务。REG_STATE_POWER_OFF3蜂窝无线电已关闭，modem下电，无法和网侧进行通信。

#### NsaState

非独立组网状态。

**系统能力**：SystemCapability.Telephony.CoreService

名称值说明NSA_STATE_NOT_SUPPORT1设备在不支持NSA的LTE小区下处于空闲状态或连接状态。NSA_STATE_NO_DETECT2在支持NSA但不支持NR覆盖检测的LTE小区下，设备处于空闲状态。NSA_STATE_CONNECTED_DETECT3设备在LTE小区下连接到LTE网络支持NSA和NR覆盖检测。NSA_STATE_IDLE_DETECT4支持NSA和NR覆盖检测的LTE小区下设备处于空闲状态。NSA_STATE_DUAL_CONNECTED5设备在支持NSA的LTE小区下连接到LTE + NR网络。NSA_STATE_SA_ATTACHED6设备在5GC附着时在NG-RAN小区下空闲或连接到NG-RAN小区。

#### NetworkSelectionMode

选网模式。

**系统能力**：SystemCapability.Telephony.CoreService

名称值说明NETWORK_SELECTION_UNKNOWN0未知选网模式。NETWORK_SELECTION_AUTOMATIC1自动选网模式。NETWORK_SELECTION_MANUAL2手动选网模式。

#### CellInformation8+

小区信息。

**系统能力**：SystemCapability.Telephony.CoreService

名称类型只读可选说明networkType[NetworkType](#ZH-CN_TOPIC_0000002529285483__networktype)否否获取服务单元的网络类型。signalInformation[SignalInformation](#ZH-CN_TOPIC_0000002529285483__signalinformation)否否信号信息。