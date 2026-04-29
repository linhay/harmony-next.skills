# @ohos.bluetoothManager (蓝牙)

蓝牙模块提供了基础的传统蓝牙能力以及BLE的扫描、广播等功能。

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 10 开始，该接口不再维护，推荐使用[@ohos.bluetooth.ble](@ohos.bluetooth.ble (蓝牙ble模块).md)等相关profile接口。

#### 导入模块

```ets
import { bluetoothManager } from '@kit.ConnectivityKit';
```

#### bluetoothManager.enableBluetooth(deprecated)

enableBluetooth(): void

开启蓝牙。


从API version 9开始支持，从API version 10开始废弃。建议使用[access.enableBluetooth](@ohos.bluetooth.access (蓝牙access模块).md#ZH-CN_TOPIC_0000002522241436__accessenablebluetooth)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码]([蓝牙服务子系统错误码](../../errors/蓝牙服务子系统错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.enableBluetooth();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.disableBluetooth(deprecated)

disableBluetooth(): void

关闭蓝牙。


从API version 9开始支持，从API version 10开始废弃。建议使用[access.disableBluetooth](@ohos.bluetooth.access (蓝牙access模块).md#ZH-CN_TOPIC_0000002522241436__accessdisablebluetooth)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.disableBluetooth();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ", errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getLocalName(deprecated)

getLocalName(): string

获取蓝牙本地设备名称。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getLocalName](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectiongetlocalname)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 蓝牙本地设备名称。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let localName: string = bluetoothManager.getLocalName();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getState(deprecated)

getState(): BluetoothState

获取蓝牙开关状态。


从API version 9开始支持，从API version 10开始废弃。建议使用[access.getState](@ohos.bluetooth.access (蓝牙access模块).md#ZH-CN_TOPIC_0000002522241436__accessgetstate)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| BluetoothState | 表示蓝牙开关状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let state: bluetoothManager.BluetoothState = bluetoothManager.getState();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getBtConnectionState(deprecated)

getBtConnectionState(): ProfileConnectionState

获取蓝牙本端的Profile连接状态，例如：任意一个支持的Profile连接状态为已连接，则此接口返回状态为已连接。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getProfileConnectionState](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectiongetprofileconnectionstate)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ProfileConnectionState | 表示蓝牙设备的Profile连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let connectionState: bluetoothManager.ProfileConnectionState = bluetoothManager.getBtConnectionState();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.setLocalName(deprecated)

setLocalName(name: string): void

设置蓝牙本地设备名称。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.setLocalName](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectionsetlocalnamedeprecated)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要设置的蓝牙名称，最大长度为248字节数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.setLocalName('device_name');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.pairDevice(deprecated)

pairDevice(deviceId: string): void

发起蓝牙配对。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.pairDevice](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectionpairdevice)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示配对的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    // 实际的地址可由扫描流程获取
    bluetoothManager.pairDevice("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getProfileConnectionState(deprecated)

getProfileConnectionState(profileId: ProfileId): ProfileConnectionState

依据ProfileId获取指定profile的连接状态。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getProfileConnectionState](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectiongetprofileconnectionstate)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profileId | ProfileId | 是 | 表示profile的枚举值，例如：PROFILE_A2DP_SOURCE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ProfileConnectionState | profile的连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let result: bluetoothManager.ProfileConnectionState = bluetoothManager.getProfileConnectionState(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getRemoteDeviceName(deprecated)

getRemoteDeviceName(deviceId: string): string

获取对端蓝牙设备的名称。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getRemoteDeviceName](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectiongetremotedevicename)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示远程设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以字符串格式返回设备名称。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let remoteDeviceName: string = bluetoothManager.getRemoteDeviceName("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getRemoteDeviceClass(deprecated)

getRemoteDeviceClass(deviceId: string): DeviceClass

获取对端蓝牙设备的类别。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getRemoteDeviceClass](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectiongetremotedeviceclass)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示远程设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DeviceClass | 远程设备的类别。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let remoteDeviceClass: bluetoothManager.DeviceClass  = bluetoothManager.getRemoteDeviceClass("XX:XX:XX:XX:XX:XX");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getPairedDevices(deprecated)

getPairedDevices(): Array<string>

获取蓝牙配对列表。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getPairedDevices](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectiongetpaireddevices)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 已配对蓝牙设备的地址列表。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let devices: Array<string> = bluetoothManager.getPairedDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.setBluetoothScanMode(deprecated)

setBluetoothScanMode(mode: ScanMode, duration: number): void

设置蓝牙扫描模式，可以被远端设备发现。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.setBluetoothScanMode](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectionsetbluetoothscanmode)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | ScanMode | 是 | 蓝牙扫描模式。 |
| duration | number | 是 | 设备可被发现的持续时间，单位为毫秒；设置为0则持续可发现。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    // 设置为可连接可发现才可被远端设备扫描到，可以连接。
    bluetoothManager.setBluetoothScanMode(bluetoothManager.ScanMode.SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 100);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.getBluetoothScanMode(deprecated)

getBluetoothScanMode(): ScanMode

获取蓝牙扫描模式。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getBluetoothScanMode](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectiongetbluetoothscanmode)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ScanMode | 蓝牙扫描模式。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let scanMode: bluetoothManager.ScanMode = bluetoothManager.getBluetoothScanMode();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.startBluetoothDiscovery(deprecated)

startBluetoothDiscovery(): void

开启蓝牙扫描，可以发现远端设备。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.startBluetoothDiscovery](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectionstartbluetoothdiscovery)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let deviceId: Array<string>;
function onReceiveEvent(data: Array<string>) {
    deviceId = data;
}
try {
    bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
    bluetoothManager.startBluetoothDiscovery();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.stopBluetoothDiscovery(deprecated)

stopBluetoothDiscovery(): void

关闭蓝牙扫描。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.stopBluetoothDiscovery](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectionstopbluetoothdiscovery)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.stopBluetoothDiscovery();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.setDevicePairingConfirmation(deprecated)

setDevicePairingConfirmation(device: string, accept: boolean): void

