# oh_rdb_transaction.h

#### 概述

提供与数据库事务相关的函数和枚举。

**引用文件：** <database/rdb/oh_rdb_transaction.h>

**库：** libnative_rdb_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 18

**相关模块：**[RDB](RDB.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_RDB_TransOptions](OH_RDB_TransOptions.md)OH_RDB_TransOptions定义[OH_RDB_TransOptions](OH_RDB_TransOptions.md)结构类型。[OH_Rdb_Transaction](OH_Rdb_Transaction.md)OH_Rdb_Transaction定义[OH_RDB_TransOptions](OH_RDB_TransOptions.md)结构类型。

#### 枚举

名称typedef关键字描述[OH_RDB_TransType](#ZH-CN_TOPIC_0000002529444669__oh_rdb_transtype)OH_RDB_TransType表示关系型数据库事务类型。

#### 函数

名称描述[OH_RDB_TransOptions *OH_RdbTrans_CreateOptions(void)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_createoptions)创建事务配置对象。[int OH_RdbTrans_DestroyOptions(OH_RDB_TransOptions *options)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_destroyoptions)销毁事务配置对象。[int OH_RdbTransOption_SetType(OH_RDB_TransOptions *options, OH_RDB_TransType type)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtransoption_settype)设置关系型数据库事务类型。[int OH_RdbTrans_Commit(OH_Rdb_Transaction *trans)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_commit)提交事务。[int OH_RdbTrans_Rollback(OH_Rdb_Transaction *trans)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_rollback)回滚事务。[int OH_RdbTrans_Insert(OH_Rdb_Transaction *trans, const char *table, const OH_VBucket *row, int64_t *rowId)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_insert)将一行数据插入到目标表中。[int OH_RdbTrans_InsertWithConflictResolution(OH_Rdb_Transaction *trans, const char *table, const OH_VBucket *row,Rdb_ConflictResolution resolution, int64_t *rowId)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_insertwithconflictresolution)将一行数据插入到目标表中，支持冲突解决。[int OH_RdbTrans_BatchInsert(OH_Rdb_Transaction *trans, const char *table, const OH_Data_VBuckets *rows,Rdb_ConflictResolution resolution, int64_t *changes)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_batchinsert)将一组数据批量插入到目标表中。[int OH_RdbTrans_Update(OH_Rdb_Transaction *trans, const OH_VBucket *row, const OH_Predicates *predicates,int64_t *changes)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_update)根据指定的条件更新数据库中的数据。[int OH_RdbTrans_UpdateWithConflictResolution(OH_Rdb_Transaction *trans, const OH_VBucket *row,const OH_Predicates *predicates, Rdb_ConflictResolution resolution, int64_t *changes)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_updatewithconflictresolution)根据指定条件更新数据库中的数据，并支持冲突解决。[int OH_RdbTrans_Delete(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, int64_t *changes)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_delete)根据指定条件从数据库中删除数据。[OH_Cursor *OH_RdbTrans_Query(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, const char *columns[],int len)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_query)根据指定的条件查询数据库中的数据。[OH_Cursor *OH_RdbTrans_QuerySql(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_querysql)根据SQL语句查询数据库中的数据。[int OH_RdbTrans_Execute(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args, OH_Data_Value **result)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_execute)执行包含指定参数的SQL语句。[int OH_RdbTrans_Destroy(OH_Rdb_Transaction *trans)](#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_destroy)销毁事务对象。

#### 枚举类型说明

#### OH_RDB_TransType

```ets
enum OH_RDB_TransType
```

**描述**

表示关系型数据库事务类型。

**起始版本：** 18

枚举项描述RDB_TRANS_DEFERRED = 0在首次访问数据库之前，事务默认设置不会启动。RDB_TRANS_IMMEDIATE数据库连接立即开始新的写入，而无需等待写入语句。RDB_TRANS_EXCLUSIVE

与RDB_TRANS_IMMEDIATE类型相似，写事务会立即启动。

RDB_TRANS_EXCLUSIVE和RDB_TRANS_IMMEDIATE类型在WAL模式下相同，但在其他日志模式下，RDB_TRANS_EXCLUSIVE会阻止其他数据库连接在事务进行时读取数据库。

RDB_TRANS_BUTTRDB事务类型的最大值。

#### 函数说明

#### OH_RdbTrans_CreateOptions()

```ets
OH_RDB_TransOptions *OH_RdbTrans_CreateOptions(void)
```

**描述**

创建事务配置对象。

**起始版本：** 18

**返回：**

类型说明[OH_RDB_TransOptions](OH_RDB_TransOptions.md)

执行成功时返回指向[OH_RDB_TransOptions](OH_RDB_TransOptions.md)实例的指针。否则返回nullptr。

使用完成后，必须通过[OH_RdbTrans_DestroyOptions](oh_rdb_transaction.h.md#ZH-CN_TOPIC_0000002529444669__oh_rdbtrans_destroyoptions)接口释放内存。

#### OH_RdbTrans_DestroyOptions()

```ets
int OH_RdbTrans_DestroyOptions(OH_RDB_TransOptions *options)
```

**描述**

销毁事务配置对象。

**起始版本：** 18

**参数：**

参数项描述[OH_RDB_TransOptions](OH_RDB_TransOptions.md) *options表示指向[OH_RDB_TransOptions](OH_RDB_TransOptions.md)实例的指针。

**返回：**

类型说明int

返回错误码。

返回RDB_OK表示成功。

返回RDB_E_INVALID_ARGS表示无效参数。

#### OH_RdbTransOption_SetType()

```ets
int OH_RdbTransOption_SetType(OH_RDB_TransOptions *options, OH_RDB_TransType type)
```

**描述**

设置关系型数据库事务类型。

**起始版本：** 18

**参数：**

参数项描述[OH_RDB_TransOptions](OH_RDB_TransOptions.md) *options表示指向[OH_RDB_TransOptions](OH_RDB_TransOptions.md)实例的指针。[OH_RDB_TransType](#ZH-CN_TOPIC_0000002529444669__oh_rdb_transtype) type表示关系型数据库事务类型。

**返回：**

类型说明int

返回错误码。

返回RDB_OK表示成功。

返回RDB_E_INVALID_ARGS表示无效参数。

#### OH_RdbTrans_Commit()

```ets
int OH_RdbTrans_Commit(OH_Rdb_Transaction *trans)
```

**描述**

提交事务。

**起始版本：** 18

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。

**返回：**

类型说明int

返回执行结果。

返回RDB_OK表示成功。

返回RDB_E_ERROR表示数据库常见错误。

返回RDB_E_INVALID_ARGS表示无效参数。

返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。

返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。

返回RDB_E_SQLITE_CORRUPT表示数据库损坏。

返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。

返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。

返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。

返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。

返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。

#### OH_RdbTrans_Rollback()

```ets
int OH_RdbTrans_Rollback(OH_Rdb_Transaction *trans)
```

**描述**

回滚事务。

**起始版本：** 18

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。

**返回：**

类型说明int

返回执行结果。

返回RDB_OK表示成功。

返回RDB_E_ERROR表示数据库常见错误。

返回RDB_E_INVALID_ARGS表示无效参数。

返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。

返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。

返回RDB_E_SQLITE_CORRUPT表示数据库损坏。

返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。

返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。

返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。

返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。

返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。

#### OH_RdbTrans_Insert()

```ets
int OH_RdbTrans_Insert(OH_Rdb_Transaction *trans, const char *table, const OH_VBucket *row, int64_t *rowId)
```

**描述**

将一行数据插入到目标表中。

**起始版本：** 18

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。const char *table表示目标表。const [OH_VBucket](OH_VBucket.md) *row表示要插入到表中的数据行。int64_t *rowId输出参数，表示插入后返回的行号。

**返回：**

类型说明int

返回执行结果。

返回RDB_OK表示成功。

返回RDB_E_ERROR表示数据库常见错误。

返回RDB_E_INVALID_ARGS表示无效参数。

返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。

返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。

返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。

返回RDB_E_SQLITE_CORRUPT表示数据库损坏。

返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。

返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。

返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。

返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。

返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。

返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。

返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。

返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。

#### OH_RdbTrans_InsertWithConflictResolution()

```ets
int OH_RdbTrans_InsertWithConflictResolution(OH_Rdb_Transaction *trans, const char *table, const OH_VBucket *row,Rdb_ConflictResolution resolution, int64_t *rowId)
```

**描述**

将一行数据插入到目标表中，支持冲突解决。

**起始版本：** 20

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。const char *table表示目标表名称。const [OH_VBucket](OH_VBucket.md) *row表示要插入到表中的数据。Rdb_ConflictResolution resolution表示发生冲突时的解决策略。int64_t *rowId输出参数，表示插入成功后返回的行号。

**返回：**

类型说明int

返回执行结果。

返回RDB_OK表示成功。

返回RDB_E_ERROR表示数据库常见错误。

返回RDB_E_INVALID_ARGS表示输入参数无效。

返回RDB_E_ALREADY_CLOSED表示数据库已关闭。

返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。

返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。

返回RDB_E_SQLITE_CORRUPT表示数据库损坏。

返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。

返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。

返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。

返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。

返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。

返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。

返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。

返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。

返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误码：违反约束导致操作中止。

#### OH_RdbTrans_BatchInsert()

```ets
int OH_RdbTrans_BatchInsert(OH_Rdb_Transaction *trans, const char *table, const OH_Data_VBuckets *rows, Rdb_ConflictResolution resolution, int64_t *changes)
```

**描述**

将一组数据批量插入到目标表中。

单次插入参数的最大数量限制为32766，超出上限会返回RDB_E_INVALID_ARGS错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

**起始版本：** 18

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。const char *table表示目标表。const [OH_Data_VBuckets](OH_Data_VBuckets.md) *rows表示要插入到表中的一组数据。Rdb_ConflictResolution resolution表示发生冲突时的解决策略。int64_t *changes输出参数，表示插入成功的次数。

**返回：**

类型说明int

返回执行结果。

返回RDB_OK表示成功。

返回RDB_E_ERROR表示数据库常见错误。

返回RDB_E_INVALID_ARGS表示无效参数。

返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。

返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。

返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。

返回RDB_E_SQLITE_CORRUPT表示数据库损坏。

返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。

返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。

返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。

返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。

返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。

返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。

返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。

返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。

返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误码：SQLite约束。

#### OH_RdbTrans_Update()

```ets
int OH_RdbTrans_Update(OH_Rdb_Transaction *trans, const OH_VBucket *row, const OH_Predicates *predicates, int64_t *changes)
```

**描述**

根据指定的条件更新数据库中的数据。

**起始版本：** 18

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。const [OH_VBucket](OH_VBucket.md) *row表示要更新到表中的数据行。const [OH_Predicates](OH_Predicates.md) *predicates表示[OH_Predicates](OH_Predicates.md)指定的更新条件。int64_t *changes输出参数，表示更新成功的次数。

**返回：**

类型说明int

返回执行结果。

返回RDB_OK表示成功。

返回RDB_E_ERROR表示数据库常见错误。

返回RDB_E_INVALID_ARGS表示无效参数。

返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。

返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。

返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。

返回RDB_E_SQLITE_CORRUPT表示数据库损坏。

返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。

返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。

返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。

返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。

返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。

返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。

返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。

返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。

#### OH_RdbTrans_UpdateWithConflictResolution()

```ets
int OH_RdbTrans_UpdateWithConflictResolution(OH_Rdb_Transaction *trans, const OH_VBucket *row,const OH_Predicates *predicates, Rdb_ConflictResolution resolution, int64_t *changes)
```

**描述**

根据指定条件更新数据库中的数据，并支持冲突解决。

**起始版本：** 20

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。const [OH_VBucket](OH_VBucket.md) *row表示要更新到表中的数据。const [OH_Predicates](OH_Predicates.md) *predicates表示[OH_Predicates](OH_Predicates.md)指定的更新条件。Rdb_ConflictResolution resolution表示发生冲突时的解决策略。int64_t *changes输出参数，表示更新成功的行数。

**返回：**

类型说明int

返回执行结果。

返回RDB_OK表示成功。

返回RDB_E_ERROR表示数据库常见错误。

返回RDB_E_INVALID_ARGS表示输入参数无效。

返回RDB_E_ALREADY_CLOSED表示数据库已关闭。

返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。

返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。

返回RDB_E_SQLITE_CORRUPT表示数据库损坏。

返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。

返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。

返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。

返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。

返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。

返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。

返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。

返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。

返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误码：违反约束导致操作中止。

#### OH_RdbTrans_Delete()

```ets
int OH_RdbTrans_Delete(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, int64_t *changes)
```

**描述**

根据指定条件从数据库中删除数据。

**起始版本：** 18

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。const [OH_Predicates](OH_Predicates.md) *predicates表示[OH_Predicates](OH_Predicates.md)指定的删除条件。int64_t *changes表示删除成功的次数。

**返回：**

类型说明int

返回执行结果。

返回RDB_OK表示成功。

返回RDB_E_ERROR表示数据库常见错误。

返回RDB_E_INVALID_ARGS表示无效参数。

返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。

返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。

返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。

返回RDB_E_SQLITE_CORRUPT表示数据库损坏。

返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。

返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。

返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。

返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。

返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。

返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。

返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。

返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。

#### OH_RdbTrans_Query()

```ets
OH_Cursor *OH_RdbTrans_Query(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, const char *columns[], int len)
```

**描述**

根据指定的条件查询数据库中的数据。

**起始版本：** 18

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。const [OH_Predicates](OH_Predicates.md) *predicates表示[OH_Predicates](OH_Predicates.md)指定的查询条件。const char *columns[]表示要查询的列，如果传入空值，则查询适用于所有列。int len表示列中元素的个数。

**返回：**

类型说明[OH_Cursor](OH_Cursor.md)如果执行成功，则返回指向[OH_Cursor](OH_Cursor.md)实例的指针。如果数据库已关闭或数据库没有响应，则返回空。

#### OH_RdbTrans_QuerySql()

```ets
OH_Cursor *OH_RdbTrans_QuerySql(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args)
```

**描述**

根据SQL语句查询数据库中的数据。

**起始版本：** 18

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。const char *sql表示要执行的SQL语句。const [OH_Data_Values](OH_Data_Values.md) *args表示指向[OH_Data_Values](OH_Data_Values.md)的指针。

**返回：**

类型说明[OH_Cursor](OH_Cursor.md)如果执行成功，则返回指向[OH_Cursor](OH_Cursor.md)实例的指针。如果数据库已关闭或数据库没有响应，则返回空。

#### OH_RdbTrans_Execute()

```ets
int OH_RdbTrans_Execute(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args, OH_Data_Value **result)
```

**描述**

执行包含指定参数的SQL语句。

**起始版本：** 18

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。const char *sql表示要执行的SQL语句。const [OH_Data_Values](OH_Data_Values.md) *argsSQL语句中包含的参数。OH_Data_Value **result执行成功时指向[OH_Data_Value](OH_Data_Value.md)实例的指针。使用完成后，必须通过[OH_Value_Destroy](oh_data_value.h.md#ZH-CN_TOPIC_0000002529284693__oh_value_destroy)接口释放内存。

**返回：**

类型说明int

返回执行结果。

返回RDB_OK表示成功。

返回RDB_E_ERROR表示数据库常见错误。

返回RDB_E_INVALID_ARGS表示无效参数。

返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。

返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。

返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。

返回RDB_E_SQLITE_CORRUPT表示数据库损坏。

返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。

返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。

返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。

返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。

返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。

返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。

返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。

返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。

#### OH_RdbTrans_Destroy()

```ets
int OH_RdbTrans_Destroy(OH_Rdb_Transaction *trans)
```

**描述**

销毁事务对象。

**起始版本：** 18

**参数：**

参数项描述[OH_Rdb_Transaction](OH_Rdb_Transaction.md) *trans表示指向[OH_Rdb_Transaction](OH_Rdb_Transaction.md)实例的指针。

**返回：**

类型说明int

返回错误码。

返回RDB_OK表示成功。

返回RDB_E_INVALID_ARGS表示无效参数。