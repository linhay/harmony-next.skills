# crypto_signature.h

#### 概述

定义验签接口。

**引用文件：** <CryptoArchitectureKit/crypto_signature.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：**[CryptoSignatureApi](../../topics/networking/CryptoSignatureApi.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_CryptoVerify](../../topics/misc/OH_CryptoVerify.md)OH_CryptoVerify定义验签结构体。[OH_CryptoSign](../../topics/misc/OH_CryptoSign.md)OH_CryptoSign定义签名结构体。[OH_CryptoEccSignatureSpec](../../topics/misc/OH_CryptoEccSignatureSpec.md)OH_CryptoEccSignatureSpec定义ECC签名规范结构体。

#### 枚举

名称typedef关键字描述[CryptoSignature_ParamType](#ZH-CN_TOPIC_0000002497605360__cryptosignature_paramtype)CryptoSignature_ParamType定义签名验签参数类型。

#### 函数

名称描述[OH_Crypto_ErrCode OH_CryptoVerify_Create(const char *algoName, OH_CryptoVerify **verify)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_create)创建验签实例。[OH_Crypto_ErrCode OH_CryptoVerify_Init(OH_CryptoVerify *ctx, OH_CryptoPubKey *pubKey)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_init)传入公钥初始化验签实例。[OH_Crypto_ErrCode OH_CryptoVerify_Update(OH_CryptoVerify *ctx, Crypto_DataBlob *in)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_update)追加待验签数据。[bool OH_CryptoVerify_Final(OH_CryptoVerify *ctx, Crypto_DataBlob *in, Crypto_DataBlob *signData)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_final)对数据进行验签。[OH_Crypto_ErrCode OH_CryptoVerify_Recover(OH_CryptoVerify *ctx, Crypto_DataBlob *signData, Crypto_DataBlob *rawSignData)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_recover)对签名数据进行恢复操作。[const char *OH_CryptoVerify_GetAlgoName(OH_CryptoVerify *ctx)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_getalgoname)获取验签算法名称。[OH_Crypto_ErrCode OH_CryptoVerify_SetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_setparam)设置验签参数。[OH_Crypto_ErrCode OH_CryptoVerify_GetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_getparam)获取验签参数。[void OH_CryptoVerify_Destroy(OH_CryptoVerify *ctx)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_destroy)销毁验签实例。[OH_Crypto_ErrCode OH_CryptoSign_Create(const char *algoName, OH_CryptoSign **sign)](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_create)根据给定的算法名称创建签名实例。[OH_Crypto_ErrCode OH_CryptoSign_Init(OH_CryptoSign *ctx, OH_CryptoPrivKey *privKey)](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_init)初始化签名实例。[OH_Crypto_ErrCode OH_CryptoSign_Update(OH_CryptoSign *ctx, const Crypto_DataBlob *in)](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_update)更新需要签名的数据。[OH_Crypto_ErrCode OH_CryptoSign_Final(OH_CryptoSign *ctx, const Crypto_DataBlob *in, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_final)完成签名操作。[const char *OH_CryptoSign_GetAlgoName(OH_CryptoSign *ctx)](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_getalgoname)获取签名实例的算法名称。[OH_Crypto_ErrCode OH_CryptoSign_SetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, const Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_setparam)设置签名实例的指定参数。[OH_Crypto_ErrCode OH_CryptoSign_GetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_getparam)从签名实例获取指定参数。[void OH_CryptoSign_Destroy(OH_CryptoSign *ctx)](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_destroy)销毁签名实例。[OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Create(Crypto_DataBlob *eccSignature, OH_CryptoEccSignatureSpec **spec)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoeccsignaturespec_create)创建ECC签名规范。[OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_GetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r, Crypto_DataBlob *s)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoeccsignaturespec_getrands)获取ECC签名的r和s值。[OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_SetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r, Crypto_DataBlob *s)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoeccsignaturespec_setrands)设置ECC签名的r和s值。[OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Encode(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *out)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoeccsignaturespec_encode)将ECC签名规范编码为DER格式的签名。[void OH_CryptoEccSignatureSpec_Destroy(OH_CryptoEccSignatureSpec *spec)](#ZH-CN_TOPIC_0000002497605360__oh_cryptoeccsignaturespec_destroy)销毁ECC签名规范。

#### 枚举类型说明

#### CryptoSignature_ParamType

```ets
enum CryptoSignature_ParamType
```

**描述**

定义签名验签参数类型。

**起始版本：** 12

枚举项描述CRYPTO_PSS_MD_NAME_STR = 100表示RSA算法中，使用PSS模式时，消息摘要功能的算法名。CRYPTO_PSS_MGF_NAME_STR = 101表示RSA算法中，使用PSS模式时，掩码生成算法（目前仅支持MGF1）。CRYPTO_PSS_MGF1_NAME_STR = 102表示RSA算法中，使用PSS模式时，MGF1掩码生成功能的消息摘要参数。CRYPTO_PSS_SALT_LEN_INT = 103表示RSA算法中，使用PSS模式时，盐值的长度，长度以字节为单位。CRYPTO_PSS_TRAILER_FIELD_INT = 104表示RSA算法中，使用PSS模式时，用于编码操作的整数，值为1。CRYPTO_SM2_USER_ID_DATABLOB = 105表示SM2算法中，用户身份标识字段。

#### 函数说明

#### OH_CryptoVerify_Create()

```ets
OH_Crypto_ErrCode OH_CryptoVerify_Create(const char *algoName, OH_CryptoVerify **verify)
```

**描述**

创建验签实例。

**起始版本：** 12

**参数：**

参数项描述const char *algoName

用于生成验签实例的算法名称。

 例如"RSA1024|PKCS1|SHA256"

[OH_CryptoVerify](../../topics/misc/OH_CryptoVerify.md) **verify指向验签实例的指针。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoVerify_Init()

```ets
OH_Crypto_ErrCode OH_CryptoVerify_Init(OH_CryptoVerify *ctx, OH_CryptoPubKey *pubKey)
```

**描述**

传入公钥初始化验签实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoVerify](../../topics/misc/OH_CryptoVerify.md) *ctx指向验签实例。[OH_CryptoPubKey](../../topics/misc/OH_CryptoPubKey.md) *pubKey公钥对象。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoVerify_Update](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_update)

[OH_CryptoVerify_Final](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_final)

#### OH_CryptoVerify_Update()

```ets
OH_Crypto_ErrCode OH_CryptoVerify_Update(OH_CryptoVerify *ctx, Crypto_DataBlob *in)
```

**描述**

追加待验签数据。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoVerify](../../topics/misc/OH_CryptoVerify.md) *ctx指向验签实例。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *in传入的消息。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoVerify_Init](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_init)

[OH_CryptoVerify_Final](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_final)

#### OH_CryptoVerify_Final()

```ets
bool OH_CryptoVerify_Final(OH_CryptoVerify *ctx, Crypto_DataBlob *in, Crypto_DataBlob *signData)
```

**描述**

对数据进行验签。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoVerify](../../topics/misc/OH_CryptoVerify.md) *ctx指向验签实例。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *in传入的数据。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *signData签名数据。

**返回：**

类型说明booltrue表示验签通过，false表示验签失败。

**参考：**

[OH_CryptoVerify_Init](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_init)

[OH_CryptoVerify_Update](#ZH-CN_TOPIC_0000002497605360__oh_cryptoverify_update)

#### OH_CryptoVerify_Recover()

```ets
OH_Crypto_ErrCode OH_CryptoVerify_Recover(OH_CryptoVerify *ctx, Crypto_DataBlob *signData,Crypto_DataBlob *rawSignData)
```

**描述**

对签名数据进行恢复操作。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoVerify](../../topics/misc/OH_CryptoVerify.md) *ctx指向验签实例。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *signData签名数据。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *rawSignData验签恢复的数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoVerify_GetAlgoName()

