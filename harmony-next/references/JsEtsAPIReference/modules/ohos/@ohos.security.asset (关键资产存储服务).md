# @ohos.security.asset (关键资产存储服务)

关键资产存储服务提供了用户短敏感数据的安全存储及管理能力。其中，短敏感数据可以是密码类（账号/密码）、Token类（应用凭据）、其他关键明文（如银行卡号）等长度较短的用户敏感数据。

本模块首批接口从API version 11 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { asset } from '@kit.AssetStoreKit';
```

#### asset.add

add(attributes: AssetMap): Promise<void>

新增一条关键资产。使用Promise异步回调。

设置[IS_PERSISTENT](#ZH-CN_TOPIC_0000002529285329__tag)属性时，需要申请ohos.permission.STORE_PERSISTENT_DATA权限。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明attributes[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是待新增关键资产的属性集合，包括关键资产明文、访问控制属性、自定义数据等。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息201The caller doesn't have the permission.401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

24000001The ASSET service is unavailable.24000003The asset already exists.24000005The screen lock status does not match.24000006Insufficient memory.24000007The asset is corrupted.24000008The database operation failed.24000009The cryptography operation failed.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000014The file operation failed.24000015Getting the system time failed.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let attr: asset.AssetMap = new Map();
attr.set(asset.Tag.SECRET, stringToArray('demo_pwd'));
attr.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label'));
asset.add(attr).then(() => {
  console.info(`Succeeded in adding Asset.`);
});
```

#### asset.addSync12+

addSync(attributes: AssetMap): void

新增一条关键资产，使用同步方式返回结果。

如果要设置[IS_PERSISTENT](#ZH-CN_TOPIC_0000002529285329__tag)属性，需要申请ohos.permission.STORE_PERSISTENT_DATA权限。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明attributes[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是待新增关键资产的属性集合，包括关键资产明文、访问控制属性、自定义数据等。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息201The caller doesn't have the permission.401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

24000001The ASSET service is unavailable.24000003The asset already exists.24000005The screen lock status does not match.24000006Insufficient memory.24000007The asset is corrupted.24000008The database operation failed.24000009The cryptography operation failed.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000014The file operation failed.24000015Getting the system time failed.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let attr: asset.AssetMap = new Map();
attr.set(asset.Tag.SECRET, stringToArray('demo_pwd'));
attr.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE_FIRST_UNLOCKED);
attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label'));
asset.addSync(attr);
```

#### asset.remove

remove(query: AssetMap): Promise<void>

删除符合条件的一条或多条关键资产。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明query[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是待删除关键资产的搜索条件，如别名、访问控制属性、自定义数据等。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息401

Parameter error. Possible causes:

1. Incorrect parameter types.

2. Parameter verification failed.

24000001The ASSET service is unavailable.24000002The asset is not found.24000006Insufficient memory.24000007The asset is corrupted.24000008The database operation failed.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000015Getting the system time failed.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
asset.remove(query).then(() => {
  console.info(`Succeeded in removing Asset.`);
});
```

#### asset.removeSync12+

removeSync(query: AssetMap): void

