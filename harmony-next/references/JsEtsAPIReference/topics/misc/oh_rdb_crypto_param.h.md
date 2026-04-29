# oh_rdb_crypto_param.h

**概述**

提供与关系型数据库加密参数相关的函数和枚举。

引用文件： <database/rdb/oh_rdb_crypto_param.h>

库： libnative_rdb_ndk.z.so

系统能力： SystemCapability.DistributedDataManager.RelationalStore.Core

起始版本： 20

相关模块： [RDB](RDB.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Rdb_CryptoParam | OH_Rdb_CryptoParam | 指定打开加密数据库时使用的加密参数。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Rdb_EncryptionAlgo | Rdb_EncryptionAlgo | 数据库加密算法。 |
| Rdb_HmacAlgo | Rdb_HmacAlgo | 打开数据库时支持的HMAC算法。 |
| Rdb_KdfAlgo | Rdb_KdfAlgo | 打开数据库时支持的KDF算法。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Rdb_CryptoParam *OH_Rdb_CreateCryptoParam(void) | 创建一个OH_Rdb_CryptoParam实例对象。 |
| int OH_Rdb_DestroyCryptoParam(OH_Rdb_CryptoParam *param) | 销毁一个OH_Rdb_CryptoParam实例对象。 |
| int OH_Crypto_SetEncryptionKey(OH_Rdb_CryptoParam *param, const uint8_t *key, int32_t length) | 设置OH_Rdb_CryptoParam对象的密钥数据。 |
| int OH_Crypto_SetIteration(OH_Rdb_CryptoParam *param, int64_t iteration) | 设置打开加密数据库时使用的KDF算法迭代次数。 |
| int OH_Crypto_SetEncryptionAlgo(OH_Rdb_CryptoParam *param, int32_t algo) | 设置打开加密数据库时使用的加密算法。 |
| int OH_Crypto_SetHmacAlgo(OH_Rdb_CryptoParam *param, int32_t algo) | 设置打开加密数据库时使用的HMAC算法。 |
| int OH_Crypto_SetKdfAlgo(OH_Rdb_CryptoParam *param, int32_t algo) | 设置打开加密数据库时使用的KDF算法。 |
| int OH_Crypto_SetCryptoPageSize(OH_Rdb_CryptoParam *param, int64_t size) | 设置打开加密数据库时使用的页大小。 |

**枚举类型说明**

**Rdb_EncryptionAlgo**

```ets
enum Rdb_EncryptionAlgo
```

描述

数据库加密算法。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| RDB_AES_256_GCM = 0 | 表示数据库使用RDB_AES_256_GCM加密。 |
| RDB_AES_256_CBC | 表示数据库使用RDB_AES_256_CBC加密。 |
| RDB_PLAIN_TEXT | 表示数据库不加密。 起始版本： 22 |

**Rdb_HmacAlgo**

```ets
enum Rdb_HmacAlgo
```

描述

打开数据库时支持的HMAC算法。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| RDB_HMAC_SHA1 = 0 | RDB_HMAC_SHA1算法。 |
| RDB_HMAC_SHA256 | RDB_HMAC_SHA256算法。 |
| RDB_HMAC_SHA512 | RDB_HMAC_SHA512算法。 |

**Rdb_KdfAlgo**

```ets
enum Rdb_KdfAlgo
```

描述

打开数据库时支持的KDF算法。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| RDB_KDF_SHA1 = 0 | RDB_KDF_SHA1算法。 |
| RDB_KDF_SHA256 | RDB_KDF_SHA256算法。 |
| RDB_KDF_SHA512 | RDB_KDF_SHA512算法。 |

**函数说明**

**OH_Rdb_CreateCryptoParam()**

```ets
OH_Rdb_CryptoParam *OH_Rdb_CreateCryptoParam(void)
```

描述

创建一个[OH_Rdb_CryptoParam](OH_Rdb_CryptoParam.md)实例对象。

起始版本： 20

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Rdb_CryptoParam | 成功时返回指向OH_Rdb_CryptoParam实例的指针。 否则返回nullptr。使用完成后，必须通过OH_Rdb_DestroyCryptoParam接口释放内存。 |

**OH_Rdb_DestroyCryptoParam()**

```ets
int OH_Rdb_DestroyCryptoParam(OH_Rdb_CryptoParam *param)
```

描述

销毁一个[OH_Rdb_CryptoParam](OH_Rdb_CryptoParam.md)实例对象。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_CryptoParam *param | 表示指向OH_Rdb_CryptoParam实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 如果执行成功，返回RDB_OK。 如果输入参数无效，返回RDB_E_INVALID_ARGS。 |

**OH_Crypto_SetEncryptionKey()**

```ets
int OH_Crypto_SetEncryptionKey(OH_Rdb_CryptoParam *param, const uint8_t *key, int32_t length)
```

描述

设置[OH_Rdb_CryptoParam](OH_Rdb_CryptoParam.md)对象的密钥数据。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_CryptoParam *param | 表示指向OH_Rdb_CryptoParam实例的指针。 |
| const uint8_t *key | 表示指向数组数据的指针。 |
| int32_t length | 表示密钥数组的大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 如果执行成功，返回RDB_OK。 如果输入参数无效，返回RDB_E_INVALID_ARGS。 |

**OH_Crypto_SetIteration()**

```ets
int OH_Crypto_SetIteration(OH_Rdb_CryptoParam *param, int64_t iteration)
```

描述

设置打开加密数据库时使用的KDF算法迭代次数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_CryptoParam *param | 表示指向OH_Rdb_CryptoParam实例的指针。 |
| int64_t iteration | 表示迭代次数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 如果执行成功，返回RDB_OK。 如果输入参数无效，返回RDB_E_INVALID_ARGS。 |

**OH_Crypto_SetEncryptionAlgo()**

```ets
int OH_Crypto_SetEncryptionAlgo(OH_Rdb_CryptoParam *param, int32_t algo)
```

描述

设置打开加密数据库时使用的加密算法。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_CryptoParam *param | 表示指向OH_Rdb_CryptoParam实例的指针。 |
| int32_t algo | 表示加密算法。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 如果执行成功，返回RDB_OK。 如果输入参数无效，返回RDB_E_INVALID_ARGS。 |

**OH_Crypto_SetHmacAlgo()**

```ets
int OH_Crypto_SetHmacAlgo(OH_Rdb_CryptoParam *param, int32_t algo)
```

描述

设置打开加密数据库时使用的HMAC算法。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_CryptoParam *param | 表示指向OH_Rdb_CryptoParam实例的指针。 |
| int32_t algo | 表示HMAC算法。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 如果执行成功，返回RDB_OK。 如果输入参数无效，返回RDB_E_INVALID_ARGS。 |

**OH_Crypto_SetKdfAlgo()**

```ets
int OH_Crypto_SetKdfAlgo(OH_Rdb_CryptoParam *param, int32_t algo)
```

描述

设置打开加密数据库时使用的KDF算法。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_CryptoParam *param | 表示指向OH_Rdb_CryptoParam实例的指针。 |
| int32_t algo | 表示KDF算法。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 如果执行成功，返回RDB_OK。 如果输入参数无效，返回RDB_E_INVALID_ARGS。 |

**OH_Crypto_SetCryptoPageSize()**

```ets
int OH_Crypto_SetCryptoPageSize(OH_Rdb_CryptoParam *param, int64_t size)
```

描述

设置打开加密数据库时使用的页大小。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Rdb_CryptoParam *param | 表示指向OH_Rdb_CryptoParam实例的指针。 |
| int64_t size | 表示页大小，单位为字节，取值应为2的幂值，最小值为1024，最大值65536。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int | 返回执行结果。 如果执行成功，返回RDB_OK。 如果输入参数无效，返回RDB_E_INVALID_ARGS。 |