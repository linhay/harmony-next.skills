# game_pad_event.h

**概述**

定义游戏手柄事件的接口。

库： libohgame_controller.z.so

系统能力： SystemCapability.Game.GameController

起始版本： 21

相关模块：[GameController](GameController.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum GamePad_AxisSourceType GamePad_AxisSourceType | 此枚举定义手柄轴事件来源类型。 |
| typedef enum GamePad_Button_ActionType GamePad_Button_ActionType | 此枚举定义手柄按键动作类型。 |
| typedef struct GamePad_ButtonEvent GamePad_ButtonEvent | 定义手柄按键事件。 |
| typedef struct GamePad_AxisEvent GamePad_AxisEvent | 定义手柄轴事件。 |
| typedef struct GamePad_PressedButton GamePad_PressedButton | 定义手柄按下的按键。 |
| typedef void(*GamePad_ButtonInputMonitorCallback) (const struct GamePad_ButtonEvent *buttonEvent) | 定义在按键事件注册监听接口中使用的回调函数。当玩家按下按键时，该回调函数将被调用。 |
| typedef void(*GamePad_AxisInputMonitorCallback) (const struct GamePad_AxisEvent *axisEvent) | 定义在轴事件注册监听接口中使用的回调函数。当玩家操作摇杆时，该回调函数将被调用。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| GamePad_AxisSourceType { DPAD = 0, LEFT_THUMBSTICK = 1, RIGHT_THUMBSTICK = 2, LEFT_TRIGGER = 3, RIGHT_TRIGGER = 4 } | 手柄轴事件来源类型。 |
| GamePad_Button_ActionType { DOWN = 0, UP = 1 } | 手柄按键动作类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| GameController_ErrorCode OH_GamePad_ButtonEvent_GetDeviceId (const struct GamePad_ButtonEvent *buttonEvent, char **deviceId) | 从按键事件GamePad_ButtonEvent中获取设备ID。 |
| GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonAction (const struct GamePad_ButtonEvent *buttonEvent, GamePad_Button_ActionType *actionType) | 从按键事件GamePad_ButtonEvent中获取按键动作类型。 |
| GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonCode (const struct GamePad_ButtonEvent *buttonEvent, int32_t *code) | 从按键事件GamePad_ButtonEvent中获取按键编码。 |
| GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonCodeName (const struct GamePad_ButtonEvent *buttonEvent, char **codeName) | 从按键事件GamePad_ButtonEvent中获取按键的名称。 |
| GameController_ErrorCode OH_GamePad_PressedButtons_GetCount (const struct GamePad_ButtonEvent *buttonEvent, int32_t *count) | 从按键事件GamePad_ButtonEvent中获取按下的按键数量。 |
| GameController_ErrorCode OH_GamePad_PressedButtons_GetButtonInfo (const struct GamePad_ButtonEvent *buttonEvent, const int32_t index, GamePad_PressedButton **pressedButton) | 从按键事件GamePad_ButtonEvent中获取指定序号的按下的按键。 |
| GameController_ErrorCode OH_GamePad_DestroyPressedButton (GamePad_PressedButton **pressedButton) | 当GamePad_PressedButton实例不再使用， 销毁该实例。 |
| GameController_ErrorCode OH_GamePad_PressedButton_GetButtonCode (const struct GamePad_PressedButton *pressedButton, int32_t *code) | 从按下的按键GamePad_PressedButton中获取按键编码。 |
| GameController_ErrorCode OH_GamePad_PressedButton_GetButtonCodeName (const struct GamePad_PressedButton *pressedButton, char **codeName) | 从按下的按键GamePad_PressedButton中获取按键的名称。 |
| GameController_ErrorCode OH_GamePad_ButtonEvent_GetActionTime (const struct GamePad_ButtonEvent *buttonEvent, int64_t *actionTime) | 从按键事件GamePad_ButtonEvent中获取按键动作的时间。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetDeviceId (const struct GamePad_AxisEvent *axisEvent, char **deviceId) | 从轴事件GamePad_AxisEvent中获取设备ID。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetAxisSourceType (const struct GamePad_AxisEvent *axisEvent, GamePad_AxisSourceType *axisSourceType) | 从轴事件GamePad_AxisEvent中获取轴事件来源类型。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetXAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue) | 从轴事件GamePad_AxisEvent中获取X轴的轴值。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetYAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue) | 从轴事件GamePad_AxisEvent中获取Y轴的轴值。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetZAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue) | 从轴事件GamePad_AxisEvent中获取Z轴的轴值。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetRZAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue) | 从轴事件GamePad_AxisEvent中获取RZ轴的轴值。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetHatXAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue) | 从轴事件GamePad_AxisEvent中获取HatX轴的轴值。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetHatYAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue) | 从轴事件GamePad_AxisEvent中获取HatY轴的轴值。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetBrakeAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue) | 从轴事件GamePad_AxisEvent中获取Brake轴的轴值。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetGasAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue) | 从轴事件GamePad_AxisEvent中获取Gas轴的轴值。 |
| GameController_ErrorCode OH_GamePad_AxisEvent_GetActionTime (const struct GamePad_AxisEvent *axisEvent, int64_t *actionTime) | 从轴事件GamePad_AxisEvent中获取动作时间。 |