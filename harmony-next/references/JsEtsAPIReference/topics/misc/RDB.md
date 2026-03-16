# RDB

#### 概述

分布式数据管理（Distributed data manager，data）支持单设备的各种结构化数据的持久化，以及端云间的同步、共享功能。

分布式数据管理定义了一系列数据类型，可以对数据进行增删改查。

**起始版本：** 11

#### 文件汇总

名称描述[data_asset.h](../../capi/headers/data_asset.h.md)

提供资产类型数据结构。

资产是指一种可以在数据管理中使用的数据结构，可以存储及查询一个文件的名称、绝对路径、相对路径、创建时间、修改时间、状态、占用空间等属性。

[oh_cursor.h](../../capi/headers/oh_cursor.h.md)提供通过查询数据库生成的数据库结果集的访问方法。结果集是指用户调用关系型数据库查询接口之后返回的结果集合，提供了多种灵活的数据访问方式，以便用户获取各项数据。[oh_data_value.h](../../capi/headers/oh_data_value.h.md)

提供与单条数据值相关的函数和枚举。

从API version 18开始，OH_ColumnType从oh_cursor.h移动至此头文件呈现，对于此类型，API version 18之前即支持使用，各版本均可正常使用。

[oh_data_values.h](../../capi/headers/oh_data_values.h.md)提供与多条数据值相关的函数和枚举。[oh_data_values_buckets.h](../../capi/headers/oh_data_values_buckets.h.md)提供与存储数据值相关的结构定义、函数和枚举。[oh_predicates.h](../../capi/headers/oh_predicates.h.md)表示关系型数据库（RDB）的谓词。[oh_rdb_crypto_param.h](../../capi/headers/oh_rdb_crypto_param.h.md)提供与关系型数据库加密参数相关的函数和枚举。[oh_rdb_transaction.h](../../capi/headers/oh_rdb_transaction.h.md)提供与数据库事务相关的函数和枚举。[oh_rdb_types.h](../../capi/headers/oh_rdb_types.h.md)提供与数据值相关的类型定义。[oh_value_object.h](../../capi/headers/oh_value_object.h.md)提供类型转换方法。[oh_values_bucket.h](../../capi/headers/oh_values_bucket.h.md)用于存储键值对的类型。[relational_store.h](../../capi/headers/relational_store.h.md)提供管理关系数据库（RDB）方法的接口，未标注支持向量数据库的接口仅支持关系型数据库。[relational_store_error_code.h](../../capi/headers/relational_store_error_code.h.md)声明关系型数据库（RDB）的错误码信息。