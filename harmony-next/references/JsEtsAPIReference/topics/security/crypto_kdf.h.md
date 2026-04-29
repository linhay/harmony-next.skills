# crypto_kdf.h

**概述**

定义密钥派生接口。

引用文件： <CryptoArchitectureKit/crypto_kdf.h>

库： libohcrypto.so

系统能力： SystemCapability.Security.CryptoFramework

起始版本： 20

相关模块： [CryptoKdfApi](CryptoKdfApi.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_CryptoKdf | OH_CryptoKdf | 定义密钥派生函数（KDF）结构。 |
| OH_CryptoKdfParams | OH_CryptoKdfParams | 定义密钥派生函数（KDF）参数结构。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| CryptoKdf_ParamType | CryptoKdf_ParamType | 定义密钥派生函数（KDF）参数类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Crypto_ErrCode OH_CryptoKdfParams_Create(const char *algoName, OH_CryptoKdfParams **params) | 创建密钥派生函数（KDF）参数。  注意：创建的资源必须通过OH_CryptoKdfParams_Destroy销毁。 |
| OH_Crypto_ErrCode OH_CryptoKdfParams_SetParam(OH_CryptoKdfParams *params, CryptoKdf_ParamType type, Crypto_DataBlob *value) | 设置密钥派生函数（KDF）参数。 |
| void OH_CryptoKdfParams_Destroy(OH_CryptoKdfParams *params) | 销毁密钥派生函数（KDF）参数。 |
| OH_Crypto_ErrCode OH_CryptoKdf_Create(const char *algoName, OH_CryptoKdf **ctx) | 创建密钥派生函数（KDF）实例。  注意：创建的资源必须通过OH_CryptoKdf_Destroy销毁。 |
| OH_Crypto_ErrCode OH_CryptoKdf_Derive(OH_CryptoKdf *ctx, const OH_CryptoKdfParams *params, int keyLen, Crypto_DataBlob *key) | 派生密钥。  注意：使用完成后必须通过OH_Crypto_FreeDataBlob释放key内存。 |
| void OH_CryptoKdf_Destroy(OH_CryptoKdf *ctx) | 销毁密钥派生函数（KDF）实例。 |

**枚举类型说明**

**CryptoKdf_ParamType**

```ets
enum CryptoKdf_ParamType
```

描述

定义密钥派生函数（KDF）参数类型。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| CRYPTO_KDF_KEY_DATABLOB = 0 | 表示KDF的密钥或密码。 |
| CRYPTO_KDF_SALT_DATABLOB = 1 | 表示KDF的盐值。 |
| CRYPTO_KDF_INFO_DATABLOB = 2 | 表示KDF的信息。 |
| CRYPTO_KDF_ITER_COUNT_INT = 3 | 表示PBKDF2的迭代次数。 |
| CRYPTO_KDF_SCRYPT_N_UINT64 = 4 | 表示SCRYPT KDF的n参数。 |
| CRYPTO_KDF_SCRYPT_R_UINT64 = 5 | 表示SCRYPT KDF的r参数。 |
| CRYPTO_KDF_SCRYPT_P_UINT64 = 6 | 表示SCRYPT KDF的p参数。 |
| CRYPTO_KDF_SCRYPT_MAX_MEM_UINT64 = 7 | 表示SCRYPT KDF的最大内存使用量。 |

**函数说明**

**OH_CryptoKdfParams_Create()**

```ets
OH_Crypto_ErrCode OH_CryptoKdfParams_Create(const char *algoName, OH_CryptoKdfParams **params)
```

描述

创建密钥派生函数（KDF）参数。

 注意：创建的资源必须通过[OH_CryptoKdfParams_Destroy](crypto_kdf.h.md#ZH-CN_TOPIC_0000002522241336__oh_cryptokdfparams_destroy)销毁。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *algoName | KDF算法名称。  例如"HKDF|SHA384|EXTRACT_AND_EXPAND"、"PBKDF2|SHA384"。 |
| OH_CryptoKdfParams **params | KDF参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。  CRYPTO_NOT_SUPPORTED：操作不支持。  CRYPTO_MEMORY_ERROR：内存错误。  CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。  CRYPTO_OPERTION_ERROR：调用三方算法库API出错。 |

**OH_CryptoKdfParams_SetParam()**

```ets
OH_Crypto_ErrCode OH_CryptoKdfParams_SetParam(OH_CryptoKdfParams *params, CryptoKdf_ParamType type, Crypto_DataBlob *value)
```

描述

设置密钥派生函数（KDF）参数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_CryptoKdfParams *params | KDF参数。 |
| CryptoKdf_ParamType type | KDF参数类型。 |
| Crypto_DataBlob *value | KDF参数值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。  CRYPTO_NOT_SUPPORTED：操作不支持。  CRYPTO_MEMORY_ERROR：内存错误。  CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。  CRYPTO_OPERTION_ERROR：调用三方算法库API出错。 |

**OH_CryptoKdfParams_Destroy()**

```ets
void OH_CryptoKdfParams_Destroy(OH_CryptoKdfParams *params)
```

描述

销毁密钥派生函数（KDF）参数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_CryptoKdfParams *params | KDF参数。 |

**OH_CryptoKdf_Create()**

```ets
OH_Crypto_ErrCode OH_CryptoKdf_Create(const char *algoName, OH_CryptoKdf **ctx)
```

描述

创建密钥派生函数（KDF）实例。

 注意：创建的资源必须通过[OH_CryptoKdf_Destroy](crypto_kdf.h.md#ZH-CN_TOPIC_0000002522241336__oh_cryptokdf_destroy)销毁。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *algoName | KDF算法名称。 |
| OH_CryptoKdf **ctx | KDF实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。  CRYPTO_NOT_SUPPORTED：操作不支持。  CRYPTO_MEMORY_ERROR：内存错误。  CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。  CRYPTO_OPERTION_ERROR：调用三方算法库API出错。 |

**OH_CryptoKdf_Derive()**

```ets
OH_Crypto_ErrCode OH_CryptoKdf_Derive(OH_CryptoKdf *ctx, const OH_CryptoKdfParams *params, int keyLen, Crypto_DataBlob *key)
```

描述

派生密钥。

 注意：使用完成后必须通过[OH_Crypto_FreeDataBlob](crypto_common.h.md#ZH-CN_TOPIC_0000002522081340__oh_crypto_freedatablob)释放key内存。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_CryptoKdf *ctx | KDF实例。 |
| const OH_CryptoKdfParams *params | KDF参数。 |
| int keyLen | 密钥派生长度。 |
| Crypto_DataBlob *key | 派生出的密钥。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。  CRYPTO_NOT_SUPPORTED：操作不支持。  CRYPTO_MEMORY_ERROR：内存错误。  CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。  CRYPTO_OPERTION_ERROR：调用三方算法库API出错。 |

**OH_CryptoKdf_Destroy()**

```ets
void OH_CryptoKdf_Destroy(OH_CryptoKdf *ctx)
```

描述

销毁密钥派生函数（KDF）实例。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_CryptoKdf *ctx | KDF实例。 |