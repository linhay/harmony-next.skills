# OH_VBucket

```ets
typedef struct {...} OH_VBucket
```

#### 概述

用于存储键值对的类型。

**起始版本：** 10

**相关模块：**[RDB](RDB.md)

所在头文件： [oh_values_bucket.h](oh_values_bucket.h.md)

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| int64_t id | OH_VBucket结构体的唯一标识符。 |
| uint16_t capability | 表示结构体的存储键值对的数量。 |

#### 成员函数

| 名称 | 描述 |
| --- | --- |
| int (*putText)(OH_VBucket *bucket, const char *field, const char *value) | 将char*值放入给定列名的OH_VBucket对象中。 |
| int (*putInt64)(OH_VBucket *bucket, const char *field, int64_t value) | 将int64_t值放入给定列名的OH_VBucket对象中。 |
| int (*putReal)(OH_VBucket *bucket, const char *field, double value) | 将double值放入给定列名的OH_VBucket对象中。 |
| int (*putBlob)(OH_VBucket *bucket, const char *field, const uint8_t *value, uint32_t size) | 将const uint8_t *值放入给定列名的OH_VBucket对象中。 |
| int (*putNull)(OH_VBucket *bucket, const char *field) | 将NULL值放入给定列名的OH_VBucket对象中。 |
| int (*clear)(OH_VBucket *bucket) | 清空OH_VBucket对象。 |
| int (*destroy)(OH_VBucket *bucket) | 销毁OH_VBucket对象，并回收该对象占用的内存。 |

#### 成员函数说明

#### putText()

```ets
int (*putText)(OH_VBucket *bucket, const char *field, const char *value)
```

**描述**

将char*值放入给定列名的OH_VBucket对象中。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |
| const char *field | 数据库表中的列名 |
| const char *value | 数据库表中指定列名对应的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

#### putInt64()

```ets
int (*putInt64)(OH_VBucket *bucket, const char *field, int64_t value)
```

**描述**

将int64_t值放入给定列名的OH_VBucket对象中。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |
| const char *field | 数据库表中的列名 |
| int64_t value | 数据库表中指定列名对应的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

#### putReal()

```ets
int (*putReal)(OH_VBucket *bucket, const char *field, double value)
```

**描述**

将double值放入给定列名的OH_VBucket对象中。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |
| const char *field | 数据库表中的列名 |
| double value | 数据库表中指定列名对应的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

#### putBlob()

```ets
int (*putBlob)(OH_VBucket *bucket, const char *field, const uint8_t *value, uint32_t size)
```

**描述**

将const uint8_t *值放入给定列名的OH_VBucket对象中。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |
| const char *field | 数据库表中的列名 |
| const uint8_t *value | 数据库表中指定列名对应的值。 |
| uint32_t size | 表示value的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

#### putNull()

```ets
int (*putNull)(OH_VBucket *bucket, const char *field)
```

**描述**

将NULL值放入给定列名的OH_VBucket对象中。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |
| const char *field | 数据库表中的列名 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

#### clear()

```ets
int (*clear)(OH_VBucket *bucket)
```

**描述**

清空[OH_VBucket](OH_VBucket.md)对象。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |

#### destroy()

```ets
int (*destroy)(OH_VBucket *bucket)
```

**描述**

销毁[OH_VBucket](OH_VBucket.md)对象，并回收该对象占用的内存。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH_VBucket *bucket | 表示指向OH_VBucket实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回操作是否成功，出错时返回对应的错误码。 |