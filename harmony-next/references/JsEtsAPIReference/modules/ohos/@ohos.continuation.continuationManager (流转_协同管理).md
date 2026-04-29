# @ohos.continuation.continuationManager (流转/协同管理)

continuationManager模块提供了流转/协同入口管理服务能力，包括连接/取消流转管理服务，注册/解注册设备连接变化监听，拉起设备选择模块，更新连接状态。


本模块首批接口从API version 8开始支持，从API version 22开始废弃，建议使用[分布式设备管理](@ohos.distributedDeviceManager (设备管理).md)替代。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { continuationManager } from '@kit.AbilityKit';
```

#### continuationManager.register(deprecated)

register(callback: AsyncCallback<number>): void

注册流转管理服务，并获取对应的注册token，无过滤条件，使用AsyncCallback方式作为异步方法。


从API version 9开始废弃，建议使用[ondevicestatechange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__ondevicestatechange)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
continuationManager.register((err, data) => {
  if (err.code != 0) {
    console.error('register failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('register finished, ' + JSON.stringify(data));
  token = data;
});
```

#### continuationManager.register(deprecated)

register(options: [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md), callback: AsyncCallback<number>): void

连接流转管理服务，并获取对应的注册token，使用AsyncCallback方式作为异步方法。


从API version 9开始废弃，建议使用[onDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__ondevicestatechange)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
continuationManager.register(
  {
    deviceType: ["00E"]
  },
  (err, data) => {
    if (err.code != 0) {
      console.error('register failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('register finished, ' + JSON.stringify(data));
    token = data;
});
```

#### continuationManager.register(deprecated)

register(options?: [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md)): Promise<number>

连接流转管理服务，并获取对应的注册token，使用Promise方式作为异步方法。


从API version 9开始废弃，建议使用[onDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__ondevicestatechange)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise形式返回流转管理服务连接后生成的token。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
continuationManager.register(
  { deviceType: ["00E"] }).then((data) => {
    console.info('register finished, ' + JSON.stringify(data));
    token = data;
  }).catch((err: BusinessError) => {
    console.error('register failed, cause: ' + JSON.stringify(err));
});
```

#### continuationManager.registerContinuation(deprecated)

registerContinuation(callback: AsyncCallback<number>): void

注册流转管理服务，并获取对应的注册token，无过滤条件，使用AsyncCallback方式作为异步方法。


从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600003 | The number of token registration times has reached the upper limit. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.registerContinuation((err, data) => {
    if (err.code != 0) {
      console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('registerContinuation finished, ' + JSON.stringify(data));
    token = data;
  });
} catch (err) {
  console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.registerContinuation(deprecated)

registerContinuation(options: [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md), callback: AsyncCallback<number>): void

连接流转管理服务，并获取对应的注册token，使用AsyncCallback方式作为异步方法。


从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<number> | 是 | AsyncCallback形式返回流转管理服务连接后生成的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600003 | The number of token registration times has reached the upper limit. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.registerContinuation(
    {
      deviceType: ["00E"]
    },
    (err, data) => {
      if (err.code != 0) {
        console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
        return;
      }
      console.info('registerContinuation finished, ' + JSON.stringify(data));
      token = data;
  });
} catch (err) {
  console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.registerContinuation(deprecated)

registerContinuation(options?: [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md)): Promise<number>

连接流转管理服务，并获取对应的注册token，使用Promise方式作为异步方法。


从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise形式返回流转管理服务连接后生成的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600003 | The number of token registration times has reached the upper limit. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
try {
  continuationManager.registerContinuation(
    {
      deviceType: ["00E"]
    }).then((data) => {
      console.info('registerContinuation finished, ' + JSON.stringify(data));
      token = data;
    }).catch((err: BusinessError) => {
      console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
  });
} catch (err) {
  console.error('registerContinuation failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.on('deviceConnect')(deprecated)

on(type: 'deviceConnect', callback: Callback<[ContinuationResult](../../topics/misc/ContinuationResult.md)>): void

异步方法，监听设备连接状态，使用Callback形式返回连接的设备信息。


从API version 9开始废弃，建议使用[onDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__ondevicestatechange)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定值"deviceConnect"。 |
| callback | Callback<[ContinuationResult](../../topics/misc/ContinuationResult.md)> | 是 | 当用户从设备选择模块中选择设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

continuationManager.on("deviceConnect", (data) => {
  console.info('onDeviceConnect deviceId: ' + JSON.stringify(data.id));
  console.info('onDeviceConnect deviceType: ' + JSON.stringify(data.type));
  console.info('onDeviceConnect deviceName: ' + JSON.stringify(data.name));
});
```

#### continuationManager.on('deviceDisconnect')(deprecated)

on(type: 'deviceDisconnect', callback: Callback<string>): void

异步方法，监听设备断开状态，使用Callback形式返回断开的设备信息。


从API version 9开始废弃，建议使用[onDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__ondevicestatechange)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定值"deviceDisconnect"。 |
| callback | Callback<string> | 是 | 当用户从设备选择模块中断开设备时调用，返回设备ID供开发者使用。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

continuationManager.on("deviceDisconnect", (data) => {
  console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
});
```

#### continuationManager.off('deviceConnect')(deprecated)

off(type: 'deviceConnect', callback?: Callback<[ContinuationResult](../../topics/misc/ContinuationResult.md)>): void

异步方法，取消监听设备连接状态，使用Callback形式返回连接的设备信息。


从API version 9开始废弃，建议使用[offDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__offdevicestatechange)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceConnect"。 |
| callback | Callback<[ContinuationResult](../../topics/misc/ContinuationResult.md)> | 否 | 当用户从设备选择模块中选择设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

continuationManager.off("deviceConnect", (data) => {
  console.info('onDeviceConnect deviceId: ' + JSON.stringify(data.id));
  console.info('onDeviceConnect deviceType: ' + JSON.stringify(data.type));
  console.info('onDeviceConnect deviceName: ' + JSON.stringify(data.name));
});
```

#### continuationManager.off('deviceDisconnect')(deprecated)

off(type: 'deviceDisconnect', callback?: Callback<string>): void

异步方法，取消监听设备断开状态，使用Callback形式返回连接的设备信息。


从API version 9开始废弃，建议使用[offDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__offdevicestatechange)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceDisconnect"。 |
| callback | Callback<string> | 否 | 当用户从设备选择模块中断开设备时调用，返回设备ID供开发者使用。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

continuationManager.off("deviceDisconnect", (data) => {
  console.info('onDeviceDisconnect deviceId: ' + JSON.stringify(data));
});
```

#### continuationManager.on('deviceSelected')(deprecated)

on(type: 'deviceSelected', token: number, callback: Callback<Array<[ContinuationResult](../../topics/misc/ContinuationResult.md)>>): void

异步方法，监听设备连接状态，使用Callback形式返回连接的设备信息。


从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定值"deviceSelected"。 |
| token | number | 是 | 注册后的token。 |
| callback | Callback<Array<[ContinuationResult](../../topics/misc/ContinuationResult.md)>> | 是 | 当用户从设备选择模块中选择设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.on("deviceSelected", token, (data) => {
    console.info('onDeviceSelected len: ' + data.length);
    for (let i = 0; i < data.length; i++) {
      console.info('onDeviceSelected deviceId: ' + JSON.stringify(data[i].id));
      console.info('onDeviceSelected deviceType: ' + JSON.stringify(data[i].type));
      console.info('onDeviceSelected deviceName: ' + JSON.stringify(data[i].name));
    }
  });
} catch (err) {
  console.error('on failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.on('deviceUnselected')(deprecated)

on(type: 'deviceUnselected', token: number, callback: Callback<Array<[ContinuationResult](../../topics/misc/ContinuationResult.md)>>): void

异步方法，监听设备断开状态，使用Callback形式返回断开的设备信息。


从API version 9开始支持，从API version 22开始废弃，建议使用[onDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__ondevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听的事件类型，固定值"deviceUnselected"。 |
| token | number | 是 | 注册后的token。 |
| callback | Callback<Array<[ContinuationResult](../../topics/misc/ContinuationResult.md)>> | 是 | 当用户从设备选择模块中断开设备时调用，返回设备ID、设备类型和设备名称供开发者使用。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.on("deviceUnselected", token, (data) => {
    console.info('onDeviceUnselected len: ' + data.length);
    for (let i = 0; i < data.length; i++) {
      console.info('onDeviceUnselected deviceId: ' + JSON.stringify(data[i].id));
      console.info('onDeviceUnselected deviceType: ' + JSON.stringify(data[i].type));
      console.info('onDeviceUnselected deviceName: ' + JSON.stringify(data[i].name));
    }
    console.info('onDeviceUnselected finished.');
  });
} catch (err) {
  console.error('on failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.off('deviceSelected')(deprecated)

off(type: 'deviceSelected', token: number): void

取消监听设备连接状态。


从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceSelected"。 |
| token | number | 是 | 注册后的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.off("deviceSelected", token);
} catch (err) {
  console.error('off failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.off('deviceUnselected')(deprecated)

off(type: 'deviceUnselected', token: number): void

取消监听设备断开状态。


从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消监听的事件类型，固定值"deviceUnselected"。 |
| token | number | 是 | 注册后的token。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |
| 16600004 | The specified callback has been registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.off("deviceUnselected", token);
} catch (err) {
  console.error('off failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.startDeviceManager(deprecated)

startDeviceManager(token: number, callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，无过滤条件，使用AsyncCallback方式作为异步方法。


从API version 9开始废弃，建议使用[startDiscovering](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__startdiscovering)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.startDeviceManager(token, (err) => {
  if (err.code != 0) {
    console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('startDeviceManager finished. ');
});
```

#### continuationManager.startDeviceManager(deprecated)

startDeviceManager(token: number, options: [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md), callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，使用AsyncCallback方式作为异步方法。


从API version 9开始废弃，建议使用[startDiscovering](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__startdiscovering)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.startDeviceManager(
  token,
  {
    deviceType: ["00E"]
  },
  (err) => {
    if (err.code != 0) {
      console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('startDeviceManager finished. ');
});
```

#### continuationManager.startDeviceManager(deprecated)

startDeviceManager(token: number, options?: [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md)): Promise<void>

拉起设备选择模块，可显示组网内可选择设备列表信息，使用Promise方式作为异步方法。


从API version 9开始废弃，建议使用[startDiscovering](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__startdiscovering)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
continuationManager.startDeviceManager(
  token,
  {
    deviceType: ["00E"]
  }).then(() => {
    console.info('startDeviceManager finished. ');
  }).catch((err: BusinessError) => {
    console.error('startDeviceManager failed, cause: ' + JSON.stringify(err));
});
```

#### continuationManager.startContinuationDeviceManager(deprecated)

startContinuationDeviceManager(token: number, callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，无过滤条件，使用AsyncCallback方式作为异步方法。


从API version 9开始支持，从API version 22开始废弃，建议使用[startDiscovering](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__startdiscovering)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(token, (err) => {
    if (err.code != 0) {
      console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('startContinuationDeviceManager finished. ');
  });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.startContinuationDeviceManager(deprecated)

startContinuationDeviceManager(token: number, options: [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md), callback: AsyncCallback<void>): void

拉起设备选择模块，可显示组网内可选择设备列表信息，使用AsyncCallback方式作为异步方法。


从API version 9开始支持，从API version 22开始废弃，建议使用[startDiscovering](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__startdiscovering)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md) | 是 | 过滤可选择设备列表的额外参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当模块选择完成，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(
    token,
    {
      deviceType: ["00E"]
    },
    (err) => {
      if (err.code != 0) {
        console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
        return;
      }
      console.info('startContinuationDeviceManager finished. ');
  });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.startContinuationDeviceManager(deprecated)

startContinuationDeviceManager(token: number, options?: [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md)): Promise<void>

拉起设备选择模块，可显示组网内可选择设备列表信息，使用Promise方式作为异步方法。


从API version 9开始支持，从API version 22开始废弃，建议使用[startDiscovering](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__startdiscovering)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| options | [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md) | 否 | 过滤可选择设备列表的额外参数，该参数可缺省。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
try {
  continuationManager.startContinuationDeviceManager(
    token,
    {
      deviceType: ["00E"]
    }).then(() => {
      console.info('startContinuationDeviceManager finished. ');
    }).catch((err: BusinessError) => {
      console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
    });
} catch (err) {
  console.error('startContinuationDeviceManager failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.updateConnectStatus(deprecated)

updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState, callback: AsyncCallback<void>): void

通知设备选择模块，更新当前的连接状态，使用AsyncCallback方式作为异步方法。


从API version 9开始废弃，建议使用[getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | DeviceConnectState | 是 | 设备连接状态。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通知设备成功，err为undefined，否则返回错误对象。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = -1;
let deviceId: string = "test deviceId";
continuationManager.updateConnectStatus(token, deviceId, continuationManager.DeviceConnectState.CONNECTED, (err) => {
  if (err.code != 0) {
    console.error('updateConnectStatus failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('updateConnectStatus finished. ');
});
```

#### continuationManager.updateConnectStatus(deprecated)

updateConnectStatus(token: number, deviceId: string, status: DeviceConnectState): Promise<void>

通知设备选择模块，更新当前的连接状态，使用Promise方式作为异步方法。


从API version 9开始废弃，建议使用[getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | DeviceConnectState | 是 | 设备连接状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = 1;
let deviceId: string = "test deviceId";
continuationManager.updateConnectStatus(token, deviceId, continuationManager.DeviceConnectState.CONNECTED)
  .then(() => {
    console.info('updateConnectStatus finished. ');
  })
  .catch((err: BusinessError) => {
    console.error('updateConnectStatus failed, cause: ' + JSON.stringify(err));
});
```

#### continuationManager.updateContinuationState(deprecated)

updateContinuationState(token: number, deviceId: string, status: DeviceConnectState, callback: AsyncCallback<void>): void

通知设备选择模块，更新当前的连接状态，使用AsyncCallback方式作为异步方法。


从API version 9开始支持，从API version 22开始废弃，建议使用[getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | DeviceConnectState | 是 | 设备连接状态。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通知设备成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
let deviceId: string = "test deviceId";
try {
  continuationManager.updateContinuationState(token, deviceId, continuationManager.DeviceConnectState.CONNECTED, (err) => {
    if (err.code != 0) {
      console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('updateContinuationState finished. ');
  });
} catch (err) {
  console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.updateContinuationState(deprecated)

updateContinuationState(token: number, deviceId: string, status: DeviceConnectState): Promise<void>

通知设备选择模块，更新当前的连接状态，使用Promise方式作为异步方法。


从API version 9开始支持，从API version 22开始废弃，建议使用[getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| deviceId | string | 是 | 设备ID。 |
| status | DeviceConnectState | 是 | 设备连接状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = 1;
let deviceId: string = "test deviceId";
try {
  continuationManager.updateContinuationState(token, deviceId, continuationManager.DeviceConnectState.CONNECTED)
    .then(() => {
      console.info('updateContinuationState finished. ');
    })
    .catch((err: BusinessError) => {
      console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
    });
} catch (err) {
  console.error('updateContinuationState failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.unregister(deprecated)

unregister(token: number, callback: AsyncCallback<void>): void

解注册流转管理服务，传入注册时获取的token进行解注册，使用AsyncCallback方式作为异步方法。


从API version 9开始废弃，建议使用[offDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__offdevicestatechange)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当解注册成功，err为undefined，否则返回错误对象。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
continuationManager.unregister(token, (err) => {
  if (err.code != 0) {
    console.error('unregister failed, cause: ' + JSON.stringify(err));
    return;
  }
  console.info('unregister finished. ');
});
```

#### continuationManager.unregister(deprecated)

unregister(token: number): Promise<void>

解注册流转管理服务，传入注册时获取的token进行解注册，使用Promise方式作为异步方法。


从API version 9开始废弃，建议使用[offDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__offdevicestatechange)替代。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = 1;
continuationManager.unregister(token)
  .then(() => {
    console.info('unregister finished. ');
  }).catch((err: BusinessError) => {
    console.error('unregister failed, cause: ' + JSON.stringify(err));
});
```

#### continuationManager.unregisterContinuation(deprecated)

unregisterContinuation(token: number, callback: AsyncCallback<void>): void

解注册流转管理服务，传入注册时获取的token进行解注册，使用AsyncCallback方式作为异步方法。


从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当解注册成功，err为undefined，否则返回错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';

let token: number = 1;
try {
  continuationManager.unregisterContinuation(token, (err) => {
    if (err.code != 0) {
      console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
      return;
    }
    console.info('unregisterContinuation finished. ');
  });
} catch (err) {
  console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
}
```

#### continuationManager.unregisterContinuation(deprecated)

unregisterContinuation(token: number): Promise<void>

解注册流转管理服务，传入注册时获取的token进行解注册，使用Promise方式作为异步方法。


从API version 9开始支持，从API version 22开始废弃，建议使用[offDeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__offdevicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**需要权限**：ohos.permission.DISTRIBUTED_DATASYNC

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| token | number | 是 | 注册后的token。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise形式返回接口调用结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[DistributedSchedule错误码](DistributedSchedule错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16600001 | The system ability works abnormally. |
| 16600002 | The specified token or callback is not registered. |

**示例：**

```ets
import { continuationManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let token: number = -1;
try {
  continuationManager.unregisterContinuation(token).then(() => {
      console.info('unregisterContinuation finished. ');
    }).catch((err: BusinessError) => {
      console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
  });
} catch (err) {
  console.error('unregisterContinuation failed, cause: ' + JSON.stringify(err));
}
```

#### DeviceConnectState(deprecated)

设备连接状态。


从API version 22开始废弃，建议使用[DeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__devicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| IDLE | 0 | 设备连接初始状态。 |
| CONNECTING | 1 | 设备连接中状态。 |
| CONNECTED | 2 | 设备已连接状态。 |
| DISCONNECTING | 3 | 设备断开连接状态。 |

#### ContinuationMode(deprecated)

设备选择模块连接模式。


从API version 22开始废弃，建议使用[DeviceStateChange](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__devicestatechange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLLABORATION_SINGLE | 0 | 设备选择模块单选模式。 |
| COLLABORATION_MULTIPLE | 1 | 设备选择模块多选模式。 |

#### [ContinuationResult](../../topics/misc/ContinuationResult.md)(deprecated)

type [ContinuationResult](../../topics/misc/ContinuationResult.md) = [_ContinuationResult](../../topics/misc/ContinuationResult.md)

流转管理入口返回的设备信息。


从API version 10开始支持，从API version 22开始废弃，建议使用[DeviceBasicInfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__devicebasicinfo)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 类型 | 说明 |
| --- | --- |
| _[ContinuationResult](../../topics/misc/ContinuationResult.md) | 表示流转管理入口返回的设备信息。 |

#### [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md)(deprecated)

type [ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md) = [_ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md)

流转管理入口中设备选择模块所需的过滤参数。


从API version 10开始支持，从API version 22开始废弃，建议使用[DeviceBasicInfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__devicebasicinfo)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

模型约束：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.DistributedAbilityManager

| 类型 | 说明 |
| --- | --- |
| _[ContinuationExtraParams](../../topics/misc/ContinuationExtraParams.md) | 表示流转管理入口中设备选择模块所需的过滤参数。 |