设置设备配对请求确认。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.setDevicePairingConfirmation](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectionsetdevicepairingconfirmation)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH 和 ohos.permission.MANAGE_BLUETOOTH（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| accept | boolean | 是 | 接受配对请求设置为true，否则设置为false。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
// 订阅“pinRequired”配对请求事件，收到远端配对请求后设置配对确认
function onReceivePinRequiredEvent(data: bluetoothManager.PinRequiredParam) { // data为配对请求的入参，配对请求参数
    console.info('pin required  = '+ JSON.stringify(data));
    bluetoothManager.setDevicePairingConfirmation(data.deviceId, true);
}
try {
    bluetoothManager.on("pinRequired", onReceivePinRequiredEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.on('bluetoothDeviceFind')(deprecated)

on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void

订阅蓝牙设备发现上报事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.on('bluetoothDeviceFind')](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectiononbluetoothdevicefind)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bluetoothDeviceFind"字符串，表示蓝牙设备发现事件。 |
| callback | Callback<Array<string>> | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<string>) { // data为蓝牙设备地址集合
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.off('bluetoothDeviceFind')(deprecated)

off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void

取消订阅蓝牙设备发现上报事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.off('bluetoothDeviceFind')](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectionoffbluetoothdevicefind)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bluetoothDeviceFind"字符串，表示蓝牙设备发现事件。 |
| callback | Callback<Array<string>> | 否 | 表示取消订阅蓝牙设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<string>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
    bluetoothManager.off('bluetoothDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.on('pinRequired')(deprecated)

on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void

订阅远端蓝牙设备的配对请求事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.on('pinRequired')](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectiononpinrequired)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"pinRequired"字符串，表示配对请求事件。 |
| callback | Callback<PinRequiredParam> | 是 | 表示回调函数的入参，配对请求。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.PinRequiredParam) { // data为配对请求参数
    console.info('pin required = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('pinRequired', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.off('pinRequired')(deprecated)

off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void

取消订阅远端蓝牙设备的配对请求事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.off('pinRequired')](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectionoffpinrequired)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"pinRequired"字符串，表示配对请求事件。 |
| callback | Callback<PinRequiredParam> | 否 | 表示取消订阅蓝牙配对请求事件上报，入参为配对请求参数。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.PinRequiredParam) {
    console.info('pin required = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('pinRequired', onReceiveEvent);
    bluetoothManager.off('pinRequired', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.on('bondStateChange')(deprecated)

on(type: 'bondStateChange', callback: Callback<BondStateParam>): void

订阅蓝牙配对状态改变事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.on('bondStateChange')](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectiononbondstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bondStateChange"字符串，表示蓝牙配对状态改变事件。 |
| callback | Callback<BondStateParam> | 是 | 表示回调函数的入参，配对的状态。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BondStateParam) { // data为回调函数入参，表示配对的状态
    console.info('pair state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.off('bondStateChange')(deprecated)

off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void

取消订阅蓝牙配对状态改变事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.off('bondStateChange')](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__connectionoffbondstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bondStateChange"字符串，表示蓝牙配对状态改变事件。 |
| callback | Callback<BondStateParam> | 否 | 表示取消订阅蓝牙配对状态改变事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BondStateParam) {
    console.info('bond state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('bondStateChange', onReceiveEvent);
    bluetoothManager.off('bondStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.on('stateChange')(deprecated)

on(type: 'stateChange', callback: Callback<BluetoothState>): void

订阅蓝牙设备开关状态事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[access.on('stateChange')](@ohos.bluetooth.access (蓝牙access模块).md#ZH-CN_TOPIC_0000002522241436__accessonstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"stateChange"字符串，表示蓝牙状态改变事件。 |
| callback | Callback<BluetoothState> | 是 | 表示回调函数的入参，蓝牙状态。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('stateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.off('stateChange')(deprecated)

off(type: 'stateChange', callback?: Callback<BluetoothState>): void

取消订阅蓝牙设备开关状态事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[access.off('stateChange')](@ohos.bluetooth.access (蓝牙access模块).md#ZH-CN_TOPIC_0000002522241436__accessoffstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"stateChange"字符串，表示蓝牙状态改变事件。 |
| callback | Callback<BluetoothState> | 否 | 表示取消订阅蓝牙状态改变事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    bluetoothManager.on('stateChange', onReceiveEvent);
    bluetoothManager.off('stateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### bluetoothManager.sppListen(deprecated)

sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void

创建一个服务端监听Socket。


从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppListen](@ohos.bluetooth.socket (蓝牙socket模块).md#ZH-CN_TOPIC_0000002553201409__socketspplisten)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 服务的名称。 |
| option | SppOption | 是 | spp监听配置参数。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，服务端Socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code: BusinessError, number: number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
}

let sppOption: bluetoothManager.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
try {
    bluetoothManager.sppListen('server1', sppOption, serverSocket);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.sppAccept(deprecated)

sppAccept(serverSocket: number, callback: AsyncCallback<number>): void

服务端监听socket等待客户端连接。


从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppAccept](@ohos.bluetooth.socket (蓝牙socket模块).md#ZH-CN_TOPIC_0000002553201409__socketsppaccept)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serverSocket | number | 是 | 服务端socket的id。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，客户端socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code: BusinessError, number: number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
}
let clientNumber = -1;
function acceptClientSocket(code: BusinessError, number: number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth clientSocket Number: ${number}`);
    // 获取的clientNumber用作服务端后续读/写操作socket的id。
    clientNumber = number;
}
try {
    bluetoothManager.sppAccept(serverNumber, acceptClientSocket);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.sppConnect(deprecated)

sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void

客户端向远端设备发起spp连接。


从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppConnect](@ohos.bluetooth.socket (蓝牙socket模块).md#ZH-CN_TOPIC_0000002553201409__socketsppconnect)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| option | SppOption | 是 | spp客户端连接配置参数。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，客户端socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
let sppOption: bluetoothManager.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
try {
    bluetoothManager.sppConnect('XX:XX:XX:XX:XX:XX', sppOption, clientSocket);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.sppCloseServerSocket(deprecated)

sppCloseServerSocket(socket: number): void

关闭服务端监听Socket，入参socket由sppListen接口返回。


从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppCloseServerSocket](@ohos.bluetooth.socket (蓝牙socket模块).md#ZH-CN_TOPIC_0000002553201409__socketsppcloseserversocket)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socket | number | 是 | 服务端监听socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code: BusinessError, number: number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
}
try {
    bluetoothManager.sppCloseServerSocket(serverNumber);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.sppCloseClientSocket(deprecated)

sppCloseClientSocket(socket: number): void

关闭客户端socket，入参socket由sppAccept或sppConnect接口获取。


从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppCloseClientSocket](@ohos.bluetooth.socket (蓝牙socket模块).md#ZH-CN_TOPIC_0000002553201409__socketsppcloseclientsocket)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socket | number | 是 | 客户端socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
try {
    bluetoothManager.sppCloseClientSocket(clientNumber);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.sppWrite(deprecated)

sppWrite(clientSocket: number, data: ArrayBuffer): void

通过socket向远端发送数据，入参clientSocket由sppAccept或sppConnect接口获取。


从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppWrite](@ohos.bluetooth.socket (蓝牙socket模块).md#ZH-CN_TOPIC_0000002553201409__socketsppwrite)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | number | 是 | 客户端socket的id。 |
| data | ArrayBuffer | 是 | 写入的数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
let arrayBuffer = new ArrayBuffer(8);
let data = new Uint8Array(arrayBuffer);
data[0] = 123;
try {
    bluetoothManager.sppWrite(clientNumber, arrayBuffer);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.on('sppRead')(deprecated)

on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void

订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。


从API version 9开始支持，从API version 10开始废弃。建议使用[socket.on('sppRead')](@ohos.bluetooth.socket (蓝牙socket模块).md#ZH-CN_TOPIC_0000002553201409__socketonsppread)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"sppRead"字符串，表示spp读请求事件。 |
| clientSocket | number | 是 | 客户端socket的id。 |
| callback | Callback<ArrayBuffer> | 是 | 表示回调函数的入参，读取到的数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
function dataRead(dataBuffer: ArrayBuffer) {
  let data = new Uint8Array(dataBuffer);
  console.info(`bluetooth data is: ${data[0]}`);
}
try {
    bluetoothManager.on('sppRead', clientNumber, dataRead);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.off('sppRead')(deprecated)

off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void

取消订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。


从API version 9开始支持，从API version 10开始废弃。建议使用[socket.off('sppRead')](@ohos.bluetooth.socket (蓝牙socket模块).md#ZH-CN_TOPIC_0000002553201409__socketoffsppread)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"sppRead"字符串，表示spp读请求事件。 |
| clientSocket | number | 是 | 客户端Socket的id。 |
| callback | Callback<ArrayBuffer> | 否 | 表示取消订阅spp读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code: BusinessError, number: number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
try {
    bluetoothManager.off('sppRead', clientNumber);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### bluetoothManager.getProfileInstance(deprecated)

getProfileInstance(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile | HidHostProfile | PanProfile

通过ProfileId，获取profile的对象实例，API9新增了HidHostProfile，PanProfile。


从API version 9开始支持，从API version 10开始废弃。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profileId | ProfileId | 是 | 表示profile的枚举值，例如：PROFILE_A2DP_SOURCE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| A2dpSourceProfile | HandsFreeAudioGatewayProfile | HidHostProfile | PanProfile | 对应的profile的对象实例，当前支持A2dpSourceProfile/HandsFreeAudioGatewayProfile/HidHostProfile/PanProfile。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### BLE

BLE模块提供了对蓝牙操作和管理的方法。

#### createGattServer(deprecated)

createGattServer(): GattServer

创建一个可使用的GattServer实例。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.createGattServer](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__blecreategattserver)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| GattServer | server端类，使用server端方法之前需要创建该类的实例进行操作。 |

**示例：**

```ets
let gattServer: bluetoothManager.GattServer  = bluetoothManager.BLE.createGattServer();
```

#### createGattClientDevice(deprecated)

createGattClientDevice(deviceId: string): GattClientDevice

创建一个可使用的GattClientDevice实例。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.createGattClientDevice](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__blecreategattclientdevice)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| GattClientDevice | client端类，使用client端方法之前需要创建该类的实例进行操作。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let device: bluetoothManager.GattClientDevice = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### getConnectedBLEDevices(deprecated)

getConnectedBLEDevices(): Array<string>

获取和当前设备连接的BLE设备。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.getConnectedBLEDevices](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__blegetconnectedbledevices)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回当前设备作为Server端时连接BLE设备地址集合。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let result: Array<string>  = bluetoothManager.BLE.getConnectedBLEDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### startBLEScan(deprecated)

startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void

发起BLE扫描流程。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.startBLEScan](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__blestartblescan)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filters | Array<ScanFilter> | 是 | 表示扫描结果过滤策略集合，如果不使用过滤的方式，该参数设置为null。 |
| options | ScanOptions | 否 | 表示扫描的参数配置，可选参数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
    console.info('BLE scan device find result = '+ JSON.stringify(data));
}
try {
    bluetoothManager.BLE.on("BLEDeviceFind", onReceiveEvent);
    let scanfilter: bluetoothManager.ScanFilter = {
        deviceId:"XX:XX:XX:XX:XX:XX",
        name:"test",
        serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
    };
    let scanoptions: bluetoothManager.ScanOptions = {
        interval: 500,
        dutyMode: bluetoothManager.ScanDuty.SCAN_MODE_LOW_POWER,
        matchMode: bluetoothManager.MatchMode.MATCH_MODE_AGGRESSIVE,
    }
    bluetoothManager.BLE.startBLEScan([scanfilter], scanoptions);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### stopBLEScan(deprecated)

stopBLEScan(): void

停止BLE扫描流程。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.stopBLEScan](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__blestopblescan)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    bluetoothManager.BLE.stopBLEScan();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### on('BLEDeviceFind')(deprecated)

on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void

订阅BLE设备发现上报事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.on('BLEDeviceFind')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__bleonbledevicefind)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | Callback<Array<ScanResult>> | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.BLE.on('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### off('BLEDeviceFind')(deprecated)

off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void

取消订阅BLE设备发现上报事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.off('BLEDeviceFind')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__bleoffbledevicefind)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | Callback<Array<ScanResult>> | 否 | 表示取消订阅BLE设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    bluetoothManager.BLE.on('BLEDeviceFind', onReceiveEvent);
    bluetoothManager.BLE.off('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### BaseProfile

profile基类。

#### getConnectionDevices(deprecated)

getConnectionDevices(): Array<string>

获取已连接设备列表。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.getConnectedDevices](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__baseprofilegetconnecteddevices)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回已连接设备的地址列表。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    let retArray: Array<string> = a2dpSrc.getConnectionDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### getDeviceState(deprecated)

getDeviceState(device: string): ProfileConnectionState

获取设备profile的连接状态。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.getConnectionState](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__baseprofilegetconnectionstate)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ProfileConnectionState | 返回profile的连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    let ret: bluetoothManager.ProfileConnectionState = a2dpSrc.getDeviceState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### A2dpSourceProfile

使用A2dpSourceProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。


从API version 9开始支持，从API version 10开始废弃。建议使用[a2dp.A2dpSourceProfile](@ohos.bluetooth.a2dp (蓝牙a2dp模块).md#ZH-CN_TOPIC_0000002553361363__a2dpsourceprofile)替代。

#### connect(deprecated)

connect(device: string): void

发起设备的A2dp服务连接请求。

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    a2dpSrc.connect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### disconnect(deprecated)

disconnect(device: string): void

断开设备的a2dp服务连接。

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    a2dpSrc.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#ZH-CN_TOPIC_0000002522241456__statechangeparamdeprecated)>): void

订阅a2dp连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<StateChangeParam> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#ZH-CN_TOPIC_0000002522241456__statechangeparamdeprecated)>): void

取消订阅a2dp连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<StateChangeParam> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
a2dpSrc.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### getPlayingState(deprecated)

getPlayingState(device: string): PlayingState

获取设备的播放状态。


从API version 9开始支持，从API version 10开始废弃。建议使用[getPlayingState](@ohos.bluetooth.a2dp (蓝牙a2dp模块).md#ZH-CN_TOPIC_0000002553361363__getplayingstate)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PlayingState | 远端设备的播放状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
    let state: bluetoothManager.PlayingState  = a2dpSrc.getPlayingState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### HandsFreeAudioGatewayProfile(deprecated)

使用HandsFreeAudioGatewayProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。


从API version 9开始支持，从API version 10开始废弃。建议使用[hfp.HandsFreeAudioGatewayProfile](@ohos.bluetooth.hfp (蓝牙hfp模块).md#ZH-CN_TOPIC_0000002522081446__handsfreeaudiogatewayprofile)替代。

**connect(deprecated)**

connect(device: string): void

连接设备的HFP服务。

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as bluetoothManager.HandsFreeAudioGatewayProfile;
    hfpAg.connect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### disconnect(deprecated)

disconnect(device: string): void

断开连接设备的HFP服务。

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as bluetoothManager.HandsFreeAudioGatewayProfile;
    hfpAg.disconnect('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#ZH-CN_TOPIC_0000002522241456__statechangeparamdeprecated)>): void

订阅HFP连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<StateChangeParam> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
try {
let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as
  bluetoothManager.HandsFreeAudioGatewayProfile;
hfpAg.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#ZH-CN_TOPIC_0000002522241456__statechangeparamdeprecated)>): void

取消订阅HFP连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<StateChangeParam> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 示例： |  |

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
try {
let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as
  bluetoothManager.HandsFreeAudioGatewayProfile;
hfpAg.on('connectionStateChange', onReceiveEvent);
hfpAg.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### HidHostProfile(deprecated)

使用HidHostProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

#### on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#ZH-CN_TOPIC_0000002522241456__statechangeparamdeprecated)>): void

订阅HidHost连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<StateChangeParam> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hidHost state = '+ JSON.stringify(data));
}
try {
let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST) as bluetoothManager.HidHostProfile;
hidHost.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#ZH-CN_TOPIC_0000002522241456__statechangeparamdeprecated)>): void

取消订阅HidHost连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<StateChangeParam> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('hidHost state = '+ JSON.stringify(data));
}
try {
let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST) as bluetoothManager.HidHostProfile;
hidHost.on('connectionStateChange', onReceiveEvent);
hidHost.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### PanProfile

使用PanProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。


从API version 9开始支持，从API version 10开始废弃。建议使用[pan.createPanProfile](@ohos.bluetooth.pan (蓝牙pan模块).md#ZH-CN_TOPIC_0000002522241440__pancreatepanprofile)替代。

#### on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](#ZH-CN_TOPIC_0000002522241456__statechangeparamdeprecated)>): void

订阅Pan连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<StateChangeParam> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('pan state = '+ JSON.stringify(data));
}
try {
let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_PAN_NETWORK) as bluetoothManager.PanProfile;
panProfile.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#ZH-CN_TOPIC_0000002522241456__statechangeparamdeprecated)>): void

取消订阅Pan连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<StateChangeParam> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
    console.info('pan state = '+ JSON.stringify(data));
}
try {
let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_PAN_NETWORK) as bluetoothManager.PanProfile;
panProfile.on('connectionStateChange', onReceiveEvent);
panProfile.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### GattServer

server端类，使用server端方法之前需要创建该类的实例进行操作，通过createGattServer()方法构造此实例。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__gattserver)替代。

#### startAdvertising(deprecated)

startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void

开始发送BLE广播。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.startAdvertising](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__blestartadvertising)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| setting | AdvertiseSetting | 是 | BLE广播的相关参数。 |
| advData | AdvertiseData | 是 | BLE广播包内容。 |
| advResponse | AdvertiseData | 否 | BLE回复扫描请求回复响应。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
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
let gattServer = bluetoothManager.BLE.createGattServer();
try {
    let setting: bluetoothManager.AdvertiseSetting = {
        interval:150,
        txPower:0,
        connectable:true,
    };
    let manufactureDataUnit: bluetoothManager.ManufactureData = {
        manufactureId:4567,
        manufactureValue:manufactureValueBuffer.buffer
    };
    let serviceDataUnit: bluetoothManager.ServiceData = {
        serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
        serviceValue:serviceValueBuffer.buffer
    };
    let advData: bluetoothManager.AdvertiseData = {
        serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
        manufactureData:[manufactureDataUnit],
        serviceData:[serviceDataUnit],
    };
    let advResponse: bluetoothManager.AdvertiseData = {
        serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
        manufactureData:[manufactureDataUnit],
        serviceData:[serviceDataUnit],
    };
    gattServer.startAdvertising(setting, advData ,advResponse);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### stopAdvertising(deprecated)

stopAdvertising(): void

停止发送BLE广播。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.stopAdvertising](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__blestopadvertising)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let server = bluetoothManager.BLE.createGattServer();
try {
    server.stopAdvertising();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### addService(deprecated)

addService(service: GattService): void

server端添加服务。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#addService](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__addservice)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| service | GattService | 是 | 服务端的service数据。BLE广播的相关参数 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
// 创建descriptors
let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;

// 创建characteristics
let characteristics: Array<bluetoothManager.BLECharacteristic> = [];
let arrayBufferC = new ArrayBuffer(8);
let cccV = new Uint8Array(arrayBufferC);
cccV[0] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let characteristicN: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
characteristics[0] = characteristic;

// 创建gattService
let gattService: bluetoothManager.GattService = {serviceUuid:'00001810-0000-1000-8000-00805F9B34FB', isPrimary: true, characteristics:characteristics, includeServices:[]};

let gattServer  = bluetoothManager.BLE.createGattServer();
try {
    gattServer.addService(gattService);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### removeService(deprecated)

removeService(serviceUuid: string): void

删除已添加的服务。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#removeService](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__removeservice)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serviceUuid | string | 是 | service的UUID，例如“00001810-0000-1000-8000-00805F9B34FB”。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let server = bluetoothManager.BLE.createGattServer();
try {
    server.removeService('00001810-0000-1000-8000-00805F9B34FB');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### close(deprecated)

close(): void

关闭服务端功能，去注册server在协议栈的注册，调用该接口后[GattServer](#ZH-CN_TOPIC_0000002522241456__gattserver)实例将不能再使用。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#close](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__close)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let server = bluetoothManager.BLE.createGattServer();
try {
    server.close();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### notifyCharacteristicChanged(deprecated)

notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): void

server端特征值发生变化时，主动通知已连接的client设备。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#notifyCharacteristicChanged](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__notifycharacteristicchanged)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 接收通知的client端设备地址，例如“XX:XX:XX:XX:XX:XX”。 |
| notifyCharacteristic | NotifyCharacteristic | 是 | 通知的特征值数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
// 创建descriptors
let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;
let arrayBufferC = new ArrayBuffer(8);
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let notifyCharacteristic: bluetoothManager.NotifyCharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: characteristic.characteristicValue, confirm: false};
let server = bluetoothManager.BLE.createGattServer();
try {
    server.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacteristic);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### sendResponse(deprecated)

sendResponse(serverResponse: ServerResponse): void

server端回复client端的读写请求。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#sendResponse](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__sendresponse)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serverResponse | ServerResponse | 是 | server端回复的响应数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
/* send response */
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue[0] = 1;
let serverResponse: bluetoothManager.ServerResponse = {
    deviceId: 'XX:XX:XX:XX:XX:XX',
    transId: 0,
    status: 0,
    offset: 0,
    value: arrayBufferCCC,
};

let gattServer = bluetoothManager.BLE.createGattServer();
try {
    gattServer.sendResponse(serverResponse);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### on('characteristicRead')(deprecated)

on(type: 'characteristicRead', callback: Callback<CharacteristicReadRequest>): void

server端订阅特征值读请求事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('characteristicRead')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__oncharacteristicread)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicRead"字符串，表示特征值读请求事件。 |
| callback | Callback<CharacteristicReadRequest> | 是 | 表示回调函数的入参，client端发送的读请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue[0] = 1;
function ReadCharacteristicReq(characteristicReadRequest: bluetoothManager.CharacteristicReadRequest) {
    let deviceId: string = characteristicReadRequest.deviceId;
    let transId: number = characteristicReadRequest.transId;
    let offset: number = characteristicReadRequest.offset;
    let characteristicUuid: string = characteristicReadRequest.characteristicUuid;

    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferCCC};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
    }

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("characteristicRead", ReadCharacteristicReq);
```

#### off('characteristicRead')(deprecated)

off(type: 'characteristicRead', callback?: Callback<CharacteristicReadRequest>): void

server端取消订阅特征值读请求事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('characteristicRead')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__offcharacteristicread)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicRead"字符串，表示特征值读请求事件。 |
| callback | Callback<CharacteristicReadRequest> | 否 | 表示取消订阅特征值读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("characteristicRead");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### on('characteristicWrite')(deprecated)

on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteRequest>): void

server端订阅特征值写请求事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('characteristicWrite')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__oncharacteristicwrite)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicWrite"字符串，表示特征值写请求事件。 |
| callback | Callback<CharacteristicWriteRequest> | 是 | 表示回调函数的入参，client端发送的写请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
function WriteCharacteristicReq(characteristicWriteRequest: bluetoothManager.CharacteristicWriteRequest) {
    let deviceId: string = characteristicWriteRequest.deviceId;
    let transId: number = characteristicWriteRequest.transId;
    let offset: number = characteristicWriteRequest.offset;
    let isPrep: boolean = characteristicWriteRequest.isPrep;
    let needRsp: boolean = characteristicWriteRequest.needRsp;
    let value: Uint8Array =  new Uint8Array(characteristicWriteRequest.value);
    let characteristicUuid: string = characteristicWriteRequest.characteristicUuid;

    cccValue[0] = value[0];
    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferCCC};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("characteristicWrite", WriteCharacteristicReq);
```

#### off('characteristicWrite')(deprecated)

off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteRequest>): void

server端取消订阅特征值写请求事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('characteristicWrite')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__offcharacteristicwrite)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicWrite"字符串，表示特征值写请求事件。 |
| callback | Callback<CharacteristicWriteRequest> | 否 | 表示取消订阅特征值写请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("characteristicWrite");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### on('descriptorRead')(deprecated)

on(type: 'descriptorRead', callback: Callback<DescriptorReadRequest>): void

server端订阅描述符读请求事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('descriptorRead')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__ondescriptorread)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorRead"字符串，表示描述符读请求事件。 |
| callback | Callback<DescriptorReadRequest> | 是 | 表示回调函数的入参，client端发送的读请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
descValue[0] = 1;
function ReadDescriptorReq(descriptorReadRequest: bluetoothManager.DescriptorReadRequest) {
    let deviceId: string = descriptorReadRequest.deviceId;
    let transId: number = descriptorReadRequest.transId;
    let offset: number = descriptorReadRequest.offset;
    let descriptorUuid: string = descriptorReadRequest.descriptorUuid;

    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("descriptorRead", ReadDescriptorReq);
```

#### off('descriptorRead')(deprecated)

off(type: 'descriptorRead', callback?: Callback<DescriptorReadRequest>): void

server端取消订阅描述符读请求事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('descriptorRead')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__offdescriptorread)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorRead"字符串，表示描述符读请求事件。 |
| callback | Callback<DescriptorReadRequest> | 否 | 表示取消订阅描述符读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("descriptorRead");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### on('descriptorWrite')(deprecated)

on(type: 'descriptorWrite', callback: Callback<DescriptorWriteRequest>): void

server端订阅描述符写请求事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('descriptorWrite')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__ondescriptorwrite)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorWrite"字符串，表示描述符写请求事件。 |
| callback | Callback<DescriptorWriteRequest> | 是 | 表示回调函数的入参，client端发送的写请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
function WriteDescriptorReq(descriptorWriteRequest: bluetoothManager.DescriptorWriteRequest) {
    let deviceId: string = descriptorWriteRequest.deviceId;
    let transId: number = descriptorWriteRequest.transId;
    let offset: number = descriptorWriteRequest.offset;
    let isPrep: boolean = descriptorWriteRequest.isPrep;
    let needRsp: boolean = descriptorWriteRequest.needRsp;
    let value: Uint8Array = new Uint8Array(descriptorWriteRequest.value);
    let descriptorUuid: string = descriptorWriteRequest.descriptorUuid;

    descValue[0] = value[0];
    let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

    try {
        gattServer.sendResponse(serverResponse);
    } catch (err) {
        console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }

let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("descriptorWrite", WriteDescriptorReq);
```

#### off('descriptorWrite')(deprecated)

off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteRequest>): void

server端取消订阅描述符写请求事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('descriptorWrite')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__offdescriptorwrite)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorWrite"字符串，表示描述符写请求事件。 |
| callback | Callback<DescriptorWriteRequest> | 否 | 表示取消订阅描述符写请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("descriptorWrite");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### on('connectStateChange')(deprecated)

on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void

server端订阅BLE连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('connectionStateChange')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__onconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectStateChange"字符串，表示BLE连接状态变化事件。 |
| callback | Callback<BLEConnectChangedState> | 是 | 表示回调函数的入参，连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function Connected(BLEConnectChangedState: bluetoothManager.BLEConnectChangedState) {
  let deviceId: string = BLEConnectChangedState.deviceId;
  let status: bluetoothManager.ProfileConnectionState  = BLEConnectChangedState.state;
}
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.on("connectStateChange", Connected);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### off('connectStateChange')(deprecated)

off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void

server端取消订阅BLE连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('connectionStateChange')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__offconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectStateChange"字符串，表示BLE连接状态变化事件。 |
| callback | Callback<BLEConnectChangedState> | 否 | 表示取消订阅BLE连接状态变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
let gattServer = bluetoothManager.BLE.createGattServer();
gattServer.off("connectStateChange");
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### GattClientDevice

client端类，使用client端方法之前需要创建该类的实例进行操作，通过createGattClientDevice(deviceId: string)方法构造此实例。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__gattclientdevice)替代。

#### connect(deprecated)

connect(): void

client端发起连接远端蓝牙低功耗设备。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#connect](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__connect)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.connect();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### disconnect(deprecated)

disconnect(): void

client端断开与远端蓝牙低功耗设备的连接。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#disconnect](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__disconnect)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.disconnect();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### close(deprecated)

close(): void

关闭客户端功能，注销client在协议栈的注册，调用该接口后[GattClientDevice](#ZH-CN_TOPIC_0000002522241456__gattclientdevice)实例将不能再使用。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#close](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__close)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.close();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### getServices(deprecated)

getServices(callback: AsyncCallback<Array<GattService>>): void

client端获取蓝牙低功耗设备的所有服务，即服务发现。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getServices](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__getservices)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<GattService>> | 是 | client进行服务发现，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
// callback 模式
function getServices(code: BusinessError, gattServices: Array<bluetoothManager.GattService>) {
  if (code.code == 0) {
      let services: Array<bluetoothManager.GattService> = gattServices;
      console.info(`bluetooth code is ${code.code}`);
      console.info(`bluetooth services size is ${services.length}`);

      for (let i = 0; i < services.length; i++) {
        console.info(`bluetooth serviceUuid is ${services[i].serviceUuid}`);
}

try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.connect();
    device.getServices(getServices);
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

#### getServices(deprecated)

getServices(): Promise<Array<GattService>>

client端获取蓝牙低功耗设备的所有服务，即服务发现。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getServices](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__getservices-1)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<GattService>> | client进行服务发现，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
// Promise 模式
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.connect();
    device.getServices().then(result => {
        console.info("getServices successfully:" + JSON.stringify(result));
    });
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void

client端读取蓝牙低功耗设备特定服务的特征值。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readCharacteristicValue](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__readcharacteristicvalue)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | BLECharacteristic | 是 | 待读取的特征值。 |
| callback | AsyncCallback<BLECharacteristic> | 是 | client读取特征值，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
function readCcc(code: BusinessError, BLECharacteristic: bluetoothManager.BLECharacteristic) {
    if (code.code != 0) {
        return;
    }
    console.info(`bluetooth characteristic uuid: ${BLECharacteristic.characteristicUuid}`);
    let value = new Uint8Array(BLECharacteristic.characteristicValue);
    console.info(`value length: ${value.length}`);
}

let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};

try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readCharacteristicValue(characteristic, readCcc);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>

client端读取蓝牙低功耗设备特定服务的特征值。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readCharacteristicValue](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__readcharacteristicvalue-1)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | BLECharacteristic | 是 | 待读取的特征值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<BLECharacteristic> | client读取特征值，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};

try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readCharacteristicValue(characteristic);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void

client端读取蓝牙低功耗设备特定的特征包含的描述符。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readDescriptorValue](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__readdescriptorvalue)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | BLEDescriptor | 是 | 待读取的描述符。 |
| callback | AsyncCallback<BLEDescriptor> | 是 | client读取描述符，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
function readDesc(code: BusinessError, BLEDescriptor: bluetoothManager.BLEDescriptor) {
    if (code.code != 0) {
        return;
    }
    console.info(`bluetooth descriptor uuid: ${BLEDescriptor.descriptorUuid}`);
    let value = new Uint8Array(BLEDescriptor.descriptorValue);
}

let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {
    serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
    descriptorValue: bufferDesc
};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readDescriptorValue(descriptor, readDesc);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>

client端读取蓝牙低功耗设备特定的特征包含的描述符。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readDescriptorValue](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__readdescriptorvalue-1)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | BLEDescriptor | 是 | 待读取的描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<BLEDescriptor> | client读取描述符，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {
    serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
    descriptorValue: bufferDesc
};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.readDescriptorValue(descriptor);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### writeCharacteristicValue(deprecated)

writeCharacteristicValue(characteristic: BLECharacteristic): void

client端向低功耗蓝牙设备写入特定的特征值。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#writeCharacteristicValue](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__writecharacteristicvalue)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | BLECharacteristic | 是 | 蓝牙设备特征对应的二进制值及其它参数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901001 | Write forbidden. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.writeCharacteristicValue(characteristic);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### writeDescriptorValue(deprecated)

writeDescriptorValue(descriptor: BLEDescriptor): void

client端向低功耗蓝牙设备特定的描述符写入二进制数据。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#writeDescriptorValue](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__writedescriptorvalue)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | BLEDescriptor | 是 | 蓝牙设备描述符的二进制值及其它参数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901001 | Write forbidden. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 22;
let descriptor: bluetoothManager.BLEDescriptor = {
    serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
    descriptorValue: bufferDesc
};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.writeDescriptorValue(descriptor);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### setBLEMtuSize(deprecated)

setBLEMtuSize(mtu: number): void

client协商远端蓝牙低功耗设备的最大传输单元（Maximum Transmission Unit, MTU），调用[connect](#ZH-CN_TOPIC_0000002522241456__connectdeprecated-1)接口连接成功后才能使用。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#setBLEMtuSize](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__setblemtusize)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mtu | number | 是 | 设置范围为22~512字节。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.setBLEMtuSize(128);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### setNotifyCharacteristicChanged(deprecated)

setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): void

向服务端发送设置通知此特征值请求。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#setCharacteristicChangeNotification](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__setcharacteristicchangenotification)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | BLECharacteristic | 是 | 蓝牙低功耗特征。 |
| enable | boolean | 是 | 启用接收notify设置为true，否则设置为false。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
// 创建descriptors
let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
    characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
    characteristicValue: bufferCCC, descriptors:descriptors};
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.setNotifyCharacteristicChanged(characteristic, false);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### on('BLECharacteristicChange')(deprecated)

on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void

订阅蓝牙低功耗设备的特征值变化事件。需要先调用setNotifyCharacteristicChanged接口才能接收server端的通知。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#on('BLECharacteristicChange')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__onblecharacteristicchange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLECharacteristicChange"字符串，表示特征值变化事件。 |
| callback | Callback<BLECharacteristic> | 是 | 表示蓝牙低功耗设备的特征值变化事件的回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
function CharacteristicChange(characteristicChangeReq: ble.BLECharacteristic) {
    let serviceUuid: string = characteristicChangeReq.serviceUuid;
    let characteristicUuid: string = characteristicChangeReq.characteristicUuid;
    let value: Uint8Array = new Uint8Array(characteristicChangeReq.characteristicValue);
}
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.on('BLECharacteristicChange', CharacteristicChange);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### off('BLECharacteristicChange')(deprecated)

off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void

取消订阅蓝牙低功耗设备的特征值变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#off('BLECharacteristicChange')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__offblecharacteristicchange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLECharacteristicChange"字符串，表示特征值变化事件。 |
| callback | Callback<BLECharacteristic> | 否 | 表示取消订阅蓝牙低功耗设备的特征值变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.off('BLECharacteristicChange');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### on('BLEConnectionStateChange')(deprecated)

on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void

client端订阅蓝牙低功耗设备的连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#on('BLEConnectionStateChange')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__onbleconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEConnectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<BLEConnectChangedState> | 是 | 表示连接状态，已连接或断开。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
function ConnectStateChanged(state: bluetoothManager.BLEConnectChangedState) {
    console.info('bluetooth connect state changed');
    let connectState: bluetoothManager.ProfileConnectionState = state.state;
}
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.on('BLEConnectionStateChange', ConnectStateChanged);
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### off('BLEConnectionStateChange')(deprecated)

off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void

取消订阅蓝牙低功耗设备的连接状态变化事件。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#off('BLEConnectionStateChange')](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__offbleconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEConnectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<BLEConnectChangedState> | 否 | 表示取消订阅蓝牙低功耗设备的连接状态变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
try {
    let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
    device.off('BLEConnectionStateChange');
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### getDeviceName(deprecated)

getDeviceName(callback: AsyncCallback<string>): void

client获取远端蓝牙低功耗设备名。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getDeviceName](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__getdevicename)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | client获取对端server设备名，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
// callback
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    gattClient.connect();
    let deviceName = gattClient.getDeviceName((err, data)=> {
        console.info('device name err ' + JSON.stringify(err));
        console.info('device name' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### getDeviceName(deprecated)

getDeviceName(): Promise<string>

client获取远端蓝牙低功耗设备名。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getDeviceName](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__getdevicename-1)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | client获取对端server设备名，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
// promise
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    gattClient.connect();
    let deviceName = gattClient.getDeviceName().then((data) => {
        console.info('device name' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### getRssiValue(deprecated)

getRssiValue(callback: AsyncCallback<number>): void

client获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用[connect](#ZH-CN_TOPIC_0000002522241456__connectdeprecated-1)接口连接成功后才能使用。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getRssiValue](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__getrssivalue)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 返回信号强度，单位 dBm，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
// callback
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    gattClient.connect();
    let rssi = gattClient.getRssiValue((err: BusinessError, data: number)=> {
        console.info('rssi err ' + JSON.stringify(err));
        console.info('rssi value' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### getRssiValue(deprecated)

getRssiValue(): Promise<number>

client获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用[connect](#ZH-CN_TOPIC_0000002522241456__connectdeprecated-1)接口连接成功后才能使用。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getRssiValue](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__getrssivalue-1)替代。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回信号强度，单位 dBm，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```ets
import { BusinessError } from '@ohos.base';
// promise
try {
    let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
    let rssi = gattClient.getRssiValue().then((data: number) => {
        console.info('rssi' + JSON.stringify(data));
    })
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### ScanMode(deprecated)

枚举，扫描模式。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.ScanMode](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__scanmode)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN_MODE_NONE | 0 | 没有扫描模式。 |
| SCAN_MODE_CONNECTABLE | 1 | 可连接扫描模式。 |
| SCAN_MODE_GENERAL_DISCOVERABLE | 2 | general发现模式。 |
| SCAN_MODE_LIMITED_DISCOVERABLE | 3 | limited发现模式。 |
| SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE | 4 | 可连接general发现模式。 |
| SCAN_MODE_CONNECTABLE_LIMITED_DISCOVERABLE | 5 | 可连接limited发现模式。 |

#### BondState(deprecated)

枚举，配对状态。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.BondState](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__bondstate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BOND_STATE_INVALID | 0 | 无效的配对。 |
| BOND_STATE_BONDING | 1 | 正在配对。 |
| BOND_STATE_BONDED | 2 | 已配对。 |

#### SppOption(deprecated)

描述spp的配置参数。


从API version 9开始支持，从API version 10开始废弃。建议使用[socket.SppOption](@ohos.bluetooth.socket (蓝牙socket模块).md#ZH-CN_TOPIC_0000002553201409__sppoptions)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uuid | string | 否 | 否 | spp单据的uuid。 |
| secure | boolean | 否 | 否 | 是否是安全通道。 |
| type | SppType | 否 | 否 | Spp链路类型。 |

#### SppType(deprecated)

枚举，Spp链路类型。


从API version 9开始支持，从API version 10开始废弃。建议使用[socket.SppType](@ohos.bluetooth.socket (蓝牙socket模块).md#ZH-CN_TOPIC_0000002553201409__spptype)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SPP_RFCOMM | 0 | 表示rfcomm链路类型。 |

#### GattService(deprecated)

描述service的接口参数定义。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattService](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__gattservice)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| isPrimary | boolean | 否 | 否 | 如果是主服务设置为true，否则设置为false。 |
| characteristics | Array<BLECharacteristic> | 否 | 否 | 当前服务包含的特征列表。 |
| includeServices | Array<GattService> | 否 | 是 | 当前服务依赖的其它服务。 |

#### BLECharacteristic(deprecated)

描述characteristic的接口参数定义。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.BLECharacteristic](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__blecharacteristic)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征对应的二进制值。 |
| descriptors | Array<BLEDescriptor> | 否 | 否 | 特定特征的描述符列表。 |

#### BLEDescriptor(deprecated)

描述descriptor的接口参数定义。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.BLEDescriptor](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__bledescriptor)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| descriptorUuid | string | 否 | 否 | 描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| descriptorValue | ArrayBuffer | 否 | 否 | 描述符对应的二进制值。 |

#### NotifyCharacteristic(deprecated)

描述server端特征值变化时发送的特征通知参数定义。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.NotifyCharacteristic](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__notifycharacteristic)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征对应的二进制值。 |
| confirm | boolean | 否 | 否 | 如果是notification则对端回复确认设置为true，如果是indication则对端不需要回复确认设置为false。 |

#### CharacteristicReadRequest(deprecated)

描述server端订阅后收到的特征值读请求事件参数结构。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.CharacteristicReadRequest](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__characteristicreadrequest)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示发送特征值读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示读特征值数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### CharacteristicWriteRequest(deprecated)

描述server端订阅后收到的特征值写请求事件参数结构。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.CharacteristicWriteRequest](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__characteristicwriterequest)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示发送特征值写请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示写请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示写特征值数据的起始位置。例如：k表示从第k个字节开始写，server端回复响应时需填写相同的offset。 |
| isPrep | boolean | 否 | 否 | 表示写请求是否立即执行。true表示立即执行。 |
| needRsp | boolean | 否 | 否 | 表示是否要给client端回复响应。true表示需要回复。 |
| value | ArrayBuffer | 否 | 否 | 表示写入的描述符二进制数据。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### DescriptorReadRequest(deprecated)

描述server端订阅后收到的描述符读请求事件参数结构。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.DescriptorReadRequest](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__descriptorreadrequest)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示发送描述符读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示读描述符数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。 |
| descriptorUuid | string | 否 | 否 | 表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### DescriptorWriteRequest(deprecated)

描述server端订阅后收到的描述符写请求事件参数结构。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.DescriptorWriteRequest](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__descriptorwriterequest)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示发送描述符写请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示写请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示写描述符数据的起始位置。例如：k表示从第k个字节开始写，server端回复响应时需填写相同的offset。 |
| isPrep | boolean | 否 | 否 | 表示写请求是否立即执行。 |
| needRsp | boolean | 否 | 否 | 表示是否要给client端回复响应。 |
| value | ArrayBuffer | 否 | 否 | 表示写入的描述符二进制数据。 |
| descriptorUuid | string | 否 | 否 | 表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

