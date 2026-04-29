# native_interface_xcomponent.h

**概述**

声明用于访问Native XComponent的API。

引用文件： <ace/xcomponent/native_interface_xcomponent.h>

库： libace_ndk.z.so

系统能力： SystemCapability.ArkUI.ArkUI.Full

起始版本： 8

相关模块： [OH_NativeXComponent Native XComponent](OH_NativeXComponent Native XComponent.md)

相关示例： [NativeXComponentSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeXComponentSample)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_NativeXComponent_HistoricalPoint | OH_NativeXComponent_HistoricalPoint | 历史接触点。 |
| OH_NativeXComponent_TouchPoint | OH_NativeXComponent_TouchPoint | 触摸事件中触摸点的信息。 |
| OH_NativeXComponent_TouchEvent | OH_NativeXComponent_TouchEvent | 触摸事件。 |
| OH_NativeXComponent_MouseEvent | OH_NativeXComponent_MouseEvent | 鼠标事件。 |
| OH_NativeXComponent_Callback | OH_NativeXComponent_Callback | 注册Surface生命周期和触摸事件回调。 |
| OH_NativeXComponent_MouseEvent_Callback | OH_NativeXComponent_MouseEvent_Callback | 注册鼠标事件的回调。 |
| OH_NativeXComponent_ExpectedRateRange | OH_NativeXComponent_ExpectedRateRange | 定义期望帧率范围。 |
| OH_NativeXComponent | OH_NativeXComponent | 提供封装的OH_NativeXComponent实例。 |
| OH_NativeXComponent_KeyEvent | OH_NativeXComponent_KeyEvent | 提供封装按键事件信息的OH_NativeXComponent_KeyEvent实例。 |
| OH_NativeXComponent_ExtraMouseEventInfo | OH_NativeXComponent_ExtraMouseEventInfo | 提供封装的扩展的鼠标事件信息实例。 |
| OH_ArkUI_SurfaceHolder | OH_ArkUI_SurfaceHolder | 提供封装的OH_ArkUI_SurfaceHolder实例。 |
| OH_ArkUI_SurfaceCallback | OH_ArkUI_SurfaceCallback | 定义Surface生命周期回调函数。 |
| NativeWindow | OHNativeWindow | 提供封装的NativeWindow实例。 |
| ArkUI_XComponentSurfaceConfig | ArkUI_XComponentSurfaceConfig | 定义XComponent组件持有的Surface选项，用于设置XComponent组件持有的Surface在渲染时是否被视为不透明。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| anonymous | - | 枚举API访问状态。 |
| ArkUI_XComponent_ImageAnalyzerState | ArkUI_XComponent_ImageAnalyzerState | XComponent图像AI分析状态码. |
| OH_NativeXComponent_TouchEventType | OH_NativeXComponent_TouchEventType | 触摸事件类型。 |
| OH_NativeXComponent_TouchPointToolType | OH_NativeXComponent_TouchPointToolType | 触摸点工具类型。 |
| OH_NativeXComponent_EventSourceType | OH_NativeXComponent_EventSourceType | 触摸事件源类型。 |
| OH_NativeXComponent_MouseEventAction | OH_NativeXComponent_MouseEventAction | 鼠标事件动作。 |
| OH_NativeXComponent_MouseEventButton | OH_NativeXComponent_MouseEventButton | 鼠标事件按键。 |
| OH_NativeXComponent_TouchEvent_SourceTool | OH_NativeXComponent_TouchEvent_SourceTool | 表示触摸事件的源工具类型 |

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t OH_NativeXComponent_GetXComponentId(OH_NativeXComponent* component, char* id, uint64_t* size) | 获取ArkUI XComponent的id。 |
| int32_t OH_NativeXComponent_GetXComponentSize(OH_NativeXComponent* component, const void* window, uint64_t* width, uint64_t* height) | 获取ArkUI XComponent持有的Surface的大小。 |
| int32_t OH_NativeXComponent_GetXComponentOffset(OH_NativeXComponent* component, const void* window, double* x, double* y) | 获取ArkUI XComponent持有的Surface相对其父组件左顶点的偏移量。 |
| int32_t OH_NativeXComponent_GetTouchEvent(OH_NativeXComponent* component, const void* window, OH_NativeXComponent_TouchEvent* touchEvent) | 获取ArkUI XComponent调度的触摸事件。 |
| int32_t OH_NativeXComponent_GetTouchPointToolType(OH_NativeXComponent* component, uint32_t pointIndex, OH_NativeXComponent_TouchPointToolType* toolType) | 获取ArkUI XComponent触摸点工具类型。 |
| int32_t OH_NativeXComponent_GetTouchPointTiltX(OH_NativeXComponent* component, uint32_t pointIndex, float* tiltX) | 获取ArkUI XComponent触摸点倾斜与X轴角度。 |
| int32_t OH_NativeXComponent_GetTouchPointTiltY(OH_NativeXComponent* component, uint32_t pointIndex, float* tiltY) | 获取ArkUI XComponent触摸点倾斜与Y轴角度。 |
| int32_t OH_NativeXComponent_GetTouchPointWindowX(OH_NativeXComponent* component, uint32_t pointIndex, float* windowX) | 获取ArkUI XComponent触摸点相对于应用窗口左上角的X坐标。 |
| int32_t OH_NativeXComponent_GetTouchPointWindowY(OH_NativeXComponent* component, uint32_t pointIndex, float* windowY) | 获取ArkUI XComponent触摸点相对于应用窗口左上角的Y坐标。 |
| int32_t OH_NativeXComponent_GetTouchPointDisplayX(OH_NativeXComponent* component, uint32_t pointIndex, float* displayX) | 获取ArkUI XComponent触摸点相对于应用所在屏幕左上角的X坐标。 |
| int32_t OH_NativeXComponent_GetTouchPointDisplayY(OH_NativeXComponent* component, uint32_t pointIndex, float* displayY) | 获取ArkUI XComponent触摸点相对于应用所在屏幕左上角的Y坐标。 |
| int32_t OH_NativeXComponent_GetHistoricalPoints(OH_NativeXComponent* component, const void* window, int32_t* size, OH_NativeXComponent_HistoricalPoint** historicalPoints) | 获取当前XComponent触摸事件的历史点信息。由于部分输入设备上报触点的频率非常高（最高可达每1 ms上报一次），而对输入事件的响应通常是为了使UI界面发生变化以响应用户操作，如果将触摸事件按照上报触点的频率如此高频率上报给应用，大多会造成冗余，因此触摸事件在一帧内只会上报一次给应用。在当前帧内上报的触点均作为历史点保存，如果应用需要直接处理这些数据，可调用该接口获取历史点信息。 |
| int32_t OH_NativeXComponent_GetMouseEvent(OH_NativeXComponent* component, const void* window, OH_NativeXComponent_MouseEvent* mouseEvent) | 获取ArkUI XComponent调度的鼠标事件。 |
| int32_t OH_NativeXComponent_RegisterCallback(OH_NativeXComponent* component, OH_NativeXComponent_Callback* callback) | 为此OH_NativeXComponent实例注册回调。 |
| int32_t OH_NativeXComponent_RegisterMouseEventCallback(OH_NativeXComponent* component, OH_NativeXComponent_MouseEvent_Callback* callback) | 为此OH_NativeXComponent实例注册鼠标事件回调。 |
| int32_t OH_NativeXComponent_GetExtraMouseEventInfo(OH_NativeXComponent* component, OH_NativeXComponent_ExtraMouseEventInfo** extraMouseEventInfo) | 从此OH_NativeXComponent实例中获取扩展的鼠标事件信息。 |
| int32_t OH_NativeXComponent_GetMouseEventModifierKeyStates (OH_NativeXComponent_ExtraMouseEventInfo* extraMouseEventInfo, uint64_t* keys) | 从OH_NativeXComponent_ExtraMouseEventInfo实例中获取功能键按压状态信息。 |
| int32_t OH_NativeXComponent_RegisterFocusEventCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window)) | 为此OH_NativeXComponent实例注册获焦事件回调。 |
| int32_t OH_NativeXComponent_RegisterKeyEventCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window)) | 为此OH_NativeXComponent实例注册按键事件回调。 |
| int32_t OH_NativeXComponent_RegisterBlurEventCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window)) | 为此OH_NativeXComponent实例注册失焦事件回调。 |
| int32_t OH_NativeXComponent_GetKeyEvent(OH_NativeXComponent* component, OH_NativeXComponent_KeyEvent** keyEvent) | 获取ArkUI XComponent调度的按键事件。 |
| int32_t OH_NativeXComponent_GetKeyEventAction(OH_NativeXComponent_KeyEvent* keyEvent, OH_NativeXComponent_KeyAction* action) | 获取传入按键事件的动作。 |
| int32_t OH_NativeXComponent_GetKeyEventCode(OH_NativeXComponent_KeyEvent* keyEvent, OH_NativeXComponent_KeyCode* code) | 获取传入按键事件的按键码。 |
| int32_t OH_NativeXComponent_GetKeyEventSourceType(OH_NativeXComponent_KeyEvent* keyEvent, OH_NativeXComponent_EventSourceType* sourceType) | 获取传入按键事件的事件源类型。 |
| int32_t OH_NativeXComponent_GetKeyEventDeviceId(OH_NativeXComponent_KeyEvent* keyEvent, int64_t* deviceId) | 获取传入按键事件的设备id。 |
| int32_t OH_NativeXComponent_GetKeyEventTimestamp(OH_NativeXComponent_KeyEvent* keyEvent, int64_t* timestamp) | 获取传入按键事件的时间戳。 |
| int32_t OH_NativeXComponent_GetKeyEventModifierKeyStates(OH_NativeXComponent_KeyEvent* keyEvent, uint64_t* keys) | 从按键事件中获取功能键按压状态信息。 |
| int32_t OH_NativeXComponent_GetKeyEventNumLockState(OH_NativeXComponent_KeyEvent* keyEvent, bool* isNumLockOn) | 从按键事件中获取NumLock（小键盘锁定）键的状态信息。 |
| int32_t OH_NativeXComponent_GetKeyEventCapsLockState(OH_NativeXComponent_KeyEvent* keyEvent, bool* isCapsLockOn) | 从按键事件中获取CapsLock（大写锁定）键的状态信息。 |
| int32_t OH_NativeXComponent_GetKeyEventScrollLockState(OH_NativeXComponent_KeyEvent* keyEvent, bool* isScrollLockOn) | 从按键事件中获取ScrollLock（滚动锁定）键的状态信息。 |
| int32_t OH_NativeXComponent_SetExpectedFrameRateRange(OH_NativeXComponent* component, OH_NativeXComponent_ExpectedRateRange* range) | 设置期望帧率范围。 |
| int32_t OH_NativeXComponent_RegisterOnFrameCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, uint64_t timestamp, uint64_t targetTimestamp)) | 为此OH_NativeXComponent实例注册显示更新回调，并使能每帧回调此函数。 |
| int32_t OH_NativeXComponent_UnregisterOnFrameCallback(OH_NativeXComponent* component) | 为此OH_NativeXComponent实例取消注册回调函数，并关闭每帧回调此函数。 |
| int32_t OH_NativeXComponent_AttachNativeRootNode(OH_NativeXComponent* component, ArkUI_NodeHandle root) | 将通过ArkUI的Native接口创建出来的UI组件挂载到当前XComponent上。 |
| int32_t OH_NativeXComponent_DetachNativeRootNode(OH_NativeXComponent* component, ArkUI_NodeHandle root) | 将ArkUI的Native组件从当前XComponent上卸载。 |
| int32_t OH_NativeXComponent_RegisterUIInputEventCallback(OH_NativeXComponent *component, void (*callback)(OH_NativeXComponent *component, ArkUI_UIInputEvent *event,ArkUI_UIInputEvent_Type type),ArkUI_UIInputEvent_Type type) | 为此OH_NativeXComponent实例注册UI输入事件回调，并使能收到UI输入事件时回调此函数。当前仅支持轴事件。 |
| int32_t OH_NativeXComponent_RegisterOnTouchInterceptCallback(OH_NativeXComponent* component, HitTestMode (*callback)(OH_NativeXComponent* component, ArkUI_UIInputEvent* event)) | 为此OH_NativeXComponent实例注册自定义事件拦截回调，并使能在做触摸测试时回调此函数。通过该回调获取到的事件对象不支持UIInput相关信息操作接口，建议切换为通过注册native node上的NODE_ON_TOUCH_INTERCEPT通用事件来支持。 |
| int32_t OH_NativeXComponent_SetNeedSoftKeyboard(OH_NativeXComponent* component, bool needSoftKeyboard) | 为此OH_NativeXComponent实例设置是否需要软键盘。 |
| int32_t OH_NativeXComponent_RegisterSurfaceShowCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window)) | 为此OH_NativeXComponent实例注册Surface显示回调，该回调在应用窗口已经从后台回到前台时触发。 |
| int32_t OH_NativeXComponent_RegisterSurfaceHideCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window)) | 为此OH_NativeXComponent实例注册Surface隐藏回调，该回调在应用窗口已经从前台进入后台时触发。 |
| int32_t OH_NativeXComponent_GetTouchEventSourceType(OH_NativeXComponent* component, int32_t pointId, OH_NativeXComponent_EventSourceType* sourceType) | 获取ArkUI XComponent触摸事件的输入设备类型。 |
| OH_NativeXComponent* OH_NativeXComponent_GetNativeXComponent(ArkUI_NodeHandle node) | 基于Native接口创建的组件实例获取OH_NativeXComponent类型的指针。 |
| int32_t OH_NativeXComponent_GetNativeAccessibilityProvider(OH_NativeXComponent* component, ArkUI_AccessibilityProvider** handle) | 获取ArkUI XComponent无障碍接入句柄指针。 |
| int32_t OH_NativeXComponent_RegisterKeyEventCallbackWithResult(OH_NativeXComponent* component, bool (*callback)(OH_NativeXComponent* component, void* window)) | 为此OH_NativeXComponent实例注册带有返回值的按键事件回调。通过此接口注册的按键事件回调都必须返回一个结果，即true或false。当返回值为true时，该事件将不会继续分发；当返回值为false时，该事件将按照事件处理流程继续分发。 |
| int32_t OH_ArkUI_XComponent_StartImageAnalyzer(ArkUI_NodeHandle node, void* userData, void (*callback)(ArkUI_NodeHandle node, ArkUI_XComponent_ImageAnalyzerState statusCode, void* userData)) | 为此XComponent组件实例开始图像AI分析，使用前需先使能图像AI分析能力。 |
| int32_t OH_ArkUI_XComponent_StopImageAnalyzer(ArkUI_NodeHandle node) | 为此XComponent组件实例停止图像AI分析。 |
| OH_ArkUI_SurfaceHolder* OH_ArkUI_SurfaceHolder_Create(ArkUI_NodeHandle node) | 创建XComponent组件的OH_ArkUI_SurfaceHolder对象。 |
| void OH_ArkUI_SurfaceHolder_Dispose(OH_ArkUI_SurfaceHolder* surfaceHolder) | 销毁OH_ArkUI_SurfaceHolder对象。 |
| int32_t OH_ArkUI_SurfaceHolder_SetUserData(OH_ArkUI_SurfaceHolder* surfaceHolder, void* userData) | 向OH_ArkUI_SurfaceHolder实例存储自定义数据。 |
| void* OH_ArkUI_SurfaceHolder_GetUserData(OH_ArkUI_SurfaceHolder* surfaceHolder) | 获取OH_ArkUI_SurfaceHolder实例存储的自定义数据。 |
| OH_ArkUI_SurfaceCallback* OH_ArkUI_SurfaceCallback_Create() | 创建OH_ArkUI_SurfaceCallback对象。 |
| void OH_ArkUI_SurfaceCallback_Dispose(OH_ArkUI_SurfaceCallback* callback) | 销毁OH_ArkUI_SurfaceCallback对象。 |
| void OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceCreated)(OH_ArkUI_SurfaceHolder* surfaceHolder)) | 设置Surface生命周期回调中的创建回调事件。 |
| void OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceChanged)(OH_ArkUI_SurfaceHolder* surfaceHolder, uint64_t width, uint64_t height)) | 设置Surface生命周期回调中的大小改变回调事件。 |
| void OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceDestroyed)(OH_ArkUI_SurfaceHolder* surfaceHolder)) | 设置Surface生命周期回调中的销毁回调事件。 |
| int32_t OH_ArkUI_SurfaceHolder_AddSurfaceCallback(OH_ArkUI_SurfaceHolder* surfaceHolder,OH_ArkUI_SurfaceCallback* callback) | 添加Surface生命周期回调到OH_ArkUI_SurfaceHolder实例。 |
| int32_t OH_ArkUI_SurfaceHolder_RemoveSurfaceCallback(OH_ArkUI_SurfaceHolder* surfaceHolder,OH_ArkUI_SurfaceCallback* callback) | 删除OH_ArkUI_SurfaceHolder实例的先前添加的Surface生命周期回调。 |
| OHNativeWindow* OH_ArkUI_XComponent_GetNativeWindow(OH_ArkUI_SurfaceHolder* surfaceHolder) | 获取OH_ArkUI_SurfaceHolder实例关联的NativeWindow。 |
| int32_t OH_ArkUI_XComponent_SetAutoInitialize(ArkUI_NodeHandle node, bool autoInitialize) | 设置XComponent组件是否需要自动初始化Surface的标志位。 |
| int32_t OH_ArkUI_XComponent_Initialize(ArkUI_NodeHandle node) | 初始化XComponent组件持有的Surface。 |
| int32_t OH_ArkUI_XComponent_Finalize(ArkUI_NodeHandle node) | 销毁XComponent组件持有的Surface。 |
| int32_t OH_ArkUI_XComponent_IsInitialized(ArkUI_NodeHandle node, bool* isInitialized) | 获取XComponent组件是否已经初始化的标志位。 |
| int32_t OH_ArkUI_XComponent_SetExpectedFrameRateRange(ArkUI_NodeHandle node, OH_NativeXComponent_ExpectedRateRange range) | 为此XComponent组件实例设置期望帧率。 |
| int32_t OH_ArkUI_XComponent_RegisterOnFrameCallback(ArkUI_NodeHandle node,void (*callback)(ArkUI_NodeHandle node, uint64_t timestamp, uint64_t targetTimestamp)) | 为此XComponent组件实例注册帧回调函数。 |
| int32_t OH_ArkUI_XComponent_UnregisterOnFrameCallback(ArkUI_NodeHandle node) | 为此XComponent组件实例取消注册帧回调函数。 |
| int32_t OH_ArkUI_XComponent_SetNeedSoftKeyboard(ArkUI_NodeHandle node, bool needSoftKeyboard) | 为此XComponent组件实例设置是否需要软键盘。 |
| ArkUI_AccessibilityProvider* OH_ArkUI_AccessibilityProvider_Create(ArkUI_NodeHandle node) | 基于此XComponent实例创建ArkUI_AccessibilityProvider实例。 |
| void OH_ArkUI_AccessibilityProvider_Dispose(ArkUI_AccessibilityProvider* provider) | 销毁由Native接口OH_ArkUI_AccessibilityProvider_Create创建的ArkUI_AccessibilityProvider实例。 |
| void OH_ArkUI_SurfaceCallback_SetSurfaceShowEvent(OH_ArkUI_SurfaceCallback* callback, void (*onSurfaceShow)(OH_ArkUI_SurfaceHolder* surfaceHolder)) | 为此OH_ArkUI_SurfaceCallback实例设置Surface显示回调，该回调在应用窗口已经从后台回到前台时触发。 |
| void OH_ArkUI_SurfaceCallback_SetSurfaceHideEvent(OH_ArkUI_SurfaceCallback* callback, void (*onSurfaceHide)(OH_ArkUI_SurfaceHolder* surfaceHolder)) | 为此OH_ArkUI_SurfaceCallback实例设置Surface隐藏回调，该回调在应用窗口已经从前台进入后台时触发。 |
| ArkUI_XComponentSurfaceConfig* OH_ArkUI_XComponentSurfaceConfig_Create() | 创建XComponent组件的ArkUI_XComponentSurfaceConfig对象。 |
| void OH_ArkUI_XComponentSurfaceConfig_Dispose(ArkUI_XComponentSurfaceConfig* config) | 销毁ArkUI_XComponentSurfaceConfig对象。 |
| void OH_ArkUI_XComponentSurfaceConfig_SetIsOpaque(ArkUI_XComponentSurfaceConfig* config, bool isOpaque) | 设置XComponent组件持有的Surface在渲染时是否被视为不透明，无论该Surface是否存在半透明像素。 |
| int32_t OH_ArkUI_SurfaceHolder_SetSurfaceConfig(OH_ArkUI_SurfaceHolder* surfaceHolder, ArkUI_XComponentSurfaceConfig *config) | 为OH_ArkUI_SurfaceHolder实例设置Surface选项。 |