```ets
const char *OH_CryptoVerify_GetAlgoName(OH_CryptoVerify *ctx)
```

**描述**

获取验签算法名称。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoVerify](../../topics/misc/OH_CryptoVerify.md) *ctx指向验签实例。

**返回：**

类型说明const char *返回验签算法名称。

#### OH_CryptoVerify_SetParam()

```ets
OH_Crypto_ErrCode OH_CryptoVerify_SetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type,Crypto_DataBlob *value)
```

**描述**

设置验签参数。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoVerify](../../topics/misc/OH_CryptoVerify.md) *ctx指向验签实例。[CryptoSignature_ParamType](#ZH-CN_TOPIC_0000002497605360__cryptosignature_paramtype) type用于指定需要设置的验签参数。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *value用于指定验签参数的具体值。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoVerify_GetParam()

```ets
OH_Crypto_ErrCode OH_CryptoVerify_GetParam(OH_CryptoVerify *ctx, CryptoSignature_ParamType type,Crypto_DataBlob *value)
```

**描述**

获取验签参数。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoVerify](../../topics/misc/OH_CryptoVerify.md) *ctx指向验签实例。[CryptoSignature_ParamType](#ZH-CN_TOPIC_0000002497605360__cryptosignature_paramtype) type用于指定需要获取的验签参数。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *value获取的验签参数的具体值。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_INVALID_PARAMS：参数无效。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoVerify_Destroy()

```ets
void OH_CryptoVerify_Destroy(OH_CryptoVerify *ctx)
```

**描述**

销毁验签实例。

**起始版本：** 12

**参数：**

参数项描述[OH_CryptoVerify](../../topics/misc/OH_CryptoVerify.md) *ctx指向验签实例。

#### OH_CryptoSign_Create()

```ets
OH_Crypto_ErrCode OH_CryptoSign_Create(const char *algoName, OH_CryptoSign **sign)
```

**描述**

根据给定的算法名称创建签名实例。

**起始版本：** 20

**参数：**

参数项描述const char *algoName

用于生成签名实例的算法名称。

 例如"RSA|PKCS1|SHA384"、"ECC|SHA384"。

[OH_CryptoSign](../../topics/misc/OH_CryptoSign.md) **sign签名实例。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoSign_Init()

```ets
OH_Crypto_ErrCode OH_CryptoSign_Init(OH_CryptoSign *ctx, OH_CryptoPrivKey *privKey)
```

**描述**

初始化签名实例。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSign](../../topics/misc/OH_CryptoSign.md) *ctx指向签名实例。[OH_CryptoPrivKey](../../topics/misc/OH_CryptoPrivKey.md) *privKey私钥。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoSign_Update](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_update)

[OH_CryptoSign_Final](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_final)

#### OH_CryptoSign_Update()

```ets
OH_Crypto_ErrCode OH_CryptoSign_Update(OH_CryptoSign *ctx, const Crypto_DataBlob *in)
```

**描述**

更新需要签名的数据。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSign](../../topics/misc/OH_CryptoSign.md) *ctx指向签名实例。[const Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *in需要签名的数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoSign_Init](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_init)

[OH_CryptoSign_Final](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_final)

#### OH_CryptoSign_Final()

```ets
OH_Crypto_ErrCode OH_CryptoSign_Final(OH_CryptoSign *ctx, const Crypto_DataBlob *in, Crypto_DataBlob *out)
```

**描述**