#### ServerResponse(deprecated)

描述server端回复client端读/写请求的响应参数结构。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ServerResponse](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__serverresponse)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示请求的传输ID，与订阅的读/写请求事件携带的ID保持一致。 |
| status | number | 否 | 否 | 表示响应的状态，设置为0即可，表示正常。 |
| offset | number | 否 | 否 | 表示请求的读/写起始位置，与订阅的读/写请求事件携带的offset保持一致。 |
| value | ArrayBuffer | 否 | 否 | 表示回复响应的二进制数据。 |

#### BLEConnectChangedState(deprecated)

描述Gatt profile连接状态。


从API version 9开始支持，从API version 10开始废弃。建议使用[BLEConnectionChangeState](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__bleconnectionchangestate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| state | ProfileConnectionState | 否 | 否 | 表示BLE连接状态的枚举。 |

#### ProfileConnectionState(deprecated)

枚举，蓝牙设备的profile连接状态。


从API version 9开始支持，从API version 10开始废弃。建议使用[constant.ProfileConnectionState](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002522241438__profileconnectionstate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE_DISCONNECTED | 0 | 表示profile已断连。 |
| STATE_CONNECTING | 1 | 表示profile正在连接。 |
| STATE_CONNECTED | 2 | 表示profile已连接。 |
| STATE_DISCONNECTING | 3 | 表示profile正在断连。 |

#### ScanFilter(deprecated)

扫描过滤参数。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanFilter](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__scanfilter)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 是 | 表示过滤的BLE设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| name | string | 否 | 是 | 表示过滤的BLE设备名。 |
| serviceUuid | string | 否 | 是 | 表示过滤包含该UUID服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| serviceUuidMask | string | 否 | 是 | 表示过滤包含该UUID服务掩码的设备，例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。 |
| serviceSolicitationUuid | string | 否 | 是 | 表示过滤包含该UUID服务请求的设备，例如：00001888-0000-1000-8000-00805F9B34FB。 |
| serviceSolicitationUuidMask | string | 否 | 是 | 表示过滤包含该UUID服务请求掩码的设备，例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。 |
| serviceData | ArrayBuffer | 否 | 是 | 表示过滤包含该服务相关数据的设备，例如：[0x90,0x00,0xF1,0xF2]。 |
| serviceDataMask | ArrayBuffer | 否 | 是 | 表示过滤包含该服务相关数据掩码的设备，例如：[0xFF,0xFF,0xFF,0xFF]。 |
| manufactureId | number | 否 | 是 | 表示过滤包含该制造商ID的设备，例如：0x0006。 |
| manufactureData | ArrayBuffer | 否 | 是 | 表示过滤包含该制造商相关数据的设备，例如：[0x1F,0x2F,0x3F]。 |
| manufactureDataMask | ArrayBuffer | 否 | 是 | 表示过滤包含该制造商相关数据掩码的设备，例如：[0xFF,0xFF,0xFF]。 |

#### ScanOptions(deprecated)

扫描的配置参数。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanOptions](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__scanoptions)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 是 | 表示扫描结果上报延迟时间，默认值为0。 |
| dutyMode | ScanDuty | 否 | 是 | 表示扫描模式，默认值为SCAN_MODE_LOW_POWER。 |
| matchMode | MatchMode | 否 | 是 | 表示硬件的过滤匹配模式，默认值为MATCH_MODE_AGGRESSIVE。 |

