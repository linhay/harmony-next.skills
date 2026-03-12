# FIDO2_AuthenticatorTransportArray

#### 概述

认证器传输方式数组。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [transportNum](FIDO2_AuthenticatorTransportArray.md#ZH-CN_TOPIC_0000002523139569__acd67a9c618c8f8c40d3cebcdc21922d1)

传输方式数量。

[FIDO2_AuthenticatorTransport](通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga02592e5b749c266e7297333afce03cec) * [transports](FIDO2_AuthenticatorTransportArray.md#ZH-CN_TOPIC_0000002523139569__aa3c4f2f321d482ae32dc3b795ecc2c65)

定义身份认证器访问类型（USB、NFC、蓝牙）。

#### 结构体成员变量说明

#### transportNum

```ets
uint32_t FIDO2_AuthenticatorTransportArray::transportNum
```

**描述**

传输方式数量。

#### transports

```ets
[FIDO2_AuthenticatorTransport](通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga02592e5b749c266e7297333afce03cec)* FIDO2_AuthenticatorTransportArray::transports
```

**描述**

定义身份认证器访问类型（USB、NFC、蓝牙）。