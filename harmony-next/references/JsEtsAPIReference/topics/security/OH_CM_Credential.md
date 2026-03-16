# OH_CM_Credential

```ets
typedef struct {...} OH_CM_Credential
```

#### 概述

定义证书凭据详情的结构体类型。

**起始版本：** 22

**相关模块：**[CertManagerType](CertManagerType.md)

**所在头文件：**[cm_native_type.h](../../capi/headers/cm_native_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t isExist表示证书数据是否存在。char type[OH_CM_MAX_LEN_TYPE_NAME]表示凭据的类型，最大长度为8字节，数据包含终止符'\0'字符。char alias[OH_CM_MAX_LEN_CERT_ALIAS]表示凭据的别名，最大长度为128字节，数据包含终止符'\0'字符。char keyUri[OH_CM_MAX_LEN_URI]表示凭据的唯一标识，最大长度为256字节，数据包含终止符'\0'字符。uint32_t certNum表示凭据中包含的证书个数。uint32_t keyNum表示凭据中包含的秘钥个数。[OH_CM_Blob](../misc/OH_CM_Blob.md) credData表示凭据二进制数据，最大长度为20480字节。[OH_CM_CertificatePurpose](../../capi/headers/cm_native_type.h.md#ZH-CN_TOPIC_0000002529445353__oh_cm_certificatepurpose) certPurpose表示证书凭据的用途。