# oh_preferences.h

**概述**

提供访问Preferences对象的接口与数据结构。

引用文件： <database/preferences/oh_preferences.h>

库： libohpreferences.so

系统能力： SystemCapability.DistributedDataManager.Preferences.Core

起始版本： 13

相关模块： [Preferences](Preferences.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Preferences | OH_Preferences | 定义Preferences对象类型。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_PreferencesDataObserver)(void *context, const OH_PreferencesPair *pairs, uint32_t count) | OH_PreferencesDataObserver | 定义数据变更触发的回调函数类型。 |
| OH_Preferences *OH_Preferences_Open(OH_PreferencesOption *option, int *errCode) | - | 打开一个Preferences实例对象并创建指向它的指针。 当不再需要使用指针时，请使用OH_Preferences_Close关闭实例对象。 |
| int OH_Preferences_Close(OH_Preferences *preference) | - | 关闭一个Preferences实例对象。 |
| int OH_Preferences_GetInt(OH_Preferences *preference, const char *key, int *value) | - | 获取Preferences实例对象中Key对应的整型值。 |
| int OH_Preferences_GetBool(OH_Preferences *preference, const char *key, bool *value) | - | 获取Preferences实例对象中Key对应的布尔值。 |
| int OH_Preferences_GetString(OH_Preferences *preference, const char *key, char **value, uint32_t *valueLen) | - | 获取Preferences实例对象中Key对应的字符串。 |
| void OH_Preferences_FreeString(char *string) | - | 释放从Preferences实例对象中获取的字符串。 |
| int OH_Preferences_SetInt(OH_Preferences *preference, const char *key, int value) | - | 根据Key设置Preferences实例对象中的整型值。 |
| int OH_Preferences_SetBool(OH_Preferences *preference, const char *key, bool value) | - | 根据Key设置Preferences实例对象中的布尔值。 |
| int OH_Preferences_SetString(OH_Preferences *preference, const char *key, const char *value) | - | 根据Key设置Preferences实例对象中的字符串。 |
| int OH_Preferences_Delete(OH_Preferences *preference, const char *key) | - | 在Preferences实例对象中删除Key对应的KV数据。 |
| int OH_Preferences_RegisterDataObserver(OH_Preferences *preference, void *context,OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount) | - | 对选取的Key注册数据变更订阅。订阅的Key的值发生变更后，在调用OH_Preferences_Close()后触发回调。 |
| int OH_Preferences_UnregisterDataObserver(OH_Preferences *preference, void *context,OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount) | - | 取消注册选取Key的数据变更订阅。 |
| int OH_Preferences_IsStorageTypeSupported(Preferences_StorageType type, bool *isSupported) | - | 校验当前平台是否支持对应存储模式。 |
| int OH_Preferences_DeletePreferences(OH_PreferencesOption *option) | - | 删除指定的Preferences对象。 |
| int OH_Preferences_SetValue(OH_Preferences *preference, const char *key, OH_PreferencesValue *value) | - | 在Preferences对象中设置值OH_PreferencesValue。 |
| int OH_Preferences_GetValue(OH_Preferences *preference, const char *key, OH_PreferencesValue **value) | - | 根据给定的Key获取Preferences对象中的值。 |
| int OH_Preferences_GetAll(OH_Preferences *preference, OH_PreferencesPair **pairs, uint32_t *count) | - | 获取Preferences对象中的所有值。 |
| bool OH_Preferences_HasKey(OH_Preferences *preference, const char *key) | - | 检查Preferences对象是否包含与指定Key匹配的KV数据，若包含则返回true，否则返回false。 |
| int OH_Preferences_Flush(OH_Preferences *preference) | - | 将OH_Preferences对象的缓存保存到xml文件中。 |
| int OH_Preferences_ClearCache(OH_Preferences *preference) | - | 清除OH_Preferences对象缓存中的所有值。 |
| int OH_Preferences_RegisterMultiProcessDataObserver(OH_Preferences *preference, void *context, OH_PreferencesDataObserver observer) | - | 为Preferences对象注册一个多进程数据观察者。 |
| int OH_Preferences_UnregisterMultiProcessDataObserver(OH_Preferences *preference, void *context, OH_PreferencesDataObserver observer) | - | 取消注册Preferences对象的多进程数据观察者。 |

