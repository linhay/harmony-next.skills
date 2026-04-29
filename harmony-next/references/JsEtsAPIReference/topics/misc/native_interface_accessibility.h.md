# native_interface_accessibility.h

**概述**

声明用于访问Native Accessibility的API，提供无障碍相关能力。

引用文件： <arkui/native_interface_accessibility.h>

库： libace_ndk.z.so

系统能力： SystemCapability.ArkUI.ArkUI.Full

起始版本： 13

相关模块： [ArkUI_Accessibility](ArkUI_Accessibility.md)

相关示例： [AccessibilityCapi](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/AccessibilityCapi)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_AccessibleAction | ArkUI_AccessibleAction | 无障碍操作内容结构。 |
| ArkUI_AccessibleRect | ArkUI_AccessibleRect | 节点所在坐标位置。 |
| ArkUI_AccessibleRangeInfo | ArkUI_AccessibleRangeInfo | 用于特定组件设置组件的当前值、最大值、最小值，如Slider、Rating、Progress组件。 |
| ArkUI_AccessibleGridInfo | ArkUI_AccessibleGridInfo | 用于特定组件设置组件的行数、列数以及选择模式，如List、Flex、Select、Swiper组件。 |
| ArkUI_AccessibleGridItemInfo | ArkUI_AccessibleGridItemInfo | 用于特定组件设置组件的属性值，如List、Flex、Select、Swiper组件。 |
| ArkUI_AccessibilityProviderCallbacks | ArkUI_AccessibilityProviderCallbacks | 第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH_ArkUI_AccessibilityProviderRegisterCallback注册到系统侧。 |
| ArkUI_AccessibilityProviderCallbacksWithInstance | ArkUI_AccessibilityProviderCallbacksWithInstance | 适配多实例场景第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance注册到系统侧。 |
| ArkUI_AccessibilityElementInfo | ArkUI_AccessibilityElementInfo | 无障碍节点信息，用于向无障碍服务、辅助应用（屏幕朗读）传递节点信息。 |
| ArkUI_AccessibilityEventInfo | ArkUI_AccessibilityEventInfo | 无障碍事件信息。当无障碍服务或辅助应用要求控件执行操作后，需要发送执行成功事件。 |
| ArkUI_AccessibilityProvider | ArkUI_AccessibilityProvider | 该结构体为第三方操作提供者，用于承载回调函数的实现。 |
| ArkUI_AccessibilityActionArguments | ArkUI_AccessibilityActionArguments | 用于设置无障碍操作的具体参数。 |
| ArkUI_AccessibilityElementInfoList | ArkUI_AccessibilityElementInfoList | 提供封装的ArkUI_AccessibilityElementInfo的List实例。 |
| ArkUI_NodeHandle | ArkUI_NodeHandle | 定义ArkUI native组件实例对象指针。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ArkUI_Accessibility_ActionType | ArkUI_Accessibility_ActionType | Accessibility操作类型的枚举。 |
| ArkUI_AccessibilityEventType | ArkUI_AccessibilityEventType | Accessibility事件类型的枚举。 |
| ArkUI_AcessbilityErrorCode | ArkUI_AcessbilityErrorCode | Accessibility错误代码状态的枚举。 |
| ArkUI_AccessibilitySearchMode | ArkUI_AccessibilitySearchMode | Accessibility搜索类型的枚举。 |
| ArkUI_AccessibilityFocusType | ArkUI_AccessibilityFocusType | Accessibility焦点类型的枚举。 |
| ArkUI_AccessibilityFocusMoveDirection | ArkUI_AccessibilityFocusMoveDirection | Accessibility焦点移动方向的枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t OH_ArkUI_AccessibilityProviderRegisterCallback(ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityProviderCallbacks* callbacks) | 第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH_ArkUI_AccessibilityProviderRegisterCallback注册到系统侧。 |
| int32_t OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance(const char* instanceId,ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityProviderCallbacksWithInstance* callbacks) | 无障碍多实例场景第三方平台注册回调函数。 |
| void OH_ArkUI_SendAccessibilityAsyncEvent(ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityEventInfo* eventInfo,void (*callback)(int32_t errorCode)) | 主动上报事件接口，通知无障碍服务。 |
| ArkUI_AccessibilityElementInfo* OH_ArkUI_AddAndGetAccessibilityElementInfo(ArkUI_AccessibilityElementInfoList* list) | 在指定的list中增加element成员，并返回element结构。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetElementId(ArkUI_AccessibilityElementInfo* elementInfo, int32_t elementId) | 为ArkUI_AccessibilityElementInfo设置componentId。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetParentId(ArkUI_AccessibilityElementInfo* elementInfo, int32_t parentId) | 为ArkUI_AccessibilityElementInfo设置parentId。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetComponentType(ArkUI_AccessibilityElementInfo* elementInfo, const char* componentType) | 为ArkUI_AccessibilityElementInfo设置组件类型。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetContents(ArkUI_AccessibilityElementInfo* elementInfo, const char* contents) | 为ArkUI_AccessibilityElementInfo设置组件文本内容。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetHintText(ArkUI_AccessibilityElementInfo* elementInfo, const char* hintText) | 为ArkUI_AccessibilityElementInfo设置提示文本。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityText(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityText) | 为ArkUI_AccessibilityElementInfo设置Accessibility文本。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityDescription(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityDescription) | 为ArkUI_AccessibilityElementInfo设置Accessibility描述信息。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetChildNodeIds(ArkUI_AccessibilityElementInfo* elementInfo, int32_t childCount, int64_t* childNodeIds) | 为ArkUI_AccessibilityElementInfo设置childCount和childNodeIds。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetOperationActions(ArkUI_AccessibilityElementInfo* elementInfo,int32_t operationCount, ArkUI_AccessibleAction* operationActions) | 为ArkUI_AccessibilityElementInfo设置operationActions。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetScreenRect(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleRect* screenRect) | 为ArkUI_AccessibilityElementInfo设置屏幕区域。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetCheckable(ArkUI_AccessibilityElementInfo* elementInfo, bool checkable) | 为ArkUI_AccessibilityElementInfo设置是否可查。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetChecked(ArkUI_AccessibilityElementInfo* elementInfo, bool checked) | 为ArkUI_AccessibilityElementInfo设置是否被检查。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetFocusable(ArkUI_AccessibilityElementInfo* elementInfo, bool focusable) | 为ArkUI_AccessibilityElementInfo设置是否可聚焦。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetFocused(ArkUI_AccessibilityElementInfo* elementInfo, bool isFocused) | 为ArkUI_AccessibilityElementInfo设置是否聚焦。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetVisible(ArkUI_AccessibilityElementInfo* elementInfo, bool isVisible) | 为ArkUI_AccessibilityElementInfo设置是否可见。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityFocused(ArkUI_AccessibilityElementInfo* elementInfo, bool accessibilityFocused) | 为ArkUI_AccessibilityElementInfo设置accessibilityFocused。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetSelected(ArkUI_AccessibilityElementInfo* elementInfo, bool selected) | 为ArkUI_AccessibilityElementInfo设置是否被选中。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetClickable(ArkUI_AccessibilityElementInfo* elementInfo, bool clickable) | 为ArkUI_AccessibilityElementInfo设置是否支持点击。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetLongClickable(ArkUI_AccessibilityElementInfo* elementInfo, bool longClickable) | 为ArkUI_AccessibilityElementInfo设置是否支持长按。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetEnabled(ArkUI_AccessibilityElementInfo* elementInfo, bool isEnabled) | 为ArkUI_AccessibilityElementInfo设置是否启用。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetIsPassword(ArkUI_AccessibilityElementInfo* elementInfo, bool isPassword) | 为ArkUI_AccessibilityElementInfo设置是否为密码。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetScrollable(ArkUI_AccessibilityElementInfo* elementInfo, bool scrollable) | 为ArkUI_AccessibilityElementInfo设置是否支持滚动。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetEditable(ArkUI_AccessibilityElementInfo* elementInfo, bool editable) | 为ArkUI_AccessibilityElementInfo设置是否支持编辑。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetIsHint(ArkUI_AccessibilityElementInfo* elementInfo, bool isHint) | 为ArkUI_AccessibilityElementInfo设置isHint。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetRangeInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleRangeInfo* rangeInfo) | 为ArkUI_AccessibilityElementInfo设置rangeInfo。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetGridInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleGridInfo* gridInfo) | 为ArkUI_AccessibilityElementInfo设置gridInfo。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetGridItemInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleGridItemInfo* gridItem) | 为ArkUI_AccessibilityElementInfo设置gridItem。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetSelectedTextStart(ArkUI_AccessibilityElementInfo* elementInfo, int32_t selectedTextStart) | 为ArkUI_AccessibilityElementInfo设置selectedTextStart。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetSelectedTextEnd(ArkUI_AccessibilityElementInfo* elementInfo, int32_t selectedTextEnd) | 为ArkUI_AccessibilityElementInfo设置selectedTextEnd。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetCurrentItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t currentItemIndex) | 为ArkUI_AccessibilityElementInfo设置currentItemIndex。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetStartItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t startItemIndex) | 为ArkUI_AccessibilityElementInfo设置startItemIndex。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetEndItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t endItemIndex) | 为ArkUI_AccessibilityElementInfo设置endItemIndex。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetItemCount(ArkUI_AccessibilityElementInfo* elementInfo, int32_t itemCount) | 为ArkUI_AccessibilityElementInfo设置itemCount。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityOffset(ArkUI_AccessibilityElementInfo* elementInfo, int32_t offset) | 为ArkUI_AccessibilityElementInfo设置offset。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityGroup(ArkUI_AccessibilityElementInfo* elementInfo, bool accessibilityGroup) | 为ArkUI_AccessibilityElementInfo设置无障碍分组。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityLevel(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityLevel) | 为ArkUI_AccessibilityElementInfo设置无障碍重要性。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetZIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t zIndex) | 为ArkUI_AccessibilityElementInfo设置zIndex。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityOpacity(ArkUI_AccessibilityElementInfo* elementInfo, float opacity) | 为ArkUI_AccessibilityElementInfo设置透明度。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetBackgroundColor(ArkUI_AccessibilityElementInfo* elementInfo, const char* backgroundColor) | 为ArkUI_AccessibilityElementInfo设置背景色。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetBackgroundImage(ArkUI_AccessibilityElementInfo* elementInfo, const char* backgroundImage) | 为ArkUI_AccessibilityElementInfo设置背景图。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetBlur(ArkUI_AccessibilityElementInfo* elementInfo, const char* blur) | 为ArkUI_AccessibilityElementInfo设置模糊度。 |
| int32_t OH_ArkUI_AccessibilityElementInfoSetHitTestBehavior(ArkUI_AccessibilityElementInfo* elementInfo, const char* hitTestBehavior) | 为ArkUI_AccessibilityElementInfo设置hitTest模式。 |
| ArkUI_AccessibilityElementInfo* OH_ArkUI_CreateAccessibilityElementInfo(void) | 创建一个ArkUI_AccessibilityElementInfo对象，创建后需要调用OH_ArkUI_DestoryAccessibilityElementInfo释放。 |
| void OH_ArkUI_DestoryAccessibilityElementInfo(ArkUI_AccessibilityElementInfo* elementInfo) | 销毁一个ArkUI_AccessibilityElementInfo对象。 |
| ArkUI_AccessibilityEventInfo* OH_ArkUI_CreateAccessibilityEventInfo(void) | 创建一个ArkUI_AccessibilityEventInfo对象，创建后需要调用OH_ArkUI_DestoryAccessibilityEventInfo释放。 |
| void OH_ArkUI_DestoryAccessibilityEventInfo(ArkUI_AccessibilityEventInfo* eventInfo) | 销毁ArkUI_AccessibilityEventInfo对象。 |
| int32_t OH_ArkUI_AccessibilityEventSetEventType(ArkUI_AccessibilityEventInfo* eventInfo, ArkUI_AccessibilityEventType eventType) | 为ArkUI_AccessibilityEventInfo设置事件类型。 |
| int32_t OH_ArkUI_AccessibilityEventSetTextAnnouncedForAccessibility(ArkUI_AccessibilityEventInfo* eventInfo, const char* textAnnouncedForAccessibility) | 为ArkUI_AccessibilityEventInfo设置textAnnouncedForAccessibility。 |
| int32_t OH_ArkUI_AccessibilityEventSetRequestFocusId(ArkUI_AccessibilityEventInfo* eventInfo, int32_t requestFocusId) | 为ArkUI_AccessibilityEventInfo设置requestFocusId。 |
| int32_t OH_ArkUI_AccessibilityEventSetElementInfo(ArkUI_AccessibilityEventInfo* eventInfo, ArkUI_AccessibilityElementInfo* elementInfo) | 为ArkUI_AccessibilityEventInfo设置elementInfo。 |
| int32_t OH_ArkUI_FindAccessibilityActionArgumentByKey(ArkUI_AccessibilityActionArguments* arguments, const char* key, char** value) | 获取ArkUI_AccessibilityActionArguments中指定key的value值。 |
| int32_t OH_ArkUI_NativeModule_GetNativeAccessibilityProvider(ArkUI_NodeHandle* node, ArkUI_AccessibilityProvider** provider) | 获取指向ArkUI_AccessibilityProvider对象指针的二级指针变量。 其中ArkUI_AccessibilityProvider对象与传入的ArkUI_NodeHandle的实例一一对应。 三方框架将自身UI组件映射为ARKUI_NODE_CUSTOM类型的RenderNode并得到ArkUI_NodeHandle。 再调用OH_ArkUI_NativeModule_GetNativeAccessibilityProvider接口获取ArkUI_AccessibilityProvider指针并注册无障碍回调。 最终实现ArkUI无障碍服务对三方框架UI的识别与事件触发。 仅当三方框架将自身UI组件映射为ARKUI_NODE_CUSTOM的RenderNode，该接口才会生效，否则会报错误码。 本接口通过RenderNode实现三方框架的接入，仅支持ARKUI_NODE_CUSTOM接入无障碍服务，可以实现无障碍控件树获取能力。 不支持多线程并发，由三方框架保证调用时的线程安全。 |

