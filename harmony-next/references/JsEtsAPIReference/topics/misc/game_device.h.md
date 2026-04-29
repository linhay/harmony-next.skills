# game_device.h

**概述**

定义游戏设备的接口。

库： libohgame_controller.z.so

系统能力： SystemCapability.Game.GameController

起始版本： 21

相关模块：[GameController](GameController.md)

**汇总**

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct GameDevice_AllDeviceInfos GameDevice_AllDeviceInfos | 定义OH_GameDevice_GetAllDeviceInfos接口的调用结果。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| GameController_ErrorCode OH_GameDevice_GetAllDeviceInfos (GameDevice_AllDeviceInfos **allDeviceInfos) | 获取所有在线设备的信息。 |
| GameController_ErrorCode OH_GameDevice_RegisterDeviceMonitor (GameDevice_DeviceMonitorCallback deviceMonitorCallback) | 注册设备状态变化事件的监听回调。 |
| GameController_ErrorCode OH_GameDevice_UnregisterDeviceMonitor (void) | 取消注册设备状态变化事件的监听回调。 |
| GameController_ErrorCode OH_GameDevice_DestroyAllDeviceInfos (GameDevice_AllDeviceInfos **allDeviceInfos) | 当GameDevice_AllDeviceInfos实例不再使用，销毁该实例。 |
| GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetCount (const struct GameDevice_AllDeviceInfos *allDeviceInfos, int32_t *count) | 获取设备数量。 |
| GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetDeviceInfo (const struct GameDevice_AllDeviceInfos *allDeviceInfos, const int32_t index, GameDevice_DeviceInfo **deviceInfo) | 从所有设备信息中获取指定序号的设备信息。 |