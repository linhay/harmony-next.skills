# @ohos.data.preferences (用户首选项)

用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。

数据存储采用键值对形式，键为字符串类型，值可为数字、字符串、布尔类型及其对应的数组。

用户首选项的持久化文件存储在[preferencesDir](../../guides/应用上下文Context.md#获取应用文件路径)路径下，创建preferences对象前，需要保证preferencesDir路径可读写。持久化文件存储路径中的[加密等级](@ohos.app.ability.contextConstant (Context相关常量).md#ZH-CN_TOPIC_0000002553200497__areamode)会影响文件的可读写状态，路径访问限制详见[应用文件目录与应用文件路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory#应用文件目录与应用文件路径)。


本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

首选项无法保证进程并发安全，会有文件损坏和数据丢失的风险，不支持在多进程场景下使用。

#### 导入模块

```ets
import { preferences } from '@kit.ArkData';
```

#### 常量

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| MAX_KEY_LENGTH | number | 是 | Key的最大长度限制为1024个字节。 |
| MAX_VALUE_LENGTH | number | 是 | Value的最大长度限制为16MB。 |

#### preferences.getPreferences

getPreferences(context: Context, name: string, callback: AsyncCallback<Preferences>): void

获取Preferences实例，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | Preferences实例的名称。 |
| callback | AsyncCallback<Preferences> | 是 | 回调函数。当获取Preferences实例成功，err为undefined，返回Preferences实例；否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[用户首选项错误码]([用户首选项错误码](../../errors/用户首选项错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

FA模型示例：

```ets
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();
let dataPreferences: preferences.Preferences | null = null;

preferences.getPreferences(context, 'myStore', (err: BusinessError, val: preferences.Preferences) => {
  if (err) {
    console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
    return;
  }
  dataPreferences = val;
  console.info("Succeeded in getting preferences.");
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let dataPreferences: preferences.Preferences | null = null;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    preferences.getPreferences(this.context, 'myStore', (err: BusinessError, val: preferences.Preferences) => {
      if (err) {
        console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
        return;
      }
      dataPreferences = val;
      console.info("Succeeded in getting preferences.");
    })
  }
```

#### preferences.getPreferences

getPreferences(context: Context, name: string): Promise<Preferences>

获取Preferences实例，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
namestring是Preferences实例的名称。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Preferences> | Promise对象，返回Preferences实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

let dataPreferences: preferences.Preferences | null = null;
let promise = preferences.getPreferences(context, 'myStore');
promise.then((object: preferences.Preferences) => {
  dataPreferences = object;
  console.info("Succeeded in getting preferences.");
}).catch((err: BusinessError) => {
  console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let dataPreferences: preferences.Preferences | null = null;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let promise = preferences.getPreferences(this.context, 'myStore');
    promise.then((object: preferences.Preferences) => {
      dataPreferences = object;
      console.info("Succeeded in getting preferences.");
    }).catch((err: BusinessError) => {
      console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
    })
  }
```

#### preferences.getPreferences10+

getPreferences(context: Context, options: Options, callback: AsyncCallback<Preferences>): void

获取Preferences实例，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| options | Options | 是 | 与Preferences实例相关的配置选项。 |
| callback | AsyncCallback<Preferences> | 是 | 回调函数。当获取Preferences实例成功，err为undefined，返回Preferences实例；否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();
let dataPreferences: preferences.Preferences | null = null;

let options: preferences.Options = { name: 'myStore' };
preferences.getPreferences(context, options, (err: BusinessError, val: preferences.Preferences) => {
  if (err) {
    console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
    return;
  }
  dataPreferences = val;
  console.info("Succeeded in getting preferences.");
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let dataPreferences: preferences.Preferences | null = null;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    preferences.getPreferences(this.context, options, (err: BusinessError, val: preferences.Preferences) => {
      if (err) {
        console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
        return;
      }
      dataPreferences = val;
      console.info("Succeeded in getting preferences.");
    })
  }
```

#### preferences.getPreferences10+

getPreferences(context: Context, options: Options): Promise<Preferences>

获取Preferences实例，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| options | Options | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Preferences> | Promise对象，返回Preferences实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

let dataPreferences: preferences.Preferences | null = null;
let options: preferences.Options = { name: 'myStore' };
let promise = preferences.getPreferences(context, options);
promise.then((object: preferences.Preferences) => {
  dataPreferences = object;
  console.info("Succeeded in getting preferences.");
}).catch((err: BusinessError) => {
  console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let dataPreferences: preferences.Preferences | null = null;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    let promise = preferences.getPreferences(this.context, options);
    promise.then((object: preferences.Preferences) => {
      dataPreferences = object;
      console.info("Succeeded in getting preferences.");
    }).catch((err: BusinessError) => {
      console.error("Failed to get preferences. code =" + err.code + ", message =" + err.message);
    })
  }
```

#### preferences.getPreferencesSync10+

getPreferencesSync(context: Context, options: Options): Preferences

获取Preferences实例，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| options | Options | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Preferences | 返回Preferences实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';

let context = featureAbility.getContext();
let dataPreferences: preferences.Preferences | null = null;

let options: preferences.Options = { name: 'myStore' };
dataPreferences = preferences.getPreferencesSync(context, options);
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

let dataPreferences: preferences.Preferences | null = null;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    dataPreferences = preferences.getPreferencesSync(this.context, options);
  }
```

#### preferences.deletePreferences

deletePreferences(context: Context, name: string, callback: AsyncCallback<void>): void

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。使用callback异步回调。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

不支持该接口与其他preference接口并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | Preferences实例的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当移除成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |
| 15500010 | Failed to delete the user preferences persistence file. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

preferences.deletePreferences(context, 'myStore', (err: BusinessError) => {
  if (err) {
    console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in deleting preferences.");
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    preferences.deletePreferences(this.context, 'myStore', (err: BusinessError) => {
      if (err) {
        console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
        return;
      }
      console.info("Succeeded in deleting preferences.");
    })
  }
```

#### preferences.deletePreferences

deletePreferences(context: Context, name: string): Promise<void>

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。使用Promise异步回调。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

不支持该接口与其他preference接口并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
namestring是Preferences实例的名称。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |
| 15500010 | Failed to delete the user preferences persistence file. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

let promise = preferences.deletePreferences(context, 'myStore');
promise.then(() => {
  console.info("Succeeded in deleting preferences.");
}).catch((err: BusinessError) => {
  console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let promise = preferences.deletePreferences(this.context, 'myStore');
    promise.then(() => {
      console.info("Succeeded in deleting preferences.");
    }).catch((err: BusinessError) => {
      console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
    })
  }
```

#### preferences.deletePreferences10+

deletePreferences(context: Context, options: Options, callback: AsyncCallback<void>): void

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。使用callback异步回调。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

不支持该接口与其他preference接口并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| options | Options | 是 | 与Preferences实例相关的配置选项。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当移除成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15500010 | Failed to delete the user preferences persistence file. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

let options: preferences.Options = { name: 'myStore' };
preferences.deletePreferences(context, options, (err: BusinessError) => {
  if (err) {
    console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in deleting preferences.");
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    preferences.deletePreferences(this.context, options, (err: BusinessError) => {
      if (err) {
        console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
        return;
      }
      console.info("Succeeded in deleting preferences.");
    })
  }
```

#### preferences.deletePreferences10+

deletePreferences(context: Context, options: Options): Promise<void>

从缓存中删除指定的Preferences实例，若Preferences实例有对应的持久化文件，则同时删除其持久化文件。使用Promise异步回调。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

不支持该接口与其他preference接口并发调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| options | Options | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15500010 | Failed to delete the user preferences persistence file. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

let options: preferences.Options = { name: 'myStore' };
let promise = preferences.deletePreferences(context, options);
promise.then(() => {
  console.info("Succeeded in deleting preferences.");
}).catch((err: BusinessError) => {
  console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    let promise = preferences.deletePreferences(this.context, options);
    promise.then(() => {
      console.info("Succeeded in deleting preferences.");
    }).catch((err: BusinessError) => {
      console.error("Failed to delete preferences. code =" + err.code + ", message =" + err.message);
    })
  }
```

#### preferences.removePreferencesFromCache

removePreferencesFromCache(context: Context, name: string, callback: AsyncCallback<void>): void

从缓存中移除指定的Preferences实例，使用callback异步回调。

应用首次调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| name | string | 是 | Preferences实例的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当移除成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();
preferences.removePreferencesFromCache(context, 'myStore', (err: BusinessError) => {
  if (err) {
    console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in removing preferences.");
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    preferences.removePreferencesFromCache(this.context, 'myStore', (err: BusinessError) => {
      if (err) {
        console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
        return;
      }
      console.info("Succeeded in removing preferences.");
    })
  }
```

#### preferences.removePreferencesFromCache

removePreferencesFromCache(context: Context, name: string): Promise<void>

从缓存中移除指定的Preferences实例，使用Promise异步回调。

应用首次调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
namestring是Preferences实例的名称。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();
let promise = preferences.removePreferencesFromCache(context, 'myStore');
promise.then(() => {
  console.info("Succeeded in removing preferences.");
}).catch((err: BusinessError) => {
  console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let promise = preferences.removePreferencesFromCache(this.context, 'myStore');
    promise.then(() => {
      console.info("Succeeded in removing preferences.");
    }).catch((err: BusinessError) => {
      console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
    })
  }
```

#### preferences.removePreferencesFromCacheSync10+

removePreferencesFromCacheSync(context: Context, name: string): void

从缓存中移除指定的Preferences实例，此为同步接口。

应用首次调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
namestring是Preferences实例的名称。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
let context = featureAbility.getContext();
preferences.removePreferencesFromCacheSync(context, 'myStore');
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    preferences.removePreferencesFromCacheSync(this.context, 'myStore');
  }
```

#### preferences.removePreferencesFromCache10+

removePreferencesFromCache(context: Context, options: Options, callback: AsyncCallback<void>): void

从缓存中移除指定的Preferences实例，使用callback异步回调。

应用首次调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| options | Options | 是 | 与Preferences实例相关的配置选项。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当移除成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();
let options: preferences.Options = { name: 'myStore' };
preferences.removePreferencesFromCache(context, options, (err: BusinessError) => {
  if (err) {
    console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in removing preferences.");
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    preferences.removePreferencesFromCache(this.context, options, (err: BusinessError) => {
      if (err) {
        console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
        return;
      }
      console.info("Succeeded in removing preferences.");
    })
  }
```

#### preferences.removePreferencesFromCache10+

removePreferencesFromCache(context: Context, options: Options): Promise<void>

从缓存中移除指定的Preferences实例，使用Promise异步回调。

应用首次调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| options | Options | 是 | 与Preferences实例相关的配置选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();
let options: preferences.Options = { name: 'myStore' };
let promise = preferences.removePreferencesFromCache(context, options);
promise.then(() => {
  console.info("Succeeded in removing preferences.");
}).catch((err: BusinessError) => {
  console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
})
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    let promise = preferences.removePreferencesFromCache(this.context, options);
    promise.then(() => {
      console.info("Succeeded in removing preferences.");
    }).catch((err: BusinessError) => {
      console.error("Failed to remove preferences. code =" + err.code + ", message =" + err.message);
    })
  }
```

#### preferences.removePreferencesFromCacheSync10+

removePreferencesFromCacheSync(context: Context, options: Options):void

从缓存中移除指定的Preferences实例，此为同步接口。

应用首次调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)接口获取某个Preferences实例后，该实例会被缓存起来，后续调用[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)时不会再次从持久化文件中读取，直接从缓存中获取Preferences实例。调用此接口移除缓存中的实例之后，再次getPreferences将会重新读取持久化文件，生成新的Preferences实例。

调用该接口后，不建议再使用旧的Preferences实例进行数据操作，否则会导致数据一致性问题，应将Preferences实例置为null，系统会统一回收。

若使用[GSKV存储模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#gskv存储)，推荐在进程退出时手动调用一次该接口。此操作会将数据缓存页写入磁盘，可一定程度上减少下一次调用getPreferences接口时的耗时。否则，下一次调用getPreferences接口时底层需要进行数据恢复，数据恢复的耗时取决于未写入磁盘的数据缓存页数量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| options | Options | 是 | 与Preferences实例相关的配置选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 801 | Capability not supported. |
| 15500000 | Inner error. |
| 15501001 | The operations is supported in stage mode only. |
| 15501002 | Invalid dataGroupId. |

**示例：**

FA模型示例：

```ets
// 获取context
import { featureAbility } from '@kit.AbilityKit';
let context = featureAbility.getContext();
let options: preferences.Options = { name: 'myStore' };
preferences.removePreferencesFromCacheSync(context, options);
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let options: preferences.Options = { name: 'myStore' };
    preferences.removePreferencesFromCacheSync(this.context, options);
  }
```

#### StorageType18+

Preferences的存储模式枚举。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| XML | 0 | 表示XML存储模式，这是Preferences的默认存储模式。 特点： 数据XML格式进行存储。对数据的操作发生在内存中，需要调用flush接口进行落盘。 |
| GSKV | 1 | 表示GSKV存储模式。 特点： 数据以GSKV数据库模式进行存储。对数据的操作实时落盘，无需调用flush接口对数据进行落盘。 |


- 在选择存储模式前，建议调用isStorageTypeSupported检查当前平台是否支持对应存储模式。
- 当选择某一模式通过getPreferences接口获取实例后，不允许中途切换模式。
- 首选项不支持不同模式间数据的迁移，若需将数据从一种模式切换至另一种模式，需通过读写首选项的形式进行数据迁移。
- 若需要变更首选项的存储路径，不能通过移动或覆盖文件的方式进行，需通过读写首选项的形式进行数据迁移。

#### preferences.isStorageTypeSupported18+

isStorageTypeSupported(type: StorageType): boolean

判断当前平台是否支持传入的存储模式，此为同步接口。如果当前平台支持传入的存储模式时，该接口返回true；反之，返回false。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | StorageType | 是 | 需要判断是否支持的存储模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | true表示当前平台支持当前校验的存储模式，false表示当前平台不支持当前校验的存储模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: Incorrect parameter types. |

**示例：**

```ets
let xmlType = preferences.StorageType.XML;
let gskvType = preferences.StorageType.GSKV;
let isXmlSupported = preferences.isStorageTypeSupported(xmlType);
let isGskvSupported = preferences.isStorageTypeSupported(gskvType);
console.info("Is xml supported in current platform: " + isXmlSupported);
console.info("Is gskv supported in current platform: " + isGskvSupported);
```

#### Options10+

Preferences实例配置选项。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | Preferences实例的名称。名称长度需大于零且小于等于255字节，名称中不能包含'/'且不能以'/'结尾。 元服务API： 从API version 11开始，该参数支持在元服务中使用。 |
| dataGroupId | string|null|undefined | 否 | 是 | 应用组ID，需要向应用市场获取，详见dataGroupId申请流程。基于dataGroupId的数据共享支持两种场景：1.同一应用的不同进程间共享，只支持三方应用中输入法和输入法的扩展场景使用；2.不同应用间的数据共享，只支持系统应用使用。 为可选参数。指定在此dataGroupId对应的沙箱路径下创建Preferences实例。当此参数不填时，默认在本应用沙箱目录下创建Preferences实例。 模型约束： 此属性仅在Stage模型下可用。 元服务API： 从API version 11开始，该参数支持在元服务中使用。 |
| storageType18+ | StorageType|null|undefined | 否 | 是 | 存储模式，为可选参数。表示当前Preferences实例需要使用的存储模式。当此参数不填时，默认使用XML存储模式。当选择某种存储模式创建Preferences后，不支持中途切换存储模式。 元服务API： 从API version 18开始，该参数支持在元服务中使用。 |

#### Preferences

首选项实例，提供获取和修改存储数据的接口。

下列接口都需先使用[preferences.getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)获取到Preferences实例，再通过此实例调用对应接口。

#### get

get(key: string, defValue: ValueType, callback: AsyncCallback<ValueType>): void

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储Key名称，不能为空，最大长度限制为MAX_KEY_LENGTH。 |
| defValue | ValueType | 是 | 默认返回值。 |
| callback | AsyncCallback<ValueType> | 是 | 回调函数。当获取成功时，err为undefined，data为键对应的值；否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.get('startup', 'default', (err: BusinessError, val: preferences.ValueType) => {
  if (err) {
    console.error("Failed to get value of 'startup'. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in getting value of 'startup'. val： " + val);
})
```

#### get

get(key: string, defValue: ValueType): Promise<ValueType>

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储Key名称，不能为空，最大长度限制为MAX_KEY_LENGTH。 |
| defValue | ValueType | 是 | 默认返回值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<ValueType> | Promise对象，返回键对应的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.get('startup', 'default');
promise.then((data: preferences.ValueType) => {
  console.info("Succeeded in getting value of 'startup'. Data: " + data);
}).catch((err: BusinessError) => {
  console.error("Failed to get value of 'startup'. code =" + err.code + ", message =" + err.message);
})
```

#### getSync10+

getSync(key: string, defValue: ValueType): ValueType

从缓存的Preferences实例中获取键对应的值，如果值为null或者非默认值类型，返回默认数据defValue，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要获取的存储Key名称，不能为空，最大长度限制为MAX_KEY_LENGTH。 |
| defValue | ValueType | 是 | 默认返回值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ValueType | 返回键对应的值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
let value: preferences.ValueType = dataPreferences.getSync('startup', 'default');
```

#### getAll

getAll(callback: AsyncCallback<Object>): void

获取缓存的Preferences实例中的所有键值数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Object> | 是 | 回调函数。当获取成功，err为undefined，value为所有键值数据；否则err为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Mandatory parameters are left unspecified. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 由于ArkTS中无Object.keys，且无法使用for..in...
// 若报ArkTS问题，请将此方法单独抽离至一个ts文件中并暴露，在需要用到的ets文件中引入使用
function getObjKeys(obj: Object): string[] {
  let keys = Object.keys(obj);
  return keys;
}

dataPreferences.getAll((err: BusinessError, value: Object) => {
  if (err) {
    console.error("Failed to get all key-values. code =" + err.code + ", message =" + err.message);
    return;
  }
  let allKeys = getObjKeys(value);
  console.info("getAll keys = " + allKeys);
  console.info("getAll object = " + JSON.stringify(value));
})
```

#### getAll

getAll(): Promise<Object>

获取缓存的Preferences实例中的所有键值数据。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Object> | Promise对象，返回所有包含的键值数据。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 由于ArkTS中无Object.keys，且无法使用for..in...
// 若报ArkTS问题，请将此方法单独抽离至一个ts文件中并暴露，在需要用到的ets文件中引入使用
function getObjKeys(obj: Object): string[] {
  let keys = Object.keys(obj);
  return keys;
}

let promise = dataPreferences.getAll();
promise.then((value: Object) => {
  let allKeys = getObjKeys(value);
  console.info('getAll keys = ' + allKeys);
  console.info("getAll object = " + JSON.stringify(value));
}).catch((err: BusinessError) => {
  console.error("Failed to get all key-values. code =" + err.code + ", message =" + err.message);
})
```

#### getAllSync10+

getAllSync(): Object

获取缓存的Preferences实例中的所有键值数据，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 返回所有包含的键值数据。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```ets
// 由于ArkTS中无Object.keys，且无法使用for..in...
// 若报ArkTS问题，请将此方法单独抽离至一个ts文件中并暴露，在需要用到的ets文件中引入使用
function getObjKeys(obj: Object): string[] {
  let keys = Object.keys(obj);
  return keys;
}

let value = dataPreferences.getAllSync();
let allKeys = getObjKeys(value);
console.info('getAll keys = ' + allKeys);
console.info("getAll object = " + JSON.stringify(value));
```

#### put

put(key: string, value: ValueType, callback: AsyncCallback<void>): void

将数据写入缓存的Preferences实例中，可通过[flush](#ZH-CN_TOPIC_0000002522240628__flush)将Preferences实例持久化，使用callback异步回调。


当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。

当对应的键已经存在时，put()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的Key，不能为空，最大长度限制为MAX_KEY_LENGTH。 |
| value | ValueType | 是 | 存储的新值。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当数据写入成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.put('startup', 'auto', (err: BusinessError) => {
  if (err) {
    console.error("Failed to put value of 'startup'. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in putting value of 'startup'.");
})
```

#### put

put(key: string, value: ValueType): Promise<void>

将数据写入缓存的Preferences实例中，可通过[flush](#ZH-CN_TOPIC_0000002522240628__flush)将Preferences实例持久化，使用Promise异步回调。


当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。

当对应的键已经存在时，put()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的Key，不能为空，最大长度限制为MAX_KEY_LENGTH。 |
| value | ValueType | 是 | 存储的新值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.put('startup', 'auto');
promise.then(() => {
  console.info("Succeeded in putting value of 'startup'.");
}).catch((err: BusinessError) => {
  console.error("Failed to put value of 'startup'. code =" + err.code + ", message =" + err.message);
})
```

#### putSync10+

putSync(key: string, value: ValueType): void

将数据写入缓存的Preferences实例中，可通过[flush](#ZH-CN_TOPIC_0000002522240628__flush)将Preferences实例持久化，此为同步接口。


当value中包含非UTF-8格式的字符串时，请使用Uint8Array类型存储，否则会造成持久化文件出现格式错误造成文件损坏。

当对应的键已经存在时，putSync()方法会覆盖其值。可以使用hasSync()方法检查是否存在对应键值对。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要修改的存储的Key，不能为空，最大长度限制为MAX_KEY_LENGTH。 |
| value | ValueType | 是 | 存储的新值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
dataPreferences.putSync('startup', 'auto');
```

#### has

has(key: string, callback: AsyncCallback<boolean>): void

检查缓存的Preferences实例中是否包含指定Key的存储键值对，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要检查的存储key名称，不能为空，最大长度限制为MAX_KEY_LENGTH。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回Preferences实例是否包含给定key的存储键值对，true表示存在，false表示不存在。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.has('startup', (err: BusinessError, val: boolean) => {
  if (err) {
    console.error("Failed to check the key 'startup'. code =" + err.code + ", message =" + err.message);
    return;
  }
  if (val) {
    console.info("The key 'startup' is contained.");
  } else {
    console.info("The key 'startup' is not contained.");
  }
})
```

#### has

has(key: string): Promise<boolean>

检查缓存的Preferences实例中是否包含指定Key的存储键值对，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要检查的存储key名称，不能为空，最大长度限制为MAX_KEY_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回Preferences实例是否包含给定key的存储键值对，true表示存在，false表示不存在。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.has('startup');
promise.then((val: boolean) => {
  if (val) {
    console.info("The key 'startup' is contained.");
  } else {
    console.info("The key 'startup' does not contain.");
  }
}).catch((err: BusinessError) => {
  console.error("Failed to check the key 'startup'. code =" + err.code + ", message =" + err.message);
})
```

#### hasSync10+

hasSync(key: string): boolean

检查缓存的Preferences实例中是否包含指定Key的存储键值对，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要检查的存储key名称，不能为空，最大长度限制为MAX_KEY_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回Preferences实例是否包含给定key的存储键值对，true表示存在，false表示不存在。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
let isExist: boolean = dataPreferences.hasSync('startup');
if (isExist) {
  console.info("The key 'startup' is contained.");
} else {
  console.info("The key 'startup' does not contain.");
}
```

#### delete

delete(key: string, callback: AsyncCallback<void>): void

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](#ZH-CN_TOPIC_0000002522240628__flush)将Preferences实例持久化，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除的存储Key名称，不能为空，最大长度限制为MAX_KEY_LENGTH。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当删除成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.delete('startup', (err: BusinessError) => {
  if (err) {
    console.error("Failed to delete the key 'startup'. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in deleting the key 'startup'.");
})
```

#### delete

delete(key: string): Promise<void>

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](#ZH-CN_TOPIC_0000002522240628__flush)将Preferences实例持久化，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除的存储key名称，不能为空，最大长度限制为MAX_KEY_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.delete('startup');
promise.then(() => {
  console.info("Succeeded in deleting the key 'startup'.");
}).catch((err: BusinessError) => {
  console.error("Failed to delete the key 'startup'. code =" + err.code +", message =" + err.message);
})
```

#### deleteSync10+

deleteSync(key: string): void

从缓存的Preferences实例中删除名为给定Key的存储键值对，可通过[flush](#ZH-CN_TOPIC_0000002522240628__flush)将Preferences实例持久化，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除的存储key名称，不能为空，最大长度限制为MAX_KEY_LENGTH。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
dataPreferences.deleteSync('startup');
```

#### flush

flush(callback: AsyncCallback<void>): void

将缓存的Preferences实例中的数据异步存储到用户首选项的持久化文件中，使用callback异步回调。

当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

只在XML存储模式下使用，在GSKV存储模式下无需调用，因为当选择该模式时首选项对数据的操作会实时落盘。Preferences存储模式可见[存储模式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#存储模式说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当保存成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Mandatory parameters are left unspecified. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in flushing.");
})
```

#### flush

flush(): Promise<void>

将缓存的Preferences实例中的数据异步存储到用户首选项的持久化文件中，使用Promise异步回调。

当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

只在XML存储模式下使用，在GSKV存储模式下无需调用，因为当选择该模式时首选项对数据的操作会实时落盘。Preferences存储模式可见[存储模式说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-preferences#存储模式说明)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.flush();
promise.then(() => {
  console.info("Succeeded in flushing.");
}).catch((err: BusinessError) => {
  console.error("Failed to flush. code =" + err.code + ", message =" + err.message);
})
```

#### flushSync14+

flushSync(): void

将缓存的Preferences实例中的数据存储到用户首选项的持久化文件中。

当数据未修改或修改后的数据与缓存数据一致时，不会刷新持久化文件。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```ets
dataPreferences.flushSync();
```

#### clear

clear(callback: AsyncCallback<void>): void

清除缓存的Preferences实例中的所有数据，可通过[flush](#ZH-CN_TOPIC_0000002522240628__flush)将Preferences实例持久化，使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当清除成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Mandatory parameters are left unspecified. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

dataPreferences.clear((err: BusinessError) =>{
  if (err) {
    console.error("Failed to clear. code =" + err.code + ", message =" + err.message);
    return;
  }
  console.info("Succeeded in clearing.");
})
```

#### clear

clear(): Promise<void>

清除缓存的Preferences实例中的所有数据，可通过[flush](#ZH-CN_TOPIC_0000002522240628__flush)将Preferences实例持久化，使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let promise = dataPreferences.clear();
promise.then(() => {
  console.info("Succeeded in clearing.");
}).catch((err: BusinessError) => {
  console.error("Failed to clear. code =" + err.code + ", message =" + err.message);
})
```

#### clearSync10+

clearSync(): void

清除缓存的Preferences实例中的所有数据，可通过[flush](#ZH-CN_TOPIC_0000002522240628__flush)将Preferences实例持久化，此为同步接口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**示例：**

```ets
dataPreferences.clearSync();
```

#### on('change')

on(type: 'change', callback: Callback<string>): void

订阅数据变更，订阅的Key的值发生变更后，在执行[flush](#ZH-CN_TOPIC_0000002522240628__flush)方法后，触发callback回调。


当调用[removePreferencesFromCache](#ZH-CN_TOPIC_0000002522240628__preferencesremovepreferencesfromcache)或[deletePreferences](#ZH-CN_TOPIC_0000002522240628__preferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'change'，表示数据变更。 |
| callback | Callback<string> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
}
dataPreferences.on('change', observer);
dataPreferences.putSync('startup', 'manual');
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
```

#### on('multiProcessChange')10+

on(type: 'multiProcessChange', callback: Callback<string>): void

订阅进程间数据变更，多个进程持有同一个首选项文件时，在任意一个进程（包括本进程）执行[flush](#ZH-CN_TOPIC_0000002522240628__flush)方法，持久化文件发生变更后，触发callback回调。

本接口提供给申请了[dataGroupId](#ZH-CN_TOPIC_0000002522240628__options10)的应用进行使用，未申请的应用不推荐使用，多进程操作可能会损坏持久化文件，导致数据丢失。


同一持久化文件在当前进程订阅进程间数据变更的最大数量为50次，超过最大限制后会订阅失败。建议在触发callback回调后及时取消订阅。

当调用[removePreferencesFromCache](#ZH-CN_TOPIC_0000002522240628__preferencesremovepreferencesfromcache)或[deletePreferences](#ZH-CN_TOPIC_0000002522240628__preferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'multiProcessChange'，表示多进程间的数据变更。 |
| callback | Callback<string> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |
| 15500019 | Failed to obtain the subscription service. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
}
dataPreferences.on('multiProcessChange', observer);
dataPreferences.putSync('startup', 'manual');
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
```

#### on('dataChange')12+

on(type: 'dataChange', keys: Array<string>, callback: Callback<Record<string, ValueType>>): void

精确订阅数据变更，只有被订阅的key值发生变更后，在执行[flush](#ZH-CN_TOPIC_0000002522240628__flush)方法后，触发callback回调。


当调用[removePreferencesFromCache](#ZH-CN_TOPIC_0000002522240628__preferencesremovepreferencesfromcache)或[deletePreferences](#ZH-CN_TOPIC_0000002522240628__preferencesdeletepreferences)后，订阅的数据变更会主动取消订阅，在重新[getPreferences](#ZH-CN_TOPIC_0000002522240628__preferencesgetpreferences)后需要重新订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'dataChange'，表示精确的数据变更。 |
| keys | Array<string> | 是 | 需要订阅的key集合。 |
| callback | Callback<Record<string, ValueType>> | 是 | 回调函数。回调支持返回多个键值对，其中键为发生变更的订阅key，值为变更后的数据：支持number、string、boolean、Array<number>、Array<string>、Array<boolean>、Uint8Array、object类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (data: Record<string, preferences.ValueType>) => {
  for (const keyValue of Object.entries(data)) {
    console.info(`observer : ${keyValue}`);
  }
  console.info("The observer called.");
}
let keys = ['name', 'age'];
dataPreferences.on('dataChange', keys, observer);
dataPreferences.putSync('name', 'xiaohong');
dataPreferences.putSync('weight', 125);
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
```

#### off('change')

off(type: 'change', callback?: Callback<string>): void

取消订阅数据变更。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'change'，表示数据变更。 |
| callback | Callback<string> | 否 | 需要取消的回调函数，不填写则全部取消。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
}
dataPreferences.on('change', observer);
dataPreferences.putSync('startup', 'auto');
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
dataPreferences.off('change', observer);
```

#### off('multiProcessChange')10+

off(type: 'multiProcessChange', callback?: Callback<string>): void

取消订阅进程间数据变更。

本接口提供给申请了[dataGroupId](#ZH-CN_TOPIC_0000002522240628__options10)的应用进行使用，未申请的应用不推荐使用，多进程操作可能会损坏持久化文件，导致数据丢失。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'multiProcessChange'，表示多进程间的数据变更。 |
| callback | Callback<string> | 否 | 需要取消的回调函数，不填写则全部取消。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (key: string) => {
  console.info("The key " + key + " changed.");
}
dataPreferences.on('multiProcessChange', observer);
dataPreferences.putSync('startup', 'auto');
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
dataPreferences.off('multiProcessChange', observer);
```

#### off('dataChange')12+

off(type: 'dataChange', keys: Array<string>, callback?: Callback<Record<string, ValueType>>): void

取消精确订阅数据变更。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件类型，固定值'dataChange'，表示精确的数据变更。 |
| keys | Array<string> | 是 | 需要取消订阅的key集合，当keys为空数组时，表示取消订阅全部key；当keys为非空数组时，表示只取消订阅key集合中的key。 |
| callback | Callback<Record<string, ValueType>> | 否 | 需要取消的回调函数，若callback不填写，表示所有的callback都需要处理；若callback填写，表示只处理该callback。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[用户首选项错误码](用户首选项错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 15500000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let observer = (data: Record<string, preferences.ValueType>) => {
  for (const keyValue of Object.entries(data)) {
    console.info(`observer : ${keyValue}`);
  }
  console.info("The observer called.");
}
let keys = ['name', 'age'];
dataPreferences.on('dataChange', keys, observer);
dataPreferences.putSync('name', 'xiaohong');
dataPreferences.putSync('weight', 125);
dataPreferences.flush((err: BusinessError) => {
  if (err) {
    console.error("Failed to flush. Cause: " + err);
    return;
  }
  console.info("Succeeded in flushing.");
})
dataPreferences.off('dataChange', keys, observer);
```

#### ValueType

type ValueType = number | string | boolean | Array<number> | Array<string> | Array<boolean> | Uint8Array | object | bigint

表示支持的值类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

| 类型 | 说明 |
| --- | --- |
| number | 表示值类型为数字。 |
| string | 表示值类型为字符串。 |
| boolean | 表示值类型为布尔值。 |
| Array<number> | 表示值类型为数字类型的数组。 |
| Array<boolean> | 表示值类型为布尔类型的数组。 |
| Array<string> | 表示值类型为字符串类型的数组。 |
| Uint8Array11+ | 表示值类型为8位无符号整型的数组。 |
| object12+ | 表示值类型为对象。 |
| bigint12+ | 表示值类型为任意精度格式的整数。 |