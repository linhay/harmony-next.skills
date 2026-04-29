# game_pad.h

**概述**

定义游戏手柄的接口。

库： libohgame_controller.z.so

系统能力： SystemCapability.Game.GameController

起始版本： 21

相关模块：[GameController](GameController.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
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