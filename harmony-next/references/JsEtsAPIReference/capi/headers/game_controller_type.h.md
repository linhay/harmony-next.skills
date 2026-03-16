# game_controller_type.h

#### 概述

定义GameController模块的通用枚举类型。

**库：** libohgame_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：**[GameController](../../topics/misc/GameController.md)

#### 汇总

#### 类型定义

名称描述typedef enum [GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)此枚举定义游戏控制器的错误码。

#### 枚举

名称描述

[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode) {

GAME_CONTROLLER_SUCCESS = 0,

GAME_CONTROLLER_PARAM_ERROR = 401,

GAME_CONTROLLER_MULTIMODAL_INPUT_ERROR = 32200001,

GAME_CONTROLLER_NO_MEMORY = 32200002

}

游戏控制器错误码。