#### ScanDuty(deprecated)

枚举，扫描模式。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanDuty](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__scanduty)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN_MODE_LOW_POWER | 0 | 表示低功耗模式，默认值。 |
| SCAN_MODE_BALANCED | 1 | 表示均衡模式。 |
| SCAN_MODE_LOW_LATENCY | 2 | 表示低延迟模式。 |

#### MatchMode(deprecated)

枚举，硬件过滤匹配模式。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.MatchMode](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__matchmode)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MATCH_MODE_AGGRESSIVE | 1 | 表示硬件上报扫描结果门限较低，比如扫描到的功率较低或者一段时间扫描到的次数较少也触发上报，默认值。 |
| MATCH_MODE_STICKY | 2 | 表示硬件上报扫描结果门限较高，更高的功率门限以及扫描到多次才会上报。 |

#### ScanResult(deprecated)

扫描结果上报数据。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanResult](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__scanresult)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示扫描到的设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| rssi | number | 否 | 否 | 表示扫描到的设备的rssi值。 |
| data | ArrayBuffer | 否 | 否 | 表示扫描到的设备发送的广播包。 |

#### BluetoothState(deprecated)

枚举，蓝牙开关状态。


从API version 9开始支持，从API version 10开始废弃。建议使用[access.BluetoothState](@ohos.bluetooth.access (蓝牙access模块).md#ZH-CN_TOPIC_0000002522241436__bluetoothstate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE_OFF | 0 | 表示蓝牙已关闭。 |
| STATE_TURNING_ON | 1 | 表示蓝牙正在打开。 |
| STATE_ON | 2 | 表示蓝牙已打开。 |
| STATE_TURNING_OFF | 3 | 表示蓝牙正在关闭。 |
| STATE_BLE_TURNING_ON | 4 | 表示蓝牙正在打开LE-only模式。 |
| STATE_BLE_ON | 5 | 表示蓝牙正处于LE-only模式。 |
| STATE_BLE_TURNING_OFF | 6 | 表示蓝牙正在关闭LE-only模式。 |

#### AdvertiseSetting(deprecated)

描述蓝牙低功耗设备发送广播的参数。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.AdvertiseSetting](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__advertisesetting)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 是 | 表示广播间隔，最小值设置32个slot表示20ms，最大值设置16384个slot，默认值设置为1600个slot表示1s。 |
| txPower | number | 否 | 是 | 表示发送功率，最小值设置-127，最大值设置1，默认值设置-7，单位dbm。 |
| connectable | boolean | 否 | 是 | 表示是否是可连接广播，默认值设置为true。 |

