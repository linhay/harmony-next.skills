# @ohos.ability.featureAbility (FeatureAbility模块)

FeatureAbility模块提供与用户进行交互的Ability的能力，包括启动新的Ability、停止Ability、获取dataAbilityHelper对象、获取当前Ability对应的窗口，连接断连Service等。

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在FA模型下使用。

#### 使用限制

FeatureAbility模块的接口只能在Page类型的Ability中调用。

#### 导入模块

```ets
import { featureAbility } from '@kit.AbilityKit';
```

#### featureAbility.startAbility

startAbility(parameter: StartAbilityParameter, callback: AsyncCallback<number>): void

启动新的Ability。使用callback异步回调。

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明parameter[StartAbilityParameter](../../topics/components/StartAbilityParameter.md)是表示被启动的Ability。callbackAsyncCallback<number>是回调函数。当启动Ability成功，err为undefined，data为0表示启动成功，data为其他表示启动失败；否则为错误对象。

**示例：**

```ets
import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.startAbility(
  {
    want:
    {
      action: '',
      entities: [''],
      type: '',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /* FA模型中abilityName由package + Ability name组成 */
      abilityName: 'com.example.myapplication.secondAbility',
      uri: ''
    },
  },
  (error, data) => {
    if (error && error.code !== 0) {
      console.error(`startAbility fail, error: ${JSON.stringify(error)}`);
    } else {
      console.log(`startAbility success, data: ${JSON.stringify(data)}`);
    }
  }
);
```

#### featureAbility.startAbility

startAbility(parameter: StartAbilityParameter): Promise<number>

启动新的Ability。使用Promise异步回调。

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**模型约束**：此接口仅可在FA模型下使用。

**参数：**

参数名类型必填说明parameter[StartAbilityParameter](../../topics/components/StartAbilityParameter.md)是表示被启动的Ability。

**返回值：**

类型说明Promise<number>Promise对象。返回0表示启动成功，返回其他表示启动失败。

**示例：**

```ets
import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.startAbility(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: ['entity.system.home'],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /* FA模型中abilityName由package + Ability name组成 */
      abilityName: 'com.example.myapplication.secondAbility',
      uri: ''
    },
  }
).then((data) => {
  console.info(`startAbility data: ${JSON.stringify(data)}`);
});
```

#### featureAbility.acquireDataAbilityHelper7+

acquireDataAbilityHelper(uri: string): DataAbilityHelper

获取dataAbilityHelper对象。

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

跨应用访问dataAbility，对端应用需配置关联启动。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明uristring是表示要打开的文件的路径。

**返回值：**

类型说明[DataAbilityHelper](../../topics/system-services/DataAbilityHelper.md)用来协助其他Ability访问DataAbility的工具类。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';

