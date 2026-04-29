# OH_CM_CredentialDetailList

```ets
typedef struct {...} OH_CM_CredentialDetailList
```

**概述**

定义证书凭据详情列表的结构体类型。

起始版本： 22

相关模块： [CertManagerType](CertManagerType.md)

所在头文件： [cm_native_type.h](cm_native_type.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t credentialCount | 表示证书凭据详情的个数。 |
| OH_CM_Credential *credential | 表示证书凭据详情列表。 |