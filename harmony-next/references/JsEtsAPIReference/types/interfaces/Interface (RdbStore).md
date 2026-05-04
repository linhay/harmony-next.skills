# Interface (RdbStore)

提供管理关系数据库（RDB）方法的接口。

在使用以下API前，请先通过[getRdbStore](Functions.md#ZH-CN_TOPIC_0000002522240630__relationalstoregetrdbstore-1)方法获取RdbStore实例，并使用该实例调用对应接口方法。

在此基础上，建议优先使用[execute](Interface (RdbStore).md#ZH-CN_TOPIC_0000002553200595__execute12)方法完成数据库表结构和初始数据的初始化，以确保相关接口调用的前置条件已满足。


本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { relationalStore } from '@kit.ArkData';
```

#### 属性

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| version10+ | number | 否 | 否 | 设置和获取数据库版本，值为大于0的正整数。 读取和设置version属性会占用数据库连接，避免对该属性进行频繁操作。 使用临时变量保存读取到的version值，在数据库变更完成后将其赋值给RdbStore实例的version属性。数据库升级时变更version属性的场景，请参考开发指南示例代码。 |
| rebuilt12+ | [RebuildType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__rebuildtype12) | 是 | 否 | 用于获取数据库是否进行过重建或修复。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码]([通用错误码](../../errors/通用错误码.md).md)和[关系型数据库错误码]([关系型数据库错误码](../../errors/关系型数据库错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

示例代码中this.context定义见Stage模型的应用[Context](Context (Stage模型的上下文基类).md)。

```ets
// 设置数据库版本
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let store: relationalStore.RdbStore | undefined = undefined;

class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: "RdbTest.db",
      securityLevel: relationalStore.SecurityLevel.S3
    };
    const SQL_CREATE_TABLE = 'CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, IDENTITY UNLIMITED INT, ASSETDATA ASSET, ASSETSDATA ASSETS, FLOATARRAY floatvector(128))';
    relationalStore.getRdbStore(this.context, STORE_CONFIG).then(async (rdbStore: relationalStore.RdbStore) => {
      store = rdbStore;
      await (store as relationalStore.RdbStore).executeSql(SQL_CREATE_TABLE);
      console.info('Get RdbStore successfully.');

      // 设置数据库版本
      if (store != undefined) {
        (store as relationalStore.RdbStore).version = 3;
        // 获取数据库版本
        console.info(`RdbStore version is ${store.version}`);
        // 获取数据库是否重建
        console.info(`RdbStore rebuilt is ${store.rebuilt}`);
      }
    }).catch((err: BusinessError) => {
      console.error(`Get RdbStore failed, code is ${err.code}, message is ${err.message}`);
    });
  }
```

#### insert

insert(table: string, values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), callback: AsyncCallback<number>):void

向目标表中插入一行数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

if (store != undefined) {
  (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1, (err: BusinessError, rowId: number) => {
    if (err) {
      console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info(`Insert is successful, rowId = ${rowId}`);
  });
}
```

#### insert10+

insert(table: string, values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), conflict: ConflictResolution, callback: AsyncCallback<number>):void

向目标表中插入一行数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 是 | 指定冲突解决模式。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

if (store != undefined) {
  (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE,
    (err: BusinessError, rowId: number) => {
      if (err) {
        console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
        return;
      }
      console.info(`Insert is successful, rowId = ${rowId}`);
    });
}
```

#### insert

insert(table: string, values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)):Promise<number>

向目标表中插入一行数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | 表示要插入到表中的数据行。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

if (store != undefined) {
  (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1).then((rowId: number) => {
    console.info(`Insert is successful, rowId = ${rowId}`);
  }).catch((err: BusinessError) => {
    console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### insert10+

insert(table: string, values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), conflict: ConflictResolution):Promise<number>

向目标表中插入一行数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 是 | 指定冲突解决模式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

if (store != undefined) {
  (store as relationalStore.RdbStore).insert("EMPLOYEE", valueBucket1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE).then((rowId: number) => {
    console.info(`Insert is successful, rowId = ${rowId}`);
  }).catch((err: BusinessError) => {
    console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### insertSync12+

insertSync(table: string, values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), conflict?: ConflictResolution):number

向目标表中插入一行数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | 表示要插入到表中的数据行。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 否 | 指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON_CONFLICT_NONE。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

if (store != undefined) {
  try {
    let rowId: number = (store as relationalStore.RdbStore).insertSync("EMPLOYEE", valueBucket1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
    console.info(`Insert is successful, rowId = ${rowId}`);
  } catch (err) {
    console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
}
```

#### insertSync12+

insertSync(table: string, values: sendableRelationalStore.[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), conflict?: ConflictResolution):number

