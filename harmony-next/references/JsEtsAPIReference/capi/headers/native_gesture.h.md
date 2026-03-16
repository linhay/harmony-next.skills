# native_gesture.h

#### 概述

提供NativeGesture接口的类型定义。

**引用文件：** <arkui/native_gesture.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：**[ArkUI_NativeModule](../../topics/system-services/ArkUI_NativeModule.md)

**相关示例：**[NdkGestureSetting](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/NdkGestureSetting)、[NdkGestureNestScroll](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/NdkGestureNestScroll)、[NdkGestureBlocking](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/NdkGestureBlocking)

#### 汇总

#### 结构体

名称typedef关键字描述[ArkUI_NativeGestureAPI_1](../../topics/networking/ArkUI_NativeGestureAPI_1.md)ArkUI_NativeGestureAPI_1手势模块接口集合。[ArkUI_NativeGestureAPI_2](../../topics/networking/ArkUI_NativeGestureAPI_2.md)-定义手势模块接口集合。[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)ArkUI_GestureRecognizer提供手势组件实例对象定义。[ArkUI_GestureInterruptInfo](../../topics/input/ArkUI_GestureInterruptInfo.md)ArkUI_GestureInterruptInfo提供手势打断数据类型对象定义。[ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)ArkUI_GestureEvent提供手势事件数据类型对象定义。[ArkUI_GestureEventTargetInfo](../../topics/input/ArkUI_GestureEventTargetInfo.md)ArkUI_GestureEventTargetInfo提供手势事件目标信息类型对象定义。[ArkUI_ParallelInnerGestureEvent](../../topics/input/ArkUI_ParallelInnerGestureEvent.md)ArkUI_ParallelInnerGestureEvent提供并行内部手势事件类型对象定义。[ArkUI_TouchRecognizer](../../topics/input/ArkUI_TouchRecognizer.md)ArkUI_TouchRecognizer定义触摸识别器。[ArkUI_TouchRecognizerHandle*](../../topics/input/ArkUI_TouchRecognizerHandle_.md)ArkUI_TouchRecognizerHandleArray定义触摸识别器句柄数组。[ArkUI_GestureRecognizerHandle*](../../topics/input/ArkUI_GestureRecognizerHandle_.md)ArkUI_GestureRecognizerHandleArray提供手势识别器句柄类型数组对象定义。

#### 枚举

名称typedef关键字描述[ArkUI_GestureEventActionType](#ZH-CN_TOPIC_0000002497605076__arkui_gestureeventactiontype)ArkUI_GestureEventActionType定义手势事件类型。[ArkUI_GesturePriority](#ZH-CN_TOPIC_0000002497605076__arkui_gesturepriority)ArkUI_GesturePriority定义手势事件模式。[ArkUI_GroupGestureMode](#ZH-CN_TOPIC_0000002497605076__arkui_groupgesturemode)ArkUI_GroupGestureMode定义手势组事件模式。[ArkUI_GestureDirection](#ZH-CN_TOPIC_0000002497605076__arkui_gesturedirection)ArkUI_GestureDirection定义滑动手势方向。[ArkUI_GestureMask](#ZH-CN_TOPIC_0000002497605076__arkui_gesturemask)ArkUI_GestureMask定义手势屏蔽模式。[ArkUI_GestureRecognizerType](#ZH-CN_TOPIC_0000002497605076__arkui_gesturerecognizertype)ArkUI_GestureRecognizerType定义手势类型。[ArkUI_GestureInterruptResult](#ZH-CN_TOPIC_0000002497605076__arkui_gestureinterruptresult)ArkUI_GestureInterruptResult定义手势打断结果。[ArkUI_GestureRecognizerState](#ZH-CN_TOPIC_0000002497605076__arkui_gesturerecognizerstate)ArkUI_GestureRecognizerState定义手势识别器状态。

#### 函数

名称typedef关键字描述[typedef void (*ArkUI_GestureRecognizerDisposeNotifyCallback)(ArkUI_GestureRecognizer* recognizer, void* userData)](#ZH-CN_TOPIC_0000002497605076__arkui_gesturerecognizerdisposenotifycallback)ArkUI_GestureRecognizerDisposeNotifyCallback定义手势识别器析构通知事件的回调函数类型。[bool OH_ArkUI_GestureInterruptInfo_GetSystemFlag(const ArkUI_GestureInterruptInfo* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureinterruptinfo_getsystemflag)-判断是否组件内置手势。[ArkUI_GestureRecognizer* OH_ArkUI_GestureInterruptInfo_GetRecognizer(const ArkUI_GestureInterruptInfo* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureinterruptinfo_getrecognizer)-返回被打断的手势指针。[ArkUI_GestureEvent* OH_ArkUI_GestureInterruptInfo_GetGestureEvent(const ArkUI_GestureInterruptInfo* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureinterruptinfo_getgestureevent)-返回打断的手势事件数据。[int32_t OH_ArkUI_GestureInterruptInfo_GetSystemRecognizerType(const ArkUI_GestureInterruptInfo* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureinterruptinfo_getsystemrecognizertype)-当要触发的是系统内部手势时，使用该方法可返回该系统内部手势的类型。[int32_t OH_ArkUI_GestureInterruptInfo_GetTouchRecognizers(const ArkUI_GestureInterruptInfo* info,ArkUI_TouchRecognizerHandleArray* recognizers, int32_t* size)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureinterruptinfo_gettouchrecognizers)-从手势打断信息中获取触摸识别器。[ArkUI_NodeHandle OH_ArkUI_TouchRecognizer_GetNodeHandle(const ArkUI_TouchRecognizerHandle recognizer)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_touchrecognizer_getnodehandle)-获取触摸识别器对应的组件句柄。[int32_t OH_ArkUI_TouchRecognizer_CancelTouch(ArkUI_TouchRecognizerHandle recognizer, ArkUI_GestureInterruptInfo* info)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_touchrecognizer_canceltouch)-在手势打断回调中向指定的触摸识别器发送取消触摸的事件[ArkUI_GestureEventActionType OH_ArkUI_GestureEvent_GetActionType(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureevent_getactiontype)-返回手势事件类型。[const ArkUI_UIInputEvent* OH_ArkUI_GestureEvent_GetRawInputEvent(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureevent_getrawinputevent)-返回手势输入。[int32_t OH_ArkUI_LongPress_GetRepeatCount(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_longpress_getrepeatcount)-返回是否为重复触发事件。[float OH_ArkUI_PanGesture_GetVelocity(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_pangesture_getvelocity)-滑动手势返回手势主方向速度。[float OH_ArkUI_PanGesture_GetVelocityX(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_pangesture_getvelocityx)-滑动手势返回当前手势的x轴方向速度。[float OH_ArkUI_PanGesture_GetVelocityY(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_pangesture_getvelocityy)-滑动手势返回当前手势的y轴方向速度。[float OH_ArkUI_PanGesture_GetOffsetX(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_pangesture_getoffsetx)-滑动手势返回当前手势事件x轴相对偏移量。[float OH_ArkUI_PanGesture_GetOffsetY(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_pangesture_getoffsety)-滑动手势返回当前手势事件y轴相对偏移量。[float OH_ArkUI_SwipeGesture_GetAngle(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_swipegesture_getangle)-

快滑手势返回当前手势事件角度信息。角度计算方式：快滑手势被识别到后，连接两根手指之间的线被识别为起始线条，随着手指的滑动，手指之间的线条会发生旋转，

 根据起始线条两端点和当前线条两端点的坐标，使用反正切函数分别计算其相对于水平方向的夹角，

 最后arctan2(cy2-cy1,cx2-cx1)-arctan2(y2-y1,x2-x1)为旋转的角度。

 以起始线条为坐标系，顺时针旋转为0到180度，逆时针旋转为-180到0度。

[float OH_ArkUI_SwipeGesture_GetVelocity(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_swipegesture_getvelocity)-快滑手势场景中所有手指滑动平均速度。[float OH_ArkUI_RotationGesture_GetAngle(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_rotationgesture_getangle)-旋转手势返回当前手势事件角度信息。[float OH_ArkUI_PinchGesture_GetScale(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_pinchgesture_getscale)-捏合手势返回当前手势事件缩放信息。[float OH_ArkUI_PinchGesture_GetCenterX(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_pinchgesture_getcenterx)-捏合手势中心点相对于当前组件元素左上角x轴坐标。[float OH_ArkUI_PinchGesture_GetCenterY(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_pinchgesture_getcentery)-捏合手势中心点相对于当前组件元素左上角y轴坐标。[ArkUI_NodeHandle OH_ArkUI_GestureEvent_GetNode(const ArkUI_GestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureevent_getnode)-获取绑定该手势的ARKUI组件[int32_t OH_ArkUI_GetResponseRecognizersFromInterruptInfo(const ArkUI_GestureInterruptInfo* event,ArkUI_GestureRecognizerHandleArray* responseChain, int32_t* count)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getresponserecognizersfrominterruptinfo)-获取手势响应链的信息。[int32_t OH_ArkUI_SetGestureRecognizerEnabled(ArkUI_GestureRecognizer* recognizer, bool enabled)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_setgesturerecognizerenabled)-设置手势识别器的使能状态。[int32_t OH_ArkUI_SetGestureRecognizerLimitFingerCount(ArkUI_GestureRecognizer* recognizer, bool limitFingerCount)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_setgesturerecognizerlimitfingercount)-设置是否严格检查触摸手指数量的标志。实际触摸手指数量不等于设置的手指数量的时候，该手势识别不成功。[bool OH_ArkUI_GetGestureRecognizerEnabled(ArkUI_GestureRecognizer* recognizer)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgesturerecognizerenabled)-获取手势识别器的使能状态。[int32_t OH_ArkUI_GetGestureRecognizerState(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureRecognizerState* state)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgesturerecognizerstate)-获取手势识别器的状态。[int32_t OH_ArkUI_GetGestureEventTargetInfo(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureEventTargetInfo** info)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgestureeventtargetinfo)-获取手势事件目标信息。[int32_t OH_ArkUI_GestureEventTargetInfo_IsScrollBegin(ArkUI_GestureEventTargetInfo* info, bool* ret)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureeventtargetinfo_isscrollbegin)-当前滚动类容器组件是否在顶部。[int32_t OH_ArkUI_GestureEventTargetInfo_IsScrollEnd(ArkUI_GestureEventTargetInfo* info, bool* ret)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureeventtargetinfo_isscrollend)-当前滚动类容器组件是否在底部。[int32_t OH_ArkUI_GetPanGestureDirectionMask(ArkUI_GestureRecognizer* recognizer,ArkUI_GestureDirectionMask* directionMask)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getpangesturedirectionmask)-获取滑动手势的滑动方向。[bool OH_ArkUI_IsBuiltInGesture(ArkUI_GestureRecognizer* recognizer)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_isbuiltingesture)-当前手势是否为系统内置手势。[int32_t OH_ArkUI_GetGestureTag(ArkUI_GestureRecognizer* recognizer, char* buffer, int32_t bufferSize, int32_t* result)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgesturetag)-获取手势识别器的标记。[int32_t OH_ArkUI_GetGestureBindNodeId(ArkUI_GestureRecognizer* recognizer, char* nodeId, int32_t size,int32_t* result)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgesturebindnodeid)-获取手势识别器绑定的组件的ID。[bool OH_ArkUI_IsGestureRecognizerValid(ArkUI_GestureRecognizer* recognizer)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_isgesturerecognizervalid)-当前手势识别器是否有效。[void* OH_ArkUI_ParallelInnerGestureEvent_GetUserData(ArkUI_ParallelInnerGestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_parallelinnergestureevent_getuserdata)-获取并行内部手势事件中的用户自定义数据。[ArkUI_GestureRecognizer* OH_ArkUI_ParallelInnerGestureEvent_GetCurrentRecognizer(ArkUI_ParallelInnerGestureEvent* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_parallelinnergestureevent_getcurrentrecognizer)-获取并行内部手势事件中的当前手势识别器。[int32_t OH_ArkUI_ParallelInnerGestureEvent_GetConflictRecognizers(ArkUI_ParallelInnerGestureEvent* event,ArkUI_GestureRecognizerHandleArray* array, int32_t* size)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_parallelinnergestureevent_getconflictrecognizers)-获取并行内部手势事件中的冲突的手势识别器。[int32_t OH_ArkUI_SetArkUIGestureRecognizerDisposeNotify(ArkUI_GestureRecognizer* recognizer,ArkUI_GestureRecognizerDisposeNotifyCallback callback, void* userData)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_setarkuigesturerecognizerdisposenotify)-设置手势识别器对象析构通知回调函数。[int32_t OH_ArkUI_GetGestureParam_DirectMask(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureDirectionMask* directMask)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgestureparam_directmask)-获取手势识别器的滑动方向。[int32_t OH_ArkUI_GetGestureParam_FingerCount(ArkUI_GestureRecognizer* recognizer, int* finger)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgestureparam_fingercount)-获取手势识别器的手指数。[int32_t OH_ArkUI_GetGestureParam_limitFingerCount(ArkUI_GestureRecognizer* recognizer, bool* isLimited)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgestureparam_limitfingercount)-获取手势识别器是否有手指数限制。[int32_t OH_ArkUI_GetGestureParam_repeat(ArkUI_GestureRecognizer* recognizer, bool* isRepeat)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgestureparam_repeat)-获取手势识别器是否连续触发事件回调。[int32_t OH_ArkUI_GetGestureParam_distance(ArkUI_GestureRecognizer* recognizer, double* distance)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgestureparam_distance)-获取手势识别器的手指允许的移动距离范围。[int32_t OH_ArkUI_GetGestureParam_speed(ArkUI_GestureRecognizer* recognizer, double* speed)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgestureparam_speed)-获取手势识别器的识别滑动的最小速度。[int32_t OH_ArkUI_GetGestureParam_duration(ArkUI_GestureRecognizer* recognizer, int* duration)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgestureparam_duration)-获取手势识别器的触发长按的最短时间。[int32_t OH_ArkUI_GetGestureParam_angle(ArkUI_GestureRecognizer* recognizer, double* angle)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgestureparam_angle)-获取手势识别器的旋转手势的最小改变度数。[int32_t OH_ArkUI_GetGestureParam_distanceThreshold(ArkUI_GestureRecognizer* recognizer, double* distanceThreshold)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_getgestureparam_distancethreshold)-获取手势识别器的手势移动阈值。[ArkUI_ErrorCode OH_ArkUI_PanGesture_SetDistanceMap(ArkUI_GestureRecognizer* recognizer, int size, int* toolTypeArray, double* distanceArray)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_pangesture_setdistancemap)-设置手势最小滑动阈值表。当设备类型为非法值时，设置不生效。[ArkUI_ErrorCode OH_ArkUI_PanGesture_GetDistanceByToolType(ArkUI_GestureRecognizer* recognizer, int toolType, double* distance)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_pangesture_getdistancebytooltype)-获取手势识别器的手势移动阈值表。仅支持对通过OH_ArkUI_PanGesture_SetDistanceMap修改过的设备类型的阈值查询。默认滑动阈值可通过查询UI_INPUT_EVENT_TOOL_TYPE_UNKNOWN类型获得，其他未设置过的类型不会返回。[ArkUI_ErrorCode OH_ArkUI_SetTouchTestDoneCallback(ArkUI_NodeHandle node,void* userData,void (*touchTestDone)(ArkUI_GestureEvent* event,ArkUI_GestureRecognizerHandleArray recognizers,int32_t count,void* userData))](#ZH-CN_TOPIC_0000002497605076__oh_arkui_settouchtestdonecallback)-注册一个在所有手势识别器收集完成后执行的回调函数。当用户开始触摸屏幕时，系统会进行命中测试并根据触摸位置收集手势识别器。随后，在处理任何移动事件之前，组件可以使用此接口确定将参与识别并相互竞争的手势识别器。[void* OH_ArkUI_GestureInterrupter_GetUserData(ArkUI_GestureInterruptInfo* event)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_gestureinterrupter_getuserdata)-获取手势中断事件中的用户自定义数据。[ArkUI_ErrorCode OH_ArkUI_PreventGestureRecognizerBegin(ArkUI_GestureRecognizer* recognizer)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_preventgesturerecognizerbegin)-在手指全部抬起前阻止手势识别器参与当前手势识别。如果系统已确定该手势识别器的结果（无论成功与否），调用此接口将无效。[ArkUI_ErrorCode OH_ArkUI_LongPressGesture_SetAllowableMovement(ArkUI_GestureRecognizer* recognizer, int32_t allowableMovement)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_longpressgesture_setallowablemovement)-设置长按手势识别器识别的手势的最大移动距离。[int32_t OH_ArkUI_LongPressGesture_GetAllowableMovement(ArkUI_GestureRecognizer* recognizer, int32_t* allowableMovement)](#ZH-CN_TOPIC_0000002497605076__oh_arkui_longpressgesture_getallowablemovement)-获取长按手势识别器识别的手势的最大移动距离。

#### 变量

名称typedef关键字描述uint32_tArkUI_GestureDirectionMask

定义滑动手势方向集合。

例：ArkUI_GestureDirectionMask directions = GESTURE_DIRECTION_LEFT | GESTURE_DIRECTION_RIGHT。

directions 表明支持左右水平方向。

uint32_tArkUI_GestureEventActionTypeMask定义手势事件类型集合。例：ArkUI_GestureEventActionTypeMask actions = GESTURE_EVENT_ACTION_ACCEPT | GESTURE_EVENT_ACTION_UPDATE;

#### 枚举类型说明

#### ArkUI_GestureEventActionType

```ets
enum ArkUI_GestureEventActionType
```

**描述：**

定义手势事件类型。

**起始版本：** 12

枚举项描述GESTURE_EVENT_ACTION_ACCEPT = 0x01手势事件触发。GESTURE_EVENT_ACTION_UPDATE = 0x02手势事件更新。GESTURE_EVENT_ACTION_END = 0x04手势事件结束。GESTURE_EVENT_ACTION_CANCEL = 0x08手势事件取消。

#### ArkUI_GesturePriority

```ets
enum ArkUI_GesturePriority
```

**描述：**

定义手势事件模式。

**起始版本：** 12

枚举项描述NORMAL = 0正常手势。PRIORITY = 1高优先级手势。PARALLEL = 2并发手势。

#### ArkUI_GroupGestureMode

```ets
enum ArkUI_GroupGestureMode
```

**描述：**

定义手势组事件模式。

**起始版本：** 12

枚举项描述SEQUENTIAL_GROUP = 0顺序手势模式，按照注册顺序识别手势，直到所有手势识别成功。若有识别失败，后续识别均失败。仅有最后一个手势响应结束事件。PARALLEL_GROUP = 1并发手势模式，注册的手势同时识别，直到所有手势识别结束，手势识别互相不影响。EXCLUSIVE_GROUP = 2互斥手势模式，注册的手势同时识别，若有一个手势识别成功，则结束手势识别。

#### ArkUI_GestureDirection

```ets
enum ArkUI_GestureDirection
```

**描述：**

定义滑动手势方向。

**起始版本：** 12

枚举项描述GESTURE_DIRECTION_ALL = 0b1111所有方向。GESTURE_DIRECTION_HORIZONTAL = 0b0011水平方向。GESTURE_DIRECTION_VERTICAL = 0b1100竖直方向。GESTURE_DIRECTION_LEFT = 0b0001向左方向。GESTURE_DIRECTION_RIGHT = 0b0010向右方向。GESTURE_DIRECTION_UP = 0b0100向上方向。GESTURE_DIRECTION_DOWN = 0b1000向下方向。GESTURE_DIRECTION_NONE = 0任何方向都不触发手势事件。

#### ArkUI_GestureMask

```ets
enum ArkUI_GestureMask
```

**描述：**

定义手势屏蔽模式。

**起始版本：** 12

枚举项描述NORMAL_GESTURE_MASK = 0不屏蔽子组件的手势，按照默认手势识别顺序进行识别。IGNORE_INTERNAL_GESTURE_MASK屏蔽子组件的手势，包括子组件上系统内置的手势。

#### ArkUI_GestureRecognizerType

```ets
enum ArkUI_GestureRecognizerType
```

**描述：**

定义手势类型。

**起始版本：** 12

枚举项描述TAP_GESTURE = 0敲击手势。LONG_PRESS_GESTURE = 1长按手势。PAN_GESTURE = 2滑动手势。PINCH_GESTURE = 3捏合手势。ROTATION_GESTURE = 4旋转手势。SWIPE_GESTURE = 5快滑手势。GROUP_GESTURE = 6手势组合。CLICK_GESTURE = 7

通过onClick注册的点击手势。

**起始版本：** 20

DRAG_DROP = 8

用于拖放的拖拽手势。

**起始版本：** 20

#### ArkUI_GestureInterruptResult

```ets
enum ArkUI_GestureInterruptResult
```

**描述：**

定义手势打断结果。

**起始版本：** 12

枚举项描述GESTURE_INTERRUPT_RESULT_CONTINUE = 0手势继续。GESTURE_INTERRUPT_RESULT_REJECT = 1手势打断。

#### ArkUI_GestureRecognizerState

```ets
enum ArkUI_GestureRecognizerState
```

**描述：**

定义手势识别器状态。

**起始版本：** 12

枚举项描述ARKUI_GESTURE_RECOGNIZER_STATE_READY = 0准备状态。ARKUI_GESTURE_RECOGNIZER_STATE_DETECTING = 1检测状态。ARKUI_GESTURE_RECOGNIZER_STATE_PENDING = 2等待状态。ARKUI_GESTURE_RECOGNIZER_STATE_BLOCKED = 3阻塞状态。ARKUI_GESTURE_RECOGNIZER_STATE_SUCCESSFUL = 4成功状态。ARKUI_GESTURE_RECOGNIZER_STATE_FAILED = 5失败状态。

#### 函数说明

#### ArkUI_GestureRecognizerDisposeNotifyCallback()

```ets
typedef void (*ArkUI_GestureRecognizerDisposeNotifyCallback)(ArkUI_GestureRecognizer* recognizer, void* userData)
```

**描述：**

定义手势识别器析构通知事件的回调函数类型。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。void* userData用户自定义数据。

#### OH_ArkUI_GestureInterruptInfo_GetSystemFlag()

```ets
bool OH_ArkUI_GestureInterruptInfo_GetSystemFlag(const ArkUI_GestureInterruptInfo* event)
```

**描述：**

判断是否组件内置手势。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureInterruptInfo](../../topics/input/ArkUI_GestureInterruptInfo.md)* event手势打断回调事件。

**返回：**

类型说明bool

true: 系统内置手势；

 false: 非系统内置手势。

#### OH_ArkUI_GestureInterruptInfo_GetRecognizer()

```ets
ArkUI_GestureRecognizer* OH_ArkUI_GestureInterruptInfo_GetRecognizer(const ArkUI_GestureInterruptInfo* event)
```

**描述：**

返回被打断的手势指针。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureInterruptInfo](../../topics/input/ArkUI_GestureInterruptInfo.md)* event手势打断回调事件。

**返回：**

类型说明[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)*被打断的手势指针。

#### OH_ArkUI_GestureInterruptInfo_GetGestureEvent()

```ets
ArkUI_GestureEvent* OH_ArkUI_GestureInterruptInfo_GetGestureEvent(const ArkUI_GestureInterruptInfo* event)
```

**描述：**

返回打断的手势事件数据。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureInterruptInfo](../../topics/input/ArkUI_GestureInterruptInfo.md)* event手势打断回调事件。

**返回：**

类型说明[ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)*打断的手势事件数据。

#### OH_ArkUI_GestureInterruptInfo_GetSystemRecognizerType()

```ets
int32_t OH_ArkUI_GestureInterruptInfo_GetSystemRecognizerType(const ArkUI_GestureInterruptInfo* event)
```

**描述：**

当要触发的是系统内部手势时，使用该方法可返回该系统内部手势的类型。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureInterruptInfo](../../topics/input/ArkUI_GestureInterruptInfo.md)* event手势打断回调事件。

**返回：**

类型说明int32_t要触发的内部手势对应的手势类型，如果当前触发的手势不是系统内部手势，则返回 -1。

#### OH_ArkUI_GestureInterruptInfo_GetTouchRecognizers()

```ets
int32_t OH_ArkUI_GestureInterruptInfo_GetTouchRecognizers(const ArkUI_GestureInterruptInfo* info,ArkUI_TouchRecognizerHandleArray* recognizers, int32_t* size)
```

**描述：**

从手势打断信息中获取触摸识别器。

**起始版本：** 15

**参数：**

参数项描述[const ArkUI_GestureInterruptInfo](../../topics/input/ArkUI_GestureInterruptInfo.md)* info指向手势打断信息的指针。[ArkUI_TouchRecognizerHandleArray](../../topics/input/ArkUI_TouchRecognizerHandle_.md)* recognizers指向触摸识别器数组的指针。int32_t* size触摸识别器数组的大小。

**返回：**

类型说明int32_t

返回 [ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 表示成功。

 返回 [ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 表示参数错误。

#### OH_ArkUI_TouchRecognizer_GetNodeHandle()

```ets
ArkUI_NodeHandle OH_ArkUI_TouchRecognizer_GetNodeHandle(const ArkUI_TouchRecognizerHandle recognizer)
```

**描述：**

获取触摸识别器对应的组件句柄。

**起始版本：** 15

**参数：**

参数项描述const [ArkUI_TouchRecognizerHandle](../../topics/input/ArkUI_TouchRecognizerHandle_.md) recognizer触摸识别器的句柄。

**返回：**

类型说明[ArkUI_NodeHandle](../../topics/components/ArkUI_Node_.md)触摸识别器对应的组件句柄。

#### OH_ArkUI_TouchRecognizer_CancelTouch()

```ets
int32_t OH_ArkUI_TouchRecognizer_CancelTouch(ArkUI_TouchRecognizerHandle recognizer, ArkUI_GestureInterruptInfo* info)
```

**描述：**

在手势打断回调中向指定的触摸识别器发送取消触摸的事件

**起始版本：** 15

**参数：**

参数项描述[ArkUI_TouchRecognizerHandle](../../topics/input/ArkUI_TouchRecognizerHandle_.md) recognizer触摸识别器的句柄。[ArkUI_GestureInterruptInfo](../../topics/input/ArkUI_GestureInterruptInfo.md)* info指向手势打断信息的指针。

**返回：**

类型说明int32_t

Returns [ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

 Returns [ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数错误。

#### OH_ArkUI_GestureEvent_GetActionType()

```ets
ArkUI_GestureEventActionType OH_ArkUI_GestureEvent_GetActionType(const ArkUI_GestureEvent* event)
```

**描述：**

返回手势事件类型。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明[ArkUI_GestureEventActionType](native_gesture.h.md#ZH-CN_TOPIC_0000002497605076__arkui_gestureeventactiontype)手势事件类型。

#### OH_ArkUI_GestureEvent_GetRawInputEvent()

```ets
const ArkUI_UIInputEvent* OH_ArkUI_GestureEvent_GetRawInputEvent(const ArkUI_GestureEvent* event)
```

**描述：**

返回手势输入。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明const [ArkUI_UIInputEvent](../../topics/input/ArkUI_UIInputEvent.md)*手势事件的原始输入事件。

#### OH_ArkUI_LongPress_GetRepeatCount()

```ets
int32_t OH_ArkUI_LongPress_GetRepeatCount(const ArkUI_GestureEvent* event)
```

**描述：**

返回是否为重复触发事件。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明int32_t是否为重复触发事件。1表示为重复触发事件，0表示为非重复触发事件。

#### OH_ArkUI_PanGesture_GetVelocity()

```ets
float OH_ArkUI_PanGesture_GetVelocity(const ArkUI_GestureEvent* event)
```

**描述：**

滑动手势返回手势主方向速度。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float当前手势主方向速度，为xy轴方向速度的平方和的算数平方根，单位px/秒。

#### OH_ArkUI_PanGesture_GetVelocityX()

```ets
float OH_ArkUI_PanGesture_GetVelocityX(const ArkUI_GestureEvent* event)
```

**描述：**

滑动手势返回当前手势的x轴方向速度。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float当前手势的x轴方向速度，单位px/秒。

#### OH_ArkUI_PanGesture_GetVelocityY()

```ets
float OH_ArkUI_PanGesture_GetVelocityY(const ArkUI_GestureEvent* event)
```

**描述：**

滑动手势返回当前手势的y轴方向速度。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float当前手势的y轴方向速度，单位px/秒。

#### OH_ArkUI_PanGesture_GetOffsetX()

```ets
float OH_ArkUI_PanGesture_GetOffsetX(const ArkUI_GestureEvent* event)
```

**描述：**

滑动手势返回当前手势事件x轴相对偏移量。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float当前手势事件x轴相对偏移量，单位为px。

#### OH_ArkUI_PanGesture_GetOffsetY()

```ets
float OH_ArkUI_PanGesture_GetOffsetY(const ArkUI_GestureEvent* event)
```

**描述：**

滑动手势返回当前手势事件y轴相对偏移量。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float当前手势事件y轴相对偏移量，单位为px。

#### OH_ArkUI_SwipeGesture_GetAngle()

```ets
float OH_ArkUI_SwipeGesture_GetAngle(const ArkUI_GestureEvent* event)
```

**描述：**

快滑手势返回当前手势事件角度信息。角度计算方式：快滑手势被识别到后，连接两根手指之间的线被识别为起始线条，随着手指的滑动，手指之间的线条会发生旋转，

 根据起始线条两端点和当前线条两端点的坐标，使用反正切函数分别计算其相对于水平方向的夹角，

 最后arctan2(cy2-cy1,cx2-cx1)-arctan2(y2-y1,x2-x1)为旋转的角度。

 以起始线条为坐标系，顺时针旋转为0到180度，逆时针旋转为-180到0度。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float快滑手势的角度，即两根手指间的线段与水平方向的夹角变化的度数。单位为deg。

#### OH_ArkUI_SwipeGesture_GetVelocity()

```ets
float OH_ArkUI_SwipeGesture_GetVelocity(const ArkUI_GestureEvent* event)
```

**描述：**

快滑手势场景中所有手指滑动平均速度。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float快滑手势速度，即所有手指滑动的平均速度，单位为px/秒。

#### OH_ArkUI_RotationGesture_GetAngle()

```ets
float OH_ArkUI_RotationGesture_GetAngle(const ArkUI_GestureEvent* event)
```

**描述：**

旋转手势返回当前手势事件角度信息。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float旋转角度。单位为deg。

#### OH_ArkUI_PinchGesture_GetScale()

```ets
float OH_ArkUI_PinchGesture_GetScale(const ArkUI_GestureEvent* event)
```

**描述：**

捏合手势返回当前手势事件缩放信息。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float缩放比例。

#### OH_ArkUI_PinchGesture_GetCenterX()

```ets
float OH_ArkUI_PinchGesture_GetCenterX(const ArkUI_GestureEvent* event)
```

**描述：**

捏合手势中心点相对于当前组件元素左上角x轴坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float捏合手势中心点相对于当前组件元素左上角x轴坐标，单位为px。

#### OH_ArkUI_PinchGesture_GetCenterY()

```ets
float OH_ArkUI_PinchGesture_GetCenterY(const ArkUI_GestureEvent* event)
```

**描述：**

捏合手势中心点相对于当前组件元素左上角y轴坐标。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明float捏合手势中心点相对于当前组件元素左上角y轴坐标，单位为px。

#### OH_ArkUI_GestureEvent_GetNode()

```ets
ArkUI_NodeHandle OH_ArkUI_GestureEvent_GetNode(const ArkUI_GestureEvent* event)
```

**描述：**

获取绑定该手势的ARKUI组件

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureEvent](../../topics/input/ArkUI_GestureEvent.md)* event手势事件。

**返回：**

类型说明[ArkUI_NodeHandle](../../topics/components/ArkUI_Node_.md)绑定该手势的ARKUI组件。若返回Null，则表示event是无效值。

#### OH_ArkUI_GetResponseRecognizersFromInterruptInfo()

```ets
int32_t OH_ArkUI_GetResponseRecognizersFromInterruptInfo(const ArkUI_GestureInterruptInfo* event,ArkUI_GestureRecognizerHandleArray* responseChain, int32_t* count)
```

**描述：**

获取手势响应链的信息。

**起始版本：** 12

**参数：**

参数项描述[const ArkUI_GestureInterruptInfo](../../topics/input/ArkUI_GestureInterruptInfo.md)* event手势打断回调事件。ArkUI_GestureRecognizerHandleArray* responseChain响应链组件上的手势识别器。int32_t* count响应链组件上的手势识别器的数量。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

#### OH_ArkUI_SetGestureRecognizerEnabled()

```ets
int32_t OH_ArkUI_SetGestureRecognizerEnabled(ArkUI_GestureRecognizer* recognizer, bool enabled)
```

**描述：**

设置手势识别器的使能状态。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。bool enabled使能状态。true表示使能，false表示无法使能。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

#### OH_ArkUI_SetGestureRecognizerLimitFingerCount()

```ets
int32_t OH_ArkUI_SetGestureRecognizerLimitFingerCount(ArkUI_GestureRecognizer* recognizer, bool limitFingerCount)
```

**描述：**

设置是否严格检查触摸手指数量的标志。实际触摸手指数量不等于设置的手指数量的时候，该手势识别不成功。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。bool limitFingerCount表示严格检查触摸手指数量的状态。true表示检查手指数量，false表示不检查手指数量。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

#### OH_ArkUI_GetGestureRecognizerEnabled()

```ets
bool OH_ArkUI_GetGestureRecognizerEnabled(ArkUI_GestureRecognizer* recognizer)
```

**描述：**

获取手势识别器的使能状态。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。

**返回：**

类型说明bool

true - 使能。

 false - 禁用。

#### OH_ArkUI_GetGestureRecognizerState()

```ets
int32_t OH_ArkUI_GetGestureRecognizerState(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureRecognizerState* state)
```

**描述：**

获取手势识别器的状态。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。[ArkUI_GestureRecognizerState](native_gesture.h.md#ZH-CN_TOPIC_0000002497605076__arkui_gesturerecognizerstate)* state手势识别器的状态。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

#### OH_ArkUI_GetGestureEventTargetInfo()

```ets
int32_t OH_ArkUI_GetGestureEventTargetInfo(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureEventTargetInfo** info)
```

**描述：**

获取手势事件目标信息。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。[ArkUI_GestureEventTargetInfo](../../topics/input/ArkUI_GestureEventTargetInfo.md)** info手势事件目标信息。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

#### OH_ArkUI_GestureEventTargetInfo_IsScrollBegin()

```ets
int32_t OH_ArkUI_GestureEventTargetInfo_IsScrollBegin(ArkUI_GestureEventTargetInfo* info, bool* ret)
```

**描述：**

当前滚动类容器组件是否在顶部。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureEventTargetInfo](../../topics/input/ArkUI_GestureEventTargetInfo.md)* info手势事件目标信息。bool* ret当前滚动类容器组件是否在顶部。true表示在顶部，false表示不在顶部。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

[ARKUI_ERROR_CODE_NON_SCROLLABLE_CONTAINER](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 非滚动类容器。

#### OH_ArkUI_GestureEventTargetInfo_IsScrollEnd()

```ets
int32_t OH_ArkUI_GestureEventTargetInfo_IsScrollEnd(ArkUI_GestureEventTargetInfo* info, bool* ret)
```

**描述：**

当前滚动类容器组件是否在底部。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureEventTargetInfo](../../topics/input/ArkUI_GestureEventTargetInfo.md)* info手势事件目标信息。bool* ret当前滚动类容器组件是否在底部。true表示在底部，false表示不在底部。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

[ARKUI_ERROR_CODE_NON_SCROLLABLE_CONTAINER](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 非滚动类容器。

#### OH_ArkUI_GetPanGestureDirectionMask()

```ets
int32_t OH_ArkUI_GetPanGestureDirectionMask(ArkUI_GestureRecognizer* recognizer,ArkUI_GestureDirectionMask* directionMask)
```

**描述：**

获取滑动手势的滑动方向。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。[ArkUI_GestureDirectionMask](#ZH-CN_TOPIC_0000002497605076__变量)* directionMask滑动手势的滑动方向。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

#### OH_ArkUI_IsBuiltInGesture()

```ets
bool OH_ArkUI_IsBuiltInGesture(ArkUI_GestureRecognizer* recognizer)
```

**描述：**

当前手势是否为系统内置手势。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。

**返回：**

类型说明bool

true - 是系统内置手势。

 false - 不是系统内置手势。

#### OH_ArkUI_GetGestureTag()

```ets
int32_t OH_ArkUI_GetGestureTag(ArkUI_GestureRecognizer* recognizer, char* buffer, int32_t bufferSize, int32_t* result)
```

**描述：**

获取手势识别器的标记。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。char* buffer存储区。int32_t bufferSize存储区大小。int32_t* result拷贝的字符串长度。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

[ARKUI_ERROR_CODE_BUFFER_SIZE_NOT_ENOUGH](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 存储区大小不足。

#### OH_ArkUI_GetGestureBindNodeId()

```ets
int32_t OH_ArkUI_GetGestureBindNodeId(ArkUI_GestureRecognizer* recognizer, char* nodeId, int32_t size,int32_t* result)
```

**描述：**

获取手势识别器绑定的组件的ID。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。char* nodeId组件的ID。int32_t size存储区大小。int32_t* result拷贝的字符串长度。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

[ARKUI_ERROR_CODE_BUFFER_SIZE_NOT_ENOUGH](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 存储区大小不足。

#### OH_ArkUI_IsGestureRecognizerValid()

```ets
bool OH_ArkUI_IsGestureRecognizerValid(ArkUI_GestureRecognizer* recognizer)
```

**描述：**

当前手势识别器是否有效。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。

**返回：**

类型说明bool

true - 手势识别器有效。

 false - 手势识别器无效。

#### OH_ArkUI_ParallelInnerGestureEvent_GetUserData()

```ets
void* OH_ArkUI_ParallelInnerGestureEvent_GetUserData(ArkUI_ParallelInnerGestureEvent* event)
```

**描述：**

获取并行内部手势事件中的用户自定义数据。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_ParallelInnerGestureEvent](../../topics/input/ArkUI_ParallelInnerGestureEvent.md)* event并行内部手势事件。

**返回：**

类型说明void*用户自定义数据的指针。

#### OH_ArkUI_ParallelInnerGestureEvent_GetCurrentRecognizer()

```ets
ArkUI_GestureRecognizer* OH_ArkUI_ParallelInnerGestureEvent_GetCurrentRecognizer(ArkUI_ParallelInnerGestureEvent* event)
```

**描述：**

获取并行内部手势事件中的当前手势识别器。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_ParallelInnerGestureEvent](../../topics/input/ArkUI_ParallelInnerGestureEvent.md)* event并行内部手势事件。

**返回：**

类型说明[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)*当前手势识别器的指针。

#### OH_ArkUI_ParallelInnerGestureEvent_GetConflictRecognizers()

```ets
int32_t OH_ArkUI_ParallelInnerGestureEvent_GetConflictRecognizers(ArkUI_ParallelInnerGestureEvent* event,ArkUI_GestureRecognizerHandleArray* array, int32_t* size)
```

**描述：**

获取并行内部手势事件中的冲突的手势识别器。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_ParallelInnerGestureEvent](../../topics/input/ArkUI_ParallelInnerGestureEvent.md)* event并行内部手势事件。[ArkUI_GestureRecognizerHandleArray](../../topics/input/ArkUI_GestureRecognizerHandle_.md)* array冲突的手势识别器数组。int32_t* size冲突的手势识别器数组的大小。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

#### OH_ArkUI_SetArkUIGestureRecognizerDisposeNotify()

```ets
int32_t OH_ArkUI_SetArkUIGestureRecognizerDisposeNotify(ArkUI_GestureRecognizer* recognizer,ArkUI_GestureRecognizerDisposeNotifyCallback callback, void* userData)
```

**描述：**

设置手势识别器对象析构通知回调函数。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。[ArkUI_GestureRecognizerDisposeNotifyCallback](native_gesture.h.md#ZH-CN_TOPIC_0000002497605076__arkui_gesturerecognizerdisposenotifycallback) callback手势识别器对象析构通知回调函数。void* userData用户自定义数据。

**返回：**

类型说明int32_t

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) - 参数错误。

#### OH_ArkUI_GetGestureParam_DirectMask()

```ets
int32_t OH_ArkUI_GetGestureParam_DirectMask(ArkUI_GestureRecognizer* recognizer, ArkUI_GestureDirectionMask* directMask)
```

**描述：**

获取手势识别器的滑动方向。

**起始版本：** 18

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。[ArkUI_GestureDirectionMask](#ZH-CN_TOPIC_0000002497605076__变量)* directMask手势识别器的滑动方向。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数错误。

#### OH_ArkUI_GetGestureParam_FingerCount()

```ets
int32_t OH_ArkUI_GetGestureParam_FingerCount(ArkUI_GestureRecognizer* recognizer, int* finger)
```

**描述：**

获取手势识别器的手指数。

**起始版本：** 18

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。int* finger手势识别器的手指数。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数错误。

#### OH_ArkUI_GetGestureParam_limitFingerCount()

```ets
int32_t OH_ArkUI_GetGestureParam_limitFingerCount(ArkUI_GestureRecognizer* recognizer, bool* isLimited)
```

**描述：**

获取手势识别器是否有手指数限制。

**起始版本：** 18

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。bool* isLimited手势识别器是否有手指数限制。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数错误。

#### OH_ArkUI_GetGestureParam_repeat()

```ets
int32_t OH_ArkUI_GetGestureParam_repeat(ArkUI_GestureRecognizer* recognizer, bool* isRepeat)
```

**描述：**

获取手势识别器是否连续触发事件回调。

**起始版本：** 18

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。bool* isRepeat手势识别器是否连续触发事件回调。true表示连续触发，false表示不连续触发。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 不支持手势识别器类型。

#### OH_ArkUI_GetGestureParam_distance()

```ets
int32_t OH_ArkUI_GetGestureParam_distance(ArkUI_GestureRecognizer* recognizer, double* distance)
```

**描述：**

获取手势识别器的手指允许的移动距离范围。

**起始版本：** 18

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。double* distance手势识别器的手指允许的移动距离范围。单位为px。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 不支持手势识别器类型。

#### OH_ArkUI_GetGestureParam_speed()

```ets
int32_t OH_ArkUI_GetGestureParam_speed(ArkUI_GestureRecognizer* recognizer, double* speed)
```

**描述：**

获取手势识别器的识别滑动的最小速度。

**起始版本：** 18

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。double* speed手势识别器的识别滑动的最小速度。单位为px/s。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 不支持手势识别器类型。

#### OH_ArkUI_GetGestureParam_duration()

```ets
int32_t OH_ArkUI_GetGestureParam_duration(ArkUI_GestureRecognizer* recognizer, int* duration)
```

**描述：**

获取手势识别器的触发长按的最短时间。

**起始版本：** 18

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。int* duration手势识别器的触发长按的最短时间。单位为ms。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 不支持手势识别器类型。

#### OH_ArkUI_GetGestureParam_angle()

```ets
int32_t OH_ArkUI_GetGestureParam_angle(ArkUI_GestureRecognizer* recognizer, double* angle)
```

**描述：**

获取手势识别器的旋转手势的最小改变度数。

**起始版本：** 18

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。double* angle手势识别器的旋转手势的最小改变度数。单位为deg。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 不支持手势识别器类型。

#### OH_ArkUI_GetGestureParam_distanceThreshold()

```ets
int32_t OH_ArkUI_GetGestureParam_distanceThreshold(ArkUI_GestureRecognizer* recognizer, double* distanceThreshold)
```

**描述：**

获取手势识别器的手势移动阈值。

**起始版本：** 18

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。double* distanceThreshold手势识别器的手势移动阈值。单位：px。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 不支持手势识别器类型。

#### OH_ArkUI_PanGesture_SetDistanceMap()

```ets
ArkUI_ErrorCode OH_ArkUI_PanGesture_SetDistanceMap(ArkUI_GestureRecognizer* recognizer, int size, int* toolTypeArray, double* distanceArray)
```

**描述：**

设置手势最小滑动阈值表。当设备类型为非法值时，设置不生效。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。int size手势最小滑动阈值数组的大小。int* toolTypeArray指向输入事件的工具类型数组的指针。double* distanceArray指向最小滑动阈值数组的指针。单位为px。

**返回：**

类型说明[ArkUI_ErrorCode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)

错误码。

 Returns [ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

 Returns [ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数错误。

 Returns [ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 不支持手势识别器类型。

#### OH_ArkUI_PanGesture_GetDistanceByToolType()

```ets
ArkUI_ErrorCode OH_ArkUI_PanGesture_GetDistanceByToolType(ArkUI_GestureRecognizer* recognizer, int toolType, double* distance)
```

**描述：**

获取手势识别器的手势移动阈值表。仅支持对通过OH_ArkUI_PanGesture_SetDistanceMap修改过的设备类型的阈值查询。默认滑动阈值可通过查询UI_INPUT_EVENT_TOOL_TYPE_UNKNOWN类型获得，其他未设置过的类型不会返回。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。int toolType输入事件的工具类型。double* distance手势识别器的手势移动阈值。单位为px。

**返回：**

类型说明[ArkUI_ErrorCode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)

错误码。

 Returns [ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

 Returns [ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数错误。

 Returns [ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 不支持手势识别器类型。

#### OH_ArkUI_SetTouchTestDoneCallback()

```ets
ArkUI_ErrorCode OH_ArkUI_SetTouchTestDoneCallback(ArkUI_NodeHandle node,void* userData,void (*touchTestDone)(ArkUI_GestureEvent* event,ArkUI_GestureRecognizerHandleArray recognizers,int32_t count,void* userData)
)
```

**描述：**

注册一个在所有手势识别器收集完成后执行的回调函数。当用户开始触摸屏幕时，系统会进行命中测试并根据触摸位置收集手势识别器。随后，在处理任何移动事件之前，组件可以使用此接口确定将参与识别并相互竞争的手势识别器。

**起始版本：** 20

**参数：**

参数项描述[ArkUI_NodeHandle](../../topics/components/ArkUI_Node_.md) node需要设置手势收集完成回调的节点句柄。void* userData用户自定义数据。touchTestDone手势收集完成的回调函数。- event：手势的基本信息。- recognizers：手势识别器数组。- count：手势识别器个数。

**返回：**

类型说明[ArkUI_ErrorCode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)

错误码。

 Returns [ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

 Returns [ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数错误。

#### OH_ArkUI_GestureInterrupter_GetUserData()

```ets
void* OH_ArkUI_GestureInterrupter_GetUserData(ArkUI_GestureInterruptInfo* event)
```

**描述：**

获取手势中断事件中的用户自定义数据。

**起始版本：** 18

**参数：**

参数项描述[ArkUI_GestureInterruptInfo](../../topics/input/ArkUI_GestureInterruptInfo.md)* event是指向手势中断信息的指针。

**返回：**

类型说明void*返回指向用户自定义数据的指针。

#### OH_ArkUI_PreventGestureRecognizerBegin()

```ets
ArkUI_ErrorCode OH_ArkUI_PreventGestureRecognizerBegin(ArkUI_GestureRecognizer* recognizer)
```

**描述：**

在手指全部抬起前阻止手势识别器参与当前手势识别。如果系统已确定该手势识别器的结果（无论成功与否），调用此接口将无效。

**起始版本：** 20

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。

**返回：**

类型说明[ArkUI_ErrorCode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)

错误码。

 Returns [ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

 Returns [ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数错误。

#### OH_ArkUI_LongPressGesture_SetAllowableMovement()

```ets
ArkUI_ErrorCode OH_ArkUI_LongPressGesture_SetAllowableMovement(ArkUI_GestureRecognizer* recognizer, int32_t allowableMovement)
```

**描述：**

设置长按手势识别器识别的手势的最大移动距离。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。int32_t allowableMovement

长按手势识别器识别的手势的最大移动距离。

单位为px。

取值范围：(0, +∞)，设置小于等于0时，按照默认值15处理。

**返回：**

类型说明[ArkUI_ErrorCode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 参数错误。

[ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 不支持手势识别器类型。

#### OH_ArkUI_LongPressGesture_GetAllowableMovement()

```ets
int32_t OH_ArkUI_LongPressGesture_GetAllowableMovement(ArkUI_GestureRecognizer* recognizer, int32_t* allowableMovement)
```

**描述：**

获取长按手势识别器识别的手势的最大移动距离。

**起始版本：** 22

**参数：**

参数项描述[ArkUI_GestureRecognizer](../../topics/input/ArkUI_GestureRecognizer.md)* recognizer手势识别器指针。int32_t* allowableMovement指向长按手势识别器识别的手势的最大移动距离的指针。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_RECOGNIZER_TYPE_NOT_SUPPORTED](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 不支持手势识别器类型。