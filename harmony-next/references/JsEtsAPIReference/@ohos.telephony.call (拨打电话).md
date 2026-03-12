# @ohos.telephony.call (拨打电话)

该模块提供呼叫管理功能，包括拨打电话、跳转到拨号界面、获取通话状态、格式化电话号码等。

如需订阅通话状态请使用[observer.on('callStateChange')](@ohos.telephony.observer (observer).md#ZH-CN_TOPIC_0000002497445512__observeroncallstatechange)。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { call } from '@kit.TelephonyKit';
```

#### call.dial(deprecated)

dial(phoneNumber: string, callback: AsyncCallback<boolean>): void

拨打电话。使用callback异步回调。

从API version 6 开始支持，从API version 9 开始废弃。替代接口能力仅对系统应用开放。

**需要权限**：ohos.permission.PLACE_CALL（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。callbackAsyncCallback<boolean>是回调函数，返回true为成功，false为失败。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

call.dial("138xxxxxxxx", (err: BusinessError, data: boolean) => {
    console.log(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### call.dial(deprecated)

dial(phoneNumber: string, options: DialOptions, callback: AsyncCallback<boolean>): void

拨打电话，可设置通话参数。使用callback异步回调。

从API version 6 开始支持，从API version 9 开始废弃。替代接口能力仅对系统应用开放。

**需要权限**：ohos.permission.PLACE_CALL（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。options[DialOptions](#ZH-CN_TOPIC_0000002529285481__dialoptions)是通话参数，选择为语音通话还是视频通话。callbackAsyncCallback<boolean>是回调函数，返回true为成功，false为失败。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let dialOptions: call.DialOptions = {
    extras: false
}
call.dial("138xxxxxxxx", dialOptions, (err: BusinessError, data: boolean) => {
    console.log(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### call.dial(deprecated)

dial(phoneNumber: string, options?: DialOptions): Promise<boolean>

拨打电话，可设置通话参数。使用Promise异步回调。

从API version 6 开始支持，从API version 9 开始废弃。替代接口能力仅对系统应用开放。

**需要权限**：ohos.permission.PLACE_CALL（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。options[DialOptions](#ZH-CN_TOPIC_0000002529285481__dialoptions)否通话参数，选择为语音通话还是视频通话。

**返回值：**

类型说明Promise<boolean>以Promise形式返回拨打电话的结果，返回true为成功，false为失败。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let dialOptions: call.DialOptions = {
    extras: false
}
call.dial("138xxxxxxxx", dialOptions).then((data: boolean) => {
    console.log(`dial success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`dial fail, promise: err->${JSON.stringify(err)}`);
});
```

#### call.makeCall7+

makeCall(phoneNumber: string, callback: AsyncCallback<void>): void

跳转到拨号界面，并显示待拨出的号码。使用callback异步回调。只支持在UIAbility中调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。callbackAsyncCallback<void>是以callback形式异步返回跳转拨号界面的结果。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
// 从API15开始支持tel格式电话号码，如："tel:13xxxx"
call.makeCall("138xxxxxxxx", (err: BusinessError) => {
    if (err) {
        console.error(`makeCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.log(`makeCall success`);
    }
});
```

#### call.makeCall7+

makeCall(phoneNumber: string): Promise<void>

跳转到拨号界面，并显示待拨出的号码。使用Promise异步回调。只支持在UIAbility中调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。

**返回值：**

类型说明Promise<void>以Promise形式异步返回拨号的结果。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
// 从API15开始支持tel格式电话号码，如："tel:13xxxx"
call.makeCall("138xxxxxxxx").then(() => {
    console.log(`makeCall success`);
}).catch((err: BusinessError) => {
    console.error(`makeCall fail, promise: err->${JSON.stringify(err)}`);
});
```

#### call.makeCall12+

makeCall(context: Context, phoneNumber: string): Promise<void>

跳转到拨号界面，并显示待拨出的号码。使用Promise异步回调。后台调用需要申请ohos.permission.START_ABILITIES_FROM_BACKGROUND权限。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Applications.Contacts

**参数：**

参数名类型必填说明contextContext是应用上下文Context。phoneNumberstring是电话号码。

**返回值：**

类型说明Promise<void>以Promise形式异步返回拨号的结果。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300002Operation failed. Cannot connect to service.8300003System internal error.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { BusinessError } from '@kit.BasicServicesKit';
// 获取context
let context = this.getUIContext().getHostContext() as Context;
// 从API15开始支持tel格式电话号码，如："tel:13xxxx"
call.makeCall(context, "138xxxxxxxx").then(() => {
    console.log(`makeCall success`);
}).catch((err: BusinessError) => {
    console.error(`makeCall fail, promise: err->${JSON.stringify(err)}`);
});
```

#### call.hasCall

hasCall(callback: AsyncCallback<boolean>): void

判断是否存在通话。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是回调函数。返回true表示当前存在通话，false表示当前不存在通话。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

call.hasCall((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`hasCall fail, err->${JSON.stringify(err)}`);
    } else {
        console.log(`hasCall success, data->${JSON.stringify(data)}`);
    }
});
```

#### call.hasCall

hasCall(): Promise<boolean>

判断是否存在通话。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**返回值：**

类型说明Promise<boolean>以Promise形式异步返回判断是否存在通话。返回true表示当前存在通话，false表示当前不存在通话。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

call.hasCall().then(() => {
    console.log(`hasCall success`);
}).catch((err: BusinessError) => {
    console.error(`hasCall fail, promise: err->${JSON.stringify(err)}`);
});
```

#### call.hasCallSync10+

hasCallSync(): boolean

判断是否存在通话。

**系统能力**：SystemCapability.Telephony.CallManager

**返回值：**

类型说明boolean返回判断是否存在通话。返回true表示当前存在通话，false表示当前不存在通话。

**示例：**

```ets
let hasCall: boolean = call.hasCallSync();
console.log(`hasCallSync success, has call is ` + hasCall);
```

#### call.getCallState

getCallState(callback: AsyncCallback<CallState>): void

获取当前通话状态。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明callbackAsyncCallback<[CallState](#ZH-CN_TOPIC_0000002529285481__callstate)>是回调函数，异步返回获取到的通话状态。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

call.getCallState((err: BusinessError, data: call.CallState) => {
    if (err) {
        console.error(`getCallState fail, err->${JSON.stringify(err)}`);
    } else {
        console.log(`getCallState success, data->${JSON.stringify(data)}`);
    }
});
```

#### call.getCallState

getCallState(): Promise<CallState>

获取当前通话状态。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**返回值：**

类型说明Promise<[CallState](#ZH-CN_TOPIC_0000002529285481__callstate)>以Promise形式异步返回获取到的通话状态。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

call.getCallState().then((data: call.CallState) => {
    console.log(`getCallState success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getCallState fail, promise: err->${JSON.stringify(err)}`);
});
```

#### call.getCallStateSync10+

getCallStateSync(): CallState

获取当前通话状态。

**系统能力**：SystemCapability.Telephony.CallManager

**返回值：**

类型说明[CallState](#ZH-CN_TOPIC_0000002529285481__callstate)返回获取到的通话状态。

**示例：**

```ets
let callState: call.CallState = call.getCallStateSync();
console.log(`the call state is:` + callState);
```

#### call.hasVoiceCapability7+

hasVoiceCapability(): boolean

检查当前设备是否具备语音通话能力。

**系统能力**：SystemCapability.Telephony.CallManager

**返回值：**

类型说明boolean返回true表示设备具备语音通话能力，返回false表示设备不具备语音通话能力。

```ets
let result: boolean = call.hasVoiceCapability();
console.log(`hasVoiceCapability: ${JSON.stringify(result)}`);
```

#### call.isEmergencyPhoneNumber7+

isEmergencyPhoneNumber(phoneNumber: string, callback: AsyncCallback<boolean>): void

判断是否是紧急电话号码。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。callbackAsyncCallback<boolean>是回调函数。返回true表示是紧急电话号码，返回false表示不是紧急电话号码。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

call.isEmergencyPhoneNumber("138xxxxxxxx", (err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isEmergencyPhoneNumber fail, err->${JSON.stringify(err)}`);
    } else {
        console.log(`isEmergencyPhoneNumber success, data->${JSON.stringify(data)}`);
    }
});
```

#### call.isEmergencyPhoneNumber7+

isEmergencyPhoneNumber(phoneNumber: string, options: EmergencyNumberOptions, callback: AsyncCallback<boolean>): void

根据电话号码参数，判断是否是紧急电话号码。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。options[EmergencyNumberOptions](#ZH-CN_TOPIC_0000002529285481__emergencynumberoptions7)是电话号码参数。callbackAsyncCallback<boolean>是回调函数。返回true表示是紧急电话号码，返回false表示不是紧急电话号码。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let options: call.EmergencyNumberOptions = {slotId: 1}
call.isEmergencyPhoneNumber("112", options, (err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isEmergencyPhoneNumber fail, err->${JSON.stringify(err)}`);
    } else {
        console.log(`isEmergencyPhoneNumber success, data->${JSON.stringify(data)}`);
    }
});
```

#### call.isEmergencyPhoneNumber7+

isEmergencyPhoneNumber(phoneNumber: string, options?: EmergencyNumberOptions): Promise<boolean>

根据电话号码参数，判断是否是紧急电话号码。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。options[EmergencyNumberOptions](#ZH-CN_TOPIC_0000002529285481__emergencynumberoptions7)否电话号码参数。

**返回值：**

类型说明Promise<boolean>以Promise形式异步返回判断是否是紧急电话号码的结果。返回true表示是紧急电话号码，返回false表示不是紧急电话号码。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let options: call.EmergencyNumberOptions = {slotId: 1}
call.isEmergencyPhoneNumber("138xxxxxxxx", options).then((data: boolean) => {
    console.log(`isEmergencyPhoneNumber success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isEmergencyPhoneNumber fail, promise: err->${JSON.stringify(err)}`);
});
```

#### call.formatPhoneNumber7+

formatPhoneNumber(phoneNumber: string, callback: AsyncCallback<string>): void

格式化电话号码。使用callback异步回调。

电话号码格式化后为标准数字字串，例如：“138 xxxx xxxx”、“0755 xxxx xxxx”。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。callbackAsyncCallback<string>是回调函数，返回格式化电话号码的结果。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

call.formatPhoneNumber("138xxxxxxxx", (err: BusinessError, data: string) => {
    if (err) {
        console.error(`formatPhoneNumber fail, err->${JSON.stringify(err)}`);
    } else {
        console.log(`formatPhoneNumber success, data->${JSON.stringify(data)}`);
    }
});
```

#### call.formatPhoneNumber7+

formatPhoneNumber(phoneNumber: string, options: NumberFormatOptions, callback: AsyncCallback<string>): void

格式化电话号码，可设置格式化参数。使用callback异步回调。

电话号码格式化后为标准数字字串，例如：“138 xxxx xxxx”、“0755 xxxx xxxx”。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。options[NumberFormatOptions](#ZH-CN_TOPIC_0000002529285481__numberformatoptions7)是格式化参数，如国家码。callbackAsyncCallback<string>是回调函数，返回格式化电话号码的结果。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let options: call.NumberFormatOptions = {
    countryCode: "CN"
}
call.formatPhoneNumber("138xxxxxxxx", options, (err: BusinessError, data: string) => {
    if (err) {
        console.error(`formatPhoneNumber fail, err->${JSON.stringify(err)}`);
    } else {
        console.log(`formatPhoneNumber success, data->${JSON.stringify(data)}`);
    }
});
```

#### call.formatPhoneNumber7+

formatPhoneNumber(phoneNumber: string, options?: NumberFormatOptions): Promise<string>

格式化电话号码，可设置格式化参数。使用Promise异步回调。

