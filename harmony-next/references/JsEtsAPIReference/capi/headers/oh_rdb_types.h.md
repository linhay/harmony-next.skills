# oh_rdb_types.h

#### 概述

提供与数据值相关的类型定义。

**引用文件：** <database/rdb/oh_rdb_types.h>

**库：** libnative_rdb_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 18

**相关模块：**[RDB](../../topics/misc/RDB.md)

#### 汇总

#### 枚举

名称typedef关键字描述[Rdb_ConflictResolution](#ZH-CN_TOPIC_0000002497604704__rdb_conflictresolution)Rdb_ConflictResolution表示冲突解决策略的枚举。

#### 枚举类型说明

#### Rdb_ConflictResolution

```ets
enum Rdb_ConflictResolution
```

**描述**

表示冲突解决策略的枚举。

**起始版本：** 18

枚举项描述RDB_CONFLICT_NONE = 1发生冲突时不执行任何操作。RDB_CONFLICT_ROLLBACK发生冲突时抛错误码，同时回滚本次事务。RDB_CONFLICT_ABORT发生冲突时抛错误码，同时回滚本次修改。RDB_CONFLICT_FAIL发生冲突时抛错误码，不回滚冲突前的修改同时终止本次修改。RDB_CONFLICT_IGNORE发生冲突时忽略冲突的数据，继续执行后续修改。RDB_CONFLICT_REPLACE发生冲突时，尝试删除后插入，如果还是冲突则等同于RDB_CONFLICT_ABORT。