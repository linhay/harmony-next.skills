# FIDO2_AttestationFormatsArray

#### 概述

依赖方的数组可以使用此成员指定一个关于认证方使用的证明语句格式的首选项。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](../misc/通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [attestationFormatsNum](FIDO2_AttestationFormatsArray.md#ZH-CN_TOPIC_0000002523299535__a9a5c37c7c8d200a5172cea8211abf188)

PubKeyCredParam个数。

char ** [attestationFormats](FIDO2_AttestationFormatsArray.md#ZH-CN_TOPIC_0000002523299535__a892d146b5f52e312bafa619a6eb792fc)

认证凭据的附加参数列表。

#### 结构体成员变量说明

#### attestationFormats

```ets
char** FIDO2_AttestationFormatsArray::attestationFormats
```

**描述**

认证凭据的附加参数列表。

#### attestationFormatsNum

```ets
uint32_t FIDO2_AttestationFormatsArray::attestationFormatsNum
```

**描述**

认证凭据的附加参数列表长度。