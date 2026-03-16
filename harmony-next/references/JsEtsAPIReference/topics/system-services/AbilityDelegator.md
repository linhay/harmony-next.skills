# AbilityDelegator

AbilityDelegator模块可以通过[AbilityMonitor](AbilityMonitor.md)实例来监听和管理[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)生命周期的变化。例如获取UIAbility当前状态（如是否已创建/是否在前台等）、查询当前获焦的UIAbility、等待UIAbility进入某个生命周期节点（如等待UIAbility进入onForeground）、启动指定UIAbility、设置超时机制等功能。

AbilityDelegator可以通过[getAbilityDelegator](../../modules/ohos/@ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry).md#ZH-CN_TOPIC_0000002497605688__abilitydelegatorregistrygetabilitydelegator)方法获取。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在[单元测试框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines)中使用。

#### 导入模块

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
```

#### AbilityDelegator

#### addAbilityMonitor9+

addAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void

添加AbilityMonitor实例。使用callback异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityMonitor](AbilityMonitor.md)是[AbilityMonitor](AbilityMonitor.md)实例。callbackAsyncCallback<void>是回调函数。当添加AbilityMonitor实例成功，err为undefined，否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling AddAbilityMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}`);
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityMonitor(monitor, (error: BusinessError) => {
  console.error(`addAbilityMonitor fail, error: ${JSON.stringify(error)}`);
});
```

#### addAbilityMonitor9+

addAbilityMonitor(monitor: AbilityMonitor): Promise<void>

添加AbilityMonitor实例。使用Promise异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityMonitor](AbilityMonitor.md)是[AbilityMonitor](AbilityMonitor.md)实例。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling AddAbilityMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};
let abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

abilityDelegator.addAbilityMonitor(monitor).then(() => {
  console.info('addAbilityMonitor promise');
});
```

#### addAbilityMonitorSync10+

addAbilityMonitorSync(monitor: AbilityMonitor): void

同步添加AbilityMonitor实例。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityMonitor](AbilityMonitor.md)是[AbilityMonitor](AbilityMonitor.md)实例。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling AddAbilityMonitorSync failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityMonitorSync(monitor);
```

#### removeAbilityMonitor9+

removeAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<void>): void

删除已经添加的AbilityMonitor实例。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityMonitor](AbilityMonitor.md)是[AbilityMonitor](AbilityMonitor.md)实例。callbackAsyncCallback<void>是回调函数。当删除已经添加的AbilityMonitor实例成功，err为undefined，否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling RemoveAbilityMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

function onAbilityCreateCallback(data: UIAbility) {
    console.info('onAbilityCreateCallback');
}

let monitor: abilityDelegatorRegistry.AbilityMonitor = {
    abilityName: 'abilityName',
    onAbilityCreate: onAbilityCreateCallback
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitor(monitor, (error: BusinessError) => {
    console.error(`removeAbilityMonitor fail, error: ${JSON.stringify(error)}`);
});
```

#### removeAbilityMonitor9+

removeAbilityMonitor(monitor: AbilityMonitor): Promise<void>

删除已经添加的AbilityMonitor实例。使用Promise异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityMonitor](AbilityMonitor.md)是[AbilityMonitor](AbilityMonitor.md)实例。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling RemoveAbilityMonitor failed.

- 示例

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitor(monitor).then(() => {
  console.info('removeAbilityMonitor promise');
});
```

#### removeAbilityMonitorSync10+

removeAbilityMonitorSync(monitor: AbilityMonitor): void

同步删除已经添加的AbilityMonitor实例。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityMonitor](AbilityMonitor.md)是[AbilityMonitor](AbilityMonitor.md)实例。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling RemoveAbilityMonitorSync failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityMonitorSync(monitor);
```

#### waitAbilityMonitor9+

waitAbilityMonitor(monitor: AbilityMonitor, callback: AsyncCallback<UIAbility>): void

等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用callback异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityMonitor](AbilityMonitor.md)是[AbilityMonitor](AbilityMonitor.md)实例。callbackAsyncCallback<[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)>是回调函数。当等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期成功，err为undefined，data为获取到的Ability实例，否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling WaitAbilityMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}`);
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor, (error: BusinessError, data: UIAbility) => {
  if (error) {
    console.error(`waitAbilityMonitor fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`waitAbilityMonitor success, data: ${JSON.stringify(data)}`);
  }
});
```

#### waitAbilityMonitor9+

waitAbilityMonitor(monitor: AbilityMonitor, timeout: number, callback: AsyncCallback<UIAbility>): void

设置等待时间，等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用callback异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityMonitor](AbilityMonitor.md)是[AbilityMonitor](AbilityMonitor.md)实例。timeoutnumber是最大等待时间，单位毫秒（ms），默认值为5000毫秒。callbackAsyncCallback<[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)>是表示指定的回调方法。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling WaitAbilityMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let timeout = 100;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info(`onAbilityCreateCallback, data: ${JSON.stringify(data)}.`);
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor, timeout, (error: BusinessError, data: UIAbility) => {
  if (error && error.code !== 0) {
    console.error(`waitAbilityMonitor fail, error: ${JSON.stringify(error)}`);
  } else {
    console.info(`waitAbilityMonitor success, data: ${JSON.stringify(data)}`);
  }
});
```

#### waitAbilityMonitor9+

waitAbilityMonitor(monitor: AbilityMonitor, timeout?: number): Promise<UIAbility>

设置等待时间，等待与AbilityMonitor实例匹配的Ability到达OnCreate生命周期，并返回Ability实例。使用Promise异步回调。不支持多线程并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityMonitor](AbilityMonitor.md)是[AbilityMonitor](AbilityMonitor.md)实例。timeoutnumber否最大等待时间，单位毫秒（ms），默认值为5000毫秒。

**返回值：**

类型说明Promise<[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)>Promise对象，返回Ability实例。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling WaitAbilityMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let monitor: abilityDelegatorRegistry.AbilityMonitor = {
  abilityName: 'abilityName',
  onAbilityCreate: onAbilityCreateCallback
};

function onAbilityCreateCallback(data: UIAbility) {
  console.info('onAbilityCreateCallback');
}

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityMonitor(monitor).then((data: UIAbility) => {
  console.info('waitAbilityMonitor promise');
});
```

#### getAppContext9+

getAppContext(): Context

获取应用Context。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明[Context](../graphics/Context (Stage模型的上下文基类).md)应用[Context](../graphics/Context (Stage模型的上下文基类).md)。

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

let context = abilityDelegator.getAppContext();
```

#### getAbilityState9+

getAbilityState(ability: UIAbility): number

获取指定ability的生命周期状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明ability[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)是指定Ability对象。

**返回值：**

类型说明number指定ability的生命周期状态。状态枚举值使用[AbilityLifecycleState](../../modules/ohos/@ohos.app.ability.abilityDelegatorRegistry (AbilityDelegatorRegistry).md#ZH-CN_TOPIC_0000002497605688__abilitylifecyclestate)。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  let state = abilityDelegator.getAbilityState(ability);
  console.info('getAbilityState ${state}');
});
```

#### getCurrentTopAbility9+

getCurrentTopAbility(callback: AsyncCallback<UIAbility>): void

获取当前应用顶部Ability。使用callback异步回调。不支持Worker线程调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)>是回调函数。当获取当前应用顶部Ability成功，err为undefined，data为获取到的Ability实例；否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling GetCurrentTopAbility failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
});
```

#### getCurrentTopAbility9+

getCurrentTopAbility(): Promise<UIAbility>

获取当前应用顶部Ability。使用Promise异步回调。不支持Worker线程调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

类型说明Promise<[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)>Promise对象，返回前应用顶部Ability。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息16000100Calling GetCurrentTopAbility failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility().then((data: UIAbility) => {
  console.info('getCurrentTopAbility promise');
  ability = data;
});
```

#### startAbility9+

startAbility(want: Want, callback: AsyncCallback<void>): void

启动指定Ability。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明want[Want](../../modules/ohos/@ohos.app.ability.Want (Want).md)是启动Ability参数。callbackAsyncCallback<void>是回调函数。当启动指定Ability成功，err为undefined，否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000001The specified ability does not exist.16000002Incorrect ability type.16000004Cannot start an invisible component.16000005The specified process does not have the permission.16000006Cross-user operations are not allowed.16000008The crowdtesting application expires.16000009An ability cannot be started or stopped in Wukong mode.16000010The call with the continuation and prepare continuation flag is forbidden.16000011The context does not exist.16000012The application is controlled.16000013The application is controlled by EDM.16000050Internal error.16000053The ability is not on the top of the UI.16000055Installation-free timed out.16200001The caller has been released.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let want: Want = {
  bundleName: 'bundleName',
  abilityName: 'abilityName'
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.startAbility(want, (err: BusinessError, data: void) => {
  console.info('startAbility callback');
});
```

#### startAbility9+

startAbility(want: Want): Promise<void>

启动指定Ability。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明want[Want](../../modules/ohos/@ohos.app.ability.Want (Want).md)是启动Ability参数。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000001The specified ability does not exist.16000002Incorrect ability type.16000004Cannot start an invisible component.16000005The specified process does not have the permission.16000006Cross-user operations are not allowed.16000008The crowdtesting application expires.16000009An ability cannot be started or stopped in Wukong mode.16000010The call with the continuation and prepare continuation flag is forbidden.16000011The context does not exist.16000012The application is controlled.16000013The application is controlled by EDM.16000050Internal error.16000053The ability is not on the top of the UI.16000055Installation-free timed out.16200001The caller has been released.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { Want } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let want: Want = {
  bundleName: 'bundleName',
  abilityName: 'abilityName'
};

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.startAbility(want).then((data: void) => {
  console.info('startAbility promise');
});
```

#### doAbilityForeground9+

doAbilityForeground(ability: UIAbility, callback: AsyncCallback<void>): void

调度指定Ability生命周期状态到Foreground状态。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明ability[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)是指定Ability对象。callbackAsyncCallback<void>是回调函数。当调度指定Ability生命周期状态到Foreground状态成功，err为undefined，否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling DoAbilityForeground failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityForeground(ability, (err: BusinessError) => {
    console.info("doAbilityForeground callback");
  });
});
```

#### doAbilityForeground9+

doAbilityForeground(ability: UIAbility): Promise<void>

调度指定Ability生命周期状态到Foreground状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明ability[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)是指定Ability对象。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling DoAbilityForeground failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityForeground(ability).then(() => {
    console.info("doAbilityForeground promise");
  });
});
```

#### doAbilityBackground9+

doAbilityBackground(ability: UIAbility, callback: AsyncCallback<void>): void

调度指定Ability生命周期状态到Background状态。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明ability[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)是指定Ability对象。callbackAsyncCallback<void>是回调函数。当调度指定Ability生命周期状态到Background状态成功，err为undefined，否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling DoAbilityBackground failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityBackground(ability, (err: BusinessError) => {
    console.info("doAbilityBackground callback");
  });
});
```

#### doAbilityBackground9+

doAbilityBackground(ability: UIAbility): Promise<void>

调度指定Ability生命周期状态到Background状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明ability[UIAbility](../../modules/ohos/@ohos.app.ability.UIAbility (带界面的应用组件).md)是指定Ability对象。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling DoAbilityBackground failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let ability: UIAbility;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.getCurrentTopAbility((err: BusinessError, data: UIAbility) => {
  console.info('getCurrentTopAbility callback');
  ability = data;
  abilityDelegator.doAbilityBackground(ability).then(() => {
    console.info("doAbilityBackground promise");
  });
});
```

#### printSync9+

printSync(msg: string): void

打印日志信息到单元测试终端控制台。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明msgstring是日志字符串。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.printSync(msg);
```

#### print

print(msg: string, callback: AsyncCallback<void>): void

打印日志信息到单元测试终端控制台。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明msgstring是日志字符串。callbackAsyncCallback<void>是回调函数。当打印日志信息到单元测试终端控制台成功，err为undefined，否则为错误对象。

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.print(msg, (err: BusinessError) => {
  console.info('print callback');
});
```

#### print

print(msg: string): Promise<void>

打印日志信息到单元测试终端控制台。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明msgstring是日志字符串。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.print(msg).then(() => {
  console.info('print promise');
});
```

#### executeShellCommand

executeShellCommand(cmd: string, callback: AsyncCallback<ShellCmdResult>): void

执行指定的shell命令。使用callback异步回调。

仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明cmdstring是shell命令字符串。callbackAsyncCallback<[ShellCmdResult](../misc/ShellCmdResult.md#ZH-CN_TOPIC_0000002529445657__shellcmdresult-1)>是回调函数。当执行指定的shell命令成功，err为undefined，data为获取到的执行结果；否则为错误对象。

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(cmd, (err: BusinessError, data: abilityDelegatorRegistry.ShellCmdResult) => {
  console.info('executeShellCommand callback');
});
```

#### executeShellCommand

executeShellCommand(cmd: string, timeoutSecs: number, callback: AsyncCallback<ShellCmdResult>): void

指定超时时间，并执行指定的shell命令。使用callback异步回调。

仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明cmdstring是shell命令字符串。timeoutSecsnumber是设定命令超时时间，单位秒（s）。callbackAsyncCallback<[ShellCmdResult](../misc/ShellCmdResult.md#ZH-CN_TOPIC_0000002529445657__shellcmdresult-1)>是回调函数。当执行指定的shell命令成功，err为undefined，data为获取到的执行结果；否则为错误对象。

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(cmd, timeout, (err: BusinessError, data: abilityDelegatorRegistry.ShellCmdResult) => {
  console.info('executeShellCommand callback');
});
```

#### executeShellCommand

executeShellCommand(cmd: string, timeoutSecs?: number): Promise<ShellCmdResult>

指定超时时间，并执行指定的shell命令。使用Promise异步回调。

仅支持如下shell命令：aa, bm, cp, mkdir, rm, uinput, hilog, ppwd, echo, uitest, acm, hidumper, wukong, pkill, ps, pidof

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明cmdstring是shell命令字符串。timeoutSecsnumber否设定命令超时时间，单位秒（s）。

**返回值：**

类型说明Promise<[ShellCmdResult](../misc/ShellCmdResult.md#ZH-CN_TOPIC_0000002529445657__shellcmdresult-1)>Promise对象，返回Shell命令执行结果[ShellCmdResult](../misc/ShellCmdResult.md#ZH-CN_TOPIC_0000002529445657__shellcmdresult-1)对象。

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let cmd = 'cmd';
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.executeShellCommand(cmd, timeout).then((data) => {
  console.info('executeShellCommand promise');
});
```

#### finishTest9+

finishTest(msg: string, code: number, callback: AsyncCallback<void>): void

结束测试并打印日志信息到单元测试终端控制台。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明msgstring是日志字符串。codenumber是日志码。callbackAsyncCallback<void>是回调函数。当结束测试并打印日志信息到单元测试终端控制台成功，err为undefined，否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling FinishTest failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.finishTest(msg, 0, (err: BusinessError) => {
  console.info('finishTest callback');
});
```

#### finishTest9+

finishTest(msg: string, code: number): Promise<void>

结束测试并打印日志信息到单元测试终端控制台。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明msgstring是日志字符串。codenumber是日志码。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling FinishTest failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let msg = 'msg';

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.finishTest(msg, 0).then(() => {
  console.info('finishTest promise');
});
```

#### addAbilityStageMonitor9+

addAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void

添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityStageMonitor](AbilityStageMonitor.md)是[AbilityStageMonitor](AbilityStageMonitor.md) 实例。callbackAsyncCallback<void>是回调函数。当添加一个用于监视指定AbilityStage的生命周期状态更改的AbilityStageMonitor对象成功，err为undefined，否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling AddAbilityStageMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError) => {
  console.info('addAbilityStageMonitor callback');
});
```

#### addAbilityStageMonitor9+

addAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>

添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityStageMonitor](AbilityStageMonitor.md)是[AbilityStageMonitor](AbilityStageMonitor.md) 实例。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling AddAbilityStageMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}).then(() => {
  console.info('addAbilityStageMonitor promise');
});
```

#### addAbilityStageMonitorSync10+

addAbilityStageMonitorSync(monitor: AbilityStageMonitor): void

同步添加一个AbilityStageMonitor对象，用于监视指定AbilityStage的生命周期状态更改。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityStageMonitor](AbilityStageMonitor.md)是[AbilityStageMonitor](AbilityStageMonitor.md) 实例。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling AddAbilityStageMonitorSync failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.addAbilityStageMonitorSync({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
});
```

#### removeAbilityStageMonitor9+

removeAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<void>): void

从应用程序内存中删除指定的AbilityStageMonitor对象。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityStageMonitor](AbilityStageMonitor.md)是[AbilityStageMonitor](AbilityStageMonitor.md) 实例。callbackAsyncCallback<void>是回调函数。当从应用程序内存中删除指定的AbilityStageMonitor对象成功，err为undefined，否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling RemoveAbilityStageMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError) => {
  console.info('removeAbilityStageMonitor callback');
});
```

#### removeAbilityStageMonitor9+

removeAbilityStageMonitor(monitor: AbilityStageMonitor): Promise<void>

从应用程序内存中删除指定的AbilityStageMonitor对象。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityStageMonitor](AbilityStageMonitor.md)是[AbilityStageMonitor](AbilityStageMonitor.md) 实例。

**返回值：**

类型说明Promise<void>Promise对象。无返回结果的Promise对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling RemoveAbilityStageMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}).then(() => {
  console.info('removeAbilityStageMonitor promise');
});
```

