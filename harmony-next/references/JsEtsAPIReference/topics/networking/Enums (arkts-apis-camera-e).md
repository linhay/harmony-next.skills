[]()[]()

# Enums

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### CameraPosition

枚举，相机位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明CAMERA_POSITION_UNSPECIFIED0相对于设备屏幕没有固定的朝向的相机。CAMERA_POSITION_BACK1后置相机。CAMERA_POSITION_FRONT2前置相机。CAMERA_POSITION_FOLD_INNER(deprecated)3

折叠态相机。

 从API version 11开始支持，从API version 12开始废弃。

[]()[]()

#### CameraType

枚举，相机类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明CAMERA_TYPE_DEFAULT0默认相机类型。CAMERA_TYPE_WIDE_ANGLE1广角相机。CAMERA_TYPE_ULTRA_WIDE2超广角相机。CAMERA_TYPE_TELEPHOTO3长焦相机。CAMERA_TYPE_TRUE_DEPTH4带景深信息的相机。[]()[]()

#### ConnectionType

枚举，相机连接类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明CAMERA_CONNECTION_BUILT_IN0内置相机。CAMERA_CONNECTION_USB_PLUGIN1USB连接的相机。CAMERA_CONNECTION_REMOTE2远程连接的相机。[]()[]()

#### HostDeviceType15+

枚举，远端相机设备类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明UNKNOWN_TYPE0未知设备类型。PHONE0x0E手机设备。TABLET0x11平板设备。[]()[]()

#### CameraStatus

枚举，相机状态。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明CAMERA_STATUS_APPEAR0新的相机出现。CAMERA_STATUS_DISAPPEAR1相机被移除。CAMERA_STATUS_AVAILABLE2相机可用。CAMERA_STATUS_UNAVAILABLE3相机不可用。[]()[]()

#### FoldStatus12+

枚举，折叠机折叠状态。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明NON_FOLDABLE0表示当前设备不可折叠。EXPANDED1表示当前设备折叠状态为完全展开。FOLDED2表示当前设备折叠状态为折叠。[]()[]()

#### SceneMode11+

枚举，相机模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明NORMAL_PHOTO1普通拍照模式。详情见[PhotoSession](../../types/interfaces/Interface (PhotoSession).md)NORMAL_VIDEO2普通录像模式。详情见[VideoSession](../../types/interfaces/Interface (VideoSession).md)SECURE_PHOTO12+12安全相机模式。详情见[SecureSession](../../types/interfaces/Interface (SecureSession).md)[]()[]()

#### CameraErrorCode

相机错误码。

接口使用不正确以及on接口监听error状态返回。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明INVALID_ARGUMENT7400101参数缺失或者参数类型不对。OPERATION_NOT_ALLOWED7400102操作流程不对，不允许。SESSION_NOT_CONFIG7400103session 未配置返回。SESSION_NOT_RUNNING7400104session 未运行返回。SESSION_CONFIG_LOCKED7400105session 配置已锁定返回。DEVICE_SETTING_LOCKED7400106设备设置已锁定返回。CONFLICT_CAMERA7400107设备重复打开返回。DEVICE_DISABLED7400108安全原因相机被禁用。DEVICE_PREEMPTED7400109相机被抢占导致无法使用。UNRESOLVED_CONFLICTS_WITH_CURRENT_CONFIGURATIONS12+7400110与当前配置存在冲突。SERVICE_FATAL_ERROR7400201相机服务异常返回。[]()[]()

#### TorchMode11+

枚举，手电筒模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明OFF0常关模式。ON1常开模式。AUTO2自动模式，系统根据环境自动调节手电筒亮度。[]()[]()

#### CameraFormat

枚举，输出格式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明CAMERA_FORMAT_RGBA_88883RGBA_8888格式的图片。CAMERA_FORMAT_YUV_420_SP1003YUV_420_SP格式的图片，对应为NV21格式的图片。CAMERA_FORMAT_JPEG2000JPEG格式的图片。CAMERA_FORMAT_YCBCR_P01011+2001YCBCR_P010格式的图片。CAMERA_FORMAT_YCRCB_P01011+2002YCRCB_P010格式的图片。CAMERA_FORMAT_HEIC13+2003HEIF格式的图片。[]()[]()

#### VideoCodecType13+

枚举，视频编码类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明AVC0视频编码类型AVC。HEVC1视频编码类型HEVC。[]()[]()

#### CameraConcurrentType18+

枚举，镜头并发类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明CAMERA_LIMITED_CAPABILITY0镜头受限能力并发。CAMERA_FULL_CAPABILITY1镜头全量能力并发。[]()[]()

#### ImageRotation

枚举，图片旋转角度。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明ROTATION_00图片旋转0度。ROTATION_9090图片旋转90度。ROTATION_180180图片旋转180度。ROTATION_270270图片旋转270度。[]()[]()

