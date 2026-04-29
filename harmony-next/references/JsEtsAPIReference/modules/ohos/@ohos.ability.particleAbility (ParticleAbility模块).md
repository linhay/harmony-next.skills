# @ohos.ability.particleAbility (ParticleAbility模块)

particleAbility模块提供了操作Data和Service类型的Ability的能力，包括启动、停止指定的particleAbility，获取dataAbilityHelper，连接、断连指定的ServiceAbility等。

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在FA模型下使用。

#### 使用限制

particleAbility模块用来对Data和Service类型的Ability进行操作。

#### 导入模块

```ets
import { particleAbility } from '@kit.AbilityKit';
```

#### particleAbility.startAbility

startAbility(parameter: [StartAbilityParameter](../../topics/misc/StartAbilityParameter.md), callback: AsyncCallback<void>): void

启动指定的particleAbility。使用callback异步回调。

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [StartAbilityParameter](../../topics/misc/StartAbilityParameter.md) | 是 | 表示启动的ability。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动指定的particleAbility成功，err为undefined，否则为错误对象。 |

**示例：**

```ets
import { particleAbility, wantConstant } from '@kit.AbilityKit';

particleAbility.startAbility(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: ['entity.system.home'],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.Data',
      abilityName: 'com.example.Data.EntryAbility',
      uri: ''
    },
  (error, data) => {
    if (error && error.code !== 0) {
      console.error(`startAbility fail, error: ${JSON.stringify(error)}`);
    } else {
      console.info(`startAbility success, data: ${JSON.stringify(data)}`);
    }
  },
);
```

#### particleAbility.startAbility

startAbility(parameter: [StartAbilityParameter](../../topics/misc/StartAbilityParameter.md)): Promise<void>

启动指定的particleAbility。使用Promise异步回调。

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [StartAbilityParameter](../../topics/misc/StartAbilityParameter.md) | 是 | 表示启动的ability。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ets
import { particleAbility, wantConstant } from '@kit.AbilityKit';

