# Http_Proxy

```ets
typedef struct Http_Proxy {...} Http_Proxy
```

#### 概述

代理配置结构体。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

**所在头文件：**[net_http_type.h](../../capi/headers/net_http_type.h.md)

#### 汇总

#### 成员变量

名称描述[Http_ProxyType](../../capi/headers/net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_proxytype) proxyType代理配置类型，参考[Http_ProxyType](../../capi/headers/net_http_type.h.md#ZH-CN_TOPIC_0000002497605460__http_proxytype)。[Http_CustomProxy](Http_CustomProxy.md) customProxy自定义代理配置信息，参考[Http_CustomProxy](Http_CustomProxy.md)。