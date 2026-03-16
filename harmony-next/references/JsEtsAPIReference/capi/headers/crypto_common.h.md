# crypto_common.h

#### 概述

定义通用API接口。

**引用文件：** <CryptoArchitectureKit/crypto_common.h>

**库：** libohcrypto.so

**系统能力：** SystemCapability.Security.CryptoFramework

**起始版本：** 12

**相关模块：**[CryptoCommonApi](../../topics/networking/CryptoCommonApi.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md)Crypto_DataBlob加解密数据结构体。

#### 枚举

名称typedef关键字描述[OH_Crypto_ErrCode](#ZH-CN_TOPIC_0000002529285349__oh_crypto_errcode)OH_Crypto_ErrCode加解密错误返回码枚举。[Crypto_CipherMode](#ZH-CN_TOPIC_0000002529285349__crypto_ciphermode)Crypto_CipherMode定义加解密操作类型。

#### 函数

名称描述[void OH_Crypto_FreeDataBlob(Crypto_DataBlob *dataBlob)](#ZH-CN_TOPIC_0000002529285349__oh_crypto_freedatablob)释放dataBlob数据。

#### 枚举类型说明

#### OH_Crypto_ErrCode

```ets
enum OH_Crypto_ErrCode
```

**描述**

加解密错误返回码枚举。

**起始版本：** 12

枚举项描述CRYPTO_SUCCESS = 0表示操作成功。CRYPTO_INVALID_PARAMS = 401输入参数不合法。CRYPTO_NOT_SUPPORTED = 801不支持的函数或算法。CRYPTO_MEMORY_ERROR = 17620001内存错误。CRYPTO_PARAMETER_CHECK_FAILED = 17620003

参数检查失败。

**起始版本：** 20

CRYPTO_OPERTION_ERROR = 17630001表示加解密操作错误。

#### Crypto_CipherMode

```ets
enum Crypto_CipherMode
```

**描述**

定义加解密操作类型。

**起始版本：** 12

枚举项描述CRYPTO_ENCRYPT_MODE = 0加密操作。CRYPTO_DECRYPT_MODE = 1解密操作。

#### 函数说明

#### OH_Crypto_FreeDataBlob()

```ets
void OH_Crypto_FreeDataBlob(Crypto_DataBlob *dataBlob)
```

**描述**

释放dataBlob数据。

**起始版本：** 12

**参数：**

参数项描述[Crypto_DataBlob](../../topics/components/Crypto_DataBlob.md) *dataBlob需要释放的dataBlob数据。