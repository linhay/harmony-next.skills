# Rdb_DistributedConfig

```ets
typedef struct Rdb_DistributedConfig {...} Rdb_DistributedConfig
```

#### 概述

记录表的分布式配置信息。

**起始版本：** 11

**相关模块：**[RDB](RDB.md)

**所在头文件：**[relational_store.h](relational_store.h.md)

#### 汇总

#### 成员变量

名称描述int version用于唯一标识Rdb_DistributedConfig结构的版本。bool isAutoSync表示该表是否支持自动同步。true表示该表支持自动同步和手动同步，false表示该表只支持手动同步，不支持自动同步。