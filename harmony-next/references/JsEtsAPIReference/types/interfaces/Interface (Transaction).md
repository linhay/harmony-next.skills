# Interface (Transaction)

提供以事务方式管理数据库的方法。事务对象是通过[createTransaction](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__createtransaction14)接口创建的，不同事务对象之间的操作是隔离的，不同类型事务的区别见[TransactionType](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604686__transactiontype14) 。

当前关系型数据库同一时刻仅支持一个写事务，所以如果当前[RdbStore](Interface (RdbStore).md)存在写事务未释放，创建IMMEDIATE或EXCLUSIVE事务会返回14800024错误码。如果是创建的DEFERRED事务，则可能在首次使用DEFERRED事务调用写操作时返回14800024错误码。通过IMMEDIATE或EXCLUSIVE创建写事务或者DEFERRED事务升级到写事务之后，[RdbStore](Interface (RdbStore).md)的写操作也会返回14800024错误码。

当事务并发量较高且写事务持续时间较长时，返回14800024错误码的次数可能会变多，开发者可以通过减少事务占用时长减少14800024出现的次数，也可以通过重试的方式处理14800024错误码。

在使用以下API前，请先通过[createTransaction](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__createtransaction14)方法获取Transaction实例，再通过此实例调用对应方法。

-

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

-

本Interface首批接口从API version 14开始支持。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**示例：**

示例代码中this.context定义见Stage模型的应用[Context](../../topics/graphics/Context (Stage模型的上下文基类).md)。

```ets
import { UIAbility } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';

let store: relationalStore.RdbStore | undefined = undefined;

export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage) {
    const STORE_CONFIG: relationalStore.StoreConfig = {
      name: 'RdbTest.db',
      securityLevel: relationalStore.SecurityLevel.S3
    };

    try {
      const rdbStore = await relationalStore.getRdbStore(this.context, STORE_CONFIG);
      store = rdbStore;
      console.info('Get RdbStore successfully.');
    } catch (error) {
      const err = error as BusinessError;
      console.error(`Get RdbStore failed, code is ${err.code},message is ${err.message}`);
    }

    if (store != undefined) {
      await store.executeSql('CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB, IDENTITY UNLIMITED INT, ASSETDATA ASSET, ASSETSDATA ASSETS, FLOATARRAY floatvector(128))');
      store.createTransaction().then(async (transaction: relationalStore.Transaction) => {
        console.info(`createTransaction success`);
        // 成功获取到事务对象后执行后续操作
      }).catch((err: BusinessError) => {
        console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
      });
    }
  }
}
```

#### 导入模块

```ets
import { relationalStore } from '@kit.ArkData';
```

#### commit14+

commit(): Promise<void>

提交已执行的SQL语句，使用Promise异步回调。如果是使用异步接口执行sql语句，请确保异步接口执行完成之后再调用commit接口，否则可能会丢失SQL操作。调用commit接口之后，该Transaction对象及创建的ResultSet对象都将被关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.

**示例：**

```ets
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      await transaction.execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER, salary REAL)');
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### rollback14+

rollback(): Promise<void>

回滚已经执行的SQL语句，使用Promise异步回调。调用rollback接口之后，该Transaction对象及创建的ResultSet对象都会被关闭。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**返回值**：

类型说明Promise<void>无返回结果的Promise对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.

**示例：**

```ets
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      await transaction.execute('DELETE FROM TEST WHERE age = ? OR age = ?', ['18', '20']);
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`execute sql failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### insert14+

insert(table: string, values: ValuesBucket, conflict?: ConflictResolution): Promise<number>

向目标表中插入一行数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__query)或[querySql](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002497604684__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002497604684__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明tablestring是指定的目标表名。values[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)是表示要插入到表中的数据行。conflict[ConflictResolution](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)否指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON_CONFLICT_NONE。

**返回值**：

类型说明Promise<number>Promise对象。如果操作成功，返回行ID；否则返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800033SQLite: Data type mismatch.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
const valueBucket1: relationalStore.ValuesBucket = {
  NAME: 'Lisa',
  AGE: 18,
  SALARY: 100.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const rowId = await transaction.insert('EMPLOYEE', valueBucket1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
      await transaction.commit();
      console.info(`Insert is successful, rowId = ${rowId}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Insert is failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### insertSync14+

