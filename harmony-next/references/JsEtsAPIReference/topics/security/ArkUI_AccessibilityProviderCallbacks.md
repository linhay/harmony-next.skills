# ArkUI_AccessibilityProviderCallbacks

```ets
typedef struct {...} ArkUI_AccessibilityProviderCallbacks
```

#### 概述

第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH_ArkUI_AccessibilityProviderRegisterCallback注册到系统侧。

**起始版本：** 13

**相关模块：**[ArkUI_Accessibility](ArkUI_Accessibility.md)

**所在头文件：**[native_interface_accessibility.h](../../capi/headers/native_interface_accessibility.h.md)

#### 汇总

#### 成员函数

名称描述[int32_t (*findAccessibilityNodeInfosById)(int64_t elementId, ArkUI_AccessibilitySearchMode mode,int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)](#ZH-CN_TOPIC_0000002529445073__findaccessibilitynodeinfosbyid)由接入方平台实现的回调函数，注册给系统侧调用。查询指定节点的节点信息。支持多实例场景。[int32_t (*findAccessibilityNodeInfosByText)(int64_t elementId, const char* text, int32_t requestId,ArkUI_AccessibilityElementInfoList* elementList)](#ZH-CN_TOPIC_0000002529445073__findaccessibilitynodeinfosbytext)由接入方平台实现的回调函数，注册给系统侧调用。基于指定的节点，查询满足指定text内容的节点信息。[int32_t (*findFocusedAccessibilityNode)(int64_t elementId, ArkUI_AccessibilityFocusType focusType,int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)](#ZH-CN_TOPIC_0000002529445073__findfocusedaccessibilitynode)当需要基于指定节点获取焦点元素信息时调用。[int32_t (*findNextFocusAccessibilityNode)(int64_t elementId, ArkUI_AccessibilityFocusMoveDirection direction,int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)](#ZH-CN_TOPIC_0000002529445073__findnextfocusaccessibilitynode)根据参考节点查询可以聚焦的节点，根据模式和方向查询下一个可以聚焦的节点。[int32_t (*executeAccessibilityAction)(int64_t elementId, ArkUI_Accessibility_ActionType action,ArkUI_AccessibilityActionArguments *actionArguments, int32_t requestId)](#ZH-CN_TOPIC_0000002529445073__executeaccessibilityaction)在指定节点上执行Action操作。[int32_t (*clearFocusedFocusAccessibilityNode)()](#ZH-CN_TOPIC_0000002529445073__clearfocusedfocusaccessibilitynode)清除当前焦点节点的焦点状态。[int32_t (*getAccessibilityNodeCursorPosition)(int64_t elementId, int32_t requestId, int32_t* index)](#ZH-CN_TOPIC_0000002529445073__getaccessibilitynodecursorposition)查询指定节点的当前光标位置。

#### 成员函数说明

#### findAccessibilityNodeInfosById()

```ets
int32_t (*findAccessibilityNodeInfosById)(int64_t elementId, ArkUI_AccessibilitySearchMode mode,int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)
```

**描述：**

由接入方平台实现的回调函数，注册给系统侧调用。查询指定节点的节点信息。支持多实例场景。

**起始版本：** 13

**参数：**

参数项描述int64_t elementId无障碍元素的唯一编号。[ArkUI_AccessibilitySearchMode](../../capi/headers/native_interface_accessibility.h.md) mode表示无障碍搜索模式。int32_t requestId表示请求ID。[ArkUI_AccessibilityElementInfoList](../components/ArkUI_AccessibilityElementInfoList.md)* elementList表示无障碍元素信息列表。

**返回：**

类型说明int32_t

如果操作成功，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

如果参数错误，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### findAccessibilityNodeInfosByText()

```ets
int32_t (*findAccessibilityNodeInfosByText)(int64_t elementId, const char* text, int32_t requestId,ArkUI_AccessibilityElementInfoList* elementList)
```

**描述：**

由接入方平台实现的回调函数，注册给系统侧调用。基于指定的节点，查询满足指定text内容的节点信息。

**起始版本：** 13

**参数：**

参数项描述int64_t elementId无障碍元素的唯一编号。const char* text表示无障碍文本。int32_t requestId表示请求ID。[ArkUI_AccessibilityElementInfoList](../components/ArkUI_AccessibilityElementInfoList.md)* elementList表示无障碍元素信息列表。

**返回：**

类型说明int32_t

如果操作成功，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

如果参数错误，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### findFocusedAccessibilityNode()

```ets
int32_t (*findFocusedAccessibilityNode)(int64_t elementId, ArkUI_AccessibilityFocusType focusType,int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

当需要基于指定节点获取焦点元素信息时调用。

**起始版本：** 13

**参数：**

参数项描述int64_t elementId无障碍元素的唯一编号。[ArkUI_AccessibilityFocusType](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_accessibilityfocustype) focusType表示焦点的类型。int32_t requestId表示请求ID。[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示无障碍元素信息。

**返回：**

类型说明int32_t

如果操作成功，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

如果参数错误，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### findNextFocusAccessibilityNode()

```ets
int32_t (*findNextFocusAccessibilityNode)(int64_t elementId, ArkUI_AccessibilityFocusMoveDirection direction,int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

根据参考节点查询可以聚焦的节点，根据模式和方向查询下一个可以聚焦的节点。

**起始版本：** 13

**参数：**

参数项描述int64_t elementId无障碍元素的唯一编号。[ArkUI_AccessibilityFocusMoveDirection](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_accessibilityfocusmovedirection) direction表示查找方向。int32_t requestId表示请求ID。[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示无障碍元素信息。

**返回：**

类型说明int32_t

如果操作成功，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

如果参数错误，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### executeAccessibilityAction()

```ets
int32_t (*executeAccessibilityAction)(int64_t elementId, ArkUI_Accessibility_ActionType action,ArkUI_AccessibilityActionArguments *actionArguments, int32_t requestId)
```

**描述：**

在指定的无障碍节点上执行无障碍Action操作。

**起始版本：** 13

**参数：**

参数项描述int64_t elementId无障碍元素的唯一编号。[ArkUI_Accessibility_ActionType](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_accessibility_actiontype) action表示要执行的动作。[ArkUI_AccessibilityActionArguments](ArkUI_AccessibilityActionArguments.md) *actionArguments表示动作的参数。int32_t requestId表示请求的ID。

**返回：**

类型说明int32_t

如果操作成功，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

如果参数错误，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### clearFocusedFocusAccessibilityNode()

```ets
int32_t (*clearFocusedFocusAccessibilityNode)()
```

**描述：**

清除当前焦点节点的焦点状态。

**起始版本：** 13

**返回：**

类型说明int32_t

如果操作成功，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

如果参数错误，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### getAccessibilityNodeCursorPosition()

```ets
int32_t (*getAccessibilityNodeCursorPosition)(int64_t elementId, int32_t requestId, int32_t* index)
```

**描述：**

查询指定节点的当前光标位置。

**起始版本：** 13

**参数：**

参数项描述int64_t elementId无障碍元素的唯一编号。int32_t requestId表示请求的ID。int32_t* index表示光标位置的索引。

**返回：**

类型说明int32_t

如果操作成功，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

如果参数错误，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。