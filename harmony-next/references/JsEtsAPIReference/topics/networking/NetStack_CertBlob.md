# NetStack_CertBlob

```ets
struct NetStack_CertBlob {...}
```

#### 概述

证书数据结构体。

**起始版本：** 11

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_ssl_c_type.h](../../capi/headers/net_ssl_c_type.h.md)

#### 汇总

#### 成员变量

名称描述enum [NetStack_CertType](../../capi/headers/net_ssl_c_type.h.md#ZH-CN_TOPIC_0000002497605458__netstack_certtype) type证书类型。uint32_t size证书内容长度。uint8_t *data证书内容。