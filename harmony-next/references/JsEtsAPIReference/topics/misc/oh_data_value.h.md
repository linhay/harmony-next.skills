# oh_data_value.h

**概述**

提供与单条数据值相关的函数和枚举。

从API version 18开始，OH_ColumnType从oh_cursor.h移动至此头文件呈现，对于此类型，API version 18之前即支持使用，各版本均可正常使用。

引用文件： <database/data/oh_data_value.h>

库： libnative_rdb_ndk.z.so

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

起始版本： 18

相关模块： [RDB](RDB.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Data_Value | OH_Data_Value | 定义OH_Data_Value结构类型。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_ColumnType | OH_ColumnType | 表示列的类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Data_Value *OH_Value_Create(void) | 创建OH_Data_Value实例，用于储存单条键值对数据。 |
| int OH_Value_Destroy(OH_Data_Value *value) | 销毁OH_Data_Value对象。 |
| int OH_Value_PutNull(OH_Data_Value *value) | 添加空数据。 |
| int OH_Value_PutInt(OH_Data_Value *value, int64_t val) | 添加整型数据。 |
| int OH_Value_PutReal(OH_Data_Value *value, double val) | 添加REAL类型数据。 |
| int OH_Value_PutText(OH_Data_Value *value, const char *val) | 添加字符串类型数据。 |
| int OH_Value_PutBlob(OH_Data_Value *value, const unsigned char *val, size_t length) | 添加BLOB类型数据。 |
| int OH_Value_PutAsset(OH_Data_Value *value, const Data_Asset *val) | 添加ASSET类型数据。 |
| int OH_Value_PutAssets(OH_Data_Value *value, const Data_Asset * const * val, size_t length) | 添加ASSETS类型数据。 |
| int OH_Value_PutFloatVector(OH_Data_Value *value, const float *val, size_t length) | 添加float数组类型数据。 |
| int OH_Value_PutUnlimitedInt(OH_Data_Value *value, int sign, const uint64_t *trueForm, size_t length) | 添加任意长度的整型数组数据。 |
| int OH_Value_GetType(OH_Data_Value *value, OH_ColumnType *type) | 获取数据类型。 |
| int OH_Value_IsNull(OH_Data_Value *value, bool *val) | 检查数据是否为空。 |
| int OH_Value_GetInt(OH_Data_Value *value, int64_t *val) | 获取整型数据。 |
| int OH_Value_GetReal(OH_Data_Value *value, double *val) | 获取REAL类型数据。 |
| int OH_Value_GetText(OH_Data_Value *value, const char **val) | 获取字符串类型数据。 |
| int OH_Value_GetBlob(OH_Data_Value *value, const uint8_t **val, size_t *length) | 获取BLOB类型数据。 |
| int OH_Value_GetAsset(OH_Data_Value *value, Data_Asset *val) | 获取ASSET类型数据。 |
| int OH_Value_GetAssetsCount(OH_Data_Value *value, size_t *length) | 获取ASSETS类型数据的大小。 |
| int OH_Value_GetAssets(OH_Data_Value *value, Data_Asset **val, size_t inLen, size_t *outLen) | 获取ASSETS类型数据。 |
| int OH_Value_GetFloatVectorCount(OH_Data_Value *value, size_t *length) | 获取float数组类型数据的大小。 |
| int OH_Value_GetFloatVector(OH_Data_Value *value, float *val, size_t inLen, size_t *outLen) | 获取float数组类型数据。 |
| int OH_Value_GetUnlimitedIntBand(OH_Data_Value *value, size_t *length) | 获取任意长度的整型数据的大小。 |
| int OH_Value_GetUnlimitedInt(OH_Data_Value *value, int *sign, uint64_t *trueForm, size_t inLen, size_t *outLen) | 获取任意长度的整型数据。 |

**枚举类型说明**

**OH_ColumnType**

```ets
enum OH_ColumnType
```

描述

表示列的类型。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| TYPE_NULL = 0 | 表示NULL类型。 |
| TYPE_INT64 | 表示INT64数据类型。 |
| TYPE_REAL | 表示REAL数据类型。 |
| TYPE_TEXT | 表示TEXT数据类型。 |
| TYPE_BLOB | 表示BLOB数据类型。 |
| TYPE_ASSET | 表示ASSET（资产附件）数据类型。 起始版本： 11 |
| TYPE_ASSETS | 表示ASSETS（多个资产附件）数据类型。 起始版本： 11 |
| TYPE_FLOAT_VECTOR | 表示FLOAT VECTOR数据类型。 起始版本： 18 |
| TYPE_UNLIMITED_INT | 表示列类型为长度大于64位的数字。 起始版本： 18 |

**函数说明**

**OH_Value_Create()**

```ets
OH_Data_Value *OH_Value_Create(void)
```

描述

创建[OH_Data_Value](OH_Data_Value.md)实例，用于储存单条键值对数据。

起始版本： 18

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Data_Value | 执行成功时返回指向OH_Data_Value实例的指针。否则返回nullptr。 使用完成后，必须通过OH_Value_Destroy接口释放内存。 |

**OH_Value_Destroy()**

```ets
int OH_Value_Destroy(OH_Data_Value *value)
```

描述

销毁[OH_Data_Value](OH_Data_Value.md)对象。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_PutNull()**

```ets
int OH_Value_PutNull(OH_Data_Value *value)
```

描述

添加空数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_PutInt()**

```ets
int OH_Value_PutInt(OH_Data_Value *value, int64_t val)
```

描述

添加整型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| int64_t val | 表示整型数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_PutReal()**

```ets
int OH_Value_PutReal(OH_Data_Value *value, double val)
```

描述

添加REAL类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| double val | 表示REAL类型数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_PutText()**

```ets
int OH_Value_PutText(OH_Data_Value *value, const char *val)
```

描述

添加字符串类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| const char *val | 表示字符串类型数据。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_PutBlob()**

```ets
int OH_Value_PutBlob(OH_Data_Value *value, const unsigned char *val, size_t length)
```

描述

添加BLOB类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| const unsigned char *val | 表示BLOB类型数据。 |
| size_t length | 该参数是输入参数，表示开发者传入的BLOB类型数据的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_PutAsset()**

```ets
int OH_Value_PutAsset(OH_Data_Value *value, const Data_Asset *val)
```

描述

添加ASSET类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| const Data_Asset *val | 表示指向Data_Asset对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_PutAssets()**

```ets
int OH_Value_PutAssets(OH_Data_Value *value, const Data_Asset * const * val, size_t length)
```

描述

添加ASSETS类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| const Data_Asset * const * val | 表示指向Data_Asset对象的指针。 |
| size_t length | 该参数是输入参数，表示开发者传入的Data_Asset对象数组元素的个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_PutFloatVector()**

```ets
int OH_Value_PutFloatVector(OH_Data_Value *value, const float *val, size_t length)
```

描述

添加float数组类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| const float *val | 表示指向float数组对象的指针。 |
| size_t length | 该参数是输入参数，表示开发者传入的表示float数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_PutUnlimitedInt()**

```ets
int OH_Value_PutUnlimitedInt(OH_Data_Value *value, int sign, const uint64_t *trueForm, size_t length)
```

描述

添加任意长度的整型数组数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| int sign | 表示正负数，0表示正整数，1表示负整数。 |
| const uint64_t *trueForm | 表示指向整型数组的指针。 |
| size_t length | 该参数是输入参数，表示开发者传入的表示整型数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_GetType()**

```ets
int OH_Value_GetType(OH_Data_Value *value, OH_ColumnType *type)
```

描述

获取数据类型。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| OH_ColumnType *type | 一个输出参数，表示数据类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_IsNull()**

```ets
int OH_Value_IsNull(OH_Data_Value *value, bool *val)
```

描述

检查数据是否为空。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| bool *val | 一个输出参数，true表示空，false表示不为空。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 |

**OH_Value_GetInt()**

```ets
int OH_Value_GetInt(OH_Data_Value *value, int64_t *val)
```

描述

获取整型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| int64_t *val | 一个输出参数，表示指向整型数据的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Value_GetReal()**

```ets
int OH_Value_GetReal(OH_Data_Value *value, double *val)
```

描述

获取REAL类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| double *val | 一个输出参数，表示指向REAL类型数据的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Value_GetText()**

```ets
int OH_Value_GetText(OH_Data_Value *value, const char **val)
```

描述

获取字符串类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| const char **val | 一个输出参数，表示指向字符串类型数据的指针。 无需申请内存和释放内存。 val的生命周期遵循value中index的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Value_GetBlob()**

```ets
int OH_Value_GetBlob(OH_Data_Value *value, const uint8_t **val, size_t *length)
```

描述

获取BLOB类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| const uint8_t **val | 一个输出参数，表示指向BLOB类型数据的指针。 无需申请内存和释放内存。 val的生命周期遵循value中index的值。 |
| size_t *length | 该参数是输出参数，表示BLOB类型数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Value_GetAsset()**

```ets
int OH_Value_GetAsset(OH_Data_Value *value, Data_Asset *val)
```

描述

获取ASSET类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| Data_Asset *val | 表示指向Data_Asset对象的指针。 需要申请数据内存。 此函数仅填充数据。否则执行失败。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Value_GetAssetsCount()**

```ets
int OH_Value_GetAssetsCount(OH_Data_Value *value, size_t *length)
```

描述

获取ASSETS类型数据的大小。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| size_t *length | 该参数是输出参数，表示ASSETS类型数据的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Value_GetAssets()**

```ets
int OH_Value_GetAssets(OH_Data_Value *value, Data_Asset **val, size_t inLen, size_t *outLen)
```

描述

获取ASSETS类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| Data_Asset **val | 表示指向Data_Asset对象的指针。 需要申请数据内存。 此函数仅填充数据。否则执行失败。 |
| size_t inLen | 表示val的大小。可以通过OH_Values_GetAssetsCount获取。 |
| size_t *outLen | 一个输出参数，表示实际获取的数据大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Value_GetFloatVectorCount()**

```ets
int OH_Value_GetFloatVectorCount(OH_Data_Value *value, size_t *length)
```

描述

获取float数组类型数据的大小。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| size_t *length | 该参数是输出参数，表示float数组类型数据的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示参数无效。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Value_GetFloatVector()**

```ets
int OH_Value_GetFloatVector(OH_Data_Value *value, float *val, size_t inLen, size_t *outLen)
```

描述

获取float数组类型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| float *val | 表示指向float数组的指针。 需要申请数据内存。 此函数仅填充数据。否则执行失败。 |
| size_t inLen | 表示val的大小。可以通过OH_Values_GetFloatVectorCount获取。 |
| size_t *outLen | 一个输出参数，表示实际获取的数据大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Value_GetUnlimitedIntBand()**

```ets
int OH_Value_GetUnlimitedIntBand(OH_Data_Value *value, size_t *length)
```

描述

获取任意长度的整型数据的大小。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| size_t *length | 该参数是输出参数，表示整型数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |

**OH_Value_GetUnlimitedInt()**

```ets
int OH_Value_GetUnlimitedInt(OH_Data_Value *value, int *sign, uint64_t *trueForm, size_t inLen, size_t *outLen)
```

描述

获取任意长度的整型数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Data_Value *value | 表示指向OH_Data_Value实例的指针。 |
| int *sign | 一个输出参数，表示正负数，0表示正整数，1表示负整数。 |
| uint64_t *trueForm | 表示指向整型数组的指针。 需要申请数据内存。 此函数仅填充数据。否则执行失败。 |
| size_t inLen | 表示trueForm的大小。可以通过OH_Values_GetUnlimitedIntBand获取。 |
| size_t *outLen | 一个输出参数，表示实际获取的数据大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回错误码。 返回RDB_OK表示成功。 返回RDB_E_INVALID_ARGS表示无效参数。 返回RDB_E_DATA_TYPE_NULL表示存储数据为空。 返回RDB_E_TYPE_MISMATCH表示数据类型不匹配。 |