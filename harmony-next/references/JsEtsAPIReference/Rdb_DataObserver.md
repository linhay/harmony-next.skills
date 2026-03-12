# Rdb_DataObserver

```ets
typedef struct Rdb_DataObserver {...} Rdb_DataObserver
```

#### 概述

表示数据观察者。

**起始版本：** 11

**相关模块：**[RDB](RDB.md)

**所在头文件：**[relational_store.h](relational_store.h.md)

#### 汇总

#### 成员变量

名称描述void* context表示数据观察者的上下文。[Rdb_SubscribeCallback](Rdb_SubscribeCallback.md) callback数据观察者的回调。