# camera.h

**概述**

声明相机的基本概念。

引用文件： <ohcamera/camera.h>

库： libohcamera.so

系统能力： SystemCapability.Multimedia.Camera.Core

起始版本： 11

相关模块： [OH_Camera](OH_Camera.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Camera_DeviceQueryInfo | Camera_DeviceQueryInfo | 相机设备的查询信息。 |
| Camera_Size | Camera_Size | 大小参数。 |
| Camera_Profile | Camera_Profile | 相机流的配置文件。 |
| Camera_FrameRateRange | Camera_FrameRateRange | 帧速率范围。 |
| Camera_VideoProfile | Camera_VideoProfile | 录像配置文件。 |
| Camera_OutputCapability | Camera_OutputCapability | 相机输出能力。 |
| Camera_Device | Camera_Device | 相机设备对象。 |
| Camera_StatusInfo | Camera_StatusInfo | 相机状态信息。 |
| Camera_Point | Camera_Point | 点参数。 |
| Camera_Location | Camera_Location | 拍照位置。 |
| Camera_PhotoCaptureSetting | Camera_PhotoCaptureSetting | 要设置的拍照捕获选项。 |
| Camera_FrameShutterInfo | Camera_FrameShutterInfo | 帧快门回调信息。 |
| Camera_CaptureEndInfo | Camera_CaptureEndInfo | 捕获结束信息。 |
| Camera_Rect | Camera_Rect | 矩形定义。 检测点应在0-1坐标系内，该坐标系左上角为(0，0)，右下角为(1，1)。 此坐标系以设备充电口在右侧时的横向设备方向为基准。 例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为(w，h)， 返回点为(x，y)，则转换后的坐标点为(1-y，x)。 |
| Camera_MetadataObject | Camera_MetadataObject | 元数据对象基础。 |
| Camera_TorchStatusInfo | Camera_TorchStatusInfo | 手电筒状态信息。 |
| Camera_SmoothZoomInfo | Camera_SmoothZoomInfo | 平滑变焦参数信息。 |
| Camera_CaptureStartInfo | Camera_CaptureStartInfo | 拍照开始信息。 |
| Camera_FrameShutterEndInfo | Camera_FrameShutterEndInfo | 拍照曝光结束信息。 |
| Camera_FoldStatusInfo | Camera_FoldStatusInfo | 折叠状态信息。 |
| Camera_AutoDeviceSwitchStatusInfo | Camera_AutoDeviceSwitchStatusInfo | 自动设备切换状态信息。 |
| Camera_ConcurrentInfo | Camera_ConcurrentInfo | 相机并发能力信息。 |
| Camera_ControlCenterStatusInfo | Camera_ControlCenterStatusInfo | 控制器效果激活状态信息。 |
| Camera_OcclusionDetectionResult | Camera_OcclusionDetectionResult | 相机镜头遮挡、脏污检测结果。 |
| Camera_Manager | Camera_Manager | 相机管理器对象。 可以使用OH_Camera_GetCameraManager方法创建指针。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| Camera_ErrorCode | Camera_ErrorCode | 相机错误代码的枚举。 |
| Camera_Status | Camera_Status | 相机状态的枚举。 |
| Camera_SceneMode | Camera_SceneMode | 相机模式的枚举。 |
| Camera_Position | Camera_Position | 相机位置的枚举。 |
| Camera_Type | Camera_Type | 相机类型的枚举。 |
| Camera_Connection | Camera_Connection | 相机连接类型的枚举。 |
| Camera_Format | Camera_Format | 相机格式类型的枚举。 |
| Camera_FlashMode | Camera_FlashMode | 闪光模式的枚举。 |
| Camera_ExposureMode | Camera_ExposureMode | 曝光模式的枚举。 |
| Camera_FocusMode | Camera_FocusMode | 聚焦模式的枚举。 |
| Camera_FocusState | Camera_FocusState | 焦点状态的枚举。 |
| Camera_VideoStabilizationMode | Camera_VideoStabilizationMode | 录像防抖模式的枚举。 |
| Camera_ImageRotation | Camera_ImageRotation | 图像旋转角度的枚举。 |
| Camera_QualityLevel | Camera_QualityLevel | 图像质量等级的枚举。 |
| Camera_MetadataObjectType | Camera_MetadataObjectType | 元数据对象类型的枚举。 |
| Camera_TorchMode | Camera_TorchMode | 手电筒模式的枚举。 |
| Camera_SmoothZoomMode | Camera_SmoothZoomMode | 平滑变焦模式的枚举。 |
| Camera_SystemPressureLevel | Camera_SystemPressureLevel | 系统压力等级的枚举。 |
| Camera_PreconfigType | Camera_PreconfigType | 预配置照片分辨率的枚举。 |
| Camera_PreconfigRatio | Camera_PreconfigRatio | 预配置照片比例的枚举。 |
| Camera_HostDeviceType | Camera_HostDeviceType | 远程设备类型枚举。 |
| Camera_FoldStatus | Camera_FoldStatus | 折叠状态枚举。 |
| Camera_QualityPrioritization | Camera_QualityPrioritization | 录像质量优先级的枚举。 |
| Camera_ConcurrentType | Camera_ConcurrentType | 相机并发状态的枚举。 |
| Camera_WhiteBalanceMode | Camera_WhiteBalanceMode | 白平衡模式枚举。 |
| Camera_ControlCenterEffectType | Camera_ControlCenterEffectType | 控制器效果类型枚举。 |
| Camera_PhotoQualityPrioritization | Camera_PhotoQualityPrioritization | 拍照画质优先策略枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| Camera_ErrorCode OH_Camera_GetCameraManager(Camera_Manager** cameraManager) | 创建CameraManager实例。 |
| Camera_ErrorCode OH_Camera_DeleteCameraManager(Camera_Manager* cameraManager) | 删除CameraManager实例。 |

**枚举类型说明**

**Camera_ErrorCode**

```ets
enum Camera_ErrorCode
```

描述

相机错误代码的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| CAMERA_OK = 0 | 相机结果正常。 |
| CAMERA_INVALID_ARGUMENT = 7400101 | 参数丢失或参数类型不正确。 |
| CAMERA_OPERATION_NOT_ALLOWED = 7400102 | 不允许操作。 |
| CAMERA_SESSION_NOT_CONFIG = 7400103 | 会话未配置。 |
| CAMERA_SESSION_NOT_RUNNING = 7400104 | 会话未运行。 |
| CAMERA_SESSION_CONFIG_LOCKED = 7400105 | 会话配置已锁定。 |
| CAMERA_DEVICE_SETTING_LOCKED = 7400106 | 设备设置已锁定。 |
| CAMERA_CONFLICT_CAMERA = 7400107 | 因冲突而无法使用相机。 |
| CAMERA_DEVICE_DISABLED = 7400108 | 由于安全原因，相机已禁用。 |
| CAMERA_DEVICE_PREEMPTED = 7400109 | 因被抢占而无法使用相机。 |
| CAMERA_UNRESOLVED_CONFLICTS_WITH_CURRENT_CONFIGURATIONS = 7400110 | 与当前配置存在冲突。 起始版本： 12 |
| CAMERA_SERVICE_FATAL_ERROR = 7400201 | 相机服务异常。 比如没有相机权限、相机服务重启、跨进程调用异常等。 |

**Camera_Status**

```ets
enum Camera_Status
```

描述

相机状态的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| CAMERA_STATUS_APPEAR = 0 | 显示状态。 |
| CAMERA_STATUS_DISAPPEAR = 1 | 消失状态。 |
| CAMERA_STATUS_AVAILABLE = 2 | 可用状态。 |
| CAMERA_STATUS_UNAVAILABLE = 3 | 不可用状态。 |

**Camera_SceneMode**

```ets
enum Camera_SceneMode
```

描述

相机模式的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| NORMAL_PHOTO = 1 | 普通相机模式。 |
| NORMAL_VIDEO = 2 | 普通视频模式。 |
| SECURE_PHOTO = 12 | 安全相机模式，主要为银行等有活体检测等安全诉求的应用提供。安全相机的使用需要加密算法框架及可信应用服务，详情请参见Device Certificate Kit简介。 |

**Camera_Position**

```ets
enum Camera_Position
```

描述

相机位置的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| CAMERA_POSITION_UNSPECIFIED = 0 | 相对于设备屏幕没有固定的朝向的相机。 |
| CAMERA_POSITION_BACK = 1 | 后置。 |
| CAMERA_POSITION_FRONT = 2 | 前置。 |

**Camera_Type**

```ets
enum Camera_Type
```

描述

相机类型的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| CAMERA_TYPE_DEFAULT = 0 | 默认相机类型。 |
| CAMERA_TYPE_WIDE_ANGLE = 1 | 广角相机。 |
| CAMERA_TYPE_ULTRA_WIDE = 2 | 超广角相机。 |
| CAMERA_TYPE_TELEPHOTO = 3 | 长焦相机。 |
| CAMERA_TYPE_TRUE_DEPTH = 4 | 景深相机。 |

**Camera_Connection**

```ets
enum Camera_Connection
```

描述

相机连接类型的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| CAMERA_CONNECTION_BUILT_IN = 0 | 内置相机。 |
| CAMERA_CONNECTION_USB_PLUGIN = 1 | 使用USB连接的相机。 |
| CAMERA_CONNECTION_REMOTE = 2 | 远程相机。 |

**Camera_Format**

```ets
enum Camera_Format
```

描述

相机格式类型的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| CAMERA_FORMAT_RGBA_8888 = 3 | RGBA 8888格式。 |
| CAMERA_FORMAT_YUV_420_SP = 1003 | YUV 420格式。 |
| CAMERA_FORMAT_JPEG = 2000 | JPEG格式。 |
| CAMERA_FORMAT_YCBCR_P010 = 2001 | YCBCR P010 格式。 起始版本： 12 |
| CAMERA_FORMAT_YCRCB_P010 = 2002 | YCRCB P010 格式。 起始版本： 12 |
| CAMERA_FORMAT_HEIC = 2003 | HEIC格式。 起始版本： 23 |

**Camera_FlashMode**

```ets
enum Camera_FlashMode
```

描述

闪光模式的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| FLASH_MODE_CLOSE = 0 | 关闭模式。 |
| FLASH_MODE_OPEN = 1 | 打开模式。 |
| FLASH_MODE_AUTO = 2 | 自动模式。 |
| FLASH_MODE_ALWAYS_OPEN = 3 | 始终打开模式。 |

**Camera_ExposureMode**

```ets
enum Camera_ExposureMode
```

描述

曝光模式的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| EXPOSURE_MODE_LOCKED = 0 | 锁定曝光模式。 不支持曝光区域中心点设置。 设置该模式后，每次拍照时曝光都会默认锁定。 |
| EXPOSURE_MODE_AUTO = 1 | 自动曝光模式。支持曝光区域中心点设置，可以使用OH_CaptureSession_SetMeteringPoint接口设置曝光区域中心点。 设置该模式后，仅设置后的首次拍照生效。 |
| EXPOSURE_MODE_CONTINUOUS_AUTO = 2 | 连续自动曝光。 设置该模式后，拍照系统会根据每次的环境变化自动调整曝光。 |

**Camera_FocusMode**

```ets
enum Camera_FocusMode
```

描述

聚焦模式的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| FOCUS_MODE_MANUAL = 0 | 手动模式。 |
| FOCUS_MODE_CONTINUOUS_AUTO = 1 | 连续自动模式。 |
| FOCUS_MODE_AUTO = 2 | 自动模式。 |
| FOCUS_MODE_LOCKED = 3 | 锁定模式。 |

**Camera_FocusState**

```ets
enum Camera_FocusState
```

描述

焦点状态的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| FOCUS_STATE_SCAN = 0 | 扫描状态。 |
| FOCUS_STATE_FOCUSED = 1 | 聚焦状态。 |
| FOCUS_STATE_UNFOCUSED = 2 | 非聚焦状态。 |

**Camera_VideoStabilizationMode**

```ets
enum Camera_VideoStabilizationMode
```

描述

录像防抖模式的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| STABILIZATION_MODE_OFF = 0 | 关闭录像防抖。 |
| STABILIZATION_MODE_LOW = 1 | LOW模式，提供基本的防抖效果。 |
| STABILIZATION_MODE_MIDDLE = 2 | MIDDLE模式，表示通过算法可以获得比LOW模式更好的效果。 |
| STABILIZATION_MODE_HIGH = 3 | HIGH模式，表示通过算法可以获得比MIDDLE模式更好的效果。 |
| STABILIZATION_MODE_AUTO = 4 | 自动选择模式，HDF相机可用。 |

**Camera_ImageRotation**

```ets
enum Camera_ImageRotation
```

描述

图像旋转角度的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| IAMGE_ROTATION_0 = 0 | 捕获图像旋转0度。 从API version 23开始，推荐使用新枚举值CAMERA_IMAGE_ROTATION_0。 |
| CAMERA_IMAGE_ROTATION_0 = 0 | 捕获图像旋转0度。 起始版本： 23 |
| IAMGE_ROTATION_90 = 90 | 捕获图像旋转90度。 从API version 23开始，推荐使用新枚举值CAMERA_IMAGE_ROTATION_90。 |
| CAMERA_IMAGE_ROTATION_90 = 90 | 捕获图像旋转90度。 起始版本： 23 |
| IAMGE_ROTATION_180 = 180 | 捕获图像旋转180度。 从API version 23开始，推荐使用新枚举值CAMERA_IMAGE_ROTATION_180。 |
| CAMERA_IMAGE_ROTATION_180 = 180 | 捕获图像旋转180度。 起始版本： 23 |
| IAMGE_ROTATION_270 = 270 | 捕获图像旋转270度。 从API version 23开始，推荐使用新枚举值CAMERA_IMAGE_ROTATION_270。 |
| CAMERA_IMAGE_ROTATION_270 = 270 | 捕获图像旋转270度。 起始版本： 23 |

**Camera_QualityLevel**

```ets
enum Camera_QualityLevel
```

描述

图像质量等级的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| QUALITY_LEVEL_HIGH = 0 | 高图像质量。 |
| QUALITY_LEVEL_MEDIUM = 1 | 中等图像质量。 |
| QUALITY_LEVEL_LOW = 2 | 低图像质量。 |

**Camera_MetadataObjectType**

```ets
enum Camera_MetadataObjectType
```

描述

元数据对象类型的枚举。

起始版本： 11

| 枚举项 | 描述 |
| --- | --- |
| FACE_DETECTION = 0 | 元数据的对象类型，用于人脸检测。 从API version 23开始，推荐使用新枚举值CAMERA_METADATA_OBJECT_TYPE_FACE_DETECTION。 |
| CAMERA_METADATA_OBJECT_TYPE_FACE_DETECTION = 0 | 元数据的对象类型，用于人脸检测。 起始版本： 23 |
| CAMERA_METADATA_OBJECT_TYPE_HUMAN_BODY = 1 | 元数据的对象类型，用于人体检测。 起始版本： 23 |

**Camera_TorchMode**

```ets
enum Camera_TorchMode
```

描述

手电筒模式的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| OFF = 0 | 设备手电筒常关。 从API version 23开始，推荐使用新枚举值CAMERA_TORCH_MODE_OFF。 |
| CAMERA_TORCH_MODE_OFF = 0 | 设备手电筒常关。 起始版本： 23 |
| ON = 1 | 设备手电筒常开。 从API version 23开始，推荐使用新枚举值CAMERA_TORCH_MODE_ON。 |
| CAMERA_TORCH_MODE_ON = 1 | 设备手电筒常开。 起始版本： 23 |
| AUTO = 2 | 设备手电筒自动模式，将根据环境光照水平打开手电筒。 从API version 23开始，推荐使用新枚举值CAMERA_TORCH_MODE_AUTO。 |
| CAMERA_TORCH_MODE_AUTO = 2 | 设备手电筒自动模式，将根据环境光照水平打开手电筒。 起始版本： 23 |

**Camera_SmoothZoomMode**

```ets
enum Camera_SmoothZoomMode
```

描述

平滑变焦模式的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| NORMAL = 0 | 贝塞尔曲线模式。 从API version 23开始，推荐使用新枚举值CAMERA_SMOOTH_ZOOM_MODE_NORMAL。 |
| CAMERA_SMOOTH_ZOOM_MODE_NORMAL = 0 | 贝塞尔曲线模式。 起始版本： 23 |

**Camera_SystemPressureLevel**

```ets
enum Camera_SystemPressureLevel
```

描述

系统压力等级的枚举。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| SYSTEM_PRESSURE_NORMAL = 0 | 系统压力正常。 |
| SYSTEM_PRESSURE_MILD = 1 | 系统压力升高，但是系统不会主动管控。 |
| SYSTEM_PRESSURE_SEVERE = 2 | 系统压力可能对图像总质量、性能产生影响。 |
| SYSTEM_PRESSURE_CRITICAL = 3 | 系统图像质量、性能产生显著影响。 |
| SYSTEM_PRESSURE_SHUTDOWN = 4 | 系统压力过高，停止工作。 |

**Camera_PreconfigType**

```ets
enum Camera_PreconfigType
```

描述

预配置照片分辨率的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| PRECONFIG_720P = 0 | 预配置照片分辨率为720P。 |
| PRECONFIG_1080P = 1 | 预配置照片分辨率为1080P。 |
| PRECONFIG_4K = 2 | 预配置照片分辨率为4K。 |
| PRECONFIG_HIGH_QUALITY = 3 | 预配置照片为高质量。 |
| PRECONFIG_HIGH_QUALITY_PHOTOSESSION_BT2020 = 4 | 预配置支持预览高动态范围显示和HDR动图拍摄。 起始版本: 23 |

**Camera_PreconfigRatio**

```ets
enum Camera_PreconfigRatio
```

描述

预配置照片比例的枚举。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| PRECONFIG_RATIO_1_1 = 0 | 预配置照片比例为1:1。 |
| PRECONFIG_RATIO_4_3 = 1 | 预配置照片比例为4:3。 |
| PRECONFIG_RATIO_16_9 = 2 | 预配置照片比例为16:9。 |

**Camera_HostDeviceType**

```ets
enum Camera_HostDeviceType
```

描述

远程设备类型枚举。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| HOST_DEVICE_TYPE_UNKNOWN_TYPE = 0 | 未知设备类型。 |
| HOST_DEVICE_TYPE_PHONE = 0x0E | 手机设备。 |
| HOST_DEVICE_TYPE_TABLET = 0x11 | 平板设备。 |

**Camera_FoldStatus**

```ets
enum Camera_FoldStatus
```

描述

折叠状态枚举。

起始版本： 13

| 枚举项 | 描述 |
| --- | --- |
| NON_FOLDABLE = 0 | 不可折叠状态。 从API version 23开始，推荐使用新枚举值CAMERA_FOLD_STATUS_NON_FOLDABLE。 |
| CAMERA_FOLD_STATUS_NON_FOLDABLE = 0 | 不可折叠状态。 起始版本： 23 |
| EXPANDED = 1 | 展开状态。 从API version 23开始，推荐使用新枚举值CAMERA_FOLD_STATUS_EXPANDED。 |
| CAMERA_FOLD_STATUS_EXPANDED = 1 | 展开状态。 起始版本： 23 |
| FOLDED = 2 | 折叠状态。 从API version 23开始，推荐使用新枚举值CAMERA_FOLD_STATUS_FOLDED。 |
| CAMERA_FOLD_STATUS_FOLDED = 2 | 折叠状态。 起始版本： 23 |

**Camera_QualityPrioritization**

```ets
enum Camera_QualityPrioritization
```

描述

录像质量优先级的枚举。

起始版本： 14

| 枚举项 | 描述 |
| --- | --- |
| HIGH_QUALITY = 0 | 高录像质量。 |
| POWER_BALANCE = 1 | 功耗平衡录像质量。 |

**Camera_ConcurrentType**

```ets
enum Camera_ConcurrentType
```

描述

相机并发状态的枚举。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| CAMERA_CONCURRENT_TYPE_LIMITED_CAPABILITY = 0 | 相机限制并发。 |
| CAMERA_CONCURRENT_TYPE_FULL_CAPABILITY = 1 | 相机全量并发。 |

**Camera_WhiteBalanceMode**

```ets
enum Camera_WhiteBalanceMode
```

描述

白平衡模式枚举。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| CAMERA_WHITE_BALANCE_MODE_AUTO = 0 | 白平衡模式：自动。 |
| CAMERA_WHITE_BALANCE_MODE_CLOUDY = 1 | 白平衡模式：阴天。 |
| CAMERA_WHITE_BALANCE_MODE_INCANDESCENT = 2 | 白平衡模式：白炽灯。 |
| CAMERA_WHITE_BALANCE_MODE_FLUORESCENT = 3 | 白平衡模式：荧光。 |
| CAMERA_WHITE_BALANCE_MODE_DAYLIGHT = 4 | 白平衡模式：晴天。 |
| CAMERA_WHITE_BALANCE_MODE_MANUAL = 5 | 白平衡模式：手动。 |
| CAMERA_WHITE_BALANCE_MODE_LOCKED = 6 | 白平衡模式：锁定。 |

**Camera_ControlCenterEffectType**

```ets
enum Camera_ControlCenterEffectType
```

描述

控制器效果类型枚举。

起始版本： 20

| 枚举项 | 描述 |
| --- | --- |
| CONTROL_CENTER_EFFECT_TYPE_BEAUTY = 0 | 控制器效果类型：美颜。 |
| CONTROL_CENTER_EFFECT_TYPE_PORTRAIT = 1 | 控制器效果类型：人像虚化。 |

**Camera_PhotoQualityPrioritization**

```ets
enum Camera_PhotoQualityPrioritization
```

描述

拍照画质优先策略枚举。

起始版本： 21

| 枚举项 | 描述 |
| --- | --- |
| CAMERA_PHOTO_QUALITY_PRIORITIZATION_HIGH_QUALITY = 0 | 画质优先，拍照需要较长的时间，以输出高画质的图片。 |
| CAMERA_PHOTO_QUALITY_PRIORITIZATION_SPEED = 1 | 性能优先，会降低画质来提升拍照的速度。 |

**函数说明**

**OH_Camera_GetCameraManager()**

```ets
Camera_ErrorCode OH_Camera_GetCameraManager(Camera_Manager** cameraManager)
```

描述

创建CameraManager实例。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_Manager** cameraManager | 如果方法调用成功，将创建Camera_Manager实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_Camera_DeleteCameraManager()**

```ets
Camera_ErrorCode OH_Camera_DeleteCameraManager(Camera_Manager* cameraManager)
```

描述

删除CameraManager实例。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_Manager* cameraManager | 要删除的Camera_Manager实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |