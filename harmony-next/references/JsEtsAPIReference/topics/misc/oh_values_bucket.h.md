# oh_values_bucket.h

**概述**

用于存储键值对的类型。

引用文件： <database/rdb/oh_values_bucket.h>

库： libnative_rdb_ndk.z.so

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

起始版本： 10

相关模块： [RDB](RDB.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_VBucket | OH_VBucket | 用于存储键值对的类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| int OH_VBucket_PutAsset(OH_VBucket *bucket, const char *field, Data_Asset *value) | 将Data_Asset 类型的对象放入给定列名的OH_VBucket对象中。 |
| int OH_VBucket_PutAssets(OH_VBucket *bucket, const char *field, Data_Asset **value, uint32_t count) | 将Data_Asset 类型的对象数组放入给定列名的OH_VBucket对象中。 |
| int OH_VBucket_PutFloatVector(OH_VBucket *bucket, const char *field, const float *vec, size_t len) | 将float数组类型对象放入给定列名的OH_VBucket对象中。 |
| int OH_VBucket_PutUnlimitedInt(OH_VBucket *bucket, const char *field, int sign, const uint64_t *trueForm, size_t len) | 将任意长度的整数类型对象放入给定列名的OH_VBucket对象中。 |

**函数说明**

**OH_VBucket_PutAsset()**

```ets
int OH_VBucket_PutAsset(OH_VBucket *bucket, const char *field, Data_Asset *value)
```

描述

将[Data_Asset](Data_Asset.md) 类型的对象放入给定列名的[OH_VBucket](OH_VBucket.md)对象中。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |
| const char *field | 数据库表中的列名。 |
| Data_Asset *value | 数据库表中指定列名对应的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK 表示成功。 RDB_E_INVALID_ARGS 表示无效参数。 |

**OH_VBucket_PutAssets()**

```ets
int OH_VBucket_PutAssets(OH_VBucket *bucket, const char *field, Data_Asset **value, uint32_t count)
```

描述

将[Data_Asset](Data_Asset.md) 类型的对象数组放入给定列名的[OH_VBucket](OH_VBucket.md)对象中。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |
| const char *field | 数据库表中的列名。 |
| Data_Asset **value | 数据库表中指定列名对应的值。 |
| uint32_t count | 表示传入的Data_Asset对象数组元素的个数. |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK 表示成功。 RDB_E_INVALID_ARGS 表示无效参数。 |

参考：

OH_VBucket

**OH_VBucket_PutFloatVector()**

```ets
int OH_VBucket_PutFloatVector(OH_VBucket *bucket, const char *field, const float *vec, size_t len)
```

描述

将float数组类型对象放入给定列名的[OH_VBucket](OH_VBucket.md)对象中。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |
| const char *field | 数据库表中的列名。 |
| const float *vec | 表示指向float数组的指针。 |
| size_t len | 表示float数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK 表示成功。 RDB_E_INVALID_ARGS 表示无效参数。 |

参考：

OH_VBucket

**OH_VBucket_PutUnlimitedInt()**

```ets
int OH_VBucket_PutUnlimitedInt(OH_VBucket *bucket, const char *field, int sign, const uint64_t *trueForm, size_t len)
```

描述

将任意长度的整数类型对象放入给定列名的[OH_VBucket](OH_VBucket.md)对象中。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |
| const char *field | 数据库表中的列名。 |
| int sign | 表示整数类型对象是正数还是负数，0表示正数，1表示负数。 |
| const uint64_t *trueForm | 表示指向整数类型数组的指针。 |
| size_t len | 表示整数数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 RDB_OK 表示成功。 RDB_E_INVALID_ARGS 表示无效参数。 |