# @ohos.security.cryptoFramework (加解密算法库框架)

提供统一的密码算法库加解密接口，以屏蔽底层硬件和算法库。

- 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
```

#### Result

表示执行结果的枚举。

**系统能力：** SystemCapability.Security.CryptoFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| INVALID_PARAMS | 401 | 非法入参。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| NOT_SUPPORT | 801 | 操作不支持。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_OUT_OF_MEMORY | 17620001 | 内存操作失败。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |
| ERR_RUNTIME_ERROR | 17620002 | 表示在ArkTS和C之间转换参数失败。 元服务API： 从API version 12开始，该接口支持在元服务中使用。 |
| ERR_PARAMETER_CHECK_FAILED20+ | 17620003 | 表示参数检查失败。 元服务API： 从API version 20开始，该接口支持在元服务中使用。 |
| ERR_CRYPTO_OPERATION | 17630001 | 调用三方算法库API出错。 元服务API： 从API version 11开始，该接口支持在元服务中使用。 |

#### DataBlob

二进制数据的封装接口，核心字段data为Uint8Array类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| data | Uint8Array | 否 | 否 | 数据。 |


Uint8Array类型数据表示8位无符号整数的数组。

#### ParamsSpec

加解密参数，在进行对称加解密时需要构造其子类对象，并将子类对象传入[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法。

适用于需要iv等参数的对称加解密模式（对于无iv等参数的模式如ECB模式，无需构造，在[init()](#ZH-CN_TOPIC_0000002553201293__init-1)中传入null即可）。


iv（Initialization Vector，初始化向量）是用于对称加密模式（如 CBC/CTR/OFB/CFB/GCM/CCM/Poly1305）中引入随机性或唯一性的字节序列，保证相同明文在相同密钥下产生不同密文。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 否 | 否 | 指明对称加解密参数的算法模式。可选值如下： - "IvParamsSpec"：适用于CBC|CTR|OFB|CFB模式。 - "GcmParamsSpec"：适用于GCM模式。 - "CcmParamsSpec"：适用于CCM模式。 |


由于[init()](#ZH-CN_TOPIC_0000002553201293__init-1)的params参数是ParamsSpec类型（父类），而实际需要传入具体的子类对象（如IvParamsSpec），因此在构造子类对象时应设置其父类ParamsSpec的algName参数，使算法库在init()时知道传入的是哪种子类对象。

#### IvParamsSpec

加解密参数[ParamsSpec](#ZH-CN_TOPIC_0000002553201293__paramsspec)的子类，用于在对称加解密时作为[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法的参数。

适用于CBC、CTR、OFB、CFB、Poly1305这些需要iv作为参数的加解密模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iv | DataBlob | 否 | 否 | 指明加解密参数iv。常见取值如下： - AES的CBC|CTR|OFB|CFB模式：iv长度为16字节。 - 3DES的CBC|OFB|CFB模式：iv长度为8字节。 - SM410+的CBC|CTR|OFB|CFB模式：iv长度为16字节。 |


传入[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法前需要指定其algName属性（来源于父类[ParamsSpec](#ZH-CN_TOPIC_0000002553201293__paramsspec)）。

#### GcmParamsSpec

加解密参数[ParamsSpec](#ZH-CN_TOPIC_0000002553201293__paramsspec)的子类，用于在对称加解密时作为[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法的参数。

适用于GCM模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iv | DataBlob | 否 | 否 | 指明加解密参数iv，长度为1~16字节，常用为12字节。 |
| aad | DataBlob | 否 | 否 | 指明加解密参数aad，长度为0~INT_MAX字节，常用为16字节。 |
| authTag | DataBlob | 否 | 否 | 指明加解密参数authTag，长度为16字节。 采用GCM模式加密时，需从doFinal()或doFinalSync()输出的DataBlob中提取末尾16字节，作为init()或initSync()方法中GcmParamsSpec的authTag。 |


1. 传入[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法前需要指定其algName属性（来源于父类[ParamsSpec](#ZH-CN_TOPIC_0000002553201293__paramsspec)）。

1. 对于1~16字节长度的iv，加解密算法库无额外限制，但结果取决于底层openssl的支持情况。
1. 当aad参数不需要使用或aad长度为0时，可以将aad的data属性设置为一个空的Uint8Array，来构造GcmParamsSpec，写法为aad: { data: new Uint8Array() }。

#### CcmParamsSpec

加解密参数[ParamsSpec](#ZH-CN_TOPIC_0000002553201293__paramsspec)的子类，用于在对称加解密时作为[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法的参数。

适用于CCM模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iv | DataBlob | 否 | 否 | 指明加解密参数iv，仅支持7字节。若传入iv长度超过7字节，超出范围将被截断。 |
| aad | DataBlob | 否 | 否 | 指明加解密参数aad。aad最小长度为1字节，最大为2048字节。 |
| authTag | DataBlob | 否 | 否 | 指定加解密参数authTag，长度为12字节。 在CCM模式加密时，需从doFinal()或doFinalSync()输出的DataBlob末尾提取12字节，作为init()或initSync()方法的参数CcmParamsSpec中的authTag。 |


传入[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法前需要指定其algName属性（来源于父类[ParamsSpec](#ZH-CN_TOPIC_0000002553201293__paramsspec)）。

#### Poly1305ParamsSpec22+

加解密参数[ParamsSpec](#ZH-CN_TOPIC_0000002553201293__paramsspec)的子类，用于在对称加解密时作为[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法的参数。

适用于[ChaCha20算法](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-encrypt-decrypt-spec#chacha20)Poly1305模式。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| iv | DataBlob | 否 | 否 | 指明加解密参数iv，长度为12字节。 |
| aad | DataBlob | 否 | 否 | 指明加解密参数aad，长度为任意字节。 |
| authTag | DataBlob | 否 | 否 | 指定加解密参数authTag，长度为16字节。 |


传入[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法前需要指定其algName属性（来源于父类[ParamsSpec](#ZH-CN_TOPIC_0000002553201293__paramsspec)）。

在Poly1305模式加密时，需从[doFinal()](#ZH-CN_TOPIC_0000002553201293__dofinal)或[doFinalSync()](#ZH-CN_TOPIC_0000002553201293__dofinalsync12)输出的[DataBlob](#ZH-CN_TOPIC_0000002553201293__datablob)末尾提取16字节，作为解密时[init()](#ZH-CN_TOPIC_0000002553201293__init-1)或[initSync()](#ZH-CN_TOPIC_0000002553201293__initsync12)方法的参数[Poly1305ParamsSpec](#ZH-CN_TOPIC_0000002553201293__poly1305paramsspec22)中的authTag。

#### CryptoMode

表示加解密操作的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ENCRYPT_MODE | 0 | 表示进行加密操作。 |
| DECRYPT_MODE | 1 | 表示进行解密操作。 |

#### AsyKeySpecItem10+

表示密钥参数的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DSA_P_BN | 101 | DSA算法的素模数p。 |
| DSA_Q_BN | 102 | DSA算法中密钥参数q（p-1的素因子）。 |
| DSA_G_BN | 103 | DSA算法的参数g。 |
| DSA_SK_BN | 104 | DSA算法的私钥sk。 |
| DSA_PK_BN | 105 | DSA算法的公钥pk。 |
| ECC_FP_P_BN | 201 | ECC算法中表示椭圆曲线Fp域的素数p。 |
| ECC_A_BN | 202 | ECC算法中椭圆曲线的第一个系数a。 |
| ECC_B_BN | 203 | ECC算法中椭圆曲线的第二个系数b。 |
| ECC_G_X_BN | 204 | ECC算法中基点g的x坐标。 |
| ECC_G_Y_BN | 205 | ECC算法中基点g的y坐标。 |
| ECC_N_BN | 206 | ECC算法中基点g的阶n。 |
| ECC_H_NUM | 207 | ECC算法中的余因子h。 |
| ECC_SK_BN | 208 | ECC算法中的私钥sk。 |
| ECC_PK_X_BN | 209 | ECC算法中，公钥pk（椭圆曲线上的一个点）的x坐标。 |
| ECC_PK_Y_BN | 210 | ECC算法中，公钥pk（椭圆曲线上的一个点）的y坐标。 |
| ECC_FIELD_TYPE_STR | 211 | ECC算法中，椭圆曲线的域类型（当前只支持Fp域）。 |
| ECC_FIELD_SIZE_NUM | 212 | ECC算法中域的大小，单位为bits（注：对于Fp域，域的大小为素数p的bits长度）。 |
| ECC_CURVE_NAME_STR | 213 | ECC算法中的SECG(Standards for Efficient Cryptography Group)曲线名称。 |
| RSA_N_BN | 301 | RSA算法中的模数n。 |
| RSA_SK_BN | 302 | RSA算法中的私钥sk（即私钥指数d）。 |
| RSA_PK_BN | 303 | RSA算法中的公钥pk（即公钥指数e）。 |
| DH_P_BN11+ | 401 | DH算法中的素数p。 |
| DH_G_BN11+ | 402 | DH算法中的参数g。 |
| DH_L_NUM11+ | 403 | DH算法中私钥长度，单位为bit。 |
| DH_SK_BN11+ | 404 | DH算法中的私钥sk。 |
| DH_PK_BN11+ | 405 | DH算法中的公钥pk。 |
| ED25519_SK_BN11+ | 501 | Ed25519算法中的私钥sk。 |
| ED25519_PK_BN11+ | 502 | Ed25519算法中的公钥pk。 |
| X25519_SK_BN11+ | 601 | X25519算法中的私钥sk。 |
| X25519_PK_BN11+ | 602 | X25519算法中的公钥pk。 |

#### AsyKeySpecType10+

表示密钥参数类型的枚举。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMMON_PARAMS_SPEC | 0 | 表示公私钥中包含的公共参数。使用此类型的参数可以调用generateKeyPair随机生成密钥对。 |
| PRIVATE_KEY_SPEC | 1 | 表示私钥中包含的参数。使用此类型的参数可以调用generatePriKey生成指定的私钥。 |
| PUBLIC_KEY_SPEC | 2 | 表示公钥中包含的参数。使用此类型的参数可以调用generatePubKey生成指定的公钥。 |
| KEY_PAIR_SPEC | 3 | 表示公私钥中包含的全量参数。使用此类型的参数可以调用generateKeyPair生成指定的密钥对。 |

#### CipherSpecItem10+

表示加解密参数的枚举。这些参数支持通过[setCipherSpec](#ZH-CN_TOPIC_0000002553201293__setcipherspec10)接口设置，通过[getCipherSpec](#ZH-CN_TOPIC_0000002553201293__getcipherspec10)接口获取。

当前只支持RSA算法和SM2算法，从API version 11开始，增加对SM2_MD_NAME_STR参数的支持，详细规格请参考[加解密规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-encrypt-decrypt-spec)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 10-11 系统能力为 SystemCapability.Security.CryptoFramework；从 API version 12 开始为SystemCapability.Security.CryptoFramework.Cipher

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OAEP_MD_NAME_STR | 100 | 表示RSA算法中，使用PKCS1_OAEP模式时，消息摘要功能的算法名。 |
| OAEP_MGF_NAME_STR | 101 | 表示RSA算法中，使用PKCS1_OAEP模式时，掩码生成算法（目前仅支持MGF1）。 |
| OAEP_MGF1_MD_STR | 102 | 表示RSA算法中，使用PKCS1_OAEP模式时，MGF1掩码生成功能的消息摘要算法。 |
| OAEP_MGF1_PSRC_UINT8ARR | 103 | 表示RSA算法中，使用PKCS1_OAEP模式时，pSource的字节流。 |
| SM2_MD_NAME_STR11+ | 104 | 表示SM2算法中，使用的摘要算法名。 |

#### SignSpecItem10+

表示签名验签参数的枚举。这些参数支持通过[setSignSpec](#ZH-CN_TOPIC_0000002553201293__setsignspec10)、[setVerifySpec](#ZH-CN_TOPIC_0000002553201293__setverifyspec10)接口设置，通过[getSignSpec](#ZH-CN_TOPIC_0000002553201293__getsignspec10)、[getVerifySpec](#ZH-CN_TOPIC_0000002553201293__getverifyspec10)接口获取。

当前只支持RSA算法和SM2算法，从API version 11开始，增加对SM2_USER_ID_UINT8ARR参数的支持，详细规格请参考[签名验签规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sign-sig-verify-overview)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 10-11 系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为 SystemCapability.Security.CryptoFramework.Signature。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PSS_MD_NAME_STR | 100 | 表示RSA算法中，使用PSS模式时，消息摘要功能的算法名。 |
| PSS_MGF_NAME_STR | 101 | 表示RSA算法中，使用PSS模式时，掩码生成算法（目前仅支持MGF1）。 |
| PSS_MGF1_MD_STR | 102 | 表示RSA算法中，使用PSS模式时，MGF1掩码生成功能的消息摘要参数。 |
| PSS_SALT_LEN_NUM | 103 | 表示RSA算法中，使用PSS模式时，盐值的长度，长度以字节为单位。 |
| PSS_TRAILER_FIELD_NUM | 104 | 表示RSA算法中，使用PSS模式时，用于编码操作的整数。 |
| SM2_USER_ID_UINT8ARR11+ | 105 | 表示SM2算法中，用户身份标识字段。 |

#### AsyKeySpec10+

指定非对称密钥参数的基本接口，用于创建密钥生成器。在指定非对称密钥参数时需要构造其子类对象，并将子类对象传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。构造子类对象时，除了RSA密钥采用小端写法外，其他bigint类型的密钥参数均采用大端写法，并使用正数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version10-11系统能力为SystemCapability.Security.CryptoFramework；从API version12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 否 | 否 | 指定非对称密钥的算法名称，比如"RSA"、"DSA"、"ECC"、"SM2"、"Ed25519"、"X25519"、"DH"。 |
| specType | AsyKeySpecType | 否 | 否 | 指定密钥参数类型，用于区分公/私钥参数。 |

#### DSACommonParamsSpec10+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定DSA算法中公私钥包含的公共参数，随机生成公/私钥。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version10-11系统能力为SystemCapability.Security.CryptoFramework；从API version12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| p | bigint | 否 | 否 | 指定DSA算法的素模数p。 |
| q | bigint | 否 | 否 | 指定DSA算法中密钥参数q（p-1的素因子）。 |
| g | bigint | 否 | 否 | 指定DSA算法的参数g。 |

#### DSAPubKeySpec10+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定DSA算法中公钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version10-11系统能力为SystemCapability.Security.CryptoFramework；从API version12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| params | DSACommonParamsSpec | 否 | 否 | 指定DSA算法中公私钥包含的公共参数。 |
| pk | bigint | 否 | 否 | 指定DSA算法的公钥值。 |

#### DSAKeyPairSpec10+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定DSA算法中公私钥包含的全量参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| params | DSACommonParamsSpec | 否 | 否 | 指定DSA算法中公私钥都包含的公共参数。 |
| sk | bigint | 否 | 否 | 指定DSA算法的私钥值sk。 |
| pk | bigint | 否 | 否 | 指定DSA算法的公钥值pk。 |

#### ECField10+

指定椭圆曲线的域类型。当前只支持Fp域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fieldType | string | 否 | 否 | 指定椭圆曲线域的类型，当前只支持"Fp"。 |

#### ECFieldFp10+

指定椭圆曲线的素数域。是[ECField](#ZH-CN_TOPIC_0000002553201293__ecfield10)的子类。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework。从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| p | bigint | 否 | 否 | 指定素数p的值。 |

#### Point10+

指定椭圆曲线上的一个点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | bigint | 否 | 否 | 指定椭圆曲线上点的x坐标。 |
| y | bigint | 否 | 否 | 指定椭圆曲线上点的y坐标。 |

#### ECCCommonParamsSpec10+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定ECC算法中公私钥包含的公共参数，随机生成公/私钥。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| field | ECField | 否 | 否 | 指定椭圆曲线的域（当前只支持Fp域）。 |
| a | bigint | 否 | 否 | 指定椭圆曲线的第一个系数a。 |
| b | bigint | 否 | 否 | 指定椭圆曲线的第二个系数b。 |
| g | Point | 否 | 否 | 指定基点g。 |
| n | bigint | 否 | 否 | 指定基点g的阶数n。 |
| h | number | 否 | 否 | 指定余因子h。 |

#### ECCPriKeySpec10+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定ECC算法中私钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| params | ECCCommonParamsSpec | 否 | 否 | 指定ECC算法中公私钥都包含的公共参数。 |
| sk | bigint | 否 | 否 | 指定ECC算法的私钥sk。 |

#### ECCPubKeySpec10+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定ECC算法中公钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| params | ECCCommonParamsSpec | 否 | 否 | 指定ECC算法中公私钥都包含的公共参数。 |
| pk | Point | 否 | 否 | 指定ECC算法的公钥pk。 |

#### ECCKeyPairSpec10+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定ECC算法中公私钥包含的全量参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| params | ECCCommonParamsSpec | 否 | 否 | 指定ECC算法中公私钥都包含的公共参数。 |
| sk | bigint | 否 | 否 | 指定ECC算法的私钥sk。 |
| pk | Point | 否 | 否 | 指定ECC算法的公钥pk。 |

#### RSACommonParamsSpec10+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定RSA算法中公私钥包含的公共参数，随机生成公/私钥。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| n | bigint | 否 | 否 | 指定模数n。 |

#### RSAPubKeySpec10+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定RSA算法中公钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| params | RSACommonParamsSpec | 否 | 否 | 指定RSA算法中公私钥都包含的公共参数。 |
| pk | bigint | 否 | 否 | 指定RSA算法的公钥pk。 |

#### RSAKeyPairSpec10+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定RSA算法中公私钥包含的全量参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| params | RSACommonParamsSpec | 否 | 否 | 指定RSA算法中公私钥都包含的公共参数。 |
| sk | bigint | 否 | 否 | 指定RSA算法的私钥sk。 |
| pk | bigint | 否 | 否 | 指定RSA算法的公钥pk。 |

#### ED25519PriKeySpec11+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定Ed25519算法中私钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sk | bigint | 否 | 否 | 指定Ed25519算法的私钥sk。 |

#### ED25519PubKeySpec11+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定Ed25519算法中公钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pk | bigint | 否 | 否 | 指定Ed25519算法的公钥pk。 |

#### ED25519KeyPairSpec11+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定Ed25519算法中公私钥包含的全量参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sk | bigint | 否 | 否 | 指定Ed25519算法的私钥sk。 |
| pk | bigint | 否 | 否 | 指定Ed25519算法的公钥pk。 |

#### X25519PriKeySpec11+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定X25519算法中私钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sk | bigint | 否 | 否 | 指定X25519算法的私钥sk。 |

#### X25519PubKeySpec11+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定X25519算法中公钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pk | bigint | 否 | 否 | 指定X25519算法的公钥pk。 |

#### X25519KeyPairSpec11+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定X25519算法中公私钥包含的全量参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| sk | bigint | 否 | 否 | 指定X25519算法的私钥sk。 |
| pk | bigint | 否 | 否 | 指定X25519算法的公钥pk。 |

#### DHCommonParamsSpec11+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定DH算法中公私钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| p | bigint | 否 | 否 | 指定DH算法中大素数p。 |
| g | bigint | 否 | 否 | 指定DH算法中参数g。 |
| l | number | 否 | 否 | 指定DH算法中私钥的长度，单位为bit。 |

#### DHPriKeySpec11+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定DH算法中私钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| params | DHCommonParamsSpec | 否 | 否 | 指定DH算法中公私钥都包含的公共参数。 |
| sk | bigint | 否 | 否 | 指定DH算法的私钥sk。 |

#### DHPubKeySpec11+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定DH算法中公钥包含的参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| params | DHCommonParamsSpec | 否 | 否 | 指定DH算法中公私钥都包含的公共参数。 |
| pk | bigint | 否 | 否 | 指定DH算法的公钥pk。 |

#### DHKeyPairSpec11+

密钥参数[AsyKeySpec](#ZH-CN_TOPIC_0000002553201293__asykeyspec10)的子类，用于指定DH算法中公私钥包含的全量参数。

在使用密钥参数生成密钥时，将其传入[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法创建密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| params | DHCommonParamsSpec | 否 | 否 | 指定DH算法中公私钥都包含的公共参数。 |
| sk | bigint | 否 | 否 | 指定DH算法的私钥sk。 |
| pk | bigint | 否 | 否 | 指定DH算法的公钥pk。 |

#### KdfSpec11+

密钥派生函数参数，使用密钥派生函数进行密钥派生时，需要构建其子类对象并作为输入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Kdf。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 否 | 否 | 指明密钥派生函数的算法名，如"PBKDF2"。 |

#### PBKDF2Spec11+

密钥派生函数参数[KdfSpec](#ZH-CN_TOPIC_0000002553201293__kdfspec11)的子类，作为PBKDF2密钥派生函数进行密钥派生时的输入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Kdf。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| password | string | Uint8Array | 否 | 否 | 用户输入的原始密码。 |
| salt | Uint8Array | 否 | 否 | 盐值。 |
| iterations | number | 否 | 否 | 迭代次数，需要为正整数。 |
| keySize | number | 否 | 否 | 派生得到的密钥字节长度。 |


password 是原始密码。如果使用 string 类型，需直接传入用于密钥派生的数据，而不是 HexString 或 base64 等字符串类型，并确保该字符串为 UTF-8 编码，否则派生结果会有差异。

#### HKDFSpec12+

密钥派生函数参数[KdfSpec](#ZH-CN_TOPIC_0000002553201293__kdfspec11)的子类，作为HKDF密钥派生函数进行密钥派生时的输入。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | Uint8Array | 否 | 否 | 密钥材料。 |
| salt | Uint8Array | 否 | 否 | 盐值。 |
| info | Uint8Array | 否 | 否 | 拓展信息。 |
| keySize | number | 否 | 否 | 派生得到的密钥字节长度。 |


key指的是用户输入的最初的密钥材料。info与salt是可选参数，根据模式的不同可以传空，但是不可不传。

例如：EXTRACT_AND_EXPAND模式需要输入全部的值，EXTRACT_ONLY模式info可以为空，在构建HKDFSpec的时候，info传入null值。

默认的模式为EXTRACT_AND_EXPAND，"HKDF|SHA256|EXTRACT_AND_EXPAND"等价于"HKDF|SHA256"。

#### ScryptSpec18+

密钥派生函数参数[KdfSpec](#ZH-CN_TOPIC_0000002553201293__kdfspec11)的子类，作为SCRYPT密钥派生函数进行密钥派生时的输入。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| passphrase | string | Uint8Array | 否 | 否 | 用户输入的原始密码。 |
| salt | Uint8Array | 否 | 否 | 盐值。 |
| n | number | 否 | 否 | 迭代次数，需要为正整数。 |
| p | number | 否 | 否 | 并行化参数，需要为正整数。 |
| r | number | 否 | 否 | 块大小参数，需要为正整数。 |
| maxMemory | number | 否 | 否 | 最大内存限制参数，需要为正整数。 |
| keySize | number | 否 | 否 | 派生得到的密钥字节长度，需要为正整数。 |


passphrase指的是原始密码，如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型，同时需要确保该字符串为utf-8编码，否则派生结果会有差异。

#### X963KdfSpec22+

密钥派生函数参数[KdfSpec](#ZH-CN_TOPIC_0000002553201293__kdfspec11)的子类，作为X963KDF密钥派生函数进行密钥派生时的输入。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| key | string | Uint8Array | 否 | 否 | 密钥材料。 |
| info | Uint8Array | 否 | 否 | 附加信息。 |
| keySize | number | 否 | 否 | 派生得到的密钥字节长度，需要为正整数。 |


key指的是用户输入的最初的密钥材料。

#### SM2CipherTextSpec12+

SM2密文参数，使用SM2密文格式转换函数进行格式转换时，需要用到此对象。可以通过指定此参数，生成符合国密标准的ASN.1格式的SM2密文，反之，也可以从ASN.1格式的SM2密文中获取具体参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| xCoordinate | bigint | 否 | 否 | x分量。 |
| yCoordinate | bigint | 否 | 否 | y分量。 |
| cipherTextData | Uint8Array | 否 | 否 | 密文。 |
| hashData | Uint8Array | 否 | 否 | 杂凑值。 |


-

hashData为使用SM3算法对明文数据运算得到的杂凑值，其长度固定为256位。

-

cipherTextData是与明文等长的密文。

-

在拼接生成C1C3C2格式的密文时，如果x分量（C1_X）或y分量（C1_Y）的长度不足32字节，需要在高位补0，使得x分量和y分量的长度均为32字节。

#### KeyEncodingConfig18+

RSA私钥编码参数，使用获取私钥字符串时，可以添加此参数，生成指定算法、密码的编码后的私钥字符串。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| password | string | 否 | 否 | 密码。 |
| cipherName | string | 否 | 否 | 算法名。 |


-

password是必选参数，表示编码用到的密码。

-

cipherName是必选参数，指定编码用到的算法。当前仅支持AES-128-CBC、AES-192-CBC、AES-256-CBC、DES-EDE3-CBC。

#### MacSpec18+

消息认证码参数，计算HMAC、CMAC消息认证码时，需要构建子类对象并作为输入参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 否 | 否 | 消息验证码算法名。 |


algName是必选参数，表示消息验证码算法。

#### HmacSpec18+

密钥派生函数参数[MacSpec](#ZH-CN_TOPIC_0000002553201293__macspec18)的子类，作为HMAC消息验证码计算的输入。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| mdName | string | 否 | 否 | 摘要算法名。 |


mdName是必选参数，表示HMAC摘要算法。

#### CmacSpec18+

密钥派生函数参数[MacSpec](#ZH-CN_TOPIC_0000002553201293__macspec18)的子类，作为CMAC消息验证码计算的输入。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| cipherName | string | 否 | 否 | 对称加密算法名。 |


cipherName是必选参数，表示CMAC对称加密算法。

#### EccSignatureSpec20+

包含（r、s）的sm2签名数据的结构体。

r和s的长度各为256位。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| r | bigint | 否 | 否 | r分量。 |
| s | bigint | 否 | 否 | s分量。 |

#### Key

密钥（父类），在运行密码算法（如加解密）时需要提前生成其子类对象，并传入[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例的[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法。

密钥通过子类密钥生成器来生成，详见子类描述。具体子类有：[SymKey](#ZH-CN_TOPIC_0000002553201293__symkey)、[PubKey](#ZH-CN_TOPIC_0000002553201293__pubkey)、[PriKey](#ZH-CN_TOPIC_0000002553201293__prikey)。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| format | string | 是 | 否 | 密钥的格式。 |
| algName | string | 是 | 否 | 密钥对应的算法名（如果是对称密钥，则含密钥长度，否则不含密钥长度）。 |

#### getEncoded

getEncoded(): DataBlob

同步方法，获取密钥数据的字节流。密钥可以是对称密钥、公钥或私钥。公钥格式需符合ASN.1语法、X.509规范和DER编码；私钥格式需符合ASN.1语法、PKCS#8规范和DER编码。

RSA算法使用密钥参数生成私钥时，私钥对象支持getEncoded。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 用于查看密钥的具体内容。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码]([crypto framework错误码](../../errors/crypto framework错误码.md).md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateAesKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  let symKey = await symKeyGenerator.generateSymKey();
  let encodedKey = symKey.getEncoded();
  console.info('key hex:' + encodedKey.data);
}
```

