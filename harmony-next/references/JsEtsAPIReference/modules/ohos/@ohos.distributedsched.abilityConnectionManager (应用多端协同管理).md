# @ohos.distributedsched.abilityConnectionManager (应用多端协同管理)

abilityConnectionManager模块提供了应用协同接口管理能力。设备组网成功（需登录同账号、双端打开蓝牙）后，系统应用和三方应用可以跨设备拉起同应用的一个[UIAbility](@ohos.app.ability.UIAbility (带界面的应用组件).md)，拉起并连接成功后可实现跨设备数据传输（文本信息）。

本模块首批接口从API version 18开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
```

#### abilityConnectionManager.createAbilityConnectionSession

createAbilityConnectionSession(serviceName: string, context: Context, peerInfo: PeerInfo , connectOptions: ConnectOptions): number

创建应用间的协同会话。

**需要权限**：ohos.permission.INTERNET、ohos.permission.GET_NETWORK_INFO、ohos.permission.SET_NETWORK_INFO和ohos.permission.DISTRIBUTED_DATASYNC

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明serviceNamestring是应用设置的服务名称（两端必须一致），最大长度为256字符。context[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)是表示应用上下文。peerInfo[PeerInfo](#ZH-CN_TOPIC_0000002529445403__peerinfo)是对端的协同信息。connectOptions[ConnectOptions](#ZH-CN_TOPIC_0000002529445403__connectoptions)是应用设置的连接选项。

**返回值：**

类型说明number成功创建的协同会话ID。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息201Permission denied.401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

1.

在设备A上，应用需要主动调用createAbilityConnectionSession()接口创建协同会话并返回sessionId。

```ets
import { abilityConnectionManager, distributedDeviceManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let dmClass: distributedDeviceManager.DeviceManager;

function initDmClass(): void {
  try {
    dmClass = distributedDeviceManager.createDeviceManager('com.example.remotephotodemo');
  } catch (err) {
    hilog.error(0x0000, 'testTag', 'createDeviceManager err: ' + JSON.stringify(err));
  }
}

function getRemoteDeviceId(): string | undefined {
  initDmClass();
  if (typeof dmClass === 'object' && dmClass !== null) {
    hilog.info(0x0000, 'testTag', 'getRemoteDeviceId begin');
    let list = dmClass.getAvailableDeviceListSync();
    if (typeof (list) === 'undefined' || typeof (list.length) === 'undefined') {
      hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: list is null');
      return;
    }
    if (list.length === 0) {
      hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: list is empty');
      return;
    }
    return list[0].networkId;
  } else {
    hilog.info(0x0000, 'testTag', 'getRemoteDeviceId err: dmClass is null');
    return;
  }
}

@Entry
@Component
struct Index {
  createSession(): void {
    // 定义peer信息
    const peerInfo: abilityConnectionManager.PeerInfo = {
      deviceId: getRemoteDeviceId()!,
      bundleName: 'com.example.remotephotodemo',
      moduleName: 'entry',
      abilityName: 'EntryAbility',
      serviceName: 'collabTest'
    };
    const myRecord: Record<string, string> = {
      "newKey1": "value1",
    };

    // 定义连接选项
    const connectOptions: abilityConnectionManager.ConnectOptions = {
      needSendData: true,
      startOptions: abilityConnectionManager.StartOptionParams.START_IN_FOREGROUND,
      parameters: myRecord
    };
    let context = this.getUIContext().getHostContext();
    try {
      let sessionId = abilityConnectionManager.createAbilityConnectionSession("collabTest", context, peerInfo, connectOptions);
      hilog.info(0x0000, 'testTag', 'createSession sessionId is', sessionId);
    } catch (error) {
      hilog.error(0x0000, 'testTag', error);
    }
  }

  build() {
  }
}
```

1.

在设备B上，对于createAbilityConnectionSession接口的调用，可在应用被拉起后触发协同生命周期函数onCollaborate时，在onCollaborate内进行。

```ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
    hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
    let param = wantParam["ohos.extra.param.key.supportCollaborateIndex"] as Record<string, Object>
    this.onCollab(param);
    return 0;
  }

  onCollab(collabParam: Record<string, Object>) {
    const sessionId = this.createSessionFromWant(collabParam);
    if (sessionId == -1) {
      hilog.info(0x0000, 'testTag', 'Invalid session ID.');
      return;
    }
  }

  createSessionFromWant(collabParam: Record<string, Object>): number {
    let sessionId = -1;
    const peerInfo = collabParam["PeerInfo"] as abilityConnectionManager.PeerInfo;
    if (peerInfo == undefined) {
      return sessionId;
    }

    const options = collabParam["ConnectOption"] as abilityConnectionManager.ConnectOptions;
    try {
      sessionId = abilityConnectionManager.createAbilityConnectionSession("collabTest", this.context, peerInfo, options);
      AppStorage.setOrCreate('sessionId', sessionId);
      hilog.info(0x0000, 'testTag', 'createSession sessionId is' + sessionId);
    } catch (error) {
      hilog.error(0x0000, 'testTag', error);
    }
    return sessionId;
  }
}
```

#### abilityConnectionManager.destroyAbilityConnectionSession

destroyAbilityConnectionSession(sessionId: number): void

销毁应用间的协同会话。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明sessionIdnumber是待销毁的协同会话ID。

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'destroyAbilityConnectionSession called');
let sessionId = 100;
abilityConnectionManager.destroyAbilityConnectionSession(sessionId);
```

