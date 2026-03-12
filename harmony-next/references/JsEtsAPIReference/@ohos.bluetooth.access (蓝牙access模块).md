# @ohos.bluetooth.access (蓝牙access模块)

本模块提供了打开和关闭蓝牙、获取蓝牙开关状态以及其他相关方法。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { access } from '@kit.ConnectivityKit';
```

#### access.enableBluetooth

enableBluetooth(): void

开启蓝牙。

- 调用该接口时，系统弹出开启蓝牙的对话框，由用户确认是否需要开启蓝牙。如果应用想要感知用户操作对话框的行为，建议使用[access.enableBluetoothAsync](#ZH-CN_TOPIC_0000002497605416__accessenablebluetoothasync20)。
- 蓝牙开关状态结果可通过[access.on('stateChange')](#ZH-CN_TOPIC_0000002497605416__accessonstatechange)的回调函数获取到。
- 建议蓝牙开关状态是[STATE_OFF](#ZH-CN_TOPIC_0000002497605416__bluetoothstate)时，才调用该接口开启蓝牙（可使用[access.getState](#ZH-CN_TOPIC_0000002497605416__accessgetstate)判断当前蓝牙开关状态）。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.enableBluetooth();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### access.enableBluetoothAsync20+

enableBluetoothAsync(): Promise<void>

开启蓝牙。使用Promise异步回调。

- 调用该接口时，系统弹出开启蓝牙的对话框，由用户确认是否需要开启蓝牙。应用可以感知用户操作对话框的行为。
- 蓝牙开关状态结果可通过[access.on('stateChange')](#ZH-CN_TOPIC_0000002497605416__accessonstatechange)的回调函数获取到。
- 建议蓝牙开关状态是[STATE_OFF](#ZH-CN_TOPIC_0000002497605416__bluetoothstate)时，才调用该接口开启蓝牙（可使用[access.getState](#ZH-CN_TOPIC_0000002497605416__accessgetstate)判断当前蓝牙开关状态）。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900013The user does not respond.2900014User refuse the action.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.enableBluetoothAsync().then(() => {
        console.info('enableBluetoothAsync');
    }, (error: BusinessError) => {
        console.error('enableBluetoothAsync: errCode:' + error.code + ',errMessage' + error.message);
    })
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### access.disableBluetooth

disableBluetooth(): void

关闭蓝牙。

- 调用该接口时，系统弹出关闭蓝牙的对话框，由用户确认是否需要关闭蓝牙。如果应用想要感知用户操作对话框的行为，建议使用[access.disableBluetoothAsync](#ZH-CN_TOPIC_0000002497605416__accessdisablebluetoothasync20)。
- 蓝牙开关状态结果可通过[access.on('stateChange')](#ZH-CN_TOPIC_0000002497605416__accessonstatechange)的回调函数获取到。
- 建议蓝牙开关状态是[STATE_ON](#ZH-CN_TOPIC_0000002497605416__bluetoothstate)时，才调用该接口关闭蓝牙（可使用[access.getState](#ZH-CN_TOPIC_0000002497605416__accessgetstate)判断当前蓝牙开关状态）。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.disableBluetooth();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### access.disableBluetoothAsync20+

disableBluetoothAsync(): Promise<void>

关闭蓝牙。使用Promise异步回调。

- 调用该接口时，系统弹出关闭蓝牙的对话框，由用户确认是否需要关闭蓝牙。应用可以感知用户操作对话框的行为。
- 蓝牙开关状态结果可通过[access.on('stateChange')](#ZH-CN_TOPIC_0000002497605416__accessonstatechange)的回调函数获取到。
- 建议蓝牙开关状态是[STATE_ON](#ZH-CN_TOPIC_0000002497605416__bluetoothstate)时，才调用该接口关闭蓝牙（可使用[access.getState](#ZH-CN_TOPIC_0000002497605416__accessgetstate)判断当前蓝牙开关状态）。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900013The user does not respond.2900014User refuse the action.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    access.disableBluetoothAsync().then(() => {
        console.info('disableBluetoothAsync');
    }, (error: BusinessError) => {
        console.error('disableBluetoothAsync: errCode:' + error.code + ',errMessage' + error.message);
    })
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### access.getState

getState(): BluetoothState

获取蓝牙开关状态。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明[BluetoothState](#ZH-CN_TOPIC_0000002497605416__bluetoothstate)表示蓝牙开关状态。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息801Capability not supported.2900001Service stopped.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let state = access.getState();
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### access.on('stateChange')**

on(type: 'stateChange', callback: Callback<BluetoothState>): void

订阅本端蓝牙开关状态变化事件。使用Callback异步回调。从API18开始不再校验ohos.permission.ACCESS_BLUETOOTH权限。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是

事件回调类型，支持的事件为'stateChange'，表示蓝牙开关状态变化事件。

如：当调用[access.enableBluetooth](#ZH-CN_TOPIC_0000002497605416__accessenablebluetooth)或[access.disableBluetooth](#ZH-CN_TOPIC_0000002497605416__accessdisablebluetooth)时，可触发该事件。

callbackCallback<[BluetoothState](#ZH-CN_TOPIC_0000002497605416__bluetoothstate)>是指定订阅的回调函数，会携带蓝牙开关状态。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function onReceiveEvent(data: access.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    access.on('stateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### access.off('stateChange')

off(type: 'stateChange', callback?: Callback<BluetoothState>): void

取消订阅本端蓝牙开关状态变化事件。从API18开始不再校验ohos.permission.ACCESS_BLUETOOTH权限。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'stateChange'，表示蓝牙开关状态变化事件。callbackCallback<[BluetoothState](#ZH-CN_TOPIC_0000002497605416__bluetoothstate)>否

指定取消订阅的回调函数通知。

若传参，则需与[access.on('stateChange')](#ZH-CN_TOPIC_0000002497605416__accessonstatechange)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function onReceiveEvent(data: access.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
try {
    access.on('stateChange', onReceiveEvent);
    access.off('stateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### access.addPersistentDeviceId16+

addPersistentDeviceId(deviceId: string): Promise<void>

持久化存储蓝牙设备的虚拟MAC地址。使用Promise异步回调。

- 应用通过蓝牙相关接口，如扫描等途径获取到的设备地址（虚拟MAC地址）和实际的设备MAC地址不同。蓝牙子系统会保存一个虚拟MAC地址和实际设备MAC地址的映射关系。若应用想长期对该蓝牙设备进行操作使用，建议用此接口持久化存储该设备的虚拟MAC地址，后续可直接使用，该地址映射关系不会再改变。
- 指定持久化存储的虚拟MAC地址需是有效的（可使用[access.isValidRandomDeviceId](#ZH-CN_TOPIC_0000002497605416__accessisvalidrandomdeviceid16)判断）。
- 使用该接口时，开发者应确保该虚拟MAC地址对应的对端蓝牙设备实际地址是保持不变的，若对端设备实际地址发生变化，持久化存储的地址信息将失效，无法继续使用。
- 可调用[access.deletePersistentDeviceId](#ZH-CN_TOPIC_0000002497605416__accessdeletepersistentdeviceid16)删除已持久化存储的虚拟MAC地址。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH 和 ohos.permission.PERSISTENT_BLUETOOTH_PEERS_MAC

**元服务API**：从API version 16开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是

对端设备的虚拟MAC地址，例如："XX:XX:XX:XX:XX:XX"。

该地址一般来源于蓝牙扫描结果，如：可通过调用[startScan](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002529285409__startscan15)或[connection.startBluetoothDiscovery](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002529445383__connectionstartbluetoothdiscovery)扫描得到。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900003Bluetooth disabled.2900010The number of supported device addresses has reached the upper limit.2900099Add persistent device address failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let deviceId = '11:22:33:44:55:66'  // 该地址可通过BLE扫描获取
try {
    access.addPersistentDeviceId(deviceId);
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

#### access.deletePersistentDeviceId16+

deletePersistentDeviceId(deviceId: string): Promise<void>

删除已持久化存储的蓝牙虚拟MAC地址。使用Promise异步回调。

- 该虚拟MAC地址通过[access.addPersistentDeviceId](#ZH-CN_TOPIC_0000002497605416__accessaddpersistentdeviceid16)持久化存储。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH 和 ohos.permission.PERSISTENT_BLUETOOTH_PEERS_MAC

**元服务API**：从API version 16开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是

对端设备的虚拟MAC地址，例如："XX:XX:XX:XX:XX:XX"，

该地址一般来源于蓝牙扫描结果，如：通过调用[startScan](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002529285409__startscan15)或[connection.startBluetoothDiscovery](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002529445383__connectionstartbluetoothdiscovery)扫描得到。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900003Bluetooth disabled.2900099delete persistent device address failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let deviceId = '11:22:33:44:55:66'  // 该地址可通过BLE扫描获取
try {
    access.deletePersistentDeviceId(deviceId);
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

#### access.getPersistentDeviceIds16+

getPersistentDeviceIds(): string[];

获取应用持久化存储过的蓝牙虚拟MAC地址。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH 和 ohos.permission.PERSISTENT_BLUETOOTH_PEERS_MAC

**元服务API**：从API version 16开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明string[]持久化存储过的蓝牙虚拟MAC地址列表。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900003Bluetooth disabled.2900099Get persistent device address failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let deviceIds = access.getPersistentDeviceIds();
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

#### access.isValidRandomDeviceId16+

isValidRandomDeviceId(deviceId: string): boolean;

判断对端蓝牙设备的虚拟MAC地址是否有效。

- 有效的虚拟MAC地址一般来源于蓝牙扫描结果，如：通过调用[startScan](@ohos.bluetooth.ble (蓝牙ble模块).md#ZH-CN_TOPIC_0000002529285409__startscan15)或[connection.startBluetoothDiscovery](@ohos.bluetooth.connection (蓝牙connection模块).md#ZH-CN_TOPIC_0000002529445383__connectionstartbluetoothdiscovery)扫描得到。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**元服务API**：从API version 16开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是对端设备的虚拟MAC地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明boolean蓝牙设备的虚拟MAC地址是否是有效的。true表示有效地址，false表示无效地址。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900003Bluetooth disabled.2900099Check persistent device address failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let deviceId = '11:22:33:44:55:66'  // 该地址可通过BLE扫描获取
    let isValid = access.isValidRandomDeviceId(deviceId);
    console.info("isValid: " + isValid);
} catch (err) {
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

#### access.convertUuid22+

convertUuid(uuid: string): string

将指定格式的的UUID转换为128bit的UUID。

常用的UUID格式主要包括16bit、32bit和128bit三种格式。蓝牙协议定义的128bit格式的基准UUID为：00000000-0000-1000-8000-00805f9b34fb。若输入16bit或者32bit的UUID，将基于蓝牙基准UUID进行转换。若输入128bit的UUID，将不做转换直接输出该UUID。

- 若输入16bit的UUID，例如“1801”，将输出“00001801-0000-1000-8000-00805f9b34fb”。
- 若输入32bit的UUID，例如“12341801”，将输出“12341801-0000-1000-8000-00805f9b34fb”。
- 若输入128bit的UUID，例如“11112222-3333-4444-5555-666677778888”，将直接输出该UUID。
- 若输入不符合以上格式的UUID或包含非16进制范围内的字符，将返回[401](通用错误码.md#ZH-CN_TOPIC_0000002529284567__401-参数检查失败)错误码。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明uuidstring是16bit、32bit、128bit的UUID。

**返回值：**

类型说明string转换后的128bit的UUID。

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let inputUuid: string = '1801';
    let convertedUuid: string = access.convertUuid(inputUuid);
    console.info("convertedUuid: " + convertedUuid);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### BluetoothState

枚举，蓝牙开关状态。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明STATE_OFF0表示蓝牙已关闭。STATE_TURNING_ON1表示蓝牙正在打开。STATE_ON2表示蓝牙已打开。STATE_TURNING_OFF3表示蓝牙正在关闭。STATE_BLE_TURNING_ON4表示蓝牙正在打开LE-only模式。STATE_BLE_ON5表示蓝牙正处于LE-only模式。STATE_BLE_TURNING_OFF6表示蓝牙正在关闭LE-only模式。