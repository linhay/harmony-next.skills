# crypto_asym_key.h

#### 概述

声明非对称密钥接口。

**引用文件：** <CryptoArchitectureKit/crypto_asym_key.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：**[CryptoAsymKeyApi](../../topics/networking/CryptoAsymKeyApi.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_CryptoKeyPair](../../topics/misc/OH_CryptoKeyPair.md)OH_CryptoKeyPair定义密钥对结构体。[OH_CryptoPubKey](../../topics/misc/OH_CryptoPubKey.md)OH_CryptoPubKey定义公钥结构体。[OH_CryptoPrivKey](../../topics/misc/OH_CryptoPrivKey.md)OH_CryptoPrivKey定义私钥结构体。[OH_CryptoAsymKeyGenerator](../../topics/misc/OH_CryptoAsymKeyGenerator.md)OH_CryptoAsymKeyGenerator定义非对称密钥生成器结构体。[OH_CryptoPrivKeyEncodingParams](../../topics/media/OH_CryptoPrivKeyEncodingParams.md)OH_CryptoPrivKeyEncodingParams定义私钥编码参数结构体。[OH_CryptoAsymKeySpec](../../topics/misc/OH_CryptoAsymKeySpec.md)OH_CryptoAsymKeySpec定义非对称密钥规格结构体。[OH_CryptoAsymKeyGeneratorWithSpec](../../topics/misc/OH_CryptoAsymKeyGeneratorWithSpec.md)OH_CryptoAsymKeyGeneratorWithSpec定义带规格的非对称密钥生成器。[OH_CryptoEcPoint](../../topics/misc/OH_CryptoEcPoint.md)OH_CryptoEcPoint定义EC点结构体。

#### 枚举

