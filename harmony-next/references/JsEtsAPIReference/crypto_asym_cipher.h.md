# crypto_asym_cipher.h

#### 概述

定义非对称密钥加密API。

**引用文件：** <CryptoArchitectureKit/crypto_asym_cipher.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：**[CryptoAsymCipherApi](CryptoAsymCipherApi.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_CryptoAsymCipher](OH_CryptoAsymCipher.md)OH_CryptoAsymCipher定义非对称加密结构。[OH_CryptoSm2CiphertextSpec](OH_CryptoSm2CiphertextSpec.md)OH_CryptoSm2CiphertextSpec定义SM2密文规格结构。

#### 枚举

名称typedef关键字描述[CryptoSm2CiphertextSpec_item](#ZH-CN_TOPIC_0000002497605356__cryptosm2ciphertextspec_item)CryptoSm2CiphertextSpec_item定义SM2密文规格项类型。

#### 函数

名称描述[OH_Crypto_ErrCode OH_CryptoAsymCipher_Create(const char *algoName, OH_CryptoAsymCipher **ctx)](#ZH-CN_TOPIC_0000002497605356__oh_cryptoasymcipher_create)根据给定的算法名称创建非对称加密。[OH_Crypto_ErrCode OH_CryptoAsymCipher_Init(OH_CryptoAsymCipher *ctx, Crypto_CipherMode mode, OH_CryptoKeyPair *key)](#ZH-CN_TOPIC_0000002497605356__oh_cryptoasymcipher_init)初始化非对称加密。[OH_Crypto_ErrCode OH_CryptoAsymCipher_Final(OH_CryptoAsymCipher *ctx, const Crypto_DataBlob *in, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002497605356__oh_cryptoasymcipher_final)完成非对称加密。[void OH_CryptoAsymCipher_Destroy(OH_CryptoAsymCipher *ctx)](#ZH-CN_TOPIC_0000002497605356__oh_cryptoasymcipher_destroy)销毁非对称加密上下文。[OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_Create(Crypto_DataBlob *sm2Ciphertext, OH_CryptoSm2CiphertextSpec **spec)](#ZH-CN_TOPIC_0000002497605356__oh_cryptosm2ciphertextspec_create)创建SM2密文规格。[OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_GetItem(OH_CryptoSm2CiphertextSpec *spec, CryptoSm2CiphertextSpec_item item, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002497605356__oh_cryptosm2ciphertextspec_getitem)获取SM2密文规格中的指定项。[OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_SetItem(OH_CryptoSm2CiphertextSpec *spec, CryptoSm2CiphertextSpec_item item, Crypto_DataBlob *in)](#ZH-CN_TOPIC_0000002497605356__oh_cryptosm2ciphertextspec_setitem)设置SM2密文规格中的指定项。[OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_Encode(OH_CryptoSm2CiphertextSpec *spec, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002497605356__oh_cryptosm2ciphertextspec_encode)将SM2密文规格编码为DER格式密文。[void OH_CryptoSm2CiphertextSpec_Destroy(OH_CryptoSm2CiphertextSpec *spec)](#ZH-CN_TOPIC_0000002497605356__oh_cryptosm2ciphertextspec_destroy)销毁SM2密文规格。

#### 枚举类型说明

#### CryptoSm2CiphertextSpec_item

```ets
enum CryptoSm2CiphertextSpec_item
```

**描述**

定义SM2密文规格项类型。

**起始版本：** 20

枚举项描述CRYPTO_SM2_CIPHERTEXT_C1_X = 0公钥x，也称为C1x。CRYPTO_SM2_CIPHERTEXT_C1_Y = 1公钥y，也称为C1y。CRYPTO_SM2_CIPHERTEXT_C2 = 2哈希值，也称为C2。CRYPTO_SM2_CIPHERTEXT_C3 = 3密文数据，也称为C3。

#### 函数说明

#### OH_CryptoAsymCipher_Create()

```ets
OH_Crypto_ErrCode OH_CryptoAsymCipher_Create(const char *algoName, OH_CryptoAsymCipher **ctx)
```

**描述**

根据给定的算法名称创建非对称加密。

**起始版本：** 20

**参数：**

参数项描述const char *algoName

用于生成加密的算法名称。

例如"RSA|PKCS1_OAEP|SHA384|MGF1_SHA384", "SM2|SM3"。

[OH_CryptoAsymCipher](OH_CryptoAsymCipher.md) **ctx指向非对称加密上下文的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymCipher_Init()

```ets
OH_Crypto_ErrCode OH_CryptoAsymCipher_Init(OH_CryptoAsymCipher *ctx, Crypto_CipherMode mode, OH_CryptoKeyPair *key)
```

**描述**

初始化非对称加密。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoAsymCipher](OH_CryptoAsymCipher.md) *ctx非对称加密上下文。[Crypto_CipherMode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__crypto_ciphermode) mode加密模式是加密还是解密。[OH_CryptoKeyPair](OH_CryptoKeyPair.md) *key非对称密钥。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoAsymCipher_Final](#ZH-CN_TOPIC_0000002497605356__oh_cryptoasymcipher_final)

#### OH_CryptoAsymCipher_Final()

```ets
OH_Crypto_ErrCode OH_CryptoAsymCipher_Final(OH_CryptoAsymCipher *ctx, const Crypto_DataBlob *in,Crypto_DataBlob *out)
```

**描述**

完成非对称加密。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoAsymCipher](OH_CryptoAsymCipher.md) *ctx非对称加密上下文。[const Crypto_DataBlob](Crypto_DataBlob.md) *in要加密或解密的数据。[Crypto_DataBlob](Crypto_DataBlob.md) *out最终加密或解密的数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoAsymCipher_Init](#ZH-CN_TOPIC_0000002497605356__oh_cryptoasymcipher_init)

#### OH_CryptoAsymCipher_Destroy()

```ets
void OH_CryptoAsymCipher_Destroy(OH_CryptoAsymCipher *ctx)
```

**描述**

销毁非对称加密上下文。

**参数：**

参数项描述[OH_CryptoAsymCipher](OH_CryptoAsymCipher.md) *ctx非对称加密上下文。

#### OH_CryptoSm2CiphertextSpec_Create()

```ets
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_Create(Crypto_DataBlob *sm2Ciphertext, OH_CryptoSm2CiphertextSpec **spec)
```

**描述**

创建SM2密文规格。

**起始版本：** 20

**参数：**

参数项描述[Crypto_DataBlob](Crypto_DataBlob.md) *sm2CiphertextSM2密文DER格式数据，如果为NULL则创建空的SM2密文规格。[OH_CryptoSm2CiphertextSpec](OH_CryptoSm2CiphertextSpec.md) **spec输出的SM2密文规格。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSm2CiphertextSpec_GetItem()

```ets
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_GetItem(OH_CryptoSm2CiphertextSpec *spec,CryptoSm2CiphertextSpec_item item, Crypto_DataBlob *out)
```

**描述**

获取SM2密文规格中的指定项。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSm2CiphertextSpec](OH_CryptoSm2CiphertextSpec.md) *specSM2密文规格。[CryptoSm2CiphertextSpec_item](#ZH-CN_TOPIC_0000002497605356__cryptosm2ciphertextspec_item) itemSM2密文规格项。[Crypto_DataBlob](zh-cn_topic_0000002497605362.html) *out输出数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSm2CiphertextSpec_SetItem()

```ets
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_SetItem(OH_CryptoSm2CiphertextSpec *spec,CryptoSm2CiphertextSpec_item item, Crypto_DataBlob *in)
```

**描述**

设置SM2密文规格中的指定项。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSm2CiphertextSpec](OH_CryptoSm2CiphertextSpec.md) *specSM2密文规格。[CryptoSm2CiphertextSpec_item](#ZH-CN_TOPIC_0000002497605356__cryptosm2ciphertextspec_item) itemSM2密文规格项。[Crypto_DataBlob](zh-cn_topic_0000002497605362.html) *in输入数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSm2CiphertextSpec_Encode()

```ets
OH_Crypto_ErrCode OH_CryptoSm2CiphertextSpec_Encode(OH_CryptoSm2CiphertextSpec *spec, Crypto_DataBlob *out)
```

**描述**

将SM2密文规格编码为DER格式密文。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSm2CiphertextSpec](OH_CryptoSm2CiphertextSpec.md) *specSM2密文规格。[Crypto_DataBlob](Crypto_DataBlob.md) *out输出数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoSm2CiphertextSpec_Destroy()

```ets
void OH_CryptoSm2CiphertextSpec_Destroy(OH_CryptoSm2CiphertextSpec *spec)
```

**描述**

销毁SM2密文规格。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSm2CiphertextSpec](OH_CryptoSm2CiphertextSpec.md) *specSM2密文规格。