传入Sendable数据，向目标表中插入一行数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | sendableRelationalStore.[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | 表示要插入到表中的可跨线程传递数据。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 否 | 指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON_CONFLICT_NONE。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 如果操作成功，返回行ID；否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { sendableRelationalStore } from '@kit.ArkData';

const valuesBucket: relationalStore.ValuesBucket = {
  "NAME": 'hangman',
  "AGE": 18,
  "SALARY": 100.5,
  "CODES": new Uint8Array([1, 2, 3])
};
const sendableValuesBucket = sendableRelationalStore.toSendableValuesBucket(valuesBucket);

if (store != undefined) {
  try {
    let rowId: number = (store as relationalStore.RdbStore).insertSync("EMPLOYEE", sendableValuesBucket, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
    console.info(`Insert is successful, rowId = ${rowId}`);
  } catch (err) {
    console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
}
```

#### batchInsert

batchInsert(table: string, values: Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>, callback: AsyncCallback<number>):void

向目标表中插入一组数据，使用callback异步回调。

接口报错，表示插入数据失败；接口没有报错但返回值为-1时，也表示插入数据失败。

按每批32766个参数，分批以[ConflictResolution.ON_CONFLICT_REPLACE](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

从API version 20开始，支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。如果操作成功，返回插入的数据个数，否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array([6, 7, 8, 9, 10]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array([11, 12, 13, 14, 15]);

const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  'NAME': value5,
  'AGE': value6,
  'SALARY': value7,
  'CODES': value8
};
const valueBucket3: relationalStore.ValuesBucket = {
  'NAME': value9,
  'AGE': value10,
  'SALARY': value11,
  'CODES': value12
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
if (store != undefined) {
  (store as relationalStore.RdbStore).batchInsert("EMPLOYEE", valueBuckets, (err, insertNum) => {
    if (err || insertNum == -1) {
      console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
  })
}
```

#### batchInsert

batchInsert(table: string, values: Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>):Promise<number>

向目标表中插入一组数据，使用Promise异步回调。

接口报错，表示插入数据失败；接口没有报错但返回值为-1时，也表示插入数据失败。

按每批32766个参数，分批以[ConflictResolution.ON_CONFLICT_REPLACE](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

从API version 20开始，该接口支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。如果操作成功，返回插入的数据个数，否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

关系型数据库：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array([6, 7, 8, 9, 10]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array([11, 12, 13, 14, 15]);

const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  'NAME': value5,
  'AGE': value6,
  'SALARY': value7,
  'CODES': value8
};
const valueBucket3: relationalStore.ValuesBucket = {
  'NAME': value9,
  'AGE': value10,
  'SALARY': value11,
  'CODES': value12
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
if (store != undefined) {
  (store as relationalStore.RdbStore).batchInsert("EMPLOYEE", valueBuckets).then((insertNum: number) => {
    if (insertNum == -1) {
      console.error(`batchInsert is failed`);
      return;
    }
    console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
  }).catch((err: BusinessError) => {
    console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
  })
}
```

向量数据库：

```ets
let createSql = "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, data1 floatvector(2));";
await store!.execute(createSql, 0, undefined);  // 创建关系表，第二个参数0表示不开启显示事务，第三个参数undefined表示sql未使用绑定参数化
let floatVector = Float32Array.from([1.2, 2.3]);
let valueBucketArray = new Array<relationalStore.ValuesBucket>();
for (let i = 0; i < 100; i++) { // 构造一个BucketArray用于写入
  const row : relationalStore.ValuesBucket = {
    "id" : i,
    "data1" : floatVector,
  }
  valueBucketArray.push(row);
}
await store!.batchInsert("test", valueBucketArray); // 执行批量写入
```

#### batchInsertSync12+

batchInsertSync(table: string, values: Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>):number

向目标表中插入一组数据。

接口报错，表示插入数据失败；接口没有报错但返回值为-1时，也表示插入数据失败。

按每批32766个参数，分批以[ConflictResolution.ON_CONFLICT_REPLACE](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)策略写入，参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小，中途失败则立即返回。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 如果操作成功，返回插入的数据个数，否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array([6, 7, 8, 9, 10]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array([11, 12, 13, 14, 15]);

const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  'NAME': value5,
  'AGE': value6,
  'SALARY': value7,
  'CODES': value8
};
const valueBucket3: relationalStore.ValuesBucket = {
  'NAME': value9,
  'AGE': value10,
  'SALARY': value11,
  'CODES': value12
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
if (store != undefined) {
  try {
    let insertNum: number = (store as relationalStore.RdbStore).batchInsertSync("EMPLOYEE", valueBuckets);
    if (insertNum == -1) {
      console.error(`batchInsertSync is failed`);
      return;
    }
    console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
  } catch (err) {
    console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
  }
```

#### batchInsertWith[ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)18+

batchInsertWithConflictResolution(table: string, values: Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>, conflict: ConflictResolution): Promise<number>

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)。使用Promise异步回调。

单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 是 | 指定冲突解决模式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。如果操作成功，返回插入的数据个数，否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array([6, 7, 8, 9, 10]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array([11, 12, 13, 14, 15]);

const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  'NAME': value5,
  'AGE': value6,
  'SALARY': value7,
  'CODES': value8
};
const valueBucket3: relationalStore.ValuesBucket = {
  'NAME': value9,
  'AGE': value10,
  'SALARY': value11,
  'CODES': value12
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
if (store != undefined) {
  (store as relationalStore.RdbStore).batchInsertWithConflictResolution("EMPLOYEE", valueBuckets, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE).then((insertNum: number) => {
    console.info(`batchInsert is successful, insertNum = ${insertNum}`);
  }).catch((err: BusinessError) => {
    console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### batchInsertWith[ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)Sync18+

batchInsertWithConflictResolutionSync(table: string, values: Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>, conflict: ConflictResolution): number

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)。

单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定的目标表名。 |
| values | Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)> | 是 | 表示要插入到表中的一组数据。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 是 | 指定冲突解决模式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 如果操作成功，返回插入的数据个数，否则返回-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);
let value5 = "Jack";
let value6 = 19;
let value7 = 101.5;
let value8 = new Uint8Array([6, 7, 8, 9, 10]);
let value9 = "Tom";
let value10 = 20;
let value11 = 102.5;
let value12 = new Uint8Array([11, 12, 13, 14, 15]);

const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  'NAME': value5,
  'AGE': value6,
  'SALARY': value7,
  'CODES': value8
};
const valueBucket3: relationalStore.ValuesBucket = {
  'NAME': value9,
  'AGE': value10,
  'SALARY': value11,
  'CODES': value12
};

let valueBuckets = new Array(valueBucket1, valueBucket2, valueBucket3);
if (store != undefined) {
  try {
    let insertNum: number = (store as relationalStore.RdbStore).batchInsertWithConflictResolutionSync("EMPLOYEE", valueBuckets, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
    console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
  } catch (err) {
    console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
  }
```

**batchInsertWithReturning23+**

batchInsertWithReturning(table: string, values: Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)，返回[Result](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__result23)。使用Promise异步回调。

单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段总数。

例如：插入数据的所有字段总数为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

模型约束： 此接口仅在Stage模型下可用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 要插入的目标表名。注意：正确的表名不应包含空格、逗号和星号，不能以点开头和结尾等，否则会抛出参数错误。 |
| values | Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)> | 是 | 要插入到表中的一组数据。注意：空数组、含有重复资产数据会抛出参数错误。 |
| config | ReturningConfig | 是 | 指定返回值的配置信息。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 否 | 指定冲突解决模式。默认为ON_CONFLICT_NONE。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Result> | Promise对象。如果操作成功，返回受影响的数据集。 |

错误码：

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

示例：

```ets
async function batchInsertWithReturningExample(rdbStore: relationalStore.RdbStore)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 20 };
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  const valueBuckets = new Array(valueBucket1, valueBucket2);
  try {
    let results = await rdbStore.batchInsertWithReturning("EMPLOYEE", valueBuckets, config);
    console.info(`batchInsertWithReturningExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`batchInsertWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`batchInsertWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
  }
```

**batchInsertWithReturningSync23+**

batchInsertWithReturningSync(table: string, values: Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>, config: ReturningConfig, conflict?: ConflictResolution): Result

向目标表中插入一组数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)，返回[Result](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__result23)。

单次插入参数的最大数量限制为32766，超出上限会返回14800001错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。

单条字符串类型字段最大支持写入8MB，超出部分将被截断，仅保留前8MB数据，若需存储超过8MB的内容，建议使用blob类型。

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

模型约束： 此接口仅在Stage模型下可用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 要插入的目标表名。注意：正确的表名不应包含空格、逗号和星号，不能以点开头和结尾等，否则会抛出参数错误。 |
| values | Array<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)> | 是 | 表示要插入到表中的一组数据。注意：空数组、含有重复资产数据会抛出参数错误。 |
| config | ReturningConfig | 是 | 指定返回值的配置信息。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 否 | 指定冲突解决模式。默认为ON_CONFLICT_NONE。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Result | 如果操作成功，返回受影响的数据集。 |

错误码：

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

示例：

```ets
function batchInsertWithReturningSyncExample(rdbStore: relationalStore.RdbStore)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 20 };
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  const valueBuckets = new Array(valueBucket1, valueBucket2);
  try {
    let results = rdbStore.batchInsertWithReturningSync("EMPLOYEE", valueBuckets, config);
    console.info(`batchInsertWithReturningSyncExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`batchInsertWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`batchInsertWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
}
```

#### update

update(values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), predicates: RdbPredicates, callback: AsyncCallback<number>):void

根据RdbPredicates的指定实例对象更新数据库中的数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的更新条件。 |
| callback | AsyncCallback<number> | 是 | 指定的callback回调方法。返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let value1 = "Rose";
let value2 = 22;
let value3 = 200.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).update(valueBucket1, predicates, (err, rows) => {
    if (err) {
      console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info(`Updated row count: ${rows}`);
  });
}
```

#### update10+

update(values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), predicates: RdbPredicates, conflict: ConflictResolution, callback: AsyncCallback<number>):void

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的更新条件。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 是 | 指定冲突解决模式。 |
| callback | AsyncCallback<number> | 是 | 指定的callback回调方法。返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let value1 = "Rose";
let value2 = 22;
let value3 = 200.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).update(valueBucket1, predicates, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE, (err, rows) => {
    if (err) {
      console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info(`Updated row count: ${rows}`);
  });
}
```

#### update

update(values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), predicates: RdbPredicates):Promise<number>

根据RdbPredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的更新条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 指定的Promise回调方法。返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Rose";
let value2 = 22;
let value3 = 200.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).update(valueBucket1, predicates).then(async (rows: number) => {
    console.info(`Updated row count: ${rows}`);
  }).catch((err: BusinessError) => {
    console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### update10+

update(values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), predicates: RdbPredicates, conflict: ConflictResolution):Promise<number>

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的更新条件。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 是 | 指定冲突解决模式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 指定的Promise回调方法。返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Rose";
let value2 = 22;
let value3 = 200.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).update(valueBucket1, predicates, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE).then(async (rows: number) => {
    console.info(`Updated row count: ${rows}`);
  }).catch((err: BusinessError) => {
    console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### updateSync12+

updateSync(values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), predicates: RdbPredicates, conflict?: ConflictResolution):number

根据RdbPredicates的指定实例对象更新数据库中的数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](#ZH-CN_TOPIC_0000002553200595__query)或[querySql](#ZH-CN_TOPIC_0000002553200595__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的更新条件。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 否 | 指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON_CONFLICT_NONE。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 返回受影响的行数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let value1 = "Rose";
let value2 = 22;
let value3 = 200.5;
let value4 = new Uint8Array([1, 2, 3, 4, 5]);

// 以下三种方式可用
const valueBucket1: relationalStore.ValuesBucket = {
  'NAME': value1,
  'AGE': value2,
  'SALARY': value3,
  'CODES': value4
};
const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value1,
  AGE: value2,
  SALARY: value3,
  CODES: value4
};
const valueBucket3: relationalStore.ValuesBucket = {
  "NAME": value1,
  "AGE": value2,
  "SALARY": value3,
  "CODES": value4
};

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  try {
    let rows: number = (store as relationalStore.RdbStore).updateSync(valueBucket1, predicates, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
    console.info(`Updated row count: ${rows}`);
  } catch (err) {
    console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
  }
```

**updateWithReturning23+**

updateWithReturning(values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Promise<Result>

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)，返回[Result](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__result23)，使用Promise异步回调。

conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

模型约束： 此接口仅在Stage模型下可用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的更新条件。 |
| config | ReturningConfig | 是 | 指定返回值的配置信息。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 否 | 指定冲突解决模式。默认为ON_CONFLICT_NONE。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Result> | Promise对象。如果操作成功，返回受影响的数据集。 |

错误码：

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

示例：

```ets
async function updateWithReturningExample(rdbStore: relationalStore.RdbStore)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 18 };
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  predicates.equalTo('NAME', 'lisi');
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  try {
    rdbStore.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
    valueBucket1['NAME'] = "zhangsan";
    valueBucket1['AGE'] = 18;
    let results = await rdbStore.updateWithReturning(valueBucket1, predicates, config);
    console.info(`updateWithReturningExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`updateWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`updateWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
  }
```

**updateWithReturningSync23+**

updateWithReturningSync(values: [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket), predicates: RdbPredicates, config: ReturningConfig, conflict?: ConflictResolution): Result

根据RdbPredicates的指定实例对象更新数据库中的数据，可以通过conflict参数指定当发生数据冲突时的解决模式[ConflictResolution](Enums.md#ZH-CN_TOPIC_0000002553360559__conflictresolution10)，返回[Result](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__result23)。

conflict参数不建议使用ON_CONFLICT_FAIL策略，可能无法返回正确的结果。

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

模型约束： 此接口仅在Stage模型下可用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| values | [ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | 是 | values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。 |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的更新条件。 |
| config | ReturningConfig | 是 | 指定返回值的配置信息。 |
| conflict | [ConflictResolution](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10) | 否 | 指定冲突解决模式。默认为ON_CONFLICT_NONE。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Result | 如果操作成功，返回受影响的数据集。 |

错误码：

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

示例：

```ets
function updateWithReturningSyncExample(rdbStore: relationalStore.RdbStore)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 18 };
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  predicates.equalTo('NAME', 'lisi');
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  try {
    rdbStore.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
    valueBucket1['NAME'] = "zhangsan";
    valueBucket1['AGE'] = 18;
    let results = rdbStore.updateWithReturningSync(valueBucket1, predicates, config);
    console.info(`updateWithReturningSyncExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`updateWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`updateWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
}
```

#### delete

delete(predicates: RdbPredicates, callback: AsyncCallback<number>):void

根据RdbPredicates的指定实例对象从数据库中删除数据，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的删除条件。 |
| callback | AsyncCallback<number> | 是 | 指定callback回调函数。返回受影响的行数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).delete(predicates, (err, rows) => {
    if (err) {
      console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info(`Delete rows: ${rows}`);
  });
}
```

#### delete

delete(predicates: RdbPredicates):Promise<number>

根据RdbPredicates的指定实例对象从数据库中删除数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的删除条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回受影响的行数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).delete(predicates).then((rows: number) => {
    console.info(`Delete rows: ${rows}`);
  }).catch((err: BusinessError) => {
    console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### deleteSync12+

deleteSync(predicates: RdbPredicates):number

根据RdbPredicates的指定实例对象从数据库中删除数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的删除条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| number | 返回受影响的行数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  try {
    let rows: number = (store as relationalStore.RdbStore).deleteSync(predicates);
    console.info(`Delete rows: ${rows}`);
  } catch (err) {
    console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
  }
```

**deleteWithReturning23+**

deleteWithReturning(predicates: RdbPredicates, config: ReturningConfig): Promise<Result>

根据RdbPredicates的实例对象从数据库中删除数据，返回[Result](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__result23)，使用Promise异步回调。

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

模型约束： 此接口仅在Stage模型下可用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的删除条件。 |
| config | ReturningConfig | 是 | 指定返回值的配置信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<Result> | Promise对象。如果操作成功，返回受影响的数据集。 |

错误码：

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

示例：

```ets
async function deleteWithReturningExample(rdbStore: relationalStore.RdbStore)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  try {
    rdbStore.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
    let results = await rdbStore.deleteWithReturning(predicates, config);
    console.info(`deleteWithReturningExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`deleteWithReturningExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`deleteWithReturningExample failed. code is ${e.code}, message is ${e.message}`);
  }
```

**deleteWithReturningSync23+**

deleteWithReturningSync(predicates: RdbPredicates, config: ReturningConfig): Result

根据RdbPredicates的实例对象从数据库中删除数据，返回[Result](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__result23)。

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

模型约束： 此接口仅在Stage模型下可用。

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的删除条件。 |
| config | ReturningConfig | 是 | 指定返回值的配置信息。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Result | 如果操作成功，返回受影响的数据集。 |

错误码：

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1. Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800047 | The WAL file size exceeds the default limit. |

示例：

```ets
function deleteWithReturningSyncExample(rdbStore: relationalStore.RdbStore)
{
  const valueBucket1: relationalStore.ValuesBucket = { 'NAME': 'lisi', 'AGE': 21 };
  const valueBucket2: relationalStore.ValuesBucket = { 'NAME': 'zhangsan', 'AGE': 18 };
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  const config: relationalStore.ReturningConfig = { columns: ['NAME', 'AGE'] };
  try {
    rdbStore.batchInsertWithReturningSync("EMPLOYEE", [valueBucket1, valueBucket2], config);
    let results = rdbStore.deleteWithReturningSync(predicates, config);
    console.info(`deleteWithReturningSyncExample is successful, changed is ${results.changed}`);
    while(results.resultSet.goToNextRow()) {
      const row = results.resultSet.getRow();
      console.info(`deleteWithReturningSyncExample, name is ${row['NAME']}, age is ${row['AGE']}`);
    }
  } catch (e) {
    console.error(`deleteWithReturningSyncExample failed. code is ${e.code}, message is ${e.message}`);
}
```

#### query10+

query(predicates: RdbPredicates, callback: AsyncCallback<ResultSet>):void

根据指定条件查询数据库中的数据，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的查询条件。 |
| callback | AsyncCallback<ResultSet> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  (store as relationalStore.RdbStore).query(predicates, async (err, resultSet) => {
    if (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
    } catch (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
    }
  });
}
```

#### query

query(predicates: RdbPredicates, columns: Array<string>, callback: AsyncCallback<ResultSet>):void

根据指定条件查询数据库中的数据，支持指定要查询的列，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 是 | 表示要查询的列。如果值为空，则查询应用于所有列。 |
| callback | AsyncCallback<ResultSet> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  (store as relationalStore.RdbStore).query(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"], async (err, resultSet) => {
    if (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
    } catch (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
    }
  });
}
```

#### query

query(predicates: RdbPredicates, columns?: Array<string>):Promise<ResultSet>

