# native_interface_accessibility.h

#### 概述

声明用于访问Native Accessibility的API，提供无障碍相关能力。

**引用文件：** <arkui/native_interface_accessibility.h>

**库：** libace_ndk.z.so

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 13

**相关模块：**[ArkUI_Accessibility](ArkUI_Accessibility.md)

**相关示例：**[AccessibilityCapi](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUIKit/AccessibilityCapi)

#### 汇总

#### 结构体

名称typedef关键字描述[ArkUI_AccessibleAction](ArkUI_AccessibleAction.md)ArkUI_AccessibleAction无障碍操作内容结构。[ArkUI_AccessibleRect](ArkUI_AccessibleRect.md)ArkUI_AccessibleRect节点所在坐标位置。[ArkUI_AccessibleRangeInfo](ArkUI_AccessibleRangeInfo.md)ArkUI_AccessibleRangeInfo用于特定组件设置组件的当前值、最大值、最小值，如Slider、Rating、Progress组件。[ArkUI_AccessibleGridInfo](ArkUI_AccessibleGridInfo.md)ArkUI_AccessibleGridInfo用于特定组件设置组件的行数、列数以及选择模式，如List、Flex、Select、Swiper组件。[ArkUI_AccessibleGridItemInfo](ArkUI_AccessibleGridItemInfo.md)ArkUI_AccessibleGridItemInfo用于特定组件设置组件的属性值，如List、Flex、Select、Swiper组件。[ArkUI_AccessibilityProviderCallbacks](ArkUI_AccessibilityProviderCallbacks.md)ArkUI_AccessibilityProviderCallbacks第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH_ArkUI_AccessibilityProviderRegisterCallback注册到系统侧。[ArkUI_AccessibilityProviderCallbacksWithInstance](ArkUI_AccessibilityProviderCallbacksWithInstance.md)ArkUI_AccessibilityProviderCallbacksWithInstance适配多实例场景第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance注册到系统侧。[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)ArkUI_AccessibilityElementInfo无障碍节点信息，用于向无障碍服务、辅助应用（屏幕朗读）传递节点信息。[ArkUI_AccessibilityEventInfo](ArkUI_AccessibilityEventInfo.md)ArkUI_AccessibilityEventInfo无障碍事件信息。当无障碍服务或辅助应用要求控件执行操作后，需要发送执行成功事件。[ArkUI_AccessibilityProvider](ArkUI_AccessibilityProvider.md)ArkUI_AccessibilityProvider该结构体为第三方操作提供者，用于承载回调函数的实现。[ArkUI_AccessibilityActionArguments](ArkUI_AccessibilityActionArguments.md)ArkUI_AccessibilityActionArguments用于设置无障碍操作的具体参数。[ArkUI_AccessibilityElementInfoList](ArkUI_AccessibilityElementInfoList.md)ArkUI_AccessibilityElementInfoList提供封装的ArkUI_AccessibilityElementInfo的List实例。

#### 枚举

