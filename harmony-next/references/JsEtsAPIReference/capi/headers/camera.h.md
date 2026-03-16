# camera.h

#### 概述

声明相机的基本概念。

**引用文件：** <ohcamera/camera.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：**[OH_Camera](../../topics/media/OH_Camera.md)

#### 汇总

#### 结构体

名称typedef关键字描述[Camera_Size](../../topics/media/Camera_Size.md)Camera_Size大小参数。[Camera_Profile](../../topics/media/Camera_Profile.md)Camera_Profile相机流的配置文件。[Camera_FrameRateRange](../../topics/components/Camera_FrameRateRange.md)Camera_FrameRateRange帧速率范围。[Camera_VideoProfile](../../topics/media/Camera_VideoProfile.md)Camera_VideoProfile录像配置文件。[Camera_OutputCapability](../../topics/system-services/Camera_OutputCapability.md)Camera_OutputCapability相机输出能力。[Camera_Device](../../topics/system-services/Camera_Device.md)Camera_Device相机设备对象。[Camera_StatusInfo](../../topics/media/Camera_StatusInfo.md)Camera_StatusInfo相机状态信息。[Camera_Point](../../topics/media/Camera_Point.md)Camera_Point点参数。[Camera_Location](../../topics/media/Camera_Location.md)Camera_Location拍照位置。[Camera_PhotoCaptureSetting](../../topics/media/Camera_PhotoCaptureSetting.md)Camera_PhotoCaptureSetting要设置的拍照捕获选项。[Camera_FrameShutterInfo](../../topics/components/Camera_FrameShutterInfo.md)Camera_FrameShutterInfo帧快门回调信息。[Camera_CaptureEndInfo](../../topics/media/Camera_CaptureEndInfo.md)Camera_CaptureEndInfo捕获结束信息。[Camera_Rect](../../topics/media/Camera_Rect.md)Camera_Rect

矩形定义。

 检测点应在0-1坐标系内，该坐标系左上角为(0，0)，右下角为(1，1)。

 此坐标系以设备充电口在右侧时的横向设备方向为基准。

 例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为(w，h)， 返回点为(x，y)，则转换后的坐标点为(1-y，x)。

[Camera_MetadataObject](../../topics/media/Camera_MetadataObject.md)Camera_MetadataObject元数据对象基础。[Camera_TorchStatusInfo](../../topics/media/Camera_TorchStatusInfo.md)Camera_TorchStatusInfo手电筒状态信息。[Camera_SmoothZoomInfo](../../topics/media/Camera_SmoothZoomInfo.md)Camera_SmoothZoomInfo平滑变焦参数信息。[Camera_CaptureStartInfo](../../topics/networking/Camera_CaptureStartInfo.md)Camera_CaptureStartInfo拍照开始信息。[Camera_FrameShutterEndInfo](../../topics/components/Camera_FrameShutterEndInfo.md)Camera_FrameShutterEndInfo拍照曝光结束信息。[Camera_FoldStatusInfo](../../topics/media/Camera_FoldStatusInfo.md)Camera_FoldStatusInfo折叠状态信息。[Camera_AutoDeviceSwitchStatusInfo](../../topics/system-services/Camera_AutoDeviceSwitchStatusInfo.md)Camera_AutoDeviceSwitchStatusInfo自动设备切换状态信息。[Camera_ConcurrentInfo](../../topics/media/Camera_ConcurrentInfo.md)Camera_ConcurrentInfo相机并发能力信息。[Camera_ControlCenterStatusInfo](../../topics/media/Camera_ControlCenterStatusInfo.md)Camera_ControlCenterStatusInfo控制器效果激活状态信息。[Camera_Manager](../../topics/media/Camera_Manager.md)Camera_Manager

