# @ohos.bluetooth.baseProfile (蓝牙baseProfile模块)

本模块提供不同的蓝牙技术协议的基础公共方法。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { baseProfile } from '@kit.ConnectivityKit';
```

#### BaseProfile

基础Profile接口定义，提供订阅和获取连接状态等公共能力。如：[A2dpSourceProfile](@ohos.bluetooth.a2dp (蓝牙a2dp模块).md#ZH-CN_TOPIC_0000002529445381__a2dpsourceprofile)、[HandsFreeAudioGatewayProfile](@ohos.bluetooth.hfp (蓝牙hfp模块).md#ZH-CN_TOPIC_0000002529285411__handsfreeaudiogatewayprofile)等[Profile](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/terminology#profile)类型都继承于该类。

#### ProfileConnectionState

type ProfileConnectionState = constant.ProfileConnectionState

本端和对端蓝牙设备间的Profile连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

类型说明[constant.ProfileConnectionState](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileconnectionstate)本端和对端蓝牙设备间的Profile连接状态。

#### StateChangeParam

本端和对端蓝牙设备间Profile连接状态变化参数。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称类型只读可选说明deviceIdstring否否对端设备地址，例如："XX:XX:XX:XX:XX:XX"。state[ProfileConnectionState](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileconnectionstate)否否Profile连接状态。cause12+[DisconnectCause](#ZH-CN_TOPIC_0000002497445438__disconnectcause12)否否Profile断开连接的原因。

#### DisconnectCause12+

枚举，Profile断开连接的原因。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

名称值说明USER_DISCONNECT0用户主动断开连接。CONNECT_FROM_KEYBOARD1连接请求需从键盘侧发起。CONNECT_FROM_MOUSE2连接请求需从鼠标侧发起。CONNECT_FROM_CAR3连接请求需从车机侧发起。TOO_MANY_CONNECTED_DEVICES4当前连接数量超过上限。CONNECT_FAIL_INTERNAL5内部错误。

#### BaseProfile.getConnectedDevices

getConnectedDevices(): Array<string>

获取和本端设备间已连接Profile的对端设备列表。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

类型说明Array<string>

返回已连接Profile的对端设备列表。

基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。

- 已配对的地址不会变更。

- 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。

- 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。

- 若要持久化保存该地址，可使用[access.addPersistentDeviceId](@ohos.bluetooth.access (蓝牙access模块).md#ZH-CN_TOPIC_0000002497605416__accessaddpersistentdeviceid16)方法。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900004Profile not supported.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
    let retArray = a2dpSrc.getConnectedDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

#### BaseProfile.getConnectionState

getConnectionState(deviceId: string): ProfileConnectionState

获取和对端设备间Profile的连接状态。

- 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取Profile连接状态。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明deviceIdstring是对端设备地址，例如："XX:XX:XX:XX:XX:XX"。

**返回值：**

类型说明[ProfileConnectionState](@ohos.bluetooth.constant (蓝牙constant模块).md#ZH-CN_TOPIC_0000002497605418__profileconnectionstate)返回Profile的连接状态。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)和[蓝牙服务子系统错误码](蓝牙服务子系统错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.2900001Service stopped.2900003Bluetooth disabled.2900004Profile not supported.2900099Operation failed.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
    let ret = a2dpSrc.getConnectionState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### BaseProfile.on('connectionStateChange')

on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void

订阅Profile的连接状态变化事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是

事件回调类型，支持的事件为'connectionStateChange'，表示Profile连接状态变化事件。

当Profile连接状态变化时，触发该事件。

callbackCallback<[StateChangeParam](#ZH-CN_TOPIC_0000002497445438__statechangeparam)>是指定订阅的回调函数，会携带Profile连接状态。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

function onReceiveEvent(data: baseProfile.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
    a2dpSrc.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

#### BaseProfile.off('connectionStateChange')

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](#ZH-CN_TOPIC_0000002497445438__statechangeparam)>): void

取消订阅Profile的连接状态变化事件。

**需要权限**：ohos.permission.ACCESS_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'connectionStateChange'，表示Profile连接状态变化事件。callbackCallback<[StateChangeParam](#ZH-CN_TOPIC_0000002497445438__statechangeparam)>否

指定取消订阅的回调函数通知。

若传参，则需与[BaseProfile.on('connectionStateChange')](#ZH-CN_TOPIC_0000002497445438__baseprofileonconnectionstatechange)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](通用错误码.md)。

错误码ID错误信息201Permission denied.401Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.801Capability not supported.

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

function onReceiveEvent(data: baseProfile.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
    a2dpSrc.on('connectionStateChange', onReceiveEvent);
    a2dpSrc.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```