**变量**

| 名称 | 描述 |
| --- | --- |
| const uint32_t OH_XCOMPONENT_ID_LEN_MAX = 128 | ArkUI XComponent的id最大长度。 起始版本： 8 |
| const uint32_t OH_MAX_TOUCH_POINTS_NUMBER = 10 | 触摸事件中的可识别的触摸点个数最大值。 起始版本： 8 |
| OH_NATIVE_XCOMPONENT_MAX_TOUCH_POINTS_NUMBER 10 | 最大支持10个触摸点。 起始版本： 8 |

**枚举类型说明**

**anonymous**

```ets
enum anonymous
```

描述：

枚举API访问状态。

起始版本： 8

| 枚举项 | 描述 |
| --- | --- |
| OH_NATIVEXCOMPONENT_RESULT_SUCCESS = 0 | 成功结果。 |
| OH_NATIVEXCOMPONENT_RESULT_FAILED = -1 | 失败结果。 |
| OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER = -2 | 无效参数。 |

**ArkUI_XComponent_ImageAnalyzerState**

```ets
enum ArkUI_XComponent_ImageAnalyzerState
```

描述：

XComponent图像AI分析状态码.

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_XCOMPONENT_AI_ANALYSIS_FINISHED = 0 | 图像AI分析完成。 |
| ARKUI_XCOMPONENT_AI_ANALYSIS_DISABLED = 110000 | 图像AI分析已禁用。 |
| ARKUI_XCOMPONENT_AI_ANALYSIS_UNSUPPORTED = 110001 | 设备不支持图像AI分析。 |
| ARKUI_XCOMPONENT_AI_ANALYSIS_ONGOING = 110002 | 图像AI分析进行中。 |
| ARKUI_XCOMPONENT_AI_ANALYSIS_STOPPED = 110003 | 图像AI分析停止。 |

**OH_NativeXComponent_TouchEventType**

```ets
enum OH_NativeXComponent_TouchEventType
```

描述：

触摸事件类型。

起始版本： 8

| 枚举项 | 描述 |
| --- | --- |
| OH_NATIVEXCOMPONENT_DOWN = 0 | 手指按下时触发触摸事件。 |
| OH_NATIVEXCOMPONENT_UP = 1 | 手指抬起时触发触摸事件。 |
| OH_NATIVEXCOMPONENT_MOVE = 2 | 手指按下状态下在屏幕上移动时触发触摸事件。 |
| OH_NATIVEXCOMPONENT_CANCEL = 3 | 触摸事件取消时触发事件。 |
| OH_NATIVEXCOMPONENT_UNKNOWN = 4 | 无效的触摸类型。 |

**OH_NativeXComponent_TouchPointToolType**

```ets
enum OH_NativeXComponent_TouchPointToolType
```

描述：

触摸点工具类型。

起始版本： 9

| 枚举项 | 描述 |
| --- | --- |
| OH_NATIVEXCOMPONENT_TOOL_TYPE_UNKNOWN = 0 | 未识别工具类型。 |
| OH_NATIVEXCOMPONENT_TOOL_TYPE_FINGER = 1 | 表示用手指。 |
| OH_NATIVEXCOMPONENT_TOOL_TYPE_PEN = 2 | 表示用触笔。 |
| OH_NATIVEXCOMPONENT_TOOL_TYPE_RUBBER = 3 | 表示用橡皮擦。 |
| OH_NATIVEXCOMPONENT_TOOL_TYPE_BRUSH = 4 | 表示用画笔。 |
| OH_NATIVEXCOMPONENT_TOOL_TYPE_PENCIL = 5 | 表示用铅笔。 |
| OH_NATIVEXCOMPONENT_TOOL_TYPE_AIRBRUSH = 6 | 表示用气笔。 |
| OH_NATIVEXCOMPONENT_TOOL_TYPE_MOUSE = 7 | 表示用鼠标。 |
| OH_NATIVEXCOMPONENT_TOOL_TYPE_LENS = 8 | 表示用晶状体。 |

**OH_NativeXComponent_EventSourceType**

```ets
enum OH_NativeXComponent_EventSourceType
```

描述：

触摸事件源类型。

起始版本： 9

| 枚举项 | 描述 |
| --- | --- |
| OH_NATIVEXCOMPONENT_SOURCE_TYPE_UNKNOWN = 0 | 未知的输入源类型。 |
| OH_NATIVEXCOMPONENT_SOURCE_TYPE_MOUSE = 1 | 表示输入源生成鼠标多点触摸事件。 |
| OH_NATIVEXCOMPONENT_SOURCE_TYPE_TOUCHSCREEN = 2 | 表示输入源生成一个触摸屏多点触摸事件。 |
| OH_NATIVEXCOMPONENT_SOURCE_TYPE_TOUCHPAD = 3 | 表示输入源生成一个触摸板多点触摸事件。 |
| OH_NATIVEXCOMPONENT_SOURCE_TYPE_JOYSTICK = 4 | 表示输入源生成一个操纵杆多点触摸事件。 |
| OH_NATIVEXCOMPONENT_SOURCE_TYPE_KEYBOARD = 5 | 表示输入源生成一个键盘事件。 起始版本： 10 |

**OH_NativeXComponent_MouseEventAction**

```ets
enum OH_NativeXComponent_MouseEventAction
```

描述：

鼠标事件动作。

起始版本： 9

| 枚举项 | 描述 |
| --- | --- |
| OH_NATIVEXCOMPONENT_MOUSE_NONE = 0 | 无效鼠标事件。 |
| OH_NATIVEXCOMPONENT_MOUSE_PRESS = 1 | 鼠标按键按下时触发鼠标事件。 |
| OH_NATIVEXCOMPONENT_MOUSE_RELEASE = 2 | 鼠标按键松开时触发鼠标事件。 |
| OH_NATIVEXCOMPONENT_MOUSE_MOVE = 3 | 鼠标在屏幕上移动时触发鼠标事件。 |
| OH_NATIVEXCOMPONENT_MOUSE_CANCEL = 4 | 鼠标按键被取消时触发鼠标事件。 起始版本： 18   说明： OH_NATIVEXCOMPONENT_MOUSE_CANCEL表示鼠标事件被取消，通常在以下场景被触发： 1.组件失去焦点：当前持有焦点的XComponent因系统事件（如弹窗打断、应用切换）失去焦点时，会触发该动作。  2.事件中断：鼠标操作过程中发生更高优先级事件（如系统级手势或强制回收事件流），导致当前鼠标操作被强制终止。 3.异常状态退出：如组件销毁、渲染环境异常等场景下，未完成的鼠标事件会被标记为取消。 |

**OH_NativeXComponent_MouseEventButton**

```ets
enum OH_NativeXComponent_MouseEventButton
```

描述：

鼠标事件按键。

起始版本： 9

| 枚举项 | 描述 |
| --- | --- |
| OH_NATIVEXCOMPONENT_NONE_BUTTON = 0 | 鼠标无按键操作时触发鼠标事件。 |
| OH_NATIVEXCOMPONENT_LEFT_BUTTON = 0x01 | 按下鼠标左键时触发鼠标事件。 |
| OH_NATIVEXCOMPONENT_RIGHT_BUTTON = 0x02 | 按下鼠标右键时触发鼠标事件。 |
| OH_NATIVEXCOMPONENT_MIDDLE_BUTTON = 0x04 | 按下鼠标中键时触发鼠标事件。 |
| OH_NATIVEXCOMPONENT_BACK_BUTTON = 0x08 | 按下鼠标左侧后退键时触发鼠标事件。 |
| OH_NATIVEXCOMPONENT_FORWARD_BUTTON = 0x10 | 按下鼠标左侧前进键时触发鼠标事件。 |

**OH_NativeXComponent_TouchEvent_SourceTool**

```ets
enum OH_NativeXComponent_TouchEvent_SourceTool
```

描述：

表示触摸事件的源工具类型

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OH_NATIVEXCOMPONENT_SOURCETOOL_UNKNOWN = 0 | 未知的触摸事件的源工具。 |
| OH_NATIVEXCOMPONENT_SOURCETOOL_FINGER = 1 | 表示触摸事件的源工具是手指。 |
| OH_NATIVEXCOMPONENT_SOURCETOOL_PEN = 2 | 表示触摸事件的源工具是钢笔。 |
| OH_NATIVEXCOMPONENT_SOURCETOOL_RUBBER = 3 | 表示触摸事件的源工具是橡皮。 |
| OH_NATIVEXCOMPONENT_SOURCETOOL_BRUSH = 4 | 表示触摸事件的源工具是笔刷。 |
| OH_NATIVEXCOMPONENT_SOURCETOOL_PENCIL = 5 | 表示触摸事件的源工具是铅笔。 |
| OH_NATIVEXCOMPONENT_SOURCETOOL_AIRBRUSH = 6 | 表示触摸事件的源工具是喷枪。 |
| OH_NATIVEXCOMPONENT_SOURCETOOL_MOUSE = 7 | 表示触摸事件的源工具是鼠标。 |
| OH_NATIVEXCOMPONENT_SOURCETOOL_LENS = 8 | 表示触摸事件的源工具是透镜。 |
| OH_NATIVEXCOMPONENT_SOURCETOOL_TOUCHPAD = 9 | 表示触摸事件的源工具是触摸板。 |

**函数说明**

**OH_NativeXComponent_GetXComponentId()**

```ets
int32_t OH_NativeXComponent_GetXComponentId(OH_NativeXComponent* component, char* id, uint64_t* size)
```

描述：

获取ArkUI XComponent的id。

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| char* id | 表示用于保存此OH_NativeXComponent实例的ID的字符缓冲区。请注意，空终止符将附加到字符缓冲区，因此字符缓冲区的大小应至少比真实id长度大一个单位。建议字符缓冲区的大小为[OH_XCOMPONENT_ID_LEN_MAX + 1]。 |
| uint64_t* size | 表示指向id长度的指针，用于接收id的长度信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetXComponentSize()**

```ets
int32_t OH_NativeXComponent_GetXComponentSize(OH_NativeXComponent* component, const void* window, uint64_t* width, uint64_t* height)
```

描述：

获取ArkUI XComponent持有的Surface的大小。

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| const void* window | 表示NativeWindow句柄。 |
| uint64_t* width | 表示指向当前Surface宽度的指针。 |
| uint64_t* height | 表示指向当前Surface高度的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetXComponentOffset()**

```ets
int32_t OH_NativeXComponent_GetXComponentOffset(OH_NativeXComponent* component, const void* window, double* x, double* y)
```

描述：

获取ArkUI XComponent持有的Surface相对其父组件左顶点的偏移量。

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| const void* window | 表示NativeWindow句柄。 |
| double* x | 表示指向当前Surface相对于XComponent父组件左顶点x坐标的指针。 |
| double* y | 表示指向当前Surface相对于XComponent父组件左顶点y坐标的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetTouchEvent()**

```ets
int32_t OH_NativeXComponent_GetTouchEvent(OH_NativeXComponent* component, const void* window, OH_NativeXComponent_TouchEvent* touchEvent)
```

描述：

获取ArkUI XComponent调度的触摸事件。

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| const void* window | 表示NativeWindow句柄。 |
| OH_NativeXComponent_TouchEvent* touchEvent | 表示指向当前触摸事件的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetTouchPointToolType()**

```ets
int32_t OH_NativeXComponent_GetTouchPointToolType(OH_NativeXComponent* component, uint32_t pointIndex,OH_NativeXComponent_TouchPointToolType* toolType)
```

描述：

获取ArkUI XComponent触摸点工具类型。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| uint32_t pointIndex | 表示触摸点的指针索引。 |
| OH_NativeXComponent_TouchPointToolType* toolType | 表示指向工具类型的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetTouchPointTiltX()**

```ets
int32_t OH_NativeXComponent_GetTouchPointTiltX(OH_NativeXComponent* component, uint32_t pointIndex, float* tiltX)
```

描述：

获取ArkUI XComponent触摸点倾斜与X轴角度。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| uint32_t pointIndex | 表示触摸点的指针索引。 |
| float* tiltX | 表示指向X倾斜度的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetTouchPointTiltY()**

```ets
int32_t OH_NativeXComponent_GetTouchPointTiltY(OH_NativeXComponent* component, uint32_t pointIndex, float* tiltY)
```

描述：

获取ArkUI XComponent触摸点倾斜与Y轴角度。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| uint32_t pointIndex | 表示触摸点的指针索引。 |
| float* tiltY | 表示指向Y倾斜度的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetTouchPointWindowX()**

```ets
int32_t OH_NativeXComponent_GetTouchPointWindowX(OH_NativeXComponent* component, uint32_t pointIndex, float* windowX)
```

描述：

获取ArkUI XComponent触摸点相对于应用窗口左上角的X坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| uint32_t pointIndex | 表示触摸点的指针索引。 |
| float* windowX | 表示指向触摸点相对于应用窗口左上角的X坐标的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS 获取windowX成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER component是空指针、windowX是空指针或者native XComponent是空指针。 |

**OH_NativeXComponent_GetTouchPointWindowY()**

```ets
int32_t OH_NativeXComponent_GetTouchPointWindowY(OH_NativeXComponent* component, uint32_t pointIndex, float* windowY)
```

描述：

获取ArkUI XComponent触摸点相对于应用窗口左上角的Y坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| uint32_t pointIndex | 表示触摸点的指针索引。 |
| float* windowY | 表示指向触摸点相对于应用窗口左上角的Y坐标的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。  OH_NATIVEXCOMPONENT_RESULT_SUCCESS 获取windowY成功。  OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER component是空指针、windowY是空指针或者native XComponent是空指针。 |

**OH_NativeXComponent_GetTouchPointDisplayX()**