电话号码格式化后为标准数字字串，例如：“138 xxxx xxxx”、“0755 xxxx xxxx”。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。options[NumberFormatOptions](#ZH-CN_TOPIC_0000002529285481__numberformatoptions7)否格式化参数，如国家码。

**返回值：**

类型说明Promise<string>以Promise形式异步返回格式化电话号码的结果。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let options: call.NumberFormatOptions = {
    countryCode: "CN"
}
call.formatPhoneNumber("138xxxxxxxx", options).then((data: string) => {
    console.log(`formatPhoneNumber success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`formatPhoneNumber fail, promise: err->${JSON.stringify(err)}`);
});
```

#### call.formatPhoneNumberToE1647+

formatPhoneNumberToE164(phoneNumber: string, countryCode: string, callback: AsyncCallback<string>): void

将电话号码格式化为E.164表示形式，使用callback异步回调。

待格式化的电话号码需要与传入的国家码相匹配，如中国电话号码需要传入国家码CN，否则格式化后的电话号码为null。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。countryCodestring是国家码，支持所有国家码，如：中国（CN）。callbackAsyncCallback<string>是回调函数，返回将电话号码格式化为E.164表示形式的结果。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

call.formatPhoneNumberToE164("138xxxxxxxx", "CN", (err: BusinessError, data: string) => {
    if (err) {
        console.error(`formatPhoneNumberToE164 fail, err->${JSON.stringify(err)}`);
    } else {
        console.log(`formatPhoneNumberToE164 success, data->${JSON.stringify(data)}`);
    }
});
```

#### call.formatPhoneNumberToE1647+

formatPhoneNumberToE164(phoneNumber: string, countryCode: string): Promise<string>

将电话号码格式化为E.164表示形式，使用Promise异步回调。

待格式化的电话号码需要与传入的国家码相匹配，如中国电话号码需要传入国家码CN，否则格式化后的电话号码为null。

支持所有国家码。

**系统能力**：SystemCapability.Telephony.CallManager

**参数：**

参数名类型必填说明phoneNumberstring是电话号码。countryCodestring是国家码，支持所有国家码，如：中国（CN）。

**返回值：**

类型说明Promise<string>以Promise形式异步返回将电话号码格式化为E.164表示形式的结果。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](电话子系统错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types;8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

call.formatPhoneNumberToE164("138xxxxxxxx", "CN").then((data: string) => {
    console.log(`formatPhoneNumberToE164 success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`formatPhoneNumberToE164 fail, promise: err->${JSON.stringify(err)}`);
});
```

#### DialOptions

拨打电话的可选参数。

**系统能力**：SystemCapability.Telephony.CallManager

名称类型只读可选说明extrasboolean否是

根据extras的值判断是否为视频通话，默认为语音通话。

- true：视频通话。

- false：语音通话。

#### CallState

通话状态码。

**系统能力**：SystemCapability.Telephony.CallManager

名称值说明CALL_STATE_UNKNOWN-1无效状态，当获取呼叫状态失败时返回。CALL_STATE_IDLE0表示没有正在进行的呼叫。CALL_STATE_RINGING1表示来电正在振铃或等待。CALL_STATE_OFFHOOK2表示至少有一个呼叫处于拨号、通话中或呼叫保持状态，并且没有新的来电振铃或等待。CALL_STATE_ANSWERED11+3表示来电已经接听。

#### TelCallState21+

通话状态码。

**系统能力**：SystemCapability.Telephony.CallManager

名称值说明TEL_CALL_STATE_UNKNOWN-1无效状态，当获取呼叫状态失败时返回。TEL_CALL_STATE_IDLE0表示没有正在进行的呼叫。TEL_CALL_STATE_RINGING1表示来电正在振铃或等待。TEL_CALL_STATE_OFFHOOK2表示至少有一个呼叫处于拨号，并且没有新的来电振铃或等待。TEL_CALL_STATE_ANSWERED3表示来电已经接听。TEL_CALL_STATE_CONNECTED4表示电话已经接通中或呼叫保持。

#### EmergencyNumberOptions7+

判断是否是紧急电话号码的可选参数。

**系统能力**：SystemCapability.Telephony.CallManager

名称类型只读可选说明slotIdnumber否是

卡槽ID：

- 卡槽1：0。

- 卡槽2：1。

#### NumberFormatOptions7+

格式化号码的可选参数。

**系统能力**：SystemCapability.Telephony.CallManager

名称类型只读可选说明countryCodestring否是国家码，支持所有国家的国家码，如：CN（中国）。默认为：CN。