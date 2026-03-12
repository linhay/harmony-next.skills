# oh_preferences.h

#### 概述

提供访问Preferences对象的接口与数据结构。

**引用文件：** <database/preferences/oh_preferences.h>

**库：** libohpreferences.so

**系统能力：** SystemCapability.DistributedDataManager.Preferences.Core

**起始版本：** 13

**相关模块：**[Preferences](Preferences.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_Preferences](OH_Preferences.md)OH_Preferences定义Preferences对象类型。

#### 函数

名称typedef关键字描述[typedef void (*OH_PreferencesDataObserver)(void *context, const OH_PreferencesPair *pairs, uint32_t count)](#ZH-CN_TOPIC_0000002497604698__oh_preferencesdataobserver)OH_PreferencesDataObserver定义数据变更触发的回调函数类型。[OH_Preferences *OH_Preferences_Open(OH_PreferencesOption *option, int *errCode)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_open)-

打开一个Preferences实例对象并创建指向它的指针。

当不再需要使用指针时，请使用[OH_Preferences_Close](oh_preferences.h.md#ZH-CN_TOPIC_0000002497604698__oh_preferences_close)关闭实例对象。

[int OH_Preferences_Close(OH_Preferences *preference)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_close)-关闭一个Preferences实例对象。[int OH_Preferences_GetInt(OH_Preferences *preference, const char *key, int *value)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_getint)-获取Preferences实例对象中Key对应的整型值。[int OH_Preferences_GetBool(OH_Preferences *preference, const char *key, bool *value)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_getbool)-获取Preferences实例对象中Key对应的布尔值。[int OH_Preferences_GetString(OH_Preferences *preference, const char *key, char **value, uint32_t *valueLen)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_getstring)-获取Preferences实例对象中Key对应的字符串。[void OH_Preferences_FreeString(char *string)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_freestring)-释放从Preferences实例对象中获取的字符串。[int OH_Preferences_SetInt(OH_Preferences *preference, const char *key, int value)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_setint)-根据Key设置Preferences实例对象中的整型值。[int OH_Preferences_SetBool(OH_Preferences *preference, const char *key, bool value)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_setbool)-根据Key设置Preferences实例对象中的布尔值。[int OH_Preferences_SetString(OH_Preferences *preference, const char *key, const char *value)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_setstring)-根据Key设置Preferences实例对象中的字符串。[int OH_Preferences_Delete(OH_Preferences *preference, const char *key)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_delete)-在Preferences实例对象中删除Key对应的KV数据。[int OH_Preferences_RegisterDataObserver(OH_Preferences *preference, void *context,OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_registerdataobserver)-对选取的Key注册数据变更订阅。订阅的Key的值发生变更后，在调用OH_Preferences_Close()后触发回调。[int OH_Preferences_UnregisterDataObserver(OH_Preferences *preference, void *context,OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_unregisterdataobserver)-取消注册选取Key的数据变更订阅。[int OH_Preferences_IsStorageTypeSupported(Preferences_StorageType type, bool *isSupported)](#ZH-CN_TOPIC_0000002497604698__oh_preferences_isstoragetypesupported)-校验当前平台是否支持对应存储模式。

#### 函数说明

#### OH_PreferencesDataObserver()

```ets
typedef void (*OH_PreferencesDataObserver)(void *context, const OH_PreferencesPair *pairs, uint32_t count)
```

**描述**

定义数据变更触发的回调函数类型。

**起始版本：** 13

**参数：**

参数项描述void *context应用上下文的指针。const [OH_PreferencesPair](OH_PreferencesPair.md) *pairs发生变更的KV数据的指针。uint32_t count发生变更的KV数据的数量。

#### OH_Preferences_Open()

```ets
OH_Preferences *OH_Preferences_Open(OH_PreferencesOption *option, int *errCode)
```

**描述**

打开一个Preferences实例对象并创建指向它的指针。

当不再需要使用指针时，请使用[OH_Preferences_Close](oh_preferences.h.md#ZH-CN_TOPIC_0000002497604698__oh_preferences_close)关闭实例对象。

**起始版本：** 13

**参数：**

参数项描述[OH_PreferencesOption](OH_PreferencesOption.md) *option指向Preferences配置选项[OH_PreferencesOption](OH_PreferencesOption.md)的指针。int *errCode

该参数作为出参使用，表示指向返回错误码的指针，详见[OH_Preferences_ErrCode](oh_preferences_err_code.h.md#ZH-CN_TOPIC_0000002497444720__oh_preferences_errcode)。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_NOT_SUPPORTED，表示系统能力不支持。

若错误码为PREFERENCES_ERROR_DELETE_FILE，表示删除文件失败。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

**返回：**

类型说明[OH_Preferences](OH_Preferences.md)当操作成功时，返回指向打开的Preferences对象[OH_Preferences](OH_Preferences.md)实例对象的指针，失败返回空指针。

#### OH_Preferences_Close()

```ets
int OH_Preferences_Close(OH_Preferences *preference)
```

**描述**

关闭一个Preferences实例对象。

**起始版本：** 13

**参数：**

参数项描述[OH_Preferences](OH_Preferences.md) *preference指向需要关闭的Preferences[OH_Preferences](OH_Preferences.md)实例对象的指针。

**返回：**

类型说明int

返回执行的错误码，详见[OH_Preferences_ErrCode](oh_preferences_err_code.h.md#ZH-CN_TOPIC_0000002497444720__oh_preferences_errcode)。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

#### OH_Preferences_GetInt()

```ets
int OH_Preferences_GetInt(OH_Preferences *preference, const char *key, int *value)
```

**描述**

获取Preferences实例对象中Key对应的整型值。

**起始版本：** 13

**参数：**

参数项描述[OH_Preferences](OH_Preferences.md) *preference指向目标Preferences[OH_Preferences](OH_Preferences.md)实例对象的指针。const char *key需要获取的Key的指针。int *value该参数作为出参使用，表示指向获取到的整型值的指针。

**返回：**

类型说明int

返回执行的错误码。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

若错误码为PREFERENCES_ERROR_KEY_NOT_FOUND，表示查询的Key不存在。

#### OH_Preferences_GetBool()

```ets
int OH_Preferences_GetBool(OH_Preferences *preference, const char *key, bool *value)
```

**描述**

获取Preferences实例对象中Key对应的布尔值。

**起始版本：** 13

**参数：**

参数项描述[OH_Preferences](OH_Preferences.md) *preference指向目标Preferences[OH_Preferences](OH_Preferences.md)实例对象的指针。const char *key需要获取的Key的指针。bool *value该参数作为出参使用，表示指向获取到的布尔值的指针。

**返回：**

类型说明int

返回执行的错误码。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

若错误码为PREFERENCES_ERROR_KEY_NOT_FOUND，表示查询的key不存在。

#### OH_Preferences_GetString()

```ets
int OH_Preferences_GetString(OH_Preferences *preference, const char *key, char **value, uint32_t *valueLen)
```

**描述**

获取Preferences实例对象中Key对应的字符串。

**起始版本：** 13

**参数：**

参数项描述[OH_Preferences](OH_Preferences.md) *preference指向目标Preferences[OH_Preferences](OH_Preferences.md)实例对象的指针。const char *key需要获取的Key的指针。char **value该参数作为出参使用，表示指向获取到的字符串的二级指针，使用完毕后需要调用释放函数[OH_Preferences_FreeString](oh_preferences.h.md#ZH-CN_TOPIC_0000002497604698__oh_preferences_freestring)释放内存。uint32_t *valueLen该参数作为出参使用，表示获取到的字符串长度的指针。

**返回：**

类型说明int

返回执行的错误码。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

若错误码为PREFERENCES_ERROR_KEY_NOT_FOUND，表示查询的Key不存在。

#### OH_Preferences_FreeString()

```ets
void OH_Preferences_FreeString(char *string)
```

**描述**

释放从Preferences实例对象中获取的字符串。

**起始版本：** 13

**参数：**

参数项描述char *string需要释放的字符串指针。

#### OH_Preferences_SetInt()

```ets
int OH_Preferences_SetInt(OH_Preferences *preference, const char *key, int value)
```

**描述**

根据Key设置Preferences实例对象中的整型值。

**起始版本：** 13

**参数：**

参数项描述[OH_Preferences](OH_Preferences.md) *preference指向目标Preferences[OH_Preferences](OH_Preferences.md)实例对象的指针。const char *key指向需要设置的Key的指针。int value需要设置的整型值。

**返回：**

类型说明int

返回执行的错误码。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

#### OH_Preferences_SetBool()

```ets
int OH_Preferences_SetBool(OH_Preferences *preference, const char *key, bool value)
```

**描述**

根据Key设置Preferences实例对象中的布尔值。

**起始版本：** 13

**参数：**

参数项描述[OH_Preferences](OH_Preferences.md) *preference指向目标Preferences[OH_Preferences](OH_Preferences.md)实例对象的指针。const char *key指向需要设置的Key的指针。bool value需要设置的布尔值。

**返回：**

类型说明int

返回执行的错误码。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

#### OH_Preferences_SetString()

```ets
int OH_Preferences_SetString(OH_Preferences *preference, const char *key, const char *value)
```

**描述**

根据Key设置Preferences实例对象中的字符串。

**起始版本：** 13

**参数：**

参数项描述[OH_Preferences](OH_Preferences.md) *preference指向目标Preferences[OH_Preferences](OH_Preferences.md)实例对象的指针。const char *key指向需要设置的Key的指针。const char *value指向需要设置的字符串指针。

**返回：**

类型说明int

返回执行的错误码。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

#### OH_Preferences_Delete()

```ets
int OH_Preferences_Delete(OH_Preferences *preference, const char *key)
```

**描述**

在Preferences实例对象中删除Key对应的KV数据。

**起始版本：** 13

**参数：**

参数项描述[OH_Preferences](OH_Preferences.md) *preference指向目标Preferences[OH_Preferences](OH_Preferences.md)实例对象的指针。const char *key指向需要删除的Key的指针。

**返回：**

类型说明int

返回执行的错误码。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

**参考：**

OH_Preferences_ErrCode

#### OH_Preferences_RegisterDataObserver()

```ets
int OH_Preferences_RegisterDataObserver(OH_Preferences *preference, void *context,OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount)
```

**描述**

对选取的Key注册数据变更订阅。订阅的Key的值发生变更后，在调用OH_Preferences_Close()后触发回调。

**起始版本：** 13

**参数：**

参数项描述[OH_Preferences](OH_Preferences.md) *preference指向目标Preferences[OH_Preferences](OH_Preferences.md)实例对象的指针。void *context应用上下文的指针。[OH_PreferencesDataObserver](#ZH-CN_TOPIC_0000002497604698__oh_preferencesdataobserver) observer订阅数据变更关联的回调函数[OH_PreferencesDataObserver](zh-cn_topic_0000002497604698.html#ZH-CN_TOPIC_0000002497604698__oh_preferencesdataobserver)。const char *keys[]需要订阅的Key数组。uint32_t keyCount需要订阅的Key的数量。

**返回：**

类型说明int

返回执行的错误码。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

若错误码为PREFERENCES_ERROR_GET_DATAOBSMGRCLIENT，表示获取数据变更订阅服务失败。

#### OH_Preferences_UnregisterDataObserver()

```ets
int OH_Preferences_UnregisterDataObserver(OH_Preferences *preference, void *context,OH_PreferencesDataObserver observer, const char *keys[], uint32_t keyCount)
```

**描述**

取消注册选取Key的数据变更订阅。

**起始版本：** 13

**参数：**

参数项描述[OH_Preferences](OH_Preferences.md) *preference指向目标Preferences[OH_Preferences](OH_Preferences.md)实例对象的指针。void *context应用上下文的指针。[OH_PreferencesDataObserver](#ZH-CN_TOPIC_0000002497604698__oh_preferencesdataobserver) observer订阅数据变更关联的回调函数[OH_PreferencesDataObserver](zh-cn_topic_0000002497604698.html#ZH-CN_TOPIC_0000002497604698__oh_preferencesdataobserver)。const char *keys[]需要取消订阅的Key数组。uint32_t keyCount需要取消订阅的Key的数量。

**返回：**

类型说明int

返回执行的错误码。

若错误码为PREFERENCES_OK，表示操作成功。

若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。

若错误码为PREFERENCES_ERROR_STORAGE，表示存储异常。

若错误码为PREFERENCES_ERROR_MALLOC，表示内存分配失败。

**参考：**

OH_Preferences_ErrCode

#### OH_Preferences_IsStorageTypeSupported()

```ets
int OH_Preferences_IsStorageTypeSupported(Preferences_StorageType type, bool *isSupported)
```

**起始版本：** 18

**参数：**

参数项描述[Preferences_StorageType](oh_preferences_option.h.md#ZH-CN_TOPIC_0000002529284691__preferences_storagetype) type要校验是否支持的存储模式。bool *isSupported校验结果的指针，作为出参使用。true表示当前平台支持当前校验的存储模式，false表示当前平台不支持当前校验的存储模式。

**返回：**

类型说明int

返回接口操作执行的状态码。

PREFERENCES_OK，表示操作成功。

PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。