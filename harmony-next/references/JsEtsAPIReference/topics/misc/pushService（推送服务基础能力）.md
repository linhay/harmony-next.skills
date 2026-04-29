# pushService（推送服务基础能力）

本模块提供Push Kit（推送服务）的基础能力，包括获取和删除推送服务Token、绑定和解绑账号、接收场景化消息、注册和解除注册token更新，以及注册和解除注册分布式消息接收事件监听的功能。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Push.PushService

起始版本： 4.0.0(10)

**导入模块**

```ets
import { pushService } from '@kit.PushKit';
```

**pushService.getToken**

getToken(callback: AsyncCallback<string>): void

获取推送服务的Token，使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

系统能力： SystemCapability.Push.PushService

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。Token获取成功时，字符长度为112，err为undefined；Token获取失败时返回错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |
| 1000900012 | Push rights are not activated. |
| 1000900013 | Cross-location application is not allowed to obtain the token. |
| 1000900014 | The device does not support getting token. |

示例：

```ets
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  pushService.getToken((err: BusinessError, data: string) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in getting push token');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', e.code, e.message);
}
```

**pushService.getToken**

getToken(): Promise<string>

获取推送服务的Token，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。返回Token，字符长度为112。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |
| 1000900012 | Push rights are not activated. |
| 1000900013 | Cross-location application is not allowed to obtain the token. |
| 1000900014 | The device does not support getting token. |

示例：

```ets
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  pushService.getToken().then((data: string) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting push token.');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to get push token: %{public}d %{public}s', e.code, e.message);
}
```

**pushService.deleteToken**

deleteToken(callback: AsyncCallback<void>): void

删除推送服务的Token，使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除Token成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |

示例：

```ets
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  pushService.deleteToken((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in deleting push token.');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', e.code, e.message);
}
```

**pushService.deleteToken**

deleteToken(): Promise<void>

删除推送服务的Token，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |

示例：

```ets
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  pushService.deleteToken().then(() => {
    hilog.info(0x0000, 'testTag', 'Succeeded in deleting push token.');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to delete push token: %{public}d %{public}s', e.code, e.message);
}
```

**pushService.bindAppProfileId**

bindAppProfileId(appProfileType: pushCommon.AppProfileType, appProfileId: string, callback: AsyncCallback<void>): void

绑定应用内账号匿名标识，使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appProfileType | pushCommon.AppProfileType | 是 | 绑定账号类型，分为华为账号和应用账号。 |
| appProfileId | string | 是 | 账号匿名标识，不可为空字符串。不建议使用真实的账号id，推荐使用账号id自行生成对应的匿名标识，能与该账号id建立唯一映射关系即可，生成算法无限制。最大长度为64。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当绑定应用内账号成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900015 | The number of bound profile-app relationships exceeds the maximum. |
| 1000900016 | The os distributed account is not logged in. |

示例：

```ets
import { pushService, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义需要绑定的profileId
const profileId: string = '1****9';
try {
  pushService.bindAppProfileId(pushCommon.AppProfileType.PROFILE_TYPE_APPLICATION_ACCOUNT, profileId, (err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in binding app profile id.');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', e.code, e.message);
}
```

**pushService.bindAppProfileId**

bindAppProfileId(appProfileType: pushCommon.AppProfileType, appProfileId: string): Promise<void>

绑定应用内账号匿名标识，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、PC/2in1、Tablet、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appProfileType | pushCommon.AppProfileType | 是 | 绑定账号类型，分为华为账号和应用账号。 |
| appProfileId | string | 是 | 账号匿名标识，不可为空字符串。不建议使用真实的账号id，推荐使用账号id自行生成对应的匿名标识，能与该账号id建立唯一映射关系即可，生成算法无限制。最大长度为64。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900015 | The number of bound profile-app relationships exceeds the maximum. |
| 1000900016 | The os distributed account is not logged in. |

示例：

```ets
import { pushService, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义需要绑定的profileId
const profileId = '1****9';
try {
  // 绑定应用账号
  pushService.bindAppProfileId(pushCommon.AppProfileType.PROFILE_TYPE_APPLICATION_ACCOUNT, profileId).then(() => {
    hilog.info(0x0000, 'testTag', 'Succeeded in binding app profile id.');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', e.code, e.message);
}
```

**pushService.unbindAppProfileId**

unbindAppProfileId(appProfileId: string, callback: AsyncCallback<void>): void

解绑应用内账号匿名标识，使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appProfileId | string | 是 | 账号匿名标识，配置为调用bindAppProfileId()时设置的appProfileId。最大长度为64。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当解绑应用内账号成功，err为undefined，否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |

示例：

```ets
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义需要解绑的profileId
const profileId: string = '1****9';
try {
  pushService.unbindAppProfileId(profileId, (err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in unbinding app profile id.');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', e.code, e.message);
}
```

**pushService.unbindAppProfileId**

unbindAppProfileId(appProfileId: string): Promise<void>

解绑应用内账号匿名标识，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appProfileId | string | 是 | 账号匿名标识，配置为调用bindAppProfileId()时设置的appProfileId。最大长度为64。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |

