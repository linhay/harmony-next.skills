# native_huks_api.h

#### 概述

声明用于访问HUKS的API。

**引用文件：** <huks/native_huks_api.h>

**库：** libhuks_ndk.z.so

**系统能力：** SystemCapability.Security.Huks.Core

在API 9-19，系统能力为SystemCapability.Security.Huks；从API 20起，系统能力变更为SystemCapability.Security.Huks.Core

**起始版本：** 9

**相关模块：**[HuksKeyApi](HuksKeyApi.md)

#### 汇总

#### 函数

名称描述[struct OH_Huks_Result OH_Huks_GetSdkVersion(struct OH_Huks_Blob *sdkVersion)](#ZH-CN_TOPIC_0000002497605400__oh_huks_getsdkversion)获取当前Huks sdk版本号。[struct OH_Huks_Result OH_Huks_GenerateKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSetIn, struct OH_Huks_ParamSet *paramSetOut)](#ZH-CN_TOPIC_0000002497605400__oh_huks_generatekeyitem)生成密钥。[struct OH_Huks_Result OH_Huks_ImportKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *key)](#ZH-CN_TOPIC_0000002497605400__oh_huks_importkeyitem)导入明文密钥。[struct OH_Huks_Result OH_Huks_ImportWrappedKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_Blob *wrappingKeyAlias, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *wrappedKeyData)](#ZH-CN_TOPIC_0000002497605400__oh_huks_importwrappedkeyitem)导入密文密钥。[struct OH_Huks_Result OH_Huks_ExportPublicKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *key)](#ZH-CN_TOPIC_0000002497605400__oh_huks_exportpublickeyitem)导出公钥。[struct OH_Huks_Result OH_Huks_DeleteKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet)](#ZH-CN_TOPIC_0000002497605400__oh_huks_deletekeyitem)删除密钥。[struct OH_Huks_Result OH_Huks_GetKeyItemParamSet(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSetIn, struct OH_Huks_ParamSet *paramSetOut)](#ZH-CN_TOPIC_0000002497605400__oh_huks_getkeyitemparamset)获取密钥的属性集。[struct OH_Huks_Result OH_Huks_IsKeyItemExist(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet)](#ZH-CN_TOPIC_0000002497605400__oh_huks_iskeyitemexist)判断密钥是否存在。[struct OH_Huks_Result OH_Huks_AttestKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_CertChain *certChain)](#ZH-CN_TOPIC_0000002497605400__oh_huks_attestkeyitem)获取密钥证书链。该API仅面向系统应用开放。[struct OH_Huks_Result OH_Huks_AnonAttestKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_CertChain *certChain)](#ZH-CN_TOPIC_0000002497605400__oh_huks_anonattestkeyitem)

获取密钥证书链。

 这是一个涉及网络的耗时接口，调用方可以通过异步线程获取证书链。

[struct OH_Huks_Result OH_Huks_InitSession(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *handle, struct OH_Huks_Blob *token)](#ZH-CN_TOPIC_0000002497605400__oh_huks_initsession)初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选）。[struct OH_Huks_Result OH_Huks_UpdateSession(const struct OH_Huks_Blob *handle, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *outData)](#ZH-CN_TOPIC_0000002497605400__oh_huks_updatesession)分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据。[struct OH_Huks_Result OH_Huks_FinishSession(const struct OH_Huks_Blob *handle, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *outData)](#ZH-CN_TOPIC_0000002497605400__oh_huks_finishsession)结束密钥会话并进行相应的密钥操作，输出处理数据。[struct OH_Huks_Result OH_Huks_AbortSession(const struct OH_Huks_Blob *handle, const struct OH_Huks_ParamSet *paramSet)](#ZH-CN_TOPIC_0000002497605400__oh_huks_abortsession)取消密钥会话。[struct OH_Huks_Result OH_Huks_ListAliases(const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_KeyAliasSet **outData)](#ZH-CN_TOPIC_0000002497605400__oh_huks_listaliases)获取密钥别名集。[struct OH_Huks_Result OH_Huks_WrapKey(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *wrappedKey)](#ZH-CN_TOPIC_0000002497605400__oh_huks_wrapkey)导出由特定密钥加密的封装密钥。[struct OH_Huks_Result OH_Huks_UnwrapKey(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *wrappedKey)](#ZH-CN_TOPIC_0000002497605400__oh_huks_unwrapkey)导入由特定密钥加密的封装密钥。

#### 函数说明

#### OH_Huks_GetSdkVersion()

```ets
struct OH_Huks_Result OH_Huks_GetSdkVersion(struct OH_Huks_Blob *sdkVersion)
```

**描述**

获取当前Huks sdk版本号。

**起始版本：** 9

**参数：**

参数项描述[struct OH_Huks_Blob](OH_Huks_Blob.md) *sdkVersion用于存放获取到的版本信息（字符串格式）。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：sdkVersion或者sdkVersion->data是null，或者sdkVersion->size太小。

#### OH_Huks_GenerateKeyItem()

```ets
struct OH_Huks_Result OH_Huks_GenerateKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSetIn, struct OH_Huks_ParamSet *paramSetOut)
```

**描述**

生成密钥。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias给要生成的密钥的别名，需要保证业务所在进程内唯一，否则会发生覆盖。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSetIn生成密钥的属性信息的参数集。[struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSetOut生成密钥为临时类型时，存放着密钥数据；非临时类型可为空。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数keyAlias、paramSetIn、paramSetOut有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_FILE_OPERATION_FAIL = 12000004 ：删除或者写文件失败。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：基础密钥文件不存在。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL = 12000006 ：加密引擎失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_CALL_SERVICE_FAILED = 12000015 ：连接用户IAM失败。

 OH_HUKS_ERR_CODE_DEVICE_PASSWORD_UNSET = 12000016 ：需要设备密码但没有设置。

 OH_HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED = 12000001 ：暂不支持该功能。

 OH_HUKS_ERR_CODE_KEY_ALREADY_EXIST = 12000017（API 20新增）: 同名密钥已存在。

#### OH_Huks_ImportKeyItem()

```ets
struct OH_Huks_Result OH_Huks_ImportKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *key)
```

**描述**

导入明文密钥。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias待导入密钥的别名，需要保证业务所在进程内唯一，否则会发生覆盖。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet待导入密钥的属性参数。[const struct OH_Huks_Blob](OH_Huks_Blob.md) *key待导入密钥数据，需符合Huks的格式要求，具体见[native_huks_type.h](native_huks_type.h.md)。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数keyAlias、paramSet、key有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_FILE_OPERATION_FAIL = 12000004 ：删除或者写文件失败。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_CALL_SERVICE_FAILED = 12000015 ：连接用户IAM失败。

 OH_HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED = 12000001 ：暂不支持该功能。

 OH_HUKS_ERR_CODE_KEY_ALREADY_EXIST = 12000017（API 20新增）: 同名密钥已存在。

#### OH_Huks_ImportWrappedKeyItem()

```ets
struct OH_Huks_Result OH_Huks_ImportWrappedKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_Blob *wrappingKeyAlias, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *wrappedKeyData)
```

**描述**

导入密文密钥。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias待导入密钥的别名，需要保证业务所在进程内唯一，否则会发生覆盖。[const struct OH_Huks_Blob](OH_Huks_Blob.md) *wrappingKeyAlias密钥别名，该对应密钥用于密钥协商出密钥解密待导入密钥。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet待导入加密密钥的属性参数。[const struct OH_Huks_Blob](OH_Huks_Blob.md) *wrappedKeyData需要导入的加密的密钥数据，需要符合Huks定义的格式，具体见[OH_Huks_AlgSuite](native_huks_type.h.md#ZH-CN_TOPIC_0000002529285393__oh_huks_algsuite)。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数keyAlias、wrappingKeyAlias、paramSet、wrappedKeyData有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_FILE_OPERATION_FAIL = 12000004 ：删除或者写文件失败。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL = 12000006 ：加密引擎失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_CALL_SERVICE_FAILED = 12000015 ：连接用户IAM失败。

 OH_HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED = 12000001 ：暂不支持该功能。

 OH_HUKS_ERR_CODE_KEY_ALREADY_EXIST = 12000017（API 20新增）: 同名密钥已存在。

#### OH_Huks_ExportPublicKeyItem()

```ets
struct OH_Huks_Result OH_Huks_ExportPublicKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *key)
```

**描述**

导出公钥。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias待导出公钥的密钥别名，应与所用密钥生成时使用的别名相同。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet导出公钥需要的属性参数。[struct OH_Huks_Blob](OH_Huks_Blob.md) *key存放导出的公钥。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数keyAlias、paramSet、key有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：密钥文件不存在。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED = 12000001 ：暂不支持该功能。

#### OH_Huks_DeleteKeyItem()

```ets
struct OH_Huks_Result OH_Huks_DeleteKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet)
```

**描述**

删除密钥。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias待删除密钥的别名，应与密钥生成时使用的别名相同。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet删除密钥需要属性参数（默认传空）。若不指定则默认要删除的密钥存储等级为[OH_HUKS_AUTH_STORAGE_LEVEL_CE](native_huks_type.h.md#ZH-CN_TOPIC_0000002529285393__oh_huks_authstoragelevel)。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数keyAlias、paramSet有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：密钥文件不存在。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

#### OH_Huks_GetKeyItemParamSet()

```ets
struct OH_Huks_Result OH_Huks_GetKeyItemParamSet(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSetIn, struct OH_Huks_ParamSet *paramSetOut)
```

**描述**

获取密钥的属性集。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias要获取参数集的密钥别名。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSetIn要获取参数集需要的属性TAG（默认传空）。[struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSetOut获取到的输出参数集。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数keyAlias、paramSetIn、paramSetOut有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：密钥文件不存在。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED = 12000001 ：暂不支持该功能。

#### OH_Huks_IsKeyItemExist()

```ets
struct OH_Huks_Result OH_Huks_IsKeyItemExist(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet)
```

**描述**

判断密钥是否存在。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias要查找的密钥的别名。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet查询密钥需要的属性TAG（默认传空）。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数keyAlias、paramSet有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：密钥文件不存在。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

#### OH_Huks_AttestKeyItem()

```ets
struct OH_Huks_Result OH_Huks_AttestKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_CertChain *certChain)
```

**描述**

获取密钥证书链。该API仅面向系统应用开放。

**需要权限：** ohos.permission.ATTEST_KEY，该权限仅系统应用可申请。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias要获取证书的密钥的别名。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet获取密钥证书需要的参数。[struct OH_Huks_CertChain](OH_Huks_CertChain.md) *certChain存放输出的密钥证书链。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数keyAlias、paramSet、certChain有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：密钥文件不存在。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL = 12000006 ：加密引擎失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED = 12000001 ：暂不支持该功能。

 OH_HUKS_ERR_CODE_PERMISSION_FAIL = 201 ：权限检查失败，请先申请请求权限。

#### OH_Huks_AnonAttestKeyItem()

```ets
struct OH_Huks_Result OH_Huks_AnonAttestKeyItem(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_CertChain *certChain)
```

**描述**

获取密钥证书链。

 这是一个涉及网络的耗时接口，调用方可以通过异步线程获取证书链。

**起始版本：** 11

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias要获取证书的密钥的别名。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet获取密钥证书需要的参数。[struct OH_Huks_CertChain](OH_Huks_CertChain.md) *certChain存放输出的密钥证书链。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数keyAlias、paramSet、certChain有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：密钥文件不存在。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL = 12000006 ：加密引擎失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED = 12000001 ：暂不支持该功能。

 OH_HUKS_ERR_CODE_PERMISSION_FAIL = 201 ：权限检查失败，请先申请请求权限。

#### OH_Huks_InitSession()

```ets
struct OH_Huks_Result OH_Huks_InitSession(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *handle, struct OH_Huks_Blob *token)
```

**描述**

初始化密钥会话接口，并获取一个句柄（必选）和挑战值（可选）。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias操作的密钥的别名。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet初始化操作的密钥参数集合。[struct OH_Huks_Blob](OH_Huks_Blob.md) *handle密钥会话的句柄，后续其他操作时传入该句柄，包括[OH_Huks_UpdateSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_updatesession)，[OH_Huks_FinishSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_finishsession)，[OH_Huks_AbortSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_abortsession)。[struct OH_Huks_Blob](zh-cn_topic_0000002529445369.html) *token存放安全访问控制时传回的token。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数 keyAlias、paramSet、handle、token有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：密钥文件不存在。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_SESSION_LIMIT = 12000010 ：已达最大会话限制。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL = 12000006 ：加密引擎失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED = 12000001 ：暂不支持该功能。

 OH_HUKS_ERR_CODE_INVALID_ARGUMENT = 12000018：（API 22新增）参数集不合法。

**参考：**

[OH_Huks_UpdateSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_updatesession)

[OH_Huks_FinishSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_finishsession)

[OH_Huks_AbortSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_abortsession)

#### OH_Huks_UpdateSession()

```ets
struct OH_Huks_Result OH_Huks_UpdateSession(const struct OH_Huks_Blob *handle, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *outData)
```

**描述**

分段添加密钥操作的数据并进行相应的密钥操作，输出处理数据。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *handle密钥会话句柄，通过[OH_Huks_InitSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_initsession)接口生成。[const struct OH_Huks_ParamSet](zh-cn_topic_0000002497445426.html) *paramSet密钥操作对应的输入参数集。[const struct OH_Huks_Blob](OH_Huks_Blob.md) *inData要处理的输入数据，如果数据过大，可分片多次调用。[struct OH_Huks_Blob](OH_Huks_Blob.md) *outData经过对应的密钥操作后输出的数据。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数handle、paramSet、inData、outData有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：密钥文件不存在，或handle不存在。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_CREDENTIAL_NOT_EXIST = 12000013 ：证书不存在。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL = 12000006 ：加密引擎失败。

 OH_HUKS_ERR_CODE_KEY_AUTH_VERIFY_FAILED = 12000008 ：认证令牌校验失败。

 OH_HUKS_ERR_CODE_KEY_AUTH_PERMANENTLY_INVALIDATED = 12000007 ：认证令牌信息校验失败。

 OH_HUKS_ERR_CODE_KEY_AUTH_TIME_OUT = 12000009 ：认证令牌超时。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_DEVICE_PASSWORD_UNSET = 12000016 ：需要设备密码但没有设置。

 OH_HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED = 12000001 ：暂不支持该功能。

**参考：**

[OH_Huks_InitSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_initsession)

[OH_Huks_FinishSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_finishsession)

[OH_Huks_AbortSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_abortsession)

#### OH_Huks_FinishSession()

```ets
struct OH_Huks_Result OH_Huks_FinishSession(const struct OH_Huks_Blob *handle, const struct OH_Huks_ParamSet *paramSet, const struct OH_Huks_Blob *inData, struct OH_Huks_Blob *outData)
```

**描述**

结束密钥会话并进行相应的密钥操作，输出处理数据。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *handle密钥会话句柄，通过[OH_Huks_InitSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_initsession)接口生成。[const struct OH_Huks_ParamSet](zh-cn_topic_0000002497445426.html) *paramSet密钥操作对应的输入参数集。[const struct OH_Huks_Blob](OH_Huks_Blob.md) *inData要处理的输入数据。[struct OH_Huks_Blob](OH_Huks_Blob.md) *outData经过对应的密钥操作后输出的数据。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数handle、paramSet、inData、outData有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：密钥文件不存在，或handle不存在。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_CREDENTIAL_NOT_EXIST = 12000013 ：证书不存在。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL = 12000006 ：加密引擎失败。

 OH_HUKS_ERR_CODE_KEY_AUTH_VERIFY_FAILED = 12000008 ：认证令牌校验失败。

 OH_HUKS_ERR_CODE_KEY_AUTH_PERMANENTLY_INVALIDATED = 12000007 ：认证令牌信息校验失败。

 OH_HUKS_ERR_CODE_KEY_AUTH_TIME_OUT = 12000009 ：认证令牌超时。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_DEVICE_PASSWORD_UNSET = 12000016 ：需要设备密码但没有设置。

 OH_HUKS_ERR_CODE_FEATURE_NOT_SUPPORTED = 12000001 ：暂不支持该功能。

 OH_HUKS_ERR_CODE_KEY_ALREADY_EXIST = 12000017（API 20新增）: 同名密钥已存在。

**参考：**

[OH_Huks_InitSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_initsession)

[OH_Huks_UpdateSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_updatesession)

[OH_Huks_AbortSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_abortsession)

#### OH_Huks_AbortSession()

```ets
struct OH_Huks_Result OH_Huks_AbortSession(const struct OH_Huks_Blob *handle, const struct OH_Huks_ParamSet *paramSet)
```

**描述**

取消密钥会话。

**起始版本：** 9

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *handle密钥会话句柄，通过[OH_Huks_InitSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_initsession)接口生成。[const struct OH_Huks_ParamSet](zh-cn_topic_0000002497445426.html) *paramSet取消密钥会话需要的输入参数集（默认传空）。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数handle、paramSet、inData、outData有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INVALID_CRYPTO_ALG_ARGUMENT = 12000003 ：密钥参数无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST = 12000011 ：密钥文件不存在，或handle不存在。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT = 12000002 ：获取密钥参数失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_CREDENTIAL_NOT_EXIST = 12000013 ：证书不存在。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

**参考：**

[OH_Huks_InitSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_initsession)

[OH_Huks_UpdateSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_updatesession)

[OH_Huks_FinishSession](#ZH-CN_TOPIC_0000002497605400__oh_huks_finishsession)

#### OH_Huks_ListAliases()

```ets
struct OH_Huks_Result OH_Huks_ListAliases(const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_KeyAliasSet **outData)
```

**描述**

获取密钥别名集。

**起始版本：** 20

**参数：**

参数项描述[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet获取密钥别名集需要的输入参数集（默认传空）。[struct OH_Huks_KeyAliasSet](OH_Huks_KeyAliasSet.md) **outData经过对应的密钥操作后输出的数据。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT = 401 ：参数paramSet、outData有一个无效。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

#### OH_Huks_WrapKey()

```ets
struct OH_Huks_Result OH_Huks_WrapKey(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *wrappedKey)
```

**描述**

导出由特定密钥加密的封装密钥。

**起始版本：** 20

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias表示要导出的密钥别名。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet表示加密导出密钥的参数集。[struct OH_Huks_Blob](OH_Huks_Blob.md) *wrappedKey表示要导出的封装好的密钥。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_NOT_SUPPORTED_API = 801 ：接口不支持。

 OH_HUKS_ERR_CODE_FILE_OPERATION_FAIL = 12000004 ：删除或者写文件失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL = 12000011 ：密钥文件不存在。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_INVALID_ARGUMENT = 12000018 ：密钥别名、参数集或者封装密钥不合法。

#### OH_Huks_UnwrapKey()

```ets
struct OH_Huks_Result OH_Huks_UnwrapKey(const struct OH_Huks_Blob *keyAlias, const struct OH_Huks_ParamSet *paramSet, struct OH_Huks_Blob *wrappedKey)
```

**描述**

导入由特定密钥加密的封装密钥。

**起始版本：** 20

**参数：**

参数项描述[const struct OH_Huks_Blob](OH_Huks_Blob.md) *keyAlias表示要导入的密钥别名。在服务进程中，别名必须唯一。否则，密钥将被覆盖。[const struct OH_Huks_ParamSet](OH_Huks_ParamSet.md) *paramSet表示加密导入密钥的参数集。[struct OH_Huks_Blob](OH_Huks_Blob.md) *wrappedKey表示要导入的封装好的密钥。

**返回：**

类型说明[struct OH_Huks_Result](OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS = 0 ：操作成功。

 OH_HUKS_ERR_CODE_NOT_SUPPORTED_API = 801 ：接口不支持。

 OH_HUKS_ERR_CODE_FILE_OPERATION_FAIL = 12000004 ：删除或者写文件失败。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL = 12000005 ：IPC通信失败。

 OH_HUKS_ERR_CODE_INTERNAL_ERROR = 12000012 ：发生系统错误。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY = 12000014 ：内存不足。

 OH_HUKS_ERR_CODE_CALL_SERVICE_FAILED = 12000015 ：连接用户IAM失败。

 OH_HUKS_ERR_CODE_INVALID_ARGUMENT = 12000018 ：密钥别名、参数集或者封装密钥不合法。