# @ohos.data.dataShare (数据共享)

**DataShare**用于应用管理其自身数据，同时支持同个设备上不同应用间的数据共享。

-

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ets
import { dataShare } from '@kit.ArkData';
```

#### dataShare.createDataProxyHandle20+

createDataProxyHandle(): Promise<DataProxyHandle>

创建DataProxyHandle实例。使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**返回值：**

类型说明Promise<[DataProxyHandle](#ZH-CN_TOPIC_0000002529284671__dataproxyhandle20)>Promise对象。返回DataProxyHandle实例。

**错误码：**

错误码的详细介绍请参见[数据共享错误码](数据共享错误码.md)。

错误码ID错误信息15700000Inner error. Possible causes: The service is not ready or is being restarted abnormally.

**示例：**

```ets
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    dataShare.createDataProxyHandle().then((dataProxyHandle) => {
      console.info("createDataProxyHandle succeed");
    }).catch((err: BusinessError) => {
      console.error(`createDataProxyHandle error: code: ${err.code}, message: ${err.message}`);
    });
  };
};
```

#### ChangeType20+

数据变更类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

名称值说明INSERT0表示数据添加。DELETE1表示数据删除。UPDATE2表示数据更新。

#### ProxyData20+

共享配置的数据结构。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

名称类型只读可选说明uristring否否共享配置的全局唯一标识。固定格式为"datashareproxy://{bundleName}/{path}"，其中bundleName为配置发布方应用的bundleName，path可随意填写，但同一应用内不允许重复。字符串长度不超过256个字节。value[ValueType](@ohos.data.ValuesBucket (数据集).md#ZH-CN_TOPIC_0000002529284681__valuetype)否是共享配置的值。不填则为空字符串。字符串长度不超过4096个字节。当首次发布共享配置时，如果未填写，将默认设置为空字符串。在更新共享配置时，如果未填写，共享配置的值将不会被更新。allowListstring[]否是允许订阅和读取共享配置的应用程序列表。不填则为空的字符串数组。数组最大长度为256，超过256的部分不生效。数组中每个元素为应用的[appIdentifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/common_problem_of_application#什么是appidentifier)，单个appIdentifier最大长度128字节，超过128字节的appIdentifier不会生效。当首次发布共享配置时，如果未填写，将默认为空的允许列表。在更新共享配置时，如果未填写，共享配置的允许列表将不会被更新。一个空的允许列表表示只有发布者能够访问该共享配置。

#### DataProxyChangeInfo20+

通知订阅者共享配置变更的数据结构。包括数据变更类型、变化的URI、变更的数据内容。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

名称类型只读可选说明type[ChangeType](#ZH-CN_TOPIC_0000002529284671__changetype20)否否通知变更的类型。uristring否否通知变更指定URI。value[ValueType](zh-cn_topic_0000002529284681.html#ZH-CN_TOPIC_0000002529284681__valuetype)否否更新的数据。

#### DataProxyErrorCode20+

配置共享批量操作返回值的状态码枚举。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

名称值说明SUCCESS0表示操作成功。URI_NOT_EXIST1URI不存在或取消订阅一个未订阅过的URI。NO_PERMISSION2没有权限在该URI上执行此操作。OVER_LIMIT3表示当前应用发布的配置超过32个配置的上限。

#### DataProxyResult20+

配置共享批量操作结果的数据结构。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

名称类型只读可选说明uristring否否被操作的URI。固定格式为"datashareproxy://{bundleName}/{path}"，其中bundleName为配置发布方应用的bundleName，path可随意填写，但同一应用内不允许重复，字符串长度不超过256个字节。result[DataProxyErrorCode](#ZH-CN_TOPIC_0000002529284671__dataproxyerrorcode20)否否操作结果的错误码。

#### DataProxyGetResult20+

配置共享批量获取操作结果的数据结构。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

名称类型只读可选说明uristring否否被操作的URI。固定格式为"datashareproxy://{bundleName}/{path}"，其中bundleName为配置发布方应用的bundleName，path可随意填写，但同一应用内不允许重复，字符串长度不超过256个字节。result[DataProxyErrorCode](#ZH-CN_TOPIC_0000002529284671__dataproxyerrorcode20)否否操作结果的错误码。value[ValueType](zh-cn_topic_0000002529284681.html#ZH-CN_TOPIC_0000002529284681__valuetype) | undefined否否如果获取操作成功，则为共享配置的值；如果获取操作失败，则未定义。allowListstring[] | undefined否否如果获取操作成功，则为共享配置的允许列表；如果获取操作失败，则未定义。只有发布者才能获取允许列表，其他应用只能获取值。

#### DataProxyType20+

数据代理类型的枚举。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

名称值说明SHARED_CONFIG0表示应用之间的共享配置。

#### DataProxyConfig20+

数据代理操作配置的数据结构。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

名称类型只读可选说明type[DataProxyType](#ZH-CN_TOPIC_0000002529284671__dataproxytype20)否否数据代理操作的类型。

#### DataProxyHandle20+

数据代理操作句柄的实例，可使用此实例访问或管理共享配置信息。在调用DataProxyHandle提供的方法前，需要先通过[createDataProxyHandle](#ZH-CN_TOPIC_0000002529284671__datasharecreatedataproxyhandle20)构建一个实例。

#### on('dataChange')20+

on(event: 'dataChange', uris: string[], config: DataProxyConfig, callback: AsyncCallback<DataProxyChangeInfo[]>): DataProxyResult[]

订阅指定URI对应共享配置变更事件。若订阅者已注册变更通知，当配置发布方修改配置时，订阅者将会接收到callback通知，通知携带数据变更类型、变化的URI、变更的共享配置内容。使用callback异步回调。该功能不允许跨用户订阅通知，不允许订阅未发布的配置。订阅成功后若权限被收回，则后续不再通知订阅者。

触发通知：配置发布方调用[publish](#ZH-CN_TOPIC_0000002529284671__publish20)、[delete](#ZH-CN_TOPIC_0000002529284671__delete20)接口发布、删除配置时会自动触发通知。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

参数名类型必填说明eventstring是订阅的事件/回调类型，支持的事件为'dataChange'，当配置发布方修改配置时，触发该事件。urisstring[]是表示要订阅的共享配置对应的URI数组，数组最大长度为32。URI固定格式为"datashareproxy://{bundleName}/{path}"，其中bundleName为配置发布方应用的bundleName，path可随意填写，但同一应用内不允许重复，字符串长度不超过256个字节。config[DataProxyConfig](#ZH-CN_TOPIC_0000002529284671__dataproxyconfig20)是表示数据代理操作的配置。callbackAsyncCallback<[DataProxyChangeInfo](#ZH-CN_TOPIC_0000002529284671__dataproxychangeinfo20)[]>是回调函数。当配置发布方修改配置时会回调该函数。

**返回值：**

类型说明[DataProxyResult](#ZH-CN_TOPIC_0000002529284671__dataproxyresult20)[]批量操作的结果数组。

**错误码：**

以下错误码的详细介绍请参见[数据共享错误码](数据共享错误码.md)。

错误码ID错误信息15700000Inner error. Possible causes: The service is not ready or is being restarted abnormally.15700014The parameter format is incorrect or the value range is invalid.

**示例：**

```ets
const urisToWatch: string[] =
  ['datashareproxy://com.example.app1/config1', 'datashareproxy://com.example.app1/config2',];
