# crypto_kdf.h

#### 概述

定义密钥派生接口。

**引用文件：** <CryptoArchitectureKit/crypto_kdf.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：**[CryptoKdfApi](../../topics/networking/CryptoKdfApi.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_CryptoKdf](../../topics/misc/OH_CryptoKdf.md)OH_CryptoKdf定义密钥派生函数（KDF）结构。[OH_CryptoKdfParams](../../topics/media/OH_CryptoKdfParams.md)OH_CryptoKdfParams定义密钥派生函数（KDF）参数结构。

#### 枚举

名称typedef关键字描述[CryptoKdf_ParamType](#ZH-CN_TOPIC_0000002497605358__cryptokdf_paramtype)CryptoKdf_ParamType定义密钥派生函数（KDF）参数类型。

#### 函数

名称描述[OH_Crypto_ErrCode OH_CryptoKdfParams_Create(const char *algoName, OH_CryptoKdfParams **params)](#ZH-CN_TOPIC_0000002497605358__oh_cryptokdfparams_create)创建密钥派生函数（KDF）参数。[OH_Crypto_ErrCode OH_CryptoKdfParams_SetParam(OH_CryptoKdfParams *params, CryptoKdf_ParamType type, Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497605358__oh_cryptokdfparams_setparam)设置密钥派生函数（KDF）参数。[void OH_CryptoKdfParams_Destroy(OH_CryptoKdfParams *params)](#ZH-CN_TOPIC_0000002497605358__oh_cryptokdfparams_destroy)销毁密钥派生函数（KDF）参数。[OH_Crypto_ErrCode OH_CryptoKdf_Create(const char *algoName, OH_CryptoKdf **ctx)](#ZH-CN_TOPIC_0000002497605358__oh_cryptokdf_create)创建密钥派生函数（KDF）实例。[OH_Crypto_ErrCode OH_CryptoKdf_Derive(OH_CryptoKdf *ctx, const OH_CryptoKdfParams *params, int keyLen,Crypto_DataBlob *key)](#ZH-CN_TOPIC_0000002497605358__oh_cryptokdf_derive)派生密钥。[void OH_CryptoKdf_Destroy(OH_CryptoKdf *ctx)](#ZH-CN_TOPIC_0000002497605358__oh_cryptokdf_destroy)销毁密钥派生函数（KDF）实例。

#### 枚举类型说明

#### CryptoKdf_ParamType

```ets
enum CryptoKdf_ParamType
```

**描述**

定义密钥派生函数（KDF）参数类型。

**起始版本：** 20

枚举项描述CRYPTO_KDF_KEY_DATABLOB = 0表示KDF的密钥或密码。CRYPTO_KDF_SALT_DATABLOB = 1表示KDF的盐值。CRYPTO_KDF_INFO_DATABLOB = 2表示KDF的信息。CRYPTO_KDF_ITER_COUNT_INT = 3表示PBKDF2的迭代次数。CRYPTO_KDF_SCRYPT_N_UINT64 = 4表示SCRYPT KDF的n参数。CRYPTO_KDF_SCRYPT_R_UINT64 = 5表示SCRYPT KDF的r参数。CRYPTO_KDF_SCRYPT_P_UINT64 = 6表示SCRYPT KDF的p参数。CRYPTO_KDF_SCRYPT_MAX_MEM_UINT64 = 7表示SCRYPT KDF的最大内存使用量。

#### 函数说明

#### OH_CryptoKdfParams_Create()

```ets
OH_Crypto_ErrCode OH_CryptoKdfParams_Create(const char *algoName, OH_CryptoKdfParams **params)
```

**描述**

创建密钥派生函数（KDF）参数。

**起始版本：** 20

**参数：**

参数项描述const char *algoName

KDF算法名称。

 例如"HKDF|SHA384|EXTRACT_AND_EXPAND"、"PBKDF2|SHA384"。

[OH_CryptoKdfParams](../../topics/media/OH_CryptoKdfParams.md) **paramsKDF参数。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoKdfParams_SetParam()

```ets
OH_Crypto_ErrCode OH_CryptoKdfParams_SetParam(OH_CryptoKdfParams *params, CryptoKdf_ParamType type,Crypto_DataBlob *value)
```

**描述**

设置密钥派生函数（KDF）参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoKdfParams](../../topics/media/OH_CryptoKdfParams.md) *paramsKDF参数。[CryptoKdf_ParamType](#ZH-CN_TOPIC_0000002497605358__cryptokdf_paramtype) typeKDF参数类型。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *valueKDF参数值。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoKdfParams_Destroy()

```ets
void OH_CryptoKdfParams_Destroy(OH_CryptoKdfParams *params)
```

**描述**

销毁密钥派生函数（KDF）参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoKdfParams](../../topics/media/OH_CryptoKdfParams.md) *paramsKDF参数。

#### OH_CryptoKdf_Create()

```ets
OH_Crypto_ErrCode OH_CryptoKdf_Create(const char *algoName, OH_CryptoKdf **ctx)
```

**描述**

创建密钥派生函数（KDF）实例。

**起始版本：** 20

**参数：**

参数项描述const char *algoNameKDF算法名称。[OH_CryptoKdf](../../topics/misc/OH_CryptoKdf.md) **ctxKDF实例。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoKdf_Derive()

```ets
OH_Crypto_ErrCode OH_CryptoKdf_Derive(OH_CryptoKdf *ctx, const OH_CryptoKdfParams *params, int keyLen,Crypto_DataBlob *key)
```

**描述**

派生密钥。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoKdf](../../topics/misc/OH_CryptoKdf.md) *ctxKDF实例。[const OH_CryptoKdfParams](../../topics/media/OH_CryptoKdfParams.md) *paramsKDF参数。int keyLen密钥派生长度。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *key派生出的密钥。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoKdf_Destroy()

```ets
void OH_CryptoKdf_Destroy(OH_CryptoKdf *ctx)
```

**描述**

销毁密钥派生函数（KDF）实例。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoKdf](../../topics/misc/OH_CryptoKdf.md) *ctxKDF实例。