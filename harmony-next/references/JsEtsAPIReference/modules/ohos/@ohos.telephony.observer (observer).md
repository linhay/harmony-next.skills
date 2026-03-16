# @ohos.telephony.observer (observer)

本模块提供订阅管理功能，可以订阅/取消订阅的事件包括：网络状态变化、信号状态变化、通话状态变化、蜂窝数据链路连接状态、蜂窝数据业务的上下行数据流状态、SIM状态变化。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { observer } from '@kit.TelephonyKit';
```

#### NetworkState

type NetworkState = radio.NetworkState

网络注册状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

类型说明[radio.NetworkState](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__networkstate)网络注册状态。

#### SignalInformation

type SignalInformation = radio.SignalInformation

网络信号强度信息对象。

**系统能力**：SystemCapability.Telephony.StateRegistry

类型说明[radio.SignalInformation](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__signalinformation)网络信号强度信息对象。

#### DataConnectState

type DataConnectState = data.DataConnectState

描述蜂窝数据链路连接状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

类型说明[data.DataConnectState](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataconnectstate)描述蜂窝数据链路连接状态。

#### RatType

type RatType = radio.RadioTechnology

无线接入技术。

**系统能力**：SystemCapability.Telephony.StateRegistry

类型说明[radio.RadioTechnology](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__radiotechnology)无线接入技术。

#### DataFlowType

type DataFlowType = data.DataFlowType

描述蜂窝数据流类型。

**系统能力**：SystemCapability.Telephony.StateRegistry

类型说明[data.DataFlowType](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataflowtype)描述蜂窝数据流类型。

#### CallState

type CallState = call.CallState

通话状态码。

**系统能力**：SystemCapability.Telephony.StateRegistry

类型说明[call.CallState](@ohos.telephony.call (拨打电话).md#ZH-CN_TOPIC_0000002529285481__callstate)通话状态码（去电过程仅通知CALL_STATE_OFFHOOK状态）。

#### CardType

type CardType = sim.CardType

卡类型。

**系统能力**：SystemCapability.Telephony.StateRegistry

类型说明[sim.CardType](@ohos.telephony.sim (SIM卡管理).md#ZH-CN_TOPIC_0000002529445457__cardtype7)卡类型。

#### SimState

type SimState = sim.SimState

SIM卡状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

类型说明[sim.SimState](@ohos.telephony.sim (SIM卡管理).md#ZH-CN_TOPIC_0000002529445457__simstate)SIM卡状态。

#### TelCallState21+

type TelCallState = call.TelCallState

通话状态码。

**系统能力**：SystemCapability.Telephony.StateRegistry

类型说明[call.TelCallState](@ohos.telephony.call (拨打电话).md#ZH-CN_TOPIC_0000002529285481__telcallstate21)通话状态码（去电过程通知去电号码状态TEL_CALL_STATE_OFFHOOK和去电接通状态TEL_CALL_STATE_CONNECTED）。

#### observer.on('networkStateChange')

on(type: 'networkStateChange', callback: Callback<NetworkState>): void

订阅网络状态变化事件，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是网络状态变化事件，参数固定为'networkStateChange'。callbackCallback<[NetworkState](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__networkstate)>是以callback形式异步返回结果。参考radio的[NetworkState](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__networkstate)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
observer.on('networkStateChange', (data: observer.NetworkState) => {
    console.log("on networkStateChange, data:" + JSON.stringify(data));
});
```

#### observer.on('networkStateChange')

on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void

