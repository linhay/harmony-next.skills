# serviceNotification（服务通知）

本模块提供服务通知的基础能力，包括请求订阅通知授权。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Push.PushService

起始版本： 4.1.0(11)

**导入模块**

```ets
import { serviceNotification } from '@kit.PushKit';
```

**serviceNotification.requestSubscribeNotification**

requestSubscribeNotification(context: Context, entityIds: Array<string>, callback: AsyncCallback<RequestResult>): void

请求订阅通知授权，使用callback异步回调。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中返回错误码1000900017。

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 请求订阅通知授权界面UIAbilityContext。 说明： context仅支持传入UIAbilityContext。 |
| entityIds | Array<string> | 是 | 模板ID列表。 |
| callback | AsyncCallback<RequestResult> | 是 | 回调函数。当请求订阅成功，err为undefined，data为订阅授权结果；否则为错误对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |
| 1000900017 | The device does not support current operation. |
| 1000900018 | Number of calls exceeded. |
| 1000900019 | Illegal entity id. |
| 1000900020 | App token is empty. |
| 1000900021 | App is not available or not registered. |
| 1000900022 | Notification switch off. |
| 1000900023 | Number of entity ids exceed the upper limit. |
| 1000900024 | Failed to display subscription UI. |
| 1000900025 | No rights to access entity id. |
| 1000900026 | Illegal entity type. |

示例：

```ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { serviceNotification } from '@kit.PushKit';
import { BusinessError } from '@kit.BasicServicesKit';
const DOMAIN = 0x0000;
export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    try {
      // entityIds请替换为待订阅的模板ID
      const entityIds = ['entityId1', 'entityId2', 'entityId3'];
      serviceNotification.requestSubscribeNotification(this.context, entityIds, (err, data) => {
        if (err) {
          hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', err.code,
            err.message);
        } else {
          hilog.info(0x0000, 'testTag', 'Succeeded in requesting subscribe notification: %{public}s',
            JSON.stringify(data.entityResult));
        }
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', e.code,
        e.message);
    }
```

**serviceNotification.requestSubscribeNotification**

requestSubscribeNotification(context: Context, entityIds: Array<string>, type?: SubscribeNotificationType): Promise<RequestResult>

请求订阅通知授权，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该接口在Phone、Tablet中可正常调用，在其他设备类型中返回错误码1000900017。

起始版本： 4.1.0(11)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 请求订阅通知授权界面UIAbilityContext。 说明： context仅支持传入UIAbilityContext。 |
| entityIds | Array<string> | 是 | 表示待订阅的模板ID列表。  当订阅type为SUBSCRIBE_WITH_HUAWEI_ID时，详情请参见选用订阅模板。 |
| type | SubscribeNotificationType | 否 | 订阅类型。默认为SUBSCRIBE_WITH_TOKEN。 说明： 起始版本：5.0.0(12)。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<RequestResult> | Promise对象，返回订阅授权结果。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 1000900001 | System internal error. |
| 1000900008 | Failed to connect to the push service. |
| 1000900009 | Internal error of the push service. |
| 1000900010 | Illegal application identity. |
| 1000900011 | The network is unavailable. |
| 1000900017 | The device does not support current operation. |
| 1000900018 | Number of calls exceeded. |
| 1000900019 | Illegal entity id. |
| 1000900020 | App token is empty. |
| 1000900021 | App is not available or not registered. |
| 1000900022 | Notification switch off. |
| 1000900023 | Number of entity ids exceed the upper limit. |
| 1000900024 | Failed to display subscription UI. |
| 1000900025 | No rights to access entity id. |
| 1000900026 | Illegal entity type. |
| 1000900030 | The user has not logged in with HUAWEI ID. |

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

错误码1000900030仅当接口在元服务中使用时才涉及。

错误码1000900011可能是推送服务无网被禁网，请到设置 移动网络 -> 流量管理 -> 应用联网，检查推送服务是否被禁网。

示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { serviceNotification } from '@kit.PushKit';
import { BusinessError } from '@kit.BasicServicesKit';
const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
    try {
      // entityIds请替换为待订阅的模板ID
      const entityIds = ['entityId1', 'entityId2', 'entityId3'];
      let type: serviceNotification.SubscribeNotificationType =
        serviceNotification.SubscribeNotificationType.SUBSCRIBE_WITH_HUAWEI_ID;
      serviceNotification.requestSubscribeNotification(this.context, entityIds, type).then((data) => {
        hilog.info(0x0000, 'testTag', 'Succeeded in requesting subscribe notification: %{public}s',
          JSON.stringify(data.entityResult));
      }).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', err.code,
          err.message);
      });
    } catch (err) {
      let e: BusinessError = err as BusinessError;
      hilog.error(0x0000, 'testTag', 'Failed to request subscribe notification: %{public}d %{public}s', e.code,
        e.message);
    }
```

**RequestResult**

表示单次订阅的授权结果。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

起始版本： 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityResult | Array<EntityResult> | 是 | 否 | 授权订阅结果。 |

**EntityResult**

表示单次订阅中每一个模板订阅的授权结果。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该接口在Phone、Tablet、PC/2in1中可正常调用，在其他设备类型中无效果。

起始版本： 4.1.0(11)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| entityId | string | 是 | 否 | 模板ID。 |
| resultCode | ResultCode | 是 | 否 | 授权订阅结果码。 |

**ResultCode**

标识授权订阅结果，为枚举值。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该枚举值在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

起始版本： 4.1.0(11)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACCEPTED | 0 | 表示模板被接受。 |
| REJECTED | 1 | 表示模板被拒绝。 |
| FILTERED | 2 | 表示模板被过滤。 |
| BANNED | 3 | 表示模板被禁止。 |
| UNKNOWN | -1 | 表示未知错误。 |

**SubscribeNotificationType**

标识订阅类型，为枚举值。

模型约束： 此接口仅可在Stage模型下使用。

元服务API： 从版本5.0.0(12)开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Push.PushService

设备行为差异：该枚举值在Phone、Tablet、PC/2in1中可正常使用，在其他设备类型中无效果。

起始版本： 5.0.0(12)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBSCRIBE_WITH_TOKEN | 0 | 表示通过Push Token订阅，仅应用支持通过Push Token订阅。 |
| SUBSCRIBE_WITH_HUAWEI_ID | 1 | 表示通过华为账号订阅，仅元服务支持通过账号订阅。详情请参见推送基于账号的订阅消息。 |