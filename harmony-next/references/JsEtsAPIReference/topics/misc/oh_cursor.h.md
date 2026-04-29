# oh_cursor.h

**概述**

提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。

引用文件： <database/rdb/oh_cursor.h>

库： libnative_rdb_ndk.z.so

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

起始版本： 10

相关模块： [RDB](RDB.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Cursor | OH_Cursor | 提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| int OH_Cursor_GetFloatVectorCount(OH_Cursor *cursor, int32_t columnIndex, size_t *length) | 获取当前行中指定列的浮点数数组大小。 |
| int OH_Cursor_GetFloatVector(OH_Cursor *cursor, int32_t columnIndex, float *val, size_t inLen, size_t *outLen) | 以浮点数数组的形式获取当前行中指定列的值。 |

**函数说明**

**OH_Cursor_GetFloatVectorCount()**

```ets
int OH_Cursor_GetFloatVectorCount(OH_Cursor *cursor, int32_t columnIndex, size_t *length)
```

描述

获取当前行中指定列的浮点数数组大小。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针。 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| size_t *length | 该参数是输出参数，结果集中指定列的浮点数数组大小会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_STEP_RESULT_CLOSED表示查询到的结果集已经关闭。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_SQLITE_PERM表示SQLite错误: 访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误: 数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误: 数据库内存不足。 返回RDB_E_SQLITE_IOERR表示SQLite错误: 磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 |

**OH_Cursor_GetFloatVector()**

```ets
int OH_Cursor_GetFloatVector(OH_Cursor *cursor, int32_t columnIndex, float *val, size_t inLen, size_t *outLen)
```

描述

以浮点数数组的形式获取当前行中指定列的值。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针。 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| float *val | 该参数是输出参数，结果集中指定列的值会以浮点数数组形式写入该变量，调用者需要申请数组内存。 |
| size_t inLen | 表示申请的浮点数数组大小。 |
| size_t *outLen | 该参数是输出参数，表示实际浮点数数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_STEP_RESULT_CLOSED表示查询到的结果集已经关闭。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_SQLITE_PERM表示SQLite错误: 访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误: 数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误: 数据库内存不足。 返回RDB_E_SQLITE_IOERR表示SQLite错误: 磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 |