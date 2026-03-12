# ServiceCollaboration_SelectInfo

#### 概述

使用[HMS_ServiceCollaboration_StartCollaboration](ServiceCollaboration.md#section4531193410296)触发跨设备互通时，被选择的设备信息。

**起始版本：** 5.0.0(12)

**相关模块：**[ServiceCollaboration](ServiceCollaboration.md)

#### 汇总

#### 成员变量

名称

描述

[ServiceCollaborationFilterType](ServiceCollaboration.md#section16675437105618)[serviceFilterType](#ZH-CN_TOPIC_0000002423821868__a9154e00b7840c2e739599ebfce7c5deb)

开发者期望的设备能力类型。

char [deviceNetworkId](#ZH-CN_TOPIC_0000002423821868__a8829d22e5d51fc0814cc3e1f5d814679) [[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH](zh-cn_topic_0000002394951629.html#ZH-CN_TOPIC_0000002394951629__ga22d10f5d68c518533857b4a3e5947647)]

被选择的设备network Id。

uint32_t [maxSize](#ZH-CN_TOPIC_0000002423821868__a8aa0e58e2736c50b8c9957c7b14c7cd3)

能被选中的最大图片数量。

#### 结构体成员变量说明

#### deviceNetworkId

```ets
char ServiceCollaboration_SelectInfo::deviceNetworkId[[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH](ServiceCollaboration.md#ZH-CN_TOPIC_0000002394951629__ga22d10f5d68c518533857b4a3e5947647)]
```

**描述**

被选择的设备network Id。

#### maxSize

```ets
uint32_t ServiceCollaboration_SelectInfo::maxSize
```

**描述**

能被选中的最大图片数量。

#### serviceFilterType

```ets
[ServiceCollaborationFilterType](ServiceCollaboration.md#section16675437105618) ServiceCollaboration_SelectInfo::serviceFilterType
```

**描述**

开发者期望的设备能力类型。