**枚举类型说明**

**ArkUI_Accessibility_ActionType**

```ets
enum ArkUI_Accessibility_ActionType
```

描述：

Accessibility操作类型的枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_INVALID = 0 | 无效值。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_CLICK = 0x00000010 | 收到事件后，组件需要对点击做出响应。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_LONG_CLICK = 0x00000020 | 收到事件后，组件需要对长点击做出响应。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_GAIN_ACCESSIBILITY_FOCUS = 0x00000040 | 表示获取辅助功能焦点的操作，特定组件已聚焦。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_CLEAR_ACCESSIBILITY_FOCUS = 0x00000080 | 表示清除辅助功能焦点的操作。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_SCROLL_FORWARD = 0x00000100 | 滚动组件响应向前滚动动作。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_SCROLL_BACKWARD = 0x00000200 | 滚动组件响应反向滚动操作。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_COPY = 0x00000400 | 复制文本组件的选定内容。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_PASTE = 0x00000800 | 粘贴文本组件的选定内容。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_CUT = 0x00001000 | 剪切文本组件的选定内容。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_SELECT_TEXT = 0x00002000 | 针对文本组件进行选择操作。结合ArkUI_AccessibilityActionArguments使用，配置selectTextStart，selectTextEnd，selectTextInForWard。进入编辑区选择一段文本内容。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_SET_TEXT = 0x00004000 | 设置文本组件的文本内容。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_SET_CURSOR_POSITION = 0x00100000 | 针对文本组件设置光标位置。结合ArkUI_AccessibilityActionArguments使用，配置offset设置位置。 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_NEXT_HTML_ITEM = 0x02000000 | 焦点移动操作中支持查找下一个焦点。此处的HTML并不代表网页元素，仅用于表示具有可自行查找下一个可见聚焦组件的能力，与Web支持的能力相似。实现findNextFocusAccessibilityNode的能力才可配置该属性。 起始版本： 15 |
| ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_PREVIOUS_HTML_ITEM = 0x04000000 | 焦点移动操作中支持查找上一个焦点。此处的HTML并不代表网页元素，仅用于表示具有可自行查找上一个可见聚焦组件的能力，与Web支持的能力相似。实现findNextFocusAccessibilityNode的能力才可配置该属性。 起始版本： 15 |

