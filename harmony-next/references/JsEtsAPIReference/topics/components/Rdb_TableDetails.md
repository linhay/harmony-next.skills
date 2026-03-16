# Rdb_TableDetails

```ets
typedef struct Rdb_TableDetails {...} Rdb_TableDetails
```

#### 概述

描述数据库表执行端云同步任务上传和下载的统计信息。

**起始版本：** 11

**相关模块：**[RDB](../misc/RDB.md)

**所在头文件：**[relational_store.h](../../capi/headers/relational_store.h.md)

#### 汇总

#### 成员变量

名称描述const char* table数据库表名。[Rdb_Statistic](../misc/Rdb_Statistic.md) upload表示数据库表中端云同步上传过程的统计信息。[Rdb_Statistic](../misc/Rdb_Statistic.md) download表示数据库表中端云同步下载过程的统计信息。