#### SymKey

对称密钥，是[Key](#ZH-CN_TOPIC_0000002553201293__key)的子类，在对称加解密时需要将其对象传入[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例的[init()](#ZH-CN_TOPIC_0000002553201293__init-1)方法使用。

对称密钥通过对称密钥生成器[SymKeyGenerator](#ZH-CN_TOPIC_0000002553201293__symkeygenerator)来生成。

#### clearMem

clearMem(): void

同步方法，将系统底层内存中的密钥内容清零。建议在不再使用对称密钥实例时调用此函数，避免密钥数据在内存中存留过久。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.SymKey。

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateAesKeyFun() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  let key = await symKeyGenerator.generateSymKey();
  let encodedKey = key.getEncoded();
  console.info('key blob: '+ encodedKey.data);
  key.clearMem();
  encodedKey = key.getEncoded();
  console.info('key blob：' + encodedKey.data);
}
```

#### PubKey

公钥，是[Key](#ZH-CN_TOPIC_0000002553201293__key)的子类，在非对称加解密、验签、密钥协商时需要将其对象作为输入使用。

公钥可以通过非对称密钥生成器[AsyKeyGenerator](#ZH-CN_TOPIC_0000002553201293__asykeygenerator)、[AsyKeyGeneratorBySpec](#ZH-CN_TOPIC_0000002553201293__asykeygeneratorbyspec10)来生成。

#### getAsyKeySpec10+

getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number

同步方法，获取密钥参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemType | AsyKeySpecItem | 是 | 指定的密钥参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | string | number | 用于查看密钥参数的具体内容。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// 根据关键规范构造EccCommonSpec结构体。EccCommonSpec结构体定义了ECC私钥和公钥的公共参数。
function genEccCommonSpec(): cryptoFramework.ECCCommonParamsSpec {
  let fieldFp: cryptoFramework.ECFieldFp = {
    fieldType: 'Fp',
    p: BigInt('0xffffffffffffffffffffffffffffffff000000000000000000000001')
  }
  let G: cryptoFramework.Point = {
    x: BigInt('0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'),
    y: BigInt('0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34')
  }
  let eccCommonSpec: cryptoFramework.ECCCommonParamsSpec = {
    algName: 'ECC',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    field: fieldFp,
    a: BigInt('0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'),
    b: BigInt('0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'),
    g: G,
    n: BigInt('0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d'),
    h: 1
  }
  return eccCommonSpec;
}

async function testgetAsyKeySpec() {
  let commKeySpec = genEccCommonSpec(); // 使用参数属性，构造ECC公私钥公共密钥参数对象。
  let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(commKeySpec); // 使用密钥参数对象创建生成器。
  let keyPair = await generatorBySpec.generateKeyPair();
  let key = keyPair.pubKey;
  let p = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FP_P_BN);
  console.info('ecc item --- p: ' + p.toString(16));
}
```

#### getEncodedDer12+

getEncodedDer(format: string): DataBlob

支持根据指定的密钥格式（如规范、压缩状态等），获取符合ASN.1语法和DER编码的公钥数据。目前仅支持ECC压缩和非压缩格式的公钥数据。


本接口和[Key.getEncoded()](#ZH-CN_TOPIC_0000002553201293__getencoded)的区别是：

1. 本接口可根据入参决定数据的输出格式。

1. [Key.getEncoded()](#ZH-CN_TOPIC_0000002553201293__getencoded)接口，不支持指定密钥格式，生成的数据格式与原始数据格式保持一致。（原始数据格式，指通过[convertKey](#ZH-CN_TOPIC_0000002553201293__convertkey-3)接口生成密钥对象时的数据格式）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| format | string | 是 | 用于指定当前密钥格式，取值仅支持"X509|COMPRESSED"和"X509|UNCOMPRESSED"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 返回满足ASN.1语法和DER编码的指定密钥格式的公钥数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGetEncodedDer() {
  let pkData = new Uint8Array([48, 90, 48, 20, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 9, 43, 36, 3, 3, 2, 8, 1, 1, 7, 3, 66, 0, 4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195, 157, 111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242, 206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152]);
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pkData };
  let generator = cryptoFramework.createAsyKeyGenerator('ECC_BrainPoolP256r1');
  let keyPair = await generator.convertKey(pubKeyBlob, null);
  let key = keyPair.pubKey;
  let returnBlob = key.getEncodedDer('X509|UNCOMPRESSED');
  console.info('returnBlob data：' + returnBlob.data);
}
```

#### getEncodedPem12+

getEncodedPem(format: string): string

同步方法，获取密钥数据的字符串。密钥可以是RSA公钥或私钥。公钥需符合X.509、PKCS#1规范，并采用PEM编码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| format | string | 是 | 指定的获取密钥字符串的编码格式。其中，公钥可为'PKCS1' 或'X509'格式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 用于获取指定密钥格式的具体内容。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let publicPkcs1Str1024: string  =
  '-----BEGIN RSA PUBLIC KEY-----\n'
    + 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n'
    + 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n'
    + 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n'
    + '-----END RSA PUBLIC KEY-----\n';

function TestPubKeyPkcs1ToX509BySync1024() {
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertPemKeySync(publicPkcs1Str1024, null);
  let pubPemKey = keyPair.pubKey;
  let pubString = pubPemKey.getEncodedPem('X509');
  console.info('[sync]TestPubKeyPkcs1ToX509BySync1024 pubString output = ' + pubString);
}
```

#### PriKey

私钥，是[Key](#ZH-CN_TOPIC_0000002553201293__key)的子类，在非对称加解密、签名、密钥协商时需要将其作为输入使用。

私钥可以通过非对称密钥生成器[AsyKeyGenerator](#ZH-CN_TOPIC_0000002553201293__asykeygenerator)、[AsyKeyGeneratorBySpec](#ZH-CN_TOPIC_0000002553201293__asykeygeneratorbyspec10)来生成。

#### clearMem

clearMem(): void

同步方法，清零系统底层内存中的密钥内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testClearMem() {
  let eccGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
    // 使用密钥生成器随机生成非对称密钥对。
    let keyGenPromise = eccGenerator.generateKeyPair();
    keyGenPromise.then(keyPair => {
      let priKey = keyPair.priKey;
      let returnBlob = priKey.getEncodedDer('PKCS8');
      console.info('returnBlob data：' + returnBlob.data);
      priKey.clearMem(); // 对于非对称私钥，clearMem()释放内部密钥结构。执行clearMem后，不支持getEncoded()。
    });
}
```

#### getAsyKeySpec10+

getAsyKeySpec(itemType: AsyKeySpecItem): bigint | string | number

同步方法，获取密钥参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemType | AsyKeySpecItem | 是 | 指定的密钥参数类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| bigint | string | number | 用于查看密钥参数的具体内容。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
// 根据关键规范构造EccCommonSpec结构体。EccCommonSpec结构体定义了ECC私钥和公钥的公共参数。
function genEccCommonSpec(): cryptoFramework.ECCCommonParamsSpec {
  let fieldFp: cryptoFramework.ECFieldFp = {
    fieldType: 'Fp',
    p: BigInt('0xffffffffffffffffffffffffffffffff000000000000000000000001')
  }
  let G: cryptoFramework.Point = {
    x: BigInt('0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'),
    y: BigInt('0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34')
  }
  let eccCommonSpec: cryptoFramework.ECCCommonParamsSpec = {
    algName: 'ECC',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    field: fieldFp,
    a: BigInt('0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'),
    b: BigInt('0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'),
    g: G,
    n: BigInt('0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d'),
    h: 1
  }
  return eccCommonSpec;
}

async function testgetAsyKeySpec() {
  let commKeySpec = genEccCommonSpec(); // 使用参数属性，构造ECC公私钥公共密钥参数对象。
  let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(commKeySpec); // 使用密钥参数对象创建生成器。
  let keyPair = await generatorBySpec.generateKeyPair();
  let key = keyPair.priKey;
  let p = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FP_P_BN);
  console.info('ecc item --- p: ' + p.toString(16));
}
```

#### getEncodedDer12+

getEncodedDer(format: string): DataBlob

支持根据指定的密钥格式（如采用哪个规范），获取满足ASN.1语法、DER编码的私钥数据。当前仅支持获取PKCS8格式的ecc私钥数据。


本接口和[Key.getEncoded()](#ZH-CN_TOPIC_0000002553201293__getencoded)的区别是：

1. 本接口可根据入参决定数据的输出格式，当前支持获取PKCS8格式的ecc私钥数据。

1. [Key.getEncoded()](#ZH-CN_TOPIC_0000002553201293__getencoded)接口，不支持指定密钥格式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| format | string | 是 | 用于指定当前密钥格式，取值当前仅支持"PKCS8"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 返回满足ASN.1语法和DER编码的指定密钥格式的ECC私钥数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGetEncodedDer() {
  let eccGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
    // 使用密钥生成器随机生成非对称密钥对。
    let keyGenPromise = eccGenerator.generateKeyPair();
    keyGenPromise.then(keyPair => {
      let priKey = keyPair.priKey;
      let returnBlob = priKey.getEncodedDer('PKCS8');
      console.info('returnBlob data：' + returnBlob.data);
    });
}
```

#### getEncodedPem12+

getEncodedPem(format: string): string

同步方法，获取密钥数据的字符串。密钥可以是RSA公钥或私钥。私钥格式需符合PKCS#8、PKCS#1规范，并采用PEM编码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| format | string | 是 | 指定的获取密钥字符串的编码格式。其中，私钥可为'PKCS1' 或'PKCS8'格式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 用于获取指定密钥格式的具体内容。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let priKeyPkcs1Str1024: string  =
  '-----BEGIN RSA PRIVATE KEY-----\n'
    + 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n'
    + 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n'
    + 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n'
    + 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n'
    + 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n'
    + '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n'
    + 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n'
    + 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n'
    + 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n'
    + 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n'
    + 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n'
    + 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n'
    + 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n'
    + '-----END RSA PRIVATE KEY-----\n';

function TestPriKeyPkcs1ToPkcs8BySync1024() {
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertPemKeySync(null, priKeyPkcs1Str1024);
  let priPemKey = keyPair.priKey;
  let priString = priPemKey.getEncodedPem('PKCS8');
  console.info('[sync]TestPriKeyPkcs1ToPkcs8BySync1024 priString output = ' + priString);
}
```

#### getEncodedPem18+

getEncodedPem(format: string, config: KeyEncodingConfig): string

同步方法，获取密钥数据的字符串。支持RSA公钥和私钥。私钥格式满足PKCS#8规范、PKCS#1规范和PEM编码方式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| format | string | 是 | 指定的获取密钥字符串的编码格式。其中，私钥可为'PKCS1' 或'PKCS8'格式。 |
| config | KeyEncodingConfig | 是 | 指定编码的算法跟口令，对私钥进行编码操作。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 用于获取指定密钥格式的具体内容。如果填了config参数，则获取编码后的内容。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let priKeyPkcs1Str1024: string  =
  '-----BEGIN RSA PRIVATE KEY-----\n'
    + 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n'
    + 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n'
    + 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n'
    + 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n'
    + 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n'
    + '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n'
    + 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n'
    + 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n'
    + 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n'
    + 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n'
    + 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n'
    + 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n'
    + 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n'
    + '-----END RSA PRIVATE KEY-----\n';

function TestPriKeyPkcs1Encoded() {
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertPemKeySync(null, priKeyPkcs1Str1024);
  let options : cryptoFramework.KeyEncodingConfig = {
    password: '123456',
    cipherName: 'AES-128-CBC'
  }
  let priPemKey = keyPair.priKey;
  let priString = priPemKey.getEncodedPem('PKCS1', options);
  console.info('[sync]TestPriKeyPkcs1Encoded priString output = ' + priString);
}
```

**getPubKey23+**

getPubKey(): Promise<PubKey>

从私钥对象中获取公钥对象。使用Promise异步回调。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.CryptoFramework.Key.AsymKey

返回值：

| 类型 | 说明 |
| --- | --- |
| Promise<PubKey> | Promise对象，返回公钥对象。 |

错误码：

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

示例：

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function compareUint8Array(a: Uint8Array, b: Uint8Array): boolean {
  let buf1 = buffer.from(a);
  let buf2 = buffer.from(b);
  if (buf1.compare(buf2, 0, b.length, 0, a.length) == 0) {
    return true;
  } else {
    return false;
  }

async function generateAsyKey() {
  let skData =
    new Uint8Array([48, 130, 2, 119, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 97, 48,
      130, 2, 93, 2, 1, 0, 2, 129, 129, 0, 199, 32, 218, 8, 4, 63, 103, 229, 64, 128, 83, 31, 23, 156, 30, 168, 101, 22,
      80, 100, 197, 243, 217, 60, 127, 110, 127, 242, 8, 251, 87, 127, 235, 38, 226, 149, 149, 108, 54, 202, 53, 1, 21,
      91, 118, 246, 97, 93, 147, 117, 162, 71, 215, 70, 9, 175, 205, 241, 230, 187, 64, 170, 154, 67, 67, 254, 71, 1,
      114, 10, 91, 195, 34, 199, 85, 172, 255, 87, 95, 159, 43, 117, 73, 73, 199, 97, 198, 117, 217, 7, 188, 196, 30,
      248, 9, 181, 150, 243, 41, 145, 91, 8, 226, 161, 251, 12, 120, 28, 36, 146, 3, 196, 48, 243, 136, 201, 207, 131,
      171, 22, 15, 7, 12, 172, 135, 196, 30, 93, 2, 3, 1, 0, 1, 2, 129, 128, 109, 100, 83, 194, 225, 170, 127, 134, 6,
      184, 56, 113, 181, 67, 179, 231, 232, 152, 168, 147, 163, 215, 193, 56, 165, 252, 235, 86, 232, 174, 67, 52, 103,
      215, 149, 212, 125, 32, 212, 188, 162, 255, 180, 94, 233, 236, 146, 50, 153, 6, 159, 158, 253, 217, 97, 10, 238,
      133, 124, 174, 211, 232, 165, 19, 100, 186, 218, 62, 46, 124, 30, 19, 251, 3, 206, 105, 255, 236, 224, 178, 148,
      103, 44, 132, 71, 83, 28, 221, 27, 189, 72, 44, 59, 253, 139, 232, 234, 14, 112, 121, 43, 142, 193, 179, 140, 200,
      97, 234, 110, 63, 205, 24, 88, 116, 86, 184, 8, 19, 254, 204, 77, 84, 66, 238, 240, 69, 72, 21, 2, 65, 0, 233,
      103, 239, 11, 215, 10, 103, 66, 46, 155, 193, 79, 37, 64, 90, 12, 167, 189, 129, 8, 131, 94, 195, 8, 210, 236, 87,
      158, 140, 2, 82, 105, 80, 253, 13, 26, 140, 202, 194, 117, 59, 57, 197, 108, 50, 20, 46, 89, 248, 132, 120, 30,
      149, 180, 135, 134, 196, 156, 160, 123, 38, 253, 15, 7, 2, 65, 0, 218, 103, 122, 117, 154, 149, 213, 110, 24, 149,
      175, 208, 136, 249, 88, 91, 89, 180, 30, 243, 69, 130, 97, 252, 177, 216, 55, 46, 67, 15, 124, 56, 113, 57, 242,
      233, 185, 193, 254, 218, 76, 165, 184, 16, 109, 190, 93, 195, 227, 37, 58, 110, 243, 142, 152, 252, 226, 91, 59,
      145, 218, 35, 106, 123, 2, 65, 0, 210, 131, 88, 58, 32, 144, 148, 131, 63, 144, 97, 112, 165, 211, 125, 164, 110,
      97, 224, 16, 50, 148, 116, 105, 239, 251, 20, 39, 190, 117, 149, 168, 193, 80, 10, 210, 136, 107, 147, 169, 178,
      106, 47, 162, 159, 36, 78, 141, 253, 52, 85, 54, 152, 165, 131, 154, 204, 151, 203, 178, 103, 126, 212, 95, 2, 65,
      0, 193, 254, 80, 3, 205, 255, 112, 200, 142, 5, 199, 88, 207, 145, 203, 45, 185, 12, 8, 193, 196, 231, 254, 233,
      89, 126, 215, 228, 187, 164, 49, 142, 96, 228, 60, 35, 230, 223, 173, 227, 113, 89, 113, 153, 6, 33, 165, 95, 173,
      143, 15, 204, 37, 130, 111, 217, 143, 165, 193, 207, 215, 150, 197, 169, 2, 64, 7, 37, 152, 14, 232, 168, 102,
      169, 167, 97, 161, 33, 86, 178, 77, 140, 12, 114, 78, 129, 47, 103, 87, 217, 177, 80, 156, 91, 240, 149, 254, 90,
      69, 232, 10, 56, 232, 63, 59, 148, 254, 101, 63, 146, 66, 96, 25, 31, 37, 154, 77, 145, 201, 213, 122, 245, 90,
      251, 219, 42, 131, 248, 148, 151
  ])
  let expectPkdata =
    new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 199, 32, 218, 8, 4, 63, 103, 229, 64, 128, 83, 31, 23, 156, 30, 168, 101, 22, 80, 100, 197, 243,
      217, 60, 127, 110, 127, 242, 8, 251, 87, 127, 235, 38, 226, 149, 149, 108, 54, 202, 53, 1, 21, 91, 118, 246, 97,
      93, 147, 117, 162, 71, 215, 70, 9, 175, 205, 241, 230, 187, 64, 170, 154, 67, 67, 254, 71, 1, 114, 10, 91, 195,
      34, 199, 85, 172, 255, 87, 95, 159, 43, 117, 73, 73, 199, 97, 198, 117, 217, 7, 188, 196, 30, 248, 9, 181, 150,
      243, 41, 145, 91, 8, 226, 161, 251, 12, 120, 28, 36, 146, 3, 196, 48, 243, 136, 201, 207, 131, 171, 22, 15, 7, 12,
      172, 135, 196, 30, 93, 2, 3, 1, 0, 1
  ])
  let skDataBlob: cryptoFramework.DataBlob = { data: skData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  try {
    let keyPair = rsaGenerator.convertKeySync(null, skDataBlob);
    let priKey = keyPair.priKey;
    let pubkey = await priKey.getPubKey();
    let pkBlob = pubkey.getEncoded();
    console.info('pk1 bin data ' + pkBlob.data);
    let ret: boolean = compareUint8Array(pkBlob.data, expectPkdata);
    console.info('result = ' + ret);
  } catch (e) {
    console.error(`get pubkey from prikey failed, ${e.code}, ${e.message}`);
  }
```

**getPubKeySync23+**

getPubKeySync(): PubKey

以同步方式，从私钥对象中获取公钥对象。

元服务API： 从API version 23开始，该接口支持在元服务中使用。

系统能力： SystemCapability.Security.CryptoFramework.Key.AsymKey

返回值：

| 类型 | 说明 |
| --- | --- |
| PubKey | 公钥对象。 |

错误码：

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

示例：

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function compareUint8Array(a: Uint8Array, b: Uint8Array): boolean {
  let buf1 = buffer.from(a);
  let buf2 = buffer.from(b);
  if (buf1.compare(buf2, 0, b.length, 0, a.length) == 0) {
    return true;
  } else {
    return false;
  }

function generateAsyKey() {
  let skData =
    new Uint8Array([48, 130, 2, 119, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 97, 48,
      130, 2, 93, 2, 1, 0, 2, 129, 129, 0, 199, 32, 218, 8, 4, 63, 103, 229, 64, 128, 83, 31, 23, 156, 30, 168, 101, 22,
      80, 100, 197, 243, 217, 60, 127, 110, 127, 242, 8, 251, 87, 127, 235, 38, 226, 149, 149, 108, 54, 202, 53, 1, 21,
      91, 118, 246, 97, 93, 147, 117, 162, 71, 215, 70, 9, 175, 205, 241, 230, 187, 64, 170, 154, 67, 67, 254, 71, 1,
      114, 10, 91, 195, 34, 199, 85, 172, 255, 87, 95, 159, 43, 117, 73, 73, 199, 97, 198, 117, 217, 7, 188, 196, 30,
      248, 9, 181, 150, 243, 41, 145, 91, 8, 226, 161, 251, 12, 120, 28, 36, 146, 3, 196, 48, 243, 136, 201, 207, 131,
      171, 22, 15, 7, 12, 172, 135, 196, 30, 93, 2, 3, 1, 0, 1, 2, 129, 128, 109, 100, 83, 194, 225, 170, 127, 134, 6,
      184, 56, 113, 181, 67, 179, 231, 232, 152, 168, 147, 163, 215, 193, 56, 165, 252, 235, 86, 232, 174, 67, 52, 103,
      215, 149, 212, 125, 32, 212, 188, 162, 255, 180, 94, 233, 236, 146, 50, 153, 6, 159, 158, 253, 217, 97, 10, 238,
      133, 124, 174, 211, 232, 165, 19, 100, 186, 218, 62, 46, 124, 30, 19, 251, 3, 206, 105, 255, 236, 224, 178, 148,
      103, 44, 132, 71, 83, 28, 221, 27, 189, 72, 44, 59, 253, 139, 232, 234, 14, 112, 121, 43, 142, 193, 179, 140, 200,
      97, 234, 110, 63, 205, 24, 88, 116, 86, 184, 8, 19, 254, 204, 77, 84, 66, 238, 240, 69, 72, 21, 2, 65, 0, 233,
      103, 239, 11, 215, 10, 103, 66, 46, 155, 193, 79, 37, 64, 90, 12, 167, 189, 129, 8, 131, 94, 195, 8, 210, 236, 87,
      158, 140, 2, 82, 105, 80, 253, 13, 26, 140, 202, 194, 117, 59, 57, 197, 108, 50, 20, 46, 89, 248, 132, 120, 30,
      149, 180, 135, 134, 196, 156, 160, 123, 38, 253, 15, 7, 2, 65, 0, 218, 103, 122, 117, 154, 149, 213, 110, 24, 149,
      175, 208, 136, 249, 88, 91, 89, 180, 30, 243, 69, 130, 97, 252, 177, 216, 55, 46, 67, 15, 124, 56, 113, 57, 242,
      233, 185, 193, 254, 218, 76, 165, 184, 16, 109, 190, 93, 195, 227, 37, 58, 110, 243, 142, 152, 252, 226, 91, 59,
      145, 218, 35, 106, 123, 2, 65, 0, 210, 131, 88, 58, 32, 144, 148, 131, 63, 144, 97, 112, 165, 211, 125, 164, 110,
      97, 224, 16, 50, 148, 116, 105, 239, 251, 20, 39, 190, 117, 149, 168, 193, 80, 10, 210, 136, 107, 147, 169, 178,
      106, 47, 162, 159, 36, 78, 141, 253, 52, 85, 54, 152, 165, 131, 154, 204, 151, 203, 178, 103, 126, 212, 95, 2, 65,
      0, 193, 254, 80, 3, 205, 255, 112, 200, 142, 5, 199, 88, 207, 145, 203, 45, 185, 12, 8, 193, 196, 231, 254, 233,
      89, 126, 215, 228, 187, 164, 49, 142, 96, 228, 60, 35, 230, 223, 173, 227, 113, 89, 113, 153, 6, 33, 165, 95, 173,
      143, 15, 204, 37, 130, 111, 217, 143, 165, 193, 207, 215, 150, 197, 169, 2, 64, 7, 37, 152, 14, 232, 168, 102,
      169, 167, 97, 161, 33, 86, 178, 77, 140, 12, 114, 78, 129, 47, 103, 87, 217, 177, 80, 156, 91, 240, 149, 254, 90,
      69, 232, 10, 56, 232, 63, 59, 148, 254, 101, 63, 146, 66, 96, 25, 31, 37, 154, 77, 145, 201, 213, 122, 245, 90,
      251, 219, 42, 131, 248, 148, 151
    ])
  let expectPkdata =
    new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 199, 32, 218, 8, 4, 63, 103, 229, 64, 128, 83, 31, 23, 156, 30, 168, 101, 22, 80, 100, 197, 243,
      217, 60, 127, 110, 127, 242, 8, 251, 87, 127, 235, 38, 226, 149, 149, 108, 54, 202, 53, 1, 21, 91, 118, 246, 97,
      93, 147, 117, 162, 71, 215, 70, 9, 175, 205, 241, 230, 187, 64, 170, 154, 67, 67, 254, 71, 1, 114, 10, 91, 195,
      34, 199, 85, 172, 255, 87, 95, 159, 43, 117, 73, 73, 199, 97, 198, 117, 217, 7, 188, 196, 30, 248, 9, 181, 150,
      243, 41, 145, 91, 8, 226, 161, 251, 12, 120, 28, 36, 146, 3, 196, 48, 243, 136, 201, 207, 131, 171, 22, 15, 7, 12,
      172, 135, 196, 30, 93, 2, 3, 1, 0, 1
    ])
  let skDataBlob: cryptoFramework.DataBlob = { data: skData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  try {
    let keyPair = rsaGenerator.convertKeySync(null, skDataBlob);
    let priKey = keyPair.priKey;
    let pubkey = priKey.getPubKeySync();
    let pkBlob = pubkey.getEncoded();
    console.info('pk1 bin data' + pkBlob.data);
    let ret: boolean = compareUint8Array(pkBlob.data, expectPkdata);
    console.info('result = ' + ret);
  } catch (e) {
    console.error(`get pubkey from prikey failed, ${e.code}, ${e.message}`);
}
```

#### KeyPair

非对称密钥对包含公钥和私钥。

可以通过非对称密钥生成器[AsyKeyGenerator](#ZH-CN_TOPIC_0000002553201293__asykeygenerator)、[AsyKeyGeneratorBySpec](#ZH-CN_TOPIC_0000002553201293__asykeygeneratorbyspec10)来生成。


KeyPair对象中的pubKey对象和priKey对象是KeyPair对象的成员。当KeyPair对象超出作用域时，其内部的pubKey对象和priKey对象将被析构。

业务方使用时应持有KeyPair对象的引用，而非内部pubKey或priKey对象的引用。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| priKey | PriKey | 是 | 否 | 私钥。 |
| pubKey | PubKey | 是 | 否 | 公钥。 |

#### cryptoFramework.createSymKeyGenerator

createSymKeyGenerator(algName: string): SymKeyGenerator

通过指定算法名称获取相应的对称密钥生成器实例。

支持的规格详见[对称密钥生成和转换规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.SymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algName | string | 是 | 待生成对称密钥生成器的算法名称。 具体取值详见对称密钥生成和转换规格一节中的“字符串参数”。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SymKeyGenerator | 返回对称密钥生成器的对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
801this operation is not supported.

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
```

#### SymKeyGenerator

对称密钥生成器。

在使用该类的方法前，先使用[createSymKeyGenerator](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatesymkeygenerator)构建SymKeyGenerator实例。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.SymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 是 | 否 | 对称密钥生成器指定的算法名称。 |

#### generateSymKey

generateSymKey(callback: AsyncCallback<SymKey>): void

获取对称密钥生成器随机生成的密钥。使用callback异步回调。

必须在使用[createSymKeyGenerator](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatesymkeygenerator)创建对称密钥生成器后，才能使用本函数。

目前支持使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。


对于HMAC算法的对称密钥，如果在创建对称密钥生成器时指定了具体哈希算法（如“HMAC|SHA256”），则会随机生成与哈希长度一致的二进制密钥数据（如256位的密钥数据）。如果未指定具体哈希算法，如仅指定“HMAC”，则不支持随机生成对称密钥数据，可通过[convertKey](#ZH-CN_TOPIC_0000002553201293__convertkey)方式生成对称密钥数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.SymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<SymKey> | 是 | 回调函数。当生成对称密钥成功，err为undefined，data为获取到的SymKey；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  symKeyGenerator.generateSymKey((err, symKey) => {
    console.info('Generate symKey result: success, algName：' + symKey.algName);
  });
```

#### generateSymKey

generateSymKey(): Promise<SymKey>

获取该对称密钥生成器随机生成的密钥。使用Promise异步回调。

必须在使用[createSymKeyGenerator](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatesymkeygenerator)创建对称密钥生成器后，才能使用本函数。

目前支持使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.SymKey。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<SymKey> | Promise对象，返回对称密钥SymKey。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  symKeyGenerator.generateSymKey()
    .then(symKey => {
      console.info('Generate symKey result: success, algName: ' + symKey.algName);
    }).catch((error: BusinessError) => {
      console.error(`Generate symKey failed, ${error.code}, ${error.message}`);
    });
```

#### generateSymKeySync12+

generateSymKeySync(): SymKey

同步获取对称密钥生成器随机生成的密钥。

必须在使用[createSymKeyGenerator](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatesymkeygenerator)创建对称密钥生成器后，才能使用本函数。

目前支持使用OpenSSL的RAND_priv_bytes()作为底层能力生成随机密钥。

对于HMAC算法的对称密钥，如果已经在创建对称密钥生成器时指定了具体哈希算法（如指定“HMAC|SHA256”），则会随机生成与哈希长度一致的二进制密钥数据（如指定“HMAC|SHA256”会随机生成256位的密钥数据）。

如果在创建对称密钥生成器时没有指定具体哈希算法，如仅指定“HMAC”，则不支持随机生成对称密钥数据，可通过[convertKeySync](#ZH-CN_TOPIC_0000002553201293__convertkeysync12)方式生成对称密钥数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SymKey | 返回对称密钥SymKey。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testGenerateSymKeySync() {
  // 创建SymKeyGenerator实例。
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  // 使用密钥生成器随机生成对称密钥。
  let key = symKeyGenerator.generateSymKeySync();
  let encodedKey = key.getEncoded();
  console.info('key hex:' + encodedKey.data);
}
```

#### convertKey

convertKey(key: DataBlob, callback: AsyncCallback<SymKey>): void

根据指定数据生成对称密钥。使用callback异步回调。

必须在使用[createSymKeyGenerator](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatesymkeygenerator)创建对称密钥生成器后，才能使用本函数。


对于HMAC算法的对称密钥，如果已经在创建对称密钥生成器时指定了具体哈希算法（如指定“HMAC|SHA256”），则需要传入与哈希长度一致的二进制密钥数据（如传入SHA256对应256位的密钥数据）。

如果在创建对称密钥生成器时没有指定具体哈希算法，如仅指定“HMAC”，则支持传入长度在[1,4096]范围内（单位为byte）的任意二进制密钥数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.SymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | DataBlob | 是 | 指定的对称密钥材料。 |
| callback | AsyncCallback<SymKey> | 是 | 回调函数。当生成对称密钥成功，err为undefined，data为获取到的SymKey；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
17620001memory operation failed.

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function genKeyMaterialBlob(): cryptoFramework.DataBlob {
  let arr = [
    0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56,
    0xad, 0x47, 0xfc, 0x5a, 0x46, 0x39, 0xee, 0x7c,
    0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72]; // keyLen = 192 (24 bytes)
  let keyMaterial = new Uint8Array(arr);
  return { data: keyMaterial };
}

function testConvertKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  let keyMaterialBlob = genKeyMaterialBlob();
  symKeyGenerator.convertKey(keyMaterialBlob, (err, symKey) => {
    console.info('Convert symKey result: success, algName: ' + symKey.algName);
  });
}
```

#### convertKey

convertKey(key: DataBlob): Promise<SymKey>

根据指定数据生成对称密钥。使用Promise异步回调。

在使用本函数前，需先通过[createSymKeyGenerator](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatesymkeygenerator)创建对称密钥生成器。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.SymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | DataBlob | 是 | 指定的密钥材料数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<SymKey> | Promise对象，返回对称密钥SymKey。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
17620001memory operation failed.

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function genKeyMaterialBlob(): cryptoFramework.DataBlob {
  let arr = [
    0xba, 0x3d, 0xc2, 0x71, 0x21, 0x1e, 0x30, 0x56,
    0xad, 0x47, 0xfc, 0x5a, 0x46, 0x39, 0xee, 0x7c,
    0xba, 0x3b, 0xc2, 0x71, 0xab, 0xa0, 0x30, 0x72]; // keyLen = 192 (24 bytes)
  let keyMaterial = new Uint8Array(arr);
  return { data: keyMaterial };
}

function testConvertKey() {
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('3DES192');
  let keyMaterialBlob = genKeyMaterialBlob();
  symKeyGenerator.convertKey(keyMaterialBlob)
    .then(symKey => {
      console.info('Convert symKey result: success, algName：' + symKey.algName);
    }).catch((error: BusinessError) => {
      console.error(`Convert symKey failed, ${error.code}, ${error.message}`);
    });
}
```

#### convertKeySync12+

convertKeySync(key: DataBlob): SymKey

根据指定数据生成对称密钥。

必须在使用[createSymKeyGenerator](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatesymkeygenerator)创建对称密钥生成器后，才能使用本函数。


对于HMAC算法的对称密钥，如果在创建对称密钥生成器时指定了具体哈希算法（如“HMAC|SHA256”），则需要传入与哈希长度一致的二进制密钥数据（如SHA256对应的256位密钥数据）。如果在创建对称密钥生成器时未指定具体哈希算法，如仅指定“HMAC”，则支持传入长度在1到4096字节范围内的任意二进制密钥数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.SymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | DataBlob | 是 | 指定的对称密钥材料。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SymKey | 对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
17620001memory operation failed.

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function testConvertKeySync() {
  // 对称密钥长度为64字节，512比特。
  let keyMessage = '87654321abcdefgh87654321abcdefgh87654321abcdefgh87654321abcdefgh';
  let keyBlob: cryptoFramework.DataBlob = {
    data : new Uint8Array(buffer.from(keyMessage, 'utf-8').buffer)
  }
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('HMAC');
  let key = symKeyGenerator.convertKeySync(keyBlob);
  let encodedKey = key.getEncoded();
  console.info('key encoded data：' + encodedKey.data);
}
```

#### cryptoFramework.createAsyKeyGenerator

createAsyKeyGenerator(algName: string): AsyKeyGenerator

通过指定算法名称的字符串，获取相应的非对称密钥生成器实例。

支持的规格详见[非对称密钥生成和转换规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algName | string | 是 | 非对称密钥生成支持的算法名。详见非对称密钥生成和转换规格中的字符串参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AsyKeyGenerator | 返回非对称密钥生成器。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
```

#### AsyKeyGenerator

非对称密钥生成器。在使用该类的方法前，需要先使用createAsyKeyGenerator()方法构建一个AsyKeyGenerator实例。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 是 | 否 | 非对称密钥生成器指定的算法名称。 |

#### generateKeyPair

generateKeyPair(callback: AsyncCallback<KeyPair>): void

获取非对称密钥生成器随机生成的密钥。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<KeyPair> | 是 | 回调函数，用于获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: Incorrect parameter types; |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
asyKeyGenerator.generateKeyPair((err, keyPair) => {
  if (err) {
    console.error('generateKeyPair result: fail.');
    return;
  }
  console.info('generateKeyPair result: success.');
})
```

#### generateKeyPair

generateKeyPair(): Promise<KeyPair>

获取非对称密钥生成器随机生成的密钥。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KeyPair> | 使用Promise的方式获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
let keyGenPromise = asyKeyGenerator.generateKeyPair();
keyGenPromise.then(keyPair => {
  console.info('generateKeyPair result: success.');
}).catch((error: BusinessError) => {
  console.error('generateKeyPair result: fail.');
});
```

#### generateKeyPairSync12+

generateKeyPairSync(): KeyPair

同步获取非对称密钥生成器随机生成的密钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**返回值：**

| 类型 | 说明 |
| --- | --- |
| KeyPair | 非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
try {
  let keyPairData = asyKeyGenerator.generateKeyPairSync();
  if (keyPairData != null) {
    console.info('[Sync]: key pair result: success.');
  } else {
    console.error('[Sync]: get key pair result: fail.');
  }
} catch (e) {
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### convertKey

convertKey(pubKey: DataBlob | null, priKey: DataBlob | null, callback: AsyncCallback<KeyPair>): void

获取指定数据生成非对称密钥。使用callback异步回调。详情请看下方密钥转换说明。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pubKey | DataBlob | null10+ | 是 | 指定的公钥材料。如果公钥不需要转换，请传入null。API 10之前只支持DataBlob， API 10之后增加支持null。 |
| priKey | DataBlob | null10+ | 是 | 指定的私钥材料。如果私钥不需要转换，请传入null。API 10之前只支持DataBlob， API 10之后增加支持null。 |
| callback | AsyncCallback<KeyPair> | 是 | 回调函数，用于获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let pubKeyArray =
  new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
    83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
    105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235,
    215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]);
let priKeyArray =
  new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171, 57,
    10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7]);
let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray }; // 公钥二进制数据。
let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray }; // 私钥二进制数据。
let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
asyKeyGenerator.convertKey(pubKeyBlob, priKeyBlob, (err, keyPair) => {
  if (err) {
    console.error('convertKey result: fail.');
    return;
  }
  console.info('convertKey result: success.');
});
```

#### convertKey

convertKey(pubKey: DataBlob | null, priKey: DataBlob | null): Promise<KeyPair>

获取指定数据生成非对称密钥。使用Promise异步回调。详情请看下方密钥转换说明。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pubKey | DataBlob | null10+ | 是 | 指定的公钥材料。如果公钥不需要转换，请传入null。API 10之前只支持DataBlob， API 10之后增加支持null。 |
| priKey | DataBlob | null10+ | 是 | 指定的私钥材料。如果私钥不需要转换，请传入null。API 10之前只支持DataBlob， API 10之后增加支持null。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KeyPair> | 使用Promise的方式获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let pubKeyArray =
  new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
    83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
    105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235,
    215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]);
let priKeyArray =
  new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171, 57,
    10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7]);
let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray }; // 公钥二进制数据。
let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray }; // 私钥二进制数据。
let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
let keyGenPromise = asyKeyGenerator.convertKey(pubKeyBlob, priKeyBlob);
keyGenPromise.then(keyPair => {
  console.info('convertKey result: success.');
}).catch((error: BusinessError) => {
  console.error(`convertKey failed, errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### convertKeySync12+

convertKeySync(pubKey: DataBlob | null, priKey: DataBlob | null): KeyPair

同步获取指定数据生成非对称密钥。详情请看下方**密钥转换说明**。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pubKey | DataBlob | null10+ | 是 | 指定公钥材料。如果公钥无需转换，请传入null。API 10前仅支持DataBlob，API 10起支持传入null。 |
| priKey | DataBlob | null10+ | 是 | 指定私钥材料。如果私钥无需转换，请传入null。API 10前仅支持DataBlob，API 10起支持传入null。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| KeyPair | 非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let pubKeyArray =
  new Uint8Array([48, 89, 48, 19, 6, 7, 42, 134, 72, 206, 61, 2, 1, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7, 3, 66, 0, 4,
    83, 96, 142, 9, 86, 214, 126, 106, 247, 233, 92, 125, 4, 128, 138, 105, 246, 162, 215, 71, 81, 58, 202, 121, 26,
    105, 211, 55, 130, 45, 236, 143, 55, 16, 248, 75, 167, 160, 167, 106, 2, 152, 243, 44, 68, 66, 0, 167, 99, 92, 235,
    215, 159, 239, 28, 106, 124, 171, 34, 145, 124, 174, 57, 92]);
let priKeyArray =
  new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56, 137, 35, 207, 0, 60, 191, 90, 61, 136, 105, 210, 16, 27, 4, 171, 57,
    10, 61, 123, 40, 189, 28, 34, 207, 236, 22, 45, 223, 10, 189, 160, 10, 6, 8, 42, 134, 72, 206, 61, 3, 1, 7]);
let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyArray }; // 公钥二进制数据。
let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyArray }; // 私钥二进制数据。
let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
try {
  let keyPairData = asyKeyGenerator.convertKeySync(pubKeyBlob, priKeyBlob);
  if (keyPairData != null) {
    console.info('[Sync]: key pair result: success.');
  } else {
    console.error('[Sync]: convert key pair result: fail.');
  }
} catch (e) {
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

**密钥转换说明**

1. 非对称密钥（RSA、ECC、DSA）的公钥和私钥调用 getEncoded() 方法后，分别返回 X.509 格式的二进制数据和 PKCS#8 格式的二进制数据。对于 ECC 私钥，返回的是 RFC5915 定义的格式。这些数据可用于跨应用传输或持久化存储。
1. 当调用convertKey方法将外来二进制数据转换为算法库非对称密钥对象时，公钥应符合ASN.1语法、X.509规范和DER编码格式；私钥应符合ASN.1语法、PKCS#8规范和DER编码格式。
1. convertKey方法中，公钥和私钥二进制数据非必选项，可单独传入公钥或私钥的数据，生成对应只包含公钥或私钥的KeyPair对象。
1. convertKey或convertKeySync方法将外来二进制数据转换为算法库非对称密钥对象时，不会校验生成的密钥对象的规格与创建非对称密钥生成器时指定的密钥规格是否一致。

#### convertPemKey12+

convertPemKey(pubKey: string | null, priKey: string | null): Promise<KeyPair>

获取指定数据生成非对称密钥。使用Promise异步回调。


1. 当调用convertPemKey方法将外来字符串数据转换为算法库非对称密钥对象时，公钥应满足ASN.1语法、X.509规范、PEM编码格式，私钥应满足ASN.1语法、PKCS#8规范、PEM编码格式。
1. convertPemKey方法中，公钥和私钥字符串数据为非必选项，可单独传入公钥或私钥的数据，生成对应只包含公钥或私钥的KeyPair对象。
1. convertPemKey方法将外来字符串数据转换为算法库非对称密钥对象时，不会校验生成的密钥对象的规格与创建非对称密钥生成器时指定的密钥规格是否一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pubKey | string | null | 是 | 指定的公钥材料。如果公钥不需要转换，请传入null。 |
| priKey | string | null | 是 | 指定的私钥材料。如果私钥不需要转换，请传入null。 说明：公钥和私钥材料不能同时为null或空字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KeyPair> | 使用Promise的方式获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let priKeyPkcs1Str1024: string  =
  '-----BEGIN RSA PRIVATE KEY-----\n'
    + 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n'
    + 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n'
    + 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n'
    + 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n'
    + 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n'
    + '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n'
    + 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n'
    + 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n'
    + 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n'
    + 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n'
    + 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n'
    + 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n'
    + 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n'
    + '-----END RSA PRIVATE KEY-----\n';
let publicPkcs1Str1024: string  =
  '-----BEGIN RSA PUBLIC KEY-----\n'
    + 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n'
    + 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n'
    + 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n'
    + '-----END RSA PUBLIC KEY-----\n';

async function TestConvertPemKeyByPromise() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  asyKeyGenerator.convertPemKey(publicPkcs1Str1024, priKeyPkcs1Str1024)
    .then(keyPair => {
      console.info('convertPemKey result: success.');
  }).catch((error: BusinessError) => {
    console.error(`convertPemKey failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

#### convertPemKey18+

convertPemKey(pubKey: string | null, priKey: string | null, password: string): Promise<KeyPair>

获取指定数据生成非对称密钥。支持加密的私钥，同步传入私钥口令解密私钥。使用Promise异步回调。

1. 当调用convertPemKey方法将外来字符串数据转换为算法库非对称密钥对象时，公钥应满足ASN.1语法、X.509规范、PEM编码格式，私钥应满足ASN.1语法、PKCS#8规范、PEM编码格式。
1. convertPemKey方法中，公钥和私钥字符串数据为非必选项，可单独传入公钥或私钥的数据，生成对应只包含公钥或私钥的KeyPair对象。
1. convertPemKey方法将外来字符串数据转换为算法库非对称密钥对象时，不会校验生成的密钥对象的规格与创建非对称密钥生成器时指定的密钥规格是否一致。
1. password为口令，传入后可以解密加密后的私钥。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pubKey | string | null | 是 | 指定的公钥材料。如果公钥不需要转换，请传入null。 |
| priKey | string | null | 是 | 指定的私钥材料。如果私钥不需要转换，请传入null。 说明：公钥和私钥材料不能同时为null或空字符串。 |
| password | string | 是 | 指定口令，用于解密私钥。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KeyPair> | 使用Promise的方式获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let priKeyPkcs1EncodingStr : string =
  '-----BEGIN RSA PRIVATE KEY-----\n'
    + 'Proc-Type: 4,ENCRYPTED\n'
    + 'DEK-Info: AES-128-CBC,815A066131BF05CF87CE610A59CC69AE\n\n'
    + '7Jd0vmOmYGFZ2yRY8fqRl3+6rQlFtNcMILvcb5KWHDSrxA0ULmJE7CW0DSRikHoA\n'
    + 't0KgafhYXeQXh0dRy9lvVRAFSLHCLJVjchx90V7ZSivBFEq7+iTozVp4AlbgYsJP\n'
    + 'vx/1sfZD2WAcyMJ7IDmJyft7xnpVSXsyWGTT4f3eaHJIh1dqjwrso7ucAW0FK6rp\n'
    + '/TONyOoXNfXtRbVtxNyCWBxt4HCSclDZFvS9y8fz9ZwmCUV7jei/YdzyQI2wnE13\n'
    + 'W8cKlpzRFL6BWi8XPrUtAw5MWeHBAPUgPWMfcmiaeyi5BJFhQCrHLi+Gj4EEJvp7\n'
    + 'mP5cbnQAx6+paV5z9m71SKrI/WSc4ixsYYdVmlL/qwAK9YliFfoPl030YJWW6rFf\n'
    + 'T7J9BUlHGUJ0RB2lURNNLakM+UZRkeE9TByzCzgTxuQtyv5Lwsh2mAk3ia5x0kUO\n'
    + 'LHg3Eoabhdh+YZA5hHaxnpF7VjspB78E0F9Btq+A41rSJ6zDOdToHey4MJ2nxdey\n'
    + 'Z3bi81TZ6Fp4IuROrvZ2B/Xl3uNKR7n+AHRKnaAO87ywzyltvjwSh2y3xhJueiRs\n'
    + 'BiYkyL3/fnocD3pexTdN6h3JgQGgO5GV8zw/NrxA85mw8o9im0HreuFObmNj36T9\n'
    + 'k5N+R/QIXW83cIQOLaWK1ThYcluytf0tDRiMoKqULiaA6HvDMigExLxuhCtnoF8I\n'
    + 'iOLN1cPdEVQjzwDHLqXP2DbWW1z9iRepLZlEm1hLRLEmOrTGKezYupVv306SSa6J\n'
    + 'OA55lAeXMbyjFaYCr54HWrpt4NwNBX1efMUURc+1LcHpzFrBTTLbfjIyq6as49pH\n'
    + '-----END RSA PRIVATE KEY-----\n'

async function TestConvertPemKeyByPromise() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  asyKeyGenerator.convertPemKey(null, priKeyPkcs1EncodingStr, '123456')
    .then(keyPair => {
      console.info('convertPemKey result: success.');
  }).catch((error: BusinessError) => {
    console.error(`convertPemKey failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

#### convertPemKeySync12+

convertPemKeySync(pubKey: string | null, priKey: string | null): KeyPair

同步获取指定数据，生成非对称密钥。


convertPemKeySync接口与convertPemKey接口注意事项相同，见[convertPemKey](#ZH-CN_TOPIC_0000002553201293__convertpemkey12)接口说明。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pubKey | string | null | 是 | 指定的公钥材料。如果公钥不需要转换，请传入null。 |
| priKey | string | null | 是 | 指定私钥材料。私钥无需转换时，请传入null。 说明：公钥和私钥材料不能同时为null或空字符串。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| KeyPair | 非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let priKeyPkcs1Str1024: string  =
  '-----BEGIN RSA PRIVATE KEY-----\n'
    + 'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n'
    + 'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n'
    + 'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n'
    + 'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n'
    + 'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n'
    + '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n'
    + 'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n'
    + 'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n'
    + 'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n'
    + 'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n'
    + 'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n'
    + 'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n'
    + 'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n'
    + '-----END RSA PRIVATE KEY-----\n';
  let publicPkcs1Str1024: string  =
  '-----BEGIN RSA PUBLIC KEY-----\n'
    + 'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n'
    + 'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n'
    + 'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n'
    + '-----END RSA PUBLIC KEY-----\n';

function TestConvertPemKeyBySync() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  try {
    let keyPairData = asyKeyGenerator.convertPemKeySync(publicPkcs1Str1024, priKeyPkcs1Str1024);
    if (keyPairData != null) {
      console.info('[Sync]: convert pem key pair result: success.');
    } else {
      console.error('[Sync]: convert pem key pair result: fail.');
    }
  } catch (e) {
    console.error(`Sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### convertPemKeySync18+

convertPemKeySync(pubKey: string | null, priKey: string | null, password: string): KeyPair

获取指定数据生成非对称密钥。支持加密的私钥，同步传入私钥口令解密私钥。使用同步方法。


convertPemKeySync接口与convertPemKey接口注意事项相同，见[convertPemKey](#ZH-CN_TOPIC_0000002553201293__convertpemkey18)接口说明。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pubKey | string | null | 是 | 指定的公钥材料。如果公钥不需要转换，请传入null。 |
| priKey | string | null | 是 | 指定私钥材料。若无需转换，请传入 null。注意：公钥与私钥材料不可同时为 null。 |
| password | string | 是 | 指定口令，用于解密私钥。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| KeyPair | 非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let priKeyPkcs1EncodingStr : string =
  '-----BEGIN RSA PRIVATE KEY-----\n'
    + 'Proc-Type: 4,ENCRYPTED\n'
    + 'DEK-Info: AES-128-CBC,815A066131BF05CF87CE610A59CC69AE\n\n'
    + '7Jd0vmOmYGFZ2yRY8fqRl3+6rQlFtNcMILvcb5KWHDSrxA0ULmJE7CW0DSRikHoA\n'
    + 't0KgafhYXeQXh0dRy9lvVRAFSLHCLJVjchx90V7ZSivBFEq7+iTozVp4AlbgYsJP\n'
    + 'vx/1sfZD2WAcyMJ7IDmJyft7xnpVSXsyWGTT4f3eaHJIh1dqjwrso7ucAW0FK6rp\n'
    + '/TONyOoXNfXtRbVtxNyCWBxt4HCSclDZFvS9y8fz9ZwmCUV7jei/YdzyQI2wnE13\n'
    + 'W8cKlpzRFL6BWi8XPrUtAw5MWeHBAPUgPWMfcmiaeyi5BJFhQCrHLi+Gj4EEJvp7\n'
    + 'mP5cbnQAx6+paV5z9m71SKrI/WSc4ixsYYdVmlL/qwAK9YliFfoPl030YJWW6rFf\n'
    + 'T7J9BUlHGUJ0RB2lURNNLakM+UZRkeE9TByzCzgTxuQtyv5Lwsh2mAk3ia5x0kUO\n'
    + 'LHg3Eoabhdh+YZA5hHaxnpF7VjspB78E0F9Btq+A41rSJ6zDOdToHey4MJ2nxdey\n'
    + 'Z3bi81TZ6Fp4IuROrvZ2B/Xl3uNKR7n+AHRKnaAO87ywzyltvjwSh2y3xhJueiRs\n'
    + 'BiYkyL3/fnocD3pexTdN6h3JgQGgO5GV8zw/NrxA85mw8o9im0HreuFObmNj36T9\n'
    + 'k5N+R/QIXW83cIQOLaWK1ThYcluytf0tDRiMoKqULiaA6HvDMigExLxuhCtnoF8I\n'
    + 'iOLN1cPdEVQjzwDHLqXP2DbWW1z9iRepLZlEm1hLRLEmOrTGKezYupVv306SSa6J\n'
    + 'OA55lAeXMbyjFaYCr54HWrpt4NwNBX1efMUURc+1LcHpzFrBTTLbfjIyq6as49pH\n'
    + '-----END RSA PRIVATE KEY-----\n'

function TestConvertPemKeyBySync() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  try {
    let keyPairData = asyKeyGenerator.convertPemKeySync(null, priKeyPkcs1EncodingStr, '123456');
    if (keyPairData != null) {
      console.info('[Sync]: convert pem key pair result: success.');
    } else {
      console.error('[Sync]: convert pem key pair result: fail.');
    }
  } catch (e) {
    console.error(`Sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### cryptoFramework.createAsyKeyGeneratorBySpec10+

createAsyKeyGeneratorBySpec(asyKeySpec: AsyKeySpec): AsyKeyGeneratorBySpec

指定密钥参数，获取非对称密钥生成器实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| asyKeySpec | AsyKeySpec | 是 | 密钥参数。非对称密钥生成器根据指定的这些参数生成公/私钥。 支持的规格详见非对称密钥生成和转换规格。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| AsyKeyGeneratorBySpec | 返回非对称密钥生成器实例。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// 配置DSA1024公钥和私钥中包含的公共参数。
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数。
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // JS输入必须是大端格式的正数。
let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
```

#### AsyKeyGeneratorBySpec10+

非对称密钥生成器。在使用该类的方法前，需要先使用[createAsyKeyGeneratorBySpec()](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateasykeygeneratorbyspec10)方法构建一个AsyKeyGeneratorBySpec实例。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 是 | 否 | 非对称密钥生成器的算法名。 |

#### generateKeyPair10+

generateKeyPair(callback: AsyncCallback<KeyPair>): void

获取非对称密钥生成器生成的密钥。使用callback异步回调。

当使用[COMMON_PARAMS_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到随机生成的密钥对；当使用[KEY_PAIR_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到各项数据与密钥参数一致的密钥对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<KeyPair> | 是 | 回调函数，用于获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: Incorrect parameter types; |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// 配置DSA1024公钥和私钥中包含的公共参数。
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数。
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGenerateKeyPair() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // JS输入必须是大端格式的正数。
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  asyKeyGeneratorBySpec.generateKeyPair((err, keyPair) => {
    if (err) {
      console.error('generateKeyPair result: fail.');
      return;
    }
    console.info('generateKeyPair result: success.');
  })
}
```

#### generateKeyPair10+

generateKeyPair(): Promise<KeyPair>

获取该非对称密钥生成器生成的密钥。使用Promise异步回调。

当使用[COMMON_PARAMS_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到随机生成的密钥对；当使用[KEY_PAIR_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到各项数据与密钥参数一致的密钥对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<KeyPair> | 使用Promise的方式获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 配置DSA1024公钥和私钥中包含的公共参数。
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数。
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGenerateKeyPair() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // JS输入必须是大端格式的正数。
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  let keyGenPromise = asyKeyGeneratorBySpec.generateKeyPair();
  keyGenPromise.then(keyPair => {
    console.info('generateKeyPair result: success.');
  }).catch((error: BusinessError) => {
    console.error(`generateKeyPair failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

#### generateKeyPairSync12+

generateKeyPairSync(): KeyPair

同步获取该非对称密钥生成器生成的密钥。

当使用[COMMON_PARAMS_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到随机生成的密钥对；当使用[KEY_PAIR_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到各项数据与密钥参数一致的密钥对。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**返回值：**

| 类型 | 说明 |
| --- | --- |
| KeyPair | 非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 配置DSA1024公钥和私钥中包含的公共参数。
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数。
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGenerateKeyPairSync() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // JS输入必须是大端格式的正数。
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  try {
    let keyPairData = asyKeyGeneratorBySpec.generateKeyPairSync();
    if (keyPairData != null) {
      console.info('[Sync]: key pair result: success.');
    } else {
      console.error('[Sync]: get key pair result: fail.');
    }
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`sync failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

#### generatePriKey10+

generatePriKey(callback: AsyncCallback<PriKey>): void

获取非对称密钥生成器生成的密钥。使用callback异步回调。

使用[PRIVATE_KEY_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型密钥参数创建密钥生成器，生成指定私钥。使用[KEY_PAIR_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型密钥参数创建密钥生成器，从生成的密钥对中获取指定私钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<PriKey> | 是 | 回调函数，用于获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: Mandatory parameters are left unspecified; |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// 配置DSA1024公钥和私钥中包含的公共参数。
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数。
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePriKey() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // JS输入必须是大端格式的正数。
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  asyKeyGeneratorBySpec.generatePriKey((err, prikey) => {
    if (err) {
      console.error('generatePriKey result: fail.');
      return;
    }
    console.info('generatePriKey result: success.');
  })
}
```

#### generatePriKey10+

generatePriKey(): Promise<PriKey>

获取该非对称密钥生成器生成的密钥。使用Promise异步回调。

当使用[PRIVATE_KEY_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到指定的私钥；当使用[KEY_PAIR_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以从生成的密钥对中获取指定的私钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PriKey> | 使用Promise的方式获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 配置DSA1024公钥和私钥中包含的公共参数。
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数。
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePriKey() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // JS输入必须是大端格式的正数。
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  let keyGenPromise = asyKeyGeneratorBySpec.generatePriKey();
  keyGenPromise.then(priKey => {
    console.info('generatePriKey result: success.');
  }).catch((error: BusinessError) => {
    console.error(`generatePriKey failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

#### generatePriKeySync12+

generatePriKeySync(): PriKey

同步获取该非对称密钥生成器生成的密钥。

当使用[PRIVATE_KEY_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到指定的私钥；当使用[KEY_PAIR_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以从生成的密钥对中获取指定的私钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PriKey | 非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// 配置DSA1024公钥和私钥中包含的公共参数。
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数。
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePriKeySync() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // JS输入必须是大端格式的正数。
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  try {
    let priKeyData = asyKeyGeneratorBySpec.generatePriKeySync();
    if (priKeyData != null) {
      console.info('[Sync]: pri key result: success.');
    } else {
      console.error('[Sync]: get pri key result: fail.');
    }
  } catch (e) {
    console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### generatePubKey10+

generatePubKey(callback: AsyncCallback<PubKey>): void

获取非对称密钥生成器生成的密钥。使用callback异步回调。

当使用[PUBLIC_KEY_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到指定的公钥；当使用[KEY_PAIR_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以从生成的密钥对中获取指定的公钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version10-11系统能力为SystemCapability.Security.CryptoFramework；从API version12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<PubKey> | 是 | 回调函数，用于获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: Incorrect parameter types; |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// 配置DSA1024公钥和私钥中包含的公共参数。
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数。
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePubKey() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // JS输入必须是大端格式的正数。
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  asyKeyGeneratorBySpec.generatePubKey((err, pubKey) => {
    if (err) {
      console.error('generatePubKey result: fail.');
      return;
    }
    console.info('generatePubKey result: success.');
  })
}
```

#### generatePubKey10+

generatePubKey(): Promise<PubKey>

获取该非对称密钥生成器生成的密钥。使用Promise异步回调。

当使用[PUBLIC_KEY_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到指定的公钥；当使用[KEY_PAIR_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以从生成的密钥对中获取指定的公钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<PubKey> | 使用Promise的方式获取非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 配置DSA1024公钥和私钥中包含的公共参数。
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数。
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePubKey() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // JS输入必须是大端格式的正数。
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  let keyGenPromise = asyKeyGeneratorBySpec.generatePubKey();
  keyGenPromise.then(pubKey => {
    console.info('generatePubKey result: success.');
  }).catch((error: BusinessError) => {
    console.error(`generatePubKey failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

#### generatePubKeySync12+

generatePubKeySync(): PubKey

同步获取该非对称密钥生成器生成的密钥。

当使用[PUBLIC_KEY_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数来创建密钥生成器时，可以得到指定的公钥；使用[KEY_PAIR_SPEC](#ZH-CN_TOPIC_0000002553201293__asykeyspectype10)类型的密钥参数时，可以从生成的密钥对中获取指定的公钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**返回值：**

| 类型 | 说明 |
| --- | --- |
| PubKey | 非对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// 配置DSA1024公钥和私钥中包含的公共参数。
function genDsa1024CommonSpecBigE() {
  let dsaCommonSpec: cryptoFramework.DSACommonParamsSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    p: BigInt('0xed1501551b8ab3547f6355ffdc2913856ddeca198833dbd04f020e5f25e47c50e0b3894f7690a0d2ea5ed3a7be25c54292a698e1f086eb3a97deb4dbf04fcad2dafd94a9f35c3ae338ab35477e16981ded6a5b13d5ff20bf55f1b262303ad3a80af71aa6aa2354d20e9c82647664bdb6b333b7bea0a5f49d55ca40bc312a1729'),
    q: BigInt('0xd23304044019d5d382cfeabf351636c7ab219694ac845051f60b047b'),
    g: BigInt('0x2cc266d8bd33c3009bd67f285a257ba74f0c3a7e12b722864632a0ac3f2c17c91c2f3f67eb2d57071ef47aaa8f8e17a21ad2c1072ee1ce281362aad01dcbcd3876455cd17e1dd55d4ed36fa011db40f0bbb8cba01d066f392b5eaa9404bfcb775f2196a6bc20eeec3db32d54e94d87ecdb7a0310a5a017c5cdb8ac78597778bd'),
  }
  return dsaCommonSpec;
}

// 设置DSA1024密钥对中包含的全参数。
function genDsa1024KeyPairSpecBigE() {
  let dsaCommonSpec = genDsa1024CommonSpecBigE();
  let dsaKeyPairSpec: cryptoFramework.DSAKeyPairSpec = {
    algName: 'DSA',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: dsaCommonSpec,
    sk: BigInt('0xa2dd2adb2d11392c2541930f61f1165c370aabd2d78d00342e0a2fd9'),
    pk: BigInt('0xae6b5d5042e758f3fc9a02d009d896df115811a75b5f7b382d8526270dbb3c029403fafb8573ba4ef0314ea86f09d01e82a14d1ebb67b0c331f41049bd6b1842658b0592e706a5e4d20c14b67977e17df7bdd464cce14b5f13bae6607760fcdf394e0b73ac70aaf141fa4dafd736bd0364b1d6e6c0d7683a5de6b9221e7f2d6b'),
  }
  return dsaKeyPairSpec;
}

function testGeneratePubKeySync() {
  let asyKeyPairSpec = genDsa1024KeyPairSpecBigE(); // JS输入必须是大端格式的正数。
  let asyKeyGeneratorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(asyKeyPairSpec);
  try {
    let pubKeyData = asyKeyGeneratorBySpec.generatePubKeySync();
    if (pubKeyData != null) {
      console.info('[Sync]: pub key result: success.');
    } else {
      console.error('[Sync]: get pub key result: fail.');
    }
  } catch (e) {
    console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### ECCKeyUtil11+

用于根据椭圆曲线名称为非对称密钥对生成公共参数。

#### genECCCommonParamsSpec11+

static genECCCommonParamsSpec(curveName: string): ECCCommonParamsSpec

根据椭圆曲线相应的NID（Name Identifier）字符串名称生成相应的非对称公共密钥参数。详见[ECC密钥生成规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#ecc)和[SM2密钥生成规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#sm2)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| curveName | string | 是 | 椭圆曲线相应的NID（Name Identifier）字符串名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ECCCommonParamsSpec | 返回ECC公共密钥参数。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let ECCCommonParamsSpec = cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_brainpoolP160r1');
    console.info('genECCCommonParamsSpec result: success.');
} catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`genECCCommonParamsSpec failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### convertPoint12+

static convertPoint(curveName: string, encodedPoint: Uint8Array): Point

根据椭圆曲线的曲线名，即相应的NID（Name Identifier），将指定的点数据转换为Point对象。当前支持压缩/非压缩格式的点数据。


根据RFC5480规范中第2.2节的描述：

1. 非压缩的点数据，表示为：前缀0x04|x坐标|y坐标；
1. 压缩的点数据，对于Fp素数域上的点（当前暂不支持F2m域），表示为：前缀0x03|x坐标 (坐标y是奇数时)，前缀0x02|x坐标 (坐标y是偶数时)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| curveName | string | 是 | 椭圆曲线的曲线名，即相应的NID（Name Identifier）。 |
| encodedPoint | Uint8Array | 是 | 指定的ECC椭圆曲线上的点的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Point | 返回ECC的Point对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

// 随机生成的非压缩点数据。
let pkData =
  new Uint8Array([4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195,
    157, 111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242,
    206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152]);
let returnPoint = cryptoFramework.ECCKeyUtil.convertPoint('NID_brainpoolP256r1', pkData);
console.info('returnPoint: ' + returnPoint.x.toString(16));
```

#### getEncodedPoint12+

static getEncodedPoint(curveName: string, point: Point, format: string): Uint8Array

根据椭圆曲线的曲线名，即相应的NID（Name Identifier），按照指定的点数据格式，将Point对象转换为点数据。当前支持压缩/非压缩格式的点数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| curveName | string | 是 | 椭圆曲线的曲线名，即相应的NID（Name Identifier）。 |
| point | Point | 是 | 椭圆曲线上的Point点对象。 |
| format | string | 是 | 需要获取的点数据格式，当前支持"COMPRESSED"或"UNCOMPRESSED"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | 返回指定格式的点数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function doTest() {
  let generator = cryptoFramework.createAsyKeyGenerator('ECC_BrainPoolP256r1');
  let keyPair = await generator.generateKeyPair();
  let eccPkX = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
  let eccPkY = keyPair.pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_Y_BN);
  console.info('ECC_PK_X_BN 16：' + eccPkX.toString(16));
  console.info('ECC_PK_Y_BN 16：' + eccPkY.toString(16));
  // 将eccPkX.toString(16)结果放入x，eccPkY.toString(16)结果放入y。
  let returnPoint: cryptoFramework.Point = {
    x: BigInt('0x' + eccPkX.toString(16)),
    y: BigInt('0x' + eccPkY.toString(16))
  };
  let returnData = cryptoFramework.ECCKeyUtil.getEncodedPoint('NID_brainpoolP256r1', returnPoint, 'UNCOMPRESSED');
  console.info('returnData: ' + returnData);
}
```

#### DHKeyUtil11+

根据素数P的长度和私钥长度（bit位数）生成DH公共密钥参数。

#### genDHCommonParamsSpec11+

static genDHCommonParamsSpec(pLen: number, skLen?: number): DHCommonParamsSpec

根据素数P的长度和私钥长度（bit位数）生成DH公共密钥参数。详见[DH密钥生成规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-asym-key-generation-conversion-spec#dh)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Key.AsymKey

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Key.AsymKey。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pLen | number | 是 | 用于指定DH公共密钥参数中素数P的长度，单位为bit。 |
| skLen | number | 否 | 用于指定DH公共密钥参数中私钥的长度，单位为bit。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DHCommonParamsSpec | 返回DH公共密钥参数。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
    let DHCommonParamsSpec = cryptoFramework.DHKeyUtil.genDHCommonParamsSpec(2048);
    console.info('genDHCommonParamsSpec result: success.');
} catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`genDHCommonParamsSpec failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### SM2CryptoUtil12+

用于SM2密码学运算的工具类。

#### genCipherTextBySpec12+

static genCipherTextBySpec(spec: SM2CipherTextSpec, mode?: string): DataBlob

根据指定的SM2密文参数，生成符合国密标准的ASN.1格式SM2密文。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spec | SM2CipherTextSpec | 是 | 指定的SM2密文参数。 |
| mode | string | 否 | 可选的密文转换模式，可用于指定密文参数的拼接顺序，当前仅支持默认值"C1C3C2"。为空或空字符串时使用默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 返回符合国密标准的ASN.1格式的SM2密文。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let spec : cryptoFramework.SM2CipherTextSpec = {
    xCoordinate: BigInt('20625015362595980457695435345498579729138244358573902431560627260141789922999'),
    yCoordinate: BigInt('48563164792857017065725892921053777369510340820930241057309844352421738767712'),
    cipherTextData: new Uint8Array([100,227,78,195,249,179,43,70,242,69,169,10,65,123]),
    hashData: new Uint8Array([87, 167, 167, 247, 88, 146, 203, 234, 83, 126, 117, 129, 52, 142, 82, 54, 152, 226, 201,
      111, 143, 115, 169, 125, 128, 42, 157, 31, 114, 198, 109, 244]),
  }
  let data = cryptoFramework.SM2CryptoUtil.genCipherTextBySpec(spec, 'C1C3C2');
  console.info('genCipherTextBySpec result: success.');
} catch (err) {
  let e: BusinessError = err as BusinessError;
  console.error(`genCipherTextBySpec failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### getCipherTextSpec12+

static getCipherTextSpec(cipherText: DataBlob, mode?: string): SM2CipherTextSpec

从符合国密标准的ASN.1格式的SM2密文中，获取具体的SM2密文参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cipherText | DataBlob | 是 | 符合国密标准的ASN.1格式的SM2密文。 |
| mode | string | 否 | 可选的密文转换模式，可用于指定密文参数的拼接顺序，当前仅支持默认值"C1C3C2"。为空或空字符串时使用默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| SM2CipherTextSpec | 返回SM2密文参数。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  let cipherTextArray =
    new Uint8Array([48, 118, 2, 32, 45, 153, 88, 82, 104, 221, 226, 43, 174, 21, 122, 248, 5, 232, 105, 41, 92, 95, 102,
      224, 216, 149, 85, 236, 110, 6, 64, 188, 149, 70, 70, 183, 2, 32, 107, 93, 198, 247, 119, 18, 40, 110, 90, 156,
      193, 158, 205, 113, 170, 128, 146, 109, 75, 17, 181, 109, 110, 91, 149, 5, 110, 233, 209, 78, 229, 96, 4, 32, 87,
      167, 167, 247, 88, 146, 203, 234, 83, 126, 117, 129, 52, 142, 82, 54, 152, 226, 201, 111, 143, 115, 169, 125, 128,
      42, 157, 31, 114, 198, 109, 244, 4, 14, 100, 227, 78, 195, 249, 179, 43, 70, 242, 69, 169, 10, 65, 123]);
    let cipherText : cryptoFramework.DataBlob = {data : cipherTextArray};
    let spec : cryptoFramework.SM2CipherTextSpec = cryptoFramework.SM2CryptoUtil.getCipherTextSpec(cipherText, 'C1C3C2');
  console.info('getCipherTextSpec result: success.');
} catch (err) {
    let e: BusinessError = err as BusinessError;
  console.error(`getCipherTextSpec failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### cryptoFramework.createCipher

createCipher(transformation: string): Cipher

通过指定算法名称，获取相应的[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transformation | string | 是 | 待生成Cipher的算法名称（含密钥长度）、加密模式以及填充方法的组合。 支持的规格详见对称密钥加解密算法规格和非对称密钥加解密算法规格。 |


1.

目前对称加解密中，PKCS5和PKCS7的实现相同，其padding长度和分组长度保持一致。在3DES中均按8字节填充，在AES中均按16字节填充。另有NoPadding表示不填充。

开发者需要自行了解密码学不同分组模式的差异，以便选择合适的参数规格。例如选择ECB和CBC模式时，建议启用填充，否则必须确保明文长度是分组大小的整数倍；选择其他模式时，可以不启用填充，此时密文长度和明文长度一致（即可能不是分组大小的整数倍）。

1. 使用RSA或SM2进行非对称加解密时，必须创建两个Cipher对象，分别进行加密和解密操作，不能对同一个Cipher对象进行加解密。对称加解密没有此要求，只要算法规格一致，可以对同一个Cipher对象进行加解密操作。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Cipher | 返回加解密生成器的对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let cipherAlgName = '3DES192|ECB|PKCS7';
try {
  let cipher = cryptoFramework.createCipher(cipherAlgName);
  console.info('cipher algName：' + cipher.algName);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### Cipher

提供加解密的算法操作功能，按序调用本类中的[init()](#ZH-CN_TOPIC_0000002553201293__init-1)、[update()](#ZH-CN_TOPIC_0000002553201293__update)、[doFinal()](#ZH-CN_TOPIC_0000002553201293__dofinal)方法，可以实现对称加密/对称解密/非对称加密/非对称解密。

完整的加解密流程示例可参考[开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-encryption-decryption-overview)。

一次完整的加/解密流程在对称加密和非对称加密中略有不同：

- 对称加解密：init为必选，update为可选（且允许多次update加/解密大数据），doFinal为必选；doFinal结束后可以重新init开始新一轮加/解密流程。
- RSA、SM2非对称加解密：init为必选，不支持update操作，doFinal为必选（允许连续多次doFinal加/解密大数据）；RSA不支持重复init，切换加解密模式或填充方式时，需要重新创建Cipher对象。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 是 | 否 | 加解密生成器指定的算法名称。 |

#### init

init(opMode: CryptoMode, key: Key, params: ParamsSpec | null, callback: AsyncCallback<void>): void

初始化加解密的[cipher](#ZH-CN_TOPIC_0000002553201293__cipher)对象，使用callback异步回调获取结果。init、update、doFinal为三段式接口，需要成组使用。其中init和doFinal必选，update可选。

必须在使用[createCipher](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatecipher)创建[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例后，才能使用本函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| opMode | CryptoMode | 是 | 加密或者解密模式。 |
| key | Key | 是 | 指定加密或解密的密钥。 |
| params | ParamsSpec | null10+ | 是 | 指定加密或解密的参数，对于ECB等没有参数的算法模式，请传入null。API 10之前只支持ParamsSpec， API 10之后增加支持null。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当加解密初始化成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. Invalid opMode value; 2. Invalid iv length; 3. Invalid key length. |
| 17630001 | crypto operation error. |

#### init

init(opMode: CryptoMode, key: Key, params: ParamsSpec | null): Promise<void>

初始化加解密的cipher对象。使用Promise异步回调。init、update、doFinal为三段式接口，需要成组使用。其中init和doFinal必选，update可选。

必须在使用[createCipher](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatecipher)创建[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例后，才能使用本函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| opMode | CryptoMode | 是 | 加密或者解密模式。 |
| key | Key | 是 | 指定加密或解密的密钥。 |
| params | ParamsSpec | null10+ | 是 | 指定加密或解密的参数，对于ECB等没有参数的算法模式，请传入null。API 10之前仅支持ParamsSpec，从API 10开始增加对null的支持。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. Invalid opMode value; 2. Invalid iv length; 3. Invalid key length. |
| 17630001 | crypto operation error. |

#### initSync12+

initSync(opMode: CryptoMode, key: Key, params: ParamsSpec | null): void

初始化加解密的[cipher](#ZH-CN_TOPIC_0000002553201293__cipher)对象，通过注册回调函数获取结果。initSync、updateSync、doFinalSync为三段式接口，需要成组使用。其中initSync和doFinalSync必选，updateSync可选。

必须在使用[createCipher](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatecipher)创建[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例后，才能使用本函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| opMode | CryptoMode | 是 | 加密或者解密模式。 |
| key | Key | 是 | 指定加密或解密的密钥。 |
| params | ParamsSpec | null | 是 | 指定加密或解密的参数，对于ECB等没有参数的算法模式，请传入null。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. Invalid opMode value; 2. Invalid iv length; 3. Invalid key length. |
| 17630001 | crypto operation error. |

#### update

update(data: DataBlob, callback: AsyncCallback<DataBlob>): void

分段更新加密或者解密数据操作。使用callback异步回调。

必须在对[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例使用[init()](#ZH-CN_TOPIC_0000002553201293__init-1)初始化后，才能使用本函数。


1.

在进行对称加解密操作时，如果开发者对各个分组模式不够熟悉，建议对每次update和doFinal的结果进行判断，确保其不为null，并在结果不为null时取出数据进行拼接，形成完整的密文或明文。这是因选择的分组模式等各项规格可能对update和doFinal的结果产生影响。

例如，对于ECB和CBC模式，不论update传入的数据是否为分组长度的整数倍，都会以分组为单位进行加解密，并输出本次update新产生的加解密分组结果。

可以理解为update只要凑满一个新的分组就会有输出，如果没有凑满则此次update输出为null，将当前未被加解密的数据留着，等下一次update或doFinal传入数据时，拼接起来继续凑分组。

最后doFinal时，会将剩下的未加解密的数据根据[createCipher](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatecipher)时设置的填充模式进行填充，补齐到分组的整数倍长度，再输出剩余的加解密结果。

对于可以将分组密码转化为流模式实现的模式，还可能出现密文长度与明文长度相同的情况。

1.

根据数据量，可以不调用update（即init完成后直接调用doFinal）或多次调用update。

算法库未对单次或累计的update数据量设置限制。对于大数据量的对称加解密操作，建议分多次调用update方法传入数据。

AES使用多次update操作的示例代码详见[使用AES对称密钥分段加解密](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment)。

1.

RSA、SM2非对称加解密不支持update操作。

1.

对于CCM模式的对称加解密算法，加密时只能调用1次update接口加密数据并调用doFinal接口获取tag，或直接调用doFinal接口加密数据并获取tag，解密时只能调用1次update接口或调用1次doFinal接口解密数据并验证tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | 是 | 需要进行加密或解密的数据。data不能为null。 |
| callback | AsyncCallback<DataBlob> | 是 | 回调函数。更新加/解密数据成功时，err为undefined，data为DataBlob；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. The data is too long. |
| 17630001 | crypto operation error. |

#### update

update(data: DataBlob): Promise<DataBlob>

分段更新加密或者解密数据操作。使用Promise异步回调。

必须在对[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例使用[init()](#ZH-CN_TOPIC_0000002553201293__init-1)初始化后，才能使用本函数。


1.

在进行对称加解密操作时，如果开发者对各分组模式不够熟悉，建议每次调用update和doFinal后，都判断结果是否为null。如果结果不为null，则取出其中的数据进行拼接，以形成完整的密文或明文。这是因为选择的分组模式等各项规格可能会影响update和doFinal的结果。

（例如对于ECB和CBC模式，不论update传入的数据是否为分组长度的整数倍，都会以分组作为基本单位进行加/解密，并输出本次update新产生的加/解密分组结果。

可以理解为，update只要凑满一个新的分组就会有输出，如果没有凑满则此次update输出为null，把当前还没被加/解密的数据留着，等下一次update/doFinal传入数据的时候，拼接起来继续凑分组。

最后doFinal的时候，会把剩下的还没加/解密的数据，根据[createCipher](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatecipher)时设置的padding模式进行填充，补齐到分组的整数倍长度，再输出剩余加解密结果。

而对于可以将分组密码转化为流模式实现的模式，还可能出现密文长度和明文长度相同的情况等。）

1.

根据数据量，可以不调用update（即init完成后直接调用doFinal）或多次调用update。

算法库目前没有对update（单次或累计）的数据量设置大小限制，建议对于大数据量的对称加解密，可以采用多次update的方式传入数据。

AES使用多次update操作的示例代码详见[使用AES对称密钥分段加解密](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm-by-segment)。

1. RSA、SM2非对称加解密不支持update操作。
1. 对于CCM模式的对称加解密算法，加密时只能调用1次update接口加密数据并调用doFinal接口获取tag，或直接调用doFinal接口加密数据并获取tag，解密时只能调用1次update接口或调用1次doFinal接口解密数据并验证tag。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | 是 | 加密或者解密的数据。data不能为null。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DataBlob> | Promise对象，返回此次更新的加/解密结果DataBlob。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. The data is too long. |
| 17630001 | crypto operation error. |

#### updateSync12+

updateSync(data: DataBlob): DataBlob

分段更新加密或者解密数据操作，通过注册回调函数获取加/解密数据。

必须在对[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例使用[initSync()](#ZH-CN_TOPIC_0000002553201293__initsync12)初始化后，才能使用本函数。

其他注意事项同上异步接口说明。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | 是 | 加密或者解密的数据。data不能为null。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 返回此次更新的加/解密结果DataBlob。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. The data is too long. |
| 17630001 | crypto operation error. |

#### doFinal

doFinal(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void

（1）在对称加解密中doFinal用于处理剩余数据和本次传入的数据，并最终结束加密或解密操作，使用callback异步回调函数获取加密或解密后的数据。如果数据量较小，可以在 doFinal 中一次性传入数据，而不使用update；如果在本次加解密流程中已经使用[update](#ZH-CN_TOPIC_0000002553201293__update)传入过数据，可以在doFinal的data参数处传入null。根据对称加解密的模式不同，doFinal的输出有以下区别：

- 在GCM和CCM模式的对称加密中，一次加密流程中，将每次update和doFinal的结果拼接起来，会得到“密文 + authTag”。GCM模式下，authTag为末尾的16字节；CCM模式下，authTag为末尾的12字节。其余部分均为密文。如果doFinal的data参数传入null，则doFinal的结果就是authTag。解密时，authTag需要填入[GcmParamsSpec](#ZH-CN_TOPIC_0000002553201293__gcmparamsspec)或[CcmParamsSpec](#ZH-CN_TOPIC_0000002553201293__ccmparamsspec)，密文作为解密时的data参数。

- 对于其他模式的对称加解密及GCM和CCM模式的对称解密：每次加/解密流程中，update和doFinal的结果拼接起来，得到完整的明文或密文。

（2）在RSA、SM2非对称加解密中，doFinal加/解密本次传入的数据，使用callback异步回调函数获取加密或者解密数据。如果数据量较大，可以多次调用doFinal，拼接结果得到完整的明文/密文。


1.

对称加解密中，调用doFinal标志着一次加解密流程已经完成，即[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例的状态被清除，因此当后续开启新一轮加解密流程时，需要重新调用init()并传入完整的参数列表进行初始化

（比如即使是对同一个Cipher实例，采用同样的对称密钥，进行加密然后解密，则解密中调用init的时候仍需填写params参数，而不能直接省略为null）。

1. 如果遇到解密失败，需检查加解密数据和init时的参数是否匹配，包括GCM模式下加密得到的authTag是否填入解密时的GcmParamsSpec等。
1.

doFinal的结果可能为null，因此使用.data字段访问doFinal结果的具体数据前，请记得先判断结果是否为null，避免产生异常。

对于加密，CFB、OFB和CTR模式，如果doFinal传null, 则返回结果为null。

对于解密，GCM、CCM、CFB、OFB和CTR模式，如果doFinal传null，则返回结果为null；对于解密，其他模式，如果明文是加密块大小的整倍数，调用update传入所有密文，调用doFinal传null, 则返回结果为null。

1. 非对称加解密时多次doFinal操作的示例代码详见[使用RSA非对称密钥分段加解密](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment)，SM2和RSA的操作类似。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | null10+ | 是 | 加密或解密的数据。在对称加解密中可为null，但不可传入{data: Uint8Array(空) }。API 10前仅支持DataBlob，API 10后增加null支持。 |
| callback | AsyncCallback<DataBlob> | 是 | 回调函数。最终加/解密成功时，err为undefined，data为加/解密结果DataBlob；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. The data is too long. |
| 17630001 | crypto operation error. |

**以AES GCM模式加密为例：**

更多加解密流程的完整示例请参考[加解密开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function generateRandom(len: number) {
  let rand = cryptoFramework.createRandom();
  let generateRandSync = rand.generateRandomSync(len);
  return generateRandSync;
}

function genGcmParamsSpec() {
  let ivBlob = generateRandom(12);
  let arr = [1, 2, 3, 4, 5, 6, 7, 8];
  let dataAad = new Uint8Array(arr);
  let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  let dataTag = new Uint8Array(arr);
  let tagBlob: cryptoFramework.DataBlob = {
    data: dataTag
  };
  let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
    iv: ivBlob,
    aad: aadBlob,
    authTag: tagBlob,
    algName: 'GcmParamsSpec'
  };
  return gcmParamsSpec;
}

function cipherByCallback() {
  let gcmParams = genGcmParamsSpec();
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let cipher = cryptoFramework.createCipher('AES128|GCM|PKCS7');
  symKeyGenerator.generateSymKey((err, symKey) => {
    cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams, (err) => {
      let message = 'This is a test';
      let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
      cipher.update(plainText, (err, encryptUpdate) => {
        cipher.doFinal(null, (err, tag) => {
          gcmParams.authTag = tag;
          console.info('encryptUpdate plainText：' + encryptUpdate.data);
        });
}
```

#### doFinal

doFinal(data: DataBlob | null): Promise<DataBlob>

（1）在对称加解密中，doFinal加/解密（分组模式产生的）剩余数据和本次传入的数据，最后结束加密或者解密数据操作，使用Promise异步回调获取加密或者解密数据。

如果数据量较小，可以在doFinal中一次性传入数据，而不使用update；如果在本次加解密流程中，已经使用update传入过数据，可以在doFinal的data参数处传入null。

根据对称加解密的模式不同，doFinal的输出有如下区别：

-

对于GCM和CCM模式的对称加密：一次加密流程中，如果将每一次update和doFinal的结果拼接起来，会得到“密文+authTag”，即末尾的16字节（GCM模式）或12字节（CCM模式）是authTag，而其余部分均为密文。（也就是说，如果doFinal的data参数传入null，则doFinal的结果就是authTag）

authTag需要填入解密时的[GcmParamsSpec](#ZH-CN_TOPIC_0000002553201293__gcmparamsspec)或[CcmParamsSpec](#ZH-CN_TOPIC_0000002553201293__ccmparamsspec)；密文则作为解密时的入参data。

- 对于其他模式的对称加解密及GCM和CCM模式的对称解密：一次加解密流程中，每次update和doFinal的结果拼接起来，得到完整的明文或密文。

（2）在RSA和SM2非对称加解密中，使用doFinal方法加解密传入的数据，并使用Promise异步回调获取加密或解密结果。如果数据量较大，可以多次调用doFinal，拼接结果以获得完整的明文或密文。


1.

对称加解密中，调用doFinal标志着一次加解密流程完成，[Cipher](#ZH-CN_TOPIC_0000002553201293__cipher)实例状态被清除。因此，后续开启新流程时，需重新调用init并传入完整参数列表进行初始化。

即使是对同一个Cipher实例，使用相同对称密钥，进行加密后解密时，调用init仍需填写params参数，不能省略为null。

1.

如果遇到解密失败，检查加解密数据和初始化时的参数是否匹配，包括GCM模式下加密得到的authTag是否填入解密时的GcmParamsSpec。

1.

doFinal的结果可能为null，因此在使用.data字段访问doFinal结果的具体数据前，请先判断结果是否为null，以避免产生异常。

对于加密，CFB、OFB 和 CTR 模式，如果doFinal传入null，则返回结果为null。

对于解密，GCM、CCM、CFB、OFB和CTR模式，如果doFinal传null，则返回结果为null；对于其他模式，如果明文是加密块大小的整倍数，调用update传入所有密文，调用doFinal传null, 则返回结果为null。

1.

非对称加解密时多次doFinal操作的示例代码详见[使用RSA非对称密钥分段加解密](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-by-segment)，SM2和RSA的操作类似。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | null10+ | 是 | 加密或者解密的数据。data参数允许为null，但不允许传入{data: Uint8Array(空) }。API 10之前只支持DataBlob，API 10之后增加支持null。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DataBlob> | Promise对象，返回剩余数据的加/解密结果DataBlob。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. The data is too long. |
| 17630001 | crypto operation error. |

**以AES GCM模式加密为例：**

此外，更多加解密流程的完整示例可参考[加解密开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function generateRandom(len: number) {
  let rand = cryptoFramework.createRandom();
  let generateRandSync = rand.generateRandomSync(len);
  return generateRandSync;
}

function genGcmParamsSpec() {
  let ivBlob = generateRandom(12);
  let arr = [1, 2, 3, 4, 5, 6, 7, 8];
  let dataAad = new Uint8Array(arr);
  let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  let dataTag = new Uint8Array(arr);
  let tagBlob: cryptoFramework.DataBlob = {
    data: dataTag
  };
  let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
    iv: ivBlob,
    aad: aadBlob,
    authTag: tagBlob,
    algName: 'GcmParamsSpec'
  };
  return gcmParamsSpec;
}

async function cipherByPromise() {
  let gcmParams = genGcmParamsSpec();
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let cipher = cryptoFramework.createCipher('AES128|GCM|PKCS7');
  let symKey = await symKeyGenerator.generateSymKey();
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
  let message = 'This is a test';
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  let encryptUpdate = await cipher.update(plainText);
  gcmParams.authTag = await cipher.doFinal(null);
  console.info('encryptUpdate plainText: ' + encryptUpdate.data);
}
```

#### doFinalSync12+

doFinalSync(data: DataBlob | null): DataBlob

（1）在对称加解密中，doFinalSync用于处理剩余数据和本次传入的数据，并结束加密或解密操作，通过注册回调函数获取加密或解密结果。

如果数据量较小，可以在doFinalSync中一次性传入数据，而不使用updateSync。如果在本次加解密流程中已经使用[updateSync](#ZH-CN_TOPIC_0000002553201293__updatesync12)传入过数据，可以在doFinalSync的data参数处传入null。

根据对称加解密的模式不同，doFinalSync的输出有以下区别：

-

对于GCM和CCM模式的对称加密：一次加密流程中，如果将每次updateSync和doFinalSync的结果拼接起来，会得到“密文 + authTag”。即末尾的16字节（GCM模式）或12字节（CCM模式）是authTag，其余部分均为密文。也就是说，如果doFinalSync的data参数传入null，则doFinalSync的结果就是 authTag。

authTag需要填入解密时的[GcmParamsSpec](#ZH-CN_TOPIC_0000002553201293__gcmparamsspec)或[CcmParamsSpec](#ZH-CN_TOPIC_0000002553201293__ccmparamsspec)；密文则作为解密时的入参data。

-

对于其他模式的对称加解密以及GCM和CCM模式的对称解密：在一次加/解密流程中，每次updateSync和doFinalSync的结果拼接起来，得到完整的明文或密文。

（2）在RSA和SM2非对称加解密中，doFinalSync用于加解密本次传入的数据，通过注册回调函数获取加密或解密后的数据。如果数据量超过单次处理能力，可以多次调用doFinalSync，并将结果拼接以获得完整的明文或密文。

其他注意事项同接口[doFinal()](#ZH-CN_TOPIC_0000002553201293__dofinal)说明。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | null | 是 | 加密或者解密的数据。在对称加解密中允许为null，但不允许传入{data: Uint8Array(空) }。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 返回剩余数据的加/解密结果DataBlob。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. The data is too long. |
| 17630001 | crypto operation error. |

**以AES GCM模式加密为例：**

此外，更多加解密流程的完整示例可参考[加解密开发指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-aes-sym-encrypt-decrypt-gcm)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function generateRandom(len: number) {
  let rand = cryptoFramework.createRandom();
  let generateRandSync = rand.generateRandomSync(len);
  return generateRandSync;
}

function genGcmParamsSpec() {
  let ivBlob = generateRandom(12);
  let arr = [1, 2, 3, 4, 5, 6, 7, 8];
  let dataAad = new Uint8Array(arr);
  let aadBlob: cryptoFramework.DataBlob = { data: dataAad };
  arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
  let dataTag = new Uint8Array(arr);
  let tagBlob: cryptoFramework.DataBlob = {
    data: dataTag
  };
  let gcmParamsSpec: cryptoFramework.GcmParamsSpec = {
    iv: ivBlob,
    aad: aadBlob,
    authTag: tagBlob,
    algName: 'GcmParamsSpec'
  };
  return gcmParamsSpec;
}

async function cipherBySync() {
  let gcmParams = genGcmParamsSpec();
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let cipher = cryptoFramework.createCipher('AES128|GCM|PKCS7');
  let symKey = await symKeyGenerator.generateSymKey();
  await cipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, symKey, gcmParams);
  let message = 'This is a test';
  let plainText: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from(message, 'utf-8').buffer) };
  let encryptUpdate = cipher.updateSync(plainText);
  gcmParams.authTag = cipher.doFinalSync(null);
  console.info('encryptUpdate plainText: ' + encryptUpdate.data);
}
```

#### setCipherSpec10+

setCipherSpec(itemType: CipherSpecItem, itemValue: Uint8Array): void

设置加解密参数。常用的加解密参数直接通过[createCipher](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatecipher) 来指定，剩余参数通过本接口指定。当前只支持RSA算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemType | CipherSpecItem | 是 | 用于指定需要设置的加解密参数。 |
| itemValue | Uint8Array | 是 | 用于指定加解密参数的具体值。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17620003 | parameter check failed. Possible causes: 1. Unsupported itemType. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
function testsetCipherSpec() {
  let cipher = cryptoFramework.createCipher('RSA2048|PKCS1_OAEP|SHA256|MGF1_SHA1');
  let pSource = new Uint8Array([1,2,3,4]);
  cipher.setCipherSpec(cryptoFramework.CipherSpecItem.OAEP_MGF1_PSRC_UINT8ARR, pSource);
}
```

#### getCipherSpec10+

getCipherSpec(itemType: CipherSpecItem): string | Uint8Array

获取加解密参数。当前只支持RSA算法和SM2算法，从API version 11开始，支持SM2算法获取加解密参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Cipher

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Cipher。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemType | CipherSpecItem | 是 | 用于指定需要获取的加解密参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Uint8Array | 获取的加解密参数的具体值。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17620003 | parameter check failed. Possible causes: 1. Unsupported itemType. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testGetCipherSpec() {
  let cipher = cryptoFramework.createCipher('RSA2048|PKCS1_OAEP|SHA256|MGF1_SHA1');
  let mdName = cipher.getCipherSpec(cryptoFramework.CipherSpecItem.OAEP_MD_NAME_STR);
  console.info('getCipherSpec: mdName =' + mdName);
}
```

#### cryptoFramework.createSign

createSign(algName: string): Sign

生成Sign实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algName | string | 是 | 指定签名算法：RSA、ECC、DSA、SM210+或Ed2551911+。使用RSA PKCS1模式时需设置摘要；使用RSA PSS模式时需设置摘要和掩码摘要。签名时，通过设置OnlySign参数可传入数据摘要仅作签名。 支持的规格详见签名验签规格。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Sign | 返回由输入算法指定生成的Sign对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let signer1 = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');

let signer2 = cryptoFramework.createSign('RSA1024|PSS|SHA256|MGF1_SHA256');

let signer3 = cryptoFramework.createSign('ECC224|SHA256');

let signer4 = cryptoFramework.createSign('DSA2048|SHA256');

let signer5 = cryptoFramework.createSign('RSA1024|PKCS1|SHA256|OnlySign');
```

#### Sign

Sign类，使用Sign方法之前需要创建该类的实例进行操作，通过[createSign(algName: string): Sign](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatesign)方法构造此实例。按序调用本类中的init、update、sign方法完成签名操作。签名操作的示例代码详见[签名验签开发指导](../../guides/使用RSA密钥对（PKCS1模式）签名验签.md)。

Sign类不支持重复初始化，当业务方需要使用新密钥签名时，需要重新创建新Sign对象并调用init初始化。

业务方使用时，调用createSign接口确定签名的模式，调用init接口设置密钥。

当待签名数据长度较短时，可在初始化后直接调用sign接口传入数据进行签名，无需调用update。

当待签名数据较长时，可通过update接口分段传入切分后的原文数据，最后调用sign接口对整体原文数据进行签名。

当使用update分段传入原文时，sign接口API 10之前只支持传入DataBlob， API 10之后增加支持null。业务方可在循环中调用update接口，循环结束后调用sign进行签名。

使用DSA算法签名时，如果摘要算法设置为NoHash，则不支持update操作，调用update接口将返回错误码ERR_CRYPTO_OPERATION。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 是 | 否 | 签名指定的算法名称。 |

#### init

init(priKey: PriKey, callback: AsyncCallback<void>): void

使用私钥初始化Sign对象。使用callback异步回调。init、update、sign为三段式接口，需要成组使用。其中init和sign必选，update可选。

Sign类不支持重复初始化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| priKey | PriKey | 是 | 用于Sign的初始化。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当签名初始化成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### init

init(priKey: PriKey): Promise<void>

使用私钥初始化Sign对象。使用Promise异步回调。init、update、sign为三段式接口，需要成组使用。其中init和sign必选，update可选。

Sign类不支持重复初始化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| priKey | PriKey | 是 | 用于Sign的初始化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### initSync12+

initSync(priKey: PriKey): void

使用私钥初始化Sign对象，通过同步方式获取结果。initSync、updateSync、signSync为三段式接口，需要成组使用。其中initSync和signSync必选，updateSync可选。

Sign类不支持重复调用initSync。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| priKey | PriKey | 是 | 用于Sign的初始化。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### update

update(data: DataBlob, callback: AsyncCallback<void>): void

追加待签名数据，使用callback异步回调完成更新。

必须在对[Sign](#ZH-CN_TOPIC_0000002553201293__sign)实例使用[init()](#ZH-CN_TOPIC_0000002553201293__init-2)初始化后，才能使用本函数。


根据数据量，可以不调用update（即[init](#ZH-CN_TOPIC_0000002553201293__init-2)完成后直接调用[sign](#ZH-CN_TOPIC_0000002553201293__sign-1)）或多次调用update。

算法库目前没有对update（单次或累计）的数据量设置大小限制，建议对于大数据量的签名操作，采用多次update的方式传入数据，避免一次性申请过大内存。

签名使用多次update操作的示例代码详见[使用RSA密钥对分段签名验签](../../guides/使用RSA密钥对分段签名验签（PKCS1模式）.md)，其余算法操作类似。

OnlySign模式下，不支持update操作，需要直接使用sign传入数据。

当使用DSA算法进行签名，并设置了摘要算法为NoHash时，则不支持update操作，update接口会返回错误码ERR_CRYPTO_OPERATION。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | 是 | 传入的消息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当签名更新成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### update

update(data: DataBlob): Promise<void>

追加待签名数据，使用Promise异步回调方式完成更新。

在使用本函数前，必须先使用[Sign](#ZH-CN_TOPIC_0000002553201293__sign)方法对[init()](#ZH-CN_TOPIC_0000002553201293__init-3)实例进行初始化。


根据数据量，可以不调用update（即[init](#ZH-CN_TOPIC_0000002553201293__init-3)完成后直接调用[sign](#ZH-CN_TOPIC_0000002553201293__sign-2)）或多次调用update。

算法库不对单次或累计的update数据量设置大小限制。建议在处理大数据量的签名操作时，采用多次update方式传入数据，以避免一次性申请过多内存。

签名使用多次update操作的示例代码详见[使用RSA密钥对分段签名验签](../../guides/使用RSA密钥对分段签名验签（PKCS1模式）.md)，其余算法操作类似。

OnlySign模式下，不支持update操作，需要直接使用sign传入数据。

当使用DSA算法进行签名，并设置了摘要算法为NoHash时，则不支持update操作，update接口会返回错误码ERR_CRYPTO_OPERATION。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | 是 | 传入的消息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### updateSync12+

updateSync(data: DataBlob): void

追加待签名数据，通过同步方式完成更新。

必须在对[Sign](#ZH-CN_TOPIC_0000002553201293__sign)实例使用[initSync()](#ZH-CN_TOPIC_0000002553201293__initsync12-1)初始化后，才能使用本函数。


根据数据量，可以不调用updateSync（即[initSync](#ZH-CN_TOPIC_0000002553201293__initsync12-1)完成后直接调用[signSync](#ZH-CN_TOPIC_0000002553201293__signsync12)）或多次调用updateSync。

算法库目前没有对updateSync（单次或累计）的数据量设置大小限制，建议对于大数据量的签名操作，采用多次updateSync的方式传入数据，避免一次性申请过大内存。

签名使用多次updateSync操作的示例代码详见[使用RSA密钥对分段签名验签](../../guides/使用RSA密钥对分段签名验签（PKCS1模式）.md)，其余算法操作类似。

OnlySign模式下，不支持updateSync操作，需要直接使用signSync传入数据。

当使用DSA算法进行签名，并设置了摘要算法为NoHash时，则不支持updateSync操作，updateSync接口会返回错误码ERR_CRYPTO_OPERATION。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | 是 | 传入的消息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | 无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### sign

sign(data: DataBlob | null, callback: AsyncCallback<DataBlob>): void

对数据进行签名。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | null10+ | 是 | 传入的消息。API 10之前只支持DataBlob， API 10之后增加支持null。 |
| callback | AsyncCallback<DataBlob> | 是 | 回调函数，用于获取DataBlob数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### sign

sign(data: DataBlob | null): Promise<DataBlob>

对数据进行签名。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | null10+ | 是 | 传入的消息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DataBlob> | 返回签名结果。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### signSync12+

signSync(data: DataBlob | null): DataBlob

对数据进行签名，通过同步方式返回签名结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | null | 是 | 传入的消息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 返回签名结果。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**callback示例：**

此外，更多签名验签的完整示例可参考[签名验签开发指导](../../guides/使用RSA密钥对（PKCS1模式）签名验签.md)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function signByCallback() {
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputVerify: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  let pkData =
    new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1]);
  let skData =
    new Uint8Array([48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184]);
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pkData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: skData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let signer = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');
  rsaGenerator.convertKey(pubKeyBlob, priKeyBlob, (err, keyPair) => {
    signer.init(keyPair.priKey, err => {
      signer.update(inputUpdate, err => {
        signer.sign(inputVerify, (err, signData) => {
          console.info('sign output = ' + signData.data);
  });
}
```

**Promise示例：**

此外，更多签名验签的完整示例可参考[签名验签开发指导](../../guides/使用RSA密钥对（PKCS1模式）签名验签.md)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = await rsaGenerator.convertKey(pubKeyBlob, priKeyBlob);
  console.info('convertKey result: success.');
  return keyPair;
}

async function signByPromise() {
  let pkData =
    new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1]);
  let skData =
    new Uint8Array([48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184]);
  let keyPair = await genKeyPairByData(pkData, skData);
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputSign: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  let signer = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');
  await signer.init(keyPair.priKey);
  await signer.update(inputUpdate);
  let signData = await signer.sign(inputSign);
  console.info('signData result: ' + signData.data);
}
```

**Sync示例：**

此外，更多签名验签的完整示例可参考[签名验签开发指导](../../guides/使用RSA密钥对（PKCS1模式）签名验签.md)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertKeySync(pubKeyBlob, priKeyBlob);
  console.info('convertKeySync result: success.');
  return keyPair;
}

function signBySync() {
  let pkData =
    new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1]);
  let skData =
    new Uint8Array([48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184]);
  let keyPair =  genKeyPairByData(pkData, skData);
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputSign: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  let signer = cryptoFramework.createSign('RSA1024|PKCS1|SHA256');
  signer.initSync(keyPair.priKey);
  signer.updateSync(inputUpdate);
  let signData = signer.signSync(inputSign);
  console.info('signData result: ' + signData.data);
}
```

#### setSignSpec10+

setSignSpec(itemType: SignSpecItem, itemValue: number): void

setSignSpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void

设置签名参数。常用签名参数可通过 [createSign](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatesign) 指定，其他参数则通过本接口设置。

只支持RSA算法、SM2算法，从API version11开始，支持SM2算法设置签名参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemType | SignSpecItem | 是 | 用于指定需要设置的签名参数。 |
| itemValue | number | Uint8Array11+ | 是 | 用于指定签名参数的具体值。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testSetSignSpec() {
  let signer = cryptoFramework.createSign('RSA|PSS|SHA256|MGF1_SHA256');
  let setN = 20;
  signer.setSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
}
```

#### getSignSpec10+

getSignSpec(itemType: SignSpecItem): string | number

获取签名参数。当前仅支持RSA算法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemType | SignSpecItem | 是 | 用于指定需要获取的签名参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | number | 获取的签名参数的具体值。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testGetSignSpec() {
  let signer = cryptoFramework.createSign('RSA|PSS|SHA256|MGF1_SHA256');
  let setN = 32;
  signer.setSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
  signer.getSignSpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM);
}
```

#### cryptoFramework.createVerify

createVerify(algName: string): Verify

生成Verify实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algName | string | 是 | 指定签名算法：RSA、ECC、DSA、SM210+或Ed2551911+。使用RSA PKCS1模式时需设置摘要；使用RSA PSS模式时需设置摘要和掩码摘要。使用RSA算法验签时，设置Recover参数可支持验签恢复。 支持的规格详见签名验签规格。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Verify | 返回由输入算法指定生成的Verify对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let verifier1 = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256');

let verifier2 = cryptoFramework.createVerify('RSA1024|PSS|SHA256|MGF1_SHA256');

let verifier3 = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256|Recover');
```

#### Verify

Verify类，使用Verify方法之前需要创建该类的实例进行操作，通过[createVerify(algName: string): Verify](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateverify)方法构造此实例。按序调用本类中的init、update、verify方法完成签名操作。验签操作的示例代码详见[签名验签开发指导](../../guides/使用RSA密钥对（PKCS1模式）签名验签.md)。

Verify类不支持重复初始化，当业务方需要使用新密钥验签时，需要重新创建新Verify对象并调用init初始化。

业务方使用时，在createVerify时确定验签的模式，调用init接口设置密钥。

当被签名的消息较短时，可在init初始化后，（无需update）直接调用verify接口传入被签名的消息和签名(signatureData)进行验签。

当被签名的消息较长时，可通过update接口分段传入被签名的消息，最后调用verify接口对消息全文进行验签。verify接口的data入参在API 10之前只支持DataBlob， API 10之后增加支持null。业务方可在循环中调用update接口，循环结束后调用verify传入签名(signatureData)进行验签。

当使用DSA算法进行验签，并设置了摘要算法为NoHash时，则不支持update操作，update接口会返回错误码ERR_CRYPTO_OPERATION。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 是 | 否 | 验签指定的算法名称。 |

#### init

init(pubKey: PubKey, callback: AsyncCallback<void>): void

传入公钥初始化Verify对象。使用callback异步回调。init、update、verify为三段式接口，需要成组使用。其中init和verify必选，update可选。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pubKey | PubKey | 是 | 公钥对象，用于Verify的初始化。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当验签初始化成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### init

init(pubKey: PubKey): Promise<void>

传入公钥初始化Verify对象。使用Promise异步回调。init、update、verify为三段式接口，需要成组使用。其中init和verify必选，update可选。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pubKey | PubKey | 是 | 公钥对象，用于Verify的初始化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### initSync12+

initSync(pubKey: PubKey): void

传入公钥初始化Verify对象，通过同步方式获取结果。initSync、updateSync、verifySync为三段式接口，需要成组使用。其中initSync和verifySync必选，updateSync可选。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pubKey | PubKey | 是 | 公钥对象，用于Verify的初始化。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | 无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### update

update(data: DataBlob, callback: AsyncCallback<void>): void

追加待验签数据，使用callback异步回调完成更新。

必须在对[Verify](#ZH-CN_TOPIC_0000002553201293__verify)实例使用[init](#ZH-CN_TOPIC_0000002553201293__init-4)初始化后，才能使用本函数。


根据数据量，可以不调用update（即[init](#ZH-CN_TOPIC_0000002553201293__init-4)完成后直接调用[verify](#ZH-CN_TOPIC_0000002553201293__verify-1)）或多次调用update。

算法库目前没有对update（单次或累计）的数据量设置大小限制，建议对于大数据量的验签操作，采用多次update的方式传入数据，避免一次性申请过大内存。

验签使用多次update操作的示例代码详见[使用RSA密钥对分段签名验签](../../guides/使用RSA密钥对分段签名验签（PKCS1模式）.md)，其余算法操作类似。

当使用DSA算法进行验签，并设置了摘要算法为NoHash时，则不支持update操作，update接口会返回错误码ERR_CRYPTO_OPERATION。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | 是 | 传入的消息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当验签更新成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### update

update(data: DataBlob): Promise<void>

追加待验签数据，使用Promise异步回调完成更新。

必须在对[Verify](#ZH-CN_TOPIC_0000002553201293__verify)实例使用[init()](#ZH-CN_TOPIC_0000002553201293__init-5)初始化后，才能使用本函数。


根据数据量，可以不调用update（即[init](#ZH-CN_TOPIC_0000002553201293__init-5)完成后直接调用[verify](#ZH-CN_TOPIC_0000002553201293__verify-2)）或多次调用update。

算法库目前没有对update（单次或累计）的数据量设置大小限制，建议对于大数据量的验签操作，采用多次update的方式传入数据，避免一次性申请过大内存。

验签使用多次update操作的示例代码详见[使用RSA密钥对分段签名验签](../../guides/使用RSA密钥对分段签名验签（PKCS1模式）.md)，其余算法操作类似。

当使用DSA算法进行验签，并设置了摘要算法为NoHash时，则不支持update操作，update接口会返回错误码ERR_CRYPTO_OPERATION。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | 是 | 传入的消息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### updateSync12+

updateSync(data: DataBlob): void

追加待验签数据，通过同步方式完成更新。

必须在对[Verify](#ZH-CN_TOPIC_0000002553201293__verify)实例使用[initSync()](#ZH-CN_TOPIC_0000002553201293__initsync12-2)初始化后，才能使用本函数。


根据数据量，可以不调用updateSync（即[initSync](#ZH-CN_TOPIC_0000002553201293__initsync12-2)完成后直接调用[verifySync](#ZH-CN_TOPIC_0000002553201293__verifysync12)）或多次调用updateSync。

算法库目前没有对updateSync（单次或累计）的数据量设置大小限制，建议对于大数据量的验签操作，采用多次updateSync的方式传入数据，避免一次性申请过大内存。

验签使用多次updateSync操作的示例代码详见[使用RSA密钥对分段签名验签](../../guides/使用RSA密钥对分段签名验签（PKCS1模式）.md)，其余算法操作类似。

当使用DSA算法进行验签，并设置了摘要算法为NoHash时，则不支持updateSync操作，updateSync接口会返回错误码ERR_CRYPTO_OPERATION。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | 是 | 传入的消息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | 无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### verify

verify(data: DataBlob | null, signatureData: DataBlob, callback: AsyncCallback<boolean>): void

对数据进行验签。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | null10+ | 是 | 传入的消息。API 10之前只支持DataBlob， API 10之后增加支持null。 |
| signatureData | DataBlob | 是 | 签名数据。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数，用于获取以boolean值表示的验签结果。返回true表示验签通过；返回false表示验签不通过。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### verify

verify(data: DataBlob | null, signatureData: DataBlob): Promise<boolean>

对数据进行验签。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | null10+ | 是 | 传入的消息。API 10之前只支持DataBlob， API 10之后增加支持null。 |
| signatureData | DataBlob | 是 | 签名数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 异步返回值，代表验签是否通过。true为通过，false为不通过。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### verifySync12+

verifySync(data: DataBlob | null, signatureData: DataBlob): boolean

对数据进行验签，通过同步方式返回验签结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | DataBlob | null | 是 | 传入的消息。 |
| signatureData | DataBlob | 是 | 签名数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 同步返回值，表示验签是否通过。true为通过，false为不通过。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**callback示例：**

此外，更多签名验签的完整示例可参考[签名验签开发指导](../../guides/使用RSA密钥对（PKCS1模式）签名验签.md)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function verifyByCallback() {
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputVerify: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  // 根据密钥数据生成的密钥和输入的验签数据，这部分代码Verify与Sign中保持一致，保证验签通过。
  let pkData =
    new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1]);
  let skData =
    new Uint8Array([48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184]);
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pkData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: skData };
  // 该数据取自Sign中的signData.data。
  let signMessageBlob: cryptoFramework.DataBlob = {
    data: new Uint8Array([9, 68, 164, 161, 230, 155, 255, 153, 10, 12, 14, 22, 146, 115, 209, 167, 223, 133, 89, 173,
      50, 249, 176, 104, 10, 251, 219, 104, 117, 196, 105, 65, 249, 139, 119, 41, 15, 171, 191, 11, 177, 177, 1, 119,
      130, 142, 87, 183, 32, 220, 226, 28, 38, 73, 222, 172, 153, 26, 87, 58, 188, 42, 150, 67, 94, 214, 147, 64, 202,
      87, 155, 125, 254, 112, 95, 176, 255, 207, 106, 43, 228, 153, 131, 240, 120, 88, 253, 179, 207, 207, 110, 223,
      173, 15, 113, 11, 183, 122, 237, 205, 206, 123, 246, 33, 167, 169, 251, 237, 199, 26, 220, 152, 190, 117, 131, 74,
      232, 50, 39, 172, 232, 178, 112, 73, 251, 235, 131, 209])
  }
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let verifier = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256');
  rsaGenerator.convertKey(pubKeyBlob, priKeyBlob, (err, keyPair) => {
    verifier.init(keyPair.pubKey, err => {
      verifier.update(inputUpdate, err => {
        verifier.verify(inputVerify, signMessageBlob, (err, res) => {
          console.info('verify result = ' + res);
  });
}
```

**Promise示例：**

更多示例请参见[签名验签开发指导](../../guides/使用RSA密钥对（PKCS1模式）签名验签.md)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = await rsaGenerator.convertKey(pubKeyBlob, priKeyBlob);
  console.info('convertKey result: success.');
  return keyPair;
}

async function verifyByPromise() {
  // 根据密钥数据生成的密钥和输入的验签数据，这部分代码Verify与Sign中保持一致，保证验签通过。
  let pkData =
    new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1]);
  let skData =
    new Uint8Array([48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184]);
  let keyPair = await genKeyPairByData(pkData, skData);
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputVerify: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  // 该数据取自Sign中的signData.data。
  let signMessageBlob: cryptoFramework.DataBlob = {
    data: new Uint8Array([9, 68, 164, 161, 230, 155, 255, 153, 10, 12, 14, 22, 146, 115, 209, 167, 223, 133, 89, 173,
      50, 249, 176, 104, 10, 251, 219, 104, 117, 196, 105, 65, 249, 139, 119, 41, 15, 171, 191, 11, 177, 177, 1, 119,
      130, 142, 87, 183, 32, 220, 226, 28, 38, 73, 222, 172, 153, 26, 87, 58, 188, 42, 150, 67, 94, 214, 147, 64, 202,
      87, 155, 125, 254, 112, 95, 176, 255, 207, 106, 43, 228, 153, 131, 240, 120, 88, 253, 179, 207, 207, 110, 223,
      173, 15, 113, 11, 183, 122, 237, 205, 206, 123, 246, 33, 167, 169, 251, 237, 199, 26, 220, 152, 190, 117, 131, 74,
      232, 50, 39, 172, 232, 178, 112, 73, 251, 235, 131, 209])
  };
  let verifier = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256');
  await verifier.init(keyPair.pubKey);
  await verifier.update(inputUpdate);
  let res = await verifier.verify(inputVerify, signMessageBlob);
  console.info('verify result: ' + res);
}
```

**Sync示例：**

此外，更多签名验签的完整示例可参考[签名验签开发指导](../../guides/使用RSA密钥对（PKCS1模式）签名验签.md)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = rsaGenerator.convertKeySync(pubKeyBlob, priKeyBlob);
  console.info('convertKey result: success.');
  return keyPair;
}

function verifyBySync() {
  // 根据密钥数据生成的密钥和输入的验签数据，这部分代码Verify与Sign中保持一致，保证验签通过。
  let pkData =
    new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1]);
  let skData =
    new Uint8Array([48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184]);
  let keyPair = genKeyPairByData(pkData, skData);
  let inputUpdate: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan1', 'utf-8').buffer) };
  let inputVerify: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is Sign test plan2', 'utf-8').buffer) };
  // 该数据取自Sign中的signData.data。
  let signMessageBlob: cryptoFramework.DataBlob = {
    data: new Uint8Array([9, 68, 164, 161, 230, 155, 255, 153, 10, 12, 14, 22, 146, 115, 209, 167, 223, 133, 89, 173,
      50, 249, 176, 104, 10, 251, 219, 104, 117, 196, 105, 65, 249, 139, 119, 41, 15, 171, 191, 11, 177, 177, 1, 119,
      130, 142, 87, 183, 32, 220, 226, 28, 38, 73, 222, 172, 153, 26, 87, 58, 188, 42, 150, 67, 94, 214, 147, 64, 202,
      87, 155, 125, 254, 112, 95, 176, 255, 207, 106, 43, 228, 153, 131, 240, 120, 88, 253, 179, 207, 207, 110, 223,
      173, 15, 113, 11, 183, 122, 237, 205, 206, 123, 246, 33, 167, 169, 251, 237, 199, 26, 220, 152, 190, 117, 131, 74,
      232, 50, 39, 172, 232, 178, 112, 73, 251, 235, 131, 209])
  };
  let verifier = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256');
  verifier.initSync(keyPair.pubKey);
  verifier.updateSync(inputUpdate);
  let res = verifier.verifySync(inputVerify, signMessageBlob);
  console.info('verify result: ' + res);
}
```

#### recover12+

recover(signatureData: DataBlob): Promise<DataBlob | null>

对数据进行签名恢复原始数据。使用Promise异步回调。


- 目前仅RSA支持。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| signatureData | DataBlob | 是 | 签名数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DataBlob | null> | 验签恢复的数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function genKeyPairByData(pubKeyData: Uint8Array, priKeyData: Uint8Array) {
  let pubKeyBlob: cryptoFramework.DataBlob = { data: pubKeyData };
  let priKeyBlob: cryptoFramework.DataBlob = { data: priKeyData };
  let rsaGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = await rsaGenerator.convertKey(pubKeyBlob, priKeyBlob);
  console.info('convertKey result: success.');
  return keyPair;
}

async function recoverByPromise() {
  // 根据密钥数据生成的密钥和输入的验签数据，这部分代码Verify与Sign中保持一致，保证验签通过。
  let pkData =
    new Uint8Array([48, 129, 159, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 3, 129, 141, 0, 48, 129, 137,
      2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166, 209, 250, 142, 74, 216,
      58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31, 172, 151, 252, 185, 123,
      20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31, 214, 93, 115, 247, 69,
      94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176, 57, 125, 235, 51, 88,
      135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50, 189, 88, 254, 255, 146,
      244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1]);
  let skData =
    new Uint8Array([48, 130, 2, 120, 2, 1, 0, 48, 13, 6, 9, 42, 134, 72, 134, 247, 13, 1, 1, 1, 5, 0, 4, 130, 2, 98, 48,
      130, 2, 94, 2, 1, 0, 2, 129, 129, 0, 214, 179, 23, 198, 183, 139, 148, 8, 173, 74, 56, 160, 15, 248, 244, 166,
      209, 250, 142, 74, 216, 58, 117, 215, 178, 247, 254, 39, 180, 227, 85, 201, 59, 133, 209, 221, 26, 9, 116, 31,
      172, 151, 252, 185, 123, 20, 25, 7, 92, 129, 5, 196, 239, 214, 126, 254, 154, 188, 239, 144, 161, 171, 65, 42, 31,
      214, 93, 115, 247, 69, 94, 143, 54, 51, 25, 49, 146, 204, 205, 165, 20, 120, 35, 184, 190, 65, 106, 12, 214, 176,
      57, 125, 235, 51, 88, 135, 76, 73, 109, 112, 147, 138, 198, 252, 5, 20, 245, 51, 7, 32, 108, 89, 125, 204, 50,
      189, 88, 254, 255, 146, 244, 244, 149, 79, 54, 216, 45, 89, 2, 3, 1, 0, 1, 2, 129, 129, 0, 152, 111, 145, 203, 10,
      88, 116, 163, 112, 126, 9, 20, 68, 34, 235, 121, 98, 14, 182, 102, 151, 125, 114, 91, 210, 122, 215, 29, 212, 5,
      176, 203, 238, 146, 5, 190, 41, 21, 91, 56, 125, 239, 111, 133, 53, 200, 192, 56, 132, 202, 42, 145, 120, 3, 224,
      40, 223, 46, 148, 29, 41, 92, 17, 40, 12, 72, 165, 69, 192, 211, 142, 233, 81, 202, 177, 235, 156, 27, 179, 48,
      18, 85, 154, 101, 193, 45, 218, 91, 24, 143, 196, 248, 16, 83, 177, 198, 136, 77, 111, 134, 60, 219, 95, 246, 23,
      5, 45, 14, 83, 29, 137, 248, 159, 28, 132, 142, 205, 99, 226, 213, 84, 232, 57, 130, 156, 81, 191, 237, 2, 65, 0,
      255, 158, 212, 13, 43, 132, 244, 135, 148, 161, 232, 219, 20, 81, 196, 102, 103, 44, 110, 71, 100, 62, 73, 200,
      32, 138, 114, 209, 171, 150, 179, 92, 198, 5, 190, 218, 79, 227, 227, 37, 32, 57, 159, 252, 107, 211, 139, 198,
      202, 248, 137, 143, 186, 205, 106, 81, 85, 207, 134, 148, 110, 204, 243, 27, 2, 65, 0, 215, 4, 181, 121, 57, 224,
      170, 168, 183, 159, 152, 8, 74, 233, 80, 244, 146, 81, 48, 159, 194, 199, 36, 187, 6, 181, 182, 223, 115, 133,
      151, 171, 78, 219, 90, 161, 248, 69, 6, 207, 173, 3, 81, 161, 2, 60, 238, 204, 177, 12, 138, 17, 220, 179, 71,
      113, 200, 248, 159, 153, 252, 150, 180, 155, 2, 65, 0, 190, 202, 185, 211, 170, 171, 238, 40, 84, 84, 21, 13, 144,
      57, 7, 178, 183, 71, 126, 120, 98, 229, 235, 4, 40, 229, 173, 149, 185, 209, 29, 199, 29, 54, 164, 161, 38, 8, 30,
      62, 83, 179, 47, 42, 165, 0, 156, 207, 160, 39, 169, 229, 81, 180, 136, 170, 116, 182, 20, 233, 45, 90, 100, 9, 2,
      65, 0, 152, 255, 47, 198, 15, 201, 238, 133, 89, 11, 133, 153, 184, 252, 37, 239, 177, 65, 118, 80, 231, 190, 222,
      66, 250, 118, 72, 166, 221, 67, 156, 245, 119, 138, 28, 6, 142, 107, 71, 122, 116, 200, 156, 199, 237, 152, 191,
      239, 4, 184, 64, 114, 143, 81, 62, 48, 23, 233, 217, 95, 47, 221, 104, 171, 2, 64, 30, 219, 1, 230, 241, 70, 246,
      243, 121, 174, 67, 66, 11, 99, 202, 17, 52, 234, 78, 29, 3, 57, 51, 123, 149, 86, 64, 192, 73, 199, 108, 101, 55,
      232, 41, 114, 153, 237, 253, 52, 205, 148, 45, 86, 186, 241, 182, 183, 42, 77, 252, 195, 29, 158, 173, 3, 182,
      207, 254, 61, 71, 184, 167, 184]);
  let keyPair = await genKeyPairByData(pkData, skData);
  // 该数据取自Sign中的signData.data。
  let signMessageBlob: cryptoFramework.DataBlob = {
    data: new Uint8Array([9, 68, 164, 161, 230, 155, 255, 153, 10, 12, 14, 22, 146, 115, 209, 167, 223, 133, 89, 173,
      50, 249, 176, 104, 10, 251, 219, 104, 117, 196, 105, 65, 249, 139, 119, 41, 15, 171, 191, 11, 177, 177, 1, 119,
      130, 142, 87, 183, 32, 220, 226, 28, 38, 73, 222, 172, 153, 26, 87, 58, 188, 42, 150, 67, 94, 214, 147, 64, 202,
      87, 155, 125, 254, 112, 95, 176, 255, 207, 106, 43, 228, 153, 131, 240, 120, 88, 253, 179, 207, 207, 110, 223,
      173, 15, 113, 11, 183, 122, 237, 205, 206, 123, 246, 33, 167, 169, 251, 237, 199, 26, 220, 152, 190, 117, 131, 74,
      232, 50, 39, 172, 232, 178, 112, 73, 251, 235, 131, 209])
  };
  let verifier = cryptoFramework.createVerify('RSA1024|PKCS1|SHA256|Recover');
  await verifier.init(keyPair.pubKey);
  try {
    let rawSignData = await verifier.recover(signMessageBlob);
    if (rawSignData != null) {
      console.info('[Promise]: recover result: ' + rawSignData.data);
    } else {
      console.error('[Promise]: get verify recover result: fail.');
    }
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`promise failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### recoverSync12+

recoverSync(signatureData: DataBlob): DataBlob | null

对数据进行签名恢复原始数据。

- 目前仅RSA支持。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| signatureData | DataBlob | 是 | 签名数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | null | 验签恢复的数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### setVerifySpec10+

setVerifySpec(itemType: SignSpecItem, itemValue: number): void

setVerifySpec(itemType: SignSpecItem, itemValue: number | Uint8Array): void

设置验签参数。常用的签名参数直接通过[createVerify](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreateverify) 来指定，剩余参数通过本接口指定。

支持RSA算法和SM2算法，从API version 11开始，支持SM2算法设置验签参数。

验签的参数应当与签名的参数保持一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemType | SignSpecItem | 是 | 用于指定需要设置的验签参数。 |
| itemValue | number | Uint8Array11+ | 是 | 用于指定验签参数的具体值。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testSetVerifySpec() {
  let verifier = cryptoFramework.createVerify('RSA2048|PSS|SHA256|MGF1_SHA256');
  let setN = 20;
  verifier.setVerifySpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
}
```

#### getVerifySpec10+

getVerifySpec(itemType: SignSpecItem): string | number

获取验签参数。当前只支持RSA算法。

验签的参数应当与签名的参数保持一致。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Signature。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| itemType | SignSpecItem | 是 | 用于指定需要获取的验签参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | number | 获取的验签参数的具体值。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function testGetVerifySpec() {
  let verifier = cryptoFramework.createVerify('RSA2048|PSS|SHA256|MGF1_SHA256');
  let setN = 20;
  verifier.setVerifySpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM, setN);
  verifier.getVerifySpec(cryptoFramework.SignSpecItem.PSS_SALT_LEN_NUM);
}
```

#### cryptoFramework.createKeyAgreement

createKeyAgreement(algName: string): KeyAgreement

生成KeyAgreement实例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.KeyAgreement

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.KeyAgreement。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algName | string | 是 | 指定密钥协商算法：目前仅支持ECC，从API version 11开始，增加支持X25519和DH。 支持的规格详见密钥协商规格。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| KeyAgreement | 返回由输入算法指定生成的KeyAgreement对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
```

#### KeyAgreement

KeyAgreement类，使用密钥协商方法之前需要创建该类的实例进行操作，通过[createKeyAgreement(algName: string): KeyAgreement](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatekeyagreement)方法构造此实例。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.KeyAgreement

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.KeyAgreement。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 是 | 否 | 密钥协商指定的算法名称。 |

#### generateSecret

generateSecret(priKey: PriKey, pubKey: PubKey, callback: AsyncCallback<DataBlob>): void

基于传入的私钥与公钥进行密钥协商。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.KeyAgreement

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.KeyAgreement。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| priKey | PriKey | 是 | 设置密钥协商的私钥输入。 |
| pubKey | PubKey | 是 | 设置密钥协商的公钥输入。 |
| callback | AsyncCallback<DataBlob> | 是 | 异步接受共享密钥的回调。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### generateSecret

generateSecret(priKey: PriKey, pubKey: PubKey): Promise<DataBlob>

基于传入的私钥与公钥进行密钥协商。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.KeyAgreement

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.KeyAgreement。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| priKey | PriKey | 是 | 设置密钥协商的私钥输入。 |
| pubKey | PubKey | 是 | 设置密钥协商的公钥输入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DataBlob> | 共享密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

#### generateSecretSync12+

generateSecretSync(priKey: PriKey, pubKey: PubKey): DataBlob

基于传入的私钥与公钥进行密钥协商，通过同步返回共享密钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.KeyAgreement

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| priKey | PriKey | 是 | 设置密钥协商的私钥输入。 |
| pubKey | PubKey | 是 | 设置密钥协商的公钥输入。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 共享密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**callback示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateSecret() {
  let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  let globalKeyPair = await eccGen.generateKeyPair();
  let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  keyAgreement.generateSecret(globalKeyPair.priKey, globalKeyPair.pubKey, (err, secret) => {
    if (err) {
      console.error('keyAgreement result: fail.');
      return;
    }
    console.info('keyAgreement output = ' + secret.data);
  });
}
```

**Promise示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function testGenerateSecret() {
  let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  let globalKeyPair = await eccGen.generateKeyPair();
  let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  let keyAgreementPromise = keyAgreement.generateSecret(globalKeyPair.priKey, globalKeyPair.pubKey);
  keyAgreementPromise.then(secret => {
    console.info('keyAgreement output = ' + secret.data);
  }).catch((error: BusinessError) => {
    console.error(`keyAgreement failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

**Sync示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

async function testGenerateSecretSync() {
  let eccGen = cryptoFramework.createAsyKeyGenerator('ECC256');
  let globalKeyPair = await eccGen.generateKeyPair();
  let keyAgreement = cryptoFramework.createKeyAgreement('ECC256');
  let secret = keyAgreement.generateSecretSync(globalKeyPair.priKey, globalKeyPair.pubKey);
  console.info('[Sync]keyAgreement output = ' + secret.data);
}
```

#### cryptoFramework.createMd

createMd(algName: string): Md

生成Md实例，用于进行消息摘要的计算与操作。

支持的规格详见[MD消息摘要算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest-overview#支持的算法与规格)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.MessageDigest。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algName | string | 是 | 指定摘要算法，支持算法请参考MD消息摘要算法规格。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Md | 返回由输入算法指定生成的Md对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
17620001memory operation failed.

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Set algName based on the algorithm supported.
  let md = cryptoFramework.createMd('SHA256');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### Md

Md类，调用Md方法进行消息摘要（Message Digest）计算。调用前，需要通过[createMd](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatemd)构造Md实例。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.MessageDigest。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 是 | 否 | 代表指定的摘要算法名。 |

#### update

update(input: DataBlob, callback: AsyncCallback<void>): void

传入消息进行Md更新摘要状态。使用callback异步回调。update和digest为两段式接口，需要成组使用。其中digest必选，update可选。


Md算法多次调用update更新的代码示例详见开发指导[消息摘要计算](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest#分段摘要算法)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.MessageDigest。

**设备行为差异：** 该接口仅在Phone、PC/2in1、Tablet、TV、Wearable设备中可正常调用，在Lite Wearable设备中返回undefined。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | DataBlob | 是 | 传入的消息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当摘要更新成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### update

update(input: DataBlob): Promise<void>

传入消息进行Md更新摘要状态。使用Promise异步回调。update和digest为两段式接口，需要成组使用。其中digest必选，update可选。


Md算法多次调用update更新的代码示例详见开发指导[消息摘要计算](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest#分段摘要算法)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.MessageDigest。

**设备行为差异：** 该接口仅在Phone、PC/2in1、Tablet、TV、Wearable设备中可正常调用，在Lite Wearable设备中返回undefined。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | DataBlob | 是 | 传入的消息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### updateSync12+

updateSync(input: DataBlob): void

传入消息进行Md更新摘要状态，通过同步方式更新。updateSync和digestSync为两段式接口，需要成组使用。其中digestSync必选，updateSync可选。

Md算法多次调用updateSync更新的代码示例详见开发指导[消息摘要计算](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-message-digest#分段摘要算法)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | DataBlob | 是 | 传入的消息。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### digest

digest(callback: AsyncCallback<DataBlob>): void

返回Md的计算结果。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.MessageDigest。

**设备行为差异：** 该接口仅在Phone、PC/2in1、Tablet、TV、Wearable设备中可正常调用，在Lite Wearable设备中返回undefined。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<DataBlob> | 是 | 回调函数，用于获取DataBlob数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function mdByCallback() {
  let md = cryptoFramework.createMd('SHA256');
  md.update({ data: new Uint8Array(buffer.from('mdTestMessage', 'utf-8').buffer) }, (err) => {
    md.digest((err, digestOutput) => {
      console.info('[Callback]: MD result: ' + digestOutput.data);
      console.info('[Callback]: MD len: ' + md.getMdLength());
    });
}
```

#### digest

digest(): Promise<DataBlob>

返回Md的计算结果。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.MessageDigest。

**设备行为差异：** 该接口仅在Phone、PC/2in1、Tablet、TV、Wearable设备中可正常调用，在Lite Wearable设备中返回undefined。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DataBlob> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function mdByPromise() {
  let md = cryptoFramework.createMd('SHA256');
  await md.update({ data: new Uint8Array(buffer.from('mdTestMessage', 'utf-8').buffer) });
  let mdOutput = await md.digest();
  console.info('[Promise]: MD result: ' + mdOutput.data);
  console.info('[Promise]: MD len: ' + md.getMdLength());
}
```

#### digestSync12+

digestSync(): DataBlob

通过同步方式返回Md的计算结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示生成的Md计算结果。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function mdBySync() {
  let md = cryptoFramework.createMd('SHA256');
  md.updateSync({ data: new Uint8Array(buffer.from('mdTestMessage', 'utf-8').buffer) });
  let mdOutput = md.digestSync();
  console.info('[Sync]: MD result: ' + mdOutput.data);
  console.info('[Sync]: MD len: ' + md.getMdLength());
}
```

#### getMdLength

getMdLength(): number

获取Md消息摘要的字节长度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.MessageDigest

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.MessageDigest。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回md计算结果的字节长度。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

function getLength() {
  let md = cryptoFramework.createMd('SHA256');
  console.info('[Promise]: MD len: ' + md.getMdLength());
}
```

#### cryptoFramework.createMac

createMac(algName: string): Mac

生成Mac实例，用于消息认证码的计算与操作。

支持的规格详见[HMAC消息认证码算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-mac-overview)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Mac。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algName | string | 是 | 指定摘要算法，支持算法请参考HMAC消息认证码算法规格。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Mac | 返回由输入算法指定生成的Mac对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
17620001memory operation failed.

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Set algName based on the algorithm supported.
  let mac = cryptoFramework.createMac('SHA256');
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### cryptoFramework.createMac18+

createMac(macSpec: MacSpec): Mac

生成Mac实例，用于进行消息认证码的计算与操作。

支持的规格详见[MAC消息认证码算法规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-compute-mac-overview)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| macSpec | MacSpec | 是 | 根据消息验证码的不同算法，指定入参结构体，支持算法请参考MAC消息认证码算法规格。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Mac | 返回由指定入参结构体生成的Mac对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Set algName based on the algorithm supported.
  let spec: cryptoFramework.HmacSpec = {
    algName: 'HMAC',
    mdName: 'SHA256',
  };
  let mac = cryptoFramework.createMac(spec);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${error.code}, errMsg: ${error.message}`);
}
```

#### Mac

Mac类，调用Mac方法进行消息认证码（Message Authentication Code）计算。调用前，需要通过[createMac](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreatemac)构造Mac实例。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Mac。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 是 | 否 | 代表指定的摘要算法名。 |

#### init

init(key: SymKey, callback: AsyncCallback<void>): void

使用对称密钥初始化Mac计算。使用callback异步回调。init、update、doFinal为三段式接口，需要成组使用。其中init和doFinal必选，update可选。


建议通过[HMAC密钥生成规格](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-sym-key-generation-conversion-spec#hmac)创建对称密钥生成器，调用[generateSymKey](#ZH-CN_TOPIC_0000002553201293__generatesymkey)随机生成对称密钥或调用[convertKey](#ZH-CN_TOPIC_0000002553201293__convertkey)传入与密钥规格长度一致的二进制密钥数据生成密钥。

当指定“HMAC”生成对称密钥生成器时，仅支持调用[convertKey](#ZH-CN_TOPIC_0000002553201293__convertkey)传入长度在[1,4096]范围内（单位为byte）的任意二进制密钥数据生成密钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

API version 9-11 系统能力为SystemCapability.Security.CryptoFramework；从API version 12 开始为SystemCapability.Security.CryptoFramework.Mac。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | SymKey | 是 | 对称密钥。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当HMAC初始化成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### init

init(key: SymKey): Promise<void>

使用对称密钥初始化Mac计算。使用Promise异步回调。init、update、doFinal为三段式接口，需要成组使用。其中init和doFinal必选，update可选。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

API version 9-11 系统能力为SystemCapability.Security.CryptoFramework；从API version 12 开始为SystemCapability.Security.CryptoFramework.Mac。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | SymKey | 是 | 对称密钥。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### initSync12+

initSync(key: SymKey): void

使用对称密钥初始化Mac计算，通过同步方式获取结果。initSync、updateSync、doFinalSync为三段式接口，需要成组使用。其中initSync和doFinalSync必选，updateSync可选。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | SymKey | 是 | 对称密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### update

update(input: DataBlob, callback: AsyncCallback<void>): void

传入消息进行Mac更新消息认证码状态。使用callback异步回调。


HMAC算法多次调用update更新的代码示例详见[消息认证码计算](../../guides/消息认证码计算HMAC.md#分段hmac)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Mac。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | DataBlob | 是 | 传入的消息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当HMAC更新成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### update

update(input: DataBlob): Promise<void>

传入消息进行Mac更新消息认证码状态。使用Promise异步回调。


HMAC算法多次调用update更新的代码示例详见[消息认证码计算](../../guides/消息认证码计算HMAC.md#分段hmac)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Mac。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | DataBlob | 是 | 传入的消息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### updateSync12+

updateSync(input: DataBlob): void

传入消息进行Mac更新消息认证码状态，通过同步方式获取结果。

HMAC算法多次调用updateSync更新的代码示例详见[消息认证码计算](../../guides/消息认证码计算HMAC.md#分段hmac)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| input | DataBlob | 是 | 传入的消息。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

#### doFinal

doFinal(callback: AsyncCallback<DataBlob>): void

返回Mac的计算结果。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Mac。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<DataBlob> | 是 | 回调函数，用于获取DataBlob数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

此外，更多HMAC的完整示例可参考开发指导中[消息认证码计算](../../guides/消息认证码计算HMAC.md#分段hmac)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function hmacByCallback() {
  let mac = cryptoFramework.createMac('SHA256');
  let keyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer) };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  symKeyGenerator.convertKey(keyBlob, (err, symKey) => {
    mac.init(symKey, (err) => {
      mac.update({ data: new Uint8Array(buffer.from('hmacTestMessage', 'utf-8').buffer) }, (err) => {
        mac.doFinal((err, output) => {
          console.info('[Callback]: HMAC result: ' + output.data);
          console.info('[Callback]: MAC len: ' + mac.getMacLength());
        });
}
```

#### doFinal

doFinal(): Promise<DataBlob>

返回Mac的计算结果。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Mac。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DataBlob> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

此外，更多HMAC的完整示例可参考开发指导[消息认证码计算](../../guides/消息认证码计算HMAC.md#分段hmac)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function hmacByPromise() {
  let mac = cryptoFramework.createMac('SHA256');
  let keyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer) };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = await symKeyGenerator.convertKey(keyBlob);
  await mac.init(symKey);
  await mac.update({ data: new Uint8Array(buffer.from('hmacTestMessage', 'utf-8').buffer) });
  let macOutput = await mac.doFinal();
  console.info('[Promise]: HMAC result: ' + macOutput.data);
  console.info('[Promise]: MAC len: ' + mac.getMacLength());
}
```

#### doFinalSync12+

doFinalSync(): DataBlob

通过同步方式返回Mac的计算结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 返回Mac的计算结果。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**示例：**

此外，更多HMAC的完整示例可参考开发指导[消息认证码计算](../../guides/消息认证码计算HMAC.md#分段hmac)。

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function hmacBySync() {
  let mac = cryptoFramework.createMac('SHA256');
  let keyBlob: cryptoFramework.DataBlob = { data: new Uint8Array(buffer.from('12345678abcdefgh', 'utf-8').buffer) };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let symKey = symKeyGenerator.convertKeySync(keyBlob);
  mac.initSync(symKey);
  mac.updateSync({ data: new Uint8Array(buffer.from('hmacTestMessage', 'utf-8').buffer) });
  let macOutput = mac.doFinalSync();
  console.info('[Sync]: HMAC result: ' + macOutput.data);
  console.info('[Sync]: MAC len: ' + mac.getMacLength());
}
```

#### getMacLength

getMacLength(): number

获取Mac消息认证码的长度（字节数）。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Mac

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Mac。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回Mac计算结果的字节长度。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function testGetMacLength() {
  let mac = cryptoFramework.createMac('SHA256');
  console.info('Mac algName is: ' + mac.algName);
  let keyData = new Uint8Array([83, 217, 231, 76, 28, 113, 23, 219, 250, 71, 209, 210, 205, 97, 32, 159]);
  let keyBlob: cryptoFramework.DataBlob = { data: keyData };
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES128');
  let promiseConvertKey = symKeyGenerator.convertKey(keyBlob);
  promiseConvertKey.then(symKey => {
    let promiseMacInit = mac.init(symKey);
    return promiseMacInit;
  })
    .then(() => {
    let blob: cryptoFramework.DataBlob = { data : new Uint8Array([83])};
    let promiseMacUpdate = mac.update(blob);
    return promiseMacUpdate;
    })
    .then(() => {
    let promiseMacDoFinal = mac.doFinal();
    return promiseMacDoFinal;
    })
    .then(macOutput => {
    console.info('[Promise]: HMAC result: ' + macOutput.data);
    let macLen = mac.getMacLength();
    console.info('MAC len: ' + macLen);
    })
    .catch((error: BusinessError) => {
      console.error(`[Promise] failed: errCode: ${error.code}, errMsg: ${error.message}`);
  });
}
```

#### cryptoFramework.createRandom

createRandom(): Random

生成Random实例，用于进行随机数的计算与设置种子。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Rand。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Random | 返回由输入算法指定生成的Random对象。 支持的规格详见框架概述随机数算法规格。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let rand = cryptoFramework.createRandom();
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### Random

Random类，调用Random方法生成随机数。调用前，需要通过[createRandom](#ZH-CN_TOPIC_0000002553201293__cryptoframeworkcreaterandom)构造Random实例。

#### 属性

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Rand。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName10+ | string | 是 | 否 | 代表当前使用的随机数生成算法，目前只支持“CTR_DRBG"。 |

#### generateRandom

generateRandom(len: number, callback: AsyncCallback<DataBlob>): void

生成指定长度的随机数。使用callback异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Rand。

**设备行为差异：** 该接口仅在Phone、PC/2in1、Tablet、TV、Wearable设备中可正常调用，在Lite Wearable设备中返回undefined。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| len | number | 是 | 表示生成随机数的长度，单位为byte，范围在[1, INT_MAX]。 |
| callback | AsyncCallback<DataBlob> | 是 | 回调函数，用于获取DataBlob数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let rand = cryptoFramework.createRandom();
rand.generateRandom(12, (err, randData) => {
  if (err) {
    console.error(`[Callback] failed, errCode: ${err.code}, errMsg: ${err.message}`);
  } else {
    console.info('[Callback]: generate random result: ' + randData.data);
  }
});
```

#### generateRandom

generateRandom(len: number): Promise<DataBlob>

生成指定长度的随机数。使用promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Rand。

**设备行为差异：** 该接口仅在Phone、PC/2in1、Tablet、TV、Wearable设备中可正常调用，在Lite Wearable设备中返回undefined。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| len | number | 是 | 表示生成随机数的长度，单位为byte，范围在[1, INT_MAX]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DataBlob> | Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
let promiseGenerateRand = rand.generateRandom(12);
promiseGenerateRand.then(randData => {
  console.info('[Promise]: rand result: ' + randData.data);
}).catch((error: BusinessError) => {
  console.error(`[Promise] failed: errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### generateRandomSync10+

generateRandomSync(len: number): DataBlob

同步生成指定长度的随机数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

API version 10-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Rand。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| len | number | 是 | 表示生成随机数的长度，单位为byte，范围在[1, INT_MAX]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 表示生成的随机数。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
try {
  let randData = rand.generateRandomSync(12);
  if (randData != null) {
    console.info('[Sync]: rand result: ' + randData.data);
  } else {
    console.error('[Sync]: get rand result: fail.');
  }
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### enableHardwareEntropy21+

enableHardwareEntropy(): void

开启硬件熵源。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17630001 | crypto operation error. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
rand.enableHardwareEntropy();
rand.generateRandom(12, (err, randData) => {
  if (err) {
    console.error('[Callback] err: ' + err.code);
  } else {
    console.info('[Callback]: generate random result: ' + randData.data);
    try {
      rand.setSeed(randData);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### setSeed

setSeed(seed: DataBlob): void

设置指定的种子。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Rand

API version 9-11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Rand。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| seed | DataBlob | 是 | 设置的种子。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rand = cryptoFramework.createRandom();
rand.generateRandom(12, (err, randData) => {
  if (err) {
    console.error('[Callback] err: ' + err.code);
  } else {
    console.info('[Callback]: generate random result: ' + randData.data);
    try {
      rand.setSeed(randData);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`sync failed: errCode: ${e.code}, errMsg: ${e.message}`);
  }
});
```

#### cryptoFramework.createKdf11+

createKdf(algName: string): Kdf

密钥派生函数（key derivation function）实例生成。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Kdf。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| algName | string | 是 | 指定密钥派生算法（包含HMAC配套的散列函数）：目前支持PBKDF2、HKDF算法、SCRYPT算法，如"PBKDF2|SHA256", "HKDF|SHA256", "SCRYPT"。 支持的规格详见密钥派生函数规格。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Kdf | 返回由输入算法指定生成的Kdf对象。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | this operation is not supported. |
| 17620001 | memory operation failed. |

**示例：**

- PBKDF2算法

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
```

#### Kdf11+

密钥派生函数（key derivation function）类，使用密钥派生方法之前需要创建该类的实例进行操作，通过createKdf(algName: string): Kdf方法构造此实例。

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Kdf。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| algName | string | 是 | 否 | 密钥派生函数的算法名称。 |

#### generateSecret11+

generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void

基于传入的密钥派生参数进行密钥派生。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Kdf。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | KdfSpec | 是 | 设置密钥派生函数的参数。 |
| callback | AsyncCallback<DataBlob> | 是 | 回调函数，用于获取派生得到的密钥DataBlob数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620003 | parameter check failed. Possible causes: 1. Invalid key length in the params; 2. Invalid info length in the params; 3. Invalid keySize in the params. |
17630001crypto operation error.

**示例：**

-

PBKDF2算法
```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let spec: cryptoFramework.PBKDF2Spec = {
  algName: 'PBKDF2',
  password: '123456',
  salt: new Uint8Array(16),
  iterations: 10000,
  keySize: 32
};
let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
kdf.generateSecret(spec, (err, secret) => {
  if (err) {
    console.error('key derivation result: fail.');
    return;
  }
  console.info('key derivation output = ' + secret.data);
});
```

-

HKDF算法
```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let spec: cryptoFramework.HKDFSpec = {
  algName: 'HKDF',
  key: '123456',
  salt: new Uint8Array(16),
  info: new Uint8Array(16),
  keySize: 32
};
let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT_AND_EXPAND');
kdf.generateSecret(spec, (err, secret) => {
  if (err) {
    console.error('key derivation result: fail.');
    return;
  }
  console.info('key derivation output = ' + secret.data);
});
```

#### generateSecret11+

generateSecret(params: KdfSpec): Promise<DataBlob>

基于传入的密钥派生参数进行密钥派生。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

API version 11系统能力为SystemCapability.Security.CryptoFramework；从API version 12开始为SystemCapability.Security.CryptoFramework.Kdf。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | KdfSpec | 是 | 设置密钥派生函数的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<DataBlob> | 通过Promise形式返回派生得到的密钥。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620003 | parameter check failed. Possible causes: 1. Invalid key length in the params; 2. Invalid info length in the params; 3. Invalid keySize in the params. |
17630001crypto operation error.

**示例：**

-

PBKDF2算法
```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let spec: cryptoFramework.PBKDF2Spec = {
  algName: 'PBKDF2',
  password: '123456',
  salt: new Uint8Array(16),
  iterations: 10000,
  keySize: 32
};
let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
let kdfPromise = kdf.generateSecret(spec);
kdfPromise.then(secret => {
  console.info('key derivation output = ' + secret.data);
}).catch((error: BusinessError) => {
  console.error(`key derivation failed: errCode: ${error.code}, errMsg: ${error.message}`);
});
```

-

HKDF算法
```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

let spec: cryptoFramework.HKDFSpec = {
  algName: 'HKDF',
  key: '123456',
  salt: new Uint8Array(16),
  info: new Uint8Array(16),
  keySize: 32
};
let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT_AND_EXPAND');
let kdfPromise = kdf.generateSecret(spec);
kdfPromise.then(secret => {
  console.info('key derivation output = ' + secret.data);
}).catch((error: BusinessError) => {
  console.error(`key derivation failed: errCode: ${error.code}, errMsg: ${error.message}`);
});
```

#### generateSecretSync12+

generateSecretSync(params: KdfSpec): DataBlob

基于传入的密钥派生参数进行密钥派生，通过同步方式返回派生得到的密钥。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Kdf

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | KdfSpec | 是 | 设置密钥派生函数的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| DataBlob | 用于获取派生得到的密钥DataBlob数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | invalid parameters. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. Invalid key length in the params; 2. Invalid info length in the params; 3. Invalid keySize in the params. |
17630001crypto operation error.

**示例：**

-

PBKDF2算法
```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let spec: cryptoFramework.PBKDF2Spec = {
  algName: 'PBKDF2',
  password: '123456',
  salt: new Uint8Array(16),
  iterations: 10000,
  keySize: 32
};
let kdf = cryptoFramework.createKdf('PBKDF2|SHA256');
let secret = kdf.generateSecretSync(spec);
console.info('[Sync]key derivation output = ' + secret.data);
```

-

HKDF算法
```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';

let spec: cryptoFramework.HKDFSpec = {
  algName: 'HKDF',
  key: '123456',
  salt: new Uint8Array(16),
  info: new Uint8Array(16),
  keySize: 32
};
let kdf = cryptoFramework.createKdf('HKDF|SHA256|EXTRACT_AND_EXPAND');
let secret = kdf.generateSecretSync(spec);
console.info('[Sync]key derivation output = ' + secret.data);
```

#### SignatureUtils20+

用于SM2数据转换的工具类。

#### genEccSignatureSpec20+

static genEccSignatureSpec(data: Uint8Array): EccSignatureSpec

从ASN1 DER格式的sm2签名数据获取r和s。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | 是 | ASN1 DER格式的签名数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| EccSignatureSpec | 包含r和s的数据结构体。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. The length of the data parameter is 0 or too large. |
17630001crypto operation error.

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function testGenEccSignatureSpec() {
  try {
    let data =
      new Uint8Array([48, 69, 2, 33, 0, 216, 15, 76, 238, 158, 165, 108, 76, 72, 63, 115, 52, 255, 51, 149, 54, 224,
        179, 49, 225, 70, 36, 117, 88, 154, 154, 27, 194, 161, 3, 1, 115, 2, 32, 51, 9, 53, 55, 248, 82, 7, 159, 179,
        144, 57, 151, 195, 17, 31, 106, 123, 32, 139, 219, 6, 253, 62, 240, 181, 134, 214, 107, 27, 230, 175, 40])
    let spec: cryptoFramework.EccSignatureSpec = cryptoFramework.SignatureUtils.genEccSignatureSpec(data)
    console.info('genEccSignatureSpec result: success.');
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`ecc failed: errCode: ${e.code}, errMsg: ${e.message}`);
}
```

#### genEccSignature20+

static genEccSignature(spec: EccSignatureSpec): Uint8Array;

将（r、s）的sm2签名数据转换为ASN1 DER格式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Security.CryptoFramework.Signature

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| spec | EccSignatureSpec | 是 | （r、s）的sm2签名数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Uint8Array | ASN1 DER格式的签名数据。 |

**错误码：**

以下错误码的详细介绍请参见[crypto framework错误码](crypto framework错误码.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17620001 | memory operation failed. |
| 17620002 | failed to convert parameters between arkts and c. |
| 17620003 | parameter check failed. Possible causes: 1. The r or s value of the spec parameter is 0 or too large. |
17630001crypto operation error.

**示例：**

```ets
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';

function testGenEccSignature() {
  try {
    let spec: cryptoFramework.EccSignatureSpec = {
      r: BigInt('97726608965854271693043443511967021777934035174185659091642456228829830775155'),
      s: BigInt('23084224202834231287427338597254751764391338275617140205467537273296855150376'),
    }

    let data = cryptoFramework.SignatureUtils.genEccSignature(spec)
    console.info('genEccSignature result: success.');
    console.info('data = ' + data)
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`ecc failed: errCode: ${e.code}, errMsg: ${e.message}`);
  }
```