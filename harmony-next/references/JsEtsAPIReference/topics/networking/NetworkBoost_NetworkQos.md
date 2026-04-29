# NetworkBoost_NetworkQos

#### 概述

网络质量回调信息。

**起始版本：** 5.1.0(18)

**相关模块：**[NetworkBoost](NetworkBoost.md)

所在头文件： [network_boost_quality.h](network_boost_quality.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost_PathType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gae8474ae83c3add50ac3fa7702c089ea8) [pathType](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__aa2c0dbab80006b4f907cc4ed6ba1069e) | 相应的数据路径上的网络质量信息。 |
| uint64_t [linkUpBandwidth](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__aa52e26c49ee8385d48729c92944aa76e) | 上行带宽信息，单位为bps。 |
| uint64_t [linkDownBandwidth](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__ad718456602334a20ef9a527cf32f736e) | 下行带宽信息，单位为bps。 |
| uint64_t [linkUpRate](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__adea87b33659ab8d87566b97d9f4afdc8) | 上行速率，单位为bps。 |
| uint64_t [linkDownRate](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__ad607a0c7adddc87641499a1c21501e9a) | 下行速率，单位为bps。 |
| uint32_t [rttMs](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__a77a16170d4a0ab235de7c0ca59db88dc) | RTT时延，单位为ms，取值范围是任意正数。 |
| uint32_t [linkUpBufferDelayMs](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__a13c017d5d078e43588c9be922c6b39dd) | 上行发送空口缓冲时延，单位为ms，取值范围是任意正数。 |
| uint32_t [linkUpBufferCongestionPercent](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__aa5d0ece94735554c3c0c8296a6e4d1d1) | 上行发送空口缓冲时延占总缓冲时间的比例，取值范围[0, 100]。 |

#### 结构体成员变量说明

#### [linkDownBandwidth](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__ad718456602334a20ef9a527cf32f736e)

```ets
uint64_t NetworkBoost_NetworkQos::linkDownBandwidth
```

**描述**

下行带宽信息，单位为bps。

#### [linkDownRate](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__ad607a0c7adddc87641499a1c21501e9a)

```ets
uint64_t NetworkBoost_NetworkQos::linkDownRate
```

**描述**

下行速率，单位为bps。

#### [linkUpBandwidth](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__aa52e26c49ee8385d48729c92944aa76e)

```ets
uint64_t NetworkBoost_NetworkQos::linkUpBandwidth
```

**描述**

上行带宽信息，单位为bps。

#### [linkUpBufferCongestionPercent](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__aa5d0ece94735554c3c0c8296a6e4d1d1)

```ets
uint32_t NetworkBoost_NetworkQos::linkUpBufferCongestionPercent
```

**描述**

上行发送空口缓冲时延占总缓冲时间的比例，取值范围[0, 100]。

#### [linkUpBufferDelayMs](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__a13c017d5d078e43588c9be922c6b39dd)

```ets
uint32_t NetworkBoost_NetworkQos::linkUpBufferDelayMs
```

**描述**

上行发送空口缓冲时延（单位ms），取值范围是任意正数。

#### [linkUpRate](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__adea87b33659ab8d87566b97d9f4afdc8)

```ets
uint64_t NetworkBoost_NetworkQos::linkUpRate
```

**描述**

上行速率，单位为bps。

#### [pathType](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__aa2c0dbab80006b4f907cc4ed6ba1069e)

```ets
[NetworkBoost_PathType](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__gae8474ae83c3add50ac3fa7702c089ea8) NetworkBoost_NetworkQos::pathType
```

**描述**

相应的数据路径上的网络质量信息。

#### [rttMs](NetworkBoost_NetworkQos.md#ZH-CN_TOPIC_0000002463535634__a77a16170d4a0ab235de7c0ca59db88dc)

```ets
uint32_t NetworkBoost_NetworkQos::rttMs
```

**描述**

RTT时延（单位ms），取值范围是任意正数。