**ArkUI_AccessibilityEventType**

```ets
enum ArkUI_AccessibilityEventType
```

描述：

Accessibility事件类型的枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_INVALID = 0 | 无效值。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_CLICKED = 0x00000001 | 点击事件，在UI组件响应后发送。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_LONG_CLICKED = 0x00000002 | 长点击事件，在UI组件响应后发送。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_SELECTED = 0x00000004 | 被选中事件，控件响应完成后发送。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_TEXT_UPDATE = 0x00000010 | 文本更新事件，需要在文本更新时发送。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_PAGE_STATE_UPDATE = 0x00000020 | 页面更新事件，当页面跳转、切换、大小更改或移动时发送。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_PAGE_CONTENT_UPDATE = 0x00000800 | 页面内容发生变化时需要发送事件。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_SCROLLED = 0x000001000 | scrolled事件，当可滚动的组件上发生滚动事件时，会发送此事件。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_ACCESSIBILITY_FOCUSED = 0x00008000 | Accessibility焦点事件，在UI组件响应后发送。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_ACCESSIBILITY_FOCUS_CLEARED = 0x00010000 | Accessibility焦点清除事件，在UI组件响应后发送。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_REQUEST_ACCESSIBILITY_FOCUS = 0x02000000 | 主动请求指定节点聚焦。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_PAGE_OPEN = 0x20000000 | UI组件上报页面打开事件。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_PAGE_CLOSE = 0x08000000 | UI组件上报页面关闭事件。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_ANNOUNCE_FOR_ACCESSIBILITY = 0x10000000 | 广播Accessibility事件，请求主动播放指定的内容事件。 |
| ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_FOCUS_NODE_UPDATE = 0x10000001 | 焦点更新事件，用于焦点更新场景。 |

