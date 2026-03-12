# oh_display_info.h

#### 概述

提供屏幕的公共枚举、公共定义等。

**引用文件：** <window_manager/oh_display_info.h>

**库：** libnative_display_manager.so

**系统能力：** SystemCapability.WindowManager.WindowManager.Core

**起始版本：** 12

**相关模块：**[OH_DisplayManager](OH_DisplayManager.md)

#### 汇总

#### 结构体

名称typedef关键字描述[NativeDisplayManager_Rect](NativeDisplayManager_Rect.md)NativeDisplayManager_Rect矩形区域。[NativeDisplayManager_WaterfallDisplayAreaRects](NativeDisplayManager_WaterfallDisplayAreaRects.md)NativeDisplayManager_WaterfallDisplayAreaRects瀑布屏曲面部分显示区域。[NativeDisplayManager_CutoutInfo](NativeDisplayManager_CutoutInfo.md)NativeDisplayManager_CutoutInfo挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。[NativeDisplayManager_DisplayHdrFormat](NativeDisplayManager_DisplayHdrFormat.md)NativeDisplayManager_DisplayHdrFormat显示设备支持的所有HDR格式。[NativeDisplayManager_DisplayColorSpace](NativeDisplayManager_DisplayColorSpace.md)NativeDisplayManager_DisplayColorSpace显示设备支持的所有色域类型。[NativeDisplayManager_DisplayInfo](NativeDisplayManager_DisplayInfo.md)NativeDisplayManager_DisplayInfo显示设备的对象属性。[NativeDisplayManager_DisplaysInfo](NativeDisplayManager_DisplaysInfo.md)NativeDisplayManager_DisplaysInfo多显示设备的Display对象。

#### 宏定义

