# cm_native_api.h

**概述**

声明用于获取特定类型证书详情的接口。

引用文件： <device_certificate/certmanager/cm_native_api.h>

库： libohcert_manager.so

系统能力： SystemCapability.Security.CertificateManager

起始版本： 22

相关模块： [CertManager](CertManager.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList) | 获取USB证书凭据的详情信息列表。 |
| int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate) | 获取特定应用私有证书凭据详细信息。 |
| int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate) | 获取特定用户公共证书凭据详细信息。 |
| void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList) | 销毁证书详情信息列表。 |
| void OH_CertManager_FreeCredential(OH_CM_Credential *certificate) | 销毁证书详情。 |

**函数说明**

**OH_CertManager_GetUkeyCertificate()**

```ets
int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)
```

描述

获取USB证书凭据的详情信息列表。

需要权限： ohos.permission.ACCESS_CERT_MANAGER

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_CM_Blob *keyUri | 存放USB证书凭据的唯一标识符（字符串格式）。 |
| const OH_CM_UkeyInfo *ukeyInfo | USB证书凭据属性信息。 |
| OH_CM_CredentialDetailList *certificateList | 获取到的USB证书凭据详情列表。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | OH_CM_ErrorCode：  OH_CM_SUCCESS = 0 ：操作成功。  OH_CM_HAS_NO_PERMISSION = 201 ：权限校验失败。  OH_CM_CAPABILITY_NOT_SUPPORTED = 801 ：设备不支持。  OH_CM_PARAMETER_VALIDATION_FAILED = 17500011 ：入参校验失败。可能原因：  1.参数格式错误。  2.参数范围无效。  OH_CM_INNER_FAILURE = 17500001 ：内部错误。可能原因：  1.IPC通讯失败。  2.内存操作错误。  3.文件操作错误。  OH_CM_NOT_FOUND = 17500002 ：证书不存在。  OH_CM_ACCESS_UKEY_SERVICE_FAILED = 17500010 ：USB证书凭据访问失败。 |

**OH_CertManager_GetPrivateCertificate()**

```ets
int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)
```

描述

获取特定应用私有证书凭据详细信息。

需要权限： ohos.permission.ACCESS_CERT_MANAGER

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_CM_Blob *keyUri | 存放应用私有证书凭据的唯一标识符（字符串格式）。 |
| OH_CM_Credential *certificate | 获取到的应用私有凭据的详情。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | OH_CM_ErrorCode：  OH_CM_SUCCESS = 0 ：操作成功。  OH_CM_HAS_NO_PERMISSION = 201 ：权限校验失败。  OH_CM_PARAMETER_VALIDATION_FAILED = 17500011 ：入参校验失败。可能原因：  1.参数格式错误。  2.参数范围无效。  OH_CM_INNER_FAILURE = 17500001 ：内部错误。可能原因：  1.IPC通讯失败。  2.内存操作错误。  3.文件操作错误。  OH_CM_NOT_FOUND = 17500002 ：证书不存在。 |

**OH_CertManager_GetPublicCertificate()**

```ets
int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)
```

描述

获取特定用户公共证书凭据详细信息。

需要权限： ohos.permission.ACCESS_CERT_MANAGER

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const OH_CM_Blob *keyUri | 存放用户公共证书凭据的唯一标识符（字符串格式）。 |
| OH_CM_Credential *certificate | 获取到的用户公共证书凭据的详情。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | OH_CM_ErrorCode：  OH_CM_SUCCESS = 0 ：操作成功。  OH_CM_HAS_NO_PERMISSION = 201 ：权限校验失败。  OH_CM_PARAMETER_VALIDATION_FAILED = 17500011 ：入参校验失败。可能原因：  1.参数格式错误。  2.参数范围无效。  OH_CM_INNER_FAILURE = 17500001 ：内部错误。可能原因：  1.IPC通讯失败。  2.内存操作错误。  3.文件操作错误。  OH_CM_NOT_FOUND = 17500002 ：证书不存在。  OH_CM_NO_AUTHORIZATION = 17500005 ：应用未经用户授权。 |

**OH_CertManager_FreeUkeyCertificate()**

```ets
void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList)
```

描述

销毁证书详情信息列表。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_CM_CredentialDetailList *certificateList | 待销毁的证书凭据详细列表。 |

**OH_CertManager_FreeCredential()**

```ets
void OH_CertManager_FreeCredential(OH_CM_Credential *certificate)
```

描述

销毁证书详情。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_CM_Credential *certificate | 待销毁的证书凭据详情。 |