名称typedef关键字描述[ArkUI_Accessibility_ActionType](#ZH-CN_TOPIC_0000002529285069__arkui_accessibility_actiontype)ArkUI_Accessibility_ActionTypeAccessibility操作类型的枚举。[ArkUI_AccessibilityEventType](#ZH-CN_TOPIC_0000002529285069__arkui_accessibilityeventtype)ArkUI_AccessibilityEventTypeAccessibility事件类型的枚举。[ArkUI_AcessbilityErrorCode](#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)ArkUI_AcessbilityErrorCodeAccessibility错误代码状态的枚举。[ArkUI_AccessibilitySearchMode](#ZH-CN_TOPIC_0000002529285069__arkui_accessibilitysearchmode)ArkUI_AccessibilitySearchModeAccessibility搜索类型的枚举。[ArkUI_AccessibilityFocusType](#ZH-CN_TOPIC_0000002529285069__arkui_accessibilityfocustype)ArkUI_AccessibilityFocusTypeAccessibility焦点类型的枚举。[ArkUI_AccessibilityFocusMoveDirection](#ZH-CN_TOPIC_0000002529285069__arkui_accessibilityfocusmovedirection)ArkUI_AccessibilityFocusMoveDirectionAccessibility焦点移动方向的枚举。

#### 函数

名称描述[int32_t OH_ArkUI_AccessibilityProviderRegisterCallback(ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityProviderCallbacks* callbacks)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityproviderregistercallback)第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH_ArkUI_AccessibilityProviderRegisterCallback注册到系统侧。[int32_t OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance(const char* instanceId,ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityProviderCallbacksWithInstance* callbacks)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityproviderregistercallbackwithinstance)无障碍多实例场景第三方平台注册回调函数。[void OH_ArkUI_SendAccessibilityAsyncEvent(ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityEventInfo* eventInfo,void (*callback)(int32_t errorCode))](#ZH-CN_TOPIC_0000002529285069__oh_arkui_sendaccessibilityasyncevent)主动上报事件接口，通知无障碍服务。[ArkUI_AccessibilityElementInfo* OH_ArkUI_AddAndGetAccessibilityElementInfo(ArkUI_AccessibilityElementInfoList* list)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_addandgetaccessibilityelementinfo)在指定的list中增加element成员，并返回element结构。[int32_t OH_ArkUI_AccessibilityElementInfoSetElementId(ArkUI_AccessibilityElementInfo* elementInfo, int32_t elementId)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetelementid)为ArkUI_AccessibilityElementInfo设置componentId。[int32_t OH_ArkUI_AccessibilityElementInfoSetParentId(ArkUI_AccessibilityElementInfo* elementInfo, int32_t parentId)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetparentid)为ArkUI_AccessibilityElementInfo设置parentId。[int32_t OH_ArkUI_AccessibilityElementInfoSetComponentType(ArkUI_AccessibilityElementInfo* elementInfo, const char* componentType)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetcomponenttype)为ArkUI_AccessibilityElementInfo设置组件类型。[int32_t OH_ArkUI_AccessibilityElementInfoSetContents(ArkUI_AccessibilityElementInfo* elementInfo, const char* contents)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetcontents)为ArkUI_AccessibilityElementInfo设置组件文本内容。[int32_t OH_ArkUI_AccessibilityElementInfoSetHintText(ArkUI_AccessibilityElementInfo* elementInfo, const char* hintText)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosethinttext)为ArkUI_AccessibilityElementInfo设置提示文本。[int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityText(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityText)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetaccessibilitytext)为ArkUI_AccessibilityElementInfo设置Accessibility文本。[int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityDescription(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityDescription)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetaccessibilitydescription)为ArkUI_AccessibilityElementInfo设置Accessibility描述信息。[int32_t OH_ArkUI_AccessibilityElementInfoSetChildNodeIds(ArkUI_AccessibilityElementInfo* elementInfo, int32_t childCount, int64_t* childNodeIds)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetchildnodeids)为ArkUI_AccessibilityElementInfo设置childCount和childNodeIds。[int32_t OH_ArkUI_AccessibilityElementInfoSetOperationActions(ArkUI_AccessibilityElementInfo* elementInfo,int32_t operationCount, ArkUI_AccessibleAction* operationActions)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetoperationactions)为ArkUI_AccessibilityElementInfo设置operationActions。[int32_t OH_ArkUI_AccessibilityElementInfoSetScreenRect(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleRect* screenRect)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetscreenrect)为ArkUI_AccessibilityElementInfo设置屏幕区域。[int32_t OH_ArkUI_AccessibilityElementInfoSetCheckable(ArkUI_AccessibilityElementInfo* elementInfo, bool checkable)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetcheckable)为ArkUI_AccessibilityElementInfo设置是否可查。[int32_t OH_ArkUI_AccessibilityElementInfoSetChecked(ArkUI_AccessibilityElementInfo* elementInfo, bool checked)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetchecked)为ArkUI_AccessibilityElementInfo设置是否被检查。[int32_t OH_ArkUI_AccessibilityElementInfoSetFocusable(ArkUI_AccessibilityElementInfo* elementInfo, bool focusable)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetfocusable)为ArkUI_AccessibilityElementInfo设置是否可聚焦。[int32_t OH_ArkUI_AccessibilityElementInfoSetFocused(ArkUI_AccessibilityElementInfo* elementInfo, bool isFocused)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetfocused)为ArkUI_AccessibilityElementInfo设置是否聚焦。[int32_t OH_ArkUI_AccessibilityElementInfoSetVisible(ArkUI_AccessibilityElementInfo* elementInfo, bool isVisible)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetvisible)为ArkUI_AccessibilityElementInfo设置是否可见。[int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityFocused(ArkUI_AccessibilityElementInfo* elementInfo, bool accessibilityFocused)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetaccessibilityfocused)为ArkUI_AccessibilityElementInfo设置accessibilityFocused。[int32_t OH_ArkUI_AccessibilityElementInfoSetSelected(ArkUI_AccessibilityElementInfo* elementInfo, bool selected)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetselected)为ArkUI_AccessibilityElementInfo设置是否被选中。[int32_t OH_ArkUI_AccessibilityElementInfoSetClickable(ArkUI_AccessibilityElementInfo* elementInfo, bool clickable)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetclickable)为ArkUI_AccessibilityElementInfo设置是否支持点击。[int32_t OH_ArkUI_AccessibilityElementInfoSetLongClickable(ArkUI_AccessibilityElementInfo* elementInfo, bool longClickable)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetlongclickable)为ArkUI_AccessibilityElementInfo设置是否支持长按。[int32_t OH_ArkUI_AccessibilityElementInfoSetEnabled(ArkUI_AccessibilityElementInfo* elementInfo, bool isEnabled)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetenabled)为ArkUI_AccessibilityElementInfo设置是否启用。[int32_t OH_ArkUI_AccessibilityElementInfoSetIsPassword(ArkUI_AccessibilityElementInfo* elementInfo, bool isPassword)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetispassword)为ArkUI_AccessibilityElementInfo设置是否为密码。[int32_t OH_ArkUI_AccessibilityElementInfoSetScrollable(ArkUI_AccessibilityElementInfo* elementInfo, bool scrollable)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetscrollable)为ArkUI_AccessibilityElementInfo设置是否支持滚动。[int32_t OH_ArkUI_AccessibilityElementInfoSetEditable(ArkUI_AccessibilityElementInfo* elementInfo, bool editable)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfoseteditable)为ArkUI_AccessibilityElementInfo设置是否支持编辑。[int32_t OH_ArkUI_AccessibilityElementInfoSetIsHint(ArkUI_AccessibilityElementInfo* elementInfo, bool isHint)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetishint)为ArkUI_AccessibilityElementInfo设置isHint。[int32_t OH_ArkUI_AccessibilityElementInfoSetRangeInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleRangeInfo* rangeInfo)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetrangeinfo)为ArkUI_AccessibilityElementInfo设置rangeInfo。[int32_t OH_ArkUI_AccessibilityElementInfoSetGridInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleGridInfo* gridInfo)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetgridinfo)为ArkUI_AccessibilityElementInfo设置gridInfo。[int32_t OH_ArkUI_AccessibilityElementInfoSetGridItemInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleGridItemInfo* gridItem)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetgriditeminfo)为ArkUI_AccessibilityElementInfo设置gridItem。[int32_t OH_ArkUI_AccessibilityElementInfoSetSelectedTextStart(ArkUI_AccessibilityElementInfo* elementInfo, int32_t selectedTextStart)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetselectedtextstart)为ArkUI_AccessibilityElementInfo设置selectedTextStart。[int32_t OH_ArkUI_AccessibilityElementInfoSetSelectedTextEnd(ArkUI_AccessibilityElementInfo* elementInfo, int32_t selectedTextEnd)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetselectedtextend)为ArkUI_AccessibilityElementInfo设置selectedTextEnd。[int32_t OH_ArkUI_AccessibilityElementInfoSetCurrentItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t currentItemIndex)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetcurrentitemindex)为ArkUI_AccessibilityElementInfo设置currentItemIndex。[int32_t OH_ArkUI_AccessibilityElementInfoSetStartItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t startItemIndex)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetstartitemindex)为ArkUI_AccessibilityElementInfo设置startItemIndex。[int32_t OH_ArkUI_AccessibilityElementInfoSetEndItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t endItemIndex)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetenditemindex)为ArkUI_AccessibilityElementInfo设置endItemIndex。[int32_t OH_ArkUI_AccessibilityElementInfoSetItemCount(ArkUI_AccessibilityElementInfo* elementInfo, int32_t itemCount)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetitemcount)为ArkUI_AccessibilityElementInfo设置itemCount。[int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityOffset(ArkUI_AccessibilityElementInfo* elementInfo, int32_t offset)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetaccessibilityoffset)为ArkUI_AccessibilityElementInfo设置offset。[int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityGroup(ArkUI_AccessibilityElementInfo* elementInfo, bool accessibilityGroup)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetaccessibilitygroup)为ArkUI_AccessibilityElementInfo设置无障碍分组。[int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityLevel(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityLevel)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetaccessibilitylevel)为ArkUI_AccessibilityElementInfo设置无障碍重要性。[int32_t OH_ArkUI_AccessibilityElementInfoSetZIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t zIndex)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetzindex)为ArkUI_AccessibilityElementInfo设置zIndex。[int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityOpacity(ArkUI_AccessibilityElementInfo* elementInfo, float opacity)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetaccessibilityopacity)为ArkUI_AccessibilityElementInfo设置透明度。[int32_t OH_ArkUI_AccessibilityElementInfoSetBackgroundColor(ArkUI_AccessibilityElementInfo* elementInfo, const char* backgroundColor)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetbackgroundcolor)为ArkUI_AccessibilityElementInfo设置背景色。[int32_t OH_ArkUI_AccessibilityElementInfoSetBackgroundImage(ArkUI_AccessibilityElementInfo* elementInfo, const char* backgroundImage)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetbackgroundimage)为ArkUI_AccessibilityElementInfo设置背景图。[int32_t OH_ArkUI_AccessibilityElementInfoSetBlur(ArkUI_AccessibilityElementInfo* elementInfo, const char* blur)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosetblur)为ArkUI_AccessibilityElementInfo设置模糊度。[int32_t OH_ArkUI_AccessibilityElementInfoSetHitTestBehavior(ArkUI_AccessibilityElementInfo* elementInfo, const char* hitTestBehavior)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityelementinfosethittestbehavior)为ArkUI_AccessibilityElementInfo设置hitTest模式。[ArkUI_AccessibilityElementInfo* OH_ArkUI_CreateAccessibilityElementInfo(void)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_createaccessibilityelementinfo)创建一个ArkUI_AccessibilityElementInfo对象，创建后需要调用OH_ArkUI_DestoryAccessibilityElementInfo释放。[void OH_ArkUI_DestoryAccessibilityElementInfo(ArkUI_AccessibilityElementInfo* elementInfo)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_destoryaccessibilityelementinfo)销毁一个ArkUI_AccessibilityElementInfo对象。[ArkUI_AccessibilityEventInfo* OH_ArkUI_CreateAccessibilityEventInfo(void)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_createaccessibilityeventinfo)创建一个ArkUI_AccessibilityEventInfo对象，创建后需要调用OH_ArkUI_DestoryAccessibilityEventInfo释放。[void OH_ArkUI_DestoryAccessibilityEventInfo(ArkUI_AccessibilityEventInfo* eventInfo)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_destoryaccessibilityeventinfo)销毁ArkUI_AccessibilityEventInfo对象。[int32_t OH_ArkUI_AccessibilityEventSetEventType(ArkUI_AccessibilityEventInfo* eventInfo, ArkUI_AccessibilityEventType eventType)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityeventseteventtype)为ArkUI_AccessibilityEventInfo设置事件类型。[int32_t OH_ArkUI_AccessibilityEventSetTextAnnouncedForAccessibility(ArkUI_AccessibilityEventInfo* eventInfo, const char* textAnnouncedForAccessibility)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityeventsettextannouncedforaccessibility)为ArkUI_AccessibilityEventInfo设置textAnnouncedForAccessibility。[int32_t OH_ArkUI_AccessibilityEventSetRequestFocusId(ArkUI_AccessibilityEventInfo* eventInfo, int32_t requestFocusId)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityeventsetrequestfocusid)为ArkUI_AccessibilityEventInfo设置requestFocusId。[int32_t OH_ArkUI_AccessibilityEventSetElementInfo(ArkUI_AccessibilityEventInfo* eventInfo, ArkUI_AccessibilityElementInfo* elementInfo)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_accessibilityeventsetelementinfo)为ArkUI_AccessibilityEventInfo设置elementInfo。[int32_t OH_ArkUI_FindAccessibilityActionArgumentByKey(ArkUI_AccessibilityActionArguments* arguments, const char* key, char** value)](#ZH-CN_TOPIC_0000002529285069__oh_arkui_findaccessibilityactionargumentbykey)获取ArkUI_AccessibilityActionArguments中指定key的value值。

#### 枚举类型说明

#### ArkUI_Accessibility_ActionType

```ets
enum ArkUI_Accessibility_ActionType
```

**描述：**

Accessibility操作类型的枚举。

**起始版本：** 13

枚举项描述ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_INVALID = 0无效值。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_CLICK = 0x00000010收到事件后，组件需要对点击做出响应。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_LONG_CLICK = 0x00000020收到事件后，组件需要对长点击做出响应。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_GAIN_ACCESSIBILITY_FOCUS = 0x00000040表示获取辅助功能焦点的操作，特定组件已聚焦。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_CLEAR_ACCESSIBILITY_FOCUS = 0x00000080表示清除辅助功能焦点的操作。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_SCROLL_FORWARD = 0x00000100滚动组件响应向前滚动动作。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_SCROLL_BACKWARD = 0x00000200滚动组件响应反向滚动操作。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_COPY = 0x00000400复制文本组件的选定内容。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_PASTE = 0x00000800粘贴文本组件的选定内容。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_CUT = 0x00001000剪切文本组件的选定内容。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_SELECT_TEXT = 0x00002000针对文本组件进行选择操作。结合ArkUI_AccessibilityActionArguments使用，配置selectTextStart，selectTextEnd，selectTextInForWard。进入编辑区选择一段文本内容。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_SET_TEXT = 0x00004000设置文本组件的文本内容。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_SET_CURSOR_POSITION = 0x00100000针对文本组件设置光标位置。结合ArkUI_AccessibilityActionArguments使用，配置offset设置位置。ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_NEXT_HTML_ITEM = 0x02000000

焦点移动操作中支持查找下一个焦点。此处的HTML并不代表网页元素，仅用于表示具有可自行查找下一个可见聚焦组件的能力，与Web支持的能力相似。实现findNextFocusAccessibilityNode的能力才可配置该属性。

**起始版本：** 15

ARKUI_ACCESSIBILITY_NATIVE_ACTION_TYPE_PREVIOUS_HTML_ITEM = 0x04000000

焦点移动操作中支持查找上一个焦点。此处的HTML并不代表网页元素，仅用于表示具有可自行查找上一个可见聚焦组件的能力，与Web支持的能力相似。实现findNextFocusAccessibilityNode的能力才可配置该属性。

**起始版本：** 15

#### ArkUI_AccessibilityEventType

```ets
enum ArkUI_AccessibilityEventType
```

**描述：**

Accessibility事件类型的枚举。

**起始版本：** 13

枚举项描述ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_INVALID = 0无效值。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_CLICKED = 0x00000001点击事件，在UI组件响应后发送。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_LONG_CLICKED = 0x00000002长点击事件，在UI组件响应后发送。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_SELECTED = 0x00000004被选中事件，控件响应完成后发送。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_TEXT_UPDATE = 0x00000010文本更新事件，需要在文本更新时发送。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_PAGE_STATE_UPDATE = 0x00000020页面更新事件，当页面跳转、切换、大小更改或移动时发送。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_PAGE_CONTENT_UPDATE = 0x00000800页面内容发生变化时需要发送事件。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_SCROLLED = 0x000001000scrolled事件，当可滚动的组件上发生滚动事件时，会发送此事件。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_ACCESSIBILITY_FOCUSED = 0x00008000Accessibility焦点事件，在UI组件响应后发送。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_ACCESSIBILITY_FOCUS_CLEARED = 0x00010000Accessibility焦点清除事件，在UI组件响应后发送。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_REQUEST_ACCESSIBILITY_FOCUS = 0x02000000主动请求指定节点聚焦。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_PAGE_OPEN = 0x20000000UI组件上报页面打开事件。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_PAGE_CLOSE = 0x08000000UI组件上报页面关闭事件。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_ANNOUNCE_FOR_ACCESSIBILITY = 0x10000000广播Accessibility事件，请求主动播放指定的内容事件。ARKUI_ACCESSIBILITY_NATIVE_EVENT_TYPE_FOCUS_NODE_UPDATE = 0x10000001焦点更新事件，用于焦点更新场景。

#### ArkUI_AcessbilityErrorCode

```ets
enum ArkUI_AcessbilityErrorCode
```

**描述：**

Accessibility错误代码状态的枚举。

**起始版本：** 13

枚举项描述ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL = 0成功。ARKUI_ACCESSIBILITY_NATIVE_RESULT_FAILED = -1失败。ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER = -2无效参数。ARKUI_ACCESSIBILITY_NATIVE_RESULT_OUT_OF_MEMORY = -3内存不足。

#### ArkUI_AccessibilitySearchMode

```ets
enum ArkUI_AccessibilitySearchMode
```

**描述：**

Accessibility搜索类型的枚举。

**起始版本：** 13

枚举项描述ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_CURRENT = 0查询当前节点。ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_PREDECESSORS = 1 << 0查询父节点。ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_SIBLINGS = 1 << 1查询兄弟节点。ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_CHILDREN = 1 << 2查询下一层孩子节点。ARKUI_ACCESSIBILITY_NATIVE_SEARCH_MODE_PREFETCH_RECURSIVE_CHILDREN = 1 << 3查询所有孩子节点。

#### ArkUI_AccessibilityFocusType

```ets
enum ArkUI_AccessibilityFocusType
```

**描述：**

Accessibility焦点类型的枚举。

**起始版本：** 13

枚举项描述ARKUI_ACCESSIBILITY_NATIVE_FOCUS_TYPE_INVALID = -1无效值。ARKUI_ACCESSIBILITY_NATIVE_FOCUS_TYPE_INPUT = 1 << 0输入焦点类型。ARKUI_ACCESSIBILITY_NATIVE_FOCUS_TYPE_ACCESSIBILITY = 1 << 1Accessibility焦点类型。

#### ArkUI_AccessibilityFocusMoveDirection

```ets
enum ArkUI_AccessibilityFocusMoveDirection
```

**描述：**

Accessibility焦点移动方向的枚举。

**起始版本：** 13

枚举项描述ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_INVALID = 0无效值。ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_UP = 0x00000001焦点向上移动。ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_DOWN = 0x00000002焦点向下移动。ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_LEFT = 0x00000004焦点向左移动。ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_RIGHT = 0x00000008焦点向右移动。ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_FORWARD = 0x00000010焦点向下一个可聚焦节点移动，基于查询请求中指定的基准节点。ARKUI_ACCESSIBILITY_NATIVE_DIRECTION_BACKWARD = 0x00000020焦点向上一个可聚焦节点移动，基于查询请求中指定的基准节点。

#### 函数说明

#### OH_ArkUI_AccessibilityProviderRegisterCallback()

```ets
int32_t OH_ArkUI_AccessibilityProviderRegisterCallback(ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityProviderCallbacks* callbacks)
```

**描述：**

第三方操作provider回调函数结构定义，需要第三方平台实现的相关函数，通过OH_ArkUI_AccessibilityProviderRegisterCallback注册到系统侧。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityProvider](ArkUI_AccessibilityProvider.md)* provider表示指向ArkUI_AccessibilityProvider实例的指针。[ArkUI_AccessibilityProviderCallbacks](ArkUI_AccessibilityProviderCallbacks.md)* callbacks表示指向GetAccessibilityNodeCursorPosition实例的指针。

**返回：**

类型说明int32_t

如果操作成功，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

如果参数错误，则返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance()

```ets
int32_t OH_ArkUI_AccessibilityProviderRegisterCallbackWithInstance(const char* instanceId, ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityProviderCallbacksWithInstance* callbacks)
```

**描述：**

无障碍多实例场景第三方平台注册回调函数。

**起始版本：** 15

**参数：**

参数项描述const char* instanceId第三方平台接入的实例ID，用于区分多实例场景中不同的第三方实例，ID由第三方平台指定与维护。[ArkUI_AccessibilityProvider](ArkUI_AccessibilityProvider.md)* provider第三方平台接入provider句柄。[ArkUI_AccessibilityProviderCallbacksWithInstance](ArkUI_AccessibilityProviderCallbacksWithInstance.md)* callbacks表示指向ArkUI_AccessibilityProviderCallbacksWithInstance实例的指针。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_SendAccessibilityAsyncEvent()

```ets
void OH_ArkUI_SendAccessibilityAsyncEvent(ArkUI_AccessibilityProvider* provider, ArkUI_AccessibilityEventInfo* eventInfo, void (*callback)(int32_t errorCode))
```

**描述：**

主动上报事件接口，通知无障碍服务。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityProvider](ArkUI_AccessibilityProvider.md)* provider第三方平台接入provider句柄。[ArkUI_AccessibilityEventInfo](ArkUI_AccessibilityEventInfo.md)* eventInfo表示指向Accessibility事件信息的指针。void (*callback)(int32_t errorCode)表示指向SendAccessibilityAsyncEvent的回调。

#### OH_ArkUI_AddAndGetAccessibilityElementInfo()

```ets
ArkUI_AccessibilityElementInfo* OH_ArkUI_AddAndGetAccessibilityElementInfo(ArkUI_AccessibilityElementInfoList* list)
```

**描述：**

在指定的list中增加element成员，并返回element结构。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfoList](ArkUI_AccessibilityElementInfoList.md)* list指定的ArkUI_AccessibilityElementInfoList结构，新创建的ElementInfo成员加入该list后返回给函数调用方。

**返回：**

类型说明[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)*返回创建完成的ArkUI_AccessibilityElementInfo结构指针；如果创建失败，则返回NULL。

#### OH_ArkUI_AccessibilityElementInfoSetElementId()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetElementId(ArkUI_AccessibilityElementInfo* elementInfo, int32_t elementId)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置componentId。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfoArkUI_AccessibilityElementInfo指针。int32_t elementId无障碍元素的唯一编号。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetParentId()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetParentId(ArkUI_AccessibilityElementInfo* elementInfo, int32_t parentId)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置parentId。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t parentId表示元素的父组件无障碍编号。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetComponentType()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetComponentType(ArkUI_AccessibilityElementInfo* elementInfo, const char* componentType)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置组件类型。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。const char* componentType表示元素所属的组件类型。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetContents()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetContents(ArkUI_AccessibilityElementInfo* elementInfo, const char* contents)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置组件文本内容。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。const char* contents表示元素被无障碍服务所识别的文本内容。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetHintText()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetHintText(ArkUI_AccessibilityElementInfo* elementInfo, const char* hintText)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置提示文本。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。const char* hintText表示提示文本。 默认为""。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetAccessibilityText()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityText(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityText)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置Accessibility文本。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。const char* accessibilityText表示Accessibility文本。默认为""。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetAccessibilityDescription()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityDescription(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityDescription)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置Accessibility描述信息。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。const char* accessibilityDescription表示Accessibility描述信息。 默认为""。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetChildNodeIds()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetChildNodeIds(ArkUI_AccessibilityElementInfo* elementInfo, int32_t childCount, int64_t* childNodeIds)
```

**描述：**

设置ArkUI_AccessibilityElementInfo的childCount和childNodeIds。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t childCount表示孩子节点数量。默认值为0。int64_t* childNodeIds表示孩子节点id集合。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetOperationActions()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetOperationActions(ArkUI_AccessibilityElementInfo* elementInfo,int32_t operationCount, ArkUI_AccessibleAction* operationActions)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置operationActions。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t* operationCount组件支持的action数量。[ArkUI_AccessibleAction](ArkUI_AccessibleAction.md)* operationActions组件支持的action。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetScreenRect()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetScreenRect(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleRect* screenRect)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置屏幕区域。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。[ArkUI_AccessibleRect](ArkUI_AccessibleRect.md)* screenRect表示屏幕区域。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetCheckable()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetCheckable(ArkUI_AccessibilityElementInfo* elementInfo, bool checkable)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否可查。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool checkable表示是否可查。true表示可查，false表示不可查。默认值为false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetChecked()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetChecked(ArkUI_AccessibilityElementInfo* elementInfo, bool checked)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否被检查。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool checked表示是否被检查。true表示被检查过，false表示未被检查。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetFocusable()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetFocusable(ArkUI_AccessibilityElementInfo* elementInfo, bool focusable)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否可聚焦。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool focusable表示是否可聚焦。true表示可聚焦，false表示不可聚焦。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetFocused()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetFocused(ArkUI_AccessibilityElementInfo* elementInfo, bool isFocused)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否聚焦。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool isFocused表示是否聚焦。true表示已聚焦，false表示未聚焦。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetVisible()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetVisible(ArkUI_AccessibilityElementInfo* elementInfo, bool isVisible)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否可见。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool isVisible表示是否可见。true表示可见，false表示不可见。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetAccessibilityFocused()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityFocused(ArkUI_AccessibilityElementInfo* elementInfo, bool accessibilityFocused)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置accessibilityFocused。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool accessibilityFocused表示是否被无障碍聚焦。true表示被无障碍聚焦，false表示未被无障碍聚焦。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetSelected()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetSelected(ArkUI_AccessibilityElementInfo* elementInfo, bool selected)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否被选中。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool selected表示是否被选中。true表示被选中，false表示未选中。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetClickable()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetClickable(ArkUI_AccessibilityElementInfo* elementInfo, bool clickable)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否支持点击。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool clickable表示是否支持点击。true表示支持，false表示不支持。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetLongClickable()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetLongClickable(ArkUI_AccessibilityElementInfo* elementInfo, bool longClickable)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否支持长按。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool longClickable表示是否支持长按。true表示支持，false表示不支持。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetEnabled()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetEnabled(ArkUI_AccessibilityElementInfo* elementInfo, bool isEnabled)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否启用。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool isEnabled表示是否启用。true表示启用，false表示未启用。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetIsPassword()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetIsPassword(ArkUI_AccessibilityElementInfo* elementInfo, bool isPassword)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否为密码。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool isPassword表示是否为密码。true表示是密码，false表示不是密码。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetScrollable()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetScrollable(ArkUI_AccessibilityElementInfo* elementInfo, bool scrollable)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否支持滚动。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool scrollable表示是否支持滚动。true表示支持，false表示不支持。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetEditable()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetEditable(ArkUI_AccessibilityElementInfo* elementInfo, bool editable)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置是否支持编辑。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool editable表示是否支持编辑。true表示支持，false表示不支持。默认值false。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetIsHint()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetIsHint(ArkUI_AccessibilityElementInfo* elementInfo, bool isHint)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置isHint。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool isHint表示是否为提示状态。true表示是提示状态，false表示不是提示状态。在提示状态下才会获取hintText信息。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetRangeInfo()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetRangeInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleRangeInfo* rangeInfo)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置rangeInfo。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfode的指针。[ArkUI_AccessibleRangeInfo](ArkUI_AccessibleRangeInfo.md)* rangeInfo表示特定组件的当前值、最大值、最小值。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetGridInfo()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetGridInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleGridInfo* gridInfo)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置gridInfo。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。[ArkUI_AccessibleGridInfo](ArkUI_AccessibleGridInfo.md)* gridInfo表示特定组件的行数、列数以及选择模式。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetGridItemInfo()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetGridItemInfo(ArkUI_AccessibilityElementInfo* elementInfo, ArkUI_AccessibleGridItemInfo* gridItem)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置gridItem。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。[ArkUI_AccessibleGridItemInfo](ArkUI_AccessibleGridItemInfo.md)* gridItem表示特定组件的属性值。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetSelectedTextStart()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetSelectedTextStart(ArkUI_AccessibilityElementInfo* elementInfo, int32_t selectedTextStart)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置selectedTextStart。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t selectedTextStart文本类控件使用，设置选中文本的起始位置。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetSelectedTextEnd()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetSelectedTextEnd(ArkUI_AccessibilityElementInfo* elementInfo, int32_t selectedTextEnd)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置selectedTextEnd。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t selectedTextEnd文本类控件使用，设置选中文本的结束位置。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetCurrentItemIndex()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetCurrentItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t currentItemIndex)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置currentItemIndex。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t currentItemIndex当前获焦控件的位置信息。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetStartItemIndex()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetStartItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t startItemIndex)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置startItemIndex。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t startItemIndex当前屏幕中显示的第一个元素的位置信息。List、Select、Swiper、Tab_Bar等组件使用。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetEndItemIndex()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetEndItemIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t endItemIndex)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置endItemIndex。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t endItemIndex当前屏幕中显示的最后一个元素的位置信息。List、Select、Swiper、Tab_Bar等组件使用。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetItemCount()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetItemCount(ArkUI_AccessibilityElementInfo* elementInfo, int32_t itemCount)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置itemCount。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t itemCount表示特定组件的元素总数。如List、Select、Swiper、Tab_Bar等组件使用。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetAccessibilityOffset()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityOffset(ArkUI_AccessibilityElementInfo* elementInfo, int32_t offset)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置offset。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t offset对于可滚动类控件，如List、Grid，内容区相对于元素顶部坐标的滚动像素偏移量。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetAccessibilityGroup()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityGroup(ArkUI_AccessibilityElementInfo* elementInfo, bool accessibilityGroup)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置无障碍分组。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。bool accessibilityGroup表示是否启用无障碍分组。true表示启用，false表示不启用。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetAccessibilityLevel()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityLevel(ArkUI_AccessibilityElementInfo* elementInfo, const char* accessibilityLevel)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置无障碍重要性。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。const char* accessibilityLevel

表示组件的无障碍重要性，用于控制某个组件是否被无障碍辅助服务所识别。

- auto：由系统根据当前组件的属性自动判断该组件是否重要，决定是否让无障碍辅助服务识别该组件。

- yes：表示该组件重要，允许无障碍辅助服务识别该组件。

- no：表示该组件不重要，不允许无障碍辅助服务识别该组件。

- no-hide-descendants：表示该组件及其子孙节点都不重要，不允许无障碍辅助服务识别该组件及其子孙节点。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetZIndex()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetZIndex(ArkUI_AccessibilityElementInfo* elementInfo, int32_t zIndex)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置zIndex。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。int32_t zIndex组件z序，用于控制元素在垂直于屏幕的z轴上的位置。UITest需要使用。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetAccessibilityOpacity()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetAccessibilityOpacity(ArkUI_AccessibilityElementInfo* elementInfo, float opacity)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置透明度。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。float opacity表示透明度。其取值范围是0到1，其中1表示完全不透明，0表示完全透明。UITest需要使用。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetBackgroundColor()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetBackgroundColor(ArkUI_AccessibilityElementInfo* elementInfo, const char* backgroundColor)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置背景色。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。const char* backgroundColor表示背景色。UITest需要使用。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetBackgroundImage()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetBackgroundImage(ArkUI_AccessibilityElementInfo* elementInfo, const char* backgroundImage)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置背景图片。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。const char* backgroundImage表示背景图片。UITest需要使用。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetBlur()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetBlur(ArkUI_AccessibilityElementInfo* elementInfo, const char* blur)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置模糊度。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。const char* blur表示模糊度。UITest需要使用。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityElementInfoSetHitTestBehavior()

```ets
int32_t OH_ArkUI_AccessibilityElementInfoSetHitTestBehavior(ArkUI_AccessibilityElementInfo* elementInfo, const char* hitTestBehavior)
```

**描述：**

为ArkUI_AccessibilityElementInfo设置hitTest模式。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。const char* hitTestBehavior表示hitTest模式，取值范围参考[HitTestMode](枚举说明.md#ZH-CN_TOPIC_0000002529284967__hittestmode9)。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_CreateAccessibilityElementInfo()

```ets
ArkUI_AccessibilityElementInfo* OH_ArkUI_CreateAccessibilityElementInfo(void)
```

**描述：**

创建一个ArkUI_AccessibilityElementInfo对象，创建后需要调用OH_ArkUI_DestoryAccessibilityElementInfo释放。

**起始版本：** 13

**返回：**

类型说明[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)*返回ArkUI_AccessibilityElementInfo对象。

#### OH_ArkUI_DestoryAccessibilityElementInfo()

```ets
void OH_ArkUI_DestoryAccessibilityElementInfo(ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

销毁一个ArkUI_AccessibilityElementInfo对象。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示指向ArkUI_AccessibilityElementInfo的指针。

#### OH_ArkUI_CreateAccessibilityEventInfo()

```ets
ArkUI_AccessibilityEventInfo* OH_ArkUI_CreateAccessibilityEventInfo(void)
```

**描述：**

创建一个ArkUI_AccessibilityEventInfo对象，创建后需要调用OH_ArkUI_DestoryAccessibilityEventInfo释放。

**起始版本：** 13

**返回：**

类型说明[ArkUI_AccessibilityEventInfo](ArkUI_AccessibilityEventInfo.md)*返回ArkUI_AccessibilityEventInfo对象。

#### OH_ArkUI_DestoryAccessibilityEventInfo()

```ets
void OH_ArkUI_DestoryAccessibilityEventInfo(ArkUI_AccessibilityEventInfo* eventInfo)
```

**描述：**

销毁ArkUI_AccessibilityEventInfo对象。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityEventInfo](ArkUI_AccessibilityEventInfo.md)* eventInfo需要被销毁的ArkUI_AccessibilityEventInfo对象。

#### OH_ArkUI_AccessibilityEventSetEventType()

```ets
int32_t OH_ArkUI_AccessibilityEventSetEventType(ArkUI_AccessibilityEventInfo* eventInfo,  ArkUI_AccessibilityEventType eventType)
```

**描述：**

为ArkUI_AccessibilityEventInfo设置事件类型。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityEventInfo](ArkUI_AccessibilityEventInfo.md)* eventInfo表示事件信息。[ArkUI_AccessibilityEventType](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_accessibilityeventtype) eventType表示事件类型。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityEventSetTextAnnouncedForAccessibility()

```ets
int32_t OH_ArkUI_AccessibilityEventSetTextAnnouncedForAccessibility(ArkUI_AccessibilityEventInfo* eventInfo,  const char* textAnnouncedForAccessibility)
```

**描述：**

为ArkUI_AccessibilityEventInfo设置textAnnouncedForAccessibility。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityEventInfo](ArkUI_AccessibilityEventInfo.md)* eventInfo表示事件信息。const char* textAnnouncedForAccessibility表示textAnnouncedForAccessibility。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityEventSetRequestFocusId()

```ets
int32_t OH_ArkUI_AccessibilityEventSetRequestFocusId(ArkUI_AccessibilityEventInfo* eventInfo,  int32_t requestFocusId)
```

