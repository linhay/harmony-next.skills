# Rdb_Statistic

```ets
typedef struct Rdb_Statistic {...} Rdb_Statistic
```

#### 概述

描述数据库表的端云同步过程的统计信息。

**起始版本：** 11

**相关模块：**[RDB](RDB.md)

**所在头文件：**[relational_store.h](../../capi/headers/relational_store.h.md)

#### 汇总

#### 成员变量

名称描述int total表示数据库表中需要端云同步的总行数。int successful表示数据库表中端云同步成功的行数。int failed表示数据库表中端云同步失败的行数。int remained表示数据库表中端云同步剩余未执行的行数。