#### abilityConnectionManager.getPeerInfoById

getPeerInfoById(sessionId: number): PeerInfo | undefined

获取指定会话中对端应用信息。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明sessionIdnumber是协同会话ID。

**返回值：**

类型说明[PeerInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-abilityconnectionmanager#peerinfo) | undefined若存在对应peeerInfo，则返回接收端的协作应用信息。若sessionId未找到，则查询失败，返回undefined。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'getPeerInfoById called');
let sessionId = 100;
const peerInfo = abilityConnectionManager.getPeerInfoById(sessionId);
```

#### abilityConnectionManager.connect

connect(sessionId: number): Promise<ConnectResult>

创建协同会话成功并获得会话ID后，设备A上可进行UIAbility的连接。使用Promise异步回调。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明sessionIdnumber是已创建的协同会话ID。

**返回值：**

类型说明Promise<ConnectResult>以Promise形式返回[连接结果](#ZH-CN_TOPIC_0000002529445403__connectresult)。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

设备A上的应用在创建协同会话成功并获得会话ID后，调用connect()方法启动UIAbility连接，并拉起设备B应用。

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.connect(sessionId).then((ConnectResult) => {
  if (!ConnectResult.isConnected) {
    hilog.info(0x0000, 'testTag', 'connect failed');
    return;
  }
}).catch(() => {
  hilog.error(0x0000, 'testTag', "connect failed");
})
```

#### abilityConnectionManager.acceptConnect

acceptConnect(sessionId: number, token: string): Promise<void>

设备B上的应用，在创建协同会话成功并获得会话ID后，调用acceptConnect()方法接受连接。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明sessionIdnumber是已创建的协同会话ID。tokenstring是设备A应用传入的token值。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

设备B上的应用，在createAbilityConnectionSession接口调用并获取sessionId成功后，可调用acceptConnect接口来选择接受连接。

```ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
    hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
    let param = wantParam["ohos.extra.param.key.supportCollaborateIndex"] as Record<string, Object>
    this.onCollab(param);
    return 0;
  }

  onCollab(collabParam: Record<string, Object>) {
    const sessionId = this.createSessionFromWant(collabParam);
    if (sessionId == -1) {
      hilog.info(0x0000, 'testTag', 'Invalid session ID.');
      return;
    }
    const collabToken = collabParam["ohos.dms.collabToken"] as string;
    abilityConnectionManager.acceptConnect(sessionId, collabToken).then(() => {
      hilog.info(0x0000, 'testTag', 'acceptConnect success');
    }).catch(() => {
      hilog.error(0x0000, 'testTag', 'failed');
    })
  }

  createSessionFromWant(collabParam: Record<string, Object>): number {
    let sessionId = -1;
    const peerInfo = collabParam["PeerInfo"] as abilityConnectionManager.PeerInfo;
    if (peerInfo == undefined) {
      return sessionId;
    }

    const options = collabParam["ConnectOption"] as abilityConnectionManager.ConnectOptions;
    try {
      sessionId = abilityConnectionManager.createAbilityConnectionSession("collabTest", this.context, peerInfo, options);
      AppStorage.setOrCreate('sessionId', sessionId);
      hilog.info(0x0000, 'testTag', 'createSession sessionId is' + sessionId);
    } catch (error) {
      hilog.error(0x0000, 'testTag', error);
    }
    return sessionId;
  }
}
```

#### abilityConnectionManager.disconnect

disconnect(sessionId: number): void

当协同业务执行完毕后，协同双端的任意一台设备，应断开UIAbility的连接，结束协同状态。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明sessionIdnumber是协同会话ID

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

hilog.info(0x0000, 'testTag', 'disconnectRemoteAbility begin');
let sessionId = 100;
abilityConnectionManager.disconnect(sessionId);
```

#### abilityConnectionManager.reject

reject(token: string, reason: string): void;

在跨端应用协同过程中，在拒绝对端的连接请求后，向对端发送拒绝原因。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明tokenstring是用于协作服务管理的令牌。reasonstring是连接被拒绝的原因。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { AbilityConstant, UIAbility, Want} from '@kit.AbilityKit';
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
    onCollaborate(wantParam: Record<string, Object>): AbilityConstant.CollaborateResult {
      hilog.info(0x0000, 'testTag', '%{public}s', 'on collaborate');
      let collabParam = wantParam["ohos.extra.param.key.supportCollaborateIndex"] as Record<string, Object>;
      const collabToken = collabParam["ohos.dms.collabToken"] as string;
      const reason = "test";
      hilog.info(0x0000, 'testTag', 'reject begin');
      abilityConnectionManager.reject(collabToken, reason);
      return AbilityConstant.CollaborateResult.REJECT;
    }
}
```

#### abilityConnectionManager.on('connect')

on(type: 'connect', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册connect事件的回调监听。使用callback异步回调。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'connect'，完成[abilityConnectionManager.connect()](#ZH-CN_TOPIC_0000002529445403__abilityconnectionmanagerconnect)调用，触发该事件。sessionIdnumber是创建的协同会话ID。callbackCallback<[EventCallbackInfo](#ZH-CN_TOPIC_0000002529445403__eventcallbackinfo)>是注册的回调函数。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.on("connect", sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'session connect, sessionId is', callbackInfo.sessionId);
});
```

#### abilityConnectionManager.off('connect')

off(type: 'connect', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消connect事件的回调监听。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'connect'。sessionIdnumber是创建的协同会话ID。callbackCallback<[EventCallbackInfo](#ZH-CN_TOPIC_0000002529445403__eventcallbackinfo)>否注册的回调函数。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';

let sessionId = 100;
abilityConnectionManager.off("connect", sessionId);
```

#### abilityConnectionManager.on('disconnect')

on(type: 'disconnect', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册disconnect事件的回调监听。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'disconnect'，完成[abilityConnectionManager.disconnect()](#ZH-CN_TOPIC_0000002529445403__abilityconnectionmanagerdisconnect)调用，触发该事件。sessionIdnumber是创建的协同会话ID。callbackCallback<[EventCallbackInfo](#ZH-CN_TOPIC_0000002529445403__eventcallbackinfo)>是注册的回调函数。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.on("disconnect", sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'session disconnect, sessionId is', callbackInfo.sessionId);
});
```

#### abilityConnectionManager.off('disconnect')

off(type: 'disconnect', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消disconnect事件的回调监听。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'disconnect'。sessionIdnumber是创建的协同会话ID。callbackCallback<[EventCallbackInfo](#ZH-CN_TOPIC_0000002529445403__eventcallbackinfo)>否注册的回调函数。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.off("disconnect", sessionId);
```

#### abilityConnectionManager.on('receiveMessage')

on(type: 'receiveMessage', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册receiveMessage事件的回调监听。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'receiveMessage'，完成[abilityConnectionManager.sendMessage()](#ZH-CN_TOPIC_0000002529445403__abilityconnectionmanagersendmessage)调用，触发该事件。sessionIdnumber是创建的协同会话ID。callbackCallback<[EventCallbackInfo](#ZH-CN_TOPIC_0000002529445403__eventcallbackinfo)>是注册的回调函数。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.on("receiveMessage", sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'receiveMessage, sessionId is', callbackInfo.sessionId);
});
```

#### abilityConnectionManager.off('receiveMessage')

off(type: 'receiveMessage', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消receiveMessage事件的回调监听。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'receiveMessage'。sessionIdnumber是创建的协同会话ID。callbackCallback<[EventCallbackInfo](#ZH-CN_TOPIC_0000002529445403__eventcallbackinfo)>否注册的回调函数。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.off("receiveMessage", sessionId);
```

#### abilityConnectionManager.on('receiveData')

on(type: 'receiveData', sessionId: number, callback: Callback<EventCallbackInfo>): void

注册receiveData事件的回调监听。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'receiveData'，完成[abilityConnectionManager.sendData()](#ZH-CN_TOPIC_0000002529445403__abilityconnectionmanagersenddata)调用，触发该事件。sessionIdnumber是创建的协同会话ID。callbackCallback<[EventCallbackInfo](#ZH-CN_TOPIC_0000002529445403__eventcallbackinfo)>是注册的回调函数。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.on("receiveData", sessionId,(callbackInfo) => {
  hilog.info(0x0000, 'testTag', 'receiveData, sessionId is', callbackInfo.sessionId);
});
```

#### abilityConnectionManager.off('receiveData')

off(type: 'receiveData', sessionId: number, callback?: Callback<EventCallbackInfo>): void

取消receiveData事件的回调监听。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明typestring是事件回调类型，支持的事件为'receiveData'，完成。sessionIdnumber是创建的协同会话ID。callbackCallback<[EventCallbackInfo](#ZH-CN_TOPIC_0000002529445403__eventcallbackinfo)>否注册的回调函数。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.off("receiveData", sessionId);
```