根据指定条件查询数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询应用于所有列。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<ResultSet> | Promise对象。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  (store as relationalStore.RdbStore).query(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]).then(async (resultSet: relationalStore.ResultSet) => {
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
    } catch (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
    }
  }).catch((err: BusinessError) => {
    console.error(`Query failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### querySync12+

querySync(predicates: RdbPredicates, columns?: Array<string>):ResultSet

根据指定条件查询数据库中的数据。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](@ohos.[taskpool](../../modules/ohos/@ohos.taskpool（启动任务池）.md)（启动任务池）.md)线程中执行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询应用于所有列。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| ResultSet | 如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  let resultSet: relationalStore.ResultSet | undefined;
  try {
    resultSet = store.querySync(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    while (resultSet.goToNextRow()) {
      const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
      const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
      const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
      const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
      console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
    }
  } catch (err) {
    console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
  } finally {
    // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
    if (resultSet) {
      resultSet.close();
    }
```

**queryWithoutRowCount23+**

queryWithoutRowCount(predicates: RdbPredicates, columns?: Array<string>): Promise<LiteResultSet>

根据指定条件查询数据库中的数据，查询时不计算行数，性能优于[query](#ZH-CN_TOPIC_0000002553200595__query-1)接口。使用Promise异步回调。

模型约束： 此接口仅在Stage模型下可用。

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询该表的所有列。默认值为空。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<LiteResultSet> | 如果操作成功，则返回LiteResultSet对象。 |

错误码：

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800014 | The target instance is already closed. |

示例：

```ets
async function queryWithoutRowCountEmployee(store : relationalStore.RdbStore) {
  let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
  predicates.equalTo("NAME", "Rose");
  if (store != undefined) {
    let resultSet: relationalStore.LiteResultSet | undefined;
    try {
      resultSet = await store.queryWithoutRowCount(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
      if (resultSet != undefined) {
        // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
        while (resultSet.goToNextRow()) {
          const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
          const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
          const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
          const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
          console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
  }
    } catch (err) {
      console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      if (resultSet != undefined) {
        resultSet.close();
      }
```

**queryWithoutRowCountSync23+**

queryWithoutRowCountSync(predicates: RdbPredicates, columns?: Array<string>): LiteResultSet

根据指定条件查询数据库中的数据，查询时不计算行数。对queryWithoutRowCountSync同步接口获得的LiteResultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](@ohos.taskpool（启动任务池）.md)线程中执行。

模型约束： 此接口仅在Stage模型下可用。

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询应用于所有列。默认值为空。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| LiteResultSet | 如果操作成功，则返回LiteResultSet对象。 |

错误码：

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800014 | The target instance is already closed. |

示例：

```ets
let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  let resultSet: relationalStore.LiteResultSet | undefined;
  try {
    resultSet = store.queryWithoutRowCountSync(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]);
    if (resultSet != undefined) {
      // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
  } catch (err) {
    console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
  } finally {
    // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
    if (resultSet != undefined) {
      resultSet.close();
    }
```

**querySqlWithoutRowCount23+**

querySqlWithoutRowCount(sql: string, bindArgs?: Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>): Promise<LiteResultSet>

根据指定条件查询数据库中的数据，查询时不计算行数。使用Promise异步回调。性能优于[querySql](#ZH-CN_TOPIC_0000002553200595__querysql-1)接口。SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。

模型约束： 此接口仅在Stage模型下可用。

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<LiteResultSet> | Promise对象。如果操作成功，则返回ResultSet对象。 |

错误码：

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800014 | The target instance is already closed. |

示例：

```ets
async function querySqlWithoutRowCountEmployee(store : relationalStore.RdbStore) {
  if (store != undefined) {
    let resultSet: relationalStore.LiteResultSet | undefined;
    try {
      resultSet = await store.querySqlWithoutRowCount('select * from EMPLOYEE where name = ?', ["Rose"]);
      if (resultSet != undefined) {
        // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
        while (resultSet.goToNextRow()) {
          const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
          const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
          const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
          const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
          console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
        }
    } catch (err) {
      console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      if (resultSet != undefined) {
        resultSet.close();
      }
```

**querySqlWithoutRowCountSync23+**

querySqlWithoutRowCountSync(sql: string, bindArgs?: Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>):LiteResultSet

根据指定SQL语句查询数据库中的数据，查询时不计算行数。SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对querySqlWithoutRowCountSync同步接口获得的LiteResultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](@ohos.taskpool（启动任务池）.md)线程中执行。

模型约束： 此接口仅在Stage模型下可用。

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

参数：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。默认值为空。 |

返回值：

| 类型 | 说明 |
| --- | --- |
| LiteResultSet | 如果操作成功，则返回LiteResultSet对象。 |

错误码：

以下错误码的详细介绍请参见[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800014 | The target instance is already closed. |

示例：

```ets
if (store != undefined) {
  let resultSet: relationalStore.LiteResultSet | undefined;
  try {
    resultSet = store.querySqlWithoutRowCountSync('select * from EMPLOYEE where name = ?', ["Rose"]);
    if (resultSet != undefined) {
      // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
  } catch (err) {
    console.error(`Query failed, code is ${err.code}, message is ${err.message}`);
  } finally {
    // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
    if (resultSet != undefined) {
      resultSet.close();
}
```

#### remoteQuery

remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string> , callback: AsyncCallback<ResultSet>): void

根据指定条件查询远程设备数据库中的数据。使用callback异步回调。


其中device通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 指定的远程设备ID。 |
| table | string | 是 | 指定的目标表名。 |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象，指定查询的条件。 |
| columns | Array<string> | 是 | 表示要查询的列。如果值为空，则查询应用于所有列。 |
| callback | AsyncCallback<ResultSet> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceId: string | undefined = undefined;

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices = dmInstance.getAvailableDeviceListSync();
  if (!devices || devices.length === 0) {
    console.error("No available devices found");
  } else {
    deviceId = devices[0].networkId;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.greaterThan("id", 0);
if (store != undefined && deviceId != undefined) {
  (store as relationalStore.RdbStore).remoteQuery(deviceId, "EMPLOYEE", predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]).then(async (resultSet: relationalStore.ResultSet) => {
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
    } catch (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to remoteQuery, code is ${err.code},message is ${err.message}`);
  });
}
```

#### remoteQuery

remoteQuery(device: string, table: string, predicates: RdbPredicates, columns: Array<string>): Promise<ResultSet>

根据指定条件查询远程设备数据库中的数据。使用Promise异步回调。


其中device通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 指定的远程设备ID。 |
| table | string | 是 | 指定的目标表名。 |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象，指定查询的条件。 |
| columns | Array<string> | 是 | 表示要查询的列。如果值为空，则查询应用于所有列。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<ResultSet> | Promise对象。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceId: string | undefined = undefined;

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
  if (!devices || devices.length === 0) {
    console.error("No available devices found");
  } else {
    deviceId = devices[0].networkId;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.greaterThan("id", 0);
if (store != undefined && deviceId != undefined) {
  (store as relationalStore.RdbStore).remoteQuery(deviceId, "EMPLOYEE", predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]).then(async (resultSet: relationalStore.ResultSet) => {
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
    } catch (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to remoteQuery, code is ${err.code},message is ${err.message}`);
  });
}
```

#### querySql10+

querySql(sql: string, callback: AsyncCallback<ResultSet>):void

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

该接口支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用，当前支持的语法见[规格限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-vector-store#规格限制)。

聚合函数不支持嵌套使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| callback | AsyncCallback<ResultSet> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

关系型数据库：

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'", async (err, resultSet) => {
    if (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
    } catch (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
    }
  });
}
```

向量数据库：

```ets
// 相似度的计算符号是<->，余弦距离的计算符号是<=>
const querySql = "select id, repr <-> '[1.5,5.6]' as distance from test ORDER BY repr <-> '[1.5,5.6]' limit 10 offset 1;";
let resultSet = await store.querySql(querySql);

// 聚合查询，其中group by支持多列
const querySql1 = "select id, repr from test group by id, repr having max(repr<=>'[1.5,5.6]');";
let resultSet1 = await store.querySql(querySql1);

// 子查询，最大支持嵌套32层
const querySql2 = "select * from test where id in (select id from test1)";
let resultSet2 = await store.querySql(querySql2);
```

#### querySql

querySql(sql: string, bindArgs: Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>, callback: AsyncCallback<ResultSet>):void

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，支持传入SQL语句中参数的值，使用callback异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

该接口支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用，当前支持的语法见[规格限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-vector-store#规格限制)。

聚合函数不支持嵌套使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | 是 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数需为空数组。 |
| callback | AsyncCallback<ResultSet> | 是 | 指定callback回调函数。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = ?", ['sanguo'], async (err, resultSet) => {
    if (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
    } catch (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
    }
  });
}
```

#### querySql

querySql(sql: string, bindArgs?: Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>):Promise<ResultSet>

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，使用此接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002522080632__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

该接口支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用，当前支持的语法见[规格限制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-persistence-by-vector-store#规格限制)。

聚合函数不支持嵌套使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<ResultSet> | Promise对象。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

关系型数据库：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'").then(async (resultSet: relationalStore.ResultSet) => {
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
    } catch (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
    }
  }).catch((err: BusinessError) => {
    console.error(`Query failed, code is ${err.code},message is ${err.message}`);
  });
}
```

向量数据库：

```ets
// 查询id为1，与[1.5, 2.5]相似度小于0.5，且以相似度进行升序排序的前10条数据
const querySql = "select id, repr <-> ? as distance from test where id = ? and repr <-> ? < 0.5 ORDER BY repr <-> ? limit 10;";
const vectorValue: Float32Array = new Float32Array([1.5, 2.5]);
let resultSet = await store.querySql(querySql, [vectorValue, 1, vectorValue, vectorValue]);
```

#### querySqlSync12+

querySqlSync(sql: string, bindArgs?: Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>):ResultSet

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](@ohos.taskpool（启动任务池）.md)线程中执行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| ResultSet | 如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |

**示例：**

```ets
if (store != undefined) {
  let resultSet: relationalStore.ResultSet | undefined;
  try {
    resultSet = store.querySqlSync("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'");
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    while (resultSet.goToNextRow()) {
      const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
      const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
      const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
      const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
      console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
    }
  } catch (err) {
    console.error(`Query failed, code is ${err.code},message is ${err.message}`);
  } finally {
    // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
    if (resultSet) {
      resultSet.close();
    }
```

#### executeSql10+

executeSql(sql: string, callback: AsyncCallback<void>):void

执行指定的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用callback异步回调。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](#ZH-CN_TOPIC_0000002553200595__querysql10)、[query](#ZH-CN_TOPIC_0000002553200595__query10)、[attach](#ZH-CN_TOPIC_0000002553200595__attach12)、[beginTransaction](#ZH-CN_TOPIC_0000002553200595__begintransaction)、[commit](#ZH-CN_TOPIC_0000002553200595__commit)等接口代替。

不支持分号分隔的多条语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
const SQL_DELETE_TABLE = "DELETE FROM test WHERE name = 'zhangsan'";
if (store != undefined) {
  (store as relationalStore.RdbStore).executeSql(SQL_DELETE_TABLE, (err) => {
    if (err) {
      console.error(`ExecuteSql failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Delete table done.');
  });
}
```

#### executeSql

executeSql(sql: string, bindArgs: Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>, callback: AsyncCallback<void>):void

执行指定的SQL语句，支持传入SQL语句中参数的值，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用callback异步回调。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](#ZH-CN_TOPIC_0000002553200595__querysql10)、[query](#ZH-CN_TOPIC_0000002553200595__query10)、[attach](#ZH-CN_TOPIC_0000002553200595__attach12)、[beginTransaction](#ZH-CN_TOPIC_0000002553200595__begintransaction)、[commit](#ZH-CN_TOPIC_0000002553200595__commit)等接口代替。

不支持分号分隔的多条语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | 是 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数需为空数组。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
const SQL_DELETE_TABLE = "DELETE FROM test WHERE name = ?";
if (store != undefined) {
  (store as relationalStore.RdbStore).executeSql(SQL_DELETE_TABLE, ['zhangsan'], (err) => {
    if (err) {
      console.error(`ExecuteSql failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Delete table done.');
  });
}
```

#### executeSql

executeSql(sql: string, bindArgs?: Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>):Promise<void>

执行指定的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](#ZH-CN_TOPIC_0000002553200595__querysql10)、[query](#ZH-CN_TOPIC_0000002553200595__query10)、[attach](#ZH-CN_TOPIC_0000002553200595__attach12)、[beginTransaction](#ZH-CN_TOPIC_0000002553200595__begintransaction)、[commit](#ZH-CN_TOPIC_0000002553200595__commit)等接口代替。

不支持分号分隔的多条语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| bindArgs | Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const SQL_DELETE_TABLE = "DELETE FROM test WHERE name = 'zhangsan'";
if (store != undefined) {
  (store as relationalStore.RdbStore).executeSql(SQL_DELETE_TABLE).then(() => {
    console.info('Delete table done.');
  }).catch((err: BusinessError) => {
    console.error(`ExecuteSql failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### execute12+

execute(sql: string, args?: Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>):Promise<ValueType>

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)，使用Promise异步回调。