particleAbility.startAbility(
  {
    want:
    {
      action: 'ohos.want.action.home',
      entities: ['entity.system.home'],
      type: 'MIMETYPE',
      flags: wantConstant.Flags.FLAG_AUTH_READ_URI_PERMISSION,
      deviceId: '',
      bundleName: 'com.example.Data',
      abilityName: 'com.example.Data.EntryAbility',
      uri: ''
    },
).then(() => {
  console.info('particleAbility startAbility');
});
```

#### particleAbility.terminateSelf

terminateSelf(callback: AsyncCallback<void>): void

销毁当前particleAbility。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当销毁当前particleAbility成功，err为undefined，否则为错误对象。 |

**示例：**

```ets
import { particleAbility } from '@kit.AbilityKit';

particleAbility.terminateSelf(
  (error) => {
    if (error && error.code !== 0) {
      console.error(`terminateSelf fail, error: ${JSON.stringify(error)}`);
    }
);
```

#### particleAbility.terminateSelf

terminateSelf(): Promise<void>

销毁当前particleAbility。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ets
import { particleAbility } from '@kit.AbilityKit';

particleAbility.terminateSelf().then(() => {
  console.info('particleAbility terminateSelf');
});
```

#### particleAbility.acquire[DataAbilityHelper](../../topics/misc/DataAbilityHelper.md)

acquire[DataAbilityHelper](../../topics/misc/DataAbilityHelper.md)(uri: string): DataAbilityHelper

获取dataAbilityHelper对象。

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

跨应用访问dataAbility，对端应用需配置关联启动。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uri | string | 是 | 表示要打开的文件的路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DataAbilityHelper](../../topics/misc/DataAbilityHelper.md) | 用来协助其他Ability访问DataAbility的工具类。 |

**示例：**

```ets
import { particleAbility } from '@kit.AbilityKit';

let uri = '';
particleAbility.acquireDataAbilityHelper(uri);
```

#### particleAbility.startBackgroundRunning(deprecated)

startBackgroundRunning(id: number, request: NotificationRequest, callback: AsyncCallback<void>): void

向系统申请长时任务。使用callback异步回调。

**需要权限**：ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask


从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.startBackgroundRunning](@ohos.resourceschedule.backgroundTaskManager (后台任务管理).md#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning)替代。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 长时任务通知id号。 |
| request | NotificationRequest | 是 | 通知参数，用于显示通知栏的信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当向系统申请长时任务成功，err为undefined，否则为错误对象。 |

**示例**：

```ets
import { particleAbility, wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import notification from '@ohos.notification';

function callback(error: BusinessError, data: void) {
  if (error && error.code !== 0) {
    console.error(`Operation failed error: ${JSON.stringify(error)}`);
  } else {
    console.info(`Operation succeeded, data: ${data}`);
}

let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let id = 1;
  particleAbility.startBackgroundRunning(id, {
    content:
    {
      contentType: notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
      normal:
      {
        title: 'title',
        text: 'text'
      }
    },
    wantAgent: wantAgentObj
  }, callback);
});
```

#### particleAbility.startBackgroundRunning(deprecated)

startBackgroundRunning(id: number, request: NotificationRequest): Promise<void>

向系统申请长时任务。使用Promise异步回调。

**需要权限**：ohos.permission.KEEP_BACKGROUND_RUNNING

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask


从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.startBackgroundRunning](@ohos.resourceschedule.backgroundTaskManager (后台任务管理).md#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstartbackgroundrunning-1)替代。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 长时任务通知id号。 |
| request | NotificationRequest | 是 | 通知参数，用于显示通知栏的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```ets
import { particleAbility, wantAgent } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import notification from '@ohos.notification';

let wantAgentInfo: wantAgent.WantAgentInfo = {
  wants: [
    {
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility'
    }
  ],
  operationType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0,
  wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let id = 1;
  particleAbility.startBackgroundRunning(id, {
    content:
    {
      contentType: notification.ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
      normal:
      {
        title: 'title',
        text: 'text'
      }
    },
    wantAgent: wantAgentObj
  }).then(() => {
    console.info('Operation succeeded');
  }).catch((err: BusinessError) => {
    console.error(`Operation failed cause: ${JSON.stringify(err)}`);
  });
```

#### particleAbility.cancelBackgroundRunning(deprecated)

cancelBackgroundRunning(callback: AsyncCallback<void>): void

向系统申请取消长时任务。使用callback异步回调。

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask


从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.stopBackgroundRunning](@ohos.resourceschedule.backgroundTaskManager (后台任务管理).md#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstopbackgroundrunning)替代。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当向系统申请取消长时任务成功，err为undefined，否则为错误对象。 |

**示例**：

```ets
import { particleAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback(error: BusinessError, data: void) {
  if (error && error.code !== 0) {
    console.error(`Operation failed error: ${JSON.stringify(error)}`);
  } else {
    console.info(`Operation succeeded, data: ${data}`);
  }

particleAbility.cancelBackgroundRunning(callback);
```

#### particleAbility.cancelBackgroundRunning(deprecated)

cancelBackgroundRunning(): Promise<void>

向系统申请取消长时任务。使用Promise异步回调。

**系统能力**：SystemCapability.ResourceSchedule.BackgroundTaskManager.ContinuousTask


从API version 7开始支持，从API version 9开始废弃，建议使用[backgroundTaskManager.stopBackgroundRunning](@ohos.resourceschedule.backgroundTaskManager (后台任务管理).md#ZH-CN_TOPIC_0000002553361127__backgroundtaskmanagerstopbackgroundrunning-1)替代。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```ets
import { particleAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

particleAbility.cancelBackgroundRunning().then(() => {
  console.info('Operation succeeded');
}).catch((err: BusinessError) => {
  console.error(`Operation failed cause: ${JSON.stringify(err)}`);
});
```

#### particleAbility.connectAbility

connectAbility(request: Want, options:[ConnectOptions](../../topics/misc/ConnectOptions.md)): number

将当前ability与指定的ServiceAbility进行连接。

组件启动规则详见：[组件启动规则（FA模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa)。

跨应用连接serviceAbility，对端应用需配置关联启动。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | Want | 是 | 表示被连接的ServiceAbility。 |
| options | [ConnectOptions](../../topics/misc/ConnectOptions.md) | 是 | 连接回调方法。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 连接的ServiceAbility的ID(ID从0开始自增，每连接成功一次ID加1)。 |

**示例**：

```ets
import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
    },
);

particleAbility.disconnectAbility(connId).then((data) => {
  console.info(`data: ${data}`);
}).catch((error: BusinessError) => {
  console.error(`particleAbilityTest result errCode: ${error.code}`);
});
```

#### particleAbility.disconnectAbility

disconnectAbility(connection: number, callback:AsyncCallback<void>): void

断开当前ability与指定ServiceAbility的连接。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 表示断开连接的ServiceAbility的ID。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当断开当前ability与指定ServiceAbility的连接成功，err为undefined，否则为错误对象。 |

**示例**：

```ets
import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
  },
);

particleAbility.disconnectAbility(connId, (err) => {
  console.error(`particleAbilityTest disconnectAbility err: ${JSON.stringify(err)}`);
});
```

#### particleAbility.disconnectAbility

disconnectAbility(connection: number): Promise<void>

断开当前ability与指定ServiceAbility的连接。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 表示断开连接的ServiceAbility的ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例**：

```ets
import { particleAbility } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { BusinessError } from '@kit.BasicServicesKit';

let connId = particleAbility.connectAbility(
  {
    bundleName: 'com.ix.ServiceAbility',
    abilityName: 'ServiceAbilityA',
  },
  {
    onConnect: (element, remote) => {
      console.info(`ConnectAbility onConnect remote is proxy: ${(remote instanceof rpc.RemoteProxy)}`);
    },
    onDisconnect: (element) => {
      console.info(`ConnectAbility onDisconnect element.deviceId: ${element.deviceId}`);
    },
    onFailed: (code) => {
      console.error(`particleAbilityTest ConnectAbility onFailed errCode: ${code}`);
    },
);

particleAbility.disconnectAbility(connId).then(() => {
  console.info('disconnectAbility success');
}).catch((error: BusinessError) => {
  console.error(`particleAbilityTest result errCode : ${error.code}`);
});
```

#### ErrorCode

定义启动Ability时返回的错误码。

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVALID_PARAMETER | -1 | 无效的参数。 |