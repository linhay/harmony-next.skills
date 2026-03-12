# crypto_digest.h

#### 概述

定义摘要算法API。

**引用文件：** <CryptoArchitectureKit/crypto_digest.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：**[CryptoDigestApi](CryptoDigestApi.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_CryptoDigest](OH_CryptoDigest.md)OH_CryptoDigest定义摘要结构体。

#### 函数

名称描述[OH_Crypto_ErrCode OH_CryptoDigest_Create(const char *algoName, OH_CryptoDigest **ctx)](#ZH-CN_TOPIC_0000002529445323__oh_cryptodigest_create)根据给定的算法名称创建一个摘要实例。[OH_Crypto_ErrCode OH_CryptoDigest_Update(OH_CryptoDigest *ctx, Crypto_DataBlob *in)](#ZH-CN_TOPIC_0000002529445323__oh_cryptodigest_update)更新摘要数据。[OH_Crypto_ErrCode OH_CryptoDigest_Final(OH_CryptoDigest *ctx, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002529445323__oh_cryptodigest_final)完成摘要计算。[uint32_t OH_CryptoDigest_GetLength(OH_CryptoDigest *ctx)](#ZH-CN_TOPIC_0000002529445323__oh_cryptodigest_getlength)获取摘要长度。[const char *OH_CryptoDigest_GetAlgoName(OH_CryptoDigest *ctx)](#ZH-CN_TOPIC_0000002529445323__oh_cryptodigest_getalgoname)获取摘要算法名称。[void OH_DigestCrypto_Destroy(OH_CryptoDigest *ctx)](#ZH-CN_TOPIC_0000002529445323__oh_digestcrypto_destroy)销毁摘要实例。

#### 函数说明

#### OH_CryptoDigest_Create()

```ets
OH_Crypto_ErrCode OH_CryptoDigest_Create(const char *algoName, OH_CryptoDigest **ctx)
```

**描述**

根据给定的算法名称创建一个摘要实例。

**起始版本：** 12

**参数：**

参数项描述const char *algoName

用于生成摘要实例的算法名称。

 例如"SHA256"。

[OH_CryptoDigest](OH_CryptoDigest.md) **ctx指向摘要实例的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoDigest_Update()

```ets
OH_Crypto_ErrCode OH_CryptoDigest_Update(OH_CryptoDigest *ctx, Crypto_DataBlob *in)
```

**描述**

更新摘要数据。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoDigest](OH_CryptoDigest.md) *ctx指向摘要实例。[Crypto_DataBlob](Crypto_DataBlob.md) *in传入的消息。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoDigest_Final](crypto_digest.h.md#ZH-CN_TOPIC_0000002529445323__oh_cryptodigest_final)

#### OH_CryptoDigest_Final()

```ets
OH_Crypto_ErrCode OH_CryptoDigest_Final(OH_CryptoDigest *ctx, Crypto_DataBlob *out)
```

**描述**

完成摘要计算。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoDigest](OH_CryptoDigest.md) *ctx指向摘要实例。[Crypto_DataBlob](Crypto_DataBlob.md) *out返回的Md的计算结果。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoDigest_Update](crypto_digest.h.md#ZH-CN_TOPIC_0000002529445323__oh_cryptodigest_update)

#### OH_CryptoDigest_GetLength()

```ets
uint32_t OH_CryptoDigest_GetLength(OH_CryptoDigest *ctx)
```

**描述**

获取摘要长度。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoDigest](OH_CryptoDigest.md) *ctx指向摘要实例。

**返回：**

类型说明uint32_t

返回摘要长度。

 如果输入参数ctx为NULL，则返回401，其他情况下返回0。

#### OH_CryptoDigest_GetAlgoName()

```ets
const char *OH_CryptoDigest_GetAlgoName(OH_CryptoDigest *ctx)
```

**描述**

获取摘要算法名称。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoDigest](OH_CryptoDigest.md) *ctx指向摘要实例。

**返回：**

类型说明const char *返回摘要算法名称。

#### OH_DigestCrypto_Destroy()

```ets
void OH_DigestCrypto_Destroy(OH_CryptoDigest *ctx)
```

**描述**

销毁摘要实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoDigest](OH_CryptoDigest.md) *ctx指向摘要实例。