名称描述[OH_DISPLAY_NAME_LENGTH](#ZH-CN_TOPIC_0000002529285077__oh_display_name_length) 32屏幕名称的最大长度。

#### 枚举

名称typedef关键字描述[NativeDisplayManager_Rotation](#ZH-CN_TOPIC_0000002529285077__nativedisplaymanager_rotation)NativeDisplayManager_Rotation屏幕顺时针的旋转角度。[NativeDisplayManager_Orientation](#ZH-CN_TOPIC_0000002529285077__nativedisplaymanager_orientation)NativeDisplayManager_Orientation屏幕的旋转方向。[NativeDisplayManager_ErrorCode](#ZH-CN_TOPIC_0000002529285077__nativedisplaymanager_errorcode)NativeDisplayManager_ErrorCode屏幕管理接口返回状态码枚举。[NativeDisplayManager_FoldDisplayMode](#ZH-CN_TOPIC_0000002529285077__nativedisplaymanager_folddisplaymode)NativeDisplayManager_FoldDisplayMode可折叠设备的显示模式枚举。[NativeDisplayManager_DisplayState](#ZH-CN_TOPIC_0000002529285077__nativedisplaymanager_displaystate)NativeDisplayManager_DisplayState显示设备的状态枚举。[NativeDisplayManager_SourceMode](#ZH-CN_TOPIC_0000002529285077__nativedisplaymanager_sourcemode)NativeDisplayManager_SourceMode设备的显示模式枚举。

#### 宏定义说明

#### OH_DISPLAY_NAME_LENGTH

```ets
#define OH_DISPLAY_NAME_LENGTH 32
```

**描述**

屏幕名称的最大长度。

**起始版本：** 14

#### 枚举类型说明

#### NativeDisplayManager_Rotation

```ets
enum NativeDisplayManager_Rotation
```

**描述**

屏幕顺时针的旋转角度。

**起始版本：** 12

枚举项描述DISPLAY_MANAGER_ROTATION_0 = 0代表屏幕顺时针旋转角度0度。DISPLAY_MANAGER_ROTATION_90 = 1代表屏幕顺时针旋转角度90度。DISPLAY_MANAGER_ROTATION_180 = 2代表屏幕顺时针旋转角度180度。DISPLAY_MANAGER_ROTATION_270 = 3代表屏幕顺时针旋转角度270度。

#### NativeDisplayManager_Orientation

```ets
enum NativeDisplayManager_Orientation
```

**描述**

屏幕的旋转方向。

**起始版本：** 12

枚举项描述DISPLAY_MANAGER_PORTRAIT = 0表示设备当前以竖屏方式显示。DISPLAY_MANAGER_LANDSCAPE = 1表示设备当前以横屏方式显示。DISPLAY_MANAGER_PORTRAIT_INVERTED = 2表示设备当前以反向竖屏方式显示。DISPLAY_MANAGER_LANDSCAPE_INVERTED = 3表示设备当前以反向横屏方式显示。DISPLAY_MANAGER_UNKNOWN表示显示未识别屏幕方向。

#### NativeDisplayManager_ErrorCode

```ets
enum NativeDisplayManager_ErrorCode
```

**描述**

屏幕管理接口返回状态码枚举。

**起始版本：** 12

枚举项描述DISPLAY_MANAGER_OK = 0成功。DISPLAY_MANAGER_ERROR_NO_PERMISSION = 201权限校验失败，应用无权限使用该API，需要申请权限。DISPLAY_MANAGER_ERROR_NOT_SYSTEM_APP = 202权限校验失败，非系统应用使用了系统API。DISPLAY_MANAGER_ERROR_INVALID_PARAM = 401参数检查失败。DISPLAY_MANAGER_ERROR_DEVICE_NOT_SUPPORTED = 801该设备不支持此API。DISPLAY_MANAGER_ERROR_INVALID_SCREEN = 1400001操作的显示设备无效。DISPLAY_MANAGER_ERROR_INVALID_CALL = 1400002当前操作对象无操作权限。DISPLAY_MANAGER_ERROR_SYSTEM_ABNORMAL = 1400003系统服务工作异常。DISPLAY_MANAGER_ERROR_ILLEGAL_PARAM = 1400004

非法参数。

**起始版本：** 20

#### NativeDisplayManager_FoldDisplayMode

```ets
enum NativeDisplayManager_FoldDisplayMode
```

**描述**

可折叠设备的显示模式枚举。

**起始版本：** 12

枚举项描述DISPLAY_MANAGER_FOLD_DISPLAY_MODE_UNKNOWN = 0表示设备当前折叠显示模式未知。DISPLAY_MANAGER_FOLD_DISPLAY_MODE_FULL = 1表示设备当前全屏显示。DISPLAY_MANAGER_FOLD_DISPLAY_MODE_MAIN = 2表示设备当前主屏幕显示。DISPLAY_MANAGER_FOLD_DISPLAY_MODE_SUB = 3表示设备当前子屏幕显示。DISPLAY_MANAGER_FOLD_DISPLAY_MODE_COORDINATION = 4表示设备当前双屏协同显示。

#### NativeDisplayManager_DisplayState

```ets
enum NativeDisplayManager_DisplayState
```

**描述**

显示设备的状态枚举。

**起始版本：** 14

枚举项描述DISPLAY_MANAGER_DISPLAY_STATE_UNKNOWN = 0表示显示设备状态未知。DISPLAY_MANAGER_DISPLAY_STATE_OFF = 1表示显示设备状态为关闭。DISPLAY_MANAGER_DISPLAY_STATE_ON = 2表示显示设备状态为开启。DISPLAY_MANAGER_DISPLAY_STATE_DOZE = 3表示显示设备为低电耗模式。DISPLAY_MANAGER_DISPLAY_STATE_DOZE_SUSPEND = 4表示显示设备为睡眠模式，CPU为挂起状态。DISPLAY_MANAGER_DISPLAY_STATE_VR = 5表示显示设备为VR模式。DISPLAY_MANAGER_DISPLAY_STATE_ON_SUSPEND = 6表示显示设备为开启状态，CPU为挂起状态。

#### NativeDisplayManager_SourceMode

```ets
enum NativeDisplayManager_SourceMode
```

**描述**

设备的显示模式枚举。

**起始版本：** 20

枚举项描述DISPLAY_SOURCE_MODE_NONE = 0表示设备当前未使用。DISPLAY_SOURCE_MODE_MAIN = 1表示设备当前为主屏。DISPLAY_SOURCE_MODE_MIRROR = 2表示设备当前为镜像显示模式。DISPLAY_SOURCE_MODE_EXTEND = 3表示设备当前为扩展显示模式。DISPLAY_SOURCE_MODE_ALONE = 4表示设备当前为异源显示模式。