#### removeAbilityStageMonitorSync10+

removeAbilityStageMonitorSync(monitor: AbilityStageMonitor): void

同步从应用程序内存中删除指定的AbilityStageMonitor对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityStageMonitor](AbilityStageMonitor.md)是[AbilityStageMonitor](AbilityStageMonitor.md) 实例。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling RemoveAbilityStageMonitorSync failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.removeAbilityStageMonitorSync({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
});
```

#### waitAbilityStageMonitor9+

waitAbilityStageMonitor(monitor: AbilityStageMonitor, callback: AsyncCallback<AbilityStage>): void

返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityStageMonitor](AbilityStageMonitor.md)是[AbilityStageMonitor](AbilityStageMonitor.md) 实例。callbackAsyncCallback<AbilityStage>是回调函数。当等待并返回与给定AbilityStageMonitor中设置的条件匹配的AbilityStage对象的操作成功，err为undefined，data为获取到的[AbilityStage](../../modules/ohos/@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)对象；否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling WaitAbilityStageMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, (err: BusinessError, data: AbilityStage) => {
  console.info('waitAbilityStageMonitor callback');
});
```

#### waitAbilityStageMonitor9+

waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout?: number): Promise<AbilityStage>

返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象，支持设置超时最大等待时间。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityStageMonitor](AbilityStageMonitor.md)是[AbilityStageMonitor](AbilityStageMonitor.md) 实例。timeoutnumber否超时最大等待时间，单位毫秒（ms），默认值为5000毫秒。

**返回值：**

类型说明Promise<AbilityStage>Promise对象，返回[AbilityStage](../../modules/ohos/@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling WaitAbilityStageMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { AbilityStage } from '@kit.AbilityKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}).then((data: AbilityStage) => {
  console.info('waitAbilityStageMonitor promise');
});
```

#### waitAbilityStageMonitor9+

waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout: number, callback: AsyncCallback<AbilityStage>): void

在指定的超时最大等待时间内，返回与AbilityStageMonitor中设置条件相匹配的AbilityStage对象。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明monitor[AbilityStageMonitor](AbilityStageMonitor.md)是[AbilityStageMonitor](AbilityStageMonitor.md) 实例。timeoutnumber是超时最大等待时间，单位毫秒（ms），默认值为5000毫秒。callbackAsyncCallback<AbilityStage>是回调函数。当等待并返回与给定AbilityStageMonitor中设置的条件匹配的AbilityStage对象的操作成功，err为undefined，data为获取到的[AbilityStage](../../modules/ohos/@ohos.app.ability.AbilityStage (AbilityStage组件管理器).md)对象；否则为错误对象。

**错误码**：

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000100Calling WaitAbilityStageMonitor failed.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';
import { AbilityStage } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;
let timeout = 100;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.waitAbilityStageMonitor({
  moduleName: 'moduleName',
  srcEntrance: 'srcEntrance',
}, timeout, (err: BusinessError, data: AbilityStage) => {
  console.info('waitAbilityStageMonitor callback');
});
```

#### setMockList11+

setMockList(mockList: Record<string, string>): void

设置模块的mock替换关系。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

参数名类型必填说明mockListRecord<string, string>是模块mock替换关系的键值对象，其中key为待替换的目标路径，value为用于替换的mock实现文件的路径。

**错误码：**

以下错误码详细介绍请参考[通用错误码](../../errors/通用错误码.md)和[元能力子系统错误码](../../errors/元能力子系统错误码.md)。

错误码ID错误信息401Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types.16000050Internal error.

**示例：**

```ets
import { abilityDelegatorRegistry } from '@kit.TestKit';

let mockList: Record<string, string> = {
  '@ohos.router': 'src/main/mock/ohos/router.mock',
  'common.time': 'src/main/mock/common/time.mock',
};
let abilityDelegator: abilityDelegatorRegistry.AbilityDelegator;

abilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
abilityDelegator.setMockList(mockList);
```