名称typedef关键字描述[CryptoAsymKey_ParamType](#ZH-CN_TOPIC_0000002497445378__cryptoasymkey_paramtype)CryptoAsymKey_ParamType定义非对称密钥参数类型。[Crypto_EncodingType](#ZH-CN_TOPIC_0000002497445378__crypto_encodingtype)Crypto_EncodingType定义编码格式。[CryptoPrivKeyEncoding_ParamType](#ZH-CN_TOPIC_0000002497445378__cryptoprivkeyencoding_paramtype)CryptoPrivKeyEncoding_ParamType定义私钥编码参数类型。[CryptoAsymKeySpec_Type](#ZH-CN_TOPIC_0000002497445378__cryptoasymkeyspec_type)CryptoAsymKeySpec_Type定义非对称密钥规格类型。

#### 函数

名称描述[OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_Create(const char *algoName, OH_CryptoAsymKeyGenerator **ctx)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeygenerator_create)通过指定算法名称的字符串，获取相应的非对称密钥生成器实例。[OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_Generate(OH_CryptoAsymKeyGenerator *ctx, OH_CryptoKeyPair **keyCtx)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeygenerator_generate)随机生成非对称密钥（密钥对）。[OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_Convert(OH_CryptoAsymKeyGenerator *ctx, Crypto_EncodingType type, Crypto_DataBlob *pubKeyData, Crypto_DataBlob *priKeyData, OH_CryptoKeyPair **keyCtx)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeygenerator_convert)将非对称密钥数据转换为密钥对。[const char *OH_CryptoAsymKeyGenerator_GetAlgoName(OH_CryptoAsymKeyGenerator *ctx)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeygenerator_getalgoname)获取非对称密钥算法名称。[void OH_CryptoAsymKeyGenerator_Destroy(OH_CryptoAsymKeyGenerator *ctx)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeygenerator_destroy)销毁非对称密钥生成器实例。[void OH_CryptoKeyPair_Destroy(OH_CryptoKeyPair *keyCtx)](#ZH-CN_TOPIC_0000002497445378__oh_cryptokeypair_destroy)销毁非对称密钥对实例。[OH_CryptoPubKey *OH_CryptoKeyPair_GetPubKey(OH_CryptoKeyPair *keyCtx)](#ZH-CN_TOPIC_0000002497445378__oh_cryptokeypair_getpubkey)从密钥对中获取公钥实例。[OH_CryptoPrivKey *OH_CryptoKeyPair_GetPrivKey(OH_CryptoKeyPair *keyCtx)](#ZH-CN_TOPIC_0000002497445378__oh_cryptokeypair_getprivkey)获取密钥对的私钥。[OH_Crypto_ErrCode OH_CryptoPubKey_Encode(OH_CryptoPubKey *key, Crypto_EncodingType type, const char *encodingStandard, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002497445378__oh_cryptopubkey_encode)根据指定的编码格式输出公钥数据。[OH_Crypto_ErrCode OH_CryptoPubKey_GetParam(OH_CryptoPubKey *key, CryptoAsymKey_ParamType item, Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497445378__oh_cryptopubkey_getparam)从公钥实例获取指定参数。[OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_SetPassword(OH_CryptoAsymKeyGenerator *ctx, const unsigned char *password, uint32_t passwordLen)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeygenerator_setpassword)设置非对称密钥生成器上下文的密码。[OH_Crypto_ErrCode OH_CryptoPrivKeyEncodingParams_Create(OH_CryptoPrivKeyEncodingParams **ctx)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoprivkeyencodingparams_create)创建私钥编码参数。[OH_Crypto_ErrCode OH_CryptoPrivKeyEncodingParams_SetParam(OH_CryptoPrivKeyEncodingParams *ctx, CryptoPrivKeyEncoding_ParamType type, Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoprivkeyencodingparams_setparam)设置私钥编码参数。[void OH_CryptoPrivKeyEncodingParams_Destroy(OH_CryptoPrivKeyEncodingParams *ctx)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoprivkeyencodingparams_destroy)销毁私钥编码参数。[OH_Crypto_ErrCode OH_CryptoPrivKey_Encode(OH_CryptoPrivKey *key, Crypto_EncodingType type, const char *encodingStandard, OH_CryptoPrivKeyEncodingParams *params, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoprivkey_encode)从私钥实例获取指定参数。[OH_Crypto_ErrCode OH_CryptoPrivKey_GetParam(OH_CryptoPrivKey *key, CryptoAsymKey_ParamType item, Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoprivkey_getparam)获取私钥的指定参数。[OH_Crypto_ErrCode OH_CryptoAsymKeySpec_GenEcCommonParamsSpec(const char *curveName, OH_CryptoAsymKeySpec **spec)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeyspec_geneccommonparamsspec)生成EC通用参数规格。[OH_Crypto_ErrCode OH_CryptoAsymKeySpec_GenDhCommonParamsSpec(int pLen, int skLen, OH_CryptoAsymKeySpec **spec)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeyspec_gendhcommonparamsspec)生成DH通用参数规格。[OH_Crypto_ErrCode OH_CryptoAsymKeySpec_Create(const char *algoName, CryptoAsymKeySpec_Type type, OH_CryptoAsymKeySpec **spec)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeyspec_create)根据给定的算法名称和规格类型创建非对称密钥规格。[OH_Crypto_ErrCode OH_CryptoAsymKeySpec_SetParam(OH_CryptoAsymKeySpec *spec, CryptoAsymKey_ParamType type, Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeyspec_setparam)设置非对称密钥规格的指定参数。[OH_Crypto_ErrCode OH_CryptoAsymKeySpec_SetCommonParamsSpec(OH_CryptoAsymKeySpec *spec, OH_CryptoAsymKeySpec *commonParamsSpec)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeyspec_setcommonparamsspec)设置非对称密钥规格的通用参数规格。[OH_Crypto_ErrCode OH_CryptoAsymKeySpec_GetParam(OH_CryptoAsymKeySpec *spec, CryptoAsymKey_ParamType type, Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeyspec_getparam)获取非对称密钥规格的指定参数。[void OH_CryptoAsymKeySpec_Destroy(OH_CryptoAsymKeySpec *spec)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeyspec_destroy)销毁非对称密钥规格。[OH_Crypto_ErrCode OH_CryptoAsymKeyGeneratorWithSpec_Create(OH_CryptoAsymKeySpec *keySpec, OH_CryptoAsymKeyGeneratorWithSpec **generator)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeygeneratorwithspec_create)创建带规格的非对称密钥生成器。[OH_Crypto_ErrCode OH_CryptoAsymKeyGeneratorWithSpec_GenKeyPair(OH_CryptoAsymKeyGeneratorWithSpec *generator, OH_CryptoKeyPair **keyPair)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeygeneratorwithspec_genkeypair)根据非对称密钥规格生成密钥对。[void OH_CryptoAsymKeyGeneratorWithSpec_Destroy(OH_CryptoAsymKeyGeneratorWithSpec *generator)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoasymkeygeneratorwithspec_destroy)销毁带规格的非对称密钥生成器。[OH_Crypto_ErrCode OH_CryptoEcPoint_Create(const char *curveName, Crypto_DataBlob *ecKeyData, OH_CryptoEcPoint **point)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoecpoint_create)创建EC点。[OH_Crypto_ErrCode OH_CryptoEcPoint_GetCoordinate(OH_CryptoEcPoint *point, Crypto_DataBlob *x, Crypto_DataBlob *y)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoecpoint_getcoordinate)获取EC点的x和y坐标。[OH_Crypto_ErrCode OH_CryptoEcPoint_SetCoordinate(OH_CryptoEcPoint *point, Crypto_DataBlob *x, Crypto_DataBlob *y)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoecpoint_setcoordinate)设置EC点的x和y坐标。[OH_Crypto_ErrCode OH_CryptoEcPoint_Encode(OH_CryptoEcPoint *point, const char *format, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoecpoint_encode)将EC点编码为指定格式。[void OH_CryptoEcPoint_Destroy(OH_CryptoEcPoint *point)](#ZH-CN_TOPIC_0000002497445378__oh_cryptoecpoint_destroy)销毁EC点。

#### 枚举类型说明

#### CryptoAsymKey_ParamType

```ets
enum CryptoAsymKey_ParamType
```

**描述**

定义非对称密钥参数类型。

**起始版本：** 12

枚举项描述CRYPTO_DSA_P_DATABLOB = 101DSA算法的素模数p。CRYPTO_DSA_Q_DATABLOB = 102DSA算法中密钥参数q（p-1的素因子）。CRYPTO_DSA_G_DATABLOB = 103DSA算法的参数g。CRYPTO_DSA_SK_DATABLOB = 104DSA算法的私钥sk。CRYPTO_DSA_PK_DATABLOB = 105DSA算法的公钥pk。CRYPTO_ECC_FP_P_DATABLOB = 201ECC算法中表示椭圆曲线Fp域的素数p。CRYPTO_ECC_A_DATABLOB = 202ECC算法中椭圆曲线的第一个系数a。CRYPTO_ECC_B_DATABLOB = 203ECC算法中椭圆曲线的第二个系数b。CRYPTO_ECC_G_X_DATABLOB = 204ECC算法中基点g的x坐标。CRYPTO_ECC_G_Y_DATABLOB = 205ECC算法中基点g的y坐标。CRYPTO_ECC_N_DATABLOB = 206ECC算法中基点g的阶n。CRYPTO_ECC_H_INT = 207ECC算法中的余因子h。CRYPTO_ECC_SK_DATABLOB = 208ECC算法中的私钥sk。CRYPTO_ECC_PK_X_DATABLOB = 209ECC算法中，公钥pk（椭圆曲线上的一个点）的x坐标。CRYPTO_ECC_PK_Y_DATABLOB = 210ECC算法中，公钥pk（椭圆曲线上的一个点）的y坐标。CRYPTO_ECC_FIELD_TYPE_STR = 211ECC算法中，椭圆曲线的域类型（当前只支持Fp域）。CRYPTO_ECC_FIELD_SIZE_INT = 212ECC算法中域的大小，单位为bits（注：对于Fp域，域的大小为素数p的bits长度）。CRYPTO_ECC_CURVE_NAME_STR = 213ECC算法中的SECG（Standards for Efficient Cryptography Group）曲线名称。CRYPTO_RSA_N_DATABLOB = 301RSA算法中的模数n。CRYPTO_RSA_D_DATABLOB = 302RSA算法中的私钥sk（即私钥指数d）。CRYPTO_RSA_E_DATABLOB = 303RSA算法中的公钥pk（即公钥指数e）。CRYPTO_DH_P_DATABLOB = 401DH算法中的素数p。CRYPTO_DH_G_DATABLOB = 402DH算法中的参数g。CRYPTO_DH_L_INT = 403DH算法中私钥长度，单位为bit。CRYPTO_DH_SK_DATABLOB = 404DH算法中的私钥sk。CRYPTO_DH_PK_DATABLOB = 405DH算法中的公钥pk。CRYPTO_ED25519_SK_DATABLOB = 501Ed25519算法中的私钥sk。CRYPTO_ED25519_PK_DATABLOB = 502Ed25519算法中的公钥pk。CRYPTO_X25519_SK_DATABLOB = 601X25519算法中的私钥sk。CRYPTO_X25519_PK_DATABLOB = 602X25519算法中的公钥pk。

#### Crypto_EncodingType

```ets
enum Crypto_EncodingType
```

**描述**

定义编码格式。

**起始版本：** 12

枚举项描述CRYPTO_PEM = 0PEM格式密钥类型。CRYPTO_DER = 1DER格式密钥类型。

#### CryptoPrivKeyEncoding_ParamType

```ets
enum CryptoPrivKeyEncoding_ParamType
```

**描述**

定义私钥编码参数类型。

**起始版本：** 20

枚举项描述CRYPTO_PRIVATE_KEY_ENCODING_PASSWORD_STR = 0表示密码字符串。CRYPTO_PRIVATE_KEY_ENCODING_SYMMETRIC_CIPHER_STR = 1表示对称加密字符串。

#### CryptoAsymKeySpec_Type

```ets
enum CryptoAsymKeySpec_Type
```

**描述**

定义非对称密钥规格类型。

**起始版本：** 20

枚举项描述CRYPTO_ASYM_KEY_COMMON_PARAMS_SPEC = 0通用参数规格。CRYPTO_ASYM_KEY_PRIVATE_KEY_SPEC = 1私钥规格。CRYPTO_ASYM_KEY_PUBLIC_KEY_SPEC = 2公钥规格。CRYPTO_ASYM_KEY_KEY_PAIR_SPEC = 3密钥对规格。

#### 函数说明

#### OH_CryptoAsymKeyGenerator_Create()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_Create(const char *algoName, OH_CryptoAsymKeyGenerator **ctx)
```

**描述**

通过指定算法名称的字符串，获取相应的非对称密钥生成器实例。

**起始版本：** 12

**参数：**

参数项描述const char *algoName

用于生成生成器的算法名称。

 例如"RSA1024|PRIMES_2"。

[OH_CryptoAsymKeyGenerator](../../topics/misc/OH_CryptoAsymKeyGenerator.md) **ctx指向非对称密钥生成器上下文的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeyGenerator_Generate()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_Generate(OH_CryptoAsymKeyGenerator *ctx, OH_CryptoKeyPair **keyCtx)
```

**描述**

随机生成非对称密钥（密钥对）。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoAsymKeyGenerator](../../topics/misc/OH_CryptoAsymKeyGenerator.md) *ctx非对称密钥生成器实例。[OH_CryptoKeyPair](../../topics/misc/OH_CryptoKeyPair.md) **keyCtx指向非对称密钥对实例的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeyGenerator_Convert()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_Convert(OH_CryptoAsymKeyGenerator *ctx, Crypto_EncodingType type,Crypto_DataBlob *pubKeyData, Crypto_DataBlob *priKeyData, OH_CryptoKeyPair **keyCtx)
```

**描述**

将非对称密钥数据转换为密钥对。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoAsymKeyGenerator](../../topics/misc/OH_CryptoAsymKeyGenerator.md) *ctx非对称密钥生成器实例。[Crypto_EncodingType](#ZH-CN_TOPIC_0000002497445378__crypto_encodingtype) type编码格式。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *pubKeyData公钥数据。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *priKeyData私钥数据。[OH_CryptoKeyPair](../../topics/misc/OH_CryptoKeyPair.md) **keyCtx指向非对称密钥对实例的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeyGenerator_GetAlgoName()

```ets
const char *OH_CryptoAsymKeyGenerator_GetAlgoName(OH_CryptoAsymKeyGenerator *ctx)
```

**描述**

获取非对称密钥算法名称。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoAsymKeyGenerator](../../topics/misc/OH_CryptoAsymKeyGenerator.md) *ctx非对称密钥生成器实例。

**返回：**

类型说明const char *返回非对称密钥算法名称。

#### OH_CryptoAsymKeyGenerator_Destroy()

```ets
void OH_CryptoAsymKeyGenerator_Destroy(OH_CryptoAsymKeyGenerator *ctx)
```

**描述**

销毁非对称密钥生成器实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoAsymKeyGenerator](../../topics/misc/OH_CryptoAsymKeyGenerator.md) *ctx非对称密钥生成器实例。

#### OH_CryptoKeyPair_Destroy()

```ets
void OH_CryptoKeyPair_Destroy(OH_CryptoKeyPair *keyCtx)
```

**描述**

销毁非对称密钥对实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoKeyPair](../../topics/misc/OH_CryptoKeyPair.md) *keyCtx密钥对实例。

#### OH_CryptoKeyPair_GetPubKey()

```ets
OH_CryptoPubKey *OH_CryptoKeyPair_GetPubKey(OH_CryptoKeyPair *keyCtx)
```

**描述**

从密钥对中获取公钥实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoKeyPair](../../topics/misc/OH_CryptoKeyPair.md) *keyCtx密钥对实例。

**返回：**

类型说明[OH_CryptoPubKey](../../topics/misc/OH_CryptoPubKey.md) *返回从密钥对中得到的公钥实例。

#### OH_CryptoKeyPair_GetPrivKey()

```ets
OH_CryptoPrivKey *OH_CryptoKeyPair_GetPrivKey(OH_CryptoKeyPair *keyCtx)
```

**描述**

获取密钥对的私钥。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoKeyPair](../../topics/misc/OH_CryptoKeyPair.md) *keyCtx密钥对实例。

**返回：**

类型说明[OH_CryptoPrivKey](../../topics/misc/OH_CryptoPrivKey.md) *返回从密钥对中得到的私钥实例。

#### OH_CryptoPubKey_Encode()

```ets
OH_Crypto_ErrCode OH_CryptoPubKey_Encode(OH_CryptoPubKey *key, Crypto_EncodingType type,const char *encodingStandard, Crypto_DataBlob *out)
```

**描述**

根据指定的编码格式输出公钥数据。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoPubKey](../../topics/misc/OH_CryptoPubKey.md) *key公钥实例。[Crypto_EncodingType](#ZH-CN_TOPIC_0000002497445378__crypto_encodingtype) type编码类型。const char *encodingStandard编码格式。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *out输出的公钥结果。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoPubKey_GetParam()

```ets
OH_Crypto_ErrCode OH_CryptoPubKey_GetParam(OH_CryptoPubKey *key, CryptoAsymKey_ParamType item, Crypto_DataBlob *value)
```

**描述**

从公钥实例获取指定参数。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoPubKey](../../topics/misc/OH_CryptoPubKey.md) *key公钥实例。[CryptoAsymKey_ParamType](#ZH-CN_TOPIC_0000002497445378__cryptoasymkey_paramtype) item非对称密钥参数类型。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *value参数输出值。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeyGenerator_SetPassword()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeyGenerator_SetPassword(OH_CryptoAsymKeyGenerator *ctx, const unsigned char *password,uint32_t passwordLen)
```

**描述**

设置非对称密钥生成器上下文的密码。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoAsymKeyGenerator](../../topics/misc/OH_CryptoAsymKeyGenerator.md) *ctx指向非对称加密上下文的指针。const unsigned char *password表示密码。uint32_t passwordLen表示密码长度。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoPrivKeyEncodingParams_Create()

```ets
OH_Crypto_ErrCode OH_CryptoPrivKeyEncodingParams_Create(OH_CryptoPrivKeyEncodingParams **ctx)
```

**描述**

创建私钥编码参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoPrivKeyEncodingParams](../../topics/media/OH_CryptoPrivKeyEncodingParams.md) **ctx私钥编码参数。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoPrivKeyEncodingParams_SetParam()

```ets
OH_Crypto_ErrCode OH_CryptoPrivKeyEncodingParams_SetParam(OH_CryptoPrivKeyEncodingParams *ctx,CryptoPrivKeyEncoding_ParamType type, Crypto_DataBlob *value)
```

**描述**

设置私钥编码参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoPrivKeyEncodingParams](../../topics/media/OH_CryptoPrivKeyEncodingParams.md) *ctx私钥编码参数。[CryptoPrivKeyEncoding_ParamType](#ZH-CN_TOPIC_0000002497445378__cryptoprivkeyencoding_paramtype) type私钥编码参数类型。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *value私钥编码参数值。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoPrivKeyEncodingParams_Destroy()

```ets
void OH_CryptoPrivKeyEncodingParams_Destroy(OH_CryptoPrivKeyEncodingParams *ctx)
```

**描述**

销毁私钥编码参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoPrivKeyEncodingParams](../../topics/media/OH_CryptoPrivKeyEncodingParams.md) *ctx私钥编码参数。

#### OH_CryptoPrivKey_Encode()

```ets
OH_Crypto_ErrCode OH_CryptoPrivKey_Encode(OH_CryptoPrivKey *key, Crypto_EncodingType type,const char *encodingStandard, OH_CryptoPrivKeyEncodingParams *params, Crypto_DataBlob *out)
```

**描述**

从私钥实例获取指定参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoPrivKey](../../topics/misc/OH_CryptoPrivKey.md) *key私钥。[Crypto_EncodingType](#ZH-CN_TOPIC_0000002497445378__crypto_encodingtype) type私钥编码类型。const char *encodingStandard

编码标准。

 例如"PKCS8"。

[OH_CryptoPrivKeyEncodingParams](../../topics/media/OH_CryptoPrivKeyEncodingParams.md) *params私钥编码参数，可以为NULL，如果要加密私钥，则应设置此参数。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *out编码结果。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoPrivKey_GetParam()

```ets
OH_Crypto_ErrCode OH_CryptoPrivKey_GetParam(OH_CryptoPrivKey *key, CryptoAsymKey_ParamType item,Crypto_DataBlob *value)
```

**描述**

获取私钥的指定参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoPrivKey](../../topics/misc/OH_CryptoPrivKey.md) *key私钥。[CryptoAsymKey_ParamType](#ZH-CN_TOPIC_0000002497445378__cryptoasymkey_paramtype) item非对称密钥参数类型。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *value输出数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeySpec_GenEcCommonParamsSpec()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeySpec_GenEcCommonParamsSpec(const char *curveName, OH_CryptoAsymKeySpec **spec)
```

**描述**

生成EC通用参数规格。

**起始版本：** 20

**参数：**

参数项描述const char *curveNameECC曲线名称。[OH_CryptoAsymKeySpec](../../topics/misc/OH_CryptoAsymKeySpec.md) **spec指向EC通用参数规格的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeySpec_GenDhCommonParamsSpec()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeySpec_GenDhCommonParamsSpec(int pLen, int skLen, OH_CryptoAsymKeySpec **spec)
```

**描述**

生成DH通用参数规格。

**起始版本：** 20

**参数：**

参数项描述int pLen素数p的字节长度。int skLen私钥的字节长度。[OH_CryptoAsymKeySpec](../../topics/misc/OH_CryptoAsymKeySpec.md) **spec指向DH通用参数规格的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeySpec_Create()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeySpec_Create(const char *algoName, CryptoAsymKeySpec_Type type,OH_CryptoAsymKeySpec **spec)
```

**描述**

根据给定的算法名称和规格类型创建非对称密钥规格。

**起始版本：** 20

**参数：**

参数项描述const char *algoName

用于生成规格的算法名称。

 例如"RSA"。

[CryptoAsymKeySpec_Type](#ZH-CN_TOPIC_0000002497445378__cryptoasymkeyspec_type) type非对称密钥规格类型。[OH_CryptoAsymKeySpec](../../topics/misc/OH_CryptoAsymKeySpec.md) **spec指向非对称密钥规格的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeySpec_SetParam()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeySpec_SetParam(OH_CryptoAsymKeySpec *spec, CryptoAsymKey_ParamType type,Crypto_DataBlob *value)
```

**描述**

设置非对称密钥规格的指定参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoAsymKeySpec](../../topics/misc/OH_CryptoAsymKeySpec.md) *spec非对称密钥规格。[CryptoAsymKey_ParamType](#ZH-CN_TOPIC_0000002497445378__cryptoasymkey_paramtype) type非对称密钥参数类型。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *value输入数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeySpec_SetCommonParamsSpec()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeySpec_SetCommonParamsSpec(OH_CryptoAsymKeySpec *spec,OH_CryptoAsymKeySpec *commonParamsSpec)
```

**描述**

设置非对称密钥规格的通用参数规格。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoAsymKeySpec](../../topics/misc/OH_CryptoAsymKeySpec.md) *spec非对称密钥规格。[OH_CryptoAsymKeySpec](../../topics/misc/OH_CryptoAsymKeySpec.md) *commonParamsSpec通用参数规格。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeySpec_GetParam()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeySpec_GetParam(OH_CryptoAsymKeySpec *spec, CryptoAsymKey_ParamType type,Crypto_DataBlob *value)
```

**描述**

获取非对称密钥规格的指定参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoAsymKeySpec](../../topics/misc/OH_CryptoAsymKeySpec.md) *spec非对称密钥规格。[CryptoAsymKey_ParamType](#ZH-CN_TOPIC_0000002497445378__cryptoasymkey_paramtype) type非对称密钥参数类型。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *value输出数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeySpec_Destroy()

```ets
void OH_CryptoAsymKeySpec_Destroy(OH_CryptoAsymKeySpec *spec)
```

**描述**

销毁非对称密钥规格。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoAsymKeySpec](../../topics/misc/OH_CryptoAsymKeySpec.md) *spec非对称密钥规格。

#### OH_CryptoAsymKeyGeneratorWithSpec_Create()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeyGeneratorWithSpec_Create(OH_CryptoAsymKeySpec *keySpec,OH_CryptoAsymKeyGeneratorWithSpec **generator)
```

**描述**

创建带规格的非对称密钥生成器。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoAsymKeySpec](../../topics/misc/OH_CryptoAsymKeySpec.md) *keySpec非对称密钥规格。[OH_CryptoAsymKeyGeneratorWithSpec](../../topics/misc/OH_CryptoAsymKeyGeneratorWithSpec.md) **generator带规格的非对称密钥生成器。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeyGeneratorWithSpec_GenKeyPair()

```ets
OH_Crypto_ErrCode OH_CryptoAsymKeyGeneratorWithSpec_GenKeyPair(OH_CryptoAsymKeyGeneratorWithSpec *generator,OH_CryptoKeyPair **keyPair)
```

**描述**

根据非对称密钥规格生成密钥对。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoAsymKeyGeneratorWithSpec](../../topics/misc/OH_CryptoAsymKeyGeneratorWithSpec.md) *generator带规格的非对称密钥生成器。[OH_CryptoKeyPair](../../topics/misc/OH_CryptoKeyPair.md) **keyPair指向密钥对的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoAsymKeyGeneratorWithSpec_Destroy()

```ets
void OH_CryptoAsymKeyGeneratorWithSpec_Destroy(OH_CryptoAsymKeyGeneratorWithSpec *generator)
```

**描述**

销毁带规格的非对称密钥生成器。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoAsymKeyGeneratorWithSpec](../../topics/misc/OH_CryptoAsymKeyGeneratorWithSpec.md) *generator带规格的非对称密钥生成器。

#### OH_CryptoEcPoint_Create()

```ets
OH_Crypto_ErrCode OH_CryptoEcPoint_Create(const char *curveName, Crypto_DataBlob *ecKeyData, OH_CryptoEcPoint **point)
```

**描述**

创建EC点。

**起始版本：** 20

**参数：**

参数项描述const char *curveName曲线名称。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *ecKeyDataEC点数据，支持"04 || x || y"、"02 || x"或"03 || x"格式。如果ecKeyData参数为NULL，将创建一个空的EC点规格。[OH_CryptoEcPoint](../../topics/misc/OH_CryptoEcPoint.md) **point指向EC点的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoEcPoint_GetCoordinate()

```ets
OH_Crypto_ErrCode OH_CryptoEcPoint_GetCoordinate(OH_CryptoEcPoint *point, Crypto_DataBlob *x, Crypto_DataBlob *y)
```

**描述**

获取EC点的x和y坐标。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoEcPoint](../../topics/misc/OH_CryptoEcPoint.md) *pointEC点。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *xEC点的x坐标,可以为NULL。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *yEC点的y坐标,可以为NULL。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoEcPoint_SetCoordinate()

```ets
OH_Crypto_ErrCode OH_CryptoEcPoint_SetCoordinate(OH_CryptoEcPoint *point, Crypto_DataBlob *x, Crypto_DataBlob *y)
```

**描述**

设置EC点的x和y坐标。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoEcPoint](../../topics/misc/OH_CryptoEcPoint.md) *pointEC点。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *xEC点的x坐标。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *yEC点的y坐标。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoEcPoint_Encode()

```ets
OH_Crypto_ErrCode OH_CryptoEcPoint_Encode(OH_CryptoEcPoint *point, const char *format, Crypto_DataBlob *out)
```

**描述**

将EC点编码为指定格式。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoEcPoint](../../topics/misc/OH_CryptoEcPoint.md) *pointEC点。const char *format编码格式,支持"UNCOMPRESSED"和"COMPRESSED"。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *out编码后的EC点数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERTION_ERROR：调用三方算法库API出错。

#### OH_CryptoEcPoint_Destroy()

```ets
void OH_CryptoEcPoint_Destroy(OH_CryptoEcPoint *point)
```

**描述**

销毁EC点。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoEcPoint](../../topics/misc/OH_CryptoEcPoint.md) *pointEC点。