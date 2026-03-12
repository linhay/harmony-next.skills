# GameController

#### 概述

GameController模块提供游戏控制器功能的API接口。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

#### 汇总

#### 文件

名称描述[game_controller_type.h](game_controller_type.h.md)定义GameController模块的通用枚举类型。[game_device.h](game_device.h.md)定义游戏设备的接口。[game_device_event.h](game_device_event.h.md)定义游戏设备事件的接口。[game_pad.h](game_pad.h.md)定义游戏手柄的接口。[game_pad_event.h](game_pad_event.h.md)定义游戏手柄事件的接口。

#### 类型定义

名称描述typedef enum [GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)此枚举定义游戏控制器的错误码。typedef struct [GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos)[GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos)定义[OH_GameDevice_GetAllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_getalldeviceinfos)接口的调用结果。typedef enum [GameDevice_StatusChangedType](#ZH-CN_TOPIC_0000002529286079__gamedevice_statuschangedtype)[GameDevice_StatusChangedType](#ZH-CN_TOPIC_0000002529286079__gamedevice_statuschangedtype)此枚举定义设备的状态变化类型。typedef enum [GameDevice_DeviceType](#ZH-CN_TOPIC_0000002529286079__gamedevice_devicetype)[GameDevice_DeviceType](#ZH-CN_TOPIC_0000002529286079__gamedevice_devicetype)此枚举定义设备类型。typedef struct [GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)定义设备信息。typedef struct [GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent)[GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent)定义设备状态变化事件。typedef void(*[GameDevice_DeviceMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamedevice_devicemonitorcallback)) (const struct [GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent) *deviceEvent)定义[OH_GameDevice_RegisterDeviceMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_registerdevicemonitor)中使用的回调函数。当设备上线或下线时，该回调函数将被调用。typedef enum [GamePad_AxisSourceType](#ZH-CN_TOPIC_0000002529286079__gamepad_axissourcetype)[GamePad_AxisSourceType](#ZH-CN_TOPIC_0000002529286079__gamepad_axissourcetype)此枚举定义手柄轴事件来源类型。typedef enum [GamePad_Button_ActionType](#ZH-CN_TOPIC_0000002529286079__gamepad_button_actiontype)[GamePad_Button_ActionType](#ZH-CN_TOPIC_0000002529286079__gamepad_button_actiontype)此枚举定义手柄按键动作类型。typedef struct [GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)定义手柄按键事件。typedef struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)定义手柄轴事件。typedef struct [GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)[GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)定义手柄按下的按键。typedef void(*[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)) (const struct [GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent) *buttonEvent)定义在按键事件注册监听接口中使用的回调函数。当玩家按下按键时，该回调函数将被调用。typedef void(*[GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback)) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent)定义在轴事件注册监听接口中使用的回调函数。当玩家操作摇杆时，该回调函数将被调用。

#### 枚举

名称描述

[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode) {

GAME_CONTROLLER_SUCCESS = 0,

GAME_CONTROLLER_PARAM_ERROR = 401,

GAME_CONTROLLER_MULTIMODAL_INPUT_ERROR = 32200001,

GAME_CONTROLLER_NO_MEMORY = 32200002

}

游戏控制器错误码。

[GameDevice_StatusChangedType](#ZH-CN_TOPIC_0000002529286079__gamedevice_statuschangedtype) {

OFFLINE = 0,

ONLINE = 1

}

设备的状态变化类型。

[GameDevice_DeviceType](#ZH-CN_TOPIC_0000002529286079__gamedevice_devicetype) {

UNKNOWN = 0,

GAME_PAD = 1

}

设备类型。

[GamePad_AxisSourceType](#ZH-CN_TOPIC_0000002529286079__gamepad_axissourcetype) {

DPAD = 0,

LEFT_THUMBSTICK = 1,

RIGHT_THUMBSTICK = 2,

LEFT_TRIGGER = 3,

RIGHT_TRIGGER = 4

}

手柄轴事件来源类型。

[GamePad_Button_ActionType](#ZH-CN_TOPIC_0000002529286079__gamepad_button_actiontype) {

DOWN = 0,

UP = 1

}

手柄按键动作类型。

#### 函数

名称描述[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_GetAllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_getalldeviceinfos) ([GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos) **allDeviceInfos)获取所有在线设备的信息。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_RegisterDeviceMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_registerdevicemonitor) ([GameDevice_DeviceMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamedevice_devicemonitorcallback) deviceMonitorCallback)注册设备状态变化事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_UnregisterDeviceMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_unregisterdevicemonitor) (void)取消注册设备状态变化事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DestroyAllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_destroyalldeviceinfos) ([GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos) **allDeviceInfos)当[GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos)实例不再使用，销毁该实例。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_AllDeviceInfos_GetCount](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_alldeviceinfos_getcount) (const struct [GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos) *allDeviceInfos, int32_t *count)获取设备数量。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_AllDeviceInfos_GetDeviceInfo](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_alldeviceinfos_getdeviceinfo) (const struct [GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos) *allDeviceInfos, const int32_t index, [GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) **deviceInfo)从所有设备信息中获取指定序号的设备信息。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceEvent_GetChangedType](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceevent_getchangedtype) (const struct [GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent) *deviceEvent, [GameDevice_StatusChangedType](#ZH-CN_TOPIC_0000002529286079__gamedevice_statuschangedtype) *statusChangedType)从设备状态变化事件中获取状态变化类型。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceEvent_GetDeviceInfo](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceevent_getdeviceinfo) (const struct [GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent) *deviceEvent, [GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) **deviceInfo)从设备状态变化事件中获取设备信息。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DestroyDeviceInfo](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_destroydeviceinfo) ([GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) **deviceInfo)当[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)实例不再使用，销毁该实例。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetDeviceId](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getdeviceid) (const struct [GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, char **deviceId)从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取设备ID。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetName](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getname) (const struct [GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, char **name)从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取设备名称。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetProduct](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getproduct) (const struct [GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, int32_t *product)从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取产品信息。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetVersion](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getversion) (const struct [GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, int32_t *version)从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取版本信息。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetPhysicalAddress](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getphysicaladdress) (const struct [GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, char **physicalAddress)从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取物理地址。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GameDevice_DeviceInfo_GetDeviceType](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_deviceinfo_getdevicetype) (const struct [GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo) *deviceInfo, [GameDevice_DeviceType](#ZH-CN_TOPIC_0000002529286079__gamedevice_devicetype) *deviceType)从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取设备类型。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_LeftShoulder_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_leftshoulder_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册LeftShoulder按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_leftshoulder_unregisterbuttoninputmonitor) (void)取消注册LeftShoulder按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_RightShoulder_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_rightshoulder_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册RightShoulder按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_RightShoulder_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_rightshoulder_unregisterbuttoninputmonitor) (void)取消注册RightShoulder按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_LeftTrigger_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_lefttrigger_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册LeftTrigger按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_LeftTrigger_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_lefttrigger_unregisterbuttoninputmonitor) (void)取消注册LeftTrigger按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_LeftTrigger_RegisterAxisInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_lefttrigger_registeraxisinputmonitor) ([GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback) inputMonitorCallback)注册LeftTrigger轴事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_LeftTrigger_UnregisterAxisInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_lefttrigger_unregisteraxisinputmonitor) (void)取消注册LeftTrigger轴事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_RightTrigger_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_righttrigger_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册RightTrigger按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_RightTrigger_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_righttrigger_unregisterbuttoninputmonitor) (void)取消注册RightTrigger按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_RightTrigger_RegisterAxisInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_righttrigger_registeraxisinputmonitor) ([GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback) inputMonitorCallback)注册RightTrigger轴事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_RightTrigger_UnregisterAxisInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_righttrigger_unregisteraxisinputmonitor) (void)取消注册RightTrigger轴事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonMenu_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonmenu_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册Menu按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonMenu_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonmenu_unregisterbuttoninputmonitor) (void)取消注册Menu按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonHome_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonhome_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册Home按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonHome_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonhome_unregisterbuttoninputmonitor) (void)取消注册Home按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonA_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttona_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册A按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonA_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttona_unregisterbuttoninputmonitor) (void)取消注册A按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonB_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonb_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册B按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonB_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonb_unregisterbuttoninputmonitor) (void)取消注册B按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonX_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonx_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册X按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonX_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonx_unregisterbuttoninputmonitor) (void)取消注册X按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonY_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttony_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册Y按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonY_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttony_unregisterbuttoninputmonitor) (void)取消注册Y按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonC_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonc_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册C按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonC_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonc_unregisterbuttoninputmonitor) (void)取消注册C按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_Dpad_LeftButton_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_dpad_leftbutton_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册方向按键的向左按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_Dpad_LeftButton_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_dpad_leftbutton_unregisterbuttoninputmonitor) (void)取消注册方向按键的向左按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_Dpad_RightButton_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_dpad_rightbutton_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册方向按键的向右按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_Dpad_RightButton_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_dpad_rightbutton_unregisterbuttoninputmonitor) (void)取消注册方向按键的向右按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_Dpad_UpButton_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_dpad_upbutton_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册方向按键的向上按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_Dpad_UpButton_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_dpad_upbutton_unregisterbuttoninputmonitor) (void)取消注册方向按键的向上按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_Dpad_DownButton_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_dpad_downbutton_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册方向按键的向下按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_Dpad_DownButton_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_dpad_downbutton_unregisterbuttoninputmonitor) (void)取消注册方向按键的向下按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_Dpad_RegisterAxisInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_dpad_registeraxisinputmonitor) ([GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback) inputMonitorCallback)注册方向按键轴事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_Dpad_UnregisterAxisInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_dpad_unregisteraxisinputmonitor) (void)取消注册方向按键轴事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_LeftThumbstick_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_leftthumbstick_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册LeftThumbstick按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_LeftThumbstick_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_leftthumbstick_unregisterbuttoninputmonitor) (void)取消注册LeftThumbstick按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_leftthumbstick_registeraxisinputmonitor) ([GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback) inputMonitorCallback)注册LeftThumbstick轴事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_leftthumbstick_unregisteraxisinputmonitor) (void)取消注册LeftThumbstick轴事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_RightThumbstick_RegisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_rightthumbstick_registerbuttoninputmonitor) ([GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback) inputMonitorCallback)注册RightThumbstick按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_RightThumbstick_UnregisterButtonInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_rightthumbstick_unregisterbuttoninputmonitor) (void)取消注册RightThumbstick按键事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_RightThumbstick_RegisterAxisInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_rightthumbstick_registeraxisinputmonitor) ([GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback) inputMonitorCallback)注册RightThumbstick轴事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_RightThumbstick_UnregisterAxisInputMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_rightthumbstick_unregisteraxisinputmonitor) (void)取消注册RightThumbstick轴事件的监听回调。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonEvent_GetDeviceId](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonevent_getdeviceid) (const struct [GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent) *buttonEvent, char **deviceId)从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取设备ID。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonEvent_GetButtonAction](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonevent_getbuttonaction) (const struct [GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent) *buttonEvent, [GamePad_Button_ActionType](#ZH-CN_TOPIC_0000002529286079__gamepad_button_actiontype) *actionType)从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取按键动作类型。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonEvent_GetButtonCode](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonevent_getbuttoncode) (const struct [GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent) *buttonEvent, int32_t *code)从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取按键编码。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonEvent_GetButtonCodeName](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonevent_getbuttoncodename) (const struct [GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent) *buttonEvent, char **codeName)从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取按键的名称。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_PressedButtons_GetCount](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_pressedbuttons_getcount) (const struct [GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent) *buttonEvent, int32_t *count)从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取按下的按键数量。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_PressedButtons_GetButtonInfo](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_pressedbuttons_getbuttoninfo) (const struct [GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent) *buttonEvent, const int32_t index, [GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton) **pressedButton)从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取指定序号的按下的按键。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_DestroyPressedButton](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_destroypressedbutton) ([GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton) **pressedButton)当[GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)实例不再使用， 销毁该实例。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_PressedButton_GetButtonCode](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_pressedbutton_getbuttoncode) (const struct [GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton) *pressedButton, int32_t *code)从按下的按键[GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)中获取按键编码。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_PressedButton_GetButtonCodeName](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_pressedbutton_getbuttoncodename) (const struct [GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton) *pressedButton, char **codeName)从按下的按键[GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)中获取按键的名称。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_ButtonEvent_GetActionTime](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_buttonevent_getactiontime) (const struct [GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent) *buttonEvent, int64_t *actionTime)从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取按键动作的时间。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetDeviceId](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_getdeviceid) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, char **deviceId)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取设备ID。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetAxisSourceType](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_getaxissourcetype) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, [GamePad_AxisSourceType](#ZH-CN_TOPIC_0000002529286079__gamepad_axissourcetype) *axisSourceType)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取轴事件来源类型。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetXAxisValue](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_getxaxisvalue) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, double *axisValue)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取X轴的轴值。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetYAxisValue](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_getyaxisvalue) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, double *axisValue)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取Y轴的轴值。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetZAxisValue](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_getzaxisvalue) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, double *axisValue)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取Z轴的轴值。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetRZAxisValue](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_getrzaxisvalue) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, double *axisValue)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取RZ轴的轴值。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetHatXAxisValue](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_gethatxaxisvalue) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, double *axisValue)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取HatX轴的轴值。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetHatYAxisValue](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_gethatyaxisvalue) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, double *axisValue)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取HatY轴的轴值。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetBrakeAxisValue](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_getbrakeaxisvalue) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, double *axisValue)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取Brake轴的轴值。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetGasAxisValue](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_getgasaxisvalue) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, double *axisValue)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取Gas轴的轴值。[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)[OH_GamePad_AxisEvent_GetActionTime](#ZH-CN_TOPIC_0000002529286079__oh_gamepad_axisevent_getactiontime) (const struct [GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent) *axisEvent, int64_t *actionTime)从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取动作时间。

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

定义[OH_GameDevice_GetAllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_getalldeviceinfos)接口的调用结果。

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

定义[OH_GameDevice_RegisterDeviceMonitor](#ZH-CN_TOPIC_0000002529286079__oh_gamedevice_registerdevicemonitor)中使用的回调函数。当设备上线或下线时，该回调函数将被调用。

**起始版本：** 21

**参数:**

名称描述deviceEvent输出参数。设备状态变化事件[GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent)。

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

名称描述axisEvent输出参数，手柄轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)。

#### GamePad_AxisSourceType

```ets
typedef enum GamePad_AxisSourceType
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

名称描述buttonEvent输出参数，手柄按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)。

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

枚举值描述GAME_CONTROLLER_SUCCESS成功。GAME_CONTROLLER_PARAM_ERROR参数非法。GAME_CONTROLLER_MULTIMODAL_INPUT_ERROR查询多模输入中所有设备信息失败。GAME_CONTROLLER_NO_MEMORY设备内存不足。

#### GameDevice_DeviceType

```ets
enum GameDevice_DeviceType
```

**描述**

此枚举定义设备类型。

**起始版本：** 21

枚举值描述UNKNOWN未知。GAME_PAD游戏手柄。

#### GameDevice_StatusChangedType

```ets
enum GameDevice_StatusChangedType
```

**描述**

此枚举定义设备的状态变化类型。

**起始版本：** 21

枚举值描述OFFLINE设备下线。ONLINE设备上线。

#### GamePad_AxisSourceType

```ets
enum GamePad_AxisSourceType
```

**描述**

此枚举定义手柄轴事件来源类型。

**起始版本：** 21

枚举值描述DPAD轴事件来源于方向按键DPAD。LEFT_THUMBSTICK轴事件来源于LeftThumbstick。RIGHT_THUMBSTICK轴事件来源于RightThumbstick。LEFT_TRIGGER轴事件来源于LeftTrigger。RIGHT_TRIGGER轴事件来源于RightTrigger。

#### GamePad_Button_ActionType

```ets
enum GamePad_Button_ActionType
```

**描述**

此枚举定义手柄按键动作类型。

**起始版本：** 21

枚举值描述DOWN按键按下。UP按键抬起。

#### 函数说明

#### OH_GameDevice_AllDeviceInfos_GetCount()

```ets
GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetCount (const struct GameDevice_AllDeviceInfos *allDeviceInfos, int32_t *count)
```

**描述**

获取设备数量。

**起始版本：** 21

**参数:**

名称描述allDeviceInfos指针指向[GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos)实例，不能为空，否则将返回错误码。count输出参数，设备数量。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述allDeviceInfos指针指向[GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos)实例，不能为空，否则将返回错误码。index指定查询的设备序号。deviceInfo输出参数，二级指针指向[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)设备信息实例。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：allDeviceInfos为null或者index小于0或者index大于等于所有设备数。

#### OH_GameDevice_DestroyAllDeviceInfos()

```ets
GameController_ErrorCode OH_GameDevice_DestroyAllDeviceInfos (GameDevice_AllDeviceInfos **allDeviceInfos)
```

**描述**

当[GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos)实例不再使用，销毁该实例。

**起始版本：** 21

**参数:**

名称描述allDeviceInfos二级指针指向[GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos)实例，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数allDeviceInfos为null。

#### OH_GameDevice_DestroyDeviceInfo()

```ets
GameController_ErrorCode OH_GameDevice_DestroyDeviceInfo (GameDevice_DeviceInfo **deviceInfo)
```

**描述**

当[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)实例不再使用，销毁该实例。

**起始版本：** 21

**参数:**

名称描述deviceInfo二级指针指向[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceInfo为null。

#### OH_GameDevice_DeviceEvent_GetChangedType()

```ets
GameController_ErrorCode OH_GameDevice_DeviceEvent_GetChangedType (const struct GameDevice_DeviceEvent *deviceEvent, GameDevice_StatusChangedType *statusChangedType)
```

**描述**

从设备状态变化事件[GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent)中获取状态变化类型。

**起始版本：** 21

**参数:**

名称描述deviceEvent指针指向[GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent)实例，不能为空，否则将返回错误码。statusChangedType输出参数，设备状态变化类型。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceEvent为null。

#### OH_GameDevice_DeviceEvent_GetDeviceInfo()

```ets
GameController_ErrorCode OH_GameDevice_DeviceEvent_GetDeviceInfo (const struct GameDevice_DeviceEvent *deviceEvent, GameDevice_DeviceInfo **deviceInfo)
```

**描述**

从设备状态变化事件[GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent)中获取设备信息。

**起始版本：** 21

**参数:**

名称描述deviceEvent指针指向[GameDevice_DeviceEvent](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceevent)实例，不能为空，否则将返回错误码。deviceInfo输出参数，二级指针指向[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)设备信息实例。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceEvent为null。

#### OH_GameDevice_DeviceInfo_GetDeviceId()

```ets
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceId (const struct GameDevice_DeviceInfo *deviceInfo, char **deviceId)
```

**描述**

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取设备ID。

**起始版本：** 21

**参数:**

名称描述deviceInfo指针指向[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。deviceId输出参数，二级指针指向设备ID。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取设备类型。

**起始版本：** 21

**参数:**

名称描述deviceInfo指针指向[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。deviceType输出参数，设备类型。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceInfo为null。

#### OH_GameDevice_DeviceInfo_GetName()

```ets
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetName (const struct GameDevice_DeviceInfo *deviceInfo, char **name)
```

**描述**

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取设备名称。

**起始版本：** 21

**参数:**

名称描述deviceInfo指针指向[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。name输出参数，二级指针指向设备名称。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取物理地址。

**起始版本：** 21

**参数:**

名称描述deviceInfo指针指向[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。physicalAddress输出参数，二级指针指向物理地址。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取产品信息。

**起始版本：** 21

**参数:**

名称描述deviceInfo指针指向[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。product输出参数，产品信息。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数deviceInfo为null。

#### OH_GameDevice_DeviceInfo_GetVersion()

```ets
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetVersion (const struct GameDevice_DeviceInfo *deviceInfo, int32_t *version)
```

**描述**

从设备信息[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)中获取版本信息。

**起始版本：** 21

**参数:**

名称描述deviceInfo指针指向[GameDevice_DeviceInfo](#ZH-CN_TOPIC_0000002529286079__gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。version输出参数，版本信息。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述allDeviceInfos输出参数。二级指针指向[GameDevice_AllDeviceInfos](#ZH-CN_TOPIC_0000002529286079__gamedevice_alldeviceinfos)实例，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述deviceMonitorCallback回调函数[GameDevice_DeviceMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamedevice_devicemonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取动作时间。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。actionTime输出参数，动作时间。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetAxisSourceType()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetAxisSourceType (const struct GamePad_AxisEvent *axisEvent, GamePad_AxisSourceType *axisSourceType)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取轴事件来源类型。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。axisSourceType输出参数，轴事件来源类型[GamePad_AxisSourceType](#ZH-CN_TOPIC_0000002529286079__gamepad_axissourcetype)。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetBrakeAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetBrakeAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取Brake轴的轴值。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。axisValue输出参数，轴值。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetDeviceId()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetDeviceId (const struct GamePad_AxisEvent *axisEvent, char **deviceId)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取设备ID。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。deviceId输出参数，二级指针指向设备ID。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取Gas轴的轴值。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。axisValue输出参数，轴值。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetHatXAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetHatXAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取HatX轴的轴值。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。axisValue输出参数，轴值。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetHatYAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetHatYAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取HatY轴的轴值。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。axisValue输出参数，轴值。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetRZAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetRZAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取RZ轴的轴值。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。axisValue输出参数，轴值。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetXAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetXAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取X轴的轴值。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。axisValue输出参数，轴值。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetYAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetYAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取Y轴的轴值。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。axisValue输出参数，轴值。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数axisEvent为null。

#### OH_GamePad_AxisEvent_GetZAxisValue()

```ets
GameController_ErrorCode OH_GamePad_AxisEvent_GetZAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)中获取Z轴的轴值。

**起始版本：** 21

**参数:**

名称描述axisEvent指针指向[GamePad_AxisEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_axisevent)实例，不能为空，否则将返回错误码。axisValue输出参数，轴值。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback输出参数，回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback输出参数，回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取按键动作的时间。

**起始版本：** 21

**参数:**

名称描述buttonEvent指针指向[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)实例，不能为空，否则将返回错误码。actionTime输出参数，按键动作的时间。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数buttonEvent为null。

#### OH_GamePad_ButtonEvent_GetButtonAction()

```ets
GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonAction (const struct GamePad_ButtonEvent *buttonEvent, GamePad_Button_ActionType *actionType)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取按键动作类型。

**起始版本：** 21

**参数:**

名称描述buttonEvent指针指向[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)实例，不能为空，否则将返回错误码。actionType输出参数，按键动作类型。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数buttonEvent为null。

#### OH_GamePad_ButtonEvent_GetButtonCode()

```ets
GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonCode (const struct GamePad_ButtonEvent *buttonEvent, int32_t *code)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取按键编码。

**起始版本：** 21

**参数:**

名称描述buttonEvent指针指向[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)实例，不能为空，否则将返回错误码。code输出参数，按键编码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数buttonEvent为null。

#### OH_GamePad_ButtonEvent_GetButtonCodeName()

```ets
GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonCodeName (const struct GamePad_ButtonEvent *buttonEvent, char **codeName)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取按键的名称。

**起始版本：** 21

**参数:**

名称描述buttonEvent指针指向[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)实例，不能为空，否则将返回错误码。codeName输出参数，二级指针指向按键的名称。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取设备ID。

**起始版本：** 21

**参数:**

名称描述buttonEvent指针指向[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)实例，不能为空，否则将返回错误码。deviceId输出参数，二级指针指向设备ID。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback输出参数，回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback输出参数，回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

当[GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)实例不再使用， 销毁该实例。

**起始版本：** 21

**参数:**

名称描述pressedButton二级指针指向[GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)实例，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

从按下的按键[GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)中获取按键编码。

**起始版本：** 21

**参数:**

名称描述pressedButton指针指向[GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)实例，不能为空，否则将返回错误码。code输出参数，按键编码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：参数pressedButton为null。

#### OH_GamePad_PressedButton_GetButtonCodeName()

```ets
GameController_ErrorCode OH_GamePad_PressedButton_GetButtonCodeName (const struct GamePad_PressedButton *pressedButton, char **codeName)
```

**描述**

从按下的按键[GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)中获取按键的名称。

**起始版本：** 21

**参数:**

名称描述pressedButton指针指向[GamePad_PressedButton](#ZH-CN_TOPIC_0000002529286079__gamepad_pressedbutton)实例，不能为空，否则将返回错误码。codeName输出参数，二级指针指向按键的名称。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取指定序号的按下的按键。

**起始版本：** 21

**参数:**

名称描述buttonEvent指针指向[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)实例，不能为空，否则将返回错误码。index指定按键序号。pressedButton输出参数，二级指针指向按下的键。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

-

GAME_CONTROLLER_SUCCESS：成功。

-

GAME_CONTROLLER_PARAM_ERROR：buttonEvent为null或index小于0或index大于等于所有按键数。

#### OH_GamePad_PressedButtons_GetCount()

```ets
GameController_ErrorCode OH_GamePad_PressedButtons_GetCount (const struct GamePad_ButtonEvent *buttonEvent, int32_t *count)
```

**描述**

从按键事件[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)中获取按下的按键数量。

**起始版本：** 21

**参数:**

名称描述buttonEvent指针指向[GamePad_ButtonEvent](#ZH-CN_TOPIC_0000002529286079__gamepad_buttonevent)实例，不能为空，否则将返回错误码。count输出参数，按下的按键数量。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_AxisInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_axisinputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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

名称描述inputMonitorCallback回调函数[GamePad_ButtonInputMonitorCallback](#ZH-CN_TOPIC_0000002529286079__gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。

**返回：**

函数的执行结果，错误码[GameController_ErrorCode](#ZH-CN_TOPIC_0000002529286079__gamecontroller_errorcode)：

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