#### abilityConnectionManager.sendMessage

sendMessage(sessionId: number, msg: string): Promise<void>

应用连接成功后，设备A或设备B可向对端设备发送文本信息。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明sessionIdnumber是协同会话ID。msgstring是文本信息内容（内容最大限制为1KB）。

**返回值：**

类型说明Promise<void>无返回结果的promise对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let sessionId = 100;
abilityConnectionManager.sendMessage(sessionId, "message send success").then(() => {
  hilog.info(0x0000, 'testTag', "sendMessage success");
}).catch(() => {
  hilog.error(0x0000, 'testTag', "connect failed");
})
```

#### abilityConnectionManager.sendData

sendData(sessionId: number, data: ArrayBuffer): Promise<void>

应用连接成功后，设备A或设备B可向对端设备发送[ArrayBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arraybuffer-object)字节流。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

**参数：**

参数名类型必填说明sessionIdnumber是协同会话ID。data[ArrayBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arraybuffer-object)是字节流信息。

**返回值：**

类型说明Promise<void>无返回结果的promise对象。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

**示例：**

```ets
import { abilityConnectionManager } from '@kit.DistributedServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { util } from '@kit.ArkTS';

let textEncoder = util.TextEncoder.create("utf-8");
const arrayBuffer  = textEncoder.encodeInto("data send success");

