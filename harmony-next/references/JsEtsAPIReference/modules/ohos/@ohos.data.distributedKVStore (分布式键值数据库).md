# @ohos.data.distributedKVStore (分布式键值数据库)

分布式键值数据库为应用程序提供不同设备间数据库的分布式协同能力。通过调用分布式键值数据库各个接口，应用程序可将数据保存到分布式键值数据库中，并可对分布式键值数据库中的数据进行增加、删除、修改、查询、端端同步等操作。

该模块提供以下常用功能：

- [KVManager](#ZH-CN_TOPIC_0000002553360553__kvmanager)：分布式键值数据库管理实例，用于获取数据库的相关信息。

- [KVStoreResultSet](#ZH-CN_TOPIC_0000002553360553__kvstoreresultset)：提供获取数据库结果集的相关方法，包括查询和移动数据读取位置等。

- [Query](#ZH-CN_TOPIC_0000002553360553__query)：使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。

- [SingleKVStore](#ZH-CN_TOPIC_0000002553360553__singlekvstore)：单版本分布式键值数据库，不对数据所属设备进行区分，提供查询数据和端端同步数据的方法。

- [DeviceKVStore](#ZH-CN_TOPIC_0000002553360553__devicekvstore)：设备协同数据库，继承自[SingleKVStore](#ZH-CN_TOPIC_0000002553360553__singlekvstore)，以设备维度对数据进行区分，提供查询数据和端端同步数据的方法。


本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { distributedKVStore } from '@kit.ArkData';
```

#### KVManagerConfig

提供KVManager实例的配置信息，包括调用方的包名和应用的上下文。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | Base[Context](../../topics/misc/UIAbilityContext.md) | 否 | 否 | 应用的上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 从API version 10开始，context的参数类型为[BaseContext](../../topics/misc/BaseContext.md)。 |
bundleNamestring否否调用方的包名。

#### Constants

分布式键值数据库常量。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| MAX_KEY_LENGTH | number | 是 | 否 | 值为1024，表示数据库中Key允许的最大长度，单位字节。 |
| MAX_VALUE_LENGTH | number | 是 | 否 | 值为4194303，表示数据库中Value允许的最大长度，单位字节。 |
| MAX_KEY_LENGTH_DEVICE | number | 是 | 否 | 值为896，表示设备协同数据库中Key允许的最大长度，单位字节。 |
| MAX_STORE_ID_LENGTH | number | 是 | 否 | 值为128，表示数据库标识符允许的最大长度，单位字节。 |
| MAX_QUERY_LENGTH | number | 是 | 否 | 值为512000，表示最大查询长度，单位字节。 |
| MAX_BATCH_SIZE | number | 是 | 否 | 值为128，表示最大批处理操作数量。 |

#### ValueType

数据类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STRING | 0 | 表示值类型为字符串。 |
| INTEGER | 1 | 表示值类型为整数。 |
| FLOAT | 2 | 表示值类型为浮点数。 |
| BYTE_ARRAY | 3 | 表示值类型为字节数组。 |
| BOOLEAN | 4 | 表示值类型为布尔值。 |
| DOUBLE | 5 | 表示值类型为双浮点数。 |

#### Value

存储在数据库中的值对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | ValueType | 否 | 否 | 值类型。 |
| value | Uint8Array | string | number | boolean | 否 | 否 | 值。 |

#### Entry

存储在数据库中的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | 否 | 否 | 键值。 |
| value | Value | 否 | 否 | 值对象。 |

#### ChangeNotification

数据变更时通知的对象，包括数据插入的数据、更新的数据、删除的数据和设备ID。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| insertEntries | Entry[] | 否 | 否 | 数据添加记录。 |
| updateEntries | Entry[] | 否 | 否 | 数据更新记录。 |
| deleteEntries | Entry[] | 否 | 否 | 数据删除记录。 |
| deviceId | string | 否 | 否 | 设备ID，此处为设备UUID。 |

#### SyncMode

同步模式枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PULL_ONLY | 0 | 表示只能从远端拉取数据到本端。 |
| PUSH_ONLY | 1 | 表示只能从本端推送数据到远端。 |
| PUSH_PULL | 2 | 表示从本端推送数据到远端，然后从远端拉取数据到本端。 |

#### SubscribeType

订阅类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SUBSCRIBE_TYPE_LOCAL | 0 | 表示订阅本地数据变更。 |
| SUBSCRIBE_TYPE_REMOTE | 1 | 表示订阅远端数据变更。 |
| SUBSCRIBE_TYPE_ALL | 2 | 表示订阅远端和本地数据变更。 |

#### KVStoreType

分布式键值数据库类型枚举。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE_COLLABORATION | 0 | 表示多设备协同数据库。 数据库特点： 数据以设备的维度管理，不存在冲突；支持按照设备的维度查询数据。 系统能力： SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |
| SINGLE_VERSION | 1 | 表示单版本数据库。 数据库特点： 数据不分设备，设备之间修改相同的Key会覆盖。 系统能力： SystemCapability.DistributedDataManager.KVStore.Core |

#### SecurityLevel

数据库的安全级别枚举。

在单设备使用场景下，KV数据库支持修改securityLevel参数进行安全等级升级。升级操作需要注意以下几点：

- 该操作不支持跨设备同步的数据库。不同安全等级的数据库之间不能进行数据同步。若需升级数据库的安全等级，建议重新创建更高安全等级的数据库。
- 关闭当前数据库后，修改securityLevel参数以重新设置数据库的安全等级，然后重新打开数据库。
- 该操作仅支持升级，例如从S2到S3，不支持降级，例如从S3到S2。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| S1 | 2 | 表示数据库的安全级别为低级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致有限的不利影响。 例如，性别、国籍，用户申请记录等。 |
| S2 | 3 | 表示数据库的安全级别为中级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严重的不利影响。 例如，个人详细通信地址，姓名昵称等。 |
| S3 | 5 | 表示数据库的安全级别为高级别，数据的泄露、篡改、破坏、销毁可能会给个人或组织导致严峻的不利影响。 例如，个人实时精确定位信息、运动轨迹等。 |
| S4 | 6 | 表示数据库的安全级别为关键级别，业界法律法规中定义的特殊数据类型，涉及个人的最私密领域的信息或者一旦泄露、篡改、破坏、销毁可能会给个人或组织造成重大的不利影响数据。 例如，政治观点、宗教、和哲学信仰、工会成员资格、基因数据、生物信息、健康和性生活状况、性取向等或设备认证鉴权、个人的信用卡等财务信息。 |

#### Options

用于提供创建数据库的配置信息。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| createIfMissing | boolean | 否 | 是 | 当数据库文件不存在时是否创建数据库，true为创建，false为不创建，默认为true。 系统能力： SystemCapability.DistributedDataManager.KVStore.Core |
| encrypt | boolean | 否 | 是 | 设置数据库文件是否加密，true为加密，false为不加密，默认为false。 系统能力： SystemCapability.DistributedDataManager.KVStore.Core |
| backup | boolean | 否 | 是 | 设置数据库文件是否备份，true为备份，false为不备份，默认为true。 系统能力： SystemCapability.DistributedDataManager.KVStore.Core |
| autoSync | boolean | 否 | 是 | 设置数据库是否支持跨设备自动同步。默认为false，即只支持手动同步。配置为true，即只支持在跨设备Call调用实现的多端协同中生效，其他场景无法生效。 系统能力： SystemCapability.DistributedDataManager.KVStore.Core 需要权限： ohos.permission.DISTRIBUTED_DATASYNC |
| kvStoreType | KVStoreType | 否 | 是 | 设置要创建的数据库类型，默认为DEVICE_COLLABORATION，即多设备协同数据库。 系统能力： SystemCapability.DistributedDataManager.KVStore.Core |
| securityLevel | SecurityLevel | 否 | 否 | 设置数据库安全级别。 系统能力： SystemCapability.DistributedDataManager.KVStore.Core |
| schema | Schema | 否 | 是 | 设置定义存储在数据库中的值，默认为undefined，即不使用Schema。 系统能力： SystemCapability.DistributedDataManager.KVStore.DistributedKVStore |

**Schema**

表示数据库模式，可以在创建或打开数据库时创建Schema对象并将它们放入[Options](#ZH-CN_TOPIC_0000002553360553__options)中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| root | FieldNode | 否 | 否 | 存放了Value中所有字段的定义。 |
| indexes | Array<string> | 否 | 否 | 索引字段定义，只有通过此字段指定的FieldNode才会创建索引，格式为：'$.field1', '$.field2'。 |
| mode | number | 否 | 否 | Schema的模式，可以取值0或1，0表示COMPATIBLE模式，1表示STRICT模式。 |
| skip | number | 否 | 否 | 支持在检查Value时，跳过skip指定的字节数，且取值范围为[0, 4 * 1024 * 1024 - 2]字节。 |

STRICT：STRICT模式要求用户插入的值必须与Schema定义严格匹配，字段数量和格式都不能有差异。如果不匹配，数据库将在插入数据时返回错误。

COMPATIBLE：选择为COMPATIBLE模式时，数据库在检查Value格式时较为宽松，只要Value具有Schema描述的特征即可，允许存在额外字段。例如，定义了id、name字段时，可以插入id、name、age等多个字段。

#### constructor

constructor()

用于创建Schema实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**示例：**

```ets
let child1 = new distributedKVStore.FieldNode('id');
child1.type = distributedKVStore.ValueType.INTEGER;
child1.nullable = false;
child1.default = '1';
let child2 = new distributedKVStore.FieldNode('name');
child2.type = distributedKVStore.ValueType.STRING;
child2.nullable = false;
child2.default = 'zhangsan';

let schema = new distributedKVStore.Schema();
schema.root.appendChild(child1);
schema.root.appendChild(child2);
schema.indexes = ['$.id', '$.name'];
schema.mode = 1;
schema.skip = 0;
```

#### FieldNode

表示 Schema 实例的节点，提供定义存储在数据库中的值的方法。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| nullable | boolean | 否 | 否 | 表示数据库字段是否可以为空。true表示此节点数据可以为空，false表示此节点数据不能为空。 |
| default | string | 否 | 否 | 表示FieldNode的默认值。default需传入type对应类型可解析的字符串字面量，确保内容类型与type字段类型一致。 |
| type | number | 否 | 否 | 表示指定节点对应的数据类型，取值为ValueType对应的枚举值。暂不支持BYTE_ARRAY，使用此类型会导致getKVStore失败。 |

#### constructor

constructor(name: string)

用于创建带有string字段FieldNode实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | FieldNode的值，不能为空，且不大于64个字符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

#### appendChild

appendChild(child: FieldNode): boolean

在当前 FieldNode 中添加一个子节点。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| child | FieldNode | 是 | 要附加的域节点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示子节点成功添加到FieldNode；返回false则表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
try {
  let node: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("root");
  let child1: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child1");
  let child2: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child2");
  let child3: distributedKVStore.FieldNode | null = new distributedKVStore.FieldNode("child3");
  node.appendChild(child1);
  node.appendChild(child2);
  node.appendChild(child3);
  console.info("appendNode " + JSON.stringify(node));
  child1 = null;
  child2 = null;
  child3 = null;
  node = null;
} catch (e) {
  console.error("AppendChild " + e);
}
```

#### distributedKVStore.createKVManager

createKVManager(config: KVManagerConfig): KVManager

创建一个KVManager对象实例，用于管理数据库对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | KVManagerConfig | 是 | 提供KVManager实例的配置信息，包括调用方的包名（不能为空）和用户信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| KVManager | 返回创建的KVManager对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

Stage模型下的示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let kvManager: distributedKVStore.KVManager;
let appId: string = 'com.example.datamanagertest';

export default class EntryAbility extends UIAbility {
  onCreate() {
    console.info("MyAbilityStage onCreate");
    let context = this.context;
    const kvManagerConfig: distributedKVStore.KVManagerConfig = {
      context: context,
      bundleName: appId
    }
    try {
      kvManager = distributedKVStore.createKVManager(kvManagerConfig);
      console.info("Succeeded in creating KVManager");
    } catch (e) {
      let error = e as BusinessError;
      console.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
    }
    if (kvManager !== undefined) {
      // 进行后续创建数据库等相关操作
      // ...
    }
```

FA模型下的示例：

```ets
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let kvManager: distributedKVStore.KVManager;
let appId: string = 'com.example.datamanagertest';
let context = featureAbility.getContext();
const kvManagerConfig: distributedKVStore.KVManagerConfig = {
  context: context,
  bundleName: appId
}
try {
  kvManager = distributedKVStore.createKVManager(kvManagerConfig);
  console.info("Succeeded in creating KVManager");
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to create KVManager.code is ${error.code},message is ${error.message}`);
}
if (kvManager !== undefined) {
  kvManager = kvManager as distributedKVStore.KVManager;
  // 进行后续创建数据库等相关操作
  // ...
}
```

#### KVManager

分布式键值数据库管理实例，用于获取分布式键值数据库的相关信息。在调用KVManager的方法前，需要先通过[createKVManager](#ZH-CN_TOPIC_0000002553360553__distributedkvstorecreatekvmanager)构建一个KVManager实例。

#### getKVStore

getKVStore<T>(storeId: string, options: Options, callback: AsyncCallback<T>): void

通过指定options和storeId，创建并获取分布式键值数据库，使用callback异步回调。

注意：

在获取已有的分布式键值数据库时，如果数据库文件无法打开（例如文件头损坏），将触发自动重建逻辑，并返回新创建的分布式键值数据库实例。建议对重要且无法重新生成的数据使用备份恢复功能，以防止数据丢失。有关备份恢复的使用方法，请参阅[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| storeId | string | 是 | 数据库唯一标识符，长度不大于MAX_STORE_ID_LENGTH，且只能包含字母数字或下划线_。 |
| options | Options | 是 | 创建分布式键值实例的配置信息。 |
| callback | AsyncCallback<T> | 是 | 回调函数。返回创建的分布式键值数据库实例（根据kvStoreType的不同，可以创建SingleKVStore实例和DeviceKVStore实例）。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码]([分布式键值数据库错误码](../../errors/分布式键值数据库错误码.md).md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100002 | Open existed database with changed options. |
| 15100003 | Database corrupted. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;
try {
  const options: distributedKVStore.Options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
    securityLevel: distributedKVStore.SecurityLevel.S3
  };
  kvManager.getKVStore('storeId', options, (err: BusinessError, store: distributedKVStore.SingleKVStore) => {
    if (err) {
      console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info("Succeeded in getting KVStore");
    kvStore = store;
    if (kvStore !== null) {
       // 进行后续相关数据操作，包括数据的增、删、改、查、订阅数据变化等操作
       // ...
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getKVStore

getKVStore<T>(storeId: string, options: Options): Promise<T>

指定options和storeId，创建并获取分布式键值数据库，使用Promise回调。

注意：

获取已有的分布式键值数据库时，如果数据库文件无法打开（如文件头损坏），将触发自动重建逻辑，并返回新创建的分布式键值数据库实例。建议对重要且无法重新生成的数据使用备份恢复功能，防止数据丢失。备份恢复的使用方法详见[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| storeId | string | 是 | 数据库唯一标识符，长度不大于MAX_STORE_ID_LENGTH，且只能包含字母数字或下划线_。 |
| options | Options | 是 | 创建分布式键值实例的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<T> | Promise对象。返回创建的分布式键值数据库实例（根据kvStoreType的不同，可以创建SingleKVStore实例和DeviceKVStore实例）。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100002 | Open existed database with changed options. |
| 15100003 | Database corrupted. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;
try {
  const options: distributedKVStore.Options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
    securityLevel: distributedKVStore.SecurityLevel.S3
  };
  kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options).then((store: distributedKVStore.SingleKVStore) => {
    console.info("Succeeded in getting KVStore");
    kvStore = store;
  }).catch((err: BusinessError) => {
    console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### closeKVStore

closeKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void

通过storeId的值关闭指定的分布式键值数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256。 |
| storeId | string | 是 | 要关闭的数据库唯一标识符，长度不大于MAX_STORE_ID_LENGTH，且只能包含字母数字或下划线_。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当要关闭的数据库成功关闭，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;
const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: false,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
  schema: undefined,
  securityLevel: distributedKVStore.SecurityLevel.S3
}
try {
  kvManager.getKVStore('storeId', options, async (err: BusinessError, store: distributedKVStore.SingleKVStore | null) => {
    if (err != undefined) {
      console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in getting KVStore');
    kvStore = store;
    kvStore = null;
    store = null;
    if (kvManager != undefined) {
      // appId为createKVManager中的appId
      kvManager.closeKVStore(appId, 'storeId', (err: BusinessError)=> {
        if (err != undefined) {
          console.error(`Failed to close KVStore.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in closing KVStore');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### closeKVStore

closeKVStore(appId: string, storeId: string): Promise<void>

通过storeId的值关闭指定的分布式键值数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256。 |
| storeId | string | 是 | 要关闭的数据库唯一标识符，长度不大于MAX_STORE_ID_LENGTH，且只能包含字母数字或下划线_。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;

const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: false,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
  schema: undefined,
  securityLevel: distributedKVStore.SecurityLevel.S3
}
try {
  kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options).then(async (store: distributedKVStore.SingleKVStore | null) => {
    console.info('Succeeded in getting KVStore');
    kvStore = store;
    kvStore = null;
    store = null;
    if (kvManager != undefined) {
      // appId为createKVManager中的appId
      kvManager.closeKVStore(appId, 'storeId').then(() => {
        console.info('Succeeded in closing KVStore');
      }).catch((err: BusinessError) => {
        console.error(`Failed to close KVStore.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to close KVStore.code is ${error.code},message is ${error.message}`);
}
```

#### deleteKVStore

deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void

通过storeId的值删除指定的分布式键值数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256。 |
| storeId | string | 是 | 要删除的数据库唯一标识符，长度不大于MAX_STORE_ID_LENGTH，且只能包含字母数字或下划线_。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当要删除的数据库成功删除，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100004 | Not found. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;

const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: false,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
  schema: undefined,
  securityLevel: distributedKVStore.SecurityLevel.S3
}
try {
  kvManager.getKVStore('storeId', options, async (err: BusinessError, store: distributedKVStore.SingleKVStore | null) => {
    if (err != undefined) {
      console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in getting KVStore');
    kvStore = store;
    kvStore = null;
    store = null;
    if (kvManager != undefined) {
      // appId为createKVManager中的appId
      kvManager.deleteKVStore(appId, 'storeId', (err: BusinessError) => {
        if (err != undefined) {
          console.error(`Failed to delete KVStore.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info(`Succeeded in deleting KVStore`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to delete KVStore.code is ${error.code},message is ${error.message}`);
}
```

#### deleteKVStore

deleteKVStore(appId: string, storeId: string): Promise<void>

通过storeId的值删除指定的分布式键值数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256。 |
| storeId | string | 是 | 要删除的数据库唯一标识符，长度不大于MAX_STORE_ID_LENGTH，且只能包含字母数字或下划线_。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100004 | Not found. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let kvStore: distributedKVStore.SingleKVStore | null = null;

const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: false,
  kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
  schema: undefined,
  securityLevel: distributedKVStore.SecurityLevel.S3
}
try {
  kvManager.getKVStore<distributedKVStore.SingleKVStore>('storeId', options).then(async (store: distributedKVStore.SingleKVStore | null) => {
    console.info('Succeeded in getting KVStore');
    kvStore = store;
    kvStore = null;
    store = null;
    if (kvManager != undefined) {
      // appId为createKVManager中的appId
      kvManager.deleteKVStore(appId, 'storeId').then(() => {
        console.info('Succeeded in deleting KVStore');
      }).catch((err: BusinessError) => {
        console.error(`Failed to delete KVStore.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get KVStore.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to delete KVStore.code is ${error.code},message is ${error.message}`);
}
```

#### getAllKVStoreId

getAllKVStoreId(appId: string, callback: AsyncCallback<string[]>): void

获取所有通过[getKVStore](#ZH-CN_TOPIC_0000002553360553__getkvstore)方法创建的且没有调用[deleteKVStore](#ZH-CN_TOPIC_0000002553360553__deletekvstore)方法删除的分布式键值数据库的storeId，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256。 |
| callback | AsyncCallback<string[]> | 是 | 回调函数。返回所有创建的分布式键值数据库的storeId。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // appId为createKVManager中的appId
  kvManager.getAllKVStoreId(appId, (err: BusinessError, data: string[]) => {
    if (err != undefined) {
      console.error(`Failed to get AllKVStoreId.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in getting AllKVStoreId');
    console.info(`GetAllKVStoreId size = ${data.length}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get AllKVStoreId.code is ${error.code},message is ${error.message}`);
}
```

#### getAllKVStoreId

getAllKVStoreId(appId: string): Promise<string[]>

获取所有通过[getKVStore](#ZH-CN_TOPIC_0000002553360553__getkvstore)方法创建的且没有调用[deleteKVStore](#ZH-CN_TOPIC_0000002553360553__deletekvstore)方法删除的分布式键值数据库的storeId，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的BundleName，不可为空且长度不大于256。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string[]> | Promise对象。返回所有创建的分布式键值数据库的storeId。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // appId为createKVManager中的appId
  console.info('GetAllKVStoreId');
  kvManager.getAllKVStoreId(appId).then((data: string[]) => {
    console.info('Succeeded in getting AllKVStoreId');
    console.info(`GetAllKVStoreId size = ${data.length}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get AllKVStoreId.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get AllKVStoreId.code is ${error.code},message is ${error.message}`);
}
```

#### on('distributedDataServiceDie')

on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void

订阅服务状态变更通知。如果服务终止，需要重新注册数据变更通知和端端同步完成事件回调通知，并且端端同步操作会返回失败。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'distributedDataServiceDie'，即服务状态变更事件。 |
| deathCallback | Callback<void> | 是 | 回调函数。订阅成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info('KVManagerOn');
  const deathCallback = () => {
    console.info('death callback call');
  }
  kvManager.on('distributedDataServiceDie', deathCallback);
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### off('distributedDataServiceDie')

off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void

取消订阅服务状态变更通知。参数中的deathCallback必须是已经订阅过的deathCallback，否则会取消订阅失败。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'distributedDataServiceDie'，即服务状态变更事件。 |
| deathCallback | Callback<void> | 否 | 回调函数。如果该参数不填，那么会将之前订阅过的所有的deathCallback取消订阅。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  console.info('KVManagerOff');
  const deathCallback = () => {
    console.info('death callback call');
  }
  kvManager.off('distributedDataServiceDie', deathCallback);
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### KVStoreResultSet

提供获取数据库结果集的相关方法，包括查询和移动数据读取位置等。同时允许打开的结果集的最大数量为8个。

KVStoreResultSet实例不会实时刷新。使用结果集后，如果数据库中的数据发生变化（如增删改操作），需要重新查询才能获取到最新的数据。

在调用KVStoreResultSet的方法前，需要先通过[getKVStore](#ZH-CN_TOPIC_0000002553360553__getkvstore)构建一个SingleKVStore或者DeviceKVStore实例。


KVStoreResultSet的游标起始位置为-1。

#### getCount

getCount(): number

获取结果集中的总行数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回数据的总行数。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let count: number;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    count = resultSet.getCount();
    console.info("getCount succeed:" + count);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("getCount failed: " + e);
}
```

#### getPosition

getPosition(): number

获取结果集中当前的读取位置。读取位置会因[moveToFirst](#ZH-CN_TOPIC_0000002553360553__movetofirst)、[moveToLast](#ZH-CN_TOPIC_0000002553360553__movetolast)等操作而发生变化。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前读取位置。取值范围>= -1，值为 -1 时表示还未开始读取，值为 0 时表示第一行。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let position: number;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeeded.');
    resultSet = result;
    position = resultSet.getPosition();
    console.info("getPosition succeed:" + position);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("getPosition failed: " + e);
}
```

#### moveToFirst

moveToFirst(): boolean

将读取位置移动到第一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    moved = resultSet.moveToFirst();
    console.info("moveToFirst succeed: " + moved);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("moveToFirst failed " + e);
}
```

#### moveToLast

moveToLast(): boolean

将读取位置移动到最后一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    moved = resultSet.moveToLast();
    console.info("moveToLast succeed:" + moved);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("moveToLast failed: " + e);
}
```

#### moveToNext

moveToNext(): boolean

将读取位置移动到下一行。如果结果集为空，则返回false。适用于全量获取数据库结果集的场景。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    do {
      moved = resultSet.moveToNext();
      console.info("moveToNext succeed: " + moved);
    } while (moved)
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("moveToNext failed: " + e);
}
```

#### moveToPrevious

moveToPrevious(): boolean

将读取位置移动到上一行。如果结果集为空，则返回false。适用于全量获取数据库结果集的场景。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    moved = resultSet.moveToLast();
    moved = resultSet.moveToPrevious();
    console.info("moveToPrevious succeed:" + moved);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("moveToPrevious failed: " + e);
}
```

#### move

move(offset: number): boolean

将读取位置移动到当前位置的相对偏移量。即当前游标位置向下偏移 offset 行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | number | 是 | 表示与当前位置的相对偏移量，正偏移表示向前移动，负偏移表示向后移动。当游标超出结果集最前或者最后的位置时，接口返回false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting resultSet');
    resultSet = result;
    moved = resultSet.move(2); //若当前位置为0，将读取位置从绝对位置为0的位置移动2行，即移动到绝对位置为2，行数为3的位置
    console.info(`Succeeded in moving.moved = ${moved}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to move.code is ${error.code},message is ${error.message}`);
}
```

#### moveToPosition

moveToPosition(position: number): boolean

将读取位置从 0 移动到绝对位置。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | number | 是 | 表示绝对位置。当绝对位置超出结果集最前或者最后的位置时，接口返回false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示操作成功；返回false则表示操作失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let moved: boolean;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting resultSet');
    resultSet = result;
    moved = resultSet.moveToPosition(1);
    console.info(`Succeeded in moving to position.moved=${moved}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to move to position.code is ${error.code},message is ${error.message}`);
}
```

#### isFirst

isFirst(): boolean

检查读取位置是否为第一行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置为第一行；返回false表示读取位置不是第一行。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let isFirst: boolean;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    isFirst = resultSet.isFirst();
    console.info("Check isFirst succeed:" + isFirst);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("Check isFirst failed: " + e);
}
```

#### isLast

isLast(): boolean

检查读取位置是否为最后一行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置为最后一行；返回false表示读取位置不是最后一行。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let isLast: boolean;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    isLast = resultSet.isLast();
    console.info("Check isLast succeed: " + isLast);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("Check isLast failed: " + e);
}
```

#### isBeforeFirst

isBeforeFirst(): boolean

检查读取位置是否在第一行之前。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置在第一行之前；返回false表示读取位置不在第一行之前。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    let isBeforeFirst = resultSet.isBeforeFirst();
    console.info("Check isBeforeFirst succeed: " + isBeforeFirst);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("Check isBeforeFirst failed: " + e);
}
```

#### isAfterLast

isAfterLast(): boolean

检查读取位置是否在最后一行之后。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示读取位置在最后一行之后；返回false表示读取位置不在最后一行之后。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    let isAfterLast = resultSet.isAfterLast();
    console.info("Check isAfterLast succeed:" + isAfterLast);
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("Check isAfterLast failed: " + e);
}
```

#### getEntry

getEntry(): Entry

从当前位置获取对应的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Entry | 返回键值对。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('getResultSet succeed.');
    resultSet = result;
    let entry = resultSet.getEntry();
    console.info("getEntry succeed:" + JSON.stringify(entry));
  }).catch((err: BusinessError) => {
    console.error('getResultSet failed: ' + err);
  });
} catch (e) {
  console.error("getEntry failed: " + e);
}
```

#### Query

使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。一个Query对象中谓词数量上限为256个。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

#### constructor

constructor()

用于创建Query实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

#### reset

reset(): Query

重置Query对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回重置的Query对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.equalTo("key", "value");
    console.info("query is " + query.getSqlLike());
    query.reset();
    console.info("query is " + query.getSqlLike());
  }
  query = null;
} catch (e) {
  console.error("simply calls should be ok :" + e);
}
```

#### equalTo

equalTo(field: string, value: number|string|boolean): Query

构造一个Query对象来查询具有指定字段的条目，其值等于指定的值。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用equalTo时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string|boolean | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.equalTo("field", "value");
    console.info(`query is ${query.getSqlLike()}`);
  }
  query = null;
} catch (e) {
  let error = e as BusinessError;
  console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### notEqualTo

notEqualTo(field: string, value: number|string|boolean): Query

构造一个Query对象以查询具有指定字段且值不等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用notEqualTo时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string|boolean | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.notEqualTo("field", "value");
    console.info(`query is ${query.getSqlLike()}`);
  }
  query = null;
} catch (e) {
  let error = e as BusinessError;
  console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### greaterThan

greaterThan(field: string, value: number|string|boolean): Query

构造一个Query对象以查询具有大于指定值的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用greaterThan时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string|boolean | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.greaterThan("field", "value");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### lessThan

lessThan(field: string, value: number|string): Query

构造一个Query对象以查询具有小于指定值的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用lessThan时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.lessThan("field", "value");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### greaterThanOrEqualTo

greaterThanOrEqualTo(field: string, value: number|string): Query

构造一个Query对象以查询具有指定字段且值大于或等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用greaterThanOrEqualTo时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.greaterThanOrEqualTo("field", "value");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### lessThanOrEqualTo

lessThanOrEqualTo(field: string, value: number|string): Query

构造一个Query对象以查询具有指定字段且值小于或等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用lessThanOrEqualTo时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | number|string | 是 | 表示指定的值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.lessThanOrEqualTo("field", "value");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### isNull

isNull(field: string): Query

构造一个Query对象以查询具有值为null的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用isNull时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.isNull("field");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### inNumber

inNumber(field: string, valueList: number[]): Query

构造一个Query对象以查询具有指定字段的条目，其值在指定的值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用inNumber时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| valueList | number[] | 是 | 表示指定的值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.inNumber("field", [0, 1]);
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### inString

inString(field: string, valueList: string[]): Query

构造一个Query对象以查询具有指定字段的条目，其值在指定的字符串值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用inString时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| valueList | string[] | 是 | 表示指定的字符串值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.inString("field", ['test1', 'test2']);
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### notInNumber

notInNumber(field: string, valueList: number[]): Query

构造一个Query对象以查询具有指定字段的条目，该字段的值不在指定的值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用notInNumber时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| valueList | number[] | 是 | 表示指定的值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notInNumber("field", [0, 1]);
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### notInString

notInString(field: string, valueList: string[]): Query

构造一个Query对象以查询具有指定字段且值不在指定字符串值列表中的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用notInString时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| valueList | string[] | 是 | 表示指定的字符串值列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notInString("field", ['test1', 'test2']);
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### like

like(field: string, value: string): Query

构造一个Query对象以查询具有与指定字符串值相似的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用like时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | string | 是 | 表示指定的字符串值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.like("field", "value");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### unlike

unlike(field: string, value: string): Query

构造一个Query对象以查询具有与指定字符串值不相似的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用unlike时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| value | string | 是 | 表示指定的字符串值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.unlike("field", "value");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### and

and(): Query

构造一个带有与条件的查询对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回查询对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo("field", "value1");
      query.and();
      query.notEqualTo("field", "value2");
      console.info("query is " + query.getSqlLike());
    }
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

#### or

or(): Query

构造一个带有或条件的Query对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回查询对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo("field", "value1");
      query.or();
      query.notEqualTo("field", "value2");
      console.info("query is " + query.getSqlLike());
    }
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

#### orderByAsc

orderByAsc(field: string): Query

构造一个Query对象，将查询结果按升序排序。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用orderByAsc时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo("field", "value");
      query.orderByAsc("field");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### orderByDesc

orderByDesc(field: string): Query

构造一个Query对象，将查询结果按降序排序。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用orderByDesc时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.notEqualTo("field", "value");
      query.orderByDesc("field");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### limit

limit(total: number, offset: number): Query

构造一个Query对象来指定结果的数量和开始位置。该接口必须要在Query对象查询和升降序等操作之后调用，调用limit接口后，不可再对Query对象进行查询和升降序等操作。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| total | number | 是 | 表示最大数据记录数，取值应为非负整数。 当total为负数时，表示查询整个结果集。 |
| offset | number | 是 | 指定查询结果的起始位置，取值应为非负整数。 当offset为负数时，表示查询整个结果集。 当offset超出结果集最后位置时，查询结果为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let total = 10;
let offset = 1;
try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.notEqualTo("field", "value");
    query.limit(total, offset);
    console.info(`query is ${query.getSqlLike()}`);
  }
  query = null;
} catch (e) {
  let error = e as BusinessError;
  console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### isNotNull

isNotNull(field: string): Query

构造一个Query对象以查询具有值不为null的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core


使用isNotNull时需要结合[Schema](#ZH-CN_TOPIC_0000002553360553__schema)使用。

使用Schema创建数据库请参见[通过键值型数据库实现数据持久化](../../guides/通过键值型数据库实现数据持久化.md#开发步骤)中使用getKVStore()方法创建并获取键值数据库示例。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| field | string | 是 | 表示指定字段，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let query: distributedKVStore.Query | null = new distributedKVStore.Query();
  if (query != null) {
    query.isNotNull("field");
    console.info(`query is ${query.getSqlLike()}`);
  }
  query = null;
} catch (e) {
  let error = e as BusinessError;
  console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### beginGroup

beginGroup(): Query

创建一个带有左括号的查询条件组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.beginGroup();
      query.isNotNull("field");
      query.endGroup();
      console.info("query is " + query.getSqlLike());
    }
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

#### endGroup

endGroup(): Query

创建一个带有右括号的查询条件组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.beginGroup();
      query.isNotNull("field");
      query.endGroup();
      console.info("query is " + query.getSqlLike());
    }
    query = null;
} catch (e) {
    console.error("duplicated calls should be ok :" + e);
}
```

#### prefixKey

prefixKey(prefix: string): Query

创建具有指定键前缀的查询条件。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prefix | string | 是 | 表示指定的键前缀，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.prefixKey("$.name");
      query.prefixKey("0");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### setSuggestIndex

setSuggestIndex(index: string): Query

设置一个指定的索引，将优先用于查询。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | string | 是 | 指示要设置的索引，不能包含'^'。包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.setSuggestIndex("$.name");
      query.setSuggestIndex("0");
      console.info(`query is ${query.getSqlLike()}`);
    }
    query = null;
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### deviceId

deviceId(deviceId:string):Query

添加设备ID作为Key的前缀。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 指示查询的设备ID，不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Query | 返回Query对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      query.deviceId("deviceId");
      console.info(`query is ${query.getSqlLike()}`);
    }
} catch (e) {
    let error = e as BusinessError;
    console.error(`duplicated calls should be ok.code is ${error.code},message is ${error.message}`);
}
```

#### getSqlLike

getSqlLike():string

获取Query对象的查询语句。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回一个字段列中包含对应子串的结果。 |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let query: distributedKVStore.Query | null = new distributedKVStore.Query();
    if (query != null) {
      let sql1 = query.getSqlLike();
      console.info(`GetSqlLike sql= ${sql1}`);
    }
} catch (e) {
    console.error("duplicated calls should be ok : " + e);
}
```

#### SingleKVStore

SingleKVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据端端同步完成的方法。

在调用SingleKVStore的方法前，需要先通过[getKVStore](#ZH-CN_TOPIC_0000002553360553__getkvstore)构建一个SingleKVStore实例。

#### put

put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void

添加指定类型键值对到数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要添加数据的Key，不能为空且长度不大于MAX_KEY_LENGTH。 |
| value | Uint8Array | string | number | boolean | 是 | 要添加数据的value，支持Uint8Array、number 、 string 、boolean，Uint8Array、string 的长度不大于MAX_VALUE_LENGTH。 |
| callback | AsyncCallback<void> | 是 | 回调函数。数据添加成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码]([关系型数据库错误码](../../errors/关系型数据库错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info("Succeeded in putting");
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### put

put(key: string, value: Uint8Array | string | number | boolean): Promise<void>

添加指定类型键值对到数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要添加数据的Key，不能为空且长度不大于MAX_KEY_LENGTH。 |
| value | Uint8Array | string | number | boolean | 是 | 要添加数据的value，支持Uint8Array、number 、 string 、boolean，Uint8Array、string 的长度不大于MAX_VALUE_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
    console.info(`Succeeded in putting data`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### putBatch

putBatch(entries: Entry[], callback: AsyncCallback<void>): void

批量插入键值对到SingleKVStore数据库中，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | Entry[] | 是 | 表示要批量插入的键值对。一个entries对象中允许的最大数据量为512M。 |
| callback | AsyncCallback<void> | 是 | 回调函数。数据批量插入成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch_test_string_key', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
        if (err != undefined) {
          console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
        }
        console.info('Succeeded in getting Entries');
        console.info(`entries.length: ${entries.length}`);
        console.info(`entries[0]: ${entries[0]}`);
      });
    } else {
      console.error('KvStore is null'); //后续示例代码与此处保持一致
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
}
```

#### putBatch

putBatch(entries: Entry[]): Promise<void>

批量插入键值对到SingleKVStore数据库中，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| entries | Entry[] | 是 | 表示要批量插入的键值对。一个entries对象中允许的最大数据量为512M。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch_test_string_key').then((entries: distributedKVStore.Entry[]) => {
        console.info('Succeeded in getting Entries');
        console.info(`PutBatch ${entries}`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
}
```

#### delete

delete(key: string, callback: AsyncCallback<void>): void

从数据库中删除指定键值的数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除数据的Key，不能为空且长度不大于MAX_KEY_LENGTH。 |
| callback | AsyncCallback<void> | 是 | 回调函数。删除指定的数据成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting');
    if (kvStore != null) {
      kvStore.delete(KEY_TEST_STRING_ELEMENT, (err: BusinessError) => {
        if (err != undefined) {
          console.error(`Failed to delete.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in deleting');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### delete

delete(key: string): Promise<void>

从数据库中删除指定键值的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要删除数据的Key，不能为空且长度不大于MAX_KEY_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
    console.info(`Succeeded in putting data`);
    if (kvStore != null) {
      kvStore.delete(KEY_TEST_STRING_ELEMENT).then(() => {
        console.info('Succeeded in deleting');
      }).catch((err: BusinessError) => {
        console.error(`Failed to delete.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### deleteBatch

deleteBatch(keys: string[], callback: AsyncCallback<void>): void

批量删除SingleKVStore数据库中的键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | string[] | 是 | 表示要批量删除的键值对，不能为空。 |
| callback | AsyncCallback<void> | 是 | 回调函数。批量删除指定的数据成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  let keys: string[] = [];
  for (let i = 0; i < 5; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
    keys.push(key + i);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.deleteBatch(keys, async (err: BusinessError) => {
        if (err != undefined) {
          console.error(`Failed to delete Batch.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in deleting Batch');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### deleteBatch

deleteBatch(keys: string[]): Promise<void>

批量删除SingleKVStore数据库中的键值对，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keys | string[] | 是 | 表示要批量删除的键值对，不能为空。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  let keys: string[] = [];
  for (let i = 0; i < 5; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
    keys.push(key + i);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.deleteBatch(keys).then(() => {
        console.info('Succeeded in deleting Batch');
      }).catch((err: BusinessError) => {
        console.error(`Failed to delete Batch.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### removeDeviceData

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

删除指定设备的数据，使用callback异步回调。


其中deviceId为[DeviceBasicInfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__devicebasicinfo)中的networkId，通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示要删除设备的networkId。 |
| callback | AsyncCallback<void> | 是 | 回调函数。删除指定设备的数据成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async (err: BusinessError) => {
    console.info('Succeeded in putting data');
    const deviceid = 'no_exist_device_id';
    if (kvStore != null) {
      kvStore.removeDeviceData(deviceid, async (err: BusinessError) => {
        if (err == undefined) {
          console.info('succeeded in removing device data');
        } else {
          console.error(`Failed to remove device data.code is ${err.code},message is ${err.message} `);
          if (kvStore != null) {
            kvStore.get(KEY_TEST_STRING_ELEMENT, async (err: BusinessError, data: boolean | string | number | Uint8Array) => {
              console.info('Succeeded in getting data');
            });
          }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`)
}
```

#### removeDeviceData

removeDeviceData(deviceId: string): Promise<void>

删除指定设备的数据，使用Promise异步回调。


其中deviceId为[DeviceBasicInfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__devicebasicinfo)中的networkId，通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示要删除设备的networkId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
    console.info('Succeeded in putting data');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put data.code is ${err.code},message is ${err.message} `);
  });
  const deviceid = 'no_exist_device_id';
  kvStore.removeDeviceData(deviceid).then(() => {
    console.info('succeeded in removing device data');
  }).catch((err: BusinessError) => {
    console.error(`Failed to remove device data.code is ${err.code},message is ${err.message} `);
  });
  kvStore.get(KEY_TEST_STRING_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
    console.info('Succeeded in getting data');
  }).catch((err: BusinessError) => {
    console.error(`Failed to get data.code is ${err.code},message is ${err.message} `);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`)
}
```

#### get

get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void

获取指定键的值，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的Key，不能为空且长度不大于MAX_KEY_LENGTH。 |
| callback | AsyncCallback<boolean | string | number | Uint8Array> | 是 | 回调函数。返回获取查询的值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info("Succeeded in putting");
    if (kvStore != null) {
      kvStore.get(KEY_TEST_STRING_ELEMENT, (err: BusinessError, data: boolean | string | number | Uint8Array) => {
        if (err != undefined) {
          console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info(`Succeeded in getting data.data=${data}`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
}
```

#### get

get(key: string): Promise<boolean | string | number | Uint8Array>

获取指定键的值，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的Key，不能为空且长度不大于MAX_KEY_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean | string | number | Uint8Array> | Promise对象。返回获取查询的值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
    console.info(`Succeeded in putting data`);
    if (kvStore != null) {
      kvStore.get(KEY_TEST_STRING_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
        console.info(`Succeeded in getting data.data=${data}`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
}
```

#### getEntries

getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取匹配指定键前缀的所有键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<Entry[]> | 是 | 回调函数。返回匹配指定前缀的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch_test_string_key', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
        if (err != undefined) {
          console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting Entries');
        console.info(`entries.length: ${entries.length}`);
        console.info(`entries[0]: ${entries[0]}`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
}
```

#### getEntries

getEntries(keyPrefix: string): Promise<Entry[]>

获取匹配指定键前缀的所有键值对，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Entry[]> | Promise对象。返回匹配指定前缀的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch_test_string_key').then((entries: distributedKVStore.Entry[]) => {
        console.info('Succeeded in getting Entries');
        console.info(`PutBatch ${entries}`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
}
```

#### getEntries

getEntries(query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<Entry[]> | 是 | 回调函数。返回与指定Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array([21, 31]);
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_bool_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE_ARRAY,
        value: arr
    }
    entries.push(entry);
  }
  console.info(`entries: {entries}`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    console.info('Succeeded in putting Batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getEntries(query, (err: BusinessError, entries: distributedKVStore.Entry[]) => {
        if (err != undefined) {
          console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting Entries');
        console.info(`entries.length: ${entries.length}`);
        console.info(`entries[0]: ${entries[0]}`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get Entries.code is ${error.code},message is ${error.message}`);
}
```

#### getEntries

getEntries(query: Query): Promise<Entry[]>

获取与指定Query对象匹配的键值对列表，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Entry[]> | Promise对象。返回与指定Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array([21, 31]);
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_bool_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE_ARRAY,
        value: arr
    }
    entries.push(entry);
  }
  console.info(`entries: {entries}`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getEntries(query).then((entries: distributedKVStore.Entry[]) => {
        console.info('Succeeded in getting Entries');
      }).catch((err: BusinessError) => {
        console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`)
  });
  console.info('Succeeded in getting Entries');
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get Entries.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void

从SingleKVStore数据库中获取具有指定前缀的结果集，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<KVStoreResultSet> | 是 | 回调函数。返回具有指定前缀的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    if (kvStore != null) {
      kvStore.getResultSet('batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting result set');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err :BusinessError) => {
            if (err != undefined) {
              console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
              return;
            }
            console.info('Succeeded in closing result set');
          });
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(keyPrefix: string): Promise<KVStoreResultSet>

从SingleKVStore数据库中获取具有指定前缀的结果集，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KVStoreResultSet> | Promise对象。返回具有指定前缀的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing result set');
      }).catch((err: BusinessError) => {
        console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(query: Query, callback: AsyncCallback<KVStoreResultSet>): void

获取与指定Query对象匹配的KVStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |
| callback | AsyncCallback<KVStoreResultSet> | 是 | 回调函数，获取与指定Query对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getResultSet(query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting result set');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(query: Query): Promise<KVStoreResultSet>

获取与指定Query对象匹配的KVStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KVStoreResultSet> | Promise对象。获取与指定Query对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch_test");
  kvStore.getResultSet(query).then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### closeResultSet

closeResultSet(resultSet: KVStoreResultSet, callback: AsyncCallback<void>): void

关闭由[SingleKvStore.getResultSet](#ZH-CN_TOPIC_0000002553360553__getresultset-1)返回的KVStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resultSet | KVStoreResultSet | 是 | 表示要关闭的KVStoreResultSet对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。关闭KVStoreResultSet对象成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let resultSet: distributedKVStore.KVStoreResultSet;
try {
  kvStore.getResultSet('batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
    if (err != undefined) {
      console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in getting result set');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet, (err: BusinessError) => {
        if (err != undefined) {
          console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in closing result set');
      })
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### closeResultSet

closeResultSet(resultSet: KVStoreResultSet): Promise<void>

关闭由[SingleKvStore.getResultSet](#ZH-CN_TOPIC_0000002553360553__getresultset-1)返回的KVStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| resultSet | KVStoreResultSet | 是 | 表示要关闭的KVStoreResultSet对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let resultSet: distributedKVStore.KVStoreResultSet;
try {
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing result set');
      }).catch((err: BusinessError) => {
        console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
  });

} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSize

getResultSize(query: Query, callback: AsyncCallback<number>): void

获取与指定Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回与指定Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, (err: BusinessError) => {
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getResultSize(query, (err: BusinessError, resultSize: number) => {
        if (err != undefined) {
          console.error(`Failed to get result size.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting result set size');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSize

getResultSize(query: Query): Promise<number>

获取与指定Query对象匹配的结果数，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。获取与指定Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch_test");
  kvStore.getResultSize(query).then((resultSize: number) => {
    console.info('Succeeded in getting result set size');
  }).catch((err: BusinessError) => {
    console.error(`Failed to get result size.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### backup

backup(file:string, callback: AsyncCallback<void>):void

以指定名称备份数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 备份数据库的指定名称，不能为空且长度不大于MAX_KEY_LENGTH。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当以指定名称备份数据库成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let backupFile = "BK001";
try {
  kvStore.backup(backupFile, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to backup.code is ${err.code},message is ${err.message} `);
    } else {
      console.info(`Succeeded in backupping data`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### backup

backup(file:string): Promise<void>

以指定名称备份数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 备份数据库的指定名称，不能为空且长度不大于MAX_KEY_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let backupFile = "BK001";
try {
  kvStore.backup(backupFile).then(() => {
    console.info(`Succeeded in backupping data`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to backup.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### restore

restore(file:string, callback: AsyncCallback<void>):void

从指定的数据库文件恢复数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 指定的数据库文件名称，不能为空且长度不大于MAX_KEY_LENGTH。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当从指定的数据库文件恢复数据库成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let backupFile = "BK001";
try {
  kvStore.restore(backupFile, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to restore.code is ${err.code},message is ${err.message}`);
    } else {
      console.info(`Succeeded in restoring data`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### restore

restore(file:string): Promise<void>

从指定的数据库文件恢复数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| file | string | 是 | 指定的数据库文件名称，不能为空且长度不大于MAX_KEY_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let backupFile = "BK001";
try {
  kvStore.restore(backupFile).then(() => {
    console.info(`Succeeded in restoring data`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to restore.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### deleteBackup

deleteBackup(files:Array<string>, callback: AsyncCallback<Array<[string, number]>>):void

根据指定名称删除备份文件，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 删除备份文件所指定的名称，不能为空且长度不大于MAX_KEY_LENGTH。 |
| callback | AsyncCallback<Array<[string, number]>> | 是 | 回调函数，返回删除备份的文件名及其处理结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let files = ["BK001", "BK002"];
try {
  kvStore.deleteBackup(files, (err: BusinessError, data: [string, number][]) => {
    if (err) {
      console.error(`Failed to delete Backup.code is ${err.code},message is ${err.message}`);
    } else {
      console.info(`Succeed in deleting Backup.data=${data}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### deleteBackup

deleteBackup(files:Array<string>): Promise<Array<[string, number]>>

根据指定名称删除备份文件，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 删除备份文件所指定的名称，不能为空且长度不大于MAX_KEY_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[string, number]>> | Promise对象，返回删除备份的文件名及其处理结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Parameter verification failed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let files = ["BK001", "BK002"];
try {
  kvStore.deleteBackup(files).then((data: [string, number][]) => {
    console.info(`Succeed in deleting Backup.data=${data}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to delete Backup.code is ${err.code},message is ${err.message}`);
  })
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### startTransaction

startTransaction(callback: AsyncCallback<void>): void

启动SingleKVStore数据库中的事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。启动SingleKVStore数据库中的事务成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

function putBatchString(len: number, prefix: string) {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < len; i++) {
    let entry: distributedKVStore.Entry = {
      key: prefix + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  return entries;
} //自定义函数，放置在作用域最外侧，防止语法检查报错

try {
  let count = 0;
  kvStore.on('dataChange', 0, (data: distributedKVStore.ChangeNotification) => {
    console.info(`startTransaction 0 ${data}`);
    count++;
  });
  kvStore.startTransaction(async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to start Transaction.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in starting Transaction');
    let entries = putBatchString(10, 'batch_test_string_key');
    console.info(`entries: ${entries}`);
    if (kvStore != null) {
      kvStore.putBatch(entries, async (err: BusinessError) => {
        if (err != undefined) {
          console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in putting Batch');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to start Transaction.code is ${error.code},message is ${error.message}`);
}
```

#### startTransaction

startTransaction(): Promise<void>

启动SingleKVStore数据库中的事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15100005 | Database or result set already closed. |

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let count = 0;
  kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE_TYPE_ALL, (data: distributedKVStore.ChangeNotification) => {
    console.info(`startTransaction 0 ${data}`);
    count++;
  });
  kvStore.startTransaction().then(async () => {
    console.info('Succeeded in starting Transaction');
  }).catch((err: BusinessError) => {
    console.error(`Failed to start Transaction.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to start Transaction.code is ${error.code},message is ${error.message}`);
}
```

#### commit

commit(callback: AsyncCallback<void>): void

提交SingleKVStore数据库中的事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。提交SingleKVStore数据库中的事务成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.commit((err: BusinessError) => {
    if (err == undefined) {
      console.info('Succeeded in committing');
    } else {
      console.error(`Failed to commit.code is ${err.code},message is ${err.message}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### commit

commit(): Promise<void>

提交SingleKVStore数据库中的事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.commit().then(async () => {
    console.info('Succeeded in committing');
  }).catch((err: BusinessError) => {
    console.error(`Failed to commit.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### rollback

rollback(callback: AsyncCallback<void>): void

在SingleKVStore数据库中回滚事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。SingleKVStore数据库中回滚事务成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.rollback((err: BusinessError) => {
    if (err == undefined) {
      console.info('Succeeded in rolling back');
    } else {
      console.error(`Failed to rollback.code is ${err.code},message is ${err.message}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### rollback

rollback(): Promise<void>

在SingleKVStore数据库中回滚事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.rollback().then(async () => {
    console.info('Succeeded in rolling back');
  }).catch((err: BusinessError) => {
    console.error(`Failed to rollback.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### enableSync

enableSync(enabled: boolean, callback: AsyncCallback<void>): void

设定是否开启端端同步，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设定是否开启端端同步，true表示开启端端同步，false表示不启用端端同步。 |
| callback | AsyncCallback<void> | 是 | 回调函数。设定成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.enableSync(true, (err: BusinessError) => {
    if (err == undefined) {
      console.info('Succeeded in enabling sync');
    } else {
      console.error(`Failed to enable sync.code is ${err.code},message is ${err.message}`);
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### enableSync

enableSync(enabled: boolean): Promise<void>

设定是否开启端端同步，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 设定是否开启端端同步，true表示开启端端同步，false表示不启用端端同步。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.enableSync(true).then(() => {
    console.info('Succeeded in enabling sync');
  }).catch((err: BusinessError) => {
    console.error(`Failed to enable sync.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### setSyncRange

setSyncRange(localLabels: string[], remoteSupportLabels: string[], callback: AsyncCallback<void>): void

设置同步范围标签，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localLabels | string[] | 是 | 表示本地设备的同步标签。 |
| remoteSupportLabels | string[] | 是 | 表示要同步数据的设备的同步标签。 |
| callback | AsyncCallback<void> | 是 | 回调函数。设置成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const localLabels = ['A', 'B'];
  const remoteSupportLabels = ['C', 'D'];
  kvStore.setSyncRange(localLabels, remoteSupportLabels, (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to set syncRange.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in setting syncRange');
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### setSyncRange

setSyncRange(localLabels: string[], remoteSupportLabels: string[]): Promise<void>

设置同步范围标签，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localLabels | string[] | 是 | 表示本地设备的同步标签。 |
| remoteSupportLabels | string[] | 是 | 表示要同步数据的设备的同步标签。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const localLabels = ['A', 'B'];
  const remoteSupportLabels = ['C', 'D'];
  kvStore.setSyncRange(localLabels, remoteSupportLabels).then(() => {
    console.info('Succeeded in setting syncRange');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set syncRange.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### setSyncParam

setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void

设置数据库端端同步允许的默认延时，使用callback异步回调。


设置默认延时后，调用[sync](#ZH-CN_TOPIC_0000002553360553__sync)接口不会立即触发端端同步，而是等待指定的延时时间后再执行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defaultAllowedDelayMs | number | 是 | 表示一个延时时间，单位为毫秒（ms），取值范围为0或[100, 86400000]。 |
| callback | AsyncCallback<void> | 是 | 回调函数。设置成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const defaultAllowedDelayMs = 500;
  kvStore.setSyncParam(defaultAllowedDelayMs, (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to set syncParam.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in setting syncParam');
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### setSyncParam

setSyncParam(defaultAllowedDelayMs: number): Promise<void>

设置数据库端端同步允许的默认延时，使用Promise异步回调。


设置默认延时后，调用[sync](#ZH-CN_TOPIC_0000002553360553__sync)接口不会立即触发端端同步，而是等待指定的延时时间后再执行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| defaultAllowedDelayMs | number | 是 | 表示一个延时时间，单位为毫秒（ms），取值范围为0或[100, 86400000]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const defaultAllowedDelayMs = 500;
  kvStore.setSyncParam(defaultAllowedDelayMs).then(() => {
    console.info('Succeeded in setting syncParam');
  }).catch((err: BusinessError) => {
    console.error(`Failed to set syncParam.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### sync

sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void

在手动同步方式下，触发数据库端端同步。关于键值型数据库的端端同步方式说明，请见[键值型数据库跨设备数据同步](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-sync-of-kv-store)。


其中deviceIds为[DeviceBasicInfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__devicebasicinfo)中的networkId, 通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

**需要权限**： ohos.permission.DISTRIBUTED_DATASYNC。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceIds | string[] | 是 | 同一组网环境下，需要同步的设备的networkId列表。 |
| mode | SyncMode | 是 | 同步模式。 |
| delayMs | number | 否 | 可选参数，允许延时时间，单位：ms（毫秒），默认为0。设置delayMs后，调用sync接口时延时时间为delayMs。未设置时以setSyncParam设置的时长为准。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let devManager: distributedDeviceManager.DeviceManager;
const KEY_TEST_SYNC_ELEMENT = 'key_test_sync';
const VALUE_TEST_SYNC_ELEMENT = 'value-string-001';
// create deviceManager
export default class EntryAbility extends UIAbility {
  onCreate() {
    let context = this.context;
    try {
      devManager = distributedDeviceManager.createDeviceManager(context.applicationInfo.name);
      let deviceIds: string[] = [];
      if (devManager != null) {
        let devices = devManager.getAvailableDeviceListSync();
        for (let i = 0; i < devices.length; i++) {
          deviceIds[i] = devices[i].networkId as string;
        }
      try {
        if (kvStore != null) {
          kvStore.on('syncComplete', (data: [string, number][]) => {
            console.info('Sync dataChange');
          });
          if (kvStore != null) {
            kvStore.put(KEY_TEST_SYNC_ELEMENT + 'testSync101', VALUE_TEST_SYNC_ELEMENT, (err: BusinessError) => {
              if (err != undefined) {
                console.error(`Failed to sync.code is ${err.code},message is ${err.message}`);
                return;
              }
              console.info('Succeeded in putting data');
              const mode = distributedKVStore.SyncMode.PULL_ONLY;
              if (kvStore != null) {
                kvStore.sync(deviceIds, mode, 1000);
              }
            });
          }
      } catch (e) {
        let error = e as BusinessError;
        console.error(`Failed to sync.code is ${error.code},message is ${error.message}`);
      }

    } catch (err) {
      let error = err as BusinessError;
      console.error("createDeviceManager errCode:" + error.code + ",errMessage:" + error.message);
    }
```

#### sync

sync(deviceIds: string[], query: Query, mode: SyncMode, delayMs?: number): void

在手动同步方式下，触发数据库端端同步，此方法为同步方法。关于键值型数据库的端端同步方式说明，请见[键值型数据库跨设备数据同步](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-sync-of-kv-store)。


其中deviceIds为[DeviceBasicInfo](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__devicebasicinfo)中的networkId, 通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

**需要权限**： ohos.permission.DISTRIBUTED_DATASYNC。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceIds | string[] | 是 | 同一组网环境下，需要同步的设备的networkId列表。 |
| query | Query | 是 | 表示数据库的查询谓词条件。 |
| mode | SyncMode | 是 | 同步模式。 |
| delayMs | number | 否 | 可选参数，允许延时时间，单位：ms（毫秒），默认为0。设置delayMs后，调用sync接口时延时时间为delayMs。未设置时以setSyncParam设置的时长为准。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_SYNC_ELEMENT = 'key_test_sync';
const VALUE_TEST_SYNC_ELEMENT = 'value-string-001';
// create deviceManager
export default class EntryAbility extends UIAbility {
  onCreate() {
    let context = this.context;
    try {
      let devManager = distributedDeviceManager.createDeviceManager(context.applicationInfo.name);
      let deviceIds: string[] = [];
      if (devManager != null) {
        let devices = devManager.getAvailableDeviceListSync();
        for (let i = 0; i < devices.length; i++) {
          deviceIds[i] = devices[i].networkId as string;
      }
      try {
        if (kvStore != null) {
          kvStore.on('syncComplete', (data: [string, number][]) => {
            console.info('Sync dataChange');
          });
          if (kvStore != null) {
            kvStore.put(KEY_TEST_SYNC_ELEMENT + 'testSync101', VALUE_TEST_SYNC_ELEMENT, (err: BusinessError) => {
              if (err != undefined) {
                console.error(`Failed to sync.code is ${err.code},message is ${err.message}`);
                return;
              }
              console.info('Succeeded in putting data');
              const mode = distributedKVStore.SyncMode.PULL_ONLY;
              const query = new distributedKVStore.Query();
              query.prefixKey("batch_test");
              query.deviceId(devManager.getLocalDeviceNetworkId());
              if (kvStore != null) {
                kvStore.sync(deviceIds, query, mode, 1000);
              }
            });
          }
      } catch (e) {
        let error = e as BusinessError;
        console.error(`Failed to sync.code is ${error.code},message is ${error.message}`);
      }

    } catch (err) {
      let error = err as BusinessError;
      console.error("createDeviceManager errCode:" + error.code + ",errMessage:" + error.message);
    }
```

#### on('dataChange')

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

订阅指定类型的数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| type | SubscribeType | 是 | 表示订阅的类型。 |
| listener | Callback<ChangeNotification> | 是 | 回调函数。成功返回数据变更时通知的对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE_TYPE_LOCAL, (data: distributedKVStore.ChangeNotification) => {
    console.info(`dataChange callback call data: ${data}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### on('syncComplete')

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅端端同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 是 | 回调函数。用于向调用方发送同步结果的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_FLOAT_ELEMENT = 'key_test_float';
const VALUE_TEST_FLOAT_ELEMENT = 321.12;
try {
  kvStore.on('syncComplete', (data: [string, number][]) => {
    console.info(`syncComplete ${data}`);
  });
  kvStore.put(KEY_TEST_FLOAT_ELEMENT, VALUE_TEST_FLOAT_ELEMENT).then(() => {
    console.info('succeeded in putting');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to subscribe syncComplete.code is ${error.code},message is ${error.message}`);
}
```

#### off('dataChange')

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'dataChange'，表示数据变更事件。 |
| listener | Callback<ChangeNotification> | 否 | 取消订阅的函数。如不设置callback，则取消所有已订阅的函数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class KvstoreModel {
  call(data: distributedKVStore.ChangeNotification) {
    console.info(`dataChange : ${data}`);
  }

  subscribeDataChange() {
    try {
      if (kvStore != null) {
        kvStore.on('dataChange', distributedKVStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
      }
    } catch (err) {
      let error = err as BusinessError;
      console.error(`Failed to subscribeDataChange.code is ${error.code},message is ${error.message}`);
    }

  unsubscribeDataChange() {
    try {
      if (kvStore != null) {
        kvStore.off('dataChange', this.call);
      }
    } catch (err) {
      let error = err as BusinessError;
      console.error(`Failed to unsubscribeDataChange.code is ${error.code},message is ${error.message}`);
    }
```

#### off('syncComplete')

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅端端同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。 |
| syncCallback | Callback<Array<[string, number]>> | 否 | 取消订阅的同步完成回调函数。如果该参数不填，则取消所有已订阅的同步完成回调函数。如果存在同一个数据库的多个ArkTS实例(通过getKVStore接口获取)分别注册监听了同步完成事件，则对于任意一个ArkTS实例取消其所有已订阅的同步完成回调函数时，其余ArkTS实例已订阅的所有同步完成回调函数也会被取消。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

class KvstoreModel {
  call(data: [string, number][]) {
    console.info(`syncComplete : ${data}`);
  }

  subscribeDataChange() {
    try {
      if (kvStore != null) {
        kvStore.on('syncComplete', this.call);
      }
    } catch (err) {
      let error = err as BusinessError;
      console.error(`Failed to subscribeDataChange.code is ${error.code},message is ${error.message}`);
    }

  unsubscribeDataChange() {
    try {
      if (kvStore != null) {
        kvStore.off('syncComplete', this.call);
      }
    } catch (err) {
      let error = err as BusinessError;
      console.error(`Failed to unsubscribeDataChange.code is ${error.code},message is ${error.message}`);
    }
```

#### getSecurityLevel

getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void

获取数据库的安全级别，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<SecurityLevel> | 是 | 回调函数。返回数据库的安全级别。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.getSecurityLevel((err: BusinessError, data: distributedKVStore.SecurityLevel) => {
    if (err != undefined) {
      console.error(`Failed to get SecurityLevel.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in getting securityLevel');
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getSecurityLevel

getSecurityLevel(): Promise<SecurityLevel>

获取数据库的安全级别，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<SecurityLevel> | Promise对象。返回数据库的安全级别。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  kvStore.getSecurityLevel().then((data: distributedKVStore.SecurityLevel) => {
    console.info('Succeeded in getting securityLevel');
  }).catch((err: BusinessError) => {
    console.error(`Failed to get SecurityLevel.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### DeviceKVStore

设备协同数据库，继承自SingleKVStore，提供查询数据和端端同步数据的方法，可以使用SingleKVStore的方法例如：put、putBatch等。

设备协同数据库，以设备维度对数据进行区分，每台设备仅能写入和修改本设备的数据，其它设备的数据对其是只读的，无法修改其它设备的数据。

比如，可以使用设备协同数据库实现设备间的图片分享，可以查看其他设备的图片，但无法修改和删除其他设备的图片。

在调用DeviceKVStore的方法前，需要先通过[getKVStore](#ZH-CN_TOPIC_0000002553360553__getkvstore)构建一个DeviceKVStore实例。

#### get

get(key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void

获取本设备指定键的值，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的Key，不能为空且长度不大于MAX_KEY_LENGTH。 |
| callback | AsyncCallback<boolean | string | number | Uint8Array> | 是 | 回调函数。返回获取查询的值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info("Succeeded in putting");
    if (kvStore != null) {
      kvStore.get(KEY_TEST_STRING_ELEMENT, (err: BusinessError, data: boolean | string | number | Uint8Array) => {
        if (err != undefined) {
          console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info(`Succeeded in getting data.data=${data}`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
}
```

#### get

get(key: string): Promise<boolean | string | number | Uint8Array>

获取本设备指定键的值，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 要查询数据的Key，不能为空且长度不大于MAX_KEY_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean | string | number | Uint8Array> | Promise对象。返回获取查询的值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(() => {
    console.info(`Succeeded in putting data`);
    if (kvStore != null) {
      kvStore.get(KEY_TEST_STRING_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
        console.info(`Succeeded in getting data.data=${data}`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
}
```

#### get

get(deviceId: string, key: string, callback: AsyncCallback<boolean | string | number | Uint8Array>): void

获取与指定设备ID和Key匹配的string值，使用callback异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| key | string | 是 | 表示要查询Key值的键, 不能为空且长度不大于MAX_KEY_LENGTH。 |
| callback | AsyncCallback<boolean|string|number|Uint8Array> | 是 | 回调函数，返回匹配给定条件的字符串值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting');
    if (kvStore != null) {
      kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT, (err: BusinessError, data: boolean | string | number | Uint8Array) => {
        if (err != undefined) {
          console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting');
      });
    }
  })
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
}
```

#### get

get(deviceId: string, key: string): Promise<boolean | string | number | Uint8Array>

获取与指定设备ID和Key匹配的string值，使用Promise异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| key | string | 是 | 表示要查询Key值的键, 不能为空且长度不大于MAX_KEY_LENGTH。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean|string|number|Uint8Array> | Promise对象。返回匹配给定条件的字符串值。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types; 3. Parameter verification failed. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
try {
  kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(async () => {
    console.info('Succeeded in putting');
    if (kvStore != null) {
      kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT).then((data: boolean | string | number | Uint8Array) => {
        console.info('Succeeded in getting');
      }).catch((err: BusinessError) => {
        console.error(`Failed to get.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((error: BusinessError) => {
    console.error(`Failed to put.code is ${error.code},message is ${error.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get.code is ${error.code},message is ${error.message}`);
}
```

#### getEntries

getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取匹配本设备指定键前缀的所有键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<Entry[]> | 是 | 回调函数。返回匹配指定前缀的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch_test_string_key', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
        if (err != undefined) {
          console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting Entries');
        console.info(`entries.length: ${entries.length}`);
        console.info(`entries[0]: ${entries[0]}`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
}
```

#### getEntries

getEntries(keyPrefix: string): Promise<Entry[]>

获取匹配本设备指定键前缀的所有键值对，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Entry[]> | Promise对象。返回匹配指定前缀的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    if (kvStore != null) {
      kvStore.getEntries('batch_test_string_key').then((entries: distributedKVStore.Entry[]) => {
        console.info('Succeeded in getting Entries');
        console.info(`PutBatch ${entries}`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put Batch.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message} `);
}
```

#### getEntries

getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取与指定设备ID和Key前缀匹配的所有键值对，使用callback异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<Entry[]> | 是 | 回调函数，返回满足给定条件的所有键值对的列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  console.info(`entries : ${entries}`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    if (kvStore != null) {
      kvStore.getEntries('localDeviceId', 'batch_test_string_key', (err: BusinessError, entries: distributedKVStore.Entry[]) => {
        if (err != undefined) {
          console.error(`Failed to get entries.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting entries');
        console.info(`entries.length: ${entries.length}`);
        console.info(`entries[0]: ${entries[0]}`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to put batch.code is ${error.code},message is ${error.message}`);
}
```

#### getEntries

getEntries(deviceId: string, keyPrefix: string): Promise<Entry[]>

获取与指定设备ID和Key前缀匹配的所有键值对，使用Promise异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Entry[]> | Promise对象。返回匹配给定条件的所有键值对的列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
    if (kvStore != null) {
      kvStore.getEntries('localDeviceId', 'batch_test_string_key').then((entries: distributedKVStore.Entry[]) => {
        console.info('Succeeded in getting entries');
        console.info(`entries.length: ${entries.length}`);
        console.info(`entries[0]: ${entries[0]}`);
        console.info(`entries[0].value: ${entries[0].value}`);
        console.info(`entries[0].value.value: ${entries[0].value.value}`);
      }).catch((err: BusinessError) => {
        console.error(`Failed to get entries.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to put batch.code is ${error.code},message is ${error.message}`);
}
```

#### getEntries

getEntries(query: Query, callback: AsyncCallback<Entry[]>): void

获取本设备与指定Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示要匹配的键前缀。 |
| callback | AsyncCallback<Entry[]> | 是 | 回调函数。返回本设备与指定Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array([21, 31]);
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_bool_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE_ARRAY,
        value: arr
    }
    entries.push(entry);
  }
  console.info(`entries: {entries}`);
  kvStore.putBatch(entries, (err: BusinessError) => {
    console.info('Succeeded in putting Batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getEntries(query, (err: BusinessError, entries: distributedKVStore.Entry[]) => {
        if (err != undefined) {
          console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting Entries');
        console.info(`entries.length: ${entries.length}`);
        console.info(`entries[0]: ${entries[0]}`);
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get Entries.code is ${error.code},message is ${error.message}`);
}
```

#### getEntries

getEntries(query: Query): Promise<Entry[]>

获取本设备与指定Query对象匹配的键值对列表，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Entry[]> | Promise对象。返回本设备与指定Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array([21, 31]);
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_bool_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE_ARRAY,
        value: arr
    }
    entries.push(entry);
  }
  console.info(`entries: {entries}`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting Batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getEntries(query).then((entries: distributedKVStore.Entry[]) => {
        console.info('Succeeded in getting Entries');
      }).catch((err: BusinessError) => {
        console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get Entries.code is ${err.code},message is ${err.message}`)
  });
  console.info('Succeeded in getting Entries');
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get Entries.code is ${error.code},message is ${error.message}`);
}
```

#### getEntries

getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定设备ID和Query对象匹配的键值对列表，使用callback异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 键值对所属的设备ID。 |
| query | Query | 是 | 表示查询对象。 |
| callback | AsyncCallback<Entry[]> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array([21, 31]);
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_bool_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE_ARRAY,
        value: arr
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    let query = new distributedKVStore.Query();
    query.deviceId('localDeviceId');
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getEntries('localDeviceId', query, (err: BusinessError, entries: distributedKVStore.Entry[]) => {
        if (err != undefined) {
          console.error(`Failed to get entries.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting entries');
        console.info(`entries.length: ${entries.length}`);
        console.info(`entries[0]: ${entries[0]}`);
      })
    }
  });
  console.info('Succeeded in getting entries');
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get entries.code is ${error.code},message is ${error.message}`);
}
```

#### getEntries

getEntries(deviceId: string, query: Query): Promise<Entry[]>

获取与指定设备ID和Query对象匹配的键值对列表，使用Promise异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 键值对所属的设备ID。 |
| query | Query | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Entry[]> | Promise对象。返回与指定设备ID和Query对象匹配的键值对列表。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let arr = new Uint8Array([21, 31]);
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_bool_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.BYTE_ARRAY,
        value: arr
    }
    entries.push(entry);
  }
  console.info(`entries: ${entries}`);
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
    let query = new distributedKVStore.Query();
    query.deviceId('localDeviceId');
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getEntries('localDeviceId', query).then((entries: distributedKVStore.Entry[]) => {
        console.info('Succeeded in getting entries');
      }).catch((err: BusinessError) => {
        console.error(`Failed to get entries.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  console.info('Succeeded in getting entries');
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get entries.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void

从DeviceKVStore数据库中获取本设备具有指定前缀的结果集，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<KVStoreResultSet> | 是 | 回调函数。返回具有指定前缀的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    if (kvStore != null) {
      kvStore.getResultSet('batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting result set');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err: BusinessError) => {
            if (err != undefined) {
              console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
              return;
            }
            console.info('Succeeded in closing result set');
          })
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(keyPrefix: string): Promise<KVStoreResultSet>

从DeviceKVStore数据库中获取本设备具有指定前缀的结果集，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KVStoreResultSet> | Promise对象。返回具有指定前缀的结果集。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  kvStore.getResultSet('batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing result set');
      }).catch((err: BusinessError) => {
        console.error(`Failed to close resultset.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KVStoreResultSet>): void

获取与指定设备ID和Key前缀匹配的KVStoreResultSet对象，使用callback异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |
| callback | AsyncCallback<KVStoreResultSet> | 是 | 回调函数。返回与指定设备ID和Key前缀匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('localDeviceId', 'batch_test_string_key', async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
    if (err != undefined) {
      console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in getting resultSet');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet, (err: BusinessError) => {
        if (err != undefined) {
          console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in closing resultSet');
      })
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(deviceId: string, keyPrefix: string): Promise<KVStoreResultSet>

获取与指定设备ID和Key前缀匹配的KVStoreResultSet对象，使用Promise异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 标识要查询其数据的设备。 |
| keyPrefix | string | 是 | 表示要匹配的键前缀。不能包含'^'，包含'^'将导致谓词失效，查询结果会返回数据库中的所有数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KVStoreResultSet> | Promise对象。返回与指定设备ID和Key前缀匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  kvStore.getResultSet('localDeviceId', 'batch_test_string_key').then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting resultSet');
    resultSet = result;
    if (kvStore != null) {
      kvStore.closeResultSet(resultSet).then(() => {
        console.info('Succeeded in closing resultSet');
      }).catch((err: BusinessError) => {
        console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KVStoreResultSet>): void

获取与指定设备ID和Query对象匹配的KVStoreResultSet对象，使用callback异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KVStoreResultSet对象所属的设备ID。 |
| query | Query | 是 | 表示查询对象。 |
| callback | AsyncCallback<KVStoreResultSet> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getResultSet('localDeviceId', query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting resultSet');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err: BusinessError) => {
            if (err != undefined) {
              console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
              return;
            }
            console.info('Succeeded in closing resultSet');
          })
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(deviceId: string, query: Query): Promise<KVStoreResultSet>

获取与指定设备ID和Query对象匹配的KVStoreResultSet对象，使用Promise异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KVStoreResultSet对象所属的设备ID。 |
| query | Query | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KVStoreResultSet> | Promise对象。返回与指定设备ID和Query对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch_test");
  if (kvStore != null) {
    kvStore.getResultSet('localDeviceId', query).then((result: distributedKVStore.KVStoreResultSet) => {
      console.info('Succeeded in getting resultSet');
      resultSet = result;
      if (kvStore != null) {
        kvStore.closeResultSet(resultSet).then(() => {
          console.info('Succeeded in closing resultSet');
        }).catch((err: BusinessError) => {
          console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
        });
      }
    }).catch((err: BusinessError) => {
      console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
    });
  }
  query.deviceId('localDeviceId');
  console.info("GetResultSet " + query.getSqlLike());

} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSet.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(query: Query): Promise<KVStoreResultSet>

获取与本设备指定Query对象匹配的KVStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KVStoreResultSet> | Promise对象。获取与本设备指定Query对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch_test");
  kvStore.getResultSet(query).then((result: distributedKVStore.KVStoreResultSet) => {
    console.info('Succeeded in getting result set');
    resultSet = result;
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultset.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSet

getResultSet(query: Query, callback:AsyncCallback<KVStoreResultSet>): void

获取与本设备指定Query对象匹配的KVStoreResultSet对象，使用callback异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |
| callback | AsyncCallback<KVStoreResultSet> | 是 | 回调函数，获取与指定Predicates对象匹配的KVStoreResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100001 | Over max limits. |
| 15100003 | Database corrupted. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let resultSet: distributedKVStore.KVStoreResultSet;
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, async (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getResultSet(query, async (err: BusinessError, result: distributedKVStore.KVStoreResultSet) => {
        if (err != undefined) {
          console.error(`Failed to get resultSet.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting resultSet');
        resultSet = result;
        if (kvStore != null) {
          kvStore.closeResultSet(resultSet, (err: BusinessError) => {
            if (err != undefined) {
              console.error(`Failed to close resultSet.code is ${err.code},message is ${err.message}`);
              return;
            }
            console.info('Succeeded in closing resultSet');
          })
        }
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSet`);
}
```

#### getResultSize

getResultSize(query: Query, callback: AsyncCallback<number>): void

获取与本设备指定Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回与本设备指定Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, (err: BusinessError) => {
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getResultSize(query, (err: BusinessError, resultSize: number) => {
        if (err != undefined) {
          console.error(`Failed to get result size.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting result set size');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSize

getResultSize(query: Query): Promise<number>

获取与本设备指定Query对象匹配的结果数，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | Query | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。获取与本设备指定Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes:1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  const query = new distributedKVStore.Query();
  query.prefixKey("batch_test");
  kvStore.getResultSize(query).then((resultSize: number) => {
    console.info('Succeeded in getting result set size');
  }).catch((err: BusinessError) => {
    console.error(`Failed to get result size.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`An unexpected error occurred.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSize

getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void;

获取与指定设备ID和Query对象匹配的结果数，使用callback异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KVStoreResultSet对象所属的设备ID。 |
| query | Query | 是 | 表示查询对象。 |
| callback | AsyncCallback<number> | 是 | 回调函数。返回与指定设备ID和Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries, (err: BusinessError) => {
    if (err != undefined) {
      console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Succeeded in putting batch');
    const query = new distributedKVStore.Query();
    query.prefixKey("batch_test");
    if (kvStore != null) {
      kvStore.getResultSize('localDeviceId', query, (err: BusinessError, resultSize: number) => {
        if (err != undefined) {
          console.error(`Failed to get resultSize.code is ${err.code},message is ${err.message}`);
          return;
        }
        console.info('Succeeded in getting resultSize');
      });
    }
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSize.code is ${error.code},message is ${error.message}`);
}
```

#### getResultSize

getResultSize(deviceId: string, query: Query): Promise<number>

获取与指定设备ID和Query对象匹配的结果数，使用Promise异步回调。


其中deviceId通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002553360553__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | KVStoreResultSet对象所属的设备ID。 |
| query | Query | 是 | 表示查询对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回与指定设备ID和Query对象匹配的结果数。 |

**错误码：**

以下错误码的详细介绍请参见[分布式键值数据库错误码](分布式键值数据库错误码.md)和[通用错误码](通用错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameters types. |
| 15100003 | Database corrupted. |
| 15100004 | Not found. |
| 15100005 | Database or result set already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let entries: distributedKVStore.Entry[] = [];
  for (let i = 0; i < 10; i++) {
    let key = 'batch_test_string_key';
    let entry: distributedKVStore.Entry = {
      key: key + i,
      value: {
        type: distributedKVStore.ValueType.STRING,
        value: 'batch_test_string_value'
    }
    entries.push(entry);
  }
  kvStore.putBatch(entries).then(async () => {
    console.info('Succeeded in putting batch');
  }).catch((err: BusinessError) => {
    console.error(`Failed to put batch.code is ${err.code},message is ${err.message}`);
  });
  let query = new distributedKVStore.Query();
  query.prefixKey("batch_test");
  kvStore.getResultSize('localDeviceId', query).then((resultSize: number) => {
    console.info('Succeeded in getting resultSize');
  }).catch((err: BusinessError) => {
    console.error(`Failed to get resultSize.code is ${err.code},message is ${err.message}`);
  });
} catch (e) {
  let error = e as BusinessError;
  console.error(`Failed to get resultSize.code is ${error.code},message is ${error.message}`);
}
```