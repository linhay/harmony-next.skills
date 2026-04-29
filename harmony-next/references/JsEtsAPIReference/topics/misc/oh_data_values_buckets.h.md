# oh_data_values_buckets.h

**概述**

提供与存储数据值相关的结构定义、函数和枚举。

引用文件： <database/data/oh_data_values_buckets.h>

库： libnative_rdb_ndk.z.so

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

起始版本： 18

相关模块： [RDB](RDB.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Data_VBuckets | OH_Data_VBuckets | 定义OH_Data_VBuckets结构类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Data_VBuckets *OH_VBuckets_Create(void) | 创建OH_Data_VBuckets实例。 |
| int OH_VBuckets_Destroy(OH_Data_VBuckets *buckets) | 销毁OH_Data_VBuckets对象。 |
| int OH_VBuckets_PutRow(OH_Data_VBuckets *buckets, const OH_VBucket *row) | 添加OH_VBucket类型数据。 |
| int OH_VBuckets_PutRows(OH_Data_VBuckets *buckets, const OH_Data_VBuckets *rows) | 添加OH_Data_VBuckets类型数据。 |
| int OH_VBuckets_RowCount(OH_Data_VBuckets *buckets, size_t *count) | 获取OH_Data_VBuckets中OH_VBucket的行数。 |

**函数说明**

**OH_VBuckets_Create()**

```ets
OH_Data_VBuckets *OH_VBuckets_Create(void)
```

描述

创建OH_Data_VBuckets实例。

起始版本： 18

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Data_VBuckets | 执行成功时返回指向OH_Data_VBuckets实例的指针。否则返回nullptr。 使用完成后，必须通过OH_VBuckets_Destroy接口释放内存。 |

**OH_VBuckets_Destroy()**

```ets
int OH_VBuckets_Destroy(OH_Data_VBuckets *buckets)
```

描述

销毁OH_Data_VBuckets对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_VBuckets *buckets | 表示指向OH_Data_VBuckets实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_VBuckets_PutRow()**

```ets
int OH_VBuckets_PutRow(OH_Data_VBuckets *buckets, const OH_VBucket *row)
```

描述

添加OH_VBucket类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_VBuckets *buckets | 表示指向OH_Data_VBuckets实例的指针。 |
| const OH_VBucket *row | 表示指向OH_VBucket实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_VBuckets_PutRows()**

```ets
int OH_VBuckets_PutRows(OH_Data_VBuckets *buckets, const OH_Data_VBuckets *rows)
```

描述

添加OH_Data_VBuckets类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_VBuckets *buckets | 表示指向OH_Data_VBuckets实例的指针。 |
| const OH_Data_VBuckets *rows | 表示指向OH_Data_VBuckets实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_VBuckets_RowCount()**

```ets
int OH_VBuckets_RowCount(OH_Data_VBuckets *buckets, size_t *count)
```

描述

获取OH_Data_VBuckets中OH_VBucket的行数。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_VBuckets *buckets | 表示指向OH_Data_VBuckets实例的指针。 |
| size_t *count | 一个输出参数，表示OH_Data_VBuckets中OH_VBucket的个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |