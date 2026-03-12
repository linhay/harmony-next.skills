# Http_Request

```ets
typedef struct Http_Request {...} Http_Request
```

#### 概述

HTTP请求结构体。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_http_type.h](net_http_type.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t requestIdHTTP请求的Id。char *urlHTTP请求的URL。[Http_RequestOptions](Http_RequestOptions.md) *optionsHTTP请求配置，指向Http_RequestOptions的指针，参考[Http_RequestOptions](Http_RequestOptions.md)。