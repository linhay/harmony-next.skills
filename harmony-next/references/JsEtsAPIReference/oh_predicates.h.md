# oh_predicates.h

#### 概述

表示关系型数据库（RDB）的谓词。

**引用文件：** <database/rdb/oh_predicates.h>

**库：** libnative_rdb_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 10

**相关模块：**[RDB](RDB.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_Predicates](OH_Predicates.md)OH_Predicates表示谓词。

#### 枚举

名称typedef关键字描述[OH_OrderType](#ZH-CN_TOPIC_0000002497444724__oh_ordertype)OH_OrderType排序方式。

#### 函数

名称描述[int OH_Predicates_NotLike(OH_Predicates *predicates, const char *field, const char *pattern)](#ZH-CN_TOPIC_0000002497444724__oh_predicates_notlike)

设置OH_Predicates以匹配数据类型为字符串且值不类似于指定值的字段。

此方法类似于SQL语句中的“Not like”。

[int OH_Predicates_Glob(OH_Predicates *predicates, const char *field, const char *pattern)](#ZH-CN_TOPIC_0000002497444724__oh_predicates_glob)

设置OH_Predicates以匹配指定字段（数据类型为字符串）且值包含通配符的字段。

与like方法不同，此方法的输入参数区分大小写。

[int OH_Predicates_NotGlob(OH_Predicates *predicates, const char *field, const char *pattern)](#ZH-CN_TOPIC_0000002497444724__oh_predicates_notglob)

设置OH_Predicates以不匹配指定字段（数据类型为字符串）且值包含通配符的字段。

与Not Like方法不同，此方法的输入参数区分大小写。

[int OH_Predicates_Having(OH_Predicates *predicates, const char *conditions, const OH_Data_Values *values)](#ZH-CN_TOPIC_0000002497444724__oh_predicates_having)设置OH_Predicates以指定条件来过滤分组结果，这些结果将出现在最终结果中。

#### 枚举类型说明

#### OH_OrderType

```ets
enum OH_OrderType
```

**描述**

排序方式。

**起始版本：** 10

枚举项描述ASC = 0升序排列。DESC = 1降序排列。

#### 函数说明

#### OH_Predicates_NotLike()

```ets
int OH_Predicates_NotLike(OH_Predicates *predicates, const char *field, const char *pattern)
```

**描述**

设置OH_Predicates以匹配数据类型为字符串且值不类似于指定值的字段。

此方法类似于SQL语句中的“Not like”。

**起始版本：** 20

**参数：**

参数项描述[OH_Predicates](OH_Predicates.md) *predicates表示指向[OH_Predicates](OH_Predicates.md)实例的指针。const char *field表示数据库表中的列名。const char *pattern表示谓词不匹配的模式。

**返回：**

类型说明int

返回执行结果。

如果执行成功，返回RDB_OK。

如果输入参数无效，返回RDB_E_INVALID_ARGS。

#### OH_Predicates_Glob()

```ets
int OH_Predicates_Glob(OH_Predicates *predicates, const char *field, const char *pattern)
```

**描述**

设置OH_Predicates以匹配指定字段（数据类型为字符串）且值包含通配符的字段。

与like方法不同，此方法的输入参数区分大小写。

**起始版本：** 20

**参数：**

参数项描述[OH_Predicates](OH_Predicates.md) *predicates表示指向[OH_Predicates](OH_Predicates.md)实例的指针。const char *field表示数据库表中的列名。const char *pattern表示谓词匹配的样式。

**返回：**

类型说明int

返回执行结果。

如果执行成功，返回RDB_OK。

如果输入参数无效，返回RDB_E_INVALID_ARGS。

#### OH_Predicates_NotGlob()

```ets
int OH_Predicates_NotGlob(OH_Predicates *predicates, const char *field, const char *pattern)
```

**描述**

设置OH_Predicates以不匹配指定字段（数据类型为字符串）且值包含通配符的字段。

与Not Like方法不同，此方法的输入参数区分大小写。

**起始版本：** 20

**参数：**

参数项描述[OH_Predicates](OH_Predicates.md) *predicates表示指向[OH_Predicates](OH_Predicates.md)实例的指针。const char *field表示数据库表中的列名。const char *pattern表示谓词不匹配的样式。

**返回：**

类型说明int

返回执行结果。

如果执行成功，返回RDB_OK。

如果输入参数无效，返回RDB_E_INVALID_ARGS。

#### OH_Predicates_Having()

```ets
int OH_Predicates_Having(OH_Predicates *predicates, const char *conditions, const OH_Data_Values *values)
```

**描述**

设置OH_Predicates以指定条件来过滤分组结果，这些结果将出现在最终结果中。

**起始版本：** 20

**参数：**

参数项描述[OH_Predicates](OH_Predicates.md) *predicates表示指向[OH_Predicates](OH_Predicates.md)实例的指针。const char *conditions表示having子句中的过滤条件。const [OH_Data_Values](OH_Data_Values.md) *values表示指向[OH_Data_Values](OH_Data_Values.md)实例的指针。

**返回：**

类型说明int

返回错误码。

如果执行成功，返回RDB_OK。

如果输入参数无效，返回RDB_E_INVALID_ARGS。