# oh_input_manager.h

#### 概述

提供事件注入和关键状态查询等功能。

**引用文件：** <multimodalinput/oh_input_manager.h>

**库：** libohinput.so

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**相关模块：**[input](../../topics/input/input.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Input_InterceptorEventCallback](../../topics/input/Input_InterceptorEventCallback.md)Input_InterceptorEventCallback拦截回调事件结构体，拦截鼠标事件、触屏输入事件和轴事件。[Input_DeviceListener](../../topics/components/Input_DeviceListener.md)Input_DeviceListener定义一个结构体用于监听设备热插拔。[Input_KeyState](../../topics/input/Input_KeyState.md)Input_KeyState定义按键信息，用于标识按键行为。例如，“Ctrl”按键信息包含键值和键类型。[Input_KeyEvent](../../topics/input/Input_KeyEvent.md)Input_KeyEvent按键事件对象。[Input_MouseEvent](../../topics/input/Input_MouseEvent.md)Input_MouseEvent鼠标事件对象。[Input_TouchEvent](../../topics/input/Input_TouchEvent.md)Input_TouchEvent触屏输入事件对象。[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)Input_AxisEvent轴事件对象。[Input_Hotkey](../../topics/input/Input_Hotkey.md)Input_Hotkey定义快捷键结构体。[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md)Input_DeviceInfo输入设备信息。[Input_InterceptorOptions](../../topics/input/Input_InterceptorOptions.md)Input_InterceptorOptions事件拦截选项。[Input_CustomCursor](../../topics/input/Input_CustomCursor.md)Input_CustomCursor自定义鼠标光标像素图资源。[Input_CursorConfig](../../topics/input/Input_CursorConfig.md)Input_CursorConfig自定义鼠标光标配置。[Input_CursorInfo](../../topics/input/Input_CursorInfo.md)Input_CursorInfo定义鼠标光标信息。

#### 枚举

名称typedef关键字描述[Input_KeyStateAction](#ZH-CN_TOPIC_0000002529445539__input_keystateaction)Input_KeyStateAction按键状态的枚举值。[Input_KeyEventAction](#ZH-CN_TOPIC_0000002529445539__input_keyeventaction)Input_KeyEventAction按键事件类型的枚举值。[Input_MouseEventAction](#ZH-CN_TOPIC_0000002529445539__input_mouseeventaction)Input_MouseEventAction鼠标动作的枚举值。[InputEvent_MouseAxis](#ZH-CN_TOPIC_0000002529445539__inputevent_mouseaxis)InputEvent_MouseAxis鼠标轴事件类型。[Input_MouseEventButton](#ZH-CN_TOPIC_0000002529445539__input_mouseeventbutton)Input_MouseEventButton鼠标按键的枚举值。[Input_TouchEventAction](#ZH-CN_TOPIC_0000002529445539__input_toucheventaction)Input_TouchEventAction触屏动作的枚举值。[Input_InjectionStatus](#ZH-CN_TOPIC_0000002529445539__input_injectionstatus)Input_InjectionStatus注入权限状态枚举值。[InputEvent_SourceType](#ZH-CN_TOPIC_0000002529445539__inputevent_sourcetype)InputEvent_SourceType输入事件源类型。[Input_KeyboardType](#ZH-CN_TOPIC_0000002529445539__input_keyboardtype)Input_KeyboardType输入设备的键盘类型。[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)Input_Result错误码枚举值。

#### 函数

名称typedef关键字描述[typedef void (*Input_HotkeyCallback)(Input_Hotkey* hotkey)](#ZH-CN_TOPIC_0000002529445539__input_hotkeycallback)Input_HotkeyCallback回调函数，用于回调快捷键事件。[typedef void (*Input_KeyEventCallback)(const Input_KeyEvent* keyEvent)](#ZH-CN_TOPIC_0000002529445539__input_keyeventcallback)Input_KeyEventCallback按键事件的回调函数，keyEvent的生命周期为回调函数内。[typedef void (*Input_MouseEventCallback)(const Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__input_mouseeventcallback)Input_MouseEventCallback鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。[typedef void (*Input_TouchEventCallback)(const Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__input_toucheventcallback)Input_TouchEventCallback触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。[typedef void (*Input_AxisEventCallback)(const Input_AxisEvent* axisEvent)](#ZH-CN_TOPIC_0000002529445539__input_axiseventcallback)Input_AxisEventCallback轴事件的回调函数，axisEvent的生命周期为回调函数内。[typedef void (*Input_DeviceAddedCallback)(int32_t deviceId)](#ZH-CN_TOPIC_0000002529445539__input_deviceaddedcallback)Input_DeviceAddedCallback回调函数，用于回调输入设备的热插事件。[typedef void (*Input_DeviceRemovedCallback)(int32_t deviceId)](#ZH-CN_TOPIC_0000002529445539__input_deviceremovedcallback)Input_DeviceRemovedCallback回调函数，用于回调输入设备的热拔事件。[typedef void (*Input_InjectAuthorizeCallback)(Input_InjectionStatus authorizedStatus)](#ZH-CN_TOPIC_0000002529445539__input_injectauthorizecallback)Input_InjectAuthorizeCallback回调函数，用于获取注入权限状态。[Input_Result OH_Input_GetKeyState(struct Input_KeyState* keyState)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeystate)-查询按键状态的枚举对象。[struct Input_KeyState* OH_Input_CreateKeyState()](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeystate)-创建按键状态的枚举对象。[void OH_Input_DestroyKeyState(struct Input_KeyState** keyState)](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeystate)-销毁按键状态的枚举对象。[void OH_Input_SetKeyCode(struct Input_KeyState* keyState, int32_t keyCode)](#ZH-CN_TOPIC_0000002529445539__oh_input_setkeycode)-设置按键状态对象的键值。[int32_t OH_Input_GetKeyCode(const struct Input_KeyState* keyState)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeycode)-获取按键状态对象的键值。[void OH_Input_SetKeyPressed(struct Input_KeyState* keyState, int32_t keyAction)](#ZH-CN_TOPIC_0000002529445539__oh_input_setkeypressed)-设置按键状态对象的按键是否按下。[int32_t OH_Input_GetKeyPressed(const struct Input_KeyState* keyState)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeypressed)-获取按键状态对象的按键是否按下。[void OH_Input_SetKeySwitch(struct Input_KeyState* keyState, int32_t keySwitch)](#ZH-CN_TOPIC_0000002529445539__oh_input_setkeyswitch)-设置按键状态对象的按键开关。[int32_t OH_Input_GetKeySwitch(const struct Input_KeyState* keyState)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeyswitch)-获取按键状态对象的按键开关。[int32_t OH_Input_InjectKeyEvent(const struct Input_KeyEvent* keyEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_injectkeyevent)-注入按键事件。[struct Input_KeyEvent* OH_Input_CreateKeyEvent()](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)-创建按键事件对象。[void OH_Input_DestroyKeyEvent(struct Input_KeyEvent** keyEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)-销毁按键事件对象。[void OH_Input_SetKeyEventAction(struct Input_KeyEvent* keyEvent, int32_t action)](#ZH-CN_TOPIC_0000002529445539__oh_input_setkeyeventaction)-设置按键事件类型。[int32_t OH_Input_GetKeyEventAction(const struct Input_KeyEvent* keyEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeyeventaction)-获取按键事件类型。[void OH_Input_SetKeyEventKeyCode(struct Input_KeyEvent* keyEvent, int32_t keyCode)](#ZH-CN_TOPIC_0000002529445539__oh_input_setkeyeventkeycode)-设置按键事件的键值。[int32_t OH_Input_GetKeyEventKeyCode(const struct Input_KeyEvent* keyEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeyeventkeycode)-获取按键事件的键值。[void OH_Input_SetKeyEventActionTime(struct Input_KeyEvent* keyEvent, int64_t actionTime)](#ZH-CN_TOPIC_0000002529445539__oh_input_setkeyeventactiontime)-设置按键事件发生的时间。[int64_t OH_Input_GetKeyEventActionTime(const struct Input_KeyEvent* keyEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeyeventactiontime)-获取按键事件发生的时间。[void OH_Input_SetKeyEventWindowId(struct Input_KeyEvent* keyEvent, int32_t windowId)](#ZH-CN_TOPIC_0000002529445539__oh_input_setkeyeventwindowid)-设置按键事件的窗口ID。[int32_t OH_Input_GetKeyEventWindowId(const struct Input_KeyEvent* keyEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeyeventwindowid)-获取按键事件的窗口ID。[void OH_Input_SetKeyEventDisplayId(struct Input_KeyEvent* keyEvent, int32_t displayId)](#ZH-CN_TOPIC_0000002529445539__oh_input_setkeyeventdisplayid)-设置按键事件的屏幕ID。[int32_t OH_Input_GetKeyEventDisplayId(const struct Input_KeyEvent* keyEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeyeventdisplayid)-获取按键事件的屏幕ID。[struct Input_MouseEvent* OH_Input_CreateMouseEvent()](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)-创建鼠标事件对象。[void OH_Input_DestroyMouseEvent(struct Input_MouseEvent** mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)-销毁鼠标事件对象。[void OH_Input_SetMouseEventAction(struct Input_MouseEvent* mouseEvent, int32_t action)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventaction)-设置鼠标事件的动作。[int32_t OH_Input_GetMouseEventAction(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventaction)-获取鼠标事件的动作。[void OH_Input_SetMouseEventDisplayX(struct Input_MouseEvent* mouseEvent, int32_t displayX)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventdisplayx)-设置鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。[int32_t OH_Input_GetMouseEventDisplayX(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventdisplayx)-获取鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。[void OH_Input_SetMouseEventDisplayY(struct Input_MouseEvent* mouseEvent, int32_t displayY)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventdisplayy)-设置鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。[int32_t OH_Input_GetMouseEventDisplayY(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventdisplayy)-获取鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。[void OH_Input_SetMouseEventButton(struct Input_MouseEvent* mouseEvent, int32_t button)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventbutton)-设置鼠标事件的按键。[int32_t OH_Input_GetMouseEventButton(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventbutton)-获取鼠标事件的按键。[void OH_Input_SetMouseEventAxisType(struct Input_MouseEvent* mouseEvent, int32_t axisType)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventaxistype)-设置鼠标轴事件的类型。[int32_t OH_Input_GetMouseEventAxisType(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventaxistype)-获取鼠标轴事件的类型。[void OH_Input_SetMouseEventAxisValue(struct Input_MouseEvent* mouseEvent, float axisValue)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventaxisvalue)-设置鼠标轴事件的值。[float OH_Input_GetMouseEventAxisValue(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventaxisvalue)-获取鼠标轴事件的值。[void OH_Input_SetMouseEventActionTime(struct Input_MouseEvent* mouseEvent, int64_t actionTime)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventactiontime)-设置鼠标事件发生的时间。[int64_t OH_Input_GetMouseEventActionTime(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventactiontime)-获取鼠标事件发生的时间。[void OH_Input_SetMouseEventWindowId(struct Input_MouseEvent* mouseEvent, int32_t windowId)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventwindowid)-设置鼠标事件的窗口ID。[int32_t OH_Input_GetMouseEventWindowId(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventwindowid)-获取鼠标事件的窗口ID。[void OH_Input_SetMouseEventDisplayId(struct Input_MouseEvent* mouseEvent, int32_t displayId)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventdisplayid)-设置鼠标事件的屏幕ID。[struct Input_TouchEvent* OH_Input_CreateTouchEvent()](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)-创建触屏输入事件对象。[void OH_Input_DestroyTouchEvent(struct Input_TouchEvent** touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)-销毁触屏输入事件对象。[void OH_Input_SetTouchEventAction(struct Input_TouchEvent* touchEvent, int32_t action)](#ZH-CN_TOPIC_0000002529445539__oh_input_settoucheventaction)-设置触屏输入事件的动作。[int32_t OH_Input_GetTouchEventAction(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_gettoucheventaction)-获取触屏输入事件的动作。[void OH_Input_SetTouchEventFingerId(struct Input_TouchEvent* touchEvent, int32_t id)](#ZH-CN_TOPIC_0000002529445539__oh_input_settoucheventfingerid)-设置触屏输入事件的手指ID。[int32_t OH_Input_GetTouchEventFingerId(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_gettoucheventfingerid)-获取触屏输入事件的手指ID。[void OH_Input_SetTouchEventDisplayX(struct Input_TouchEvent* touchEvent, int32_t displayX)](#ZH-CN_TOPIC_0000002529445539__oh_input_settoucheventdisplayx)-设置触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。[int32_t OH_Input_GetTouchEventDisplayX(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_gettoucheventdisplayx)-获取触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。[void OH_Input_SetTouchEventDisplayY(struct Input_TouchEvent* touchEvent, int32_t displayY)](#ZH-CN_TOPIC_0000002529445539__oh_input_settoucheventdisplayy)-设置触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。[int32_t OH_Input_GetTouchEventDisplayY(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_gettoucheventdisplayy)-获取触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。[void OH_Input_SetTouchEventActionTime(struct Input_TouchEvent* touchEvent, int64_t actionTime)](#ZH-CN_TOPIC_0000002529445539__oh_input_settoucheventactiontime)-设置触屏输入事件发生的时间。[int64_t OH_Input_GetTouchEventActionTime(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_gettoucheventactiontime)-获取触屏输入事件发生的时间。[void OH_Input_SetTouchEventWindowId(struct Input_TouchEvent* touchEvent, int32_t windowId)](#ZH-CN_TOPIC_0000002529445539__oh_input_settoucheventwindowid)-设置触屏输入事件的窗口ID。[int32_t OH_Input_GetTouchEventWindowId(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_gettoucheventwindowid)-获取触屏输入事件的窗口ID。[void OH_Input_SetTouchEventDisplayId(struct Input_TouchEvent* touchEvent, int32_t displayId)](#ZH-CN_TOPIC_0000002529445539__oh_input_settoucheventdisplayid)-设置触屏输入事件的屏幕ID。[int32_t OH_Input_GetTouchEventDisplayId(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_gettoucheventdisplayid)-获取触屏输入事件的屏幕ID。[void OH_Input_CancelInjection()](#ZH-CN_TOPIC_0000002529445539__oh_input_cancelinjection)-取消事件注入并撤销授权。[Input_Result OH_Input_RequestInjection(Input_InjectAuthorizeCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_requestinjection)-当前应用申请注入权限，包括申请注入按键事件[OH_Input_InjectKeyEvent](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__oh_input_injectkeyevent)、注入触屏输入事件[OH_Input_InjectTouchEvent](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__oh_input_injecttouchevent)、注入鼠标事件[OH_Input_InjectMouseEvent](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__oh_input_injectmouseevent)等注入操作的权限。[Input_Result OH_Input_QueryAuthorizedStatus(Input_InjectionStatus* status)](#ZH-CN_TOPIC_0000002529445539__oh_input_queryauthorizedstatus)-查询当前应用注入的权限状态。[Input_AxisEvent* OH_Input_CreateAxisEvent(void)](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)-创建轴事件对象。[Input_Result OH_Input_DestroyAxisEvent(Input_AxisEvent** axisEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)-销毁轴事件对象。[Input_Result OH_Input_SetAxisEventAction(Input_AxisEvent* axisEvent, InputEvent_AxisAction action)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventaction)-设置轴事件的动作。[Input_Result OH_Input_GetAxisEventAction(const Input_AxisEvent* axisEvent, InputEvent_AxisAction *action)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventaction)-获取轴事件的动作。[Input_Result OH_Input_SetAxisEventDisplayX(Input_AxisEvent* axisEvent, float displayX)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventdisplayx)-设置轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。[Input_Result OH_Input_GetAxisEventDisplayX(const Input_AxisEvent* axisEvent, float* displayX)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventdisplayx)-获取轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。[Input_Result OH_Input_SetAxisEventDisplayY(Input_AxisEvent* axisEvent, float displayY)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventdisplayy)-设置轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。[Input_Result OH_Input_GetAxisEventDisplayY(const Input_AxisEvent* axisEvent, float* displayY)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventdisplayy)-获取轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。[Input_Result OH_Input_SetAxisEventAxisValue(Input_AxisEvent* axisEvent,InputEvent_AxisType axisType, double axisValue)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventaxisvalue)-设置轴事件指定轴类型的轴值。[Input_Result OH_Input_GetAxisEventAxisValue(const Input_AxisEvent* axisEvent,InputEvent_AxisType axisType, double* axisValue)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventaxisvalue)-获取轴事件指定轴类型的轴值。[Input_Result OH_Input_SetAxisEventActionTime(Input_AxisEvent* axisEvent, int64_t actionTime)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventactiontime)-设置轴事件发生的时间。[Input_Result OH_Input_GetAxisEventActionTime(const Input_AxisEvent* axisEvent, int64_t* actionTime)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventactiontime)-获取轴事件发生的时间。[Input_Result OH_Input_SetAxisEventType(Input_AxisEvent* axisEvent, InputEvent_AxisEventType axisEventType)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventtype)-设置轴事件类型。[Input_Result OH_Input_GetAxisEventType(const Input_AxisEvent* axisEvent, InputEvent_AxisEventType* axisEventType)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventtype)-获取轴事件类型。[Input_Result OH_Input_SetAxisEventSourceType(Input_AxisEvent* axisEvent, InputEvent_SourceType sourceType)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventsourcetype)-设置轴事件源类型。[Input_Result OH_Input_GetAxisEventSourceType(const Input_AxisEvent* axisEvent, InputEvent_SourceType* sourceType)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventsourcetype)-获取轴事件源类型。[Input_Result OH_Input_SetAxisEventWindowId(Input_AxisEvent* axisEvent, int32_t windowId)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventwindowid)-设置轴事件的窗口ID。[Input_Result OH_Input_GetAxisEventWindowId(const Input_AxisEvent* axisEvent, int32_t* windowId)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventwindowid)-获取轴事件的窗口ID。[Input_Result OH_Input_SetAxisEventDisplayId(Input_AxisEvent* axisEvent, int32_t displayId)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventdisplayid)-设置轴事件的屏幕ID。[Input_Result OH_Input_GetAxisEventDisplayId(const Input_AxisEvent* axisEvent, int32_t* displayId)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventdisplayid)-获取轴事件的屏幕ID。[Input_Result OH_Input_AddKeyEventMonitor(Input_KeyEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_addkeyeventmonitor)-添加按键事件监听。[Input_Result OH_Input_AddMouseEventMonitor(Input_MouseEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_addmouseeventmonitor)-添加鼠标事件监听,包含鼠标点击，移动，不包含滚轮事件，滚轮事件归属于轴事件。[Input_Result OH_Input_AddTouchEventMonitor(Input_TouchEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_addtoucheventmonitor)-添加触屏输入事件监听。[Input_Result OH_Input_AddAxisEventMonitorForAll(Input_AxisEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_addaxiseventmonitorforall)-添加所有类型轴事件监听，轴事件类型定义在[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)中。[Input_Result OH_Input_AddAxisEventMonitor(InputEvent_AxisEventType axisEventType, Input_AxisEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_addaxiseventmonitor)-添加指定类型的轴事件监听，轴事件类型定义在[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)中。[Input_Result OH_Input_RemoveKeyEventMonitor(Input_KeyEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_removekeyeventmonitor)-移除按键事件监听。[Input_Result OH_Input_RemoveMouseEventMonitor(Input_MouseEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_removemouseeventmonitor)-移除鼠标事件监听。[Input_Result OH_Input_RemoveTouchEventMonitor(Input_TouchEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_removetoucheventmonitor)-移除触屏输入事件监听。[Input_Result OH_Input_RemoveAxisEventMonitorForAll(Input_AxisEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_removeaxiseventmonitorforall)-移除所有类型轴事件监听。[Input_Result OH_Input_RemoveAxisEventMonitor(InputEvent_AxisEventType axisEventType, Input_AxisEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_removeaxiseventmonitor)-移除指定类型轴事件监听，轴事件类型定义在[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)中。[Input_Result OH_Input_AddKeyEventInterceptor(Input_KeyEventCallback callback, Input_InterceptorOptions *option)](#ZH-CN_TOPIC_0000002529445539__oh_input_addkeyeventinterceptor)-添加按键事件的拦截，重复添加只有第一次生效。仅在应用获焦时拦截按键事件。[Input_Result OH_Input_AddInputEventInterceptor(Input_InterceptorEventCallback *callback,Input_InterceptorOptions *option)](#ZH-CN_TOPIC_0000002529445539__oh_input_addinputeventinterceptor)-添加输入事件拦截，包括鼠标、触屏和轴事件，重复添加只有第一次生效。仅命中应用窗口时拦截输入事件。[Input_Result OH_Input_RemoveKeyEventInterceptor(void)](#ZH-CN_TOPIC_0000002529445539__oh_input_removekeyeventinterceptor)-移除按键事件拦截。[Input_Result OH_Input_RemoveInputEventInterceptor(void)](#ZH-CN_TOPIC_0000002529445539__oh_input_removeinputeventinterceptor)-移除输入事件拦截，包括鼠标、触屏和轴事件。[Input_Result OH_Input_GetIntervalSinceLastInput(int64_t *timeInterval)](#ZH-CN_TOPIC_0000002529445539__oh_input_getintervalsincelastinput)-获取距离上次系统输入事件的时间间隔。[Input_Hotkey *OH_Input_CreateHotkey(void)](#ZH-CN_TOPIC_0000002529445539__oh_input_createhotkey)-创建快捷键对象。[void OH_Input_DestroyHotkey(Input_Hotkey **hotkey)](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyhotkey)-销毁快捷键对象。[void OH_Input_SetPreKeys(Input_Hotkey *hotkey, int32_t *preKeys, int32_t size)](#ZH-CN_TOPIC_0000002529445539__oh_input_setprekeys)-设置修饰键。[Input_Result OH_Input_GetPreKeys(const Input_Hotkey *hotkey, int32_t **preKeys, int32_t *preKeyCount)](#ZH-CN_TOPIC_0000002529445539__oh_input_getprekeys)-获取修饰键。[void OH_Input_SetFinalKey(Input_Hotkey* hotkey, int32_t finalKey)](#ZH-CN_TOPIC_0000002529445539__oh_input_setfinalkey)-设置被修饰键。[Input_Result OH_Input_GetFinalKey(const Input_Hotkey* hotkey, int32_t *finalKeyCode)](#ZH-CN_TOPIC_0000002529445539__oh_input_getfinalkey)-获取被修饰键。[Input_Hotkey **OH_Input_CreateAllSystemHotkeys(int32_t count)](#ZH-CN_TOPIC_0000002529445539__oh_input_createallsystemhotkeys)-创建[Input_Hotkey](../../topics/input/Input_Hotkey.md)类型实例的数组。[void OH_Input_DestroyAllSystemHotkeys(Input_Hotkey **hotkeys, int32_t count)](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyallsystemhotkeys)-销毁[Input_Hotkey](../../topics/input/Input_Hotkey.md)实例数组并回收内存。[Input_Result OH_Input_GetAllSystemHotkeys(Input_Hotkey **hotkey, int32_t *count)](#ZH-CN_TOPIC_0000002529445539__oh_input_getallsystemhotkeys)-获取设置的所有快捷键。[void OH_Input_SetRepeat(Input_Hotkey* hotkey, bool isRepeat)](#ZH-CN_TOPIC_0000002529445539__oh_input_setrepeat)-设置是否上报重复key事件。[Input_Result OH_Input_GetRepeat(const Input_Hotkey* hotkey, bool *isRepeat)](#ZH-CN_TOPIC_0000002529445539__oh_input_getrepeat)-获取是否上报重复key事件。[Input_Result OH_Input_AddHotkeyMonitor(const Input_Hotkey* hotkey, Input_HotkeyCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_addhotkeymonitor)-订阅快捷键事件。此接口在智能穿戴、轻量级智能穿戴设备不生效。[Input_Result OH_Input_RemoveHotkeyMonitor(const Input_Hotkey* hotkey, Input_HotkeyCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_removehotkeymonitor)-取消订阅快捷键。[Input_Result OH_Input_RegisterDeviceListener(Input_DeviceListener* listener)](#ZH-CN_TOPIC_0000002529445539__oh_input_registerdevicelistener)-注册设备热插拔的监听器。[Input_Result OH_Input_UnregisterDeviceListener(Input_DeviceListener* listener)](#ZH-CN_TOPIC_0000002529445539__oh_input_unregisterdevicelistener)-取消注册设备热插拔的监听。[Input_Result OH_Input_UnregisterDeviceListeners()](#ZH-CN_TOPIC_0000002529445539__oh_input_unregisterdevicelisteners)-取消注册所有的设备热插拔的监听。[Input_Result OH_Input_GetDeviceIds(int32_t *deviceIds, int32_t inSize, int32_t *outSize)](#ZH-CN_TOPIC_0000002529445539__oh_input_getdeviceids)-获取所有输入设备的ID列表。[Input_Result OH_Input_GetDevice(int32_t deviceId, Input_DeviceInfo **deviceInfo)](#ZH-CN_TOPIC_0000002529445539__oh_input_getdevice)-获取输入设备信息。[Input_DeviceInfo* OH_Input_CreateDeviceInfo(void)](#ZH-CN_TOPIC_0000002529445539__oh_input_createdeviceinfo)-创建输入设备信息的对象。[void OH_Input_DestroyDeviceInfo(Input_DeviceInfo **deviceInfo)](#ZH-CN_TOPIC_0000002529445539__oh_input_destroydeviceinfo)-销毁输入设备信息的对象。[Input_Result OH_Input_GetKeyboardType(int32_t deviceId, int32_t *keyboardType)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeyboardtype)-获取输入设备的键盘类型。[Input_Result OH_Input_GetDeviceId(Input_DeviceInfo *deviceInfo, int32_t *id)](#ZH-CN_TOPIC_0000002529445539__oh_input_getdeviceid)-获取输入设备的ID。[Input_Result OH_Input_GetDeviceName(Input_DeviceInfo *deviceInfo, char **name)](#ZH-CN_TOPIC_0000002529445539__oh_input_getdevicename)-获取输入设备的名称。[Input_Result OH_Input_GetCapabilities(Input_DeviceInfo *deviceInfo, int32_t *capabilities)](#ZH-CN_TOPIC_0000002529445539__oh_input_getcapabilities)-获取有关输入设备能力信息，比如设备是触摸屏、触控板、键盘等。[Input_Result OH_Input_GetDeviceVersion(Input_DeviceInfo *deviceInfo, int32_t *version)](#ZH-CN_TOPIC_0000002529445539__oh_input_getdeviceversion)-获取输入设备的版本信息。[Input_Result OH_Input_GetDeviceProduct(Input_DeviceInfo *deviceInfo, int32_t *product)](#ZH-CN_TOPIC_0000002529445539__oh_input_getdeviceproduct)-获取输入设备的产品信息。[Input_Result OH_Input_GetDeviceVendor(Input_DeviceInfo *deviceInfo, int32_t *vendor)](#ZH-CN_TOPIC_0000002529445539__oh_input_getdevicevendor)-获取输入设备的厂商信息。[Input_Result OH_Input_GetDeviceAddress(Input_DeviceInfo *deviceInfo, char **address)](#ZH-CN_TOPIC_0000002529445539__oh_input_getdeviceaddress)-获取输入设备的物理地址。[Input_Result OH_Input_GetFunctionKeyState(int32_t keyCode, int32_t *state)](#ZH-CN_TOPIC_0000002529445539__oh_input_getfunctionkeystate)-获取功能键状态。[int32_t OH_Input_InjectTouchEvent(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_injecttouchevent)-使用以指定屏幕左上角为原点的相对坐标系的坐标注入触屏输入事件。[int32_t OH_Input_InjectMouseEvent(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_injectmouseevent)-使用以指定屏幕左上角为原点的相对坐标系的坐标注入鼠标事件。[int32_t OH_Input_GetMouseEventDisplayId(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventdisplayid)-获取鼠标事件的屏幕ID。[Input_Result OH_Input_QueryMaxTouchPoints(int32_t *count)](#ZH-CN_TOPIC_0000002529445539__oh_input_querymaxtouchpoints)-查询设备支持的最大触屏报点数。[int32_t OH_Input_InjectMouseEventGlobal(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_injectmouseeventglobal)-使用以主屏左上角为原点的全局坐标系的坐标注入鼠标事件。[void OH_Input_SetMouseEventGlobalX(struct Input_MouseEvent* mouseEvent, int32_t globalX)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventglobalx)-设置鼠标事件以主屏左上角为原点的全局坐标系的X坐标。[int32_t OH_Input_GetMouseEventGlobalX(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventglobalx)-获取鼠标事件以主屏左上角为原点的全局坐标系的X坐标。[void OH_Input_SetMouseEventGlobalY(struct Input_MouseEvent* mouseEvent, int32_t globalY)](#ZH-CN_TOPIC_0000002529445539__oh_input_setmouseeventglobaly)-设置鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。[int32_t OH_Input_GetMouseEventGlobalY(const struct Input_MouseEvent* mouseEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventglobaly)-获取鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。[int32_t OH_Input_InjectTouchEventGlobal(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_injecttoucheventglobal)-使用以主屏左上角为原点的全局坐标系的坐标注入触屏输入事件。[void OH_Input_SetTouchEventGlobalX(struct Input_TouchEvent* touchEvent, int32_t globalX)](#ZH-CN_TOPIC_0000002529445539__oh_input_settoucheventglobalx)-设置触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。[int32_t OH_Input_GetTouchEventGlobalX(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_gettoucheventglobalx)-获取触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。[void OH_Input_SetTouchEventGlobalY(struct Input_TouchEvent* touchEvent, int32_t globalY)](#ZH-CN_TOPIC_0000002529445539__oh_input_settoucheventglobaly)-设置触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。[int32_t OH_Input_GetTouchEventGlobalY(const struct Input_TouchEvent* touchEvent)](#ZH-CN_TOPIC_0000002529445539__oh_input_gettoucheventglobaly)-获取触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。[Input_Result OH_Input_SetAxisEventGlobalX(struct Input_AxisEvent* axisEvent, int32_t globalX)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventglobalx)-设置轴事件以主屏左上角为原点的全局坐标系的X坐标。[Input_Result OH_Input_GetAxisEventGlobalX(const Input_AxisEvent* axisEvent, int32_t* globalX)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventglobalx)-获取轴事件以主屏左上角为原点的全局坐标系的X坐标。[Input_Result OH_Input_SetAxisEventGlobalY(struct Input_AxisEvent* axisEvent, int32_t globalY)](#ZH-CN_TOPIC_0000002529445539__oh_input_setaxiseventglobaly)-设置轴事件以主屏左上角为原点的全局坐标系的Y坐标。[Input_Result OH_Input_GetAxisEventGlobalY(const Input_AxisEvent* axisEvent, int32_t* globalY)](#ZH-CN_TOPIC_0000002529445539__oh_input_getaxiseventglobaly)-获取轴事件以主屏左上角为原点的全局坐标系的Y坐标。[Input_Result OH_Input_GetPointerLocation(int32_t *displayId, double *displayX, double *displayY)](#ZH-CN_TOPIC_0000002529445539__oh_input_getpointerlocation)-获取鼠标在屏幕上的坐标点。[Input_Result OH_Input_GetKeyEventId(const struct Input_KeyEvent* keyEvent, int32_t* eventId)](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeyeventid)-获取按键事件的ID。[Input_Result OH_Input_AddKeyEventHook(Input_KeyEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_addkeyeventhook)-添加一个按键事件拦截钩子函数。[Input_Result OH_Input_RemoveKeyEventHook(Input_KeyEventCallback callback)](#ZH-CN_TOPIC_0000002529445539__oh_input_removekeyeventhook)-移除按键事件拦截钩子函数。[Input_Result OH_Input_DispatchToNextHandler(int32_t eventId)](#ZH-CN_TOPIC_0000002529445539__oh_input_dispatchtonexthandler)-重新分发按键事件。[Input_Result OH_Input_SetPointerVisible(bool visible)](#ZH-CN_TOPIC_0000002529445539__oh_input_setpointervisible)-设置当前窗口的鼠标光标的显示或隐藏状态。[Input_Result OH_Input_GetPointerStyle(int32_t windowId, int32_t *pointerStyle)](#ZH-CN_TOPIC_0000002529445539__oh_input_getpointerstyle)-获取指定窗口的鼠标光标样式。[Input_Result OH_Input_SetPointerStyle(int32_t windowId, int32_t pointerStyle)](#ZH-CN_TOPIC_0000002529445539__oh_input_setpointerstyle)-设置指定窗口的鼠标光标样式。[Input_CustomCursor* OH_Input_CustomCursor_Create(OH_PixelmapNative* pixelMap, int32_t anchorX, int32_t anchorY)](#ZH-CN_TOPIC_0000002529445539__oh_input_customcursor_create)-创建自定义鼠标光标资源对象。[void OH_Input_CustomCursor_Destroy(Input_CustomCursor** customCursor)](#ZH-CN_TOPIC_0000002529445539__oh_input_customcursor_destroy)-销毁自定义鼠标光标资源对象。[Input_Result OH_Input_CustomCursor_GetPixelMap(Input_CustomCursor* customCursor, OH_PixelmapNative** pixelMap)](#ZH-CN_TOPIC_0000002529445539__oh_input_customcursor_getpixelmap)-获取指定自定义鼠标光标资源的自定义鼠标光标像素图。[Input_Result OH_Input_CustomCursor_GetAnchor(Input_CustomCursor* customCursor, int32_t* anchorX, int32_t* anchorY)](#ZH-CN_TOPIC_0000002529445539__oh_input_customcursor_getanchor)-获取指定自定义鼠标光标资源的焦点坐标。[Input_CursorConfig* OH_Input_CursorConfig_Create(bool followSystem)](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorconfig_create)-创建自定义鼠标光标配置对象。[void OH_Input_CursorConfig_Destroy(Input_CursorConfig** cursorConfig)](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorconfig_destroy)-销毁自定义鼠标光标配置对象。[Input_Result OH_Input_CursorConfig_IsFollowSystem(Input_CursorConfig *cursorConfig, bool *followSystem)](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorconfig_isfollowsystem)-查询自定义鼠标光标配置是否跟随系统设置调整光标大小。[Input_Result OH_Input_SetCustomCursor(int32_t windowId, Input_CustomCursor* customCursor, Input_CursorConfig* cursorConfig)](#ZH-CN_TOPIC_0000002529445539__oh_input_setcustomcursor)-设置自定义鼠标光标样式。[struct Input_CursorInfo* OH_Input_CursorInfo_Create()](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorinfo_create)-创建鼠标光标信息对象。[void OH_Input_CursorInfo_Destroy(Input_CursorInfo** cursorInfo)](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorinfo_destroy)-销毁鼠标光标信息对象。[Input_Result OH_Input_CursorInfo_IsVisible(Input_CursorInfo* cursorInfo, bool* visible)](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorinfo_isvisible)-获取指定鼠标光标信息对象对应的光标显示状态。[Input_Result OH_Input_CursorInfo_GetStyle(Input_CursorInfo* cursorInfo, Input_PointerStyle* style)](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorinfo_getstyle)-获取指定鼠标光标信息对象对应的光标样式。[Input_Result OH_Input_CursorInfo_GetSizeLevel(Input_CursorInfo* cursorInfo, int32_t* sizeLevel)](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorinfo_getsizelevel)-获取指定鼠标光标信息对象对应的光标大小档位。[Input_Result OH_Input_CursorInfo_GetColor(Input_CursorInfo* cursorInfo, uint32_t* color)](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorinfo_getcolor)-获取指定鼠标光标信息对象对应的光标颜色, 使用32位ARGB整数表示。[Input_Result OH_Input_GetMouseEventCursorInfo(const struct Input_MouseEvent* mouseEvent, Input_CursorInfo* cursorInfo)](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventcursorinfo)-获取鼠标事件的鼠标光标信息，包括光标显示状态、光标样式、光标大小档位、光标颜色。[Input_Result OH_Input_GetCursorInfo(Input_CursorInfo* cursorInfo, OH_PixelmapNative** pixelmap)](#ZH-CN_TOPIC_0000002529445539__oh_input_getcursorinfo)-查询当前鼠标光标信息，包括光标显示状态、光标样式、光标大小档位、光标颜色。如果pixelmap参数非空，且光标样式为[DEVELOPER_DEFINED_ICON](oh_pointer_style.h.md#ZH-CN_TOPIC_0000002497445596__input_pointerstyle)，则会同时返回光标的PixelMap位图对象。

#### 枚举类型说明

#### Input_KeyStateAction

```ets
enum Input_KeyStateAction
```

**描述**

按键状态的枚举值。

**起始版本：** 12

枚举项描述KEY_DEFAULT = -1默认状态。KEY_PRESSED = 0按键按下。KEY_RELEASED = 1按键抬起。KEY_SWITCH_ON = 2按键开关使能。KEY_SWITCH_OFF = 3按键开关去使能。

#### Input_KeyEventAction

```ets
enum Input_KeyEventAction
```

**描述**

按键事件类型的枚举值。

**起始版本：** 12

枚举项描述KEY_ACTION_CANCEL = 0按键动作取消。KEY_ACTION_DOWN = 1按键按下。KEY_ACTION_UP = 2按键抬起。

#### Input_MouseEventAction

```ets
enum Input_MouseEventAction
```

**描述**

鼠标动作的枚举值。

**起始版本：** 12

枚举项描述MOUSE_ACTION_CANCEL = 0取消鼠标动作。MOUSE_ACTION_MOVE = 1移动鼠标。MOUSE_ACTION_BUTTON_DOWN = 2按下鼠标。MOUSE_ACTION_BUTTON_UP = 3抬起鼠标按键。MOUSE_ACTION_AXIS_BEGIN = 4鼠标轴事件开始。MOUSE_ACTION_AXIS_UPDATE = 5更新鼠标轴事件。MOUSE_ACTION_AXIS_END = 6鼠标轴事件结束。

#### InputEvent_MouseAxis

```ets
enum InputEvent_MouseAxis
```

**描述**

鼠标轴事件类型。

**起始版本：** 12

枚举项描述MOUSE_AXIS_SCROLL_VERTICAL = 0垂直滚动轴。MOUSE_AXIS_SCROLL_HORIZONTAL = 1水平滚动轴。

#### Input_MouseEventButton

```ets
enum Input_MouseEventButton
```

**描述**

鼠标按键的枚举值。

**起始版本：** 12

枚举项描述MOUSE_BUTTON_NONE = -1无效按键。MOUSE_BUTTON_LEFT = 0鼠标左键。MOUSE_BUTTON_MIDDLE = 1鼠标中间键。MOUSE_BUTTON_RIGHT = 2鼠标右键。MOUSE_BUTTON_FORWARD = 3鼠标前进键。MOUSE_BUTTON_BACK = 4鼠标返回键。

#### Input_TouchEventAction

```ets
enum Input_TouchEventAction
```

**描述**

触屏动作的枚举值。

**起始版本：** 12

枚举项描述TOUCH_ACTION_CANCEL = 0触屏取消。TOUCH_ACTION_DOWN = 1触屏按下。TOUCH_ACTION_MOVE = 2触屏移动。TOUCH_ACTION_UP = 3触屏抬起。

#### Input_InjectionStatus

```ets
enum Input_InjectionStatus
```

**描述**

注入权限状态枚举值。

**起始版本：** 20

枚举项描述UNAUTHORIZED = 0未授权。AUTHORIZING = 1授权中。AUTHORIZED = 2已授权。

#### InputEvent_SourceType

```ets
enum InputEvent_SourceType
```

**描述**

输入事件源类型。

**起始版本：** 12

枚举项描述SOURCE_TYPE_MOUSE = 1表示输入源生成鼠标光标移动、按键按下和释放以及滚轮滚动的事件。SOURCE_TYPE_TOUCHSCREEN = 2表示输入源产生触摸屏多点触屏输入事件。SOURCE_TYPE_TOUCHPAD = 3表示输入源产生触控板多点触屏输入事件。

#### Input_KeyboardType

```ets
enum Input_KeyboardType
```

**描述**

输入设备的键盘类型。

**起始版本：** 13

枚举项描述KEYBOARD_TYPE_NONE = 0表示无按键设备。KEYBOARD_TYPE_UNKNOWN = 1表示未知按键设备。KEYBOARD_TYPE_ALPHABETIC = 2表示全键盘设备。KEYBOARD_TYPE_DIGITAL = 3表示数字键盘设备。KEYBOARD_TYPE_STYLUS = 4表示手写笔设备。KEYBOARD_TYPE_REMOTE_CONTROL = 5表示遥控器设备。

#### Input_Result

```ets
enum Input_Result
```

**描述**

错误码枚举值。

**起始版本：** 12

枚举项描述INPUT_SUCCESS = 0操作成功。INPUT_PERMISSION_DENIED = 201权限验证失败。INPUT_NOT_SYSTEM_APPLICATION = 202非系统应用。INPUT_PARAMETER_ERROR = 401参数检查失败。INPUT_DEVICE_NOT_SUPPORTED = 801

表示不支持该功能。

**起始版本：** 14。

INPUT_SERVICE_EXCEPTION = 3800001服务异常。INPUT_REPEAT_INTERCEPTOR = 4200001应用创建拦截后，再次执行创建拦截的操作。INPUT_OCCUPIED_BY_SYSTEM = 4200002

已经被系统应用占用。

**起始版本：** 14。

INPUT_OCCUPIED_BY_OTHER = 4200003

已经被其他应用占用。

**起始版本：** 14。

INPUT_KEYBOARD_DEVICE_NOT_EXIST = 3900002

未连接键盘设备。

**起始版本：** 15。

INPUT_INJECTION_AUTHORIZING = 3900005

正在授权中。

**起始版本：** 20。

INPUT_INJECTION_OPERATION_FREQUENT = 3900006

重复请求。

**起始版本：** 20。

INPUT_INJECTION_AUTHORIZED = 3900007

当前应用已经授权。

**起始版本：** 20。

INPUT_INJECTION_AUTHORIZED_OTHERS = 3900008

其它应用已经授权。

**起始版本：** 20。

INPUT_APP_NOT_FOCUSED = 3900009

当前应用不是焦点应用。

**起始版本：** 20。

INPUT_DEVICE_NO_POINTER = 3900010

无鼠标类输入外设。

**起始版本：** 20。

INPUT_INVALID_WINDOWID = 26500001

无效的窗口ID。

**起始版本：** 22。

#### 函数说明

#### Input_HotkeyCallback()

```ets
typedef void (*Input_HotkeyCallback)(Input_Hotkey* hotkey)
```

**描述**

回调函数，用于回调快捷键事件。

**起始版本：** 14

#### Input_KeyEventCallback()

```ets
typedef void (*Input_KeyEventCallback)(const Input_KeyEvent* keyEvent)
```

**描述**

按键事件的回调函数，keyEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

参数项描述const [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

#### Input_MouseEventCallback()

```ets
typedef void (*Input_MouseEventCallback)(const Input_MouseEvent* mouseEvent)
```

**描述**

鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

参数项描述const [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

#### Input_TouchEventCallback()

```ets
typedef void (*Input_TouchEventCallback)(const Input_TouchEvent* touchEvent)
```

**描述**

触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

参数项描述const [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

#### Input_AxisEventCallback()

```ets
typedef void (*Input_AxisEventCallback)(const Input_AxisEvent* axisEvent)
```

**描述**

轴事件的回调函数，axisEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

#### Input_DeviceAddedCallback()

```ets
typedef void (*Input_DeviceAddedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于回调输入设备的热插事件。

**起始版本：** 13

**参数：**

参数项描述int32_t deviceId输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

#### Input_DeviceRemovedCallback()

```ets
typedef void (*Input_DeviceRemovedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于回调输入设备的热拔事件。

**起始版本：** 13

**参数：**

参数项描述int32_t deviceId输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。

#### Input_InjectAuthorizeCallback()

```ets
typedef void (*Input_InjectAuthorizeCallback)(Input_InjectionStatus authorizedStatus)
```

**描述**

回调函数，用于获取注入权限状态。

**起始版本：** 20

**参数：**

参数项描述[Input_InjectionStatus](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_injectionstatus) authorizedStatus注入权限状态。

#### OH_Input_GetKeyState()

```ets
Input_Result OH_Input_GetKeyState(struct Input_KeyState* keyState)
```

**描述**

查询按键状态的枚举对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_KeyState](../../topics/input/Input_KeyState.md)* keyState按键状态的枚举对象，具体请参考[Input_KeyStateAction](#ZH-CN_TOPIC_0000002529445539__input_keystateaction)。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

如果操作成功，@return返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；

 否则返回[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)中定义的其他错误代码。

#### OH_Input_CreateKeyState()

```ets
struct Input_KeyState* OH_Input_CreateKeyState()
```

**描述**

创建按键状态的枚举对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**返回：**

类型说明struct如果操作成功，@return返回一个[Input_KeyState](../../topics/input/Input_KeyState.md)指针对象；否则返回空指针。

#### OH_Input_DestroyKeyState()

```ets
void OH_Input_DestroyKeyState(struct Input_KeyState** keyState)
```

**描述**

销毁按键状态的枚举对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_KeyState](../../topics/input/Input_KeyState.md)** keyState按键状态的枚举对象，具体请参考[Input_KeyStateAction](#ZH-CN_TOPIC_0000002529445539__input_keystateaction)。

#### OH_Input_SetKeyCode()

```ets
void OH_Input_SetKeyCode(struct Input_KeyState* keyState, int32_t keyCode)
```

**描述**

设置按键状态对象的键值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_KeyState](../../topics/input/Input_KeyState.md)* keyState按键状态的枚举对象，具体请参考[Input_KeyStateAction](#ZH-CN_TOPIC_0000002529445539__input_keystateaction)。int32_t keyCode按键键值。

#### OH_Input_GetKeyCode()

```ets
int32_t OH_Input_GetKeyCode(const struct Input_KeyState* keyState)
```

**描述**

获取按键状态对象的键值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_KeyState](../../topics/input/Input_KeyState.md)* keyState按键状态的枚举对象，具体请参考[Input_KeyStateAction](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_keystateaction)。

**返回：**

类型说明int32_t返回按键状态对象的键值。

#### OH_Input_SetKeyPressed()

```ets
void OH_Input_SetKeyPressed(struct Input_KeyState* keyState, int32_t keyAction)
```

**描述**

设置按键状态对象的按键是否按下。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_KeyState](../../topics/input/Input_KeyState.md)* keyState按键状态的枚举对象，具体请参考[Input_KeyStateAction](#ZH-CN_TOPIC_0000002529445539__input_keystateaction)。int32_t keyAction按键是否按下，具体请参考[Input_KeyEventAction](#ZH-CN_TOPIC_0000002529445539__input_keyeventaction)。

#### OH_Input_GetKeyPressed()

```ets
int32_t OH_Input_GetKeyPressed(const struct Input_KeyState* keyState)
```

**描述**

获取按键状态对象的按键是否按下。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_KeyState](../../topics/input/Input_KeyState.md)* keyState按键状态的枚举对象，具体请参考[Input_KeyStateAction](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_keystateaction)。

**返回：**

类型说明int32_t返回按键状态对象的按键按下状态。

#### OH_Input_SetKeySwitch()

```ets
void OH_Input_SetKeySwitch(struct Input_KeyState* keyState, int32_t keySwitch)
```

**描述**

设置按键状态对象的按键开关。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_KeyState](../../topics/input/Input_KeyState.md)* keyState按键状态的枚举对象，具体请参考[Input_KeyStateAction](#ZH-CN_TOPIC_0000002529445539__input_keystateaction)。int32_t keySwitch按键开关。

#### OH_Input_GetKeySwitch()

```ets
int32_t OH_Input_GetKeySwitch(const struct Input_KeyState* keyState)
```

**描述**

获取按键状态对象的按键开关。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_KeyState](../../topics/input/Input_KeyState.md)* keyState按键状态的枚举对象，具体请参考[Input_KeyStateAction](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_keystateaction)。

**返回：**

类型说明int32_t返回按键状态对象的按键开关。

#### OH_Input_InjectKeyEvent()

```ets
int32_t OH_Input_InjectKeyEvent(const struct Input_KeyEvent* keyEvent)
```

**描述**

注入按键事件。

如果当前处于用户未授权状态，调用该接口注入事件不生效。

从API version 20开始，建议先使用[OH_Input_RequestInjection](#ZH-CN_TOPIC_0000002529445539__oh_input_requestinjection)请求授权。然后通过[OH_Input_QueryAuthorizedStatus](#ZH-CN_TOPIC_0000002529445539__oh_input_queryauthorizedstatus)查询授权状态，当授权状态为[AUTHORIZED](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_injectionstatus)时，再使用该接口。

从API version 22开始，如果注入了修饰键（KEYCODE_META_LEFT、KEYCODE_META_RIGHT、KEYCODE_CTRL_LEFT、KEYCODE_CTRL_RIGHT、

KEYCODE_ALT_LEFT、KEYCODE_ALT_RIGHT、KEYCODE_SHIFT_LEFT、KEYCODE_SHIFT_RIGHT、KEYCODE_CAPS_LOCK、KEYCODE_SCROLL_LOCK、KEYCODE_NUM_LOCK）

的按压事件（KEY_ACTION_DOWN）时，请及时注入该按键的抬起事件（KEY_ACTION_UP），以避免该按键长时间处于按压状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。并通过[OH_Input_SetKeyEventKeyCode](#ZH-CN_TOPIC_0000002529445539__oh_input_setkeyeventkeycode)、[OH_Input_SetKeyEventAction](#ZH-CN_TOPIC_0000002529445539__oh_input_setkeyeventaction)接口可以设置按键事件的键值和按键事件的类型。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

**返回：**

类型说明int32_t

OH_Input_InjectKeyEvent 函数错误码。

 若注入成功，返回[INPUT_SUCCESS](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_result)；

 若缺少权限，返回[INPUT_PERMISSION_DENIED](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_result)；

 若参数错误，返回[INPUT_PARAMETER_ERROR](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_CreateKeyEvent()

```ets
struct Input_KeyEvent* OH_Input_CreateKeyEvent()
```

**描述**

创建按键事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**返回：**

类型说明struct如果操作成功返回一个[Input_KeyEvent](../../topics/input/Input_KeyEvent.md)指针对象，否则返回空指针。

#### OH_Input_DestroyKeyEvent()

```ets
void OH_Input_DestroyKeyEvent(struct Input_KeyEvent** keyEvent)
```

**描述**

销毁按键事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)** keyEvent按键事件对象。

#### OH_Input_SetKeyEventAction()

```ets
void OH_Input_SetKeyEventAction(struct Input_KeyEvent* keyEvent, int32_t action)
```

**描述**

设置按键事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

int32_t action按键事件类型。相关取值可参考[Input_KeyEventAction](#ZH-CN_TOPIC_0000002529445539__input_keyeventaction)。

#### OH_Input_GetKeyEventAction()

```ets
int32_t OH_Input_GetKeyEventAction(const struct Input_KeyEvent* keyEvent)
```

**描述**

获取按键事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

**返回：**

类型说明int32_t返回按键事件类型。相关取值可参考[Input_KeyEventAction](#ZH-CN_TOPIC_0000002529445539__input_keyeventaction)。

#### OH_Input_SetKeyEventKeyCode()

```ets
void OH_Input_SetKeyEventKeyCode(struct Input_KeyEvent* keyEvent, int32_t keyCode)
```

**描述**

设置按键事件的键值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

int32_t keyCode按键的键值。

#### OH_Input_GetKeyEventKeyCode()

```ets
int32_t OH_Input_GetKeyEventKeyCode(const struct Input_KeyEvent* keyEvent)
```

**描述**

获取按键事件的键值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

**返回：**

类型说明int32_tKey code.

#### OH_Input_SetKeyEventActionTime()

```ets
void OH_Input_SetKeyEventActionTime(struct Input_KeyEvent* keyEvent, int64_t actionTime)
```

**描述**

设置按键事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

int64_t actionTime按键事件发生的时间，表示从1970.1.1 00:00:00 GMT逝去的微秒数。

#### OH_Input_GetKeyEventActionTime()

```ets
int64_t OH_Input_GetKeyEventActionTime(const struct Input_KeyEvent* keyEvent)
```

**描述**

获取按键事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

**返回：**

类型说明int64_t返回按键事件发生的时间。

#### OH_Input_SetKeyEventWindowId()

```ets
void OH_Input_SetKeyEventWindowId(struct Input_KeyEvent* keyEvent, int32_t windowId)
```

**描述**

设置按键事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

int32_t windowId按键事件对应的窗口ID。

#### OH_Input_GetKeyEventWindowId()

```ets
int32_t OH_Input_GetKeyEventWindowId(const struct Input_KeyEvent* keyEvent)
```

**描述**

获取按键事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述const struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

**返回：**

类型说明int32_t按键事件的窗口ID。

#### OH_Input_GetKeyEventDisplayId()

```ets
int32_t OH_Input_GetKeyEventDisplayId(const struct Input_KeyEvent* keyEvent)
```

**描述**

获取按键事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述const struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

**返回：**

类型说明int32_t按键事件的屏幕ID。

#### OH_Input_SetKeyEventDisplayId()

```ets
void OH_Input_SetKeyEventDisplayId(struct Input_KeyEvent* keyEvent, int32_t displayId)
```

**描述**

设置按键事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述struct [Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

int32_t displayId按键事件对应的屏幕ID。

#### OH_Input_CreateMouseEvent()

```ets
struct Input_MouseEvent* OH_Input_CreateMouseEvent()
```

**描述**

创建鼠标事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**返回：**

类型说明struct如果操作成功返回一个[Input_MouseEvent](../../topics/input/Input_MouseEvent.md)指针对象，否则返回空指针。

#### OH_Input_DestroyMouseEvent()

```ets
void OH_Input_DestroyMouseEvent(struct Input_MouseEvent** mouseEvent)
```

**描述**

销毁鼠标事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)** mouseEvent鼠标事件对象。

#### OH_Input_SetMouseEventAction()

```ets
void OH_Input_SetMouseEventAction(struct Input_MouseEvent* mouseEvent, int32_t action)
```

**描述**

设置鼠标事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

int32_t action鼠标的动作。相关取值可参考[Input_MouseEventAction](#ZH-CN_TOPIC_0000002529445539__input_mouseeventaction)。

#### OH_Input_GetMouseEventAction()

```ets
int32_t OH_Input_GetMouseEventAction(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t鼠标的动作。

#### OH_Input_SetMouseEventDisplayX()

```ets
void OH_Input_SetMouseEventDisplayX(struct Input_MouseEvent* mouseEvent, int32_t displayX)
```

**描述**

设置鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

int32_t displayX鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。

#### OH_Input_GetMouseEventDisplayX()

```ets
int32_t OH_Input_GetMouseEventDisplayX(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。

#### OH_Input_SetMouseEventDisplayY()

```ets
void OH_Input_SetMouseEventDisplayY(struct Input_MouseEvent* mouseEvent, int32_t displayY)
```

**描述**

设置鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

int32_t displayY鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

#### OH_Input_GetMouseEventDisplayY()

```ets
int32_t OH_Input_GetMouseEventDisplayY(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

#### OH_Input_SetMouseEventButton()

```ets
void OH_Input_SetMouseEventButton(struct Input_MouseEvent* mouseEvent, int32_t button)
```

**描述**

设置鼠标事件的按键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

int32_t button鼠标按键。相关取值可参考[Input_MouseEventButton](#ZH-CN_TOPIC_0000002529445539__input_mouseeventbutton)。

#### OH_Input_GetMouseEventButton()

```ets
int32_t OH_Input_GetMouseEventButton(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件的按键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t鼠标按键。相关取值可参考[Input_MouseEventButton](#ZH-CN_TOPIC_0000002529445539__input_mouseeventbutton)。

#### OH_Input_SetMouseEventAxisType()

```ets
void OH_Input_SetMouseEventAxisType(struct Input_MouseEvent* mouseEvent, int32_t axisType)
```

**描述**

设置鼠标轴事件的类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

int32_t axisType鼠标轴类型，比如垂直轴、水平轴。相关取值可参考[InputEvent_MouseAxis](#ZH-CN_TOPIC_0000002529445539__inputevent_mouseaxis)。

#### OH_Input_GetMouseEventAxisType()

```ets
int32_t OH_Input_GetMouseEventAxisType(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标轴事件的类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t鼠标轴类型。相关取值可参考[InputEvent_MouseAxis](#ZH-CN_TOPIC_0000002529445539__inputevent_mouseaxis)。

#### OH_Input_SetMouseEventAxisValue()

```ets
void OH_Input_SetMouseEventAxisValue(struct Input_MouseEvent* mouseEvent, float axisValue)
```

**描述**

设置鼠标轴事件的值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

float axisValue轴事件的值，正数向前滚动（例如，1.0表示向前滚动一个单位），负数向后滚动（例如，-1.0表示向后滚动一个单位）,零表示没有滚动。

#### OH_Input_GetMouseEventAxisValue()

```ets
float OH_Input_GetMouseEventAxisValue(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标轴事件的值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明float轴事件的值。

#### OH_Input_SetMouseEventActionTime()

```ets
void OH_Input_SetMouseEventActionTime(struct Input_MouseEvent* mouseEvent, int64_t actionTime)
```

**描述**

设置鼠标事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

int64_t actionTime鼠标事件发生的时间，表示从1970.1.1 00:00:00 GMT逝去的微秒数。

#### OH_Input_GetMouseEventActionTime()

```ets
int64_t OH_Input_GetMouseEventActionTime(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int64_t返回鼠标事件发生的时间。

#### OH_Input_SetMouseEventWindowId()

```ets
void OH_Input_SetMouseEventWindowId(struct Input_MouseEvent* mouseEvent, int32_t windowId)
```

**描述**

设置鼠标事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

int32_t windowId鼠标事件的窗口ID。

#### OH_Input_GetMouseEventWindowId()

```ets
int32_t OH_Input_GetMouseEventWindowId(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t鼠标事件的窗口ID。

#### OH_Input_SetMouseEventDisplayId()

```ets
void OH_Input_SetMouseEventDisplayId(struct Input_MouseEvent* mouseEvent, int32_t displayId)
```

**描述**

设置鼠标事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

int32_t displayId鼠标事件的屏幕ID。

#### OH_Input_CreateTouchEvent()

```ets
struct Input_TouchEvent* OH_Input_CreateTouchEvent()
```

**描述**

创建触屏输入事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**返回：**

类型说明struct如果操作成功返回一个[Input_TouchEvent](../../topics/input/Input_TouchEvent.md)指针对象，否则返回空指针。

#### OH_Input_DestroyTouchEvent()

```ets
void OH_Input_DestroyTouchEvent(struct Input_TouchEvent** touchEvent)
```

**描述**

销毁触屏输入事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)** touchEvent触屏输入事件对象。

#### OH_Input_SetTouchEventAction()

```ets
void OH_Input_SetTouchEventAction(struct Input_TouchEvent* touchEvent, int32_t action)
```

**描述**

设置触屏输入事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

int32_t action触屏的动作。相关取值可参考[Input_TouchEventAction](#ZH-CN_TOPIC_0000002529445539__input_toucheventaction)。

#### OH_Input_GetTouchEventAction()

```ets
int32_t OH_Input_GetTouchEventAction(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int32_t触屏的动作。相关取值可参考[Input_TouchEventAction](#ZH-CN_TOPIC_0000002529445539__input_toucheventaction)。

#### OH_Input_SetTouchEventFingerId()

```ets
void OH_Input_SetTouchEventFingerId(struct Input_TouchEvent* touchEvent, int32_t id)
```

**描述**

设置触屏输入事件的手指ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

int32_t id触屏的手指ID。第一个手指碰到屏幕，ID就是0，第二个手指碰到屏幕，ID就是1，依次累加。

#### OH_Input_GetTouchEventFingerId()

```ets
int32_t OH_Input_GetTouchEventFingerId(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件的手指ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int32_t触屏的手指ID。第一个手指碰到屏幕，ID就是0，第二个手指碰到屏幕，ID就是1，依次累加。

#### OH_Input_SetTouchEventDisplayX()

```ets
void OH_Input_SetTouchEventDisplayX(struct Input_TouchEvent* touchEvent, int32_t displayX)
```

**描述**

设置触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

int32_t displayX触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。

#### OH_Input_GetTouchEventDisplayX()

```ets
int32_t OH_Input_GetTouchEventDisplayX(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int32_t触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。

#### OH_Input_SetTouchEventDisplayY()

```ets
void OH_Input_SetTouchEventDisplayY(struct Input_TouchEvent* touchEvent, int32_t displayY)
```

**描述**

设置触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

int32_t displayY触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

#### OH_Input_GetTouchEventDisplayY()

```ets
int32_t OH_Input_GetTouchEventDisplayY(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int32_t触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

#### OH_Input_SetTouchEventActionTime()

```ets
void OH_Input_SetTouchEventActionTime(struct Input_TouchEvent* touchEvent, int64_t actionTime)
```

**描述**

设置触屏输入事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

int64_t actionTime触屏输入事件发生的时间，表示从1970.1.1 00:00:00 GMT逝去的微秒数。

#### OH_Input_GetTouchEventActionTime()

```ets
int64_t OH_Input_GetTouchEventActionTime(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int64_t返回触屏输入事件发生的时间。

#### OH_Input_SetTouchEventWindowId()

```ets
void OH_Input_SetTouchEventWindowId(struct Input_TouchEvent* touchEvent, int32_t windowId)
```

**描述**

设置触屏输入事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

int32_t windowId触屏输入事件的窗口ID。

#### OH_Input_GetTouchEventWindowId()

```ets
int32_t OH_Input_GetTouchEventWindowId(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int32_t触屏输入事件的窗口ID。

#### OH_Input_SetTouchEventDisplayId()

```ets
void OH_Input_SetTouchEventDisplayId(struct Input_TouchEvent* touchEvent, int32_t displayId)
```

**描述**

设置触屏输入事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

int32_t displayId触屏输入事件的屏幕ID。

#### OH_Input_GetTouchEventDisplayId()

```ets
int32_t OH_Input_GetTouchEventDisplayId(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int32_t触屏输入事件的屏幕ID。

#### OH_Input_CancelInjection()

```ets
void OH_Input_CancelInjection()
```

**描述**

取消事件注入并撤销授权。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

#### OH_Input_RequestInjection()

```ets
Input_Result OH_Input_RequestInjection(Input_InjectAuthorizeCallback callback)
```

**描述**

当前应用申请注入权限，包括申请注入按键事件[OH_Input_InjectKeyEvent](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__oh_input_injectkeyevent)、注入触屏输入事件[OH_Input_InjectTouchEvent](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__oh_input_injecttouchevent)、注入鼠标事件[OH_Input_InjectMouseEvent](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__oh_input_injectmouseevent)等注入操作的权限。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**设备行为差异**：该接口仅在PC/2in1设备上生效，在其他设备上返回801错误码。

**起始版本：** 20

**参数：**

参数项描述[Input_InjectAuthorizeCallback](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_injectauthorizecallback) callback授权状态回调，具体请参考[Input_InjectAuthorizeCallback](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_injectauthorizecallback)。

**返回：**

类型说明[Input_Result](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_result)

返回结果码，参见[Input_Result](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_result)。

 INPUT_SUCCESS = 0 申请授权成功，等待用户授权结果并回调授权状态。

 INPUT_PARAMETER_ERROR = 401 参数错误，参数callback为空。

 INPUT_DEVICE_NOT_SUPPORTED = 801 表示不支持该功能。

 INPUT_SERVICE_EXCEPTION = 3800001 服务器错误。

 INPUT_INJECTION_AUTHORIZING = 3900005 正在授权中。

 INPUT_INJECTION_OPERATION_FREQUENT = 3900006 重复请求（当前应用连续申请授权弹窗成功，间隔时间不超过3秒）。

 INPUT_INJECTION_AUTHORIZED = 3900007 当前应用已经授权。

 INPUT_INJECTION_AUTHORIZED_OTHERS = 3900008 其它应用已经授权。

#### OH_Input_QueryAuthorizedStatus()

```ets
Input_Result OH_Input_QueryAuthorizedStatus(Input_InjectionStatus* status)
```

**描述**

查询当前应用注入的权限状态。

**起始版本：** 20

**参数：**

参数项描述[Input_InjectionStatus](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_injectionstatus)* status当前应用注入权限状态。参见[Input_InjectionStatus](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_injectionstatus)。

**返回：**

类型说明[Input_Result](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_result)

返回结果码，参见[Input_Result](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_result)。

 INPUT_SUCCESS = 0 查询成功。

 INPUT_PARAMETER_ERROR = 401 参数错误，参数status为空。

 INPUT_SERVICE_EXCEPTION = 3800001 服务器错误。

#### OH_Input_CreateAxisEvent()

```ets
Input_AxisEvent* OH_Input_CreateAxisEvent(void)
```

**描述**

创建轴事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**返回：**

类型说明Input_AxisEvent*成功返回[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)对象实例，失败则返回null。

#### OH_Input_DestroyAxisEvent()

```ets
Input_Result OH_Input_DestroyAxisEvent(Input_AxisEvent** axisEvent)
```

**描述**

销毁轴事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)** axisEvent轴事件对象实例的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若销毁成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent为NULL或者axisEvent为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetAxisEventAction()

```ets
Input_Result OH_Input_SetAxisEventAction(Input_AxisEvent* axisEvent, InputEvent_AxisAction action)
```

**描述**

设置轴事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

[InputEvent_AxisAction](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axisaction) action轴事件动作，具体请参考[InputEvent_AxisAction](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axisaction)。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若设置轴事件的动作成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_GetAxisEventAction()

```ets
Input_Result OH_Input_GetAxisEventAction(const Input_AxisEvent* axisEvent, InputEvent_AxisAction *action)
```

**描述**

获取轴事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

[InputEvent_AxisAction](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axisaction) *actionaction 出参，返回轴事件动作，具体请参考在[InputEvent_AxisAction](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axisaction)。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若获取轴事件的动作成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent或者action为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetAxisEventDisplayX()

```ets
Input_Result OH_Input_SetAxisEventDisplayX(Input_AxisEvent* axisEvent, float displayX)
```

**描述**

设置轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

float displayX轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若设置轴事件的X坐标成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_GetAxisEventDisplayX()

```ets
Input_Result OH_Input_GetAxisEventDisplayX(const Input_AxisEvent* axisEvent, float* displayX)
```

**描述**

获取轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

float* displayX出参，返回轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若获取轴事件的X坐标成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent或者displayX为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetAxisEventDisplayY()

```ets
Input_Result OH_Input_SetAxisEventDisplayY(Input_AxisEvent* axisEvent, float displayY)
```

**描述**

设置轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

float displayY轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若设置轴事件的Y坐标成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_GetAxisEventDisplayY()

```ets
Input_Result OH_Input_GetAxisEventDisplayY(const Input_AxisEvent* axisEvent, float* displayY)
```

**描述**

获取轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

float* displayY出参，返回轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若获取轴事件的Y坐标成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent或者displayY为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetAxisEventAxisValue()

```ets
Input_Result OH_Input_SetAxisEventAxisValue(Input_AxisEvent* axisEvent,InputEvent_AxisType axisType, double axisValue)
```

**描述**

设置轴事件指定轴类型的轴值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

[InputEvent_AxisType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axistype) axisType轴类型，具体请参考[InputEvent_AxisType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axistype)。double axisValue轴事件的值，正数向前滚动（例如，1.0表示向前滚动一个单位），负数向后滚动（例如，-1.0表示向后滚动一个单位）,零表示没有滚动。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若设置轴事件指定轴类型的轴值成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_GetAxisEventAxisValue()

```ets
Input_Result OH_Input_GetAxisEventAxisValue(const Input_AxisEvent* axisEvent,InputEvent_AxisType axisType, double* axisValue)
```

**描述**

获取轴事件指定轴类型的轴值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

[InputEvent_AxisType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axistype) axisType轴类型，具体请参考[InputEvent_AxisType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axistype)。double* axisValue出参，返回轴事件的值，正数向前滚动（例如，1.0表示向前滚动一个单位），负数向后滚动（例如，-1.0表示向后滚动一个单位）,零表示没有滚动。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若获取轴事件指定轴类型的轴值成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent或者axisValue为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetAxisEventActionTime()

```ets
Input_Result OH_Input_SetAxisEventActionTime(Input_AxisEvent* axisEvent, int64_t actionTime)
```

**描述**

设置轴事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

int64_t actionTime轴事件发生的时间，表示从1970.1.1 00:00:00 GMT逝去的微秒数。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若设置轴事件发生的时间成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_GetAxisEventActionTime()

```ets
Input_Result OH_Input_GetAxisEventActionTime(const Input_AxisEvent* axisEvent, int64_t* actionTime)
```

**描述**

获取轴事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

int64_t* actionTime出参，返回轴事件发生的时间，表示从1970.1.1 00:00:00 GMT逝去的微秒数。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若获取轴事件发生的时间成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent或者actionTime为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetAxisEventType()

```ets
Input_Result OH_Input_SetAxisEventType(Input_AxisEvent* axisEvent, InputEvent_AxisEventType axisEventType)
```

**描述**

设置轴事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype) axisEventType轴事件类型，具体请参考[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若设置轴事件类型成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_GetAxisEventType()

```ets
Input_Result OH_Input_GetAxisEventType(const Input_AxisEvent* axisEvent, InputEvent_AxisEventType* axisEventType)
```

**描述**

获取轴事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)* axisEventType出参，返回轴事件类型，具体请参考[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若获取轴事件类型成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent或者axisEventType为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetAxisEventSourceType()

```ets
Input_Result OH_Input_SetAxisEventSourceType(Input_AxisEvent* axisEvent, InputEvent_SourceType sourceType)
```

**描述**

设置轴事件源类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

[InputEvent_SourceType](#ZH-CN_TOPIC_0000002529445539__inputevent_sourcetype) sourceType轴事件源类型,具体请参考[InputEvent_SourceType](#ZH-CN_TOPIC_0000002529445539__inputevent_sourcetype)。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若设置轴事件源类型成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_GetAxisEventSourceType()

```ets
Input_Result OH_Input_GetAxisEventSourceType(const Input_AxisEvent* axisEvent, InputEvent_SourceType* sourceType)
```

**描述**

获取轴事件源类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

[InputEvent_SourceType](#ZH-CN_TOPIC_0000002529445539__inputevent_sourcetype)* sourceType出参，返回轴事件源类型，具体请参考[InputEvent_SourceType](#ZH-CN_TOPIC_0000002529445539__inputevent_sourcetype)。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若获取轴事件源类型成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent或者sourceType为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetAxisEventWindowId()

```ets
Input_Result OH_Input_SetAxisEventWindowId(Input_AxisEvent* axisEvent, int32_t windowId)
```

**描述**

设置轴事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

int32_t windowId轴事件窗口ID。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若设置轴事件的窗口ID成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_GetAxisEventWindowId()

```ets
Input_Result OH_Input_GetAxisEventWindowId(const Input_AxisEvent* axisEvent, int32_t* windowId)
```

**描述**

获取轴事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

int32_t* windowId出参，返回轴事件窗口ID。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若获取轴事件的窗口ID成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent或者windowId为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetAxisEventDisplayId()

```ets
Input_Result OH_Input_SetAxisEventDisplayId(Input_AxisEvent* axisEvent, int32_t displayId)
```

**描述**

设置轴事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述[Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

int32_t displayId轴事件屏幕ID。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若设置轴事件的屏幕ID成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_GetAxisEventDisplayId()

```ets
Input_Result OH_Input_GetAxisEventDisplayId(const Input_AxisEvent* axisEvent, int32_t* displayId)
```

**描述**

获取轴事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

int32_t* displayId出参，返回轴事件屏幕ID。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)若获取轴事件的屏幕ID成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若axisEvent或者displayId为NULL，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_AddKeyEventMonitor()

```ets
Input_Result OH_Input_AddKeyEventMonitor(Input_KeyEventCallback callback)
```

**描述**

添加按键事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT_MONITORING

**起始版本：** 12

**参数：**

参数项描述[Input_KeyEventCallback](#ZH-CN_TOPIC_0000002529445539__input_keyeventcallback) callback回调函数，用于接收按键事件。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若添加按键事件监听成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_AddMouseEventMonitor()

```ets
Input_Result OH_Input_AddMouseEventMonitor(Input_MouseEventCallback callback)
```

**描述**

添加鼠标事件监听,包含鼠标点击，移动，不包含滚轮事件，滚轮事件归属于轴事件。

该接口处于录屏场景时才允许调用，否则调用该接口不生效。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT_MONITORING

**起始版本：** 12

**参数：**

参数项描述[Input_MouseEventCallback](#ZH-CN_TOPIC_0000002529445539__input_mouseeventcallback) callback回调函数，用于接收鼠标事件。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若添加鼠标事件监听成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_AddTouchEventMonitor()

```ets
Input_Result OH_Input_AddTouchEventMonitor(Input_TouchEventCallback callback)
```

**描述**

添加触屏输入事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT_MONITORING

**起始版本：** 12

**参数：**

参数项描述[Input_TouchEventCallback](#ZH-CN_TOPIC_0000002529445539__input_toucheventcallback) callback回调函数，用于接收触屏输入事件。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若添加触屏输入事件监听成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_AddAxisEventMonitorForAll()

```ets
Input_Result OH_Input_AddAxisEventMonitorForAll(Input_AxisEventCallback callback)
```

**描述**

添加所有类型轴事件监听，轴事件类型定义在[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)中。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT_MONITORING

**起始版本：** 12

**参数：**

参数项描述[Input_AxisEventCallback](#ZH-CN_TOPIC_0000002529445539__input_axiseventcallback) callback回调函数，用于接收轴事件。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若添加轴事件监听成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_AddAxisEventMonitor()

```ets
Input_Result OH_Input_AddAxisEventMonitor(InputEvent_AxisEventType axisEventType, Input_AxisEventCallback callback)
```

**描述**

添加指定类型的轴事件监听，轴事件类型定义在[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)中。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT_MONITORING

**起始版本：** 12

**参数：**

参数项描述[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype) axisEventType要监听的轴事件类型，轴事件类型定义在[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)中。[Input_AxisEventCallback](#ZH-CN_TOPIC_0000002529445539__input_axiseventcallback) callback回调函数，用于接收指定类型的轴事件

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若添加轴事件监听成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_RemoveKeyEventMonitor()

```ets
Input_Result OH_Input_RemoveKeyEventMonitor(Input_KeyEventCallback callback)
```

**描述**

移除按键事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT_MONITORING

**起始版本：** 12

**参数：**

参数项描述[Input_KeyEventCallback](#ZH-CN_TOPIC_0000002529445539__input_keyeventcallback) callback指定要被移除的用于按键事件监听的回调函数。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若移除按键事件监听成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空或者没有被添加监听，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_RemoveMouseEventMonitor()

```ets
Input_Result OH_Input_RemoveMouseEventMonitor(Input_MouseEventCallback callback)
```

**描述**

移除鼠标事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT_MONITORING

**起始版本：** 12

**参数：**

参数项描述[Input_MouseEventCallback](#ZH-CN_TOPIC_0000002529445539__input_mouseeventcallback) callback指定要被移除的用于鼠标事件监听的回调函数。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若移除鼠标事件监听成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空或者没有被添加监听，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_RemoveTouchEventMonitor()

```ets
Input_Result OH_Input_RemoveTouchEventMonitor(Input_TouchEventCallback callback)
```

**描述**

移除触屏输入事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT_MONITORING

**起始版本：** 12

**参数：**

参数项描述[Input_TouchEventCallback](#ZH-CN_TOPIC_0000002529445539__input_toucheventcallback) callback指定要被移除的用于触屏输入事件监听的回调函数。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若移除触屏输入事件监听成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空或者没有被添加监听，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_RemoveAxisEventMonitorForAll()

```ets
Input_Result OH_Input_RemoveAxisEventMonitorForAll(Input_AxisEventCallback callback)
```

**描述**

移除所有类型轴事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT_MONITORING

**起始版本：** 12

**参数：**

参数项描述[Input_AxisEventCallback](#ZH-CN_TOPIC_0000002529445539__input_axiseventcallback) callback指定要被移除的用于所有类型轴事件监听的回调函数。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若移除轴事件监听成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空或者没有被添加监听，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_RemoveAxisEventMonitor()

```ets
Input_Result OH_Input_RemoveAxisEventMonitor(InputEvent_AxisEventType axisEventType, Input_AxisEventCallback callback)
```

**描述**

移除指定类型轴事件监听，轴事件类型定义在[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)中。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT_MONITORING

**起始版本：** 12

**参数：**

参数项描述[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype) axisEventType指定要移除监听的轴事件类型，轴事件类型定义在[InputEvent_AxisEventType](oh_axis_type.h.md#ZH-CN_TOPIC_0000002529285565__inputevent_axiseventtype)中。[Input_AxisEventCallback](#ZH-CN_TOPIC_0000002529445539__input_axiseventcallback) callback指定要被移除的用于指定类型轴事件监听的回调函数。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若移除轴事件监听成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空或者没有被添加监听，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_AddKeyEventInterceptor()

```ets
Input_Result OH_Input_AddKeyEventInterceptor(Input_KeyEventCallback callback, Input_InterceptorOptions *option)
```

**描述**

添加按键事件的拦截，重复添加只有第一次生效。仅在应用获焦时拦截按键事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INTERCEPT_INPUT_EVENT

**起始版本：** 12

**参数：**

参数项描述[Input_KeyEventCallback](#ZH-CN_TOPIC_0000002529445539__input_keyeventcallback) callback回调函数，用于接收按键事件。[Input_InterceptorOptions](../../topics/input/Input_InterceptorOptions.md) *optionoption 输入事件拦截的可选项，传null则使用默认值。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若添加按键事件的拦截成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若重复添加拦截器，则返回[INPUT_REPEAT_INTERCEPTOR](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若服务异常；则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_AddInputEventInterceptor()

```ets
Input_Result OH_Input_AddInputEventInterceptor(Input_InterceptorEventCallback *callback,Input_InterceptorOptions *option)
```

**描述**

添加输入事件拦截，包括鼠标、触屏和轴事件，重复添加只有第一次生效。仅命中应用窗口时拦截输入事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INTERCEPT_INPUT_EVENT

**起始版本：** 12

**参数：**

参数项描述[Input_InterceptorEventCallback](../../topics/input/Input_InterceptorEventCallback.md) *callbackcallback 用于回调输入事件的结构体指针，请参考定义[Input_InterceptorEventCallback](../../topics/input/Input_InterceptorEventCallback.md)。[Input_InterceptorOptions](../../topics/input/Input_InterceptorOptions.md) *optionoption 输入事件拦截的可选项，传null则使用默认值。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若添加输入事件的拦截成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若callback为空，则返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)；若重复添加拦截器，则返回[INPUT_REPEAT_INTERCEPTOR](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若服务异常；则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_RemoveKeyEventInterceptor()

```ets
Input_Result OH_Input_RemoveKeyEventInterceptor(void)
```

**描述**

移除按键事件拦截。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INTERCEPT_INPUT_EVENT

**起始版本：** 12

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若移除按键事件拦截成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_RemoveInputEventInterceptor()

```ets
Input_Result OH_Input_RemoveInputEventInterceptor(void)
```

**描述**

移除输入事件拦截，包括鼠标、触屏和轴事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INTERCEPT_INPUT_EVENT

**起始版本：** 12

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

若移除输入事件拦截成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若权限校验失败，则返回[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若服务异常，则返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_GetIntervalSinceLastInput()

```ets
Input_Result OH_Input_GetIntervalSinceLastInput(int64_t *timeInterval)
```

**描述**

获取距离上次系统输入事件的时间间隔。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述int64_t *timeIntervaltimeInterval 时间间隔，单位：μs。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetIntervalSinceLastInput 函数错误码。

 若获取时间间隔成功，则返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若获取失败，返回[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_CreateHotkey()

```ets
Input_Hotkey *OH_Input_CreateHotkey(void)
```

**描述**

创建快捷键对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**返回：**

类型说明[Input_Hotkey](../../topics/input/Input_Hotkey.md)如果操作成功,则返回一个[Input_Hotkey](../../topics/input/Input_Hotkey.md)指针对象。否则, 返回一个空指针， 可能的原因是内存分配失败。

#### OH_Input_DestroyHotkey()

```ets
void OH_Input_DestroyHotkey(Input_Hotkey **hotkey)
```

**描述**

销毁快捷键对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述[Input_Hotkey](../../topics/input/Input_Hotkey.md) **hotkeyhotkey 快捷键对象的实例。

#### OH_Input_SetPreKeys()

```ets
void OH_Input_SetPreKeys(Input_Hotkey *hotkey, int32_t *preKeys, int32_t size)
```

**描述**

设置修饰键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述[Input_Hotkey](../../topics/input/Input_Hotkey.md) *hotkeyhotkey 快捷键对象的实例。int32_t *preKeyspreKeys 修饰键列表。int32_t size修饰键个数， 取值范围1~2个。

#### OH_Input_GetPreKeys()

```ets
Input_Result OH_Input_GetPreKeys(const Input_Hotkey *hotkey, int32_t **preKeys, int32_t *preKeyCount)
```

**描述**

获取修饰键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述const [Input_Hotkey](../../topics/input/Input_Hotkey.md) *hotkeyhotkey 快捷键对象的实例。int32_t **preKeyspreKeys 返回修饰键列表。int32_t *preKeyCountpreKeyCount 返回修饰键个数。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetPreKeys 函数错误码。

 若获取成功，返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；若获取失败，返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetFinalKey()

```ets
void OH_Input_SetFinalKey(Input_Hotkey* hotkey, int32_t finalKey)
```

**描述**

设置被修饰键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述[Input_Hotkey](../../topics/input/Input_Hotkey.md)* hotkey快捷键对象的实例。int32_t finalKey被修饰键值，被修饰键值只能是1个。

#### OH_Input_GetFinalKey()

```ets
Input_Result OH_Input_GetFinalKey(const Input_Hotkey* hotkey, int32_t *finalKeyCode)
```

**描述**

获取被修饰键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述const [Input_Hotkey](../../topics/input/Input_Hotkey.md)* hotkey快捷键对象的实例。int32_t *finalKeyCodefinalKeyCode 返回被修饰键键值。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetFinalKey 函数错误码。

 若获取成功，返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若获取失败，返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_CreateAllSystemHotkeys()

```ets
Input_Hotkey **OH_Input_CreateAllSystemHotkeys(int32_t count)
```

**描述**

创建[Input_Hotkey](../../topics/input/Input_Hotkey.md)类型实例的数组。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述int32_t count创建[Input_Hotkey](../../topics/input/Input_Hotkey.md)实例的数量。

**返回：**

类型说明[Input_Hotkey](../../topics/input/Input_Hotkey.md)

OH_Input_CreateAllSystemHotkeys 函数错误码。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 创建实例数组的双指针成功。

#### OH_Input_DestroyAllSystemHotkeys()

```ets
void OH_Input_DestroyAllSystemHotkeys(Input_Hotkey **hotkeys, int32_t count)
```

**描述**

销毁[Input_Hotkey](../../topics/input/Input_Hotkey.md)实例数组并回收内存。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述[Input_Hotkey](../../topics/input/Input_Hotkey.md) **hotkeyshotkeys 指向[Input_Hotkey](../../topics/input/Input_Hotkey.md)实例数组的双指针。int32_t count销毁[Input_Hotkey](../../topics/input/Input_Hotkey.md)实例的数量。

#### OH_Input_GetAllSystemHotkeys()

```ets
Input_Result OH_Input_GetAllSystemHotkeys(Input_Hotkey **hotkey, int32_t *count)
```

**描述**

获取设置的所有快捷键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述[Input_Hotkey](../../topics/input/Input_Hotkey.md) **hotkeyhotkey 返回[Input_Hotkey](../../topics/input/Input_Hotkey.md) 类型实例数组。首次调用可传入NULL，可获取数组长度。int32_t *countcount 返回支持快捷键的个数。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetAllSystemHotkeys 函数错误码。

 若获取成功，返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若获取失败，返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_SetRepeat()

```ets
void OH_Input_SetRepeat(Input_Hotkey* hotkey, bool isRepeat)
```

**描述**

设置是否上报重复key事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述[Input_Hotkey](../../topics/input/Input_Hotkey.md)* hotkey快捷键对象的实例。bool isRepeat是否上报重复key事件。true表示上报，false表示不上报。

#### OH_Input_GetRepeat()

```ets
Input_Result OH_Input_GetRepeat(const Input_Hotkey* hotkey, bool *isRepeat)
```

**描述**

获取是否上报重复key事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述const [Input_Hotkey](../../topics/input/Input_Hotkey.md)* hotkey快捷键对象的实例。bool *isRepeatisRepeat 返回Key事件是否重复。true表示重复，false表示不重复。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetRepeat 函数错误码。

 若获取成功，返回[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result)；

 若获取失败，返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

#### OH_Input_AddHotkeyMonitor()

```ets
Input_Result OH_Input_AddHotkeyMonitor(const Input_Hotkey* hotkey, Input_HotkeyCallback callback)
```

**描述**

订阅快捷键事件。此接口在智能穿戴、轻量级智能穿戴设备不生效。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述const [Input_Hotkey](../../topics/input/Input_Hotkey.md)* hotkey指定要订阅的快捷键对象。[Input_HotkeyCallback](#ZH-CN_TOPIC_0000002529445539__input_hotkeycallback) callback回调函数，用于回调快捷键事件。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_AddHotkeyMonitor 函数错误码。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示订阅组合按键成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 参数检查失败。

[INPUT_OCCUPIED_BY_SYSTEM](#ZH-CN_TOPIC_0000002529445539__input_result) 该快捷键已被系统占用，可以通过接口[OH_Input_GetAllSystemHotkeys](#ZH-CN_TOPIC_0000002529445539__oh_input_getallsystemhotkeys)查询所有的系统快捷键。

[INPUT_OCCUPIED_BY_OTHER](#ZH-CN_TOPIC_0000002529445539__input_result) 已被抢占订阅。

[INPUT_DEVICE_NOT_SUPPORTED](#ZH-CN_TOPIC_0000002529445539__input_result) 表示不支持该功能。

#### OH_Input_RemoveHotkeyMonitor()

```ets
Input_Result OH_Input_RemoveHotkeyMonitor(const Input_Hotkey* hotkey, Input_HotkeyCallback callback)
```

**描述**

取消订阅快捷键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

参数项描述const [Input_Hotkey](../../topics/input/Input_Hotkey.md)* hotkey指定要取消订阅的快捷键对象。[Input_HotkeyCallback](#ZH-CN_TOPIC_0000002529445539__input_hotkeycallback) callback回调函数，用于回调快捷键事件。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_RemoveHotkeyMonitor 函数错误码。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 取消订阅组合按键成功， [INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 参数检查失败。

#### OH_Input_RegisterDeviceListener()

```ets
Input_Result OH_Input_RegisterDeviceListener(Input_DeviceListener* listener)
```

**描述**

注册设备热插拔的监听器。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述[Input_DeviceListener](../../topics/components/Input_DeviceListener.md)* listener指向设备热插拔监听器[Input_DeviceListener](../../topics/components/Input_DeviceListener.md)的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_RegisterDeviceListener 的返回值。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示注册成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示listener 为NULL。

#### OH_Input_UnregisterDeviceListener()

```ets
Input_Result OH_Input_UnregisterDeviceListener(Input_DeviceListener* listener)
```

**描述**

取消注册设备热插拔的监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述[Input_DeviceListener](../../topics/components/Input_DeviceListener.md)* listener指向设备热插拔监听器[Input_DeviceListener](../../topics/components/Input_DeviceListener.md)的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_UnregisterDeviceListener 的返回值。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示取消注册成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示listener 为 NULL 或者 listener 未被注册。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示由于服务异常调用失败。

#### OH_Input_UnregisterDeviceListeners()

```ets
Input_Result OH_Input_UnregisterDeviceListeners()
```

**描述**

取消注册所有的设备热插拔的监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_UnregisterDeviceListener 的返回值。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示调用成功。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示由于服务异常调用失败。

#### OH_Input_GetDeviceIds()

```ets
Input_Result OH_Input_GetDeviceIds(int32_t *deviceIds, int32_t inSize, int32_t *outSize)
```

**描述**

获取所有输入设备的ID列表。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述int32_t *deviceIdsdeviceIds 保存输入设备ID的列表。int32_t inSize保存输入设备ID列表的大小。int32_t *outSizeoutSize 输出输入设备ID列表的长度，值小于等于inSize长度。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示deviceIds或outSize为空指针或inSize小于0。

#### OH_Input_GetDevice()

```ets
Input_Result OH_Input_GetDevice(int32_t deviceId, Input_DeviceInfo **deviceInfo)
```

**描述**

获取输入设备信息。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述int32_t deviceId输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md) **deviceInfodeviceInfo 指向输入设备信息[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md)的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示deviceInfo为空指针或deviceId无效。

 可以通过 [OH_Input_GetDeviceIds](#ZH-CN_TOPIC_0000002529445539__oh_input_getdeviceids) 表示接口查询系统支持的设备ID。

#### OH_Input_CreateDeviceInfo()

```ets
Input_DeviceInfo* OH_Input_CreateDeviceInfo(void)
```

**描述**

创建输入设备信息的对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**返回：**

类型说明Input_DeviceInfo*如果操作成功，返回设备信息[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md)实例的指针。否则返回空指针，可能的原因是分配内存失败。

#### OH_Input_DestroyDeviceInfo()

```ets
void OH_Input_DestroyDeviceInfo(Input_DeviceInfo **deviceInfo)
```

**描述**

销毁输入设备信息的对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md) **deviceInfodeviceInfo 设备信息的对象。

#### OH_Input_GetKeyboardType()

```ets
Input_Result OH_Input_GetKeyboardType(int32_t deviceId, int32_t *keyboardType)
```

**描述**

获取输入设备的键盘类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述int32_t deviceId输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。int32_t *keyboardTypekeyboardType 指向输入设备的键盘指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示设备ID为无效值或者keyboardType是空指针。

#### OH_Input_GetDeviceId()

```ets
Input_Result OH_Input_GetDeviceId(Input_DeviceInfo *deviceInfo, int32_t *id)
```

**描述**

获取输入设备的ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md) *deviceInfodeviceInfo 输入设备信息[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md)。int32_t *idid 指向输入设备ID的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示deviceInfo或者ID是空指针。

#### OH_Input_GetDeviceName()

```ets
Input_Result OH_Input_GetDeviceName(Input_DeviceInfo *deviceInfo, char **name)
```

**描述**

获取输入设备的名称。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md) *deviceInfodeviceInfo 输入设备信息[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md)。char **namename 指向输入设备名称的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示deviceInfo或者name是空指针。

#### OH_Input_GetCapabilities()

```ets
Input_Result OH_Input_GetCapabilities(Input_DeviceInfo *deviceInfo, int32_t *capabilities)
```

**描述**

获取有关输入设备能力信息，比如设备是触摸屏、触控板、键盘等。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md) *deviceInfodeviceInfo 输入设备信息[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md)。int32_t *capabilitiescapabilities 指向输入设备能力信息的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示deviceInfo或者capabilities是空指针。

#### OH_Input_GetDeviceVersion()

```ets
Input_Result OH_Input_GetDeviceVersion(Input_DeviceInfo *deviceInfo, int32_t *version)
```

**描述**

获取输入设备的版本信息。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md) *deviceInfodeviceInfo 输入设备信息[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md)。int32_t *versionversion 指向输入设备版本信息的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示deviceInfo或者version是空指针。

#### OH_Input_GetDeviceProduct()

```ets
Input_Result OH_Input_GetDeviceProduct(Input_DeviceInfo *deviceInfo, int32_t *product)
```

**描述**

获取输入设备的产品信息。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md) *deviceInfodeviceInfo 输入设备信息[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md)。int32_t *productproduct 指向输入设备产品信息的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示deviceInfo或者product是空指针。

#### OH_Input_GetDeviceVendor()

```ets
Input_Result OH_Input_GetDeviceVendor(Input_DeviceInfo *deviceInfo, int32_t *vendor)
```

**描述**

获取输入设备的厂商信息。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md) *deviceInfodeviceInfo 输入设备信息[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md)。int32_t *vendorvendor 指向输入设备厂商信息的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示deviceInfo或者vendor是空指针。

#### OH_Input_GetDeviceAddress()

```ets
Input_Result OH_Input_GetDeviceAddress(Input_DeviceInfo *deviceInfo, char **address)
```

**描述**

获取输入设备的物理地址。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

参数项描述[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md) *deviceInfodeviceInfo 输入设备信息[Input_DeviceInfo](../../topics/system-services/Input_DeviceInfo.md)。char **addressaddress 指向输入设备物理地址的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示deviceInfo或者address是空指针。

#### OH_Input_GetFunctionKeyState()

```ets
Input_Result OH_Input_GetFunctionKeyState(int32_t keyCode, int32_t *state)
```

**描述**

获取功能键状态。

**起始版本：** 15

**参数：**

参数项描述int32_t keyCode功能键值。目前仅支持CapsLock键，键值为1。int32_t *statestate 功能键状态。0表示功能键关闭，1表示功能键打开。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetFunctionKeyState的执行结果。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示获取状态成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数错误。

[INPUT_KEYBOARD_DEVICE_NOT_EXIST](#ZH-CN_TOPIC_0000002529445539__input_result) 表示键盘设备不存在。

#### OH_Input_InjectTouchEvent()

```ets
int32_t OH_Input_InjectTouchEvent(const struct Input_TouchEvent* touchEvent)
```

**描述**

使用以指定屏幕左上角为原点的相对坐标系的坐标注入触屏输入事件。

如果当前处于用户未授权状态，调用该接口注入事件不生效。

从API version 20开始，建议先使用[OH_Input_RequestInjection](#ZH-CN_TOPIC_0000002529445539__oh_input_requestinjection)请求授权。然后通过[OH_Input_QueryAuthorizedStatus](#ZH-CN_TOPIC_0000002529445539__oh_input_queryauthorizedstatus)查询授权状态，当授权状态为[AUTHORIZED](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_injectionstatus)时，再使用该接口。

**起始版本：** 12

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int32_t

OH_Input_InjectTouchEvent的执行结果。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示注入成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数错误。

[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result) 表示缺少权限。

#### OH_Input_InjectMouseEvent()

```ets
int32_t OH_Input_InjectMouseEvent(const struct Input_MouseEvent* mouseEvent)
```

**描述**

使用以指定屏幕左上角为原点的相对坐标系的坐标注入鼠标事件。

如果当前处于用户未授权状态，调用该接口注入事件不生效。

从API version 20开始，建议先使用[OH_Input_RequestInjection](#ZH-CN_TOPIC_0000002529445539__oh_input_requestinjection)请求授权。然后通过[OH_Input_QueryAuthorizedStatus](#ZH-CN_TOPIC_0000002529445539__oh_input_queryauthorizedstatus)查询授权状态，当授权状态为[AUTHORIZED](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_injectionstatus)时，再使用该接口。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t

OH_Input_InjectTouchEvent的执行结果。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示注入成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数错误。

[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result) 表示缺少权限。

#### OH_Input_GetMouseEventDisplayId()

```ets
int32_t OH_Input_GetMouseEventDisplayId(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t若获取鼠标事件的屏幕ID成功，则返回鼠标事件的屏幕ID；若mouseEvent为NULL，则返回-1。

#### OH_Input_QueryMaxTouchPoints()

```ets
Input_Result OH_Input_QueryMaxTouchPoints(int32_t *count)
```

**描述**

查询设备支持的最大触屏报点数。

**起始版本：** 20

**参数：**

参数项描述int32_t *count设备支持的最大触屏报点数，count取值范围为0-10，-1表示未知数量。

**返回：**

类型说明[Input_Result](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_QueryMaxTouchPoints的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示查询成功。

[INPUT_PARAMETER_ERROR](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数错误。

#### OH_Input_InjectMouseEventGlobal()

```ets
int32_t OH_Input_InjectMouseEventGlobal(const struct Input_MouseEvent* mouseEvent)
```

**描述**

使用以主屏左上角为原点的全局坐标系的坐标注入鼠标事件。

如果当前处于用户未授权状态，调用该接口注入事件不生效。

建议先使用[OH_Input_RequestInjection](#ZH-CN_TOPIC_0000002529445539__oh_input_requestinjection)请求授权。然后通过[OH_Input_QueryAuthorizedStatus](#ZH-CN_TOPIC_0000002529445539__oh_input_queryauthorizedstatus)查询授权状态，当授权状态为[AUTHORIZED](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_injectionstatus)时，再使用该接口。

**起始版本：** 20

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t

OH_Input_InjectMouseEventGlobal的执行结果。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示注入成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数错误。

[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result) 表示缺少权限。

#### OH_Input_SetMouseEventGlobalX()

```ets
void OH_Input_SetMouseEventGlobalX(struct Input_MouseEvent* mouseEvent, int32_t globalX)
```

**描述**

设置鼠标事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

int32_t globalX鼠标事件以主屏左上角为原点的全局坐标系的X坐标。

#### OH_Input_GetMouseEventGlobalX()

```ets
int32_t OH_Input_GetMouseEventGlobalX(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t鼠标事件以主屏左上角为原点的全局坐标系的X坐标。

#### OH_Input_SetMouseEventGlobalY()

```ets
void OH_Input_SetMouseEventGlobalY(struct Input_MouseEvent* mouseEvent, int32_t globalY)
```

**描述**

设置鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

int32_t globalY鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。

#### OH_Input_GetMouseEventGlobalY()

```ets
int32_t OH_Input_GetMouseEventGlobalY(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

参数项描述const struct [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent

鼠标事件对象，通过[OH_Input_CreateMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createmouseevent)接口可以创建鼠标事件对象。

使用完需使用[OH_Input_DestroyMouseEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroymouseevent)接口销毁鼠标事件对象。

**返回：**

类型说明int32_t鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。

#### OH_Input_InjectTouchEventGlobal()

```ets
int32_t OH_Input_InjectTouchEventGlobal(const struct Input_TouchEvent* touchEvent)
```

**描述**

使用以主屏左上角为原点的全局坐标系的坐标注入触屏输入事件。

如果当前处于用户未授权状态，调用该接口注入事件不生效。

建议先使用[OH_Input_RequestInjection](#ZH-CN_TOPIC_0000002529445539__oh_input_requestinjection)请求授权。然后通过[OH_Input_QueryAuthorizedStatus](#ZH-CN_TOPIC_0000002529445539__oh_input_queryauthorizedstatus)查询授权状态，当授权状态为[AUTHORIZED](oh_input_manager.h.md#ZH-CN_TOPIC_0000002529445539__input_injectionstatus)时，再使用该接口。

**起始版本：** 20

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int32_t

OH_Input_InjectTouchEventGlobal的执行结果。

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示注入成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数错误。

[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result) 表示缺少权限。

#### OH_Input_SetTouchEventGlobalX()

```ets
void OH_Input_SetTouchEventGlobalX(struct Input_TouchEvent* touchEvent, int32_t globalX)
```

**描述**

设置触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

int32_t globalX触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。

#### OH_Input_GetTouchEventGlobalX()

```ets
int32_t OH_Input_GetTouchEventGlobalX(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int32_t触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。

#### OH_Input_SetTouchEventGlobalY()

```ets
void OH_Input_SetTouchEventGlobalY(struct Input_TouchEvent* touchEvent, int32_t globalY)
```

**描述**

设置触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

int32_t globalY触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。

#### OH_Input_GetTouchEventGlobalY()

```ets
int32_t OH_Input_GetTouchEventGlobalY(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

参数项描述const struct [Input_TouchEvent](../../topics/input/Input_TouchEvent.md)* touchEvent

触屏输入事件对象，通过[OH_Input_CreateTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createtouchevent)接口可以创建触屏输入事件对象。

使用完需使用[OH_Input_DestroyTouchEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroytouchevent)接口销毁触屏输入事件对象。

**返回：**

类型说明int32_t触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。

#### OH_Input_SetAxisEventGlobalX()

```ets
Input_Result OH_Input_SetAxisEventGlobalX(struct Input_AxisEvent* axisEvent, int32_t globalX)
```

**描述**

设置轴事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

int32_t globalX轴事件以主屏左上角为原点的全局坐标系的X坐标。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示axisEvent是空指针。

#### OH_Input_GetAxisEventGlobalX()

```ets
Input_Result OH_Input_GetAxisEventGlobalX(const Input_AxisEvent* axisEvent, int32_t* globalX)
```

**描述**

获取轴事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

int32_t* globalX轴事件以主屏左上角为原点的全局坐标系的X坐标。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示axisEvent或者globalX是空指针。

#### OH_Input_SetAxisEventGlobalY()

```ets
Input_Result OH_Input_SetAxisEventGlobalY(struct Input_AxisEvent* axisEvent, int32_t globalY)
```

**描述**

设置轴事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

int32_t globalY轴事件以主屏左上角为原点的全局坐标系的Y坐标。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示axisEvent是空指针。

#### OH_Input_GetAxisEventGlobalY()

```ets
Input_Result OH_Input_GetAxisEventGlobalY(const Input_AxisEvent* axisEvent, int32_t* globalY)
```

**描述**

获取轴事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

参数项描述const [Input_AxisEvent](../../topics/input/Input_AxisEvent.md)* axisEvent

轴事件对象，通过[OH_Input_CreateAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createaxisevent)接口可以创建轴事件对象。

使用完需使用[OH_Input_DestroyAxisEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroyaxisevent)接口销毁轴事件对象。

int32_t* globalY轴事件以主屏左上角为原点的全局坐标系的Y坐标。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示axisEvent或者globalY是空指针。

#### OH_Input_GetPointerLocation()

```ets
Input_Result OH_Input_GetPointerLocation(int32_t *displayId, double *displayX, double *displayY)
```

**描述**

获取当前屏幕上鼠标的坐标点。

**起始版本：** 20

**参数：**

参数项描述int32_t *displayId当前屏幕的屏幕ID。double *displayX鼠标在当前屏幕的X坐标。double *displayY鼠标在当前屏幕的Y坐标。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetPointerLocation的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示查询成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数错误。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示服务异常。

[INPUT_APP_NOT_FOCUSED](#ZH-CN_TOPIC_0000002529445539__input_result) 表示当前应用不是焦点应用。

[INPUT_DEVICE_NO_POINTER](#ZH-CN_TOPIC_0000002529445539__input_result) 表示无鼠标类输入外设。

#### OH_Input_GetKeyEventId()

```ets
Input_Result OH_Input_GetKeyEventId(const struct Input_KeyEvent* keyEvent, int32_t* eventId)
```

**描述**

获取按键事件的ID。

**起始版本：** 21

**参数：**

参数项描述[Input_KeyEvent](../../topics/input/Input_KeyEvent.md)* keyEvent

按键事件对象，通过[OH_Input_CreateKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_createkeyevent)接口可以创建按键事件对象。

使用完需使用[OH_Input_DestroyKeyEvent](#ZH-CN_TOPIC_0000002529445539__oh_input_destroykeyevent)接口销毁按键事件对象。

int32_t* eventId按键事件的ID。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetKeyEventId的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

#### OH_Input_AddKeyEventHook()

```ets
Input_Result OH_Input_AddKeyEventHook(Input_KeyEventCallback callback)
```

**描述**

添加一个按键事件拦截钩子函数。

添加后可以通过[OH_Input_RemoveKeyEventHook](#ZH-CN_TOPIC_0000002529445539__oh_input_removekeyeventhook)接口移除。一个进程仅支持设置一个钩子，一个应用支持多个钩子函数，后添加的生效优先级更高。

在使用该接口之前，需要用户在设备的“设置”->“隐私和安全”->“权限管理”中打开“键盘输入辅助”权限。该权限仅PC/2in1、Tablet设备支持。

**需要权限：** ohos.permission.HOOK_KEY_EVENT

**起始版本：** 21

**参数：**

参数项描述[Input_KeyEventCallback](#ZH-CN_TOPIC_0000002529445539__input_keyeventcallback) callback钩子函数，用于拦截待分发的所有按键事件。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_AddKeyEventHook的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

[INPUT_DEVICE_NOT_SUPPORTED](#ZH-CN_TOPIC_0000002529445539__input_result) 表示不支持该功能。

[INPUT_PERMISSION_DENIED](#ZH-CN_TOPIC_0000002529445539__input_result) 表示权限验证失败。

[INPUT_REPEAT_INTERCEPTOR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示重复设置钩子。一个进程仅支持设置一个钩子。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示服务异常，请重试。

#### OH_Input_RemoveKeyEventHook()

```ets
Input_Result OH_Input_RemoveKeyEventHook(Input_KeyEventCallback callback)
```

**描述**

移除按键事件拦截钩子函数。

通常与[OH_Input_AddKeyEventHook](#ZH-CN_TOPIC_0000002529445539__oh_input_addkeyeventhook)接口配合使用。

**起始版本：** 21

**参数：**

参数项描述[Input_KeyEventCallback](#ZH-CN_TOPIC_0000002529445539__input_keyeventcallback) callback钩子函数，用于拦截待分发的所有按键事件。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_RemoveKeyEventHook的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。如果之前没有添加对应钩子，移除时也会返回成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示服务异常，请重试。

#### OH_Input_DispatchToNextHandler()

```ets
Input_Result OH_Input_DispatchToNextHandler(int32_t eventId)
```

**描述**

重新分发按键事件。

只有被钩子拦截的按键事件才能被重新分发，重新分发的事件必须保持原有优先级顺序。

调用该接口后，按键事件可在3秒内重新分发。如果超过3秒，将返回[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result)。

重新分发的事件需要保证配对关系。如果重新分发了一个或多个按键按下事件[KEY_ACTION_DOWN](#ZH-CN_TOPIC_0000002529445539__input_keyeventaction)，再重新分发按键抬起事件[KEY_ACTION_UP](#ZH-CN_TOPIC_0000002529445539__input_keyeventaction)或按键动作取消事件[KEY_ACTION_CANCEL](#ZH-CN_TOPIC_0000002529445539__input_keyeventaction)可以成功。

如果仅分发[KEY_ACTION_UP](#ZH-CN_TOPIC_0000002529445539__input_keyeventaction)或[KEY_ACTION_CANCEL](#ZH-CN_TOPIC_0000002529445539__input_keyeventaction)按键事件，接口可以调用成功，但不会执行实际的分发动作。

如果分发的事件未被钩子拦截，函数调用会成功，但不会执行实际的分发动作。

**起始版本：** 21

**参数：**

参数项描述int32_t eventId按键事件的ID。可以通过[OH_Input_GetKeyEventId](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeyeventid)接口获取。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_DispatchToNextHandler的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。可通过[OH_Input_GetKeyEventId](#ZH-CN_TOPIC_0000002529445539__oh_input_getkeyeventid)查看传入的eventId是否准确。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示服务异常，请重试。

#### OH_Input_SetPointerVisible()

```ets
Input_Result OH_Input_SetPointerVisible(bool visible)
```

**描述**

设置当前窗口的鼠标光标的显示或隐藏状态。

**起始版本：** 22

**参数：**

参数项描述bool visible鼠标光标是否显示。true表示显示，false表示不显示。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_SetPointerVisible的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_DEVICE_NOT_SUPPORTED](#ZH-CN_TOPIC_0000002529445539__input_result) 表示设备不支持。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示服务异常，请重试。

#### OH_Input_GetPointerStyle()

```ets
Input_Result OH_Input_GetPointerStyle(int32_t windowId, int32_t *pointerStyle)
```

**描述**

获取指定窗口的鼠标光标样式。

**起始版本：** 22

**参数：**

参数项描述int32_t windowId

窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。

 仅支持传入当前窗口和全局窗口的ID，传入其他ID返回全局窗口的默认光标样式，当前窗口ID可以通过[getWindowProperties](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)获取。

int32_t* pointerStyle鼠标光标样式的指针。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetPointerStyle的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示服务异常，请重试。

#### OH_Input_SetPointerStyle()

```ets
Input_Result OH_Input_SetPointerStyle(int32_t windowId, int32_t pointerStyle)
```

**描述**

设置指定窗口的鼠标光标样式。

**起始版本：** 22

**参数：**

参数项描述int32_t windowId

窗口ID。取值范围为大于等于0的整数。

 仅支持传入当前窗口的光标样式，传入其他窗口ID本接口可以运行成功但设置不生效，当前窗口ID可以通过[getWindowProperties](../../types/interfaces/Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)获取。

int32_t pointerStyle鼠标光标样式，取值为[Input_PointerStyle](oh_pointer_style.h.md#ZH-CN_TOPIC_0000002497445596__input_pointerstyle)的枚举值。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_SetPointerStyle的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示服务异常，请重试。

#### OH_Input_CustomCursor_Create()

```ets
Input_CustomCursor* OH_Input_CustomCursor_Create(OH_PixelmapNative* pixelMap, int32_t anchorX, int32_t anchorY)
```

**描述**

创建自定义鼠标光标资源对象。

**起始版本：** 22

**参数：**

参数项描述OH_PixelmapNative* pixelMap[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)自定义鼠标光标像素图。最小限制为资源图本身的最小限制。最大限制为256 x 256px。int32_t anchorX自定义鼠标光标焦点的水平坐标。该坐标受自定义鼠标光标大小的限制。最小值为0，最大值为资源图的宽度最大值，单位为px。int32_t anchorY自定义鼠标光标焦点的垂直坐标。该坐标受自定义鼠标光标大小的限制。最小值为0，最大值为资源图的高度最大值，单位为px。

**返回：**

类型说明Input_CustomCursor*[Input_CustomCursor](../../topics/input/Input_CustomCursor.md)对象。操作成功时返回自定义鼠标光标资源对象的指针。异常时返回空指针。

#### OH_Input_CustomCursor_Destroy()

```ets
void OH_Input_CustomCursor_Destroy(Input_CustomCursor** customCursor)
```

**描述**

销毁自定义鼠标光标资源对象。

**起始版本：** 22

**参数：**

参数项描述Input_CustomCursor** customCursor自定义鼠标光标资源[Input_CustomCursor](../../topics/input/Input_CustomCursor.md)。

#### OH_Input_CustomCursor_GetPixelMap()

```ets
Input_Result OH_Input_CustomCursor_GetPixelMap(Input_CustomCursor* customCursor, OH_PixelmapNative** pixelMap)
```

**描述**

获取指定自定义鼠标光标资源的自定义鼠标光标像素图。

**起始版本：** 22

**参数：**

参数项描述Input_CustomCursor* customCursor自定义鼠标光标资源[Input_CustomCursor](../../topics/input/Input_CustomCursor.md)。OH_PixelmapNative** pixelMap[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)自定义鼠标光标像素图。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_CustomCursor_GetPixelMap的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

#### OH_Input_CustomCursor_GetAnchor()

```ets
Input_Result OH_Input_CustomCursor_GetAnchor(Input_CustomCursor* customCursor, int32_t* anchorX, int32_t* anchorY)
```

**描述**

获取指定自定义鼠标光标资源的焦点坐标。

**起始版本：** 22

**参数：**

参数项描述Input_CustomCursor* customCursor自定义鼠标光标资源[Input_CustomCursor](../../topics/input/Input_CustomCursor.md)。int32_t* anchorX自定义鼠标光标资源的焦点水平坐标，单位为px。int32_t* anchorY自定义鼠标光标资源的焦点垂直坐标，单位为px。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_CustomCursor_GetAnchor的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

#### OH_Input_CursorConfig_Create()

```ets
Input_CursorConfig* OH_Input_CursorConfig_Create(bool followSystem)
```

**描述**

创建自定义鼠标光标配置对象。

**起始版本：** 22

**参数：**

参数项描述bool followSystem是否根据系统设置调整鼠标光标大小。false表示使用自定义鼠标光标样式大小，true表示根据系统设置调整鼠标光标大小，可调整范围为：[光标资源图大小，256×256]，单位为px。

**返回：**

类型说明Input_CursorConfig*自定义鼠标光标配置[Input_CursorConfig](../../topics/input/Input_CursorConfig.md)对象。

#### OH_Input_CursorConfig_Destroy()

```ets
void OH_Input_CursorConfig_Destroy(Input_CursorConfig** cursorConfig)
```

**描述**

销毁自定义鼠标光标配置对象。

**起始版本：** 22

**参数：**

参数项描述Input_CursorConfig** cursorConfig自定义鼠标光标配置[Input_CursorConfig](../../topics/input/Input_CursorConfig.md)对象。

#### OH_Input_CursorConfig_IsFollowSystem()

```ets
Input_Result OH_Input_CursorConfig_IsFollowSystem(Input_CursorConfig *cursorConfig, bool *followSystem)
```

**描述**

查询自定义鼠标光标配置是否跟随系统设置调整光标大小。

**起始版本：** 22

**参数：**

参数项描述Input_CursorConfig* cursorConfig自定义鼠标光标配置[Input_CursorConfig](../../topics/input/Input_CursorConfig.md)。bool* followSystem是否根据系统设置调整光标大小，取值为true表示根据系统设置调整鼠标光标大小，取值为false表示使用自定义鼠标光标样式大小。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_CursorConfig_IsFollowSystem的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

#### OH_Input_SetCustomCursor()

```ets
Input_Result OH_Input_SetCustomCursor(int32_t windowId, Input_CustomCursor* customCursor, Input_CursorConfig* cursorConfig)
```

**描述**

设置自定义鼠标光标样式。

应用窗口布局改变、热区切换、页面跳转、光标移出再回到窗口、光标在窗口不同区域移动，以上场景可能导致光标切换回系统样式，需要开发者重新设置光标样式。

**起始版本：** 22

**参数：**

参数项描述int32_t windowId窗口ID。取值范围为大于等于0的整数，仅支持传入当前窗口的光标样式。Input_CustomCursor* customCursor自定义鼠标光标资源[Input_CustomCursor](../../topics/input/Input_CustomCursor.md)。Input_CursorConfig* cursorConfig自定义鼠标光标配置[Input_CursorConfig](../../topics/input/Input_CursorConfig.md)。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_SetCustomCursor的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

[INPUT_INVALID_WINDOWID](#ZH-CN_TOPIC_0000002529445539__input_result) 表示窗口ID无效。

[INPUT_DEVICE_NOT_SUPPORTED](#ZH-CN_TOPIC_0000002529445539__input_result) 表示设备不支持。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示服务异常。可能的原因：1.自定义鼠标光标焦点的横坐标或纵坐标大于自定义鼠标光标像素图的宽度或高度。2.系统服务异常，请重试。

#### OH_Input_CursorInfo_Create()

```ets
struct Input_CursorInfo* OH_Input_CursorInfo_Create()
```

**描述**

创建鼠标光标信息对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**起始版本：** 22

**返回：**

类型说明struct Input_CursorInfo*创建成功返回一个[Input_CursorInfo](../../topics/input/Input_CursorInfo.md)对象，否则返回空指针，可能原因是内存分配失败。

#### OH_Input_CursorInfo_Destroy()

```ets
void OH_Input_CursorInfo_Destroy(Input_CursorInfo** cursorInfo)
```

**描述**

销毁鼠标光标信息对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**起始版本：** 22

**参数：**

参数项描述[Input_CursorInfo](../../topics/input/Input_CursorInfo.md)** cursorInfo鼠标光标信息对象。

#### OH_Input_CursorInfo_IsVisible()

```ets
Input_Result OH_Input_CursorInfo_IsVisible(Input_CursorInfo* cursorInfo, bool* visible)
```

**描述**

获取指定鼠标光标信息对象对应的光标显示状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**起始版本：** 22

**参数：**

参数项描述[Input_CursorInfo](../../topics/input/Input_CursorInfo.md)* cursorInfo指定鼠标光标信息对象。可以通过[OH_Input_GetMouseEventCursorInfo](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventcursorinfo)查询指定鼠标事件的鼠标光标信息、或通过[OH_Input_GetCursorInfo](#ZH-CN_TOPIC_0000002529445539__oh_input_getcursorinfo)接口查询当前的鼠标光标信息。bool* visible鼠标光标显示或隐藏状态。true代表显示状态，false代表隐藏状态。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_CursorInfo_IsVisible的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

#### OH_Input_CursorInfo_GetStyle()

```ets
Input_Result OH_Input_CursorInfo_GetStyle(Input_CursorInfo* cursorInfo, Input_PointerStyle* style)
```

**描述**

获取指定鼠标光标信息对象对应的光标样式。

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**起始版本：** 22

**参数：**

参数项描述[Input_CursorInfo](../../topics/input/Input_CursorInfo.md)* cursorInfo指定鼠标光标信息对象。可以通过[OH_Input_GetMouseEventCursorInfo](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventcursorinfo)查询指定鼠标事件的鼠标光标信息、或通过[OH_Input_GetCursorInfo](#ZH-CN_TOPIC_0000002529445539__oh_input_getcursorinfo)接口查询当前的鼠标光标信息。[Input_PointerStyle](oh_pointer_style.h.md)鼠标光标信息的光标样式枚举，具体请参考[Input_PointerStyle](oh_pointer_style.h.md#ZH-CN_TOPIC_0000002497445596__input_pointerstyle)。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_CursorInfo_GetStyle的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败或者光标不可见。

#### OH_Input_CursorInfo_GetSizeLevel()

```ets
Input_Result OH_Input_CursorInfo_GetSizeLevel(Input_CursorInfo* cursorInfo, int32_t* sizeLevel)
```

**描述**

获取指定鼠标光标信息对象对应的光标大小档位。

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**起始版本：** 22

**参数：**

参数项描述[Input_CursorInfo](../../topics/input/Input_CursorInfo.md)* cursorInfo指定鼠标光标信息对象。可以通过[OH_Input_GetMouseEventCursorInfo](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventcursorinfo)查询指定鼠标事件的鼠标光标信息、或通过[OH_Input_GetCursorInfo](#ZH-CN_TOPIC_0000002529445539__oh_input_getcursorinfo)接口查询当前的鼠标光标信息。int32_t* sizeLevel鼠标光标信息的光标大小档位。取值范围为整数1~7，数值越大则光标越大。应用自定义光标[DEVELOPER_DEFINED_ICON](oh_pointer_style.h.md#ZH-CN_TOPIC_0000002497445596__input_pointerstyle)请以实际位图大小为准。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_CursorInfo_GetSizeLevel的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败或者光标不可见。

#### OH_Input_CursorInfo_GetColor()

```ets
Input_Result OH_Input_CursorInfo_GetColor(Input_CursorInfo* cursorInfo, uint32_t* color)
```

**描述**

获取指定鼠标光标信息对象对应的光标颜色, 使用32位ARGB整数表示。

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**起始版本：** 22

**参数：**

参数项描述[Input_CursorInfo](../../topics/input/Input_CursorInfo.md)* cursorInfo指定鼠标光标信息对象。可以通过[OH_Input_GetMouseEventCursorInfo](#ZH-CN_TOPIC_0000002529445539__oh_input_getmouseeventcursorinfo)查询指定鼠标事件的鼠标光标信息、或通过[OH_Input_GetCursorInfo](#ZH-CN_TOPIC_0000002529445539__oh_input_getcursorinfo)接口查询当前的鼠标光标信息。uint32_t* color鼠标光标信息的光标颜色, 使用32位ARGB整数表示。应用自定义光标[DEVELOPER_DEFINED_ICON](oh_pointer_style.h.md#ZH-CN_TOPIC_0000002497445596__input_pointerstyle)请以实际位图颜色为准。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_CursorInfo_GetColor的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败或者光标不可见。

#### OH_Input_GetMouseEventCursorInfo()

```ets
Input_Result OH_Input_GetMouseEventCursorInfo(const struct Input_MouseEvent* mouseEvent, Input_CursorInfo* cursorInfo)
```

**描述**

获取鼠标事件的鼠标光标信息，包括光标显示状态、光标样式、光标大小档位、光标颜色。

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**起始版本：** 22

**参数：**

参数项描述const [Input_MouseEvent](../../topics/input/Input_MouseEvent.md)* mouseEvent鼠标事件对象。可以通过[OH_Input_AddMouseEventMonitor](#ZH-CN_TOPIC_0000002529445539__oh_input_addmouseeventmonitor)或者[OH_Input_AddInputEventInterceptor](#ZH-CN_TOPIC_0000002529445539__oh_input_addinputeventinterceptor)接口的回调函数中获取鼠标事件对象。[Input_CursorInfo](../../topics/input/Input_CursorInfo.md)* cursorInfo鼠标光标信息对象，可以通过[OH_Input_CursorInfo_Create](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorinfo_create)接口创建鼠标光标信息对象。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetMouseEventCursorInfo的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

#### OH_Input_GetCursorInfo()

```ets
Input_Result OH_Input_GetCursorInfo(Input_CursorInfo* cursorInfo, OH_PixelmapNative** pixelmap)
```

**描述**

查询当前鼠标光标信息，包括光标显示状态、光标样式、光标大小档位、光标颜色。如果pixelmap参数非空，且光标样式为[DEVELOPER_DEFINED_ICON](oh_pointer_style.h.md#ZH-CN_TOPIC_0000002497445596__input_pointerstyle)，则会同时返回光标的PixelMap位图对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**起始版本：** 22

**参数：**

参数项描述[Input_CursorInfo](../../topics/input/Input_CursorInfo.md)* cursorInfo鼠标光标信息对象，可以通过[OH_Input_CursorInfo_Create](#ZH-CN_TOPIC_0000002529445539__oh_input_cursorinfo_create)接口创建鼠标光标信息对象。[OH_PixelmapNative](../../topics/graphics/OH_PixelmapNative.md)** pixelmap

PixelMap位图对象，如果该参数非空且光标为应用自定义，则会返回光标的PixelMap位图对象，否则不返回PixelMap位图对象。首先通过[OH_PixelmapInitializationOptions_Create](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_create)接口创建OH_PixelmapInitializationOptions对象，然后调用[OH_PixelmapInitializationOptions_SetWidth](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_setwidth)接口设置大于0的宽度，调用[OH_PixelmapInitializationOptions_SetHeight](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_setheight)接口设置大于0的高度，最后以该OH_PixelmapInitializationOptions对象作为入参调用[OH_PixelmapNative_CreateEmptyPixelmap](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createemptypixelmap)接口创建PixelMap位图对象。

使用完需要先调用[OH_PixelmapNative_Release](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_release)接口释放PixelMap位图对象，然后调用[OH_PixelmapNative_Destroy](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_destroy)接口销毁PixelMap位图对象。

**返回：**

类型说明[Input_Result](#ZH-CN_TOPIC_0000002529445539__input_result)

OH_Input_GetCursorInfo的执行结果：

[INPUT_SUCCESS](#ZH-CN_TOPIC_0000002529445539__input_result) 表示操作成功。

[INPUT_PARAMETER_ERROR](#ZH-CN_TOPIC_0000002529445539__input_result) 表示参数检查失败。

[INPUT_SERVICE_EXCEPTION](#ZH-CN_TOPIC_0000002529445539__input_result) 表示服务异常，请重试。