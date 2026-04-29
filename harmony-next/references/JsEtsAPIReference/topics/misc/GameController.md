# GameController

#### 概述

GameController模块提供游戏控制器功能的API接口。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

#### 汇总

#### 文件

| 名称 | 描述 |
| --- | --- |
| [game_controller_type.h](game_controller_type.h.md) | 定义GameController模块的通用枚举类型。 |
| [game_device.h](game_device.h.md) | 定义游戏设备的接口。 |
| [game_device_event.h](game_device_event.h.md) | 定义游戏设备事件的接口。 |
| [game_pad.h](game_pad.h.md) | 定义游戏手柄的接口。 |
| [game_pad_event.h](game_pad_event.h.md) | 定义游戏手柄事件的接口。 |

#### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef enum GameController_ErrorCode GameController_ErrorCode | 此枚举定义游戏控制器的错误码。 |
| typedef struct GameDevice_AllDeviceInfos GameDevice_AllDeviceInfos | 定义OH_GameDevice_GetAllDeviceInfos接口的调用结果。 |
| typedef enum GameDevice_StatusChangedType GameDevice_StatusChangedType | 此枚举定义设备的状态变化类型。 |
| typedef enum GameDevice_DeviceType GameDevice_DeviceType | 此枚举定义设备类型。 |
| typedef struct GameDevice_DeviceInfo GameDevice_DeviceInfo | 定义设备信息。 |
| typedef struct GameDevice_DeviceEvent GameDevice_DeviceEvent | 定义设备状态变化事件。 |
| typedef void(*GameDevice_DeviceMonitorCallback) (const struct GameDevice_DeviceEvent *deviceEvent) | 定义OH_GameDevice_RegisterDeviceMonitor中使用的回调函数。当设备上线或下线时，该回调函数将被调用。 |
| typedef enum GamePad_AxisSourceType GamePad_AxisSourceType | 此枚举定义手柄轴事件来源类型。 |
| typedef enum GamePad_Button_ActionType GamePad_Button_ActionType | 此枚举定义手柄按键动作类型。 |
| typedef struct GamePad_ButtonEvent GamePad_ButtonEvent | 定义手柄按键事件。 |
| typedef struct GamePad_AxisEvent GamePad_AxisEvent | 定义手柄轴事件。 |
| typedef struct GamePad_PressedButton GamePad_PressedButton | 定义手柄按下的按键。 |
| typedef void(*GamePad_ButtonInputMonitorCallback) (const struct GamePad_ButtonEvent *buttonEvent) | 定义在按键事件注册监听接口中使用的回调函数。当玩家按下按键时，该回调函数将被调用。 |
| typedef void(*GamePad_AxisInputMonitorCallback) (const struct GamePad_AxisEvent *axisEvent) | 定义在轴事件注册监听接口中使用的回调函数。当玩家操作摇杆时，该回调函数将被调用。 |

#### 枚举

名称描述
| --- | --- |
| GameController_ErrorCode { GAME_CONTROLLER_SUCCESS = 0, GAME_CONTROLLER_PARAM_ERROR = 401, GAME_CONTROLLER_MULTIMODAL_INPUT_ERROR = 32200001, GAME_CONTROLLER_NO_MEMORY = 32200002 } | 游戏控制器错误码。 |
| GameDevice_StatusChangedType { OFFLINE = 0, ONLINE = 1 } | 设备的状态变化类型。 |
| GameDevice_DeviceType { UNKNOWN = 0, GAME_PAD = 1 } | 设备类型。 |
| GamePad_AxisSourceType { DPAD = 0, LEFT_THUMBSTICK = 1, RIGHT_THUMBSTICK = 2, LEFT_TRIGGER = 3, RIGHT_TRIGGER = 4 } | 手柄轴事件来源类型。 |
| GamePad_Button_ActionType { DOWN = 0, UP = 1 } | 手柄按键动作类型。 |

#### 函数

