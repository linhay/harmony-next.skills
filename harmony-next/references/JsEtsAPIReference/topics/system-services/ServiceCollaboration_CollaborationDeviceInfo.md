# ServiceCollaboration_CollaborationDeviceInfo

#### 概述

跨设备互通获取的设备信息对象，包含设备的基本信息和能力类型。

**起始版本：** 5.0.0(12)

**相关模块：**[ServiceCollaboration](ServiceCollaboration.md)

#### 汇总

#### 成员变量

名称

描述

uint32_t [deviceType](#ZH-CN_TOPIC_0000002416552656__a17cfb1e778b48e1ab1086c3db5730247)

对端设备类型。只有手机或者平板。手机设备类型的值为0x14，平板设备类型的值为0x17。

char [deviceNetworkId](#ZH-CN_TOPIC_0000002416552656__ac029c525120d06c49e2870b2558a4713) [[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH](ServiceCollaboration.md#ZH-CN_TOPIC_0000002394951629__ga22d10f5d68c518533857b4a3e5947647)]

对端设备network Id。

char [deviceName](#ZH-CN_TOPIC_0000002416552656__a0e045f8cff3ce1255996f3fce3e39809) [[COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH](ServiceCollaboration.md#section115253318501)]

对端设备名。

uint32_t [filterNum](#ZH-CN_TOPIC_0000002416552656__a52bb822ea7f7a30c9396b0db636ed182)

对端设备支持的能力类型列表的大小。

[ServiceCollaborationFilterType](ServiceCollaboration.md#section16675437105618) * [serviceFilterTypes](#ZH-CN_TOPIC_0000002416552656__a02e04d9d0416ecd2c34fde480f4b5a69)

对端设备支持的能力类型列表。

#### 结构体成员变量说明

#### deviceName

```ets
char ServiceCollaboration_CollaborationDeviceInfo::deviceName[[COLLABORATIONDEVICEINFO_DEVICENAME_MAXLENGTH](ServiceCollaboration.md#section115253318501)]
```

**描述**

对端设备名。

#### deviceNetworkId

```ets
char ServiceCollaboration_CollaborationDeviceInfo::deviceNetworkId[[COLLABORATIONDEVICEINFO_DEVICENETWORKID_MAXLENGTH](ServiceCollaboration.md#ZH-CN_TOPIC_0000002394951629__ga22d10f5d68c518533857b4a3e5947647)]
```

**描述**

对端设备network Id。

#### deviceType

```ets
uint32_t ServiceCollaboration_CollaborationDeviceInfo::deviceType
```

**描述**

对端设备类型。只有手机或者平板。手机设备类型的值为0x14，平板设备类型的值为0x17。

#### filterNum

```ets
uint32_t ServiceCollaboration_CollaborationDeviceInfo::filterNum
```

**描述**

对端设备支持的能力类型列表的大小。

#### serviceFilterTypes

```ets
[ServiceCollaborationFilterType](ServiceCollaboration.md#section16675437105618)* ServiceCollaboration_CollaborationDeviceInfo::serviceFilterTypes
```

**描述**

对端设备支持的能力类型列表。