**函数说明**

**OH_PreferencesDataObserver()**

```ets
typedef void (*OH_PreferencesDataObserver)(void *context, const OH_PreferencesPair *pairs, uint32_t count)
```

描述

定义数据变更触发的回调函数类型。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| void *context | 应用上下文的指针。 |
| const OH_PreferencesPair *pairs | 发生变更的KV数据的指针。 |
| uint32_t count | 发生变更的KV数据的数量。 |

**OH_Preferences_Open()**

```ets
OH_Preferences *OH_Preferences_Open(OH_PreferencesOption *option, int *errCode)
```

描述

打开一个Preferences实例对象并创建指向它的指针。

当不再需要使用指针时，请使用[OH_Preferences_Close](oh_preferences.h.md#ZH-CN_TOPIC_0000002553360571__oh_preferences_close)关闭实例对象。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PreferencesOption *option | 指向Preferences配置选项OH_PreferencesOption的指针。 |
| int *errCode | 该参数作为出参使用，表示指向返回错误码的指针，详见OH_Preferences_ErrCode。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_NOT_SUPPORTED，表示系统能力不支持。 若错误码为PREFERENCES_ERROR_DELETE_FILE，表示删除文件失败。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Preferences | 当操作成功时，返回指向打开的Preferences对象OH_Preferences实例对象的指针，失败返回空指针。 |

**OH_Preferences_Close()**

```ets
int OH_Preferences_Close(OH_Preferences *preference)
```

描述

关闭一个Preferences实例对象。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向需要关闭的PreferencesOH_Preferences实例对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码，详见OH_Preferences_ErrCode。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 |

**OH_Preferences_GetInt()**

```ets
int OH_Preferences_GetInt(OH_Preferences *preference, const char *key, int *value)
```

描述

获取Preferences实例对象中Key对应的整型值。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标PreferencesOH_Preferences实例对象的指针。 |
| const char *key | 需要获取的Key的指针。 |
| int *value | 该参数作为出参使用，表示指向获取到的整型值的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 若错误码为PREFERENCES_ERROR_KEY_NOT_FOUND，表示查询的Key不存在。 |

**OH_Preferences_GetBool()**

```ets
int OH_Preferences_GetBool(OH_Preferences *preference, const char *key, bool *value)
```

描述

获取Preferences实例对象中Key对应的布尔值。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标PreferencesOH_Preferences实例对象的指针。 |
| const char *key | 需要获取的Key的指针。 |
| bool *value | 该参数作为出参使用，表示指向获取到的布尔值的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 若错误码为PREFERENCES_ERROR_KEY_NOT_FOUND，表示查询的key不存在。 |

**OH_Preferences_GetString()**

```ets
int OH_Preferences_GetString(OH_Preferences *preference, const char *key, char **value, uint32_t *valueLen)
```

描述

获取Preferences实例对象中Key对应的字符串。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标PreferencesOH_Preferences实例对象的指针。 |
| const char *key | 需要获取的Key的指针。 |
| char **value | 该参数作为出参使用，表示指向获取到的字符串的二级指针，使用完毕后需要调用释放函数OH_Preferences_FreeString释放内存。 |
| uint32_t *valueLen | 该参数作为出参使用，表示获取到的字符串长度的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 若错误码为PREFERENCES_ERROR_KEY_NOT_FOUND，表示查询的Key不存在。 |

**OH_Preferences_FreeString()**

```ets
void OH_Preferences_FreeString(char *string)
```

描述

释放从Preferences实例对象中获取的字符串。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| char *string | 需要释放的字符串指针。 |

**OH_Preferences_SetInt()**

```ets
int OH_Preferences_SetInt(OH_Preferences *preference, const char *key, int value)
```

描述

根据Key设置Preferences实例对象中的整型值。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标PreferencesOH_Preferences实例对象的指针。 |
| const char *key | 指向需要设置的Key的指针。 |
| int value | 需要设置的整型值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 |

**OH_Preferences_SetBool()**

```ets
int OH_Preferences_SetBool(OH_Preferences *preference, const char *key, bool value)
```

描述

根据Key设置Preferences实例对象中的布尔值。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标PreferencesOH_Preferences实例对象的指针。 |
| const char *key | 指向需要设置的Key的指针。 |
| bool value | 需要设置的布尔值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 |

**OH_Preferences_SetString()**

```ets
int OH_Preferences_SetString(OH_Preferences *preference, const char *key, const char *value)
```

描述

根据Key设置Preferences实例对象中的字符串。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标PreferencesOH_Preferences实例对象的指针。 |
| const char *key | 指向需要设置的Key的指针。 |
| const char *value | 指向需要设置的字符串指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 |

**OH_Preferences_Delete()**

```ets
int OH_Preferences_Delete(OH_Preferences *preference, const char *key)
```

描述

在Preferences实例对象中删除Key对应的KV数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标PreferencesOH_Preferences实例对象的指针。 |
| const char *key | 指向需要删除的Key的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 |

**OH_Preferences_RegisterDataObserver()**

```ets
int OH_Preferences_RegisterDataObserver(OH_Preferences *preference, void *context,OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount)
```

描述

对选取的Key注册数据变更订阅。订阅的Key的值发生变更后，在调用OH_Preferences_Close()后触发回调。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标PreferencesOH_Preferences实例对象的指针。 |
| void *context | 应用上下文的指针。 |
| OH_PreferencesDataObserver observer | 订阅数据变更关联的回调函数OH_PreferencesDataObserver。 |
| const char *keys[] | 需要订阅的Key数组。 |
| uint32_t keyCount | 需要订阅的Key的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 若错误码为PREFERENCES_ERROR_GET_DATAOBSMGRCLIENT，表示获取数据变更订阅服务失败。 |

**OH_Preferences_UnregisterDataObserver()**

```ets
int OH_Preferences_UnregisterDataObserver(OH_Preferences *preference, void *context,OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount)
```

描述

取消注册选取Key的数据变更订阅。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标PreferencesOH_Preferences实例对象的指针。 |
| void *context | 应用上下文的指针。 |
| OH_PreferencesDataObserver observer | 订阅数据变更关联的回调函数OH_PreferencesDataObserver。 |
| const char *keys[] | 需要取消订阅的Key数组。 |
| uint32_t keyCount | 需要取消订阅的Key的数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。 若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。 |

**OH_Preferences_IsStorageTypeSupported()**

```ets
int OH_Preferences_IsStorageTypeSupported(Preferences_StorageType type, bool *isSupported)
```

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| Preferences_StorageType type | 要校验是否支持的存储模式。 |
| bool *isSupported | 校验结果的指针，作为出参使用。true表示当前平台支持当前校验的存储模式，false表示当前平台不支持当前校验的存储模式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回接口操作执行的状态码。 PREFERENCES_OK，表示操作成功。 PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 |

**OH_Preferences_DeletePreferences()**

```ets
int OH_Preferences_DeletePreferences(OH_PreferencesOption *option)
```

描述

删除指定的Preferences对象。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PreferencesOption *option | 指向Preferences配置选项OH_PreferencesOption的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 若错误码为PREFERENCES_ERROR_NOT_SUPPORTED，表示系统能力不支持。 若错误码为PREFERENCES_ERROR_DELETE_FILE，表示删除文件失败。 |

**OH_Preferences_SetValue()**

```ets
int OH_Preferences_SetValue(OH_Preferences *preference, const char *key, OH_PreferencesValue *value)
```

描述

在Preferences对象中设置值[OH_PreferencesValue](OH_PreferencesValue.md)。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标OH_Preferences实例的指针。 |
| const char *key | 指向需要设置的Key的指针。 |
| OH_PreferencesValue *value | 指向需要设置的OH_PreferencesValue值的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |

**OH_Preferences_GetValue()**

```ets
int OH_Preferences_GetValue(OH_Preferences *preference, const char *key, OH_PreferencesValue **value)
```

描述

根据给定的Key获取Preferences对象中的值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标OH_Preferences实例的指针。 |
| const char *key | 指向需要获取值的Key的指针。 |
| OH_PreferencesValue **value | 指向获取到的OH_PreferencesValue值的二级指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 若错误码PREFERENCES_ERROR_KEY_NOT_FOUND表示查询的Key不存在。 |

**OH_Preferences_GetAll()**

```ets
int OH_Preferences_GetAll(OH_Preferences *preference, OH_PreferencesPair **pairs, uint32_t *count)
```

描述

获取Preferences对象中的所有值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标OH_Preferences实例的指针。 |
| OH_PreferencesPair **pairs | 指向要获取的KV数据的指针。当不再需要此KV数据时，用户需要调用OH_Preferences_FreeString释放内存。 |
| uint32_t *count | 指向获取到的所有值的数量的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES_OK表示操作成功。 若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。 若错误码PREFERENCES_ERROR_STORAGE表示存储异常。 若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 若错误码PREFERENCES_ERROR_KEY_NOT_FOUND表示查询的Key不存在。 |

**OH_Preferences_HasKey()**

```ets
bool OH_Preferences_HasKey(OH_Preferences *preference, const char *key)
```

描述

检查Preferences对象是否包含与指定Key匹配的KV数据，若包含则返回true，否则返回false。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标OH_Preferences实例的指针。 |
| const char *key | 指向需要检查的Key的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| bool | 返回true则表示Preferences对象包含与指定Key匹配的KV数据，否则返回false。 |

**OH_Preferences_Flush()**

```ets
int OH_Preferences_Flush(OH_Preferences *preference)
```

描述

将[OH_Preferences](OH_Preferences.md)对象的缓存保存到xml文件中。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标OH_Preferences实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES_OK表示操作成功。  若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。  若错误码PREFERENCES_ERROR_NOT_SUPPORTED表示系统能力不支持。 |

**OH_Preferences_ClearCache()**

```ets
int OH_Preferences_ClearCache(OH_Preferences *preference)
```

描述

清除[OH_Preferences](OH_Preferences.md)对象缓存中的所有值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标OH_Preferences实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES_OK表示操作成功。  若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。  若错误码PREFERENCES_ERROR_NOT_SUPPORTED表示系统能力不支持。 |

**OH_Preferences_RegisterMultiProcessDataObserver()**

```ets
int OH_Preferences_RegisterMultiProcessDataObserver(OH_Preferences *preference, void *context, OH_PreferencesDataObserver observer)
```

描述

为Preferences对象注册一个多进程数据观察者。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标OH_Preferences实例的指针。 |
| void *context | 指向数据观察者上下文的指针。 |
| OH_PreferencesDataObserver observer | 要注册的OH_PreferencesDataObserver回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES_OK表示操作成功。  若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。  若错误码PREFERENCES_ERROR_STORAGE表示存储异常。  若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。  若错误码PREFERENCES_ERROR_GET_DATAOBSMGRCLIENT表示获取数据变更订阅服务失败。 |

**OH_Preferences_UnregisterMultiProcessDataObserver()**

```ets
int OH_Preferences_UnregisterMultiProcessDataObserver(OH_Preferences *preference, void *context, OH_PreferencesDataObserver observer)
```

描述

取消注册Preferences对象的多进程数据观察者。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Preferences *preference | 指向目标OH_Preferences实例的指针。 |
| void *context | 指向数据观察者上下文的指针。 |
| OH_PreferencesDataObserver observer | 要取消注册的OH_PreferencesDataObserver回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。  若错误码PREFERENCES_OK表示操作成功。  若错误码PREFERENCES_ERROR_INVALID_PARAM表示参数不合法。  若错误码PREFERENCES_ERROR_STORAGE表示存储异常。  若错误码PREFERENCES_ERROR_MALLOC表示内存分配失败。 |