```ets
int32_t OH_NativeXComponent_GetTouchPointDisplayX(OH_NativeXComponent* component, uint32_t pointIndex, float* displayX)
```

描述：

获取ArkUI XComponent触摸点相对于应用所在屏幕左上角的X坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| uint32_t pointIndex | 表示触摸点的指针索引。 |
| float* displayX | 表示指向触摸点相对于应用所在屏幕左上角的X坐标的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS 获取displayX成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER component是空指针、displayX是空指针或者native XComponent是空指针。 |

**OH_NativeXComponent_GetTouchPointDisplayY()**

```ets
int32_t OH_NativeXComponent_GetTouchPointDisplayY(OH_NativeXComponent* component, uint32_t pointIndex, float* displayY)
```

描述：

获取ArkUI XComponent触摸点相对于应用所在屏幕左上角的Y坐标。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| uint32_t pointIndex | 表示触摸点的指针索引。 |
| float* displayY | 表示指向触摸点相对于应用所在屏幕左上角的Y坐标的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS 获取displayY成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER component是空指针、displayY是空指针或者native XComponent是空指针。 |

**OH_NativeXComponent_GetHistoricalPoints()**

```ets
int32_t OH_NativeXComponent_GetHistoricalPoints(OH_NativeXComponent* component, const void* window,int32_t* size, OH_NativeXComponent_HistoricalPoint** historicalPoints)
```

描述：

获取当前XComponent触摸事件的历史点信息。由于部分输入设备上报触点的频率非常高（最高可达每1 ms上报一次），而对输入事件的响应通常是为了使UI界面发生变化以响应用户操作，如果将触摸事件按照上报触点的频率如此高频率上报给应用，大多会造成冗余，因此触摸事件在一帧内只会上报一次给应用。在当前帧内上报的触点均作为历史点保存，如果应用需要直接处理这些数据，可调用该接口获取历史点信息。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| const void* window | 表示NativeWindow句柄。 |
| int32_t* size | 表示当前历史接触点数组的长度。 |
| OH_NativeXComponent_HistoricalPoint** historicalPoints | 表示指向当前历史接触点数组的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetMouseEvent()**

```ets
int32_t OH_NativeXComponent_GetMouseEvent(OH_NativeXComponent* component, const void* window, OH_NativeXComponent_MouseEvent* mouseEvent)
```

描述：

获取ArkUI XComponent调度的鼠标事件。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| const void* window | 表示NativeWindow句柄。 |
| OH_NativeXComponent_MouseEvent* mouseEvent | 表示指向当前鼠标事件的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_RegisterCallback()**

```ets
int32_t OH_NativeXComponent_RegisterCallback(OH_NativeXComponent* component, OH_NativeXComponent_Callback* callback)
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册回调。

起始版本： 8

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| OH_NativeXComponent_Callback* callback | 表示指向Surface生命周期和触摸事件回调的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_RegisterMouseEventCallback()**

```ets
int32_t OH_NativeXComponent_RegisterMouseEventCallback(OH_NativeXComponent* component, OH_NativeXComponent_MouseEvent_Callback* callback)
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册鼠标事件回调。

起始版本： 9

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| OH_NativeXComponent_MouseEvent_Callback* callback | 表示指向鼠标事件回调的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetExtraMouseEventInfo()**

```ets
int32_t OH_NativeXComponent_GetExtraMouseEventInfo(OH_NativeXComponent* component, OH_NativeXComponent_ExtraMouseEventInfo** extraMouseEventInfo)
```

描述：

从此[OH_NativeXComponent](OH_NativeXComponent.md)实例中获取扩展的鼠标事件信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| OH_NativeXComponent_ExtraMouseEventInfo** extraMouseEventInfo | 表示指向OH_NativeXComponent_ExtraMouseEventInfo类型指针的地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_NativeXComponent_GetMouseEventModifierKeyStates()**

```ets
int32_t OH_NativeXComponent_GetMouseEventModifierKeyStates(OH_NativeXComponent_ExtraMouseEventInfo* extraMouseEventInfo, uint64_t* keys)
```

描述：

从[OH_NativeXComponent_ExtraMouseEventInfo](OH_NativeXComponent_ExtraMouseEventInfo.md)实例中获取功能键按压状态信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent_ExtraMouseEventInfo* extraMouseEventInfo | 表示指向扩展的鼠标事件信息实例的指针。 |
| uint64_t* keys | 表示用于接收功能键按压状态信息的64位无符号整数的地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_NativeXComponent_RegisterFocusEventCallback()**

```ets
int32_t OH_NativeXComponent_RegisterFocusEventCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window))
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册获焦事件回调。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void (*callback)(OH_NativeXComponent* component, void* window) | 表示指向获焦事件回调的指针。- window: 表示NativeWindow句柄。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_RegisterKeyEventCallback()**

```ets
int32_t OH_NativeXComponent_RegisterKeyEventCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window))
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册按键事件回调。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void (*callback)(OH_NativeXComponent* component, void* window) | 表示指向按键事件回调的指针。- window: 表示NativeWindow句柄。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_RegisterBlurEventCallback()**

```ets
int32_t OH_NativeXComponent_RegisterBlurEventCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window))
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册失焦事件回调。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void (*callback)(OH_NativeXComponent* component, void* window) | 表示指向失焦事件回调的指针。- window: 表示NativeWindow句柄。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetKeyEvent()**

```ets
int32_t OH_NativeXComponent_GetKeyEvent(OH_NativeXComponent* component, OH_NativeXComponent_KeyEvent** keyEvent)
```

描述：

获取ArkUI XComponent调度的按键事件。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| OH_NativeXComponent_KeyEvent** keyEvent | 表示指向当前按键事件指针的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetKeyEventAction()**

```ets
int32_t OH_NativeXComponent_GetKeyEventAction(OH_NativeXComponent_KeyEvent* keyEvent, OH_NativeXComponent_KeyAction* action)
```

描述：

获取传入按键事件的动作。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent_KeyEvent* keyEvent | 表示指向OH_NativeXComponent_KeyEvent实例的指针。 |
| OH_NativeXComponent_KeyAction* action | 表示指向按键事件动作的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetKeyEventCode()**

```ets
int32_t OH_NativeXComponent_GetKeyEventCode(OH_NativeXComponent_KeyEvent* keyEvent, OH_NativeXComponent_KeyCode* code)
```

描述：

获取传入按键事件的按键码。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent_KeyEvent* keyEvent | 表示指向OH_NativeXComponent_KeyEvent实例的指针。 |
| OH_NativeXComponent_KeyCode* code | 表示指向按键事件按键码的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetKeyEventSourceType()**

```ets
int32_t OH_NativeXComponent_GetKeyEventSourceType(OH_NativeXComponent_KeyEvent* keyEvent, OH_NativeXComponent_EventSourceType* sourceType)
```

描述：

获取传入按键事件的事件源类型。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent_KeyEvent* keyEvent | 表示指向OH_NativeXComponent_KeyEvent实例的指针。 |
| OH_NativeXComponent_EventSourceType* sourceType | 表示指向按键事件事件源类型的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetKeyEventDeviceId()**

```ets
int32_t OH_NativeXComponent_GetKeyEventDeviceId(OH_NativeXComponent_KeyEvent* keyEvent, int64_t* deviceId)
```

描述：

获取传入按键事件的设备id。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent_KeyEvent* keyEvent | 表示指向OH_NativeXComponent_KeyEvent实例的指针。 |
| int64_t* deviceId | 表示指向按键事件设备id的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetKeyEventTimestamp()**

```ets
int32_t OH_NativeXComponent_GetKeyEventTimestamp(OH_NativeXComponent_KeyEvent* keyEvent, int64_t* timestamp)
```

描述：

获取传入按键事件的时间戳。

起始版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent_KeyEvent* keyEvent | 表示指向OH_NativeXComponent_KeyEvent实例的指针。 |
| int64_t* timestamp | 表示指向按键事件时间戳的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetKeyEventModifierKeyStates()**

```ets
int32_t OH_NativeXComponent_GetKeyEventModifierKeyStates(OH_NativeXComponent_KeyEvent* keyEvent, uint64_t* keys)
```

描述：

从按键事件中获取功能键按压状态信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent_KeyEvent* keyEvent | 表示指向按键事件的指针。 |
| uint64_t* keys | 表示用于接收功能键按压状态信息的64位无符号整数的地址。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_NativeXComponent_GetKeyEventNumLockState()**

```ets
int32_t OH_NativeXComponent_GetKeyEventNumLockState(OH_NativeXComponent_KeyEvent* keyEvent, bool* isNumLockOn)
```

描述：

从按键事件中获取NumLock（小键盘锁定）键的状态信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent_KeyEvent* keyEvent | 表示指向按键事件的指针。 |
| bool* isNumLockOn | 表示用于接收NumLock（小键盘锁定）键状态的bool类型变量的地址。true表示小键盘锁定，false表示小键盘解锁。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_NativeXComponent_GetKeyEventCapsLockState()**

```ets
int32_t OH_NativeXComponent_GetKeyEventCapsLockState(OH_NativeXComponent_KeyEvent* keyEvent, bool* isCapsLockOn)
```

描述：

从按键事件中获取CapsLock（大写锁定）键的状态信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent_KeyEvent* keyEvent | 表示指向按键事件的指针。 |
| bool* isCapsLockOn | 表示用于接收CapsLock（大写锁定）键状态的bool类型变量的地址。true表示大写处于锁定，false表示大写处于解锁。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_NativeXComponent_GetKeyEventScrollLockState()**

```ets
int32_t OH_NativeXComponent_GetKeyEventScrollLockState(OH_NativeXComponent_KeyEvent* keyEvent, bool* isScrollLockOn)
```

描述：

从按键事件中获取ScrollLock（滚动锁定）键的状态信息。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent_KeyEvent* keyEvent | 表示指向按键事件的指针。 |
| bool* isScrollLockOn | 表示用于接收ScrollLock（滚动锁定）键状态的bool类型变量的地址。true表示滚动处于锁定，false表示滚动处于解锁。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_NativeXComponent_SetExpectedFrameRateRange()**

```ets
int32_t OH_NativeXComponent_SetExpectedFrameRateRange(OH_NativeXComponent* component, OH_NativeXComponent_ExpectedRateRange* range)
```

描述：

设置期望帧率范围。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| OH_NativeXComponent_ExpectedRateRange* range | 表示指向OH_NativeXComponent_ExpectedRateRange类型的期望帧率信息对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_RegisterOnFrameCallback()**

```ets
int32_t OH_NativeXComponent_RegisterOnFrameCallback(OH_NativeXComponent* component,void (*callback)(OH_NativeXComponent* component, uint64_t timestamp, uint64_t targetTimestamp))
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册显示更新回调，并使能每帧回调此函数。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void (*callback)(OH_NativeXComponent* component, uint64_t timestamp, uint64_t targetTimestamp) | 表示指向显示更新回调的指针。- timestamp: 当前帧到达的时间（单位：纳秒）。- targetTimestamp: 下一帧预期到达的时间（单位：纳秒）。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_UnregisterOnFrameCallback()**

```ets
int32_t OH_NativeXComponent_UnregisterOnFrameCallback(OH_NativeXComponent* component)
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例取消注册回调函数，并关闭每帧回调此函数。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_AttachNativeRootNode()**

```ets
int32_t OH_NativeXComponent_AttachNativeRootNode(OH_NativeXComponent* component, ArkUI_NodeHandle root)
```

描述：

将通过ArkUI的Native接口创建出来的UI组件挂载到当前XComponent上。

起始版本： 12

废弃版本： 20

替代接口： [OH_ArkUI_NodeContent_AddNode](native_node.h.md#ZH-CN_TOPIC_0000002522081032__oh_arkui_nodecontent_addnode)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| ArkUI_NodeHandle root | 表示指向Native接口创建的组件实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 成功。 返回 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 参数异常。 |

**OH_NativeXComponent_DetachNativeRootNode()**

```ets
int32_t OH_NativeXComponent_DetachNativeRootNode(OH_NativeXComponent* component, ArkUI_NodeHandle root)
```

描述：

将ArkUI的Native组件从当前XComponent上卸载。

起始版本： 12

废弃版本： 20

替代接口： [OH_ArkUI_NodeContent_RemoveNode](native_node.h.md#ZH-CN_TOPIC_0000002522081032__oh_arkui_nodecontent_removenode)

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| ArkUI_NodeHandle root | 表示指向Native接口创建的组件实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 成功。 返回 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 参数异常。 |

**OH_NativeXComponent_RegisterUIInputEventCallback()**

```ets
int32_t OH_NativeXComponent_RegisterUIInputEventCallback(OH_NativeXComponent *component,void (*callback)(OH_NativeXComponent *component, ArkUI_UIInputEvent *event,ArkUI_UIInputEvent_Type type),ArkUI_UIInputEvent_Type type)
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册UI输入事件回调，并使能收到UI输入事件时回调此函数。当前仅支持轴事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent *component | 表示指向OH_NativeXComponent实例的指针。 |
| void (*callback)(OH_NativeXComponent *component, ArkUI_UIInputEvent *event,ArkUI_UIInputEvent_Type type) | 表示指向UI输入事件回调的指针。- event: 表示指向UI输入事件的指针。 |
| ArkUI_UIInputEvent_Type type | 表示当前UI输入事件的类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 参数异常。 |

**OH_NativeXComponent_RegisterOnTouchInterceptCallback()**

```ets
int32_t OH_NativeXComponent_RegisterOnTouchInterceptCallback(OH_NativeXComponent* component, HitTestMode (*callback)(OH_NativeXComponent* component, ArkUI_UIInputEvent* event))
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册自定义事件拦截回调，并使能在做触摸测试时回调此函数。通过该回调获取到的事件对象不支持UIInput相关信息操作接口，建议切换为通过注册native node上的[NODE_ON_TOUCH_INTERCEPT](native_node.h.md#ZH-CN_TOPIC_0000002522081032__arkui_nodeeventtype)通用事件来支持。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| HitTestMode (*callback)(OH_NativeXComponent* component, ArkUI_UIInputEvent* event) | 表示指向自定义事件拦截回调的指针。- event: 表示指向UI输入事件的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 参数异常。 |

**OH_NativeXComponent_SetNeedSoftKeyboard()**

```ets
int32_t OH_NativeXComponent_SetNeedSoftKeyboard(OH_NativeXComponent* component, bool needSoftKeyboard)
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例设置是否需要软键盘。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| bool needSoftKeyboard | 表示此OH_NativeXComponent实例是否需要软键盘。需要时为true，不需要时为false，默认值为false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_RegisterSurfaceShowCallback()**

```ets
int32_t OH_NativeXComponent_RegisterSurfaceShowCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window))
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册Surface显示回调，该回调在应用窗口已经从后台回到前台时触发。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void (*callback)(OH_NativeXComponent* component, void* window) | 表示指向Surface显示回调的指针。- window: 表示NativeWindow句柄。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_RegisterSurfaceHideCallback()**

```ets
int32_t OH_NativeXComponent_RegisterSurfaceHideCallback(OH_NativeXComponent* component, void (*callback)(OH_NativeXComponent* component, void* window))
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册Surface隐藏回调，该回调在应用窗口已经从前台进入后台时触发。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| void (*callback)(OH_NativeXComponent* component, void* window) | 表示指向Surface隐藏回调的指针。- window: 表示NativeWindow句柄。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 执行成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_NativeXComponent_GetTouchEventSourceType()**

```ets
int32_t OH_NativeXComponent_GetTouchEventSourceType(OH_NativeXComponent* component, int32_t pointId, OH_NativeXComponent_EventSourceType* sourceType)
```

描述：

获取ArkUI XComponent触摸事件的输入设备类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| int32_t pointId | 表示触摸点的id。仅当传入的id为触发该touch事件的触点id时，可正确返回输入设备类型，否则返回OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER。 |
| OH_NativeXComponent_EventSourceType* sourceType | 表示指向返回设备类型的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 参数异常。 OH_NATIVEXCOMPONENT_RESULT_FAILED - 其他错误。 |

**OH_NativeXComponent_GetNativeXComponent()**

```ets
OH_NativeXComponent* OH_NativeXComponent_GetNativeXComponent(ArkUI_NodeHandle node)
```

描述：

基于Native接口创建的组件实例获取[OH_NativeXComponent](OH_NativeXComponent.md)类型的指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 指向Native接口创建的组件实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_NativeXComponent* | 表示指向OH_NativeXComponent实例的指针。 |

**OH_NativeXComponent_GetNativeAccessibilityProvider()**

```ets
int32_t OH_NativeXComponent_GetNativeAccessibilityProvider(OH_NativeXComponent* component, ArkUI_AccessibilityProvider** handle)
```

描述：

获取ArkUI XComponent无障碍接入句柄指针。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| ArkUI_AccessibilityProvider** handle | 表示指向ArkUI_AccessibilityProvider实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 参数异常。 OH_NATIVEXCOMPONENT_RESULT_FAILED - 其他错误。 |

**OH_NativeXComponent_RegisterKeyEventCallbackWithResult()**

```ets
int32_t OH_NativeXComponent_RegisterKeyEventCallbackWithResult(OH_NativeXComponent* component, bool (*callback)(OH_NativeXComponent* component, void* window))
```

描述：

为此[OH_NativeXComponent](OH_NativeXComponent.md)实例注册带有返回值的按键事件回调。通过此接口注册的按键事件回调都必须返回一个结果，即true或false。当返回值为true时，该事件将不会继续分发；当返回值为false时，该事件将按照事件处理流程继续分发。

起始版本： 14

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeXComponent* component | 表示指向OH_NativeXComponent实例的指针。 |
| bool (*callback)(OH_NativeXComponent* component, void* window) | 表示指向按键事件回调的指针。- window: 表示NativeWindow句柄。当回调返回值为true时，该事件将不会继续分发；当回调返回值为false时，该事件将按照事件处理流程继续分发。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 OH_NATIVEXCOMPONENT_RESULT_SUCCESS - 回调函数注册成功。 OH_NATIVEXCOMPONENT_RESULT_BAD_PARAMETER - 传入参数异常。 |

**OH_ArkUI_XComponent_StartImageAnalyzer()**

```ets
int32_t OH_ArkUI_XComponent_StartImageAnalyzer(ArkUI_NodeHandle node, void* userData,void (*callback)(ArkUI_NodeHandle node, ArkUI_XComponent_ImageAnalyzerState statusCode, void* userData))
```

描述：

为此XComponent组件实例开始图像AI分析，使用前需先使能图像AI分析能力。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示XComponent组件实例。 |
| void* userData | 表示开发者需要在回调函数执行时获取的数据的指针。 |
| void (*callback)(ArkUI_NodeHandle node, ArkUI_XComponent_ImageAnalyzerState statusCode, void* userData) | 表示图像AI分析状态刷新时触发的回调函数。- statusCode: 回调函数的入参之一，表示当前的图像分析状态。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_XComponent_StopImageAnalyzer()**

```ets
int32_t OH_ArkUI_XComponent_StopImageAnalyzer(ArkUI_NodeHandle node)
```

描述：

为此XComponent组件实例停止图像AI分析。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示XComponent组件实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_SurfaceHolder_Create()**

```ets
OH_ArkUI_SurfaceHolder* OH_ArkUI_SurfaceHolder_Create(ArkUI_NodeHandle node)
```

描述：

创建XComponent组件的[OH_ArkUI_SurfaceHolder](OH_ArkUI_SurfaceHolder.md)对象。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示指向Native接口创建的XComponent组件实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| OH_ArkUI_SurfaceHolder* | 返回被创建的OH_ArkUI_SurfaceHolder对象的指针。 |

**OH_ArkUI_SurfaceHolder_Dispose()**

```ets
void OH_ArkUI_SurfaceHolder_Dispose(OH_ArkUI_SurfaceHolder* surfaceHolder)
```

描述：

销毁[OH_ArkUI_SurfaceHolder](OH_ArkUI_SurfaceHolder.md)对象。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceHolder* surfaceHolder | 表示指向需要销毁的OH_ArkUI_SurfaceHolder实例的指针。 |

**OH_ArkUI_SurfaceHolder_SetUserData()**

```ets
int32_t OH_ArkUI_SurfaceHolder_SetUserData(OH_ArkUI_SurfaceHolder* surfaceHolder, void* userData)
```

描述：

向[OH_ArkUI_SurfaceHolder](OH_ArkUI_SurfaceHolder.md)实例存储自定义数据。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceHolder* surfaceHolder | 表示指向存储自定义数据的OH_ArkUI_SurfaceHolder实例的指针。 |
| void* userData | 表示指向要存储的自定义数据的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_SurfaceHolder_GetUserData()**

```ets
void* OH_ArkUI_SurfaceHolder_GetUserData(OH_ArkUI_SurfaceHolder* surfaceHolder)
```

描述：

获取[OH_ArkUI_SurfaceHolder](OH_ArkUI_SurfaceHolder.md)实例存储的自定义数据。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceHolder* surfaceHolder | 表示指向存储自定义数据的OH_ArkUI_SurfaceHolder实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| void* | 返回自定义数据。 |

**OH_ArkUI_SurfaceCallback_Create()**

```ets
OH_ArkUI_SurfaceCallback* OH_ArkUI_SurfaceCallback_Create()
```

描述：

创建[OH_ArkUI_SurfaceCallback](OH_ArkUI_SurfaceCallback.md)对象。

起始版本： 19

返回：

| 类型 | 说明 |
| --- | --- |
| OH_ArkUI_SurfaceCallback* | 返回创建的OH_ArkUI_SurfaceCallback对象的指针。 |

**OH_ArkUI_SurfaceCallback_Dispose()**

```ets
void OH_ArkUI_SurfaceCallback_Dispose(OH_ArkUI_SurfaceCallback* callback)
```

描述：

销毁[OH_ArkUI_SurfaceCallback](OH_ArkUI_SurfaceCallback.md)对象。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceCallback* callback | 表示指向需要销毁的OH_ArkUI_SurfaceCallback对象的指针。 |

**OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent()**

```ets
void OH_ArkUI_SurfaceCallback_SetSurfaceCreatedEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceCreated)(OH_ArkUI_SurfaceHolder* surfaceHolder))
```

描述：

设置Surface生命周期回调中的创建回调事件。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceCallback* callback | 表示指向Surface生命周期回调的指针。 |
| void (*onSurfaceCreated)(OH_ArkUI_SurfaceHolder* surfaceHolder) | 表示声明Surface创建时会触发的回调事件。- surfaceHolder: 表示指向OH_ArkUI_SurfaceHolder实例的指针。 |

**OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent()**

```ets
void OH_ArkUI_SurfaceCallback_SetSurfaceChangedEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceChanged)(OH_ArkUI_SurfaceHolder* surfaceHolder, uint64_t width, uint64_t height))
```

描述：

设置Surface生命周期回调中的大小改变回调事件。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceCallback* callback | 表示指向Surface生命周期回调的指针。 |
| void (*onSurfaceChanged)(OH_ArkUI_SurfaceHolder* surfaceHolder, uint64_t width, uint64_t height) | 表示声明Surface大小改变时会触发的回调事件。- surfaceHolder: 表示指向OH_ArkUI_SurfaceHolder实例的指针。- width: 表示Surface大小变化后的宽度。- height: 表示Surface大小变化后的高度。 |

**OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent()**

```ets
void OH_ArkUI_SurfaceCallback_SetSurfaceDestroyedEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceDestroyed)(OH_ArkUI_SurfaceHolder* surfaceHolder))
```

描述：

设置Surface生命周期回调中的销毁回调事件。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceCallback* callback | 表示指向Surface生命周期回调的指针。 |
| void (*onSurfaceDestroyed)(OH_ArkUI_SurfaceHolder* surfaceHolder) | 表示声明Surface销毁时会触发的回调事件。- surfaceHolder: 表示指向OH_ArkUI_SurfaceHolder实例的指针。 |

**OH_ArkUI_SurfaceHolder_AddSurfaceCallback()**

```ets
int32_t OH_ArkUI_SurfaceHolder_AddSurfaceCallback(OH_ArkUI_SurfaceHolder* surfaceHolder,OH_ArkUI_SurfaceCallback* callback)
```

描述：

添加Surface生命周期回调到[OH_ArkUI_SurfaceHolder](OH_ArkUI_SurfaceHolder.md)实例。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceHolder* surfaceHolder | 表示指向OH_ArkUI_SurfaceHolder实例的指针。 |
| OH_ArkUI_SurfaceCallback* callback | 表示指向新回调的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_SurfaceHolder_RemoveSurfaceCallback()**

```ets
int32_t OH_ArkUI_SurfaceHolder_RemoveSurfaceCallback(OH_ArkUI_SurfaceHolder* surfaceHolder,OH_ArkUI_SurfaceCallback* callback)
```

描述：

删除[OH_ArkUI_SurfaceHolder](OH_ArkUI_SurfaceHolder.md)实例的先前添加的Surface生命周期回调。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceHolder* surfaceHolder | 表示指向OH_ArkUI_SurfaceHolder实例的指针。 |
| OH_ArkUI_SurfaceCallback* callback | 表示指向需要删除的回调的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_XComponent_GetNativeWindow()**

```ets
OHNativeWindow* OH_ArkUI_XComponent_GetNativeWindow(OH_ArkUI_SurfaceHolder* surfaceHolder)
```

描述：

获取[OH_ArkUI_SurfaceHolder](OH_ArkUI_SurfaceHolder.md)实例关联的NativeWindow。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceHolder* surfaceHolder | 表示指向OH_ArkUI_SurfaceHolder实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| NativeWindow* | 返回OH_ArkUI_SurfaceHolder实例关联的NativeWindow。 |

**OH_ArkUI_XComponent_SetAutoInitialize()**

```ets
int32_t OH_ArkUI_XComponent_SetAutoInitialize(ArkUI_NodeHandle node, bool autoInitialize)
```

