# relational_store.h

**概述**

提供管理关系数据库（RDB）方法的接口，未标注支持向量数据库的接口仅支持关系型数据库。

引用文件： <database/rdb/relational_store.h>

库： libnative_rdb_ndk.z.so

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

起始版本： 10

相关模块： [RDB](RDB.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Rdb_Config | OH_Rdb_Config | 管理关系数据库配置。 |
| OH_Rdb_Store | OH_Rdb_Store | 表示数据库类型。 |
| Rdb_DistributedConfig | Rdb_DistributedConfig | 记录表的分布式配置信息。 |
| Rdb_KeyInfo | Rdb_KeyInfo | 描述发生变化的行的主键或者行号。 |
| Rdb_KeyData | - | 存放变化的具体数据。 |
| Rdb_ChangeInfo | Rdb_ChangeInfo | 记录端云同步过程详情。 |
| Rdb_SubscribeCallback | Rdb_SubscribeCallback | 表示回调函数。 |
| Rdb_DataObserver | Rdb_DataObserver | 表示数据观察者。 |
| Rdb_Statistic | Rdb_Statistic | 描述数据库表的端云同步过程的统计信息。 |
| Rdb_TableDetails | Rdb_TableDetails | 描述数据库表执行端云同步任务上传和下载的统计信息。 |
| Rdb_ProgressDetails | Rdb_ProgressDetails | 描述数据库整体执行端云同步任务上传和下载的统计信息。 |
| Rdb_ProgressObserver | Rdb_ProgressObserver | 端云同步进度观察者。 |
| OH_Rdb_ConfigV2 | OH_Rdb_ConfigV2 | 管理关系数据库配置，与OH_Rdb_Config的区别是该结构体成员变量不对外暴露，使用一系列方法配置该结构体的属性，支持向量数据库。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Rdb_SecurityLevel | OH_Rdb_SecurityLevel | 数据库的安全级别枚举。 |
| Rdb_SecurityArea | Rdb_SecurityArea | 描述数据库的安全区域等级。 |
| Rdb_DBType | Rdb_DBType | 描述数据库的内核类型。 |
| Rdb_Tokenizer | Rdb_Tokenizer | 描述数据库的分词器类型。 |
| Rdb_DistributedType | Rdb_DistributedType | 描述表的分布式类型的枚举。 |
| Rdb_ChangeType | Rdb_ChangeType | 描述数据变更类型。 |
| Rdb_SubscribeType | Rdb_SubscribeType | 描述订阅类型。 |
| Rdb_SyncMode | Rdb_SyncMode | 表示数据库的同步模式 |
| Rdb_Progress | Rdb_Progress | 描述端云同步过程。 |
| Rdb_ProgressCode | Rdb_ProgressCode | 表示端云同步过程的状态。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Rdb_ConfigV2 *OH_Rdb_CreateConfig() | - | 创建一个OH_Rdb_ConfigV2实例，并返回指向该实例的指针。 |
| int OH_Rdb_DestroyConfig(OH_Rdb_ConfigV2 *config) | - | 销毁由OH_Rdb_CreateConfig创建的OH_Rdb_ConfigV2对象。 |
| int OH_Rdb_SetDatabaseDir(OH_Rdb_ConfigV2 *config, const char *databaseDir) | - | 给指定的数据库文件配置OH_Rdb_ConfigV2，设置数据库文件路径。 |
| int OH_Rdb_SetStoreName(OH_Rdb_ConfigV2 *config, const char *storeName) | - | 给指定的数据库文件配置OH_Rdb_ConfigV2，设置数据库名称。 |
| int OH_Rdb_SetBundleName(OH_Rdb_ConfigV2 *config, const char *bundleName) | - | 给指定的数据库文件配置OH_Rdb_ConfigV2，设置应用包名。 |
| int OH_Rdb_SetModuleName(OH_Rdb_ConfigV2 *config, const char *moduleName) | - | 给指定的数据库文件配置OH_Rdb_ConfigV2，设置应用模块名。 |
| int OH_Rdb_SetEncrypted(OH_Rdb_ConfigV2 *config, bool isEncrypted) | - | 给指定的数据库文件配置OH_Rdb_ConfigV2，设置数据库是否加密。 |
| int OH_Rdb_SetSecurityLevel(OH_Rdb_ConfigV2 *config, int securityLevel) | - | 给指定的数据库文件配置OH_Rdb_ConfigV2，设置数据库安全级别OH_Rdb_SecurityLevel。 |
| int OH_Rdb_SetArea(OH_Rdb_ConfigV2 *config, int area) | - | 给指定的数据库文件配置OH_Rdb_ConfigV2，设置数据库安全区域等级Rdb_SecurityArea。 |
| int OH_Rdb_SetDbType(OH_Rdb_ConfigV2 *config, int dbType) | - | 给指定的数据库文件配置OH_Rdb_ConfigV2，设置数据库类型Rdb_DBType。 |
| int OH_Rdb_SetCustomDir(OH_Rdb_ConfigV2 *config, const char *customDir) | - | 设置数据库的自定义目录。 |
| int OH_Rdb_SetReadOnly(OH_Rdb_ConfigV2 *config, bool readOnly) | - | 设置关系型数据库是否为只读模式。 |
| int OH_Rdb_SetPlugins(OH_Rdb_ConfigV2 *config, const char **plugins, int32_t length) | - | 设置具有特定功能（如全文检索）的动态库。 |
| int OH_Rdb_SetCryptoParam(OH_Rdb_ConfigV2 *config, const OH_Rdb_CryptoParam *cryptoParam) | - | 设置自定义加密参数。 |
| int OH_Rdb_IsTokenizerSupported(Rdb_Tokenizer tokenizer, bool *isSupported) | - | 判断当前平台是否支持传入的分词器。 |
| int OH_Rdb_SetTokenizer(OH_Rdb_ConfigV2 *config, Rdb_Tokenizer tokenizer) | - | 给指定的数据库文件配置设置分词器类型。 |
| int OH_Rdb_SetPersistent(OH_Rdb_ConfigV2 *config, bool isPersistent) | - | 指定数据库是否需要持久化。 |
| const int *OH_Rdb_GetSupportedDbType(int *typeCount) | - | 获得支持的数据库类型Rdb_DBType。 |
| OH_VObject *OH_Rdb_CreateValueObject() | - | 创建OH_VObject实例。 |
| OH_VBucket *OH_Rdb_CreateValuesBucket() | - | 创建OH_VBucket实例。 |
| OH_Predicates *OH_Rdb_CreatePredicates(const char *table) | - | 创建OH_Predicates实例。 |
| OH_Rdb_Store *OH_Rdb_GetOrOpen(const OH_Rdb_Config *config, int *errCode) | - | 获得一个相关的OH_Rdb_Store实例，操作关系型数据库。 |
| OH_Rdb_Store *OH_Rdb_CreateOrOpen(const OH_Rdb_ConfigV2 *config, int *errCode) | - | 使用指定的数据库文件配置OH_Rdb_ConfigV2，获得一个对应的OH_Rdb_Store实例，用来操作关系型数据库。 |
| int OH_Rdb_CloseStore(OH_Rdb_Store *store) | - | 销毁OH_Rdb_Store对象，并回收该对象占用的内存。 |
| int OH_Rdb_DeleteStore(const OH_Rdb_Config *config) | - | 使用指定的数据库文件配置删除数据库。 |
| int OH_Rdb_DeleteStoreV2(const OH_Rdb_ConfigV2 *config) | - | 使用指定的数据库文件配置OH_Rdb_ConfigV2删除数据库。 当使用向量数据库时，在调用接口前，应当确保向量数据库已经打开的OH_Rdb_Store和OH_Cursor均已成功关闭。 |
| int OH_Rdb_Insert(OH_Rdb_Store *store, const char *table, OH_VBucket *valuesBucket) | - | 向目标表中插入一行数据。 |
| int OH_Rdb_InsertWithConflictResolution(OH_Rdb_Store *store, const char *table, OH_VBucket *row,Rdb_ConflictResolution resolution, int64_t *rowId) | - | 向目标表中插入一行数据，并支持冲突解决。 |
| int OH_Rdb_BatchInsert(OH_Rdb_Store *store, const char *table,const OH_Data_VBuckets *rows, Rdb_ConflictResolution resolution, int64_t *changes) | - | 将一批数据插入到目标表中。 |
| int OH_Rdb_Update(OH_Rdb_Store *store, OH_VBucket *valuesBucket, OH_Predicates *predicates) | - | 根据指定的条件更新数据库中的数据。 |
| int OH_Rdb_UpdateWithConflictResolution(OH_Rdb_Store *store, OH_VBucket *row, OH_Predicates *predicates,Rdb_ConflictResolution resolution, int64_t *changes) | - | 根据指定条件更新数据库中的数据，并支持冲突解决。 |
| int OH_Rdb_Delete(OH_Rdb_Store *store, OH_Predicates *predicates) | - | 根据指定的条件删除数据库中的数据。 |
| OH_Cursor *OH_Rdb_Query(OH_Rdb_Store *store, OH_Predicates *predicates, const char *const *columnNames, int length) | - | 根据指定条件查询数据库中的数据 |
| int OH_Rdb_Execute(OH_Rdb_Store *store, const char *sql) | - | 执行无返回值的SQL语句。 |
| int OH_Rdb_ExecuteV2(OH_Rdb_Store *store, const char *sql, const OH_Data_Values *args, OH_Data_Value **result) | - | 执行有返回值的SQL语句，支持向量数据库。 |
| int OH_Rdb_ExecuteByTrxId(OH_Rdb_Store *store, int64_t trxId, const char *sql) | - | 使用指定的事务ID执行无返回值的SQL语句，仅支持向量数据库。 |
| OH_Cursor *OH_Rdb_ExecuteQuery(OH_Rdb_Store *store, const char *sql) | - | 根据指定SQL语句查询数据库中的数据，支持向量数据库。 |
| OH_Cursor *OH_Rdb_ExecuteQueryV2(OH_Rdb_Store *store, const char *sql, const OH_Data_Values *args) | - | 根据指定SQL语句查询数据库中的数据，支持向量数据库。 |
| int OH_Rdb_BeginTransaction(OH_Rdb_Store *store) | - | 在开始执行SQL语句之前，开始事务。 |
| int OH_Rdb_RollBack(OH_Rdb_Store *store) | - | 回滚已经执行的SQL语句。 |
| int OH_Rdb_Commit(OH_Rdb_Store *store) | - | 提交已执行的SQL语句 |
| int OH_Rdb_BeginTransWithTrxId(OH_Rdb_Store *store, int64_t *trxId) | - | 在开始执行SQL语句之前，开始事务，并获得该事务的ID，仅支持向量数据库。 |
| int OH_Rdb_RollBackByTrxId(OH_Rdb_Store *store, int64_t trxId) | - | 使用指定的事务ID, 回滚已经执行的SQL语句，仅支持向量数据库。 |
| int OH_Rdb_CommitByTrxId(OH_Rdb_Store *store, int64_t trxId) | - | 使用指定的事务ID, 提交已经执行的SQL语句，仅支持向量数据库。 |
| int OH_Rdb_Backup(OH_Rdb_Store *store, const char *databasePath) | - | 以指定路径备份数据库，支持向量数据库。 |
| int OH_Rdb_Restore(OH_Rdb_Store *store, const char *databasePath) | - | 从指定的数据库备份文件恢复数据库，支持向量数据库。 |
| int OH_Rdb_GetVersion(OH_Rdb_Store *store, int *version) | - | 获取数据库版本。 |
| int OH_Rdb_SetVersion(OH_Rdb_Store *store, int version) | - | 设置数据库版本。 |
| int OH_Rdb_SetDistributedTables(OH_Rdb_Store *store, const char *tables[], uint32_t count, Rdb_DistributedType type,const Rdb_DistributedConfig *config) | - | 设置分布式数据库表。 |
| OH_Cursor *OH_Rdb_FindModifyTime(OH_Rdb_Store *store, const char *tableName, const char *columnName,OH_VObject *values) | - | 获取数据库表中数据的最后修改时间。 |
| typedef void (*Rdb_BriefObserver)(void *context, const char *values[], uint32_t count) | Rdb_BriefObserver | 端云数据更改事件的回调函数。 |
| typedef void (*Rdb_DetailsObserver)(void *context, const Rdb_ChangeInfo **changeInfo, uint32_t count) | Rdb_DetailsObserver | 端云数据更改事件的细节的回调函数。 |
| int OH_Rdb_Subscribe(OH_Rdb_Store *store, Rdb_SubscribeType type, const Rdb_DataObserver *observer) | - | 为数据库注册观察者。当分布式数据库或本地数据库中的数据发生更改时，将调用回调。 |
| int OH_Rdb_Unsubscribe(OH_Rdb_Store *store, Rdb_SubscribeType type, const Rdb_DataObserver *observer) | - | 从数据库中删除指定类型的指定观察者。 |
| Rdb_TableDetails *OH_Rdb_GetTableDetails(Rdb_ProgressDetails *progress, int32_t version) | - | 从端云同步任务的统计信息中获取数据库表的统计信息。 |
| typedef void (*Rdb_ProgressCallback)(void *context, Rdb_ProgressDetails *progressDetails) | Rdb_ProgressCallback | 端云同步进度的回调函数。 |
| typedef void (*Rdb_SyncCallback)(Rdb_ProgressDetails *progressDetails) | Rdb_SyncCallback | 数据库端云同步的回调函数。 |
| int OH_Rdb_CloudSync(OH_Rdb_Store *store, Rdb_SyncMode mode, const char *tables[], uint32_t count,const Rdb_ProgressObserver *observer) | - | 进行端云同步。 |
| int OH_Rdb_SubscribeAutoSyncProgress(OH_Rdb_Store *store, const Rdb_ProgressObserver *observer) | - | 订阅RDB存储的自动同步进度。 当收到自动同步进度的通知时，将调用回调。 |
| int OH_Rdb_UnsubscribeAutoSyncProgress(OH_Rdb_Store *store, const Rdb_ProgressObserver *observer) | - | 取消订阅RDB存储的自动同步进程。 |
| int OH_Rdb_LockRow(OH_Rdb_Store *store, OH_Predicates *predicates) | - | 根据指定的条件锁定数据库中的数据，锁定数据不执行端云同步。 |
| int OH_Rdb_UnlockRow(OH_Rdb_Store *store, OH_Predicates *predicates) | - | 根据指定的条件锁解锁数据库中的数据。 |
| OH_Cursor *OH_Rdb_QueryLockedRow(OH_Rdb_Store *store, OH_Predicates *predicates, const char *const *columnNames, int length) | - | 根据指定条件查询数据库中锁定的数据。 |
| int OH_Rdb_CreateTransaction(OH_Rdb_Store *store, const OH_RDB_TransOptions *options, OH_Rdb_Transaction **trans) | - | 创建一个事务对象。 |
| int OH_Rdb_Attach(OH_Rdb_Store *store, const OH_Rdb_ConfigV2 *config, const char *attachName, int64_t waitTime,size_t *attachedNumber) | - | 将数据库文件附加到当前连接的数据库。 |
| int OH_Rdb_Detach(OH_Rdb_Store *store, const char *attachName, int64_t waitTime, size_t *attachedNumber) | - | 从当前数据库中分离指定的数据库。 |
| int OH_Rdb_SetLocale(OH_Rdb_Store *store, const char *locale) | - | 支持不同语言的排序规则。 |
| int OH_Rdb_SetSemanticIndex(OH_Rdb_ConfigV2 *config, bool enableSemanticIndex) | - | 开启或关闭基于语义索引的知识加工。 |
| int OH_Rdb_RekeyEx(OH_Rdb_Store *store, OH_Rdb_CryptoParam *param) | - | 更改加密数据库密钥。 不支持对非WAL模式的数据库进行密钥更新。 手动更新时需要独占访问数据库，此时若存在任何未释放的结果集、事务或其他进程打开的数据库均会导致更新失败。 支持加密数据库的参数更新，以及加密数据库与非加密数据库之间的相互转换。 数据库越大，执行更新所需的时间越长。 加密参数变更需谨慎，调用OH_Rdb_CreateOrOpen时需要传入正确的加密参数，否则可能打开数据库失败。 |
| typedef void (*Rdb_CorruptedHandler)(void *context, OH_Rdb_ConfigV2 *config, OH_Rdb_Store *store) | Rdb_CorruptedHandler | 数据库异常处理的回调函数。 |
| int OH_Rdb_RegisterCorruptedHandler(const OH_Rdb_ConfigV2 *config, void *context, const Rdb_CorruptedHandler handler) | - | 注册数据库异常处理。当数据库发生异常时，将调用异常处理的回调函数。 异常处理逻辑为用户自定义，回调时触发的业务需要用户自行保障。 每个路径只允许注册一次。 |
| int OH_Rdb_UnregisterCorruptedHandler(const OH_Rdb_ConfigV2 *config, void *context, const Rdb_CorruptedHandler handler) | - | 取消注册的数据库异常处理的回调函数。 handler和context必须要和订阅时保持一致，否则取消失败。 |
| OH_Cursor *OH_Rdb_QueryWithoutRowCount(OH_Rdb_Store *store, OH_Predicates *predicates, const char * const columns[], int length) | - | 根据指定条件查询数据库中的数据，不计算行数。 |
| OH_Cursor *OH_Rdb_QuerySqlWithoutRowCount(OH_Rdb_Store *store, const char *sql, const OH_Data_Values *args) | - | 执行有返回值的SQL语句，不计算行数，支持向量数据库。 |
| int OH_Rdb_BatchInsertWithReturning(OH_Rdb_Store *store, const char *table, const OH_Data_VBuckets *rows, Rdb_ConflictResolution resolution, OH_RDB_ReturningContext *context) | - | 将批量数据插入目标表，并将变更信息输出到上下文中。 |
| int OH_Rdb_UpdateWithReturning(OH_Rdb_Store *store, OH_VBucket *row, OH_Predicates *predicates, Rdb_ConflictResolution resolution, OH_RDB_ReturningContext *context) | - | 根据指定条件更新数据库中的数据并输出更改信息到上下文。 |
| int OH_Rdb_DeleteWithReturning(OH_Rdb_Store *store, OH_Predicates *predicates, OH_RDB_ReturningContext *context) | - | 根据指定条件从数据库中删除数据并输出更改信息到上下文。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| DISTRIBUTED_CONFIG_VERSION 1 | 描述Rdb_DistributedConfig的版本。 起始版本： 11 |
| DISTRIBUTED_CHANGE_INFO_VERSION 1 | 描述Rdb_ChangeInfo的版本。 起始版本： 11 |
| DISTRIBUTED_PROGRESS_DETAIL_VERSION 1 | 描述Rdb_ProgressDetails的版本。 起始版本： 11 |

**枚举类型说明**

**OH_Rdb_SecurityLevel**

```ets
enum OH_Rdb_SecurityLevel
```

描述

数据库的安全级别枚举。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| S1 = 1 | S1: 表示数据库的安全级别为低级别。当数据泄露时会产生较低影响。 |
| S2 | S2: 表示数据库的安全级别为中级别。当数据泄露时会产生较大影响。 |
| S3 | S3: 表示数据库的安全级别为高级别。当数据泄露时会产生重大影响。 |
| S4 | S4: 表示数据库的安全级别为关键级别。当数据泄露时会产生严重影响。 |

**Rdb_SecurityArea**

```ets
enum Rdb_SecurityArea
```

描述

描述数据库的安全区域等级。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| RDB_SECURITY_AREA_EL1 = 1 | 安全区域等级为1。 |
| RDB_SECURITY_AREA_EL2 | 安全区域等级为2。 |
| RDB_SECURITY_AREA_EL3 | 安全区域等级为3。 |
| RDB_SECURITY_AREA_EL4 | 安全区域等级为4。 |
| RDB_SECURITY_AREA_EL5 | 安全区域等级为5。 起始版本： 12 |

**Rdb_DBType**

```ets
enum Rdb_DBType
```

描述

描述数据库的内核类型。

起始版本： 14

| 枚举项 | 描述 |
| --- | --- |
| RDB_SQLITE = 1 | 表示使用sqlite作为数据库内核。 |
| RDB_CAYLEY = 2 | 表示使用凯莱数据库作为数据库内核。 |
| DBTYPE_BUTT = 64 | 表示内核类型枚举值允许取值的最大值，这是一个非法值。 |

**Rdb_Tokenizer**

```ets
enum Rdb_Tokenizer
```

描述

描述数据库的分词器类型。

起始版本： 17

| 枚举项 | 描述 |
| --- | --- |
| RDB_NONE_TOKENIZER = 1 | 表示不使用分词器。 |
| RDB_ICU_TOKENIZER = 2 | 表示使用ICU分词器。 |
| RDB_CUSTOM_TOKENIZER = 3 | 表示使用CUSTOM分词器。 起始版本： 18 |

**Rdb_DistributedType**

```ets
enum Rdb_DistributedType
```

描述

描述表的分布式类型的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| RDB_DISTRIBUTED_CLOUD | 表示在设备和云端之间分布式的数据库表。 |

**Rdb_ChangeType**

```ets
enum Rdb_ChangeType
```

描述

描述数据变更类型。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| RDB_DATA_CHANGE | 表示是数据发生变更。 |
| RDB_ASSET_CHANGE | 表示是资产附件发生了变更。 |

**Rdb_SubscribeType**

```ets
enum Rdb_SubscribeType
```

描述

描述订阅类型。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| RDB_SUBSCRIBE_TYPE_CLOUD | 订阅云端数据更改。 |
| RDB_SUBSCRIBE_TYPE_CLOUD_DETAILS | 订阅云端数据更改详情。 |
| RDB_SUBSCRIBE_TYPE_LOCAL_DETAILS | 订阅本地数据更改详情。 起始版本： 12 |

**Rdb_SyncMode**

```ets
enum Rdb_SyncMode
```

描述

表示数据库的同步模式。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| RDB_SYNC_MODE_TIME_FIRST | 表示数据从修改时间较近的一端同步到修改时间较远的一端。 |
| RDB_SYNC_MODE_NATIVE_FIRST | 表示数据从本地设备同步到云端。 |
| RDB_SYNC_MODE_CLOUD_FIRST | 表示数据从云端同步到本地设备。 |

**Rdb_Progress**

```ets
enum Rdb_Progress
```

描述

描述端云同步过程。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| RDB_SYNC_BEGIN | 表示端云同步过程开始。 |
| RDB_SYNC_IN_PROGRESS | 表示正在端云同步过程中。 |
| RDB_SYNC_FINISH | 表示端云同步过程已完成。 |

**Rdb_ProgressCode**

```ets
enum Rdb_ProgressCode
```

描述

表示端云同步过程的状态。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| RDB_SUCCESS | 表示端云同步过程成功。 |
| RDB_UNKNOWN_ERROR | 表示端云同步过程遇到未知错误。 |
| RDB_NETWORK_ERROR | 表示端云同步过程遇到网络错误。 |
| RDB_CLOUD_DISABLED | 表示云端不可用。 |
| RDB_LOCKED_BY_OTHERS | 表示有其他设备正在端云同步，本设备无法进行端云同步。 |
| RDB_RECORD_LIMIT_EXCEEDED | 表示本次端云同步需要同步的条目或大小超出最大值。由云端配置最大值。 |
| RDB_NO_SPACE_FOR_ASSET | 表示云空间剩余空间小于待同步的资产大小。 |

**函数说明**

**OH_Rdb_SetSemanticIndex()**

```ets
int OH_Rdb_SetSemanticIndex(OH_Rdb_ConfigV2 *config, bool enableSemanticIndex)
```

描述

开启或关闭基于语义索引的知识加工。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2实例的指针。 |
| bool enableSemanticIndex | 开启或关闭基于语义索引的知识加工能力标志。 true表示开启。false表示关闭。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。错误码定义详见OH_Rdb_ErrCode。 若返回RDB_OK，指向成功。 若返回RDB_E_INVALID_ARGS，表示传入了无效参数。 |

**OH_Rdb_CreateConfig()**

```ets
OH_Rdb_ConfigV2 *OH_Rdb_CreateConfig()
```

描述

创建一个[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)实例，并返回指向该实例的指针。

起始版本： 14

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Rdb_ConfigV2 | 返回一个指向OH_Rdb_ConfigV2实例的指针。 使用完成后，必须通过OH_Rdb_DestroyConfig接口释放内存。 |

参考：

OH_Rdb_ConfigV2

**OH_Rdb_DestroyConfig()**

```ets
int OH_Rdb_DestroyConfig(OH_Rdb_ConfigV2 *config)
```

描述

销毁由[OH_Rdb_CreateConfig](relational_store.h.md#ZH-CN_TOPIC_0000002522080654__oh_rdb_createconfig)创建的[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)对象。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SetDatabaseDir()**

```ets
int OH_Rdb_SetDatabaseDir(OH_Rdb_ConfigV2 *config, const char *databaseDir)
```

描述

给指定的数据库文件配置[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)，设置数据库文件路径。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| const char *dataBaseDir | 表示数据库文件路径。包含数据库名称在内的全路径长度不超过1024个字符。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SetStoreName()**

```ets
int OH_Rdb_SetStoreName(OH_Rdb_ConfigV2 *config, const char *storeName)
```

描述

给指定的数据库文件配置[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)，设置数据库名称。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| const char *storeName | 表示数据库名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SetBundleName()**

```ets
int OH_Rdb_SetBundleName(OH_Rdb_ConfigV2 *config, const char *bundleName)
```

描述

给指定的数据库文件配置[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)，设置应用包名。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| const char *bundleName | 表示数据库应用包名。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SetModuleName()**

```ets
int OH_Rdb_SetModuleName(OH_Rdb_ConfigV2 *config, const char *moduleName)
```

描述

给指定的数据库文件配置[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)，设置应用模块名。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| const char *moduleName | 表示数据库应用模块名。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SetEncrypted()**

```ets
int OH_Rdb_SetEncrypted(OH_Rdb_ConfigV2 *config, bool isEncrypted)
```

描述

给指定的数据库文件配置[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)，设置数据库是否加密。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| bool isEncrypted | 表示数据库是否加密。true表示加密，false表示不加密。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SetSecurityLevel()**

```ets
int OH_Rdb_SetSecurityLevel(OH_Rdb_ConfigV2 *config, int securityLevel)
```

描述

给指定的数据库文件配置[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)，设置数据库安全级别[OH_Rdb_SecurityLevel](relational_store.h.md#ZH-CN_TOPIC_0000002522080654__oh_rdb_securitylevel)。

创建数据库时必须调用该方法，否则数据库文件无法创建成功，调用[OH_Rdb_CreateOrOpen](#ZH-CN_TOPIC_0000002522080654__oh_rdb_createoropen)接口时将返回错误码RDB_E_INVALID_ARGS。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| int securityLevel | 表示数据库安全级别OH_Rdb_SecurityLevel。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SetArea()**

```ets
int OH_Rdb_SetArea(OH_Rdb_ConfigV2 *config, int area)
```

描述

给指定的数据库文件配置[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)，设置数据库安全区域等级[Rdb_SecurityArea](relational_store.h.md#ZH-CN_TOPIC_0000002522080654__rdb_securityarea)。

创建数据库时必须调用该方法，否则数据库文件无法创建成功，调用[OH_Rdb_CreateOrOpen](#ZH-CN_TOPIC_0000002522080654__oh_rdb_createoropen)接口时将返回错误码RDB_E_INVALID_ARGS。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| int area | 表示数据库安全区域等级Rdb_SecurityArea。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SetDbType()**

```ets
int OH_Rdb_SetDbType(OH_Rdb_ConfigV2 *config, int dbType)
```

描述

给指定的数据库文件配置[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)，设置数据库类型[Rdb_DBType](relational_store.h.md#ZH-CN_TOPIC_0000002522080654__rdb_dbtype)。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| int dbType | 表示数据库的数据库类型Rdb_DBType。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 RDB_E_NOT_SUPPORTED表示不支持当前操作。 |

**OH_Rdb_SetCustomDir()**

```ets
int OH_Rdb_SetCustomDir(OH_Rdb_ConfigV2 *config, const char *customDir)
```

描述

设置数据库的自定义目录。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 表示此关系型数据库相关的数据库配置OH_Rdb_ConfigV2的指针。 |
| const char *customDir | 表示数据库的自定义目录，目录长度不能超过128字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 |

**OH_Rdb_SetReadOnly()**

```ets
int OH_Rdb_SetReadOnly(OH_Rdb_ConfigV2 *config, bool readOnly)
```

描述

设置关系型数据库是否为只读模式。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 表示此关系型数据库相关的数据库配置OH_Rdb_ConfigV2的指针。 |
| bool readOnly | 表示关系型数据库存储是否为只读模式，true表示设置为只读模式，false表示设置为读写模式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 |

**OH_Rdb_SetPlugins()**

```ets
int OH_Rdb_SetPlugins(OH_Rdb_ConfigV2 *config, const char **plugins, int32_t length)
```

描述

设置具有特定功能（如全文检索）的动态库。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 表示此关系型数据库相关的数据库配置OH_Rdb_ConfigV2的指针。 |
| const char **plugins | 表示动态库的名称数组。 |
| int32_t length | 表示插件数组的大小，最大值为16。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 |

**OH_Rdb_SetCryptoParam()**

```ets
int OH_Rdb_SetCryptoParam(OH_Rdb_ConfigV2 *config, const OH_Rdb_CryptoParam *cryptoParam)
```

描述

设置自定义加密参数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 表示此关系型数据库相关的数据库配置OH_Rdb_ConfigV2的指针。 |
| const OH_Rdb_CryptoParam *cryptoParam | 表示自定义加密参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 |

**OH_Rdb_IsTokenizerSupported()**

```ets
int OH_Rdb_IsTokenizerSupported(Rdb_Tokenizer tokenizer, bool *isSupported)
```

描述

判断当前平台是否支持传入的分词器。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| Rdb_Tokenizer tokenizer | 要校验是否支持的分词器。 |
| bool *isSupported | 校验结果的指针，作为出参使用。true表示当前平台支持当前校验的分词器，false表示当前平台不支持当前校验的分词器。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回接口操作执行的状态码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SetTokenizer()**

```ets
int OH_Rdb_SetTokenizer(OH_Rdb_ConfigV2 *config, Rdb_Tokenizer tokenizer)
```

描述

给指定的数据库文件配置设置分词器类型。

起始版本： 17

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向此RDB存储相关的数据库配置的指针。 |
| Rdb_Tokenizer tokenizer | 表示数据库的分词器类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回接口操作执行的状态码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 RDB_E_NOT_SUPPORTED表示不支持当前操作。 |

**OH_Rdb_SetPersistent()**

```ets
int OH_Rdb_SetPersistent(OH_Rdb_ConfigV2 *config, bool isPersistent)
```

描述

指定数据库是否需要持久化。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2实例的指针。 指示与此RDB存储相关的数据库的配置。 |
| bool isPersistent | 指示数据库是否需要持久性。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的状态代码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_GetSupportedDbType()**

```ets
const int *OH_Rdb_GetSupportedDbType(int *typeCount)
```

描述

获得支持的数据库类型[Rdb_DBType](relational_store.h.md#ZH-CN_TOPIC_0000002522080654__rdb_dbtype)。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| int *typeCount | 表示支持的数据库类型的数组的长度, 作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const int * | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_CreateValueObject()**

```ets
OH_VObject *OH_Rdb_CreateValueObject()
```

描述

创建[OH_VObject](OH_VObject.md)实例。

起始版本： 10

返回：

| 类型 | 说明 |
| --- | --- |
| OH_VObject | 创建成功则返回一个指向OH_VObject结构体实例的指针，否则返回NULL。 |

参考：

OH_VObject

**OH_Rdb_CreateValuesBucket()**

```ets
OH_VBucket *OH_Rdb_CreateValuesBucket()
```

描述

创建[OH_VBucket](OH_VBucket.md)实例。

起始版本： 10

返回：

| 类型 | 说明 |
| --- | --- |
| OH_VBucket | 创建成功则返回一个指向OH_VBucket结构体实例的指针，否则返回NULL。 |

参考：

OH_VBucket

**OH_Rdb_CreatePredicates()**

```ets
OH_Predicates *OH_Rdb_CreatePredicates(const char *table)
```

描述

创建[OH_Predicates](OH_Predicates.md)实例。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *table | 表示数据库表名。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Predicates | 创建成功则返回一个指向OH_Predicates结构体实例的指针，否则返回NULL。 |

参考：

OH_Predicates

**OH_Rdb_GetOrOpen()**

```ets
OH_Rdb_Store *OH_Rdb_GetOrOpen(const OH_Rdb_Config *config, int *errCode)
```

描述

获得一个相关的[OH_Rdb_Store](OH_Rdb_Store.md)实例，操作关系型数据库。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Rdb_Config *config | 指向OH_Rdb_Config实例的指针，与此RDB存储相关的数据库配置。 |
| int *errCode | 表示函数执行状态, 作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Rdb_Store | 创建成功则返回一个指向OH_Rdb_Store结构体实例的指针，否则返回NULL。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_CreateOrOpen()**

```ets
OH_Rdb_Store *OH_Rdb_CreateOrOpen(const OH_Rdb_ConfigV2 *config, int *errCode)
```

描述

使用指定的数据库文件配置[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)，获得一个对应的[OH_Rdb_Store](OH_Rdb_Store.md)实例，用来操作关系型数据库。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| int *errCode | 表示函数执行状态，作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Rdb_Store | 创建成功则返回一个指向OH_Rdb_Store结构体实例的指针，否则返回NULL。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_CloseStore()**

```ets
int OH_Rdb_CloseStore(OH_Rdb_Store *store)
```

描述

销毁[OH_Rdb_Store](OH_Rdb_Store.md)对象，并回收该对象占用的内存。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_DeleteStore()**

```ets
int OH_Rdb_DeleteStore(const OH_Rdb_Config *config)
```

描述

使用指定的数据库文件配置删除数据库。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Rdb_Config *config | 表示数据库的配置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_DeleteStoreV2()**

```ets
int OH_Rdb_DeleteStoreV2(const OH_Rdb_ConfigV2 *config)
```

描述

使用指定的数据库文件配置[OH_Rdb_ConfigV2](OH_Rdb_ConfigV2.md)删除数据库。

当使用向量数据库时，在调用接口前，应当确保向量数据库已经打开的OH_Rdb_Store和OH_Cursor均已成功关闭。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Rdb_ConfigV2 *config | 表示数据库的配置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_Insert()**

```ets
int OH_Rdb_Insert(OH_Rdb_Store *store, const char *table, OH_VBucket *valuesBucket)
```

描述

向目标表中插入一行数据。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *table | 表示指定的目标表名。 |
| OH_VBucket *valuesBucket | 表示要插入到表中的数据行OH_VBucket。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 如果插入成功，返回rowID，否则返回的结果小于0。 RDB_ERR表示插入失败。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_InsertWithConflictResolution()**

```ets
int OH_Rdb_InsertWithConflictResolution(OH_Rdb_Store *store, const char *table, OH_VBucket *row,Rdb_ConflictResolution resolution, int64_t *rowId)
```

描述

向目标表中插入一行数据，并支持冲突解决。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *table | 表示目标表的名称。 |
| OH_VBucket *row | 表示要插入到表中的数据。 |
| Rdb_ConflictResolution resolution | 表示发生冲突时的解决策略。 |
| int64_t *rowId | 表示插入成功后返回的行号。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL文件大小超过默认限制。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库已损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误：违反约束导致操作中止。 |

**OH_Rdb_BatchInsert()**

```ets
int OH_Rdb_BatchInsert(OH_Rdb_Store *store, const char *table,const OH_Data_VBuckets *rows, Rdb_ConflictResolution resolution, int64_t *changes)
```

描述

将一批数据插入到目标表中。

单次插入参数的最大数量限制为32766，超出上限会返回RDB_E_INVALID_ARGS错误码。参数数量计算方式为插入数据条数乘以插入数据的所有字段的并集大小。

例如：插入数据的所有字段的并集大小为10，则最多可以插入3276条数据（3276*10=32760）。

请确保在调用接口时遵守此限制，以避免因参数数量过多而导致错误。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *tables | 要设置的分布式数据库表表名。 |
| const OH_Data_VBuckets *rows | 表示要插入到表中的一组数据。 |
| Rdb_ConflictResolution resolution | 表示发生冲突时的解决策略。 |
| int64_t *changes | 输出参数，表示插入成功的次数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误码：SQLite约束。 |

**OH_Rdb_Update()**

```ets
int OH_Rdb_Update(OH_Rdb_Store *store, OH_VBucket *valuesBucket, OH_Predicates *predicates)
```

描述

根据指定的条件更新数据库中的数据。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_VBucket *valuesBucket | 表示要更新到表中的数据行OH_VBucket。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针，指定更新条件。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 如果更新成功，返回更新的行数，否则返回的结果小于0。 RDB_ERR表示更新失败。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_UpdateWithConflictResolution()**

```ets
int OH_Rdb_UpdateWithConflictResolution(OH_Rdb_Store *store, OH_VBucket *row, OH_Predicates *predicates,Rdb_ConflictResolution resolution, int64_t *changes)
```

描述

根据指定条件更新数据库中的数据，并支持冲突解决。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_VBucket *row | 表示要更新到表中的数据行。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针，指定更新条件。 |
| Rdb_ConflictResolution resolution | 表示发生冲突时的解决策略。 |
| int64_t *changes | 输出参数，表示成功更新的行数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_ERROR 表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL文件大小超过默认限制。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库已损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误：违反约束导致操作中止。 |

**OH_Rdb_Delete()**

```ets
int OH_Rdb_Delete(OH_Rdb_Store *store, OH_Predicates *predicates)
```

描述

根据指定的条件删除数据库中的数据。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针，指定删除条件。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 如果删除成功，返回删除的行数；如果失败，则返回的结果小于0。 RDB_ERR表示删除失败。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_Query()**

```ets
OH_Cursor *OH_Rdb_Query(OH_Rdb_Store *store, OH_Predicates *predicates, const char *const *columnNames, int length)
```

描述

根据指定条件查询数据库中的数据

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针，指定查询条件。 |
| const char *const *columnNames | 表示要查询的列。如果值为空，则查询应用于所有列。 |
| int length | 该参数为输入参数，表示开发者传入的columnNames数组的长度。若length大于columnNames数组的实际长度，则会访问越界。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor * | 如果查询成功则返回一个指向OH_Cursor结构体实例的指针，否则返回NULL。 |

**OH_Rdb_Execute()**

```ets
int OH_Rdb_Execute(OH_Rdb_Store *store, const char *sql)
```

描述

执行无返回值的SQL语句。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *sql | 指定要执行的SQL语句。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

参考：

OH_Rdb_Store

**OH_Rdb_ExecuteV2()**

```ets
int OH_Rdb_ExecuteV2(OH_Rdb_Store *store, const char *sql, const OH_Data_Values *args, OH_Data_Value **result)
```

描述

执行有返回值的SQL语句，支持向量数据库。

不支持开头包含注释的语句。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *sql | 指定要执行的SQL语句。 |
| const OH_Data_Values *args | 可选参数，指向OH_Data_Values实例的指针。 |
| OH_Data_Value **result | 执行成功时指向OH_Data_Value实例的指针，作为出参使用。使用完成后，必须通过OH_Value_Destroy接口释放内存。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_ALREADY_CLOSED表示数据库已经关闭。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL日志文件大小超过默认值。 返回RDB_E_SQLITE_FULL表示SQLite错误码：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误码：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误码：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误码：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误码：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误码：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误码：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误码：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误码：数据类型不匹配。 |

参考：

OH_Value_Destroy

**OH_Rdb_ExecuteByTrxId()**

```ets
int OH_Rdb_ExecuteByTrxId(OH_Rdb_Store *store, int64_t trxId, const char *sql)
```

描述

使用指定的事务ID执行无返回值的SQL语句，仅支持向量数据库。

不支持开头包含注释的语句。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 表示一个指向OH_Rdb_Store 实例的指针。 |
| int64_t trxId | 调用OH_Rdb_BeginTransWithTrxId获得的事务ID，当设置为0时，表示不启用事务。 |
| const char *sql | 指定要执行的SQL语句。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数，可能情况如下： 传入参数为空指针。 当前事务ID不是调用OH_Rdb_BeginTransWithTrxId获得的。 当前事务ID已经调用OH_Rdb_CommitByTrxId提交。 当前事务ID已经调用OH_Rdb_RollBackByTrxId回滚。 当store或者sql为NULL时。 RDB_E_NOT_SUPPORTED表示不支持当前操作。 |

参考：

OH_Rdb_Store

**OH_Rdb_ExecuteQuery()**

```ets
OH_Cursor *OH_Rdb_ExecuteQuery(OH_Rdb_Store *store, const char *sql)
```

描述

根据指定SQL语句查询数据库中的数据，支持向量数据库。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *sql | 指定要执行的SQL语句。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor | 如果查询成功则返回一个指向OH_Cursor结构体实例的指针，否则返回NULL。 |

参考：

OH_Rdb_Store

**OH_Rdb_ExecuteQueryV2()**

```ets
OH_Cursor *OH_Rdb_ExecuteQueryV2(OH_Rdb_Store *store, const char *sql, const OH_Data_Values *args)
```

描述

根据指定SQL语句查询数据库中的数据，支持向量数据库。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *sql | 指定要执行的SQL语句。 |
| const OH_Data_Values *args | 可选参数，指向OH_Data_Values实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor * | 如果查询成功则返回一个指向OH_Cursor结构体实例的指针，使用完成后及时释放OH_Cursor。 如果SQL语句无效或内存分配失败，则返回NULL。 |

参考：

OH_Rdb_Store

**OH_Rdb_BeginTransaction()**

```ets
int OH_Rdb_BeginTransaction(OH_Rdb_Store *store)
```

描述

在开始执行SQL语句之前，开始事务。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_RollBack()**

```ets
int OH_Rdb_RollBack(OH_Rdb_Store *store)
```

描述

回滚已经执行的SQL语句。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_Commit()**

```ets
int OH_Rdb_Commit(OH_Rdb_Store *store)
```

描述

提交已执行的SQL语句

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_BeginTransWithTrxId()**

```ets
int OH_Rdb_BeginTransWithTrxId(OH_Rdb_Store *store, int64_t *trxId)
```

描述

在开始执行SQL语句之前，开始事务，并获得该事务的ID，仅支持向量数据库。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 表示一个指向OH_Rdb_Store实例的指针。 |
| int64_t *trxId | 事务ID，作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 RDB_E_NOT_SUPPORTED表示不支持当前操作。 |

**OH_Rdb_RollBackByTrxId()**

```ets
int OH_Rdb_RollBackByTrxId(OH_Rdb_Store *store, int64_t trxId)
```

描述

使用指定的事务ID, 回滚已经执行的SQL语句，仅支持向量数据库。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 表示一个指向OH_Rdb_Store实例的指针。 |
| int64_t trxId | 表示需要回滚的事务的ID。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数, 可能情况如下： 传入参数为空指针。 当前事务ID不是调用OH_Rdb_BeginTransWithTrxId获得的。 当前事务ID已经调用OH_Rdb_CommitByTrxId提交。 当前事务ID已经调用OH_Rdb_RollBackByTrxId回滚。 RDB_E_NOT_SUPPORTED表示不支持当前操作。 |

**OH_Rdb_CommitByTrxId()**

```ets
int OH_Rdb_CommitByTrxId(OH_Rdb_Store *store, int64_t trxId)
```

描述

使用指定的事务ID, 提交已经执行的SQL语句，仅支持向量数据库。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 表示一个指向OH_Rdb_Store实例的指针。 |
| int64_t trxId | 表示需要提交的事务的ID。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK 表示成功. RDB_E_INVALID_ARGS表示无效参数，可能情况如下： 传入参数为空指针。 当前事务ID不是调用OH_Rdb_BeginTransWithTrxId获得的。 当前事务ID已经调用OH_Rdb_CommitByTrxId提交。 当前事务ID已经调用OH_Rdb_RollBackByTrxId回滚。 RDB_E_NOT_SUPPORTED表示不支持当前操作。 |

参考：

OH_Rdb_Store

**OH_Rdb_Backup()**

```ets
int OH_Rdb_Backup(OH_Rdb_Store *store, const char *databasePath)
```

描述

以指定路径备份数据库，支持向量数据库。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *databasePath | 指定数据库的备份文件路径。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

参考：

OH_Rdb_Store

**OH_Rdb_Restore()**

```ets
int OH_Rdb_Restore(OH_Rdb_Store *store, const char *databasePath)
```

描述

从指定的数据库备份文件恢复数据库，支持向量数据库。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *databasePath | 指定数据库的备份文件路径。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_GetVersion()**

```ets
int OH_Rdb_GetVersion(OH_Rdb_Store *store, int *version)
```

描述

获取数据库版本。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| int *version | 表示版本号，作为出参使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SetVersion()**

```ets
int OH_Rdb_SetVersion(OH_Rdb_Store *store, int version)
```

描述

设置数据库版本。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| int version | 表示版本号。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

参考：

OH_Rdb_Store

**OH_Rdb_SetDistributedTables()**

```ets
int OH_Rdb_SetDistributedTables(OH_Rdb_Store *store, const char *tables[], uint32_t count, Rdb_DistributedType type,const Rdb_DistributedConfig *config)
```

描述

设置分布式数据库表。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *tables[] | 要设置的分布式数据库表表名。 |
| uint32_t count | 要设置的分布式数据库表的数量。 |
| Rdb_DistributedType type | 表的分布式类型Rdb_DistributedType。 |
| const Rdb_DistributedConfig *config | 表的分布式配置信息Rdb_DistributedConfig。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

参考：

OH_Rdb_Store

**OH_Rdb_FindModifyTime()**

```ets
OH_Cursor *OH_Rdb_FindModifyTime(OH_Rdb_Store *store, const char *tableName, const char *columnName,OH_VObject *values)
```

描述

获取数据库表中数据的最后修改时间。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *tableName | 要查找的分布式数据库表表名。 |
| const char *columnName | 指定要查询的数据库表的列名。 |
| OH_VObject *values | 指定要查询的行的主键。如果数据库表无主键，参数columnName需传入"rowid"，此时values为要查询的数据库表的行号。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor | 如果操作成功则返回一个指向OH_Rdb_Store结构体实例的指针，否则返回NULL。 |

**Rdb_BriefObserver()**

```ets
typedef void (*Rdb_BriefObserver)(void *context, const char *values[], uint32_t count)
```

描述

端云数据更改事件的回调函数。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| void *context | 表示数据观察者的上下文。 |
| const char *values[] | 表示更改的端云帐户。 |
| uint32_t count | 表示更改的端云帐户数量。 |

**Rdb_DetailsObserver()**

```ets
typedef void (*Rdb_DetailsObserver)(void *context, const Rdb_ChangeInfo **changeInfo, uint32_t count)
```

描述

端云数据更改事件的细节的回调函数。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| void *context | 表示数据观察者的上下文。 |
| const Rdb_ChangeInfo **changeInfo | 表示已更改表的信息Rdb_ChangeInfo。 |
| uint32_t count | 表示更改的表的数量。 |

**OH_Rdb_Subscribe()**

```ets
int OH_Rdb_Subscribe(OH_Rdb_Store *store, Rdb_SubscribeType type, const Rdb_DataObserver *observer)
```

描述

为数据库注册观察者。当分布式数据库或本地数据库中的数据发生更改时，将调用回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| Rdb_SubscribeType type | 表示在Rdb_SubscribeType中定义的订阅类型。如果其值为RDB_SUBSCRIBE_TYPE_LOCAL_DETAILS，则在本地数据库中的数据更改时调用回调。 |
| const Rdb_DataObserver *observer | 数据库中更改事件的观察者Rdb_DataObserver。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_Unsubscribe()**

```ets
int OH_Rdb_Unsubscribe(OH_Rdb_Store *store, Rdb_SubscribeType type, const Rdb_DataObserver *observer)
```

描述

从数据库中删除指定类型的指定观察者。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针 |
| Rdb_SubscribeType type | 表示在Rdb_SubscribeType中定义的订阅类型。 |
| const Rdb_DataObserver *observer | 数据库中更改事件的观察者Rdb_DataObserver。如果这是nullptr，表示删除该类型的所有观察者。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_GetTableDetails()**

```ets
Rdb_TableDetails *OH_Rdb_GetTableDetails(Rdb_ProgressDetails *progress, int32_t version)
```

描述

从端云同步任务的统计信息中获取数据库表的统计信息。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Rdb_ProgressDetails *progress | 指向Rdb_ProgressDetails实例的指针。 |
| int32_t version | 表示当前Rdb_ProgressDetails的版本。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Rdb_TableDetails | 如果操作成功，会返回一个Rdb_TableDetails结构体的指针，否则返回NULL。 |

参考：

Rdb_TableDetails

**Rdb_ProgressCallback()**

```ets
typedef void (*Rdb_ProgressCallback)(void *context, Rdb_ProgressDetails *progressDetails)
```

描述

端云同步进度的回调函数。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| void *context | 回调数据的上下文。 |
| Rdb_ProgressDetails *progressDetails | 端云同步进度的详细信息。 |

**Rdb_SyncCallback()**

```ets
typedef void (*Rdb_SyncCallback)(Rdb_ProgressDetails *progressDetails)
```

描述

数据库端云同步的回调函数。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Rdb_ProgressDetails *progressDetails | 数据库端云同步的统计信息。 |

**OH_Rdb_CloudSync()**

```ets
int OH_Rdb_CloudSync(OH_Rdb_Store *store, Rdb_SyncMode mode, const char *tables[], uint32_t count,const Rdb_ProgressObserver *observer)
```

描述

进行端云同步。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| Rdb_SyncMode mode | 表示同步过程的类型Rdb_SyncMode. |
| const char *tables[] | 表示需要同步的表名。 |
| uint32_t count | 同步的表的数量，如果传入的值为0，同步数据库的所有表。 |
| const Rdb_ProgressObserver *observer | 端云同步进度的观察者Rdb_ProgressObserver。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_SubscribeAutoSyncProgress()**

```ets
int OH_Rdb_SubscribeAutoSyncProgress(OH_Rdb_Store *store, const Rdb_ProgressObserver *observer)
```

描述

订阅RDB存储的自动同步进度。

当收到自动同步进度的通知时，将调用回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向目标OH_Rdb_Store实例的指针。 |
| const Rdb_ProgressObserver *observer | 用于自动同步进度的观察者Rdb_ProgressObserver。表示调用返回自动同步进度的回调。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_UnsubscribeAutoSyncProgress()**

```ets
int OH_Rdb_UnsubscribeAutoSyncProgress(OH_Rdb_Store *store, const Rdb_ProgressObserver *observer)
```

描述

取消订阅RDB存储的自动同步进程。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向目标OH_Rdb_Store实例的指针。 |
| const Rdb_ProgressObserver *observer | 表示自动同步进度的观察者Rdb_ProgressObserver。如果是空指针，则自动同步进程的所有回调都将被取消注册。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_LockRow()**

```ets
int OH_Rdb_LockRow(OH_Rdb_Store *store, OH_Predicates *predicates)
```

描述

根据指定的条件锁定数据库中的数据，锁定数据不执行端云同步。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针，指定锁定条件。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回锁定结果。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_UnlockRow()**

```ets
int OH_Rdb_UnlockRow(OH_Rdb_Store *store, OH_Predicates *predicates)
```

描述

根据指定的条件锁解锁数据库中的数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针，指定解锁条件。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回解锁结果。 RDB_OK表示成功。 RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Rdb_QueryLockedRow()**

```ets
OH_Cursor *OH_Rdb_QueryLockedRow(OH_Rdb_Store *store, OH_Predicates *predicates, const char *const *columnNames, int length)
```

描述

根据指定条件查询数据库中锁定的数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针，指定查询条件。 |
| const char *const *columnNames | 表示要查询的列。如果值为空，则查询应用于所有列。 |
| int length | 该参数为输入参数，表示开发者传入的columnNames数组的长度。若length大于columnNames数组的实际长度，则会访问越界。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor | 如果查询成功则返回一个指向OH_Cursor结构体实例的指针，否则返回NULL。 |

**OH_Rdb_CreateTransaction()**

```ets
int OH_Rdb_CreateTransaction(OH_Rdb_Store *store, const OH_RDB_TransOptions *options, OH_Rdb_Transaction **trans)
```

描述

创建一个事务对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const OH_RDB_TransOptions *options | 指向OH_RDB_TransOptions实例的指针。 |
| OH_Rdb_Transaction **trans | 输出参数，表示执行成功时指向OH_Rdb_Transaction实例的指针。否则返回nullptr。 使用完成后，必须通过OH_RdbTrans_Destroy接口释放内存。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示成功。 返回RDB_E_ERROR表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_DATABASE_BUSY表示数据库无响应。 返回RDB_E_SQLITE_FULL表示SQLite错误: 数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库已损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误: 访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误: 数据库文件被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误: 数据库内存不足。 返回RDB_E_SQLITE_IOERR表示SQLite错误: 磁盘I/O错误。 返回RDB_E_SQLITE_CANT_OPEN表示SQLite错误: 无法打开数据库文件。 |

**OH_Rdb_Attach()**

```ets
int OH_Rdb_Attach(OH_Rdb_Store *store, const OH_Rdb_ConfigV2 *config, const char *attachName, int64_t waitTime,size_t *attachedNumber)
```

描述

将数据库文件附加到当前连接的数据库。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const OH_Rdb_ConfigV2 *config | 指向与此RDB存储相关的数据库配置OH_Rdb_ConfigV2的指针。 |
| const char *attachName | 表示数据库的别名。 |
| int64_t waitTime | 表示附加数据库的最大允许时间，范围为1到300，单位为秒。 |
| size_t *attachedNumber | 表示已附加的数据库数量，作为输出参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_ERROR 表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_NOT_SUPPORTED表示不支持的操作。 返回RDB_E_DATABASE_BUSY表示数据库无响应。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库已损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误：违反约束导致操作中止。 |

**OH_Rdb_Detach()**

```ets
int OH_Rdb_Detach(OH_Rdb_Store *store, const char *attachName, int64_t waitTime, size_t *attachedNumber)
```

描述

从当前数据库中分离指定的数据库。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *attachName | 表示数据库的别名。 |
| int64_t waitTime | 表示分离数据库的最大允许时间，范围为1到300，单位为秒。 |
| size_t *attachedNumber | 表示已附加的数据库数量，作为输出参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_ERROR 表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_NOT_SUPPORTED表示不支持的操作。 返回RDB_E_DATABASE_BUSY表示数据库无响应。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库已损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误：数据库中的表被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误：磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误：违反约束导致操作中止。 |

**OH_Rdb_SetLocale()**

```ets
int OH_Rdb_SetLocale(OH_Rdb_Store *store, const char *locale)
```

描述

支持不同语言的排序规则。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *locale | 与语言相关的区域设置，例如 zh。该值符合 ISO 639 标准。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_ERR表示函数执行异常。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误：数据库内存不足。 |

**OH_Rdb_RekeyEx()**

```ets
int OH_Rdb_RekeyEx(OH_Rdb_Store *store, OH_Rdb_CryptoParam *param)
```

描述

更改加密数据库密钥。

不支持对非WAL模式的数据库进行密钥更新。

手动更新时需要独占访问数据库，此时若存在任何未释放的结果集、事务或其他进程打开的数据库均会导致更新失败。

支持加密数据库的参数更新，以及加密数据库与非加密数据库之间的相互转换。

数据库越大，执行更新所需的时间越长。

加密参数变更需谨慎，调用OH_Rdb_CreateOrOpen时需要传入正确的加密参数，否则可能打开数据库失败。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_Rdb_CryptoParam *param | 指向OH_Rdb_CryptoParam实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_ERROR 表示数据库常见错误。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_ALREADY_CLOSED表示数据库已关闭。 返回RDB_E_SQLITE_CORRUPT表示数据库已损坏。 返回RDB_E_SQLITE_PERM表示SQLite错误：访问权限被拒绝。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_NOMEM表示SQLite错误：数据库内存不足。 返回RDB_E_SQLITE_READONLY表示SQLite错误：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误：磁盘I/O错误。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 |

**Rdb_CorruptedHandler()**

```ets
typedef void (*Rdb_CorruptedHandler)(void *context, OH_Rdb_ConfigV2 *config, OH_Rdb_Store *store)
```

描述

数据库异常处理的回调函数。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| void *context | 表示数据异常处理的上下文，生命周期由业务自身管理。 |
| OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置，不可在回调函数外部使用。 |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针，该指针由系统产生，回调函数结束后即刻释放，不可在回调函数外部使用。 |

**OH_Rdb_RegisterCorruptedHandler()**

```ets
int OH_Rdb_RegisterCorruptedHandler(const OH_Rdb_ConfigV2 *config, void *context, const Rdb_CorruptedHandler handler)
```

描述

注册数据库异常处理。当数据库发生异常时，将调用异常处理的回调函数。

异常处理逻辑为用户自定义，回调时触发的业务需要用户自行保障。

每个路径只允许注册一次。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| void *context | 表示数据异常处理的上下文。 |
| const Rdb_CorruptedHandler handler | 数据库异常处理的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_SUB_LIMIT_REACHED表示注册数量超过限制。 |

**OH_Rdb_UnregisterCorruptedHandler()**

```ets
int OH_Rdb_UnregisterCorruptedHandler(const OH_Rdb_ConfigV2 *config, void *context, const Rdb_CorruptedHandler handler)
```

描述

取消注册的数据库异常处理的回调函数。

handler和context必须要和订阅时保持一致，否则取消失败。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_Rdb_ConfigV2 *config | 指向OH_Rdb_ConfigV2对象的指针，即与此RDB存储相关的数据库配置。 |
| void *context | 表示数据异常处理的上下文。 |
| const Rdb_CorruptedHandler handler | 数据库异常处理的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 |

**OH_Rdb_QueryWithoutRowCount()**

```ets
OH_Cursor *OH_Rdb_QueryWithoutRowCount(OH_Rdb_Store *store, OH_Predicates *predicates, const char * const columns[], int length)
```

描述

根据指定条件查询数据库中的数据，不计算行数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针，指定查询条件。 |
| const char * const columns[] | 要查询的列。如果值为空，则查询所有列。 |
| int length | 该参数为输入参数，表示开发者传入的columns数组的长度。若length大于columns数组的实际长度，则会访问越界。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor * | 如果查询成功则返回一个指向OH_Cursor结构体实例的指针。如果获取store失败或结果集为空，则返回nullptr。 |

**OH_Rdb_QuerySqlWithoutRowCount()**

```ets
OH_Cursor *OH_Rdb_QuerySqlWithoutRowCount(OH_Rdb_Store *store, const char *sql, const OH_Data_Values *args)
```

描述

执行有返回值的SQL语句，不计算行数，支持向量数据库。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *sql | 要执行的SQL语句。 |
| const OH_Data_Values *args | 指向OH_Data_Values实例的指针。SQL语句完整时，args可填写为nullptr。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Cursor * | 如果查询成功则返回一个指向OH_Cursor结构体实例的指针。如果SQL语句无效或内存分配失败，则返回nullptr。 |

**OH_Rdb_BatchInsertWithReturning()**

```ets
int OH_Rdb_BatchInsertWithReturning(OH_Rdb_Store *store, const char *table, const OH_Data_VBuckets *rows, Rdb_ConflictResolution resolution, OH_RDB_ReturningContext *context)
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
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| const char *table | 要插入的目标表名。 |
| const OH_Data_VBuckets *rows | 要插入到表中的行数据。 |
| Rdb_ConflictResolution resolution | 发生冲突时的解决策略Rdb_ConflictResolution，不建议使用RDB_CONFLICT_FAIL，因为失败时会抛异常， 无法正常获取实际的变更数据。 |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL文件大小超过默认限制。 返回RDB_E_NOT_SUPPORTED表示不支持的操作。 返回RDB_E_DATABASE_BUSY表示数据库忙。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误：数据库中的表被锁定。 返回RDB_E_SQLITE_READONLY表示SQLite错误：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误：发生某种磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误：由于违反约束而中止。 返回RDB_E_SQLITE_ERROR表示SQLite错误。可能原因：语法错误，例如表或列不存在。 具体错误码可参考OH_Rdb_ErrCode。 |

**OH_Rdb_UpdateWithReturning()**

```ets
int OH_Rdb_UpdateWithReturning(OH_Rdb_Store *store, OH_VBucket *row, OH_Predicates *predicates, Rdb_ConflictResolution resolution, OH_RDB_ReturningContext *context)
```

描述

根据指定条件更新数据库中的数据并输出更改信息到上下文。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_VBucket *row | 要更新到表中的行数据。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针。 |
| Rdb_ConflictResolution resolution | 发生冲突时的解决策略Rdb_ConflictResolution，不建议使用RDB_CONFLICT_FAIL，因为失败时会抛异常， 无法正常获取实际的变更数据。 |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL文件大小超过默认限制。 返回RDB_E_NOT_SUPPORTED表示不支持的操作。 返回RDB_E_EMPTY_VALUES_BUCKET表示值桶为空。 返回RDB_E_DATABASE_BUSY表示数据库忙。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误：数据库中的表被锁定。 返回RDB_E_SQLITE_READONLY表示SQLite错误：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误：发生某种磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误：数据类型不匹配。 返回RDB_E_SQLITE_CONSTRAINT表示SQLite错误：由于违反约束而中止。 返回RDB_E_SQLITE_ERROR表示SQLite错误。可能原因：语法错误，例如表或列不存在。 具体错误码可参考OH_Rdb_ErrCode。 |

**OH_Rdb_DeleteWithReturning()**

```ets
int OH_Rdb_DeleteWithReturning(OH_Rdb_Store *store, OH_Predicates *predicates, OH_RDB_ReturningContext *context)
```

描述

根据指定条件从数据库中删除数据并输出更改信息到上下文。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_Store *store | 指向OH_Rdb_Store实例的指针。 |
| OH_Predicates *predicates | 指向OH_Predicates实例的指针。 |
| OH_RDB_ReturningContext *context | 指向OH_RDB_ReturningContext实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 返回RDB_OK表示执行成功。 返回RDB_E_INVALID_ARGS表示输入参数无效。 返回RDB_E_WAL_SIZE_OVER_LIMIT表示WAL文件大小超过默认限制。 返回RDB_E_NOT_SUPPORTED表示不支持的操作。 返回RDB_E_DATABASE_BUSY表示数据库忙。 返回RDB_E_SQLITE_FULL表示SQLite错误：数据库已满。 返回RDB_E_SQLITE_CORRUPT表示数据库损坏。 返回RDB_E_SQLITE_BUSY表示SQLite错误：数据库文件被锁定。 返回RDB_E_SQLITE_LOCKED表示SQLite错误：数据库中的表被锁定。 返回RDB_E_SQLITE_READONLY表示SQLite错误：尝试写入只读数据库。 返回RDB_E_SQLITE_IOERR表示SQLite错误：发生某种磁盘I/O错误。 返回RDB_E_SQLITE_TOO_BIG表示SQLite错误：TEXT或BLOB超出大小限制。 返回RDB_E_SQLITE_MISMATCH表示SQLite错误：数据类型不匹配。 返回RDB_E_SQLITE_ERROR表示SQLite错误。可能原因：语法错误，例如表或列不存在。 具体错误码可参考OH_Rdb_ErrCode。 |