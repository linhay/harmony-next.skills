# native_dialog.h

#### 概述

提供ArkUI在Native侧的自定义弹窗接口定义集合。

**引用文件：** <arkui/native_dialog.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**相关模块：**[ArkUI_NativeModule](ArkUI_NativeModule.md)

**相关示例：**[NativeDialogSample](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/NativeDialogSample)

#### 汇总

#### 结构体

名称typedef关键字描述[ArkUI_NativeDialogAPI_1](ArkUI_NativeDialogAPI_1.md)ArkUI_NativeDialogAPI_1ArkUI提供的Native侧自定义弹窗接口集合。[ArkUI_NativeDialogAPI_2](ArkUI_NativeDialogAPI_2.md)ArkUI_NativeDialogAPI_2ArkUI提供的Native侧自定义弹窗接口集合。[ArkUI_NativeDialogAPI_3](ArkUI_NativeDialogAPI_3.md)ArkUI_NativeDialogAPI_3ArkUI提供的Native侧自定义弹窗接口集合。[ArkUI_DialogDismissEvent](ArkUI_DialogDismissEvent.md)ArkUI_DialogDismissEvent定义弹窗关闭事件对象。[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)ArkUI_CustomDialogOptions定义自定义弹窗的内容对象。

#### 枚举

名称typedef关键字描述[ArkUI_DismissReason](#ZH-CN_TOPIC_0000002529445041__arkui_dismissreason)ArkUI_DismissReason弹窗关闭的触发方式。[ArkUI_LevelMode](#ZH-CN_TOPIC_0000002529445041__arkui_levelmode)ArkUI_LevelMode设置弹窗显示层级。[ArkUI_ImmersiveMode](#ZH-CN_TOPIC_0000002529445041__arkui_immersivemode)ArkUI_ImmersiveMode指定嵌入式弹窗的蒙层覆盖区域。[ArkUI_DialogState](#ZH-CN_TOPIC_0000002529445041__arkui_dialogstate)ArkUI_DialogState枚举对话框的状态。

#### 函数

名称typedef关键字描述[typedef bool (*ArkUI_OnWillDismissEvent)(int32_t reason)](#ZH-CN_TOPIC_0000002529445041__arkui_onwilldismissevent)ArkUI_OnWillDismissEvent弹窗关闭的回调函数。[void OH_ArkUI_DialogDismissEvent_SetShouldBlockDismiss(ArkUI_DialogDismissEvent* event, bool shouldBlockDismiss)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_dialogdismissevent_setshouldblockdismiss)-设置是否需要屏蔽系统关闭弹窗行为，true表示屏蔽系统行为不关闭弹窗，false表示不屏蔽。[void* OH_ArkUI_DialogDismissEvent_GetUserData(ArkUI_DialogDismissEvent* event)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_dialogdismissevent_getuserdata)-获取弹窗关闭事件对象中的用户自定义数据指针。[int32_t OH_ArkUI_DialogDismissEvent_GetDismissReason(ArkUI_DialogDismissEvent* event)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_dialogdismissevent_getdismissreason)-获取交互式关闭事件指针中的关闭原因。[int32_t OH_ArkUI_CustomDialog_OpenDialog(ArkUI_CustomDialogOptions* options, void (*callback)(int32_t dialogId))](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_opendialog)-弹出自定义弹窗。[int32_t OH_ArkUI_CustomDialog_UpdateDialog(ArkUI_CustomDialogOptions* options, void (*callback)(int32_t dialogId))](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_updatedialog)-更新自定义弹窗。[int32_t OH_ArkUI_CustomDialog_CloseDialog(int32_t dialogId)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_closedialog)-关闭自定义弹窗。[ArkUI_CustomDialogOptions* OH_ArkUI_CustomDialog_CreateOptions(ArkUI_NodeHandle content)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_createoptions)-创建自定义弹窗options。[void OH_ArkUI_CustomDialog_DisposeOptions(ArkUI_CustomDialogOptions* options)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_disposeoptions)-销毁自定义弹窗options.[int32_t OH_ArkUI_CustomDialog_SetLevelMode(ArkUI_CustomDialogOptions* options, ArkUI_LevelMode levelMode)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setlevelmode)-设置弹窗的显示层级。[int32_t OH_ArkUI_CustomDialog_SetLevelUniqueId(ArkUI_CustomDialogOptions* options, int32_t uniqueId)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setleveluniqueid)-设置弹窗显示层级页面下的节点id。[int32_t OH_ArkUI_CustomDialog_SetImmersiveMode(ArkUI_CustomDialogOptions* options, ArkUI_ImmersiveMode immersiveMode)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setimmersivemode)-设置嵌入式弹窗蒙层的显示区域。[int32_t OH_ArkUI_CustomDialog_SetBackgroundColor(ArkUI_CustomDialogOptions* options, uint32_t backgroundColor)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setbackgroundcolor)-设置弹窗的背景颜色。[int32_t OH_ArkUI_CustomDialog_SetCornerRadius(ArkUI_CustomDialogOptions* options, float topLeft, float topRight, float bottomLeft, float bottomRight)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setcornerradius)-设置弹窗的圆角半径。[int32_t OH_ArkUI_CustomDialog_SetBorderWidth(ArkUI_CustomDialogOptions* options, float top, float right, float bottom, float left, ArkUI_LengthMetricUnit unit)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setborderwidth)-设置弹窗的边框宽度。[int32_t OH_ArkUI_CustomDialog_SetBorderColor(ArkUI_CustomDialogOptions* options, uint32_t top, uint32_t right, uint32_t bottom, uint32_t left)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setbordercolor)-设置弹窗的边框颜色。[int32_t OH_ArkUI_CustomDialog_SetBorderStyle(ArkUI_CustomDialogOptions* options, int32_t top, int32_t right, int32_t bottom, int32_t left)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setborderstyle)-设置弹窗的边框样式。[int32_t OH_ArkUI_CustomDialog_SetWidth(ArkUI_CustomDialogOptions* options, float width, ArkUI_LengthMetricUnit unit)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setwidth)-设置弹窗的背板宽度。[int32_t OH_ArkUI_CustomDialog_SetHeight(ArkUI_CustomDialogOptions* options, float height, ArkUI_LengthMetricUnit unit)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setheight)-设置弹窗的背板高度。[int32_t OH_ArkUI_CustomDialog_SetShadow(ArkUI_CustomDialogOptions* options, ArkUI_ShadowStyle shadow)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setshadow)-设置弹窗的背板阴影。[int32_t OH_ArkUI_CustomDialog_SetCustomShadow(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* customShadow)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setcustomshadow)-设置弹窗的背板阴影。[int32_t OH_ArkUI_CustomDialog_SetBackgroundBlurStyle(ArkUI_CustomDialogOptions* options, ArkUI_BlurStyle blurStyle)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setbackgroundblurstyle)-设置弹窗的背板模糊材质。[int32_t OH_ArkUI_CustomDialog_SetAlignment(ArkUI_CustomDialogOptions* options, int32_t alignment, float offsetX, float offsetY)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setalignment)-设置弹窗的对齐模式。[int32_t OH_ArkUI_CustomDialog_SetModalMode(ArkUI_CustomDialogOptions* options, bool isModal)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setmodalmode)-设置自定义弹窗是否开启模态样式的弹窗。[int32_t OH_ArkUI_CustomDialog_SetAutoCancel(ArkUI_CustomDialogOptions* options, bool autoCancel)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setautocancel)-设置自定义弹窗是否允许点击遮罩层退出。[int32_t OH_ArkUI_CustomDialog_SetSubwindowMode(ArkUI_CustomDialogOptions* options, bool showInSubwindow)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setsubwindowmode)-设置弹窗是否在子窗口显示此弹窗。[int32_t OH_ArkUI_CustomDialog_SetMask(ArkUI_CustomDialogOptions* options, uint32_t maskColor, const ArkUI_Rect* maskRect)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setmask)-设置自定义弹窗遮罩属性。[int32_t OH_ArkUI_CustomDialog_SetKeyboardAvoidMode(ArkUI_CustomDialogOptions* options, ArkUI_KeyboardAvoidMode keyboardAvoidMode)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setkeyboardavoidmode)-设置弹窗避让键盘的模式。[int32_t OH_ArkUI_CustomDialog_SetHoverModeEnabled(ArkUI_CustomDialogOptions* options, bool enabled)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_sethovermodeenabled)-设置弹窗是否响应悬停态。[int32_t OH_ArkUI_CustomDialog_SetHoverModeArea(ArkUI_CustomDialogOptions* options, ArkUI_HoverModeAreaType hoverModeAreaType)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_sethovermodearea)-设置悬停态下弹窗默认展示区域。[int32_t OH_ArkUI_CustomDialog_RegisterOnWillDismissCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(ArkUI_DialogDismissEvent* event))](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_registeronwilldismisscallback)-注册系统关闭自定义弹窗的监听事件。[int32_t OH_ArkUI_CustomDialog_RegisterOnWillAppearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_registeronwillappearcallback)-注册自定义弹窗显示动效前的监听事件。[int32_t OH_ArkUI_CustomDialog_RegisterOnDidAppearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_registerondidappearcallback)-注册自定义弹窗弹出时的监听事件。[int32_t OH_ArkUI_CustomDialog_RegisterOnWillDisappearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_registeronwilldisappearcallback)-注册自定义弹窗退出动效前的监听事件。[int32_t OH_ArkUI_CustomDialog_RegisterOnDidDisappearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_registerondiddisappearcallback)-注册自定义弹窗消失时的监听事件。[int32_t OH_ArkUI_CustomDialog_GetState(ArkUI_NativeDialogHandle handle, ArkUI_DialogState* state)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_getstate)-获取弹窗的状态。[int32_t OH_ArkUI_CustomDialog_SetBackgroundBlurStyleOptions(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* backgroundBlurStyleOptions)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setbackgroundblurstyleoptions)-设置弹窗的背景模糊效果。[int32_t OH_ArkUI_CustomDialog_SetBackgroundEffect(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* backgroundEffect)](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_setbackgroundeffect)-设置弹窗的背景效果参数。

#### 枚举类型说明

#### ArkUI_DismissReason

```ets
enum ArkUI_DismissReason
```

**描述：**

弹窗关闭的触发方式。

**起始版本：** 12

枚举项描述DIALOG_DISMISS_BACK_PRESS = 0系统定义的返回操作、键盘ESC触发。DIALOG_DISMISS_TOUCH_OUTSIDE = 1点击遮障层触发。DIALOG_DISMISS_CLOSE_BUTTON = 2点击关闭按钮。DIALOG_DISMISS_SLIDE_DOWN = 3下拉关闭。

#### ArkUI_LevelMode

```ets
enum ArkUI_LevelMode
```

**描述：**

设置弹窗显示层级。

**起始版本：** 15

枚举项描述ARKUI_LEVEL_MODE_OVERLAY = 0显示在应用最上层。ARKUI_LEVEL_MODE_EMBEDDED = 1嵌入式显示在应用的页面内。

#### ArkUI_ImmersiveMode

```ets
enum ArkUI_ImmersiveMode
```

**描述：**

指定嵌入式弹窗的蒙层覆盖区域。

**起始版本：** 15

枚举项描述ARKUI_IMMERSIVE_MODE_DEFAULT = 0弹窗蒙层按照显示页面给定的布局约束显示。ARKUI_IMMERSIVE_MODE_EXTEND = 1弹窗蒙层可扩展至覆盖状态栏和导航条。

#### ArkUI_DialogState

```ets
enum ArkUI_DialogState
```

**描述：**

枚举对话框的状态。

**起始版本：** 20

枚举项描述DIALOG_UNINITIALIZED = 0未初始化，控制器未与dialog绑定时。DIALOG_INITIALIZED = 1已初始化，控制器与dialog绑定后。DIALOG_APPEARING = 2显示中，dialog显示动画过程中。DIALOG_APPEARED = 3已显示，dialog显示动画结束。DIALOG_DISAPPEARING = 4消失中，dialog消失动画过程中。DIALOG_DISAPPEARED = 5已消失，dialog消失动画结束后。

#### 函数说明

#### ArkUI_OnWillDismissEvent()

```ets
typedef bool (*ArkUI_OnWillDismissEvent)(int32_t reason)
```

**描述：**

弹窗关闭的回调函数。

**起始版本：** 12

**参数:**

名称描述reason触发弹窗关闭的原因。

**返回值：**

类型说明bool返回任意值都表示不关闭弹窗。

#### OH_ArkUI_DialogDismissEvent_SetShouldBlockDismiss()

```ets
void OH_ArkUI_DialogDismissEvent_SetShouldBlockDismiss(ArkUI_DialogDismissEvent* event, bool shouldBlockDismiss)
```

**描述：**

设置是否需要屏蔽系统关闭弹窗行为，true表示屏蔽系统行为不关闭弹窗，false表示不屏蔽。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DialogDismissEvent](ArkUI_DialogDismissEvent.md)* event弹窗关闭事件对象指针。bool shouldBlockDismiss实现需要屏蔽系统关闭弹窗行为。

#### OH_ArkUI_DialogDismissEvent_GetUserData()

```ets
void* OH_ArkUI_DialogDismissEvent_GetUserData(ArkUI_DialogDismissEvent* event)
```

**描述：**

获取弹窗关闭事件对象中的用户自定义数据指针。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DialogDismissEvent](ArkUI_DialogDismissEvent.md)* event弹窗关闭事件对象指针。

**返回：**

类型说明void*用户自定义数据指针。

#### OH_ArkUI_DialogDismissEvent_GetDismissReason()

```ets
int32_t OH_ArkUI_DialogDismissEvent_GetDismissReason(ArkUI_DialogDismissEvent* event)
```

**描述：**

获取交互式关闭事件指针中的关闭原因。

**起始版本：** 12

**参数：**

参数项描述[ArkUI_DialogDismissEvent](ArkUI_DialogDismissEvent.md)* event弹窗关闭事件对象指针。

**返回：**

类型说明int32_t

关闭原因，异常情况返回-1。

[DIALOG_DISMISS_BACK_PRESS](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_dismissreason) 对应点击三键back、侧滑（左滑/右滑）、键盘ESC关闭。

[DIALOG_DISMISS_TOUCH_OUTSIDE](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_dismissreason) 点击遮障层时。

[DIALOG_DISMISS_CLOSE_BUTTON](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_dismissreason) 点击关闭按钮。

[DIALOG_DISMISS_SLIDE_DOWN](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_dismissreason) 下拉关闭。

#### OH_ArkUI_CustomDialog_OpenDialog()

```ets
int32_t OH_ArkUI_CustomDialog_OpenDialog(ArkUI_CustomDialogOptions* options, void (*callback)(int32_t dialogId))
```

**描述：**

弹出自定义弹窗。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。callback开启弹窗的回调，返回入参是弹窗ID。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_UpdateDialog()

```ets
int32_t OH_ArkUI_CustomDialog_UpdateDialog(ArkUI_CustomDialogOptions* options, void (*callback)(int32_t dialogId))
```

**描述：**

更新自定义弹窗。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。callback更新弹窗的回调，返回入参是弹窗ID。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_CloseDialog()

```ets
int32_t OH_ArkUI_CustomDialog_CloseDialog(int32_t dialogId)
```

**描述：**

关闭自定义弹窗。

**起始版本：** 19

**参数：**

参数项描述int32_t dialogId需要关闭的弹窗ID。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_CreateOptions()

```ets
ArkUI_CustomDialogOptions* OH_ArkUI_CustomDialog_CreateOptions(ArkUI_NodeHandle content)
```

**描述：**

创建自定义弹窗options。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_NodeHandle](ArkUI_Node_.md) content自定义弹窗的内容。

**返回：**

类型说明[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)*自定义弹窗options的指针。

#### OH_ArkUI_CustomDialog_DisposeOptions()

```ets
void OH_ArkUI_CustomDialog_DisposeOptions(ArkUI_CustomDialogOptions* options)
```

**描述：**

销毁自定义弹窗options。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options自定义弹窗options的指针。

#### OH_ArkUI_CustomDialog_SetLevelMode()

```ets
int32_t OH_ArkUI_CustomDialog_SetLevelMode(ArkUI_CustomDialogOptions* options, ArkUI_LevelMode levelMode)
```

**描述：**

设置弹窗的显示层级。

本方法需要在调用[OH_ArkUI_CustomDialog_OpenDialog](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options指向自定义弹窗options的指针。[ArkUI_LevelMode](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_levelmode) levelMode显示层级的枚举值， 类型为[ArkUI_LevelMode](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_levelmode)。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetLevelUniqueId()

```ets
int32_t OH_ArkUI_CustomDialog_SetLevelUniqueId(ArkUI_CustomDialogOptions* options, int32_t uniqueId)
```

**描述：**

设置弹窗显示层级页面下的节点id。

本方法需要在调用[OH_ArkUI_CustomDialog_OpenDialog](#ZH-CN_TOPIC_0000002529445041__oh_arkui_customdialog_opendialog)方法之前调用。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options指向自定义弹窗options的指针。int32_t uniqueId指定节点id，会查找该节点所在页面，并将弹窗显示在该页面下。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetImmersiveMode()

```ets
int32_t OH_ArkUI_CustomDialog_SetImmersiveMode(ArkUI_CustomDialogOptions* options, ArkUI_ImmersiveMode immersiveMode)
```

**描述：**

设置嵌入式弹窗蒙层的显示区域。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options指向自定义弹窗options的指针。[ArkUI_ImmersiveMode](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_immersivemode) immersiveMode显示区域类型的枚举值， 类型为[ArkUI_ImmersiveMode](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_immersivemode)。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetBackgroundColor()

```ets
int32_t OH_ArkUI_CustomDialog_SetBackgroundColor(ArkUI_CustomDialogOptions* options, uint32_t backgroundColor)
```

**描述：**

设置弹窗的背景颜色。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。uint32_t backgroundColor弹窗背景颜色。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetCornerRadius()

```ets
int32_t OH_ArkUI_CustomDialog_SetCornerRadius(ArkUI_CustomDialogOptions* options, float topLeft, float topRight, float bottomLeft, float bottomRight)
```

**描述：**

设置弹窗的圆角半径。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。float topLeft弹窗左上角的圆角半径。float topRight弹窗右上角的圆角半径。float bottomLeft弹窗左下角的圆角半径。float bottomRight弹窗右下角的圆角半径。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetBorderWidth()

```ets
int32_t OH_ArkUI_CustomDialog_SetBorderWidth(ArkUI_CustomDialogOptions* options, float top, float right, float bottom, float left, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置弹窗的边框宽度。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。float top弹窗上边框的宽度。float right弹窗右边框的宽度。float bottom弹窗下边框的宽度。float left弹窗左边框的宽度。[ArkUI_LengthMetricUnit](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_lengthmetricunit) unit指定宽度的单位，默认为vp。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetBorderColor()

```ets
int32_t OH_ArkUI_CustomDialog_SetBorderColor(ArkUI_CustomDialogOptions* options, uint32_t top, uint32_t right, uint32_t bottom, uint32_t left)
```

**描述：**

设置弹窗的边框颜色。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。uint32_t top弹窗上边框的颜色。uint32_t right弹窗右边框的颜色。uint32_t bottom弹窗下边框的颜色。uint32_t left弹窗左边框的颜色。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetBorderStyle()

```ets
int32_t OH_ArkUI_CustomDialog_SetBorderStyle(ArkUI_CustomDialogOptions* options, int32_t top, int32_t right, int32_t bottom, int32_t left)
```

**描述：**

设置弹窗的边框样式。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。int32_t top弹窗上边框的样式。int32_t right弹窗右边框的样式。int32_t bottom弹窗下边框的样式。int32_t left弹窗左边框的样式。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetWidth()

```ets
int32_t OH_ArkUI_CustomDialog_SetWidth(ArkUI_CustomDialogOptions* options, float width, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置弹窗的背板宽度。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。float width弹窗的背板宽度。[ArkUI_LengthMetricUnit](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_lengthmetricunit) unit指定宽度的单位，默认为vp。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetHeight()

```ets
int32_t OH_ArkUI_CustomDialog_SetHeight(ArkUI_CustomDialogOptions* options, float height, ArkUI_LengthMetricUnit unit)
```

**描述：**

设置弹窗的背板高度。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。float height弹窗的背板高度。[ArkUI_LengthMetricUnit](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_lengthmetricunit) unit指定高度的单位，默认为vp。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetShadow()

```ets
int32_t OH_ArkUI_CustomDialog_SetShadow(ArkUI_CustomDialogOptions* options, ArkUI_ShadowStyle shadow)
```

**描述：**

设置弹窗的背板阴影。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。[ArkUI_ShadowStyle](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_shadowstyle) shadow弹窗的背板阴影样式，枚举值。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetCustomShadow()

```ets
int32_t OH_ArkUI_CustomDialog_SetCustomShadow(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* customShadow)
```

**描述：**

设置弹窗的背板阴影。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。[const ArkUI_AttributeItem](ArkUI_AttributeItem.md)* customShadow弹窗的自定义阴影参数，格式与[ArkUI_NodeAttributeType](native_node.h.md#ZH-CN_TOPIC_0000002529285071__arkui_nodeattributetype)中的NODE_CUSTOM_SHADOW属性一致。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetBackgroundBlurStyle()

```ets
int32_t OH_ArkUI_CustomDialog_SetBackgroundBlurStyle(ArkUI_CustomDialogOptions* options, ArkUI_BlurStyle blurStyle)
```

**描述：**

设置弹窗的背板模糊材质。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。[ArkUI_BlurStyle](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_blurstyle) blurStyle弹窗的背板模糊材质，枚举值。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetAlignment()

```ets
int32_t OH_ArkUI_CustomDialog_SetAlignment(ArkUI_CustomDialogOptions* options, int32_t alignment, float offsetX, float offsetY)
```

**描述：**

设置弹窗的对齐模式。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。int32_t alignment弹窗的对齐模式，参数类型[ArkUI_Alignment](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_alignment)。float offsetX弹窗的水平偏移量，浮点型。float offsetY弹窗的垂直偏移量，浮点型。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetModalMode()

```ets
int32_t OH_ArkUI_CustomDialog_SetModalMode(ArkUI_CustomDialogOptions* options, bool isModal)
```

**描述：**

设置自定义弹窗是否开启模态样式的弹窗。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。bool isModal

设置是否开启模态窗口。模态窗口有蒙层，非模态窗口无蒙层。设置为true表示开启模态窗口。设置为false表示关闭模态窗口。

默认值：false

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetAutoCancel()

```ets
int32_t OH_ArkUI_CustomDialog_SetAutoCancel(ArkUI_CustomDialogOptions* options, bool autoCancel)
```

**描述：**

设置自定义弹窗是否允许点击遮罩层退出。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。bool autoCancel

设置是否允许点击遮罩层退出，true表示关闭弹窗，false表示不关闭弹窗。

默认值：ture

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetSubwindowMode()

```ets
int32_t OH_ArkUI_CustomDialog_SetSubwindowMode(ArkUI_CustomDialogOptions* options, bool showInSubwindow)
```

**描述：**

设置弹窗是否在子窗口显示此弹窗。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。bool showInSubwindow设置弹窗需要显示在主窗口之外时，是否在子窗口显示此弹窗。默认false，弹窗显示在应用内，而非独立子窗口。值为true时，可以显示在主窗口外。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetMask()

```ets
int32_t OH_ArkUI_CustomDialog_SetMask(ArkUI_CustomDialogOptions* options, uint32_t maskColor, const ArkUI_Rect* maskRect)
```

**描述：**

设置自定义弹窗遮罩属性。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。uint32_t maskColor弹窗的遮罩颜色，0xargb格式。[const ArkUI_Rect](ArkUI_Rect.md)* maskRect遮蔽层区域范围的指针，遮蔽层区域内的事件不透传，在遮蔽层区域外的事件透传。参数类型[ArkUI_Rect](ArkUI_Rect.md)。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetKeyboardAvoidMode()

```ets
int32_t OH_ArkUI_CustomDialog_SetKeyboardAvoidMode(ArkUI_CustomDialogOptions* options, ArkUI_KeyboardAvoidMode keyboardAvoidMode)
```

**描述：**

设置弹窗避让键盘的模式。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。[ArkUI_KeyboardAvoidMode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_keyboardavoidmode) keyboardAvoidMode键盘避让模式，枚举值。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetHoverModeEnabled()

```ets
int32_t OH_ArkUI_CustomDialog_SetHoverModeEnabled(ArkUI_CustomDialogOptions* options, bool enabled)
```

**描述：**

设置弹窗是否响应悬停态。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。bool enabled是否响应悬停态，默认false。值为true时响应悬停态，值为false时不响应悬停态。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetHoverModeArea()

```ets
int32_t OH_ArkUI_CustomDialog_SetHoverModeArea(ArkUI_CustomDialogOptions* options, ArkUI_HoverModeAreaType hoverModeAreaType)
```

**描述：**

设置悬停态下弹窗默认展示区域。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。[ArkUI_HoverModeAreaType](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_hovermodeareatype) hoverModeAreaType悬停态区域，枚举值。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_RegisterOnWillDismissCallback()

```ets
int32_t OH_ArkUI_CustomDialog_RegisterOnWillDismissCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(ArkUI_DialogDismissEvent* event))
```

**描述：**

注册系统关闭自定义弹窗的监听事件。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。void* userData用户自定义数据指针。callback

监听自定义弹窗关闭的回调事件。

 - event: 回调函数的入参，捕获关闭原因。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_RegisterOnWillAppearCallback()

```ets
int32_t OH_ArkUI_CustomDialog_RegisterOnWillAppearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗显示动效前的监听事件。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。void* userData用户自定义数据指针。callback弹窗显示动效前的事件回调。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_RegisterOnDidAppearCallback()

```ets
int32_t OH_ArkUI_CustomDialog_RegisterOnDidAppearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗弹出时的监听事件。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。void* userData用户自定义数据指针。callback弹窗弹出后的事件回调。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_RegisterOnWillDisappearCallback()

```ets
int32_t OH_ArkUI_CustomDialog_RegisterOnWillDisappearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗退出动效前的监听事件。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。void* userData用户自定义数据指针。callback弹窗退出动效前的事件回调。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_RegisterOnDidDisappearCallback()

```ets
int32_t OH_ArkUI_CustomDialog_RegisterOnDidDisappearCallback(ArkUI_CustomDialogOptions* options, void* userData, void (*callback)(void* userData))
```

**描述：**

注册自定义弹窗消失时的监听事件。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。void* userData用户自定义数据指针。callback弹窗消失时的事件回调。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_GetState()

```ets
int32_t OH_ArkUI_CustomDialog_GetState(ArkUI_NativeDialogHandle handle, ArkUI_DialogState* state)
```

**描述：**

获取弹窗的状态。

**起始版本：** 20

**参数：**

参数项描述[ArkUI_NativeDialogHandle](ArkUI_NativeDialog_.md) handle指向自定义弹窗控制器的指针。[ArkUI_DialogState](native_dialog.h.md#ZH-CN_TOPIC_0000002529445041__arkui_dialogstate)* state自定义弹窗的状态。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetBackgroundBlurStyleOptions()

```ets
int32_t OH_ArkUI_CustomDialog_SetBackgroundBlurStyleOptions(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* backgroundBlurStyleOptions)
```

**描述：**

设置弹窗的背景模糊效果。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。[const ArkUI_AttributeItem](ArkUI_AttributeItem.md)* backgroundBlurStyleOptions

弹窗的背景模糊效果。参数[ArkUI_AttributeItem](ArkUI_AttributeItem.md)格式：

 .value[0].i32 表示深浅色模式，取[ArkUI_ColorMode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_colormode)枚举值。

 .value[1]?.i32 表示取色模式，取[ArkUI_AdaptiveColor](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_adaptivecolor)枚举值。

 .value[2]?.f32 表示模糊效果程度，取[0.0,1.0]范围内的值。

 .value[3]?.u32 表示灰阶模糊参数，对黑色的提亮程度，有效值范围为[0,127]。

 .value[4]?.u32 表示灰阶模糊参数，对白色的压暗程度，有效值范围为[0,127]。

 .value[5]?.i32 表示模糊激活策略，取[ArkUI_BlurStyleActivePolicy](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_blurstyleactivepolicy)枚举值。

 .value[6]?.u32 表示窗口失焦后，窗口内控件模糊效果会被移除，此时控件背板的颜色，0xargb类型。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。

#### OH_ArkUI_CustomDialog_SetBackgroundEffect()

```ets
int32_t OH_ArkUI_CustomDialog_SetBackgroundEffect(ArkUI_CustomDialogOptions* options, const ArkUI_AttributeItem* backgroundEffect)
```

**描述：**

设置弹窗的背景效果参数。

**起始版本：** 19

**参数：**

参数项描述[ArkUI_CustomDialogOptions](ArkUI_CustomDialogOptions.md)* options弹窗参数。[const ArkUI_AttributeItem](ArkUI_AttributeItem.md)* backgroundEffect

弹窗的背景效果参数。参数[ArkUI_AttributeItem](ArkUI_AttributeItem.md)格式：

 .value[0].f32 表示模糊半径，单位为vp。

 .value[1]?.f32 表示饱和度。

 .value[2]?.f32 表示亮度。

 .value[3]?.u32 表示颜色，0xargb类型。

 .value[4]?.i32 表示取色模式，取[ArkUI_AdaptiveColor](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_adaptivecolor)枚举值。

 .value[5]?.u32 表示灰阶模糊参数，对黑色的提亮程度，有效值范围为[0,127]。

 .value[6]?.u32 表示灰阶模糊参数，对白色的压暗程度，有效值范围为[0,127]。

 .value[7]?.i32 表示模糊激活策略，取[ArkUI_BlurStyleActivePolicy](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_blurstyleactivepolicy)枚举值。

 .value[8]?.u32 表示窗口失焦后，窗口内控件模糊效果会被移除，此时控件背板的颜色，0xargb类型。

**返回：**

类型说明int32_t

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 成功。

[ARKUI_ERROR_CODE_PARAM_INVALID](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 函数参数异常。