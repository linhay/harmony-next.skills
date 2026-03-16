# AuthenticationExtensionsClientOutputs

#### 概述

身份认证扩展输出。

**起始版本：** 6.0.0(20)

**相关模块：**[FIDO2](../misc/通行密钥.md)

#### 汇总

#### 成员变量

名称

描述

char * [placeholder](AuthenticationExtensionsClientOutputs.md#ZH-CN_TOPIC_0000002490979816__af2d2d80788cd960be72bb9c17dde05a5)

占位符，表示返回的JSON消息中包含key clientExtensionResults。默认返回NULL。

#### 结构体成员变量说明

#### placeholder

```ets
char* AuthenticationExtensionsClientOutputs::placeholder
```

**描述**

占位符，表示返回的JSON消息中包含"clientExtensionResults"这个key值。总是返回NULL。