[]()[]()

# Interfaces (其他)

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

[]()[]()

#### CameraDevice

相机设备信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明cameraIdstring是否相机ID。cameraPosition[CameraPosition](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__cameraposition)是否相机位置。cameraType[CameraType](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__cameratype)是否相机类型。connectionType[ConnectionType](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__connectiontype)是否相机连接类型。cameraOrientation12+number是否相机安装角度，不会随着屏幕旋转而改变，取值范围为0°-360°，单位：度。hostDeviceName15+string是否远端设备名称。若当前无远端设备，返回为空。hostDeviceType15+[HostDeviceType](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__hostdevicetype15)是否远端设备类型。[]()[]()

#### CameraStatusInfo

相机管理器回调返回的接口实例，该实例表示相机状态信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明camera[CameraDevice](Interfaces (其他) (arkts-apis-camera-i).md#ZH-CN_TOPIC_0000002497605794__cameradevice)否否相机信息。status[CameraStatus](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__camerastatus)否否相机状态。[]()[]()

#### FoldStatusInfo12+

相机管理器回调返回的接口实例，表示折叠机折叠状态信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明supportedCameras[Array<CameraDevice>](Interfaces (其他) (arkts-apis-camera-i).md#ZH-CN_TOPIC_0000002497605794__cameradevice)是否当前折叠状态所支持的相机信息列表。foldStatus[FoldStatus](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__foldstatus12)是否折叠屏折叠状态。[]()[]()

#### Profile

相机配置信息项。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明format[CameraFormat](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__cameraformat)是否输出格式。size[Size](#ZH-CN_TOPIC_0000002497605794__size)是否

分辨率。

设置的是相机的分辨率宽度和高度，而非实际输出图像的宽度和高度。

[]()[]()

#### FrameRateRange

帧率范围。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明minnumber是否最小帧率，单位：fps。maxnumber是否最大帧率，单位：fps。[]()[]()

#### VideoProfile

视频配置信息项，继承[Profile](#ZH-CN_TOPIC_0000002497605794__profile)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明frameRateRange[FrameRateRange](Interfaces (其他) (arkts-apis-camera-i).md#ZH-CN_TOPIC_0000002497605794__frameraterange)是否帧率范围，单位：fps(frames per second)。[]()[]()

#### CameraOutputCapability

相机输出能力项。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明previewProfilesArray<[Profile](#ZH-CN_TOPIC_0000002497605794__profile)>是否支持的预览配置信息集合。photoProfilesArray<[Profile](#ZH-CN_TOPIC_0000002497605794__profile)>是否支持的拍照配置信息集合。videoProfilesArray<[VideoProfile](#ZH-CN_TOPIC_0000002497605794__videoprofile)>是否支持的录像配置信息集合。supportedMetadataObjectTypesArray<[MetadataObjectType](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__metadataobjecttype)>是否支持的metadata流类型信息集合。[]()[]()

#### TorchStatusInfo11+

手电筒回调返回的接口实例，表示手电筒状态信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明isTorchAvailableboolean是否手电筒是否可用。true表示手电筒可用，false表示手电筒不可用。isTorchActiveboolean是否手电筒是否被激活。true表示手电筒被激活，false表示手电筒未被激活。torchLevelnumber是否手电筒亮度等级，取值范围为[0,1]，越靠近1，亮度越大。[]()[]()

#### Size

尺寸参数。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明heightnumber否否图像尺寸高(像素)。widthnumber否否图像尺寸宽(像素)。[]()[]()

#### Point

点坐标用于对焦和曝光配置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明xnumber否否点的x坐标。ynumber否否点的y坐标。[]()[]()

#### CameraConcurrentInfo18+

相机的输出并发能力信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明device[CameraDevice](Interfaces (其他) (arkts-apis-camera-i).md#ZH-CN_TOPIC_0000002497605794__cameradevice)是否相机并发设备。type[CameraConcurrentType](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__cameraconcurrenttype18)是否镜头并发类型。modesArray<[SceneMode](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__scenemode11) >是否相机支持的模式。outputCapabilitiesArray<[CameraOutputCapability](#ZH-CN_TOPIC_0000002497605794__cameraoutputcapability) >是否相机对应模式的输出能力集。[]()[]()

#### Location

图片地理位置信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明latitudenumber否否纬度（度）。取值范围：[-90, 90]。longitudenumber否否经度（度）。取值范围：[-180, 180]。altitudenumber否否海拔（米）。[]()[]()

#### PhotoCaptureSetting

拍摄照片的设置。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明quality[QualityLevel](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__qualitylevel)否是图片质量（默认低）。rotation[ImageRotation](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__imagerotation)否是图片旋转角度（默认0度，顺时针旋转）。location[Location](#ZH-CN_TOPIC_0000002497605794__location)否是图片地理位置信息（默认以设备硬件信息为准）。mirrorboolean否是镜像使能开关（默认关）。使用之前需要使用[isMirrorSupported](Interface (PhotoOutput).md#ZH-CN_TOPIC_0000002529445751__ismirrorsupported)进行判断是否支持。true表示使能，false表示不使能。[]()[]()

#### FrameShutterInfo

拍照帧输出信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明captureIdnumber否否拍照的ID。timestampnumber否否快门时间戳，单位毫秒。[]()[]()

#### FrameShutterEndInfo12+

拍照曝光结束信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明captureIdnumber否否拍照的ID。[]()[]()

#### CaptureStartInfo11+

拍照开始信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明captureIdnumber否否拍照的ID。timenumber否否预估的单次拍照底层出sensor采集帧时间，如果上报-1，代表没有预估时间。[]()[]()

#### CaptureEndInfo

拍照停止信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明captureIdnumber否否拍照的ID。frameCountnumber否否帧数。[]()[]()

#### AutoDeviceSwitchStatus13+

自动切换镜头状态信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明isDeviceSwitchedboolean是否自动切换镜头是否成功。true表示成功，false表示失败。isDeviceCapabilityChangedboolean是否自动切换镜头成功后，其镜头能力值是否发生改变。true表示发生变化，false表示未发生变化。[]()[]()

#### Rect

矩形定义，返回的检测点坐标系以设备充电口在右侧时的横向设备方向为基准。该坐标系左上角为（0，0），右下角为（1，1），其中（topLeftX，topLeftY）表示矩形区域的左上角坐标，width和height分别表示矩形区域的宽和高。因此在实际使用中根据业务诉求需要裁剪或者选择人脸区域时，必须将矩形区域的x坐标和y坐标分别乘以实际相机预览输出流的宽和高，即可得到裁剪后的人脸矩形区域。

实际预览流的宽高指的是相机输出流的分辨率，请参考[profile](Interfaces (其他) (arkts-apis-camera-i).md#ZH-CN_TOPIC_0000002497605794__profile)中的size。

预览流的数据获取请参考[双路预览(ArkTs)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-dual-channel-preview)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明topLeftXnumber否否矩形区域左上角x坐标，范围[0, 1]。topLeftYnumber否否矩形区域左上角y坐标，范围[0, 1]。widthnumber否否矩形宽，范围[0, 1]。heightnumber否否矩形高，范围[0, 1]。[]()[]()

#### MetadataObject

相机元能力信息，[CameraInput](Interface (CameraInput).md)相机信息中的数据来源，通过metadataOutput.on('metadataObjectsAvailable')接口获取。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明type[MetadataObjectType](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__metadataobjecttype)是否metadata 类型。timestampnumber是否当前时间戳，单位为纳秒（ns）。boundingBox[Rect](#ZH-CN_TOPIC_0000002497605794__rect)是否metadata 区域框。[]()[]()

#### SmoothZoomInfo11+

平滑变焦参数信息。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明durationnumber否否平滑变焦总时长，单位ms。[]()[]()

#### ControlCenterStatusInfo20+

相机控制器效果激活状态信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明effectType[ControlCenterEffectType](../../topics/networking/Enums (arkts-apis-camera-e).md#ZH-CN_TOPIC_0000002497445814__controlcentereffecttype20)是否相机控制器效果类型。isActiveboolean是否相机控制器效果激活状态。true表示已激活，false表示未激活。[]()[]()

#### IsoInfo22+

感光度（ISO）参数信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

名称类型只读可选说明isonumber是是ISO值。