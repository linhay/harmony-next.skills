# NetworkBoost_HandoverComplete

#### 概述

连接迁移完成信息。

**起始版本：** 5.1.0(18)

**相关模块：**[NetworkBoost](NetworkBoost.md)

所在头文件： [network_boost_handover.h](network_boost_handover.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost_ErrorResult](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga98419dae6f140b89cac79821f9cbbc9d) [result](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a940df802a9744d5ea6f1c1c4e4460371) | 连接迁移结果。 |
| bool [handoverContinue](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a0bf437c3ed4b6a4677cc33ede5e98e32) | 是否继续等待HandoverComplete消息，当存在两条以上路径时，会存在多个HandoverComplete消息。 true表示还有新链路待激活，系统还会上报HandoverComplete消息，一般发生在连接迁移到多个网络的场景。 false表示当前已经是最后一个HandoverComplete消息，连接迁移流程完成。 |
| uint32_t [oldPathLifetime](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a4b9a08e22f33ca1f09c30f3ca3b01425) | 老链路的剩余生存时长，单位为s，取值为任意正整数或0。 |
| [NetworkBoost_DataSpeedAction](NetworkBoost_DataSpeedAction.md) [oldDataSpeedAction](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__ae0dfbb93116a17a8df951ab5ee40b437) | 老链路发包建议。 |
| bool [pathTypeChanged](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a610d963e22ad2c6151dc5c3f1770a42b) | 新老链路类型是否发生变更。true表示发生变化，如Wi-Fi<->蜂窝。false表示没有发生变化。 |
| [NetworkBoost_NetHandle](NetworkBoost_NetHandle.md) [newNetHandle](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a9de97d7518d5b5da314053ae4b4df8a3) | 新链路的NetHandle信息。 |
| [NetworkBoost_ReEstAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga99d4ae084f2d5e3744231152e58e51aa) [reEstAction](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a29c0a1d7ce857c5e3bfb5e775344250b) | 链路重建类型。 |
| NetworkBoost_DataSpeedAction [newDataSpeedAction](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a5588fe3f833622f5eb81d34cc6fcbe5f) | 新链路发包建议。 |

#### 结构体成员变量说明

#### [handoverContinue](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a0bf437c3ed4b6a4677cc33ede5e98e32)

```ets
bool NetworkBoost_HandoverComplete::handoverContinue
```

**描述**

是否继续等待HandoverComplete消息，当存在两条以上路径时，会存在多个HandoverComplete消息。

true表示还有新链路待激活，系统还会上报HandoverComplete消息，一般发生在连接迁移到多个网络的场景。

false表示当前已经是最后一个HandoverComplete消息，连接迁移流程完成。

#### [newDataSpeedAction](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a5588fe3f833622f5eb81d34cc6fcbe5f)

```ets
[NetworkBoost_DataSpeedAction](NetworkBoost_DataSpeedAction.md) NetworkBoost_HandoverComplete::newDataSpeedAction
```

**描述**

新链路发包建议。

#### [newNetHandle](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a9de97d7518d5b5da314053ae4b4df8a3)

```ets
[NetworkBoost_NetHandle](NetworkBoost_NetHandle.md) NetworkBoost_HandoverComplete::newNetHandle
```

**描述**

新链路的NetHandle信息。

#### [oldDataSpeedAction](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__ae0dfbb93116a17a8df951ab5ee40b437)

```ets
[NetworkBoost_DataSpeedAction](NetworkBoost_DataSpeedAction.md) NetworkBoost_HandoverComplete::oldDataSpeedAction
```

**描述**

老链路发包建议。

#### [oldPathLifetime](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a4b9a08e22f33ca1f09c30f3ca3b01425)

```ets
uint32_t NetworkBoost_HandoverComplete::oldPathLifetime
```

**描述**

老链路的剩余生存时长，单位为s，取值为任意正整数或0。

#### [pathTypeChanged](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a610d963e22ad2c6151dc5c3f1770a42b)

```ets
bool NetworkBoost_HandoverComplete::pathTypeChanged
```

**描述**

新老链路类型是否发生变更。true表示发生变化，如Wi-Fi<->蜂窝。false表示没有发生变化。

#### [reEstAction](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a29c0a1d7ce857c5e3bfb5e775344250b)

```ets
[NetworkBoost_ReEstAction](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga99d4ae084f2d5e3744231152e58e51aa) NetworkBoost_HandoverComplete::reEstAction
```

**描述**

链路重建类型。

#### [result](NetworkBoost_HandoverComplete.md#ZH-CN_TOPIC_0000002496694673__a940df802a9744d5ea6f1c1c4e4460371)

```ets
[NetworkBoost_ErrorResult](NetworkBoost.md#ZH-CN_TOPIC_0000002463695266__ga98419dae6f140b89cac79821f9cbbc9d) NetworkBoost_HandoverComplete::result
```

**描述**

连接迁移结果。
