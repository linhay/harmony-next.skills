# OH_Cursor

```ets
typedef struct {...} OH_Cursor
```

**概述**

表示结果集。提供通过查询数据库生成的数据库结果集的访问方法。

起始版本： 10

相关模块： [RDB](RDB.md)

所在头文件： [oh_cursor.h](oh_cursor.h.md)

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int64_t id | OH_Cursor结构体的唯一标识符。 |

**成员函数**

| 名称 | 描述 |
| --- | --- |
| int (*getColumnCount)(OH_Cursor *cursor, int *count) | 函数指针，获取结果集中的列数。 |
| int (*getColumnType)(OH_Cursor *cursor, int32_t columnIndex, OH_ColumnType *columnType) | 函数指针，根据指定的列索引获取列类型。 |
| int (*getColumnIndex)(OH_Cursor *cursor, const char *name, int *columnIndex) | 函数指针，根据指定的列名获取列索引。 |
| int (*getColumnName)(OH_Cursor *cursor, int32_t columnIndex, char *name, int length) | 函数指针，根据指定的列索引获取列名。 |
| int (*getRowCount)(OH_Cursor *cursor, int *count) | 函数指针，获取结果集中的行数。 |
| int (*goToNextRow)(OH_Cursor *cursor) | 函数指针，转到结果集的下一行。 |
| int (*getSize)(OH_Cursor *cursor, int32_t columnIndex, size_t *size) | 函数指针，当结果集中列的数据类型是BLOB或者TEXT时，获取其值所需的内存。 |
| int (*getText)(OH_Cursor *cursor, int32_t columnIndex, char *value, int length) | 函数指针，以字符串形式获取当前行中指定列的值。 |
| int (*getInt64)(OH_Cursor *cursor, int32_t columnIndex, int64_t *value) | 函数指针，以int64_t形式获取当前行中指定列的值。 |
| int (*getReal)(OH_Cursor *cursor, int32_t columnIndex, double *value) | 函数指针，以double形式获取当前行中指定列的值。 |
| int (*getBlob)(OH_Cursor *cursor, int32_t columnIndex, unsigned char *value, int length) | 函数指针，以字节数组的形式获取当前行中指定列的值。 |
| int (*isNull)(OH_Cursor *cursor, int32_t columnIndex, bool *isNull) | 函数指针，检查当前行中指定列的值是否为null。 |
| int (*destroy)(OH_Cursor *cursor) | 函数指针，关闭结果集。 |
| int (*getAsset)(OH_Cursor *cursor, int32_t columnIndex, Data_Asset *value) | 函数指针，以资产的形式获取当前行中指定列的值。 |
| int (*getAssets)(OH_Cursor *cursor, int32_t columnIndex, Data_Asset **value, uint32_t *length) | 函数指针，以资产数组的形式获取当前行中指定列的值。 |

**成员函数说明**

**getColumnCount()**

```ets
int (*getColumnCount)(OH_Cursor *cursor, int *count)
```

描述

函数指针，获取结果集中的列数。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int *count | 该参数是输出参数，结果集中的列数会写入该变量 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getColumnType()**

```ets
int (*getColumnType)(OH_Cursor *cursor, int32_t columnIndex, OH_ColumnType *columnType)
```

描述

函数指针，根据指定的列索引获取列类型。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| OH_ColumnType *columnType | 该参数是输出参数，结果集中指定列的数据类型OH_ColumnType会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getColumnIndex()**

```ets
int (*getColumnIndex)(OH_Cursor *cursor, const char *name, int *columnIndex)
```

描述

函数指针，根据指定的列名获取列索引。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| const char *name | 表示结果集中指定列的名称。 |
| int *columnIndex | 该参数是输出参数，结果集中指定列的索引会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getColumnName()**

```ets
 int (*getColumnName)(OH_Cursor *cursor, int32_t columnIndex, char *name, int length)
```

描述

函数指针，根据指定的列索引获取列名。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| char *name | 该参数是输出参数，结果集中指定列的名称会写入该变量。 |
| int length | 该参数为输入参数，表示开发者传入的包括终止符在内的列名字符串的总长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getRowCount()**

```ets
int (*getRowCount)(OH_Cursor *cursor, int *count)
```

描述

函数指针，获取结果集中的行数。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int *count | 该参数是输出参数，结果集中的列数会写入该变量 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**goToNextRow()**

```ets
 int (*goToNextRow)(OH_Cursor *cursor)
```

描述

函数指针，转到结果集的下一行。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getSize()**

```ets
int (*getSize)(OH_Cursor *cursor, int32_t columnIndex, size_t *size)
```

描述

函数指针，当结果集中列的数据类型是BLOB或者TEXT时，获取其值所需的内存。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针。 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| size_t *size | 该参数是输出参数，BLOB或者TEXT数据所需内存大小会写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getText()**

```ets
int (*getText)(OH_Cursor *cursor, int32_t columnIndex, char *value, int length)
```

描述

函数指针，以字符串形式获取当前行中指定列的值。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int32_t columnIndex | 该表示结果集中指定列的索引，索引值从0开始。 |
| char *value | 该参数是输出参数，结果集中指定列的值会以字符串形式写入该变量。 |
| int length | 该参数是输入参数，表示value的长度，该值可通过getSize获取。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getInt64()**

```ets
int (*getInt64)(OH_Cursor *cursor, int32_t columnIndex, int64_t *value)
```

描述

函数指针，以int64_t形式获取当前行中指定列的值。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| int64_t *value | 该参数是输出参数，结果集中指定列的值会以int64_t形式写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getReal()**

```ets
int (*getReal)(OH_Cursor *cursor, int32_t columnIndex, double *value)
```

描述

函数指针，以double形式获取当前行中指定列的值。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| double *value | 该参数是输出参数，结果集中指定列的值会以double形式写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getBlob()**

```ets
int (*getBlob)(OH_Cursor *cursor, int32_t columnIndex, unsigned char *value, int length)
```

描述

函数指针，以字节数组的形式获取当前行中指定列的值。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| unsigned char *value | 该参数是输出参数，结果集中指定列的值会以字节数组形式写入该变量。 |
| int length | 该参数为输入参数，表示传入的value的长度，该值可通过getSize获取。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**isNull()**

```ets
int (*isNull)(OH_Cursor *cursor, int32_t columnIndex, bool *isNull)
```

描述

函数指针，检查当前行中指定列的值是否为null。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| bool *isNull | 该参数是输出参数，如果当前行中指定列的值为null，该值为true，否则为false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**destroy()**

```ets
int (*destroy)(OH_Cursor *cursor)
```

描述

函数指针，关闭结果集。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getAsset()**

```ets
int (*getAsset)(OH_Cursor *cursor, int32_t columnIndex, Data_Asset *value)
```

描述

函数指针，以资产的形式获取当前行中指定列的值。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| Data_Asset *value | 该参数是输出参数，结果集中指定列的值会以资产形式写入该变量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

**getAssets()**

```ets
int (*getAssets)(OH_Cursor *cursor, int32_t columnIndex, Data_Asset **value, uint32_t *length)
```

描述

函数指针，以资产数组的形式获取当前行中指定列的值。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Cursor *cursor | 表示指向OH_Cursor实例的指针 |
| int32_t columnIndex | 表示结果集中指定列的索引，索引值从0开始。 |
| Data_Asset **value | 该参数是输出参数，结果集中指定列的值会以资产数组形式写入该变量。 |
| uint32_t *length | 既是入参又是出参：作为入参，需要开发者传入一个uint32_t类型的变量，表示输入缓冲区的大小；作为出参，表示函数执行后，length指向的变量会被更新为实际返回的资产数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |