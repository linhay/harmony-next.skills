# asset_api.h

**概述**

声明用于访问关键资产的接口。

引用文件： <asset/asset_api.h>

库： libasset_ndk.z.so

系统能力： SystemCapability.Security.Asset

起始版本： 11

相关模块： [AssetApi](AssetApi.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t OH_Asset_Add(const Asset_Attr *attributes, uint32_t attrCnt) | 新增一条关键资产。 如果要设置Asset_Tag.ASSET_TAG_IS_PERSISTENT属性，需要申请ohos.permission.STORE_PERSISTENT_DATA权限。 |
| int32_t OH_Asset_Remove(const Asset_Attr *query, uint32_t queryCnt) | 删除符合条件的一条或多条关键资产。 |
| int32_t OH_Asset_Update(const Asset_Attr *query, uint32_t queryCnt, const Asset_Attr *attributesToUpdate, uint32_t updateCnt) | 更新符合条件的一条关键资产。 |
| int32_t OH_Asset_PreQuery(const Asset_Attr *query, uint32_t queryCnt, Asset_Blob *challenge) | 查询的预处理，用于需要用户认证的关键资产。 |
| int32_t OH_Asset_Query(const Asset_Attr *query, uint32_t queryCnt, Asset_ResultSet *resultSet) | 查询一条或多条符合条件的关键资产。 |
| int32_t OH_Asset_PostQuery(const Asset_Attr *handle, uint32_t handleCnt) | 查询的后置处理，用于需要用户认证的关键资产。 |
| int32_t OH_Asset_QuerySyncResult(const Asset_Attr *query, uint32_t queryCnt, Asset_SyncResult *syncResult) | 查询关键资产的同步结果。 |
| Asset_Attr *OH_Asset_ParseAttr(const Asset_Result *result, Asset_Tag tag) | 解析查询结果，并获取指定的属性值。 |
| void OH_Asset_FreeBlob(Asset_Blob *blob) | 释放挑战值所占用的内存。 |
| void OH_Asset_FreeResultSet(Asset_ResultSet *resultSet) | 释放查询结果所占用的内存。 |

**函数说明**

**OH_Asset_Add()**

```ets
int32_t OH_Asset_Add(const Asset_Attr *attributes, uint32_t attrCnt)
```

描述

新增一条关键资产。

如果要设置[Asset_Tag](asset_type.h.md#ZH-CN_TOPIC_0000002553201287__asset_tag).ASSET_TAG_IS_PERSISTENT属性，需要申请ohos.permission.STORE_PERSISTENT_DATA权限。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const Asset_Attr *attributes | 待新增关键资产的属性集合。 |
| uint32_t attrCnt | 待新增关键资产的属性数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | Asset_ResultCode:  ASSET_SUCCESS = 0：操作成功。  ASSET_PERMISSION_DENIED = 201：调用方不是一个系统应用。  ASSET_INVALID_ARGUMENT = 401：参数错误。 可能原因:  1. 必选参数未指定。  2. 参数类型错误。  3. 参数校验失败。  ASSET_SERVICE_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET_DUPLICATED = 24000003：关键资产已存在。  ASSET_STATUS_MISMATCH = 24000005：锁屏状态不匹配。  ASSET_OUT_OF_MEMORY = 24000006：系统内存不足。  ASSET_DATA_CORRUPTED = 24000007：关键资产损坏。  ASSET_DATABASE_ERROR = 24000008：数据库操作失败。  ASSET_CRYPTO_ERROR = 24000009：算法库操作失败。  ASSET_IPC_ERROR = 24000010：进程通信错误。  ASSET_BMS_ERROR = 24000011：包管理服务异常。  ASSET_ACCOUNT_ERROR = 24000012：账号系统服务异常。  ASSET_ACCESS_TOKEN_ERROR = 24000013：访问控制服务异常。  ASSET_FILE_OPERATION_ERROR = 24000014：文件操作失败。  ASSET_GET_SYSTEM_TIME_ERROR = 24000015：获取系统时间失败。 |

**OH_Asset_Remove()**

```ets
int32_t OH_Asset_Remove(const Asset_Attr *query, uint32_t queryCnt)
```

描述

删除符合条件的一条或多条关键资产。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const Asset_Attr *query | 待删除关键资产的搜索条件。 |
| uint32_t queryCnt | 待删除关键资产搜索条件的个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | Asset_ResultCode:  ASSET_SUCCESS = 0：操作成功。  ASSET_INVALID_ARGUMENT = 401：参数错误。 可能原因:  1. 参数类型错误。  2. 参数校验失败。  ASSET_SERVICE_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET_NOT_FOUND = 24000002：未找到关键资产。  ASSET_OUT_OF_MEMORY = 24000006：系统内存不足。  ASSET_DATA_CORRUPTED = 24000007：关键资产损坏。  ASSET_DATABASE_ERROR = 24000008：数据库操作失败。  ASSET_IPC_ERROR = 24000010：进程通信错误。  ASSET_BMS_ERROR = 24000011：包管理服务异常。  ASSET_ACCOUNT_ERROR = 24000012：账号系统服务异常。  ASSET_ACCESS_TOKEN_ERROR = 24000013：访问控制服务异常。  ASSET_GET_SYSTEM_TIME_ERROR = 24000015：获取系统时间失败。 |

**OH_Asset_Update()**

```ets
int32_t OH_Asset_Update(const Asset_Attr *query, uint32_t queryCnt,const Asset_Attr *attributesToUpdate, uint32_t updateCnt)
```

描述

更新符合条件的一条关键资产。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const Asset_Attr *query | 待更新关键资产的搜索条件。 |
| uint32_t queryCnt | 待更新关键资产搜索条件的个数。 |
| const Asset_Attr *attributesToUpdate | 待更新关键资产的属性集合。 |
| uint32_t updateCnt | 待更新关键资产的属性数量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | Asset_ResultCode:  ASSET_SUCCESS = 0：操作成功。  ASSET_INVALID_ARGUMENT = 401：参数错误。 可能原因:  1. 必选参数未指定。  2. 参数类型错误。  3. 参数校验失败。  ASSET_SERVICE_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET_NOT_FOUND = 24000002：未找到关键资产。  ASSET_STATUS_MISMATCH = 24000005：锁屏状态不匹配。  ASSET_OUT_OF_MEMORY = 24000006：系统内存不足。  ASSET_DATA_CORRUPTED = 24000007：关键资产损坏。  ASSET_DATABASE_ERROR = 24000008：数据库操作失败。  ASSET_CRYPTO_ERROR = 24000009：算法库操作失败。  ASSET_IPC_ERROR = 24000010：进程通信错误。  ASSET_BMS_ERROR = 24000011：包管理服务异常。  ASSET_ACCOUNT_ERROR = 24000012：账号系统服务异常。  ASSET_ACCESS_TOKEN_ERROR = 24000013：访问控制服务异常。  ASSET_GET_SYSTEM_TIME_ERROR = 24000015：获取系统时间失败。 |

**OH_Asset_PreQuery()**

```ets
int32_t OH_Asset_PreQuery(const Asset_Attr *query, uint32_t queryCnt, Asset_Blob *challenge)
```

描述

查询的预处理，用于需要用户认证的关键资产。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const Asset_Attr *query | 关键资产的查询条件。 |
| uint32_t queryCnt | 关键资产查询条件的个数。 |
| Asset_Blob *challenge | 挑战值，在后续调用OH_Asset_Query时使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | Asset_ResultCode:  ASSET_SUCCESS = 0：操作成功。  ASSET_INVALID_ARGUMENT = 401：参数错误。 可能原因:  1. 参数类型错误。  2. 参数校验失败。  ASSET_SERVICE_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET_NOT_FOUND = 24000002：未找到关键资产。  ASSET_STATUS_MISMATCH = 24000005：锁屏状态不匹配。  ASSET_OUT_OF_MEMORY = 24000006：系统内存不足。  ASSET_DATA_CORRUPTED = 24000007：关键资产损坏。  ASSET_DATABASE_ERROR = 24000008：数据库操作失败。  ASSET_CRYPTO_ERROR = 24000009：算法库操作失败。  ASSET_IPC_ERROR = 24000010：进程通信错误。  ASSET_BMS_ERROR = 24000011：包管理服务异常。  ASSET_ACCOUNT_ERROR = 24000012：账号系统服务异常。  ASSET_ACCESS_TOKEN_ERROR = 24000013：访问控制服务异常。  ASSET_LIMIT_EXCEEDED = 24000016：缓存数量超限。  ASSET_UNSUPPORTED = 24000017：该子功能不支持。 |

**OH_Asset_Query()**

```ets
int32_t OH_Asset_Query(const Asset_Attr *query, uint32_t queryCnt, Asset_ResultSet *resultSet)
```

描述

查询一条或多条符合条件的关键资产。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const Asset_Attr *query | 关键资产的查询条件。 |
| uint32_t queryCnt | 关键资产查询条件的个数。 |
| Asset_ResultSet *resultSet | 查询结果列表。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | Asset_ResultCode:  ASSET_SUCCESS = 0：操作成功。  ASSET_INVALID_ARGUMENT = 401：参数错误。 可能原因:  1. 参数类型错误。  2. 参数校验失败。  ASSET_SERVICE_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET_NOT_FOUND = 24000002：未找到关键资产。  ASSET_ACCESS_DENIED = 24000004：访问被拒绝。  ASSET_STATUS_MISMATCH = 24000005：锁屏状态不匹配。  ASSET_OUT_OF_MEMORY = 24000006：系统内存不足。  ASSET_DATA_CORRUPTED = 24000007：关键资产损坏。  ASSET_DATABASE_ERROR = 24000008：数据库操作失败。  ASSET_CRYPTO_ERROR = 24000009：算法库操作失败。  ASSET_IPC_ERROR = 24000010：进程通信错误。  ASSET_BMS_ERROR = 24000011：包管理服务异常。  ASSET_ACCOUNT_ERROR = 24000012：账号系统服务异常。  ASSET_ACCESS_TOKEN_ERROR = 24000013：访问控制服务异常。  ASSET_UNSUPPORTED = 24000017：该子功能不支持。 |

**OH_Asset_PostQuery()**

```ets
int32_t OH_Asset_PostQuery(const Asset_Attr *handle, uint32_t handleCnt)
```

描述

查询的后置处理，用于需要用户认证的关键资产。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const Asset_Attr *handle | 待处理的查询句柄，当前包含OH_Asset_PreQuery执行成功返回的挑战值。 |
| uint32_t handleCnt | 句柄属性集合中元素的个数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | Asset_ResultCode:  ASSET_SUCCESS = 0：操作成功。  ASSET_INVALID_ARGUMENT = 401：参数错误。 可能原因:  1. 必选参数未指定。  2. 参数类型错误。  3. 参数校验失败。  ASSET_SERVICE_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET_OUT_OF_MEMORY = 24000006：系统内存不足。  ASSET_IPC_ERROR = 24000010：进程通信错误。  ASSET_BMS_ERROR = 24000011：包管理服务异常。  ASSET_ACCOUNT_ERROR = 24000012：账号系统服务异常。  ASSET_ACCESS_TOKEN_ERROR = 24000013：访问控制服务异常。 |

**OH_Asset_QuerySyncResult()**

```ets
int32_t OH_Asset_QuerySyncResult(const Asset_Attr *query, uint32_t queryCnt, Asset_SyncResult *syncResult)
```

描述

查询关键资产的同步结果。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| const Asset_Attr *query | 关键资产同步结果的查询条件。 |
| uint32_t queryCnt | 关键资产同步结果的查询条件个数。 |
| Asset_SyncResult *syncResult | 查询到的关键资产同步结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | Asset_ResultCode：  ASSET_SUCCESS = 0：操作成功。  ASSET_SERVICE_UNAVAILABLE = 24000001：关键资产服务不可用。  ASSET_OUT_OF_MEMORY = 24000006：系统内存不足。  ASSET_IPC_ERROR = 24000010：进程通信错误。  ASSET_BMS_ERROR = 24000011：包管理服务异常。  ASSET_ACCOUNT_ERROR = 24000012：账号系统服务异常。  ASSET_ACCESS_TOKEN_ERROR = 24000013：访问控制服务异常。  ASSET_FILE_OPERATION_ERROR = 24000014：文件操作失败。  ASSET_PARAM_VERIFICATION_FAILED = 24000018：参数校验失败。 |

**OH_Asset_ParseAttr()**

```ets
Asset_Attr *OH_Asset_ParseAttr(const Asset_Result *result, Asset_Tag tag)
```

描述

解析查询结果，并获取指定的属性值。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| const Asset_Result *result | 从OH_Asset_Query中获取的查询结果。 |
| Asset_Tag tag | 待获取的属性标签。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Asset_Attr | 如果操作成功，则以Asset_Attr的形式返回属性，该属性不需要业务进行释放；否则返回NULL。 |

**OH_Asset_FreeBlob()**

```ets
void OH_Asset_FreeBlob(Asset_Blob *blob)
```

描述

释放挑战值所占用的内存。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Asset_Blob *blob | 从OH_Asset_PreQuery获取的挑战值。 |

**OH_Asset_FreeResultSet()**

```ets
void OH_Asset_FreeResultSet(Asset_ResultSet *resultSet)
```

描述

释放查询结果所占用的内存。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Asset_ResultSet *resultSet | 从OH_Asset_Query得到的查询结果列表。 |