订阅指定卡槽位的网络状态变化事件，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET_NETWORK_INFO

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是网络状态变化事件，参数固定为'networkStateChange'。options[ObserverOptions](#ZH-CN_TOPIC_0000002497445512__observeroptions11)是电话相关事件订阅参数可选项。callbackCallback<[NetworkState](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__networkstate)>是以callback形式异步返回结果，参考radio的[NetworkState](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__networkstate)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('networkStateChange', options, (data: observer.NetworkState) => {
    console.log("on networkStateChange, data:" + JSON.stringify(data));
});
```

#### observer.off('networkStateChange')

off(type: 'networkStateChange', callback?: Callback<NetworkState>): void

取消订阅网络状态变化事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是网络状态变化事件，参数固定为'networkStateChange'。callbackCallback<[NetworkState](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__networkstate)>否以callback形式异步返回结果，参考radio的[NetworkState](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__networkstate)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
let callback: (data: observer.NetworkState) => void = (data: observer.NetworkState) => {
    console.log("on networkStateChange, data:" + JSON.stringify(data));
}
observer.on('networkStateChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('networkStateChange', callback);
observer.off('networkStateChange');
```

#### observer.on('signalInfoChange')

on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void

订阅信号状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是信号状态变化事件，参数固定为'signalInfoChange'。callbackCallback<Array<[SignalInformation](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__signalinformation)>>是以callback形式异步返回结果，参考radio的[SignalInformation](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__signalinformation)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { radio } from '@kit.TelephonyKit';

observer.on('signalInfoChange', (data: Array<radio.SignalInformation>) => {
    console.log("on signalInfoChange, data:" + JSON.stringify(data));
});
```

#### observer.on('signalInfoChange')

on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void

订阅指定卡槽位的信号状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是信号状态变化事件，参数固定为'signalInfoChange'。options[ObserverOptions](#ZH-CN_TOPIC_0000002497445512__observeroptions11)是电话相关事件订阅参数可选项。callbackCallback<Array<[SignalInformation](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__signalinformation)>>是以callback形式异步返回结果，参考radio的[SignalInformation](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__signalinformation)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { radio } from '@kit.TelephonyKit';

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('signalInfoChange', options, (data: Array<radio.SignalInformation>) => {
    console.log("on signalInfoChange, data:" + JSON.stringify(data));
});
```

#### observer.off('signalInfoChange')

off(type: 'signalInfoChange', callback?: Callback<Array<SignalInformation>>): void

取消订阅信号状态变化事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是信号状态变化事件，参数固定为'signalInfoChange'。callbackCallback<Array<[SignalInformation](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__signalinformation)>>否以callback形式异步返回结果，参考radio的[SignalInformation](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__signalinformation)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { radio } from '@kit.TelephonyKit';

