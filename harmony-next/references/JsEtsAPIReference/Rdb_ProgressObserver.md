# Rdb_ProgressObserver

```ets
typedef struct Rdb_ProgressObserver {...} Rdb_ProgressObserver
```

#### 概述

端云同步进度观察者。

**起始版本：** 11

**相关模块：**[RDB](RDB.md)

**所在头文件：**[relational_store.h](relational_store.h.md)

#### 汇总

#### 成员变量

名称描述void* context端云同步进度观察者的上下文。[Rdb_ProgressCallback](relational_store.h.md#ZH-CN_TOPIC_0000002529444671__rdb_progresscallback) callback端云同步进度观察者的回调函数。