let dataAbilityHelper = featureAbility.acquireDataAbilityHelper(
  'dataability:///com.example.DataAbility'
);
```

#### featureAbility.startAbilityForResult7+

startAbilityForResult(parameter: StartAbilityParameter, callback: AsyncCallback<AbilityResult>): void

启动一个Ability。使用callback异步回调。启动Ability后，存在如下几种情况：

- 正常情况下可通过调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002529444565__featureabilityterminateselfwithresult7)接口使之终止并且返回结果给调用方。
- 异常情况下比如杀死Ability会返回异常信息给调用方, 异常信息中resultCode为-1。
- 如果被启动的Ability模式是单实例模式, 不同应用多次调用该接口启动这个Ability，当这个Ability调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002529444565__featureabilityterminateselfwithresult7)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明parameter[StartAbilityParameter](../../topics/components/StartAbilityParameter.md)是表示被启动的Ability。callbackAsyncCallback<[AbilityResult](../../topics/system-services/AbilityResult.md)>是回调函数。当启动Ability成功，err为undefined，data为ability的启动结果；否则为错误对象。

**示例：**

```ets
import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.startAbilityForResult(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: ['entity.system.home'],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /* FA模型中abilityName由package + Ability name组成 */
      abilityName: 'com.example.myapplication.secondAbility',
      uri: ''
    },
  },
  (error, data) => {
    if (error && error.code !== 0) {
      console.error(`startAbilityForResult fail, error: ${JSON.stringify(error)}`);
    } else {
      console.log(`startAbilityForResult success, data: ${JSON.stringify(data)}`);
    }
  }
);
```

#### featureAbility.startAbilityForResult7+

startAbilityForResult(parameter: StartAbilityParameter): Promise<AbilityResult>

启动一个Ability。使用Promise异步回调。启动Ability后，存在如下几种情况：

- 正常情况下可通过调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002529444565__featureabilityterminateselfwithresult7)接口使之终止并且返回结果给调用方。
- 异常情况下比如杀死Ability会返回异常信息给调用方, 异常信息中resultCode为-1。
- 如果被启动的Ability模式是单实例模式, 不同应用多次调用该接口启动这个Ability，当这个Ability调用[terminateSelfWithResult](#ZH-CN_TOPIC_0000002529444565__featureabilityterminateselfwithresult7)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明parameter[StartAbilityParameter](../../topics/components/StartAbilityParameter.md)是表示被启动的Ability。

**返回值：**

类型说明Promise<[AbilityResult](../../topics/system-services/AbilityResult.md)>Promise对象，返回启动Ability的结果。

**示例：**

```ets
import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.startAbilityForResult(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: ['entity.system.home'],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /* FA模型中abilityName由package + Ability name组成 */
      abilityName: 'com.example.myapplication.secondAbility',
      uri: '',
      parameters:
      {
        mykey0: 1111,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'xxxxxxxxxxxxxxxxxxxxxx',
        mykey4: [1, 15],
        mykey5: [false, true, false],
        mykey6: ['aaaaaa', 'bbbbb', 'ccccccccccc'],
        mykey7: true,
      },
    },
  },
).then((data) => {
  console.info(`startAbilityForResult data: ${JSON.stringify(data)}`);
});
```

#### featureAbility.terminateSelfWithResult7+

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

停止当前的Ability。使用callback异步回调。如果该Ability是通过调用[startAbilityForResult](#ZH-CN_TOPIC_0000002529444565__featureabilitystartabilityforresult7)接口被拉起的，调用terminateSelfWithResult接口时会将结果返回给调用者，如果该Ability不是通过调用[startAbilityForResult](#ZH-CN_TOPIC_0000002529444565__featureabilitystartabilityforresult7)接口被拉起的，调用terminateSelfWithResult接口时不会有结果返回给调用者。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明parameter[AbilityResult](../../topics/system-services/AbilityResult.md)是表示停止Ability之后返回的结果。callbackAsyncCallback<void>是回调函数。当停止当前Ability成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.terminateSelfWithResult(
  {
    resultCode: 1,
    want:
    {
      action: 'ohos.want.action.home',
      entities: ['entity.system.home'],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /* FA模型中abilityName由package + Ability name组成 */
      abilityName: 'com.example.myapplication.secondAbility',
      uri: '',
      parameters: {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [1, 15],
        mykey5: [false, true, false],
        mykey6: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey7: true,
      }
    },
  },
  (error) => {
    console.error(`error: ${JSON.stringify(error)}`);
  }
);
```

#### featureAbility.terminateSelfWithResult7+

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