相机管理器对象。

 可以使用[OH_Camera_GetCameraManager](#ZH-CN_TOPIC_0000002497605798__oh_camera_getcameramanager)方法创建指针。

#### 枚举

名称typedef关键字描述[Camera_ErrorCode](#ZH-CN_TOPIC_0000002497605798__camera_errorcode)Camera_ErrorCode相机错误代码的枚举。[Camera_Status](#ZH-CN_TOPIC_0000002497605798__camera_status)Camera_Status相机状态的枚举。[Camera_SceneMode](#ZH-CN_TOPIC_0000002497605798__camera_scenemode)Camera_SceneMode相机模式的枚举。[Camera_Position](#ZH-CN_TOPIC_0000002497605798__camera_position)Camera_Position相机位置的枚举。[Camera_Type](#ZH-CN_TOPIC_0000002497605798__camera_type)Camera_Type相机类型的枚举。[Camera_Connection](#ZH-CN_TOPIC_0000002497605798__camera_connection)Camera_Connection相机连接类型的枚举。[Camera_Format](#ZH-CN_TOPIC_0000002497605798__camera_format)Camera_Format相机格式类型的枚举。[Camera_FlashMode](#ZH-CN_TOPIC_0000002497605798__camera_flashmode)Camera_FlashMode闪光模式的枚举。[Camera_ExposureMode](#ZH-CN_TOPIC_0000002497605798__camera_exposuremode)Camera_ExposureMode曝光模式的枚举。[Camera_FocusMode](#ZH-CN_TOPIC_0000002497605798__camera_focusmode)Camera_FocusMode聚焦模式的枚举。[Camera_FocusState](#ZH-CN_TOPIC_0000002497605798__camera_focusstate)Camera_FocusState焦点状态的枚举。[Camera_VideoStabilizationMode](#ZH-CN_TOPIC_0000002497605798__camera_videostabilizationmode)Camera_VideoStabilizationMode录像防抖模式的枚举。[Camera_ImageRotation](#ZH-CN_TOPIC_0000002497605798__camera_imagerotation)Camera_ImageRotation图像旋转角度的枚举。[Camera_QualityLevel](#ZH-CN_TOPIC_0000002497605798__camera_qualitylevel)Camera_QualityLevel图像质量等级的枚举。[Camera_MetadataObjectType](#ZH-CN_TOPIC_0000002497605798__camera_metadataobjecttype)Camera_MetadataObjectType元数据对象类型的枚举。[Camera_TorchMode](#ZH-CN_TOPIC_0000002497605798__camera_torchmode)Camera_TorchMode手电筒模式的枚举。[Camera_SmoothZoomMode](#ZH-CN_TOPIC_0000002497605798__camera_smoothzoommode)Camera_SmoothZoomMode平滑变焦模式的枚举。[Camera_SystemPressureLevel](#ZH-CN_TOPIC_0000002497605798__camera_systempressurelevel)Camera_SystemPressureLevel系统压力等级的枚举。[Camera_PreconfigType](#ZH-CN_TOPIC_0000002497605798__camera_preconfigtype)Camera_PreconfigType预配置照片分辨率的枚举。[Camera_PreconfigRatio](#ZH-CN_TOPIC_0000002497605798__camera_preconfigratio)Camera_PreconfigRatio预配置照片比例的枚举。[Camera_HostDeviceType](#ZH-CN_TOPIC_0000002497605798__camera_hostdevicetype)Camera_HostDeviceType远程设备类型枚举。[Camera_FoldStatus](#ZH-CN_TOPIC_0000002497605798__camera_foldstatus)Camera_FoldStatus折叠状态枚举。[Camera_QualityPrioritization](#ZH-CN_TOPIC_0000002497605798__camera_qualityprioritization)Camera_QualityPrioritization录像质量优先级的枚举。[Camera_ConcurrentType](#ZH-CN_TOPIC_0000002497605798__camera_concurrenttype)Camera_ConcurrentType相机并发状态的枚举。[Camera_WhiteBalanceMode](#ZH-CN_TOPIC_0000002497605798__camera_whitebalancemode)Camera_WhiteBalanceMode白平衡模式枚举。[Camera_ControlCenterEffectType](#ZH-CN_TOPIC_0000002497605798__camera_controlcentereffecttype)Camera_ControlCenterEffectType控制器效果类型枚举。[Camera_PhotoQualityPrioritization](#ZH-CN_TOPIC_0000002497605798__camera_photoqualityprioritization)Camera_PhotoQualityPrioritization拍照画质优先策略枚举。

#### 函数

名称描述[Camera_ErrorCode OH_Camera_GetCameraManager(Camera_Manager** cameraManager)](#ZH-CN_TOPIC_0000002497605798__oh_camera_getcameramanager)创建CameraManager实例。[Camera_ErrorCode OH_Camera_DeleteCameraManager(Camera_Manager* cameraManager)](#ZH-CN_TOPIC_0000002497605798__oh_camera_deletecameramanager)删除CameraManager实例。

#### 枚举类型说明

#### Camera_ErrorCode

```ets
enum Camera_ErrorCode
```

**描述**

相机错误代码的枚举。

**起始版本：** 11

枚举项描述CAMERA_OK = 0相机结果正常。CAMERA_INVALID_ARGUMENT = 7400101参数丢失或参数类型不正确。CAMERA_OPERATION_NOT_ALLOWED = 7400102不允许操作。CAMERA_SESSION_NOT_CONFIG = 7400103会话未配置。CAMERA_SESSION_NOT_RUNNING = 7400104会话未运行。CAMERA_SESSION_CONFIG_LOCKED = 7400105会话配置已锁定。CAMERA_DEVICE_SETTING_LOCKED = 7400106设备设置已锁定。CAMERA_CONFLICT_CAMERA = 7400107因冲突而无法使用相机。CAMERA_DEVICE_DISABLED = 7400108由于安全原因，相机已禁用。CAMERA_DEVICE_PREEMPTED = 7400109因被抢占而无法使用相机。CAMERA_UNRESOLVED_CONFLICTS_WITH_CURRENT_CONFIGURATIONS = 7400110

与当前配置存在冲突。

**起始版本：** 12

CAMERA_SERVICE_FATAL_ERROR = 7400201

相机服务致命错误。

 比如没有相机权限、相机服务重启、跨进程调用异常等。

#### Camera_Status

```ets
enum Camera_Status
```

**描述**

相机状态的枚举。

**起始版本：** 11

枚举项描述CAMERA_STATUS_APPEAR = 0显示状态。CAMERA_STATUS_DISAPPEAR = 1消失状态。CAMERA_STATUS_AVAILABLE = 2可用状态。CAMERA_STATUS_UNAVAILABLE = 3不可用状态。

#### Camera_SceneMode

```ets
enum Camera_SceneMode
```

**描述**

相机模式的枚举。

**起始版本：** 12

枚举项描述NORMAL_PHOTO = 1普通相机模式。NORMAL_VIDEO = 2普通视频模式。SECURE_PHOTO = 12安全相机模式。

#### Camera_Position

```ets
enum Camera_Position
```

**描述**

相机位置的枚举。

**起始版本：** 11

枚举项描述CAMERA_POSITION_UNSPECIFIED = 0相对于设备屏幕没有固定的朝向的相机。CAMERA_POSITION_BACK = 1后置。CAMERA_POSITION_FRONT = 2前置。

#### Camera_Type

```ets
enum Camera_Type
```

**描述**

相机类型的枚举。

**起始版本：** 11

枚举项描述CAMERA_TYPE_DEFAULT = 0默认相机类型。CAMERA_TYPE_WIDE_ANGLE = 1广角相机。CAMERA_TYPE_ULTRA_WIDE = 2超广角相机。CAMERA_TYPE_TELEPHOTO = 3长焦相机。CAMERA_TYPE_TRUE_DEPTH = 4景深相机。

#### Camera_Connection

```ets
enum Camera_Connection
```

**描述**

相机连接类型的枚举。

**起始版本：** 11

枚举项描述CAMERA_CONNECTION_BUILT_IN = 0内置相机。CAMERA_CONNECTION_USB_PLUGIN = 1使用USB连接的相机。CAMERA_CONNECTION_REMOTE = 2远程相机。

#### Camera_Format

```ets
enum Camera_Format
```

**描述**

相机格式类型的枚举。

**起始版本：** 11

枚举项描述CAMERA_FORMAT_RGBA_8888 = 3RGBA 8888格式。CAMERA_FORMAT_YUV_420_SP = 1003YUV 420格式。CAMERA_FORMAT_JPEG = 2000JPEG格式。CAMERA_FORMAT_YCBCR_P010 = 2001

YCBCR P010 格式。

**起始版本：** 12

CAMERA_FORMAT_YCRCB_P010 = 2002

YCRCB P010 格式。

**起始版本：** 12

#### Camera_FlashMode

```ets
enum Camera_FlashMode
```

**描述**

闪光模式的枚举。

**起始版本：** 11

枚举项描述FLASH_MODE_CLOSE = 0关闭模式。FLASH_MODE_OPEN = 1打开模式。FLASH_MODE_AUTO = 2自动模式。FLASH_MODE_ALWAYS_OPEN = 3始终打开模式。

#### Camera_ExposureMode

```ets
enum Camera_ExposureMode
```

**描述**

曝光模式的枚举。

**起始版本：** 11

枚举项描述EXPOSURE_MODE_LOCKED = 0锁定曝光模式。EXPOSURE_MODE_AUTO = 1自动曝光模式。EXPOSURE_MODE_CONTINUOUS_AUTO = 2连续自动曝光。

#### Camera_FocusMode

```ets
enum Camera_FocusMode
```

**描述**

聚焦模式的枚举。

**起始版本：** 11

枚举项描述FOCUS_MODE_MANUAL = 0手动模式。FOCUS_MODE_CONTINUOUS_AUTO = 1连续自动模式。FOCUS_MODE_AUTO = 2自动模式。FOCUS_MODE_LOCKED = 3锁定模式。

#### Camera_FocusState

```ets
enum Camera_FocusState
```

**描述**

焦点状态的枚举。

**起始版本：** 11

枚举项描述FOCUS_STATE_SCAN = 0扫描状态。FOCUS_STATE_FOCUSED = 1聚焦状态。FOCUS_STATE_UNFOCUSED = 2非聚焦状态。

#### Camera_VideoStabilizationMode

```ets
enum Camera_VideoStabilizationMode
```

**描述**

录像防抖模式的枚举。

**起始版本：** 11

枚举项描述STABILIZATION_MODE_OFF = 0关闭录像防抖。STABILIZATION_MODE_LOW = 1LOW模式，提供基本的防抖效果。STABILIZATION_MODE_MIDDLE = 2MIDDLE模式，表示通过算法可以获得比LOW模式更好的效果。STABILIZATION_MODE_HIGH = 3HIGH模式，表示通过算法可以获得比MIDDLE模式更好的效果。STABILIZATION_MODE_AUTO = 4自动选择模式，HDF相机可用。

#### Camera_ImageRotation

```ets
enum Camera_ImageRotation
```

**描述**

图像旋转角度的枚举。

**起始版本：** 11

枚举项描述IAMGE_ROTATION_0 = 0

捕获图像旋转0度。

 从API version 22开始，推荐使用新枚举值[CAMERA_IMAGE_ROTATION_0](#ZH-CN_TOPIC_0000002497605798__camera_imagerotation)。

CAMERA_IMAGE_ROTATION_0 = 0

捕获图像旋转0度。

**起始版本：** 22

IAMGE_ROTATION_90 = 90

捕获图像旋转90度。

 从API version 22开始，推荐使用新枚举值[CAMERA_IMAGE_ROTATION_90](#ZH-CN_TOPIC_0000002497605798__camera_imagerotation)。

CAMERA_IMAGE_ROTATION_90 = 90

捕获图像旋转90度。

**起始版本：** 22

IAMGE_ROTATION_180 = 180

捕获图像旋转180度。

 从API version 22开始，推荐使用新枚举值[CAMERA_IMAGE_ROTATION_180](#ZH-CN_TOPIC_0000002497605798__camera_imagerotation)。

CAMERA_IMAGE_ROTATION_180 = 180

捕获图像旋转180度。

**起始版本：** 22

IAMGE_ROTATION_270 = 270

捕获图像旋转270度。

 从API version 22开始，推荐使用新枚举值[CAMERA_IMAGE_ROTATION_270](#ZH-CN_TOPIC_0000002497605798__camera_imagerotation)。

CAMERA_IMAGE_ROTATION_270 = 270

捕获图像旋转270度。

**起始版本：** 22

#### Camera_QualityLevel

```ets
enum Camera_QualityLevel
```

**描述**

图像质量等级的枚举。

**起始版本：** 11

枚举项描述QUALITY_LEVEL_HIGH = 0高图像质量。QUALITY_LEVEL_MEDIUM = 1中等图像质量。QUALITY_LEVEL_LOW = 2低图像质量。

#### Camera_MetadataObjectType

```ets
enum Camera_MetadataObjectType
```

**描述**

元数据对象类型的枚举。

**起始版本：** 11

枚举项描述FACE_DETECTION = 0metadata对象类型，用于人脸检测。

#### Camera_TorchMode

```ets
enum Camera_TorchMode
```

**描述**

手电筒模式的枚举。

**起始版本：** 12

枚举项描述OFF = 0

设备手电筒常关。

 从API version 22开始，推荐使用新枚举值[CAMERA_TORCH_MODE_OFF](#ZH-CN_TOPIC_0000002497605798__camera_torchmode)。

CAMERA_TORCH_MODE_OFF = 0

设备手电筒常关。

**起始版本：** 22

ON = 1

设备手电筒常开。

 从API version 22开始，推荐使用新枚举值[CAMERA_TORCH_MODE_ON](#ZH-CN_TOPIC_0000002497605798__camera_torchmode)。

CAMERA_TORCH_MODE_ON = 1

设备手电筒常开。

**起始版本：** 22

AUTO = 2

设备手电筒自动模式，将根据环境光照水平打开手电筒。

 从API version 22开始，推荐使用新枚举值[CAMERA_TORCH_MODE_AUTO](#ZH-CN_TOPIC_0000002497605798__camera_torchmode)。

CAMERA_TORCH_MODE_AUTO = 2

设备手电筒自动模式，将根据环境光照水平打开手电筒。

**起始版本：** 22

#### Camera_SmoothZoomMode

```ets
enum Camera_SmoothZoomMode
```

**描述**

平滑变焦模式的枚举。

**起始版本：** 12

枚举项描述NORMAL = 0

贝塞尔曲线模式。

 从API version 22开始，推荐使用新枚举值[CAMERA_SMOOTH_ZOOM_MODE_NORMAL](#ZH-CN_TOPIC_0000002497605798__camera_smoothzoommode)。

CAMERA_SMOOTH_ZOOM_MODE_NORMAL = 0

贝塞尔曲线模式。

**起始版本：** 22

#### Camera_SystemPressureLevel

```ets
enum Camera_SystemPressureLevel
```

**描述**

系统压力等级的枚举。

**起始版本：** 20

枚举项描述SYSTEM_PRESSURE_NORMAL = 0系统压力正常。SYSTEM_PRESSURE_MILD = 1系统压力升高，但是系统不会主动管控。SYSTEM_PRESSURE_SEVERE = 2系统压力可能对图像总质量、性能产生影响。SYSTEM_PRESSURE_CRITICAL = 3系统图像质量、性能产生显著影响。SYSTEM_PRESSURE_SHUTDOWN = 4系统压力过高，停止工作。

#### Camera_PreconfigType

```ets
enum Camera_PreconfigType
```

**描述**

预配置照片分辨率的枚举。

**起始版本：** 12

枚举项描述PRECONFIG_720P = 0预配置照片分辨率为720P。PRECONFIG_1080P = 1预配置照片分辨率为1080P。PRECONFIG_4K = 2预配置照片分辨率为4K。PRECONFIG_HIGH_QUALITY = 3预配置照片为高质量。

#### Camera_PreconfigRatio

```ets
enum Camera_PreconfigRatio
```

**描述**

预配置照片比例的枚举。

**起始版本：** 12

枚举项描述PRECONFIG_RATIO_1_1 = 0预配置照片比例为1:1。PRECONFIG_RATIO_4_3 = 1预配置照片比例为4:3。PRECONFIG_RATIO_16_9 = 2预配置照片比例为16:9。

#### Camera_HostDeviceType

```ets
enum Camera_HostDeviceType
```

**描述**

远程设备类型枚举。

**起始版本：** 15

枚举项描述HOST_DEVICE_TYPE_UNKNOWN_TYPE = 0未知设备类型。HOST_DEVICE_TYPE_PHONE = 0x0E手机设备。HOST_DEVICE_TYPE_TABLET = 0x11平板设备。

#### Camera_FoldStatus

```ets
enum Camera_FoldStatus
```

**描述**

折叠状态枚举。

**起始版本：** 13

枚举项描述NON_FOLDABLE = 0

不可折叠状态。

 从API version 22开始，推荐使用新枚举值[CAMERA_FOLD_STATUS_NON_FOLDABLE](#ZH-CN_TOPIC_0000002497605798__camera_foldstatus)。

CAMERA_FOLD_STATUS_NON_FOLDABLE = 0

不可折叠状态。

**起始版本：** 22

EXPANDED = 1

展开状态。

 从API version 22开始，推荐使用新枚举值[CAMERA_FOLD_STATUS_EXPANDED](#ZH-CN_TOPIC_0000002497605798__camera_foldstatus)。

CAMERA_FOLD_STATUS_EXPANDED = 1

展开状态。

**起始版本：** 22

FOLDED = 2

折叠状态。

 从API version 22开始，推荐使用新枚举值[CAMERA_FOLD_STATUS_FOLDED](#ZH-CN_TOPIC_0000002497605798__camera_foldstatus)。

CAMERA_FOLD_STATUS_FOLDED = 2

折叠状态。

**起始版本：** 22

#### Camera_QualityPrioritization

```ets
enum Camera_QualityPrioritization
```

**描述**

录像质量优先级的枚举。

**起始版本：** 14

枚举项描述HIGH_QUALITY = 0高录像质量。POWER_BALANCE = 1功耗平衡录像质量。

#### Camera_ConcurrentType

```ets
enum Camera_ConcurrentType
```

**描述**

相机并发状态的枚举。

**起始版本：** 18

枚举项描述CAMERA_CONCURRENT_TYPE_LIMITED_CAPABILITY = 0相机限制并发。CAMERA_CONCURRENT_TYPE_FULL_CAPABILITY = 1相机全量并发。

#### Camera_WhiteBalanceMode

```ets
enum Camera_WhiteBalanceMode
```

**描述**

白平衡模式枚举。

**起始版本：** 20

枚举项描述CAMERA_WHITE_BALANCE_MODE_AUTO = 0白平衡模式：自动。CAMERA_WHITE_BALANCE_MODE_CLOUDY = 1白平衡模式：阴天。CAMERA_WHITE_BALANCE_MODE_INCANDESCENT = 2白平衡模式：白炽灯。CAMERA_WHITE_BALANCE_MODE_FLUORESCENT = 3白平衡模式：荧光。CAMERA_WHITE_BALANCE_MODE_DAYLIGHT = 4白平衡模式：晴天。CAMERA_WHITE_BALANCE_MODE_MANUAL = 5白平衡模式：手动。CAMERA_WHITE_BALANCE_MODE_LOCKED = 6白平衡模式：锁定。

#### Camera_ControlCenterEffectType

```ets
enum Camera_ControlCenterEffectType
```

**描述**

控制器效果类型枚举。

**起始版本：** 20

枚举项描述CONTROL_CENTER_EFFECT_TYPE_BEAUTY = 0控制器效果类型：美颜。CONTROL_CENTER_EFFECT_TYPE_PORTRAIT = 1控制器效果类型：人像虚化。

#### Camera_PhotoQualityPrioritization

```ets
enum Camera_PhotoQualityPrioritization
```

**描述**

拍照画质优先策略枚举。

**起始版本：** 21

枚举项描述CAMERA_PHOTO_QUALITY_PRIORITIZATION_HIGH_QUALITY = 0画质优先，拍照需要较长的时间，以输出高画质的图片。CAMERA_PHOTO_QUALITY_PRIORITIZATION_SPEED = 1性能优先，会降低画质来提升拍照的速度。

#### 函数说明

#### OH_Camera_GetCameraManager()

```ets
Camera_ErrorCode OH_Camera_GetCameraManager(Camera_Manager** cameraManager)
```

**描述**

创建CameraManager实例。

**起始版本：** 11

**参数：**

参数项描述[Camera_Manager](../../topics/media/Camera_Manager.md)** cameraManager如果方法调用成功，将创建Camera_Manager实例。

**返回：**

类型说明[Camera_ErrorCode](#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_Camera_DeleteCameraManager()

```ets
Camera_ErrorCode OH_Camera_DeleteCameraManager(Camera_Manager* cameraManager)
```

**描述**

删除CameraManager实例。

**起始版本：** 11

**参数：**

参数项描述[Camera_Manager](../../topics/media/Camera_Manager.md)* cameraManager要删除的Camera_Manager实例。

**返回：**

类型说明[Camera_ErrorCode](#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。