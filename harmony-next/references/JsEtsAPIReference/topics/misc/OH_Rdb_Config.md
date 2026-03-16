# OH_Rdb_Config

```ets
typedef struct  {...} OH_Rdb_Config
```

#### 概述

管理关系数据库配置。

**起始版本：** 10

**相关模块：**[RDB](RDB.md)

**所在头文件：**[relational_store.h](../../capi/headers/relational_store.h.md)

#### 汇总

#### 成员变量

名称描述int selfSize该结构体的大小。const char* dataBaseDir数据库文件路径。const char* storeName数据库名称。const char* bundleName应用包名。const char* moduleName应用模块名。bool isEncrypt指定数据库是否加密。true表示加密，false表示不加密。int securityLevel设置数据库安全级别[OH_Rdb_SecurityLevel](../../capi/headers/relational_store.h.md#ZH-CN_TOPIC_0000002529444671__oh_rdb_securitylevel)。int area

设置数据库安全区域等级[Rdb_SecurityArea](../../capi/headers/relational_store.h.md#ZH-CN_TOPIC_0000002529444671__rdb_securityarea)

**起始版本：** 11