const config: dataShare.DataProxyConfig = {
  type: dataShare.DataProxyType.SHARED_CONFIG,
};
const callback = (err: BusinessError<void>, changes: dataShare.DataProxyChangeInfo[]): void => {
  if (err) {
    console.error('err:', err);
  } else {
    changes.forEach((change) => {
      console.info(`Change Type: ${change.type}, URI: ${change.uri}, Value: ${change.value}`);
    });
  }
};
const results: dataShare.DataProxyResult[] = dataProxyHandle.on('dataChange', urisToWatch, config, callback);
results.forEach((result) => {
  console.info(`URI: ${result.uri}, Result: ${result.result}`);
});
```

#### off('dataChange')20+

off(event: 'dataChange', uris: string[], config: DataProxyConfig, callback?: AsyncCallback<DataProxyChangeInfo[]>): DataProxyResult[]

取消订阅指定URI对应代理数据变更事件。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

参数名类型必填说明eventstring是订阅的事件/回调类型，支持的事件为'dataChange'。urisstring[]是表示要取消订阅的共享配置对应的URI数组，数组最大长度为32。URI固定格式为"datashareproxy://{bundleName}/{path}"，其中bundleName为配置发布方应用的bundleName，path可随意填写，但同一应用内不允许重复，字符串长度不超过256个字节。config[DataProxyConfig](#ZH-CN_TOPIC_0000002529284671__dataproxyconfig20)是表示数据代理操作的配置。callbackAsyncCallback<[DataProxyChangeInfo](#ZH-CN_TOPIC_0000002529284671__dataproxychangeinfo20)[]>否回调函数。表示指定取消订阅的callback通知，如果为空、undefined或null，则取消订阅这些URI下所有的通知事件。

**返回值：**

类型说明[DataProxyResult](#ZH-CN_TOPIC_0000002529284671__dataproxyresult20)[]批量操作的结果数组。

**错误码：**

以下错误码的详细介绍请参见[数据共享错误码](数据共享错误码.md)。

错误码ID错误信息15700000Inner error. Possible causes: The service is not ready or is being restarted abnormally.15700014The parameter format is incorrect or the value range is invalid.

**示例：**

```ets
const urisToUnWatch: string[] =
  ['datashareproxy://com.example.app1/config1', 'datashareproxy://com.example.app1/config2',];
