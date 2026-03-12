# oh_window.h

#### 概述

定义窗口管理的相关接口，主要用于设置和获取指定窗口的属性，以及设置指定窗口的状态栏样式、导航栏样式。

**引用文件：** <window_manager/oh_window.h>

**库：** libnative_window_manager.so

**系统能力：** SystemCapability.Window.SessionManager

**起始版本：** 15

**相关模块：**[WindowManager](WindowManager.md)

#### 汇总

#### 函数

名称typedef关键字描述[int32_t OH_WindowManager_SetWindowStatusBarEnabled(int32_t windowId, bool enabled, bool enableAnimation)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_setwindowstatusbarenabled)-设置指定窗口是否显示状态栏。[int32_t OH_WindowManager_SetWindowStatusBarColor(int32_t windowId, int32_t color)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_setwindowstatusbarcolor)-设置指定窗口的状态栏内容颜色。[int32_t OH_WindowManager_SetWindowNavigationBarEnabled(int32_t windowId, bool enabled, bool enableAnimation)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_setwindownavigationbarenabled)-设置指定窗口是否显示导航栏。[int32_t OH_WindowManager_GetWindowAvoidArea(int32_t windowId, WindowManager_AvoidAreaType type, WindowManager_AvoidArea* avoidArea)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_getwindowavoidarea)-获取指定窗口的避让区域。[int32_t OH_WindowManager_IsWindowShown(int32_t windowId, bool* isShow)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_iswindowshown)-判断指定窗口是否显示。[int32_t OH_WindowManager_ShowWindow(int32_t windowId)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_showwindow)-显示指定窗口。[int32_t OH_WindowManager_SetWindowTouchable(int32_t windowId, bool isTouchable)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_setwindowtouchable)-设置指定窗口是否可触。[int32_t OH_WindowManager_SetWindowFocusable(int32_t windowId, bool isFocusable)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_setwindowfocusable)-设置指定窗口是否可获焦。[int32_t OH_WindowManager_SetWindowBackgroundColor(int32_t windowId, const char* color)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_setwindowbackgroundcolor)-设置指定窗口背景颜色。[int32_t OH_WindowManager_SetWindowBrightness(int32_t windowId, float brightness)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_setwindowbrightness)-设置指定窗口的屏幕亮度。[int32_t OH_WindowManager_SetWindowKeepScreenOn(int32_t windowId, bool isKeepScreenOn)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_setwindowkeepscreenon)-设置指定窗口是否开启屏幕常亮。[int32_t OH_WindowManager_SetWindowPrivacyMode(int32_t windowId, bool isPrivacy)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_setwindowprivacymode)-设置指定窗口是否开启隐私模式。[int32_t OH_WindowManager_GetWindowProperties(int32_t windowId, WindowManager_WindowProperties* windowProperties)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_getwindowproperties)-获取指定窗口属性。[int32_t OH_WindowManager_Snapshot(int32_t windowId, OH_PixelmapNative* pixelMap)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_snapshot)-获取指定窗口截图。[int32_t OH_WindowManager_GetAllWindowLayoutInfoList(int64_t displayId,WindowManager_Rect** windowLayoutInfoList, size_t* windowLayoutInfoSize)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_getallwindowlayoutinfolist)-获取指定屏幕上可见的窗口布局信息数组，按当前窗口层级排列，层级最高的对应数组下标为0。[void OH_WindowManager_ReleaseAllWindowLayoutInfoList(WindowManager_Rect* windowLayoutInfoList)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_releaseallwindowlayoutinfolist)-释放窗口布局信息数组占用的内存。[int32_t OH_WindowManager_InjectTouchEvent(int32_t windowId, Input_TouchEvent* touchEvent, int32_t windowX, int32_t windowY)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_injecttouchevent)-将多模触摸事件注入给目标窗口，仅支持注入同进程窗口，且该注入不会触发窗口焦点和层级变化，不会触发窗口拖拽，事件会直接发送给ArkUI。该接口需要在指定窗口加载UI之后调用。[int32_t OH_WindowManager_GetAllMainWindowInfo(WindowManager_MainWindowInfo** infoList, size_t* mainWindowInfoSize)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_getallmainwindowinfo)-获取全部主窗信息。[void OH_WindowManager_ReleaseAllMainWindowInfo(WindowManager_MainWindowInfo* infoList)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_releaseallmainwindowinfo)-释放主窗口信息列表的内存。[typedef void (*OH_WindowManager_WindowSnapshotCallback)(const OH_PixelmapNative** snapshotPixelMapList, size_t snapshotListSize)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_windowsnapshotcallback)OH_WindowManager_WindowSnapshotCallback接收主窗口截图列表的回调接口。[int32_t OH_WindowManager_GetMainWindowSnapshot(int32_t* windowIdList, size_t windowIdListSize, WindowManager_WindowSnapshotConfig config, OH_WindowManager_WindowSnapshotCallback callback)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_getmainwindowsnapshot)-获取一个或多个指定windowId的主窗口截图。[void OH_WindowManager_ReleaseMainWindowSnapshot(const OH_PixelmapNative* snapshotPixelMapList)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_releasemainwindowsnapshot)-释放主窗口截图列表的内存。[int32_t OH_WindowManager_LockCursor(int32_t windowId, bool isCursorFollowMovement)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_lockcursor)-锁定鼠标光标，控制鼠标光标不超过指定窗口区域，同时可控制光标是否跟随鼠标移动。仅支持获焦窗口调用，失焦之后会自动取消锁定。[int32_t OH_WindowManager_UnlockCursor(int32_t windowId)](#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_unlockcursor)-清除窗口设置的鼠标光标指定的模式。

#### 函数说明

#### OH_WindowManager_SetWindowStatusBarEnabled()

```ets
int32_t OH_WindowManager_SetWindowStatusBarEnabled(int32_t windowId, bool enabled, bool enableAnimation)
```

**描述**

设置指定窗口是否显示状态栏。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。bool enabled设置状态栏是否显示。true表示设置状态栏显示，false表示设置状态栏隐藏。bool enableAnimation设置是否开启状态栏的显隐动画。true表示开启状态栏的显隐动画，false表示关闭状态栏的显隐动画。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_DEVICE_NOT_SUPPORTED，表示不支持功能。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_SetWindowStatusBarColor()

```ets
int32_t OH_WindowManager_SetWindowStatusBarColor(int32_t windowId, int32_t color)
```

**描述**

设置指定窗口的状态栏内容颜色。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。int32_t color要设置的颜色值，格式为ARGB。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_DEVICE_NOT_SUPPORTED，表示不支持功能。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_SetWindowNavigationBarEnabled()

```ets
int32_t OH_WindowManager_SetWindowNavigationBarEnabled(int32_t windowId, bool enabled, bool enableAnimation)
```

**描述**

设置指定窗口是否显示导航栏。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。bool enabled设置导航栏是否显示。true表示设置导航栏显示，false表示设置导航栏隐藏。bool enableAnimation设置是否开启导航栏的显隐动画。true表示开启导航栏的显隐动画，false表示关闭导航栏的显隐动画。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_DEVICE_NOT_SUPPORTED，表示不支持功能。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_GetWindowAvoidArea()

```ets
int32_t OH_WindowManager_GetWindowAvoidArea(int32_t windowId, WindowManager_AvoidAreaType type, WindowManager_AvoidArea* avoidArea)
```

**描述**

获取指定窗口的避让区域。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。[WindowManager_AvoidAreaType](oh_window_comm.h.md#ZH-CN_TOPIC_0000002529285075__windowmanager_avoidareatype) type避让区域的类型。[WindowManager_AvoidArea](WindowManager_AvoidArea.md)* avoidArea返回指向指定窗口的避让区域的指针，作为出参使用。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功，返回指向对应窗口id的避让区域的指针。

 返回WINDOW_MANAGER_ERRORCODE_INVALID_PARAM，表示参数错误。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_IsWindowShown()

```ets
int32_t OH_WindowManager_IsWindowShown(int32_t windowId, bool* isShow)
```

**描述**

判断指定窗口是否显示。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。bool* isShow返回指定窗口是否显示的结果。true表示指定窗口显示，false表示指定窗口不显示，作为出参使用。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_INVALID_PARAM，表示参数错误。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

#### OH_WindowManager_ShowWindow()

```ets
int32_t OH_WindowManager_ShowWindow(int32_t windowId)
```

**描述**

显示指定窗口。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_SetWindowTouchable()

```ets
int32_t OH_WindowManager_SetWindowTouchable(int32_t windowId, bool isTouchable)
```

**描述**

设置指定窗口是否可触。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。bool isTouchable窗口是否可触。true表示窗口可触，false表示窗口不可触。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_SetWindowFocusable()

```ets
int32_t OH_WindowManager_SetWindowFocusable(int32_t windowId, bool isFocusable)
```

**描述**

设置指定窗口是否可获焦。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。bool isFocusable窗口是否可获焦。true表示窗口可获焦，false表示窗口不可获焦。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_SetWindowBackgroundColor()

```ets
int32_t OH_WindowManager_SetWindowBackgroundColor(int32_t windowId, const char* color)
```

**描述**

设置指定窗口背景颜色。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。const char* color设置窗口的背景色。该参数为字符串类型，格式为十六进制RGB或ARGB颜色。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_INVALID_PARAM，表示参数错误。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

#### OH_WindowManager_SetWindowBrightness()

```ets
int32_t OH_WindowManager_SetWindowBrightness(int32_t windowId, float brightness)
```

**描述**

指定主窗口设置窗口亮度。当窗口处于前台且获焦时，窗口亮度生效。

窗口亮度生效时只会影响当前设备屏幕亮度，无法修改虚拟屏（如投屏所在的屏幕）的屏幕亮度。

当接口入参为-1时，窗口亮度恢复为系统屏幕亮度（可以通过控制中心或快捷键调整）。

当窗口退至后台时，窗口亮度失效，可以通过控制中心或快捷键调整。不建议窗口退至后台时调用此接口，否则可能引发时序问题。

- 针对非2in1设备：当前窗口的窗口亮度生效时，控制中心调整系统屏幕亮度不生效。
- 针对2in1设备：

  - 在HarmonyOS5.0.2之前，窗口设置屏幕亮度生效时，控制中心或快捷键调整系统屏幕亮度不生效。
  - 从HarmonyOS5.0.2开始，窗口亮度与系统屏幕亮度保持一致，可以通过本接口、控制中心或者快捷键设置系统屏幕亮度。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。float brightness指定的屏幕亮度值。该参数为浮点数，取值范围为[0.0, 1.0]或-1.0。1.0表示最亮，-1.0表示恢复成设置窗口亮度前的系统控制中心亮度。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_INVALID_PARAM，表示参数错误。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_SetWindowKeepScreenOn()

```ets
int32_t OH_WindowManager_SetWindowKeepScreenOn(int32_t windowId, bool isKeepScreenOn)
```

**描述**

设置指定窗口是否开启屏幕常亮。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。bool isKeepScreenOn指定窗口是否开启屏幕常亮。true表示开启屏幕常亮，false表示关闭屏幕常亮。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_SetWindowPrivacyMode()

```ets
int32_t OH_WindowManager_SetWindowPrivacyMode(int32_t windowId, bool isPrivacy)
```

**描述**

设置指定窗口是否开启隐私模式。

**需要权限：** ohos.permission.PRIVACY_WINDOW

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。bool isPrivacy指定窗口是否开启隐私模式。true表示开启隐私模式，false表示关闭隐私模式。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

 返回WINDOW_MANAGER_ERRORCODE_NO_PERMISSION，权限校验错误。

#### OH_WindowManager_GetWindowProperties()

```ets
int32_t OH_WindowManager_GetWindowProperties(int32_t windowId, WindowManager_WindowProperties* windowProperties)
```

**描述**

获取指定窗口属性。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。[WindowManager_WindowProperties](WindowManager_WindowProperties.md)* windowProperties返回指向指定窗口的属性的指针，作为出参使用。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功，在windowProperties中返回窗口属性的指针。

 返回WINDOW_MANAGER_ERRORCODE_INVALID_PARAM，表示参数错误。

 返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

#### OH_WindowManager_Snapshot()

```ets
int32_t OH_WindowManager_Snapshot(int32_t windowId, OH_PixelmapNative* pixelMap)
```

**描述**

获取指定窗口截图。

**起始版本：** 15

**参数：**

参数项描述int32_t windowId

创建窗口时的窗口id。默认值为0。该参数为整数。

窗口id非法或者窗口已经销毁，不能获取指定窗口截图，需要传入有效的窗口id才能成功获取指定窗口截图。

请通过窗口对象调用[getWindowProperties()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)接口（ArkTS接口）获取有效的窗口id。

[OH_PixelmapNative](OH_PixelmapNative.md)* pixelMap返回指向指定窗口的截图的指针，作为出参使用。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功，在返回pixelMap中的像素图的指针。

 返回WINDOW_MANAGER_ERRORCODE_INVALID_PARAM，表示参数错误。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_GetAllWindowLayoutInfoList()

```ets
int32_t OH_WindowManager_GetAllWindowLayoutInfoList(int64_t displayId,WindowManager_Rect** windowLayoutInfoList, size_t* windowLayoutInfoSize)
```

**描述**

获取指定屏幕上可见的窗口布局信息数组，按当前窗口层级排列，层级最高的对应数组下标为0。

**起始版本：** 17

**参数：**

参数项描述int64_t displayId指定屏幕的id。请通过窗口对象调用[getWindowProperties()](Interface (Window).md#ZH-CN_TOPIC_0000002497604802__getwindowproperties9)接口（ArkTS接口）获取有效的屏幕id。[WindowManager_Rect](WindowManager_Rect.md)** windowLayoutInfoList指定屏幕上可见的窗口布局信息数组的数组指针，作为出参使用。size_t* windowLayoutInfoSize指定屏幕上可见的窗口布局信息数组长度的指针，作为出参使用。

**返回：**

类型说明int32_t

返回结果代码。

 返回OK，表示函数调用成功，返回指定屏幕上可见的窗口布局信息数组的数组指针和数组长度的指针。

 返回WINDOW_MANAGER_ERRORCODE_INVALID_PARAM，表示参数错误。

 返回WINDOW_MANAGER_ERRORCODE_DEVICE_NOT_SUPPORTED，表示不支持功能。

 返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_ReleaseAllWindowLayoutInfoList()

```ets
void OH_WindowManager_ReleaseAllWindowLayoutInfoList(WindowManager_Rect* windowLayoutInfoList)
```

**描述**

释放窗口布局信息数组占用的内存。

**起始版本：** 17

**参数：**

参数项描述[WindowManager_Rect](WindowManager_Rect.md)* windowLayoutInfoList指定屏幕上可见的窗口布局信息数组的数组指针，可通过[OH_WindowManager_GetAllWindowLayoutInfoList](oh_window.h.md#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_getallwindowlayoutinfolist)接口获取。

#### OH_WindowManager_InjectTouchEvent()

```ets
int32_t OH_WindowManager_InjectTouchEvent(int32_t windowId, Input_TouchEvent* touchEvent, int32_t windowX, int32_t windowY)
```

**描述**

将多模触摸事件注入给目标窗口，仅支持注入同进程窗口，且该注入不会触发窗口焦点和层级变化，不会触发窗口拖拽，事件会直接发送给ArkUI。该接口需要在指定窗口加载UI之后调用。

**起始版本：** 20

**参数：**

参数项描述int32_t windowId创建窗口时的窗口id。默认值为0。该参数为整数。[Input_TouchEvent](Input_TouchEvent.md)* touchEvent多模触摸事件，具体可见[Input_TouchEvent](Input_TouchEvent.md)，事件定义在oh_input_manager.h中。该参数包含的部分字段有参数限制，其中，action应为大于等于0且小于等于3的整数；id、displayX、displayY和actionTime应为不小于0的整数。以上参数不符合限制条件会返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示：窗口管理器服务异常。int32_t windowX注入事件相对于注入窗口的落点横坐标。该参数为整数。int32_t windowY注入事件相对于注入窗口的落点纵坐标。该参数为整数。

**返回：**

类型说明int32_t

返回结果代码。

返回OK，表示函数调用成功。

返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_GetAllMainWindowInfo()

```ets
int32_t OH_WindowManager_GetAllMainWindowInfo(WindowManager_MainWindowInfo** infoList, size_t* mainWindowInfoSize)
```

**描述**

获取全部主窗信息。

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**需要权限：** ohos.permission.CUSTOM_SCREEN_CAPTURE

**起始版本：** 21

**参数：**

参数项描述[WindowManager_MainWindowInfo](WindowManager_MainWindowInfo.md)** infoList指向主窗口信息列表的指针，作为出参使用。size_t* mainWindowInfoSize指向主窗口信息数组长度的指针，作为出参使用。

**返回：**

类型说明int32_t

返回结果代码。

返回OK，表示函数调用成功。

返回WINDOW_MANAGER_ERRORCODE_NO_PERMISSION，权限校验错误。

返回WINDOW_MANAGER_ERRORCODE_DEVICE_NOT_SUPPORTED，表示不支持功能。

返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_ReleaseAllMainWindowInfo()

```ets
void OH_WindowManager_ReleaseAllMainWindowInfo(WindowManager_MainWindowInfo* infoList)
```

**描述**

释放主窗口信息列表的内存。

**起始版本：** 21

**参数：**

参数项描述[WindowManager_MainWindowInfo](WindowManager_MainWindowInfo.md)* infoList主窗信息列表。

#### OH_WindowManager_WindowSnapshotCallback()

```ets
typedef void (*OH_WindowManager_WindowSnapshotCallback)(const OH_PixelmapNative** snapshotPixelMapList, size_t snapshotListSize)
```

**描述**

接收主窗口截图列表的回调接口。

**起始版本：** 21

**参数：**

参数项描述[const OH_PixelmapNative](OH_PixelmapNative.md)** snapshotPixelMapList窗口截图列表。size_t snapshotListSize窗口截图列表的大小。

#### OH_WindowManager_GetMainWindowSnapshot()

```ets
int32_t OH_WindowManager_GetMainWindowSnapshot(int32_t* windowIdList, size_t windowIdListSize, WindowManager_WindowSnapshotConfig config, OH_WindowManager_WindowSnapshotCallback callback)
```

**描述**

获取一个或多个指定windowId的主窗口截图。

**设备行为差异：** 该接口在2in1设备中可正常调用，在其他设备中返回801错误码。

**需要权限：** ohos.permission.CUSTOM_SCREEN_CAPTURE

**起始版本：** 21

**参数：**

参数项描述int32_t* windowIdList需要获取截图的主窗口ID列表。size_t windowIdListSize主窗口ID列表的长度。[WindowManager_WindowSnapshotConfig](WindowManager_WindowSnapshotConfig.md) config获取窗口截图时的配置信息。[OH_WindowManager_WindowSnapshotCallback](oh_window.h.md#ZH-CN_TOPIC_0000002497445104__oh_windowmanager_windowsnapshotcallback) callback获取窗口截图的回调对象。用于返回窗口截图列表，并按照指定的窗口ID列表顺序排列。

**返回：**

类型说明int32_t

返回结果代码。

返回OK，表示函数调用成功。

返回WINDOW_MANAGER_ERRORCODE_NO_PERMISSION，权限校验错误。

返回WINDOW_MANAGER_ERRORCODE_DEVICE_NOT_SUPPORTED，表示不支持功能。

返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_ReleaseMainWindowSnapshot()

```ets
void OH_WindowManager_ReleaseMainWindowSnapshot(const OH_PixelmapNative* snapshotPixelMapList)
```

**描述**

释放主窗口截图列表的内存。

**起始版本：** 21

**参数：**

参数项描述[const OH_PixelmapNative](OH_PixelmapNative.md)* snapshotPixelMapList窗口截图列表。

#### OH_WindowManager_LockCursor()

```ets
int32_t OH_WindowManager_LockCursor(int32_t windowId, bool isCursorFollowMovement)
```

**描述**

锁定鼠标光标，控制鼠标光标不超过指定窗口区域，同时可控制光标是否跟随鼠标移动。仅支持获焦窗口调用，失焦之后会自动取消锁定。

**需要权限：** ohos.permission.LOCK_WINDOW_CURSOR

**起始版本：** 22

**参数：**

参数项描述int32_t windowId创建窗口时的窗口ID。该参数为整数。bool isCursorFollowMovement设置鼠标光标的锁定模式，若为true，则光标会跟随鼠标移动；若为false，则光标不会跟随鼠标移动。

**返回：**

类型说明int32_t

返回结果代码。

返回OK，表示函数调用成功。

返回WINDOW_MANAGER_ERRORCODE_NO_PERMISSION，表示没有权限调用该接口。

返回WINDOW_MANAGER_ERRORCODE_DEVICE_NOT_SUPPORTED，表示不支持该设备。

返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。

#### OH_WindowManager_UnlockCursor()

```ets
int32_t OH_WindowManager_UnlockCursor(int32_t windowId)
```

**描述**

清除窗口设置的鼠标光标指定的模式。

**需要权限：** ohos.permission.LOCK_WINDOW_CURSOR

**起始版本：** 22

**参数：**

参数项描述int32_t windowId创建窗口时的窗口ID。该参数为整数。

**返回：**

类型说明int32_t

返回结果代码。

返回OK，表示函数调用成功。

返回WINDOW_MANAGER_ERRORCODE_NO_PERMISSION，表示没有权限调用该接口。

返回WINDOW_MANAGER_ERRORCODE_DEVICE_NOT_SUPPORTED，表示不支持该设备。

返回WINDOW_MANAGER_ERRORCODE_STATE_ABNORMAL，表示窗口状态异常。

返回WINDOW_MANAGER_ERRORCODE_SYSTEM_ABNORMAL，表示窗口管理器服务异常。