**描述：**

为ArkUI_AccessibilityEventInfo设置requestFocusId。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityEventInfo](ArkUI_AccessibilityEventInfo.md)* eventInfo表示事件信息。int32_t requestFocusId表示请求焦点id。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_AccessibilityEventSetElementInfo()

```ets
int32_t OH_ArkUI_AccessibilityEventSetElementInfo(ArkUI_AccessibilityEventInfo* eventInfo,  ArkUI_AccessibilityElementInfo* elementInfo)
```

**描述：**

为ArkUI_AccessibilityEventInfo设置elementInfo。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityEventInfo](ArkUI_AccessibilityEventInfo.md)* eventInfo表示事件信息。[ArkUI_AccessibilityElementInfo](ArkUI_AccessibilityElementInfo.md)* elementInfo表示ArkUI_AccessibilityElementInfo元素信息。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

#### OH_ArkUI_FindAccessibilityActionArgumentByKey()

```ets
int32_t OH_ArkUI_FindAccessibilityActionArgumentByKey(ArkUI_AccessibilityActionArguments* arguments, const char* key, char** value)
```

**描述：**

获取ArkUI_AccessibilityActionArguments中指定key的value值。

**起始版本：** 13

**参数：**

参数项描述[ArkUI_AccessibilityActionArguments](ArkUI_AccessibilityActionArguments.md)* arguments表示ArkUI_AccessibilityActionArguments对象信息。const char* key表示key。char** value表示value。

**返回：**

类型说明int32_t

成功返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_SUCCESSFUL](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。

参数错误返回[ARKUI_ACCESSIBILITY_NATIVE_RESULT_BAD_PARAMETER](native_interface_accessibility.h.md#ZH-CN_TOPIC_0000002529285069__arkui_acessbilityerrorcode)。