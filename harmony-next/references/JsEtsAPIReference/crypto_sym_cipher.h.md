# crypto_sym_cipher.h

#### 概述

定义对称密钥加密API。

**引用文件：** <CryptoArchitectureKit/crypto_sym_cipher.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：**[CryptoSymCipherApi](CryptoSymCipherApi.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_CryptoSymCipher](OH_CryptoSymCipher.md)OH_CryptoSymCipher定义对称加解密结构体。[OH_CryptoSymCipherParams](OH_CryptoSymCipherParams.md)OH_CryptoSymCipherParams定义对称加解密参数结构体。

#### 枚举

名称typedef关键字描述[CryptoSymCipher_ParamsType](#ZH-CN_TOPIC_0000002497445382__cryptosymcipher_paramstype)CryptoSymCipher_ParamsType定义对称加解密参数类型。

#### 函数

名称描述[OH_Crypto_ErrCode OH_CryptoSymCipherParams_Create(OH_CryptoSymCipherParams **params)](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipherparams_create)创建对称密钥加解密参数实例。[OH_Crypto_ErrCode OH_CryptoSymCipherParams_SetParam(OH_CryptoSymCipherParams *params, CryptoSymCipher_ParamsType paramsType, Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipherparams_setparam)设置对称密钥加解密参数。[void OH_CryptoSymCipherParams_Destroy(OH_CryptoSymCipherParams *params)](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipherparams_destroy)销毁对称密钥加解密参数实例。[OH_Crypto_ErrCode OH_CryptoSymCipher_Create(const char *algoName, OH_CryptoSymCipher **ctx)](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_create)根据给定的算法名称创建对称密钥加解密实例。[OH_Crypto_ErrCode OH_CryptoSymCipher_Init(OH_CryptoSymCipher *ctx, Crypto_CipherMode mod, OH_CryptoSymKey *key, OH_CryptoSymCipherParams *params)](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_init)初始化对称密钥加解密实例。[OH_Crypto_ErrCode OH_CryptoSymCipher_Update(OH_CryptoSymCipher *ctx, Crypto_DataBlob *in, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_update)更新加密或者解密数据操作。[OH_Crypto_ErrCode OH_CryptoSymCipher_Final(OH_CryptoSymCipher *ctx, Crypto_DataBlob *in, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_final)输出加/解密（分组模式产生的）剩余数据，最后结束加密或者解密数据操作。[const char *OH_CryptoSymCipher_GetAlgoName(OH_CryptoSymCipher *ctx)](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_getalgoname)获取对称密钥加解密实例的算法名称。[void OH_CryptoSymCipher_Destroy(OH_CryptoSymCipher *ctx)](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_destroy)销毁对称密钥加解密实例。

#### 枚举类型说明

#### CryptoSymCipher_ParamsType

```ets
enum CryptoSymCipher_ParamsType
```

**描述**

定义对称加解密参数类型。

**起始版本：** 12

枚举项描述CRYPTO_IV_DATABLOB = 100表示iv等参数。CRYPTO_AAD_DATABLOB = 101表示GCM模式下的附加认证数据。CRYPTO_TAG_DATABLOB = 102表示加密操作的输出标签,用于完整性检查。

#### 函数说明

#### OH_CryptoSymCipherParams_Create()

```ets
OH_Crypto_ErrCode OH_CryptoSymCipherParams_Create(OH_CryptoSymCipherParams **params)
```

**描述**

创建对称密钥加解密参数实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymCipherParams](OH_CryptoSymCipherParams.md) **params指向对称加解密参数实例的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSymCipherParams_SetParam()

```ets
OH_Crypto_ErrCode OH_CryptoSymCipherParams_SetParam(OH_CryptoSymCipherParams *params,CryptoSymCipher_ParamsType paramsType, Crypto_DataBlob *value)
```

**描述**

设置对称密钥加解密参数。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymCipherParams](OH_CryptoSymCipherParams.md) *params指向对称密钥加解密参数实例。[CryptoSymCipher_ParamsType](#ZH-CN_TOPIC_0000002497445382__cryptosymcipher_paramstype) paramsType设置对称密钥加解密参数类型。[Crypto_DataBlob](zh-cn_topic_0000002497605362.html) *value设置的参数值。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSymCipherParams_Destroy()

```ets
void OH_CryptoSymCipherParams_Destroy(OH_CryptoSymCipherParams *params)
```

**描述**

销毁对称密钥加解密参数实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymCipherParams](OH_CryptoSymCipherParams.md) *params指向对称密钥加解密参数实例。

#### OH_CryptoSymCipher_Create()

```ets
OH_Crypto_ErrCode OH_CryptoSymCipher_Create(const char *algoName, OH_CryptoSymCipher **ctx)
```

**描述**

根据给定的算法名称创建对称密钥加解密实例。

**起始版本：** 12

**参数：**

参数项描述const char *algoName

用于生成加密实例的算法名称。

 例如"AES128|GCM|PKCS7"。

[OH_CryptoSymCipher](OH_CryptoSymCipher.md) **ctx指向对称密钥加密实例的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSymCipher_Init()

```ets
OH_Crypto_ErrCode OH_CryptoSymCipher_Init(OH_CryptoSymCipher *ctx, Crypto_CipherMode mod,OH_CryptoSymKey *key, OH_CryptoSymCipherParams *params)
```

**描述**

初始化对称密钥加解密实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymCipher](OH_CryptoSymCipher.md) *ctx对称密钥加密实例。[Crypto_CipherMode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__crypto_ciphermode) mod加解密模式。[OH_CryptoSymKey](OH_CryptoSymKey.md) *key对称密钥。[OH_CryptoSymCipherParams](OH_CryptoSymCipherParams.md) *params指向对称密钥参数实例。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoSymCipher_Update](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_update)

