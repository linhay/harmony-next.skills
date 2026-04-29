# Http_Request

```ets
typedef struct Http_Request {...} Http_Request
```

#### 概述

HTTP请求结构体。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

所在头文件： [net_http_type.h](net_http_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32_t requestId | HTTP请求的Id。 |
| char *url | HTTP请求的URL。 |
| [Http_RequestOptions](Http_RequestOptions.md) *options | HTTP请求配置，指向Http_RequestOptions的指针，参考Http_RequestOptions。 |
