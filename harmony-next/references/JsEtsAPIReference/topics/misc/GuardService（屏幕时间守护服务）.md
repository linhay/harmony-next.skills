# GuardService（屏幕时间守护服务）

本模块提供管控Screen Time Guard Kit对外开放能力，包括应用授权能力、使用时长管控、应用访问限制等功能。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

**导入模块**

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';
```

**GuardServiceErrorCode**

该枚举定义了Screen Time Guard Kit屏幕时间守护服务错误码。

模型约束： 此枚举仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INTERNAL_ERROR | 1019000001 | 内部错误。 |
| USER_NOT_AUTHORIZED | 1019000002 | 用户未授权。 |
| USER_CANCELED | 1019000003 | 用户取消。 |
| STRATEGIES_EXCEED_LIMIT | 1019000004 | 策略数量超限。 |
| STRATEGY_NAME_ALREADY_EXIST | 1019000005 | 策略名称重复。 |
| NONEXISTENT_STRATEGY | 1019000006 | 策略不存在。 |
| STRATEGY_ALREADY_EXECUTED | 1019000007 | 策略重复执行。 |
| STRATEGY_NOT_STARTED | 1019000008 | 策略未执行。 |
| INVALID_PARAM | 1019000009 | 无效参数。 起始版本： 6.0.2(22) |

**requestUserAuth**

requestUserAuth(context: common.UIAbilityContext): Promise<void>

请求用户授权访问Screen Time Guard Kit的所有管控接口，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | common.UIAbilityContext | 是 | UIAbility的上下文环境。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function requestUserAuth can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

示例：

```ets
import { common } from '@kit.AbilityKit';
import { guardService } from '@kit.ScreenTimeGuardKit';