该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](#ZH-CN_TOPIC_0000002553200595__querysql10)、[query](#ZH-CN_TOPIC_0000002553200595__query10)、[attach](#ZH-CN_TOPIC_0000002553200595__attach12)、[beginTransaction](#ZH-CN_TOPIC_0000002553200595__begintransaction)、[commit](#ZH-CN_TOPIC_0000002553200595__commit)等接口代替。

向量数据库使用该接口执行插入操作，数据来源于子查询时，支持全字段插入，暂不支持部分字段插入。

不支持分号分隔的多条语句。

不支持开头包含注释的语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| args | Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | Promise对象，返回sql执行后的结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

关系型数据库：

```ets
import { BusinessError } from '@kit.BasicServicesKit';

// 校验数据库完整性
if (store != undefined) {
  const SQL_CHECK_INTEGRITY = 'PRAGMA integrity_check';
  (store as relationalStore.RdbStore).execute(SQL_CHECK_INTEGRITY).then((data) => {
    console.info(`check result: ${data}`);
  }).catch((err: BusinessError) => {
    console.error(`check failed, code is ${err.code}, message is ${err.message}`);
  });
}

// 删除表中所有数据
if (store != undefined) {
  const SQL_DELETE_TABLE = 'DELETE FROM test';
  (store as relationalStore.RdbStore).execute(SQL_DELETE_TABLE).then((data) => {
    console.info(`delete result: ${data}`);
  }).catch((err: BusinessError) => {
    console.error(`delete failed, code is ${err.code}, message is ${err.message}`);
  });
}

// 删表
if (store != undefined) {
  const SQL_DROP_TABLE = 'DROP TABLE test';
  (store as relationalStore.RdbStore).execute(SQL_DROP_TABLE).then((data) => {
    console.info(`drop result: ${data}`);
  }).catch((err: BusinessError) => {
    console.error(`drop failed, code is ${err.code}, message is ${err.message}`);
  });
}
```

向量数据库：

```ets
// FLOATVECTOR(2)是维度为2的向量属性，后续操作repr需依照该维度进行。
let createSql = "CREATE TABLE test (ID INTEGER PRIMARY KEY,REPR FLOATVECTOR(2));";
// 建表
await store!.execute(createSql);
// 使用参数绑定插入数据
let insertSql = "insert into test VALUES(?, ?);";
const vectorValue: Float32Array = Float32Array.from([1.5, 6.6]);
await store!.execute(insertSql, [0, vectorValue]);
// 不使用绑定参数直接执行
await store!.execute("insert into test values(1, '[3.5, 1.8]');");
```

#### execute12+

execute(sql: string, txId: number, args?: Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>): Promise<ValueType>

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。

该接口仅支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用。使用该接口执行插入操作，数据来源于子查询时，支持全字段插入，暂不支持部分字段插入。

此接口不支持执行查询，可以使用[querySql](#ZH-CN_TOPIC_0000002553200595__querysql10)接口代替。

不支持分号分隔的多条语句。

不支持开头包含注释的语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| txId | number | 是 | 通过beginTrans获取的事务ID，如果传0，该语句默认在单独事务内。 |
| args | Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。该参数不填，填null或者填undefined，都认为是sql参数语句完整。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | Promise对象，返回null。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
if (store != null) {
  let txId: number;
  (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
    txId = temTxId;
    (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, ["18", "20"])
      .then(() => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).commit(txId);
        }
      })
      .catch((err: BusinessError) => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).rollback(txId);
        }
        console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
      });
}
```

#### executeSync12+

executeSync(sql: string, args?: Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>): ValueType

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)。

该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。

此接口不支持执行查询、附加数据库和事务操作，可以使用[querySql](#ZH-CN_TOPIC_0000002553200595__querysql10)、[query](#ZH-CN_TOPIC_0000002553200595__query10)、[attach](#ZH-CN_TOPIC_0000002553200595__attach12)、[beginTransaction](#ZH-CN_TOPIC_0000002553200595__begintransaction)、[commit](#ZH-CN_TOPIC_0000002553200595__commit)等接口代替。

不支持分号分隔的多条语句。

不支持开头包含注释的语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sql | string | 是 | 指定要执行的SQL语句。 |
| args | Array<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)> | 否 | SQL语句中参数的值。该值与sql参数语句中的占位符相对应。该参数不填，或者填null或undefined，都认为是sql参数语句完整。默认值为空。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype) | 返回sql执行后的结果 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
// 校验数据库完整性
if (store != undefined) {
  const SQL_CHECK_INTEGRITY = 'PRAGMA integrity_check';
  try {
    let data = (store as relationalStore.RdbStore).executeSync(SQL_CHECK_INTEGRITY);
    console.info(`check result: ${data}`);
  } catch (err) {
    console.error(`check failed, code is ${err.code}, message is ${err.message}`);
  }

// 删除表中所有数据
if (store != undefined) {
  const SQL_DELETE_TABLE = 'DELETE FROM test';
  try {
    let data = (store as relationalStore.RdbStore).executeSync(SQL_DELETE_TABLE);
    console.info(`delete result: ${data}`);
  } catch (err) {
    console.error(`delete failed, code is ${err.code}, message is ${err.message}`);
}

// 删表
if (store != undefined) {
  const SQL_DROP_TABLE = 'DROP TABLE test';
  try {
    let data = (store as relationalStore.RdbStore).executeSync(SQL_DROP_TABLE);
    console.info(`drop result: ${data}`);
  } catch (err) {
    console.error(`drop failed, code is ${err.code}, message is ${err.message}`);
  }
```

#### get[ModifyTime](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__modifytime10)10+

getModifyTime(table: string, columnName: string, primaryKeys: [PRIKeyType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__prikeytype10)[], callback: AsyncCallback<ModifyTime>): void

获取数据库表中数据的最后修改时间，使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定要查询的数据库表的表名。 |
| columnName | string | 是 | 指定要查询的数据库表的列名。 |
| primaryKeys | [PRIKeyType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__prikeytype10)[] | 是 | 指定要查询的行的主键。 如果数据库表无主键，参数columnName需传入"rowid"，此时primaryKeys为要查询的数据库表的行号。 如果数据库表无主键，参数columnName传入不为"rowid"，返回对应的错误码。 |
| callback | AsyncCallback<[ModifyTime](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__modifytime10)> | 是 | 指定callback回调函数。如果操作成功，则返回ModifyTime对象，表示数据的最后修改时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 3 - 4 parameter(s)! 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. 4. The columnName must be not empty string. 5. The PRIKey must be number or string. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
let PRIKey = [1, 4, 2, 3];
if (store != undefined) {
  (store as relationalStore.RdbStore).getModifyTime("EMPLOYEE", "NAME", PRIKey, (err, modifyTime: relationalStore.ModifyTime) => {
    if (err) {
      console.error(`getModifyTime failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    let size = modifyTime.size;
  });
}
```

#### get[ModifyTime](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__modifytime10)10+

getModifyTime(table: string, columnName: string, primaryKeys: [PRIKeyType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__prikeytype10)[]): Promise<ModifyTime>

获取数据库表中数据的最后修改时间，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 指定要查询的数据库表的表名。 |
| columnName | string | 是 | 指定要查询的数据库表的列名。 |
| primaryKeys | [PRIKeyType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__prikeytype10)[] | 是 | 指定要查询的行的主键。 如果数据库表无主键，参数columnName需传入"rowid"，此时primaryKeys为要查询的数据库表的行号。 如果数据库表无主键，参数columnName传入不为"rowid"，返回对应的错误码。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[ModifyTime](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__modifytime10)> | 返回ModifyTime类型的Promise对象，表示数据最后的修改时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 3 - 4 parameter(s)! 2. The RdbStore must be not nullptr.3. The tablesNames must be not empty string. 4. The columnName must be not empty string. 5. The PRIKey must be number or string. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let PRIKey = [1, 2, 3];
if (store != undefined) {
  (store as relationalStore.RdbStore).getModifyTime("EMPLOYEE", "NAME", PRIKey)
    .then((modifyTime: relationalStore.ModifyTime) => {
      let size = modifyTime.size;
    })
    .catch((err: BusinessError) => {
      console.error(`getModifyTime failed, code is ${err.code},message is ${err.message}`);
    });
}
```

#### beginTransaction

beginTransaction():void

在开始执行SQL语句之前，开始事务。

此接口不允许嵌套事务，且不支持在多进程或多线程中使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3]);

if (store != undefined) {
  (store as relationalStore.RdbStore).beginTransaction();
  const valueBucket: relationalStore.ValuesBucket = {
    'NAME': value1,
    'AGE': value2,
    'SALARY': value3,
    'CODES': value4
  };
  (store as relationalStore.RdbStore).insert("test", valueBucket);
  (store as relationalStore.RdbStore).commit();
}
```

#### beginTrans12+

beginTrans(): Promise<number>

在开始执行SQL语句之前，开始事务，使用Promise异步回调。

与[beginTransaction](#ZH-CN_TOPIC_0000002553200595__begintransaction)的区别在于：该接口会返回事务ID，[execute](#ZH-CN_TOPIC_0000002553200595__execute12-1)可以指定不同事务ID达到事务隔离目的。

该接口仅支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回事务ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 801 | Capability not supported the sql(attach,begin,commit,rollback etc.). |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |
| 14800047 | The WAL file size exceeds the default limit. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
if (store != null) {
  let txId: number;
  (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
    txId = temTxId;
    (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, ["18", "20"])
      .then(() => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).commit(txId);
        }
      })
      .catch((err: BusinessError) => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).rollback(txId);
        }
        console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
      });
}
```

#### createTransaction14+

createTransaction(options?: TransactionOptions): Promise<Transaction>

创建一个事务对象并开始事务，使用Promise异步回调。

与[beginTransaction](#ZH-CN_TOPIC_0000002553200595__begintransaction)的区别在于：createTransaction接口会返回一个事务对象，不同事务对象之间是隔离的。使用事务对象进行插入、删除或更新数据等操作，无法被注册数据变更通知[on('dataChange')](#ZH-CN_TOPIC_0000002553200595__ondatachange)监听到。

一个store最多支持同时存在四个事务对象，超过后会返回14800015错误码，此时需要检查是否持有事务对象时间过长或并发事务过多，若确认无法通过上述优化解决问题，建议等待现有事务释放后，再尝试新建事务对象。

优先使用createTransaction，不再推荐使用beginTransaction。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | TransactionOptions | 否 | 表示事务对象的配置信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Transaction> | Promise对象，返回事务对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database is busy. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).createTransaction().then(async (transaction: relationalStore.Transaction) => {
    transaction.execute("DELETE FROM test WHERE age = ? OR age = ?", [21, 20]).then(() => {
      transaction.commit();
    }).catch((e: BusinessError) => {
      transaction.rollback();
      console.error(`execute sql failed, code is ${e.code},message is ${e.message}`);
    });
  }).catch((err: BusinessError) => {
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### commit

commit():void

提交已执行的SQL语句，跟[beginTransaction](#ZH-CN_TOPIC_0000002553200595__begintransaction)配合使用。

此接口不允许嵌套事务，且不支持在多进程或多线程中使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3]);

if (store != undefined) {
  (store as relationalStore.RdbStore).beginTransaction();
  const valueBucket: relationalStore.ValuesBucket = {
    'NAME': value1,
    'AGE': value2,
    'SALARY': value3,
    'CODES': value4
  };
  (store as relationalStore.RdbStore).insert("test", valueBucket);
  (store as relationalStore.RdbStore).commit();
}
```

#### commit12+

commit(txId : number):Promise<void>

提交已执行的SQL语句，跟[beginTrans](#ZH-CN_TOPIC_0000002553200595__begintrans12)配合使用，使用Promise异步回调。

该接口仅支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| txId | number | 是 | 通过beginTrans获取的事务ID。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
if (store != null) {
  let txId: number;
  (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
    txId = temTxId;
    (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, ["18", "20"])
      .then(() => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).commit(txId);
        }
      })
      .catch((err: BusinessError) => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).rollback(txId);
        }
        console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
      });
}
```

#### rollBack

rollBack():void

回滚已经执行的SQL语句。

此接口不允许嵌套事务，且不支持在多进程或多线程中使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3]);

if (store != undefined) {
  try {
    (store as relationalStore.RdbStore).beginTransaction();
    const valueBucket: relationalStore.ValuesBucket = {
      'NAME': value1,
      'AGE': value2,
      'SALARY': value3,
      'CODES': value4
    };
    (store as relationalStore.RdbStore).insert("test", valueBucket);
    (store as relationalStore.RdbStore).commit();
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error(`Transaction failed, code is ${code},message is ${message}`);
    (store as relationalStore.RdbStore).rollBack();
  }
```

#### rollback12+

rollback(txId : number):Promise<void>

