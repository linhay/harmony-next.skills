# advertising（星闪广播能力）

本模块提供了发送星闪广播的相关功能，包括启动广播、停止广播、订阅广播状态等。

**起始版本：**5.0.1(13)

#### 导入模块

```ets
import { advertising } from '@kit.NearLinkKit';
```

#### AdvertisingParams

表示发送广播携带的参数。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

advertisingSettings

[AdvertisingSettings](#section1525727766)

否

否

广播配置参数。

advertisingData

[AdvertisingData](#section1235325161112)

否

否

广播数据包。

#### AdvertisingSettings

表示广播配置参数。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

interval

number

否

是

广播间隔配置参数。单位slot，范围160-16777215，默认值为5000。1个slot对应的时间长度是0.125ms，例如：5000*0.125=625ms。

power

[TxPowerMode](#section185441313151716)

否

是

广播发射功率配置参数。如果不配置，则默认值为ADV_TX_POWER_LOW。

isConnectable

boolean

否

是

true: 表示可连接的广播。false：表示不可连接的广播。默认值为true。

#### AdvertisingData

表示广播数据包。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

serviceUuids

Array<string>

否

是

服务UUID列表。若未配置则默认不携带该字段。UUID格式参考[星闪标准服务UUID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-faq#section1263634155618)。

manufacturerData

Array<[ManufacturerData](#section1622511479139)>

否

是

厂商数据。若未配置则默认不携带该字段。

serviceData

Array<[ServiceData](#section15831210191613)>

否

是

服务数据。若未配置则默认不携带该字段。

includeDeviceName

boolean

否

是

指示广播数据中是否携带本机设备名。true：表示包含设备名称。false：表示不包含设备名称。默认值为false。

#### ManufacturerData

表示厂商数据。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

manufacturerId

number

否

否

厂商ID。取值范围(0, 65535]。

manufacturerData

ArrayBuffer

否

否

厂商数据。

#### ServiceData

表示服务相关数据。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

serviceUuid

string

否

否

表示服务的UUID。UUID格式参考[星闪标准服务UUID](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-faq#section1263634155618)。

serviceData

ArrayBuffer

否

否

表示服务数据。

#### AdvertisingStateChangeInfo

表示广播启停状态变化信息。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

类型

只读

可选

说明

advertisingId

number

否

否

表示广播ID。取值范围[0, 255]。

state

[AdvertisingState](#section757023015351)

否

否

表示当前广播状态。

#### TxPowerMode

表示广播发送模式，为枚举值。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

值

说明

ADV_TX_POWER_LOW

1

表示低功耗模式。

ADV_TX_POWER_MEDIUM

2

表示中等功耗模式。

ADV_TX_POWER_HIGH

3

表示高功耗模式。

#### AdvertisingState

表示广播状态，为枚举值。

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

名称

值

说明

STARTED

1

表示广播已启动。

STOPPED

2

表示广播已停止。

#### startAdvertising

startAdvertising(advertisingParams: AdvertisingParams): Promise<number>

发送星闪广播。使用Promise异步回调。

**需要权限：**ohos.permission.ACCESS_NEARLINK

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

advertisingParams

[AdvertisingParams](#section295015817218)

是

广播相关参数。

**返回值：**

类型

说明

Promise<number>

Promise对象，返回本次开启的广播ID。广播ID是随机分配的唯一标识值。

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

1009700003

Nearlink is off

1009700099

Operation failed

**示例：**

```ets
import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer[0] = 1;
manufactureValueBuffer[1] = 2;
manufactureValueBuffer[2] = 3;
manufactureValueBuffer[3] = 4;
let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer[0] = 4;
serviceValueBuffer[1] = 6;
serviceValueBuffer[2] = 7;
serviceValueBuffer[3] = 8;
console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
let setting: advertising.AdvertisingSettings = {
  interval:5000,
  power:advertising.TxPowerMode.ADV_TX_POWER_LOW
};
let manufactureDataUnit: advertising.ManufacturerData = {
  manufacturerId:4567,
  manufacturerData:manufactureValueBuffer.buffer
};
let serviceDataUnit: advertising.ServiceData = {
  serviceUuid:"37bea880-fc70-11ea-b720-000000001234",
  serviceData:serviceValueBuffer.buffer
};
let advData: advertising.AdvertisingData = {
  serviceUuids:["37bea880-fc70-11ea-b720-000000001234"],
  manufacturerData:[manufactureDataUnit],
  serviceData:[serviceDataUnit]
};
let advertisingParams: advertising.AdvertisingParams = {
  advertisingSettings: setting,
  advertisingData: advData
}
let advId = -1;
try {
  advertising.startAdvertising(advertisingParams).then((advertisingId:number) => {
    advId = advertisingId;
    console.info('advertising id:'+ JSON.stringify(advId));
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### stopAdvertising

stopAdvertising(advertisingId: number): Promise<void>

停止发送星闪广播。使用Promise异步回调。

**需要权限：**ohos.permission.ACCESS_NEARLINK

**系统能力：**SystemCapability.Communication.NearLink.Core

**起始版本：**5.0.1(13)

**参数：**

参数名

类型

必填

说明

advertisingId

number

是

广播ID，开启广播时获取。取值范围[0, 255]。

**返回值：**

类型

说明

Promise<void>

Promise对象，无返回值。

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

1009700003

Nearlink is off

1009700099

Operation failed

**示例：**

```ets
import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let advId: number = 1; // advId在开启广播时获取，参考startAdvertising接口返回值
  advertising.stopAdvertising(advId).then(() => {
    console.info("stop advertising success");
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### on( 'advertisingStateChange')

on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void

订阅星闪广播状态变化事件。

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

固定填写"advertisingStateChange"字符串，表示星闪广播状态变化事件。

callback

Callback<[AdvertisingStateChangeInfo](#section188870256234)>

是

表示广播状态变化回调函数。

**错误码：**

错误码ID

错误信息

201

Permission denied

401

Invalid parameter

801

Capability not supported

**示例：**

```ets
import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let onReceiveEvent:(data: advertising.AdvertisingStateChangeInfo) => void = (data: advertising.AdvertisingStateChangeInfo) => {
  console.info('advertisingId:'+ data.advertisingId);
  console.info('advertisingState:'+ data.state);
}
try {
  advertising.on('advertisingStateChange', onReceiveEvent);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### off( 'advertisingStateChange')

off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void

取消订阅星闪广播状态变化事件。

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

固定填写"advertisingStateChange"字符串，表示星闪广播状态变化事件。

callback

Callback<[AdvertisingStateChangeInfo](#section188870256234)>

否

可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。

**错误码：**

错误码ID

错误信息

201

Permission denied

401

Invalid parameter

801

Capability not supported

**示例：**

```ets
import { advertising } from '@kit.NearLinkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  advertising.off('advertisingStateChang*e*');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```