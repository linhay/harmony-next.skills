# Http_HeaderEntry

```ets
typedef struct Http_HeaderEntry {...} Http_HeaderEntry
```

#### 概述

请求或者响应的标头的所有键值对。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_http_type.h](net_http_type.h.md)

#### 汇总

#### 成员变量

名称描述char *key请求或者响应的标头中的键。[Http_HeaderValue](Http_HeaderValue.md) *value请求或者响应的标头中的键对应的值，参考[Http_HeaderValue](Http_HeaderValue.md)。struct Http_HeaderEntry *next链式存储。指向下一个Http_HeaderEntry。