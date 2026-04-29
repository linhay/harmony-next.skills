# game_device_event.h

**概述**

定义游戏设备事件的接口。

库： libohgame_controller.z.so

系统能力： SystemCapability.Game.GameController

起始版本： 21

相关模块：[GameController](GameController.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef enum GameDevice_StatusChangedType GameDevice_StatusChangedType | 此枚举定义设备的状态变化类型。 |
| typedef enum GameDevice_DeviceType GameDevice_DeviceType | 此枚举定义设备类型。 |
| typedef struct GameDevice_DeviceInfo GameDevice_DeviceInfo | 定义设备信息。 |
| typedef struct GameDevice_DeviceEvent GameDevice_DeviceEvent | 定义设备状态变化事件。 |
| typedef void(*GameDevice_DeviceMonitorCallback) (const struct GameDevice_DeviceEvent *deviceEvent) | 定义OH_GameDevice_RegisterDeviceMonitor中使用的回调函数。当设备上线或下线时，该回调函数将被调用。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| GameDevice_StatusChangedType { OFFLINE = 0, ONLINE = 1 } | 设备的状态变化类型。 |
| GameDevice_DeviceType { UNKNOWN = 0, GAME_PAD = 1 } | 设备类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| GameController_ErrorCode OH_GameDevice_DeviceEvent_GetChangedType (const struct GameDevice_DeviceEvent *deviceEvent, GameDevice_StatusChangedType *statusChangedType) | 从设备状态变化事件中获取状态变化类型。 |
| GameController_ErrorCode OH_GameDevice_DeviceEvent_GetDeviceInfo (const struct GameDevice_DeviceEvent *deviceEvent, GameDevice_DeviceInfo **deviceInfo) | 从设备状态变化事件中获取设备信息。 |
| GameController_ErrorCode OH_GameDevice_DestroyDeviceInfo (GameDevice_DeviceInfo **deviceInfo) | 当GameDevice_DeviceInfo实例不再使用，销毁该实例。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceId (const struct GameDevice_DeviceInfo *deviceInfo, char **deviceId) | 从设备信息GameDevice_DeviceInfo中获取设备ID。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetName (const struct GameDevice_DeviceInfo *deviceInfo, char **name) | 从设备信息GameDevice_DeviceInfo中获取设备名称。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetProduct (const struct GameDevice_DeviceInfo *deviceInfo, int32_t *product) | 从设备信息GameDevice_DeviceInfo中获取产品信息。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetVersion (const struct GameDevice_DeviceInfo *deviceInfo, int32_t *version) | 从设备信息GameDevice_DeviceInfo中获取版本信息。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetPhysicalAddress (const struct GameDevice_DeviceInfo *deviceInfo, char **physicalAddress) | 从设备信息GameDevice_DeviceInfo中获取物理地址。 |
| GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceType (const struct GameDevice_DeviceInfo *deviceInfo, GameDevice_DeviceType *deviceType) | 从设备信息GameDevice_DeviceInfo中获取设备类型。 |