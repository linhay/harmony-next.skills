# Rdb_KeyInfo

```ets
typedef struct {...} Rdb_KeyInfo
```

#### 概述

描述发生变化的行的主键或者行号。

**起始版本：** 11

**相关模块：**[RDB](RDB.md)

**所在头文件：**[relational_store.h](relational_store.h.md)

#### 汇总

#### 成员变量

名称描述int count表示发生变化的主键或者行号的数量。int type表示主键的类型[OH_ColumnType](oh_data_value.h.md#ZH-CN_TOPIC_0000002529284693__oh_columntype)。[Rdb_KeyData](Rdb_KeyData.md)* data存放变化的具体数据