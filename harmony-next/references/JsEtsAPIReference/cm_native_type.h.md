# cm_native_type.h

#### 概述

提供CertManager中的枚举变量、结构体定义、宏定义和错误码。

**引用文件：** <device_certificate/certmanager/cm_native_type.h>

**库：** libohcert_manager.so

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 22

**相关模块：**[CertManagerType](CertManagerType.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_CM_Blob](OH_CM_Blob.md)OH_CM_Blob定义存放数据的结构体类型。[OH_CM_Credential](OH_CM_Credential.md)OH_CM_Credential定义证书凭据详情的结构体类型。[OH_CM_CredentialDetailList](OH_CM_CredentialDetailList.md)OH_CM_CredentialDetailList定义证书凭据详情列表的结构体类型。[OH_CM_UkeyInfo](OH_CM_UkeyInfo.md)OH_CM_UkeyInfo定义USB证书凭据信息的结构体类型。

#### 枚举

名称typedef关键字描述[OH_CM_ErrorCode](#ZH-CN_TOPIC_0000002529445353__oh_cm_errorcode)OH_CM_ErrorCode错误码。[OH_CM_CertificatePurpose](#ZH-CN_TOPIC_0000002529445353__oh_cm_certificatepurpose)OH_CM_CertificatePurpose证书凭据用途类型。

#### 宏定义

名称描述OH_CM_MAX_LEN_CERTIFICATE_CHAIN 24588

证书链最大长度。

**起始版本：** 22

OH_CM_MAX_LEN_URI 256

URI最大长度。

**起始版本：** 22

OH_CM_MAX_LEN_CERT_ALIAS 129

证书别名最大长度。

**起始版本：** 22

OH_CM_MAX_LEN_TYPE_NAME 1025

证书类型最大长度。

**起始版本：** 22

#### 枚举类型说明

#### OH_CM_ErrorCode

```ets
enum OH_CM_ErrorCode
```

**描述**

错误码。

**起始版本：** 22

枚举项描述OH_CM_SUCCESS = 0成功。OH_CM_HAS_NO_PERMISSION = 201权限校验失败。OH_CM_CAPABILITY_NOT_SUPPORTED = 801设备不支持。OH_CM_INNER_FAILURE = 17500001内部错误。可能原因：1.IPC通讯失败。2.内存操作错误；3.文件操作错误。OH_CM_NOT_FOUND = 17500002证书不存在。OH_CM_INVALID_CERT_FORMAT = 17500003密钥库格式无效或密钥库密码不正确。OH_CM_MAX_CERT_COUNT_REACHED = 17500004证书或凭据数量达到上限。OH_CM_NO_AUTHORIZATION = 17500005应用未经用户授权。OH_CM_DEVICE_ENTER_ADVSECMODE = 17500007设备进入坚盾守护模式。OH_CM_STORE_PATH_NOT_SUPPORTED = 17500009不支持指定的证书存储路径。OH_CM_ACCESS_UKEY_SERVICE_FAILED = 17500010USB证书凭据访问失败。OH_CM_PARAMETER_VALIDATION_FAILED = 17500011参数校验失败，例如参数格式或参数范围无效。

#### OH_CM_CertificatePurpose

```ets
enum OH_CM_CertificatePurpose
```

**描述**

证书凭据用途类型。

**起始版本：** 22

枚举项描述OH_CM_CERT_PURPOSE_DEFAULT = 0默认用途，用于凭据签名用途。OH_CM_CERT_PURPOSE_ALL = 1所有用途，用于查询凭据功能。OH_CM_CERT_PURPOSE_SIGN = 2签名用途。OH_CM_CERT_PURPOSE_ENCRYPT = 3加密用途。