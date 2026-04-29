# oh_display_info.h

**概述**

提供屏幕的公共枚举、公共定义等。

引用文件： <window_manager/oh_display_info.h>

库： libnative_display_manager.so

系统能力： SystemCapability.WindowManager.WindowManager.Core

起始版本： 12

相关模块： [OH_DisplayManager](OH_DisplayManager.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| NativeDisplayManager_Rect | NativeDisplayManager_Rect | 矩形区域。 |
| NativeDisplayManager_WaterfallDisplayAreaRects | NativeDisplayManager_WaterfallDisplayAreaRects | 瀑布屏曲面部分显示区域。 |
| NativeDisplayManager_CutoutInfo | NativeDisplayManager_CutoutInfo | 挖孔屏、刘海屏、瀑布屏等不可用屏幕区域信息。 |
| NativeDisplayManager_DisplayHdrFormat | NativeDisplayManager_DisplayHdrFormat | 显示设备支持的所有HDR格式。 |
| NativeDisplayManager_DisplayColorSpace | NativeDisplayManager_DisplayColorSpace | 显示设备支持的所有色域类型。 |
| NativeDisplayManager_DisplayInfo | NativeDisplayManager_DisplayInfo | 显示设备的对象属性。 |
| NativeDisplayManager_DisplaysInfo | NativeDisplayManager_DisplaysInfo | 多显示设备的Display对象。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| OH_DISPLAY_NAME_LENGTH 32 | 屏幕名称的最大长度。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| NativeDisplayManager_Rotation | NativeDisplayManager_Rotation | 屏幕顺时针的旋转角度。 |
| NativeDisplayManager_Orientation | NativeDisplayManager_Orientation | 屏幕的旋转方向。 |
| NativeDisplayManager_ErrorCode | NativeDisplayManager_ErrorCode | 屏幕管理接口返回状态码枚举。 |
| NativeDisplayManager_FoldDisplayMode | NativeDisplayManager_FoldDisplayMode | 可折叠设备的显示模式枚举。 |
| NativeDisplayManager_DisplayState | NativeDisplayManager_DisplayState | 显示设备的状态枚举。 |
| NativeDisplayManager_SourceMode | NativeDisplayManager_SourceMode | 设备的显示模式枚举。 |

**宏定义说明**

**OH_DISPLAY_NAME_LENGTH**

```ets
#define OH_DISPLAY_NAME_LENGTH 32
```

描述

屏幕名称的最大长度。

起始版本： 14

**枚举类型说明**

**NativeDisplayManager_Rotation**

```ets
enum NativeDisplayManager_Rotation
```

描述

屏幕顺时针的旋转角度。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY_MANAGER_ROTATION_0 = 0 | 代表屏幕顺时针旋转角度0度。 |
| DISPLAY_MANAGER_ROTATION_90 = 1 | 代表屏幕顺时针旋转角度90度。 |
| DISPLAY_MANAGER_ROTATION_180 = 2 | 代表屏幕顺时针旋转角度180度。 |
| DISPLAY_MANAGER_ROTATION_270 = 3 | 代表屏幕顺时针旋转角度270度。 |

**NativeDisplayManager_Orientation**

```ets
enum NativeDisplayManager_Orientation
```

描述

屏幕的旋转方向。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY_MANAGER_PORTRAIT = 0 | 表示设备当前以竖屏方式显示。 |
| DISPLAY_MANAGER_LANDSCAPE = 1 | 表示设备当前以横屏方式显示。 |
| DISPLAY_MANAGER_PORTRAIT_INVERTED = 2 | 表示设备当前以反向竖屏方式显示。 |
| DISPLAY_MANAGER_LANDSCAPE_INVERTED = 3 | 表示设备当前以反向横屏方式显示。 |
| DISPLAY_MANAGER_UNKNOWN | 表示显示未识别屏幕方向。 |

**NativeDisplayManager_ErrorCode**

```ets
enum NativeDisplayManager_ErrorCode
```

描述

屏幕管理接口返回状态码枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY_MANAGER_OK = 0 | 成功。 |
| DISPLAY_MANAGER_ERROR_NO_PERMISSION = 201 | 权限校验失败，应用无权限使用该API，需要申请权限。 |
| DISPLAY_MANAGER_ERROR_NOT_SYSTEM_APP = 202 | 权限校验失败，非系统应用使用了系统API。 |
| DISPLAY_MANAGER_ERROR_INVALID_PARAM = 401 | 参数检查失败。 |
| DISPLAY_MANAGER_ERROR_DEVICE_NOT_SUPPORTED = 801 | 该设备不支持此API。 |
| DISPLAY_MANAGER_ERROR_INVALID_SCREEN = 1400001 | 操作的显示设备无效。 |
| DISPLAY_MANAGER_ERROR_INVALID_CALL = 1400002 | 当前操作对象无操作权限。 |
| DISPLAY_MANAGER_ERROR_SYSTEM_ABNORMAL = 1400003 | 系统服务工作异常。 |
| DISPLAY_MANAGER_ERROR_ILLEGAL_PARAM = 1400004 | 非法参数。 起始版本： 20 |

**NativeDisplayManager_FoldDisplayMode**

```ets
enum NativeDisplayManager_FoldDisplayMode
```

描述

可折叠设备的显示模式枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY_MANAGER_FOLD_DISPLAY_MODE_UNKNOWN = 0 | 表示设备当前折叠显示模式未知。 |
| DISPLAY_MANAGER_FOLD_DISPLAY_MODE_FULL = 1 | 表示设备当前全屏显示。 |
| DISPLAY_MANAGER_FOLD_DISPLAY_MODE_MAIN = 2 | 表示设备当前主屏幕显示。 |
| DISPLAY_MANAGER_FOLD_DISPLAY_MODE_SUB = 3 | 表示设备当前子屏幕显示。 |
| DISPLAY_MANAGER_FOLD_DISPLAY_MODE_COORDINATION = 4 | 表示设备当前双屏协同显示。 |

**NativeDisplayManager_DisplayState**

```ets
enum NativeDisplayManager_DisplayState
```

描述

显示设备的状态枚举。

起始版本： 14

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY_MANAGER_DISPLAY_STATE_UNKNOWN = 0 | 表示显示设备状态未知。 |
| DISPLAY_MANAGER_DISPLAY_STATE_OFF = 1 | 表示显示设备状态为关闭。 |
| DISPLAY_MANAGER_DISPLAY_STATE_ON = 2 | 表示显示设备状态为开启。 |
| DISPLAY_MANAGER_DISPLAY_STATE_DOZE = 3 | 表示显示设备为低电耗模式。 |
| DISPLAY_MANAGER_DISPLAY_STATE_DOZE_SUSPEND = 4 | 表示显示设备为睡眠模式，CPU为挂起状态。 |
| DISPLAY_MANAGER_DISPLAY_STATE_VR = 5 | 表示显示设备为VR模式。 |
| DISPLAY_MANAGER_DISPLAY_STATE_ON_SUSPEND = 6 | 表示显示设备为开启状态，CPU为挂起状态。 |

**NativeDisplayManager_SourceMode**

```ets
enum NativeDisplayManager_SourceMode
```

描述

设备的显示模式枚举。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| DISPLAY_SOURCE_MODE_NONE = 0 | 表示设备当前未使用。 |
| DISPLAY_SOURCE_MODE_MAIN = 1 | 表示设备当前为主屏。 |
| DISPLAY_SOURCE_MODE_MIRROR = 2 | 表示设备当前为镜像显示模式。 |
| DISPLAY_SOURCE_MODE_EXTEND = 3 | 表示设备当前为扩展显示模式。 |
| DISPLAY_SOURCE_MODE_ALONE = 4 | 表示设备当前为异源显示模式。 |