**ArkUI_AcessbilityErrorCode**

```ets
enum ArkUI_AcessbilityErrorCode
```

描述：

Accessibility错误代码状态的枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL = 0 | 成功。 |
| ARKUI_ACCESSIBILITY_NATIVE_RESULT_FAILED = -1 | 失败。 |
| ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER = -2 | 无效参数。 |
| ARKUI_ACCESSIBILITY_NATIVE_RESULT_OUT_OF_MEMORY = -3 | 内存不足。 |

**ArkUI_AccessibilitySearchMode**

```ets
enum ArkUI_AccessibilitySearchMode
```

描述：

Accessibility搜索类型的枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_CURRENT = 0 | 查询当前节点。 |
| ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_PREDECESSORS = 1 << 0 | 查询父节点。 |
| ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_SIBLINGS = 1 << 1 | 查询兄弟节点。 |
| ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_CHILDREN = 1 << 2 | 查询下一层孩子节点。 |
| ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_RECURSIVE_CHILDREN = 1 << 3 | 查询所有孩子节点。 |

**ArkUI_AccessibilityFocusType**

```ets
enum ArkUI_AccessibilityFocusType
```

描述：

Accessibility焦点类型的枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_NATIVE_FOCUS_TYPE_INVALID = -1 | 无效值。 |
| ARKUI_ACCESSIBILITY_NATIVE_FOCUS_TYPE_INPUT = 1 << 0 | 输入焦点类型。 |
| ARKUI_ACCESSIBILITY_NATIVE_FOCUS_TYPE_ACCESSIBILITY = 1 << 1 | Accessibility焦点类型。 |

**ArkUI_AccessibilityFocusMoveDirection**

```ets
enum ArkUI_AccessibilityFocusMoveDirection
```

描述：

Accessibility焦点移动方向的枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_INVALID = 0 | 无效值。 |
| ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_UP = 0x00000001 | 焦点向上移动。 |
| ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_DOWN = 0x00000002 | 焦点向下移动。 |
| ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_LEFT = 0x00000004 | 焦点向左移动。 |
| ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_RIGHT = 0x00000008 | 焦点向右移动。 |
| ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_FORWARD = 0x00000010 | 焦点向下一个可聚焦节点移动，基于查询请求中指定的基准节点。 |
| ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_BACKWARD = 0x00000020 | 焦点向上一个可聚焦节点移动，基于查询请求中指定的基准节点。 |

**函数说明**

**OH_ArkUI_AccessibilityProviderRegisterCallback()**

```ets
int32_t OH_ArkUI_AccessibilityProviderRegisterCallback(ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityProviderCallbacks* callbacks)
```

描述：

第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH_ArkUI_AccessibilityProviderRegisterCallback注册到系统侧。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityProvider* provider | 表示指向ArkUI_AccessibilityProvider实例的指针。 |
| ArkUI_AccessibilityProviderCallbacks* callbacks | 表示指向GetAccessibilityNodeCursorPosition实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 如果操作成功，则返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 如果参数错误，则返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance()**

```ets
int32_t OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance(const char* instanceId, ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityProviderCallbacksWithInstance* callbacks)
```

描述：

无障碍多实例场景第三方平台注册回调函数。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| const char* instanceId | 第三方平台接入的实例ID，用于区分多实例场景中不同的第三方实例，ID由第三方平台指定与维护。 |
| ArkUI_AccessibilityProvider* provider | 第三方平台接入provider句柄。 |
| ArkUI_AccessibilityProviderCallbacksWithInstance* callbacks | 表示指向ArkUI_AccessibilityProviderCallbacksWithInstance实例的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_SendAccessibilityAsyncEvent()**

```ets
void OH_ArkUI_SendAccessibilityAsyncEvent(ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityEventInfo* eventInfo, void (*callback)(int32_t errorCode))
```

描述：

主动上报事件接口，通知无障碍服务。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityProvider* provider | 第三方平台接入provider句柄。 |
| ArkUI_AccessibilityEventInfo* eventInfo | 表示指向Accessibility事件信息的指针。 |
| void (*callback)(int32_t errorCode) | 表示指向SendAccessibilityAsyncEvent的回调。 |

**OH_ArkUI_AddAndGetAccessibilityElementInfo()**

```ets
ArkUI_AccessibilityElementInfo* OH_ArkUI_AddAndGetAccessibilityElementInfo(ArkUI_AccessibilityElementInfoList* list)
```

描述：

在指定的list中增加element成员，并返回element结构。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfoList* list | 指定的ArkUI_AccessibilityElementInfoList结构，新创建的ElementInfo成员加入该list后返回给函数调用方。 |

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* | 返回创建完成的ArkUI_AccessibilityElementInfo结构指针；如果创建失败，则返回NULL。 |

**OH_ArkUI_AccessibilityElementInfoSetElementId()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetElementId(ArkUI_AccessibilityElementInfo* elementInfo, int32_t elementId)
```

描述：

为ArkUI_AccessibilityElementInfo设置componentId。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | ArkUI_AccessibilityElementInfo指针。 |
| int32_t elementId | 无障碍元素的唯一编号。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetParentId()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetParentId(ArkUI_AccessibilityElementInfo* elementInfo, int32_t parentId)
```

描述：

为ArkUI_AccessibilityElementInfo设置parentId。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t parentId | 表示元素的父组件无障碍编号。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetComponentType()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetComponentType(ArkUI_AccessibilityElementInfo* elementInfo, const char* componentType)
```

描述：

为ArkUI_AccessibilityElementInfo设置组件类型。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| const char* componentType | 表示元素所属的组件类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetContents()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetContents(ArkUI_AccessibilityElementInfo* elementInfo, const char* contents)
```

描述：

为ArkUI_AccessibilityElementInfo设置组件文本内容。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| const char* contents | 表示元素被无障碍服务所识别的文本内容。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetHintText()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetHintText(ArkUI_AccessibilityElementInfo* elementInfo, const char* hintText)
```

描述：

为ArkUI_AccessibilityElementInfo设置提示文本。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| const char* hintText | 表示提示文本。 默认为""。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetAccessibilityText()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityText(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityText)
```

描述：

为ArkUI_AccessibilityElementInfo设置Accessibility文本。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| const char* accessibilityText | 表示Accessibility文本。默认为""。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetAccessibilityDescription()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityDescription(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityDescription)
```

描述：

为ArkUI_AccessibilityElementInfo设置Accessibility描述信息。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| const char* accessibilityDescription | 表示Accessibility描述信息。 默认为""。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetChildNodeIds()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetChildNodeIds(ArkUI_AccessibilityElementInfo* elementInfo, int32_t childCount, int64_t* childNodeIds)
```

描述：

设置ArkUI_AccessibilityElementInfo的childCount和childNodeIds。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t childCount | 表示孩子节点数量。默认值为0。 |
| int64_t* childNodeIds | 表示孩子节点id集合。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetOperationActions()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetOperationActions(ArkUI_AccessibilityElementInfo* elementInfo,int32_t operationCount, ArkUI_AccessibleAction* operationActions)
```

描述：

为ArkUI_AccessibilityElementInfo设置operationActions。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t* operationCount | 组件支持的action数量。 |
| ArkUI_AccessibleAction* operationActions | 组件支持的action。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetScreenRect()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetScreenRect(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleRect* screenRect)
```

