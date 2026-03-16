[]()[]()

# Functions

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### 导入模块

```ets
import { relationalStore } from '@kit.ArkData';
```

[]()[]()

#### relationalStore.getRdbStore

getRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<RdbStore>): void

创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用callback异步回调。

对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)。对应路径下已有数据库文件时，将打开已有数据库文件。

开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)，数据库创建后，禁止对该参数进行修改。

当前开库的加密类型本设备上创建该数据库时的加密类型结果非加密加密将数据库以加密方式打开。加密非加密将数据库以非加密方式打开。

getRdbStore目前不支持多线程并发操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](../graphics/Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](../graphics/Context (Stage模型的上下文基类).md)。

config[StoreConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)是与此RDB存储相关的数据库配置。callbackAsyncCallback<[RdbStore](../../types/interfaces/Interface (RdbStore).md)>是指定callback回调函数，返回RdbStore对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800010Failed to open or delete the database by an invalid database path.14800011Failed to open the database because it is corrupted.14801001The operation is supported in the stage model only.14801002Invalid data group ID.14800017StoreConfig is changed.14800020The secret key is corrupted or lost.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800022SQLite: Callback routine requested an abort.14800023SQLite: Access permission denied.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800030SQLite: Unable to open the database file.

**示例：**

FA模型示例：

```ets
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;
let context = featureAbility.getContext();

const STORE_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.getRdbStore(context, STORE_CONFIG, async (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
  if (err) {
    console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  console.info('Get RdbStore successfully.');
  store = rdbStore;
  // 成功获取到 rdbStore 后执行后续操作
});
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };

    relationalStore.getRdbStore(this.context, STORE_CONFIG, async (err: BusinessError, rdbStore: relationalStore.RdbStore) => {
      if (err) {
        console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
        return;
      }
      console.info('Get RdbStore successfully.');
      store = rdbStore;
      // 成功获取到 rdbStore 后执行后续操作
    });
  }
}
```

[]()[]()

#### relationalStore.getRdbStore

getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore>

创建或打开已有的关系型数据库，开发者可以根据自己的需求配置config参数，然后通过RdbStore调用相关接口执行数据操作。使用Promise异步回调。

对应沙箱路径下无数据库文件时，将创建数据库文件，文件创建位置详见[StoreConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)。对应路径下已有数据库文件时，将打开已有数据库文件。

开发者在创建数据库时，应谨慎配置是否进行数据库加密的参数[encrypt](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)，数据库创建后，禁止对该参数进行修改。

当前开库的加密类型本设备上创建该数据库时的加密类型结果非加密加密将数据库以加密方式打开。加密非加密将数据库以非加密方式打开。

getRdbStore目前不支持多线程并发操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](../graphics/Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](../graphics/Context (Stage模型的上下文基类).md)。

config[StoreConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)是与此RDB存储相关的数据库配置。

**返回值**：

类型说明Promise<[RdbStore](../../types/interfaces/Interface (RdbStore).md)>Promise对象。返回RdbStore对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800010Failed to open or delete the database by an invalid database path.14800011Failed to open the database because it is corrupted.14801001The operation is supported in the stage model only.14801002Invalid data group ID.14800017StoreConfig is changed.14800020The secret key is corrupted or lost.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800022SQLite: Callback routine requested an abort.14800023SQLite: Access permission denied.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800030SQLite: Unable to open the database file.

**示例：**

FA模型示例：

```ets
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;
let context = featureAbility.getContext();

const STORE_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.getRdbStore(context, STORE_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
  store = rdbStore;
  console.info('Get RdbStore successfully.');
}).catch((err: BusinessError) => {
  console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
});
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let store: relationalStore.RdbStore | undefined = undefined;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };

    relationalStore.getRdbStore(this.context, STORE_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
      store = rdbStore;
      console.info('Get RdbStore successfully.');
    }).catch((err: BusinessError) => {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    });
  }
}
```

[]()[]()

#### relationalStore.deleteRdbStore

deleteRdbStore(context: Context, name: string, callback: AsyncCallback<void>): void

删除数据库文件，使用callback异步回调。