删除符合条件的一条或多条关键资产，使用同步方式。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明query[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是待删除关键资产的搜索条件，如别名、访问控制属性、自定义数据等。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息401

Parameter error. Possible causes:

1. Incorrect parameter types.

2. Parameter verification failed.

24000001The ASSET service is unavailable.24000002The asset is not found.24000006Insufficient memory.24000007The asset is corrupted.24000008The database operation failed.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000015Getting the system time failed.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
asset.removeSync(query);
```

#### asset.update

update(query: AssetMap, attributesToUpdate: AssetMap): Promise<void>

更新符合条件的一条关键资产。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明query[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是待更新关键资产的搜索条件，如关键资产别名、访问控制属性、自定义数据等。attributesToUpdate[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是待更新关键资产的属性集合，如关键资产明文、自定义数据等。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

24000001The ASSET service is unavailable.24000002The asset is not found.24000005The screen lock status does not match.24000006Insufficient memory.24000007The asset is corrupted.24000008The database operation failed.24000009The cryptography operation failed.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000015Getting the system time failed.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
let attrsToUpdate: asset.AssetMap = new Map();
attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo_pwd_new'));
asset.update(query, attrsToUpdate).then(() => {
  console.info(`Succeeded in updating Asset.`);
});
```

#### asset.updateSync12+

updateSync(query: AssetMap, attributesToUpdate: AssetMap): void

更新符合条件的一条关键资产，使用同步方式返回结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明query[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是待更新关键资产的搜索条件，如关键资产别名、访问控制属性、自定义数据等。attributesToUpdate[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是待更新关键资产的属性集合，如关键资产明文、自定义数据等。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

24000001The ASSET service is unavailable.24000002The asset is not found.24000005The screen lock status does not match.24000006Insufficient memory.24000007The asset is corrupted.24000008The database operation failed.24000009The cryptography operation failed.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000015Getting the system time failed.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
let attrsToUpdate: asset.AssetMap = new Map();
attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo_pwd_new'));
asset.updateSync(query, attrsToUpdate);
```

#### asset.preQuery

preQuery(query: AssetMap): Promise<Uint8Array>

查询的预处理，用于需要用户认证的关键资产。在用户认证成功后，应当随后调用[asset.query](#ZH-CN_TOPIC_0000002529285329__assetquery)和[asset.postQuery](#ZH-CN_TOPIC_0000002529285329__assetpostquery)接口。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明query[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是关键资产的查询条件，如别名、访问控制属性、自定义数据等。

**返回值：**

类型说明Promise<Uint8Array>

Promise对象，返回挑战值。

**说明：** 挑战值用于后续的用户认证。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息401

Parameter error. Possible causes:

1. Incorrect parameter types.

2. Parameter verification failed.

24000001The ASSET service is unavailable.24000002The asset is not found.24000005The screen lock status does not match.24000006Insufficient memory.24000007The asset is corrupted.24000008The database operation failed.24000009The cryptography operation failed.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000016The cache exceeds the limit.24000017The capability is not supported.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
asset.preQuery(query).then((challenge: Uint8Array) => {
  console.info(`Succeeded in pre-querying Asset.`);
});
```

#### asset.preQuerySync12+

preQuerySync(query: AssetMap): Uint8Array

查询的预处理，用于需要用户认证的关键资产。在用户认证成功后，应当随后调用[asset.querySync](#ZH-CN_TOPIC_0000002529285329__assetquerysync12)、[asset.postQuerySync](#ZH-CN_TOPIC_0000002529285329__assetpostquerysync12)。使用同步方式返回结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明query[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是关键资产的查询条件，如别名、访问控制属性、自定义数据等。

**返回值：**

类型说明Uint8Array

挑战值。

**说明：** 挑战值用于后续用户认证。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息401

Parameter error. Possible causes:

1. Incorrect parameter types.

2. Parameter verification failed.

24000001The ASSET service is unavailable.24000002The asset is not found.24000005The screen lock status does not match.24000006Insufficient memory.24000007The asset is corrupted.24000008The database operation failed.24000009The cryptography operation failed.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000016The cache exceeds the limit.24000017The capability is not supported.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
let challenge: Uint8Array = asset.preQuerySync(query);
console.info(`Succeeded in pre-querying with sync, the challenge is: `, challenge);
```

#### asset.query

query(query: AssetMap): Promise<Array<AssetMap>>

查询一条或多条符合条件的关键资产。若查询需要用户认证的关键资产，则需要在本函数前调用[asset.preQuery](#ZH-CN_TOPIC_0000002529285329__assetprequery)接口，在本函数后调用[asset.postQuery](#ZH-CN_TOPIC_0000002529285329__assetpostquery)接口，开发步骤请参考[开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-query-auth)。使用Promise异步回调。

如果未查询到符合条件的关键资产，将抛出“未找到关键资产”的异常，而非返回空的查询结果列表。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明query[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是关键资产的查询条件，如别名、访问控制属性、自定义数据等。

**返回值：**

类型说明Promise<Array<AssetMap>>Promise对象，返回查询结果列表。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息401

Parameter error. Possible causes:

1. Incorrect parameter types.

2. Parameter verification failed.

24000001The ASSET service is unavailable.24000002The asset is not found.24000004Access denied.24000005The screen lock status does not match.24000006Insufficient memory.24000007The asset is corrupted.24000008The database operation failed.24000009The cryptography operation failed.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000017The capability is not supported.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
// 如果只需要返回关键资产的属性，可以将RETURN_TYPE设置为ATTRIBUTES。返回属性不需解密，查询时间较短。
query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ALL); // 此处表示需要返回关键资产的所有信息，即属性+明文。返回明文需要解密，查询时间较长。
asset.query(query).then((res: Array<asset.AssetMap>) => {
  for (let i = 0; i < res.length; i++) {
    // 解析属性。
    let accessibility: number = res[i].get(asset.Tag.ACCESSIBILITY) as number;
    console.info(`Succeeded in getting accessibility, which is: ${accessibility}.`);
  }
  console.info(`Succeeded in querying Asset.`);
});
```

#### asset.querySync12+

querySync(query: AssetMap): Array<AssetMap>

查询一条或多条符合条件的关键资产。若查询需要用户认证的关键资产，则需要在本函数前调用[asset.preQuerySync](#ZH-CN_TOPIC_0000002529285329__assetprequerysync12)，在本函数后调用[asset.postQuerySync](#ZH-CN_TOPIC_0000002529285329__assetpostquerysync12)，开发步骤请参考[开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-query-auth)。使用同步方式返回结果。

如果未查询到符合条件的关键资产，将抛出“未找到关键资产”的异常，而非返回空的查询结果列表。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明query[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是关键资产的查询条件，如别名、访问控制属性、自定义数据等。

**返回值：**

类型说明Array<AssetMap>查询结果列表。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息401

Parameter error. Possible causes:

1. Incorrect parameter types.

2. Parameter verification failed.

24000001The ASSET service is unavailable.24000002The asset is not found.24000004Access denied.24000005The screen lock status does not match.24000006Insufficient memory.24000007The asset is corrupted.24000008The database operation failed.24000009The cryptography operation failed.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000017The capability is not supported.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
// 如果只需要返回关键资产的属性，可以将RETURN_TYPE设置为ATTRIBUTES。返回属性不需解密，查询时间较短。
query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ALL); // 此处表示需要返回关键资产的所有信息，即属性+明文。返回明文需要解密，查询时间较长。
let res: Array<asset.AssetMap> = asset.querySync(query);
for (let i = 0; i < res.length; i++) {
  // 解析属性。
  let accessibility: number = res[i].get(asset.Tag.ACCESSIBILITY) as number;
  console.info(`Succeeded in getting accessibility, which is: ${accessibility}.`);
}
console.info(`Succeeded in querying Asset.`);
```

#### asset.postQuery

postQuery(handle: AssetMap): Promise<void>

查询的后置处理，用于需要用户认证的关键资产（与[asset.preQuery](#ZH-CN_TOPIC_0000002529285329__assetprequery)函数成对出现）。使用Promise异步回调。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明handle[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是待处理的查询句柄，包含[asset.preQuery](#ZH-CN_TOPIC_0000002529285329__assetprequery)执行成功返回的挑战值。

**返回值：**

类型说明Promise<void>Promise对象，无返回结果。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

24000001The ASSET service is unavailable.24000006Insufficient memory.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';

let handle: asset.AssetMap = new Map();
// 此处传入的new Uint8Array(32)仅作为示例，实际应传入asset.preQuery执行成功返回的挑战值。
handle.set(asset.Tag.AUTH_CHALLENGE, new Uint8Array(32));
asset.postQuery(handle).then(() => {
  console.info(`Succeeded in post-querying Asset.`);
});
```

#### asset.postQuerySync12+

postQuerySync(handle: AssetMap): void

查询的后置处理，用于需要用户认证的关键资产。需与[asset.preQuerySync](#ZH-CN_TOPIC_0000002529285329__assetprequerysync12)函数成对出现。使用同步方式返回结果。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明handle[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是待处理的查询句柄，包含[asset.preQuerySync](#ZH-CN_TOPIC_0000002529285329__assetprequerysync12)执行成功返回的挑战值。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)

错误码ID错误信息401

Parameter error. Possible causes:

1. Mandatory parameters are left unspecified.

2. Incorrect parameter types.

3. Parameter verification failed.

24000001The ASSET service is unavailable.24000006Insufficient memory.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';

let handle: asset.AssetMap = new Map();
// 此处传入的new Uint8Array(32)仅作为示例，实际应传入asset.preQuerySync执行成功返回的挑战值。
handle.set(asset.Tag.AUTH_CHALLENGE, new Uint8Array(32));
asset.postQuerySync(handle)
```

#### asset.querySyncResult20+

querySyncResult(query: AssetMap): Promise<SyncResult>

执行同步操作后，查询同步执行结果。使用Promise异步回调。

**系统能力：** SystemCapability.Security.Asset

**参数：**

参数名类型必填说明query[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)是同步结果查询条件，如关键资产所属群组、业务自定义属性信息是否加密。

**返回值：**

类型说明Promise<[SyncResult](#ZH-CN_TOPIC_0000002529285329__syncresult20)>Promise对象，返回同步执行结果。

**错误码：**

以下错误码的详细介绍请参见[关键资产存储服务错误码](../../errors/关键资产存储服务(ASSET)错误码.md)。

错误码ID错误信息24000001The ASSET service is unavailable.24000006Insufficient memory.24000010IPC failed.24000011Calling the Bundle Manager service failed.24000012Calling the OS Account service failed.24000013Calling the Access Token service failed.24000014The file operation failed.24000018Parameter verification failed.

**示例：**

```ets
import { asset } from '@kit.AssetStoreKit';

let query: asset.AssetMap = new Map();
asset.querySyncResult(query).then((res: asset.SyncResult) => {
  console.info(`Succeeded in querying sync result: ${JSON.stringify(res)}`);
});
```

#### TagType

枚举，关键资产属性支持的数据类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

名称值说明BOOL0x01 << 28标识关键资产属性对应的数据类型是布尔。NUMBER0x02 << 28标识关键资产属性对应的数据类型是整型。BYTES0x03 << 28标识关键资产属性对应的数据类型是字节数组。

#### Tag

枚举，关键资产支持的属性名称类型，用作[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)的键。

**系统能力：** SystemCapability.Security.Asset

以下为Tag类型的全量枚举值，每个接口可传的Tag枚举及对应的Value取值范围不同，详见[各个场景的开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-store-kit-overview)。

名称值说明SECRETTagType.BYTES | 0x01

关键资产明文。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

ALIASTagType.BYTES | 0x02

关键资产别名，每条关键资产的唯一索引。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

ACCESSIBILITYTagType.NUMBER | 0x03

基于锁屏状态的访问控制。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

REQUIRE_PASSWORD_SETTagType.BOOL | 0x04

是否仅在设置了锁屏密码的情况下，可访问关键资产。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AUTH_TYPETagType.NUMBER | 0x05

访问关键资产所需的用户认证类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AUTH_VALIDITY_PERIODTagType.NUMBER | 0x06

用户认证的有效期。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AUTH_CHALLENGETagType.BYTES | 0x07

用户认证的挑战值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

AUTH_TOKENTagType.BYTES | 0x08

用户认证通过的授权令牌。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

SYNC_TYPETagType.NUMBER | 0x10

关键资产支持的同步类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

IS_PERSISTENTTagType.BOOL | 0x11在应用卸载时是否保留关键资产。DATA_LABEL_CRITICAL_1TagType.BYTES | 0x20

关键资产附属信息，内容由业务自定义且**有完整性保护**。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_CRITICAL_2TagType.BYTES | 0x21

关键资产附属信息，内容由业务自定义且**有完整性保护**。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_CRITICAL_3TagType.BYTES | 0x22

关键资产附属信息，内容由业务自定义且**有完整性保护**。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_CRITICAL_4TagType.BYTES | 0x23

关键资产附属信息，内容由业务自定义且**有完整性保护**。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_NORMAL_1TagType.BYTES | 0x30

关键资产附属信息，内容由业务自定义且**无完整性保护**。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_NORMAL_2TagType.BYTES | 0x31

关键资产附属信息，内容由业务自定义且**无完整性保护**。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_NORMAL_3TagType.BYTES | 0x32

关键资产附属信息，内容由业务自定义且**无完整性保护**。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_NORMAL_4TagType.BYTES | 0x33

关键资产附属信息，内容由业务自定义且**无完整性保护**。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_NORMAL_LOCAL_112+TagType.BYTES | 0x34

关键资产附属的本地信息，内容由业务自定义且**无完整性保护**，该项信息不会进行同步。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_NORMAL_LOCAL_212+TagType.BYTES | 0x35

关键资产附属的本地信息，内容由业务自定义且**无完整性保护**，该项信息不会进行同步。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_NORMAL_LOCAL_312+TagType.BYTES | 0x36

关键资产附属的本地信息，内容由业务自定义且**无完整性保护**，该项信息不会进行同步。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_LABEL_NORMAL_LOCAL_412+TagType.BYTES | 0x37

关键资产附属的本地信息，内容由业务自定义且**无完整性保护**，该项信息不会进行同步。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

RETURN_TYPETagType.NUMBER | 0x40

关键资产查询返回的结果类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

RETURN_LIMITTagType.NUMBER | 0x41

关键资产查询返回的结果数量。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

RETURN_OFFSETTagType.NUMBER | 0x42

关键资产查询返回的结果偏移量。

**说明：** 用于分批查询场景，指定从第几个开始返回。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

RETURN_ORDERED_BYTagType.NUMBER | 0x43

关键资产查询返回的结果排序依据，仅支持按照附属信息排序。

**说明：** 默认按照关键资产新增的顺序返回。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

CONFLICT_RESOLUTIONTagType.NUMBER | 0x44

新增关键资产时的冲突（如：别名相同）处理策略。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

UPDATE_TIME12+TagType.BYTES | 0x45

数据的更新时间（时间戳形式）。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

OPERATION_TYPE12+TagType.NUMBER | 0x46附加的操作类型。REQUIRE_ATTR_ENCRYPTED14+TagType.BOOL | 0x47

是否加密业务自定义附属信息。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

GROUP_ID18+TagType.BYTES | 0x48

关键资产所属群组。

WRAP_TYPE18+TagType.NUMBER | 0x49

关键资产支持的加密导入导出类型。

#### Value

type Value = boolean | number | Uint8Array

关键资产属性的内容，用作[AssetMap](#ZH-CN_TOPIC_0000002529285329__assetmap)的值。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

类型说明boolean表示值类型为布尔类型，取值范围为true或false。number表示值类型为数字，取值范围为Tag对应的枚举值或数值。Uint8Array表示值类型为字节数组，内容由业务自定义。

#### AssetMap

type AssetMap = Map<Tag, Value>

关键资产属性的键-值对集合。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

类型说明Map<Tag, Value>表示值类型是Map，键值对取值范围分别参考[Tag](#ZH-CN_TOPIC_0000002529285329__tag)和[Value](#ZH-CN_TOPIC_0000002529285329__value)。

#### Accessibility

枚举，关键资产基于锁屏状态的访问控制类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

名称值说明DEVICE_POWERED_ON0开机后可访问。DEVICE_FIRST_UNLOCKED1

首次解锁后可访问

**说明：** 未设置锁屏密码时，等同于开机后可访问。

DEVICE_UNLOCKED2

解锁状态时可访问

**说明：** 未设置锁屏密码时，等同于开机后可访问。

#### AuthType

枚举，关键资产支持的用户认证类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

名称值说明NONE0x00访问关键资产前无需用户认证。ANY0xFF任意一种用户认证方式（PIN码、人脸、指纹等）通过后，均可访问关键资产。

#### SyncType

枚举，关键资产支持的同步类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

名称值说明NEVER0不允许同步关键资产。THIS_DEVICE1 << 0

只在本设备进行同步，如仅在本设备还原的备份场景。

**说明：** 本字段是能力预埋，当前不支持。

TRUSTED_DEVICE1 << 1只在可信设备间进行同步，如克隆场景。TRUSTED_ACCOUNT12+1 << 2

只在登录可信账号的设备间进行同步，如云同步场景。

**说明：** 本字段是能力预埋，当前不支持。

#### ReturnType

枚举，关键资产查询返回的结果类型。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

名称值说明ALL0

返回关键资产明文及属性。

**说明：** 查询单条关键资产明文时，需设置此类型。

ATTRIBUTES1

返回关键资产属性，不含关键资产明文。

**说明：** 批量查询关键资产属性时，需设置此类型。

#### ConflictResolution

枚举，新增关键资产时的冲突（如：别名相同）处理策略。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.Asset

名称值说明OVERWRITE0覆盖原有的关键资产。THROW_ERROR1抛出异常，由业务进行后续处理。

#### OperationType12+

枚举，附属的操作类型。

**系统能力：** SystemCapability.Security.Asset

名称值说明NEED_SYNC0需要进行同步操作。NEED_LOGOUT1需要进行登出操作。

#### WrapType18+

枚举，关键资产支持的加密导入导出类型。

**系统能力：** SystemCapability.Security.Asset

名称值说明NEVER0不允许加密导入导出关键资产。TRUSTED_ACCOUNT1只在登录可信账号的设备进行加密导入导出关键资产。

#### SyncResult20+

关键资产同步的结果。

**系统能力：** SystemCapability.Security.Asset

名称类型只读可选说明resultCodenumber是否关键资产同步的结果码。同步成功时结果码为0，同步失败时结果码参考[ErrorCode](#ZH-CN_TOPIC_0000002529285329__errorcode)。totalCountnumber是是触发同步的关键资产总数。failedCountnumber是是关键资产同步失败的数量。

#### ErrorCode

表示错误码的枚举。

**系统能力：** SystemCapability.Security.Asset

名称值说明PERMISSION_DENIED201调用方无权限。NOT_SYSTEM_APPLICATION12+202调用方不是一个系统应用。INVALID_ARGUMENT401

参数错误。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

SERVICE_UNAVAILABLE24000001

关键资产服务不可用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

NOT_FOUND24000002

未找到关键资产。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DUPLICATED24000003

关键资产已存在。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

ACCESS_DENIED24000004

拒绝访问关键资产。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

STATUS_MISMATCH24000005

锁屏状态不匹配。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

OUT_OF_MEMORY24000006

系统内存不足。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATA_CORRUPTED24000007

关键资产损坏。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

DATABASE_ERROR24000008

数据库操作失败。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

CRYPTO_ERROR24000009

算法库操作失败。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

IPC_ERROR24000010

进程通信错误。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

BMS_ERROR24000011

包管理服务异常。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

ACCOUNT_ERROR24000012

账号系统异常。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

ACCESS_TOKEN_ERROR24000013

访问控制服务异常。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

FILE_OPERATION_ERROR24000014

文件操作失败。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

GET_SYSTEM_TIME_ERROR24000015

获取系统时间失败。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

LIMIT_EXCEEDED24000016

缓存数量超限。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

UNSUPPORTED24000017

该子功能不支持。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

PARAM_VERIFICATION_FAILED20+24000018

参数校验失败。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。