# Http_HeaderValue

```ets
typedef struct Http_HeaderValue {...} Http_HeaderValue
```

#### 概述

请求或者响应的标头映射的值类型。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_http_type.h](../../capi/headers/net_http_type.h.md)

#### 汇总

#### 成员变量

名称描述char *value标头键值对的值。struct Http_HeaderValue *next链式存储。指向下一个Http_HeaderValue。