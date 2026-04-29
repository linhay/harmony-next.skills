# crypto_key_agreement.h

**概述**

定义密钥协商接口。

引用文件： <CryptoArchitectureKit/crypto_key_agreement.h>

库： libohcrypto.so

系统能力： SystemCapability.Security.CryptoFramework

起始版本： 20

相关模块： [CryptoKeyAgreementApi](CryptoKeyAgreementApi.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_CryptoKeyAgreement | OH_CryptoKeyAgreement | 定义密钥协商结构。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| OH_Crypto_ErrCode OH_CryptoKeyAgreement_Create(const char *algoName, OH_CryptoKeyAgreement **ctx) | 根据给定的算法名称创建密钥协商实例。  注意：创建的资源必须通过OH_CryptoKeyAgreement_Destroy销毁。 |
| OH_Crypto_ErrCode OH_CryptoKeyAgreement_GenerateSecret(OH_CryptoKeyAgreement *ctx, OH_CryptoPrivKey *privkey, OH_CryptoPubKey *pubkey, Crypto_DataBlob *secret) | 生成密钥协商的秘密值。  注意：使用完成后必须通过OH_Crypto_FreeDataBlob释放secret内存。 |
| void OH_CryptoKeyAgreement_Destroy(OH_CryptoKeyAgreement *ctx) | 销毁密钥协商实例。 |

**函数说明**

**OH_CryptoKeyAgreement_Create()**

```ets
OH_Crypto_ErrCode OH_CryptoKeyAgreement_Create(const char *algoName, OH_CryptoKeyAgreement **ctx)
```

描述

根据给定的算法名称创建密钥协商实例。

 注意：创建的资源必须通过[OH_CryptoKeyAgreement_Destroy](crypto_key_agreement.h.md#ZH-CN_TOPIC_0000002553201305__oh_cryptokeyagreement_destroy)销毁。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *algoName | 用于生成密钥协商实例的算法名称。  例如"ECC"、"X25519"。 |
| OH_CryptoKeyAgreement **ctx | 密钥协商实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。  CRYPTO_NOT_SUPPORTED：操作不支持。  CRYPTO_MEMORY_ERROR：内存错误。  CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。  CRYPTO_OPERTION_ERROR：调用三方算法库API出错。 |

**OH_CryptoKeyAgreement_GenerateSecret()**

```ets
OH_Crypto_ErrCode OH_CryptoKeyAgreement_GenerateSecret(OH_CryptoKeyAgreement *ctx, OH_CryptoPrivKey *privkey, OH_CryptoPubKey *pubkey, Crypto_DataBlob *secret)
```

描述

生成密钥协商的秘密值。

 注意：使用完成后必须通过[OH_Crypto_FreeDataBlob](crypto_common.h.md#ZH-CN_TOPIC_0000002522081340__oh_crypto_freedatablob)释放secret内存。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_CryptoKeyAgreement *ctx | 密钥协商实例。 |
| OH_CryptoPrivKey *privkey | 私钥。 |
| OH_CryptoPubKey *pubkey | 公钥。 |
| Crypto_DataBlob *secret | 秘密值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_Crypto_ErrCode | CRYPTO_SUCCESS：操作成功。  CRYPTO_NOT_SUPPORTED：操作不支持。  CRYPTO_MEMORY_ERROR：内存错误。  CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。  CRYPTO_OPERTION_ERROR：调用三方算法库API出错。 |

**OH_CryptoKeyAgreement_Destroy()**

```ets
void OH_CryptoKeyAgreement_Destroy(OH_CryptoKeyAgreement *ctx)
```

描述

销毁密钥协商实例。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_CryptoKeyAgreement *ctx | 密钥协商实例。 |