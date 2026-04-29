# Rcp_ResponseCookies

**概述**

响应Cookie。

起始版本： 5.0.0(12)

相关模块： [RemoteCommunication](RemoteCommunication.md)

所在头文件： [rcp.h](rcp.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| char * name | 响应Cookie名称。 |
| char * value | 响应Cookie值。 |
| char * domain | 响应Cookie域属性。 |
| char * path | 响应Cookie路径属性。 |
| char * expires | 响应Cookie过期属性。 |
| uint64_t maxAge | 响应Cookie maxAge属性。 |
| bool secure | 响应Cookie安全属性。 |
| bool httpOnly | 响应Cookie httpOnly属性。 |
| char * sameSite | 响应Cookie sameSite属性。 |
| uint64_t rawSize | 此响应Cookie的原始大小。 |
| char * originString | 原始字符串。 |
| Rcp_CookieAttributes * cookieAttributes | 响应Cookie中的所有属性。 |
| struct Rcp_ResponseCookies * next | 链式存储。指向下一个Rcp_ResponseCookies的指针。 |

**结构体成员变量说明**

**cookieAttributes**

```ets
Rcp_CookieAttributes* Rcp_ResponseCookies::cookieAttributes
```

描述

响应Cookie中的所有属性。

**domain**

```ets
char* Rcp_ResponseCookies::domain
```

描述

响应Cookie域属性。

**expires**

```ets
char* Rcp_ResponseCookies::expires
```

描述

响应Cookie过期属性。

**httpOnly**

```ets
bool Rcp_ResponseCookies::httpOnly
```

描述

响应Cookie httpOnly属性。

**maxAge**

```ets
uint64_t Rcp_ResponseCookies::maxAge
```

描述

响应Cookie maxAge属性。

**name**

```ets
char* Rcp_ResponseCookies::name
```

描述

响应Cookie名称。

**next**

```ets
struct Rcp_ResponseCookies* Rcp_ResponseCookies::next
```

描述

链式存储。指向下一个[Rcp_ResponseCookies](Rcp_ResponseCookies.md#ZH-CN_TOPIC_0000002553201519__rcp_responsecookies)的指针。

**originString**

```ets
char* Rcp_ResponseCookies::originString
```

描述

原始字符串。

**path**

```ets
char* Rcp_ResponseCookies::path
```

描述

响应Cookie路径属性。

**rawSize**

```ets
uint64_t Rcp_ResponseCookies::rawSize
```

描述

此响应Cookie的原始大小。

**sameSite**

```ets
char* Rcp_ResponseCookies::sameSite
```

描述

响应Cookie sameSite属性。

**secure**

```ets
bool Rcp_ResponseCookies::secure
```

描述

响应Cookie安全属性。

**value**

```ets
char* Rcp_ResponseCookies::value
```

描述

响应Cookie值。