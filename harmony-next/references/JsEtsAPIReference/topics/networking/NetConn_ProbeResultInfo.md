# NetConn_ProbeResultInfo

```ets
typedef struct NetConn_ProbeResultInfo {...} NetConn_ProbeResultInfo
```

#### 概述

定义探测结果信息。

**起始版本：** 20

**相关模块：**[NetConnection](NetConnection.md)

所在头文件： [net_connection_type.h](net_connection_type.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8_t lossRate | 丢包率，百分制，值100表示100%丢包；50表示50%丢包。 |
| uint32_t rtt[NETCONN_MAX_RTT_NUM] | 时延结果，包含最小、最大、平均、标准差。 |