| 名称 | 描述 |
| --- | --- |
| GameController_ErrorCode OH_GameDevice_GetAllDeviceInfos (GameDevice_AllDeviceInfos **allDeviceInfos) | 获取所有在线设备的信息。 |
| GameController_ErrorCode OH_GameDevice_RegisterDeviceMonitor (GameDevice_DeviceMonitorCallback deviceMonitorCallback) | 注册设备状态变化事件的监听回调。 |
| GameController_ErrorCode OH_GameDevice_UnregisterDeviceMonitor (void) | 取消注册设备状态变化事件的监听回调。 |
| GameController_ErrorCode OH_GameDevice_DestroyAllDeviceInfos (GameDevice_AllDeviceInfos **allDeviceInfos) | 当GameDevice_AllDeviceInfos实例不再使用，销毁该实例。 |
| GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetCount (const struct GameDevice_AllDeviceInfos *allDeviceInfos, int32_t *count) | 获取设备数量。 |
| GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetDeviceInfo (const struct GameDevice_AllDeviceInfos *allDeviceInfos, const int32_t index, GameDevice_DeviceInfo **deviceInfo) | 从所有设备信息中获取指定序号的设备信息。 |
| GameController_ErrorCode OH_GameDevice_DeviceEvent_GetChangedType (const struct GameDevice_DeviceEvent *deviceEvent, GameDevice_StatusChangedType *statusChangedType) | 从设备状态变化事件中获取状态变化类型。 |
| GameController_ErrorCode OH_GameDevice_DeviceEvent_GetDeviceInfo (const struct GameDevice_DeviceEvent *deviceEvent, GameDevice_DeviceInfo **deviceInfo) | 从设备状态变化事件中获取设备信息。 |
| GameController_ErrorCode OH_GameDevice_DestroyDeviceInfo (GameDevice_DeviceInfo **deviceInfo) | 当GameDevice_DeviceInfo实例不再使用，销毁该实例。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceId (const struct GameDevice_DeviceInfo *deviceInfo, char **deviceId) | 从设备信息GameDevice_DeviceInfo中获取设备ID。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetName (const struct GameDevice_DeviceInfo *deviceInfo, char **name) | 从设备信息GameDevice_DeviceInfo中获取设备名称。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetProduct (const struct GameDevice_DeviceInfo *deviceInfo, int32_t *product) | 从设备信息GameDevice_DeviceInfo中获取产品信息。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetVersion (const struct GameDevice_DeviceInfo *deviceInfo, int32_t *version) | 从设备信息GameDevice_DeviceInfo中获取版本信息。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetPhysicalAddress (const struct GameDevice_DeviceInfo *deviceInfo, char **physicalAddress) | 从设备信息GameDevice_DeviceInfo中获取物理地址。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceType (const struct GameDevice_DeviceInfo *deviceInfo, GameDevice_DeviceType *deviceType) | 从设备信息GameDevice_DeviceInfo中获取设备类型。 |
| GameController_ErrorCode OH_GamePad_LeftShoulder_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册LeftShoulder按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor (void) | 取消注册LeftShoulder按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightShoulder_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册RightShoulder按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightShoulder_UnregisterButtonInputMonitor (void) | 取消注册RightShoulder按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册LeftTrigger按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterButtonInputMonitor (void) | 取消注册LeftTrigger按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback) | 注册LeftTrigger轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterAxisInputMonitor (void) | 取消注册LeftTrigger轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightTrigger_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册RightTrigger按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterButtonInputMonitor (void) | 取消注册RightTrigger按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightTrigger_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback) | 注册RightTrigger轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterAxisInputMonitor (void) | 取消注册RightTrigger轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonMenu_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册Menu按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonMenu_UnregisterButtonInputMonitor (void) | 取消注册Menu按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonHome_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册Home按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonHome_UnregisterButtonInputMonitor (void) | 取消注册Home按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonA_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册A按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonA_UnregisterButtonInputMonitor (void) | 取消注册A按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonB_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册B按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonB_UnregisterButtonInputMonitor (void) | 取消注册B按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonX_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册X按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonX_UnregisterButtonInputMonitor (void) | 取消注册X按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonY_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册Y按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonY_UnregisterButtonInputMonitor (void) | 取消注册Y按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonC_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册C按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_ButtonC_UnregisterButtonInputMonitor (void) | 取消注册C按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_LeftButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册方向按键的向左按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_LeftButton_UnregisterButtonInputMonitor (void) | 取消注册方向按键的向左按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_RightButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册方向按键的向右按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_RightButton_UnregisterButtonInputMonitor (void) | 取消注册方向按键的向右按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_UpButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册方向按键的向上按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_UpButton_UnregisterButtonInputMonitor (void) | 取消注册方向按键的向上按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_DownButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册方向按键的向下按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_DownButton_UnregisterButtonInputMonitor (void) | 取消注册方向按键的向下按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback) | 注册方向按键轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_Dpad_UnregisterAxisInputMonitor (void) | 取消注册方向按键轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册LeftThumbstick按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterButtonInputMonitor (void) | 取消注册LeftThumbstick按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback) | 注册LeftThumbstick轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor (void) | 取消注册LeftThumbstick轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback) | 注册RightThumbstick按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterButtonInputMonitor (void) | 取消注册RightThumbstick按键事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback) | 注册RightThumbstick轴事件的监听回调。 |
| GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterAxisInputMonitor (void) | 取消注册RightThumbstick轴事件的监听回调。 |
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

#### 类型定义说明

#### GameController_ErrorCode

```ets
typedef enum GameController_ErrorCodeGameController_ErrorCode
```

**描述**

此枚举定义游戏控制器的错误码。

**起始版本：** 21

#### GameDevice_AllDeviceInfos

```ets
typedef struct GameDevice_AllDeviceInfosGameDevice_AllDeviceInfos
```

**描述**

定义[OH_GameDevice_GetAllDeviceInfos](#ZH-CN_TOPIC_0000002522242336__oh_gamedevice_getalldeviceinfos)接口的调用结果。

**起始版本：** 21

#### GameDevice_DeviceEvent

```ets
typedef struct GameDevice_DeviceEventGameDevice_DeviceEvent
```

**描述**

定义设备状态变化事件。

**起始版本：** 21

#### GameDevice_DeviceInfo

```ets
typedef struct GameDevice_DeviceInfoGameDevice_DeviceInfo
```

**描述**

定义设备信息。

**起始版本：** 21

#### GameDevice_DeviceMonitorCallback

```ets
typedef void(*GameDevice_DeviceMonitorCallback) (const struct GameDevice_DeviceEvent *deviceEvent)
```

**描述**

定义[OH_GameDevice_RegisterDeviceMonitor](#ZH-CN_TOPIC_0000002522242336__oh_gamedevice_registerdevicemonitor)中使用的回调函数。当设备上线或下线时，该回调函数将被调用。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceEvent | 输出参数。设备状态变化事件GameDevice_DeviceEvent。 |

#### GameDevice_DeviceType

```ets
typedef enum GameDevice_DeviceTypeGameDevice_DeviceType
```

**描述**

此枚举定义设备类型。

**起始版本：** 21

#### GameDevice_StatusChangedType

```ets
typedef enum GameDevice_StatusChangedTypeGameDevice_StatusChangedType
```

**描述**

此枚举定义设备的状态变化类型。

**起始版本：** 21

#### GamePad_AxisEvent

```ets
typedef struct GamePad_AxisEventGamePad_AxisEvent
```

**描述**

定义手柄轴事件。

**起始版本：** 21

#### GamePad_AxisInputMonitorCallback

```ets
typedef void(*GamePad_AxisInputMonitorCallback) (const struct GamePad_AxisEvent *axisEvent)
```

**描述**

定义在轴事件注册监听接口中使用的回调函数。当玩家操作摇杆时，该回调函数将被调用。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 输出参数，手柄轴事件GamePad_AxisEvent。 |

#### GamePad_AxisSourceType

```ets
typedef enum GamePad_AxisSourceType GamePad_AxisSourceType
```

**描述**

此枚举定义手柄轴事件来源类型。

**起始版本：** 21

#### GamePad_Button_ActionType

```ets
typedef enum GamePad_Button_ActionTypeGamePad_Button_ActionType
```

**描述**

此枚举定义手柄按键动作类型。

**起始版本：** 21

#### GamePad_ButtonEvent

```ets
typedef struct GamePad_ButtonEventGamePad_ButtonEvent
```

**描述**

定义手柄按键事件。

**起始版本：** 21

#### GamePad_ButtonInputMonitorCallback

```ets
typedef void(*GamePad_ButtonInputMonitorCallback) (const struct GamePad_ButtonEvent *buttonEvent)
```

**描述**

定义在按键事件注册监听接口中使用的回调函数。当玩家按下按键时，该回调函数将被调用。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 输出参数，手柄按键事件GamePad_ButtonEvent。 |

#### GamePad_PressedButton

```ets
typedef struct GamePad_PressedButtonGamePad_PressedButton
```

**描述**

定义手柄按下的按键。

**起始版本：** 21

#### 枚举类型说明

#### GameController_ErrorCode

```ets
enum GameController_ErrorCode
```

**描述**

此枚举定义游戏控制器的错误码。

**起始版本：** 21

| 枚举值 | 描述 |
| --- | --- |
| GAME_CONTROLLER_SUCCESS | 成功。 |
| GAME_CONTROLLER_PARAM_ERROR | 参数非法。 |
| GAME_CONTROLLER_MULTIMODAL_INPUT_ERROR | 查询多模输入中所有设备信息失败。 |
| GAME_CONTROLLER_NO_MEMORY | 设备内存不足。 |

#### GameDevice_DeviceType

```ets
enum GameDevice_DeviceType
```

**描述**

此枚举定义设备类型。

**起始版本：** 21

| 枚举值 | 描述 |
| --- | --- |
| UNKNOWN | 未知。 |
| GAME_PAD | 游戏手柄。 |

#### GameDevice_StatusChangedType

```ets
enum GameDevice_StatusChangedType
```

**描述**

此枚举定义设备的状态变化类型。

**起始版本：** 21

| 枚举值 | 描述 |
| --- | --- |
| OFFLINE | 设备下线。 |
| ONLINE | 设备上线。 |

#### GamePad_AxisSourceType

```ets
enum GamePad_AxisSourceType
```

**描述**

此枚举定义手柄轴事件来源类型。

**起始版本：** 21

| 枚举值 | 描述 |
| --- | --- |
| DPAD | 轴事件来源于方向按键DPAD。 |
| LEFT_THUMBSTICK | 轴事件来源于LeftThumbstick。 |
| RIGHT_THUMBSTICK | 轴事件来源于RightThumbstick。 |
| LEFT_TRIGGER | 轴事件来源于LeftTrigger。 |
| RIGHT_TRIGGER | 轴事件来源于RightTrigger。 |

#### GamePad_Button_ActionType

```ets
enum GamePad_Button_ActionType
```

**描述**

此枚举定义手柄按键动作类型。

**起始版本：** 21

| 枚举值 | 描述 |
| --- | --- |
| DOWN | 按键按下。 |
| UP | 按键抬起。 |

#### 函数说明

#### OH_GameDevice_AllDeviceInfos_GetCount()

```ets
GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetCount (const struct GameDevice_AllDeviceInfos *allDeviceInfos, int32_t *count)
```

**描述**

获取设备数量。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| allDeviceInfos | 指针指向GameDevice_AllDeviceInfos实例，不能为空，否则将返回错误码。 |
| count | 输出参数，设备数量。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数allDeviceInfos为null。

#### OH_GameDevice_AllDeviceInfos_GetDeviceInfo()

```ets
GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetDeviceInfo (const struct GameDevice_AllDeviceInfos *allDeviceInfos, const int32_t index, GameDevice_DeviceInfo **deviceInfo)
```

**描述**

从所有设备信息中获取指定序号的设备信息。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| allDeviceInfos | 指针指向GameDevice_AllDeviceInfos实例，不能为空，否则将返回错误码。 |
| index | 指定查询的设备序号。 |
| deviceInfo | 输出参数，二级指针指向GameDevice_DeviceInfo设备信息实例。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：allDeviceInfos为null或者index小于0或者index大于等于所有设备数。

#### OH_GameDevice_DestroyAllDeviceInfos()

```ets
GameController_ErrorCode OH_GameDevice_DestroyAllDeviceInfos (GameDevice_AllDeviceInfos **allDeviceInfos)
```

**描述**

当[GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002522242336__gamedevice_alldeviceinfos)实例不再使用，销毁该实例。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| allDeviceInfos | 二级指针指向GameDevice_AllDeviceInfos实例，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数allDeviceInfos为null。

#### OH_GameDevice_DestroyDeviceInfo()

```ets
GameController_ErrorCode OH_GameDevice_DestroyDeviceInfo (GameDevice_DeviceInfo **deviceInfo)
```

**描述**

当[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002522242336__gamedevice_deviceinfo)实例不再使用，销毁该实例。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 二级指针指向GameDevice_DeviceInfo实例，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceInfo为null。

#### OH_GameDevice_DeviceEvent_GetChangedType()

```ets
GameController_ErrorCode OH_GameDevice_DeviceEvent_GetChangedType (const struct GameDevice_DeviceEvent *deviceEvent, GameDevice_StatusChangedType *statusChangedType)
```

**描述**

从设备状态变化事件[GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002522242336__gamedevice_deviceevent)中获取状态变化类型。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceEvent | 指针指向GameDevice_DeviceEvent实例，不能为空，否则将返回错误码。 |
| statusChangedType | 输出参数，设备状态变化类型。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceEvent为null。

#### OH_GameDevice_DeviceEvent_GetDeviceInfo()

```ets
GameController_ErrorCode OH_GameDevice_DeviceEvent_GetDeviceInfo (const struct GameDevice_DeviceEvent *deviceEvent, GameDevice_DeviceInfo **deviceInfo)
```

**描述**

从设备状态变化事件[GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002522242336__gamedevice_deviceevent)中获取设备信息。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceEvent | 指针指向GameDevice_DeviceEvent实例，不能为空，否则将返回错误码。 |
| deviceInfo | 输出参数，二级指针指向GameDevice_DeviceInfo设备信息实例。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceEvent为null。

#### OH_GameDevice_DeviceInfo_GetDeviceId()

```ets
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceId (const struct GameDevice_DeviceInfo *deviceInfo, char **deviceId)
```

**描述**

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002522242336__gamedevice_deviceinfo)中获取设备ID。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空，否则将返回错误码。 |
| deviceId | 输出参数，二级指针指向设备ID。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceInfo或deviceId为null。

-

GAME_CONTROLLER_NO_MEMORY：设备内存不足。

#### OH_GameDevice_DeviceInfo_GetDeviceType()

```ets
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceType (const struct GameDevice_DeviceInfo *deviceInfo, GameDevice_DeviceType *deviceType)
```

**描述**

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002522242336__gamedevice_deviceinfo)中获取设备类型。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空，否则将返回错误码。 |
| deviceType | 输出参数，设备类型。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceInfo为null。

#### OH_GameDevice_DeviceInfo_GetName()

```ets
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetName (const struct GameDevice_DeviceInfo *deviceInfo, char **name)
```

**描述**

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002522242336__gamedevice_deviceinfo)中获取设备名称。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空，否则将返回错误码。 |
| name | 输出参数，二级指针指向设备名称。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceInfo或name为null。

-

GAME_CONTROLLER_NO_MEMORY：设备内存不足。

#### OH_GameDevice_DeviceInfo_GetPhysicalAddress()

```ets
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetPhysicalAddress (const struct GameDevice_DeviceInfo *deviceInfo, char **physicalAddress)
```

**描述**

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002522242336__gamedevice_deviceinfo)中获取物理地址。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空，否则将返回错误码。 |
| physicalAddress | 输出参数，二级指针指向物理地址。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceInfo或physicalAddress为null。

-

GAME_CONTROLLER_NO_MEMORY：设备内存不足。

#### OH_GameDevice_DeviceInfo_GetProduct()

```ets
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetProduct (const struct GameDevice_DeviceInfo *deviceInfo, int32_t *product)
```

**描述**

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002522242336__gamedevice_deviceinfo)中获取产品信息。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空，否则将返回错误码。 |
| product | 输出参数，产品信息。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceInfo为null。

