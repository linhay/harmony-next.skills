# Rdb_ChangeInfo

```ets
typedef struct Rdb_ChangeInfo {...} Rdb_ChangeInfo
```

#### 概述

记录端云同步过程详情。

**起始版本：** 11

**相关模块：**[RDB](RDB.md)

**所在头文件：**[relational_store.h](../../capi/headers/relational_store.h.md)

#### 汇总

#### 成员变量

名称描述int version用于唯一标识Rdb_DistributedConfig结构的版本。const char* tableName表示发生变化的表的名称。int ChangeType表示发生变化的数据的类型，数据或者资产附件发生变化。[Rdb_KeyInfo](Rdb_KeyInfo.md) inserted记录插入数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示插入数据的行号。[Rdb_KeyInfo](Rdb_KeyInfo.md) updated记录更新数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示更新数据的行号。[Rdb_KeyInfo](Rdb_KeyInfo.md) deleted记录删除数据的位置，如果该表的主键是string类型，该值是主键的值，否则该值表示删除数据的行号。