@Entry
@Component
struct TestPage {
  build() {
    Column() {
      Button("TestRequestUserAuth")
        .onClick(async () => {
          guardService.requestUserAuth(this.getUIContext().getHostContext() as common.UIAbilityContext)
            .then(() => {
              console.info('requestUserAuth invoke success');
            })
    }
```

**revokeUserAuth**

revokeUserAuth(): Promise<void>

取消用户授权访问Screen Time Guard Kit的相关管控接口，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function revokeUserAuth can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |

示例：

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';

async function testRevokeUserAuth() {
  await guardService.revokeUserAuth()
    .then(() => {
      console.info('revokeUserAuth invoke success.');
    })
}
```

**getUserAuthStatus**

getUserAuthStatus(): Promise<AuthStatus>

获取用户授权状态，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<AuthStatus> | Promise对象，初始未申请授权时的状态为AUTH_INIT，用户同意授权时为AUTH_GRANTED，用户拒绝授权时为AUTH_DENIED。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function getUserAuthStatus can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |

示例：

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';

async function testGetUserAuthStatus() {
  guardService.getUserAuthStatus()
    .then((status) => {
      const statusToMsg = ['AUTH_INIT', 'AUTH_GRANTED', 'AUTH_DENIED'];
      console.info('getUserAuthStatus invoke success. ' + statusToMsg[status + 1]);
    })
}
```

**AuthStatus**

用户授权状态类型的枚举。

模型约束： 此枚举仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTH_INIT | -1 | 初始状态 |
| AUTH_GRANTED | 0 | 用户已授权 |
| AUTH_DENIED | 1 | 用户已拒绝 |

**AppInfo**

该接口为应用token信息。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| appTokens | string[] | 否 | 否 | 应用token数组。 数组数量上限：100。  说明： 1. token数组中存在错误的tokens，若只是部分错误，则取其中正常的tokens做显示和应用。  2. 该数组可以为空数组，即用户不设置任何应用在禁止/允许清单中，是正常场景。 |

**addGuardStrategy**

addGuardStrategy(guardStrategy: GuardStrategy): Promise<void>

添加屏幕时间管控策略，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| guardStrategy | GuardStrategy | 是 | 管控策略。  说明： 添加管控策略时策略数量的上限为50条。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function addGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000004 | The number of strategies exceeds the upper limit. |
| 1019000005 | The strategy name is already existed. |

示例：

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';

async function testAddGuardStrategy() {
  const time: guardService.TimeStrategy = {
    type: guardService.TimeStrategyType.START_END_TIME_TYPE,
    startTime: "08:00",
    endTime: "19:00",
    repeat: [1,2,3]
  }
  const info: guardService.AppInfo = {
    appTokens: [] // 可以通过调用startAppPicker接口获取相应的应用token
  }
  const strategy: guardService.GuardStrategy = {
    name: "TestStrategy",
    timeStrategy: time,
    appInfo: info,
    appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
  }
  guardService.addGuardStrategy(strategy)
    .then(() => {
      console.info('addGuardStrategy invoke success.');
    })
}
```

**GuardStrategy**

该接口为守护策略对象。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 策略名称。长度不超过64字符，仅支持字母、数字和下划线。 |
| timeStrategy | TimeStrategy | 否 | 否 | 时间策略。 |
| appInfo | AppInfo | 否 | 否 | 应用信息。 |
| appRestrictionType | RestrictionType | 否 | 否 | 限制类型。 |

**TimeStrategy**

该接口为时间策略对象。

模型约束： 此接口仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | TimeStrategyType | 否 | 否 | 时间管控策略类型。 |
| startTime | string | 否 | 是 | 起始时间，以"HH:mm"的形式。参数范围："00:00"-"23:59"。  说明： 若TimeStrategyType为START_END_TIME_TYPE，则此参数必填。 |
| endTime | string | 否 | 是 | 结束时间，以"HH:mm"的形式。参数范围："00:00"-"23:59"。  说明： 若TimeStrategyType为START_END_TIME_TYPE，则此参数必填。  说明： 1. 若结束时间小于起始时间，则代表的是次日。  2. startTime与endTime的值不能相同。 |
| totalDuration | number | 否 | 是 | 总时长，单位是分钟。参数范围：0-1440。  说明： 若TimeStrategyType为TOTAL_DURATION_TYPE，则此参数必填。 |
| repeat | number[] | 否 | 是 | 重复执行时间，支持填写1~7，代表周一到周日。 如果传入的是空数组则表示只执行一次。  说明： TimeStrategyType为START_END_TIME_TYPE时此参数才生效。 |

**TimeStrategyType**

时长策略类型的枚举。

模型约束： 此枚举仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| START_END_TIME_TYPE | 1 | 起始时间策略类型，表示策略在配置的起始时间和结束时间内生效。如果为此类型，则TimeStrategy接口中的startTime、endTime必填，totalDuration非必填。 |
| TOTAL_DURATION_TYPE | 2 | 总时长策略类型，表示策略生效的总时长，从调用startGuardStrategy接口成功后开始计时。如果为此类型，则TimeStrategy接口中的startTime、endTime非必填，totalDuration必填。 |
| INCLUSIVE_DURATION_TYPE | 3 | 共享时长策略类型，表示策略关联的所有应用共享同一可用时长配额，超额后所有应用均受时长限制，从调用startGuardStrategy接口成功后开始计时。如果为此类型，则TimeStrategy接口中的startTime、endTime非必填，totalDuration必填，RestrictionType只支持TRUSTLIST_TYPE。 起始版本： 6.0.2(22) |

**RestrictionType**

限制类型的枚举。

模型约束： 此枚举仅可在Stage模型下使用。

系统能力： SystemCapability.ScreenTimeGuard.GuardService

起始版本： 6.0.0(20)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TRUSTLIST_TYPE | 1 | 按允许清单做限制。 |
| BLOCKLIST_TYPE | 2 | 按禁止清单做限制。 |

**updateGuardStrategy**

updateGuardStrategy(strategyName: string, guardStrategy: GuardStrategy): Promise<void>

修改屏幕时间管控策略，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 待更新的时间管控策略名称。长度不超过64字符，仅支持字母、数字和下划线。 |
| guardStrategy | GuardStrategy | 是 | 新的时间管控策略。  说明： 如想修改策略名称，可以在guardStrategy的name属性中传入新名称。但不能是已存在的名称，如果名称已存在则返回401错误码。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function updateGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |

示例：

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';

async function testUpdateGuardService() {
  const time: guardService.TimeStrategy = {
    type: guardService.TimeStrategyType.START_END_TIME_TYPE,
    startTime: "08:00",
    endTime: "19:00",
    repeat: [1,2,3,4,5]
  }
  const info: guardService.AppInfo = {
    appTokens: [] // 可以通过调用startAppPicker接口获取相应的应用token
  }
  const strategy: guardService.GuardStrategy = {
    name: "TestStrategyChanged",
    timeStrategy: time,
    appInfo: info,
    appRestrictionType: guardService.RestrictionType.BLOCKLIST_TYPE
  }
  // "TestStrategy"策略需提前通过addGuardStrategy接口添加
  guardService.updateGuardStrategy("TestStrategy", strategy)
    .then(() => {
      console.info('updateGuardStrategy invoke success.');
    })
}
```

**queryGuardStrategies**

queryGuardStrategies(): Promise<GuardStrategy[]>

查询该应用下的所有管控策略，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<GuardStrategy[]> | Promise对象。返回GuardStrategy[]，该应用下所有管控策略的数组。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 801 | Capability not supported. function queryGuardStrategies can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

示例：

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';

async function testQueryGuardService() {
  guardService.queryGuardStrategies()
    .then((guardStrategy: guardService.GuardStrategy[]) => {
      console.info('queryGuardStrategies invoke success, GuardStrategies: ' + guardStrategy);
    })
}
```

**removeGuardStrategy**

removeGuardStrategy(strategyName: string): Promise<void>

删除管控策略，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 时间管控策略名称。长度不超过64字符，仅支持字母、数字和下划线。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function removeGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |

示例：

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';

async function testRemoveGuardService() {
  await guardService.removeGuardStrategy("TestStrategy")
    .then(() => {
      console.info('removeGuardStrategy invoke success');
    })
}
```

**startGuardStrategy**

startGuardStrategy(strategyName: string): Promise<void>

根据策略名称，立即启动指定的管控策略，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 时间管控策略名称。长度不超过64字符，仅支持字母、数字和下划线。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function startGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |
| 1019000007 | The strategy is already being executed. |

示例：

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';

async function testGuardService() {
  guardService.startGuardStrategy("TestStrategy")
    .then(() => {
      console.info('startGuardStrategy invoke success');
    })
}
```

**stopGuardStrategy**

stopGuardStrategy(strategyName: string): Promise<void>

根据策略名称，立即停止指定的管控策略，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 时间管控策略名称。长度不超过64字符，仅支持字母、数字和下划线。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function stopGuardStrategy can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |
| 1019000006 | Nonexistent strategy. |
| 1019000008 | This strategy has not been started yet. |

示例：

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';

async function testStopGuardService() {
  guardService.stopGuardStrategy("TestStrategy")
    .then(() => {
      console.info('stopGuardStrategy invoke success');
    })
}
```

**setAppsRestriction**

setAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>

可根据传入应用token数组，以及限制类型（黑/允许清单），实现对相应的应用添加访问限制，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appInfo | AppInfo | 是 | 被选择的应用token集合，是一个字符串数组。 |
| restrictionType | RestrictionType | 是 | 限制类型 TRUSTLIST_TYPE表示对appInfo外的应用进行限制，BLOCKLIST_TYPE表示对appInfo内的应用进行限制。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function setAppsRestriction can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

示例：

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';

async function testSetAppsRestriction() {
  let selectedTokens: string[] = []; // 可以通过调用startAppPicker接口获取相应的应用token
  let appInfo: guardService.AppInfo = { appTokens: selectedTokens };
  let restrictionType: guardService.RestrictionType = guardService.RestrictionType.BLOCKLIST_TYPE;
  guardService.setAppsRestriction(appInfo, restrictionType)
    .then(() => {
      console.info('setAppsRestriction invoke success');
    });
}
```

**releaseAppsRestriction**

releaseAppsRestriction(appInfo: AppInfo, restrictionType: RestrictionType): Promise<void>

可根据传入应用token数组，以及限制类型（黑/允许清单），实现对相应的应用解除访问限制，使用Promise异步回调。

模型约束： 此接口仅可在Stage模型下使用。

需要权限： ohos.permission.MANAGE_SCREEN_TIME_GUARD

系统能力： SystemCapability.ScreenTimeGuard.GuardService

设备行为差异： 该接口在Phone、Tablet设备中可正常调用，在其他设备中返回801错误码。

起始版本： 6.0.0(20)

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appInfo | AppInfo | 是 | 被选择的应用token集合，是一个字符串数组。 |
| restrictionType | RestrictionType | 是 | 限制类型 TRUSTLIST_TYPE表示对appInfo外的应用进行限制，BLOCKLIST_TYPE表示对appInfo内的应用进行限制。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

错误码：

以下错误码的详细介绍请参见[ArkTS API错误码](ArkTS API错误码.md)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
| 801 | Capability not supported. function releaseAppsRestriction can not work correctly due to limited device capabilities. |
| 1019000001 | Internal error. |
| 1019000002 | The user has not authorized the application to access this interface. |

示例：

```ets
import { guardService } from '@kit.ScreenTimeGuardKit';

async function testReleaseAppsRestriction() {
  let selectedTokens: string[] = []; // 可以通过调用startAppPicker获取相应应用的token
  let appInfo: guardService.AppInfo = { appTokens: selectedTokens };
  let restrictionType: guardService.RestrictionType = guardService.RestrictionType.BLOCKLIST_TYPE;
  guardService.releaseAppsRestriction(appInfo, restrictionType)
    .then(() => {
      console.info('releaseAppsRestriction invoke success');
    });
}
```