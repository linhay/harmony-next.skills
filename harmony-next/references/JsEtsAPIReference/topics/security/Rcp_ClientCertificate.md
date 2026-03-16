# Rcp_ClientCertificate

#### 概述

发送到远程服务器的客户端证书，远程服务器将使用它来验证客户端的标识。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](../misc/RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

char * [content](Rcp_ClientCertificate.md#ZH-CN_TOPIC_0000002282549672__aa6630a26570a25349dab3e9280f782b9)

客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。

char * [filePath](Rcp_ClientCertificate.md#ZH-CN_TOPIC_0000002282549672__a8d7f4b03387823946edd84952772998b)

客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。

char * [key](Rcp_ClientCertificate.md#ZH-CN_TOPIC_0000002282549672__ac6d5c955c1cfeefc9a70cf45131ad25f)

客户端证书私钥的文件名。

char * [keyPassword](Rcp_ClientCertificate.md#ZH-CN_TOPIC_0000002282549672__a05de541cd1c59f9f0bd1305ebc11a56a)

客户端证书私钥的密码。

[Rcp_CertType](../misc/RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f79c1d41b9c586d99f1c22ed81b9aee)[type](Rcp_ClientCertificate.md#ZH-CN_TOPIC_0000002282549672__a50eedad042bd9de8ef3c5dad02af78af)

客户端证书类型。

#### 结构体成员变量说明

#### content

```ets
char* Rcp_ClientCertificate::content
```

**描述**

客户端证书内容。它应采用“PEM”、“DER”或“P12”格式。

#### filePath

```ets
char* Rcp_ClientCertificate::filePath
```

**描述**

客户端证书的路径。文件的格式应为“PEM”、“DER”或“P12”格式。

#### key

```ets
char* Rcp_ClientCertificate::key
```

**描述**

客户端证书私钥的文件名。

#### keyPassword

```ets
char* Rcp_ClientCertificate::keyPassword
```

**描述**

客户端证书私钥的密码。

#### type

```ets
[Rcp_CertType](../misc/RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga4f79c1d41b9c586d99f1c22ed81b9aee) Rcp_ClientCertificate::type
```

**描述**

客户端证书类型。