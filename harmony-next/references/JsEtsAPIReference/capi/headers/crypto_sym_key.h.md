# crypto_sym_key.h

#### 概述

定义对称密钥接口。

**引用文件：** <CryptoArchitectureKit/crypto_sym_key.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：**[CryptoSymKeyApi](../../topics/networking/CryptoSymKeyApi.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_CryptoSymKey](../../topics/misc/OH_CryptoSymKey.md)OH_CryptoSymKey定义对称密钥生成器结构。[OH_CryptoSymKeyGenerator](../../topics/misc/OH_CryptoSymKeyGenerator.md)OH_CryptoSymKeyGenerator定义对称密钥结构。

#### 函数

名称描述[OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Create(const char *algoName, OH_CryptoSymKeyGenerator **ctx)](#ZH-CN_TOPIC_0000002529285353__oh_cryptosymkeygenerator_create)根据给定的算法名称创建对称密钥生成器。[OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Generate(OH_CryptoSymKeyGenerator *ctx, OH_CryptoSymKey **keyCtx)](#ZH-CN_TOPIC_0000002529285353__oh_cryptosymkeygenerator_generate)随机生成对称密钥。[OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Convert(OH_CryptoSymKeyGenerator *ctx, const Crypto_DataBlob *keyData, OH_CryptoSymKey **keyCtx)](#ZH-CN_TOPIC_0000002529285353__oh_cryptosymkeygenerator_convert)将对称密钥数据转换为对称密钥。[const char *OH_CryptoSymKeyGenerator_GetAlgoName(OH_CryptoSymKeyGenerator *ctx)](#ZH-CN_TOPIC_0000002529285353__oh_cryptosymkeygenerator_getalgoname)获取对称密钥生成器的算法名称。[void OH_CryptoSymKeyGenerator_Destroy(OH_CryptoSymKeyGenerator *ctx)](#ZH-CN_TOPIC_0000002529285353__oh_cryptosymkeygenerator_destroy)销毁对称密钥生成器。[const char *OH_CryptoSymKey_GetAlgoName(OH_CryptoSymKey *keyCtx)](#ZH-CN_TOPIC_0000002529285353__oh_cryptosymkey_getalgoname)从对称密钥获取对称密钥算法名称。[OH_Crypto_ErrCode OH_CryptoSymKey_GetKeyData(OH_CryptoSymKey *keyCtx, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002529285353__oh_cryptosymkey_getkeydata)从密钥实例获取对称密钥数据。[void OH_CryptoSymKey_Destroy(OH_CryptoSymKey *keyCtx)](#ZH-CN_TOPIC_0000002529285353__oh_cryptosymkey_destroy)销毁对称密钥实例。

#### 函数说明

#### OH_CryptoSymKeyGenerator_Create()

```ets
OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Create(const char *algoName, OH_CryptoSymKeyGenerator **ctx)
```

**描述**

根据给定的算法名称创建对称密钥生成器。

**起始版本：** 12

**参数：**

参数项描述const char *algoName

用于生成生成器的算法名称。

 例如"AES256"、"AES128"、"SM4"等。

[OH_CryptoSymKeyGenerator](../../topics/misc/OH_CryptoSymKeyGenerator.md) **ctx指向对称密钥生成器实例的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSymKeyGenerator_Generate()

```ets
OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Generate(OH_CryptoSymKeyGenerator *ctx, OH_CryptoSymKey **keyCtx)
```

**描述**

随机生成对称密钥。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymKeyGenerator](../../topics/misc/OH_CryptoSymKeyGenerator.md) *ctx指向对称密钥生成器实例。[OH_CryptoSymKey](../../topics/misc/OH_CryptoSymKey.md) **keyCtx指向对称密钥的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSymKeyGenerator_Convert()

```ets
OH_Crypto_ErrCode OH_CryptoSymKeyGenerator_Convert(OH_CryptoSymKeyGenerator *ctx,const Crypto_DataBlob *keyData, OH_CryptoSymKey **keyCtx)
```

**描述**

将对称密钥数据转换为对称密钥。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymKeyGenerator](../../topics/misc/OH_CryptoSymKeyGenerator.md) *ctx指向对称密钥生成器实例。[const Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *keyData指向生成对称密钥的数据。[OH_CryptoSymKey](../../topics/misc/OH_CryptoSymKey.md) **keyCtx指向对称密钥实例的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSymKeyGenerator_GetAlgoName()

```ets
const char *OH_CryptoSymKeyGenerator_GetAlgoName(OH_CryptoSymKeyGenerator *ctx)
```

**描述**

获取对称密钥生成器的算法名称。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymKeyGenerator](../../topics/misc/OH_CryptoSymKeyGenerator.md) *ctx指向对称密钥生成器实例的指针。

**返回：**

类型说明const char *返回对称密钥生成器算法名称。

#### OH_CryptoSymKeyGenerator_Destroy()

```ets
void OH_CryptoSymKeyGenerator_Destroy(OH_CryptoSymKeyGenerator *ctx)
```

**描述**

销毁对称密钥生成器。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymKeyGenerator](../../topics/misc/OH_CryptoSymKeyGenerator.md) *ctx指向对称密钥生成器实例的指针。

#### OH_CryptoSymKey_GetAlgoName()

```ets
const char *OH_CryptoSymKey_GetAlgoName(OH_CryptoSymKey *keyCtx)
```

**描述**

从对称密钥获取对称密钥算法名称。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymKey](../../topics/misc/OH_CryptoSymKey.md) *keyCtx指向对称密钥实例。

**返回：**

类型说明const char *返回对称密钥算法名称。

#### OH_CryptoSymKey_GetKeyData()

```ets
OH_Crypto_ErrCode OH_CryptoSymKey_GetKeyData(OH_CryptoSymKey *keyCtx, Crypto_DataBlob *out)
```

**描述**

从密钥实例获取对称密钥数据。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymKey](../../topics/misc/OH_CryptoSymKey.md) *keyCtx指向对称密钥实例。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *out获取到的结果。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSymKey_Destroy()

```ets
void OH_CryptoSymKey_Destroy(OH_CryptoSymKey *keyCtx)
```

**描述**

销毁对称密钥实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoSymKey](../../topics/misc/OH_CryptoSymKey.md) *keyCtx指向对称密钥实例。