[OH_CryptoSymCipher_Final](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_final)

#### OH_CryptoSymCipher_Update()

```ets
OH_Crypto_ErrCode OH_CryptoSymCipher_Update(OH_CryptoSymCipher *ctx, Crypto_DataBlob *in, Crypto_DataBlob *out)
```

**描述**

更新加密或者解密数据操作。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymCipher](OH_CryptoSymCipher.md) *ctx指向对称密钥加解密实例。[Crypto_DataBlob](Crypto_DataBlob.md) *in加密或者解密的数据。[Crypto_DataBlob](Crypto_DataBlob.md) *out更新的结果。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoSymCipher_Init](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_init)

[OH_CryptoSymCipher_Final](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_final)

#### OH_CryptoSymCipher_Final()

```ets
OH_Crypto_ErrCode OH_CryptoSymCipher_Final(OH_CryptoSymCipher *ctx, Crypto_DataBlob *in, Crypto_DataBlob *out)
```

**描述**

输出加/解密（分组模式产生的）剩余数据，最后结束加密或者解密数据操作。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymCipher](OH_CryptoSymCipher.md) *ctx对称密钥加密实例。[Crypto_DataBlob](Crypto_DataBlob.md) *in要加密或解密的数据。[Crypto_DataBlob](Crypto_DataBlob.md) *out返回剩余数据的加/解密结果。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoSymCipher_Init](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_init)

[OH_CryptoSymCipher_Update](#ZH-CN_TOPIC_0000002497445382__oh_cryptosymcipher_update)

#### OH_CryptoSymCipher_GetAlgoName()

```ets
const char *OH_CryptoSymCipher_GetAlgoName(OH_CryptoSymCipher *ctx)
```

**描述**

获取对称密钥加解密实例的算法名称。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymCipher](OH_CryptoSymCipher.md) *ctx指向对称密钥加解密实例。

**返回：**

类型说明const char *返回对称密钥加密算法名称。

#### OH_CryptoSymCipher_Destroy()

```ets
void OH_CryptoSymCipher_Destroy(OH_CryptoSymCipher *ctx)
```

**描述**

销毁对称密钥加解密实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymCipher](OH_CryptoSymCipher.md) *ctx指向对称密钥加解密实例。