let sessionId = 100;
abilityConnectionManager.sendData(sessionId, arrayBuffer.buffer).then(() => {
  hilog.info(0x0000, 'testTag', "sendMessage success");
}).catch(() => {
  hilog.info(0x0000, 'testTag', "sendMessage failed");
})
```

#### PeerInfo

应用协同信息。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称类型只读可选说明deviceIdstring否否对端设备ID。bundleNamestring否否对端应用的包名。moduleNamestring否否对端应用的模块名。abilityNamestring否否对端应用的组件名。serviceNamestring否是应用设置的服务名称。

#### ConnectOptions

应用连接时所需的连接选项。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称类型只读可选说明needSendDataboolean否是true代表需要传输数据，false代表不需要传输数据。startOptions[StartOptionParams](#ZH-CN_TOPIC_0000002529445403__startoptionparams)否是配置应用启动选项。parametersRecord<string, string>否是配置连接所需的额外信息。

#### ConnectResult

连接的结果。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称类型只读可选说明isConnectedboolean否否true表示连接成功，false表示连接失败。errorCode[ConnectErrorCode](#ZH-CN_TOPIC_0000002529445403__connecterrorcode)否是表示连接错误码。reasonstring否是表示拒绝连接的原因。

#### EventCallbackInfo

回调方法的接收信息。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称类型只读可选说明sessionIdnumber否否表示当前事件对应的协同会话ID。reason[DisconnectReason](#ZH-CN_TOPIC_0000002529445403__disconnectreason)否是表示断连原因。msgstring否是表示接收的消息。dataArrayBuffer否是表示接收的字节流。

#### CollaborateEventInfo

协同事件信息。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称类型只读可选说明eventType[CollaborateEventType](#ZH-CN_TOPIC_0000002529445403__collaborateeventtype)否否表示协同事件的类型。eventMsgstring否是表示协同事件的消息内容。

#### ConnectErrorCode

连接的错误码。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称值说明CONNECTED_SESSION_EXISTS0表示应用之间存在已连接的会话。PEER_APP_REJECTED1表示对端应用拒绝了协作请求。LOCAL_WIFI_NOT_OPEN2表示本端WiFi未开启。PEER_WIFI_NOT_OPEN3表示对端WiFi未开启。PEER_ABILITY_NO_ONCOLLABORATE4表示未实现onCollaborate方法。SYSTEM_INTERNAL_ERROR5表示系统内部错误。

#### StartOptionParams

启动选项参数的枚举。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称值说明START_IN_FOREGROUND0表示将对端应用启动至前台。

#### CollaborateEventType

协同事件类型的枚举。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称值说明SEND_FAILURE0表示任务发送失败。COLOR_SPACE_CONVERSION_FAILURE1表示色彩空间转换失败。

#### DisconnectReason

当前断连原因的枚举。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称值说明PEER_APP_CLOSE_COLLABORATION0表示对端应用主动关闭了协作。PEER_APP_EXIT1表示对端应用退出。NETWORK_DISCONNECTED2表示网络断开。

#### CollaborationKeys

应用协作键值的枚举。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称值说明PEER_INFOohos.collaboration.key.peerInfo表示对端设备信息的键值。CONNECT_OPTIONSohos.collaboration.key.connectOptions表示连接选项的键值。COLLABORATE_TYPEohos.collaboration.key.abilityCollaborateType表示协作类型的键值。

#### CollaborationValues

应用协作相关值的枚举。

**系统能力**：SystemCapability.DistributedSched.AppCollaboration

名称值说明ABILITY_COLLABORATION_TYPE_DEFAULTohos.collaboration.value.abilityCollab表示默认的协作类型。ABILITY_COLLABORATION_TYPE_CONNECT_PROXYohos.collaboration.value.connectProxy表示连接代理的协作类型。