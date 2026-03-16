# FIDO2_TokenBinding

#### 概述

Token binding协议，用于客户端与依赖方通信。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](../misc/通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

[FIDO2_TokenBindingStatus](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga3a0c5c93081cd75c8ecd7a1efac8252e)[status](FIDO2_TokenBinding.md#ZH-CN_TOPIC_0000002523139575__a0e1fafe7c82fb1abd4fab1dcf6f047a0)

客户端的绑定状态。

char * [id](FIDO2_TokenBinding.md#ZH-CN_TOPIC_0000002523139575__a2991164fd206d98a42ce81e23040623f)

令牌绑定标识符。

#### 结构体成员变量说明

#### id

```ets
char* FIDO2_TokenBinding::id
```

**描述**

令牌绑定标识符。

#### status

```ets
[FIDO2_TokenBindingStatus](../misc/通行密钥.md#ZH-CN_TOPIC_0000002523299537__ga3a0c5c93081cd75c8ecd7a1efac8252e) FIDO2_TokenBinding::status
```

**描述**

客户端的绑定状态。