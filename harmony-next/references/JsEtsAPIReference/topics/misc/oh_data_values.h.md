# oh_data_values.h

**概述**

提供与多条数据值相关的函数和枚举。

引用文件： <database/data/oh_data_values.h>

库： libnative_rdb_ndk.z.so

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

起始版本： 18

相关模块： [RDB](RDB.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Data_Values | OH_Data_Values | 定义OH_Data_Values结构类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Data_Values *OH_Values_Create(void) | 创建OH_Data_Values实例，用于储存多条键值对数据。 |
| int OH_Values_Destroy(OH_Data_Values *values) | 销毁OH_Data_Values对象。 |
| int OH_Values_Put(OH_Data_Values *values, const OH_Data_Value *val) | 添加OH_Data_Value类型数据给OH_Data_Values对象。 |
| int OH_Values_PutNull(OH_Data_Values *values) | 添加空数据给OH_Data_Values对象。 |
| int OH_Values_PutInt(OH_Data_Values *values, int64_t val) | 添加整型数据给OH_Data_Values对象。 |
| int OH_Values_PutReal(OH_Data_Values *values, double val) | 添加REAL类型数据给OH_Data_Values对象。 |
| int OH_Values_PutText(OH_Data_Values *values, const char *val) | 添加字符串类型数据给OH_Data_Values对象。 |
| int OH_Values_PutBlob(OH_Data_Values *values, const unsigned char *val, size_t length) | 添加BLOB类型数据给OH_Data_Values对象。 |
| int OH_Values_PutAsset(OH_Data_Values *values, const Data_Asset *val) | 添加ASSET类型数据给OH_Data_Values对象。 |
| int OH_Values_PutAssets(OH_Data_Values *values, const Data_Asset * const * val, size_t length) | 添加ASSETS类型数据给OH_Data_Values对象。 |
| int OH_Values_PutFloatVector(OH_Data_Values *values, const float *val, size_t length) | 添加float数组类型数据给OH_Data_Values对象。 |
| int OH_Values_PutUnlimitedInt(OH_Data_Values *values, int sign, const uint64_t *trueForm, size_t length) | 添加任意长度的整型数组数据给OH_Data_Values对象。 |
| int OH_Values_Count(OH_Data_Values *values, size_t *count) | 获取数据个数。 |
| int OH_Values_GetType(OH_Data_Values *values, int index, OH_ColumnType *type) | 获取数据类型。 |
| int OH_Values_Get(OH_Data_Values *values, int index, OH_Data_Value **val) | 获取OH_Data_Value类型数据。 |
| int OH_Values_IsNull(OH_Data_Values *values, int index, bool *val) | 检查数据是否为空。 |
| int OH_Values_GetInt(OH_Data_Values *values, int index, int64_t *val) | 获取整型数据。 |
| int OH_Values_GetReal(OH_Data_Values *values, int index, double *val) | 获取REAL类型数据。 |
| int OH_Values_GetText(OH_Data_Values *values, int index, const char **val) | 获取字符串类型数据。 |
| int OH_Values_GetBlob(OH_Data_Values *values, int index, const uint8_t **val, size_t *length) | 获取BLOB类型数据。 |
| int OH_Values_GetAsset(OH_Data_Values *values, int index, Data_Asset *val) | 获取ASSET类型数据。 |
| int OH_Values_GetAssetsCount(OH_Data_Values *values, int index, size_t *length) | 获取ASSETS类型数据的大小。 |
| int OH_Values_GetAssets(OH_Data_Values *values, int index, Data_Asset **val, size_t inLen, size_t *outLen) | 获取ASSETS类型数据。 |
| int OH_Values_GetFloatVectorCount(OH_Data_Values *values, int index, size_t *length) | 获取float数组类型数据的大小。 |
| int OH_Values_GetFloatVector(OH_Data_Values *values, int index, float *val, size_t inLen, size_t *outLen) | 获取float数组类型数据。 |
| int OH_Values_GetUnlimitedIntBand(OH_Data_Values *values, int index, size_t *length) | 获取任意长度的整型数据的大小。 |
| int OH_Values_GetUnlimitedInt(OH_Data_Values *values, int index, int *sign, uint64_t *trueForm, size_t inLen,size_t *outLen) | 获取任意长度的整型数据。 |

**函数说明**

**OH_Values_Create()**

```ets
OH_Data_Values *OH_Values_Create(void)
```

描述

创建[OH_Data_Values](OH_Data_Values.md)实例，用于储存多条键值对数据。

起始版本： 18

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Data_Values | 执行成功时返回指向OH_Data_Values实例的指针，否则返回nullptr。 使用完成后，必须通过OH_Values_Destroy接口释放内存。 |

**OH_Values_Destroy()**

```ets
int OH_Values_Destroy(OH_Data_Values *values)
```

描述

销毁[OH_Data_Values](OH_Data_Values.md)对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_Put()**

```ets
int OH_Values_Put(OH_Data_Values *values, const OH_Data_Value *val)
```

描述

添加OH_Data_Value类型数据给OH_Data_Values对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| const OH_Data_Value *val | 表示指向OH_Data_Value对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_PutNull()**

```ets
int OH_Values_PutNull(OH_Data_Values *values)
```

描述

添加空数据给OH_Data_Values对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_PutInt()**

```ets
int OH_Values_PutInt(OH_Data_Values *values, int64_t val)
```

描述

添加整型数据给OH_Data_Values对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int64_t val | 表示整型数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_PutReal()**

```ets
int OH_Values_PutReal(OH_Data_Values *values, double val)
```

描述

添加REAL类型数据给OH_Data_Values对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| double val | 表示REAL类型数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_PutText()**

```ets
int OH_Values_PutText(OH_Data_Values *values, const char *val)
```

描述

添加字符串类型数据给OH_Data_Values对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| const char *val | 表示字符串类型数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_PutBlob()**

```ets
int OH_Values_PutBlob(OH_Data_Values *values, const unsigned char *val, size_t length)
```

描述

添加BLOB类型数据给OH_Data_Values对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| const unsigned char *val | 表示BLOB类型数据。 |
| size_t length | 该参数为输入参数，表示开发者传入的BLOB类型数据的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_PutAsset()**

```ets
int OH_Values_PutAsset(OH_Data_Values *values, const Data_Asset *val)
```

描述

添加ASSET类型数据给OH_Data_Values对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| const Data_Asset *val | 表示指向Data_Asset对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_PutAssets()**

```ets
int OH_Values_PutAssets(OH_Data_Values *values, const Data_Asset * const * val, size_t length)
```

描述

添加ASSETS类型数据给OH_Data_Values对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| const Data_Asset * const * val | 表示指向Data_Asset对象的指针。 |
| size_t length | 该参数为输入参数，表示开发者传入的Data_Asset对象数组元素的个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_PutFloatVector()**

```ets
int OH_Values_PutFloatVector(OH_Data_Values *values, const float *val, size_t length)
```

描述

添加float数组类型数据给OH_Data_Values对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| const float *val | 表示指向float数组对象的指针。 |
| size_t length | 该参数为输入参数，表示开发者传入的float数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_PutUnlimitedInt()**

```ets
int OH_Values_PutUnlimitedInt(OH_Data_Values *values, int sign, const uint64_t *trueForm, size_t length)
```

描述

添加任意长度的整型数组数据给OH_Data_Values对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int sign | 表示正负数，0表示正整数，1表示负整数。 |
| const uint64_t *trueForm | 表示指向整型数组的指针。 |
| size_t length | 该参数为输入参数，表示开发者传入的整型数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_Count()**

```ets
int OH_Values_Count(OH_Data_Values *values, size_t *count)
```

描述

获取数据个数。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| size_t *count | 一个输出参数，表示values中数据的个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_GetType()**

```ets
int OH_Values_GetType(OH_Data_Values *values, int index, OH_ColumnType *type)
```

描述

获取数据类型。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| OH_ColumnType *type | 一个输出参数，表示数据类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_Get()**

```ets
int OH_Values_Get(OH_Data_Values *values, int index, OH_Data_Value **val)
```

描述

获取OH_Data_Value类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| OH_Data_Value **val | 一个输出参数，表示指向OH_Data_Value实例的指针。 无需申请内存和释放内存。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_IsNull()**

```ets
int OH_Values_IsNull(OH_Data_Values *values, int index, bool *val)
```

描述

检查数据是否为空。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| bool *val | 一个输出参数，true表示空，false表示不为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Values_GetInt()**

```ets
int OH_Values_GetInt(OH_Data_Values *values, int index, int64_t *val)
```

描述

获取整型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| int64_t *val | 一个输出参数，表示指向整型数据的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Values_GetReal()**

```ets
int OH_Values_GetReal(OH_Data_Values *values, int index, double *val)
```

描述

获取REAL类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| double *val | 一个输出参数，表示指向REAL类型数据的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Values_GetText()**

```ets
int OH_Values_GetText(OH_Data_Values *values, int index, const char **val)
```

描述

获取字符串类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| const char **val | 一个输出参数，表示指向字符串类型数据的指针。 无需申请内存和释放内存。 val的生命周期遵循values中index的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Values_GetBlob()**

```ets
int OH_Values_GetBlob(OH_Data_Values *values, int index, const uint8_t **val, size_t *length)
```

描述

获取BLOB类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| const uint8_t **val | 一个输出参数，表示指向BLOB类型数据的指针。 无需申请内存和释放内存。 val的生命周期遵循values中index的值。 |
| size_t *length | 该参数为输出参数，表示BLOB类型数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Values_GetAsset()**

```ets
int OH_Values_GetAsset(OH_Data_Values *values, int index, Data_Asset *val)
```

描述

获取ASSET类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| Data_Asset *val | 表示指向Data_Asset对象的指针。 需要申请数据内存。 此函数仅填充数据，否则执行失败。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Values_GetAssetsCount()**

```ets
int OH_Values_GetAssetsCount(OH_Data_Values *values, int index, size_t *length)
```

描述

获取ASSETS类型数据的大小。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| size_t *length | 该参数为输出参数，表示ASSETS类型数据的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Values_GetAssets()**

```ets
int OH_Values_GetAssets(OH_Data_Values *values, int index, Data_Asset **val, size_t inLen, size_t *outLen)
```

描述

获取ASSETS类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| Data_Asset **val | 表示指向Data_Asset对象的指针。 使用时需要申请数据内存。 此函数仅填充数据，否则执行失败。 |
| size_t inLen | 表示val的大小。可以通过OH_Values_GetAssetsCount获取。 |
| size_t *outLen | 一个输出参数，表示实际获取的数据大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Values_GetFloatVectorCount()**

```ets
int OH_Values_GetFloatVectorCount(OH_Data_Values *values, int index, size_t *length)
```

描述

获取float数组类型数据的大小。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| size_t *length | 该参数为输出参数，表示float数组类型数据的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Values_GetFloatVector()**

```ets
int OH_Values_GetFloatVector(OH_Data_Values *values, int index, float *val, size_t inLen, size_t *outLen)
```

描述

获取float数组类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| float *val | 表示指向float数组的指针。 需要申请数据内存。 此函数仅填充数据，否则执行失败。 |
| size_t inLen | 表示val的大小。可以通过OH_Values_GetFloatVectorCount获取。 |
| size_t *outLen | 一个输出参数，表示实际获取的数据大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Values_GetUnlimitedIntBand()**

```ets
int OH_Values_GetUnlimitedIntBand(OH_Data_Values *values, int index, size_t *length)
```

描述

获取任意长度的整型数据的大小。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| size_t *length | 该参数为输出参数，表示整型数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Values_GetUnlimitedInt()**

```ets
int OH_Values_GetUnlimitedInt(OH_Data_Values *values, int index, int *sign, uint64_t *trueForm, size_t inLen, size_t *outLen)
```

描述

获取任意长度的整型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Values *values | 表示指向OH_Data_Values实例的指针。 |
| int index | 表示values中目标数据的从零开始的索引。 |
| int *sign | 一个输出参数，表示正负数，0表示正整数，1表示负整数。 |
| uint64_t *trueForm | 表示指向整型数组的指针。 需要申请数据内存。 此函数仅填充数据，否则执行失败。 |
| size_t inLen | 表示trueForm的大小。可以通过OH_Values_GetUnlimitedIntBand获取。 |
| size_t *outLen | 一个输出参数，表示实际获取的数据大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |