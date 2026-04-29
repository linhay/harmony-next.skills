# oh_preferences_value.h

**概述**

提供访问Preferences值（PreferencesValue）对象的接口、枚举类型与数据结构。

引用文件： <database/preferences/oh_preferences_value.h>

库： libohpreferences.so

系统能力： SystemCapability.DistributedDataManager.Preferences.Core

起始版本： 13

相关模块： [Preferences](Preferences.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_PreferencesPair | OH_PreferencesPair | 定义Preferences使用的KV数据对象类型。 |
| OH_PreferencesValue | OH_PreferencesValue | 定义PreferencesValue对象类型。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Preference_ValueType | Preference_ValueType | 定义PreferencesValue的数据类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| const char *OH_PreferencesPair_GetKey(const OH_PreferencesPair *pairs, uint32_t index) | 获取KV数据中索引对应数据的键。 |
| const OH_PreferencesValue *OH_PreferencesPair_GetPreferencesValue(const OH_PreferencesPair *pairs, uint32_t index) | 获取KV数据数组中索引对应的值。 |
| Preference_ValueType OH_PreferencesValue_GetValueType(const OH_PreferencesValue *object) | 获取PreferencesValue对象的数据类型。 |
| int OH_PreferencesValue_GetInt(const OH_PreferencesValue *object, int *value) | 从PreferencesValue对象OH_PreferencesValue中获取一个整型值。 |
| int OH_PreferencesValue_GetBool(const OH_PreferencesValue *object, bool *value) | 从PreferencesValue对象OH_PreferencesValue中获取一个布尔值。 |
| int OH_PreferencesValue_GetString(const OH_PreferencesValue *object, char **value, uint32_t *valueLen) | 从PreferencesValue对象OH_PreferencesValue中获取字符串。 |
| void OH_PreferencesPair_Destroy(OH_PreferencesPair *pairs, uint32_t count) | 销毁一个OH_PreferencesPair实例。 |
| OH_PreferencesValue* OH_PreferencesValue_Create(void) | 创建一个OH_PreferencesValue实例。 |
| void OH_PreferencesValue_Destroy(OH_PreferencesValue *value) | 销毁一个OH_PreferencesValue实例。 |
| int OH_PreferencesValue_SetInt(const OH_PreferencesValue *object, int value) | 为OH_PreferencesValue实例设置整型值。 |
| int OH_PreferencesValue_SetBool(const OH_PreferencesValue *object, bool value) | 为OH_PreferencesValue实例设置布尔值。 |
| int OH_PreferencesValue_SetString(const OH_PreferencesValue *object, const char *value) | 为OH_PreferencesValue实例设置字符串值。 |
| int OH_PreferencesValue_SetInt64(const OH_PreferencesValue *object, int64_t value) | 为OH_PreferencesValue实例设置int64值。 |
| int OH_PreferencesValue_GetInt64(const OH_PreferencesValue *object, int64_t *value) | 获取OH_PreferencesValue实例的int64值。 |
| int OH_PreferencesValue_SetDouble(const OH_PreferencesValue *object, double value) | 为OH_PreferencesValue实例设置double值。 |
| int OH_PreferencesValue_GetDouble(const OH_PreferencesValue *object, double *value) | 获取OH_PreferencesValue实例的double值。 |
| int OH_PreferencesValue_SetIntArray(const OH_PreferencesValue *object, const int *value, uint32_t count) | 为OH_PreferencesValue实例设置整型数组值。 |
| int OH_PreferencesValue_GetIntArray(const OH_PreferencesValue *object, int **value, uint32_t *count) | 获取OH_PreferencesValue实例的整型数组值。 |
| int OH_PreferencesValue_SetBoolArray(const OH_PreferencesValue *object, const bool *value, uint32_t count) | 为OH_PreferencesValue实例设置布尔数组值。 |
| int OH_PreferencesValue_GetBoolArray(const OH_PreferencesValue *object, bool **value, uint32_t *count) | 获取OH_PreferencesValue实例的布尔数组值。 |
| int OH_PreferencesValue_SetStringArray(const OH_PreferencesValue *object, const char **value, uint32_t count) | 为OH_PreferencesValue实例设置字符串数组值。 |
| int OH_PreferencesValue_GetStringArray(const OH_PreferencesValue *object, char ***value, uint32_t *count) | 获取OH_PreferencesValue实例的字符串数组值。 |
| int OH_PreferencesValue_SetInt64Array(const OH_PreferencesValue *object, const int64_t *value, uint32_t count) | 为OH_PreferencesValue实例设置int64数组值。 |
| int OH_PreferencesValue_GetInt64Array(const OH_PreferencesValue *object, int64_t **value, uint32_t *count) | 获取OH_PreferencesValue实例的int64数组值。 |
| int OH_PreferencesValue_SetDoubleArray(const OH_PreferencesValue *object, const double *value, uint32_t count) | 为OH_PreferencesValue实例设置double数组值。 |
| int OH_PreferencesValue_GetDoubleArray(const OH_PreferencesValue *object, double **value, uint32_t *count) | 获取OH_PreferencesValue实例的double数组值。 |
| int OH_PreferencesValue_SetBlob(const OH_PreferencesValue *object, const uint8_t *value, uint32_t count) | 为OH_PreferencesValue实例设置二进制值。 |
| int OH_PreferencesValue_GetBlob(const OH_PreferencesValue *object, uint8_t **value, uint32_t *count) | 获取OH_PreferencesValue实例的二进制值。 |

**枚举类型说明**

**Preference_ValueType**

```ets
enum Preference_ValueType
```

描述

定义PreferencesValue的数据类型。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| PREFERENCE_TYPE_NULL = 0 | 空类型。 |
| PREFERENCE_TYPE_INT | 整型类型。 |
| PREFERENCE_TYPE_BOOL | 布尔类型。 |
| PREFERENCE_TYPE_STRING | 字符串类型。 |
| PREFERENCE_TYPE_INT64 | 64位整型类型。 起始版本： 23 |
| PREFERENCE_TYPE_DOUBLE | 浮点型类型。 起始版本： 23 |
| PREFERENCE_TYPE_INT_ARRAY | 整型数组。 起始版本： 23 |
| PREFERENCE_TYPE_BOOL_ARRAY | 布尔数组。 起始版本： 23 |
| PREFERENCE_TYPE_STRING_ARRAY | 字符串数组。 起始版本： 23 |
| PREFERENCE_TYPE_INT64_ARRAY | 64位整型数组。 起始版本： 23 |
| PREFERENCE_TYPE_DOUBLE_ARRAY | 浮点型数组。 起始版本： 23 |
| PREFERENCE_TYPE_BLOB | 二进制数据。 起始版本： 23 |
| PREFERENCE_TYPE_BUTT | 结束类型。 |

**函数说明**

**OH_PreferencesPair_GetKey()**

```ets
const char *OH_PreferencesPair_GetKey(const OH_PreferencesPair *pairs, uint32_t index)
```

描述

获取KV数据中索引对应数据的键。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesPair *pairs | 目标KV数据OH_PreferencesPair的指针。 |
| uint32_t index | 目标KV数据OH_PreferencesPair的索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const char * | 如果操作成功，返回获取到的键的指针。操作失败或传参不合法返回空指针。 |

**OH_PreferencesPair_GetPreferencesValue()**

```ets
const OH_PreferencesValue *OH_PreferencesPair_GetPreferencesValue(const OH_PreferencesPair *pairs, uint32_t index)
```

描述

获取KV数据数组中索引对应的值。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesPair *pairs | 目标KV数据OH_PreferencesPair的指针。 |
| uint32_t index | 目标KV数据OH_PreferencesPair的索引值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| const OH_PreferencesValue | 如果操作成功，返回获取到的值对象的指针。操作失败或传参不合法返回空指针。 |

**OH_PreferencesValue_GetValueType()**

```ets
Preference_ValueType OH_PreferencesValue_GetValueType(const OH_PreferencesValue *object)
```

描述

获取PreferencesValue对象的数据类型。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 对象OH_PreferencesValue的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Preference_ValueType | 返回获取到的数据类型枚举。若返回数据类型枚举为PREFERENCE_TYPE_NULL，代表传参不合法。 |

**OH_PreferencesValue_GetInt()**

```ets
int OH_PreferencesValue_GetInt(const OH_PreferencesValue *object, int *value)
```

描述

从PreferencesValue对象[OH_PreferencesValue](OH_PreferencesValue.md)中获取一个整型值。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 对象OH_PreferencesValue的指针。 |
| int *value | 该参数作为出参使用，表示指向获取到的整型值的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 |

**OH_PreferencesValue_GetBool()**

```ets
int OH_PreferencesValue_GetBool(const OH_PreferencesValue *object, bool *value)
```

描述

从PreferencesValue对象[OH_PreferencesValue](OH_PreferencesValue.md)中获取一个布尔值。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 对象OH_PreferencesValue的指针。 |
| bool *value | 该参数作为出参使用，表示指向获取到的布尔值的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 |

**OH_PreferencesValue_GetString()**

```ets
int OH_PreferencesValue_GetString(const OH_PreferencesValue *object, char **value, uint32_t *valueLen)
```

描述

从PreferencesValue对象[OH_PreferencesValue](OH_PreferencesValue.md)中获取字符串。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 对象OH_PreferencesValue的指针。 |
| char **value | 该参数作为出参使用，表示指向获取到的字符串的二级指针，使用完毕后需要调用释放函数OH_Preferences_FreeString释放内存。 |
| uint32_t *valueLen | 该参数作为出参使用，表示指向获取到的字符串长度的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 |

**OH_PreferencesPair_Destroy()**

```ets
void OH_PreferencesPair_Destroy(OH_PreferencesPair *pairs, uint32_t count)
```

描述

销毁一个[OH_PreferencesPair](OH_PreferencesPair.md)实例。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PreferencesPair *pairs | 指向目标OH_PreferencesPair实例的指针。 |
| uint32_t count | 需要销毁的KV数组大小。 |

**OH_PreferencesValue_Create()**

```ets
OH_PreferencesValue* OH_PreferencesValue_Create(void)
```

描述

创建一个[OH_PreferencesValue](OH_PreferencesValue.md)实例。

起始版本： 23

返回：

| 类型 | 说明 |
| --- | --- |
| OH_PreferencesValue* | 如果操作成功，返回指向OH_PreferencesValue值对象的指针，否则返回nullptr。 |

**OH_PreferencesValue_Destroy()**

```ets
void OH_PreferencesValue_Destroy(OH_PreferencesValue *value)
```

描述

销毁一个[OH_PreferencesValue](OH_PreferencesValue.md)实例。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PreferencesValue *value | 指向目标OH_PreferencesValue实例的指针。 |

**OH_PreferencesValue_SetInt()**

```ets
int OH_PreferencesValue_SetInt(const OH_PreferencesValue *object, int value)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置整型值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| int value | 需要设置的整型值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_SetBool()**

```ets
int OH_PreferencesValue_SetBool(const OH_PreferencesValue *object, bool value)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置布尔值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| bool value | 需要设置的布尔值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_SetString()**

```ets
int OH_PreferencesValue_SetString(const OH_PreferencesValue *object, const char *value)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置字符串值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| const char *value | 需要设置的字符串值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_SetInt64()**

```ets
int OH_PreferencesValue_SetInt64(const OH_PreferencesValue *object, int64_t value)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置int64值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| int64_t value | 需要设置的int64值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_GetInt64()**

```ets
int OH_PreferencesValue_GetInt64(const OH_PreferencesValue *object, int64_t *value)
```

描述

获取[OH_PreferencesValue](OH_PreferencesValue.md)实例的int64值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| int64_t *value | 指向获取到的int64值的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_SetDouble()**

```ets
int OH_PreferencesValue_SetDouble(const OH_PreferencesValue *object, double value)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置double值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| double value | 需要设置的double值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_GetDouble()**

```ets
int OH_PreferencesValue_GetDouble(const OH_PreferencesValue *object, double *value)
```

描述

获取[OH_PreferencesValue](OH_PreferencesValue.md)实例的double值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| double *value | 指向获取到的double值的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_SetIntArray()**

```ets
int OH_PreferencesValue_SetIntArray(const OH_PreferencesValue *object, const int *value, uint32_t count)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置整型数组值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| const int *value | 需要设置的整型数组值。 |
| uint32_t count | 指向需要设置的数组大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_GetIntArray()**

```ets
int OH_PreferencesValue_GetIntArray(const OH_PreferencesValue *object, int **value, uint32_t *count)
```

描述

获取[OH_PreferencesValue](OH_PreferencesValue.md)实例的整型数组值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| int **value | 指向获取到的整型数组值的二级指针。 |
| uint32_t *count | 指向获取到的数组大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_SetBoolArray()**

```ets
int OH_PreferencesValue_SetBoolArray(const OH_PreferencesValue *object, const bool *value, uint32_t count)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置布尔数组值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| const bool *value | 需要设置的布尔数组值。 |
| uint32_t count | 指向需要设置的数组大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_GetBoolArray()**

```ets
int OH_PreferencesValue_GetBoolArray(const OH_PreferencesValue *object, bool **value, uint32_t *count)
```

描述

获取[OH_PreferencesValue](OH_PreferencesValue.md)实例的布尔数组值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| bool **value | 指向获取到的布尔数组值的二级指针。 |
| uint32_t *count | 指向获取到的数组大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_SetStringArray()**

```ets
int OH_PreferencesValue_SetStringArray(const OH_PreferencesValue *object, const char **value, uint32_t count)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置字符串数组值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| const char **value | 需要设置的字符串数组值。 |
| uint32_t count | 指向需要设置的数组大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_GetStringArray()**

```ets
int OH_PreferencesValue_GetStringArray(const OH_PreferencesValue *object, char ***value, uint32_t *count)
```

描述

获取[OH_PreferencesValue](OH_PreferencesValue.md)实例的字符串数组值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| char ***value | 指向获取到的字符串数组值的二级指针。 |
| uint32_t *count | 指向获取到的数组大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_SetInt64Array()**

```ets
int OH_PreferencesValue_SetInt64Array(const OH_PreferencesValue *object, const int64_t *value, uint32_t count)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置int64数组值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| const int64_t *value | 需要设置的int64数组值。 |
| uint32_t count | 指向需要设置的数组大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_GetInt64Array()**

```ets
int OH_PreferencesValue_GetInt64Array(const OH_PreferencesValue *object, int64_t **value, uint32_t *count)
```

描述

获取[OH_PreferencesValue](OH_PreferencesValue.md)实例的int64数组值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| int64_t **value | 指向获取到的int64数组值的二级指针。 |
| uint32_t *count | 指向获取到的数组大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_SetDoubleArray()**

```ets
int OH_PreferencesValue_SetDoubleArray(const OH_PreferencesValue *object, const double *value, uint32_t count)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置double数组值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| const double *value | 需要设置的double数组值。 |
| uint32_t count | 指向需要设置的数组大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_GetDoubleArray()**

```ets
int OH_PreferencesValue_GetDoubleArray(const OH_PreferencesValue *object, double **value, uint32_t *count)
```

描述

获取[OH_PreferencesValue](OH_PreferencesValue.md)实例的double数组值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| double **value | 指向获取到的double数组值的二级指针。 |
| uint32_t *count | 指向获取到的数组大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_SetBlob()**

```ets
int OH_PreferencesValue_SetBlob(const OH_PreferencesValue *object, const uint8_t *value, uint32_t count)
```

描述

为[OH_PreferencesValue](OH_PreferencesValue.md)实例设置二进制值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| const uint8_t *value | 需要设置的二进制值。 |
| uint32_t count | 指向需要设置的二进制大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_PreferencesValue_GetBlob()**

```ets
int OH_PreferencesValue_GetBlob(const OH_PreferencesValue *object, uint8_t **value, uint32_t *count)
```

描述

获取[OH_PreferencesValue](OH_PreferencesValue.md)实例的二进制值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_PreferencesValue *object | 指向目标OH_PreferencesValue实例的指针。 |
| uint8_t **value | 指向获取到的二进制值的二级指针。 |
| uint32_t *count | 指向获取到的二进制大小的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |