# network_boost.h

#### 概述

声明用于网络加速的API。提供基本的函数、结构体和const定义。

**库：** libnetwork_boost.so

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.2(22)

**相关模块：**[NetworkBoost](NetworkBoost.md)

#### 汇总

#### 结构体

名称

描述

struct [NetworkBoost_SceneDesc](NetworkBoost_SceneDesc.md)

业务场景描述信息。

#### 枚举

名称

描述

struct [NetworkBoost_SceneEvent](NetworkBoost.md#section9626183119507){

SCENE_EVENT_ENTER = 0, SCENE_EVENT_UPDATE = 1, SCENE_EVENT_LEAVE = 2

}

业务事件枚举。

#### 函数

名称

描述

int32_t [HMS_NetworkBoost_SetSceneDesc](NetworkBoost.md#section1441013415156)([NetworkBoost_SceneDesc](NetworkBoost_SceneDesc.md) sceneDesc)

设置业务场景。