# Http_CustomProxy

```ets
typedef struct Http_CustomProxy {...} Http_CustomProxy
```

#### 概述

用户自定义代理配置。

**起始版本：** 20

**相关模块：**[netstack](Netstack.md)

所在头文件： [net_http_type.h](net_http_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char *host | 代理服务器主机名， 如果没有显式设置端口，端口将默认为1080。 |
| int32_t port | 主机端口。取值范围[0, 65535]。 |
| const char *exclusionLists | 不使用代理的主机名列表，主机名支持域名、IP地址以及通配符形式。 |