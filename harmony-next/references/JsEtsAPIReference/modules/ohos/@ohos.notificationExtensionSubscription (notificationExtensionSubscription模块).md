# @ohos.notificationExtensionSubscription (notificationExtensionSubscription模块)

本模块提供管理通知扩展的能力，具体包括：打开通知扩展订阅设置界面、订阅和取消订阅通知扩展、获取和设置通知授权状态。

本模块首批接口从API version 22开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { notificationExtensionSubscription } from '@kit.NotificationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

#### notificationExtensionSubscription.openSubscriptionSettings

openSubscriptionSettings(context: UIAbilityContext): Promise<void>

打开应用的通知扩展订阅授权页面，以半模态弹窗形式显示。用户可在该页面授权"允许获取本机通知"开关与"已获取的本机通知"应用开关。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**参数：**

参数名类型必填说明context[UIAbilityContext](../../topics/graphics/UIAbilityContext.md)是通知设置页面绑定Ability的上下文。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息201Permission denied or Current device is not supported.1600001Internal error.1600018The notification settings window is already displayed.1600023The application does not implement the NotificationSubscriberExtensionAbility.

**示例：**

```ets
import { common } from '@kit.AbilityKit';

const DOMAIN = 0x0000;

try {
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  notificationExtensionSubscription.openSubscriptionSettings(context).then(() => {
    hilog.info(DOMAIN, 'testTag', `openSubscriberSettings success`);
  }).catch((e:Error) => {
    let error = e as BusinessError
    hilog.error(DOMAIN, 'testTag', `failed to call openSubscriptionSettings ${JSON.stringify(error)}`)
  });
} catch (error) {
  hilog.error(DOMAIN, 'testTag', `failed to call openSubscriptionSettings ${JSON.stringify(error)}`)
}
```

#### notificationExtensionSubscription.subscribe

subscribe(info: NotificationExtensionSubscriptionInfo[]): Promise<void>

订阅通知扩展。使用[蓝牙模块](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/connectivity-kit-intro#蓝牙简介)相关接口获取蓝牙设备的唯一地址后方可订阅。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**参数：**

参数名类型必填说明info[NotificationExtensionSubscriptionInfo[]](NotificationExtensionSubscriptionInfo.md)是订阅的信息列表（数组）。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息201Permission denied or Current device is not supported.1600001Internal error.1600003Failed to connect to the service.1600023The application does not implement the NotificationSubscriberExtensionAbility.

**示例：**

```ets
let infos: notificationExtensionSubscription.NotificationExtensionSubscriptionInfo[] = [
  {
    addr: '01:23:45:67:89:AB', // 使用动态获取的蓝牙地址
    type: notificationExtensionSubscription.SubscribeType.BLUETOOTH
  }
];
notificationExtensionSubscription.subscribe(infos).then(() => {
  console.info("subscribe success");
}).catch((err: BusinessError) => {
  console.error(`subscribe fail: ${JSON.stringify(err)}`);
});
```

#### notificationExtensionSubscription.unsubscribe

unsubscribe(): Promise<void>

取消通知扩展的订阅。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息201Permission denied or Current device is not supported.1600001Internal error.1600003Failed to connect to the service.

**示例：**

```ets
notificationExtensionSubscription.unsubscribe().then(() => {
  console.info("unsubscribe success");
}).catch((err: BusinessError) => {
  console.error(`unsubscribe fail: ${JSON.stringify(err)}`);
});
```

#### notificationExtensionSubscription.getSubscribeInfo

getSubscribeInfo(): Promise<NotificationExtensionSubscriptionInfo[]>

获取当前应用的通知扩展订阅信息。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**返回值：**

类型说明Promise<[NotificationExtensionSubscriptionInfo[]](NotificationExtensionSubscriptionInfo.md)>Promise对象，返回一个[NotificationExtensionSubscriptionInfo[]](NotificationExtensionSubscriptionInfo.md)对象数组，表示应用的订阅信息。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息201Permission denied or Current device is not supported.1600001Internal error.1600003Failed to connect to the service.

**示例：**

```ets
notificationExtensionSubscription.getSubscribeInfo().then((data) => {
  console.info(`getSubscribeInfo successfully. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getSubscribeInfo fail: ${JSON.stringify(err)}`);
});
```

#### notificationExtensionSubscription.isUserGranted

isUserGranted(): Promise<boolean>

查询"允许获取本机通知"的开关状态。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**返回值：**

类型说明Promise<boolean>Promise对象。返回true表示功能已启用；返回false表示功能未启用。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)、[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息201Permission denied or Current device is not supported.1600001Internal error.1600003Failed to connect to the service.

**示例：**

```ets
notificationExtensionSubscription.isUserGranted().then((isOpen: boolean) => {
  if (isOpen) {
    console.info('isUserGranted true');
  } else {
    console.info('isUserGranted false');
  }
}).catch((err: BusinessError) => {
  console.error(`isUserGranted fail: ${JSON.stringify(err)}`);
});
```

#### notificationExtensionSubscription.getUserGrantedEnabledBundles

getUserGrantedEnabledBundles(): Promise<GrantedBundleInfo[]>

获取指定应用中"已获取的本机通知"通知开关开启的应用列表。使用Promise异步回调。

**系统能力**：SystemCapability.Notification.Notification

**需要权限**：ohos.permission.SUBSCRIBE_NOTIFICATION

**返回值：**

类型说明Promise<[GrantedBundleInfo[]](NotificationCommonDef.md#ZH-CN_TOPIC_0000002529446079__grantedbundleinfo22)>Promise对象，返回获取指定应用中"已获取的本机通知"通知开关开启的应用列表。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[通知错误码](../../errors/通知错误码.md)。

错误码ID错误信息201Permission denied or Current device is not supported.1600001Internal error.1600003Failed to connect to the service.

**示例：**

```ets
notificationExtensionSubscription.getUserGrantedEnabledBundles().then((data) => {
  console.info(`getUserGrantedEnabledBundles successfully. Data: ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`getUserGrantedEnabledBundles fail: ${JSON.stringify(err)}`);
});
```

#### NotificationExtensionSubscriptionInfo

type NotificationExtensionSubscriptionInfo = _NotificationExtensionSubscriptionInfo

用于描述通知扩展订阅的信息。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_NotificationExtensionSubscriptionInfo](../../topics/payment/NotificationExtensionSubscriptionInfo.md)用于描述通知扩展订阅的信息。

#### SubscribeType

表示通知扩展订阅的类型。

**系统能力**：SystemCapability.Notification.Notification

名称值说明BLUETOOTH0通过蓝牙订阅通知。

#### BundleOption

type BundleOption = _BundleOption

指定应用的包信息。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_BundleOption](../../topics/misc/NotificationCommonDef.md#ZH-CN_TOPIC_0000002529446079__bundleoption)指定应用的包信息。

#### GrantedBundleInfo

type GrantedBundleInfo = _GrantedBundleInfo

授权应用的包信息。

**系统能力**： SystemCapability.Notification.Notification

类型说明[_GrantedBundleInfo](../../topics/misc/NotificationCommonDef.md#ZH-CN_TOPIC_0000002529446079__grantedbundleinfo22)授权应用的包信息。