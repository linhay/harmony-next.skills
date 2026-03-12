# @ohos.data.distributedData (分布式数据管理)

分布式数据管理为应用程序提供不同设备间数据库的分布式协同能力。通过调用分布式数据各个接口，应用程序可将数据保存到分布式数据库中，并可对分布式数据库中的数据进行增加、删除、修改、查询、同步等操作。

该模块提供以下分布式数据管理相关的常用功能：

- [KVManager](#ZH-CN_TOPIC_0000002529284683__kvmanager)：数据管理实例，用于获取KVStore的相关信息。
- [KvStoreResultSet8+](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)：提供获取KVStore数据库结果集的相关方法，包括查询和移动数据读取位置等。
- [Query8+](#ZH-CN_TOPIC_0000002529284683__query8)：使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。
- [KVStore](#ZH-CN_TOPIC_0000002529284683__kvstore)：KVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据同步完成的方法。
- [SingleKVStore](#ZH-CN_TOPIC_0000002529284683__singlekvstore)：单版本分布式数据库，继承自[KVStore](#ZH-CN_TOPIC_0000002529284683__kvstore)，不对数据所属设备进行区分，提供查询数据和同步数据的方法。
- [DeviceKVStore8+](#ZH-CN_TOPIC_0000002529284683__devicekvstore8)：设备协同数据库，继承自[KVStore](#ZH-CN_TOPIC_0000002529284683__kvstore)，以设备维度对数据进行区分，提供查询数据和同步数据的方法。

-

从API Version 9开始，该接口不再维护，推荐使用新接口[@ohos.data.distributedKVStore](@ohos.data.distributedKVStore (分布式键值数据库).md)。

-

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本模块中所有需要获取deviceId的接口，都仅系统应用可用。

#### 导入模块

```ets
import distributedData from '@ohos.data.distributedData';
```

#### distributedData.createKVManager

createKVManager(config: KVManagerConfig, callback: AsyncCallback<KVManager>): void

创建一个KVManager对象实例，用于管理数据库对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明config[KVManagerConfig](#ZH-CN_TOPIC_0000002529284683__kvmanagerconfig)是提供KVManager实例的配置信息，包括调用方的Bundle名称和用户信息。callbackAsyncCallback<[KVManager](#ZH-CN_TOPIC_0000002529284683__kvmanager)>是回调函数。返回创建的KVManager对象实例。

**示例：**

```ets

let kvManager;
try {
    const kvManagerConfig = {
        bundleName : 'com.example.datamanagertest',
        userInfo : {
            userId : '0',
            userType : distributedData.UserType.SAME_USER_ID
        }
    }
    distributedData.createKVManager(kvManagerConfig, function (err, manager) {
        if (err) {
            console.log("Failed to create KVManager: "  + JSON.stringify(err));
            return;
        }
        console.log("Succeeded in creating KVManager");
        kvManager = manager;
    });
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```

#### distributedData.createKVManager

createKVManager(config: KVManagerConfig): Promise<KVManager>

创建一个KVManager对象实例，用于管理数据库对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明config[KVManagerConfig](#ZH-CN_TOPIC_0000002529284683__kvmanager)是提供KVManager实例的配置信息，包括调用方的包名和用户信息。

**返回值：**

类型说明Promise<[KVManager](#ZH-CN_TOPIC_0000002529284683__kvmanager)>Promise对象。返回创建的KVManager对象实例。

**示例：**

```ets

try {
  const kvManagerConfig = {
    bundleName: 'com.example.datamanagertest',
    userInfo: {
      userId: '0',
      userType: distributedData.UserType.SAME_USER_ID
    }
  }
  distributedData.createKVManager(kvManagerConfig).then((manager) => {
    console.log("Succeeded in creating KVManager");
    kvManager = manager;
  }).catch((err) => {
    console.error("Failed to create KVManager: " + JSON.stringify(err));
  });
} catch (e) {
  console.log("An unexpected error occurred. Error:" + e);
}
```

#### KVManagerConfig

提供KVManager实例的配置信息，包括调用方的Bundle名称和用户信息。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

名称类型必填说明userInfo[UserInfo](#ZH-CN_TOPIC_0000002529284683__userinfo)是调用方的用户信息。bundleNamestring是调用方的Bundle名称。

#### UserInfo

用户信息。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

名称类型必填说明userIdstring否指示要设置的用户ID，默认为'0'。userType[UserType](#ZH-CN_TOPIC_0000002529284683__usertype)否指示要设置的用户类型，默认为0。

#### UserType

用户类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

名称值说明SAME_USER_ID0使用同一账号登录不同设备的用户。

#### KVManager

数据管理实例，用于获取KVStore的相关信息。在调用KVManager的方法前，需要先通过[createKVManager](#ZH-CN_TOPIC_0000002529284683__distributeddatacreatekvmanager)构建一个KVManager实例。

#### getKVStore

getKVStore<T extends KVStore>(storeId: string, options: Options, callback: AsyncCallback<T>): void

通过指定Options和storeId，创建并获取KVStore数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明storeIdstring是数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。options[Options](#ZH-CN_TOPIC_0000002529284683__options)是创建KVStore实例的配置信息。callbackAsyncCallback<T>是回调函数。返回创建的KVStore数据库实例。

**示例：**

```ets
let kvStore;
let kvManager;
try {
    const options = {
        createIfMissing : true,
        encrypt : false,
        backup : false,
        autoSync : true,
        kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
        securityLevel : distributedData.SecurityLevel.S3,
    };
    kvManager.getKVStore('storeId', options, function (err, store) {
        if (err) {
            console.log("getKVStore err: "  + JSON.stringify(err));
            return;
        }
        console.log("getKVStore success");
        kvStore = store;
    });
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```

#### getKVStore

getKVStore<T extends KVStore>(storeId: string, options: Options): Promise<T>

通过指定Options和storeId，创建并获取KVStore数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明storeIdstring是数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。options[Options](#ZH-CN_TOPIC_0000002529284683__options)是创建KVStore实例的配置信息。

**返回值：**

类型说明Promise<T> ，<T extends [KVStore](#ZH-CN_TOPIC_0000002529284683__kvstore)>Promise对象。返回创建的KVStore数据库实例。

**示例：**

```ets
let kvStore;
let kvManager;
try {
    const options = {
        createIfMissing : true,
        encrypt : false,
        backup : false,
        autoSync : true,
        kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
        securityLevel : distributedData.SecurityLevel.S3,
    };
    kvManager.getKVStore('storeId', options).then((store) => {
        console.log("getKVStore success");
        kvStore = store;
    }).catch((err) => {
        console.log("getKVStore err: "  + JSON.stringify(err));
    });
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```

#### closeKVStore8+

closeKVStore(appId: string, storeId: string, kvStore: KVStore, callback: AsyncCallback<void>): void

通过storeId的值关闭指定的KVStore数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明appIdstring是所调用数据库方的包名。storeIdstring是要关闭的数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。kvStore[KVStore](#ZH-CN_TOPIC_0000002529284683__kvstore)是要关闭的KVStore数据库。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
let kvManager;
const options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedData.KVStoreType.SINGLE_VERSION,
    schema: undefined,
    securityLevel: distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('storeId', options, async function (err, store) {
        console.log('getKVStore success');
        kvStore = store;
        kvManager.closeKVStore('appId', 'storeId', kvStore, function (err, data) {
            console.log('closeKVStore success');
        });
    });
} catch (e) {
    console.log('closeKVStore e ' + e);
}
```

#### closeKVStore8+

closeKVStore(appId: string, storeId: string, kvStore: KVStore): Promise<void>

通过storeId的值关闭指定的KVStore数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明appIdstring是所调用数据库方的包名。storeIdstring是要关闭的数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。kvStore[KVStore](#ZH-CN_TOPIC_0000002529284683__kvstore)是要关闭的KVStore数据库。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvManager;
let kvStore;
const options = {
    createIfMissing: true,
    encrypt: false,
    backup: false,
    autoSync: false,
    kvStoreType: distributedData.KVStoreType.SINGLE_VERSION,
    schema: undefined,
    securityLevel: distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('storeId', options).then(async (store) => {
        console.log('getKVStore success');
        kvStore = store;
        kvManager.closeKVStore('appId', 'storeId', kvStore).then(() => {
            console.log('closeKVStore success');
        }).catch((err) => {
            console.log('closeKVStore err ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('CloseKVStore getKVStore err ' + JSON.stringify(err));
    });
} catch (e) {
    console.log('closeKVStore e ' + e);
}
```

#### deleteKVStore8+

deleteKVStore(appId: string, storeId: string, callback: AsyncCallback<void>): void

通过storeId的值删除指定的KVStore数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明appIdstring是所调用数据库方的包名。storeIdstring是要删除的数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvManager;
let kvStore;
const options = {
    createIfMissing : true,
    encrypt : false,
    backup : false,
    autoSync : true,
    kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
    schema : undefined,
    securityLevel : distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('store', options, async function (err, store) {
        console.log('getKVStore success');
        kvStore = store;
        kvManager.deleteKVStore('appId', 'storeId', function (err, data) {
            console.log('deleteKVStore success');
        });
    });
} catch (e) {
    console.log('DeleteKVStore e ' + e);
}
```

#### deleteKVStore8+

deleteKVStore(appId: string, storeId: string): Promise<void>

通过storeId的值删除指定的KVStore数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明appIdstring是所调用数据库方的包名。storeIdstring是要删除的数据库唯一标识符，长度不大于[MAX_STORE_ID_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvManager;
let kvStore;
const options = {
    createIfMissing : true,
    encrypt : false,
    backup : false,
    autoSync : true,
    kvStoreType : distributedData.KVStoreType.SINGLE_VERSION,
    schema : undefined,
    securityLevel : distributedData.SecurityLevel.S3,
}
try {
    kvManager.getKVStore('storeId', options).then(async (store) => {
        console.log('getKVStore success');
        kvStore = store;
        kvManager.deleteKVStore('appId', 'storeId').then(() => {
            console.log('deleteKVStore success');
        }).catch((err) => {
            console.log('deleteKVStore err ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('getKVStore err ' + JSON.stringify(err));
    });
} catch (e) {
    console.log('deleteKVStore e ' + e);
}
```

#### getAllKVStoreId8+

getAllKVStoreId(appId: string, callback: AsyncCallback<string[]>): void

获取所有通过[getKVStore](#ZH-CN_TOPIC_0000002529284683__getkvstore)方法创建的且没有调用[deleteKVStore](#ZH-CN_TOPIC_0000002529284683__deletekvstore8)方法删除的KVStore数据库的storeId，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明appIdstring是所调用数据库方的包名。callbackAsyncCallback<string[]>是回调函数。返回所有创建的KvStore数据库的storeId。

**示例：**

```ets
let kvManager;
try {
    kvManager.getAllKVStoreId('appId', function (err, data) {
        console.log('GetAllKVStoreId success');
        console.log('GetAllKVStoreId size = ' + data.length);
    });
} catch (e) {
    console.log('GetAllKVStoreId e ' + e);
}
```

#### getAllKVStoreId8+

getAllKVStoreId(appId: string): Promise<string[]>

获取所有通过[getKVStore](#ZH-CN_TOPIC_0000002529284683__getkvstore)方法创建的且没有调用[deleteKVStore](#ZH-CN_TOPIC_0000002529284683__deletekvstore8)方法删除的KVStore数据库的storeId，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明appIdstring是所调用数据库方的包名。

**返回值：**

类型说明Promise<string[]>Promise对象。返回所有创建的KvStore数据库的storeId。

**示例：**

```ets
let kvManager;
try {
    console.log('GetAllKVStoreId');
    kvManager.getAllKVStoreId('appId').then((data) => {
        console.log('getAllKVStoreId success');
        console.log('size = ' + data.length);
    }).catch((err) => {
        console.log('getAllKVStoreId err ' + JSON.stringify(err));
    });
} catch(e) {
    console.log('getAllKVStoreId e ' + e);
}
```

#### on('distributedDataServiceDie')8+

on(event: 'distributedDataServiceDie', deathCallback: Callback<void>): void

订阅服务状态变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明eventstring是订阅的事件名，固定为'distributedDataServiceDie'，即服务状态变更事件。deathCallbackCallback<void>是回调函数。

**示例：**

```ets
let kvManager;
try {
    console.log('KVManagerOn');
    const deathCallback = function () {
        console.log('death callback call');
    }
    kvManager.on('distributedDataServiceDie', deathCallback);
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```

#### off('distributedDataServiceDie')8+

off(event: 'distributedDataServiceDie', deathCallback?: Callback<void>): void

取消订阅服务状态变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明eventstring是取消订阅的事件名，固定为'distributedDataServiceDie'，即服务状态变更事件。deathCallbackCallback<void>否取消订阅的函数。如不设置callback，则取消所有已订阅的函数。

**示例：**

```ets
let kvManager;
try {
    console.log('KVManagerOff');
    const deathCallback = function () {
        console.log('death callback call');
    }
    kvManager.off('distributedDataServiceDie', deathCallback);
} catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}

```

#### Options

用于提供创建数据库的配置信息。

名称类型必填说明createIfMissingboolean否

当数据库文件不存在时是否创建数据库，默认为true，即创建。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

encryptboolean否

设置数据库文件是否加密，默认为false，即不加密。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

backupboolean否

设置数据库文件是否备份，默认为true，即备份。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

autoSyncboolean否

设置数据库文件是否自动同步。默认为false，即手动同步。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**需要权限**： ohos.permission.DISTRIBUTED_DATASYNC

kvStoreType[KVStoreType](#ZH-CN_TOPIC_0000002529284683__kvstoretype)否

设置要创建的数据库类型，默认为DEVICE_COLLABORATION，即多设备协同数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

securityLevel[SecurityLevel](#ZH-CN_TOPIC_0000002529284683__securitylevel)否

设置数据库安全级别(S1-S4)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

schema8+[Schema](#ZH-CN_TOPIC_0000002529284683__schema8)否

设置定义存储在数据库中的值，默认为undefined，即不使用schema。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

#### KVStoreType

KVStore数据库类型枚举。

名称值说明DEVICE_COLLABORATION0

表示多设备协同数据库。

**数据库特点：** 数据以设备的维度管理，不存在冲突；支持按照设备的维度查询数据。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

SINGLE_VERSION1

表示单版本数据库。

**数据库特点：** 数据不分设备，设备之间修改相同的key会覆盖。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

MULTI_VERSION2

表示多版本数据库。当前暂不支持使用此接口。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

#### SecurityLevel

数据库的安全级别枚举。

名称值说明NO_LEVEL0

表示数据库不设置安全级别(已废弃)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

S01

表示数据库的安全级别为公共级别(已废弃)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

S12

表示数据库的安全级别为低级别，当数据泄露时会产生较低影响。例如，包含壁纸等系统数据的数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

S23

表示数据库的安全级别为中级别，当数据泄露时会产生较大影响。例如，包含录音、视频等用户生成数据或通话记录等信息的数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

S35

表示数据库的安全级别为高级别，当数据泄露时会产生重大影响。例如，包含用户运动、健康、位置等信息的数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

S46

表示数据库的安全级别为关键级别，当数据泄露时会产生严重影响。例如，包含认证凭据、财务数据等信息的数据库。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

#### Constants

KVStore常量。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

名称值说明MAX_KEY_LENGTH1024数据库中Key允许的最大长度，单位字节。MAX_VALUE_LENGTH4194303数据库中Value允许的最大长度，单位字节。MAX_KEY_LENGTH_DEVICE896最大设备密钥长度，单位字节。MAX_STORE_ID_LENGTH128数据库标识符允许的最大长度，单位字节。MAX_QUERY_LENGTH512000最大查询长度，单位字节。MAX_BATCH_SIZE128最大批处理操作数量。

#### Schema8+

表示数据库模式，可以在创建或打开数据库时创建Schema对象并将它们放入[Options](#ZH-CN_TOPIC_0000002529284683__options)中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

名称类型可读可写说明root8+[FieldNode](#ZH-CN_TOPIC_0000002529284683__fieldnode8)是是表示json根对象。indexes8+Array<string>是是表示json类型的字符串数组。mode8+number是是表示Schema的模式。skip8+number是是Schema的跳跃大小。

#### constructor8+

constructor()

用于创建Schema实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

#### FieldNode8+

表示 Schema 实例的节点，提供定义存储在数据库中的值的方法。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

名称类型可读可写说明nullable8+boolean是是表示数据库字段是否可以为空。default8+string是是表示Fieldnode的默认值。type8+number是是表示指定节点对应数据类型的值。

#### constructor8+

constructor(name: string)

用于创建带有string字段FieldNode实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明namestring是FieldNode的值。

#### appendChild8+

appendChild(child: FieldNode): boolean

在当前 FieldNode 中添加一个子节点。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明child[FieldNode](#ZH-CN_TOPIC_0000002529284683__fieldnode8)是要附加的域节点。

**返回值：**

类型说明boolean返回true表示子节点成功添加到FieldNode；返回false则表示操作失败。

**示例：**

```ets
import ddm from '@ohos.data.distributedData';
try {
    let node = new ddm.FieldNode("root");
    let child1 = new ddm.FieldNode("child1");
    let child2 = new ddm.FieldNode("child2");
    let child3 = new ddm.FieldNode("child3");
    node.appendChild(child1);
    node.appendChild(child2);
    node.appendChild(child3);
    console.log("appendNode " + JSON.stringify(node));
    child1 = null;
    child2 = null;
    child3 = null;
    node = null;
} catch (e) {
    console.log("AppendChild " + e);
}
```

#### KvStoreResultSet8+

提供获取KVStore数据库结果集的相关方法，包括查询和移动数据读取位置等。

在调用KvStoreResultSet的方法前，需要先通过[getKVStore](#ZH-CN_TOPIC_0000002529284683__getkvstore)构建一个KVStore实例。

#### getCount8+

getCount(): number

获取结果集中的总行数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明number返回数据的总行数。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const count = resultSet.getCount();
    console.log("getCount succeed:" + count);
} catch (e) {
    console.log("getCount failed: " + e);
}
```

#### getPosition8+

getPosition(): number

获取结果集中当前的读取位置。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明number返回当前读取位置。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeeded.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const position = resultSet.getPosition();
    console.log("getPosition succeed:" + position);
} catch (e) {
    console.log("getPosition failed: " + e);
}
```

#### moveToFirst8+

moveToFirst(): boolean

将读取位置移动到第一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明boolean返回true表示操作成功；返回false则表示操作失败。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved1 = resultSet.moveToFirst();
    console.log("moveToFirst succeed: " + moved1);
} catch (e) {
    console.log("moveToFirst failed " + e);
}
```

#### moveToLast8+

moveToLast(): boolean

将读取位置移动到最后一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明boolean返回true表示操作成功；返回false则表示操作失败。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved2 = resultSet.moveToLast();
    console.log("moveToLast succeed:" + moved2);
} catch (e) {
    console.log("moveToLast failed: " + e);
}
```

#### moveToNext8+

moveToNext(): boolean

将读取位置移动到下一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明boolean返回true表示操作成功；返回false则表示操作失败。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved3 = resultSet.moveToNext();
    console.log("moveToNext succeed: " + moved3);
} catch (e) {
    console.log("moveToNext failed: " + e);
}
```

#### moveToPrevious8+

moveToPrevious(): boolean

将读取位置移动到上一行。如果结果集为空，则返回false。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明boolean返回true表示操作成功；返回false则表示操作失败。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved4 = resultSet.moveToPrevious();
    console.log("moveToPrevious succeed:" + moved4);
} catch (e) {
    console.log("moveToPrevious failed: " + e);
}
```

#### move8+

move(offset: number): boolean

将读取位置移动到当前位置的相对偏移量。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明offsetnumber是表示与当前位置的相对偏移量，负偏移表示向后移动，正偏移表示向前移动。

**返回值：**

类型说明boolean返回true表示操作成功；返回false则表示操作失败。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved5 = resultSet.move(1);
    console.log("move succeed:" + moved5);
} catch (e) {
    console.log("move failed: " + e);
}
```

#### moveToPosition8+

moveToPosition(position: number): boolean

将读取位置从 0 移动到绝对位置。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明positionnumber是表示绝对位置。

**返回值：**

类型说明boolean返回true表示操作成功；返回false则表示操作失败。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const moved6 = resultSet.moveToPosition(1);
    console.log("moveToPosition succeed: " + moved6);
} catch (e) {
    console.log("moveToPosition failed: " + e);
}
```

#### isFirst8+

isFirst(): boolean

检查读取位置是否为第一行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明boolean返回true表示读取位置为第一行；返回false表示读取位置不是第一行。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const isfirst = resultSet.isFirst();
    console.log("Check isFirst succeed:" + isfirst);
} catch (e) {
    console.log("Check isFirst failed: " + e);
}
```

#### isLast8+

isLast(): boolean

检查读取位置是否为最后一行。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明boolean返回true表示读取位置为最后一行；返回false表示读取位置不是最后一行。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const islast = resultSet.isLast();
    console.log("Check isLast succeed: " + islast);
} catch (e) {
    console.log("Check isLast failed: " + e);
}
```

#### isBeforeFirst8+

isBeforeFirst(): boolean

检查读取位置是否在第一行之前。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明boolean返回true表示读取位置在第一行之前；返回false表示读取位置不在第一行之前。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const isbeforefirst = resultSet.isBeforeFirst();
    console.log("Check isBeforeFirst succeed: " + isbeforefirst);
} catch (e) {
    console.log("Check isBeforeFirst failed: " + e);
}
```

#### isAfterLast8+

isAfterLast(): boolean

检查读取位置是否在最后一行之后。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明boolean返回true表示读取位置在最后一行之后；返回false表示读取位置不在最后一行之后。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const isafterlast = resultSet.isAfterLast();
    console.log("Check isAfterLast succeed:" + isafterlast);
} catch (e) {
    console.log("Check isAfterLast failed: " + e);
}
```

#### getEntry8+

getEntry(): Entry

从当前位置获取对应的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明[Entry](#ZH-CN_TOPIC_0000002529284683__entry)返回键值对。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + err);
    });
    const entry  = resultSet.getEntry();
    console.log("getEntry succeed:" + JSON.stringify(entry));
} catch (e) {
    console.log("getEntry failed: " + e);
}
```

#### Query8+

使用谓词表示数据库查询，提供创建Query实例、查询数据库中的数据和添加谓词的方法。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

#### constructor8+

constructor()

用于创建Schema实例的构造函数。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

#### reset8+

reset(): Query

重置Query对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回重置的Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.equalTo("key", "value");
    console.log("query is " + query.getSqlLike());
    query.reset();
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("simply calls should be ok :" + e);
}
```

#### equalTo8+

equalTo(field: string, value: number|string|boolean): Query

构造一个Query对象来查询具有指定字段的条目，其值等于指定的值。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valuenumber|string|boolean是表示指定的值。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.equalTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### notEqualTo8+

notEqualTo(field: string, value: number|string|boolean): Query

构造一个Query对象以查询具有指定字段且值不等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valuenumber|string|boolean是表示指定的值。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### greaterThan8+

greaterThan(field: string, value: number|string|boolean): Query

构造一个Query对象以查询具有大于指定值的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valuenumber|string|boolean是表示指定的值。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.greaterThan("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### lessThan8+

lessThan(field: string, value: number|string): Query

构造一个Query对象以查询具有小于指定值的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valuenumber|string是表示指定的值。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.lessThan("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### greaterThanOrEqualTo8+

greaterThanOrEqualTo(field: string, value: number|string): Query

构造一个Query对象以查询具有指定字段且值大于或等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valuenumber|string是表示指定的值。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.greaterThanOrEqualTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### lessThanOrEqualTo8+

lessThanOrEqualTo(field: string, value: number|string): Query

构造一个Query对象以查询具有指定字段且值小于或等于指定值的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valuenumber|string是表示指定的值。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.lessThanOrEqualTo("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### isNull8+

isNull(field: string): Query

构造一个Query对象以查询具有值为null的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.isNull("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### inNumber8+

inNumber(field: string, valueList: number[]): Query

构造一个Query对象以查询具有指定字段的条目，其值在指定的值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valueListnumber[]是表示指定的值列表。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.inNumber("field", [0, 1]);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### inString8+

inString(field: string, valueList: string[]): Query

构造一个Query对象以查询具有指定字段的条目，其值在指定的字符串值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valueListstring[]是表示指定的字符串值列表。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.inString("field", ['test1', 'test2']);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### notInNumber8+

notInNumber(field: string, valueList: number[]): Query

构造一个Query对象以查询具有指定字段的条目，该字段的值不在指定的值列表中。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valueListnumber[]是表示指定的值列表。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.notInNumber("field", [0, 1]);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### notInString8+

notInString(field: string, valueList: string[]): Query

构造一个Query对象以查询具有指定字段且值不在指定字符串值列表中的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valueListstring[]是表示指定的字符串值列表。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.notInString("field", ['test1', 'test2']);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### like8+

like(field: string, value: string): Query

构造一个Query对象以查询具有与指定字符串值相似的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valuestring是表示指定的字符串值。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.like("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### unlike8+

unlike(field: string, value: string): Query

构造一个Query对象以查询具有与指定字符串值不相似的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。valuestring是表示指定的字符串值。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.unlike("field", "value");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### and8+

and(): Query

构造一个带有与条件的查询对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回查询对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value1");
    query.and();
    query.notEqualTo("field", "value2");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### or8+

or(): Query

构造一个带有或条件的Query对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回查询对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value1");
    query.or();
    query.notEqualTo("field", "value2");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### orderByAsc8+

orderByAsc(field: string): Query

构造一个Query对象，将查询结果按升序排序。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.orderByAsc("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### orderByDesc8+

orderByDesc(field: string): Query

构造一个Query对象，将查询结果按降序排序。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.orderByDesc("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### limit8+

limit(total: number, offset: number): Query

构造一个Query对象来指定结果的数量和开始位置。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明totalnumber是表示指定的结果数。offsetnumber是表示起始位置。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
let total = 10;
let offset = 1;
try {
    let query = new distributedData.Query();
    query.notEqualTo("field", "value");
    query.limit(total, offset);
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### isNotNull8+

isNotNull(field: string): Query

构造一个Query对象以查询具有值不为null的指定字段的条目。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明fieldstring是表示指定字段，不能包含' ^ '。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.isNotNull("field");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### beginGroup8+

beginGroup(): Query

创建一个带有左括号的查询条件组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.beginGroup();
    query.isNotNull("field");
    query.endGroup();
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### endGroup8+

endGroup(): Query

创建一个带有右括号的查询条件组。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.beginGroup();
    query.isNotNull("field");
    query.endGroup();
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### prefixKey8+

prefixKey(prefix: string): Query

创建具有指定键前缀的查询条件。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明prefixstring是表示指定的键前缀。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.prefixKey("$.name");
    query.prefixKey("0");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
    console.log("duplicated calls should be ok :" + e);
}
```

#### setSuggestIndex8+

setSuggestIndex(index: string): Query

设置一个指定的索引，将优先用于查询。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明indexstring是指示要设置的索引。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.setSuggestIndex("$.name");
    query.setSuggestIndex("0");
    console.log("query is " + query.getSqlLike());
    query = null;
} catch (e) {
   console.log("duplicated calls should be ok :" + e);
}
```

#### deviceId8+

deviceId(deviceId:string):Query

添加设备ID作为key的前缀。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明deviceIdstring是指示查询的设备ID。

**返回值：**

类型说明[Query](#ZH-CN_TOPIC_0000002529284683__query8)返回Query对象。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    query.deviceId("deviceId");
    console.log("query is " + query.getSqlLike());
} catch (e) {
    console.log("should be ok on Method Chaining : " + e);
}
```

#### getSqlLike8+

getSqlLike():string

获取Query对象的查询语句。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明string返回一个字段列中包含对应子串的结果。

**示例：**

```ets
try {
    let query = new distributedData.Query();
    let sql1 = query.getSqlLike();
    console.log("GetSqlLike sql=" + sql1);
} catch (e) {
    console.log("duplicated calls should be ok : " + e);
}
```

#### KVStore

KVStore数据库实例，提供增加数据、删除数据和订阅数据变更、订阅数据同步完成的方法。

在调用KVStore的方法前，需要先通过[getKVStore](#ZH-CN_TOPIC_0000002529284683__getkvstore)构建一个KVStore实例。

#### put

put(key: string, value: Uint8Array | string | number | boolean, callback: AsyncCallback<void>): void

添加指定类型键值对到数据库，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keystring是要添加数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。valueUint8Array | string | number | boolean是要添加数据的value，支持Uint8Array、number 、 string 、boolean，Uint8Array、string 的长度不大于[MAX_VALUE_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, function (err,data) {
        if (err != undefined) {
            console.log("put err: " + JSON.stringify(err));
            return;
        }
        console.log("put success");
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```

#### put

put(key: string, value: Uint8Array | string | number | boolean): Promise<void>

添加指定类型键值对到数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keystring是要添加数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。valueUint8Array | string | number | boolean是要添加数据的value，支持Uint8Array、number 、 string 、boolean，Uint8Array、string 的长度不大于[MAX_VALUE_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((data) => {
        console.log("put success: " + JSON.stringify(data));
    }).catch((err) => {
        console.log("put err: " + JSON.stringify(err));
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```

#### delete

delete(key: string, callback: AsyncCallback<void>): void

从数据库中删除指定键值的数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keystring是要删除数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, function (err,data) {
        if (err != undefined) {
            console.log("put err: " + JSON.stringify(err));
            return;
        }
        console.log("put success");
        kvStore.delete(KEY_TEST_STRING_ELEMENT, function (err,data) {
            if (err != undefined) {
                console.log("delete err: " + JSON.stringify(err));
                return;
            }
            console.log("delete success");
        });
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```

#### delete

delete(key: string): Promise<void>

从数据库中删除指定键值的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keystring是要删除数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((data) => {
        console.log("put success: " + JSON.stringify(data));
        kvStore.delete(KEY_TEST_STRING_ELEMENT).then((data) => {
            console.log("delete success");
        }).catch((err) => {
            console.log("delete err: " + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log("put err: " + JSON.stringify(err));
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```

#### on('dataChange')

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

订阅指定类型的数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是订阅的事件名，固定为'dataChange'，表示数据变更事件。type[SubscribeType](#ZH-CN_TOPIC_0000002529284683__subscribetype)是表示订阅的类型。listenerCallback<[ChangeNotification](#ZH-CN_TOPIC_0000002529284683__changenotification)>是回调函数。

**示例：**

```ets
let kvStore;
kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_LOCAL, function (data) {
    console.log("dataChange callback call data: " + JSON.stringify(data));
});
```

#### on('syncComplete')

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是订阅的事件名，固定为'syncComplete'，表示同步完成事件。syncCallbackCallback<Array<[string, number]>>是回调函数。用于向调用方发送同步结果的回调。

**示例：**

```ets
let kvStore;
kvStore.on('syncComplete', function (data) {
    console.log("callback call data: " + data);
});
```

#### off('dataChange')8+

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是取消订阅的事件名，固定为'dataChange'，表示数据变更事件。listenerCallback<[ChangeNotification](#ZH-CN_TOPIC_0000002529284683__changenotification)>否取消订阅的函数。如不设置callback，则取消所有订阅的函数。

**示例：**

```ets
let kvStore;
class KvstoreModel {
    call(data) {
        console.log("dataChange: " + data);
    }
    subscribeDataChange() {
        if (kvStore != null) {
            kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
        }
    }
    unsubscribeDataChange() {
        if (kvStore != null) {
            kvStore.off('dataChange', this.call);
        }
    }
}
```

#### off('syncComplete')8+

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。syncCallbackCallback<Array<[string, number]>>否取消订阅的函数。如不设置callback，则取消所有订阅的函数。

**示例：**

```ets
let kvStore;
class KvstoreModel {
    call(data) {
        console.log("syncComplete: " + data);
    }
    subscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.on('syncComplete', this.call);
        }
    }
    unsubscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.off('syncComplete', this.call);
        }
    }
}
```

#### putBatch8+

putBatch(entries: Entry[], callback: AsyncCallback<void>): void

批量插入键值对到KVStore数据库中，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明entries[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]是表示要批量插入的键值对。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        kvStore.getEntries('batch_test_string_key', function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries[0]: ' + JSON.stringify(entries[0]));
        });
    });
}catch(e) {
    console.log('PutBatch e ' + JSON.stringify(e));
}
```

#### putBatch8+

putBatch(entries: Entry[]): Promise<void>

批量插入键值对到KVStore数据库中，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明entries[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]是表示要批量插入的键值对。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        kvStore.getEntries('batch_test_string_key').then((entries) => {
            console.log('getEntries success');
            console.log('PutBatch ' + JSON.stringify(entries));
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('PutBatch e ' + JSON.stringify(e));
}
```

#### deleteBatch8+

deleteBatch(keys: string[], callback: AsyncCallback<void>): void

批量删除KVStore数据库中的键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keysstring[]是表示要批量删除的键值对。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    let keys = [];
    for (var i = 0; i < 5; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
        keys.push(key + i);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        kvStore.deleteBatch(keys, async function (err,data) {
            console.log('deleteBatch success');
        });
    });
}catch(e) {
    console.log('DeleteBatch e ' + e);
}
```

#### deleteBatch8+

deleteBatch(keys: string[]): Promise<void>

批量删除KVStore数据库中的键值对，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keysstring[]是表示要批量删除的键值对。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    let keys = [];
    for (var i = 0; i < 5; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
        keys.push(key + i);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        kvStore.deleteBatch(keys).then((err) => {
            console.log('deleteBatch success');
        }).catch((err) => {
            console.log('deleteBatch fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('DeleteBatch e ' + e);
}
```

#### startTransaction8+

startTransaction(callback: AsyncCallback<void>): void

启动KVStore数据库中的事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
function putBatchString(len, prefix) {
    let entries = [];
    for (var i = 0; i < len; i++) {
        var entry = {
            key : prefix + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    return entries;
}
try {
    var count = 0;
    kvStore.on('dataChange', 0, function (data) {
        console.log('startTransaction 0' + data)
        count++;
    });
    kvStore.startTransaction(async function (err,data) {
        console.log('startTransaction success');
        let entries = putBatchString(10, 'batch_test_string_key');
        console.log('entries: ' + JSON.stringify(entries));
        kvStore.putBatch(entries, async function (err,data) {
            console.log('putBatch success');
        });
    });
}catch(e) {
    console.log('startTransaction e ' + e);
}
```

#### startTransaction8+

startTransaction(): Promise<void>

启动KVStore数据库中的事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
try {
    var count = 0;
    kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_ALL, function (data) {
        console.log('startTransaction ' + JSON.stringify(data));
        count++;
    });
    kvStore.startTransaction().then(async (err) => {
        console.log('startTransaction success');
    }).catch((err) => {
        console.log('startTransaction fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('startTransaction e ' + e);
}
```

#### commit8+

commit(callback: AsyncCallback<void>): void

提交KVStore数据库中的事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
try {
    kvStore.commit(function (err,data) {
        if (err == undefined) {
            console.log('commit success');
        } else {
            console.log('commit fail');
        }
    });
}catch(e) {
    console.log('Commit e ' + e);
}
```

#### commit8+

commit(): Promise<void>

提交KVStore数据库中的事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
try {
    kvStore.commit().then(async (err) => {
        console.log('commit success');
    }).catch((err) => {
        console.log('commit fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('Commit e ' + e);
}
```

#### rollback8+

rollback(callback: AsyncCallback<void>): void

在KVStore数据库中回滚事务，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
try {
    kvStore.rollback(function (err,data) {
        if (err == undefined) {
            console.log('commit success');
        } else {
            console.log('commit fail');
        }
    });
}catch(e) {
    console.log('Rollback e ' + e);
}
```

#### rollback8+

rollback(): Promise<void>

在KVStore数据库中回滚事务，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
try {
    kvStore.rollback().then(async (err) => {
        console.log('rollback success');
    }).catch((err) => {
        console.log('rollback fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('Rollback e ' + e);
}
```

#### enableSync8+

enableSync(enabled: boolean, callback: AsyncCallback<void>): void

设定是否开启同步，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明enabledboolean是设定是否开启同步，true表示开启同步，false表示不启用同步。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
try {
    kvStore.enableSync(true, function (err,data) {
        if (err == undefined) {
            console.log('enableSync success');
        } else {
            console.log('enableSync fail');
        }
    });
}catch(e) {
    console.log('EnableSync e ' + e);
}
```

#### enableSync8+

enableSync(enabled: boolean): Promise<void>

设定是否开启同步，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明enabledboolean是设定是否开启同步，true表示开启同步，false表示不启用同步。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
try {
    kvStore.enableSync(true).then((err) => {
        console.log('enableSync success');
    }).catch((err) => {
        console.log('enableSync fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('EnableSync e ' + e);
}
```

#### setSyncRange8+

setSyncRange(localLabels: string[], remoteSupportLabels: string[], callback: AsyncCallback<void>): void

设置同步范围标签，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明localLabelsstring[]是表示本地设备的同步标签。remoteSupportLabelsstring[]是表示要同步数据的设备的同步标签。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
try {
    const localLabels = ['A', 'B'];
    const remoteSupportLabels = ['C', 'D'];
    kvStore.setSyncRange(localLabels, remoteSupportLabels, function (err,data) {
        console.log('SetSyncRange put success');
    });
}catch(e) {
    console.log('SetSyncRange e ' + e);
}
```

#### setSyncRange8+

setSyncRange(localLabels: string[], remoteSupportLabels: string[]): Promise<void>

设置同步范围标签，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明localLabelsstring[]是表示本地设备的同步标签。remoteSupportLabelsstring[]是表示要同步数据的设备的同步标签。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
try {
    const localLabels = ['A', 'B'];
    const remoteSupportLabels = ['C', 'D'];
    kvStore.setSyncRange(localLabels, remoteSupportLabels).then((err) => {
        console.log('setSyncRange success');
    }).catch((err) => {
        console.log('delete fail ' + err);
    });
}catch(e) {
    console.log('SetSyncRange e ' + e);
}
```

#### SubscribeType

订阅类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

名称值说明SUBSCRIBE_TYPE_LOCAL0表示订阅本地数据变更。SUBSCRIBE_TYPE_REMOTE1表示订阅远端数据变更。SUBSCRIBE_TYPE_ALL2表示订阅远端和本地数据变更。

#### ChangeNotification

数据变更时通知的对象，包括数据插入的数据、更新的数据、删除的数据和设备ID。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

名称类型必填说明insertEntries[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]是数据添加记录。updateEntries[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]是数据更新记录。deleteEntries[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]是数据删除记录。deviceIdstring是设备ID，此处为设备UUID。

#### Entry

存储在数据库中的键值对。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

名称类型必填说明keystring是键值。value[Value](#ZH-CN_TOPIC_0000002529284683__value)是值对象。

#### Value

存储在数据库中的值对象。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

名称类型必填说明type[ValueType](#ZH-CN_TOPIC_0000002529284683__value)是值类型。valueUint8Array | string | number | boolean是值。

#### ValueType

数据类型枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

名称值说明STRING0表示值类型为字符串。INTEGER1表示值类型为整数。FLOAT2表示值类型为浮点数。BYTE_ARRAY3表示值类型为字节数组。BOOLEAN4表示值类型为布尔值。DOUBLE5表示值类型为双浮点数。

#### SingleKVStore

单版本数据库，继承自[KVStore](#ZH-CN_TOPIC_0000002529284683__kvstore)数据库，提供查询数据和同步数据的方法。

单版本数据库，不对数据所属设备进行区分，不同设备使用相同键写入数据会互相覆盖。比如，可以使用单版本数据库实现个人日历、联系人数据在不同设备间的数据同步。

在调用SingleKVStore的方法前，需要先通过[getKVStore](#ZH-CN_TOPIC_0000002529284683__getkvstore)构建一个SingleKVStore实例。

#### get

get(key: string, callback: AsyncCallback<Uint8Array | string | boolean | number>): void

获取指定键的值，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keystring是要查询数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。callbackAsyncCallback<Uint8Array | string | boolean | number>是回调函数。返回获取查询的值。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, function (err,data) {
        if (err != undefined) {
            console.log("put err: " + JSON.stringify(err));
            return;
        }
        console.log("put success");
        kvStore.get(KEY_TEST_STRING_ELEMENT, function (err,data) {
            console.log("get success data: " + data);
        });
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```

#### get

get(key: string): Promise<Uint8Array | string | boolean | number>

获取指定键的值，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keystring是要查询数据的key，不能为空且长度不大于[MAX_KEY_LENGTH](#ZH-CN_TOPIC_0000002529284683__constants)。

**返回值：**

类型说明Promise<Uint8Array | string | boolean | number>Promise对象。返回获取查询的值。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-test-string';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((data) => {
        console.log("put success: " + JSON.stringify(data));
        kvStore.get(KEY_TEST_STRING_ELEMENT).then((data) => {
            console.log("get success data: " + data);
        }).catch((err) => {
            console.log("get err: " + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log("put err: " + JSON.stringify(err));
    });
}catch (e) {
    console.log("An unexpected error occurred. Error:" + e);
}
```

#### getEntries8+

getEntries(keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取匹配指定键前缀的所有键值对，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keyPrefixstring是表示要匹配的键前缀。callbackAsyncCallback<[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]>是回调函数。返回匹配指定前缀的键值对列表。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_number_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.INTEGER,
                value : 222
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        kvStore.getEntries('batch_test_number_key', function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries[0]: ' + JSON.stringify(entries[0]));
        });
    });
}catch(e) {
    console.log('PutBatch e ' + e);
}
```

#### getEntries8+

getEntries(keyPrefix: string): Promise<Entry[]>

获取匹配指定键前缀的所有键值对，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keyPrefixstring是表示要匹配的键前缀。

**返回值：**

类型说明Promise<[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]>Promise对象。返回匹配指定前缀的键值对列表。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + entries);
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        kvStore.getEntries('batch_test_string_key').then((entries) => {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries[0]: ' + JSON.stringify(entries[0]));
            console.log('entries[0].value: ' + JSON.stringify(entries[0].value));
            console.log('entries[0].value.value: ' + entries[0].value.value);
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('PutBatch e ' + e);
}
```

#### getEntries8+

getEntries(query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示要匹配的键前缀。callbackAsyncCallback<[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]>是回调函数。返回与指定Query对象匹配的键值对列表。

**示例：**

```ets
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getEntries(query, function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries[0]: ' + JSON.stringify(entries[0]));
        });
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}
```

#### getEntries8+

getEntries(query: Query): Promise<Entry[]>

获取与指定Query对象匹配的键值对列表，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。

**返回值：**

类型说明Promise<[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]>Promise对象。返回与指定Query对象匹配的键值对列表。

**示例：**

```ets
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getEntries(query).then((entries) => {
            console.log('getEntries success');
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('GetEntries putBatch fail ' + JSON.stringify(err))
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}
```

#### getResultSet8+

getResultSet(keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void

从KvStore数据库中获取具有指定前缀的结果集，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keyPrefixstring是表示要匹配的键前缀。callbackAsyncCallback<[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)>是回调函数。返回具有指定前缀的结果集。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('GetResultSet putBatch success');
        kvStore.getResultSet('batch_test_string_key', async function (err, result) {
            console.log('GetResultSet getResultSet succeed.');
            resultSet = result;
            kvStore.closeResultSet(resultSet, function (err, data) {
                console.log('GetResultSet closeResultSet success');
            })
        });
    });
}catch(e) {
    console.log('GetResultSet e ' + e);
}
```

#### getResultSet8+

getResultSet(keyPrefix: string): Promise<KvStoreResultSet>

从KVStore数据库中获取具有指定前缀的结果集，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明keyPrefixstring是表示要匹配的键前缀。

**返回值：**

类型说明Promise<[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)>Promise对象。返回具有指定前缀的结果集。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('PutBatch putBatch fail ' + JSON.stringify(err));
    });
    kvStore.getResultSet('batch_test_string_key').then((result) => {
        console.log('GetResult getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
    kvStore.closeResultSet(resultSet).then((err) => {
        console.log('GetResult closeResultSet success');
    }).catch((err) => {
        console.log('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResult e ' + e);
}
```

#### getResultSet8+

getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定Query对象匹配的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明queryQuery是表示查询对象。callbackAsyncCallback<[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)>是回调函数，获取与指定Query对象匹配的KvStoreResultSet对象。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getResultSet(query, async function (err, result) {
            console.log('getResultSet succeed.');
            resultSet = result;
        });
    });
} catch(e) {
    console.log('GetResultSet e ' + e);
}
```

#### getResultSet8+

getResultSet(query: Query): Promise<KvStoreResultSet>

获取与指定Query对象匹配的KvStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。

**返回值：**

类型说明Promise<[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)>Promise对象。获取与指定Query对象匹配的KvStoreResultSet对象。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch_test");
    kvStore.getResultSet(query).then((result) => {
        console.log(' getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSet e ' + e);
}
```

#### closeResultSet8+

closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void

关闭由[SingleKVStore.getResultSet](#ZH-CN_TOPIC_0000002529284683__getresultset8)返回的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明resultSet[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)是表示要关闭的KvStoreResultSet对象。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
try {
    let resultSet = null;
    kvStore.closeResultSet(resultSet, function (err, data) {
        if (err == undefined) {
            console.log('closeResultSet success');
        } else {
            console.log('closeResultSet fail');
        }
    });
}catch(e) {
    console.log('CloseResultSet e ' + e);
}
```

#### closeResultSet8+

closeResultSet(resultSet: KvStoreResultSet): Promise<void>

关闭由[SingleKVStore.getResultSet](#ZH-CN_TOPIC_0000002529284683__getresultset8)返回的KvStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明resultSet[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)是表示要关闭的KvStoreResultSet对象。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
try {
    let resultSet = null;
    kvStore.closeResultSet(resultSet).then(() => {
        console.log('closeResultSet success');
    }).catch((err) => {
        console.log('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('CloseResultSet e ' + e);
}
```

#### getResultSize8+

getResultSize(query: Query, callback: AsyncCallback<number>): void

获取与指定Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。callbackAsyncCallback<number>是回调函数。返回与指定Query对象匹配的结果数。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getResultSize(query, async function (err, resultSize) {
            console.log('getResultSet succeed.');
        });
    });
} catch(e) {
    console.log('GetResultSize e ' + e);
}
```

#### getResultSize8+

getResultSize(query: Query): Promise<number>

获取与指定Query对象匹配的结果数，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。

**返回值：**

类型说明Promise<number>Promise对象。获取与指定Query对象匹配的结果数。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch_test");
    kvStore.getResultSize(query).then((resultSize) => {
        console.log('getResultSet succeed.');
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSize e ' + e);
}
```

#### removeDeviceData8+

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

删除指定设备的数据，使用callback异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明deviceIdstring是表示要删除设备的名称。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async function (err,data) {
        console.log('put success');
        const deviceid = 'no_exist_device_id';
        kvStore.removeDeviceData(deviceid, async function (err,data) {
            if (err == undefined) {
                console.log('removeDeviceData success');
            } else {
                console.log('removeDeviceData fail');
                kvStore.get(KEY_TEST_STRING_ELEMENT, async function (err,data) {
                    console.log('RemoveDeviceData get success');
                });
            }
        });
    });
}catch(e) {
    console.log('RemoveDeviceData e ' + e);
}
```

#### removeDeviceData8+

removeDeviceData(deviceId: string): Promise<void>

删除指定设备的数据，使用Promise异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明deviceIdstring是表示要删除设备的名称。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((err) => {
        console.log('removeDeviceData put success');
    }).catch((err) => {
        console.log('put fail ' + JSON.stringify(err));
    });
    const deviceid = 'no_exist_device_id';
    kvStore.removeDeviceData(deviceid).then((err) => {
        console.log('removeDeviceData success');
    }).catch((err) => {
        console.log('removeDeviceData fail ' + JSON.stringify(err));
    });
    kvStore.get(KEY_TEST_STRING_ELEMENT).then((data) => {
        console.log('get success data:' + data);
    }).catch((err) => {
        console.log('RemoveDeviceData get fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('RemoveDeviceData e ' + e);
}
```

#### sync

sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void

在手动同步方式下，触发数据库同步。

其中deviceIds为DeviceInfo中的networkId，通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

**需要权限**： ohos.permission.DISTRIBUTED_DATASYNC。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明deviceIdsstring[]是同一组网环境下，需要同步的设备的networkId列表。mode[SyncMode](#ZH-CN_TOPIC_0000002529284683__syncmode)是同步模式。delayMsnumber否可选参数，允许延时时间，单位：ms（毫秒），默认为0。

**示例：**

```ets
import deviceManager from '@ohos.distributedHardware.deviceManager';

let devManager;
let kvStore;
const KEY_TEST_SYNC_ELEMENT = 'key_test_sync';
const VALUE_TEST_SYNC_ELEMENT = 'value-string-001';
// create deviceManager
deviceManager.createDeviceManager('bundleName', (err, value) => {
  if (!err) {
    devManager = value;
    let deviceIds = [];
    if (devManager != null) {
      var devices = devManager.getTrustedDeviceListSync();
      for (var i = 0; i < devices.length; i++) {
        deviceIds[i] = devices[i].networkId;
      }
    }
    try {
      kvStore.on('syncComplete', function (data) {
        console.log('Sync dataChange');
      });
      kvStore.put(KEY_TEST_SYNC_ELEMENT + 'testSync101', VALUE_TEST_SYNC_ELEMENT, function (err, data) {
        if (err != undefined) {
          console.log("put err: " + JSON.stringify(err));
          return;
        }
        console.log('Succeeded in putting data');
        const mode = distributedData.SyncMode.PULL_ONLY;
        kvStore.sync(deviceIds, mode, 1000);
      });
    } catch (e) {
      console.log('Sync e' + e);
    }
  }
});
```

#### on('dataChange')8+

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

订阅指定类型的数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是订阅的事件名，固定为'dataChange'，表示数据变更事件。type[SubscribeType](#ZH-CN_TOPIC_0000002529284683__subscribetype)是表示订阅的类型。listenerCallback<[ChangeNotification](#ZH-CN_TOPIC_0000002529284683__changenotification)>是回调函数。

**示例：**

```ets
let kvStore;
kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_LOCAL, function (data) {
    console.log("dataChange callback call data: " + JSON.stringify(data));
});
```

#### on('syncComplete')8+

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是订阅的事件名，固定为'syncComplete'，表示同步完成事件。syncCallbackCallback<Array<[string, number]>>是回调函数。用于向调用方发送同步结果的回调。

**示例：**

```ets
let kvStore;
const KEY_TEST_FLOAT_ELEMENT = 'key_test_float';
const VALUE_TEST_FLOAT_ELEMENT = 321.12;
try {
    kvStore.on('syncComplete', function (data) {
        console.log('syncComplete ' + data)
    });
    kvStore.put(KEY_TEST_FLOAT_ELEMENT, VALUE_TEST_FLOAT_ELEMENT).then((data) => {
        console.log('syncComplete put success');
    }).catch((error) => {
        console.log('syncComplete put fail ' + error);
    });
}catch(e) {
    console.log('syncComplete put e ' + e);
}
```

#### off('dataChange')8+

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是取消订阅的事件名，固定为'dataChange'，表示数据变更事件。listenerCallback<[ChangeNotification](#ZH-CN_TOPIC_0000002529284683__changenotification)>否取消订阅的函数。如不设置callback，则取消所有订阅的函数。

**示例：**

```ets
let kvStore;
class KvstoreModel {
    call(data) {
        console.log("dataChange: " + data);
    }
    subscribeDataChange() {
        if (kvStore != null) {
            kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
        }
    }
    unsubscribeDataChange() {
        if (kvStore != null) {
            kvStore.off('dataChange', this.call);
        }
    }
}
```

#### off('syncComplete')8+

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。syncCallbackCallback<Array<[string, number]>>否取消订阅的函数。如不设置callback，则取消所有订阅的函数。

**示例：**

```ets
let kvStore;
class KvstoreModel {
    call(data) {
        console.log("syncComplete: " + data);
    }
    subscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.on('syncComplete', this.call);
        }
    }
    unsubscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.off('syncComplete', this.call);
        }
    }
}
```

#### setSyncParam8+

setSyncParam(defaultAllowedDelayMs: number, callback: AsyncCallback<void>): void

设置数据库同步允许的默认延迟，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明defaultAllowedDelayMsnumber是表示数据库同步允许的默认延迟，以毫秒为单位。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
try {
    const defaultAllowedDelayMs = 500;
    kvStore.setSyncParam(defaultAllowedDelayMs, function (err,data) {
        console.log('SetSyncParam put success');
    });
}catch(e) {
    console.log('testSingleKvStoreSetSyncParam e ' + e);
}
```

#### setSyncParam8+

setSyncParam(defaultAllowedDelayMs: number): Promise<void>

设置数据库同步允许的默认延迟，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明defaultAllowedDelayMsnumber是表示数据库同步允许的默认延迟，以毫秒为单位。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
try {
    const defaultAllowedDelayMs = 500;
    kvStore.setSyncParam(defaultAllowedDelayMs).then((err) => {
        console.log('SetSyncParam put success');
    }).catch((err) => {
        console.log('SetSyncParam put fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('SetSyncParam e ' + e);
}
```

#### getSecurityLevel8+

getSecurityLevel(callback: AsyncCallback<SecurityLevel>): void

获取数据库的安全级别，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明callbackAsyncCallback<[SecurityLevel](#ZH-CN_TOPIC_0000002529284683__securitylevel)>是回调函数。返回数据库的安全级别。

**示例：**

```ets
let kvStore;
try {
    kvStore.getSecurityLevel(function (err,data) {
        console.log('getSecurityLevel success');
    });
}catch(e) {
    console.log('GetSecurityLevel e ' + e);
}
```

#### getSecurityLevel8+

getSecurityLevel(): Promise<SecurityLevel>

获取数据库的安全级别，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**返回值：**

类型说明Promise<[SecurityLevel](#ZH-CN_TOPIC_0000002529284683__securitylevel)>Promise对象。返回数据库的安全级别。

**示例：**

```ets
let kvStore;
try {
    kvStore.getSecurityLevel().then((data) => {
        console.log(' getSecurityLevel success');
    }).catch((err) => {
        console.log('getSecurityLevel fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetSecurityLevel e ' + e);
}
```

#### DeviceKVStore8+

设备协同数据库，继承自KVStore，提供查询数据和同步数据的方法。

设备协同数据库，以设备维度对数据进行区分，每台设备仅能写入和修改本设备的数据，其它设备的数据对其是只读的，无法修改其它设备的数据。

比如，可以使用设备协同数据库实现设备间的图片分享，可以查看其他设备的图片，但无法修改和删除其他设备的图片。

在调用DeviceKVStore的方法前，需要先通过[getKVStore](#ZH-CN_TOPIC_0000002529284683__getkvstore)构建一个DeviceKVStore实例。

#### get8+

get(deviceId: string, key: string, callback: AsyncCallback<boolean|string|number|Uint8Array>): void

获取与指定设备ID和key匹配的string值，使用callback异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是标识要查询其数据的设备。keystring是表示要查询key值的键。callbackAsyncCallback<boolean|string|number|Uint8Array>是回调函数，返回匹配给定条件的字符串值。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
try{
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async function (err,data) {
        console.log('put success');
        kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT, function (err,data) {
            console.log('get success');
        });
    })
}catch(e) {
    console.log('get e' + e);
}
```

#### get8+

get(deviceId: string, key: string): Promise<boolean|string|number|Uint8Array>

获取与指定设备ID和key匹配的string值，使用Promise异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是标识要查询其数据的设备。keystring是表示要查询key值的键。

**返回值：**

类型说明Promise<boolean|string|number|Uint8Array>Promise对象。返回匹配给定条件的字符串值。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string_2';
const VALUE_TEST_STRING_ELEMENT = 'value-string-002';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then(async (data) => {
        console.log(' put success');
        kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT).then((data) => {
            console.log('get success');
        }).catch((err) => {
            console.log('get fail ' + JSON.stringify(err));
        });
    }).catch((error) => {
        console.log('put error' + error);
    });
} catch (e) {
    console.log('Get e ' + e);
}
```

#### getEntries8+

getEntries(deviceId: string, keyPrefix: string, callback: AsyncCallback<Entry[]>): void

获取与指定设备ID和key前缀匹配的所有键值对，使用callback异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是标识要查询其数据的设备。keyPrefixstring是表示要匹配的键前缀。callbackAsyncCallback<[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]>是回调函数，返回满足给定条件的所有键值对的列表。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + entries);
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        kvStore.getEntries('localDeviceId', 'batch_test_string_key', function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries[0]: ' + JSON.stringify(entries[0]));
        });
    });
}catch(e) {
    console.log('PutBatch e ' + e);
}
```

#### getEntries8+

getEntries(deviceId: string, keyPrefix: string): Promise<Entry[]>

获取与指定设备ID和key前缀匹配的所有键值对，使用Promise异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是标识要查询其数据的设备。keyPrefixstring是表示要匹配的键前缀。

**返回值：**

类型说明Promise<[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]>Promise对象。返回匹配给定条件的所有键值对的列表。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + entries);
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        kvStore.getEntries('localDeviceId', 'batch_test_string_key').then((entries) => {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries[0]: ' + JSON.stringify(entries[0]));
            console.log('entries[0].value: ' + JSON.stringify(entries[0].value));
            console.log('entries[0].value.value: ' + entries[0].value.value);
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('PutBatch e ' + e);
}
```

#### getEntries8+

getEntries(query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定Query对象匹配的键值对列表，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。callbackAsyncCallback<[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]>是回调函数，返回与指定Query对象匹配的键值对列表。

**示例：**

```ets
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        query.deviceId('localDeviceId');
        kvStore.getEntries(query, function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries[0]: ' + JSON.stringify(entries[0]));
        });
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}
```

#### getEntries8+

getEntries(query: Query): Promise<Entry[]>

获取与指定Query对象匹配的键值对列表，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。

**返回值：**

类型说明Promise<[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]>Promise对象。返回与指定Query对象匹配的键值对列表。

**示例：**

```ets
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getEntries(query).then((entries) => {
            console.log('getEntries success');
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('GetEntries putBatch fail ' + JSON.stringify(err))
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}
```

#### getEntries8+

getEntries(deviceId: string, query: Query, callback: AsyncCallback<Entry[]>): void

获取与指定设备ID和Query对象匹配的键值对列表，使用callback异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是键值对所属的设备ID。query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。callbackAsyncCallback<[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]>是回调函数。返回与指定设备ID和Query对象匹配的键值对列表。

**示例：**

```ets
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries, async function (err,data) {
        console.log('putBatch success');
        var query = new distributedData.Query();
        query.deviceId('localDeviceId');
        query.prefixKey("batch_test");
        kvStore.getEntries('localDeviceId', query, function (err,entries) {
            console.log('getEntries success');
            console.log('entries.length: ' + entries.length);
            console.log('entries[0]: ' + JSON.stringify(entries[0]));
        })
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}
```

#### getEntries8+

getEntries(deviceId: string, query: Query): Promise<Entry[]>

获取与指定设备ID和Query对象匹配的键值对列表，使用Promise异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是键值对所属的设备ID。query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。

**返回值：**

类型说明Promise<[Entry](#ZH-CN_TOPIC_0000002529284683__entry)[]>Promise对象。返回与指定设备ID和Query对象匹配的键值对列表。

**示例：**

```ets
let kvStore;
try {
    var arr = new Uint8Array([21,31]);
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_bool_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.BYTE_ARRAY,
                value : arr
            }
        }
        entries.push(entry);
    }
    console.log('entries: ' + JSON.stringify(entries));
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
        var query = new distributedData.Query();
        query.deviceId('localDeviceId');
        query.prefixKey("batch_test");
        kvStore.getEntries('localDeviceId', query).then((entries) => {
            console.log('getEntries success');
        }).catch((err) => {
            console.log('getEntries fail ' + JSON.stringify(err));
        });
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
    console.log('GetEntries success');
}catch(e) {
    console.log('GetEntries e ' + e);
}
```

#### getResultSet8+

getResultSet(deviceId: string, keyPrefix: string, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定设备ID和key前缀匹配的KvStoreResultSet对象，使用callback异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是标识要查询其数据的设备。keyPrefixstring是表示要匹配的键前缀。callbackAsyncCallback<[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)>是回调函数。返回与指定设备ID和key前缀匹配的KvStoreResultSet对象。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('localDeviceId', 'batch_test_string_key', async function (err, result) {
        console.log('getResultSet succeed.');
        resultSet = result;
        kvStore.closeResultSet(resultSet, function (err, data) {
            console.log('closeResultSet success');
        })
    });
}catch(e) {
    console.log('GetResultSet e ' + e);
}
```

#### getResultSet8+

getResultSet(deviceId: string, keyPrefix: string): Promise<KvStoreResultSet>

获取与指定设备ID和key前缀匹配的KvStoreResultSet对象，使用Promise异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是标识要查询其数据的设备。keyPrefixstring是表示要匹配的键前缀。

**返回值：**

类型说明Promise<[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)>Promise对象。返回与指定设备ID和key前缀匹配的KvStoreResultSet对象。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    kvStore.getResultSet('localDeviceId', 'batch_test_string_key').then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
    kvStore.closeResultSet(resultSet).then((err) => {
        console.log('closeResultSet success');
    }).catch((err) => {
        console.log('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSet e ' + e);
}
```

#### getResultSet8+

getResultSet(query: Query, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定Query对象匹配的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。callbackAsyncCallback<[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)>是回调函数，返回与指定Query对象匹配的KvStoreResultSet对象。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        query.deviceId('localDeviceId');
        kvStore.getResultSet(query, async function (err, result) {
            console.log('getResultSet succeed.');
            resultSet = result;
            kvStore.closeResultSet(resultSet, function (err, data) {
                console.log('closeResultSet success');
            })
        });
    });
} catch(e) {
    console.log('GetResultSet e ' + e);
}
```

#### getResultSet8+

getResultSet(query: Query): Promise<KvStoreResultSet>

获取与指定Query对象匹配的KvStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。

**返回值：**

类型说明Promise<[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)>Promise对象。返回与指定Query对象匹配的KvStoreResultSet对象。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('putBatch fail ' + err);
    });
    const query = new distributedData.Query();
    query.deviceId('localDeviceId');
    query.prefixKey("batch_test");
    console.log("GetResultSet " + query.getSqlLike());
    kvStore.getResultSet(query).then((result) => {
        console.log('getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
    kvStore.closeResultSet(resultSet).then((err) => {
        console.log('closeResultSet success');
    }).catch((err) => {
        console.log('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSet e ' + e);
}
```

#### getResultSet8+

getResultSet(deviceId: string, query: Query, callback: AsyncCallback<KvStoreResultSet>): void

获取与指定设备ID和Query对象匹配的KvStoreResultSet对象，使用callback异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是KvStoreResultSet对象所属的设备ID。query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。callbackAsyncCallback<[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)>是回调函数。返回与指定设备ID和Query对象匹配的KvStoreResultSet对象。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getResultSet('localDeviceId', query, async function (err, result) {
            console.log('getResultSet succeed.');
            resultSet = result;
            kvStore.closeResultSet(resultSet, function (err, data) {
                console.log('closeResultSet success');
            })
        });
    });
} catch(e) {
    console.log('GetResultSet e ' + e);
}
```

#### getResultSet8+

getResultSet(deviceId: string, query: Query): Promise<KvStoreResultSet>

获取与指定设备ID和Query对象匹配的KvStoreResultSet对象，使用Promise异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是KvStoreResultSet对象所属的设备ID。query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。

**返回值：**

类型说明Promise<[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)>Promise对象。返回与指定设备ID和Query对象匹配的KvStoreResultSet对象。

**示例：**

```ets
let kvStore;
try {
    let resultSet;
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('GetResultSet putBatch success');
    }).catch((err) => {
        console.log('PutBatch putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch_test");
    kvStore.getResultSet('localDeviceId', query).then((result) => {
        console.log('GetResultSet getResultSet succeed.');
        resultSet = result;
    }).catch((err) => {
        console.log('GetResultSet getResultSet failed: ' + JSON.stringify(err));
    });
    query.deviceId('localDeviceId');
    console.log("GetResultSet " + query.getSqlLike());
    kvStore.closeResultSet(resultSet).then((err) => {
        console.log('GetResultSet closeResultSet success');
    }).catch((err) => {
        console.log('GetResultSet closeResultSet fail ' + JSON.stringify(err));
    });

}catch(e) {
    console.log('GetResultSet e ' + e);
}
```

#### closeResultSet8+

closeResultSet(resultSet: KvStoreResultSet, callback: AsyncCallback<void>): void

关闭由[DeviceKVStore.getResultSet](#ZH-CN_TOPIC_0000002529284683__getresultset8-4)返回的KvStoreResultSet对象，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明resultSet[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)是指示要关闭的KvStoreResultSet对象。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
try {
    console.log('CloseResultSet success');
    let resultSet = null;
    kvStore.closeResultSet(resultSet, function (err, data) {
        if (err == undefined) {
            console.log('closeResultSet success');
        } else {
            console.log('closeResultSet fail');
        }
    });
}catch(e) {
    console.log('CloseResultSet e ' + e);
}
```

#### closeResultSet8+

closeResultSet(resultSet: KvStoreResultSet): Promise<void>

关闭由[DeviceKVStore.getResultSet](#ZH-CN_TOPIC_0000002529284683__getresultset8-4)返回的KvStoreResultSet对象，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明resultSet[KvStoreResultSet](#ZH-CN_TOPIC_0000002529284683__kvstoreresultset8)是指示要关闭的KvStoreResultSet对象。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
try {
    console.log('CloseResultSet success');
    let resultSet = null;
    kvStore.closeResultSet(resultSet).then(() => {
        console.log('closeResultSet success');
    }).catch((err) => {
        console.log('closeResultSet fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('CloseResultSet e ' + e);
}
```

#### getResultSize8+

getResultSize(query: Query, callback: AsyncCallback<number>): void

获取与指定Query对象匹配的结果数，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。callbackAsyncCallback<number>是回调函数，返回与指定Query对象匹配的结果数。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        query.deviceId('localDeviceId');
        kvStore.getResultSize(query, async function (err, resultSize) {
            console.log('getResultSet succeed.');
        });
    });
} catch(e) {
    console.log('GetResultSize e ' + e);
}
```

#### getResultSize8+

getResultSize(query: Query): Promise<number>

获取与指定Query对象匹配的结果数，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。

**返回值：**

类型说明Promise<number>Promise对象。返回与指定Query对象匹配的结果数。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
    const query = new distributedData.Query();
    query.prefixKey("batch_test");
    query.deviceId('localDeviceId');
    kvStore.getResultSize(query).then((resultSize) => {
        console.log('getResultSet succeed.');
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSize e ' + e);
}
```

#### getResultSize8+

getResultSize(deviceId: string, query: Query, callback: AsyncCallback<number>): void;

获取与指定设备ID和Query对象匹配的结果数，使用callback异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是KvStoreResultSet对象所属的设备ID。query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。callbackAsyncCallback<number>是回调函数。返回与指定设备ID和Query对象匹配的结果数。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries, async function (err, data) {
        console.log('putBatch success');
        const query = new distributedData.Query();
        query.prefixKey("batch_test");
        kvStore.getResultSize('localDeviceId', query, async function (err, resultSize) {
            console.log('getResultSet succeed.');
        });
    });
} catch(e) {
    console.log('GetResultSize e ' + e);
}
```

#### getResultSize8+

getResultSize(deviceId: string, query: Query): Promise<number>

获取与指定设备ID和Query对象匹配的结果数，使用Promise异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是KvStoreResultSet对象所属的设备ID。query[Query](#ZH-CN_TOPIC_0000002529284683__query8)是表示查询对象。

**返回值：**

类型说明Promise<number>Promise对象。返回与指定设备ID和Query对象匹配的结果数。

**示例：**

```ets
let kvStore;
try {
    let entries = [];
    for (var i = 0; i < 10; i++) {
        var key = 'batch_test_string_key';
        var entry = {
            key : key + i,
            value : {
                type : distributedData.ValueType.STRING,
                value : 'batch_test_string_value'
            }
        }
        entries.push(entry);
    }
    kvStore.putBatch(entries).then(async (err) => {
        console.log('putBatch success');
    }).catch((err) => {
        console.log('putBatch fail ' + JSON.stringify(err));
    });
    var query = new distributedData.Query();
    query.prefixKey("batch_test");
    kvStore.getResultSize('localDeviceId', query).then((resultSize) => {
        console.log('getResultSet succeed.');
    }).catch((err) => {
        console.log('getResultSet failed: ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('GetResultSize e ' + e);
}
```

#### removeDeviceData8+

removeDeviceData(deviceId: string, callback: AsyncCallback<void>): void

从当前数据库中删除指定设备的数据，使用callback异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是标识要删除其数据的设备。callbackAsyncCallback<void>是回调函数。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT, async function (err,data) {
        console.log('RemoveDeviceData  put success');
        const deviceid = 'no_exist_device_id';
        kvStore.removeDeviceData(deviceid, async function (err,data) {
            if (err == undefined) {
                console.log('removeDeviceData success');
            } else {
                console.log('removeDeviceData fail');
                kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT, async function (err,data) {
                    console.log('RemoveDeviceData get success');
                });
            }
        });
    });
}catch(e) {
    console.log('RemoveDeviceData e ' + e);
}
```

#### removeDeviceData8+

removeDeviceData(deviceId: string): Promise<void>

从当前数据库中删除指定设备的数据，使用Promise异步回调。

其中deviceId通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

deviceId具体获取方式请参考[sync接口示例](#ZH-CN_TOPIC_0000002529284683__sync)。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.DistributedKVStore

**参数：**

参数名类型必填说明deviceIdstring是标识要删除其数据的设备。

**返回值：**

类型说明Promise<void>无返回结果的Promise对象。

**示例：**

```ets
let kvStore;
const KEY_TEST_STRING_ELEMENT = 'key_test_string';
const VALUE_TEST_STRING_ELEMENT = 'value-string-001';
try {
    kvStore.put(KEY_TEST_STRING_ELEMENT, VALUE_TEST_STRING_ELEMENT).then((err) => {
        console.log('RemoveDeviceData put success');
    }).catch((err) => {
        console.log('RemoveDeviceData put fail ' + JSON.stringify(err));
    });
    const deviceid = 'no_exist_device_id';
    kvStore.removeDeviceData(deviceid).then((err) => {
        console.log('removeDeviceData success');
    }).catch((err) => {
        console.log('removeDeviceData fail ' + JSON.stringify(err));
    });
    kvStore.get('localDeviceId', KEY_TEST_STRING_ELEMENT).then((data) => {
        console.log('RemoveDeviceData get success data:' + data);
    }).catch((err) => {
        console.log('RemoveDeviceData get fail ' + JSON.stringify(err));
    });
}catch(e) {
    console.log('RemoveDeviceData e ' + e);
}
```

#### sync8+

sync(deviceIds: string[], mode: SyncMode, delayMs?: number): void

在手动同步方式下，触发数据库同步。

其中deviceIds为DeviceInfo中的networkId，通过调用deviceManager.getTrustedDeviceListSync方法得到。deviceManager模块的接口均为系统接口，仅系统应用可用。

**需要权限**： ohos.permission.DISTRIBUTED_DATASYNC。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明deviceIdsstring[]是需要同步DeviceKVStore数据库的设备networkId列表。mode[SyncMode](#ZH-CN_TOPIC_0000002529284683__syncmode)是同步模式。delayMsnumber否可选参数，允许延时时间，单位：ms（毫秒），默认为0。

**示例：**

```ets
import deviceManager from '@ohos.distributedHardware.deviceManager';

let devManager;
let kvStore;
const KEY_TEST_SYNC_ELEMENT = 'key_test_sync';
const VALUE_TEST_SYNC_ELEMENT = 'value-string-001';
// create deviceManager
deviceManager.createDeviceManager('bundleName', (err, value) => {
  if (!err) {
    devManager = value;
    let deviceIds = [];
    if (devManager != null) {
      var devices = devManager.getTrustedDeviceListSync();
      for (var i = 0; i < devices.length; i++) {
        deviceIds[i] = devices[i].networkId;
      }
    }
    try {
      kvStore.on('syncComplete', function (data) {
        console.log('Sync dataChange');
      });
      kvStore.put(KEY_TEST_SYNC_ELEMENT + 'testSync101', VALUE_TEST_SYNC_ELEMENT, function (err, data) {
        if (err != undefined) {
          console.log("put err: " + JSON.stringify(err));
          return;
        }
        console.log('Succeeded in putting data');
        const mode = distributedData.SyncMode.PULL_ONLY;
        kvStore.sync(deviceIds, mode, 1000);
      });
    } catch (e) {
      console.log('Sync e' + e);
    }
  }
});
```

#### on('dataChange')8+

on(event: 'dataChange', type: SubscribeType, listener: Callback<ChangeNotification>): void

订阅指定类型的数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是订阅的事件名，固定为'dataChange'，表示数据变更事件。type[SubscribeType](#ZH-CN_TOPIC_0000002529284683__subscribetype)是表示订阅的类型。listenerCallback<[ChangeNotification](#ZH-CN_TOPIC_0000002529284683__changenotification)>是回调函数。

**示例：**

```ets
let kvStore;
kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_LOCAL, function (data) {
    console.log("dataChange callback call data: " + JSON.stringify(data));
});
```

#### on('syncComplete')8+

on(event: 'syncComplete', syncCallback: Callback<Array<[string, number]>>): void

订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是订阅的事件名，固定为'syncComplete'，表示同步完成事件。syncCallbackCallback<Array<[string, number]>>是回调函数。用于向调用方发送同步结果的回调。

**示例：**

```ets
let kvStore;
const KEY_TEST_FLOAT_ELEMENT = 'key_test_float';
const VALUE_TEST_FLOAT_ELEMENT = 321.12;
try {
    kvStore.on('syncComplete', function (data) {
        console.log('syncComplete ' + data)
    });
    kvStore.put(KEY_TEST_FLOAT_ELEMENT, VALUE_TEST_FLOAT_ELEMENT).then((data) => {
        console.log('syncComplete put success');
    }).catch((error) => {
        console.log('syncComplete put fail ' + error);
    });
}catch(e) {
    console.log('syncComplete put e ' + e);
}
```

#### off('dataChange')8+

off(event:'dataChange', listener?: Callback<ChangeNotification>): void

取消订阅数据变更通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是取消订阅的事件名，固定为'dataChange'，表示数据变更事件。listenerCallback<[ChangeNotification](#ZH-CN_TOPIC_0000002529284683__changenotification)>否取消订阅的函数。如不设置callback，则取消所有订阅的函数。

**示例：**

```ets
let kvStore;
class KvstoreModel {
    call(data) {
        console.log("dataChange: " + data);
    }
    subscribeDataChange() {
        if (kvStore != null) {
            kvStore.on('dataChange', distributedData.SubscribeType.SUBSCRIBE_TYPE_REMOTE, this.call);
        }
    }
    unsubscribeDataChange() {
        if (kvStore != null) {
            kvStore.off('dataChange', this.call);
        }
    }
}
```

#### off('syncComplete')8+

off(event: 'syncComplete', syncCallback?: Callback<Array<[string, number]>>): void

取消订阅同步完成事件回调通知。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

**参数：**

参数名类型必填说明eventstring是取消订阅的事件名，固定为'syncComplete'，表示同步完成事件。syncCallbackCallback<Array<[string, number]>>否取消订阅的函数。如不设置callback，则取消所有订阅的函数。

**示例：**

```ets
let kvStore;
class KvstoreModel {
    call(data) {
        console.log("syncComplete: " + data);
    }
    subscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.on('syncComplete', this.call);
        }
    }
    unsubscribeSyncComplete() {
        if (kvStore != null) {
            kvStore.off('syncComplete', this.call);
        }
    }
}
```

#### SyncMode

同步模式枚举。

**系统能力：** SystemCapability.DistributedDataManager.KVStore.Core

名称值说明PULL_ONLY0表示只能从远端拉取数据到本端。PUSH_ONLY1表示只能从本端推送数据到远端。PUSH_PULL2表示从本端推送数据到远端，然后从远端拉取数据到本端。