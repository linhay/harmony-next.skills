# Rcp_ResponseCookies

#### 概述

响应Cookie。

**起始版本：** 5.0.0(12)

**相关模块：**[RemoteCommunication](RemoteCommunication.md)

#### 汇总

#### 成员变量

名称

描述

char * [name](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__a4fb5e327e05b807620387ee2500d314d)

响应Cookie名称。

char * [value](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__a7fb6c2177d99ffae4f13f411352196b2)

响应Cookie值。

char * [domain](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__a6f836af033fc293b012d49070c15dbd0)

响应Cookie域属性。

char * [path](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__a56c12937ae44e3ecb7d6c85e2d2ded03)

响应Cookie路径属性。

char * [expires](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__ac6870a218b3c8cf7f70d4666e1a9f9ad)

响应Cookie过期属性。

uint64_t [maxAge](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__aa3607ffbf45b1d9fb297d826df3b250a)

响应Cookie maxAge属性。

bool [secure](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__a81a2dd49c05c77313928d7843c49950b)

响应Cookie安全属性。

bool [httpOnly](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__a9b26fb82d3e441c63128bf1e88c6ce5c)

响应Cookie httpOnly属性。

char * [sameSite](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__ad4cb031c71dacc43b4deafbbe2c8e5ae)

响应Cookie sameSite属性。

uint64_t [rawSize](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__a395f93dbd2c0f272495ebcc2fb8aeae5)

此响应Cookie的原始大小。

char * [originString](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__a29a4b1bfb8eefa5accf5b2844524a80b)

原始字符串。

[Rcp_CookieAttributes](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga08c7b992199bec7e5acdc50ce8ae2651) * [cookieAttributes](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__a355c49aca4e4fe1bc799e83e115c60bf)

响应Cookie中的所有属性。

struct [Rcp_ResponseCookies](Rcp_ResponseCookies.md) * [next](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002282446466__aed191dfba2a7e291b08df92f48be033f)

链式存储。指向下一个[Rcp_ResponseCookies](Rcp_ResponseCookies.md)的指针。

#### 结构体成员变量说明

#### cookieAttributes

```ets
[Rcp_CookieAttributes](RemoteCommunication.md#ZH-CN_TOPIC_0000002282549700__ga08c7b992199bec7e5acdc50ce8ae2651)* Rcp_ResponseCookies::cookieAttributes
```

**描述**

响应Cookie中的所有属性。

#### domain

```ets
char* Rcp_ResponseCookies::domain
```

**描述**

响应Cookie域属性。

#### expires

```ets
char* Rcp_ResponseCookies::expires
```

**描述**

响应Cookie过期属性。

#### httpOnly

```ets
bool Rcp_ResponseCookies::httpOnly
```

**描述**

响应Cookie httpOnly属性。

#### maxAge

```ets
uint64_t Rcp_ResponseCookies::maxAge
```

**描述**

响应Cookie maxAge属性。

#### name

```ets
char* Rcp_ResponseCookies::name
```

**描述**

响应Cookie名称。

#### next

```ets
struct [Rcp_ResponseCookies](Rcp_ResponseCookies.md)* Rcp_ResponseCookies::next
```

**描述**

链式存储。指向下一个[Rcp_ResponseCookies](Rcp_ResponseCookies.md)的指针。

#### originString

```ets
char* Rcp_ResponseCookies::originString
```

**描述**

原始字符串。

#### path

```ets
char* Rcp_ResponseCookies::path
```

**描述**

响应Cookie路径属性。

#### rawSize

```ets
uint64_t Rcp_ResponseCookies::rawSize
```

**描述**

此响应Cookie的原始大小。

#### sameSite

```ets
char* Rcp_ResponseCookies::sameSite
```

**描述**

响应Cookie sameSite属性。

#### secure

```ets
bool Rcp_ResponseCookies::secure
```

**描述**

响应Cookie安全属性。

#### value

```ets
char* Rcp_ResponseCookies::value
```

**描述**

响应Cookie值。