let callback: (data: Array<radio.SignalInformation>) => void = (data: Array<radio.SignalInformation>) => {
    console.log("on signalInfoChange, data:" + JSON.stringify(data));
}
observer.on('signalInfoChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('signalInfoChange', callback);
observer.off('signalInfoChange');
```

#### observer.on('callStateChange')

on(type: 'callStateChange', callback: Callback<CallStateInfo>): void

订阅通话状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是通话状态变化事件，参数固定为'callStateChange'。callbackCallback<[CallStateInfo](#ZH-CN_TOPIC_0000002497445512__callstateinfo11)>是

以callback形式异步返回结果。

应用可获取到CallStateInfo。

其中，三方应用仅能获取state通话状态。number受系统权限管控，仅面向系统应用开放。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
observer.on('callStateChange', (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
});
```

#### observer.on('callStateChange')

on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void

订阅通话状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是通话状态变化事件，参数固定为'callStateChange'。options[ObserverOptions](#ZH-CN_TOPIC_0000002497445512__observeroptions11)是电话相关事件订阅参数可选项。callbackCallback<[CallStateInfo](#ZH-CN_TOPIC_0000002497445512__callstateinfo11)>是

以callback形式异步返回结果。

应用可获取到CallStateInfo。

其中，三方应用仅能获取state通话状态。number受系统权限管控，仅面向系统应用开放。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('callStateChange', options, (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
});
```

#### observer.off('callStateChange')

off(type: 'callStateChange', callback?: Callback<CallStateInfo>): void

取消订阅通话状态变化事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是通话状态变化事件，参数固定为'callStateChange'。callbackCallback<[CallStateInfo](#ZH-CN_TOPIC_0000002497445512__callstateinfo11)>否

以callback形式异步返回结果，参考call的[CallState](@ohos.telephony.call (拨打电话).md#ZH-CN_TOPIC_0000002529285481__callstate)。

number：电话号码。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
let callback: (data: observer.CallStateInfo) => void = (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
}
observer.on('callStateChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('callStateChange', callback);
observer.off('callStateChange');
```

#### observer.on('callStateChangeEx')21+

on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void

订阅通话状态变化拓展事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是通话状态变化事件，参数固定为'callStateChangeEx'。callbackCallback<[TelCallState](@ohos.telephony.call (拨打电话).md#ZH-CN_TOPIC_0000002529285481__telcallstate21)>是

以callback形式异步返回结果。

应用可获取到TelCallState。

options[ObserverOptions](#ZH-CN_TOPIC_0000002497445512__observeroptions11)否电话相关事件订阅参数可选项。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息8800001Invalid parameter value.8800002Service connection failed.8800003System internal error.8800999Unknown error.

**示例：**

```ets
import { call } from '@kit.TelephonyKit';

let callback: (data: call.TelCallState) => void = (data: call.TelCallState) => {
    console.info("on callStateChangeEx, data:" + JSON.stringify(data));
}
let options: observer.ObserverOptions = {
    slotId: 0
}

observer.on('callStateChangeEx', callback, options);
observer.on('callStateChangeEx', callback);
```

#### observer.off('callStateChangeEx')21+

off(type: 'callStateChangeEx', callback?: Callback<TelCallState>): void

取消订阅通话状态变化拓展事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是通话状态变化事件，参数固定为'callStateChange'。callbackCallback<[TelCallState](@ohos.telephony.call (拨打电话).md#ZH-CN_TOPIC_0000002529285481__telcallstate21)>否

以callback形式异步返回结果，参考call的[TelCallState](@ohos.telephony.call (拨打电话).md#ZH-CN_TOPIC_0000002529285481__telcallstate21)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息8800001Invalid parameter value.8800002Service connection failed.8800003System internal error.8800999Unknown error.

**示例：**

```ets
import { call } from '@kit.TelephonyKit';
let callback: (data: call.TelCallState) => void = (data: call.TelCallState) => {
    console.info("on callStateChangeEx, data:" + JSON.stringify(data));
}
observer.on('callStateChangeEx', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('callStateChangeEx', callback);
observer.off('callStateChangeEx');
```

#### observer.on('cellularDataConnectionStateChange')7+

on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void

订阅蜂窝数据链路连接状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是蜂窝数据链路连接状态事件，参数固定为'cellularDataConnectionStateChange'。callbackCallback<[DataConnectionStateInfo](#ZH-CN_TOPIC_0000002497445512__dataconnectionstateinfo11)>是以callback形式异步返回结果，参考data的[DataConnectState](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataconnectstate)，radio的[RadioTechnology](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__radiotechnology)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
observer.on('cellularDataConnectionStateChange', (data: observer.DataConnectionStateInfo) => {
    console.log("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
});
```

#### observer.on('cellularDataConnectionStateChange')7+

on(type: 'cellularDataConnectionStateChange', options: ObserverOptions, callback: Callback<DataConnectionStateInfo>): void

订阅指定卡槽位的蜂窝数据链路连接状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是蜂窝数据链路连接状态事件，参数固定为'cellularDataConnectionStateChange'。options[ObserverOptions](#ZH-CN_TOPIC_0000002497445512__observeroptions11)是电话相关事件订阅参数可选项。callbackCallback<[DataConnectionStateInfo](#ZH-CN_TOPIC_0000002497445512__dataconnectionstateinfo11)>是以callback形式异步返回结果，参考data的[DataConnectState](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataconnectstate)，radio的[RadioTechnology](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__radiotechnology)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('cellularDataConnectionStateChange', options, (data: observer.DataConnectionStateInfo) => {
    console.log("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
});
```

#### observer.off('cellularDataConnectionStateChange')7+

off(type: 'cellularDataConnectionStateChange', callback?: Callback<DataConnectionStateInfo>): void

移除订阅蜂窝数据链路连接状态，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是蜂窝数据链路连接状态事件，参数固定为'cellularDataConnectionStateChange'。callbackCallback<[DataConnectionStateInfo](#ZH-CN_TOPIC_0000002497445512__dataconnectionstateinfo11)>否以callback形式异步返回结果，参考data的[DataConnectState](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataconnectstate)，radio的[RadioTechnology](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__radiotechnology)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
let callback: (data: observer.DataConnectionStateInfo) => void = (data: observer.DataConnectionStateInfo) => {
    console.log("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
}
observer.on('cellularDataConnectionStateChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('cellularDataConnectionStateChange', callback);
observer.off('cellularDataConnectionStateChange');
```

#### observer.on('cellularDataFlowChange')7+

on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void

订阅蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是蜂窝数据业务的上下行数据流状态事件，参数固定为'cellularDataFlowChange'。callbackCallback<[DataFlowType](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataflowtype)>是以callback形式异步返回结果，参考data的[DataFlowType](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataflowtype)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';

observer.on('cellularDataFlowChange', (data: data.DataFlowType) => {
    console.log("on cellularDataFlowChange, data:" + JSON.stringify(data));
});
```

#### observer.on('cellularDataFlowChange')7+

on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void

订阅指定卡槽位的蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是蜂窝数据业务的上下行数据流状态事件，参数固定为'cellularDataFlowChange'。options[ObserverOptions](#ZH-CN_TOPIC_0000002497445512__observeroptions11)是电话相关事件订阅参数可选项。callbackCallback<[DataFlowType](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataflowtype)>是以callback形式异步返回结果，参考data的[DataFlowType](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataflowtype)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('cellularDataFlowChange', options, (data: data.DataFlowType) => {
    console.log("on cellularDataFlowChange, data:" + JSON.stringify(data));
});
```

#### observer.off('cellularDataFlowChange')7+

off(type: 'cellularDataFlowChange', callback?: Callback<DataFlowType>): void

移除订阅蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是蜂窝数据业务的上下行数据流状态事件，参数固定为'cellularDataFlowChange'。callbackCallback<[DataFlowType](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataflowtype)>否以callback形式异步返回结果，参考data的[DataFlowType](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataflowtype)。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
import { data } from '@kit.TelephonyKit';

let callback: (data: data.DataFlowType) => void = (data: data.DataFlowType) => {
    console.log("on cellularDataFlowChange, data:" + JSON.stringify(data));
}
observer.on('cellularDataFlowChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('cellularDataFlowChange', callback);
observer.off('cellularDataFlowChange');
```

#### observer.on('simStateChange')7+

on(type: 'simStateChange', callback: Callback<SimStateData>): void

订阅sim状态更改事件，使用callback方式作为异步方法。

此接口不包含sim卡的激活状态，具体请参见[sim.isSimActive](@ohos.telephony.sim (SIM卡管理).md#ZH-CN_TOPIC_0000002529445457__simissimactive7)接口。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是sim状态更改事件，参数固定为'simStateChange'。callbackCallback<[SimStateData](#ZH-CN_TOPIC_0000002497445512__simstatedata7)>是以callback形式异步返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
observer.on('simStateChange', (data: observer.SimStateData) => {
    console.log("on simStateChange, data:" + JSON.stringify(data));
});
```

#### observer.on('simStateChange')7+

on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void

订阅指定卡槽位的sim状态更改事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是sim状态更改事件，参数固定为'simStateChange'。options[ObserverOptions](#ZH-CN_TOPIC_0000002497445512__observeroptions11)是电话相关事件订阅参数可选项。callbackCallback<[SimStateData](#ZH-CN_TOPIC_0000002497445512__simstatedata7)>是以callback形式异步返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('simStateChange', options, (data: observer.SimStateData) => {
    console.log("on simStateChange, data:" + JSON.stringify(data));
});
```

#### observer.off('simStateChange')7+

off(type: 'simStateChange', callback?: Callback<SimStateData>): void

移除订阅sim状态更改事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是sim状态更改事件，参数固定为'simStateChange'。callbackCallback<[SimStateData](#ZH-CN_TOPIC_0000002497445512__simstatedata7)>否以callback形式异步返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
let callback: (data: observer.SimStateData) => void = (data: observer.SimStateData) => {
    console.log("on simStateChange, data:" + JSON.stringify(data));
}
observer.on('simStateChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('simStateChange', callback);
observer.off('simStateChange');
```

#### observer.on('iccAccountInfoChange')10+

on(type: 'iccAccountInfoChange', callback: Callback<void>): void

订阅卡帐户变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是卡帐户变化事件，参数固定为'iccAccountInfoChange'。callbackCallback<void>是以callback形式异步返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
observer.on('iccAccountInfoChange', () => {
    console.log("on iccAccountInfoChange success");
});
```

#### observer.off('iccAccountInfoChange')10+

off(type: 'iccAccountInfoChange', callback?: Callback<void>): void

移除订阅卡帐户变化事件，使用callback方式作为异步方法。

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

参数名类型必填说明typestring是卡帐户变化事件，参数固定为'iccAccountInfoChange'。callbackCallback<void>否以callback形式异步返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](../../errors/通用错误码.md)和[ohos.telephony(电话子系统)错误码](../../errors/电话子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.8300001Invalid parameter value.8300002Service connection failed.8300003System internal error.8300999Unknown error.

**示例：**

```ets
let callback: () => void = () => {
    console.log("on iccAccountInfoChange success");
}
observer.on('iccAccountInfoChange', callback);
// 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
observer.off('iccAccountInfoChange', callback);
observer.off('iccAccountInfoChange');
```

#### LockReason8+

SIM卡锁类型。

**系统能力**：SystemCapability.Telephony.StateRegistry

名称值说明SIM_NONE0无锁。SIM_PIN1PIN锁。SIM_PUK2PUK锁。SIM_PN_PIN3网络PIN锁。SIM_PN_PUK4网络PUK锁。SIM_PU_PIN5子网PIN锁。SIM_PU_PUK6子网PUK锁。SIM_PP_PIN7服务提供商PIN锁。SIM_PP_PUK8服务提供商PUK锁。SIM_PC_PIN9组织PIN锁。SIM_PC_PUK10组织PUK锁。SIM_SIM_PIN11SIM PIN锁。SIM_SIM_PUK12SIM PUK锁。

#### SimStateData7+

SIM卡类型和状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

名称类型只读可选说明type[CardType](@ohos.telephony.sim (SIM卡管理).md#ZH-CN_TOPIC_0000002529445457__cardtype7)否否SIM卡类型。state[SimState](@ohos.telephony.sim (SIM卡管理).md#ZH-CN_TOPIC_0000002529445457__simstate)否否SIM卡状态。reason8+[LockReason](#ZH-CN_TOPIC_0000002497445512__lockreason8)否否SIM卡锁类型。

#### CallStateInfo11+

通话状态相关信息。

**系统能力**：SystemCapability.Telephony.StateRegistry

名称类型只读可选说明state[CallState](@ohos.telephony.call (拨打电话).md#ZH-CN_TOPIC_0000002529285481__callstate)否否通话类型。numberstring否否电话号码。

#### DataConnectionStateInfo11+

数据连接状态相关信息。

**系统能力**：SystemCapability.Telephony.StateRegistry

名称类型只读可选说明state[DataConnectState](@ohos.telephony.data (蜂窝数据).md#ZH-CN_TOPIC_0000002529445455__dataconnectstate)否否数据连接状态。network[RatType](@ohos.telephony.radio (网络搜索).md#ZH-CN_TOPIC_0000002529285483__radiotechnology)否否网络类型。

#### ObserverOptions11+

电话相关事件订阅参数可选项。

**系统能力**：SystemCapability.Telephony.StateRegistry

名称类型只读可选说明slotIdnumber否否

卡槽ID。

- 0：卡槽1。

- 1：卡槽2。