#### OH_GameDevice_DeviceInfo_GetVersion()

```ets
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetVersion (const struct GameDevice_DeviceInfo *deviceInfo, int32_t *version)
```

**描述**

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002522242336__gamedevice_deviceinfo)中获取版本信息。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向GameDevice_DeviceInfo实例，不能为空，否则将返回错误码。 |
| version | 输出参数，版本信息。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceInfo为null。

#### OH_GameDevice_GetAllDeviceInfos()

```ets
GameController_ErrorCode OH_GameDevice_GetAllDeviceInfos (GameDevice_AllDeviceInfos **allDeviceInfos)
```

**描述**

获取所有在线设备的信息。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| allDeviceInfos | 输出参数。二级指针指向GameDevice_AllDeviceInfos实例，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_MULTIMODAL_INPUT_ERROR：查询多模输入中所有设备信息失败。

#### OH_GameDevice_RegisterDeviceMonitor()

```ets
GameController_ErrorCode OH_GameDevice_RegisterDeviceMonitor (GameDevice_DeviceMonitorCallback deviceMonitorCallback)
```

**描述**

注册设备状态变化事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceMonitorCallback | 回调函数GameDevice_DeviceMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceMonitorCallback为null。

#### OH_GameDevice_UnregisterDeviceMonitor()

```ets
GameController_ErrorCode OH_GameDevice_UnregisterDeviceMonitor (void)
```

**描述**

取消注册设备状态变化事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_AxisEvent_GetActionTime()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetActionTime (const struct GamePad_AxisEvent *axisEvent, int64_t *actionTime)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取动作时间。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| actionTime | 输出参数，动作时间。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetAxisSourceType()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetAxisSourceType (const struct GamePad_AxisEvent *axisEvent, GamePad_AxisSourceType *axisSourceType)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取轴事件来源类型。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| axisSourceType | 输出参数，轴事件来源类型GamePad_AxisSourceType。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetBrakeAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetBrakeAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取Brake轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetDeviceId()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetDeviceId (const struct GamePad_AxisEvent *axisEvent, char **deviceId)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取设备ID。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| deviceId | 输出参数，二级指针指向设备ID。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent或deviceId为null。

-

GAME_CONTROLLER_NO_MEMORY：设备内存不足。

#### OH_GamePad_AxisEvent_GetGasAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetGasAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取Gas轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetHatXAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetHatXAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取HatX轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetHatYAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetHatYAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取HatY轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetRZAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetRZAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取RZ轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetXAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetXAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取X轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetYAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetYAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取Y轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetZAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetZAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_axisevent)中获取Z轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向GamePad_AxisEvent实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_ButtonA_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonA_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册A按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_ButtonA_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonA_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册A按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_ButtonB_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonB_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册B按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 输出参数，回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_ButtonB_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonB_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册B按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_ButtonC_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonC_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册C按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 输出参数，回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_ButtonC_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonC_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册C按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_ButtonEvent_GetActionTime()

