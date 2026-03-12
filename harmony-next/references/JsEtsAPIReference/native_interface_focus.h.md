# native_interface_focus.h

#### 概述

定义焦点管理的相关接口，主要用于主动转移焦点或管理控制焦点转移默认行为，控制焦点激活态。

**引用文件：** <arkui/native_interface_focus.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 15

**相关模块：**[ArkUI_NativeModule](ArkUI_NativeModule.md)

**相关示例：**[NdkFocus](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/NdkFocus)

#### 汇总

#### 枚举

名称typedef关键字描述[ArkUI_KeyProcessingMode](#ZH-CN_TOPIC_0000002529445043__arkui_keyprocessingmode)ArkUI_KeyProcessingMode按键事件处理的优先级。

#### 函数

名称描述[ArkUI_ErrorCode OH_ArkUI_FocusRequest(ArkUI_NodeHandle node)](#ZH-CN_TOPIC_0000002529445043__oh_arkui_focusrequest)为特定节点请求焦点。[void OH_ArkUI_FocusClear(ArkUI_ContextHandle uiContext)](#ZH-CN_TOPIC_0000002529445043__oh_arkui_focusclear)将当前焦点清除到根容器节点。[void OH_ArkUI_FocusActivate(ArkUI_ContextHandle uiContext, bool isActive, bool isAutoInactive)](#ZH-CN_TOPIC_0000002529445043__oh_arkui_focusactivate)设置当前界面的焦点激活态，获焦节点显示焦点框。[void OH_ArkUI_FocusSetAutoTransfer(ArkUI_ContextHandle uiContext, bool autoTransfer)](#ZH-CN_TOPIC_0000002529445043__oh_arkui_focussetautotransfer)设置页面切换时，焦点转移行为。[void OH_ArkUI_FocusSetKeyProcessingMode(ArkUI_ContextHandle uiContext, ArkUI_KeyProcessingMode mode)](#ZH-CN_TOPIC_0000002529445043__oh_arkui_focussetkeyprocessingmode)设置按键事件处理的优先级。

#### 枚举类型说明

#### ArkUI_KeyProcessingMode

```ets
enum ArkUI_KeyProcessingMode
```

**描述：**

按键事件处理的优先级。

**起始版本：** 15

枚举项描述ARKUI_KEY_PROCESSING_MODE_FOCUS_NAVIGATION = 0按键事件用于移动焦点。ARKUI_KEY_PROCESSING_MODE_FOCUS_ANCESTOR_EVENT = 1按键事件向上传递给祖先组件。

#### 函数说明

#### OH_ArkUI_FocusRequest()

```ets
ArkUI_ErrorCode OH_ArkUI_FocusRequest(ArkUI_NodeHandle node)
```

**描述：**

为特定节点请求焦点。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_NodeHandle](ArkUI_Node_.md) node节点。

**返回：**

类型说明[ArkUI_ErrorCode](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode)

错误码。

[ARKUI_ERROR_CODE_NO_ERROR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 请求成功。

[ARKUI_ERROR_CODE_FOCUS_NON_FOCUSABLE](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 节点无法获得焦点。

[ARKUI_ERROR_CODE_FOCUS_NON_FOCUSABLE_ANCESTOR](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 祖先节点无法获得焦点。

[ARKUI_ERROR_CODE_FOCUS_NON_EXISTENT](native_type.h.md#ZH-CN_TOPIC_0000002497445102__arkui_errorcode) 节点不存在。

#### OH_ArkUI_FocusClear()

```ets
void OH_ArkUI_FocusClear(ArkUI_ContextHandle uiContext)
```

**描述：**

将当前焦点清除到根容器节点。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_ContextHandle](ArkUI_Context_.md) uiContextUI实例对象指针。

#### OH_ArkUI_FocusActivate()

```ets
void OH_ArkUI_FocusActivate(ArkUI_ContextHandle uiContext, bool isActive, bool isAutoInactive)
```

**描述：**

设置当前界面的焦点激活态，获焦节点显示焦点框。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_ContextHandle](ArkUI_Context_.md) uiContextUI实例对象指针。bool isActive设置是否进入/退出焦点激活态。true表示进入焦点激活态，false表示退出焦点激活态。bool isAutoInactive当触摸事件或鼠标按下事件触发时，"true" 表示将状态设置为退出焦点激活态,"false" 表示在调用对应设置API前，保持当前状态。

#### OH_ArkUI_FocusSetAutoTransfer()

```ets
void OH_ArkUI_FocusSetAutoTransfer(ArkUI_ContextHandle uiContext, bool autoTransfer)
```

**描述：**

设置页面切换时，焦点转移行为。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_ContextHandle](ArkUI_Context_.md) uiContextUI实例对象指针。bool autoTransfer页面切换时，是否转移焦点。true表示页面切换时转移焦点，false表示页面切换时焦点不转移。

#### OH_ArkUI_FocusSetKeyProcessingMode()

```ets
void OH_ArkUI_FocusSetKeyProcessingMode(ArkUI_ContextHandle uiContext, ArkUI_KeyProcessingMode mode)
```

**描述：**

设置按键事件处理的优先级。

**起始版本：** 15

**参数：**

参数项描述[ArkUI_ContextHandle](ArkUI_Context_.md) uiContextUI实例对象指针。[ArkUI_KeyProcessingMode](native_interface_focus.h.md#ZH-CN_TOPIC_0000002529445043__arkui_keyprocessingmode) mode按键事件处理的优先级。