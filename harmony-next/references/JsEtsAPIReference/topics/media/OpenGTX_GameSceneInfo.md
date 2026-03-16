# OpenGTX_GameSceneInfo

#### 概述

此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](../graphics/GraphicsAccelerate.md)

#### 汇总

#### 成员变量

名称

描述

[OpenGTX_SceneID](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad7e5d2d235183dc0c6549331d6bc2932)[sceneID](OpenGTX_GameSceneInfo.md#ZH-CN_TOPIC_0000002385157846__aebbf4e9b7189fe91c035c5f883c0aa17)

游戏场景类型。

char* [description](OpenGTX_GameSceneInfo.md#ZH-CN_TOPIC_0000002385157846__ad16ededcd444a4183f46987c55a98ff4)

对游戏场景的描述，字符长度范围[0,256]。

int32_t [recommendFPS](OpenGTX_GameSceneInfo.md#ZH-CN_TOPIC_0000002385157846__a1187bcfe8f07e6e974a2c7690c78af65)

当前场景的建议帧率。取值范围0、[30,[targetFPS](../misc/OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a97b1fac259c0724de14f964712c85cae)]，若设置0则该值不生效。

int32_t [minFPS](OpenGTX_GameSceneInfo.md#ZH-CN_TOPIC_0000002385157846__a9d6a81921f08d4a6e6e8e122f5c8ace7)

当前场景预期的最小帧率。取值范围0、[30,[targetFPS](../misc/OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a97b1fac259c0724de14f964712c85cae)]，若设置0则该值不生效。

int32_t [maxFPS](OpenGTX_GameSceneInfo.md#ZH-CN_TOPIC_0000002385157846__a854d149c4c4e0b6953800592f96b312b)

当前场景预期的最大帧率。取值范围0、[30,[targetFPS](../misc/OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a97b1fac259c0724de14f964712c85cae)]，若设置0则该值不生效。

[OpenGTX_ResolutionValue](../misc/OpenGTX_ResolutionValue.md)[resolutionCurValue](OpenGTX_GameSceneInfo.md#ZH-CN_TOPIC_0000002385157846__ad91afb9f2d7a372969002871e184a4ca)

当前场景的分辨率，取值范围360p-8k。

#### 结构体成员变量说明

#### description

```ets
char* OpenGTX_GameSceneInfo::description
```

**描述**

对游戏场景的描述，字符长度范围[0,256]。

#### maxFPS

```ets
int32_t OpenGTX_GameSceneInfo::maxFPS
```

**描述**

当前场景预期的最大帧率。取值范围0、[30,[targetFPS](../misc/OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a97b1fac259c0724de14f964712c85cae)]，若设置0则该值不生效。

#### minFPS

```ets
int32_t OpenGTX_GameSceneInfo::minFPS
```

**描述**

当前场景预期的最小帧率。取值范围0、[30,[targetFPS](../misc/OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a97b1fac259c0724de14f964712c85cae)]，若设置0则该值不生效。

#### recommendFPS

```ets
int32_t OpenGTX_GameSceneInfo::recommendFPS
```

**描述**

当前场景的建议帧率。取值范围0、[30,[targetFPS](../misc/OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002385317750__a97b1fac259c0724de14f964712c85cae)]，若设置0则该值不生效。

#### resolutionCurValue

```ets
[OpenGTX_ResolutionValue](../misc/OpenGTX_ResolutionValue.md) OpenGTX_GameSceneInfo::resolutionCurValue
```

**描述**

当前场景的分辨率，取值范围360p-8k。

#### sceneID

```ets
[OpenGTX_SceneID](../graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gad7e5d2d235183dc0c6549331d6bc2932) OpenGTX_GameSceneInfo::sceneID
```

**描述**

游戏场景类型。