```ets
GameController_ErrorCode OH_GamePad_ButtonEvent_GetActionTime (const struct GamePad_ButtonEvent *buttonEvent, int64_t *actionTime)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_buttonevent)中获取按键动作的时间。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向GamePad_ButtonEvent实例，不能为空，否则将返回错误码。 |
| actionTime | 输出参数，按键动作的时间。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数buttonEvent为null。

#### OH_GamePad_ButtonEvent_GetButtonAction()

```ets
GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonAction (const struct GamePad_ButtonEvent *buttonEvent, GamePad_Button_ActionType *actionType)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_buttonevent)中获取按键动作类型。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向GamePad_ButtonEvent实例，不能为空，否则将返回错误码。 |
| actionType | 输出参数，按键动作类型。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数buttonEvent为null。

#### OH_GamePad_ButtonEvent_GetButtonCode()

```ets
GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonCode (const struct GamePad_ButtonEvent *buttonEvent, int32_t *code)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_buttonevent)中获取按键编码。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向GamePad_ButtonEvent实例，不能为空，否则将返回错误码。 |
| code | 输出参数，按键编码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数buttonEvent为null。

#### OH_GamePad_ButtonEvent_GetButtonCodeName()

```ets
GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonCodeName (const struct GamePad_ButtonEvent *buttonEvent, char **codeName)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_buttonevent)中获取按键的名称。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向GamePad_ButtonEvent实例，不能为空，否则将返回错误码。 |
| codeName | 输出参数，二级指针指向按键的名称。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数buttonEvent或codeName为null。

-

GAME_CONTROLLER_NO_MEMORY：设备内存不足。

#### OH_GamePad_ButtonEvent_GetDeviceId()

```ets
GameController_ErrorCode OH_GamePad_ButtonEvent_GetDeviceId (const struct GamePad_ButtonEvent *buttonEvent, char **deviceId)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_buttonevent)中获取设备ID。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向GamePad_ButtonEvent实例，不能为空，否则将返回错误码。 |
| deviceId | 输出参数，二级指针指向设备ID。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数buttonEvent或deviceId为null。

-

GAME_CONTROLLER_NO_MEMORY：设备内存不足。

#### OH_GamePad_ButtonHome_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonHome_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册Home按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_ButtonHome_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonHome_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册Home按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_ButtonMenu_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonMenu_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册Menu按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_ButtonMenu_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonMenu_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册Menu按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_ButtonX_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonX_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册X按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 输出参数，回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_ButtonX_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonX_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册X按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_ButtonY_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonY_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册Y按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 输出参数，回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_ButtonY_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_ButtonY_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册Y按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_DestroyPressedButton()

```ets
GameController_ErrorCode OH_GamePad_DestroyPressedButton (GamePad_PressedButton **pressedButton)
```

**描述**

当[GamePad_PressedButton](#ZH-CN_TOPIC_0000002522242336__gamepad_pressedbutton)实例不再使用， 销毁该实例。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| pressedButton | 二级指针指向GamePad_PressedButton实例，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数pressedButton为null。

#### OH_GamePad_Dpad_DownButton_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_Dpad_DownButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向下按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_Dpad_DownButton_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_Dpad_DownButton_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册方向按键的向下按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_Dpad_LeftButton_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_Dpad_LeftButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向左按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_Dpad_LeftButton_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_Dpad_LeftButton_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册方向按键的向左按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_Dpad_RegisterAxisInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_Dpad_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键轴事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_AxisInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_Dpad_RightButton_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_Dpad_RightButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向右按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_Dpad_RightButton_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_Dpad_RightButton_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册方向按键的向右按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_Dpad_UnregisterAxisInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_Dpad_UnregisterAxisInputMonitor (void)
```

**描述**