#### QualityLevel

枚举，图片质量。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明QUALITY_LEVEL_HIGH0图片质量高。QUALITY_LEVEL_MEDIUM1图片质量中等。QUALITY_LEVEL_LOW2图片质量差。[]()[]()

#### MetadataObjectType

枚举，metadata流。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明FACE_DETECTION0metadata对象类型，用于人脸检测。[]()[]()

#### FlashMode

枚举，闪光灯模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明FLASH_MODE_CLOSE0闪光灯关闭。FLASH_MODE_OPEN1闪光灯打开。FLASH_MODE_AUTO2自动闪光灯。FLASH_MODE_ALWAYS_OPEN3闪光灯常亮。[]()[]()

#### ExposureMode

枚举，曝光模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明EXPOSURE_MODE_LOCKED0锁定曝光模式。不支持曝光区域中心点设置。EXPOSURE_MODE_AUTO1自动曝光模式。支持曝光区域中心点设置，可以使用[AutoExposure.setMeteringPoint](../../types/interfaces/Interface (AutoExposure).md#ZH-CN_TOPIC_0000002529285769__setmeteringpoint11)接口设置曝光区域中心点。EXPOSURE_MODE_CONTINUOUS_AUTO2连续自动曝光。不支持曝光区域中心点设置。[]()[]()

#### FocusMode

枚举，焦距模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明FOCUS_MODE_MANUAL0手动对焦。通过手动修改相机焦距来改变对焦位置，不支持对焦点设置。FOCUS_MODE_CONTINUOUS_AUTO1连续自动对焦。不支持对焦点设置。FOCUS_MODE_AUTO2自动对焦。支持对焦点设置，可以使用[Focus.setFocusPoint](../../types/interfaces/Interface (Focus).md#ZH-CN_TOPIC_0000002497445804__setfocuspoint11)设置对焦点，根据对焦点执行一次自动对焦。FOCUS_MODE_LOCKED3对焦锁定。不支持对焦点设置。[]()[]()

#### FocusState

枚举，焦距状态。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明FOCUS_STATE_SCAN0触发对焦。FOCUS_STATE_FOCUSED1对焦成功。FOCUS_STATE_UNFOCUSED2未完成对焦。[]()[]()

#### VideoStabilizationMode

枚举，视频防抖模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明OFF0关闭视频防抖功能。LOW1使用基础防抖算法。MIDDLE2使用防抖效果一般的防抖算法，防抖效果优于LOW类型。HIGH3使用防抖效果最好的防抖算法，防抖效果优于MIDDLE类型。AUTO4自动进行选择防抖算法。[]()[]()

#### SmoothZoomMode11+

平滑变焦模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明NORMAL0贝塞尔曲线模式。[]()[]()

#### PreconfigType12+

枚举，提供预配置的类型。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明PRECONFIG_720P0720P预配置。PRECONFIG_1080P11080P预配置。PRECONFIG_4K24K预配置。PRECONFIG_HIGH_QUALITY3高质量预配置。[]()[]()

#### PreconfigRatio12+

枚举，提供预配置的分辨率比例。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明PRECONFIG_RATIO_1_101:1画幅。PRECONFIG_RATIO_4_314:3画幅。PRECONFIG_RATIO_16_9216:9画幅。[]()[]()

#### QualityPrioritization14+

枚举，录像质量优先级。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明HIGH_QUALITY0高录像质量。POWER_BALANCE1功耗平衡的录像质量。[]()[]()

#### WhiteBalanceMode20+

枚举，白平衡模式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明AUTO0自动CLOUDY1阴天INCANDESCENT2白炽光FLUORESCENT3荧光DAYLIGHT4日光MANUAL5手动LOCKED6锁定[]()[]()

#### SystemPressureLevel20+

枚举，系统压力等级。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明SYSTEM_PRESSURE_NORMAL0系统压力正常。SYSTEM_PRESSURE_MILD1系统压力升高，但是系统不会主动管控。SYSTEM_PRESSURE_SEVERE2系统压力可能对图像总质量、性能产生影响。SYSTEM_PRESSURE_CRITICAL3系统压力对图像质量、性能产生显著影响。SYSTEM_PRESSURE_SHUTDOWN4系统压力过高，停止工作。[]()[]()

#### ControlCenterEffectType20+

枚举，相机控制器支持的效果类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明BEAUTY0美颜。PORTRAIT1人像虚化。[]()[]()

#### PhotoQualityPrioritization21+

枚举，拍照画质优先策略。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称值说明HIGH_QUALITY0画质优先，拍照需要较长的时间，以输出高画质的图片。SPEED1性能优先，会降低画质来提升拍照的速度。