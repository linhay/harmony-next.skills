# @ohos.bluetooth.connection (蓝牙connection模块)

connection模块提供了蓝牙设备的配对、连接及状态查询等能力。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { connection } from '@kit.ConnectivityKit';
```

#### ProfileConnectionState

type ProfileConnectionState = constant.ProfileConnectionState

蓝牙设备的Profile协议连接状态。Profile协议包括A2DP（Advanced Audio Distribution Profile）、HFP（Hands-Free Profile）和HID（Human Interface Device）等。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

类型说明[constant.ProfileConnectionState](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileconnectionstate)蓝牙设备的Profile协议连接状态。

#### ProfileId

type ProfileId = constant.ProfileId

枚举，蓝牙Profile协议。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

类型说明[constant.ProfileId](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileid)蓝牙Profile协议的枚举。

#### ProfileUuids12+

type ProfileUuids = constant.ProfileUuids

蓝牙Profile协议的UUID。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

类型说明[constant.ProfileUuids](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileuuids12)蓝牙Profile协议的UUID。

#### MajorClass

type MajorClass = constant.MajorClass

蓝牙设备的主要类型。蓝牙标准协议字段。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

类型说明[constant.MajorClass](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__majorclass)蓝牙设备的主要类型。

#### MajorMinorClass

type MajorMinorClass = constant.MajorMinorClass

蓝牙设备的子类型，在[MajorClass](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__majorclass)基础上进一步细分的类型。蓝牙标准协议字段。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

类型说明[constant.MajorMinorClass](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__majorminorclass)蓝牙设备的子类型。

#### BluetoothAddress21+

type BluetoothAddress = common.BluetoothAddress

描述蓝牙设备地址信息的参数结构，包括地址与地址类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

类型说明[common.BluetoothAddress](@ohos.bluetooth.common (蓝牙common模块).md#ZH-CN_TOPIC_0000002497445440__bluetoothaddress)蓝牙设备的地址信息。

#### connection.pairDevice

pairDevice(deviceId: string, callback: AsyncCallback<void>): void

主动发起与对端蓝牙设备的配对流程。使用Callback异步回调。

- 若开发者不知道目标设备的[地址类型](@ohos.bluetooth.common (蓝牙common模块).md#ZH-CN_TOPIC_0000002497445440__bluetoothaddresstype)，建议调用此接口发起配对。
- 蓝牙配对状态通过[on('bondStateChange')](#ZH-CN_TOPIC_0000002529445383__connectiononbondstatechange)的回调结果获取。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是需要配对的对端蓝牙设备地址，例如："XX:XX:XX:XX:XX:XX"。callbackAsyncCallback<void>是回调函数。当配对成功，err为undefined，否则为错误对象。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
// callback
try {
    connection.pairDevice('11:22:33:44:55:66', (err: BusinessError) => {
        console.info('pairDevice, device name err:' + JSON.stringify(err));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.pairDevice

pairDevice(deviceId: string): Promise<void>

主动发起与对端蓝牙设备的配对流程。使用Promise异步回调。

- 若开发者不知道目标设备的[地址类型](@ohos.bluetooth.common (蓝牙common模块).md#ZH-CN_TOPIC_0000002497445440__bluetoothaddresstype)，建议调用此接口发起配对。
- 蓝牙配对状态通过[on('bondStateChange')](#ZH-CN_TOPIC_0000002529445383__connectiononbondstatechange)的回调结果获取。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是需要配对的对端蓝牙设备地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.pairDevice('11:22:33:44:55:66').then(() => {
        console.info('pairDevice');
    }, (error: BusinessError) => {
        console.error('pairDevice: errCode:' + error.code + ',errMessage' + error.message);
    })

} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.pairDevice21+

pairDevice(deviceId: BluetoothAddress): Promise<void>

主动发起与对端蓝牙设备的配对流程。使用Promise异步回调。

- 若开发者已知目标设备的MAC地址及[地址类型](@ohos.bluetooth.common (蓝牙common模块).md#ZH-CN_TOPIC_0000002497445440__bluetoothaddresstype)，建议调用此接口发起配对。
- 蓝牙配对状态通过[on('bondStateChange')](#ZH-CN_TOPIC_0000002529445383__connectiononbondstatechange)的回调结果获取。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceId[BluetoothAddress](@ohos.bluetooth.common (蓝牙common模块).md#ZH-CN_TOPIC_0000002497445440__bluetoothaddress)是需要配对的对端蓝牙设备地址信息，包括地址与地址类型。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码**：

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.ConnectivityKit';
// promise
try {
    let btAddr: common.BluetoothAddress = {
        "address": '11:22:33:44:55:66', // 目标设备的实际MAC地址或虚拟MAC地址
        "addressType": common.BluetoothAddressType.REAL, // 相应的地址类型
    }
    connection.pairDevice(btAddr).then(() => {
        console.info('pairDevice');
    }, (error: BusinessError) => {
        console.error('errCode: ' + error.code + ', errMessage' + error.message);
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getRemoteDeviceName

getRemoteDeviceName(deviceId: string): string

获取对端蓝牙设备的名称。

- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取设备名称。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备的地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明string以字符串格式返回设备名称。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    let remoteDeviceName: string = connection.getRemoteDeviceName('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getRemoteDeviceName16+

getRemoteDeviceName(deviceId: string, alias?: boolean): string

获取对端蓝牙设备的名称，其中alias为可选参数。

- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取设备名称。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 16开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备的地址，例如："XX:XX:XX:XX:XX:XX"。aliasboolean否

表示是否获取对端蓝牙设备别名。

- 如果携带alias，则根据alias判断是否获取对端蓝牙设备别名：true表示获取对端蓝牙设备别名，false表示获取对端蓝牙设备原始名称。

- 如果未携带alias，则默认值为true，返回对端蓝牙设备别名。

**返回值：**

类型说明string以字符串格式返回设备名称。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Failed to obtain the name or alias of the peer Bluetooth device.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    let remoteDeviceName: string = connection.getRemoteDeviceName('XX:XX:XX:XX:XX:XX', true);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getRemoteDeviceClass

getRemoteDeviceClass(deviceId: string): DeviceClass

获取对端蓝牙设备的类别。

- 从API version 18开始，此接口不再校验ohos.permission.ACCESS_BLUETOOTH权限。
- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取设备类别信息。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备的地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明[DeviceClass](#ZH-CN_TOPIC_0000002529445383__deviceclass)对端设备的类别。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    let remoteDeviceClass: connection.DeviceClass = connection.getRemoteDeviceClass('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getRemoteDeviceTransport20+

getRemoteDeviceTransport(deviceId: string): BluetoothTransport

获取对端蓝牙设备的传输类型。

- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取设备的传输类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备的地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明[BluetoothTransport](#ZH-CN_TOPIC_0000002529445383__bluetoothtransport)对端设备的传输类型。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Get transport failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let transport: connection.BluetoothTransport = connection.getRemoteDeviceTransport('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getRemoteProfileUuids12+

getRemoteProfileUuids(deviceId: string, callback: AsyncCallback<Array<ProfileUuids>>): void

获取对端蓝牙设备的Profile协议能力，通过UUID区分。使用Callback异步回调。

- 建议仅对已配对的设备调用该方法。
- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取Profile协议能力。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备地址，例如："XX:XX:XX:XX:XX:XX"。callbackAsyncCallback<Array<[ProfileUuids](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileuuids12)>>是回调函数。当获取UUID成功，err为undefined，获取到的是Profile协议能力集合；否则为错误对象。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    connection.getRemoteProfileUuids('XX:XX:XX:XX:XX:XX', (err: BusinessError, data: Array<connection.ProfileUuids>) => {
        console.info('getRemoteProfileUuids, err: ' + JSON.stringify(err) + ', data: ' + JSON.stringify(data));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getRemoteProfileUuids12+

getRemoteProfileUuids(deviceId: string): Promise<Array<ProfileUuids>>

获取对端蓝牙设备的Profile协议能力，通过UUID区分。使用Promise异步回调。

- 建议仅对已配对的设备调用该方法。
- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取Profile协议能力。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明Promise<Array<[ProfileUuids](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileuuids12)>>Promise对象，返回支持的Profile协议能力集合。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    connection.getRemoteProfileUuids('XX:XX:XX:XX:XX:XX').then(() => {
        console.info('getRemoteProfileUuids');
    }, (err: BusinessError) => {
        console.error('getRemoteProfileUuids: errCode' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getLocalName

getLocalName(): string

获取本机蓝牙设备的名称。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明string本机蓝牙设备名称。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    let localName: string = connection.getLocalName();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getPairedDevices

getPairedDevices(): Array<string>

获取已配对蓝牙设备的地址集合。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明Array<string>

已配对蓝牙设备的地址集合。

基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。

- 已配对的地址不会变更。

- 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。

- 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。

- 若要持久化保存该地址，可使用[access.addPersistentDeviceId](@ohos.bluetooth.access (蓝牙access模块).md#ZH-CN_TOPIC_0000002497605416__accessaddpersistentdeviceid16)方法。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    let devices: Array<string> = connection.getPairedDevices();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getPairState11+

getPairState(deviceId: string): BondState

获取对端蓝牙设备的配对状态信息。

- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取配对状态信息。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备的地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明[BondState](#ZH-CN_TOPIC_0000002529445383__bondstate)表示设备的蓝牙配对状态。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    let res: connection.BondState = connection.getPairState("XX:XX:XX:XX:XX:XX");
    console.info('getPairState: ' + res);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getProfileConnectionState

getProfileConnectionState(profileId?: ProfileId): ProfileConnectionState

获取蓝牙Profile协议的连接状态，其中ProfileId为可选参数。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明profileId[ProfileId](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileid)否

表示Profile协议的枚举值。如果携带ProfileId，则返回指定Profile协议的连接状态。如果未携带ProfileId，则检查所有支持的Profile连接状态，按如下优先级顺序检查并返回：

- 存在已连接的Profile协议，则返回[STATE_CONNECTED](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileconnectionstate)。

- 存在正在连接的Profile协议，则返回[STATE_CONNECTING](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileconnectionstate)。

- 存在正在断连的Profile协议，则返回[STATE_DISCONNECTING](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileconnectionstate)。

- 以上条件均不满足，则返回[STATE_DISCONNECTED](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileconnectionstate)。

**返回值：**

类型说明[ProfileConnectionState](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileconnectionstate)Profile协议的连接状态。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Incorrect parameter types.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900004Profile not supported.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { constant } from '@kit.ConnectivityKit';
try {
    let result: connection.ProfileConnectionState = connection.getProfileConnectionState(constant.ProfileId.PROFILE_A2DP_SOURCE);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.setDevicePairingConfirmation

setDevicePairingConfirmation(deviceId: string, accept: boolean): void

收到对端蓝牙设备的配对请求事件后，确认请求结果。

- 对端蓝牙的配对请求通过[on('pinRequired')](#ZH-CN_TOPIC_0000002529445383__connectiononpinrequired)的回调结果获取。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH 和 ohos.permission.MANAGE_BLUETOOTH（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备地址，例如："XX:XX:XX:XX:XX:XX"。acceptboolean是是否接受对端设备的配对请求。true表示接受，false表示不接受。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
// 订阅“pinRequired”配对请求事件，收到对端配对请求后设置配对确认。
function onReceivePinRequiredEvent(data: connection.PinRequiredParam) { // data为配对请求的入参，配对请求参数。
    console.info('pin required  = '+ JSON.stringify(data));
    connection.setDevicePairingConfirmation(data.deviceId, true);
}
try {
    connection.on('pinRequired', onReceivePinRequiredEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.setDevicePinCode

setDevicePinCode(deviceId: string, code: string, callback: AsyncCallback<void>): void

蓝牙配对时，弹框提示用户输入个人身份识别码（Personal identification number，PIN），调用此接口设置PIN码，完成蓝牙配对。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备MAC地址，例如："XX:XX:XX:XX:XX:XX"。codestring是用户输入的PIN码，该字符串的字符个数范围为(0, 16]，例如："12345"。callbackAsyncCallback<void>是回调函数，当设置PinCode成功，err为undefined，否则为错误对象。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
// callback
try {
    connection.setDevicePinCode('11:22:33:44:55:66', '12345', (err: BusinessError) => {
        console.info('setDevicePinCode,device name err: ' + JSON.stringify(err));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.setDevicePinCode

setDevicePinCode(deviceId: string, code: string): Promise<void>

蓝牙配对时，弹框提示用户输入PIN码，调用此接口请求用户输入PIN码，完成蓝牙配对。使用Promise异步回调。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备MAC地址，例如："XX:XX:XX:XX:XX:XX"。codestring是用户输入的PIN码，该字符串的字符个数范围为(0, 16]，例如："12345"。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.setDevicePinCode('11:22:33:44:55:66', '12345').then(() => {
        console.info('setDevicePinCode');
    }, (error: BusinessError) => {
        console.error('setDevicePinCode: errCode:' + error.code + ',errMessage' + error.message);
    })

} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.setLocalName(deprecated)

setLocalName(name: string): void

设置本机蓝牙设备名称，不能设置为空字符串。如果设为空字符串会失败。

从API version 10开始支持，从API version 12开始废弃，不再提供替代接口。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明namestring是需要设置的蓝牙名称，名称长度范围：(0, 248]，单位：Byte。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    connection.setLocalName('device_name');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.setBluetoothScanMode

setBluetoothScanMode(mode: ScanMode, duration: number): void

设置蓝牙扫描模式，决定本机设备是否可被连接，或者可被发现。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明mode[ScanMode](#ZH-CN_TOPIC_0000002529445383__scanmode)是蓝牙扫描模式。当扫描模式为SCAN_MODE_GENERAL_DISCOVERABLE时，超出duration持续时间(不为0)，扫描模式会重新设置为SCAN_MODE_CONNECTABLE。durationnumber是设备可被发现的持续时间，单位：ms。设置为0则表示持续可发现。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    // 设置为可连接可发现才可被对端设备扫描到，可以连接。
    connection.setBluetoothScanMode(connection.ScanMode.SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 100);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getBluetoothScanMode

getBluetoothScanMode(): ScanMode

获取蓝牙扫描模式。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明[ScanMode](#ZH-CN_TOPIC_0000002529445383__scanmode)蓝牙扫描模式。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    let scanMode: connection.ScanMode = connection.getBluetoothScanMode();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.startBluetoothDiscovery

startBluetoothDiscovery(): void

开启蓝牙扫描，发现对端蓝牙设备。

-

该接口支持发现传统蓝牙设备和低功耗蓝牙设备，整个蓝牙扫描过程大约持续12s。

-

扫描结果可通过API version 10开始支持的[connection.on('bluetoothDeviceFind')](#ZH-CN_TOPIC_0000002529445383__connectiononbluetoothdevicefind)或者API version 18开始支持的[connection.on('discoveryResult')](#ZH-CN_TOPIC_0000002529445383__connectionondiscoveryresult18)的回调函数获取到。推荐使用[connection.on('discoveryResult')](#ZH-CN_TOPIC_0000002529445383__connectionondiscoveryresult18)，该方式可以获取到更多设备信息。

-

若在扫描过程中，请勿重复调用该方法（可使用[connection.isBluetoothDiscovering](#ZH-CN_TOPIC_0000002529445383__connectionisbluetoothdiscovering11)判断蓝牙当前是否处于扫描过程中）。

-

调用[connection.stopBluetoothDiscovery](#ZH-CN_TOPIC_0000002529445383__connectionstopbluetoothdiscovery)可以停止该方法开启的扫描流程，扫描停止后，才能开启下一次蓝牙扫描。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: Array<string>) {
    console.info('data length' + data.length);
}
try {
    connection.on('bluetoothDeviceFind', onReceiveEvent);
    connection.startBluetoothDiscovery();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.stopBluetoothDiscovery

stopBluetoothDiscovery(): void

关闭蓝牙扫描。

-

关闭的扫描是由[connection.startBluetoothDiscovery](#ZH-CN_TOPIC_0000002529445383__connectionstartbluetoothdiscovery)触发的。

-

当应用不再需要扫描设备时，需主动调用该方法关闭扫描。

-

若不在扫描过程中，请勿重复调用该方法（可使用[connection.isBluetoothDiscovering](#ZH-CN_TOPIC_0000002529445383__connectionisbluetoothdiscovering11)判断蓝牙当前是否处于扫描过程中）。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    connection.stopBluetoothDiscovery();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.isBluetoothDiscovering11+

isBluetoothDiscovering(): boolean

判断本机蓝牙设备是否处于设备扫描状态。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明boolean是否开启蓝牙发现。true表示正在发起设备扫描，false表示未发起设备扫描。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
    let res: boolean = connection.isBluetoothDiscovering();
    console.info('isBluetoothDiscovering: ' + res);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.setRemoteDeviceName12+

setRemoteDeviceName(deviceId: string, name: string): Promise<void>

设置对端蓝牙设备的名称，不能设置为空字符串。如果设为空字符串会失败。使用Promise异步回调。

- 建议仅对已配对的设备调用该方法。
- 从API version 21开始，此接口支持使用对端设备的实际MAC地址进行名称设置。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端设备MAC地址，例如："XX:XX:XX:XX:XX:XX"。namestring是修改对端设备名称，名称长度范围：(0, 64]，单位：Byte。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.2900001Service stopped.2900003Bluetooth disabled.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.setRemoteDeviceName('11:22:33:44:55:66', 'RemoteDeviceName').then(() => {
        console.info('setRemoteDeviceName success');
    }, (error: BusinessError) => {
        console.error('setRemoteDeviceName: errCode: ' + error.code + ',errMessage' + error.message);
    })
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getRemoteDeviceBatteryInfo12+

getRemoteDeviceBatteryInfo(deviceId: string): Promise<BatteryInfo>

获取对端蓝牙设备的电量信息。使用Promise异步回调。

- 对端蓝牙设备的电量信息变更通过[on('batteryChange')](#ZH-CN_TOPIC_0000002529445383__connectiononbatterychange12)的回调结果获取。
- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取电量信息。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示对端蓝牙设备的MAC地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明Promise<[BatteryInfo](#ZH-CN_TOPIC_0000002529445383__batteryinfo12)>Promise对象，返回电量信息对象。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.2900001Service stopped.2900003Bluetooth disabled.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.getRemoteDeviceBatteryInfo('11:22:33:AA:BB:FF').then((data: connection.BatteryInfo) => {
        console.info('getRemoteDeviceBatteryInfo success, DeviceType:' + JSON.stringify(data));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.on('batteryChange')12+

on(type: 'batteryChange', callback: Callback<BatteryInfo>): void

订阅对端设备的电量信息变化事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'batteryChange'，表示对端设备的电量信息变化事件。当该设备通知电量变化时，会触发该事件。callbackCallback<[BatteryInfo](#ZH-CN_TOPIC_0000002529445383__batteryinfo12)>是指定订阅的回调函数，返回电量信息。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
let onReceiveEvent: (data: connection.BatteryInfo) => void = (data: connection.BatteryInfo) => {
    console.info('BatteryInfo = '+ JSON.stringify(data));
}
try {
    connection.on('batteryChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.off('batteryChange')12+

off(type: 'batteryChange', callback?: Callback<BatteryInfo>): void

取消订阅对端设备的电量信息变化事件。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'batteryChange'，表示对端设备的电量信息变化事件。callbackCallback<[BatteryInfo](#ZH-CN_TOPIC_0000002529445383__batteryinfo12)>否

指定取消订阅的回调函数通知。

若传参，则需与[connection.on('batteryChange')](#ZH-CN_TOPIC_0000002529445383__connectiononbatterychange12)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
let onReceiveEvent: (data: connection.BatteryInfo) => void = (data: connection.BatteryInfo) => {
    console.info('BatteryInfo = '+ JSON.stringify(data));
}
try {
    connection.on('batteryChange', onReceiveEvent);
    connection.off('batteryChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.on('bluetoothDeviceFind')

on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void

订阅蓝牙设备扫描结果上报事件。使用Callback异步回调。

-

可扫描到的设备类型包括传统蓝牙设备和低功耗蓝牙设备。

-

该上报方式只支持获取设备地址信息。

- 推荐使用API version 18开始支持的[connection.on('discoveryResult')](#ZH-CN_TOPIC_0000002529445383__connectionondiscoveryresult18)扫描上报方式，可获取到更多设备信息，包括设备地址、设备信号强度、设备名称和设备类型。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'bluetoothDeviceFind'，表示蓝牙设备扫描结果上报事件。当调用[connection.startBluetoothDiscovery](#ZH-CN_TOPIC_0000002529445383__connectionstartbluetoothdiscovery)后，开始设备扫描，若扫描到设备，触发该事件。callbackCallback<Array<string>>是

指定订阅的回调函数，会携带扫描到的设备地址集合。

基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。

- 已配对的地址不会变更。

- 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。

- 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。

- 若要持久化保存该地址，可使用[access.addPersistentDeviceId](@ohos.bluetooth.access (蓝牙access模块).md#ZH-CN_TOPIC_0000002497605416__accessaddpersistentdeviceid16)方法。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: Array<string>) { // data为蓝牙设备地址集合。
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    connection.on('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.off('bluetoothDeviceFind')

off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void

取消订阅蓝牙设备扫描结果上报事件。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'bluetoothDeviceFind'，表示蓝牙设备扫描结果上报事件。callbackCallback<Array<string>>否

指定取消订阅的回调函数通知。

若传参，则需与[connection.on('bluetoothDeviceFind')](#ZH-CN_TOPIC_0000002529445383__connectiononbluetoothdevicefind)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: Array<string>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    connection.on('bluetoothDeviceFind', onReceiveEvent);
    connection.off('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.on('bondStateChange')

on(type: 'bondStateChange', callback: Callback<BondStateParam>): void

订阅蓝牙配对状态变化事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是

事件回调类型，支持的事件为'bondStateChange'，表示蓝牙配对状态变化事件。

当调用[connection.pairDevice](#ZH-CN_TOPIC_0000002529445383__connectionpairdevice)发起主动配对，或者本机设备收到其他设备的配对请求时，触发该事件。

callbackCallback<[BondStateParam](#ZH-CN_TOPIC_0000002529445383__bondstateparam)>是指定订阅的回调函数，会携带配对状态结果。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: connection.BondStateParam) { // data为回调函数入参，表示配对的状态。
    console.info('pair state = '+ JSON.stringify(data));
}
try {
    connection.on('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.off('bondStateChange')

off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void

取消订阅蓝牙配对状态变化事件。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'bondStateChange'，表示蓝牙配对状态变化事件。callbackCallback<[BondStateParam](#ZH-CN_TOPIC_0000002529445383__bondstateparam)>否

指定取消订阅的回调函数通知。

若传参，则需与[connection.on('bondStateChange')](#ZH-CN_TOPIC_0000002529445383__connectiononbondstatechange)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: connection.BondStateParam) {
    console.info('bond state = '+ JSON.stringify(data));
}
try {
    connection.on('bondStateChange', onReceiveEvent);
    connection.off('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.on('pinRequired')

on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void

订阅配对请求事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是

事件回调类型，支持的事件为'pinRequired'，表示配对请求事件。

当调用[connection.pairDevice](#ZH-CN_TOPIC_0000002529445383__connectionpairdevice)发起主动配对，或者本机设备收到其他设备的配对请求时，触发该事件。

callbackCallback<[PinRequiredParam](#ZH-CN_TOPIC_0000002529445383__pinrequiredparam)>是指定订阅的回调函数，会携带配对请求。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: connection.PinRequiredParam) { // data为配对请求参数。
    console.info('pin required = '+ JSON.stringify(data));
}
try {
    connection.on('pinRequired', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.off('pinRequired')

off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void

取消订阅配对请求事件。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'pinRequired'，表示配对请求事件。callbackCallback<[PinRequiredParam](#ZH-CN_TOPIC_0000002529445383__pinrequiredparam)>否

指定取消订阅的回调函数通知。

若传参，则需与[connection.on('pinRequired')](#ZH-CN_TOPIC_0000002529445383__connectiononpinrequired)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: connection.PinRequiredParam) {
    console.info('pin required = '+ JSON.stringify(data));
}
try {
    connection.on('pinRequired', onReceiveEvent);
    connection.off('pinRequired', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.on('discoveryResult')18+

on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void

订阅蓝牙设备扫描结果上报事件。使用Callback异步回调。

-

可扫描到的设备类型包括传统蓝牙设备和低功耗蓝牙设备。

- 该上报方式支持获取设备地址、设备信号强度、设备名称和设备类型。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'discoveryResult'，表示蓝牙设备扫描结果上报事件。当调用[connection.startBluetoothDiscovery](#ZH-CN_TOPIC_0000002529445383__connectionstartbluetoothdiscovery)后，开始设备扫描，若扫描到设备，触发该事件。callbackCallback<Array<[DiscoveryResult](#ZH-CN_TOPIC_0000002529445383__discoveryresult18)>>是指定订阅的回调函数，会携带扫描结果的集合。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
let onReceiveEvent: (data: Array<connection.DiscoveryResult>) => void = (data: Array<connection.DiscoveryResult>) => { // data为蓝牙设备扫描结果集合。
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    connection.on('discoveryResult', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.off('discoveryResult')18+

off(type: 'discoveryResult', callback?: Callback<Array<DiscoveryResult>>): void

取消订阅蓝牙设备发现上报事件。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'discoveryResult'，表示蓝牙设备扫描结果上报事件。callbackCallback<Array<[DiscoveryResult](#ZH-CN_TOPIC_0000002529445383__discoveryresult18)>>否

指定取消订阅的回调函数通知。

若传参，则需与[connection.on('discoveryResult')](#ZH-CN_TOPIC_0000002529445383__connectionondiscoveryresult18)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
let onReceiveEvent: (data: Array<connection.DiscoveryResult>) => void = (data: Array<connection.DiscoveryResult>) => { // data为蓝牙设备扫描结果集合。
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    connection.on('discoveryResult', onReceiveEvent);
    connection.off('discoveryResult', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.getLastConnectionTime15+

getLastConnectionTime(deviceId: string): Promise<number>

获取对端蓝牙设备最近一次连接的时间点。使用Promise异步回调。

- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取最近一次连接时间。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示远端设备MAC地址。例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明Promise<number>Promise对象，返回对端蓝牙设备最近一次连接的时间点，格式为秒级的UNIX时间戳。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.getLastConnectionTime('11:22:33:44:55:66').then((time: number) => {
        console.info(`connectionTime: ${time}`);
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.connectAllowedProfiles16+

connectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void

连接对端设备支持的profile（只包括A2DP、HFP和HID）。使用Callback异步回调。

- 需先调用[connection.pairDevice](#ZH-CN_TOPIC_0000002529445383__connectionpairdevice)发起配对，且仅允许在每次发起配对后30s内调用此接口一次。
- 当配对成功后，建议先调用[getRemoteProfileUuids](#ZH-CN_TOPIC_0000002529445383__connectiongetremoteprofileuuids12)主动查询目标设备支持的profile能力。若存在应用需要的能力，才调用此接口。
- 从API version 21开始，此接口支持使用对端设备的实际MAC地址进行profile连接。

**需要权限：**: ohos.permission.ACCESS_BLUETOOTH

**系统能力：**: SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示需要连接的对端设备地址，例如："XX:XX:XX:XX:XX:XX"。callbackAsyncCallback<void>是回调函数。当发起连接成功，err为undefined，否则为错误对象。

**错误码：**

以下错误码的详细介绍请参见 [通用错误码说明文档](../../errors/通用错误码.md)和[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
  connection.connectAllowedProfiles('68:13:24:79:4C:8C', (err: BusinessError) => {
    if (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
      return;
    }
    console.info('connectAllowedProfiles');
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### connection.connectAllowedProfiles16+

connectAllowedProfiles(deviceId: string): Promise<void>

连接对端设备支持的profile（只包括A2DP、HFP和HID）。使用Promise异步回调。

- 需先调用[connection.pairDevice](#ZH-CN_TOPIC_0000002529445383__connectionpairdevice)发起配对，且仅允许在每次发起配对后30s内调用此接口一次。
- 当配对成功后，建议先调用[getRemoteProfileUuids](#ZH-CN_TOPIC_0000002529445383__connectiongetremoteprofileuuids12)主动查询目标设备支持的profile能力。若存在应用需要的能力，才调用此接口。
- 从API version 21开始，此接口支持使用对端设备的实际MAC地址进行profile连接。

**需要权限：**: ohos.permission.ACCESS_BLUETOOTH

**系统能力：**: SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是表示需要连接的对端设备地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见 [通用错误码说明文档](../../errors/通用错误码.md)和[蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900099Operation failed.

**示例：**

```ets
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
try {
  connection.connectAllowedProfiles('68:13:24:79:4C:8C').then(() => {
      console.info('connectAllowedProfiles');
    }, (err: BusinessError) => {
      console.error('connectAllowedProfiles:errCode' + err.code + ', errMessage: ' + err.message);
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### BondStateParam

描述配对状态结果的参数结构。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称类型只读可选说明deviceIdstring否否配对中的对端设备地址。state[BondState](#ZH-CN_TOPIC_0000002529445383__bondstate)否否配对状态。cause12+[UnbondCause](#ZH-CN_TOPIC_0000002529445383__unbondcause12)否否配对失败的原因。

#### PinRequiredParam

描述配对请求的参数结构。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称类型只读可选说明deviceIdstring否否要配对的对端设备地址。pinCodestring否否配对过程中的密钥。

#### DeviceClass

描述蓝牙设备的类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称类型只读可选说明majorClass[MajorClass](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__majorclass)否否主要类型。是蓝牙标准协议中定义的类型字段。majorMinorClass[MajorMinorClass](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__majorminorclass)否否子类型，是在主要类型上基础上进一步细分的类型。是蓝牙标准协议中定义的类型字段。classOfDevicenumber否否设备类型。是蓝牙标准协议中定义的类型字段，包含了[MajorClass](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__majorclass)、[MajorMinorClass](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__majorminorclass)和支持的主要服务这三种设备信息。

#### BatteryInfo12+

描述设备的电量信息。

只有支持蓝牙标准协议定义的电量信息AT（Attention）命令（包括：+XEVENT和IPHONEACCEV）的设备才支持上报有效的电量信息。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称类型只读可选说明batteryLevelnumber否否

表示设备的电量值。

如果该值为-1，表示没有电量信息。

leftEarBatteryLevelnumber否否

若是蓝牙耳机设备类型，表示左侧耳机的电量值。

如果该值为-1，表示没有电量信息。

leftEarChargeState[DeviceChargeState](#ZH-CN_TOPIC_0000002529445383__devicechargestate12)否否若是蓝牙耳机设备类型，表示左侧耳机的充电状态。rightEarBatteryLevelnumber否否

若是蓝牙耳机设备类型，表示右侧耳机的电量值。

如果该值为-1，表示没有电量信息。

rightEarChargeState[DeviceChargeState](#ZH-CN_TOPIC_0000002529445383__devicechargestate12)否否若是蓝牙耳机设备类型，表示右侧耳机的充电状态。boxBatteryLevelnumber否否

若是蓝牙耳机设备类型，表示耳机仓的电量值。

如果值该为-1，表示没有电量信息。

boxChargeState[DeviceChargeState](#ZH-CN_TOPIC_0000002529445383__devicechargestate12)否否若是蓝牙耳机设备类型，表示耳机仓的充电状态。

#### BluetoothTransport

枚举，表示设备传输类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明TRANSPORT_BR_EDR0传统蓝牙（Basic Rate/Enhanced Data Rate，BR/EDR）设备传输方式。TRANSPORT_LE1低功耗蓝牙（Bluetooth Low Energy，BLE）设备传输方式。TRANSPORT_DUAL20+2同时支持传统蓝牙（BR/EDR）和低功耗蓝牙（BLE）的双模设备传输方式。设备可以根据需要选择使用传统蓝牙（BR/EDR）或低功耗蓝牙（BLE）进行通信。TRANSPORT_UNKNOWN20+3未知的设备传输方式。

#### ScanMode

枚举，表示扫描模式。该模式决定设备是否可被发现或可被连接。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明SCAN_MODE_NONE0不可发现、不可连接模式。SCAN_MODE_CONNECTABLE1可连接模式。SCAN_MODE_GENERAL_DISCOVERABLE2通用可发现模式，可被长时间发现。SCAN_MODE_LIMITED_DISCOVERABLE3有限可发现模式，持续一定时间。SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE4可连接及通用可发现模式。SCAN_MODE_CONNECTABLE_LIMITED_DISCOVERABLE5可连接及有限可发现模式。

#### BondState

枚举，配对状态。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明BOND_STATE_INVALID0未配对状态。BOND_STATE_BONDING1配对中的状态。BOND_STATE_BONDED2已配对状态。

#### UnbondCause12+

枚举，配对失败原因。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明USER_REMOVED0用户主动移除设备。若配对状态[BondState](#ZH-CN_TOPIC_0000002529445383__bondstate)是已配对，也表示配对成功。REMOTE_DEVICE_DOWN1对端设备不在线。例如：对端设备蓝牙是关闭的。AUTH_FAILURE2鉴权失败。例如：两端设备密钥不匹配。AUTH_REJECTED3鉴权被拒绝。例如：对端设备拒绝了配对请求。INTERNAL_ERROR4内部错误。例如：设备不支持配对、配对过程超时等异常。

#### DeviceChargeState12+

枚举，表示设备当前的充电状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明DEVICE_NORMAL_CHARGE_NOT_CHARGED0不支持超级快充能力的设备当前处于未充电状态。DEVICE_NORMAL_CHARGE_IN_CHARGING1不支持超级快充能力的设备当前处于充电状态。DEVICE_SUPER_CHARGE_NOT_CHARGED2支持超级快充能力的设备当前处于未充电状态。DEVICE_SUPER_CHARGE_IN_CHARGING3支持超级快充能力的设备当前处于充电状态。

#### DiscoveryResult18+

扫描到设备后，上报的扫描结果。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称类型只读可选说明deviceIdstring否否

扫描到的设备地址。

基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。

- 已配对的地址不会变更。

- 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。

- 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。

- 若要持久化保存该地址，可使用[access.addPersistentDeviceId](@ohos.bluetooth.access (蓝牙access模块).md#ZH-CN_TOPIC_0000002497605416__accessaddpersistentdeviceid16)方法。

rssinumber否否扫描到的设备信号强度，单位：dBm。deviceNamestring否否扫描到的设备名称。deviceClass[DeviceClass](#ZH-CN_TOPIC_0000002529445383__deviceclass)否否扫描到的设备类型。