示例：

```ets
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 定义需要解绑的profileId
const profileId: string = '1****9';
try {
  pushService.unbindAppProfileId(profileId).then(() => {
    hilog.info(0x0000, 'testTag', 'Succeeded in unbinding app profile id.');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to unbind app profile id: %{public}d %{public}s', e.code, e.message);
}
```

**pushService.PushType**

type PushType = 'DEFAULT' |'IM' | 'VoIP' | 'BACKGROUND' | 'EMERGENCY'

场景化消息类型，取值类型为下表类型中的并集。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 5.0.2(14)

| 类型 | 说明 |
| --- | --- |
| 'DEFAULT' | 通知消息场景。 |
| 'IM' | 语音播报消息场景。 |
| 'VoIP' | 应用内通话消息场景。 |
| 'BACKGROUND' | 后台消息场景。 |
| 'EMERGENCY' | 紧急事件消息场景。 |

**pushService.receiveMessage**

receiveMessage(pushType: PushType, ability: Ability, onMessage: Callback<pushCommon.PushPayload>): void

接收Push场景化消息。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：对于5.1.0(18)以前版本，该接口在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。对于5.1.0(18)版本，该接口在Phone、Tablet、PC/2in1、Wearable中可正常使用，在其他设备类型中无效果。对于5.1.1(19)及之后版本，该接口在Phone、Tablet、PC/2in1、Wearable、TV中均可正常使用。

