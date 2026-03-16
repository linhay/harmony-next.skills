# native_huks_external_crypto_api.h

#### 概述

定义面向外部密钥管理扩展的通用密钥库（HUKS）API。

**引用文件：** <huks/native_huks_external_crypto_api.h>

**库：** libhuks_external_crypto.z.so

**系统能力：** SystemCapability.Security.Huks.CryptoExtension

**起始版本：** 22

**相关模块：**[HuksExternalCryptoApi](../../topics/networking/HuksExternalCryptoApi.md)

#### 汇总

#### 函数

名称描述[struct OH_Huks_Result OH_Huks_RegisterProvider(const struct OH_Huks_Blob *providerName, const OH_Huks_ExternalCryptoParamSet *paramSet)](#ZH-CN_TOPIC_0000002529285391__oh_huks_registerprovider)注册外部密钥管理能力扩展提供者。[struct OH_Huks_Result OH_Huks_UnregisterProvider(const struct OH_Huks_Blob *providerName, const OH_Huks_ExternalCryptoParamSet *paramSet)](#ZH-CN_TOPIC_0000002529285391__oh_huks_unregisterprovider)注销外部密钥管理能力扩展提供者。[struct OH_Huks_Result OH_Huks_OpenResource(const struct OH_Huks_Blob *resourceId, const OH_Huks_ExternalCryptoParamSet *paramSet)](#ZH-CN_TOPIC_0000002529285391__oh_huks_openresource)

根据指定的资源ID打开资源。

 注意：打开的资源必须通过[OH_Huks_CloseResource](#ZH-CN_TOPIC_0000002529285391__oh_huks_closeresource)关闭。

[struct OH_Huks_Result OH_Huks_CloseResource(const struct OH_Huks_Blob *resourceId, const OH_Huks_ExternalCryptoParamSet *paramSet)](#ZH-CN_TOPIC_0000002529285391__oh_huks_closeresource)根据指定的资源ID关闭资源。[struct OH_Huks_Result OH_Huks_GetUkeyPinAuthState(const struct OH_Huks_Blob *resourceId, const OH_Huks_ExternalCryptoParamSet *paramSet, OH_Huks_ExternalPinAuthState *authState)](#ZH-CN_TOPIC_0000002529285391__oh_huks_getukeypinauthstate)获取指定Ukey资源ID的PIN授权状态。[struct OH_Huks_Result OH_Huks_GetProperty(const struct OH_Huks_Blob *resourceId, const struct OH_Huks_Blob *propertyId, const OH_Huks_ExternalCryptoParamSet *paramSetIn, OH_Huks_ExternalCryptoParamSet **paramSetOut)](#ZH-CN_TOPIC_0000002529285391__oh_huks_getproperty)外部密钥管理能力扩展提供者获取属性信息。[struct OH_Huks_Result OH_Huks_InitExternalCryptoParamSet(OH_Huks_ExternalCryptoParamSet **paramSet)](#ZH-CN_TOPIC_0000002529285391__oh_huks_initexternalcryptoparamset)初始化一个参数集合。[struct OH_Huks_Result OH_Huks_AddExternalCryptoParams(OH_Huks_ExternalCryptoParamSet *paramSet, const OH_Huks_ExternalCryptoParam *params, uint32_t paramCnt)](#ZH-CN_TOPIC_0000002529285391__oh_huks_addexternalcryptoparams)向参数集合中添加参数。[struct OH_Huks_Result OH_Huks_BuildExternalCryptoParamSet(OH_Huks_ExternalCryptoParamSet **paramSet)](#ZH-CN_TOPIC_0000002529285391__oh_huks_buildexternalcryptoparamset)构建一个参数集合。[void OH_Huks_FreeExternalCryptoParamSet(OH_Huks_ExternalCryptoParamSet **paramSet)](#ZH-CN_TOPIC_0000002529285391__oh_huks_freeexternalcryptoparamset)销毁一个参数集合并释放相关内存。[struct OH_Huks_Result OH_Huks_GetExternalCryptoParam(OH_Huks_ExternalCryptoParamSet *paramSet, const uint32_t tag, OH_Huks_ExternalCryptoParam **param)](#ZH-CN_TOPIC_0000002529285391__oh_huks_getexternalcryptoparam)从参数集合中获取指定参数。

#### 函数说明

#### OH_Huks_RegisterProvider()

```ets
struct OH_Huks_Result OH_Huks_RegisterProvider(const struct OH_Huks_Blob *providerName, const OH_Huks_ExternalCryptoParamSet *paramSet)
```

**描述**

注册外部密钥管理能力扩展提供者。

**需要权限：** ohos.permission.CRYPTO_EXTENSION_REGISTER

**起始版本：** 22

**参数：**

参数项描述[const struct OH_Huks_Blob](../../topics/misc/OH_Huks_Blob.md) *providerName指定提供者名称。[const OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) *paramSet指向注册参数的指针。

**返回：**

类型说明[struct OH_Huks_Result](../../topics/misc/OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS 0 - 操作成功。

 OH_HUKS_ERR_CODE_PERMISSION_FAIL 201 - 权限校验失败，请先申请所需权限。

 OH_HUKS_ERR_CODE_NOT_SUPPORTED_API 801 - 不支持的API。

 OH_HUKS_ERR_CODE_MISSING_CRYPTO_ALG_ARGUMENT 12000002 - 未能获取提供者参数。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL 12000005 - IPC通信失败。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY 12000014 - 内存不足。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT 12000018 - providerName或paramSet无效。

 OH_HUKS_ERR_CODE_ITEM_NOT_EXIST 12000019 - 提供者已被注册。

 OH_HUKS_ERR_CODE_EXTERNAL_ERROR 12000020 - 依赖模块发生错误。

 OH_HUKS_ERR_CODE_EXCEED_LIMIT 12000025 - 提供者数量超过限制。

#### OH_Huks_UnregisterProvider()

```ets
struct OH_Huks_Result OH_Huks_UnregisterProvider(const struct OH_Huks_Blob *providerName, const OH_Huks_ExternalCryptoParamSet *paramSet)
```

**描述**

注销外部密钥管理能力扩展提供者。

**需要权限：** ohos.permission.CRYPTO_EXTENSION_REGISTER

**起始版本：** 22

**参数：**

参数项描述[const struct OH_Huks_Blob](../../topics/misc/OH_Huks_Blob.md) *providerName指定提供者名称。[const OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) *paramSet指向注册参数的指针。

**返回：**

类型说明[struct OH_Huks_Result](../../topics/misc/OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS 0 - 操作成功。

 OH_HUKS_ERR_CODE_PERMISSION_FAIL 201 - 权限校验失败，请先申请所需权限。

 OH_HUKS_ERR_CODE_NOT_SUPPORTED_API 801 - 不支持的API。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL 12000005 - IPC通信失败。

 HUKS_ERR_CODE_ITEM_NOT_EXIST 12000011 - 未找到指定的提供者。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY 12000014 - 内存不足。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT 12000018 - providerName无效。

 OH_HUKS_ERR_CODE_EXTERNAL_ERROR 12000020 - 依赖模块发生错误。

#### OH_Huks_OpenResource()

```ets
struct OH_Huks_Result OH_Huks_OpenResource(const struct OH_Huks_Blob *resourceId, const OH_Huks_ExternalCryptoParamSet *paramSet)
```

**描述**

根据指定的资源ID打开资源。

 注意：打开的资源必须通过[OH_Huks_CloseResource](#ZH-CN_TOPIC_0000002529285391__oh_huks_closeresource)关闭。

**起始版本：** 22

**参数：**

参数项描述[const struct OH_Huks_Blob](../../topics/misc/OH_Huks_Blob.md) *resourceId指定提供者的资源ID。[const OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) *paramSet指向句柄操作参数的指针。

**返回：**

类型说明[struct OH_Huks_Result](../../topics/misc/OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS 0 - 操作成功。

 OH_HUKS_ERR_CODE_NOT_SUPPORTED_API 801 - 不支持的API。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL 12000005 - IPC通信失败。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL 12000006 - Ukey驱动报错。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY 12000014 - 内存不足。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT 12000018 - resourceId或paramSet无效。

 OH_HUKS_ERR_CODE_EXTERNAL_ERROR 12000020 - 提供者执行失败。

 OH_HUKS_ERR_CODE_PIN_LOCKED 12000021 - PIN码被锁定。

 OH_HUKS_ERR_CODE_BUSY 12000024 - 提供者或Ukey忙。

 OH_HUKS_ERR_CODE_EXCEED_LIMIT 12000025 - 打开资源的数量超过限制。

#### OH_Huks_CloseResource()

```ets
struct OH_Huks_Result OH_Huks_CloseResource(const struct OH_Huks_Blob *resourceId, const OH_Huks_ExternalCryptoParamSet *paramSet)
```

**描述**

根据指定的资源ID关闭资源。

**起始版本：** 22

**参数：**

参数项描述[const struct OH_Huks_Blob](../../topics/misc/OH_Huks_Blob.md) *resourceId指定提供者的资源ID。[const OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) *paramSet指向句柄操作参数的指针。

**返回：**

类型说明[struct OH_Huks_Result](../../topics/misc/OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS 0 - 操作成功。

 OH_HUKS_ERR_CODE_NOT_SUPPORTED_API 801 - 不支持的 API。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL 12000005 - IPC通信失败。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL 12000006 - Ukey驱动报错。

 HUKS_ERR_CODE_ITEM_NOT_EXIST 12000011 - 未找到缓存的指定句柄。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY 12000014 - 内存不足。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT 12000018 - resourceId或paramSet无效。

 OH_HUKS_ERR_CODE_EXTERNAL_ERROR 12000020 - 提供者执行失败。

 OH_HUKS_ERR_CODE_PIN_LOCKED 12000021 - PIN码被锁定。

 OH_HUKS_ERR_CODE_BUSY 12000024 - 提供者或Ukey忙。

#### OH_Huks_GetUkeyPinAuthState()

```ets
struct OH_Huks_Result OH_Huks_GetUkeyPinAuthState(const struct OH_Huks_Blob *resourceId, const OH_Huks_ExternalCryptoParamSet *paramSet, OH_Huks_ExternalPinAuthState *authState)
```

**描述**

获取指定Ukey资源ID的PIN授权状态。

**起始版本：** 22

**参数：**

参数项描述[const struct OH_Huks_Blob](../../topics/misc/OH_Huks_Blob.md) *resourceId指定提供者的资源ID。[const OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) *paramSet指向PIN授权参数的指针。bool *authState用于返回指定索引的授权状态。

**返回：**

类型说明[struct OH_Huks_Result](../../topics/misc/OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS 0 - 操作成功。

 OH_HUKS_ERR_CODE_NOT_SUPPORTED_API 801 - 不支持的API。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL 12000005 - IPC通信失败。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL 12000006 - Ukey驱动报错。

 HUKS_ERR_CODE_ITEM_NOT_EXIST 12000011 - 未找到缓存的指定句柄。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY 12000014 - 内存不足。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT 12000018 - resourceId或paramSet无效。

 OH_HUKS_ERR_CODE_EXTERNAL_ERROR 12000020 - 提供者执行失败。

 OH_HUKS_ERR_CODE_BUSY 12000024 - 提供者或Ukey忙。

#### OH_Huks_GetProperty()

```ets
struct OH_Huks_Result OH_Huks_GetProperty(const struct OH_Huks_Blob *resourceId, const struct OH_Huks_Blob *propertyId, const OH_Huks_ExternalCryptoParamSet *paramSetIn, OH_Huks_ExternalCryptoParamSet **paramSetOut)
```

**描述**

外部密钥管理能力扩展提供者获取属性信息。

**起始版本：** 22

**参数：**

参数项描述[const struct OH_Huks_Blob](../../topics/misc/OH_Huks_Blob.md) *resourceId指定提供者的资源ID。[const struct OH_Huks_Blob](../../topics/misc/OH_Huks_Blob.md) *propertyId指定按GMT 0016-2023定义的属性函数名称。[const OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) *paramSetIn指向输入操作参数的指针。[OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) **paramSetOut指向输出参数的指针，且必须包含参数OH_HUKS_EXT_CRYPTO_TAG_EXTRA_DATA。

**返回：**

类型说明[struct OH_Huks_Result](../../topics/misc/OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS 0 - 操作成功。

 OH_HUKS_ERR_CODE_NOT_SUPPORTED_API 801 - 不支持的API。

 OH_HUKS_ERR_CODE_COMMUNICATION_FAIL 12000005 - IPC通信失败。

 OH_HUKS_ERR_CODE_CRYPTO_FAIL 12000006 - 驱动错误。

 HUKS_ERR_CODE_ITEM_NOT_EXIST 12000011 - 未找到缓存的指定句柄。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY 12000014 - 内存不足。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT 12000018 - resourceId、propertyId、paramSet或回调无效。

 OH_HUKS_ERR_CODE_EXTERNAL_ERROR 12000020 - 提供者或Ukey内部执行失败。

 OH_HUKS_ERR_CODE_PIN_LOCKED 12000021 - PIN码被锁定。

 OH_HUKS_ERR_CODE_PIN_NO_AUTH 12000023 - PIN码未通过认证。

 OH_HUKS_ERR_CODE_BUSY 12000024 - 提供者或Ukey中的资源正在被使用。

#### OH_Huks_InitExternalCryptoParamSet()

```ets
struct OH_Huks_Result OH_Huks_InitExternalCryptoParamSet(OH_Huks_ExternalCryptoParamSet **paramSet)
```

**描述**

初始化一个参数集合。

**起始版本：** 22

**参数：**

参数项描述[OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) **paramSet指向要初始化的参数集合的二级指针。

**返回：**

类型说明[struct OH_Huks_Result](../../topics/misc/OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS 0 - 操作成功。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY 12000014 - 内存不足。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT 401 - params为NULL或paramSet无效。

#### OH_Huks_AddExternalCryptoParams()

```ets
struct OH_Huks_Result OH_Huks_AddExternalCryptoParams(OH_Huks_ExternalCryptoParamSet *paramSet, const OH_Huks_ExternalCryptoParam *params, uint32_t paramCnt)
```

**描述**

向参数集合中添加参数。

**起始版本：** 22

**参数：**

参数项描述[OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) *paramSet指向将要添加参数的参数集合。[const OH_Huks_ExternalCryptoParam](../../topics/media/OH_Huks_ExternalCryptoParam.md) *params指向要添加的参数数组。uint32_t paramCnt要添加的参数数量。

**返回：**

类型说明[struct OH_Huks_Result](../../topics/misc/OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS 0 - 操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT 401 - params为NULL或paramSet无效。

#### OH_Huks_BuildExternalCryptoParamSet()

```ets
struct OH_Huks_Result OH_Huks_BuildExternalCryptoParamSet(OH_Huks_ExternalCryptoParamSet **paramSet)
```

**描述**

构建一个参数集合。

**起始版本：** 22

**参数：**

参数项描述[OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) **paramSet指向要构建的参数集合的二级指针。

**返回：**

类型说明[struct OH_Huks_Result](../../topics/misc/OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS 0 - 操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT 401 - paramSet无效。

 OH_HUKS_ERR_CODE_INSUFFICIENT_MEMORY 12000014 - 内存不足。

#### OH_Huks_FreeExternalCryptoParamSet()

```ets
void OH_Huks_FreeExternalCryptoParamSet(OH_Huks_ExternalCryptoParamSet **paramSet)
```

**描述**

销毁一个参数集合并释放相关内存。

**起始版本：** 22

**参数：**

参数项描述[OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) **paramSet指向要销毁的参数集合的二级指针。

#### OH_Huks_GetExternalCryptoParam()

```ets
struct OH_Huks_Result OH_Huks_GetExternalCryptoParam(OH_Huks_ExternalCryptoParamSet *paramSet, const uint32_t tag, OH_Huks_ExternalCryptoParam **param)
```

**描述**

从参数集合中获取指定参数。

**起始版本：** 22

**参数：**

参数项描述[OH_Huks_ExternalCryptoParamSet](../../topics/media/OH_Huks_ExternalCryptoParamSet.md) *paramSet指向目标参数集合的指针。const uint32_t tag指定要获取的参数标签值。[OH_Huks_ExternalCryptoParam](../../topics/media/OH_Huks_ExternalCryptoParam.md) **param用于返回获取到的参数的二级指针。

**返回：**

类型说明[struct OH_Huks_Result](../../topics/misc/OH_Huks_Result.md)

可能的返回码（errorCode）：

 OH_HUKS_SUCCESS 0 - 操作成功。

 OH_HUKS_ERR_CODE_ILLEGAL_ARGUMENT 401 - paramSet或param无效，或参数在集合中不存在。