const config: dataShare.DataProxyConfig = {
  type: dataShare.DataProxyType.SHARED_CONFIG,
};
const callback = (err: BusinessError<void>, changes: dataShare.DataProxyChangeInfo[]): void => {
  if (err) {
    console.error('err:', err);
  } else {
    changes.forEach((change) => {
      console.info(`Change Type: ${change.type}, URI: ${change.uri}, Value: ${change.value}`);
    });
  }
};
const results: dataShare.DataProxyResult[] = dataProxyHandle.off('dataChange', urisToUnWatch, config, callback);
results.forEach((result) => {
  console.info(`URI: ${result.uri}, Result: ${result.result}`);
});
```

#### publish20+

publish(data: ProxyData[], config: DataProxyConfig): Promise<DataProxyResult[]>

发布共享配置项。发布后，发布者和允许列表中指定的应用可以访问该共享配置项。如果要发布的URI已经存在，则更新对应的共享配置项。如果发布的配置项中存在任一URI的长度超出上限或者格式校验失败，则当前发布操作失败。只有发布者才允许更新共享配置项，每个应用支持最多32个共享配置。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

参数名类型必填说明data[ProxyData](#ZH-CN_TOPIC_0000002529284671__proxydata20)[]是表示需要创建或者更新的共享配置项数组。数组最大长度为32。config[DataProxyConfig](#ZH-CN_TOPIC_0000002529284671__dataproxyconfig20)是表示数据代理操作的配置。

**返回值：**

类型说明Promise<[DataProxyResult](#ZH-CN_TOPIC_0000002529284671__dataproxyresult20)[]>Promise对象。返回批量操作的结果数组。

**错误码：**

以下错误码的详细介绍请参见[数据共享错误码](数据共享错误码.md)。

错误码ID错误信息15700000Inner error. Possible causes: The service is not ready or is being restarted abnormally.15700014The parameter format is incorrect or the value range is invalid.

**示例：**

```ets
const newConfigData: dataShare.ProxyData[] = [{
  uri: 'datashareproxy://com.example.app1/config1',
  value: 'Value1',
  allowList: ['appIdentifier2', 'appIdentifier3'], //此处字符串仅作示例，使用时需替换为应用实际的appIdentifier
}, {
  uri: 'datashareproxy://com.example.app1/config2',
  value: 'Value2',
  allowList: ['appIdentifier3', 'appIdentifier4'], //此处字符串仅作示例，使用时需替换为应用实际的appIdentifier
}];
const config: dataShare.DataProxyConfig = {
  type: dataShare.DataProxyType.SHARED_CONFIG,
};
dataProxyHandle.publish(newConfigData, config).then((results: dataShare.DataProxyResult[]) => {
  results.forEach((result) => {
    console.info(`URI: ${result.uri}, Result: ${result.result}`);
  });
}).catch((error: BusinessError) => {
  console.error('Error publishing config:', error);
});
```

#### delete20+

delete(uris: string[], config: DataProxyConfig): Promise<DataProxyResult[]>

根据URI删除指定的共享配置项，只有配置发布方能删除共享配置项。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

参数名类型必填说明urisstring[]是表示需要删除的共享配置对应的URI数组，数组最大长度为32。URI固定格式为"datashareproxy://{bundleName}/{path}"，其中bundleName为配置发布方应用的bundleName，path可随意填写，但同一应用内不允许重复，字符串长度不超过256个字节。config[DataProxyConfig](#ZH-CN_TOPIC_0000002529284671__dataproxyconfig20)是表示共享配置的类型。

**返回值：**

类型说明Promise<[DataProxyResult](#ZH-CN_TOPIC_0000002529284671__dataproxyresult20)[]>Promise对象。返回批量操作的结果数组。

**错误码：**

以下错误码的详细介绍请参见[数据共享错误码](数据共享错误码.md)。

错误码ID错误信息15700000Inner error. Possible causes: The service is not ready or is being restarted abnormally.15700014The parameter format is incorrect or the value range is invalid.

**示例：**

```ets
const urisToDelete: string[] =
  ['datashareproxy://com.example.app1/config1', 'datashareproxy://com.example.app1/config2',];
