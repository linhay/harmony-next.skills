# Rdb_ProgressDetails

```ets
typedef struct Rdb_ProgressDetails {...} Rdb_ProgressDetails
```

**概述**

描述数据库整体执行端云同步任务上传和下载的统计信息。

起始版本： 11

相关模块： [RDB](RDB.md)

所在头文件： [relational_store.h](relational_store.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int version | 用于唯一标识OH_TableDetails结构的版本。 |
| int schedule | 表示端云同步过程。 |
| int code | 表示端云同步过程的状态。 |
| int32_t tableLength | 表示端云同步的表的数量。 |