描述：

设置XComponent组件是否需要自动初始化Surface的标志位。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示指向XComponent组件实例的指针。 |
| bool autoInitialize | 表示XComponent组件是否需要自动初始化Surface。如果autoInitialize值是true，OnSurfaceCreated回调会在挂树时被触发，OnSurfaceDestroyed回调会在下树时被触发。false表示组件不需要自动初始化Surface。 autoInitialize默认值是true。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_XComponent_Initialize()**

```ets
int32_t OH_ArkUI_XComponent_Initialize(ArkUI_NodeHandle node)
```

描述：

初始化XComponent组件持有的Surface。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示指向XComponent组件实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 返回 ARKUI_ERROR_CODE_XCOMPONENT_STATE_INVALID - XComponent持有的Surface已经被初始化。 |

**OH_ArkUI_XComponent_Finalize()**

```ets
int32_t OH_ArkUI_XComponent_Finalize(ArkUI_NodeHandle node)
```

描述：

销毁XComponent组件持有的Surface。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示指向XComponent组件实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 返回 ARKUI_ERROR_CODE_XCOMPONENT_STATE_INVALID - XComponent持有的Surface已经被销毁。 |

**OH_ArkUI_XComponent_IsInitialized()**

```ets
int32_t OH_ArkUI_XComponent_IsInitialized(ArkUI_NodeHandle node, bool* isInitialized)
```

描述：

获取XComponent组件是否已经初始化的标志位。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示指向XComponent组件实例的指针。 |
| bool* isInitialized | 表示XComponent组件是否已经初始化Surface。true表示组件已初始化Surface，false表示组件未初始化Surface。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_XComponent_SetExpectedFrameRateRange()**

```ets
int32_t OH_ArkUI_XComponent_SetExpectedFrameRateRange(ArkUI_NodeHandle node, OH_NativeXComponent_ExpectedRateRange range)
```

描述：

为此XComponent组件实例设置期望帧率。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示XComponent组件实例。 |
| OH_NativeXComponent_ExpectedRateRange range | 表示OH_NativeXComponent_ExpectedRateRange类型的期望帧率信息对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_XComponent_RegisterOnFrameCallback()**

```ets
int32_t OH_ArkUI_XComponent_RegisterOnFrameCallback(ArkUI_NodeHandle node,void (*callback)(ArkUI_NodeHandle node, uint64_t timestamp, uint64_t targetTimestamp))
```

描述：

为此XComponent组件实例注册帧回调函数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示XComponent组件实例。 |
| void (*callback)(ArkUI_NodeHandle node, uint64_t timestamp, uint64_t targetTimestamp) | 表示执行帧回调函数的指针。- timestamp: 当前帧到达的时间（单位：纳秒）。- targetTimestamp: 下一帧预期到达的时间（单位：纳秒）。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_XComponent_UnregisterOnFrameCallback()**

```ets
int32_t OH_ArkUI_XComponent_UnregisterOnFrameCallback(ArkUI_NodeHandle node)
```

描述：

为此XComponent组件实例取消注册帧回调函数。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示XComponent组件实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_XComponent_SetNeedSoftKeyboard()**

```ets
int32_t OH_ArkUI_XComponent_SetNeedSoftKeyboard(ArkUI_NodeHandle node, bool needSoftKeyboard)
```

描述：

为此XComponent组件实例设置是否需要软键盘。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示XComponent组件实例。 |
| bool needSoftKeyboard | 表示是否需要软键盘。需要时为true，不需要时为false，默认值为false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行的状态代码。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |

**OH_ArkUI_AccessibilityProvider_Create()**

```ets
ArkUI_AccessibilityProvider* OH_ArkUI_AccessibilityProvider_Create(ArkUI_NodeHandle node)
```

描述：

基于此XComponent实例创建[ArkUI_AccessibilityProvider](ArkUI_AccessibilityProvider.md)实例。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle node | 表示XComponent组件实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_AccessibilityProvider* | ArkUI_AccessibilityProvider类型的指针。 |

**OH_ArkUI_AccessibilityProvider_Dispose()**

```ets
void OH_ArkUI_AccessibilityProvider_Dispose(ArkUI_AccessibilityProvider* provider)
```

描述：

销毁由Native接口[OH_ArkUI_AccessibilityProvider_Create](native_interface_xcomponent.h.md#ZH-CN_TOPIC_0000002522241028__oh_arkui_accessibilityprovider_create)创建的[ArkUI_AccessibilityProvider](ArkUI_AccessibilityProvider.md)实例。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityProvider* provider | 表示由Native接口OH_ArkUI_AccessibilityProvider_Create创建的ArkUI_AccessibilityProvider实例。 |

**OH_ArkUI_SurfaceCallback_SetSurfaceShowEvent()**

```ets
void OH_ArkUI_SurfaceCallback_SetSurfaceShowEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceShow)(OH_ArkUI_SurfaceHolder* surfaceHolder))
```

描述：

为此[OH_ArkUI_SurfaceCallback](OH_ArkUI_SurfaceCallback.md)实例设置Surface显示回调，该回调在应用窗口已经从后台回到前台时触发。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceCallback* callback | 表示指向OH_ArkUI_SurfaceCallback实例的指针。 |
| onSurfaceShow | 表示Surface显示回调函数指针。- surfaceHolder: 表示指向OH_ArkUI_SurfaceHolder实例的指针。 |

**OH_ArkUI_SurfaceCallback_SetSurfaceHideEvent()**

```ets
void OH_ArkUI_SurfaceCallback_SetSurfaceHideEvent(OH_ArkUI_SurfaceCallback* callback,void (*onSurfaceHide)(OH_ArkUI_SurfaceHolder* surfaceHolder))
```

描述：

为此[OH_ArkUI_SurfaceCallback](OH_ArkUI_SurfaceCallback.md)实例设置Surface隐藏回调，该回调在应用窗口已经从前台进入后台时触发。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceCallback* callback | 表示指向OH_ArkUI_SurfaceCallback实例的指针。 |
| onSurfaceHide | 表示Surface隐藏回调函数指针。- surfaceHolder: 表示指向OH_ArkUI_SurfaceHolder实例的指针。 |

**OH_ArkUI_XComponentSurfaceConfig_Create()**

```ets
ArkUI_XComponentSurfaceConfig* OH_ArkUI_XComponentSurfaceConfig_Create()
```

描述：

创建XComponent组件的[ArkUI_XComponentSurfaceConfig](ArkUI_XComponentSurfaceConfig.md)对象。

起始版本： 22

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_XComponentSurfaceConfig* | 返回创建的ArkUI_XComponentSurfaceConfig对象的指针。 |

**OH_ArkUI_XComponentSurfaceConfig_Dispose()**

```ets
void OH_ArkUI_XComponentSurfaceConfig_Dispose(ArkUI_XComponentSurfaceConfig* config)
```

描述：

销毁[ArkUI_XComponentSurfaceConfig](ArkUI_XComponentSurfaceConfig.md)对象。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_XComponentSurfaceConfig* config | 表示指向需要销毁的ArkUI_XComponentSurfaceConfig对象的指针。 |

**OH_ArkUI_XComponentSurfaceConfig_SetIsOpaque()**

```ets
void OH_ArkUI_XComponentSurfaceConfig_SetIsOpaque(ArkUI_XComponentSurfaceConfig* config, bool isOpaque)
```

描述：

设置XComponent组件持有的Surface在渲染时是否被视为不透明，无论该Surface是否存在半透明像素。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_XComponentSurfaceConfig* config | 表示指向ArkUI_XComponentSurfaceConfig实例的指针。 |
| bool isOpaque | 表示设置XComponent组件持有的Surface在渲染时是否需要被视为不透明。true表示需要被视为不透明，false表示不需要被视为不透明，默认值为false，即在渲染时会应用Surface中绘制内容像素的透明度。 |

**OH_ArkUI_SurfaceHolder_SetSurfaceConfig()**

```ets
int32_t OH_ArkUI_SurfaceHolder_SetSurfaceConfig(OH_ArkUI_SurfaceHolder* surfaceHolder, ArkUI_XComponentSurfaceConfig *config)
```

描述：

为[OH_ArkUI_SurfaceHolder](OH_ArkUI_SurfaceHolder.md)实例设置Surface选项。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ArkUI_SurfaceHolder* surfaceHolder | 表示指向OH_ArkUI_SurfaceHolder实例的指针。 |
| ArkUI_XComponentSurfaceConfig *config | 表示指向ArkUI_XComponentSurfaceConfig实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回执行结果。 返回 ARKUI_ERROR_CODE_NO_ERROR - 执行成功。 返回 ARKUI_ERROR_CODE_PARAM_INVALID - 传入参数异常。 |