const config: dataShare.DataProxyConfig = {
  type: dataShare.DataProxyType.SHARED_CONFIG,
};
dataProxyHandle.delete(urisToDelete, config).then((results: dataShare.DataProxyResult[]) => {
  results.forEach((result) => {
    console.info(`URI: ${result.uri}, Result: ${result.result}`);
  });
}).catch((error: BusinessError) => {
  console.error('Error deleting config:', error);
});
```

#### get20+

get(uris: string[], config: DataProxyConfig): Promise<DataProxyGetResult[]>

根据URI获取指定的共享配置项。只有发布者和允许列表中指定的应用可以访问该共享配置项。

**系统能力：** SystemCapability.DistributedDataManager.DataShare.Consumer

**参数：**

参数名类型必填说明urisstring[]是表示需要获取的共享配置的URI数组，数组最大长度为32。URI固定格式为"datashareproxy://{bundleName}/{path}"，其中bundleName为配置发布方应用的bundleName，path可随意填写，但同一应用内不允许重复，字符串长度不超过256个字节。config[DataProxyConfig](#ZH-CN_TOPIC_0000002529284671__dataproxyconfig20)是表示共享配置的类型。

**返回值：**

类型说明Promise<[DataProxyGetResult](#ZH-CN_TOPIC_0000002529284671__dataproxygetresult20)[]>Promise对象。返回批量获取操作的结果数组。

**错误码：**

以下错误码的详细介绍请参见[数据共享错误码](数据共享错误码.md)。

错误码ID错误信息15700000Inner error. Possible causes: The service is not ready or is being restarted abnormally.15700014The parameter format is incorrect or the value range is invalid.

**示例：**

```ets
const urisToGet: string[] =
  ['datashareproxy://com.example.app1/config1', 'datashareproxy://com.example.app1/config2',];
const config: dataShare.DataProxyConfig = {
  type: dataShare.DataProxyType.SHARED_CONFIG,
};
dataProxyHandle.get(urisToGet, config).then((results: dataShare.DataProxyGetResult[]) => {
  results.forEach((result) => {
    console.info(`URI: ${result.uri}, Result: ${result.result}, AllowList: ${result.allowList}`);
  });
}).catch((error: BusinessError) => {
  console.error('Error getting config:', error);
});
```