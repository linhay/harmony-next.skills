# ArkUI_AccessibilityProviderCallbacksWithInstance

```ets
typedef struct {...} ArkUI_AccessibilityProviderCallbacksWithInstance
```

#### 概述

适配多实例场景第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance注册到系统侧。

**起始版本：** 15

**相关模块：**[ArkUI_Accessibility](ArkUI_Accessibility.md)

**所在头文件：**[native_interface_accessibility.h](../../capi/headers/native_interface_accessibility.h.md)

#### 汇总

#### 成员函数

名称描述[int32_t (*findAccessibilityNodeInfosById)(const char* instanceId, int64_t elementId,ArkUI_AccessibilitySearchMode mode, int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)](#ZH-CN_TOPIC_0000002497605108__findaccessibilitynodeinfosbyid)由接入方平台实现的回调函数，注册给系统侧调用。基于指定的节点，查询所需的节点信息。支持多实例场景。[int32_t (*findAccessibilityNodeInfosByText)(const char* instanceId, int64_t elementId, const char* text,int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)](#ZH-CN_TOPIC_0000002497605108__findaccessibilitynodeinfosbytext)由接入方平台实现的回调函数，注册给系统侧调用。基于指定的节点，查询满足指定组件文本内容的节点信息。支持多实例场景。[int32_t (*findFocusedAccessibilityNode)(const char* instanceId, int64_t elementId,ArkUI_AccessibilityFocusType focusType, int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)](#ZH-CN_TOPIC_0000002497605108__findfocusedaccessibilitynode)由接入方平台实现的回调函数，注册给系统侧调用。从指定节点查找已经聚焦的节点。支持多实例场景。[int32_t (*findNextFocusAccessibilityNode)(const char* instanceId, int64_t elementId, ArkUI_AccessibilityFocusMoveDirection direction,int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)](#ZH-CN_TOPIC_0000002497605108__findnextfocusaccessibilitynode)由接入方平台实现的回调函数，注册给系统侧调用。从指定节点查询指定方向的节点。支持多实例场景。[int32_t (*executeAccessibilityAction)(const char* instanceId, int64_t elementId,ArkUI_Accessibility_ActionType action, ArkUI_AccessibilityActionArguments *actionArguments, int32_t requestId)](#ZH-CN_TOPIC_0000002497605108__executeaccessibilityaction)由接入方平台实现的回调函数，注册给系统侧调用。对指定节点执行指定的操作。支持多实例场景。[int32_t (*clearFocusedFocusAccessibilityNode)(const char* instanceId)](#ZH-CN_TOPIC_0000002497605108__clearfocusedfocusaccessibilitynode)由接入方平台实现的回调函数，注册给系统侧调用。 清除当前获焦的节点。支持多实例场景。[int32_t (*getAccessibilityNodeCursorPosition)(const char* instanceId, int64_t elementId,int32_t requestId, int32_t* index)](#ZH-CN_TOPIC_0000002497605108__getaccessibilitynodecursorposition)由接入方平台实现的回调函数，注册给系统侧调用。获取当前组件中（文本组件）光标位置。支持多实例场景。

#### 成员函数说明

#### findAccessibilityNodeInfosById()

```ets
int32_t (*findAccessibilityNodeInfosById)(const char* instanceId, int64_t elementId,ArkUI_AccessibilitySearchMode mode, int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)
```

**描述：**

由接入方平台实现的回调函数，注册给系统侧调用。基于指定的节点，查询所需的节点信息。支持多实例场景。

**起始版本：** 15

**参数：**

参数项描述const char* instanceId第三方框架的实例编码。int64_t elementId无障碍元素的唯一编号。[ArkUI_AccessibilitySearchMode](../../capi/headers/native_interface_accessibility.h.md) mode无障碍服务的搜索模式。int32_t requestId请求id，用于关联请求过程，建议日志打印时附带输出该信息，方便问题定位。[ArkUI_AccessibilityElementInfoList](../components/ArkUI_AccessibilityElementInfoList.md)* elementList本次查询到的所有无障碍元素列表。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

 参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### findAccessibilityNodeInfosByText()

```ets
int32_t (*findAccessibilityNodeInfosByText)(const char* instanceId, int64_t elementId, const char* text,int32_t requestId, ArkUI_AccessibilityElementInfoList* elementList)
```

**描述：**

由接入方平台实现的回调函数，注册给系统侧调用。基于指定的节点，查询满足指定组件文本内容的节点信息。支持多实例场景。

**起始版本：** 15

**参数：**

参数项描述const char* instanceId第三方框架的实例编码。int64_t elementId无障碍元素的唯一编号。const char* text组件需要匹配的文本内容。int32_t requestId请求id，用于关联请求过程，方便问题定位。建议日志打印时附带输出该信息，方便定位。[ArkUI_AccessibilityElementInfoList](../components/ArkUI_AccessibilityElementInfoList.md)* elementList本次查询到的所有无障碍元素列表。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

 参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### findFocusedAccessibilityNode()

```ets
int32_t (*findFocusedAccessibilityNode)(const char* instanceId, int64_t elementId,ArkUI_AccessibilityFocusType focusType, int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

由接入方平台实现的回调函数，注册给系统侧调用。从指定节点查找已经聚焦的节点。支持多实例场景。

**起始版本：** 15

**参数：**

参数项描述const char* instanceId第三方框架的实例编码。int64_t elementId无障碍元素的唯一编号。[ArkUI_AccessibilityFocusType](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_accessibilityfocustype) focusType焦点类型。int32_t requestId请求id，用于关联请求过程，建议日志打印时附带输出该信息，方便问题定位。[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo本次查询到的无障碍元素。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

 参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### findNextFocusAccessibilityNode()

```ets
int32_t (*findNextFocusAccessibilityNode)(const char* instanceId, int64_t elementId, ArkUI_AccessibilityFocusMoveDirection direction,int32_t requestId, ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

由接入方平台实现的回调函数，注册给系统侧调用。从指定节点查询指定方向的节点。支持多实例场景。

**起始版本：** 15

**参数：**

参数项描述const char* instanceId第三方框架的实例编码。int64_t elementId无障碍元素的唯一编号。[ArkUI_AccessibilityFocusMoveDirection](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_accessibilityfocusmovedirection) direction搜索方向。int32_t requestId请求id，用于关联请求过程，方便问题定位。建议日志打印时附带输出该信息，方便定位。[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo本次查询到的无障碍元素。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### executeAccessibilityAction()

```ets
int32_t (*executeAccessibilityAction)(const char* instanceId, int64_t elementId,ArkUI_Accessibility_ActionType action, ArkUI_AccessibilityActionArguments *actionArguments, int32_t requestId)
```

**描述：**

由接入方平台实现的回调函数，注册给系统侧调用。对指定节点执行指定的操作。支持多实例场景。

**起始版本：** 15

**参数：**

参数项描述const char* instanceId第三方框架的实例编码。int64_t elementId无障碍元素的唯一编号。[ArkUI_Accessibility_ActionType](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_accessibility_actiontype) action需要执行的操作，比如聚焦、点击和长按等。[ArkUI_AccessibilityActionArguments](ArkUI_AccessibilityActionArguments.md) *actionArguments控制操作的参数。int32_t requestId请求id，用于关联请求过程，方便问题定位。建议日志打印时附带输出该信息，方便定位。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### clearFocusedFocusAccessibilityNode()

```ets
int32_t (*clearFocusedFocusAccessibilityNode)(const char* instanceId)
```

**描述：**

由接入方平台实现的回调函数，注册给系统侧调用。 清除当前获焦的节点。支持多实例场景。

**起始版本：** 15

**参数：**

参数项描述const char* instanceId第三方框架的实例编码。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### getAccessibilityNodeCursorPosition()

```ets
int32_t (*getAccessibilityNodeCursorPosition)(const char* instanceId, int64_t elementId,int32_t requestId, int32_t* index)
```

**描述：**

由接入方平台实现的回调函数，注册给系统侧调用。获取当前组件中（文本组件）光标位置。支持多实例场景。

**起始版本：** 15

**参数：**

参数项描述const char* instanceId第三方框架的实例编码。int64_t elementId无障碍元素的唯一编号。int32_t requestId请求id，用于关联请求过程，方便问题定位。建议日志打印时附带输出该信息，方便定位。int32_t* index光标的位置结果。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](../../capi/headers/native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。