起始版本： 4.0.0(10)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pushType | PushType | 是 | 场景化消息类型。 说明： · pushService.PushType中EMERGENCY（紧急事件消息场景）起始版本：5.0.0(12)。本场景仅为地震灾害等特殊场景使用。 · pushService.PushType中DEFAULT（通知消息场景）起始版本：5.0.2(14)。调用示例代码请参考应用在前台时处理通知消息中步骤3。 · IM（语音播报消息场景）调用示例代码请参考开发步骤中步骤3。 · VoIP（应用内通话消息场景） 调用示例代码请参考开发步骤中步骤2。 · BACKGROUND（后台消息场景） 调用示例代码请参考开发步骤中步骤5。 |
| ability | Ability | 是 | UIAbility。 |
| onMessage | Callback<pushCommon.PushPayload> | 是 | 回调函数，返回接收场景化消息的数据。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900005 | Messages of the same push type cannot be received repeatedly. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { pushService, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 无需新增UIAbility，在原有UIAbility的onCreate方法中调用即可。以PushMessageAbility为例
export default class PushMessageAbility extends UIAbility {
  // onCreate()为同步接口，不支持异步回调
  onCreate(): void {
    try {
      // receiveMessage()不能放在异步方法之后，否则可能影响消息接收
      // 注册BACKGROUND场景化消息
      pushService.receiveMessage('BACKGROUND', this, (data: pushCommon.PushPayload) => {
        // process message，并建议对Callback进行try-catch
        try {
          hilog.info(0x0000, 'testTag', 'Receive background message : %{public}s', JSON.stringify(data));
        } catch (e) {
          let errRes: BusinessError = e as BusinessError;
          hilog.error(0x0000, 'testTag', 'Failed to process data: %{public}d %{public}s', errRes.code, errRes.message);
        }
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to receive message: %{public}d %{public}s', e.code, e.message);
    }
```

**pushService.on('tokenUpdate')**

on(type: 'tokenUpdate', ability: Ability, callback: Callback<string>): void

注册token更新，使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该接口在Wearable中可正常调用，在其他设备类型中无效果。

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tokenUpdate'，即token更新事件。 |
| ability | Ability | 是 | UIAbility，包含UI界面的应用组件。 |
| callback | Callback<string> | 是 | 回调函数，返回token更新的数据。Token长度为112。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 无需新增UIAbility，在原有UIAbility的onCreate方法中调用即可。以PushMessageAbility为例
export default class PushMessageAbility extends UIAbility {
  onCreate(): void {
    const callBack = (data: string) => {
      try {
        hilog.info(0x0000, 'testTag', 'update token: %{public}s', data);
      } catch (e) {
        let err: BusinessError = e as BusinessError;
        hilog.error(0x0000, 'testTag', 'Failed to update data: %{public}d %{public}s', err.code, err.message);
      }

    try {
      // 注册token更新回调场景
      pushService.on('tokenUpdate', this, callBack);
      hilog.info(0x0000, 'testTag', 'Register on success');
    } catch (e) {
      let err: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'testTag', 'Register on error: %{public}d %{public}s', err.code, err.message);
    }
```

**pushService.off('tokenUpdate')**

off(type: 'tokenUpdate', callback?: Callback<string>): void

解除注册token更新，使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该接口在Wearable中可正常调用，在其他设备类型中无效果。

起始版本： 5.1.0(18)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tokenUpdate'，即token更新事件。 |
| callback | Callback<string> | 否 | 回调函数， 用于取消注册tokenUpdate监听事件。 注：若取消注册时不传入callback，则会取消注册tokenUpdate事件下所有的callback。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 无需新增UIAbility，在原有UIAbility的onDestroy方法中调用即可。以PushMessageAbility为例
export default class PushMessageAbility extends UIAbility {
  onDestroy(): void {
    try {
      // 解除注册token更新回调场景
      pushService.off('tokenUpdate');
      hilog.info(0x0000, 'testTag', 'Register off success');
    } catch (e) {
      let err: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'testTag', 'Register off error: %{public}d %{public}s', err.code, err.message);
    }
```

**pushService.on('distributedMessageReceive')**

on(type: 'distributedMessageReceive', callee: Callee, callback: DistributedMessageCallback): void

注册分布式消息接收事件监听，使用callback异步回调。应用需要在UIAbility的onCreate()方法进行注册，每个应用只能注册一次。该UIAbility对应action为action.ohos.push.distribute.listener。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

若调用接收场景化消息接口（[pushService.receiveMessage](#ZH-CN_TOPIC_0000002553202477__pushservicereceivemessage)）和注册分布式消息事件在同一个UIAbility中，则action.ohos.push.distribute.listener和action.ohos.push.listener定义在同一个actions数组中，否则分别定义在对应UIAbility中的actions中。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'distributedMessageReceive'，即分布式消息接收事件。 |
| callee | Callee | 是 | 通用组件服务端注册和解除客户端Caller通知送信的callback接口，从UIAbility中获取。 |
| callback | DistributedMessageCallback | 是 | 回调函数，注册分布式消息接收事件监听的回调，在收到分布式消息后异步执行。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900031 | The same type of callback can be registered only once. |
| 1000900001 | System internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { pushService, pushCommon } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class PushMessageAbility extends UIAbility {
  private callback: pushService.DistributedMessageCallback = async (data:  pushCommon.PushPayload) => {
    let resultCode = pushService.ResultCode.SUCCESS;
    try {
      hilog.info(0x0000, 'testTag', 'Distribute message: %{public}s', JSON.stringify(data));
      // 处理业务逻辑，如将数据内容发布到穿戴设备上等
    } catch (e) {
      resultCode = pushService.ResultCode.FAILED;
      let errRes: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to receive distribute data: %{public}d %{public}s', errRes.code, errRes.message);
    }
    // 处理结束后，返回执行结果
    return { resultCode };
  };

  onCreate(): void {
    try {
      // 注册distributeMessageReceive分布式消息接收回调场景
      pushService.on('distributedMessageReceive', this.callee, this.callback);
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Register on error: %{public}d %{public}s', e.code, e.message);
    }
```

**pushService.off('distributedMessageReceive')**

off(type: 'distributedMessageReceive', callback?: DistributedMessageCallback): void

解除注册分布式消息接收事件监听，使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'distributedMessageReceive'即分布式消息接收事件。 |
| callback | DistributedMessageCallback | 否 | 回调函数，用于取消注册distributedMessageReceive监听事件。取消注册后，应用无法在该callback方法中接收分布式消息。 注：若取消注册时不传入callback，则会取消注册distributedMessageReceive事件下所有的callback。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1000900001 | System internal error. |

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { pushCommon, pushService } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class PushMessageAbility extends UIAbility {
  private callback: pushService.DistributedMessageCallback = async (data:  pushCommon.PushPayload) => {
    let resultCode = pushService.ResultCode.SUCCESS;
    try {
      hilog.info(0x0000, 'testTag', 'Distribute message: %{public}s', JSON.stringify(data));
      // 处理业务逻辑，如将数据内容发布到穿戴设备上等
    } catch (e) {
      resultCode = pushService.ResultCode.FAILED;
      let errRes: BusinessError = e as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to receive distribute data: %{public}d %{public}s', errRes.code, errRes.message);
    }
    // 处理结束后，返回执行结果
    return { resultCode };
  };

  onDestroy(): void {
    try {
      // 解除注册distributedMessageReceive分布式消息接收回调场景
      pushService.off('distributedMessageReceive', this.callback);
      hilog.info(0x0000, 'testTag', 'Register off success');
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Register off error: %{public}d %{public}s', e.code, e.message);
    }
```

**DistributedMessageCallback**

type DistributedMessageCallback = (PushPayload: pushCommon.PushPayload) => Promise<DistributedMessageResult>

分布式消息接收事件中使用的回调函数。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| PushPayload | pushCommon.PushPayload | 是 | 分布式消息数据的参数定义。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<DistributedMessageResult> | Promise对象。返回DistributedMessageResult对象，见DistributedMessageResult说明。 |

**DistributedMessageResult**

distributedMessageReceive事件中使用的回调类型。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该接口在Phone、Tablet中可正常调用，在其他设备类型中无效果。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| resultCode | ResultCode | 否 | 否 | 回调函数执行结果，枚举类型，见枚举ResultCode说明。 |

**ResultCode**

表示[DistributedMessageCallback](#ZH-CN_TOPIC_0000002553202477__distributedmessagecallback)回调函数执行结果的枚举。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该枚举值在Phone、Tablet中可正常使用，在其他设备类型中无效果。

起始版本： 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUCCESS | 0 | 执行成功。 |
| FAILED | 1 | 执行失败。 |