#### AdvertiseData(deprecated)

描述BLE广播数据包的内容。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.AdvertiseData](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__advertisedata)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuids | Array<string> | 否 | 否 | 表示要广播的服务 UUID 列表。 |
| manufactureData | Array<ManufactureData> | 否 | 否 | 表示要广播的广播的制造商信息列表。 |
| serviceData | Array<ServiceData> | 否 | 否 | 表示要广播的服务数据列表。 |

#### ManufactureData(deprecated)

描述BLE广播数据包的内容。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ManufactureData](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__manufacturedata)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufactureId | number | 否 | 否 | 表示制造商的ID，由蓝牙SIG分配。 |
| manufactureValue | ArrayBuffer | 否 | 否 | 表示制造商发送的制造商数据。 |

#### ServiceData(deprecated)

描述广播包中服务数据内容。


从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ServiceData](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002522081444__servicedata)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务的UUID。 |
| serviceValue | ArrayBuffer | 否 | 否 | 表示服务数据。 |

#### PinRequiredParam(deprecated)

描述配对请求参数。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.PinRequiredParam](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__pinrequiredparam)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示要配对的设备ID。 |
| pinCode | string | 否 | 否 | 表示要配对的密钥。 |

#### BondStateParam(deprecated)

描述配对状态参数。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.BondStateParam](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__bondstateparam)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示要配对的设备ID。 |
| state | BondState | 否 | 否 | 表示配对设备的状态。 |