描述：

为ArkUI_AccessibilityElementInfo设置屏幕区域。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| ArkUI_AccessibleRect* screenRect | 表示屏幕区域。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetCheckable()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetCheckable(ArkUI_AccessibilityElementInfo* elementInfo, bool checkable)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否可查。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool checkable | 表示是否可查。true表示可查，false表示不可查。默认值为false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetChecked()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetChecked(ArkUI_AccessibilityElementInfo* elementInfo, bool checked)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否被检查。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool checked | 表示是否被检查。true表示被检查过，false表示未被检查。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetFocusable()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetFocusable(ArkUI_AccessibilityElementInfo* elementInfo, bool focusable)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否可聚焦。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool focusable | 表示是否可聚焦。true表示可聚焦，false表示不可聚焦。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetFocused()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetFocused(ArkUI_AccessibilityElementInfo* elementInfo, bool isFocused)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否聚焦。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool isFocused | 表示是否聚焦。true表示已聚焦，false表示未聚焦。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetVisible()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetVisible(ArkUI_AccessibilityElementInfo* elementInfo, bool isVisible)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否可见。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool isVisible | 表示是否可见。true表示可见，false表示不可见。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetAccessibilityFocused()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityFocused(ArkUI_AccessibilityElementInfo* elementInfo, bool accessibilityFocused)
```

描述：

为ArkUI_AccessibilityElementInfo设置accessibilityFocused。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool accessibilityFocused | 表示是否被无障碍聚焦。true表示被无障碍聚焦，false表示未被无障碍聚焦。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetSelected()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetSelected(ArkUI_AccessibilityElementInfo* elementInfo, bool selected)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否被选中。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool selected | 表示是否被选中。true表示被选中，false表示未选中。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetClickable()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetClickable(ArkUI_AccessibilityElementInfo* elementInfo, bool clickable)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否支持点击。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool clickable | 表示是否支持点击。true表示支持，false表示不支持。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetLongClickable()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetLongClickable(ArkUI_AccessibilityElementInfo* elementInfo, bool longClickable)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否支持长按。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool longClickable | 表示是否支持长按。true表示支持，false表示不支持。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetEnabled()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetEnabled(ArkUI_AccessibilityElementInfo* elementInfo, bool isEnabled)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否启用。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool isEnabled | 表示是否启用。true表示启用，false表示未启用。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetIsPassword()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetIsPassword(ArkUI_AccessibilityElementInfo* elementInfo, bool isPassword)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否为密码。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool isPassword | 表示是否为密码。true表示是密码，false表示不是密码。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetScrollable()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetScrollable(ArkUI_AccessibilityElementInfo* elementInfo, bool scrollable)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否支持滚动。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool scrollable | 表示是否支持滚动。true表示支持，false表示不支持。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetEditable()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetEditable(ArkUI_AccessibilityElementInfo* elementInfo, bool editable)
```

描述：

为ArkUI_AccessibilityElementInfo设置是否支持编辑。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool editable | 表示是否支持编辑。true表示支持，false表示不支持。默认值false。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetIsHint()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetIsHint(ArkUI_AccessibilityElementInfo* elementInfo, bool isHint)
```

描述：

为ArkUI_AccessibilityElementInfo设置isHint。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool isHint | 表示是否为提示状态。true表示是提示状态，false表示不是提示状态。在提示状态下才会获取hintText信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetRangeInfo()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetRangeInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleRangeInfo* rangeInfo)
```

描述：

为ArkUI_AccessibilityElementInfo设置rangeInfo。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| ArkUI_AccessibleRangeInfo* rangeInfo | 表示特定组件的当前值、最大值、最小值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetGridInfo()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetGridInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleGridInfo* gridInfo)
```

描述：

为ArkUI_AccessibilityElementInfo设置gridInfo。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| ArkUI_AccessibleGridInfo* gridInfo | 表示特定组件的行数、列数以及选择模式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetGridItemInfo()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetGridItemInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleGridItemInfo* gridItem)
```

描述：

为ArkUI_AccessibilityElementInfo设置gridItem。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| ArkUI_AccessibleGridItemInfo* gridItem | 表示特定组件的属性值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetSelectedTextStart()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetSelectedTextStart(ArkUI_AccessibilityElementInfo* elementInfo, int32_t selectedTextStart)
```

描述：

为ArkUI_AccessibilityElementInfo设置selectedTextStart。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t selectedTextStart | 文本类控件使用，设置选中文本的起始位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetSelectedTextEnd()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetSelectedTextEnd(ArkUI_AccessibilityElementInfo* elementInfo, int32_t selectedTextEnd)
```

描述：

为ArkUI_AccessibilityElementInfo设置selectedTextEnd。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t selectedTextEnd | 文本类控件使用，设置选中文本的结束位置。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetCurrentItemIndex()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetCurrentItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t currentItemIndex)
```

描述：

为ArkUI_AccessibilityElementInfo设置currentItemIndex。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t currentItemIndex | 当前获焦控件的位置信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetStartItemIndex()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetStartItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t startItemIndex)
```

描述：