停止当前的Ability。使用Promise异步回调。如果该Ability是通过调用[startAbilityForResult](#ZH-CN_TOPIC_0000002529444565__featureabilitystartabilityforresult7)接口被拉起的，调用terminateSelfWithResult接口时会将结果返回给调用者，如果该Ability不是通过调用[startAbilityForResult](#ZH-CN_TOPIC_0000002529444565__featureabilitystartabilityforresult7)接口被拉起的，调用terminateSelfWithResult接口时不会有结果返回给调用者。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明parameter[AbilityResult](../../topics/system-services/AbilityResult.md)是表示停止Ability之后返回的结果。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { featureAbility, wantConstant } from '@kit.AbilityKit';

featureAbility.terminateSelfWithResult(
  {
    resultCode: 1,
    want:
    {
      action: 'ohos.want.action.home',
      entities: ['entity.system.home'],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.myapplication',
      /* FA模型中abilityName由package + Ability name组成 */
      abilityName: 'com.example.myapplication.secondAbility',
      uri:'',
      parameters: {
        mykey0: 2222,
        mykey1: [1, 2, 3],
        mykey2: '[1, 2, 3]',
        mykey3: 'ssssssssssssssssssssssssss',
        mykey4: [1, 15],
        mykey5: [false, true, false],
        mykey6: ['qqqqq', 'wwwwww', 'aaaaaaaaaaaaaaaaa'],
        mykey7: true,
      }
    },
  }
).then(() => {
  console.info('==========================>terminateSelfWithResult=======================>');
});
```

#### featureAbility.hasWindowFocus7+

hasWindowFocus(callback: AsyncCallback<boolean>): void

检查Ability的主窗口是否具有窗口焦点。使用callback异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明callbackAsyncCallback<boolean>是

回调函数。

如果此Ability当前具有视窗焦点，则返回true；否则返回false。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';

featureAbility.hasWindowFocus((error, data) => {
  if (error && error.code !== 0) {
    console.error(`hasWindowFocus fail, error: ${JSON.stringify(error)}`);
  } else {
    console.log(`hasWindowFocus success, data: ${JSON.stringify(data)}`);
  }
});
```

#### featureAbility.hasWindowFocus7+

hasWindowFocus(): Promise<boolean>

检查Ability的主窗口是否具有窗口焦点。使用Promise异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

类型说明Promise<boolean>Promise对象。如果此Ability当前具有视窗焦点，则返回true；否则返回false。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';

featureAbility.hasWindowFocus().then((data) => {
  console.info(`hasWindowFocus data: ${JSON.stringify(data)}`);
});
```

#### featureAbility.getWant

getWant(callback: AsyncCallback<Want>): void

获取要拉起的Ability对应的Want。使用callback异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明callbackAsyncCallback<[Want](@ohos.application.Want (Want).md)>是回调函数，返回want信息。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';

featureAbility.getWant((error, data) => {
  if (error && error.code !== 0) {
    console.error(`getWant fail, error: ${JSON.stringify(error)}`);
  } else {
    console.log(`getWant success, data: ${JSON.stringify(data)}`);
  }
});
```

#### featureAbility.getWant

getWant(): Promise<Want>

获取要拉起的Ability对应的Want。使用Promise异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

类型说明Promise<[Want](@ohos.application.Want (Want).md)>Promise对象，返回want信息。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';

featureAbility.getWant().then((data) => {
  console.info(`getWant data: ${JSON.stringify(data)}`);
});
```

#### featureAbility.getContext

getContext(): Context

获取应用上下文。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

类型说明Context返回应用程序上下文。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';

let context = featureAbility.getContext();
context.getBundleName((error, data) => {
  if (error && error.code !== 0) {
    console.error(`getBundleName fail, error: ${JSON.stringify(error)}`);
  } else {
    console.log(`getBundleName success, data: ${JSON.stringify(data)}`);
  }
});
```

#### featureAbility.terminateSelf7+

terminateSelf(callback: AsyncCallback<void>): void

停止当前的Ability。使用callback异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。当停止当前的Ability成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';

featureAbility.terminateSelf(
  (error) => {
    console.error(`error: ${JSON.stringify(error)}`);
  }
)
```

#### featureAbility.terminateSelf7+

terminateSelf(): Promise<void>

停止当前的Ability。使用Promise异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

featureAbility.terminateSelf().then(() => {
  console.info('==========================>terminateSelf=======================>');
}).catch((error: BusinessError) => {
  console.error(`terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}`);
});
```

#### featureAbility.connectAbility7+

connectAbility(request: Want, options:ConnectOptions): number

将当前Ability与指定的ServiceAbility进行连接。

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

跨应用连接serviceAbility，对端应用需配置关联启动。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明request[Want](@ohos.application.Want (Want).md)是表示被连接的ServiceAbility。options[ConnectOptions](../../topics/misc/ConnectOptions.md)是表示连接回调函数。

**返回值：**

类型说明number连接的ServiceAbility的ID(ID从0开始自增，每连接成功一次ID加1)。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectId = featureAbility.connectAbility(
  {
    deviceId: '',
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'com.ix.ServiceAbility.ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.log(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.log(`ConnectAbility onDisconnect element.deviceId : ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`featureAbilityTest ConnectAbility onFailed errCode : ${code}`);
    },
  },
);
```

#### featureAbility.disconnectAbility7+

disconnectAbility(connection: number, callback:AsyncCallback<void>): void

断开与指定ServiceAbility的连接。使用callback异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明connectionnumber是表示断开连接的ServiceAbility的ID。callbackAsyncCallback<void>是回调函数。当断开与指定ServiceAbility的连接成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connectId = featureAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'com.ix.ServiceAbility.ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.log(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.log(`ConnectAbility onDisconnect element.deviceId : ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`featureAbilityTest ConnectAbility onFailed errCode : ${code}`);
    },
  },
);

featureAbility.disconnectAbility(connectId, (error) => {
  if (error && error.code !== 0) {
    console.error(`disconnectAbility fail, connectId: ${connectId}, error: ${JSON.stringify(error)}`);
  } else {
    console.log(`disconnectAbility success， connectId: ${connectId}`);
  }
});
```

#### featureAbility.disconnectAbility7+

disconnectAbility(connection: number): Promise<void>

断开与指定ServiceAbility的连接。使用Promise异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明connectionnumber是表示断开连接的ServiceAbility的ID。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connectId = featureAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'com.ix.ServiceAbility.ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.log(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.log(`ConnectAbility onDisconnect element.deviceId : ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`featureAbilityTest ConnectAbility onFailed errCode : ${code}`);
    },
  },
);

