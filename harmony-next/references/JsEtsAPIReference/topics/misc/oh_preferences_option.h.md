# oh_preferences_option.h

**概述**

提供访问Preferences配置选项（PreferencesOption）的接口与数据结构。

引用文件： <database/preferences/oh_preferences_option.h>

库： libohpreferences.so

系统能力： SystemCapability.DistributedDataManager.Preferences.Core

起始版本： 13

相关模块： [Preferences](Preferences.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_PreferencesOption | OH_PreferencesOption | 定义Preferences配置选项的数据结构。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Preferences_StorageType | Preferences_StorageType | 首选项配置选项的存储模式枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_PreferencesOption *OH_PreferencesOption_Create(void) | 创建一个Preferences配置选项的OH_PreferencesOption实例对象以及指向它的指针。 当不再需要使用指针时，请使用OH_PreferencesOption_Destroy销毁实例对象，否则会导致内存泄漏。 |
| int OH_PreferencesOption_SetFileName(OH_PreferencesOption *option, const char *fileName) | 设置Preferences配置选项OH_PreferencesOption实例对象的文件名称。 |
| int OH_PreferencesOption_SetBundleName(OH_PreferencesOption *option, const char *bundleName) | 设置Preferences配置选项OH_PreferencesOption实例对象的包名称。 |
| int OH_PreferencesOption_SetDataGroupId(OH_PreferencesOption *option, const char *dataGroupId) | 设置Preferences配置选项OH_PreferencesOption实例对象的应用组ID。 设置应用组ID后，会指定在此应用组ID对应的沙箱路径下创建Preferences实例。应用组ID需要向应用市场获取，暂不支持。 当传入的应用组ID为空字符串时，默认在本应用沙箱目录下创建Preferences实例。 |
| int OH_PreferencesOption_SetStorageType(OH_PreferencesOption *option, Preferences_StorageType type) | 设置Preferences实例对象的存储模式。 |
| int OH_PreferencesOption_Destroy(OH_PreferencesOption *option) | 销毁Preferences配置选项OH_PreferencesOption实例。 |

**枚举类型说明**

**Preferences_StorageType**

```ets
enum Preferences_StorageType
```

描述

首选项配置选项的存储模式枚举。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| PREFERENCES_STORAGE_XML = 0 | XML存储模式，对数据的操作发生在内存中，调用OH_Preferences_Close时落盘，不支持多进程。 |
| PREFERENCES_STORAGE_GSKV | GSKV存储模式，对数据的操作实时落盘，可支持多进程 |

**函数说明**

**OH_PreferencesOption_Create()**

```ets
OH_PreferencesOption *OH_PreferencesOption_Create(void)
```

描述

创建一个Preferences配置选项的[OH_PreferencesOption](OH_PreferencesOption.md)实例对象以及指向它的指针。

当不再需要使用指针时，请使用[OH_PreferencesOption_Destroy](oh_preferences_option.h.md#ZH-CN_TOPIC_0000002553200611__oh_preferencesoption_destroy)销毁实例对象，否则会导致内存泄漏。

起始版本： 13

返回：

| 类型 | 说明 |
| --- | --- |
| OH_PreferencesOption | 如果操作成功，返回指向Preferences配置选项OH_PreferencesOption实例对象的指针。失败返回空指针。 |

**OH_PreferencesOption_SetFileName()**

```ets
int OH_PreferencesOption_SetFileName(OH_PreferencesOption *option, const char *fileName)
```

描述

设置Preferences配置选项[OH_PreferencesOption](OH_PreferencesOption.md)实例对象的文件名称。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PreferencesOption *option | 指向Preferences配置选项OH_PreferencesOption实例对象的指针。 |
| const char *fileName | 需要设置的文件名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 |

参考：

OH_Preferences_ErrCode

**OH_PreferencesOption_SetBundleName()**

```ets
int OH_PreferencesOption_SetBundleName(OH_PreferencesOption *option, const char *bundleName)
```

描述

设置Preferences配置选项[OH_PreferencesOption](OH_PreferencesOption.md)实例对象的包名称。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PreferencesOption *option | 配置选项OH_PreferencesOption实例对象的指针。 |
| const char *bundleName | 需要设置的包名称。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 |

**OH_PreferencesOption_SetDataGroupId()**

```ets
int OH_PreferencesOption_SetDataGroupId(OH_PreferencesOption *option, const char *dataGroupId)
```

描述

设置Preferences配置选项[OH_PreferencesOption](OH_PreferencesOption.md)实例对象的应用组ID。

设置应用组ID后，会指定在此应用组ID对应的沙箱路径下创建Preferences实例。应用组ID需要向应用市场获取，暂不支持。

当传入的应用组ID为空字符串时，默认在本应用沙箱目录下创建Preferences实例。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PreferencesOption *option | 配置选项OH_PreferencesOption实例对象的指针。 |
| const char *dataGroupId | 需要设置的应用组ID。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 |

**OH_PreferencesOption_SetStorageType()**

```ets
int OH_PreferencesOption_SetStorageType(OH_PreferencesOption *option, Preferences_StorageType type)
```

描述

设置Preferences实例对象的存储模式。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PreferencesOption *option | 指向要设置存储模式的配置项的指针。 |
| Preferences_StorageType type | 需要设置的存储模式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行的错误码。 若错误码为PREFERENCES_OK，表示操作成功。 若错误码为PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 |

**OH_PreferencesOption_Destroy()**

```ets
int OH_PreferencesOption_Destroy(OH_PreferencesOption *option)
```

描述

销毁Preferences配置选项[OH_PreferencesOption](OH_PreferencesOption.md)实例。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PreferencesOption *option | 配置选项OH_PreferencesOption实例对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回接口操作执行的状态码。 PREFERENCES_OK，表示操作成功。 PREFERENCES_ERROR_INVALID_PARAM，表示参数不合法。 |