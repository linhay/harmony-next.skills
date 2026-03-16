# manager（星闪开关能力）

本模块提供了管理星闪基础能力，包括获取设备信息、订阅状态变化事件等。

**起始版本：**5.0.1(13)

#### 导入模块

```ets
import { manager } from '@kit.NearLinkKit';
```

#### PairingState

type PairingState = [constant.PairingState](constant（星闪公共常量定义）.md#section1976472485918)

表示和远端设备的配对状态，为枚举值。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

类型

说明

[constant.PairingState](constant（星闪公共常量定义）.md#section1976472485918)

和远端设备的配对状态。

#### ConnectionState

type ConnectionState = [constant.ConnectionState](constant（星闪公共常量定义）.md#section14942121015417)

表示和远端设备的连接状态，为枚举值。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

类型

说明

[constant.ConnectionState](constant（星闪公共常量定义）.md#section14942121015417)

和远端设备的连接状态。

#### AcbState

type AcbState = [constant.AcbState](constant（星闪公共常量定义）.md#section144650555553)

表示和远端设备的逻辑链路连接状态，为枚举值。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.1.0(18)

类型

说明

[constant.AcbState](constant（星闪公共常量定义）.md#section144650555553)

和远端设备的逻辑链路连接状态。

#### getState

getState(): NearlinkState

查询星闪开关状态。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

**返回值：**

类型

说明

[NearlinkState](#section454667203316)

表示星闪开关状态。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

801

Capability not supported

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let state: manager.NearlinkState = manager.getState();
  console.info('state:' + JSON.stringify(state));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### getLocalName

getLocalName(): string

查询本机星闪名称。

**需要权限：**ohos.permission.ACCESS_NEARLINK

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

**返回值：**

类型

说明

string

表示星闪设备本地名称。最大长度为30。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied

801

Capability not supported

1009700003

Nearlink is off

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let name: string = manager.getLocalName();
  console.info('state:' + JSON.stringify(name));
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### getPairedDevices

getPairedDevices(): Array<string>

获取与当前设备配对的设备列表。

**需要权限：**ohos.permission.ACCESS_NEARLINK

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**6.0.1(21)

**返回值：**

类型

说明

Array<string>

配对设备地址的列表。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied

801

Capability not supported

1009700003

Nearlink is off

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let pairedDevices: Array<string> = manager.getPairedDevices();
  if (pairedDevices.length > 0) {
        console.info('getPairedDevices return: ' + JSON.stringify(pairedDevices));
    } else {
        console.info('No Paired Devices found.');
    }
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### on( 'stateChange')

on(type: 'stateChange', callback: Callback<NearlinkState>): void

订阅星闪开关状态变化事件。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"stateChange"字符串，表示星闪开关状态变化事件。

callback

Callback<[NearlinkState](#section454667203316)>

是

表示开关状态变化回调函数的入参。回调函数由用户创建通过该接口注册。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid parameter

801

Capability not supported

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<manager.NearlinkState> = (data: manager.NearlinkState) => {
  if (data === manager.NearlinkState.STATE_TURNING_ON) {
    console.info('nearlink STATE_TURNING_ON');
  } else if (data === manager.NearlinkState.STATE_ON) {
    console.info('nearlink STATE_ON');
  } else if (data === manager.NearlinkState.STATE_TURNING_OFF) {
    console.info('nearlink STATE_TURNING_OFF');
  } else if (data === manager.NearlinkState.STATE_OFF) {
    console.info('nearlink STATE_OFF');
  }
};
try {
  manager.on('stateChange', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### off( 'stateChange')

off(type: 'stateChange', callback?: Callback<NearlinkState>): void

取消订阅星闪开关状态变化事件。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"stateChange"字符串，表示星闪开关状态变化事件。

callback

Callback<[NearlinkState](#section454667203316)>

否

可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

401

Invalid parameter

801

Capability not supported

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('stateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### on( 'pairingStateChange')

on(type: 'pairingStateChange', callback: Callback<PairingStateParam>): void

订阅配对请求事件。回调函数携带远端设备的随机地址。

**需要权限：**ohos.permission.ACCESS_NEARLINK

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"pairingStateChange"字符串，表示配对请求事件。

callback

Callback<[PairingStateParam](#section185441313151716)>

是

表示配对状态变化回调函数的入参。回调函数由用户创建通过该接口注册。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied

401

Invalid parameter

801

Capability not supported

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onPairingStateEvent:(data: manager.PairingStateParam) => void = (data: manager.PairingStateParam) => {
  console.info('onPairStateChange addr: '+ data.address + 'state:' + data.state);
}
try {
  manager.on('pairingStateChange', onPairingStateEvent);
} catch (err) {
  console.info('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### off( 'pairingStateChange')

off(type: 'pairingStateChange', callback?: Callback<PairingStateParam>): void

取消订阅配对请求事件。

**需要权限：**ohos.permission.ACCESS_NEARLINK

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写'pairingStateChange'字符串，表示配对请求事件。

callback

Callback<[PairingStateParam](#section185441313151716)>

否

可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied

401

Invalid parameter

801

Capability not supported

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('pairingStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### on( 'connectionStateChange')

on(type: 'connectionStateChange', callback: Callback<ConnectionStateParam>): void

订阅连接状态变化事件。回调函数携带远端设备的随机地址。

**需要权限：**ohos.permission.ACCESS_NEARLINK

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"connectionStateChange"字符串，表示连接状态变化事件。

callback

Callback<[ConnectionStateParam](#section477651052718)>

是

表示连接状态变化回调函数的入参。回调函数由用户创建通过该接口注册。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied

401

Invalid parameter

801

Capability not supported

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<manager.ConnectionStateParam> = (data: manager.ConnectionStateParam) => {
  console.info('data:' + JSON.stringify(data));
};
try {
  manager.on('connectionStateChange', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### off( 'connectionStateChange')

off(type: 'connectionStateChange', callback?: Callback<ConnectionStateParam>): void

取消订阅连接状态变化事件。

**需要权限：**ohos.permission.ACCESS_NEARLINK

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"connectionStateChange"字符串，表示连接状态变化事件。

callback

Callback<[ConnectionStateParam](#section477651052718)>

否

可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied

401

Invalid parameter

801

Capability not supported

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('connectionStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### on('acbStateChange')

on(type: 'acbStateChange', callback: Callback<[AcbStateParam](#section58892382115)>): void

订阅逻辑链路连接状态变化事件。回调函数携带远端设备的随机地址。

**需要权限：**ohos.permission.ACCESS_NEARLINK

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.1.0(18)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"acbStateChange"字符串，表示逻辑链路连接状态变化事件。

callback

Callback<[AcbStateParam](#section58892382115)>

是

表示逻辑链路连接状态变化回调函数的入参。回调函数由用户创建，通过该接口注册。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

801

Capability not supported

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { Callback } from '@kit.BasicServicesKit';

let callback: Callback<manager.AcbStateParam> = (data: manager.AcbStateParam) => {
  console.info('data:' + JSON.stringify(data));
};
try {
  manager.on('acbStateChange', callback);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### off( 'acbStateChange')

off(type: 'acbStateChange', callback?: Callback<[AcbStateParam](#section58892382115)>): void

取消订阅逻辑链路连接状态变化事件。

**需要权限：**ohos.permission.ACCESS_NEARLINK

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.1.0(18)

**参数：**

参数名

类型

必填

说明

type

string

是

固定填写"acbStateChange"字符串，表示逻辑链路连接状态变化事件。

callback

Callback<[AcbStateParam](#section58892382115)>

否

可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](../../errors/ArkTS API错误码.md)。

错误码ID

错误信息

201

Permission denied

401

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

801

Capability not supported

1009700099

Operation failed

**示例：**

```ets
import { manager } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  manager.off('acbStateChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### PairingStateParam

订阅的配对状态变化结果。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

address

string

否

否

设备地址，表示和该设备的配对状态发生变化。地址格式参考："11:22:33:AA:BB:FF"。

preState

[PairingState](constant（星闪公共常量定义）.md#section1976472485918)

否

否

本次上报之前的配对状态。

state

[PairingState](constant（星闪公共常量定义）.md#section1976472485918)

否

否

当前配对状态。

reason

[PairingReason](#section985712528369)

否

否

原因值。

#### PairingRequestParam

表示订阅的配对请求事件上报结果。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

address

string

否

否

设备地址，表示收到该设备的配对请求上报。地址格式参考："11:22:33:AA:BB:FF"。

passkey

string

否

否

表示配对交互的配对码，显示给用户确认。长度固定为6，字符串内容为数字。

pairingType

[PairingType](#section1080014428381)

否

否

表示配对类型。

#### ConnectionStateParam

订阅的连接状态变化事件上报结果。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

address

string

否

否

设备地址，表示和该设备的连接状态发生变化。地址格式参考："11:22:33:AA:BB:FF"。

preState

[ConnectionState](constant（星闪公共常量定义）.md#section14942121015417)

否

否

本次上报之前的连接状态。

state

[ConnectionState](constant（星闪公共常量定义）.md#section14942121015417)

否

否

当前连接状态。

connectionReason

[ConnectionReason](#section189609817294)

否

否

原因值。

#### NearlinkState

星闪的开关状态，为枚举值。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

值

说明

STATE_TURNING_ON

0

表示星闪正在打开。

STATE_ON

1

表示星闪已打开。

STATE_TURNING_OFF

2

表示星闪正在关闭。

STATE_OFF

3

表示星闪已关闭。

#### PairingReason

表示星闪配对状态变化结果的原因值，为枚举值。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

值

说明

PAIRING_REASON_SUCCESS

0

表示配对成功。

PAIRING_REASON_FAILURE

1

表示配对失败。

PAIRING_REASON_PROFILE_UNSUPPORTED

2

表示对端设备不支持服务导致配对失败。

**起始版本：**5.1.0(18)

PAIRING_REASON_EXCEED_ACB_MAX

3

表示连接设备数已达上限导致配对失败。

**起始版本：**5.1.0(18)

PAIRING_REASON_REMOTE_CANCELED

4

表示对端设备取消配对导致配对失败。

**起始版本：**5.1.0(18)

PAIRING_REASON_LOCAL_CANCELED

5

表示本端设备取消配对导致配对失败。

**起始版本**：5.1.0(18)

#### PairingType

星闪配对类型，为枚举值。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

值

说明

NO_PASSKEY_CONFIRMATION

0

表示不需要passkey的配对方式，用户无需检查配对码。

PAIRING_TYPE_PASSCODE

1

表示通行码鉴权方式，用户需在一端设备输入另一端设备显示的配对码。

**起始版本：**5.1.0(18)

PAIRING_TYPE_NUMBER_COMPARE

2

表示数字比较鉴权方式，用户需在两端设备确认配对码一致。

**起始版本：**5.1.0(18)

#### ConnectionReason

星闪连接状态变化结果的原因值。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

值

说明

CONNECTION_SUCCESS

0

表示连接成功。

CONNECTION_FAILURE

1

表示连接失败。

#### AcbStateParam

订阅的逻辑链路连接状态变化事件上报结果。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.1.0(18)

名称

类型

只读

可选

说明

address

string

否

否

设备地址，表示和该设备的逻辑链路连接状态发生变化。地址格式参考："11:22:33:AA:BB:FF"。

state

[AcbState](constant（星闪公共常量定义）.md#section144650555553)

否

否

当前逻辑链路连接状态。