#### StateChangeParam(deprecated)

描述profile状态改变参数。


从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.StateChangeParam](@ohos.bluetooth.baseProfile (蓝牙baseProfile模块).md#ZH-CN_TOPIC_0000002553201405__statechangeparam)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示蓝牙设备地址。 |
| state | ProfileConnectionState | 否 | 否 | 表示蓝牙设备的profile连接状态。 |

#### DeviceClass(deprecated)

描述蓝牙设备的类别。


从API version 9开始支持，从API version 10开始废弃。建议使用[connection.DeviceClass](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002553361365__deviceclass)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| majorClass | MajorClass | 否 | 否 | 表示蓝牙设备主要类别的枚举。 |
| majorMinorClass | MajorMinorClass | 否 | 否 | 表示主要次要蓝牙设备类别的枚举。 |
| classOfDevice | number | 否 | 否 | 表示设备类别。 |

#### MajorClass(deprecated)

枚举，蓝牙设备主要类别。


从API version 9开始支持，从API version 10开始废弃。建议使用[constant.MajorClass](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002522241438__majorclass)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MAJOR_MISC | 0x0000 | 表示杂项设备。 |
| MAJOR_COMPUTER | 0x0100 | 表示计算机设备。 |
| MAJOR_PHONE | 0x0200 | 表示手机设备。 |
| MAJOR_NETWORKING | 0x0300 | 表示网络设备。 |
| MAJOR_AUDIO_VIDEO | 0x0400 | 表示音频和视频设备。 |
| MAJOR_PERIPHERAL | 0x0500 | 表示外围设备。 |
| MAJOR_IMAGING | 0x0600 | 表示成像设备。 |
| MAJOR_WEARABLE | 0x0700 | 表示可穿戴设备。 |
| MAJOR_TOY | 0x0800 | 表示玩具设备。 |
| MAJOR_HEALTH | 0x0900 | 表示健康设备。 |
| MAJOR_UNCATEGORIZED | 0x1F00 | 表示未分类设备。 |

#### MajorMinorClass(deprecated)

枚举，主要次要蓝牙设备类别。


从API version 9开始支持，从API version 10开始废弃。建议使用[constant.MajorMinorClass](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002522241438__majorminorclass)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPUTER_UNCATEGORIZED | 0x0100 | 表示未分类计算机设备。 |
| COMPUTER_DESKTOP | 0x0104 | 表示台式计算机设备。 |
| COMPUTER_SERVER | 0x0108 | 表示服务器设备。 |
| COMPUTER_LAPTOP | 0x010C | 表示便携式计算机设备。 |
| COMPUTER_HANDHELD_PC_PDA | 0x0110 | 表示手持式计算机设备。 |
| COMPUTER_PALM_SIZE_PC_PDA | 0x0114 | 表示掌上电脑设备。 |
| COMPUTER_WEARABLE | 0x0118 | 表示可穿戴计算机设备。 |
| COMPUTER_TABLET | 0x011C | 表示平板电脑设备。 |
| PHONE_UNCATEGORIZED | 0x0200 | 表示未分类手机设备。 |
| PHONE_CELLULAR | 0x0204 | 表示便携式手机设备。 |
| PHONE_CORDLESS | 0x0208 | 表示无线电话设备。 |
| PHONE_SMART | 0x020C | 表示智能手机设备。 |
| PHONE_MODEM_OR_GATEWAY | 0x0210 | 表示调制解调器或网关手机设备。 |
| PHONE_ISDN | 0x0214 | 表示ISDN手机设备。 |
| NETWORK_FULLY_AVAILABLE | 0x0300 | 表示网络完全可用设备。 |
| NETWORK_1_TO_17_UTILIZED | 0x0320 | 表示使用网络1到17设备。 |
| NETWORK_17_TO_33_UTILIZED | 0x0340 | 表示使用网络17到33设备。 |
| NETWORK_33_TO_50_UTILIZED | 0x0360 | 表示使用网络33到50设备。 |
| NETWORK_60_TO_67_UTILIZED | 0x0380 | 表示使用网络60到67设备。 |
| NETWORK_67_TO_83_UTILIZED | 0x03A0 | 表示使用网络67到83设备。 |
| NETWORK_83_TO_99_UTILIZED | 0x03C0 | 表示使用网络83到99设备。 |
| NETWORK_NO_SERVICE | 0x03E0 | 表示网络无服务设备。 |
| AUDIO_VIDEO_UNCATEGORIZED | 0x0400 | 表示未分类音频视频设备。 |
| AUDIO_VIDEO_WEARABLE_HEADSET | 0x0404 | 表示可穿戴式音频视频设备。 |
| AUDIO_VIDEO_HANDSFREE | 0x0408 | 表示免提音频视频设备。 |
| AUDIO_VIDEO_MICROPHONE | 0x0410 | 表示麦克风音频视频设备。 |
| AUDIO_VIDEO_LOUDSPEAKER | 0x0414 | 表示扬声器音频视频设备。 |
| AUDIO_VIDEO_HEADPHONES | 0x0418 | 表示头戴式音频视频设备。 |
| AUDIO_VIDEO_PORTABLE_AUDIO | 0x041C | 表示便携式音频视频设备。 |
| AUDIO_VIDEO_CAR_AUDIO | 0x0420 | 表示汽车音频视频设备。 |
| AUDIO_VIDEO_SET_TOP_BOX | 0x0424 | 表示机顶盒音频视频设备。 |
| AUDIO_VIDEO_HIFI_AUDIO | 0x0428 | 表示高保真音响设备。 |
| AUDIO_VIDEO_VCR | 0x042C | 表示录像机音频视频设备。 |
| AUDIO_VIDEO_VIDEO_CAMERA | 0x0430 | 表示照相机音频视频设备。 |
| AUDIO_VIDEO_CAMCORDER | 0x0434 | 表示摄像机音频视频设备。 |
| AUDIO_VIDEO_VIDEO_MONITOR | 0x0438 | 表示监视器音频视频设备。 |
| AUDIO_VIDEO_VIDEO_DISPLAY_AND_LOUDSPEAKER | 0x043C | 表示视频显示器和扬声器设备。 |
| AUDIO_VIDEO_VIDEO_CONFERENCING | 0x0440 | 表示音频视频会议设备。 |
| AUDIO_VIDEO_VIDEO_GAMING_TOY | 0x0448 | 表示游戏玩具音频视频设备。 |
| PERIPHERAL_NON_KEYBOARD_NON_POINTING | 0x0500 | 表示非键盘非指向外围设备。 |
| PERIPHERAL_KEYBOARD | 0x0540 | 表示外设键盘设备。 |
| PERIPHERAL_POINTING_DEVICE | 0x0580 | 表示定点装置外围设备。 |
| PERIPHERAL_KEYBOARD_POINTING | 0x05C0 | 表示键盘指向外围设备。 |
| PERIPHERAL_UNCATEGORIZED | 0x0500 | 表示未分类外围设备。 |
| PERIPHERAL_JOYSTICK | 0x0504 | 表示周边操纵杆设备。 |
| PERIPHERAL_GAMEPAD | 0x0508 | 表示周边游戏板设备。 |
| PERIPHERAL_REMOTE_CONTROL | 0x05C0 | 表示远程控制外围设备。 |
| PERIPHERAL_SENSING_DEVICE | 0x0510 | 表示外围传感设备设备。 |
| PERIPHERAL_DIGITIZER_TABLET | 0x0514 | 表示外围数字化仪平板电脑设备。 |
| PERIPHERAL_CARD_READER | 0x0518 | 表示外围读卡器设备。 |
| PERIPHERAL_DIGITAL_PEN | 0x051C | 表示外设数码笔设备。 |
| PERIPHERAL_SCANNER_RFID | 0x0520 | 表示射频识别扫描仪外围设备。 |
| PERIPHERAL_GESTURAL_INPUT | 0x0522 | 表示手势输入外围设备。 |
| IMAGING_UNCATEGORIZED | 0x0600 | 表示未分类的图像设备。 |
| IMAGING_DISPLAY | 0x0610 | 表示图像显示设备。 |
| IMAGING_CAMERA | 0x0620 | 表示成像照相机设备。 |
| IMAGING_SCANNER | 0x0640 | 表示成像扫描仪设备。 |
| IMAGING_PRINTER | 0x0680 | 表示成像打印机设备。 |
| WEARABLE_UNCATEGORIZED | 0x0700 | 表示未分类的可穿戴设备。 |
| WEARABLE_WRIST_WATCH | 0x0704 | 表示可穿戴腕表设备。 |
| WEARABLE_PAGER | 0x0708 | 表示可穿戴寻呼机设备。 |
| WEARABLE_JACKET | 0x070C | 表示夹克可穿戴设备。 |
| WEARABLE_HELMET | 0x0710 | 表示可穿戴头盔设备。 |
| WEARABLE_GLASSES | 0x0714 | 表示可穿戴眼镜设备。 |
| TOY_UNCATEGORIZED | 0x0800 | 表示未分类的玩具设备。 |
| TOY_ROBOT | 0x0804 | 表示玩具机器人设备。 |
| TOY_VEHICLE | 0x0808 | 表示玩具车设备。 |
| TOY_DOLL_ACTION_FIGURE | 0x080C | 表示人形娃娃玩具设备。 |
| TOY_CONTROLLER | 0x0810 | 表示玩具控制器设备。 |
| TOY_GAME | 0x0814 | 表示玩具游戏设备。 |
| HEALTH_UNCATEGORIZED | 0x0900 | 表示未分类健康设备。 |
| HEALTH_BLOOD_PRESSURE | 0x0904 | 表示血压健康设备。 |
| HEALTH_THERMOMETER | 0x0908 | 表示温度计健康设备。 |
| HEALTH_WEIGHING | 0x090C | 表示体重健康设备。 |
| HEALTH_GLUCOSE | 0x0910 | 表示葡萄糖健康设备。 |
| HEALTH_PULSE_OXIMETER | 0x0914 | 表示脉搏血氧仪健康设备。 |
| HEALTH_PULSE_RATE | 0x0918 | 表示脉搏率健康设备。 |
| HEALTH_DATA_DISPLAY | 0x091C | 表示数据显示健康设备。 |
| HEALTH_STEP_COUNTER | 0x0920 | 表示阶梯计数器健康设备。 |
| HEALTH_BODY_COMPOSITION_ANALYZER | 0x0924 | 表示身体成分分析仪健康设备。 |
| HEALTH_PEAK_FLOW_MONITOR | 0x0928 | 表示湿度计健康设备。 |
| HEALTH_MEDICATION_MONITOR | 0x092C | 表示药物监视仪健康设备。 |
| HEALTH_KNEE_PROSTHESIS | 0x0930 | 表示膝盖假肢健康设备。 |
| HEALTH_ANKLE_PROSTHESIS | 0x0934 | 表示脚踝假肢健康设备。 |
| HEALTH_GENERIC_HEALTH_MANAGER | 0x0938 | 表示通用健康管理设备。 |
| HEALTH_PERSONAL_MOBILITY_DEVICE | 0x093C | 表示个人移动健康设备。 |

#### PlayingState(deprecated)

枚举，蓝牙A2DP 播放状态。


从API version 9开始支持，从API version 10开始废弃。建议使用[a2dp.PlayingState](@ohos.bluetooth.a2dp (蓝牙a2dp模块).md#ZH-CN_TOPIC_0000002553361363__playingstate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE_NOT_PLAYING | 0x0000 | 表示未播放。 |
| STATE_PLAYING | 0x0001 | 表示正在播放。 |

#### ProfileId(deprecated)

蓝牙profile枚举，API9新增PROFILE_HID_HOST，PROFILE_PAN_NETWORK。


从API version 9开始支持，从API version 10开始废弃。建议使用[constant.ProfileId](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002522241438__profileid)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROFILE_A2DP_SOURCE | 1 | 表示A2DP profile。 |
| PROFILE_HANDS_FREE_AUDIO_GATEWAY | 4 | 表示HFP profile。 |
| PROFILE_HID_HOST | 6 | 表示HID profile。 |
| PROFILE_PAN_NETWORK | 7 | 表示PAN profile。 |