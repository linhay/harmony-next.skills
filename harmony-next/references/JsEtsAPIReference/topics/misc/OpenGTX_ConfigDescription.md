# OpenGTX_ConfigDescription

#### 概述

此结构体描述OpenGTX属性配置。

**起始版本：** 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [opengtx_base.h](opengtx_base.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OpenGTX_LTPO_Mode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad531d05ca502b93f4153e4b1f749ed0c) [mode](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__ac2431cda0fb7b43a7e4adbaefcbce01d) | LTPO方案模式，支持场景模式、触控模式、自适应模式。 |
| int32_t [targetFPS](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a97b1fac259c0724de14f964712c85cae) | 游戏应用目标帧率，取值范围[30,144]。 |
| char* [packageName](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a44b999153a4f1e122d87503b323bfa3d) | 游戏包名，字节长度范围[1,256]。 |
| char* [appVersion](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a88573b5b4d5bf3d031adf01c4b70f09e) | 游戏应用版本号，字节长度范围[1,256]。 |
| [OpenGTX_EngineType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gadd5a5e0b3b4aa3ea8b0974cba13c0389) [engineType](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a61392b5ab91e08d90223b3c0d14b5f50) | 游戏引擎类型。 |
| char* [engineVersion](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a523c7df207cd9e0ff65ce91792686b46) | 游戏引擎版本号，字节长度范围[0,256]。 |
| [OpenGTX_GameType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga34d898acfaacb3750db454a9ed2038a5) [gameType](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__ae966ba7827b4c860c32696e2aff929df) | 游戏类型。 |
| [OpenGTX_PictureQualityMaxLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gacd5c090213b3593e7c9ab6c93118ff8e) [pictureQualityMaxLevel](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a715706d392c4953b9593e7ff6b663602) | 图像质量。 |
| [OpenGTX_ResolutionValue](OpenGTX_ResolutionValue.md) [resolutionMaxValue](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a461418a95fa10f0b28db6e4222bea507) | 游戏应用支持的最高分辨率，取值范围360p-8k。 |
| int32_t [gameMainThreadId](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a2dfd147c0ebf5f2aed883f9bcdde3027) | 游戏应用的逻辑线程ID，取值范围[0,∞)。 |
| int32_t [gameRenderThreadId](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a77910cdc99dddd0e701e655026df85e9) | 游戏应用的渲染线程ID，取值范围[0,∞)。 |
| int32_t [gameKeyThreadIds](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__af341958c7e20141209ddc2b89badc368) [5] | 游戏应用的关键线程ID列表，取值范围[0,∞)。 |
| bool [vulkanSupport](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a59a8786658db75e046a1502f0ebaadaa) | 是否支持Vulkan。 取值范围：[true, false]。 |

#### 结构体成员变量说明

#### [appVersion](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a88573b5b4d5bf3d031adf01c4b70f09e)

```ets
char* OpenGTX_ConfigDescription::appVersion
```

**描述**

游戏应用版本号，字节长度范围[1,256]。

#### [engineType](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a61392b5ab91e08d90223b3c0d14b5f50)

```ets
[OpenGTX_EngineType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gadd5a5e0b3b4aa3ea8b0974cba13c0389) OpenGTX_ConfigDescription::engineType
```

**描述**

游戏引擎类型。

#### [engineVersion](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a523c7df207cd9e0ff65ce91792686b46)

```ets
char* OpenGTX_ConfigDescription::engineVersion
```

**描述**

游戏引擎版本号，字节长度范围[0,256]。

#### [gameKeyThreadIds](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__af341958c7e20141209ddc2b89badc368)[5]

```ets
int32_t OpenGTX_ConfigDescription::gameKeyThreadIds[5]
```

**描述**

游戏应用的关键线程ID列表，取值范围[0,∞)。

#### [gameMainThreadId](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a2dfd147c0ebf5f2aed883f9bcdde3027)

```ets
int32_t OpenGTX_ConfigDescription::gameMainThreadId
```

**描述**

游戏应用的逻辑线程ID，取值范围[0,∞)。

#### [gameRenderThreadId](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a77910cdc99dddd0e701e655026df85e9)

```ets
int32_t OpenGTX_ConfigDescription::gameRenderThreadId
```

**描述**

游戏应用的渲染线程ID，取值范围[0,∞)。

#### [gameType](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__ae966ba7827b4c860c32696e2aff929df)

```ets
[OpenGTX_GameType](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga34d898acfaacb3750db454a9ed2038a5) OpenGTX_ConfigDescription::gameType
```

**描述**

游戏类型。

#### [mode](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__ac2431cda0fb7b43a7e4adbaefcbce01d)

```ets
[OpenGTX_LTPO_Mode](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad531d05ca502b93f4153e4b1f749ed0c) OpenGTX_ConfigDescription::mode
```

**描述**

LTPO方案模式，支持场景模式、触控模式、自适应模式。

#### [packageName](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a44b999153a4f1e122d87503b323bfa3d)

```ets
char* OpenGTX_ConfigDescription::packageName
```

**描述**

游戏包名，字节长度范围[1,256]。

#### [pictureQualityMaxLevel](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a715706d392c4953b9593e7ff6b663602)

```ets
[OpenGTX_PictureQualityMaxLevel](GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gacd5c090213b3593e7c9ab6c93118ff8e) OpenGTX_ConfigDescription::pictureQualityMaxLevel
```

**描述**

图像质量。

#### [resolutionMaxValue](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a461418a95fa10f0b28db6e4222bea507)

```ets
[OpenGTX_ResolutionValue](OpenGTX_ResolutionValue.md) OpenGTX_ConfigDescription::resolutionMaxValue
```

**描述**

游戏应用支持的最高分辨率，取值范围360p-8k。

#### [targetFPS](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a97b1fac259c0724de14f964712c85cae)

```ets
int32_t OpenGTX_ConfigDescription::targetFPS
```

**描述**

游戏应用目标帧率，取值范围[30,144]。

#### [vulkanSupport](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a59a8786658db75e046a1502f0ebaadaa)

```ets
bool OpenGTX_ConfigDescription::vulkanSupport
```

**描述**

是否支持Vulkan。
