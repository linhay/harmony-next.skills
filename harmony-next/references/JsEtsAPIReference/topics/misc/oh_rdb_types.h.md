# oh_rdb_types.h

**概述**

提供与数据值相关的类型定义。

引用文件： <database/rdb/oh_rdb_types.h>

库： libnative_rdb_ndk.z.so

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

起始版本： 18

相关模块： [RDB](RDB.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_RDB_ReturningContext | OH_RDB_ReturningContext | returning相关接口的上下文。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Rdb_ConflictResolution | Rdb_ConflictResolution | 表示冲突解决策略的枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_RDB_ReturningContext *OH_RDB_CreateReturningContext(void) | 创建OH_RDB_ReturningContext的实例对象。 |
| void OH_RDB_DestroyReturningContext(OH_RDB_ReturningContext *context) | 销毁OH_RDB_ReturningContext实例对象。 |
| int OH_RDB_SetReturningFields(OH_RDB_ReturningContext *context, const char *const fields[], int32_t len) | 设置結果集中返回的字段。 |
| int OH_RDB_SetMaxReturningCount(OH_RDB_ReturningContext *context, int32_t count) | 设置返回结果集的最大行数量。 |
| OH_Cursor *OH_RDB_GetReturningValues(OH_RDB_ReturningContext *context) | 获取数据变化的游标，默认包含1024条。 |
| int64_t OH_RDB_GetChangedCount(OH_RDB_ReturningContext *context) | 获取受此操作影响的数据行的数量。 |

**枚举类型说明**

**Rdb_ConflictResolution**

```ets
enum Rdb_ConflictResolution
```

描述

表示冲突解决策略的枚举。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| RDB_CONFLICT_NONE = 1 | 发生冲突时不执行任何操作。 |
| RDB_CONFLICT_ROLLBACK | 发生冲突时抛错误码，同时回滚本次事务。 |
| RDB_CONFLICT_ABORT | 发生冲突时抛错误码，同时回滚本次修改。 |
| RDB_CONFLICT_FAIL | 发生冲突时抛错误码，不回滚冲突前的修改同时终止本次修改。 |
| RDB_CONFLICT_IGNORE | 发生冲突时忽略冲突的数据，继续执行后续修改。 |
| RDB_CONFLICT_REPLACE | 发生冲突时，尝试删除后插入，如果还是冲突则等同于RDB_CONFLICT_ABORT。 |

**函数说明**

**OH_RDB_CreateReturningContext()**

```ets
OH_RDB_ReturningContext *OH_RDB_CreateReturningContext(void)
```

描述

创建[OH_RDB_ReturningContext](OH_RDB_ReturningContext.md)的实例对象。

起始版本： 23

返回：

| 类型 | 说明 |
| --- | --- |
| OH_RDB_ReturningContext * | 执行成功时返回指向OH_RDB_ReturningContext实例的指针。 否则返回nullptr。使用完成后必须通过OH_RDB_DestroyReturningContext接口释放内存。 |

**OH_RDB_DestroyReturningContext()**

```ets
void OH_RDB_DestroyReturningContext(OH_RDB_ReturningContext *context)
```

描述

销毁[OH_RDB_ReturningContext](OH_RDB_ReturningContext.md)实例对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |

**OH_RDB_SetReturningFields()**

```ets
int OH_RDB_SetReturningFields(OH_RDB_ReturningContext *context, const char *const fields[], int32_t len)
```

描述

设置結果集中返回的字段。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |
| const char *const fields[] | 要返回的列名。 |
| int32_t len | 字段长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 执行成功返回RDB_OK。 输入参数无效返回RDB_E_INVALID_ARGS。 |

**OH_RDB_SetMaxReturningCount()**

```ets
int OH_RDB_SetMaxReturningCount(OH_RDB_ReturningContext *context, int32_t count)
```

描述

设置返回结果集的最大行数量。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |
| int32_t count | 表示返回结果集的最大条目数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 执行成功返回RDB_OK。 输入参数无效返回RDB_E_INVALID_ARGS。 |

**OH_RDB_GetReturningValues()**

```ets
OH_Cursor *OH_RDB_GetReturningValues(OH_RDB_ReturningContext *context)
```

描述

获取数据变化的游标，默认包含1024条。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor * | 返回指向OH_Cursor结构体实例的指针。 如果获取游标失败，则返回nullptr。使用OH_RDB_DestroyReturningContext接口释放内存时会销毁游标，无需单独释放。 |

**OH_RDB_GetChangedCount()**

```ets
int64_t OH_RDB_GetChangedCount(OH_RDB_ReturningContext *context)
```

描述

获取受此操作影响的数据行的数量。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int64_t | 返回已更改的条目数，如果获取变更失败则返回-1。 |