为ArkUI_AccessibilityElementInfo设置startItemIndex。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t startItemIndex | 当前屏幕中显示的第一个元素的位置信息。List、Select、Swiper、Tab_Bar等组件使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetEndItemIndex()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetEndItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t endItemIndex)
```

描述：

为ArkUI_AccessibilityElementInfo设置endItemIndex。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t endItemIndex | 当前屏幕中显示的最后一个元素的位置信息。List、Select、Swiper、Tab_Bar等组件使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetItemCount()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetItemCount(ArkUI_AccessibilityElementInfo* elementInfo, int32_t itemCount)
```

描述：

为ArkUI_AccessibilityElementInfo设置itemCount。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t itemCount | 表示特定组件的元素总数。如List、Select、Swiper、Tab_Bar等组件使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetAccessibilityOffset()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityOffset(ArkUI_AccessibilityElementInfo* elementInfo, int32_t offset)
```

描述：

为ArkUI_AccessibilityElementInfo设置offset。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t offset | 对于可滚动类控件，如List、Grid，内容区相对于元素顶部坐标的滚动像素偏移量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetAccessibilityGroup()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityGroup(ArkUI_AccessibilityElementInfo* elementInfo, bool accessibilityGroup)
```

描述：

为ArkUI_AccessibilityElementInfo设置无障碍分组。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| bool accessibilityGroup | 表示是否启用无障碍分组。true表示启用，false表示不启用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetAccessibilityLevel()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityLevel(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityLevel)
```

描述：

为ArkUI_AccessibilityElementInfo设置无障碍重要性。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| const char* accessibilityLevel | 表示组件的无障碍重要性，用于控制某个组件是否被无障碍辅助服务所识别。 - auto：由系统根据当前组件的属性自动判断该组件是否重要，决定是否让无障碍辅助服务识别该组件。 - yes：表示该组件重要，允许无障碍辅助服务识别该组件。 - no：表示该组件不重要，不允许无障碍辅助服务识别该组件。 - no-hide-descendants：表示该组件及其子孙节点都不重要，不允许无障碍辅助服务识别该组件及其子孙节点。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetZIndex()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetZIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t zIndex)
```

描述：

为ArkUI_AccessibilityElementInfo设置zIndex。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| int32_t zIndex | 组件z序，用于控制元素在垂直于屏幕的z轴上的位置。UITest需要使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetAccessibilityOpacity()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityOpacity(ArkUI_AccessibilityElementInfo* elementInfo, float opacity)
```

描述：

为ArkUI_AccessibilityElementInfo设置透明度。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| float opacity | 表示透明度。其取值范围是0到1，其中1表示完全不透明，0表示完全透明。UITest需要使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetBackgroundColor()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetBackgroundColor(ArkUI_AccessibilityElementInfo* elementInfo, const char* backgroundColor)
```

描述：

为ArkUI_AccessibilityElementInfo设置背景色。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| const char* backgroundColor | 表示背景色。UITest需要使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetBackgroundImage()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetBackgroundImage(ArkUI_AccessibilityElementInfo* elementInfo, const char* backgroundImage)
```

描述：

为ArkUI_AccessibilityElementInfo设置背景图片。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| const char* backgroundImage | 表示背景图片。UITest需要使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetBlur()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetBlur(ArkUI_AccessibilityElementInfo* elementInfo, const char* blur)
```

描述：