完成签名操作。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSign](../../topics/misc/OH_CryptoSign.md) *ctx指向签名实例。[const Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *in需要签名的数据。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *out签名结果。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

**参考：**

[OH_CryptoSign_Init](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_init)

[OH_CryptoSign_Update](#ZH-CN_TOPIC_0000002497605360__oh_cryptosign_update)

#### OH_CryptoSign_GetAlgoName()

```ets
const char *OH_CryptoSign_GetAlgoName(OH_CryptoSign *ctx)
```

**描述**

获取签名实例的算法名称。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSign](../../topics/misc/OH_CryptoSign.md) *ctx指向签名实例。

**返回：**

类型说明const char *返回签名算法名称。

#### OH_CryptoSign_SetParam()

```ets
OH_Crypto_ErrCode OH_CryptoSign_SetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type,const Crypto_DataBlob *value)
```

**描述**

设置签名实例的指定参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSign](../../topics/misc/OH_CryptoSign.md) *ctx指向签名实例。[CryptoSignature_ParamType](#ZH-CN_TOPIC_0000002497605360__cryptosignature_paramtype) type签名参数类型。[const Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *value输入数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoSign_GetParam()

```ets
OH_Crypto_ErrCode OH_CryptoSign_GetParam(OH_CryptoSign *ctx, CryptoSignature_ParamType type, Crypto_DataBlob *value)
```

**描述**

从签名实例获取指定参数。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSign](../../topics/misc/OH_CryptoSign.md) *ctx指向签名实例。[CryptoSignature_ParamType](#ZH-CN_TOPIC_0000002497605360__cryptosignature_paramtype) type签名参数类型。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *value输出数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoSign_Destroy()

```ets
void OH_CryptoSign_Destroy(OH_CryptoSign *ctx)
```

**描述**

销毁签名实例。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoSign](../../topics/misc/OH_CryptoSign.md) *ctx指向签名实例。

#### OH_CryptoEccSignatureSpec_Create()

```ets
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Create(Crypto_DataBlob *eccSignature,OH_CryptoEccSignatureSpec **spec)
```

**描述**

创建ECC签名规范。

**起始版本：** 20

**参数：**

参数项描述[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *eccSignatureECC签名（DER格式），如果EccSignature参数为NULL，将创建一个空的ECC签名规范。[OH_CryptoEccSignatureSpec](../../topics/misc/OH_CryptoEccSignatureSpec.md) **spec输出的ECC签名规范。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoEccSignatureSpec_GetRAndS()

```ets
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_GetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r,Crypto_DataBlob *s)
```

**描述**

获取ECC签名的r和s值。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoEccSignatureSpec](../../topics/misc/OH_CryptoEccSignatureSpec.md) *spec指向ECC签名规范。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *rr值。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *ss值。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoEccSignatureSpec_SetRAndS()

```ets
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_SetRAndS(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *r,Crypto_DataBlob *s)
```

**描述**

设置ECC签名的r和s值。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoEccSignatureSpec](../../topics/misc/OH_CryptoEccSignatureSpec.md) *spec指向ECC签名规范。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *rr值。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *ss值。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoEccSignatureSpec_Encode()

```ets
OH_Crypto_ErrCode OH_CryptoEccSignatureSpec_Encode(OH_CryptoEccSignatureSpec *spec, Crypto_DataBlob *out)
```

**描述**

将ECC签名规范编码为DER格式的签名。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoEccSignatureSpec](../../topics/misc/OH_CryptoEccSignatureSpec.md) *spec指向ECC签名规范。[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *out输出数据。

**返回：**

类型说明[OH_Crypto_ErrCode](crypto_common.h.md#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)

CRYPTO_SUCCESS：操作成功。

 CRYPTO_NOT_SUPPORTED：操作不支持。

 CRYPTO_MEMORY_ERROR：内存错误。

 CRYPTO_PARAMETER_CHECK_FAILED：参数检查失败。

 CRYPTO_OPERATION_ERROR：调用三方算法库API出错。

#### OH_CryptoEccSignatureSpec_Destroy()

```ets
void OH_CryptoEccSignatureSpec_Destroy(OH_CryptoEccSignatureSpec *spec)
```

**描述**

销毁ECC签名规范。

**起始版本：** 20

**参数：**

参数项描述[OH_CryptoEccSignatureSpec](../../topics/misc/OH_CryptoEccSignatureSpec.md) *spec指向ECC签名规范。