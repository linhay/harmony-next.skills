# @ohos.net.mdns (MDNS管理)

MDNS即多播DNS（Multicast DNS），提供局域网内的本地服务添加、移除、发现、解析等能力。

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { mdns } from '@kit.NetworkKit';
```

#### mdns.addLocalService

addLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

添加一个MDNS服务，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。

serviceInfo[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)是MDNS服务的信息。callbackAsyncCallback<[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)>是回调函数。成功添加error为undefined，data为添加到本地的MDNS服务信息。

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](MDNS错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2204003Callback duplicated.2204008Failed to delete the service instance.2204010Failed to send the message.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.addLocalService(context, localServiceInfo, (error:BusinessError, data:mdns.LocalServiceInfo) =>  {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```

#### mdns.addLocalService

addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

添加一个MDNS服务，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。

serviceInfo[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)是MDNS服务的信息。

**返回值：**

类型说明Promise<[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)>以Promise形式返回添加的MDNS服务信息。

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](MDNS错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2204003Callback duplicated.2204008Failed to delete the service instance.2204010Failed to send the message.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
    address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.addLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

#### mdns.removeLocalService

removeLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

移除一个MDNS服务，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。

serviceInfo[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)是MDNS服务的信息。callbackAsyncCallback<[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)>是回调函数。成功移除error为undefined，data为移除本地的MDNS服务信息。

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](MDNS错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2204002Callback not found.2204008Failed to delete the service instance.2204010Failed to send the message.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.removeLocalService(context, localServiceInfo, (error: BusinessError, data: mdns.LocalServiceInfo) =>  {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```

#### mdns.removeLocalService

removeLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

移除一个MDNS服务，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。

serviceInfo[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)是MDNS服务的信息。

**返回值：**

类型说明Promise<[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)>以Promise形式返回移除的MDNS服务信息。

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](MDNS错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2204002Callback not found.2204008Failed to delete the service instance.2204010Failed to send the message.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.removeLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

#### mdns.createDiscoveryService

createDiscoveryService(context: Context, serviceType: string): DiscoveryService

返回一个DiscoveryService对象，该对象用于发现指定服务类型（serviceType）的MDNS服务。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。

serviceTypestring是需要发现的MDNS服务类型。

**返回值：**

类型说明DiscoveryService基于指定服务类型（serviceType）和Context的发现服务对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let serviceType = "_print._tcp";
let discoveryService : Object = mdns.createDiscoveryService(context, serviceType);
```

#### mdns.resolveLocalService

resolveLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

解析一个MDNS服务，使用callback方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。

serviceInfo[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)是MDNS服务的信息。callbackAsyncCallback<[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)>是回调函数。成功移除error为undefined，data为解析的MDNS服务信息。

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](MDNS错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2204003Callback duplicated.2204006Request timeout.2204010Failed to send the message.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.resolveLocalService(context, localServiceInfo, (error: BusinessError, data: mdns.LocalServiceInfo) =>  {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```

#### mdns.resolveLocalService

resolveLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

解析一个MDNS服务，使用Promise方式作为异步方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**： SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](Context (Stage模型的上下文基类).md)。

serviceInfo[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)是mDNS服务的信息。

**返回值：**

类型说明Promise<[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)>以Promise形式返回解析的MDNS服务信息。

**错误码：**

以下错误码的详细介绍请参见[MDNS错误码](MDNS错误码.md)和[通用错误码](通用错误码.md)。

错误码ID错误信息401Parameter error.2100002Failed to connect to the service.2100003System internal error.2204003Callback duplicated.2204006Request timeout.2204010Failed to send the message.

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "_print._tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.**.***",
  },
  serviceAttribute: [{key: "111", value: [1]}]
}

mdns.resolveLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

#### DiscoveryService

指定服务类型的发现服务对象。

#### startSearchingMDNS

startSearchingMDNS(): void

开始搜索局域网内的MDNS服务。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();
```

#### stopSearchingMDNS

stopSearchingMDNS(): void

停止搜索局域网内的MDNS服务。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

Stage模型示例：

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 获取context。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.stopSearchingMDNS();
```

#### on('discoveryStart')

on(type: 'discoveryStart', callback: Callback<DiscoveryEventInfo>): void

订阅开启监听mDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明typestring是

订阅事件，固定为'discoveryStart'。

discoveryStart：开始搜索局域网内的MDNS服务事件。

callbackCallback<[DiscoveryEventInfo](#ZH-CN_TOPIC_0000002529445413__discoveryeventinfo11)>是MDNS服务的信息和事件错误信息。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();
```

#### off('discoveryStart')

off(type: 'discoveryStart', callback?: Callback<DiscoveryEventInfo>): void

取消开启监听MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明typestring是

取消订阅的事件，固定为'discoveryStart'。

discoveryStart：开始搜索局域网内的MDNS服务事件。

callbackCallback<[DiscoveryEventInfo](#ZH-CN_TOPIC_0000002529445413__discoveryeventinfo11)>否MDNS服务的信息和事件错误信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

discoveryService.off('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});
```

#### on('discoveryStop')

on(type: 'discoveryStop', callback: Callback<DiscoveryEventInfo>): void

订阅停止监听MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明typestring是

订阅事件，固定为'discoveryStop'。

discoveryStop：停止搜索局域网内的MDNS服务事件。

callbackCallback<[DiscoveryEventInfo](#ZH-CN_TOPIC_0000002529445413__discoveryeventinfo11)>是MDNS服务的信息和事件错误信息。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();
```

#### off('discoveryStop')

off(type: 'discoveryStop', callback?: Callback<[DiscoveryEventInfo](#ZH-CN_TOPIC_0000002529445413__discoveryeventinfo11)>): void

取消订阅停止监听MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明typestring是

取消订阅的事件'discoveryStop'。

discoveryStop：停止搜索局域网内的MDNS服务事件。

callbackCallback<[DiscoveryEventInfo](#ZH-CN_TOPIC_0000002529445413__discoveryeventinfo11)>否MDNS服务的信息和事件错误信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

discoveryService.off('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});
```

#### on('serviceFound')

on(type: 'serviceFound', callback: Callback<LocalServiceInfo>): void

订阅发现MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明typestring是

订阅事件，固定为'serviceFound'。

serviceFound：发现MDNS服务事件。

callbackCallback<[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)>是MDNS服务的信息，需调用resolveLocalService解析这个MDNS服务信息。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
  console.info('serviceFound', JSON.stringify(data));
  mdns.resolveLocalService(context, data, (error: BusinessError, resolveData: mdns.LocalServiceInfo) =>  {
    console.info('serviceFound', JSON.stringify(resolveData));
  });
});

discoveryService.stopSearchingMDNS();
```

#### off('serviceFound')

off(type: 'serviceFound', callback?: Callback<LocalServiceInfo>): void

取消订阅发现MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明typestring是

取消订阅的事件，固定为'serviceFound'。

serviceFound：发现MDNS服务事件。

callbackCallback<[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)>否MDNS服务的信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
  console.info('serviceFound', JSON.stringify(data));
  mdns.resolveLocalService(context, data, (error: BusinessError, resolveData: mdns.LocalServiceInfo) =>  {
    console.info('serviceFound', JSON.stringify(resolveData));
  });
});

discoveryService.stopSearchingMDNS();

discoveryService.off('serviceFound', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

#### on('serviceLost')

on(type: 'serviceLost', callback: Callback<LocalServiceInfo>): void

订阅移除MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明typestring是

订阅事件，固定为'serviceLost'。

serviceLost：移除MDNS服务事件。

callbackCallback<[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)>是MDNS服务的信息。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();
```

#### off('serviceLost')

off(type: 'serviceLost', callback?: Callback<LocalServiceInfo>): void

取消订阅移除MDNS服务的通知。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

**参数：**

参数名类型必填说明typestring是

取消订阅的事件，固定为'serviceLost'。

serviceLost：移除MDNS服务事件。

callbackCallback<[LocalServiceInfo](#ZH-CN_TOPIC_0000002529445413__localserviceinfo)>否MDNS服务的信息。可以指定传入on中的callback取消对应的订阅，也可以不指定callback清空所有订阅。

**示例：**

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage#获取uiability的上下文信息)。

```ets
import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 参考mdns.createDiscoveryService。
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "_print._tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

discoveryService.off('serviceLost', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});
```

#### LocalServiceInfo

MDNS服务信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

名称类型只读可选说明serviceTypestring否否MDNS服务的类型。格式：_<name>.<_tcp/_udp>，name长度小于63字符并且不能包含字符'.'。serviceNamestring否否MDNS服务的名字。portnumber否是MDNS服务的端口号。取值范围[0，65535]。host[NetAddress](@ohos.net.connection (网络连接管理).md#ZH-CN_TOPIC_0000002497605446__netaddress)否是MDNS服务设备的IP地址。采用设备的IP，添加服务和移除服务时候不生效。serviceAttributeArray<[ServiceAttribute](#ZH-CN_TOPIC_0000002529445413__serviceattribute)>否是MDNS服务属性信息。

#### ServiceAttribute

MDNS服务属性信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

名称类型只读可选说明keystring否否MDNS服务属性键值，键值长度应该小于9个字符。valueArray<number>否否MDNS服务属性值。

#### DiscoveryEventInfo11+

监听到的MDNS服务事件信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

名称类型只读可选说明serviceInfoLocalServiceInfo否否MDNS服务信息。errorCodeMdnsError否是MDNS错误信息。

#### MdnsError

MDNS错误信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.MDNS

名称值说明INTERNAL_ERROR0内部错误导致操作失败。ALREADY_ACTIVE1服务已经存在导致操作失败。MAX_LIMIT2请求超过最大限制导致操作失败。

#### NetAddress

type NetAddress = connection.NetAddress

获取网络地址。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.NetManager.Core

类型说明connection.NetAddress定义网络地址。