取消注册方向按键轴事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_Dpad_UpButton_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_Dpad_UpButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向上按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_Dpad_UpButton_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_Dpad_UpButton_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册方向按键的向上按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_LeftShoulder_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_LeftShoulder_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftShoulder按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册LeftShoulder按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftThumbstick轴事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_AxisInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_LeftThumbstick_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftThumbstick按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor (void)
```

**描述**

取消注册LeftThumbstick轴事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_LeftThumbstick_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册LeftThumbstick按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_LeftTrigger_RegisterAxisInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftTrigger轴事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_AxisInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_LeftTrigger_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftTrigger按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_LeftTrigger_UnregisterAxisInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterAxisInputMonitor (void)
```

**描述**

取消注册LeftTrigger轴事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_LeftTrigger_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册LeftTrigger按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_PressedButton_GetButtonCode()

```ets
GameController_ErrorCode OH_GamePad_PressedButton_GetButtonCode (const struct GamePad_PressedButton *pressedButton, int32_t *code)
```

**描述**

从按下的按键[GamePad_PressedButton](#ZH-CN_TOPIC_0000002522242336__gamepad_pressedbutton)中获取按键编码。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| pressedButton | 指针指向GamePad_PressedButton实例，不能为空，否则将返回错误码。 |
| code | 输出参数，按键编码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数pressedButton为null。

#### OH_GamePad_PressedButton_GetButtonCodeName()

```ets
GameController_ErrorCode OH_GamePad_PressedButton_GetButtonCodeName (const struct GamePad_PressedButton *pressedButton, char **codeName)
```

**描述**

从按下的按键[GamePad_PressedButton](#ZH-CN_TOPIC_0000002522242336__gamepad_pressedbutton)中获取按键的名称。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| pressedButton | 指针指向GamePad_PressedButton实例，不能为空，否则将返回错误码。 |
| codeName | 输出参数，二级指针指向按键的名称。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数pressedButton或codeName为null。

-

GAME_CONTROLLER_NO_MEMORY：设备内存不足。

#### OH_GamePad_PressedButtons_GetButtonInfo()

```ets
GameController_ErrorCode OH_GamePad_PressedButtons_GetButtonInfo (const struct GamePad_ButtonEvent *buttonEvent, const int32_t index, GamePad_PressedButton **pressedButton)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_buttonevent)中获取指定序号的按下的按键。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向GamePad_ButtonEvent实例，不能为空，否则将返回错误码。 |
| index | 指定按键序号。 |
| pressedButton | 输出参数，二级指针指向按下的键。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：buttonEvent为null或index小于0或index大于等于所有按键数。

#### OH_GamePad_PressedButtons_GetCount()

```ets
GameController_ErrorCode OH_GamePad_PressedButtons_GetCount (const struct GamePad_ButtonEvent *buttonEvent, int32_t *count)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002522242336__gamepad_buttonevent)中获取按下的按键数量。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向GamePad_ButtonEvent实例，不能为空，否则将返回错误码。 |
| count | 输出参数，按下的按键数量。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数buttonEvent为null。

#### OH_GamePad_RightShoulder_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_RightShoulder_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightShoulder按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_RightShoulder_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_RightShoulder_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册RightShoulder按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_RightThumbstick_RegisterAxisInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightThumbstick轴事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_AxisInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_RightThumbstick_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightThumbstick按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_RightThumbstick_UnregisterAxisInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterAxisInputMonitor (void)
```

**描述**

取消注册RightThumbstick轴事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_RightThumbstick_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册RightThumbstick按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_RightTrigger_RegisterAxisInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_RightTrigger_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightTrigger轴事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_AxisInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_RightTrigger_RegisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_RightTrigger_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightTrigger按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数GamePad_ButtonInputMonitorCallback，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002522242336__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数inputMonitorCallback为null。

#### OH_GamePad_RightTrigger_UnregisterAxisInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterAxisInputMonitor (void)
```

**描述**

取消注册RightTrigger轴事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。

#### OH_GamePad_RightTrigger_UnregisterButtonInputMonitor()

```ets
GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册RightTrigger按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME_CONTROLLER_SUCCESS。
