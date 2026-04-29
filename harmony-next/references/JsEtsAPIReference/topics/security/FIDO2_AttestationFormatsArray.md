# FIDO2_AttestationFormatsArray

**概述**

依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。

起始版本： 6.0.0(20)

相关模块： [FIDO2](通行密钥.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| uint32_t attestationFormatsNum | PubKeyCredParam个数。 |
| char ** attestationFormats | 认证凭据的附加参数列表。 |

**结构体成员变量说明**

**attestationFormats**

```ets
char** FIDO2_AttestationFormatsArray::attestationFormats
```

描述

认证凭据的附加参数列表。

**attestationFormatsNum**

```ets
uint32_t FIDO2_AttestationFormatsArray::attestationFormatsNum
```

描述

认证凭据的附加参数列表长度。