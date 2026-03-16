# game_device_event.h

#### 概述

定义游戏设备事件的接口。

**库：** libohgame_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：**[GameController](../../topics/misc/GameController.md)

#### 汇总

#### 类型定义

名称描述typedef enum [GameDevice_StatusChangedType](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_statuschangedtype)[GameDevice_StatusChangedType](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_statuschangedtype)此枚举定义设备的状态变化类型。typedef enum [GameDevice_DeviceType](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_devicetype)[GameDevice_DeviceType](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_devicetype)此枚举定义设备类型。typedef struct [GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)[GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)定义设备信息。typedef struct [GameDevice_DeviceEvent](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent)[GameDevice_DeviceEvent](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent)定义设备状态变化事件。typedef void(*[GameDevice_DeviceMonitorCallback](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_devicemonitorcallback)) (const struct [GameDevice_DeviceEvent](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent) *deviceEvent)定义[OH_GameDevice_RegisterDeviceMonitor](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_registerdevicemonitor)中使用的回调函数。当设备上线或下线时，该回调函数将被调用。

#### 枚举

名称描述

[GameDevice_StatusChangedType](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_statuschangedtype) {

OFFLINE = 0,

ONLINE = 1

}

设备的状态变化类型。

[GameDevice_DeviceType](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_devicetype) {

UNKNOWN = 0,

GAME_PAD = 1

}

设备类型。

#### 函数

名称描述[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceEvent_GetChangedType](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceevent_getchangedtype) (const struct [GameDevice_DeviceEvent](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent) *deviceEvent, [GameDevice_StatusChangedType](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_statuschangedtype) *statusChangedType)从设备状态变化事件中获取状态变化类型。[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceEvent_GetDeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceevent_getdeviceinfo) (const struct [GameDevice_DeviceEvent](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent) *deviceEvent, [GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) **deviceInfo)从设备状态变化事件中获取设备信息。[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DestroyDeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_destroydeviceinfo) ([GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) **deviceInfo)当[GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)实例不再使用，销毁该实例。[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetDeviceId](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getdeviceid) (const struct [GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, char **deviceId)从设备信息[GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取设备ID。[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetName](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getname) (const struct [GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, char **name)从设备信息[GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取设备名称。[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetProduct](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getproduct) (const struct [GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, int32_t *product)从设备信息[GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取产品信息。[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetVersion](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getversion) (const struct [GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, int32_t *version)从设备信息[GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取版本信息。[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetPhysicalAddress](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getphysicaladdress) (const struct [GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, char **physicalAddress)从设备信息[GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取物理地址。[GameController_ErrorCode](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetDeviceType](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getdevicetype) (const struct [GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, [GameDevice_DeviceType](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_devicetype) *deviceType)从设备信息[GameDevice_DeviceInfo](../../topics/misc/GameController.md#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取设备类型。