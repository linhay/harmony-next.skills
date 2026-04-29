# OpenGTX_GameSceneInfo

**概述**

此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

所在头文件： [opengtx_base.h](opengtx_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| OpenGTX_SceneID sceneID | 游戏场景类型。 |
| char* description | 对游戏场景的描述，字节长度范围[0,256]。 |
| int32_t recommendFPS | 当前场景的建议帧率。取值范围0、[30,targetFPS]，若设置0则该值不生效。 |
| int32_t minFPS | 当前场景预期的最小帧率。取值范围0、[30,targetFPS]，若设置0则该值不生效。 |
| int32_t maxFPS | 当前场景预期的最大帧率。取值范围0、[30,targetFPS]，若设置0则该值不生效。 |
| OpenGTX_ResolutionValue resolutionCurValue | 当前场景的分辨率，取值范围360p-8k。 |

**结构体成员变量说明**

**description**

```ets
char* OpenGTX_GameSceneInfo::description
```

描述

对游戏场景的描述，字节长度范围[0,256]。

**maxFPS**

```ets
int32_t OpenGTX_GameSceneInfo::maxFPS
```

描述

当前场景预期的最大帧率。取值范围0、[30,[targetFPS](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002553202211__targetfps)]，若设置0则该值不生效。

**minFPS**

```ets
int32_t OpenGTX_GameSceneInfo::minFPS
```

描述

当前场景预期的最小帧率。取值范围0、[30,[targetFPS](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002553202211__targetfps)]，若设置0则该值不生效。

**recommendFPS**

```ets
int32_t OpenGTX_GameSceneInfo::recommendFPS
```

描述

当前场景的建议帧率。取值范围0、[30,[targetFPS](OpenGTX_ConfigDescription.md#ZH-CN_TOPIC_0000002553202211__targetfps)]，若设置0则该值不生效。

**resolutionCurValue**

```ets
OpenGTX_ResolutionValue OpenGTX_GameSceneInfo::resolutionCurValue
```

描述

当前场景的分辨率，取值范围360p-8k。

**sceneID**

```ets
OpenGTX_SceneID OpenGTX_GameSceneInfo::sceneID
```

描述

游戏场景类型。