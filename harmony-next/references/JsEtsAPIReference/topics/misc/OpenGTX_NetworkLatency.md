# OpenGTX_NetworkLatency

**概述**

此结构体描述当前设备网络延迟信息，游戏应用获取到网络延迟后传递此参数。

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [opengtx_base.h](opengtx_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| int32_t total | 游戏的总延迟，以ms为单位，取值范围[0,200]。 |
| int32_t up | 游戏上行时延，以ms为单位，取值范围[0,200]。 |
| int32_t down | 游戏下行时延，以ms为单位，取值范围[0,200]。 |

**结构体成员变量说明**

**down**

```ets
int32_t OpenGTX_NetworkLatency::down
```

描述

游戏下行时延，以ms为单位，取值范围[0,200]。

**total**

```ets
int32_t OpenGTX_NetworkLatency::total
```

描述

游戏的总延迟，以ms为单位，取值范围[0,200]。

**up**

```ets
int32_t OpenGTX_NetworkLatency::up
```

描述

游戏上行时延，以ms为单位，取值范围[0,200]。