为ArkUI_AccessibilityElementInfo设置模糊度。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| const char* blur | 表示模糊度。UITest需要使用。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityElementInfoSetHitTestBehavior()**

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetHitTestBehavior(ArkUI_AccessibilityElementInfo* elementInfo, const char* hitTestBehavior)
```

描述：

为ArkUI_AccessibilityElementInfo设置hitTest模式。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |
| const char* hitTestBehavior | 表示hitTest模式，取值范围参考HitTestMode。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_CreateAccessibilityElementInfo()**

```ets
ArkUI_AccessibilityElementInfo* OH_ArkUI_CreateAccessibilityElementInfo(void)
```

描述：

创建一个ArkUI_AccessibilityElementInfo对象，创建后需要调用OH_ArkUI_DestoryAccessibilityElementInfo释放。

起始版本： 13

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* | 返回ArkUI_AccessibilityElementInfo对象。 |

**OH_ArkUI_DestoryAccessibilityElementInfo()**

```ets
void OH_ArkUI_DestoryAccessibilityElementInfo(ArkUI_AccessibilityElementInfo* elementInfo)
```

描述：

销毁一个ArkUI_AccessibilityElementInfo对象。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示指向ArkUI_AccessibilityElementInfo的指针。 |

**OH_ArkUI_CreateAccessibilityEventInfo()**

```ets
ArkUI_AccessibilityEventInfo* OH_ArkUI_CreateAccessibilityEventInfo(void)
```

描述：

创建一个ArkUI_AccessibilityEventInfo对象，创建后需要调用OH_ArkUI_DestoryAccessibilityEventInfo释放。

起始版本： 13

返回：

| 类型 | 说明 |
| --- | --- |
| ArkUI_AccessibilityEventInfo* | 返回ArkUI_AccessibilityEventInfo对象。 |

**OH_ArkUI_DestoryAccessibilityEventInfo()**

```ets
void OH_ArkUI_DestoryAccessibilityEventInfo(ArkUI_AccessibilityEventInfo* eventInfo)
```

描述：

销毁ArkUI_AccessibilityEventInfo对象。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityEventInfo* eventInfo | 需要被销毁的ArkUI_AccessibilityEventInfo对象。 |

**OH_ArkUI_AccessibilityEventSetEventType()**

```ets
int32_t OH_ArkUI_AccessibilityEventSetEventType(ArkUI_AccessibilityEventInfo* eventInfo,  ArkUI_AccessibilityEventType eventType)
```

描述：

为ArkUI_AccessibilityEventInfo设置事件类型。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityEventInfo* eventInfo | 表示事件信息。 |
| ArkUI_AccessibilityEventType eventType | 表示事件类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityEventSetTextAnnouncedForAccessibility()**

```ets
int32_t OH_ArkUI_AccessibilityEventSetTextAnnouncedForAccessibility(ArkUI_AccessibilityEventInfo* eventInfo,  const char* textAnnouncedForAccessibility)
```

描述：

为ArkUI_AccessibilityEventInfo设置textAnnouncedForAccessibility。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityEventInfo* eventInfo | 表示事件信息。 |
| const char* textAnnouncedForAccessibility | 表示textAnnouncedForAccessibility。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityEventSetRequestFocusId()**

```ets
int32_t OH_ArkUI_AccessibilityEventSetRequestFocusId(ArkUI_AccessibilityEventInfo* eventInfo,  int32_t requestFocusId)
```

描述：

为ArkUI_AccessibilityEventInfo设置requestFocusId。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityEventInfo* eventInfo | 表示事件信息。 |
| int32_t requestFocusId | 表示请求焦点id。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_AccessibilityEventSetElementInfo()**

```ets
int32_t OH_ArkUI_AccessibilityEventSetElementInfo(ArkUI_AccessibilityEventInfo* eventInfo,  ArkUI_AccessibilityElementInfo* elementInfo)
```

描述：

为ArkUI_AccessibilityEventInfo设置elementInfo。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityEventInfo* eventInfo | 表示事件信息。 |
| ArkUI_AccessibilityElementInfo* elementInfo | 表示ArkUI_AccessibilityElementInfo元素信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_FindAccessibilityActionArgumentByKey()**

```ets
int32_t OH_ArkUI_FindAccessibilityActionArgumentByKey(ArkUI_AccessibilityActionArguments* arguments, const char* key, char** value)
```

描述：

获取ArkUI_AccessibilityActionArguments中指定key的value值。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_AccessibilityActionArguments* arguments | 表示ArkUI_AccessibilityActionArguments对象信息。 |
| const char* key | 表示key。 |
| char** value | 表示value。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 成功返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 |

**OH_ArkUI_NativeModule_GetNativeAccessibilityProvider()**

```ets
int32_t OH_ArkUI_NativeModule_GetNativeAccessibilityProvider(ArkUI_NodeHandle* node, ArkUI_AccessibilityProvider** provider)
```

描述：

获取指向[ArkUI_AccessibilityProvider](ArkUI_AccessibilityProvider.md)对象指针的二级指针变量。

其中[ArkUI_AccessibilityProvider](ArkUI_AccessibilityProvider.md)对象与传入的[ArkUI_NodeHandle](ArkUI_Node_.md)的实例一一对应。

三方框架将自身UI组件映射为[ARKUI_NODE_CUSTOM](native_node.h.md#ZH-CN_TOPIC_0000002522081032__arkui_nodetype)类型的[RenderNode](RenderNode.md)并得到[ArkUI_NodeHandle](ArkUI_Node_.md)。

再调用OH_ArkUI_NativeModule_GetNativeAccessibilityProvider接口获取[ArkUI_AccessibilityProvider](ArkUI_AccessibilityProvider.md)指针并注册无障碍回调。

最终实现ArkUI无障碍服务对三方框架UI的识别与事件触发。

仅当三方框架将自身UI组件映射为[ARKUI_NODE_CUSTOM](native_node.h.md#ZH-CN_TOPIC_0000002522081032__arkui_nodetype)的[RenderNode](RenderNode.md)，该接口才会生效，否则会报错误码。

本接口通过[RenderNode](RenderNode.md)实现三方框架的接入，仅支持[ARKUI_NODE_CUSTOM](native_node.h.md#ZH-CN_TOPIC_0000002522081032__arkui_nodetype)接入无障碍服务，可以实现无障碍控件树获取能力。

不支持多线程并发，由三方框架保证调用时的线程安全。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| ArkUI_NodeHandle* node | 指向一个ArkUI_NodeHandle对象的指针。 |
| ArkUI_AccessibilityProvider** provider | 指向一个ArkUI_AccessibilityProvider类型对象的指针。provider用于注册无障碍回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 返回状态码。 成功返回ARKUI_ERROR_CODE_NO_ERROR。 参数错误返回ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER。 参数错误：1. 传入的参数node或者provider为空指针。 2. node对应的ArkUI_NodeHandle类型不为ARKUI_NODE_CUSTOM。 |