insertSync(table: string, values: ValuesBucket | sendableRelationalStore.ValuesBucket, conflict?: ConflictResolution): number

向目标表中插入一行数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__query)或[querySql](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002497604684__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002497604684__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明tablestring是指定的目标表名。values[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket) | [sendableRelationalStore.ValuesBucket](../../modules/ohos/@ohos.data.sendableRelationalStore (共享关系型数据库).md#ZH-CN_TOPIC_0000002529284679__valuesbucket)是表示要插入到表中的数据行。conflict[ConflictResolution](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)否指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON_CONFLICT_NONE。

**返回值**：

类型说明number如果操作成功，返回行ID；否则返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800033SQLite: Data type mismatch.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
let value5 = 'Lisa';
let value6 = 18;
let value7 = 100.5;
let value8 = new Uint8Array([1, 2, 3, 4, 5]);

const valueBucket2: relationalStore.ValuesBucket = {
  NAME: value5,
  AGE: value6,
  SALARY: value7,
  CODES: value8
};
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let rowId: number = transaction.insertSync(
        'EMPLOYEE',
        valueBucket2,
        relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
      );
      await transaction.commit();
      console.info(`Insert is successful, rowId = ${rowId}`);
    } catch (e) {
      await transaction.rollback();
      console.error(`Insert is failed, code is ${e.code},message is ${e.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### batchInsert14+

batchInsert(table: string, values: Array<ValuesBucket>): Promise<number>

向目标表中插入一组数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明tablestring是指定的目标表名。valuesArray<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>是表示要插入到表中的一组数据。

**返回值**：

类型说明Promise<number>Promise对象。如果操作成功，返回插入的数据个数，否则返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800033SQLite: Data type mismatch.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
const valueBucket3: relationalStore.ValuesBucket = {
  NAME: 'Lisa',
  AGE: 18,
  SALARY: 100.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
const valueBucket4: relationalStore.ValuesBucket = {
  NAME: 'Jack',
  AGE: 19,
  SALARY: 101.5,
  CODES: new Uint8Array([6, 7, 8, 9, 10])
};
const valueBucket5: relationalStore.ValuesBucket = {
  NAME: 'Tom',
  AGE: 20,
  SALARY: 102.5,
  CODES: new Uint8Array([11, 12, 13, 14, 15])
};

let valueBuckets = new Array(valueBucket3, valueBucket4, valueBucket5);
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const insertNum = await transaction.batchInsert('EMPLOYEE', valueBuckets);
      await transaction.commit();
      console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### batchInsertSync14+

batchInsertSync(table: string, values: Array<ValuesBucket>): number

向目标表中插入一组数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明tablestring是指定的目标表名。valuesArray<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>是表示要插入到表中的一组数据。

**返回值**：

类型说明number如果操作成功，返回插入的数据个数，否则返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800033SQLite: Data type mismatch.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
const valueBucket6: relationalStore.ValuesBucket = {
  NAME: 'Lisa',
  AGE: 18,
  SALARY: 100.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
const valueBucket7: relationalStore.ValuesBucket = {
  NAME: 'Jack',
  AGE: 19,
  SALARY: 101.5,
  CODES: new Uint8Array([6, 7, 8, 9, 10])
};
const valueBucket8: relationalStore.ValuesBucket = {
  NAME: 'Tom',
  AGE: 20,
  SALARY: 102.5,
  CODES: new Uint8Array([11, 12, 13, 14, 15])
};

let valueBuckets2 = new Array(valueBucket6, valueBucket7, valueBucket8);
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let insertNum: number = (transaction as relationalStore.Transaction).batchInsertSync('EMPLOYEE', valueBuckets2);
      await transaction.commit();
      console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### batchInsertWithConflictResolution18+

batchInsertWithConflictResolution(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): Promise<number>

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)，使用Promise异步回调。

单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明tablestring是指定的目标表名。valuesArray<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>是表示要插入到表中的一组数据。conflict[ConflictResolution](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)是指定冲突解决模式。如果是ON_CONFLICT_ROLLBACK模式，当发生冲突时会回滚整个事务。

**返回值**：

类型说明Promise<number>Promise对象。如果操作成功，返回插入的数据个数，否则返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800022SQLite: Callback routine requested an abort.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800032SQLite: Abort due to constraint violation.14800033SQLite: Data type mismatch.14800034SQLite: Library used incorrectly.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
const valueBucket9: relationalStore.ValuesBucket = {
  NAME: 'Lisa',
  AGE: 18,
  SALARY: 100.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
const valueBucketA: relationalStore.ValuesBucket = {
  NAME: 'Jack',
  AGE: 19,
  SALARY: 101.5,
  CODES: new Uint8Array([6, 7, 8, 9, 10])
};
const valueBucketB: relationalStore.ValuesBucket = {
  NAME: 'Tom',
  AGE: 20,
  SALARY: 102.5,
  CODES: new Uint8Array([11, 12, 13, 14, 15])
};

let valueBuckets3 = new Array(valueBucket9, valueBucketA, valueBucketB);

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const insertNum = await transaction.batchInsertWithConflictResolution(
        'EMPLOYEE',
        valueBuckets3,
        relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
      );
      await transaction.commit();
      console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### batchInsertWithConflictResolutionSync18+

batchInsertWithConflictResolutionSync(table: string, values: Array<ValuesBucket>, conflict: ConflictResolution): number

向目标表中插入一组数据，可以通过conflict参数指定冲突解决模式[ConflictResolution](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)。

单次插入参数的最大数量限制为32766，超出上限会返回14800000错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明tablestring是指定的目标表名。valuesArray<[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)>是表示要插入到表中的一组数据。conflict[ConflictResolution](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)是指定冲突解决模式。如果是ON_CONFLICT_ROLLBACK模式，当发生冲突时会回滚整个事务。

**返回值**：

类型说明number如果操作成功，返回插入的数据个数，否则返回-1。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800022SQLite: Callback routine requested an abort.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800032SQLite: Abort due to constraint violation.14800033SQLite: Data type mismatch.14800034SQLite: Library used incorrectly.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
const valueBucketC: relationalStore.ValuesBucket = {
  NAME: 'Lisa',
  AGE: 18,
  SALARY: 100.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
const valueBucketD: relationalStore.ValuesBucket = {
  NAME: 'Jack',
  AGE: 19,
  SALARY: 101.5,
  CODES: new Uint8Array([6, 7, 8, 9, 10])
};
const valueBucketE: relationalStore.ValuesBucket = {
  NAME: 'Tom',
  AGE: 20,
  SALARY: 102.5,
  CODES: new Uint8Array([11, 12, 13, 14, 15])
};

let valueBuckets4 = new Array(valueBucketC, valueBucketD, valueBucketE);
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const insertNum = transaction.batchInsertWithConflictResolutionSync(
        'EMPLOYEE',
        valueBuckets4,
        relationalStore.ConflictResolution.ON_CONFLICT_REPLACE
      );
      await transaction.commit();
      console.info(`batchInsert is successful, the number of values that were inserted = ${insertNum}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`batchInsert is failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### update14+

update(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): Promise<number>

根据RdbPredicates的指定实例对象更新数据库中的数据，使用Promise异步回调。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__query)或[querySql](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002497604684__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002497604684__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明values[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)是values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。predicates[RdbPredicates](../classes/Class (RdbPredicates).md)是RdbPredicates的实例对象指定的更新条件。conflict[ConflictResolution](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)否指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON_CONFLICT_NONE。

**返回值**：

类型说明Promise<number>指定的Promise回调方法。返回受影响的行数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800033SQLite: Data type mismatch.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
const valueBucketF: relationalStore.ValuesBucket = {
  NAME: 'Rose',
  AGE: 22,
  SALARY: 200.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
let predicates = new relationalStore.RdbPredicates('EMPLOYEE');
predicates.equalTo('NAME', 'Lisa');

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const rows = await transaction.update(valueBucketF, predicates, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
      await transaction.commit();
      console.info(`Updated row count: ${rows}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### updateSync14+

updateSync(values: ValuesBucket, predicates: RdbPredicates, conflict?: ConflictResolution): number

根据RdbPredicates的指定实例对象更新数据库中的数据。由于共享内存的大小限制为2MB，因此单条数据的大小也必须严格小于2MB。如果单条数据超过此限制，在后续通过RdbStore的[query](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__query)或[querySql](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__querysql)接口获取ResultSet后，调用[getValue](Interface (ResultSet).md#ZH-CN_TOPIC_0000002497604684__getvalue12)、[getString](Interface (ResultSet).md#ZH-CN_TOPIC_0000002497604684__getstring)等get方法时将无法成功获取数据，并可能导致操作失败或抛出异常。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明values[ValuesBucket](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuesbucket)是values指示数据库中要更新的数据行。键值对与数据库表的列名相关联。predicates[RdbPredicates](../classes/Class (RdbPredicates).md)是RdbPredicates的实例对象指定的更新条件。conflict[ConflictResolution](../../topics/misc/Enums.md#ZH-CN_TOPIC_0000002497604686__conflictresolution10)否指定冲突解决模式。默认值是relationalStore.ConflictResolution.ON_CONFLICT_NONE。

**返回值**：

类型说明number返回受影响的行数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800033SQLite: Data type mismatch.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
const valueBucketG: relationalStore.ValuesBucket = {
  NAME: 'Rose',
  AGE: 22,
  SALARY: 200.5,
  CODES: new Uint8Array([1, 2, 3, 4, 5])
};
let predicates1 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates1.equalTo('NAME', 'Lisa');

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let rows = transaction.updateSync(valueBucketG, predicates1, relationalStore.ConflictResolution.ON_CONFLICT_REPLACE);
      await transaction.commit();
      console.info(`Updated row count: ${rows}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Updated failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### delete14+

delete(predicates: RdbPredicates):Promise<number>

根据RdbPredicates的指定实例对象从数据库中删除数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明predicates[RdbPredicates](../classes/Class (RdbPredicates).md)是RdbPredicates的实例对象指定的删除条件。

**返回值**：

类型说明Promise<number>Promise对象。返回受影响的行数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800033SQLite: Data type mismatch.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
let predicates2 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates2.equalTo('NAME', 'Lisa');

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const rows = await transaction.delete(predicates2);
      await transaction.commit();
      console.info(`Delete rows: ${rows}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### deleteSync14+

deleteSync(predicates: RdbPredicates): number

根据RdbPredicates的指定实例对象从数据库中删除数据。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明predicates[RdbPredicates](../classes/Class (RdbPredicates).md)是RdbPredicates的实例对象指定的删除条件。

**返回值**：

类型说明number返回受影响的行数。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800033SQLite: Data type mismatch.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
let predicates3 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates3.equalTo('NAME', 'Lisa');
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let rows = transaction.deleteSync(predicates3);
      await transaction.commit();
      console.info(`Delete rows: ${rows}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Delete failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### query14+

query(predicates: RdbPredicates, columns?: Array<string>): Promise<ResultSet>

根据指定条件查询数据库中的数据，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明predicates[RdbPredicates](../classes/Class (RdbPredicates).md)是RdbPredicates的实例对象指定的查询条件。columnsArray<string>否表示要查询的列。如果值为空，则查询应用于所有列。

**返回值**：

类型说明Promise<[ResultSet](Interface (ResultSet).md)>Promise对象。如果操作成功，则返回ResultSet对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800026SQLite: The database is out of memory.14800028SQLite: Some kind of disk I/O error occurred.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
let predicates4 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates4.equalTo('NAME', 'Rose');

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const resultSet = await transaction.query(predicates4, ['ID', 'NAME', 'AGE', 'SALARY', 'CODES']);
      console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
      // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
        const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
        const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
        const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### querySync14+

querySync(predicates: RdbPredicates, columns?: Array<string>): ResultSet

根据指定条件查询数据库中的数据。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](../../modules/ohos/@ohos.taskpool（启动任务池）.md)线程中执行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明predicates[RdbPredicates](../classes/Class (RdbPredicates).md)是RdbPredicates的实例对象指定的查询条件。columnsArray<string>否表示要查询的列。如果值为空，则查询应用于所有列。默认值为空。

**返回值**：

类型说明[ResultSet](Interface (ResultSet).md)如果操作成功，则返回ResultSet对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800028SQLite: Some kind of disk I/O error occurred.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
let predicates5 = new relationalStore.RdbPredicates('EMPLOYEE');
predicates5.equalTo('NAME', 'Rose');

if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let resultSet = transaction.querySync(predicates5, ['ID', 'NAME', 'AGE', 'SALARY', 'CODES']);
      console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
      // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
        const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
        const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
        const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### querySql14+

querySql(sql: string, args?: Array<ValueType>): Promise<ResultSet>

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个，使用Promise异步回调。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明sqlstring是指定要执行的SQL语句。argsArray<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>否SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。

**返回值**：

类型说明Promise<[ResultSet](Interface (ResultSet).md)>Promise对象。如果操作成功，则返回ResultSet对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800028SQLite: Some kind of disk I/O error occurred.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const resultSet = await transaction.querySql("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'");
      console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
      // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
        const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
        const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
        const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### querySqlSync14+

querySqlSync(sql: string, args?: Array<ValueType>): ResultSet

根据指定SQL语句查询数据库中的数据，SQL语句中的各种表达式和操作符之间的关系操作符号不超过1000个。对query同步接口获得的resultSet进行操作时，若逻辑复杂且循环次数过多，可能造成freeze问题，建议将此步骤放到[taskpool](../../modules/ohos/@ohos.taskpool（启动任务池）.md)线程中执行。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明sqlstring是指定要执行的SQL语句。argsArray<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>否SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。默认值为空。

**返回值**：

类型说明[ResultSet](Interface (ResultSet).md)如果操作成功，则返回ResultSet对象。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800028SQLite: Some kind of disk I/O error occurred.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      let resultSet = transaction.querySqlSync("SELECT * FROM EMPLOYEE CROSS JOIN BOOK WHERE BOOK.NAME = 'sanguo'");
      console.info(`ResultSet column names: ${resultSet.columnNames}, column count: ${resultSet.columnCount}`);
      // resultSet是一个数据集合的游标，默认指向第-1个记录，有效的数据从0开始。
      while (resultSet.goToNextRow()) {
        const id = resultSet.getLong(resultSet.getColumnIndex('ID'));
        const name = resultSet.getString(resultSet.getColumnIndex('NAME'));
        const age = resultSet.getLong(resultSet.getColumnIndex('AGE'));
        const salary = resultSet.getDouble(resultSet.getColumnIndex('SALARY'));
        console.info(`id=${id}, name=${name}, age=${age}, salary=${salary}`);
      }
      // 释放数据集的内存，若不释放可能会引起fd泄露与内存泄露
      resultSet.close();
      await transaction.commit();
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`Query failed, code is ${err.code},message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### execute14+

execute(sql: string, args?: Array<ValueType>): Promise<ValueType>

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为ValueType，使用Promise异步回调。

该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。

此接口不支持执行查询、附加数据库和事务操作，查询可以使用[querySql](#ZH-CN_TOPIC_0000002497444706__querysql14)、[query](#ZH-CN_TOPIC_0000002497444706__query14)接口代替、附加数据库可以使用[attach](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__attach12)接口代替。

不支持分号分隔的多条语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明sqlstring是指定要执行的SQL语句。argsArray<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>否SQL语句中参数的值。该值与sql参数语句中的占位符相对应。当sql参数语句完整时，该参数不填。

**返回值**：

类型说明Promise<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>Promise对象，返回sql执行后的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported the sql(attach,begin,commit,rollback etc.).14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800033SQLite: Data type mismatch.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      // 删除表中所有数据
      const SQL_DELETE_TABLE = 'DELETE FROM EMPLOYEE';
      const data = await transaction.execute(SQL_DELETE_TABLE);
      await transaction.commit();
      console.info(`delete result: ${data}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`delete failed, code is ${err.code}, message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```

#### executeSync14+

executeSync(sql: string, args?: Array<ValueType>): ValueType

执行包含指定参数的SQL语句，语句中的各种表达式和操作符之间的关系操作符号不超过1000个，返回值类型为ValueType。

该接口支持执行增删改操作，支持执行PRAGMA语法的sql，支持对表的操作（建表、删表、修改表），返回结果类型由执行具体sql的结果决定。

此接口不支持执行查询、附加数据库和事务操作，查询可以使用[querySql](#ZH-CN_TOPIC_0000002497444706__querysql14)、[query](#ZH-CN_TOPIC_0000002497444706__query14)接口代替、附加数据库可以使用[attach](Interface (RdbStore).md#ZH-CN_TOPIC_0000002529444649__attach12)接口代替。

不支持分号分隔的多条语句。

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**参数：**

参数名类型必填说明sqlstring是指定要执行的SQL语句。argsArray<[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)>否SQL语句中参数的值。该值与sql参数语句中的占位符相对应。该参数不填，或者填null或undefined，都认为是sql参数语句完整。默认值为空。

**返回值**：

类型说明[ValueType](../../topics/misc/Types.md#ZH-CN_TOPIC_0000002497444708__valuetype)返回sql执行后的结果。

**错误码：**

以下错误码的详细介绍请参见[通用错误码](../../errors/通用错误码.md)和[关系型数据库错误码](../../errors/关系型数据库错误码.md)。其中，14800011错误码处理可参考[数据库备份与恢复](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-backup-and-restore)。

**错误码ID****错误信息**401Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed.801Capability not supported the sql(attach,begin,commit,rollback etc.).14800000Inner error.14800011Failed to open the database because it is corrupted.14800014The RdbStore or ResultSet is already closed.14800021SQLite: Generic error. Possible causes: Insert failed or the updated data does not exist.14800023SQLite: Access permission denied.14800024SQLite: The database file is locked.14800025SQLite: A table in the database is locked.14800026SQLite: The database is out of memory.14800027SQLite: Attempt to write a readonly database.14800028SQLite: Some kind of disk I/O error occurred.14800029SQLite: The database is full.14800031SQLite: TEXT or BLOB exceeds size limit.14800033SQLite: Data type mismatch.14800047The WAL file size exceeds the default limit.

**示例：**

```ets
// 删除表中所有数据
if (store != undefined) {
  try {
    const transaction = await store.createTransaction();
    try {
      const SQL_DELETE_TABLE = 'DELETE FROM EMPLOYEE';
      let data = transaction.executeSync(SQL_DELETE_TABLE);
      await transaction.commit();
      console.info(`delete result: ${data}`);
    } catch (error) {
      const err = error as BusinessError;
      await transaction.rollback();
      console.error(`delete failed, code is ${err.code}, message is ${err.message}`);
    }
  } catch (error) {
    const err = error as BusinessError;
    console.error(`createTransaction failed, code is ${err.code},message is ${err.message}`);
  }
}
```