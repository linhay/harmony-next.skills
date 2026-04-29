# oh_rdb_transaction.h

**概述**

提供与数据库事务相关的函数和枚举。

引用文件： <database/rdb/oh_rdb_transaction.h>

库： libnative_rdb_ndk.z.so

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

起始版本： 18

相关模块： [RDB](RDB.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_RDB_TransOptions | OH_RDB_TransOptions | 定义OH_RDB_TransOptions结构类型。 |
| OH_Rdb_Transaction | OH_Rdb_Transaction | 定义OH_RDB_TransOptions结构类型。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_RDB_TransType | OH_RDB_TransType | 表示关系型数据库事务类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_RDB_TransOptions *OH_RdbTrans_CreateOptions(void) | 创建事务配置对象。 |
| int OH_RdbTrans_DestroyOptions(OH_RDB_TransOptions *options) | 销毁事务配置对象。 |
| int OH_RdbTransOption_SetType(OH_RDB_TransOptions *options, OH_RDB_TransType type) | 设置关系型数据库事务类型。 |
| int OH_RdbTrans_Commit(OH_Rdb_Transaction *trans) | 提交事务。 |
| int OH_RdbTrans_Rollback(OH_Rdb_Transaction *trans) | 回滚事务。 |
| int OH_RdbTrans_Insert(OH_Rdb_Transaction *trans, const char *table, const OH_VBucket *row, int64_t *rowId) | 将一行数据插入到目标表中。 |
| int OH_RdbTrans_InsertWithConflictResolution(OH_Rdb_Transaction *trans, const char *table, const OH_VBucket *row,Rdb_ConflictResolution resolution, int64_t *rowId) | 将一行数据插入到目标表中，支持冲突解决。 |
| int OH_RdbTrans_BatchInsert(OH_Rdb_Transaction *trans, const char *table, const OH_Data_VBuckets *rows,Rdb_ConflictResolution resolution, int64_t *changes) | 将一组数据批量插入到目标表中。 |
| int OH_RdbTrans_Update(OH_Rdb_Transaction *trans, const OH_VBucket *row, const OH_Predicates *predicates,int64_t *changes) | 根据指定的条件更新数据库中的数据。 |
| int OH_RdbTrans_UpdateWithConflictResolution(OH_Rdb_Transaction *trans, const OH_VBucket *row,const OH_Predicates *predicates, Rdb_ConflictResolution resolution, int64_t *changes) | 根据指定条件更新数据库中的数据，并支持冲突解决。 |
| int OH_RdbTrans_Delete(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, int64_t *changes) | 根据指定条件从数据库中删除数据。 |
| OH_Cursor *OH_RdbTrans_Query(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, const char *columns[],int len) | 根据指定的条件查询数据库中的数据。 |
| OH_Cursor *OH_RdbTrans_QuerySql(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args) | 根据SQL语句查询数据库中的数据。 |
| int OH_RdbTrans_Execute(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args, OH_Data_Value **result) | 执行包含指定参数的SQL语句。 |
| int OH_RdbTrans_Destroy(OH_Rdb_Transaction *trans) | 销毁事务对象。 |
| OH_Cursor *OH_RdbTrans_QueryWithoutRowCount(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, const char * const columns[], int len) | 根据指定的条件查询数据库中的数据，不计算行数。 |
| OH_Cursor *OH_RdbTrans_QuerySqlWithoutRowCount(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args) | 根据SQL语句查询数据库中的数据，不计算行数。 |
| int OH_RdbTrans_BatchInsertWithReturning(OH_Rdb_Transaction *trans, const char *table, const OH_Data_VBuckets *rows, Rdb_ConflictResolution resolution, OH_RDB_ReturningContext *context) | 将批量数据插入目标表，并将变更信息输出到上下文中。 |
| int OH_RdbTrans_UpdateWithReturning(OH_Rdb_Transaction *trans, OH_VBucket *row, OH_Predicates *predicates, Rdb_ConflictResolution resolution, OH_RDB_ReturningContext *context) | 根据指定条件更新数据库中的数据并输出更改信息到上下文。 |
| int OH_RdbTrans_DeleteWithReturning(OH_Rdb_Transaction *trans, OH_Predicates *predicates, OH_RDB_ReturningContext *context) | 根据指定条件从数据库中删除数据并输出更改信息到上下文。 |

**枚举类型说明**

**OH_RDB_TransType**

```ets
enum OH_RDB_TransType
```

描述

表示关系型数据库事务类型。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| RDB_TRANS_DEFERRED = 0 | 在首次访问数据库之前，事务默认设置不会启动。 |
| RDB_TRANS_IMMEDIATE | 数据库连接立即开始新的写入，而无需等待写入语句。 |
| RDB_TRANS_EXCLUSIVE | 与RDB_TRANS_IMMEDIATE类型相似，写事务会立即启动。 RDB_TRANS_EXCLUSIVE和RDB_TRANS_IMMEDIATE类型在WAL模式下相同，但在其他日志模式下，RDB_TRANS_EXCLUSIVE会阻止其他数据库连接在事务进行时读取数据库。 |
| RDB_TRANS_BUTT | RDB事务类型的最大值。 |

**函数说明**

**OH_RdbTrans_CreateOptions()**

```ets
OH_RDB_TransOptions *OH_RdbTrans_CreateOptions(void)
```

描述

创建事务配置对象。

起始版本： 18

返回：

| 类型 | 说明 |
| --- | --- |
| OH_RDB_TransOptions | 执行成功时返回指向OH_RDB_TransOptions实例的指针。否则返回nullptr。 使用完成后，必须通过OH_RdbTrans_DestroyOptions接口释放内存。 |

**OH_RdbTrans_DestroyOptions()**

```ets
int OH_RdbTrans_DestroyOptions(OH_RDB_TransOptions *options)
```

描述

销毁事务配置对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_RDB_TransOptions *options | 指向OH_RDB_TransOptions实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_RdbTransOption_SetType()**

```ets
int OH_RdbTransOption_SetType(OH_RDB_TransOptions *options, OH_RDB_TransType type)
```

描述

设置关系型数据库事务类型。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_RDB_TransOptions *options | 指向OH_RDB_TransOptions实例的指针。 |
| OH_RDB_TransType type | 表示关系型数据库事务类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_RdbTrans_Commit()**

```ets
int OH_RdbTrans_Commit(OH_Rdb_Transaction *trans)
```

描述

提交事务。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 |

**OH_RdbTrans_Rollback()**

```ets
int OH_RdbTrans_Rollback(OH_Rdb_Transaction *trans)
```

描述

回滚事务。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 |

**OH_RdbTrans_Insert()**

```ets
int OH_RdbTrans_Insert(OH_Rdb_Transaction *trans, const char *table, const OH_VBucket *row, int64_t *rowId)
```

描述

将一行数据插入到目标表中。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const char *table | 要插入的目标表名。 |
| const OH_VBucket *row | 要插入到表中的数据行。 |
| int64_t *rowId | 输出参数，表示插入后返回的行号。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 |

**OH_RdbTrans_InsertWithConflictResolution()**

```ets
int OH_RdbTrans_InsertWithConflictResolution(OH_Rdb_Transaction *trans, const char *table, const OH_VBucket *row,Rdb_ConflictResolution resolution, int64_t *rowId)
```

描述

将一行数据插入到目标表中，支持冲突解决。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const char *table | 要插入的目标表名。 |
| const OH_VBucket *row | 表示要插入到表中的数据。 |
| Rdb_ConflictResolution resolution | 表示发生冲突时的解决策略。 |
| int64_t *rowId | 输出参数，表示插入成功后返回的行号。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误码：违反约束导致操作中止。 |

**OH_RdbTrans_BatchInsert()**

```ets
int OH_RdbTrans_BatchInsert(OH_Rdb_Transaction *trans, const char *table, const OH_Data_VBuckets *rows, Rdb_ConflictResolution resolution, int64_t *changes)
```

描述

将一组数据批量插入到目标表中。

单次插入参数的最大数量限制为32766，超出上限会返回RDB_E_INVALID_ARGS错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const char *table | 要插入的目标表名。 |
| const OH_Data_VBuckets *rows | 表示要插入到表中的一组数据。 |
| Rdb_ConflictResolution resolution | 表示发生冲突时的解决策略。 |
| int64_t *changes | 输出参数，表示插入成功的次数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误码：SQLite约束。 |

**OH_RdbTrans_Update()**

```ets
int OH_RdbTrans_Update(OH_Rdb_Transaction *trans, const OH_VBucket *row, const OH_Predicates *predicates, int64_t *changes)
```

描述

根据指定的条件更新数据库中的数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const OH_VBucket *row | 表示要更新到表中的数据行。 |
| const OH_Predicates *predicates | 表示OH_Predicates指定的更新条件。 |
| int64_t *changes | 输出参数，表示更新成功的次数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 |

**OH_RdbTrans_UpdateWithConflictResolution()**

```ets
int OH_RdbTrans_UpdateWithConflictResolution(OH_Rdb_Transaction *trans, const OH_VBucket *row,const OH_Predicates *predicates, Rdb_ConflictResolution resolution, int64_t *changes)
```

描述

根据指定条件更新数据库中的数据，并支持冲突解决。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const OH_VBucket *row | 表示要更新到表中的数据。 |
| const OH_Predicates *predicates | 表示OH_Predicates指定的更新条件。 |
| Rdb_ConflictResolution resolution | 表示发生冲突时的解决策略。 |
| int64_t *changes | 输出参数，表示更新成功的行数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误码：违反约束导致操作中止。 |

**OH_RdbTrans_Delete()**

```ets
int OH_RdbTrans_Delete(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, int64_t *changes)
```

描述

根据指定条件从数据库中删除数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const OH_Predicates *predicates | 表示OH_Predicates指定的删除条件。 |
| int64_t *changes | 表示删除成功的次数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 |

**OH_RdbTrans_Query()**

```ets
OH_Cursor *OH_RdbTrans_Query(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, const char *columns[], int len)
```

描述

根据指定的条件查询数据库中的数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const OH_Predicates *predicates | 表示OH_Predicates指定的查询条件。 |
| const char *columns[] | 表示要查询的列，如果传入空值，则查询适用于所有列。 |
| int len | 表示列中元素的个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor | 如果执行成功，则返回指向OH_Cursor实例的指针。如果数据库已关闭或数据库没有响应，则返回空。 |

**OH_RdbTrans_QuerySql()**

```ets
OH_Cursor *OH_RdbTrans_QuerySql(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args)
```

描述

根据SQL语句查询数据库中的数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const char *sql | 表示要执行的SQL语句。 |
| const OH_Data_Values *args | 指向OH_Data_Values的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor | 如果执行成功，则返回指向OH_Cursor实例的指针。如果数据库已关闭或数据库没有响应，则返回空。 |

**OH_RdbTrans_Execute()**

```ets
int OH_RdbTrans_Execute(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args, OH_Data_Value **result)
```

描述

执行包含指定参数的SQL语句。

不支持开头包含注释的语句。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const char *sql | 表示要执行的SQL语句。 |
| const OH_Data_Values *args | SQL语句中包含的参数。 |
| OH_Data_Value **result | 执行成功时指向OH_Data_Value实例的指针。使用完成后，必须通过OH_Value_Destroy接口释放内存。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 |

**OH_RdbTrans_Destroy()**

```ets
int OH_RdbTrans_Destroy(OH_Rdb_Transaction *trans)
```

描述

销毁事务对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_RdbTrans_QueryWithoutRowCount()**

```ets
OH_Cursor *OH_RdbTrans_QueryWithoutRowCount(OH_Rdb_Transaction *trans, const OH_Predicates *predicates, const char * const columns[], int len)
```

描述

根据指定的条件查询数据库中的数据，不计算行数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const OH_Predicates *predicates | OH_Predicates指定的查询条件。 |
| const char * const columns[] | 要查询的列，如果传入空值，则查询所有列。 |
| int len | 传入的columns数组的长度。若len大于columns数组的实际长度，则会访问越界。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor * | 如果执行成功，则返回指向OH_Cursor实例的指针。如果数据库已关闭或数据库没有响应，则返回nullptr。 |

**OH_RdbTrans_QuerySqlWithoutRowCount()**

```ets
OH_Cursor *OH_RdbTrans_QuerySqlWithoutRowCount(OH_Rdb_Transaction *trans, const char *sql, const OH_Data_Values *args)
```

描述

根据SQL语句查询数据库中的数据，不计算行数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const char *sql | 要执行的SQL语句。 |
| const OH_Data_Values *args | 指向OH_Data_Values的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor * | 如果执行成功，则返回指向OH_Cursor实例的指针。如果数据库已关闭或数据库没有响应，则返回nullptr。 |

**OH_RdbTrans_BatchInsertWithReturning()**

```ets
int OH_RdbTrans_BatchInsertWithReturning(OH_Rdb_Transaction *trans, const char *table, const OH_Data_VBuckets *rows, Rdb_ConflictResolution resolution, OH_RDB_ReturningContext *context)
```

描述

将批量数据插入目标表，并将变更信息输出到上下文中。

一次最多可以插入32766个参数。如果参数数量超过上限，则返回错误代码RDB_E_INVALID_ARGS。

参数数量计算方式为插入数据条数乘以插入数据时所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| const char *table | 要插入的目标表名。 |
| const OH_Data_VBuckets *rows | 要插入到表中的行数据。 |
| Rdb_ConflictResolution resolution | 发生冲突时的解决策略Rdb_ConflictResolution，不建议使用RDB_CONFLICT_FAIL，因为失败时会抛异常， 无法正常获取实际的变更数据。 |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL文件大小超过默认限制。 返回RDB_E_NOT_SUPPORTED表示不支持的操作。 返回RDB_E_DATABASE_BUSY表示数据库忙。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误：数据库中的表被锁定。 返回RDB_E_SQLITE_IOERR表示SQLite错误：发生某种磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误：由于违反约束而中止。 返回RDB_E_SQLITE_ERROR表示SQLite错误。可能原因：语法错误，例如表或列不存在。 具体错误码可参考OH_Rdb_ErrCode。 |

**OH_RdbTrans_UpdateWithReturning()**

```ets
int OH_RdbTrans_UpdateWithReturning(OH_Rdb_Transaction *trans, OH_VBucket *row, OH_Predicates *predicates, Rdb_ConflictResolution resolution, OH_RDB_ReturningContext *context)
```

描述

根据指定条件更新数据库中的数据并输出更改信息到上下文。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| OH_VBucket *row | 要更新到表中的行数据。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针。 |
| Rdb_ConflictResolution resolution | 发生冲突时的解决策略Rdb_ConflictResolution，不建议使用RDB_CONFLICT_FAIL，因为失败时会抛异常， 无法正常获取实际的变更数据。 |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL文件大小超过默认限制。 返回RDB_E_NOT_SUPPORTED表示不支持的操作。 返回RDB_E_EMPTY_VALUES_BUCKET表示值桶为空。 返回RDB_E_DATABASE_BUSY表示数据库忙。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误：数据库中的表被锁定。 返回RDB_E_SQLITE_IOERR表示SQLite错误：发生某种磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误：由于违反约束而中止。 返回RDB_E_SQLITE_ERROR表示SQLite错误。可能原因：语法错误，例如表或列不存在。 具体错误码可参考OH_Rdb_ErrCode。 |

**OH_RdbTrans_DeleteWithReturning()**

```ets
int OH_RdbTrans_DeleteWithReturning(OH_Rdb_Transaction *trans, OH_Predicates *predicates, OH_RDB_ReturningContext *context)
```

描述

根据指定条件从数据库中删除数据并输出更改信息到上下文。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Transaction *trans | 指向OH_Rdb_Transaction实例的指针。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针。 |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL文件大小超过默认限制。 返回RDB_E_NOT_SUPPORTED表示不支持的操作。 返回RDB_E_DATABASE_BUSY表示数据库忙。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误：数据库中的表被锁定。 返回RDB_E_SQLITE_IOERR表示SQLite错误：发生某种磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误：数据类型不匹配。 返回RDB_E_SQLITE_ERROR表示SQLite错误。可能原因：语法错误，例如表或列不存在。 具体错误码可参考OH_Rdb_ErrCode。 |