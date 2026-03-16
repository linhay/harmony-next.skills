# @ohos.telephony.sms (短信服务)

短信服务提供了管理短信的一些基础能力，包括创建、发送短信，获取发送短信的默认SIM卡槽ID、检查当前设备是否具备短信发送和接收能力等。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { sms } from '@kit.TelephonyKit';
```

#### sms.createMessage

createMessage(pdu: Array<number>, specification: string, callback: AsyncCallback<ShortMessage>): void

根据协议数据单元(PDU)和指定的短信协议创建短信实例。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

参数名类型必填说明pduArray<number>是协议数据单元，从收到的信息中获取。specificationstring是

短信协议类型。

- 3gpp：表示GSM/UMTS/LTE SMS。

- 3gpp2：表示CDMA SMS。

callbackAsyncCallback<[ShortMessage](#ZH-CN_TOPIC_0000002497605492__shortmessage)>是获取短信实例的回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

const specification: string = '3gpp';
// 以数组的形式显示协议数据单元(PDU)，类型为number。
const pdu: Array<number> = [0x01, 0x00, 0x05, 0x81, 0x01, 0x80, 0xF6, 0x00, 0x00, 0x05, 0xE8, 0x32, 0x9B, 0xFD, 0x06];
sms.createMessage(pdu, specification, (err: BusinessError, data: sms.ShortMessage) => {
    console.log(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sms.createMessage

createMessage(pdu: Array<number>, specification: string): Promise<ShortMessage>

根据协议数据单元(PDU)和指定的短信协议创建短信实例。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

参数名类型必填说明pduArray<number>是协议数据单元，从收到的信息中获取。specificationstring是

短信协议类型。

- 3gpp：表示GSM/UMTS/LTE SMS。

- 3gpp2：表示CDMA SMS。

**返回值：**

类型说明Promise<[ShortMessage](#ZH-CN_TOPIC_0000002497605492__shortmessage)>以Promise形式返回创建的短信实例。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

const specification: string = '3gpp';
// 以数组的形式显示协议数据单元(PDU)，类型为number。
const pdu: Array<number> = [0x01, 0x00, 0x05, 0x81, 0x01, 0x80, 0xF6, 0x00, 0x00, 0x05, 0xE8, 0x32, 0x9B, 0xFD, 0x06];
sms.createMessage(pdu, specification).then((data: sms.ShortMessage) => {
    console.log(`createMessage success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`createMessage failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sms.sendMessage(deprecated)

sendMessage(options: SendMessageOptions): void

发送短信。

从 API version 6开始支持，从API version 10开始废弃。建议使用[sendShortMessage](#ZH-CN_TOPIC_0000002497605492__smssendshortmessage10)替代。

**需要权限**：ohos.permission.SEND_MESSAGES（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

参数名类型必填说明options[SendMessageOptions](#ZH-CN_TOPIC_0000002497605492__sendmessageoptions)是发送短信的参数和回调，参考[SendMessageOptions](#ZH-CN_TOPIC_0000002497605492__sendmessageoptions)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { sms } from '@kit.TelephonyKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let sendCallback: AsyncCallback<sms.ISendShortMessageCallback> = (err: BusinessError, data: sms.ISendShortMessageCallback) => {
    console.log(`sendCallback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
};
let deliveryCallback: AsyncCallback<sms.IDeliveryShortMessageCallback> = (err: BusinessError, data: sms.IDeliveryShortMessageCallback) => {
    console.log(`deliveryCallback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
};
let options: sms.SendMessageOptions = {
    slotId: 0,
    content: '短信内容',
    destinationHost: '+861xxxxxxxxxx',
    serviceCenter: '+861xxxxxxxxxx',
    destinationPort: 1000,
    sendCallback: sendCallback,
    deliveryCallback: deliveryCallback
};
sms.sendMessage(options);
```

#### sms.sendShortMessage10+

sendShortMessage(options: SendMessageOptions, callback: AsyncCallback<void>): void

发送短信。使用callback异步回调。

**需要权限**：ohos.permission.SEND_MESSAGES（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

参数名类型必填说明options[SendMessageOptions](#ZH-CN_TOPIC_0000002497605492__sendmessageoptions)是发送短信的参数和回调，参考[SendMessageOptions](#ZH-CN_TOPIC_0000002497605492__sendmessageoptions)。callbackAsyncCallback<void>是发送短信的回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { sms } from '@kit.TelephonyKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let sendCallback: AsyncCallback<sms.ISendShortMessageCallback> = (err: BusinessError, data: sms.ISendShortMessageCallback) => {
    console.log(`sendCallback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
};
let deliveryCallback: AsyncCallback<sms.IDeliveryShortMessageCallback> = (err: BusinessError, data: sms.IDeliveryShortMessageCallback) => {
    console.log(`deliveryCallback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
};
let options: sms.SendMessageOptions = {
    slotId: 0,
    content: '短信内容',
    destinationHost: '+861xxxxxxxxxx',
    serviceCenter: '+861xxxxxxxxxx',
    destinationPort: 1000,
    sendCallback: sendCallback,
    deliveryCallback: deliveryCallback
};
sms.sendShortMessage(options, (err: BusinessError) => {
    console.log(`callback: err->${JSON.stringify(err)}`);
});
```

#### sms.sendShortMessage10+

sendShortMessage(options: SendMessageOptions): Promise<void>

发送短信。使用Promise异步回调。

**需要权限**：ohos.permission.SEND_MESSAGES（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

参数名类型必填说明options[SendMessageOptions](#ZH-CN_TOPIC_0000002497605492__sendmessageoptions)是发送短信的参数和回调，参考[SendMessageOptions](#ZH-CN_TOPIC_0000002497605492__sendmessageoptions)。

**返回值：**

类型说明Promise<void>以Promise形式返回发送短信的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300999Unknown error code.

**示例：**

```ets
import { sms } from '@kit.TelephonyKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let sendCallback: AsyncCallback<sms.ISendShortMessageCallback> = (err: BusinessError, data: sms.ISendShortMessageCallback) => {
    console.log(`sendCallback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
};
let deliveryCallback: AsyncCallback<sms.IDeliveryShortMessageCallback> = (err: BusinessError, data: sms.IDeliveryShortMessageCallback) => {
    console.log(`deliveryCallback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
};
let options: sms.SendMessageOptions = {
    slotId: 0,
    content: '短信内容',
    destinationHost: '+861xxxxxxxxxx',
    serviceCenter: '+861xxxxxxxxxx',
    destinationPort: 1000,
    sendCallback: sendCallback,
    deliveryCallback: deliveryCallback
};
let promise = sms.sendShortMessage(options);
promise.then(() => {
    console.log(`sendShortMessage success`);
}).catch((err: BusinessError) => {
    console.error(`sendShortMessage failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sms.getDefaultSmsSlotId7+

getDefaultSmsSlotId(callback: AsyncCallback<number>): void

获取发送短信的默认SIM卡槽ID。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是

获取发送短信的默认SIM卡槽ID的回调函数。

- 0：卡槽1。

- 1：卡槽2。

**示例：**

```ets
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSlotId((err: BusinessError, data: number) => {
    console.log(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sms.getDefaultSmsSlotId7+

getDefaultSmsSlotId(): Promise<number>

获取发送短信的默认SIM卡槽ID。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**返回值：**

类型说明Promise<number>

以Promise形式返回发送短信的默认SIM卡：

- 0：卡槽1。

- 1：卡槽2。

**示例：**

```ets
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSlotId().then((data: number) => {
    console.log(`getDefaultSmsSlotId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultSmsSlotId failed, promise: err->${JSON.stringify(err)}`);
});
```

#### sms.hasSmsCapability7+

hasSmsCapability(): boolean

检查当前设备是否具备短信发送和接收能力，该方法是同步方法。

**系统能力**：SystemCapability.Telephony.SmsMms

**返回值：**

类型说明boolean

- true：设备具备短信发送和接收能力。

- false：设备不具备短信发送和接收能力。

```ets
import { sms } from '@kit.TelephonyKit';

let result = sms.hasSmsCapability();
console.log(`hasSmsCapability: ${JSON.stringify(result)}`);
```

#### sms.getDefaultSmsSimId10+

getDefaultSmsSimId(callback: AsyncCallback<number>): void

获取发送短信的默认SIM卡ID。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

参数名类型必填说明callbackAsyncCallback<number>是

获取默认短信SIM的SIM ID的回调函数。

与SIM卡绑定，从1开始递增。

无卡时返回值为-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300004Do not have sim card.8300999Unknown error code.8301001SIM card is not activated.

**示例：**

```ets
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSimId((err: BusinessError, data: number) => {
    console.log(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
});
```

#### sms.getDefaultSmsSimId10+

getDefaultSmsSimId(): Promise<number>

获取发送短信的默认SIM卡ID。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**返回值：**

类型说明Promise<number>

以Promise形式返回发送短信的默认SIM卡ID：

与SIM卡绑定，从1开始递增。

无卡时返回值为-1。

**错误码：**

以下错误码的详细介绍请参见[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息8300001Invalid parameter value.8300002Operation failed. Cannot connect to service.8300003System internal error.8300004Do not have sim card.8300999Unknown error code.8301001SIM card is not activated.

**示例：**

```ets
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let promise = sms.getDefaultSmsSimId();
promise.then((data: number) => {
    console.log(`getDefaultSmsSimId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultSmsSimId failed, promise: err->${JSON.stringify(err)}`);
});
```

#### ShortMessage

短信实例。

**系统能力**：SystemCapability.Telephony.SmsMms

名称类型只读可选说明hasReplyPathboolean否否

收到的短信是否包含“TP-Reply-Path”，默认为false。

-true：是

-false：否

“TP-Reply-Path”：设备根据发送SMS消息的短消息中心进行回复。

isReplaceMessageboolean否否

收到的短信是否为“替换短信”，默认为false。

-true：是

-false：否

“替换短信”有关详细信息，参见 [“3GPP TS 23.040 9.2.3.9”](https://www.3gpp.org/ftp/specs/archive/23_series/23.040)。

isSmsStatusReportMessageboolean否否

当前消息是否为“短信状态报告”，默认为false。

-true：是

-false：否

“短信状态报告”是一种特定格式的短信，被用来从Service Center到Mobile Station传送状态报告。

messageClass[ShortMessageClass](#ZH-CN_TOPIC_0000002497605492__shortmessageclass)否否短信类型。pduArray<number>否否SMS消息中的协议数据单元 (PDU)。protocolIdnumber否否发送短信时使用的协议标识。scAddressstring否否短消息服务中心(SMSC)地址。scTimestampnumber否否SMSC时间戳。statusnumber否否SMS-STATUS-REPORT消息中的短信状态指示短信服务中心(SMSC)发送的短信状态。visibleMessageBodystring否否短信正文。visibleRawAddressstring否否发送者地址。

#### ShortMessageClass

短信类型。

**系统能力**：SystemCapability.Telephony.SmsMms

名称值说明UNKNOWN0未知类型。INSTANT_MESSAGE1即时消息，收到后立即显示。OPTIONAL_MESSAGE2存储在设备或SIM卡上的短信。SIM_MESSAGE3包含SIM卡信息的短信，需要存储在SIM卡中。FORWARD_MESSAGE4要转发到另一台设备的短信。

#### SendMessageOptions

发送短信的参数和回调。根据SendMessageOptions中的可选参数content的值判断短信类型。

**系统能力**：SystemCapability.Telephony.SmsMms

名称类型只读可选说明slotIdnumber否否

用于发送短信的SIM卡槽ID：

- 0：卡槽1。

- 1：卡槽2。

destinationHoststring否否短信的发送地址。contentstring | Array<number>否否如果内容是字符串，则这是一条文本短信。如果内容是字节数组，则这是一条数据短信。serviceCenterstring否是短信中心地址。默认使用SIM卡中的短信中心地址。destinationPortnumber否是如果发送数据消息，destinationPort 是必需的。否则是可选的。sendCallbackAsyncCallback<[ISendShortMessageCallback](#ZH-CN_TOPIC_0000002497605492__isendshortmessagecallback)>否是短信发送结果回调，返回短信发送的结果，参考[ISendShortMessageCallback](#ZH-CN_TOPIC_0000002497605492__isendshortmessagecallback)。发送数据短信时，此项必填。deliveryCallbackAsyncCallback<[IDeliveryShortMessageCallback](#ZH-CN_TOPIC_0000002497605492__ideliveryshortmessagecallback)>否是短信送达结果回调，返回短信递送报告，参考[IDeliveryShortMessageCallback](#ZH-CN_TOPIC_0000002497605492__ideliveryshortmessagecallback)。发送数据短信时，此项必填。

#### ISendShortMessageCallback

回调实例。返回短信发送结果、存储已发送短信的URI和是否为长短信的最后一部分。

**系统能力**：SystemCapability.Telephony.SmsMms

名称类型只读可选说明isLastPartboolean否否

指定这是否是长短信的最后一部分。默认为false。

-true：是

-false：否

result[SendSmsResult](#ZH-CN_TOPIC_0000002497605492__sendsmsresult)否否短信发送结果。urlstring否否存储发送短信的URI。

#### IDeliveryShortMessageCallback

回调实例，返回短信送达报告。

**系统能力**：SystemCapability.Telephony.SmsMms

名称类型只读可选说明pduArray<number>否否短信送达报告。

#### SendSmsResult

短信发送结果。

**系统能力**：SystemCapability.Telephony.SmsMms

名称值说明SEND_SMS_SUCCESS0发送短信成功。SEND_SMS_FAILURE_UNKNOWN1发送短信失败，原因未知。SEND_SMS_FAILURE_RADIO_OFF2发送短信失败，原因为调制解调器关机。SEND_SMS_FAILURE_SERVICE_UNAVAILABLE3发送短信失败，原因为网络不可用、不支持发送或接收短信。