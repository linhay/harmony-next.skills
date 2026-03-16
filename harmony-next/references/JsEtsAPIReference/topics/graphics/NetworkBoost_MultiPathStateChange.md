# NetworkBoost_MultiPathStateChange

#### 概述

多网状态信息，用于注册多网状态变化事件回调后，系统多网状态发生变化的事件通知。

**起始版本：** 6.0.2(22)

**相关模块：**[NetworkBoost](../networking/NetworkBoost.md)

#### 汇总

#### 成员变量

名称

描述

[NetworkBoost_MultiPathState](../networking/NetworkBoost.md#section12626124820456)[multiPathState](#section159871228122717)

多网状态。

[NetworkBoost_MultiPathChangeCause](../networking/NetworkBoost.md#section19927184203916)[changeCause](#section2054235172714)

多网状态变化原因。

[NetworkBoost_NetHandle](../networking/NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga83a1277967e95e2965b6f8dbee5945cc)[netHandle](#section18578175863714)

多网链路的netHandle。

[NetworkBoost_PathState](../networking/NetworkBoost.md#section1774664693518)[pathState](#section135790582373)

多网链路状态。

[NetworkBoost_PathType](../networking/NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga45748b2a298346cbea2f1cbe573ffe72)[pathType](#section1487115310381)

多网链路类型。

#### 结构体成员变量说明

#### multiPathState

```ets
NetworkBoost_MultiPathState NetworkBoost_MultiPathStateChange::multiPathState
```

**描述**

多网状态，可以通过该信息获取当前多网所处状态，包含空闲态、建立中、已建立和释放中四种状态。

#### changeCause

```ets
NetworkBoost_MultiPathChangeCause NetworkBoost_MultiPathStateChange::changeCause
```

**描述**

多网状态变化原因，在多网状态发生变化时，通过该信息可以获取发生多网状态发生变化的原因。

#### netHandle

```ets
NetworkBoost_NetHandle NetworkBoost_MultiPathStateChange::netHandle
```

**描述**

多网链路的netHandle。

#### pathState

```ets
NetworkBoost_PathState NetworkBoost_MultiPathStateChange::pathState
```

**描述**

多网链路状态。

#### pathType

```ets
NetworkBoost_PathType NetworkBoost_MultiPathStateChange::pathType
```

**描述**

多网链路类型。