featureAbility.disconnectAbility(connectId).then(() => {
  console.log('disconnectAbility success');
}).catch((error: BusinessError)=>{
  console.error(`featureAbilityTest result errCode : ${error.code}`);
});
```

#### featureAbility.getWindow7+

getWindow(callback: AsyncCallback<window.Window>): void

获取当前Ability对应的窗口。使用callback异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

参数名类型必填说明callbackAsyncCallback<[window.Window](../../types/interfaces/Interface (Window).md)>是回调函数，返回当前Ability对应的窗口。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

featureAbility.getWindow((error: BusinessError, data: window.Window) => {
  if (error && error.code !== 0) {
    console.error(`getWindow fail, error: ${JSON.stringify(error)}`);
  } else {
    console.log(`getWindow success, data: ${typeof(data)}`);
  }
});
```

#### featureAbility.getWindow7+

getWindow(): Promise<window.Window>

获取当前Ability对应的窗口。使用Promise异步回调。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

类型说明Promise<[window.Window](../../types/interfaces/Interface (Window).md)>Promise对象，返回当前Ability对应的窗口。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

featureAbility.getWindow().then((data: window.Window) => {
  console.log(`getWindow success, data: ${typeof(data)}`);
}).catch((error: BusinessError)=>{
  console.error(`getWindow fail, error: ${JSON.stringify(error)}`);
});
```

#### AbilityWindowConfiguration7+

表示当前Ability对应的窗口配置项，使用时通过featureAbility.AbilityWindowConfiguration获取。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

名称值说明WINDOW_MODE_UNDEFINED0未定义。WINDOW_MODE_FULLSCREEN1全屏。WINDOW_MODE_SPLIT_PRIMARY100屏幕如果是水平方向表示左分屏，屏幕如果是竖直方向表示上分屏。WINDOW_MODE_SPLIT_SECONDARY101屏幕如果是水平方向表示右分屏，屏幕如果是竖直方向表示下分屏。WINDOW_MODE_FLOATING102悬浮窗。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';

featureAbility.AbilityWindowConfiguration.WINDOW_MODE_UNDEFINED
```

#### AbilityStartSetting7+

表示当前Ability对应的窗口属性，abilityStartSetting属性是一个定义为[key: string]: any的对象，key对应设定类型为：AbilityStartSetting枚举类型，value对应设定类型为：AbilityWindowConfiguration枚举类型。

使用时通过featureAbility.AbilityStartSetting获取。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

名称值说明BOUNDS_KEY'abilityBounds'窗口显示大小属性的参数名。WINDOW_MODE_KEY'windowMode'窗口显示模式属性的参数名。DISPLAY_ID_KEY'displayId'窗口显示设备ID属性的参数名。

**示例：**

```ets
import { featureAbility } from '@kit.AbilityKit';

featureAbility.AbilityStartSetting.BOUNDS_KEY
```

#### ErrorCode7+

定义启动Ability时返回的错误码。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

名称值说明NO_ERROR0没有异常。INVALID_PARAMETER-1无效的参数。ABILITY_NOT_FOUND-2找不到ABILITY。PERMISSION_DENY-3权限拒绝。

#### DataAbilityOperationType7+

表示数据的操作类型。DataAbility批量操作数据时可以通过该枚举值指定操作类型。

**模型约束**：此接口仅可在FA模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

名称值说明TYPE_INSERT1插入类型。TYPE_UPDATE2修改类型。TYPE_DELETE3删除类型。TYPE_ASSERT4声明类型。

#### Context9+

type Context = _Context

Context模块。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在FA模型下使用。

类型说明[_Context](../../topics/graphics/Context (FA模型的上下文基类).md)Context模块。

#### AppVersionInfo9+

type AppVersionInfo = _AppVersionInfo

应用版本信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在FA模型下使用。

类型说明[_AppVersionInfo](../../topics/system-services/AppVersionInfo.md)应用版本信息。

#### ProcessInfo9+

type ProcessInfo = _ProcessInfo

进程信息。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**模型约束**：此接口仅可在FA模型下使用。

类型说明[_ProcessInfo](../../topics/system-services/ProcessInfo.md)进程信息。