回滚已经执行的SQL语句，跟[beginTrans](#ZH-CN_TOPIC_0000002553200595__begintrans12)配合使用，使用Promise异步回调。

该接口仅支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| txId | number | 是 | 通过beginTrans获取的事务ID。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';
if (store != null) {
  let txId: number;
  (store as relationalStore.RdbStore).beginTrans().then((temTxId: number) => {
    txId = temTxId;
    (store as relationalStore.RdbStore).execute("DELETE FROM TEST WHERE age = ? OR age = ?", txId, ["18", "20"])
      .then(() => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).commit(txId);
        }
      })
      .catch((err: BusinessError) => {
        if (txId !== undefined) {
          (store as relationalStore.RdbStore).rollback(txId);
        }
        console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
      });
}
```

#### backup

backup(destName:string, callback: AsyncCallback<void>):void

以指定名称备份数据库，使用callback异步回调。

该接口支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| destName | string | 是 | 指定数据库的备份文件名。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).backup("dbBackup.db", (err) => {
    if (err) {
      console.error(`Backup failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Backup success.');
  });
}
```

#### backup

backup(destName:string): Promise<void>

以指定名称备份数据库，使用Promise异步回调。

该接口支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| destName | string | 是 | 指定数据库的备份文件名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  let promiseBackup = (store as relationalStore.RdbStore).backup("dbBackup.db");
  promiseBackup.then(() => {
    console.info('Backup success.');
  }).catch((err: BusinessError) => {
    console.error(`Backup failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### restore

restore(srcName:string, callback: AsyncCallback<void>):void

从指定的数据库备份文件恢复数据库，使用callback异步回调。

该接口支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcName | string | 是 | 指定数据库的备份文件名。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).restore("dbBackup.db", (err) => {
    if (err) {
      console.error(`Restore failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Restore success.');
  });
}
```

#### restore

restore(srcName:string): Promise<void>

从指定的数据库备份文件恢复数据库，使用Promise异步回调。

该接口支持[向量数据库](Interfaces (其他).md#ZH-CN_TOPIC_0000002553200597__storeconfig)使用。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| srcName | string | 是 | 指定数据库的备份文件名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  let promiseRestore = (store as relationalStore.RdbStore).restore("dbBackup.db");
  promiseRestore.then(() => {
    console.info('Restore success.');
  }).catch((err: BusinessError) => {
    console.error(`Restore failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### setDistributedTables

setDistributedTables(tables: Array<string>, callback: AsyncCallback<void>): void

设置分布式数据库表，使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式数据库的表名。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).setDistributedTables(["EMPLOYEE"], (err) => {
    if (err) {
      console.error(`SetDistributedTables failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('SetDistributedTables successfully.');
  });
}
```

#### setDistributedTables

setDistributedTables(tables: Array<string>): Promise<void>

设置分布式数据库表，使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式数据库的表名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).setDistributedTables(["EMPLOYEE"]).then(() => {
    console.info('SetDistributedTables successfully.');
  }).catch((err: BusinessError) => {
    console.error(`SetDistributedTables failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### setDistributedTables10+

setDistributedTables(tables: Array<string>, type: [DistributedType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__distributedtype10), callback: AsyncCallback<void>): void

设置分布式数据库表，支持指定表的分布式类型，使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式数据库的表名。 |
| type | [DistributedType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__distributedtype10) | 是 | 表的分布式类型。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800051 | The type of the distributed table does not match. |

**示例：**

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).setDistributedTables(["EMPLOYEE"], relationalStore.DistributedType.DISTRIBUTED_CLOUD, (err) => {
    if (err) {
      console.error(`SetDistributedTables failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('SetDistributedTables successfully.');
  });
}
```

#### setDistributedTables10+

setDistributedTables(tables: Array<string>, type: [DistributedType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__distributedtype10), config: DistributedConfig, callback: AsyncCallback<void>): void

设置分布式数据库表，支持指定表的分布式类型和表的分布式配置信息，使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式数据库的表名。 |
| type | [DistributedType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__distributedtype10) | 是 | 表的分布式类型。 |
| config | DistributedConfig | 是 | 表的分布式配置信息。 |
| callback | AsyncCallback<void> | 是 | 指定callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800051 | The type of the distributed table does not match. |

**示例：**

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).setDistributedTables(["EMPLOYEE"], relationalStore.DistributedType.DISTRIBUTED_CLOUD, {
    autoSync: true
  }, (err) => {
    if (err) {
      console.error(`SetDistributedTables failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('SetDistributedTables successfully.');
  });
}
```

#### setDistributedTables10+

setDistributedTables(tables: Array<string>, type?: [DistributedType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__distributedtype10), config?: DistributedConfig): Promise<void>

设置分布式数据库表，支持指定表的分布式类型和表的分布式配置信息，使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tables | Array<string> | 是 | 要设置的分布式数据库的表名。 |
| type | [DistributedType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__distributedtype10) | 否 | 表的分布式类型。默认值是relationalStore.DistributedType.DISTRIBUTED_DEVICE。 |
| config | DistributedConfig | 否 | 表的分布式配置信息。不传入时默认autoSync为false，即只支持手动同步。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800051 | The type of the distributed table does not match. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).setDistributedTables(["EMPLOYEE"], relationalStore.DistributedType.DISTRIBUTED_CLOUD, {
    autoSync: true
  }).then(() => {
    console.info('SetDistributedTables successfully.');
  }).catch((err: BusinessError) => {
    console.error(`SetDistributedTables failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### obtainDistributedTableName

obtainDistributedTableName(device: string, table: string, callback: AsyncCallback<string>): void

根据远程设备的本地表名获取指定远程设备的分布式表名。在查询远程设备数据库时，需要使用分布式表名，使用callback异步回调。


其中device通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远程设备ID 。 |
| table | string | 是 | 远程设备的本地表名。 |
| callback | AsyncCallback<string> | 是 | 指定的callback回调函数。如果操作成功，返回远程设备的分布式表名。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceId: string | undefined = undefined;

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices = dmInstance.getAvailableDeviceListSync();
  if (!devices || devices.length === 0) {
    console.error("No available devices found");
  } else {
  deviceId = devices[0].networkId;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

if (store != undefined && deviceId != undefined) {
  (store as relationalStore.RdbStore).obtainDistributedTableName(deviceId, "EMPLOYEE", (err, tableName) => {
    if (err) {
      console.error(`ObtainDistributedTableName failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info(`ObtainDistributedTableName successfully, tableName= ${tableName}`);
  });
}
```

#### obtainDistributedTableName

obtainDistributedTableName(device: string, table: string): Promise<string>

根据远程设备的本地表名获取指定远程设备的分布式表名。在查询远程设备数据库时，需要使用分布式表名，使用Promise异步回调。


其中device通过调用[deviceManager.getAvailableDeviceListSync](@ohos.distributedDeviceManager (设备管理).md#ZH-CN_TOPIC_0000002522081466__getavailabledevicelistsync)方法得到。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远程设备ID。 |
| table | string | 是 | 远程设备的本地表名。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象。如果操作成功，返回远程设备的分布式表名。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceId: string | undefined = undefined;

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices = dmInstance.getAvailableDeviceListSync();
  if (!devices || devices.length === 0) {
    console.error("No available devices found");
  } else {
    deviceId = devices[0].networkId;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

if (store != undefined && deviceId != undefined) {
  (store as relationalStore.RdbStore).obtainDistributedTableName(deviceId, "EMPLOYEE").then((tableName: string) => {
    console.info(`ObtainDistributedTableName successfully, tableName= ${tableName}`);
  }).catch((err: BusinessError) => {
    console.error(`ObtainDistributedTableName failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### sync

sync(mode: [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode), predicates: RdbPredicates, callback: AsyncCallback<Array<[string, number]>>): void

在设备之间同步数据，使用callback异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode) | 是 | 指同步模式。该值可以是relationalStore.SyncMode.SYNC_MODE_PUSH、relationalStore.SyncMode.SYNC_MODE_PULL。 |
| predicates | RdbPredicates | 是 | 约束同步数据和设备。 |
| callback | AsyncCallback<Array<[string, number]>> | 是 | 指定的callback回调函数，用于向调用者发送同步结果。string：设备ID；number：每个设备同步状态，0表示成功，1表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceIds: Array<string> = [];

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    deviceIds[i] = devices[i].networkId!;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.inDevices(deviceIds);
if (store != undefined) {
  (store as relationalStore.RdbStore).sync(relationalStore.SyncMode.SYNC_MODE_PUSH, predicates, (err, result) => {
    if (err) {
      console.error(`Sync failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Sync done.');
    for (let i = 0; i < result.length; i++) {
      console.info(`device= ${result[i][0]}, status= ${result[i][1]}`);
    }
  });
}
```

#### sync

sync(mode: [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode), predicates: RdbPredicates): Promise<Array<[string, number]>>

在设备之间同步数据，使用Promise异步回调。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode) | 是 | 指同步模式。该值可以是relationalStore.SyncMode.SYNC_MODE_PUSH、relationalStore.SyncMode.SYNC_MODE_PULL。 |
| predicates | RdbPredicates | 是 | 约束同步数据和设备。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[string, number]>> | Promise对象，用于向调用者发送同步结果。string：设备ID；number：每个设备同步状态，0表示成功，1表示失败。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

let dmInstance: distributedDeviceManager.DeviceManager;
let deviceIds: Array<string> = [];

try {
  dmInstance = distributedDeviceManager.createDeviceManager("com.example.appdatamgrverify");
  let devices: Array<distributedDeviceManager.DeviceBasicInfo> = dmInstance.getAvailableDeviceListSync();
  for (let i = 0; i < devices.length; i++) {
    deviceIds[i] = devices[i].networkId!;
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error("createDeviceManager errCode:" + code + ",errMessage:" + message);
}

let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.inDevices(deviceIds);
if (store != undefined) {
  (store as relationalStore.RdbStore).sync(relationalStore.SyncMode.SYNC_MODE_PUSH, predicates).then((result: Object[][]) => {
    console.info('Sync done.');
    for (let i = 0; i < result.length; i++) {
      console.info(`device= ${result[i][0]}, status= ${result[i][1]}`);
    }
  }).catch((err: BusinessError) => {
    console.error(`Sync failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### cloudSync10+

cloudSync(mode: [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode), progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void

手动执行对所有分布式表的端云同步，使用callback异步回调。使用该接口需要实现云服务功能。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode) | 是 | 表示数据库的同步模式。 |
| progress | Callback<ProgressDetails> | 是 | 用来处理数据库同步详细信息的回调函数。 |
| callback | AsyncCallback<void> | 是 | 指定的callback回调函数，用于向调用者发送同步结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode) of cloud. 4. The progress must be a callback type. 5. The callback must be a function. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST, (progressDetails) => {
    console.info(`Progress: ${progressDetails}`);
  }, (err) => {
    if (err) {
      console.error(`Cloud sync failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Cloud sync succeeded');
  });
}
```

#### cloudSync10+

cloudSync(mode: [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode), progress: Callback<ProgressDetails>): Promise<void>

手动执行对所有分布式表的端云同步，使用Promise异步回调。使用该接口需要实现云服务功能。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode) | 是 | 表示数据库的同步模式。 |
| progress | Callback<ProgressDetails> | 是 | 用来处理数据库同步详细信息的回调函数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，用于向调用者发送同步结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode) of cloud. 4. The progress must be a callback type. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST, (progressDetail: relationalStore.ProgressDetails) => {
    console.info(`progress: ${progressDetail}`);
  }).then(() => {
    console.info('Cloud sync succeeded');
  }).catch((err: BusinessError) => {
    console.error(`cloudSync failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### cloudSync10+

cloudSync(mode: [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode), tables: string[], progress: Callback<ProgressDetails>, callback: AsyncCallback<void>): void

手动执行对指定表的端云同步，使用callback异步回调。使用该接口需要实现云服务功能。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode) | 是 | 表示数据库的同步模式。 |
| tables | string[] | 是 | 指定同步的表名。 |
| progress | Callback<ProgressDetails> | 是 | 用来处理数据库同步详细信息的回调函数。 |
| callback | AsyncCallback<void> | 是 | 指定的callback回调函数，用于向调用者发送同步结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode) of cloud. 4. The tablesNames must be not empty. 5. The progress must be a callback type. 6.The callback must be a function. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
const tables = ["table1", "table2"];

if (store != undefined) {
  (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST, tables, (progressDetail: relationalStore.ProgressDetails) => {
    console.info(`Progress: ${progressDetail}`);
  }, (err) => {
    if (err) {
      console.error(`Cloud sync failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('Cloud sync succeeded');
  });
};
```

#### cloudSync10+

cloudSync(mode: [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode), tables: string[], progress: Callback<ProgressDetails>): Promise<void>

手动执行对指定表的端云同步，使用Promise异步回调。使用该接口需要实现云服务功能。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode) | 是 | 表示数据库的同步模式。 |
| tables | string[] | 是 | 指定同步的表名。 |
| progress | Callback<ProgressDetails> | 是 | 用来处理数据库同步详细信息的回调函数。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，用于向调用者发送同步结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 2 - 4 parameter(s). 2. The RdbStore must be not nullptr. 3. The mode must be a [SyncMode](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__syncmode) of cloud. 4. The tablesNames must be not empty. 5. The progress must be a callback type |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

const tables = ["table1", "table2"];

if (store != undefined) {
  (store as relationalStore.RdbStore).cloudSync(relationalStore.SyncMode.SYNC_MODE_CLOUD_FIRST, tables, (progressDetail: relationalStore.ProgressDetails) => {
    console.info(`progress: ${progressDetail}`);
  }).then(() => {
    console.info('Cloud sync succeeded');
  }).catch((err: BusinessError) => {
    console.error(`cloudSync failed, code is ${err.code},message is ${err.message}`);
  });
};
```

#### on('dataChange')

on(event: 'dataChange', type: [SubscribeType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__subscribetype), observer: Callback<Array<string>>): void

注册数据库的数据变更的事件监听。当分布式数据库中的数据发生更改时，将调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'dataChange'，表示数据更改。 |
| type | [SubscribeType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__subscribetype) | 是 | 订阅类型。 |
| observer | Callback<Array<string>> | 是 | 指分布式数据库中数据更改事件的观察者。Array<string>为数据库中的数据发生改变的对端设备ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = (devices: Array<string>) => {
  if (devices !== undefined) {
    for (let i = 0; i < devices.length; i++) {
      console.info(`device= ${devices[i]} data changed`);
  }
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}
```

#### on('dataChange')10+

on(event: 'dataChange', type: [SubscribeType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__subscribetype), observer: Callback<Array<string>>| Callback<Array<ChangeInfo>>): void

注册数据库的数据变更的事件监听。当分布式数据库或本地数据库中的数据发生更改时，将调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'dataChange'，表示数据更改。 |
| type | [SubscribeType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__subscribetype) | 是 | 订阅类型。 |
| observer | Callback<Array<string>> | Callback<Array<ChangeInfo>> | 是 | 回调函数。 当type为SUBSCRIBE_TYPE_REMOTE，observer类型需为Callback<Array<string>>，其中Array<string>为数据库中的数据发生改变的对端设备ID。 当type为SUBSCRIBE_TYPE_CLOUD，observer类型需为Callback<Array<string>>，其中Array<string>为数据库中的数据发生改变的云端账号。 当type为SUBSCRIBE_TYPE_CLOUD_DETAILS，observer类型需为Callback<Array<ChangeInfo>>，其中Array<ChangeInfo>为数据库端云同步过程的详情。 当type为SUBSCRIBE_TYPE_LOCAL_DETAILS，observer类型需为Callback<Array<ChangeInfo>>，其中Array<ChangeInfo>为本地数据库中的数据更改的详情。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例1：type为SUBSCRIBE_TYPE_REMOTE**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = (devices: Array<string>) => {
  if (devices !== undefined) {
    for (let i = 0; i < devices.length; i++) {
      console.info(`device= ${devices[i]} data changed`);
  }
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}
```

**示例2：type为SUBSCRIBE_TYPE_LOCAL_DETAILS**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let changeInfos = (changeInfos: Array<relationalStore.ChangeInfo>) => {
  for (let i = 0; i < changeInfos.length; i++) {
    console.info(`changeInfos = ${JSON.stringify(changeInfos[i])}`);
  }
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_LOCAL_DETAILS, changeInfos);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`on dataChange fail, code is ${code},message is ${message}`);
}

let value1 = "Lisa";
let value2 = 18;
let value3 = 100.5;
let value4 = new Uint8Array([1, 2, 3]);

try {
  const valueBucket: relationalStore.ValuesBucket = {
    'name': value1,
    'age': value2,
    'salary': value3,
    'blobType': value4
  };

  if (store != undefined) {
    (store as relationalStore.RdbStore).insert('test', valueBucket);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`insert fail, code is ${code},message is ${message}`);
}
```

#### on10+

on(event: string, interProcess: boolean, observer: Callback<void>): void

注册数据库的进程内或者进程间事件监听。当调用[emit](#ZH-CN_TOPIC_0000002553200595__emit10)接口时，将调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅事件名称，与emit接口触发事件时的名称一致。 |
| interProcess | boolean | 是 | 指定是进程间还是本进程订阅。 true：进程间。 false：本进程。 |
observerCallback<void>是回调函数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800050 | Failed to obtain the subscription service. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = () => {
  console.info(`storeObserver`);
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('storeObserver', false, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}
```

#### on('autoSyncProgress')11+

on(event: 'autoSyncProgress', progress: Callback<ProgressDetails>): void

在已打开端云同步，并且网络状态正常的条件下，注册自动同步进度通知，自动同步进行时调用回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'autoSyncProgress'，表示自动同步进度通知。 |
| progress | Callback<ProgressDetails> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. 4. The event must be a not empty string. 5. The progress must be function. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let progressDetail = (progressDetail: relationalStore.ProgressDetails) => {
  console.info(`progress: ${progressDetail}`);
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('autoSyncProgress', progressDetail);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}
```

#### on('statistics')12+

on(event: 'statistics', observer: Callback<SqlExecutionInfo>): void

订阅SQL统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅事件名称，取值为'statistics'，表示sql执行时间的统计。 |
| observer | Callback<SqlExecutionInfo> | 是 | 回调函数。用于返回数据库中SQL执行时间的统计信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let sqlExecutionInfo = (sqlExecutionInfo: relationalStore.SqlExecutionInfo) => {
  if (sqlExecutionInfo.sql.length > 0) {
  console.info(`sql: ${sqlExecutionInfo.sql[0]}`);
  console.info(`totalTime: ${sqlExecutionInfo.totalTime}`);
  console.info(`waitTime: ${sqlExecutionInfo.waitTime}`);
  console.info(`prepareTime: ${sqlExecutionInfo.prepareTime}`);
  console.info(`executeTime: ${sqlExecutionInfo.executeTime}`);
  }
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('statistics', sqlExecutionInfo);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}

try {
  let value1 = "Lisa";
  let value2 = 18;
  let value3 = 100.5;
  let value4 = new Uint8Array([1, 2, 3, 4, 5]);

  const valueBucket: relationalStore.ValuesBucket = {
    'NAME': value1,
    'AGE': value2,
    'SALARY': value3,
    'CODES': value4
  };
  if (store != undefined) {
    (store as relationalStore.RdbStore).insert('test', valueBucket);
  }
} catch (err) {
  console.error(`insert fail, code:${err.code}, message: ${err.message}`);
}
```

#### on('sqliteErrorOccurred')20+

on(event: 'sqliteErrorOccurred', observer: Callback<ExceptionMessage>): void

记录执行SQL语句时的异常日志。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅事件名称，取值为'sqliteErrorOccurred'，记录SQL语句执行过程中的错误信息。 |
| observer | Callback<ExceptionMessage> | 是 | 回调函数。用于返回SQL执行时出现的异常信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  if (store != undefined) {
    store.on('sqliteErrorOccurred', exceptionMessage => {
      let sqliteCode = exceptionMessage.code;
      let sqliteMessage = exceptionMessage.message;
      let errSQL = exceptionMessage.sql;
      console.error(`error log is ${sqliteCode}, errMessage is ${sqliteMessage}, errSQL is ${errSQL}`);
    })
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}
const CREATE_TABLE_TEST = "CREATE TABLE IF NOT EXISTS test (" + "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
  "name TEXT NOT NULL, " + "age INTEGER, " + "salary REAL)";
try {
  let value = new Uint8Array([1, 2, 3, 4, 5]);
  const valueBucket: relationalStore.ValuesBucket = {
    'name': "Lisa",
    'age': 18,
    'salary': 100.5,
    'codes': value,
  };
  if (store != undefined) {
    await (store as relationalStore.RdbStore).executeSql(CREATE_TABLE_TEST);
    await (store as relationalStore.RdbStore).insert('test', valueBucket);
  }
} catch (err) {
  console.error(`Insert fail, code:${err.code}, message: ${err.message}`);
}
```

#### on('perfStat')20+

on(event: 'perfStat', observer: Callback<SqlExecutionInfo>): void

订阅SQL统计信息。使用[createTransaction](#ZH-CN_TOPIC_0000002553200595__createtransaction14)创建的事务进行相关操作（[Transaction](Interface (Transaction).md)），只会在事务结束（COMMIT/ROLLBACK）时通知一次统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 订阅事件名称，取值为'perfStat'，统计执行SQL的时间。 |
| observer | Callback<SqlExecutionInfo> | 是 | 回调函数。用于返回数据库执行SQL的时间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let sqlExecutionInfo = (sqlExecutionInfo: relationalStore.SqlExecutionInfo) => {
  if (sqlExecutionInfo.sql.length > 0) {
  console.info(`sql: ${sqlExecutionInfo.sql[0]}`);
  console.info(`totalTime: ${sqlExecutionInfo.totalTime}`);
  console.info(`waitTime: ${sqlExecutionInfo.waitTime}`);
  console.info(`prepareTime: ${sqlExecutionInfo.prepareTime}`);
  console.info(`executeTime: ${sqlExecutionInfo.executeTime}`);
  }
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('perfStat', sqlExecutionInfo);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}

try {
  let value1 = "Lisa";
  let value2 = 18;
  let value3 = 100.5;
  let value4 = new Uint8Array([1, 2, 3, 4, 5]);

  const valueBucket: relationalStore.ValuesBucket = {
    'NAME': value1,
    'AGE': value2,
    'SALARY': value3,
    'CODES': value4
  };
  if (store != undefined) {
    const rowId = await store.insert('EMPLOYEE', valueBucket);
    console.info(`Insert success, rowId is: ${rowId}`);
  }
} catch (err) {
  console.error(`insert fail, code:${err.code}, message: ${err.message}`);
}
```

#### off('dataChange')

off(event:'dataChange', type: [SubscribeType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__subscribetype), observer: Callback<Array<string>>): void

取消数据变更的事件监听。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'dataChange'，表示数据更改。 |
| type | [SubscribeType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__subscribetype) | 是 | 订阅类型。 |
| observer | Callback<Array<string>> | 是 | 指已注册的数据更改观察者。Array<string>为数据库中的数据发生改变的对端设备ID。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = (devices: Array<string>) => {
  if (devices !== undefined) {
    for (let i = 0; i < devices.length; i++) {
      console.info(`device= ${devices[i]} data changed`);
  }
};

try {
  if (store != undefined) {
    // 此处不能使用Lambda表达式
    (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Unregister observer failed, code is ${code},message is ${message}`);
}
```

#### off('dataChange')10+

off(event:'dataChange', type: [SubscribeType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__subscribetype), observer?: Callback<Array<string>>| Callback<Array<ChangeInfo>>): void

取消数据变更的事件监听。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'dataChange'，表示数据更改。 |
| type | [SubscribeType](../enums/Enums.md#ZH-CN_TOPIC_0000002497604686__subscribetype) | 是 | 订阅类型。 |
| observer | Callback<Array<string>>| Callback<Array<ChangeInfo>> | 否 | 回调函数。 当type为SUBSCRIBE_TYPE_REMOTE，observer类型需为Callback<Array<string>>，其中Array<string>为数据库中的数据发生改变的对端设备ID。 当type为SUBSCRIBE_TYPE_CLOUD，observer类型需为Callback<Array<string>>，其中Array<string>为数据库中的数据发生改变的云端账号。 当type为SUBSCRIBE_TYPE_CLOUD_DETAILS，observer类型需为Callback<Array<ChangeInfo>>，其中Array<ChangeInfo>为数据库端云同步过程的详情。 当type为SUBSCRIBE_TYPE_LOCAL_DETAILS，observer类型需为Callback<Array<ChangeInfo>>，其中Array<ChangeInfo>为本地数据库中的数据更改的详情。 当observer没有传入时，表示取消当前type类型下所有数据变更的事件监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Permission verification failed, application which is not a system application uses system API. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = (devices: Array<string>) => {
  if (devices !== undefined) {
    for (let i = 0; i < devices.length; i++) {
      console.info(`device= ${devices[i]} data changed`);
  }
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('dataChange', relationalStore.SubscribeType.SUBSCRIBE_TYPE_REMOTE, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Unregister observer failed, code is ${code},message is ${message}`);
}
```

#### off10+

off(event: string, interProcess: boolean, observer?: Callback<void>): void

取消数据库的进程内或者进程间事件监听。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅事件名称。事件名称与on接口调用时订阅事件的名称一致。 |
| interProcess | boolean | 是 | 指定是进程间还是本进程取消订阅。 true：进程间。 false：本进程。 |
observerCallback<void>否该参数存在，则取消指定Callback监听回调，否则取消该event事件的所有监听回调。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800050 | Failed to obtain the subscription service. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let storeObserver = () => {
  console.info(`storeObserver`);
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('storeObserver', false, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('storeObserver', false, storeObserver);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Unregister observer failed, code is ${code},message is ${message}`);
}
```

#### off('autoSyncProgress')11+

off(event: 'autoSyncProgress', progress?: Callback<ProgressDetails>): void

取消订阅自动同步进度的通知。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取值为'autoSyncProgress'，表示自动同步进度通知。 |
| progress | Callback<ProgressDetails> | 否 | 指已注册的自动同步进度观察者。该参数存在，则取消订阅指定回调，该参数为null或undefined或不存在，则取消订阅所有回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be valid. 3. The event must be a not empty string. 4. The progress must be function. |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let progressDetail = (progressDetail: relationalStore.ProgressDetails) => {
  console.info(`progress: ${progressDetail}`);
};

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).on('autoSyncProgress', progressDetail);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Register observer failed, code is ${code},message is ${message}`);
}

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('autoSyncProgress', progressDetail);
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Unregister failed, code is ${code},message is ${message}`);
}
```

#### off('statistics')12+

off(event: 'statistics', observer?: Callback<SqlExecutionInfo>): void

取消订阅SQL统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅事件名称。取值为'statistics'，表示sql执行时间的统计。 |
| observer | Callback<SqlExecutionInfo> | 否 | 回调函数。该参数存在，则取消指定Callback监听回调，否则取消该event事件的所有监听回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('statistics');
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Unregister observer failed, code is ${code},message is ${message}`);
}
```

#### off('sqliteErrorOccurred')20+

off(event: 'sqliteErrorOccurred', observer?: Callback<ExceptionMessage>): void

停止记录SQL执行过程中的异常日志。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅事件名称，取值为'sqliteErrorOccurred'，记录SQL语句执行过程中的错误信息。 |
| observer | Callback<ExceptionMessage> | 否 | 回调函数。该参数存在，则取消指定Callback监听回调，否则取消该event事件的所有监听回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('sqliteErrorOccurred');
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Unregister observer failed, code is ${code},message is ${message}`);
}
```

#### off('perfStat')20+

off(event: 'perfStat', observer?: Callback<SqlExecutionInfo>): void

取消订阅SQL统计信息。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 取消订阅事件名称。取值为'perfStat'，统计执行SQL的时间。 |
| observer | Callback<SqlExecutionInfo> | 否 | 回调函数，表示订阅时的回调函数。该参数存在，则取消指定Callback监听回调，否则取消该event事件的所有监听回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14800014 | The target instance is already closed. |

```ets
import { BusinessError } from '@kit.BasicServicesKit';

try {
  if (store != undefined) {
    (store as relationalStore.RdbStore).off('perfStat');
  }
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error(`Unregister observer failed, code is ${code},message is ${message}`);
}
```

#### emit10+

emit(event: string): void

通知通过[on](#ZH-CN_TOPIC_0000002553200595__on10)注册的进程间或者进程内监听事件。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | string | 是 | 通知订阅事件的名称，可自定义事件名称，不能与系统已有事件dataChange，autoSyncProgress，statistics名称重复。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800014 | The target instance is already closed. |
| 14800050 | Failed to obtain the subscription service. |

**示例：**

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).emit('storeObserver');
}
```

#### cleanDirtyData11+

cleanDirtyData(table: string, cursor: number, callback: AsyncCallback<void>): void

清理云端删除的数据同步到本地后，未自动清理的，且数据的游标（cursor）小于指定游标的数据。使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 表示当前数据库的表的名称。 |
| cursor | number | 是 | 整数类型，表示数据游标，小于此游标的脏数据将被清理。 |
| callback | AsyncCallback<void> | 是 | 指定的callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. 4. The cursor must be valid cursor. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).cleanDirtyData('test_table', 100, (err) => {
    if (err) {
      console.error(`clean dirty data failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('clean dirty data succeeded');
  });
}
```

#### cleanDirtyData11+

cleanDirtyData(table: string, callback: AsyncCallback<void>): void

清理云端删除的数据同步到本地后，未自动清理的所有数据。使用callback异步回调。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 表示当前数据库的表的名称。 |
| callback | AsyncCallback<void> | 是 | 指定的callback回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s). 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
if (store != undefined) {
  (store as relationalStore.RdbStore).cleanDirtyData('test_table', (err) => {
    if (err) {
      console.error(`clean dirty data failed, code is ${err.code},message is ${err.message}`);
      return;
    }
    console.info('clean dirty data succeeded');
  });
}
```

#### cleanDirtyData11+

cleanDirtyData(table: string, cursor?: number): Promise<void>

清理云端删除的数据同步到本地后，未自动清理的，且数据的游标（cursor）小于指定游标的数据，使用Promise异步回调。若无cursor参数，将全部清理。

**系统能力：** SystemCapability.DistributedDataManager.CloudSync.Client

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| table | string | 是 | 表示当前数据库的表的名称。 |
| cursor | number | 否 | 整数类型，表示数据游标，小于此游标的脏数据将被清理。当此参数不填时，清理当前表的所有脏数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Need 1 - 3 parameter(s)! 2. The RdbStore must be not nullptr. 3. The tablesNames must be not empty string. 4. The cursor must be valid cursor. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).cleanDirtyData('test_table', 100).then(() => {
    console.info('clean dirty data  succeeded');
  }).catch((err: BusinessError) => {
    console.error(`clean dirty data failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### attach12+

attach(fullPath: string, attachName: string, waitTime?: number) : Promise<number>

将一个数据库文件附加到当前数据库中，以便在SQL语句中可以直接访问附加数据库中的数据，使用Promise异步回调。

数据库文件来自文件，且此API不支持附加加密数据库。调用attach接口后，数据库切换为非WAL模式，性能会存在一定的劣化。

attach时，数据库会切换为非WAL模式，切换模式需要确保所有的ResultSet都已经Close，所有的写操作已经结束，否则会报错14800015。

attach不能并发调用，否则可能出现未响应情况并报错14800015，需要重试。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fullPath | string | 是 | 表示要附加的数据库的路径。 |
| attachName | string | 是 | 表示附加后的数据库的别名。 |
| waitTime | number | 否 | 表示附加数据库文件的等待时长。默认值2s，最小值1s，最大值300s。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回附加数据库的数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800016 | The database alias already exists. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
// 非加密数据库附加非加密数据库。
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).attach("/path/rdbstore1.db", "attachDB").then((number: number) => {
    console.info('attach succeeded');
  }).catch((err: BusinessError) => {
    console.error(`attach failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### attach12+

attach(context: Context, config: StoreConfig, attachName: string, waitTime?: number) : Promise<number>

将一个当前应用的数据库附加到当前数据库中，以便在SQL语句中可以直接访问附加数据库中的数据，使用Promise异步回调。

此API不支持加密数据库附加非加密数据库。调用attach接口后，数据库切换为非WAL模式，性能会存在一定的劣化。

attach时，数据库会切换为非WAL模式，切换模式需要确保所有的ResultSet都已经Close，所有的写操作已经结束，否则会报错14800015。

attach不能并发调用，否则可能出现未响应情况并报错14800015，需要重试。除此之外，attach附加加密数据库时，可能受到并发的影响，出现解密失败的情况，报错14800011，需要显式指定加密参数并重试。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | Context | 是 | 应用的上下文。 FA模型的应用Context定义见Context。 Stage模型的应用Context定义见Context。 |
| config | StoreConfig | 是 | 与此RDB存储相关的数据库配置。 |
| attachName | string | 是 | 表示附加后的数据库的别名。 |
| waitTime | number | 否 | 表示附加数据库文件的等待时长。默认值2s，最小值1s，最大值300s。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回附加数据库的数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 14800000 | Inner error. |
| 14800010 | Failed to open or delete the database by an invalid database path. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800016 | The database alias already exists. |
| 14801001 | The operation is supported in the stage model only. |
| 14801002 | Invalid data group ID. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例1：非加密数据库附加非加密数据库**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let attachStore: relationalStore.RdbStore | undefined = undefined;

const STORE_CONFIG1: relationalStore.StoreConfig = {
  name: "rdbstore1.db",
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.getRdbStore(this.context, STORE_CONFIG1).then(async (rdbStore: relationalStore.RdbStore) => {
  attachStore = rdbStore;
  console.info('Get RdbStore successfully.');
  if (store != undefined) {
    (store as relationalStore.RdbStore).attach(this.context, STORE_CONFIG1, "attachDB").then((number: number) => {
      console.info(`attach succeeded, number is ${number}`);
    }).catch((err: BusinessError) => {
      console.error(`attach failed, code is ${err.code},message is ${err.message}`);
    });
  }
}).catch((err: BusinessError) => {
  console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
});
```

**示例2：非加密数据库附加加密数据库**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let attachStore: relationalStore.RdbStore | undefined = undefined;

const STORE_CONFIG2: relationalStore.StoreConfig = {
  name: "rdbstore2.db",
  encrypt: true,
  securityLevel: relationalStore.SecurityLevel.S3
};

relationalStore.getRdbStore(this.context, STORE_CONFIG2).then(async (rdbStore: relationalStore.RdbStore) => {
  attachStore = rdbStore;
  console.info('Get RdbStore successfully.');
  if (store != undefined) {
    (store as relationalStore.RdbStore).attach(this.context, STORE_CONFIG2, "attachDB2", 10).then((number: number) => {
      console.info(`attach succeeded, number is ${number}`);
    }).catch((err: BusinessError) => {
      console.error(`attach failed, code is ${err.code},message is ${err.message}`);
    });
  }
}).catch((err: BusinessError) => {
  console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
});
```

#### detach12+

detach(attachName: string, waitTime?: number) : Promise<number>

将附加的数据库从当前数据库中分离，使用Promise异步回调。

当所有的附加的数据库被分离后，数据库会重新切换为WAL模式。

在detach之前，所有的数据库操作要确保已经结束，所有的ResultSet已经Close。并且不能并发调用，可能出现未响应情况，需要重试。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attachName | string | 是 | 表示附加后的数据库的别名。 |
| waitTime | number | 否 | 表示分离数据库的等待时长。默认值2s，最小值1s，最大值300s。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回分离后剩余附加的数据库的数量。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).detach("attachDB").then((number: number) => {
    console.info(`detach succeeded, number is ${number}`);
  }).catch((err: BusinessError) => {
    console.error(`detach failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### lockRow12+

lockRow(predicates: RdbPredicates):Promise<void>

根据RdbPredicates的指定实例对象从数据库中锁定数据，锁定数据不执行端云同步，使用Promise异步回调。

该接口只支持主键为基本类型的表、不支持共享表、无主键表和复合类型主键表。

该接口不支持依赖关系表之间的锁传递，如果表存在依赖关系，需要根据依赖关系手动调用该接口。

该接口不支持对已删除数据的操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的锁定条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800018 | No data meets the condition. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).lockRow(predicates).then(() => {
    console.info(`Lock success`);
  }).catch((err: BusinessError) => {
    console.error(`Lock failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### unlockRow12+

unlockRow(predicates: RdbPredicates):Promise<void>

根据RdbPredicates的指定实例对象从数据库中解锁数据，使用Promise异步回调。

该接口只支持主键为基本类型的表、不支持共享表、无主键表和复合类型主键表。

该接口不支持依赖关系表之间的锁传递，如果表存在依赖关系，需要根据依赖关系手动调用该接口。

该接口不支持对已删除数据的操作。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的锁定条件。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800018 | No data meets the condition. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Lisa");
if (store != undefined) {
  (store as relationalStore.RdbStore).unlockRow(predicates).then(() => {
    console.info(`Unlock success`);
  }).catch((err: BusinessError) => {
    console.error(`Unlock failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### queryLockedRow12+

queryLockedRow(predicates: RdbPredicates, columns?: Array<string>):Promise<ResultSet>

根据指定条件查询数据库中锁定的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| predicates | RdbPredicates | 是 | RdbPredicates的实例对象指定的查询条件。 |
| columns | Array<string> | 否 | 表示要查询的列。如果值为空，则查询应用于所有列。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<ResultSet> | Promise对象。如果操作成功，则返回ResultSet对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](../../guides/数据库备份与恢复.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14800000 | Inner error. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800022 | SQLite: Callback routine requested an abort. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800025 | SQLite: A table in the database is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |
| 14800030 | SQLite: Unable to open the database file. |
| 14800031 | SQLite: TEXT or BLOB exceeds size limit. |
| 14800032 | SQLite: Abort due to constraint violation. |
| 14800033 | SQLite: Data type mismatch. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

let predicates = new relationalStore.RdbPredicates("EMPLOYEE");
predicates.equalTo("NAME", "Rose");
if (store != undefined) {
  (store as relationalStore.RdbStore).queryLockedRow(predicates, ["ID", "NAME", "AGE", "SALARY", "CODES"]).then(async (resultSet: relationalStore.ResultSet) => {
    console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
    // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
    try {
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex("ID"));
        const name = resultSet.getString(resultSet.getColumnIndex("NAME"));
        const age = resultSet.getLong(resultSet.getColumnIndex("AGE"));
        const salary = resultSet.getDouble(resultSet.getColumnIndex("SALARY"));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
    } catch (err) {
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    } finally {
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
    }
  }).catch((err: BusinessError) => {
    console.error(`Query failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### close12+

close(): Promise<void>

关闭数据库，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: The RdbStore verification failed. |
| 14800000 | Inner error. |

**示例：**

```ets
import { BusinessError } from '@kit.BasicServicesKit';

if (store != undefined) {
  (store as relationalStore.RdbStore).close().then(() => {
    console.info(`close succeeded`);
  }).catch((err: BusinessError) => {
    console.error(`close failed, code is ${err.code},message is ${err.message}`);
  });
}
```

#### rekey20+

rekey(cryptoParam?: CryptoParam): Promise<void>

手动更新加密数据库的密钥。使用Promise异步回调。

不支持对非WAL模式的数据库进行密钥更新。

手动更新密钥时需要独占访问数据库，此时若存在任何未释放的结果集（ResultSet）、事务（Transaction）或其他进程打开的数据库均会引发失败。

仅支持加密数据库进行密钥更新，不支持非加密数据库变加密数据库及加密数据库变非加密数据库，且需要保持加密参数和密钥生成方式与建库时一致。

数据库越大，密钥更新所需的时间越长。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cryptoParam | CryptoParam | 否 | 指定用户自定义的加密参数。 当此参数不填时，使用默认的加密参数，见CryptoParam。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800015 | The database does not respond. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |

**示例：**

示例代码中this.context定义见Stage模型的应用[Context](Context (Stage模型的上下文基类).md)。

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 示例1：使用默认的加密参数
export default class EntryAbility extends UIAbility {
  onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    const STORE_CONFIG1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true
    };

    relationalStore.getRdbStore(this.context, STORE_CONFIG1).then(async (rdbStore: relationalStore.RdbStore) => {
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam1: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array()
      };

      if (store != undefined) {
        try {
          (store as relationalStore.RdbStore).rekey(cryptoParam1);
          console.info('rekey is successful');
        } catch (err) {
          console.error(`rekey is failed, code is ${err.code},message is ${err.message}`);
        }
    }).catch((err: BusinessError) => {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    });
}
```

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 示例2：使用自定义的加密参数
export default class EntryAbility extends UIAbility {
  onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    let cryptoParam: relationalStore.CryptoParam = {
      encryptionKey: new Uint8Array([1, 2, 3, 4, 5, 6]),
      iterationCount: 1000,
      encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
      hmacAlgo: relationalStore.HmacAlgo.SHA256,
      kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
      cryptoPageSize: 1024
    };

    const STORE_CONFIG2: relationalStore.StoreConfig = {
      name: 'rdbstore2.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true,
      cryptoParam: cryptoParam
    };

    relationalStore.getRdbStore(this.context, STORE_CONFIG2).then(async (rdbStore: relationalStore.RdbStore) => {
      store = rdbStore;
      console.info('Get RdbStore successfully.');
      let cryptoParam2: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array([6, 5, 4, 3, 2, 1]),
        iterationCount: 1000,
        encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
        hmacAlgo: relationalStore.HmacAlgo.SHA256,
        kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
        cryptoPageSize: 1024
      };

      if (store != undefined) {
        try {
          (store as relationalStore.RdbStore).rekey(cryptoParam2);
          console.info('rekey is successful');
        } catch (err) {
          console.error(`rekey is failed, code is ${err.code},message is ${err.message}`);
        }
    }).catch((err: BusinessError) => {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    });
}
```

#### setLocale20+

setLocale(locale: string) : Promise<void>

设置自定义排序的语言。使用Promise异步回调。

该值符合ISO 639标准，但是仅支持ICU中的部分语言，对于不支持的语言，设置自定义排序的语言时会报错14800001。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locale | string | 是 | 设置自定义排序的语言。该值符合ISO 639标准，如："zh"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800014 | The target instance is already closed. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800034 | SQLite: Library used incorrectly. |

**示例：**

```ets
try {
  if (store != undefined) {
    await store.setLocale("zh");
    store.querySql("SELECT * FROM EMPLOYEE ORDER BY NAME COLLATE LOCALES", async (err, resultSet) => {
      if (err) {
        console.error(`Query failed, code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info(`ResultSet rowCount ${resultSet.rowCount}`);
    });
  }
} catch (err) {
  console.error(`SetLocale failed, code: ${err.code}, message: ${err.message}`);
}
```

#### rekeyEx22+

rekeyEx(cryptoParam: CryptoParam): Promise<void>

手动更新数据库的密钥或加密参数，使用Promise异步回调。

不支持对非WAL模式的数据库进行密钥更新。

手动更新时需要独占访问数据库，此时若存在任何未释放的结果集（ResultSet）、事务（Transaction）或其他进程打开的数据库均会导致更新失败。

支持加密数据库的参数更新，以及加密数据库与非加密数据库之间的相互转换。

数据库越大，执行更新所需的时间越长。

加密参数变更需谨慎，在完成rekeyEx操作后，[getRdbStore](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529284675__relationalstoregetrdbstore-1)时必须使用新的参数来打开数据库，否则可能会导致开库失败。

如果rekey过程因设备断电等原因中断，操作可能成功也可能失败。因此，建议业务方做好兜底保障（使用RekeyEx前后的参数进行冗余重试），确保不会错误地判断数据库的状态，从而避免出现数据库无法打开的问题。

如果有加密参数变更，不建议[getRdbStore](../../topics/misc/Functions.md#ZH-CN_TOPIC_0000002529284675__relationalstoregetrdbstore-1)时使用AllowedRebuild参数，防止因为传入的错误加密参数导致数据库发生重建。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cryptoParam | CryptoParam | 是 | 指定用户自定义的加密参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](通用错误码.md)和[关系型数据库错误码](关系型数据库错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 14800001 | Invalid arguments. Possible causes: 1.Parameter is out of valid range. |
| 14800011 | The current operation failed because the database is corrupted. |
| 14800014 | The target instance is already closed. |
| 14800021 | SQLite: Generic error. |
| 14800023 | SQLite: Access permission denied. |
| 14800024 | SQLite: The database file is locked. |
| 14800026 | SQLite: The database is out of memory. |
| 14800027 | SQLite: Attempt to write a readonly database. |
| 14800028 | SQLite: Some kind of disk I/O error occurred. |
| 14800029 | SQLite: The database is full. |

**示例1：原数据库为默认参数加密数据库，更换密钥和加密参数**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array(),
        encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_CBC,
        hmacAlgo: relationalStore.HmacAlgo.SHA256,
        kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
        iterationCount: 1000,
        cryptoPageSize: 2048,
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
        }
      // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
    } catch (err) {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    };
}
```

**示例2：原数据库为自定义参数加密数据库，更换自定义密钥和加密参数**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    let cryptoParam: relationalStore.CryptoParam = {
      // 安全提醒：1.空数组encryptionKey表示使用系统生成的密钥（仅适用于部分场景）；2.生产环境应使用应用沙箱密钥或安全存储服务管理密钥，不要在代码中硬编码固定密钥
      encryptionKey: new Uint8Array([1, 2, 3, 4, 5, 6]),
      iterationCount: 1000,
      encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
      hmacAlgo: relationalStore.HmacAlgo.SHA256,
      kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
      cryptoPageSize: 1024
    };
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true,
      cryptoParam: cryptoParam
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam1: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array([6, 5, 4, 3, 2, 1]),
        iterationCount: 5000,
        encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_CBC,
        hmacAlgo: relationalStore.HmacAlgo.SHA512,
        kdfAlgo: relationalStore.KdfAlgo.KDF_SHA512,
        cryptoPageSize: 2048
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam1);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
        }
      // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
    } catch (err) {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    };
}
```

**示例3：原数据库为默认参数加密库，更换自定义密钥和加密参数**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam: relationalStore.CryptoParam = {
        // 安全提醒：1.空数组encryptionKey表示使用系统生成的密钥（仅适用于部分场景）；2.生产环境应使用应用沙箱密钥或安全存储服务管理密钥，不要在代码中硬编码固定密钥
        encryptionKey: new Uint8Array([6, 5, 4, 3, 2, 1]),
        encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_CBC,
        hmacAlgo: relationalStore.HmacAlgo.SHA256,
        kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
        iterationCount: 1000,
        cryptoPageSize: 2048,
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
        }
      // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
    } catch (err) {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    };
}
```

**示例4：原数据库为自定义参数加密数据库，更换数据库生成密钥和自定义加密参数**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    let cryptoParam: relationalStore.CryptoParam = {
      // 安全提醒：1.空数组encryptionKey表示使用系统生成的密钥（仅适用于部分场景）；2.生产环境应使用应用沙箱密钥或安全存储服务管理密钥，不要在代码中硬编码固定密钥
      encryptionKey: new Uint8Array([1, 2, 3, 4, 5, 6]),
      iterationCount: 1000,
      encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
      hmacAlgo: relationalStore.HmacAlgo.SHA256,
      kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
      cryptoPageSize: 1024
    };
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore2.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true,
      cryptoParam: cryptoParam
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam1: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array(),
        iterationCount: 5000,
        encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_CBC,
        hmacAlgo: relationalStore.HmacAlgo.SHA512,
        kdfAlgo: relationalStore.KdfAlgo.KDF_SHA512,
        cryptoPageSize: 2048
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam1);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
        }
      // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
    } catch (err) {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    };
}
```

**示例5：原数据库为自定义参数加密数据库，更换为非加密数据库**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    let cryptoParam: relationalStore.CryptoParam = {
      // 安全提醒：1.空数组encryptionKey表示使用系统生成的密钥（仅适用于部分场景）；2.生产环境应使用应用沙箱密钥或安全存储服务管理密钥，不要在代码中硬编码固定密钥
      encryptionKey: new Uint8Array([1, 2, 3, 4, 5, 6]),
      iterationCount: 1000,
      encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
      hmacAlgo: relationalStore.HmacAlgo.SHA256,
      kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
      cryptoPageSize: 1024
    };
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: true,
      cryptoParam: cryptoParam
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam1: relationalStore.CryptoParam = {
        encryptionKey: new Uint8Array(),
        encryptionAlgo: relationalStore.EncryptionAlgo.PLAIN_TEXT
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam1);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
        }
      // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
    } catch (err) {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    };
}
```

**示例6：原数据库为非加密数据库，更换为自定义参数加密数据库**

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  async onCreate() {
    let store: relationalStore.RdbStore | undefined = undefined;
    const configV1: relationalStore.StoreConfig = {
      name: 'rdbstore1.db',
      securityLevel: relationalStore.SecurityLevel.S3,
      encrypt: false,
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, configV1);
      store = rdbStore;
      console.info('Get RdbStore successfully.');

      let cryptoParam: relationalStore.CryptoParam = {
        // 安全提醒：1.空数组encryptionKey表示使用系统生成的密钥（仅适用于部分场景）；2.生产环境应使用应用沙箱密钥或安全存储服务管理密钥，不要在代码中硬编码固定密钥
        encryptionKey: new Uint8Array([1, 2, 3, 4, 5, 6]),
        iterationCount: 1000,
        encryptionAlgo: relationalStore.EncryptionAlgo.AES_256_GCM,
        hmacAlgo: relationalStore.HmacAlgo.SHA256,
        kdfAlgo: relationalStore.KdfAlgo.KDF_SHA256,
        cryptoPageSize: 1024
      };

      if (store != undefined) {
        try {
          await (store as relationalStore.RdbStore).rekeyEx(cryptoParam);
          console.info('rekeyEx is successful');
        } catch (err) {
          console.error(`rekeyEx is failed, code is ${err.code},message is ${err.message}`);
        }
      // 在完成rekeyEx操作后，如果后续需要重新getRdbStore时必须使用新的参数来打开数据库
    } catch (err) {
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    };
  }
```