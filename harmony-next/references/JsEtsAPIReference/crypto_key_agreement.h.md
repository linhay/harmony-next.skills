# crypto_key_agreement.h

#### 概述

定义密钥协商接口。

**引用文件：** <CryptoArchitectureKit/crypto_key_agreement.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 20

**相关模块：**[CryptoKeyAgreementApi](CryptoKeyAgreementApi.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_CryptoKeyAgreement](OH_CryptoKeyAgreement.md)OH_CryptoKeyAgreement定义密钥协商结构。

#### 函数

名称描述[OH_Crypto_ErrCode OH_CryptoKeyAgreement_Create(const char *algoName, OH_CryptoKeyAgreement **ctx)](#ZH-CN_TOPIC_0000002497445380__oh_cryptokeyagreement_create)根据给定的算法名称创建密钥协商实例。[OH_Crypto_ErrCode OH_CryptoKeyAgreement_GenerateSecret(OH_CryptoKeyAgreement *ctx, OH_CryptoPrivKey *privkey, OH_CryptoPubKey *pubkey, Crypto_DataBlob *secret)](#ZH-CN_TOPIC_0000002497445380__oh_cryptokeyagreement_generatesecret)生成密钥协商的秘密值。[void OH_CryptoKeyAgreement_Destroy(OH_CryptoKeyAgreement *ctx)](#ZH-CN_TOPIC_0000002497445380__oh_cryptokeyagreement_destroy)销毁密钥协商实例。

#### 函数说明

#### OH_CryptoKeyAgreement_Create()

```ets
OH_Crypto_ErrCode OH_CryptoKeyAgreement_Create(const char *algoName, OH_CryptoKeyAgreement **ctx)
```

**描述**

根据给定的算法名称创建密钥协商实例。

**起始版本：** 20

**参数：**

参数项描述const char *algoName

用于生成密钥协商实例的算法名称。

 例如"ECC"、"X25519"。

[OH_CryptoKeyAgreement](OH_CryptoKeyAgreement.md) **ctx密钥协商实例。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoKeyAgreement_GenerateSecret()

```ets
OH_Crypto_ErrCode OH_CryptoKeyAgreement_GenerateSecret(OH_CryptoKeyAgreement *ctx, OH_CryptoPrivKey *privkey,OH_CryptoPubKey *pubkey, Crypto_DataBlob *secret)
```

**描述**

生成密钥协商的秘密值。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoKeyAgreement](OH_CryptoKeyAgreement.md) *ctx密钥协商实例。[OH_CryptoPrivKey](OH_CryptoPrivKey.md) *privkey私钥。[OH_CryptoPubKey](OH_CryptoPubKey.md) *pubkey公钥。[Crypto_DataBlob](Crypto_DataBlob.md) *secret秘密值。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoKeyAgreement_Destroy()

```ets
void OH_CryptoKeyAgreement_Destroy(OH_CryptoKeyAgreement *ctx)
```

**描述**

销毁密钥协商实例。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoKeyAgreement](OH_CryptoKeyAgreement.md) *ctx密钥协商实例。