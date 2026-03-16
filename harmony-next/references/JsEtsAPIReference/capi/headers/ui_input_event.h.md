# ui_input_event.h

#### 概述

提供ArkUI在Native侧的事件定义。

**引用文件：** <arkui/ui_input_event.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：**[ArkUI_EventModule](../../topics/system-services/ArkUI_EventModule.md)

**相关示例：**[NdkInputEvent](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/NdkInputEvent)、[CoastingAxisEventNDK](https://gitcode.com/HarmonyOS/applications_app_samples/tree/master/code/DocsSample/ArkUISample/CoastingAxisEventNDK)

#### 汇总

#### 结构体

名称typedef关键字描述[ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)ArkUI_UIInputEventUI输入事件定义。[ArkUI_CoastingAxisEvent](../../topics/input/ArkUI_CoastingAxisEvent.md)ArkUI_CoastingAxisEvent定义惯性滚动轴事件。

#### 枚举

名称typedef关键字描述[ArkUI_UIInputEvent_Type](#ZH-CN_TOPIC_0000002497605082__arkui_uiinputevent_type)ArkUI_UIInputEvent_TypeUI输入事件类型定义。[anonymous1](#ZH-CN_TOPIC_0000002497605082__anonymous1)-定义输入事件的Action Code。[anonymous2](#ZH-CN_TOPIC_0000002497605082__anonymous2)-产生输入事件的工具类型定义。[anonymous3](#ZH-CN_TOPIC_0000002497605082__anonymous3)-产生输入事件的来源类型定义。[HitTestMode](#ZH-CN_TOPIC_0000002497605082__hittestmode)HitTestMode定义触摸测试类型的枚举值。[anonymous4](#ZH-CN_TOPIC_0000002497605082__anonymous4)-定义鼠标事件的Action Code。[anonymous5](#ZH-CN_TOPIC_0000002497605082__anonymous5)-定义鼠标事件的按键类型。[ArkUI_ModifierKeyName](#ZH-CN_TOPIC_0000002497605082__arkui_modifierkeyname)ArkUI_ModifierKeyName定义modifier按键。[anonymous6](#ZH-CN_TOPIC_0000002497605082__anonymous6)-定义焦点轴事件的轴类型。[ArkUI_InteractionHand](#ZH-CN_TOPIC_0000002497605082__arkui_interactionhand)ArkUI_InteractionHand定义触摸事件是左手还是右手。[anonymous7](#ZH-CN_TOPIC_0000002497605082__anonymous7)-定义轴事件的操作类型。[anonymous8](#ZH-CN_TOPIC_0000002497605082__anonymous8)-定义轴事件的轴类型。[ArkUI_CoastingAxisEventPhase](#ZH-CN_TOPIC_0000002497605082__arkui_coastingaxiseventphase)ArkUI_CoastingAxisEventPhase定义惯性滚动轴事件的阶段。

#### 函数

名称描述[int32_t OH_ArkUI_UIInputEvent_GetType(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_gettype)获取UI输入事件的类型。在访问一个ArkUI_UIInputEvent指针对象之前，推荐使用该方法判断该输入事件的类型，该接口会返回[ArkUI_UIInputEvent_Type](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__arkui_uiinputevent_type)枚举中的一种。比如，当事件是一个触控类型时，由于触控类型是指向性事件，那么使用OH_ArkUI_UIInputEvent_GetXXX及OH_ArkUI_PointerEvent_GetXXX系列接口，均可以正常访问；而如果使用OH_ArkUI_KeyEvent_GetXXX相关接口去访问它，则会有无法预期的结果。对于还未支持的事件类型，接口返回默认值0。[int32_t OH_ArkUI_UIInputEvent_GetAction(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_getaction)获取输入事件的action类型。action类型为基础事件在不同阶段的类型定义，通常代表了事件的特点，并表征事件的开始与结束，如touch down, touch up。触控事件的action类型为UI_TOUCH_EVENT_ACTION_XXX，鼠标事件的action类型为UI_MOUSE_EVENT_ACTION_XXX。[int32_t OH_ArkUI_UIInputEvent_GetSourceType(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_getsourcetype)获取UI输入事件的触发源类型。输入源为产生输入事件的真实物理设备，如触摸屏，鼠标等，由UI_INPUT_EVENT_SOURCE_TYPE_XXX定义，而输入工具为操作输入源设备来产生事件的工具，如手指、触控笔。在某些情况下两者可能容易发生混淆，比如当用户在操作鼠标时，鼠标既是输入源，也是输入工具。[int32_t OH_ArkUI_UIInputEvent_GetToolType(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_gettooltype)获取UI输入事件的工具类型。输入工具为操作输入源设备来产生事件的操作方，如手指、触控笔，他们自身不真实产生事件，但可以驱动输入源设备不断产生事件。返回的类型由UI_INPUT_EVENT_TOOL_TYPE_XXX枚举值定义。[int64_t OH_ArkUI_UIInputEvent_GetEventTime(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_geteventtime)获取UI输入事件发生的时间。单位为ns。[uint32_t OH_ArkUI_PointerEvent_GetPointerCount(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getpointercount)从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取多点触控的接触点数量。指向性事件一般是附带有事件发生位置信息的事件，如触摸事件，用户操作时，可以感知事件在什么位置发生。而非指向性事件，如按键事件，一般没有位置信息，没有触点的说法，所以该接口对按键事件无效。对于触摸事件，该接口多用于处理多指触控，判断用户有几根手指在操作当前控件。而对于鼠标和轴事件，可认为触点只有1个，该接口永远返回1。[int32_t OH_ArkUI_PointerEvent_GetPointerId(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getpointerid)从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取多点触控的接触点标识。返回事件发生时，事件触点的唯一标识符，用于区分同类输入设备的多点触控信息。其数值没有除标识触点外的其他含义。[int32_t OH_ArkUI_PointerEvent_GetChangedPointerId(const ArkUI_UIInputEvent* event, uint32_t* pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getchangedpointerid)获取当前触摸事件触发的id。[float OH_ArkUI_PointerEvent_GetX(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getx)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前组件左上角的X坐标。[float OH_ArkUI_PointerEvent_GetXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getxbyindex)从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前组件左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，返回默认值0.0f。[float OH_ArkUI_PointerEvent_GetY(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gety)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前组件左上角的Y坐标。[float OH_ArkUI_PointerEvent_GetYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getybyindex)从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前组件左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，返回默认值0.0f。[float OH_ArkUI_PointerEvent_GetWindowX(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getwindowx)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前应用窗口左上角的X坐标。[float OH_ArkUI_PointerEvent_GetWindowXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getwindowxbyindex)从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前应用窗口左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。[float OH_ArkUI_PointerEvent_GetWindowY(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getwindowy)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前应用窗口左上角的Y坐标。[float OH_ArkUI_PointerEvent_GetWindowYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getwindowybyindex)从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前应用窗口左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。[float OH_ArkUI_PointerEvent_GetDisplayX(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getdisplayx)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前屏幕左上角的X坐标。[float OH_ArkUI_PointerEvent_GetDisplayXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getdisplayxbyindex)从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前屏幕左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。[float OH_ArkUI_PointerEvent_GetDisplayY(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getdisplayy)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前屏幕左上角的Y坐标。[float OH_ArkUI_PointerEvent_GetDisplayYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getdisplayybyindex)从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前屏幕左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。[float OH_ArkUI_PointerEvent_GetGlobalDisplayX(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getglobaldisplayx)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的X坐标。只能从pointer-likely事件中获取位置信息。[float OH_ArkUI_PointerEvent_GetGlobalDisplayXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getglobaldisplayxbyindex)从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的X坐标。只能从指针事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。[float OH_ArkUI_PointerEvent_GetGlobalDisplayY(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getglobaldisplayy)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的Y坐标。只能从pointer-likely事件中获取位置信息。[float OH_ArkUI_PointerEvent_GetGlobalDisplayYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getglobaldisplayybyindex)从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的Y坐标。只能从指针事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。[float OH_ArkUI_PointerEvent_GetPressure(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getpressure)从带有指向性的输入事件（如触摸事件）中获取触屏压力。[float OH_ArkUI_PointerEvent_GetTiltX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gettiltx)从指向性输入事件（如触摸事件）中获取相对YZ平面的角度，取值的范围[-90, 90]，其中正值是向右倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件。[float OH_ArkUI_PointerEvent_GetTiltY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gettilty)从指向性输入事件（如触摸事件）中获取相对XZ平面的角度，取值的范围[-90, 90]，其中正值是向下倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件。[int32_t OH_ArkUI_PointerEvent_GetRollAngle(const ArkUI_UIInputEvent* event, double* rollAngle)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getrollangle)获取触控笔绕Z轴旋转的角度。[float OH_ArkUI_PointerEvent_GetTouchAreaWidth(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gettouchareawidth)从指向性输入事件（如触摸事件）中获取触屏区域的宽度。仅适用于手指操作产生的触控事件，这通常是一个圆形区域的半径。[float OH_ArkUI_PointerEvent_GetTouchAreaHeight(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gettouchareaheight)从指向性输入事件（如触摸事件）中获取触屏区域的高度。仅适用于手指操作产生的触控事件，这通常是一个圆形区域的半径。[int32_t OH_ArkUI_PointerEvent_GetInteractionHand(const ArkUI_UIInputEvent *event, ArkUI_InteractionHand *hand)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getinteractionhand)获取当前触摸事件是左手点击触发还是右手点击触发。仅在部分触控产品上有效。[int32_t OH_ArkUI_PointerEvent_GetInteractionHandByIndex(const ArkUI_UIInputEvent *event, int32_t pointerIndex, ArkUI_InteractionHand *hand)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getinteractionhandbyindex)获取当前触摸事件是左手点击触发还是右手点击触发。仅在部分触控产品上有效。[uint32_t OH_ArkUI_PointerEvent_GetHistorySize(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorysize)从指向性输入事件（如触摸事件）中获取历史事件数量。历史事件为此次事件与上一次事件之间发生的原始事件，仅适用于move事件。[int64_t OH_ArkUI_PointerEvent_GetHistoryEventTime(const ArkUI_UIInputEvent* event, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistoryeventtime)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取历史事件发生的时间。[uint32_t OH_ArkUI_PointerEvent_GetHistoryPointerCount(const ArkUI_UIInputEvent* event, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorypointercount)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中多点触控的接触点数量。[int32_t OH_ArkUI_PointerEvent_GetHistoryPointerId(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorypointerid)从指向性输入事件（如触摸事件）的历史点中获取多点触控的接触点标识。返回事件发生时，事件触点的唯一标识符，用于区分同类输入设备的多点触控信息。其数值没有除标识触点外的其他含义。[float OH_ArkUI_PointerEvent_GetHistoryX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistoryx)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前组件左上角的X坐标。[float OH_ArkUI_PointerEvent_GetHistoryY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistoryy)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前组件左上角的Y坐标。[float OH_ArkUI_PointerEvent_GetHistoryWindowX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorywindowx)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前应用窗口左上角的X坐标。[float OH_ArkUI_PointerEvent_GetHistoryWindowY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorywindowy)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前应用窗口左上角的Y坐标。[float OH_ArkUI_PointerEvent_GetHistoryDisplayX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorydisplayx)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前屏幕左上角的X坐标。[float OH_ArkUI_PointerEvent_GetHistoryDisplayY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorydisplayy)从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前屏幕左上角的Y坐标。[float OH_ArkUI_PointerEvent_GetHistoryGlobalDisplayX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistoryglobaldisplayx)从给定指针索引和历史记录索引的输入事件（如触摸事件、鼠标事件、轴事件）中获取历史事件中相对于全局显示的特定触摸点的X坐标。只能从指针事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。[float OH_ArkUI_PointerEvent_GetHistoryGlobalDisplayY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistoryglobaldisplayy)从给定指针索引和历史记录索引的输入事件（如触摸事件、鼠标事件、轴事件）中获取历史事件中相对于全局显示的特定触摸点的Y坐标。只能从指针事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。[float OH_ArkUI_PointerEvent_GetHistoryPressure(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorypressure)从带有指向性的输入事件（如触摸事件）中获取特定历史事件中的触屏压力。[float OH_ArkUI_PointerEvent_GetHistoryTiltX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorytiltx)从带有指向性的输入事件（如触摸事件）中获取特定历史事件中的相对YZ平面的角度，取值的范围[-90, 90]，其中正值是向右倾斜。[float OH_ArkUI_PointerEvent_GetHistoryTiltY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorytilty)从带有指向性的输入事件（如触摸事件）中获取特定历史事件中的相对XZ平面的角度，值的范围[-90, 90]，其中正值是向下倾斜。[float OH_ArkUI_PointerEvent_GetHistoryTouchAreaWidth(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorytouchareawidth)从带有指向性的输入事件（如触摸事件）中获取特定历史事件中的触屏区域的宽度。[float OH_ArkUI_PointerEvent_GetHistoryTouchAreaHeight(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorytouchareaheight)从带有指向性的输入事件（如触摸事件）中获取特定历史事件中的触屏区域的高度。[double OH_ArkUI_AxisEvent_GetVerticalAxisValue(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_getverticalaxisvalue)获取当前轴事件的垂直滚动轴的值。通常由鼠标滚轮，或用户在触控板上双指竖向滑动产生。当通过鼠标滚动触发时：1.上报的数值单位为角度，为单次滚动角度增量，非滚动总量；2.上报的数值已与用户配置的放大系数[OH_ArkUI_AxisEvent_GetScrollStep](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_getscrollstep)叠加运算；3.数值的正负代表方向，向前滚动鼠标滚轮时上报数值为正数，向后滚动鼠标滚轮时上报数值为负数；当通过触控板双指竖向滑动时：1.上报的数值单位为PX，为单次滚动增量，非滚动总量；2.上报的数值不受用户配置的放大系数[OH_ArkUI_AxisEvent_GetScrollStep](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_getscrollstep)影响；3.数值的正负代表方向，双指从上往下滑动时上报数值为负数，双指从下往上滑动时上报数值为正数；4.方向会受系统设置中"自然滚动"配置的影响。通常情况下，垂直滚动轴事件只能驱动竖向的滑动手势响应，但当鼠标指针下命中的可滑动手势里，如果可响应的方向都是一致的，那么垂直滚动轴事件可以驱动这些滑动手势得到响应，即使这些手势所定义的方向是横向的。[double OH_ArkUI_AxisEvent_GetHorizontalAxisValue(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_gethorizontalaxisvalue)获取当前轴事件的水平滚动轴的值，通过在触控板上双指横向滑动产生。[double OH_ArkUI_AxisEvent_GetPinchAxisScaleValue(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_getpinchaxisscalevalue)获取当前轴事件的捏合轴缩放的值。通过触控板双指缩放/捏合操作产生。上报的scale数值，为相对于初始状态时的当前scale值。初始状态为系统识别到用户通过触控板发生了捏合操作时的两指位置状态，此时的scale数值为1.0。在手指抬起前的本次捏合操作过程中，所上报的scale数值均将初始状态作为参考系，从初始状态往中心捏合，则上报的scale会从1.0逐步往0.0缩小；当从初始化状态往外扩大双指距离时，会从1.0逐步变大。[int32_t OH_ArkUI_AxisEvent_GetAxisAction(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_getaxisaction)获取当前轴事件的操作类型。[int32_t OH_ArkUI_AxisEvent_HasAxis(const ArkUI_UIInputEvent* event, int32_t axis)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_hasaxis)检测此轴事件是否包含指定的轴类型。[int32_t OH_ArkUI_PointerEvent_SetInterceptHitTestMode(const ArkUI_UIInputEvent* event, HitTestMode mode)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_setintercepthittestmode)配置HitTest模式。仅适用于接收基础事件的场景，如使用NODE_ON_TOUCH接收touch事件场景。对于通过[OH_ArkUI_GestureEvent_GetRawInputEvent](native_gesture.h.md#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureevent_getrawinputevent)接口从一个手势事件中获取到的ArkUI_UIInputEvent对象，无法使用该接口。[int32_t OH_ArkUI_MouseEvent_GetMouseButton(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_mouseevent_getmousebutton)获取鼠标事件的按键类型的值。[int32_t OH_ArkUI_MouseEvent_GetMouseAction(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_mouseevent_getmouseaction)获取鼠标事件的鼠标动作类型的值。[int32_t OH_ArkUI_PointerEvent_SetStopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_setstoppropagation)设置是否阻止事件冒泡。仅适用于接收基础事件的场景，如使用NODE_ON_TOUCH接收touch事件场景。对于通过 [OH_ArkUI_GestureEvent_GetRawInputEvent](native_gesture.h.md#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureevent_getrawinputevent)接口从一个手势事件中获取到的ArkUI_UIInputEvent对象，无法使用该接口。[int32_t OH_ArkUI_UIInputEvent_GetDeviceId(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_getdeviceid)获取当前按键的输入设备ID。[int32_t OH_ArkUI_UIInputEvent_GetPressedKeys(const ArkUI_UIInputEvent* event, int32_t* pressedKeyCodes, int32_t* length)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_getpressedkeys)获取所有按下的按键，当前只支持按键事件。[double OH_ArkUI_FocusAxisEvent_GetAxisValue(const ArkUI_UIInputEvent* event, int32_t axis)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_focusaxisevent_getaxisvalue)获取焦点轴事件的轴值。[int32_t OH_ArkUI_FocusAxisEvent_SetStopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_focusaxisevent_setstoppropagation)设置是否阻止焦点轴事件冒泡。[int32_t OH_ArkUI_UIInputEvent_GetModifierKeyStates(const ArkUI_UIInputEvent* event, uint64_t* keys)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_getmodifierkeystates)获取UI输入事件的修饰键状态。该接口会通过keys传出当前事件发生时所有修饰键的状态，你可以通过与[ArkUI_ModifierKeyName](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__arkui_modifierkeyname)中定义的修饰键类型进行位计算操作获取哪些键处于按下状态。[int32_t OH_ArkUI_AxisEvent_SetPropagation(const ArkUI_UIInputEvent* event, bool propagation)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_setpropagation)设置是否使能轴事件冒泡。默认不会进行冒泡传递，仅发送给第一个可响应轴事件的控件。可在接收到轴事件时，主动使能冒泡传递，以便当前事件可以继续传递给响应链上的下一个可响应轴事件的祖先组件处理。不支持对从手势事件中获取到的轴事件进行设置。[int32_t OH_ArkUI_AxisEvent_GetScrollStep(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_getscrollstep)获取滚动轴事件的滚动步长系数，适用于鼠标滚轮产生的轴事件。这个值可以告诉你用户所配置的滚动放大系数。[float OH_ArkUI_UIInputEvent_GetEventTargetWidth(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_geteventtargetwidth)获取事件命中的组件的宽度。[float OH_ArkUI_UIInputEvent_GetEventTargetHeight(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_geteventtargetheight)获取事件命中的组件的高度。[float OH_ArkUI_UIInputEvent_GetEventTargetPositionX(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_geteventtargetpositionx)获取事件命中的组件的X坐标。[float OH_ArkUI_UIInputEvent_GetEventTargetPositionY(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_geteventtargetpositiony)获取事件命中的组件的Y坐标。[float OH_ArkUI_UIInputEvent_GetEventTargetGlobalPositionX(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_geteventtargetglobalpositionx)获取事件命中的组件的全局X坐标。[float OH_ArkUI_UIInputEvent_GetEventTargetGlobalPositionY(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_geteventtargetglobalpositiony)获取事件命中的组件的全局Y坐标。[int64_t OH_ArkUI_PointerEvent_GetPressedTimeByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getpressedtimebyindex)获取指定触点的按下时间。仅对触摸事件有效。[float OH_ArkUI_MouseEvent_GetRawDeltaX(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_mouseevent_getrawdeltax)获取鼠标设备在二维平面X轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。[float OH_ArkUI_MouseEvent_GetRawDeltaY(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_mouseevent_getrawdeltay)获取鼠标设备在二维平面Y轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。[int32_t OH_ArkUI_MouseEvent_GetPressedButtons(const ArkUI_UIInputEvent* event, int32_t* pressedButtons, int32_t* length)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_mouseevent_getpressedbuttons)从鼠标事件中获取按下的按键。[int32_t OH_ArkUI_UIInputEvent_GetTargetDisplayId(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_gettargetdisplayid)获取发生UI输入事件的屏幕ID。[bool OH_ArkUI_HoverEvent_IsHovered(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_hoverevent_ishovered)获取鼠标是否悬浮在当前组件上[int32_t OH_ArkUI_PointerEvent_CreateClonedEvent(const ArkUI_UIInputEvent* event, ArkUI_UIInputEvent** clonedEvent)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_createclonedevent)基于原始事件指针创建克隆事件指针。仅对触摸事件有效。[int32_t OH_ArkUI_PointerEvent_DestroyClonedEvent(const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_destroyclonedevent)销毁克隆事件指针。[int32_t OH_ArkUI_PointerEvent_SetClonedEventLocalPosition(const ArkUI_UIInputEvent* event, float x, float y)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_setclonedeventlocalposition)设置指向性事件相对于当前组件左上角的X坐标和Y坐标。[int32_t OH_ArkUI_PointerEvent_SetClonedEventLocalPositionByIndex(const ArkUI_UIInputEvent* event, float x, float y, int32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_setclonedeventlocalpositionbyindex)设置指向性事件特有接触点相对于当前组件左上角的X坐标和Y坐标。[int32_t OH_ArkUI_PointerEvent_SetClonedEventActionType(const ArkUI_UIInputEvent* event, int32_t actionType)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_setclonedeventactiontype)设置当前带有指向性的克隆输入事件的事件类型。[int32_t OH_ArkUI_PointerEvent_SetClonedEventChangedFingerId(const ArkUI_UIInputEvent* event, int32_t fingerId)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_setclonedeventchangedfingerid)设置当前带有指向性的克隆输入事件的触摸点ID。[int32_t OH_ArkUI_PointerEvent_SetClonedEventFingerIdByIndex(const ArkUI_UIInputEvent* event, int32_t fingerId, int32_t pointerIndex)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_setclonedeventfingeridbyindex)设置带有指向性的克隆输入事件特定接触点的触摸点ID。[int32_t OH_ArkUI_PointerEvent_PostClonedEvent(ArkUI_NodeHandle node, const ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_postclonedevent)转发克隆事件到特定节点。[ArkUI_ErrorCode OH_ArkUI_UIInputEvent_GetLatestStatus()](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_getlateststatus)调用该方法获取最近一次UIInput相关方法的执行情况。通常情况下不需要使用该方法，仅在返回值结果不确定是否异常时使用。以下是一个使用示例（对于返回的float类型，0.0并不代表错误，因此可以进一步使用OH_ArkUI_UIInputEvent_GetLatestStatus方法来确认是否发生异常）。float x = OH_ArkUI_PointerEvent_GetX(event);if (ARKUI_ERROR_CODE_NO_ERROR != OH_ArkUI_UIInputEvent_GetlatestStatus()) {// errorreturn;}系统将在每次执行UIInput相关函数时主动清空上一次函数调用的状态，以确保每次通过该接口获取的均为最近一次的状态。[ArkUI_CoastingAxisEvent OH_ArkUI_UIInputEvent_GetCoastingAxisEvent(ArkUI_UIInputEvent* event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_uiinputevent_getcoastingaxisevent)获取惯性滚动轴事件的指针。[int64_t OH_ArkUI_CoastingAxisEvent_GetEventTime(ArkUI_CoastingAxisEvent event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_coastingaxisevent_geteventtime)获取惯性滚动轴事件发生的时间。[ArkUI_CoastingAxisEventPhase OH_ArkUI_CoastingAxisEvent_GetPhase(ArkUI_CoastingAxisEvent event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_coastingaxisevent_getphase)获取惯性滚动轴事件发生时的滚动阶段。[float OH_ArkUI_CoastingAxisEvent_GetDeltaY(ArkUI_CoastingAxisEvent event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_coastingaxisevent_getdeltay)获取惯性滚动轴事件垂直方向的增量值。单位为px，表示为单次滚动增量，非滚动总量。数值的正负代表方向，双指从上往下滑动时为负数，双指从下往上滑动时为正数。[float OH_ArkUI_CoastingAxisEvent_GetDeltaX(ArkUI_CoastingAxisEvent event)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_coastingaxisevent_getdeltax)获取惯性滚动轴事件水平方向的增量值。单位为px，表示为单次滚动增量，非滚动总量。数值的正负代表方向，双指从左往右滑动时为负数，双指从右往左滑动时为正数。[int32_t OH_ArkUI_CoastingAxisEvent_SetPropagation(ArkUI_CoastingAxisEvent event, bool propagation)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_coastingaxisevent_setpropagation)设置惯性滚动轴事件是否启用冒泡，默认禁止冒泡。[ArkUI_ErrorCode OH_ArkUI_TouchTestInfo_GetTouchTestInfoList(ArkUI_TouchTestInfo* info, ArkUI_TouchTestInfoItemArray* array, int32_t* size)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfo_gettouchtestinfolist)获取触摸测试信息中的触摸测试信息项数组。[float OH_ArkUI_TouchTestInfoItem_GetX(const ArkUI_TouchTestInfoItem* info)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfoitem_getx)从触摸测试信息项中获取相对于子组件左上角的X坐标，单位为px。[float OH_ArkUI_TouchTestInfoItem_GetY(const ArkUI_TouchTestInfoItem* info)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfoitem_gety)从触摸测试信息项中获取相对于子组件左上角的Y坐标，单位为px。[float OH_ArkUI_TouchTestInfoItem_GetWindowX(const ArkUI_TouchTestInfoItem* info)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfoitem_getwindowx)从触摸测试信息项中获取相对于当前应用窗口左上角的X坐标，单位为px。[float OH_ArkUI_TouchTestInfoItem_GetWindowY(const ArkUI_TouchTestInfoItem* info)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfoitem_getwindowy)从触摸测试信息项中获取相对于当前应用窗口左上角的Y坐标，单位为px。[float OH_ArkUI_TouchTestInfoItem_GetXRelativeToParent(const ArkUI_TouchTestInfoItem* info)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfoitem_getxrelativetoparent)从触摸测试信息项中获取相对于父组件左上角的X坐标，单位为px。[float OH_ArkUI_TouchTestInfoItem_GetYRelativeToParent(const ArkUI_TouchTestInfoItem* info)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfoitem_getyrelativetoparent)从触摸测试信息项中获取相对于父组件左上角的Y坐标，单位为px。[ArkUI_ErrorCode OH_ArkUI_TouchTestInfoItem_GetChildRect(const ArkUI_TouchTestInfoItem* info, ArkUI_Rect* childRect)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfoitem_getchildrect)从触摸测试信息项中获取子组件的帧矩形信息。[ArkUI_ErrorCode OH_ArkUI_TouchTestInfoItem_GetChildId(const ArkUI_TouchTestInfoItem* info, char* buffer, int32_t bufferSize)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfoitem_getchildid)从触摸测试信息项中获取子组件的ID。[ArkUI_ErrorCode OH_ArkUI_TouchTestInfo_SetTouchResultStrategy(ArkUI_TouchTestInfo* info, ArkUI_TouchTestStrategy strategy)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfo_settouchresultstrategy)设置触摸测试策略，即组件及其子组件在命中测试过程中的行为方式。[ArkUI_ErrorCode OH_ArkUI_TouchTestInfo_SetTouchResultId(ArkUI_TouchTestInfo* info, const char* id)](#ZH-CN_TOPIC_0000002497605082__oh_arkui_touchtestinfo_settouchresultid)设置命中测试过程中需要作用的子组件ID。

#### 枚举类型说明

#### ArkUI_UIInputEvent_Type

```ets
enum ArkUI_UIInputEvent_Type
```

**描述：**

UI输入事件类型定义。

**起始版本：** 12

枚举项描述ARKUI_UIINPUTEVENT_TYPE_UNKNOWN = 0未知。ARKUI_UIINPUTEVENT_TYPE_TOUCH = 1触摸事件。ARKUI_UIINPUTEVENT_TYPE_AXIS = 2轴事件。ARKUI_UIINPUTEVENT_TYPE_MOUSE = 3鼠标事件。ARKUI_UIINPUTEVENT_TYPE_KEY = 4

按键事件。

**起始版本：** 20

#### anonymous1

```ets
enum anonymous1
```

**描述：**

定义输入事件的Action Code。

**起始版本：** 12

枚举项描述UI_TOUCH_EVENT_ACTION_CANCEL = 0触摸取消。UI_TOUCH_EVENT_ACTION_DOWN = 1触摸按下。UI_TOUCH_EVENT_ACTION_MOVE = 2触摸移动。UI_TOUCH_EVENT_ACTION_UP = 3触摸抬起。

#### anonymous2

```ets
enum anonymous2
```

**描述：**

产生输入事件的工具类型定义。

**起始版本：** 12

枚举项描述UI_INPUT_EVENT_TOOL_TYPE_UNKNOWN = 0不支持的工具类型。UI_INPUT_EVENT_TOOL_TYPE_FINGER = 1手指。UI_INPUT_EVENT_TOOL_TYPE_PEN = 2笔。UI_INPUT_EVENT_TOOL_TYPE_MOUSE = 3鼠标。UI_INPUT_EVENT_TOOL_TYPE_TOUCHPAD = 4触控板。UI_INPUT_EVENT_TOOL_TYPE_JOYSTICK = 5操纵杆。

#### anonymous3

```ets
enum anonymous3
```

**描述：**

产生输入事件的来源类型定义。

**起始版本：** 12

枚举项描述UI_INPUT_EVENT_SOURCE_TYPE_UNKNOWN = 0未知输入源。UI_INPUT_EVENT_SOURCE_TYPE_MOUSE = 1鼠标。UI_INPUT_EVENT_SOURCE_TYPE_TOUCH_SCREEN = 2触摸屏。UI_INPUT_EVENT_SOURCE_TYPE_KEY = 4

按键。

**起始版本：** 22

UI_INPUT_EVENT_SOURCE_TYPE_JOYSTICK = 5

手柄。

**起始版本：** 22

#### HitTestMode

```ets
enum HitTestMode
```

**描述：**

定义触摸测试类型的枚举值。

**起始版本：** 12

枚举项描述HTM_DEFAULT = 0默认触摸测试效果。自身及子节点响应触摸测试，但阻塞兄弟节点的触摸测试，不影响祖先节点的触摸测试。HTM_BLOCK = 1自身响应触摸测试，阻塞子节点、兄弟节点和祖先节点的触摸测试。HTM_TRANSPARENT = 2自身和子节点都响应触摸测试，不会阻塞兄弟节点和祖先节点的触摸测试。HTM_NONE = 3自身不响应触摸测试，不会阻塞子节点、兄弟节点和祖先节点的触摸测试。HTM_BLOCK_HIERARCHY = 4

自身和子节点响应触摸测试，阻止所有优先级较低的兄弟节点和父节点参与触摸测试。

**起始版本：** 20

HTM_BLOCK_DESCENDANTS = 5

自身不响应触摸测试，并且所有的后代（孩子，孙子等）也不响应触摸测试，不会影响祖先节点的触摸测试。

**起始版本：** 20

#### anonymous4

```ets
enum anonymous4
```

**描述：**

定义鼠标事件的Action Code。

**起始版本：** 12

枚举项描述UI_MOUSE_EVENT_ACTION_UNKNOWN = 0无效行为。UI_MOUSE_EVENT_ACTION_PRESS = 1鼠标按键按下。UI_MOUSE_EVENT_ACTION_RELEASE = 2鼠标按键松开。UI_MOUSE_EVENT_ACTION_MOVE = 3鼠标移动。UI_MOUSE_EVENT_ACTION_CANCEL = 13

鼠标按键被取消。

**起始版本：** 18

#### anonymous5

```ets
enum anonymous5
```

**描述：**

定义鼠标事件的按键类型。

**起始版本：** 12

枚举项描述UI_MOUSE_EVENT_BUTTON_NONE = 0无按键。UI_MOUSE_EVENT_BUTTON_LEFT = 1鼠标左键。UI_MOUSE_EVENT_BUTTON_RIGHT = 2鼠标右键。UI_MOUSE_EVENT_BUTTON_MIDDLE = 3鼠标中键。UI_MOUSE_EVENT_BUTTON_BACK = 4鼠标左侧后退键。UI_MOUSE_EVENT_BUTTON_FORWARD = 5鼠标左侧前进键。

#### ArkUI_ModifierKeyName

```ets
enum ArkUI_ModifierKeyName
```

**描述：**

定义modifier按键。

**起始版本：** 12

枚举项描述ARKUI_MODIFIER_KEY_CTRL = 1 << 0Ctrl.ARKUI_MODIFIER_KEY_SHIFT = 1 << 1Shift.ARKUI_MODIFIER_KEY_ALT = 1 << 2Alt.ARKUI_MODIFIER_KEY_FN = 1 << 3Fn（仅调试使用，通常不上报Fn状态）.

#### anonymous6

```ets
enum anonymous6
```

**描述：**

定义焦点轴事件的轴类型。

**起始版本：** 15

枚举项描述UI_FOCUS_AXIS_EVENT_ABS_X = 0游戏手柄X轴。UI_FOCUS_AXIS_EVENT_ABS_Y = 1游戏手柄Y轴。UI_FOCUS_AXIS_EVENT_ABS_Z = 2游戏手柄Z轴。UI_FOCUS_AXIS_EVENT_ABS_RZ = 3游戏手柄RZ轴。UI_FOCUS_AXIS_EVENT_ABS_GAS = 4游戏手柄GAS轴。UI_FOCUS_AXIS_EVENT_ABS_BRAKE = 5游戏手柄BRAKE轴。UI_FOCUS_AXIS_EVENT_ABS_HAT0X = 6游戏手柄HAT0X轴。UI_FOCUS_AXIS_EVENT_ABS_HAT0Y = 7游戏手柄HAT0Y轴。

#### ArkUI_InteractionHand

```ets
enum ArkUI_InteractionHand
```

**描述：**

定义触摸事件是左手还是右手。

**起始版本：** 15

枚举项描述ARKUI_EVENT_HAND_NONE = 0未知。ARKUI_EVENT_HAND_LEFT = 1左手。ARKUI_EVENT_HAND_RIGHT = 2右手。

#### anonymous7

```ets
enum anonymous7
```

**描述：**

定义轴事件的操作类型。

**起始版本：** 15

枚举项描述UI_AXIS_EVENT_ACTION_NONE = 0轴事件异常。UI_AXIS_EVENT_ACTION_BEGIN = 1轴事件开始。UI_AXIS_EVENT_ACTION_UPDATE = 2轴事件更新。UI_AXIS_EVENT_ACTION_END = 3轴事件结束。UI_AXIS_EVENT_ACTION_CANCEL = 4轴事件取消。

#### anonymous8

```ets
enum anonymous8
```

**描述：**

定义轴事件的轴类型。

**起始版本：** 22

枚举项描述UI_AXIS_TYPE_VERTICAL_AXIS = 0垂直滚动轴。UI_AXIS_TYPE_HORIZONTAL_AXIS = 1水平滚动轴。UI_AXIS_TYPE_PINCH_AXIS = 2捏合轴。

#### ArkUI_CoastingAxisEventPhase

```ets
enum ArkUI_CoastingAxisEventPhase
```

**描述：**

定义惯性滚动轴事件的阶段。

**起始版本：** 22

枚举项描述ARKUI_COASTING_AXIS_EVENT_PHASE_NONE = 0非惯性轴事件阶段，异常默认值，可以通过检查惯性轴阶段值不为该值来判断当前惯性轴事件是有效的。ARKUI_COASTING_AXIS_EVENT_PHASE_BEGIN = 1惯性滚动轴事件开始，此为惯性阶段的第一个事件。ARKUI_COASTING_AXIS_EVENT_PHASE_UPDATE = 2惯性滚动轴事件更新，此阶段可以获取惯性轴值增量来处理滚动偏移。ARKUI_COASTING_AXIS_EVENT_PHASE_END = 3惯性滚动轴事件结束，此值在惯性被刹停（惯性滚动阶段用户重新触摸触控板或通过鼠标及触屏与组件产生交互等）或惯性衰减至自然停止时发送，到达此阶段时，应立即停止惯性滚动效果。

#### ArkUI_TouchTestStrategy

```ets
enum ArkUI_TouchTestStrategy
```

**描述：**

定义触摸测试策略。

**起始版本：** 22

枚举项描述ARKUI_TOUCH_TEST_STRATEGY_DEFAULT = 0自定义分发不产生影响，系统按当前节点命中状态分发事件。ARKUI_TOUCH_TEST_STRATEGY_FORWARD_COMPETITION = 1应用指定分发事件到某个子节点，其他兄弟节点是否分发事件交由系统决定。ARKUI_TOUCH_TEST_STRATEGY_FORWARD = 2应用指定分发事件到某个子节点，系统不再分发事件到其他兄弟节点。

#### 函数说明

#### OH_ArkUI_UIInputEvent_GetType()

```ets
int32_t OH_ArkUI_UIInputEvent_GetType(const ArkUI_UIInputEvent* event)
```

**描述：**

获取UI输入事件的类型。在访问一个ArkUI_UIInputEvent指针对象之前，推荐使用该方法判断该输入事件的类型，该接口会返回[ArkUI_UIInputEvent_Type](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__arkui_uiinputevent_type)枚举中的一种。比如，当事件是一个触控类型时，由于触控类型是指向性事件，那么使用OH_ArkUI_UIInputEvent_GetXXX及OH_ArkUI_PointerEvent_GetXXX系列接口，均可以正常访问；而如果使用OH_ArkUI_KeyEvent_GetXXX相关接口去访问它，则会有无法预期的结果。对于还未支持的事件类型，接口返回默认值0。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明int32_t返回当前UI输入事件的类型，如果参数异常则返回0。

#### OH_ArkUI_UIInputEvent_GetAction()

```ets
int32_t OH_ArkUI_UIInputEvent_GetAction(const ArkUI_UIInputEvent* event)
```

**描述：**

获取输入事件的action类型。action类型为基础事件在不同阶段的类型定义，通常代表了事件的特点，并表征事件的开始与结束，如touch down, touch up。触控事件的action类型为[UI_TOUCH_EVENT_ACTION_XXX](#ZH-CN_TOPIC_0000002497605082__anonymous1)，鼠标事件的action类型为[UI_MOUSE_EVENT_ACTION_XXX](#ZH-CN_TOPIC_0000002497605082__anonymous4)。轴事件的action类型获取请使用[OH_ArkUI_AxisEvent_GetAxisAction](#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_getaxisaction)，返回值类型为[UI_AXIS_EVENT_ACTION_XXX](#ZH-CN_TOPIC_0000002497605082__anonymous7)，按键事件的action类型获取请使用[OH_ArkUI_KeyEvent_GetType](native_key_event.h.md#ZH-CN_TOPIC_0000002497445100__oh_arkui_keyevent_gettype)接口。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明int32_t返回当前UI输入事件的操作类型，如果参数异常则返回-1。

#### OH_ArkUI_UIInputEvent_GetSourceType()

```ets
int32_t OH_ArkUI_UIInputEvent_GetSourceType(const ArkUI_UIInputEvent* event)
```

**描述：**

获取UI输入事件的触发源类型。输入源为产生输入事件的真实物理设备，如触摸屏，鼠标等，由UI_INPUT_EVENT_SOURCE_TYPE_XXX定义，而输入工具为操作输入源设备来产生事件的工具，如手指、触控笔。在某些情况下两者可能容易发生混淆，比如当用户在操作鼠标时，鼠标既是输入源，也是输入工具。对于按键事件，并不支持获取输入源类型，返回unkown。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明int32_t返回产生当前UI输入事件的来源类型。

#### OH_ArkUI_UIInputEvent_GetToolType()

```ets
int32_t OH_ArkUI_UIInputEvent_GetToolType(const ArkUI_UIInputEvent* event)
```

**描述：**

获取UI输入事件的工具类型。输入工具为操作输入源设备来产生事件的操作方，如手指、触控笔，他们自身不真实产生事件，但可以驱动输入源设备不断产生事件。返回的类型由UI_INPUT_EVENT_TOOL_TYPE_XXX枚举值定义。对于按键事件，并不支持获取输入工具类型，返回unkown。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明int32_t返回产生当前UI输入事件的工具类型。

#### OH_ArkUI_UIInputEvent_GetEventTime()

```ets
int64_t OH_ArkUI_UIInputEvent_GetEventTime(const ArkUI_UIInputEvent* event)
```

**描述：**

获取UI输入事件发生的时间。单位为ns。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明int64_t返回UI输入事件发生的时间，如果参数异常则返回0。

#### OH_ArkUI_PointerEvent_GetPointerCount()

```ets
uint32_t OH_ArkUI_PointerEvent_GetPointerCount(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取多点触控的接触点数量。指向性事件一般是附带有事件发生位置信息的事件，如触摸事件，用户操作时，可以感知事件在什么位置发生。而非指向性事件，如按键事件，一般没有位置信息，没有触点的说法，所以该接口对按键事件无效。对于触摸事件，该接口多用于处理多指触控，判断用户有几根手指在操作当前控件。而对于鼠标和轴事件，可认为触点只有1个，该接口永远返回1。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明uint32_t返回当前带有指向性的输入事件的接触点数量。

#### OH_ArkUI_PointerEvent_GetPointerId()

```ets
int32_t OH_ArkUI_PointerEvent_GetPointerId(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取多点触控的接触点标识。返回事件发生时，事件触点的唯一标识符，用于区分同类输入设备的多点触控信息。其数值没有除标识触点外的其他含义。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明int32_t返回特定接触点标识。

#### OH_ArkUI_PointerEvent_GetChangedPointerId()

```ets
int32_t OH_ArkUI_PointerEvent_GetChangedPointerId(const ArkUI_UIInputEvent* event, uint32_t* pointerIndex)
```

**描述：**

获取触发当前事件的对应的手指id。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t* pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_PointerEvent_GetX()

```ets
float OH_ArkUI_PointerEvent_GetX(const ArkUI_UIInputEvent* event)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前组件左上角的X坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前组件左上角的X坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetXByIndex()

```ets
float OH_ArkUI_PointerEvent_GetXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前组件左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，返回默认值0.0f。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前组件左上角的X坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetY()

```ets
float OH_ArkUI_PointerEvent_GetY(const ArkUI_UIInputEvent* event)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前组件左上角的Y坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前组件左上角的Y坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetYByIndex()

```ets
float OH_ArkUI_PointerEvent_GetYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前组件左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，返回默认值0.0f。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前组件左上角的Y坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetWindowX()

```ets
float OH_ArkUI_PointerEvent_GetWindowX(const ArkUI_UIInputEvent* event)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前应用窗口左上角的X坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前应用窗口左上角的X坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetWindowXByIndex()

```ets
float OH_ArkUI_PointerEvent_GetWindowXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前应用窗口左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前应用窗口左上角的X坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetWindowY()

```ets
float OH_ArkUI_PointerEvent_GetWindowY(const ArkUI_UIInputEvent* event)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前应用窗口左上角的Y坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前应用窗口左上角的Y坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetWindowYByIndex()

```ets
float OH_ArkUI_PointerEvent_GetWindowYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前应用窗口左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前应用窗口左上角的Y坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetDisplayX()

```ets
float OH_ArkUI_PointerEvent_GetDisplayX(const ArkUI_UIInputEvent* event)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前屏幕左上角的X坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前屏幕左上角的X坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetDisplayXByIndex()

```ets
float OH_ArkUI_PointerEvent_GetDisplayXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前屏幕左上角的X坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前屏幕左上角的X坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetDisplayY()

```ets
float OH_ArkUI_PointerEvent_GetDisplayY(const ArkUI_UIInputEvent* event)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于当前屏幕左上角的Y坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前屏幕左上角的Y坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetDisplayYByIndex()

```ets
float OH_ArkUI_PointerEvent_GetDisplayYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取特定接触点相对于当前屏幕左上角的Y坐标。对于鼠标和轴事件，当给定的索引大于0时，总是返回默认值0.0f。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前屏幕左上角的Y坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetGlobalDisplayX()

```ets
float OH_ArkUI_PointerEvent_GetGlobalDisplayX(const ArkUI_UIInputEvent* event)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的X坐标。只能从pointer-likely事件中获取位置信息。

**起始版本：** 20

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明floatfloat 返回相对于全局显示的X坐标，单位为px。如果发生任何参数错误，例如传递的一个事件没有位置信息，则返回0。

#### OH_ArkUI_PointerEvent_GetGlobalDisplayXByIndex()

```ets
float OH_ArkUI_PointerEvent_GetGlobalDisplayXByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的X坐标。只能从指针事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。

**起始版本：** 20

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中目标触控点的索引。有效值范围[0, [OH_ArkUI_PointerEvent_GetPointerCount()](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getpointercount) - 1]

**返回：**

类型说明floatfloat 返回相对于全局显示的X坐标，单位为px。如果发生任何参数错误，则返回0.0f。

#### OH_ArkUI_PointerEvent_GetGlobalDisplayY()

```ets
float OH_ArkUI_PointerEvent_GetGlobalDisplayY(const ArkUI_UIInputEvent* event)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的Y坐标。只能从pointer-likely事件中获取位置信息。

**起始版本：** 20

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明floatfloat 返回相对于全局显示的Y坐标，单位为px。如果发生任何参数错误，例如传递的一个事件没有位置信息，则返回0。

#### OH_ArkUI_PointerEvent_GetGlobalDisplayYByIndex()

```ets
float OH_ArkUI_PointerEvent_GetGlobalDisplayYByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件、鼠标事件、轴事件）中获取相对于全局显示的Y坐标。只能从指针事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。

**起始版本：** 20

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中目标触控点的索引。有效值范围[0, [OH_ArkUI_PointerEvent_GetPointerCount()](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getpointercount) - 1]

**返回：**

类型说明floatfloat 返回相对于全局显示的Y坐标，单位为px。如果发生任何参数错误，则返回0.0f。

#### OH_ArkUI_PointerEvent_GetPressure()

```ets
float OH_ArkUI_PointerEvent_GetPressure(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件）中获取触屏压力。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件产生的触屏压力，如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetTiltX()

```ets
float OH_ArkUI_PointerEvent_GetTiltX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取相对YZ平面的角度，取值的范围[-90, 90]，其中正值是向右倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件中相对YZ平面的角度。

#### OH_ArkUI_PointerEvent_GetTiltY()

```ets
float OH_ArkUI_PointerEvent_GetTiltY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取相对XZ平面的角度，取值的范围[-90, 90]，其中正值是向右倾斜。仅适用于支持倾角上报的触控笔操作产生的触控事件。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件中相对XZ平面的角度。

#### OH_ArkUI_PointerEvent_GetRollAngle()

```ets
int32_t OH_ArkUI_PointerEvent_GetRollAngle(const ArkUI_UIInputEvent* event, double* rollAngle)
```

**描述：**

获取触控笔绕Z轴旋转的角度。

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event指向当前UI输入事件的指针。double* rollAngle触控笔绕Z轴旋转的角度，单位为deg。

**返回：**

类型说明int32_t

错误码。

Returns [ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

Returns [ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_PointerEvent_GetTouchAreaWidth()

```ets
float OH_ArkUI_PointerEvent_GetTouchAreaWidth(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取触屏区域的宽度。仅适用于手指操作产生的触控事件，这通常是一个圆形区域的半径。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件中触屏区域的宽度，单位为px。

#### OH_ArkUI_PointerEvent_GetTouchAreaHeight()

```ets
float OH_ArkUI_PointerEvent_GetTouchAreaHeight(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

从指向性输入事件（如触摸事件）中获取触屏区域的高度。仅适用于手指操作产生的触控事件，这通常是一个圆形区域的半径。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件中触屏区域的高度，单位为px。

#### OH_ArkUI_PointerEvent_GetInteractionHand()

```ets
int32_t OH_ArkUI_PointerEvent_GetInteractionHand(const ArkUI_UIInputEvent *event, ArkUI_InteractionHand *hand)
```

**描述：**

获取当前触摸事件是左手点击触发还是右手点击触发。仅在部分触控产品上有效。该值并非在按下时就能实时获取，在系统完成结果推断之前，皆默认返回NONE，因此请不要过度依赖该接口返回的结果。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md) *event表示指向当前UI输入事件的指针。[ArkUI_InteractionHand](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__arkui_interactionhand) *hand表示触摸点是左手还是右手。

**返回：**

类型说明int32_t

返回结果。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果发生参数异常，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_PointerEvent_GetInteractionHandByIndex()

```ets
int32_t OH_ArkUI_PointerEvent_GetInteractionHandByIndex(const ArkUI_UIInputEvent *event, int32_t pointerIndex, ArkUI_InteractionHand *hand)
```

**描述：**

获取当前触摸事件是左手点击触发还是右手点击触发。仅在部分触控产品上有效。该值并非在按下时就能实时获取，在系统完成结果推断之前，皆默认返回NONE，因此请不要过度依赖该接口返回的结果。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md) *event表示指向当前UI输入事件的指针。int32_t pointerIndex表示多点触控数据列表中目标触控点的索引。[ArkUI_InteractionHand](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__arkui_interactionhand) *hand表示触摸点是左手还是右手。

**返回：**

类型说明int32_t

返回结果。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果发生参数异常，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_PointerEvent_GetHistorySize()

```ets
uint32_t OH_ArkUI_PointerEvent_GetHistorySize(const ArkUI_UIInputEvent* event)
```

**描述：**

从指向性输入事件（如触摸事件）中获取历史事件数量。历史事件为此次事件与上一次事件之间发生的原始事件，仅适用于move事件。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明uint32_t返回当前历史事件数量。

#### OH_ArkUI_PointerEvent_GetHistoryEventTime()

```ets
int64_t OH_ArkUI_PointerEvent_GetHistoryEventTime(const ArkUI_UIInputEvent* event, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取历史事件发生的时间。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明int64_t返回UI输入事件发生的时间，单位为ns。如果参数异常则返回0。

#### OH_ArkUI_PointerEvent_GetHistoryPointerCount()

```ets
uint32_t OH_ArkUI_PointerEvent_GetHistoryPointerCount(const ArkUI_UIInputEvent* event, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中多点触控的接触点数量。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明uint32_t特定历史事件中多点触控的接触点数量。

#### OH_ArkUI_PointerEvent_GetHistoryPointerId()

```ets
int32_t OH_ArkUI_PointerEvent_GetHistoryPointerId(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从指向性输入事件（如触摸事件）的历史点中获取多点触控的接触点标识。返回事件发生时，事件触点的唯一标识符，用于区分同类输入设备的多点触控信息。其数值没有除标识触点外的其他含义。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明int32_t返回特定历史事件中的特定接触点标识。

#### OH_ArkUI_PointerEvent_GetHistoryX()

```ets
float OH_ArkUI_PointerEvent_GetHistoryX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前组件左上角的X坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前组件左上角的X坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetHistoryY()

```ets
float OH_ArkUI_PointerEvent_GetHistoryY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前组件左上角的Y坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前组件左上角的Y坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetHistoryWindowX()

```ets
float OH_ArkUI_PointerEvent_GetHistoryWindowX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前应用窗口左上角的X坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前应用窗口左上角的X坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetHistoryWindowY()

```ets
float OH_ArkUI_PointerEvent_GetHistoryWindowY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前应用窗口左上角的Y坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前应用窗口左上角的Y坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetHistoryDisplayX()

```ets
float OH_ArkUI_PointerEvent_GetHistoryDisplayX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前屏幕左上角的X坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前屏幕左上角的X坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetHistoryDisplayY()

```ets
float OH_ArkUI_PointerEvent_GetHistoryDisplayY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件、鼠标事件、轴事件）中获取特定历史事件中特定接触点相对于当前屏幕左上角的Y坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件相对于当前屏幕左上角的Y坐标，单位为px。如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetHistoryGlobalDisplayX()

```ets
float OH_ArkUI_PointerEvent_GetHistoryGlobalDisplayX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从给定指针索引和历史记录索引的输入事件（如触摸事件、鼠标事件、轴事件）中获取历史事件中相对于全局显示的特定触摸点的X坐标。只能从指针事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。

**起始版本：** 20

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中目标触控点的索引。有效值范围[0, [OH_ArkUI_PointerEvent_GetPointerCount()](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getpointercount) - 1]uint32_t historyIndex表示要返回的历史值，必须小于[OH_ArkUI_PointerEvent_GetHistorySize](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorysize)。

**返回：**

类型说明floatfloat 返回相对于全局显示的X坐标，单位为px。如果发生任何参数错误，则返回0.0f。

#### OH_ArkUI_PointerEvent_GetHistoryGlobalDisplayY()

```ets
float OH_ArkUI_PointerEvent_GetHistoryGlobalDisplayY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从给定指针索引和历史记录索引的输入事件（如触摸事件、鼠标事件、轴事件）中获取历史事件中相对于全局显示的特定触摸点的Y坐标。只能从指针事件中获取位置信息，对于鼠标和轴事件，当给定的pointerIndex大于0时，始终返回默认值0.0f。

**起始版本：** 20

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中目标触控点的索引。有效值范围[0, [OH_ArkUI_PointerEvent_GetPointerCount()](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_getpointercount) - 1]uint32_t historyIndex表示要返回的历史值，必须小于[OH_ArkUI_PointerEvent_GetHistorySize](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_gethistorysize)。

**返回：**

类型说明floatfloat 返回相对于全局显示的Y坐标，如果发生任何参数错误，则返回0.0f。

#### OH_ArkUI_PointerEvent_GetHistoryPressure()

```ets
float OH_ArkUI_PointerEvent_GetHistoryPressure(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件）中获取特定历史事件中的触屏压力。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件产生的触屏压力，如果参数异常则返回0.0f。

#### OH_ArkUI_PointerEvent_GetHistoryTiltX()

```ets
float OH_ArkUI_PointerEvent_GetHistoryTiltX(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件）中获取特定历史事件中的相对YZ平面的角度，取值的范围[-90, 90]，单位为deg，其中正值是向右倾斜。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件中相对YZ平面的角度。

#### OH_ArkUI_PointerEvent_GetHistoryTiltY()

```ets
float OH_ArkUI_PointerEvent_GetHistoryTiltY(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件）中获取特定历史事件中的相对XZ平面的角度，值的范围[-90, 90]，单位为deg，其中正值是向下倾斜。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件中相对XZ平面的角度。

#### OH_ArkUI_PointerEvent_GetHistoryTouchAreaWidth()

```ets
float OH_ArkUI_PointerEvent_GetHistoryTouchAreaWidth(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件）中获取特定历史事件中的触屏区域的宽度。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件中触屏区域的宽度，单位为px。

#### OH_ArkUI_PointerEvent_GetHistoryTouchAreaHeight()

```ets
float OH_ArkUI_PointerEvent_GetHistoryTouchAreaHeight(const ArkUI_UIInputEvent* event, uint32_t pointerIndex, uint32_t historyIndex)
```

**描述：**

从带有指向性的输入事件（如触摸事件）中获取特定历史事件中的触屏区域的高度。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。uint32_t pointerIndex表示多点触控数据列表中的序号。uint32_t historyIndex表示历史事件数据列表的序号。

**返回：**

类型说明float返回当前带有指向性的输入事件中触屏区域的高度，单位为px。

#### OH_ArkUI_AxisEvent_GetVerticalAxisValue()

```ets
double OH_ArkUI_AxisEvent_GetVerticalAxisValue(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前轴事件的垂直滚动轴的值。通常由鼠标滚轮，或用户在触控板上双指竖向滑动产生。当通过鼠标滚动触发时：1.上报的数值单位为角度，为单次滚动角度增量，非滚动总量；2.上报的数值已与用户配置的放大系数[OH_ArkUI_AxisEvent_GetScrollStep](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_getscrollstep)叠加运算；3.数值的正负代表方向，向前滚动鼠标滚轮时上报数值为负数，向后滚动鼠标滚轮时上报数值为正数；当通过触控板双指竖向滑动时：1.上报的数值单位为PX，为单次滚动增量，非滚动总量；2.上报的数值不受用户配置的放大系数[OH_ArkUI_AxisEvent_GetScrollStep](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_getscrollstep)影响；3.数值的正负代表方向，双指从上往下滑动时上报数值为负数，双指从下往上滑动时上报数值为正数；4.方向会受系统设置中"自然滚动"配置的影响。通常情况下，垂直滚动轴事件只能驱动竖向的滑动手势响应，但当鼠标指针下命中的可滑动手势里，如果可响应的方向都是一致的，那么垂直滚动轴事件可以驱动这些滑动手势得到响应，即使这些手势所定义的方向是横向的。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明double返回当前轴事件的垂直滚动轴的值，如果参数异常则返回0.0。

#### OH_ArkUI_AxisEvent_GetHorizontalAxisValue()

```ets
double OH_ArkUI_AxisEvent_GetHorizontalAxisValue(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前轴事件的水平滚动轴的值，通过在触控板上双指横向滑动产生。1.上报的数值单位为PX，为单次滚动增量，非滚动总量；2.上报的数值不受用户配置的放大系数[OH_ArkUI_AxisEvent_GetScrollStep](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__oh_arkui_axisevent_getscrollstep)影响；3.数值的正负代表方向，双指从左往右滑动时上报数值为负数，双指从右往左滑动时上报数值为正数；4.方向会受系统设置中"自然滚动"配置的影响。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明double返回当前轴事件的水平滚动轴的值，如果参数异常则返回0.0。

#### OH_ArkUI_AxisEvent_GetPinchAxisScaleValue()

```ets
double OH_ArkUI_AxisEvent_GetPinchAxisScaleValue(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前轴事件的捏合轴缩放的值。通过触控板双指缩放/捏合操作产生。上报的scale数值，为相对于初始状态时的当前scale值。初始状态为系统识别到用户通过触控板发生了捏合操作时的两指位置状态，此时的scale数值为1.0。在手指抬起前的本次捏合操作过程中，所上报的scale数值均将初始状态作为参考系，从初始状态往中心捏合，则上报的scale会从1.0逐步往0.0缩小；当从初始化状态往外扩大双指距离时，会从1.0逐步变大。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明double返回当前轴事件的捏合轴缩放的值，如果参数异常则返回0.0。

#### OH_ArkUI_AxisEvent_GetAxisAction()

```ets
int32_t OH_ArkUI_AxisEvent_GetAxisAction(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前轴事件的操作类型。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明int32_t返回当前轴事件的操作类型。

#### OH_ArkUI_AxisEvent_HasAxis()

```ets
int32_t OH_ArkUI_AxisEvent_HasAxis(const ArkUI_UIInputEvent* event, int32_t axis)
```

**描述：**

检测此轴事件是否包含指定的轴类型。

**起始版本：** 22

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。int32_t axis表示轴事件的轴类型[UI_AXIS_TYPE_XXX](#ZH-CN_TOPIC_0000002497605082__anonymous8)。

**返回值：**

类型说明int32_t返回此轴事件是否包含指定的轴类型。返回true表示包含指定的轴类型，返回false表示不包含指定的轴类型。

#### OH_ArkUI_PointerEvent_SetInterceptHitTestMode()

```ets
int32_t OH_ArkUI_PointerEvent_SetInterceptHitTestMode(const ArkUI_UIInputEvent* event, HitTestMode mode)
```

**描述：**

配置HitTest模式。仅适用于接收基础事件的场景，如使用NODE_ON_TOUCH接收touch事件场景。对于通过[OH_ArkUI_GestureEvent_GetRawInputEvent](native_gesture.h.md#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureevent_getrawinputevent)接口从一个手势事件中获取到的ArkUI_UIInputEvent对象，无法使用该接口。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。[HitTestMode](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__hittestmode) mode指定HitTest模式，参数类型[HitTestMode](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__hittestmode)。

**返回：**

类型说明int32_t返回执行的状态代码。

#### OH_ArkUI_MouseEvent_GetMouseButton()

```ets
int32_t OH_ArkUI_MouseEvent_GetMouseButton(const ArkUI_UIInputEvent* event)
```

**描述：**

获取鼠标事件的按键类型的值。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明int32_t返回鼠标按键类型，1为左键，2为右键，3为中键，4为后退键，5为前进键。

#### OH_ArkUI_MouseEvent_GetMouseAction()

```ets
int32_t OH_ArkUI_MouseEvent_GetMouseAction(const ArkUI_UIInputEvent* event)
```

**描述：**

获取鼠标事件的鼠标动作类型的值。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。

**返回：**

类型说明int32_t返回鼠标动作类型，1表示按键按下，2表示按键松开，3表示鼠标移动。

#### OH_ArkUI_PointerEvent_SetStopPropagation()

```ets
int32_t OH_ArkUI_PointerEvent_SetStopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)
```

**描述：**

设置是否阻止事件冒泡。仅适用于接收基础事件的场景，如使用NODE_ON_TOUCH接收touch事件场景，不适用于轴事件。对于通过[OH_ArkUI_GestureEvent_GetRawInputEvent](native_gesture.h.md#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureevent_getrawinputevent)接口从一个手势事件中获取到的ArkUI_UIInputEvent对象，无法使用该接口。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。bool stopPropagation表示是否阻止事件冒泡。true表示阻止事件冒泡，false表示不阻止事件冒泡。

**返回：**

类型说明int32_t返回执行的状态代码。返回0表示设置成功，如果返回401，表示返回失败，可能的原因是参数异常，例如event是一个空指针。

#### OH_ArkUI_UIInputEvent_GetDeviceId()

```ets
int32_t OH_ArkUI_UIInputEvent_GetDeviceId(const ArkUI_UIInputEvent* event)
```

**描述：**

获取当前按键的输入设备ID。

**起始版本：** 14

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明int32_t当前按键的输入设备ID。

#### OH_ArkUI_UIInputEvent_GetPressedKeys()

```ets
int32_t OH_ArkUI_UIInputEvent_GetPressedKeys(const ArkUI_UIInputEvent* event, int32_t* pressedKeyCodes, int32_t* length)
```

**描述：**

获取所有按下的按键，当前只支持按键事件。

**起始版本：** 14

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。int32_t* pressedKeyCodes输出参数，表示所有按下键的数组，指向的内存空间需要调用者申请。int32_t* length作为输入参数表示传入的pressedKeyCodes数组长度，作为输出参数表示实际按下按键的个数。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_BUFFER_SIZE_NOT_ENOUGH](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 内存分配不足。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_FocusAxisEvent_GetAxisValue()

```ets
double OH_ArkUI_FocusAxisEvent_GetAxisValue(const ArkUI_UIInputEvent* event, int32_t axis)
```

**描述：**

获取焦点轴事件的轴值。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。int32_t axis焦点轴事件的轴类型。

**返回：**

类型说明double焦点轴事件的轴值，如果参数异常则返回0.0。

#### OH_ArkUI_FocusAxisEvent_SetStopPropagation()

```ets
int32_t OH_ArkUI_FocusAxisEvent_SetStopPropagation(const ArkUI_UIInputEvent* event, bool stopPropagation)
```

**描述：**

设置是否阻止焦点轴事件冒泡。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前UI输入事件的指针。bool stopPropagation表示是否阻止事件冒泡。true表示阻止事件冒泡，false表示不阻止事件冒泡。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数异常。

#### OH_ArkUI_UIInputEvent_GetModifierKeyStates()

```ets
int32_t OH_ArkUI_UIInputEvent_GetModifierKeyStates(const ArkUI_UIInputEvent* event, uint64_t* keys)
```

**描述：**

获取UI输入事件的修饰键状态。该接口会通过keys传出当前事件发生时所有修饰键的状态，你可以通过与[ArkUI_ModifierKeyName](ui_input_event.h.md#ZH-CN_TOPIC_0000002497605082__arkui_modifierkeyname)中定义的修饰键类型进行位计算操作获取哪些键处于按下状态。

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。uint64_t* keys返回当前处于按下状态的modifier key组合，应用可通过位运算进行判断。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_AxisEvent_SetPropagation()

```ets
int32_t OH_ArkUI_AxisEvent_SetPropagation(const ArkUI_UIInputEvent* event, bool propagation)
```

**描述：**

设置是否使能轴事件冒泡。默认不会进行冒泡传递，仅发送给第一个可响应轴事件的控件。可在接收到轴事件时，主动使能冒泡传递，以便当前事件可以继续传递给响应链上的下一个可响应轴事件的祖先组件处理。不支持对从手势事件中获取到的轴事件进行设置。

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event表示指向当前 UI 输入事件的指针。bool propagation表示是否激活事件冒泡。true表示激活事件冒泡，false表示不激活事件冒泡。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数异常。

#### OH_ArkUI_AxisEvent_GetScrollStep()

```ets
int32_t OH_ArkUI_AxisEvent_GetScrollStep(const ArkUI_UIInputEvent* event)
```

**描述：**

获取滚动轴事件的滚动步长系数，适用于鼠标滚轮产生的轴事件。这个值可以告诉你用户所配置的滚动放大系数。

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event指向 ArkUI_UIInputEvent事件指针。

**返回：**

类型说明int32_t返回鼠标滚轮轴滚动步长配置。

#### OH_ArkUI_UIInputEvent_GetEventTargetWidth()

```ets
float OH_ArkUI_UIInputEvent_GetEventTargetWidth(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的宽度。

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event指向ArkUI_UIInputEvent对象的指针。

**返回：**

类型说明float返回事件命中的组件的宽度；如果发生任何参数错误，则返回 0.0f。

#### OH_ArkUI_UIInputEvent_GetEventTargetHeight()

```ets
float OH_ArkUI_UIInputEvent_GetEventTargetHeight(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的高度。

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event指向ArkUI_UIInputEvent对象的指针。

**返回：**

类型说明float返回事件命中的组件的高度；如果发生任何参数错误，则返回 0.0f。

#### OH_ArkUI_UIInputEvent_GetEventTargetPositionX()

```ets
float OH_ArkUI_UIInputEvent_GetEventTargetPositionX(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的X坐标。

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event指向ArkUI_UIInputEvent对象的指针。

**返回：**

类型说明float返回事件命中的组件的X坐标；如果发生任何参数错误，则返回 0.0f。

#### OH_ArkUI_UIInputEvent_GetEventTargetPositionY()

```ets
float OH_ArkUI_UIInputEvent_GetEventTargetPositionY(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的Y坐标。

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event指向ArkUI_UIInputEvent对象的指针。

**返回：**

类型说明float返回事件命中的组件的Y坐标；如果发生任何参数错误，则返回 0.0f。

#### OH_ArkUI_UIInputEvent_GetEventTargetGlobalPositionX()

```ets
float OH_ArkUI_UIInputEvent_GetEventTargetGlobalPositionX(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的全局X坐标。

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event指向ArkUI_UIInputEvent对象的指针。

**返回：**

类型说明float返回事件命中的组件的全局X坐标；如果发生任何参数错误，则返回 0.0f。

#### OH_ArkUI_UIInputEvent_GetEventTargetGlobalPositionY()

```ets
float OH_ArkUI_UIInputEvent_GetEventTargetGlobalPositionY(const ArkUI_UIInputEvent* event)
```

**描述：**

获取事件命中的组件的全局Y坐标。

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* event指向ArkUI_UIInputEvent对象的指针。

**返回：**

类型说明float返回事件命中的组件的全局Y坐标；如果发生任何参数错误，则返回 0.0f。

#### OH_ArkUI_PointerEvent_GetPressedTimeByIndex()

```ets
int64_t OH_ArkUI_PointerEvent_GetPressedTimeByIndex(const ArkUI_UIInputEvent* event, uint32_t pointerIndex)
```

**描述：**

获取指定触点的按下时间。仅对触摸事件有效。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。uint32_t pointerIndex指示多点触控数据列表中目标触控点的索引。

**返回：**

类型说明int64_t返回特定触摸点的按下时间，单位为ns；如果发生任何参数错误，则返回0。

#### OH_ArkUI_MouseEvent_GetRawDeltaX()

```ets
float OH_ArkUI_MouseEvent_GetRawDeltaX(const ArkUI_UIInputEvent* event)
```

**描述：**

获取鼠标设备在二维平面X轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明float返回鼠标设备在二维平面X轴的移动增量，使用物理世界中鼠标移动的距离单位进行表示；如果发生任何参数错误，则返回0.0f。

#### OH_ArkUI_MouseEvent_GetRawDeltaY()

```ets
float OH_ArkUI_MouseEvent_GetRawDeltaY(const ArkUI_UIInputEvent* event)
```

**描述：**

获取鼠标设备在二维平面Y轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明float返回鼠标设备在二维平面Y轴的移动增量，使用物理世界中鼠标移动的距离单位进行表示；如果发生任何参数错误，则返回0.0f。

#### OH_ArkUI_MouseEvent_GetPressedButtons()

```ets
int32_t OH_ArkUI_MouseEvent_GetPressedButtons(const ArkUI_UIInputEvent* event, int32_t* pressedButtons, int32_t* length)
```

**描述：**

从鼠标事件中获取按下的按键。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。int32_t* pressedButtons指示按下按键的列表。需要先创建一个int数组，用来储存按下的按键，按键的值请参考[anonymous5](#ZH-CN_TOPIC_0000002497605082__anonymous5)。int32_t* length指示列表数组的总长度。

**返回：**

类型说明int32_t

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果给定的缓冲区不够，则返回[ARKUI_ERROR_CODE_BUFFER_SIZE_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_UIInputEvent_GetTargetDisplayId()

```ets
int32_t OH_ArkUI_UIInputEvent_GetTargetDisplayId(const ArkUI_UIInputEvent* event)
```

**描述：**

获取发生UI输入事件的屏幕ID。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明int32_t返回屏幕ID；如果发生任何参数错误，则返回0。

#### OH_ArkUI_HoverEvent_IsHovered()

```ets
bool OH_ArkUI_HoverEvent_IsHovered(const ArkUI_UIInputEvent* event)
```

**描述：**

获取鼠标是否悬浮在当前组件上

**起始版本：** 17

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明bool

如果鼠标悬浮在当前组件上则返回true。

如果鼠标没有悬浮在当前组件上，返回false

#### OH_ArkUI_PointerEvent_CreateClonedEvent()

```ets
int32_t OH_ArkUI_PointerEvent_CreateClonedEvent(const ArkUI_UIInputEvent* event, ArkUI_UIInputEvent** clonedEvent)
```

**描述：**

基于原始事件指针创建克隆事件指针。仅对触摸事件有效。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。[ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)** clonedEventArkUI_UIInputEvent克隆事件指针。

**返回：**

类型说明int32_t

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果事件指针创建失败，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_PointerEvent_DestroyClonedEvent()

```ets
int32_t OH_ArkUI_PointerEvent_DestroyClonedEvent(const ArkUI_UIInputEvent* event)
```

**描述：**

销毁克隆事件指针。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明int32_t

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果输入的事件指针不是克隆事件指针，则返回[ARKUI_ERROR_CODE_NOT_CLONED_POINTER_EVENT](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_PointerEvent_SetClonedEventLocalPosition()

```ets
int32_t OH_ArkUI_PointerEvent_SetClonedEventLocalPosition(const ArkUI_UIInputEvent* event, float x, float y)
```

**描述：**

设置指向性事件相对于当前组件左上角的X坐标和Y坐标。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。float x当前带有指向性的输入事件相对于当前组件左上角的X坐标，单位为px。float y当前带有指向性的输入事件相对于当前组件左上角的Y坐标，单位为px。

**返回：**

类型说明int32_t

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果输入的事件指针不是克隆事件指针，则返回[ARKUI_ERROR_CODE_NOT_CLONED_POINTER_EVENT](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_PointerEvent_SetClonedEventLocalPositionByIndex()

```ets
int32_t OH_ArkUI_PointerEvent_SetClonedEventLocalPositionByIndex(const ArkUI_UIInputEvent* event, float x, float y, int32_t pointerIndex)
```

**描述：**

设置指向性事件特有接触点相对于当前组件左上角的X坐标和Y坐标。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。float x当前带有指向性的输入事件相对于当前组件左上角的X坐标，单位为px。float y当前带有指向性的输入事件相对于当前组件左上角的Y坐标，单位为px。int32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明int32_t

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果输入的事件指针不是克隆事件指针，则返回[ARKUI_ERROR_CODE_NOT_CLONED_POINTER_EVENT](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_PointerEvent_SetClonedEventActionType()

```ets
int32_t OH_ArkUI_PointerEvent_SetClonedEventActionType(const ArkUI_UIInputEvent* event, int32_t actionType)
```

**描述：**

设置当前带有指向性的克隆输入事件的事件类型。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。int32_t actionTypeArkUI_UIInputEvent克隆事件类型。

**返回：**

类型说明int32_t

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果输入的事件指针不是克隆事件指针，则返回[ARKUI_ERROR_CODE_NOT_CLONED_POINTER_EVENT](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_PointerEvent_SetClonedEventChangedFingerId()

```ets
int32_t OH_ArkUI_PointerEvent_SetClonedEventChangedFingerId(const ArkUI_UIInputEvent* event, int32_t fingerId)
```

**描述：**

设置当前带有指向性的克隆输入事件的触摸点ID。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。int32_t fingerId触发当前事件指针的触摸点ID。

**返回：**

类型说明int32_t

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果输入的事件指针不是克隆事件指针，则返回[ARKUI_ERROR_CODE_NOT_CLONED_POINTER_EVENT](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_PointerEvent_SetClonedEventFingerIdByIndex()

```ets
int32_t OH_ArkUI_PointerEvent_SetClonedEventFingerIdByIndex(const ArkUI_UIInputEvent* event, int32_t fingerId, int32_t pointerIndex)
```

**描述：**

设置带有指向性的克隆输入事件特定接触点的触摸点ID。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。int32_t fingerId指向性的输入事件特定接触点的触摸点ID。int32_t pointerIndex表示多点触控数据列表中的序号。

**返回：**

类型说明int32_t

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果输入的事件指针不是克隆事件指针，则返回[ARKUI_ERROR_CODE_NOT_CLONED_POINTER_EVENT](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_PointerEvent_PostClonedEvent()

```ets
int32_t OH_ArkUI_PointerEvent_PostClonedEvent(ArkUI_NodeHandle node, const ArkUI_UIInputEvent* event)
```

**描述：**

转发克隆事件到特定节点。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_NodeHandle](../../topics/components/ArkUI_Node_.md) node目标节点。[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明int32_t

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果输入的事件指针不是克隆事件指针，则返回[ARKUI_ERROR_CODE_NOT_CLONED_POINTER_EVENT](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果组件状态异常，则返回[ARKUI_ERROR_CODE_POST_CLONED_COMPONENT_STATUS_ABNORMAL](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果未命中可响应事件的组件，则返回[ARKUI_ERROR_CODE_POST_CLONED_NO_COMPONENT_HIT_TO_RESPOND_TO_THE_EVENT](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_UIInputEvent_GetLatestStatus()

```ets
ArkUI_ErrorCode OH_ArkUI_UIInputEvent_GetLatestStatus()
```

**描述：**

调用该方法获取最近一次UIInput相关方法的执行情况。通常情况下不需要使用该方法，仅在返回值结果不确定是否异常时使用。以下是一个使用示例（对于返回的float类型，0.0并不代表错误，因此可以进一步使用OH_ArkUI_UIInputEvent_GetLatestStatus方法来确认是否发生异常）。float x = OH_ArkUI_PointerEvent_GetX(event);if (ARKUI_ERROR_CODE_NO_ERROR != OH_ArkUI_UIInputEvent_GetlatestStatus()) {// errorreturn;}系统将在每次执行UIInput相关函数时主动清空上一次函数调用的状态，以确保每次通过该接口获取的均为最近一次的状态。

**起始版本：** 20

**返回：**

类型说明[ArkUI_ErrorCode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)返回最近一次调用UIInput方法产生的结果代码。

#### OH_ArkUI_UIInputEvent_GetCoastingAxisEvent()

```ets
ArkUI_CoastingAxisEvent* OH_ArkUI_UIInputEvent_GetCoastingAxisEvent(ArkUI_UIInputEvent* event)
```

**描述：**

从组件事件中获取惯性滚动轴事件，仅当用户在触摸板上使用双指滑动一定距离并快速抬手，且指针位置下存在注册了[NODE_ON_COASTING_AXIS_EVENT](native_node.h.md#ZH-CN_TOPIC_0000002529285071__arkui_nodeeventtype)事件的组件时，才能获取到有效事件。在从[ArkUI_NodeEvent](../../topics/components/ArkUI_NodeEvent.md)对象获取到[ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)对象后调用此方法。

惯性滚动轴事件仅在双指抛滑并离开触控板时触发，因此仅支持触控板。惯性滚动轴事件会在手指离开触控板后，根据抛滑速度产生轴值逐渐衰减的事件。由于刷新频率和性能的影响，当前事件轴值可能高于或低于上一个事件值。在惯性滚动轴事件期间，以下四种行为会中断事件，并立即收到ARKUI_COASTING_AXIS_EVENT_PHASE_END。

1.

手指触摸触控板。

1.

滚动鼠标滚轮。

1.

手指或鼠标点击注册了惯性滚动轴事件的节点。需要注意的是，点击未注册此事件的节点不会产生任何效果。例如，A节点注册了惯性滚动轴事件，当事件发生时，让B节点滚动，但点击B节点不会中断此事件。点击事件的中断行为受[HitTest模式](#ZH-CN_TOPIC_0000002497605082__oh_arkui_pointerevent_setintercepthittestmode)的影响。此外，如果用户点击区域存在已收集的可响应惯性滚动轴事件的节点，本次惯性滚动轴事件会被强制终止。

1.

应用休眠（例如最小化、锁屏）。

**起始版本：** 22

**参数:**

参数项描述[const ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)* eventArkUI_UIInputEvent事件指针。

**返回：**

类型说明[ArkUI_CoastingAxisEvent](../../topics/input/ArkUI_CoastingAxisEvent.md)返回指向惯性滚动轴事件的指针，如果未发生任何惯性滚动轴事件或发生任何参数错误，则返回空指针。

#### OH_ArkUI_CoastingAxisEvent_GetEventTime()

```ets
int64_t OH_ArkUI_CoastingAxisEvent_GetEventTime(ArkUI_CoastingAxisEvent* event)
```

**描述：**

获取惯性滚动轴事件发生的时间。

**起始版本：** 22

**参数:**

参数项描述[ArkUI_CoastingAxisEvent](../../topics/input/ArkUI_CoastingAxisEvent.md)* eventArkUI_CoastingAxisEvent事件指针。

**返回：**

类型说明int64_t返回UI输入事件发生的时间；如果发生任何参数错误则返回0。

#### OH_ArkUI_CoastingAxisEvent_GetPhase()

```ets
ArkUI_CoastingAxisEventPhase OH_ArkUI_CoastingAxisEvent_GetPhase(ArkUI_CoastingAxisEvent* event)
```

**描述：**

获取惯性滚动轴事件发生时的滚动阶段。

**起始版本：** 22

**参数:**

参数项描述[ArkUI_CoastingAxisEvent](../../topics/input/ArkUI_CoastingAxisEvent.md)* eventArkUI_CoastingAxisEvent事件指针。

**返回：**

类型说明[ArkUI_CoastingAxisEventPhase](#ZH-CN_TOPIC_0000002497605082__arkui_coastingaxiseventphase)

返回事件阶段，参见[ArkUI_CoastingAxisEventPhase](#ZH-CN_TOPIC_0000002497605082__arkui_coastingaxiseventphase)。

如果发生任何参数错误则返回ARKUI_COASTING_AXIS_EVENT_PHASE_NONE。

#### OH_ArkUI_CoastingAxisEvent_GetDeltaY

```ets
float OH_ArkUI_CoastingAxisEvent_GetDeltaY(ArkUI_CoastingAxisEvent* event)
```

**描述：**

获取惯性滚动轴事件垂直方向的增量值。单位为px，表示为单次滚动增量，非滚动总量。数值的正负代表方向，双指从上往下滑动时为负数，双指从下往上滑动时为正数。

**起始版本：** 22

**参数:**

参数项描述[ArkUI_CoastingAxisEvent](../../topics/input/ArkUI_CoastingAxisEvent.md)* eventArkUI_CoastingAxisEvent事件指针。

**返回：**

类型说明float返回Y轴增量值，以px为单位；如果发生任何参数错误则返回0.0f。

#### OH_ArkUI_CoastingAxisEvent_GetDeltaX

```ets
float OH_ArkUI_CoastingAxisEvent_GetDeltaX(ArkUI_CoastingAxisEvent* event)
```

**描述：**

获取惯性滚动轴事件水平方向的增量值。单位为px，表示为单次滚动增量，非滚动总量。数值的正负代表方向，双指从左往右滑动时为负数，双指从右往左滑动时为正数。

**起始版本：** 22

**参数:**

参数项描述[ArkUI_CoastingAxisEvent](../../topics/input/ArkUI_CoastingAxisEvent.md)* eventArkUI_CoastingAxisEvent事件指针。

**返回：**

类型说明float返回X轴增量值，以px为单位；如果发生任何参数错误则返回0.0f。

#### OH_ArkUI_CoastingAxisEvent_SetPropagation()

```ets
int32_t OH_ArkUI_CoastingAxisEvent_SetPropagation(ArkUI_CoastingAxisEvent* event, bool propagation)
```

**描述：**

设置惯性滚动轴事件是否启用冒泡，默认禁止冒泡。

**起始版本：** 22

**参数:**

参数项描述[ArkUI_CoastingAxisEvent](../../topics/input/ArkUI_CoastingAxisEvent.md)* eventArkUI_CoastingAxisEvent事件指针。bool propagation是否启用事件冒泡。true表示启用，false表示禁用。

**返回：**

类型说明int32_t

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_TouchTestInfo_GetTouchTestInfoList

```ets
ArkUI_ErrorCode OH_ArkUI_TouchTestInfo_GetTouchTestInfoList(ArkUI_TouchTestInfo* info,
    ArkUI_TouchTestInfoItemArray* array, int32_t* size);
```

**描述：**

获取触摸测试信息项数组。

**起始版本：** 22

**参数:**

参数项描述ArkUI_TouchTestInfo* info指向触摸测试信息的指针。ArkUI_TouchTestInfoItemArray* array指向触摸测试信息项数组的指针。int32_t* size触摸测试信息项数组的大小。

**返回：**

类型说明ArkUI_ErrorCode

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_TouchTestInfoItem_GetX

```ets
float OH_ArkUI_TouchTestInfoItem_GetX(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于子组件左上角的X坐标，单位为px。

**起始版本：** 22

**参数:**

参数项描述const ArkUI_TouchTestInfoItem* info指向触摸测试信息项的指针。

**返回：**

类型说明float相对于子组件左上角的X坐标，单位为px。若参数错误，返回0.0f。

#### OH_ArkUI_TouchTestInfoItem_GetY

```ets
float OH_ArkUI_TouchTestInfoItem_GetY(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于子组件左上角的Y坐标，单位为px。

**起始版本：** 22

**参数:**

参数项描述const ArkUI_TouchTestInfoItem* info指向触摸测试信息项的指针。

**返回：**

类型说明float相对于子组件左上角的Y坐标，单位为px。若参数错误，返回0.0f。

#### OH_ArkUI_TouchTestInfoItem_GetWindowX

```ets
float OH_ArkUI_TouchTestInfoItem_GetWindowX(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于当前应用窗口左上角的X坐标，单位为px。

**起始版本：** 22

**参数:**

参数项描述const ArkUI_TouchTestInfoItem* info指向触摸测试信息项的指针。

**返回：**

类型说明float相对于当前应用窗口左上角的X坐标，单位为px。若参数错误，返回0.0f。

#### OH_ArkUI_TouchTestInfoItem_GetWindowY

```ets
float OH_ArkUI_TouchTestInfoItem_GetWindowY(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于当前应用窗口左上角的Y坐标，单位为px。

**起始版本：** 22

**参数:**

参数项描述const ArkUI_TouchTestInfoItem* info指向触摸测试信息项的指针。

**返回：**

类型说明float相对于当前应用窗口左上角的Y坐标，单位为px。若参数错误，返回0.0f。

#### OH_ArkUI_TouchTestInfoItem_GetXRelativeToParent

```ets
float OH_ArkUI_TouchTestInfoItem_GetXRelativeToParent(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于父组件左上角的X坐标，单位为px。

**起始版本：** 22

**参数:**

参数项描述const ArkUI_TouchTestInfoItem* info指向触摸测试信息项的指针。

**返回：**

类型说明float相对于父组件左上角的X坐标，单位为px。若参数错误，返回0.0f。

#### OH_ArkUI_TouchTestInfoItem_GetYRelativeToParent

```ets
float OH_ArkUI_TouchTestInfoItem_GetYRelativeToParent(const ArkUI_TouchTestInfoItem* info);
```

**描述：**

从触摸测试信息项中获取相对于父组件左上角的Y坐标，单位为px。

**起始版本：** 22

**参数:**

参数项描述const ArkUI_TouchTestInfoItem* info指向触摸测试信息项的指针。

**返回：**

类型说明float相对于父组件左上角的Y坐标，单位为px。若参数错误，返回0.0f。

#### OH_ArkUI_TouchTestInfoItem_GetChildRect

```ets
ArkUI_ErrorCode OH_ArkUI_TouchTestInfoItem_GetChildRect(const ArkUI_TouchTestInfoItem* info, ArkUI_Rect* childRect);
```

**描述：**

从触摸测试信息项中获取子组件的帧矩形信息。

**起始版本：** 22

**参数:**

参数项描述const ArkUI_TouchTestInfoItem* info指向触摸测试信息项的指针。[ArkUI_Rect](../../topics/media/ArkUI_Rect.md)* childRect指向子组件帧矩形的指针，用于存储获取到的帧矩形信息。

**返回：**

类型说明ArkUI_ErrorCode

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_TouchTestInfoItem_GetChildId

```ets
ArkUI_ErrorCode OH_ArkUI_TouchTestInfoItem_GetChildId(const ArkUI_TouchTestInfoItem* info, char* buffer,
    int32_t bufferSize);
```

**描述：**

从触摸测试信息项中获取子组件的ID。

**起始版本：** 22

**参数:**

参数项描述const ArkUI_TouchTestInfoItem* info指向触摸测试信息项的指针。char* buffer存储结果的缓冲区。int32_t bufferSize缓冲区的大小。

**返回：**

类型说明ArkUI_ErrorCode

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果缓冲区空间不足，则返回[ARKUI_ERROR_CODE_BUFFER_SIZE_NOT_ENOUGH](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_TouchTestInfo_SetTouchResultStrategy

```ets
ArkUI_ErrorCode OH_ArkUI_TouchTestInfo_SetTouchResultStrategy(ArkUI_TouchTestInfo* info, ArkUI_TouchTestStrategy strategy);
```

**描述：**

设置触摸测试策略，即组件及其子组件在命中测试过程中的行为方式。

**起始版本：** 22

**参数:**

参数项描述ArkUI_TouchTestInfo* info指向触摸测试信息的指针。[ArkUI_TouchTestStrategy](#ZH-CN_TOPIC_0000002497605082__arkui_touchteststrategy) strategy触摸测试策略，定义组件及子组件在命中测试中的行为规则。

**返回：**

类型说明ArkUI_ErrorCode

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

#### OH_ArkUI_TouchTestInfo_SetTouchResultId

```ets
ArkUI_ErrorCode OH_ArkUI_TouchTestInfo_SetTouchResultId(ArkUI_TouchTestInfo* info, const char* id);
```

**描述：**

设置命中测试过程中需要作用的子组件ID。

**起始版本：** 22

**参数:**

参数项描述ArkUI_TouchTestInfo* info指向触摸测试信息的指针。const char* id子组件的ID，指定命中测试中需要作用的目标子组件。

**返回：**

类型说明ArkUI_ErrorCode

返回结果代码。

如果操作成功，则返回[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。

如果入参错误，则返回[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)。