删除成功后，建议将数据库对象置为null。建立数据库时，若在[StoreConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)中配置了自定义路径，则调用此接口进行删库无效，必须使用 [deleteRdbStore](#ZH-CN_TOPIC_0000002529284675__relationalstoredeleterdbstore10) 接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](../graphics/Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](../graphics/Context (Stage模型的上下文基类).md)。

namestring是数据库名称。callbackAsyncCallback<void>是指定callback回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800010Failed to open or delete the database by an invalid database path.

**示例：**

FA模型示例：

```ets
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

relationalStore.deleteRdbStore(context, "RdbTest.db", (err: BusinessError) => {
  if (err) {
    console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
  // 及时将相关变量置空以释放资源。
  console.info('Delete RdbStore successfully.');
});
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    relationalStore.deleteRdbStore(this.context, "RdbTest.db", (err: BusinessError) => {
      if (err) {
        console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
        return;
      }
      // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
      // 及时将相关变量置空以释放资源。
      console.info('Delete RdbStore successfully.');
    });
  }
}
```

[]()[]()

#### relationalStore.deleteRdbStore

deleteRdbStore(context: Context, name: string): Promise<void>

使用指定的数据库文件配置删除数据库，使用Promise异步回调。

删除成功后，建议将数据库对象置为null。建立数据库时，若在[StoreConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)中配置了自定义路径，则调用此接口进行删库无效，必须使用 [deleteRdbStore](#ZH-CN_TOPIC_0000002529284675__relationalstoredeleterdbstore10-1) 接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](../graphics/Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](../graphics/Context (Stage模型的上下文基类).md)。

namestring是数据库名称。

**返回值**：

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800010Failed to open or delete the database by an invalid database path.

**示例：**

FA模型示例：

```ets
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

relationalStore.deleteRdbStore(context, "RdbTest.db").then(() => {
  // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
  // 及时将相关变量置空以释放资源。
  console.info('Delete RdbStore successfully.');
}).catch((err: BusinessError) => {
  console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
});
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    relationalStore.deleteRdbStore(this.context, "RdbTest.db").then(() => {
      // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
      // 及时将相关变量置空以释放资源。
      console.info('Delete RdbStore successfully.');
    }).catch((err: BusinessError) => {
      console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
    });
  }
}
```

[]()[]()

#### relationalStore.deleteRdbStore10+

deleteRdbStore(context: Context, config: StoreConfig, callback: AsyncCallback<void>): void

使用指定的数据库文件配置删除数据库，使用callback异步回调。

删除成功后，建议将数据库对象置为null。若数据库文件处于公共沙箱目录下，则删除数据库时必须使用该接口，当存在多个进程操作同一个数据库的情况，建议向其他进程发送数据库删除通知使其感知并处理。建立数据库时，若在[StoreConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)中配置了自定义路径，则必须调用此接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](../graphics/Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](../graphics/Context (Stage模型的上下文基类).md)。

config[StoreConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)是与此RDB存储相关的数据库配置。callbackAsyncCallback<void>是指定callback回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800010Failed to open or delete the database by an invalid database path.14801001The operation is supported in the stage model only.14801002Invalid data group ID.

**示例：**

FA模型示例：

```ets
import { featureAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

const STORE_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.deleteRdbStore(context, STORE_CONFIG, (err: BusinessError) => {
  if (err) {
    console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
    return;
  }
  // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
  // 及时将相关变量置空以释放资源。
  console.info('Delete RdbStore successfully.');
});
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };
    relationalStore.deleteRdbStore(this.context, STORE_CONFIG, (err: BusinessError) => {
      if (err) {
        console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
        return;
      }
      // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
      // 及时将相关变量置空以释放资源。
      console.info('Delete RdbStore successfully.');
    });
  }
}
```

[]()[]()

#### relationalStore.deleteRdbStore10+

deleteRdbStore(context: Context, config: StoreConfig): Promise<void>

使用指定的数据库文件配置删除数据库，使用Promise异步回调。

删除成功后，建议将数据库对象置为null。若数据库文件处于公共沙箱目录下，则删除数据库时必须使用该接口，当存在多个进程操作同一个数据库的情况，建议向其他进程发送数据库删除通知使其感知并处理。建立数据库时，若在[StoreConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)中配置了自定义路径，则必须调用此接口进行删库。

当使用向量数据库时，在调用deleteRdbStore接口前，应当确保向量数据库已打开的RdbStore和ResultSet均已成功关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数**

参数名类型必填说明contextContext是

应用的上下文。

FA模型的应用Context定义见[Context](../graphics/Context (FA模型的上下文基类).md)。

Stage模型的应用Context定义见[Context](../graphics/Context (Stage模型的上下文基类).md)。

config[StoreConfig](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__storeconfig)是与此RDB存储相关的数据库配置。

**返回值**：

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported.14800000Inner error.14800010Failed to open or delete the database by an invalid database path.14801001The operation is supported in the stage model only.14801002Invalid data group ID.

**示例：**

FA模型示例：

```ets
import { featureAbility } from "@kit.AbilityKit";
import { BusinessError } from '@kit.BasicServicesKit';

let context = featureAbility.getContext();

const STORE_CONFIG: relationalStore.StoreConfig = {
  name: "RdbTest.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.deleteRdbStore(context, STORE_CONFIG).then(() => {
  // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
  // 及时将相关变量置空以释放资源。
  console.info('Delete RdbStore successfully.');
}).catch((err: BusinessError) => {
  console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
});
```

Stage模型示例：

```ets
import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };
    relationalStore.deleteRdbStore(this.context, STORE_CONFIG).then(() => {
      // 数据库删除成功后，已初始化的RdbStore实例将无法继续使用。
      // 及时将相关变量置空以释放资源。
      console.info('Delete RdbStore successfully.');
    }).catch((err: BusinessError) => {
      console.error(`Delete RdbStore failed, code is ${err.code},message is ${err.message}`);
    });
  }
}
```

[]()[]()

#### relationalStore.isVectorSupported18+

isVectorSupported(): boolean

判断系统是否提供向量数据库能力。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

类型说明boolean系统具备向量数据库能力时返回true，否则返回false。

**示例：**

```ets
import { contextConstant, UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { relationalStore } from '@kit.ArkData';

let store: relationalStore.RdbStore | undefined = undefined;
export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    let supported = relationalStore.isVectorSupported();
    if (supported) {
      // 支持向量数据库
      console.info("Vector database supported on current platform.");
      const STORE_CONFIG: relationalStore.StoreConfig = {
        name: "VectorTest.db",
        securityLevel: relationalStore.SecurityLevel.S3,
        vector: true
      };
      try {
        const context = this.context.getApplicationContext().createAreaModeContext(contextConstant.AreaMode.EL3);
        const rdbStore = await relationalStore.getRdbStore(context, STORE_CONFIG);
        console.info('Get RdbStore successfully.');
        store = rdbStore;
        // 成功获取到 rdbStore 后执行后续操作
      } catch (error) {
        const err = error as BusinessError;
        console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
      }
    } else {
      console.info("Vector database not supported on current platform.");
    }
  }
}
```

[]()[]()

#### relationalStore.isTokenizerSupported18+

isTokenizerSupported(tokenizer: Tokenizer): boolean

判断当前平台是否支持传入的分词器，此为同步接口。

如果当前平台支持传入的分词器时，此接口返回值为true；反之，返回值为false。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明tokenizer[Tokenizer](Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__tokenizer17)是需要被判断是否支持的分词器。

**返回值：**

类型说明booleantrue表示当前平台支持当前传入的分词器，false表示当前平台不支持当前传入的分词器。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.

**示例：**

```ets
let customType = relationalStore.Tokenizer.CUSTOM_TOKENIZER;
let customTypeSupported = relationalStore.isTokenizerSupported(customType);
console.info("custom tokenizer supported on current platform: " + customTypeSupported);
```

[]()[]()

#### relationalStore.getInsertSqlInfo20+

getInsertSqlInfo(table: string, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo

获取用于插入数据的SQL语句，此为同步接口。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明tablestring是要写入数据的数据库表名。values[ValuesBucket](Types (arkts-apis-data-relationalstore-t).md#ZH-CN_TOPIC_0000002497444708__valuesbucket)是要写入数据库中数据的字段信息以及对应的值信息。conflict[ConflictResolution](Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)否指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON_CONFLICT_NONE。

**返回值：**

类型说明[SqlInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__sqlinfo20)SqlInfo对象，其中sql为返回的sql语句，args为执行SQL中的参数信息。

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**14800001Invalid arguments. Possible causes: 1. Parameter is out of valid range.

**示例：**

```ets
const bucket: relationalStore.ValuesBucket = {
  name: "Logitech",
  age: 18,
  sex: "man",
  desc: "asserter"
};
const sqlInfo: relationalStore.SqlInfo = relationalStore.getInsertSqlInfo(
  "USER",
  bucket,
  relationalStore.ConflictResolution.ON_CONFLICT_NONE
);
```

[]()[]()

#### relationalStore.getUpdateSqlInfo20+

getUpdateSqlInfo(predicates: RdbPredicates, values: ValuesBucket, conflict?: ConflictResolution): SqlInfo

获取用于更新数据的SQL语句，此为同步接口。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明predicates[RdbPredicates](../../types/classes/Class (RdbPredicates).md)是与指定字段匹配的谓词。values[ValuesBucket](Types (arkts-apis-data-relationalstore-t).md#ZH-CN_TOPIC_0000002497444708__valuesbucket)是要写入数据库中数据的字段信息以及对应的值信息。conflict[ConflictResolution](Enums (arkts-apis-data-relationalstore-e).md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)否指定冲突解决模式。 默认值是relationalStore.ConflictResolution.ON_CONFLICT_NONE。

**返回值：**

类型说明[SqlInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__sqlinfo20)SqlInfo对象，其中sql为返回的sql语句，args为执行SQL中的参数信息。

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**14800001Invalid arguments. Possible causes: 1. Parameter is out of valid range.

**示例：**

```ets
const bucket: relationalStore.ValuesBucket = {
  name: "Logitech",
  age: 18,
  sex: "man",
  desc: "asserter"
};
const predicates = new relationalStore.RdbPredicates("users");
const sqlInfo: relationalStore.SqlInfo = relationalStore.getUpdateSqlInfo(
  predicates,
  bucket,
  relationalStore.ConflictResolution.ON_CONFLICT_NONE
);
```

[]()[]()

#### relationalStore.getDeleteSqlInfo20+

getDeleteSqlInfo(predicates: RdbPredicates): SqlInfo

获取用于删除数据的SQL语句，此为同步接口。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明predicates[RdbPredicates](../../types/classes/Class (RdbPredicates).md)是与指定字段匹配的谓词。

**返回值：**

类型说明[SqlInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__sqlinfo20)SqlInfo对象，其中sql为返回的sql语句，args为执行SQL中的参数信息。

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**14800001Invalid arguments. Possible causes: 1. Parameter is out of valid range.

**示例：**

```ets
const predicates = new relationalStore.RdbPredicates("users");
predicates.equalTo("tableName", "a");
predicates.notEqualTo("age", 18);
const sqlInfo: relationalStore.SqlInfo = relationalStore.getDeleteSqlInfo(predicates);
```

[]()[]()

#### relationalStore.getQuerySqlInfo20+

getQuerySqlInfo(predicates: RdbPredicates, columns?: Array<string>): SqlInfo

获取用于查询数据的SQL语句，此为同步接口。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明predicates[RdbPredicates](../../types/classes/Class (RdbPredicates).md)是与指定字段匹配的谓词。columnsArray<string>否要查询的列；如果不指定此参数，则查询所有列。

**返回值：**

类型说明[SqlInfo](../../types/interfaces/Interfaces (其他) (arkts-apis-data-relationalstore-i).md#ZH-CN_TOPIC_0000002529284677__sqlinfo20)SqlInfo对象，其中sql为返回的sql语句，args为执行SQL中的参数信息。

**错误码：**

以下错误码的详细介绍请参见[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**14800001Invalid arguments. Possible causes: 1. Parameter is out of valid range.

**示例：**

```ets
const predicates = new relationalStore.RdbPredicates("users");
predicates.notEqualTo("age", 18);
predicates.equalTo("name", "zhangsan");
const sqlInfo: relationalStore.SqlInfo = relationalStore.getQuerySqlInfo(predicates);
```