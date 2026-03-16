# AR Engine

#### 概述

本模块提供AR Engine（AR引擎服务）的AR增强现实能力相关接口。AR Engine的基础核心能力包含：运动跟踪能力、环境跟踪能力和命中检测能力。

**起始版本：** 5.0.0(12)

#### 汇总

#### 文件

名称

描述

[ar_engine_core.h](../../capi/headers/ar_engine_core.h.md)

本声明用于访问AR Engine（AR引擎服务）的API。提供AR（增强现实）能力的相关接口。AR的基础核心能力，包含：运动跟踪能力、环境跟踪能力和命中检测能力。

#### 结构体

名称

描述

struct [AREngine_ARAugmentedImageSource](../graphics/AREngine_ARAugmentedImageSource.md)

图像数据。

struct [AREngine_ClipPlaneDistance](AREngine_ClipPlaneDistance.md)

裁剪平面距离数据。

struct [AREngine_ARSemanticDensePointData](AREngine_ARSemanticDensePointData.md)

高精几何重建对象的稠密点云数据。

struct [AREngine_ARSemanticDenseCubeData](AREngine_ARSemanticDenseCubeData.md)

高精几何重建对象的立方体数据。

#### 宏定义

名称

描述

[ARENGINE_AABB_POINT_SIZE](#section1046854145717) = 6

包围盒坐标集数组大小。

[ARENGINE_DISTORTION_COUNT](#section2059093619593) = 5

相机畸变参数的个数。

[ARENGINE_POSE_RAW_SIZE](#section14280842115815) = 7

位姿数据数组大小。

[ARENGINE_VIEW_MATRIX_SIZE](#section02261581599) = 16

变换矩阵数组大小。

#### 类型定义

名称

描述

typedef struct [AREngine_ARAnchor](#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)[AREngine_ARAnchor](#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)

锚点对象。

typedef struct [AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872)[AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872)

锚点对象列表。

typedef struct [AREngine_ARAugmentedImage](#section68491824155217)[AREngine_ARAugmentedImage](#section68491824155217)

跟踪图像对象。

typedef struct [AREngine_ARAugmentedImageDatabase](#section152051642330)[AREngine_ARAugmentedImageDatabase](#section152051642330)

跟踪图像数据库对象。

typedef struct [AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)[AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)

当前帧对应的相机信息。

typedef struct [AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba)[AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba)

相机的配置信息。

typedef struct [AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)[AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)

相机内参。

typedef struct [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)

用于配置[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)的能力项（使用哪些能力、模式等）。

typedef struct [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)

AR Engine处理的一帧数据。

typedef struct [AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)[AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)

命中检测结果对象。

typedef struct [AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3)[AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3)

命中检测结果列表。

typedef struct [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)

相机视频流帧对象。

typedef struct [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)

平面对象。

typedef struct [AREngine_ARPoint](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6)[AREngine_ARPoint](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6)

点对象。

typedef struct [AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc)[AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc)

可跟踪的3D点云的集合。

typedef struct [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)

位姿对象。

typedef struct [AREngine_ARSceneMesh](#section543212520614)[AREngine_ARSceneMesh](#section543212520614)

环境mesh数据的集合。

typedef struct [AREngine_ARSemanticDenseData](#section1410813229144)[AREngine_ARSemanticDenseData](#section1410813229144)

表示高精几何重建对象数据的集合。

typedef struct [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)

管理AR Engine的系统状态。

typedef struct [AREngine_ARTarget](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0)[AREngine_ARTarget](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0)

物体对象。

typedef struct [AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970)[AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970)

可跟踪对象，如点、平面等。

typedef struct [AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205)[AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205)

可跟踪对象列表。

typedef void (*[HMS_AREngine_PhotoAvailableCallback](#section430673420224))([OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-oh-nativebuffer) *photoBuffer)

输出拍照流图像回调。

#### 枚举

名称

描述

[AREngine_ARAddAugmentedImageReason](#section2441053595) {

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_NONE = 0,

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_SIZE_NOT_MATCH = 1,

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_LIGHT_ANOMALY = 2,

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_FEATURE_LIMIT = 3,

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_OTHER = 4

}

跟踪失败的可能原因。

[AREngine_ARConfidenceLevel](#section959011484610) {

ARENGINE_DEPTH_CONFIDENCE_LOW = 0,

ARENGINE_DEPTH_CONFIDENCE_MEDIUM = 1,

ARENGINE_DEPTH_CONFIDENCE_HIGH = 2

}

深度置信度。

[AREngine_ARDepthMode](#section12321429115215) {

ARENGINE_DEPTH_MODE_DISABLED = 0,

ARENGINE_DEPTH_MODE_AUTOMATIC = 1

}

深度模式。

[AREngine_ARFocusMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf50530faa0d094182a0db0c73b75d875) {

ARENGINE_FOCUS_MODE_FIXED = 0,

ARENGINE_FOCUS_MODE_AUTO = 1

}

对焦模式。

[AREngine_ARImageDatabaseMode](#section683253471219) {

ARENGINE_ADD_NORMAL = 0,

ARENGINE_ADD_AUTO = 1

}

用于跟踪的特征库图像添加方式。

[AREngine_ARImageFormat](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadfcf7a1211ed12a90f377610d0f838ac) {

ARENGINE_IMAGE_UNKNOWN = 0,

ARENGINE_IMAGE_YUV_420_888 = 2,

ARENGINE_IMAGE_Y_8 = 3,

ARENGINE_IMAGE_Y_16 = 4

}

图像数据格式。

[AREngine_ARImageStreamMode](#section184201559356) {

ARENGINE_IMAGE_STREAM_MODE_PREVIEW = 0,

ARENGINE_IMAGE_STREAM_MODE_PREVIEW_AND_PHOTO = 1

}

设置图片数据流模式，默认情况下系统设置为ARENGINE_IMAGE_STREAM_MODE_PREVIEW。

[AREngine_ARMeshMode](#section19436658201620) {

ARENGINE_MESH_MODE_DISABLED = 0,

ARENGINE_MESH_MODE_ENABLE=1

}

Mesh启用模式。

[AREngine_ARPlaneFindingMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab8e7db52d819359026fc4a82815d3fff) {

ARENGINE_PLANE_FINDING_MODE_DISABLED = 0,

ARENGINE_PLANE_FINDING_MODE_HORIZONTAL = 1,

ARENGINE_PLANE_FINDING_MODE_VERTICAL = 2,

ARENGINE_PLANE_FINDING_MODE_HORIZONTAL_AND_VERTICAL = 3

}

平面搜索模式。

[AREngine_ARPlaneType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga895db37a92155584c5448bee30a8beab) {

ARENGINE_PLANE_FACING_HORIZONTAL_UPWARD = 0,

ARENGINE_PLANE_FACING_HORIZONTAL_DOWNWARD = 1,

ARENGINE_PLANE_FACING_VERTICAL = 2,

ARENGINE_PLANE_FACING_INVALID = 3

}

平面类型。

[AREngine_ARPointOrientationMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0e2893593f4372954fd97519e0a63855) {

ARENGINE_POINT_ORIENTATION_INITIALIZED_TO_IDENTITY = 0,

ARENGINE_POINT_ORIENTATION_ESTIMATED_SURFACE_NORMAL = 1

}

朝向模式。

[AREngine_ARPoseMode](#section1249515330198) {

ARENGINE_POSE_MODE_GRAVITY = 0,

ARENGINE_POSE_MODE_GRAVITY_HEADING = 1

}

AR Engine输出的相机位姿对齐格式。

[AREngine_ARPoseType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae551da7b220b8b38140c3c28882e5010) {

ARENGINE_POSE_TYPE_IDENTITY = 0,

ARENGINE_POSE_TYPE_ROTATE_90 = 1,

ARENGINE_POSE_TYPE_ROTATE_180 = 2,

ARENGINE_POSE_TYPE_ROTATE_270 = 3

}

位姿类型。

[AREngine_ARPowerMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3d925e007e2847e69f22af68ec922507) {

ARENGINE_POWER_MODE_NORMAL = 0,

ARENGINE_POWER_MODE_POWER_SAVING = 1,

ARENGINE_POWER_MODE_PERFORMANCE_FIRST = 2,

ARENGINE_POWER_MODE_BOOST = 3 ,

ARENGINE_POWER_MODE_ULTRA_POWER_SAVING = 11

}

电源功耗模式。

[AREngine_ARPreviewMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadef0f2099b106b872a014ef6551906ae) {

ARENGINE_PREVIEW_MODE_ENABLED = 0,

ARENGINE_PREVIEW_MODE_DISABLED = 1

}

预览模式。

[AREngine_ARSemanticDenseMode](#section09971756142213) {

ARENGINE_SEMANTIC_DENSE_MODE_DISABLED = 0,

ARENGINE_SEMANTIC_DENSE_MODE_NORMAL = 1,

ARENGINE_SEMANTIC_DENSE_MODE_CUBE_VOLUME = 2,

ARENGINE_SEMANTIC_DENSE_MODE_CUBE_SPACE = 3

}

高精几何重建识别模式。

[AREngine_ARSemanticMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga34d3000de29454b99d89406d288d6ed5) {

ARENGINE_SEMANTIC_MODE_NONE = 0,

ARENGINE_SEMANTIC_MODE_PLANE = 1,

ARENGINE_SEMANTIC_MODE_TARGET = 2

}

语义模式。

[AREngine_ARSemanticPlaneLabel](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gafbb6b69fefdc417ba6437ce2fe587cb1) {

ARENGINE_PLANE_UNKNOWN = 0,

ARENGINE_PLANE_WALL = 1,

ARENGINE_PLANE_FLOOR = 2,

ARENGINE_PLANE_SEAT = 3,

ARENGINE_PLANE_TABLE = 4,

ARENGINE_PLANE_CEILING = 5,

ARENGINE_PLANE_DOOR = 6,

ARENGINE_PLANE_WINDOW = 7,

ARENGINE_PLANE_BED = 8,

ARENGINE_PLANE_SPACE = 9,

ARENGINE_CUBE_VOLUME = 10,

ARENGINE_CUBE_SPACE = 11

}

当前平面识别到的语义类型。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d) {

ARENGINE_SUCCESS = 0,

ARENGINE_ERROR_PERMISSION_NOT_GRANTED = 201,

ARENGINE_ERROR_INVALID_ARGUMENT = 401,

ARENGINE_ERROR_DEVICE_NOT_SUPPORTED = 801,

ARENGINE_ERROR_FATAL = 1009200001,

ARENGINE_ERROR_SESSION_PAUSED = 1009200002,

ARENGINE_ERROR_SESSION_NOT_PAUSED = 1009200003,

ARENGINE_ERROR_NOT_TRACKING = 1009200004,

ARENGINE_ERROR_TEXTURE_NOT_SET = 1009200005,

ARENGINE_ERROR_MISSING_GL_CONTEXT = 1009200006,

ARENGINE_ERROR_UNSUPPORTED_CONFIGURATION = 1009200007,

ARENGINE_ERROR_RESOURCE_EXHAUSTED = 1009200008,

ARENGINE_ERROR_NOT_AVAILABLE = 1009200009,

ARENGINE_ERROR_CAMERA_NOT_AVAILABLE = 1009200010,

ARENGINE_ERROR_IMAGE_EXCEED_NUM_LIMIT = 1009200011,

ARENGINE_ERROR_IMAGE_INSUFFICIENT_QUALITY = 1009200012,

ARENGINE_ERROR_IMAGE_INVALID_DATABASE = 1009200013,

ARENGINE_ERROR_IMAGE_ADD_IMAGE_TRACKING_STATE = 1009200014,

ARENGINE_ERROR_NATIVEBUFFER_CREATE_FAILED = 1009200015,

ARENGINE_ERROR_NATIVEBUFFER_WRITE_FAILED = 1009200016

}

接口返回错误码。

[AREngine_ARTargetShapeLabel](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaed68dc13cc314da98d79c88b12d3ae49) {

ARENGINE_TARGET_SHAPE_UNKNOWN = 0,

ARENGINE_TARGET_SHAPE_CUBE = 1,

ARENGINE_TARGET_SHAPE_CIRCLE = 2,

ARENGINE_TARGET_SHAPE_RECTANGLE = 3

}

识别到的物体形状。

[AREngine_ARTrackableType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d) {

ARENGINE_TRACKABLE_BASE = 0x41520100,

ARENGINE_TRACKABLE_PLANE = 0x41520101,

ARENGINE_TRACKABLE_POINT = 0x41520102,

ARENGINE_TRACKABLE_AUGMENTED_IMAGE = 0x41520104,

ARENGINE_TRACKABLE_TARGET = 0x50000008,

ARENGINE_TRACKABLE_INVALID = 0

}

可跟踪对象类型，如平面、点等。

[AREngine_ARTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382) {

ARENGINE_TRACKING_STATE_TRACKING = 0,

ARENGINE_TRACKING_STATE_PAUSED = 1,

ARENGINE_TRACKING_STATE_STOPPED = 2

}

可跟踪对象的跟踪状态。

[AREngine_ARTrackingStateReason](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga67774b71935ef2f8a2ae5e5822c3dcdb) {

ARENGINE_TRACKING_STATE_REASON_NONE = 0,

ARENGINE_TRACKING_STATE_REASON_EXCESSIVE_MOTION = 1,

ARENGINE_TRACKING_STATE_REASON_INSUFFICIENT_FEATURES = 2

}

可能的跟踪失败原因。

[AREngine_ARType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga987888aea7dcaa9abcdb64581c850bf5) {

ARENGINE_TYPE_WORLD = 0x01,

ARENGINE_TYPE_IMAGE = 0x80

}

AR能力类型。

[AREngine_ARUpdateMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabd21cc975ee97b7fb2133af0068ebb5e) {

ARENGINE_UPDATE_MODE_BLOCKING = 0,

ARENGINE_UPDATE_MODE_LATEST = 1

}

调用[HMS_AREngine_ARSession_Update](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259)方法后数据更新模式。

#### 函数

名称

描述

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchor_Detach](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6b731c00cc038f62d21ccb280067114b) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) *anchor)

通知AR Engine停止跟踪并解绑一个锚点。

 注意：

由于此函数并没有释放锚点[AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)，开发者需要通过调用 [HMS_AREngine_ARAnchor_Release](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad04b12f9a2b0415789de5d6e1692f51c)来释放锚点。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchor_GetPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad937acfc5d49f0909bdd84677bb0731a) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) *anchor, [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

获取指定锚点在世界坐标系中的位姿信息。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchor_GetTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6d8c173cc1ef3888f1bedfd6adb2efb3) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) *anchor, [AREngine_ARTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382) *outTrackingState)

获取指定锚点位姿的追踪状态。

void [HMS_AREngine_ARAnchor_Release](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad04b12f9a2b0415789de5d6e1692f51c) ([AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) *anchor)

释放指定锚点对象的内存。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchorList_AcquireItem](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f520dddd96c9918163bff8b68f428fc) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) *anchorList, int32_t index, [AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) **outAnchor)

从锚点对象列表中获取指定位置的锚点信息。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchorList_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga30492334f7a06b98ef0ad5831d33b198) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) **outAnchorList)

创建一个锚点对象列表。

void [HMS_AREngine_ARAnchorList_Destroy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga5b1078469a123466245f65524c9c33be) ([AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) *anchorList)

释放一个锚点对象列表。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchorList_GetSize](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9e96df41cdb973d7e45c714b1bd31fd1) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) *anchorList, int32_t *outSize)

获取锚点对象列表中包含锚点的数量。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImage_AcquireName](#section110712352334) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAugmentedImage](#section68491824155217) *augmentedImage, char *augmentedImageName, uint32_t *outNameLength)

返回跟踪图像的名称。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImage_GetCenterPose](#section498975343520) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAugmentedImage](#section68491824155217) *augmentedImage, [AREngine_ARPose](#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

获取跟踪图像中心点在世界坐标系中的位姿信息。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImage_GetExtendX](#section917593011382) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAugmentedImage](#section68491824155217) *augmentedImage, float *outExtendX)

以图像的中心点为坐标原点，获取X轴上的估计值。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImage_GetExtendZ](#section9630192711390) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAugmentedImage](#section68491824155217) *augmentedImage, float *outExtendZ)

以图像的中心点为坐标原点，获取Z轴上的估计值。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImage_GetIndex](#section27041685401) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAugmentedImage](#section68491824155217) *augmentedImage, uint32_t *outIndex)

获取跟踪图像数据库中跟踪图像的索引。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_AddImage](#section0315115618403) ([AREngine_ARAugmentedImageDatabase](#section152051642330) *database, const [AREngine_ARAugmentedImageSource](../graphics/AREngine_ARAugmentedImageSource.md) *image, uint32_t *outIndex, [AREngine_ARAddAugmentedImageReason](#section2441053595) *outReason)

将图像添加到图像数据库并输出对应图像的索引。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_Create](#section4108822184411) ([AREngine_ARAugmentedImageDatabase](#section152051642330) **outDatabase)

创建一个空的跟踪图像数据库。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_Deserialize](#section1619582764511) (const uint8_t *buffer, const uint64_t bufSize, [AREngine_ARAugmentedImageDatabase](#section152051642330) **outDatabase)

反序列化特征数据库。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_Destroy](#section14702121818469) ([AREngine_ARAugmentedImageDatabase](#section152051642330) *database)

释放图像数据库对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_GetAddMode](#section1731662218476) (const [AREngine_ARAugmentedImageDatabase](#section152051642330) *database, [AREngine_ARImageDatabaseMode](#section683253471219) *outAddMode)

获取添加跟踪图像模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_SetAddMode](#section2579104674818) (const [AREngine_ARAugmentedImageDatabase](#section152051642330) *database, [AREngine_ARImageDatabaseMode](#section683253471219) addMode)

设置添加跟踪图像模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_GetCapacity](#section650873916491) (const [AREngine_ARAugmentedImageDatabase](#section152051642330) *database, uint32_t *outCapacity)

获取可以添加的最大图像数。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_GetImageCount](#section6183812506) (const [AREngine_ARAugmentedImageDatabase](#section152051642330) *database, uint32_t *outImageCount)

获取数据库中存储的图像数量。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_Serialize](#section6536162875117) (const [AREngine_ARAugmentedImageDatabase](#section152051642330) *database, uint8_t **outBuffer, uint64_t *outBufSize)

序列化特征数据库。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetDisplayOrientedPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga088648130f3a91cdf8d7b95f5ee1faf2) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

设置outPose为虚拟相机（面向显示）在世界空间中的位姿，用以将AR内容渲染到最新帧中。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetImageIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8e6f32adc3bd59504042d4e18bfb3432) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *outIntrinsics)

获取物理相机离线内参的对象，可通过该对象获取相机的焦距、图像尺寸、主轴点和畸变参数。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga00df108c4ba187967a10e9c4d2e27d3a) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

设置outPose为最新帧中物理相机在世界空间中的位姿。该位姿是OpenGL相机的位姿。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetProjectionMatrix](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga01feacf9cd393a0598e2ac5cf7b61693) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ClipPlaneDistance](AREngine_ClipPlaneDistance.md) clipPlaneDistance, float *outDestColMajor4x4, int32_t destColMajor4x4Num)

获取用于在相机图像上层渲染虚拟内容的投影矩阵，可用于相机坐标系到裁剪坐标系转换。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dc931eee56ae5ea899f8acc08eb3f36) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ARTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382) *outTrackingState)

获取相机的当前追踪状态。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetTrackingStateReason](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab5411813f2e4ac6de4ebbccfc1bbbd35) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ARTrackingStateReason](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga67774b71935ef2f8a2ae5e5822c3dcdb) *outTrackingStateReason)

获取相机的当前追踪状态为[ARENGINE_TRACKING_STATE_PAUSED](#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)时的原因。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetViewMatrix](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga130b4689d7d967e812d24fc2be071d68) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, float *outColMajor4x4, int32_t colMajor4x4Num)

获取最新帧中相机的视图矩阵。

void [HMS_AREngine_ARCamera_Release](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga16909b4002b9c6250dad88bb8397adc9) ([AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera)

释放对相机的引用。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraConfig_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac6402425c6c6390da3c4e57d328da443) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba) **outCameraConfig)

创建一个相机配置对象。

void [HMS_AREngine_ARCameraConfig_Destroy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2540153f0404799943470c41dff3b5f4) ([AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba) *cameraConfig)

释放相机配置对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraConfig_GetImageDimensions](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac3dc81c1c9e6945dd4a3de30e45ccc8f) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba) *cameraConfig, int32_t *outWidth, int32_t *outHeight)

从相机配置对象中获取相机送到CPU处理的图像尺寸。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraConfig_GetTextureDimensions](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga19ade172d2e2dcd67495f6be1bcc2706) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba) *cameraConfig, int32_t *outWidth, int32_t *outHeight)

从相机配置对象中获取相机送到GPU处理的图像纹理尺寸。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraIntrinsics_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga027e92d8f7b25e6e577a9658545e2c2a) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) **outIntrinsics)

创建一个相机内参对象。

void [HMS_AREngine_ARCameraIntrinsics_Destroy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga09323e31d8bd08e5c1d60bccb118b68b) ([AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *intrinsics)

释放指定的相机内参对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraIntrinsics_GetDistortion](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7caab88bb0e859921004ab1121ee2b5d) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *intrinsics, float *outDistortion, int32_t distortionNum)

获取相机的畸变系数。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraIntrinsics_GetFocalLength](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab57c6586ac4d2da1b87f1c0394ffc1b3) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *intrinsics, float *outFocalX, float *outFocalY)

获取指定相机的焦距，焦距以像素为单位。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraIntrinsics_GetImageDimensions](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaab99bc9ba5b9b734ef11888fe2bb3f86) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *intrinsics, int32_t *outWidth, int32_t *outHeight)

获取相机图像的尺寸，包括宽度和高度，以像素为单位。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraIntrinsics_GetPrincipalPoint](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb38c1df26e1af9d993574c7f13b8f5c) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *intrinsics, float *outPrincipalX, float *outPrincipalY)

获取指定相机的主轴点，主点位置以像素为单位表示。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga97376432184fe702f2451e32b52298fb) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) **outConfig)

创建具有适当默认配置的配置对象。

void [HMS_AREngine_ARConfig_Destroy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac86d0db69e8658f2f6bd267d7b288c0a) ([AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config)

释放指定的配置对象的内存空间。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetARType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga827ca7c2c2f288338f781e87e28ef996) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga987888aea7dcaa9abcdb64581c850bf5) *type)

获取当前使用的AR能力类型。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetARType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf12b21d8591c5265f8a0e847b716d65c) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga987888aea7dcaa9abcdb64581c850bf5) type)

设置当前要使用的AR能力类型。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetCameraPreviewMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf4746b3377bd69a52d0587a582cc4679) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPreviewMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadef0f2099b106b872a014ef6551906ae) *outMode)

获取当前的预览模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetCameraPreviewMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac5e6992e38516f75cc6faf1a34047f5d) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPreviewMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadef0f2099b106b872a014ef6551906ae) mode)

设置预览模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetDepthMode](#section6878812194715) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARDepthMode](#section12321429115215) *outDepthMode)

获取当前的深度模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetDepthMode](#section12608229155413) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARDepthMode](#section12321429115215) depthMode)

设置深度模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetFocusMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae92d8207f54468354ed52ad132e172f9) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARFocusMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf50530faa0d094182a0db0c73b75d875) *focusMode)

获取当前配置的相机对焦模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetFocusMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bcf745a74196cb21dca5e4feec18325) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARFocusMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf50530faa0d094182a0db0c73b75d875) focusMode)

设置当前所需的相机对焦模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetMaxMapSize](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga65bae175f2ac6da6dca71988c3ac37df) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, uint64_t *maxMapSize)

获取地图数据使用的最大内存大小。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetMaxMapSize](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga82fd530a4377b0c0e01c9031aa238372) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, uint64_t maxMapSize)

设置地图数据最大使用内存大小。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetMeshMode](#section5607016063) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARMeshMode](#section19436658201620) *outMeshMode)

获取当前mesh模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetMeshMode](#section53081741287) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARMeshMode](#section19436658201620) meshMode)

设置mesh模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetPlaneFindingMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8aa9412802c98ece87d140b063f50839) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPlaneFindingMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab8e7db52d819359026fc4a82815d3fff) *planeFindingMode)

获取当前配置的平面识别模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetPlaneFindingMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga884a7db93778e24eef0dfaa794c45674) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPlaneFindingMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab8e7db52d819359026fc4a82815d3fff) planeFindingMode)

设置当前所需的平面识别模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetPoseMode](#section7289861874) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPoseMode](#section1249515330198) *poseMode)

获取相机输出的位姿坐标系对齐模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetPoseMode](#section53221628698) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPoseMode](#section1249515330198) poseMode)

设置相机输出的位姿坐标系对齐模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetPowerMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3c02b15907c21a20e6efcd018750a29f) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPowerMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3d925e007e2847e69f22af68ec922507) *powerMode)

获取当前配置的功耗模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetPowerMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac5048a3977d04d75ba622a0411b03774) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPowerMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3d925e007e2847e69f22af68ec922507) powerMode)

设置功耗模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetPreviewSize](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8e9f74ef162604dc9bf07204237b45ab) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, uint32_t width, uint32_t height)

设置预览画面尺寸，仅支持宽高比为4:3，超出范围的值将自动采用默认分辨1440*1080填充。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetSemanticDenseMode](#section1099254315514) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARSemanticDenseMode](#section09971756142213) *outSemanticDenseMode)

获取已设置的高精几何重建模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetSemanticDenseMode](#section1569718841012) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARSemanticDenseMode](#section09971756142213) semanticDenseMode)

设置当前所需的高精几何重建模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetSemanticMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga61325a1e0157e477c2ff95c1c0030567) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARSemanticMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga34d3000de29454b99d89406d288d6ed5) *mode)

获取已设置成功的语义识别模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetSemanticMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae87c1ef02b6e9bab123fae2086da248) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARSemanticMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga34d3000de29454b99d89406d288d6ed5) mode)

设置当前所需的语义识别模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetUpdateMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf32a3cb1f345cd5a243683ecdec63cef) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARUpdateMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabd21cc975ee97b7fb2133af0068ebb5e) *updateMode)

获取当前配置的预览更新模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetUpdateMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga871c8aebc084cbba41220d255c46803b) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARUpdateMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabd21cc975ee97b7fb2133af0068ebb5e) updateMode)

设置预览更新模式。

[AREngine_ARStatus](#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetPhotoStreamSize](#section21861035164816)(const [AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, uint32_t width, uint32_t height)

PreviewAndPhotoMode模式下，设置从拍照流获取图像的分辨率。仅支持4:3大小分辨率。如果超出这个范围，系统会自动设置图像分辨率为该设备在4:3宽高比下的最高分辨率。

[AREngine_ARStatus](#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetImageStreamMode](#section10809428846)(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARImageStreamMode mode)

设置图像流模式。

[AREngine_ARStatus](#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetImageStreamMode](#section387103819713)(const [AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARImageStreamMode](#section184201559356) *outMode)

获取图像流模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga5295c975a0ff3d633a1dde5a8eb70863) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) **outCamera)

获取当前帧的相机参数对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireCameraImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad5619c3cbd2b9ea0cfeff22b72f8d81d) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) **outImage)

获取相机的当前帧的图像。

[AREngine_ARStatus](#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireCameraPhotoImage](#section18751333994)(const [AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const A[AREngine_ARFrame](#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)*frame, [HMS_AREngine_PhotoAvailableCallback](#section430673420224) photoCallback)

获取当前帧的拍照流图片。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireDepthConfidenceImage](#section4424501286) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) **outConfidenceImage)

获取当前帧的深度置信度图像。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireDepthImage16Bits](#section138574584154) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) **outDepthImage);

获取当前帧的深度图像。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquirePointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga877f7fc9d9c303f1fd8efb00ec383b34) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc) **outPointCloud)

返回当前帧的点云数据。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireSceneMesh](#section25711548111020) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARSceneMesh](#section543212520614) **outSceneMesh)

获取当前帧的mesh信息。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireSemanticDenseData](#section17136162216547) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARSemanticDenseData](#section1410813229144) **outSemanticDenseData);

获取当前帧的高精几何重建对象数据。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadfcb9589137a39c5afcb217e18853a9d) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) **outFrame)

创建一个新的[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)对象，将指针存储到*outFrame中。

void [HMS_AREngine_ARFrame_Destroy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0ca6a470025dbccb44b4fdefc26513f6) ([AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame)

删除当前[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_GetDisplayGeometryChanged](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4fb55932c19ef9c49523a0a5385a9242) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, int32_t *outGeometryChangeState)

获取显示（长宽和旋转）是否发生变化。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_GetTimestamp](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga266c2e5c80a961163d3422b96b079701) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, int64_t *outTimestampNs)

获取当前帧对应的时间戳信息，单位为ns。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_GetUpdatedTrackables](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0fc74148f836093108b85ab4c7ecdd1c) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARTrackableType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d) filterType, [AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) *outTrackableList)

获取[HMS_AREngine_ARSession_Update](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259)更新后发生变化的指定类型的可跟踪对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_HitTest](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad9377f19261d5bbc2044497729b4e0df) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, float pixelX, float pixelY, [AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3) *hitResultList)

从摄像头发射一条射线，该射线的方向由预览区上的点(pixelX，pixelY)确定(pixelX，pixelY可以通过XComponent的[DispatchTouchEvent()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback#dispatchtouchevent)事件获取)。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_TransformDisplayUvCoords](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4c7699abab9b82369c0d42b496667fc7) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, int32_t elementSize, const float *uvsIn, float *uvsOut)

调整纹理映射坐标，以便可以正确地显示相机捕捉到的背景图片。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResult_AcquireNewAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga30abe7b3457c991815dd79fcfaf26018) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *hitResult, [AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) **outAnchor)

在碰撞命中位置创建一个新的锚点。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResult_AcquireTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac3a02e30bb7706d87c4c29d38b363840) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *hitResult, [AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) **outTrackable)

获取被命中的可追踪对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResult_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4b06bcca0f6fc0b081ef8210765d9c91) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) **outHitResult)

创建一个空的命中检测结果对象。

void [HMS_AREngine_ARHitResult_Destroy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3b3796d7186cb09c4861ebabe2d5b654) ([AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *hitResult)

释放命中检测结果对象使用的内存。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResult_GetDistance](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6929e52bb352622806d2298497c6b4c8) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *hitResult, float *outDistance)

返回从相机到命中位置的距离，以m为单位。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResult_GetHitPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8beaa085410712425041e81f9bc6aa09) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *hitResult, [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

获取交点的位姿。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResultList_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad5dfe929e7952954764d05b8d69abace) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3) **outHitResultList)

创建一个命中检测结果对象列表。

void [HMS_AREngine_ARHitResultList_Destroy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae065ef9a28168b420c96b72ca80c892) ([AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3) *hitResultList)

释放命中检测结果对象列表，以及其中的所有命中检测结果对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResultList_GetItem](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf165c7a1c9ae003cac2a1c2ac2e5e5c4) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3) *hitResultList, int32_t index, [AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *outHitResult)

在命中检测结果列表中获取指定索引的命中检测结果对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResultList_GetSize](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga131d081663d457c594664c977bd9033c) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3) *hitResultList, int32_t *outSize)

获取命中检测结果对象列表中包含的对象数。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetFormat](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga852b211c7e285ccc154295eb1c604f37) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, [AREngine_ARImageFormat](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadfcf7a1211ed12a90f377610d0f838ac) *outFormat)

获取当前帧的图像格式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetHeight](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga34c21703e40868ce0fe5795fa82a08fa) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t *outHeight)

获取当前帧的图像数据的高度。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetWidth](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2c2454e9611dc68e26b8fefb39021597) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t *outWidth)

获取当前帧的图像数据的宽度。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetNativeBuffer](#section367418528228) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, [OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer) **outNativeBuffer);

获取当前帧图像对象的NativeBuffer数据。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetPlaneCount](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga107fbf6737b499aea941fbbfeab1b3e9) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t *outCount)

获取当前帧图像的平面数量。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetPlaneData](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaedc5247eb982443c3f8a2dc8cfd5fdee) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t planeIndex, const uint8_t **outData, int32_t *outLength)

获取当前帧图像的平面数据。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetPlanePixelStride](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac31f741115e6936f7b8e3ef94579d270) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t planeIndex, int32_t *outPixelStride)

获取图像中两个连续像素的起点之间的字节距离。像素步幅始终大于0。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetPlaneRowStride](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga35e66d4a869539d2261e41df17730691) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t planeIndex, int32_t *outRowStride)

获取图像中两个连续像素行的起始位置之间的字节数。行间距始终大于0。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetTimestamp](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7d2c7f1d596d41bfe1c181057283b740) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int64_t *outTimestamp)

获取图像的时间戳。

void [HMS_AREngine_ARImage_Release](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga42fd222576edf6507f6d319a3374cd94) ([AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image)

释放当前帧的图像对象,，由[HMS_AREngine_ARFrame_AcquireCameraImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad5619c3cbd2b9ea0cfeff22b72f8d81d)创建的对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_AcquireSubsumedBy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga56686d6a5ff45fcb04812538aa807ac3) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) **outSubsumedBy)

获取平面的父平面（一个平面被另一个平面合并时，会产生父平面），如果无父平面返回为NULL。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetCenterPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabbb03027afb984be8542d00d2eebd063) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

获取从平面的局部坐标系到世界坐标系转换的位姿信息。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetExtentX](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga49db45eb6072384247a057c403a69c8d) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, float *outExtentX)

获取平面的矩形边界沿平面局部坐标系X轴的长度，如矩形的宽度。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetExtentZ](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4daf6a365f1107f146c5d264dfee292c) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, float *outExtentZ)

获取平面的矩形边界沿平面局部坐标系Z轴的长度，如矩形的高度。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetLabel](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga913456f9586c82adcdbcae291ec8e17c) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, [AREngine_ARSemanticPlaneLabel](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gafbb6b69fefdc417ba6437ce2fe587cb1) *label)

获取平面的语义类型，如桌面、地板等。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetPolygon](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3537ce62e6a92dcdbddff0f39de0fae3) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, float *outPolygonXz, int32_t polygonSize)

获取检测到平面的二维顶点数组，格式为[x1，z1，x2，z2，...]。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetPolygonSize](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga98760556eee2a4a69c33699b7ce3edc6) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, int32_t *outPolygonSize)

获取检测到平面的二维顶点数组大小。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8aa35ca398b38eee8c53bd1db8d6ab88) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, [AREngine_ARPlaneType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga895db37a92155584c5448bee30a8beab) *outPlaneType)

获取平面的类型。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_IsPoseInExtents](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8ded2552569a9e89c1befe8f15123af6) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, const [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, int32_t *outPoseInExtents)

判断位姿是否位于平面的矩形范围内。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_IsPoseInPolygon](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab00d22a9c927a2745821023e8e72a8d0) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, const [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, int32_t *outPoseInPolygon)

判断位姿是否位于平面的多边形范围内。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPoint_GetOrientationMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad869ed2a4ac6409bf94c768d9d1d8127) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPoint](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6) *point, [AREngine_ARPointOrientationMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0e2893593f4372954fd97519e0a63855) *outOrientationMode)

获取输入点的朝向模式。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPoint_GetPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8255eece88d8dc76c554eed360fb7c7b) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPoint](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6) *point, [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

获取输入点的位姿信息。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPointCloud_GetData](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4061cacb3f3ce45e529acb9afbcdc5ce) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc) *pointCloud, const float **outPointCloudData)

获取点云中所有点的坐标及置信度数组。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPointCloud_GetNumberOfPoints](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad9701fe82b6468f33f6741cc7f347d45) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc) *pointCloud, int32_t *outNumberOfPoints)

获取点云中所有点的坐标及置信度数组大小。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPointCloud_GetTimestamp](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9e430d52fa372903bcbe40ca5f6a9d9d) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc) *pointCloud, int64_t *outTimestampNs)

获取检测到当前特征点云的时间，以ns为单位。

void [HMS_AREngine_ARPointCloud_Release](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3751c56632f7f6d383cf9409ec6769bc) ([AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc) *pointCloud)

释放点云对象使用的内存。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPose_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gafb471f39563ca1a4947d4f87c77e24e2) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const float *poseRaw, const uint32_t poseRawSize, [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) **outPose)

分配并初始化一个新的位姿对象。

void [HMS_AREngine_ARPose_Destroy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab988254f4654c8aaadb5740061846057) ([AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose)

释放位姿对象使用的内存。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPose_GetMatrix](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga787f4daf9efd13c79737ef18cef6d7c7) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, float *outMatrixColMajor4x4, int32_t matrixColMajor4x4Size)

将位姿数据转换成4X4的矩阵。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPose_GetPoseRaw](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1ee66c006ffe8255cc04f2a24c277709) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, float *outPoseRaw, int32_t poseRawSize)

从位姿对象提取位姿数据。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSceneMesh_AcquireIndexList](#section7629354145) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSceneMesh](#section543212520614) *sceneMesh, int32_t *outData, int32_t dataSize)

获取mesh面片的索引集合。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSceneMesh_AcquireIndexListSize](#section12621161917152) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSceneMesh](#section543212520614) *sceneMesh, int32_t *outSize)

获取mesh面片的索引个数。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSceneMesh_AcquireVertexList](#section2126723166) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSceneMesh](#section543212520614) *sceneMesh, float *outData, int32_t dataSize)

获取mesh的顶点集合。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSceneMesh_AcquireVertexNormalList](#section115249588168) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSceneMesh](#section543212520614) *sceneMesh, float *outData, int32_t dataSize)

获取mesh面片的法向量集合。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSceneMesh_AcquireVerticesSize](#section1860218429179) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSceneMesh](#section543212520614) *sceneMesh, int32_t *outSize)

获取mesh的顶点个数。

void [HMS_AREngine_ARSceneMesh_Release](#section446832931813) ([AREngine_ARSceneMesh](#section543212520614) *SceneMesh)

释放当前帧的mesh信息。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSemanticDense_AcquireCubeData](#section7554459949) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSemanticDenseData](#section1410813229144) *semanticDenseData, [AREngine_ARSemanticDenseCubeData](AREngine_ARSemanticDenseCubeData.md) **outCubeData)

获取识别到的高精几何重建对象数据中的立方体数据。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSemanticDense_AcquireCubeDataSize](#section383013458212) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSemanticDenseData](#section1410813229144) *semanticDenseData, int64_t *outSize)

获取识别到的高精几何重建对象数据中的立方体数量。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSemanticDense_AcquirePointData](#section288942515910) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSemanticDenseData](#section1410813229144) *semanticDenseData, [AREngine_ARSemanticDensePointData](AREngine_ARSemanticDensePointData.md) **outPointData)

获取识别到的高精几何重建对象数据中的稠密点云数据。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSemanticDense_AcquirePointDataSize](#section6669112114532) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSemanticDenseData](#section1410813229144) *semanticDenseData, int64_t *outSize)

获取识别到的高精几何重建对象数据中的稠密点云数量。

void [HMS_AREngine_ARSemanticDense_Release](#section390280482) ([AREngine_ARSemanticDenseData](#section1410813229144) *semanticDenseData)

释放高精几何重建对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_AcquireNewAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2ae6dee4baab7cf2c5d0cdd1c845cf0c) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, [AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) **outAnchor)

创建一个持续跟踪的锚点。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Configure](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6394ae995148abbe3d00082817bf320a) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config)

配置[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)会话。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga47713cb18234569e03b5216b6c8442d3) (void *env, void *applicationContext, [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) **outSessionPointer)

创建一个新的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)会话。

void [HMS_AREngine_ARSession_Destroy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3a2be9998c9cd6373ff1f5209b645a95) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session)

释放[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)会话使用的资源。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_GetCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga31b28b049ac25b94c02fb27ca56c497d) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba) *outCameraConfig)

获取相机配置信息。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_GetAllAnchors](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4828823e5f3cc1067dbd6a2c8b9c9635) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) *outAnchorList)

获取所有锚点，包括[AREngine_ARTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)中包含的所有状态下的锚点。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_GetAllTrackables](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac5b39338f95317671d8de6d4f409cf9c) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARTrackableType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d) filterType, [AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) *outTrackableList)

获取所有指定类型的可跟踪对象集合。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Pause](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga09dedb5c633141321591db0981629de1) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session)

暂停会话，停止相机预览流，不清除平面和锚点数据，释放相机（否则其他应用无法使用相机服务）。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Resume](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7138d56b767738b8aadcbc74f4c328db) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session)

开始运行[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)，或者在调用[HMS_AREngine_ARSession_Pause](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga09dedb5c633141321591db0981629de1)以后恢复[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)的运行状态。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_SetCameraGLTexture](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac697e4be36db63ed6098f154aa9ac01c) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, uint32_t textureId)

设置可用于存储相机预览流数据的OpenGL纹理。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_SetDisplayGeometry](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3f23bf747def8303c3fb261a9e9a2286) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARPoseType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae551da7b220b8b38140c3c28882e5010) rotation, int32_t width, int32_t height)

设置显示的高和宽，以像素为单位。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Stop](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0b7405ae0fc1e1257103192a2b7b48d3) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session)

停止AR Engine，停止相机预览流，清除平面和锚点数据，并释放相机，终止本次会话。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Update](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *outFrame)

更新AR Engine的计算结果。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTarget_GetAxisAlignedBoundingBox](#ZH-CN_TOPIC_0000002500306234__gaaf54fe7a3c38dbb4c0bcaa3c83dd0d76)(const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTarget](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0) *target, float *outAabb, int32_t aabbSize)

获取语义物体最小外接包围盒坐标，坐标格式为(xmin，ymin，zmin，xmax，ymax，zmax)。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTarget_GetCenterPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaa9a304640d54942be238a7ddd2c13276) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTarget](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0) *target, [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outARPose)

获取从目标语义对象的局部坐标系到世界坐标系转换的位姿对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTarget_GetRadius](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0fb23a8217c7191f765b0d656160ffa1) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTarget](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0) *target, float *radius)

获取语义物体的球体半径。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTarget_GetShapeType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6c702efd6c4fdc3eeb8f5dc38968ec65) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTarget](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0) *target, [AREngine_ARTargetShapeLabel](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaed68dc13cc314da98d79c88b12d3ae49) *shape)

获取语义物体的形状类型。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackable_AcquireNewAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacf03897f0ac28d338143f3fa350c1491) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) *trackable, [AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, [AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) **outAnchor)

通过可跟踪对象的位姿信息创建对应的锚点对象，该锚点将和当前的可跟踪对象绑定。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackable_GetAnchors](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7a3b98b0281f2e31ac3d9c47b0dffab) ([AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) *trackable, [AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) *outAnchorList)

获取绑定到输入可跟踪对象的锚点对象列表。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackable_GetTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7805739b2dbeae0d3b04242538a4a840) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) *trackable, [AREngine_ARTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382) *outTrackingState)

获取当前可跟踪对象的跟踪状态。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackable_GetType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga72c800291d0df799fa795db3d3485e4f) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) *trackable, [AREngine_ARTrackableType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d) *outTrackableType)

获取可跟踪对象的类型。

void [HMS_AREngine_ARTrackable_Release](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6ec735cd18e955442f29416ff58ddd64) ([AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) *trackable)

释放可跟踪对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackableList_AcquireItem](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab1782eeeeddc01b77a140af915cb351c) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) *trackableList, int32_t index, [AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) **outTrackable)

从可跟踪列表中获取指定index的对象。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackableList_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7860d63545ab862e9f3b1fe0a8a83d42) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) **outTrackableList)

创建一个可跟踪对象列表。

void [HMS_AREngine_ARTrackableList_Destroy](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad6e2ffd71d7cdaa3ae553937437b37c8) ([AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) *trackableList)

释放可跟踪对象列表，以及它持有的所有锚点引用。

[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackableList_GetSize](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad9729d4436f3d969286f31b33d07513e) (const [AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) *trackableList, int32_t *outSize)

获取此列表中的可跟踪对象的数量。

#### 宏定义说明

#### ARENGINE_AABB_POINT_SIZE

```ets
const static int32_t ARENGINE_AABB_POINT_SIZE = 6
```

**描述：**

包围盒坐标集数组大小。

**起始版本：** 5.0.0(12)

#### ARENGINE_DISTORTION_COUNT

```ets
const static int32_t ARENGINE_DISTORTION_COUNT = 5
```

**描述：**

相机畸变参数的个数。

**起始版本：** 5.0.0(12)

#### ARENGINE_POSE_RAW_SIZE

```ets
const static int32_t ARENGINE_POSE_RAW_SIZE = 7
```

**描述：**

位姿数据数组大小。

**起始版本：** 5.0.0(12)

#### ARENGINE_VIEW_MATRIX_SIZE

```ets
const static int32_t ARENGINE_VIEW_MATRIX_SIZE = 16
```

**描述：**

变换矩阵数组大小。

**起始版本：** 5.0.0(12)

#### 类型定义说明

#### AREngine_ARAnchor

```ets
typedef struct AREngine_ARAnchor AREngine_ARAnchor
```

**描述**

锚点对象。

描述与可跟踪对象关联的空间位置。

**起始版本：** 5.0.0(12)

#### AREngine_ARAnchorList

```ets
typedef struct AREngine_ARAnchorList AREngine_ARAnchorList
```

**描述**

锚点对象列表。

包含一系列锚点对象。

**起始版本：** 5.0.0(12)

#### AREngine_ARAugmentedImage

```ets
typedef struct AREngine_ARAugmentedImage AREngine_ARAugmentedImage
```

**描述**

跟踪图像对象。

**起始版本：** 5.1.0(18)

#### AREngine_ARAugmentedImageDatabase

```ets
typedef struct AREngine_ARAugmentedImageDatabase AREngine_ARAugmentedImageDatabase
```

**描述**

跟踪图像数据库对象。

**起始版本：** 5.1.0(18)

#### AREngine_ARCamera

```ets
typedef struct AREngine_ARCamera AREngine_ARCamera
```

**描述**

当前帧对应的相机信息。

**起始版本：** 5.0.0(12)

#### AREngine_ARCameraConfig

```ets
typedef struct AREngine_ARCameraConfig AREngine_ARCameraConfig
```

**描述**

相机的配置信息。

如CPU图像的尺寸，GPU纹理的尺寸。

**起始版本：** 5.0.0(12)

#### AREngine_ARCameraIntrinsics

```ets
typedef struct AREngine_ARCameraIntrinsics AREngine_ARCameraIntrinsics
```

**描述**

相机内参。

包括fx；fy；cx；cy；畸变参数。

**起始版本：** 5.0.0(12)

#### AREngine_ARConfig

```ets
typedef struct AREngine_ARConfig AREngine_ARConfig
```

**描述**

用于配置[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)的能力项（使用哪些能力、模式等）。

**起始版本：** 5.0.0(12)

#### AREngine_ARFrame

```ets
typedef struct AREngine_ARFrame AREngine_ARFrame
```

**描述**

AR Engine处理的一帧数据。

**起始版本：** 5.0.0(12)

#### AREngine_ARHitResult

```ets
typedef struct AREngine_ARHitResult AREngine_ARHitResult
```

**描述**

命中检测结果对象。

描述单个可跟踪对象的命中检测结果。

**起始版本：** 5.0.0(12)

#### AREngine_ARHitResultList

```ets
typedef struct AREngine_ARHitResultList AREngine_ARHitResultList
```

**描述**

命中检测结果列表。

包含一系列命中检测的结果对象。

**起始版本：** 5.0.0(12)

#### AREngine_ARImage

```ets
typedef struct AREngine_ARImage AREngine_ARImage
```

**描述**

相机视频流帧对象。

**起始版本：** 5.0.0(12)

#### AREngine_ARPlane

```ets
typedef struct AREngine_ARPlane AREngine_ARPlane
```

**描述**

平面对象。

描述被检测到的可跟踪平面信息。

**起始版本：** 5.0.0(12)

#### AREngine_ARPoint

```ets
typedef struct AREngine_ARPoint AREngine_ARPoint
```

**描述**

点对象。

描述被检测到的可跟踪点数据。

**起始版本：** 5.0.0(12)

#### AREngine_ARPointCloud

```ets
typedef struct AREngine_ARPointCloud AREngine_ARPointCloud
```

**描述**

可跟踪的3D点云的集合。

**起始版本：** 5.0.0(12)

#### AREngine_ARPose

```ets
typedef struct AREngine_ARPose AREngine_ARPose
```

**描述**

位姿对象。

描述从一个坐标系到另一个坐标系的不可变的刚体变换，例如平移或旋转。

详细可参考[世界坐标系与位姿示意](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-pose#section134071231142820)。

**起始版本：** 5.0.0(12)

#### AREngine_ARSceneMesh

```ets
typedef struct AREngine_ARSceneMesh AREngine_ARSceneMesh
```

**描述**

环境mesh数据的集合。

**起始版本：** 5.1.0(18)

#### AREngine_ARSemanticDenseData

```ets
typedef struct AREngine_ARSemanticDenseData AREngine_ARSemanticDenseData
```

**描述**

表示高精几何重建对象数据的集合。

**起始版本：** 6.0.0(20)

#### AREngine_ARSession

```ets
typedef struct AREngine_ARSession AREngine_ARSession
```

**描述**

管理AR Engine的系统状态。

**起始版本：** 5.0.0(12)

#### AREngine_ARTarget

```ets
typedef struct AREngine_ARTarget AREngine_ARTarget
```

**描述**

物体对象。

描述被检测到的可跟踪语义目标信息，例如语义平面。

**起始版本：** 5.0.0(12)

#### AREngine_ARTrackable

```ets
typedef struct AREngine_ARTrackable AREngine_ARTrackable
```

**描述**

可跟踪对象，如点、平面等。

应用获取到此对象后，如需对此对象进行具体操作，如通过[HMS_AREngine_ARPlane_GetCenterPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabbb03027afb984be8542d00d2eebd063)接口获取平面的中心点位置， 通过[HMS_AREngine_ARPoint_GetPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8255eece88d8dc76c554eed360fb7c7b)接口获取点的位姿信息等， 可以根据可跟踪对象类型（通过[HMS_AREngine_ARTrackable_GetType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga72c800291d0df799fa795db3d3485e4f)接口获取）转换成相应的对象， 如[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)，[AREngine_ARPoint](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6)等，转换方式可参考： [AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *arPlane = reinterpret_cast<[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *>(trackable)。

**起始版本：** 5.0.0(12)

#### AREngine_ARTrackableList

```ets
typedef struct AREngine_ARTrackableList AREngine_ARTrackableList
```

**描述**

可跟踪对象列表。

**起始版本：** 5.0.0(12)

#### HMS_AREngine_PhotoAvailableCallback

```ets
typedef void (*HMS_AREngine_PhotoAvailableCallback)(OH_NativeBuffer *photoBuffer)
```

**描述**

输出拍照流图像回调。

**起始版本：**6.0.2(22)

**参数：**

名称

描述

photoBuffer

拍照流图像数据。

#### 枚举类型说明

#### AREngine_ARAddAugmentedImageReason

```ets
enum AREngine_ARAddAugmentedImageReason
```

**描述**

跟踪失败的可能原因。

**起始版本：** 5.1.0(18)

枚举值

描述

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_NONE

添加的图像符合质量要求。

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_SIZE_NOT_MATCH

尝试将质量不足（尺寸不匹配）的图像添加到图像数据库。

 说明：

图像尺寸评价从宽高比、分辨率两个维度进行。建议宽高比、分辨率的评价为Unfit以上。

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_LIGHT_ANOMALY

尝试将质量不足（太亮或太暗）的图像添加到图像数据库中。

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_FEATURE_LIMIT

尝试将质量不足（图像颜色比较单一）的图像添加到图像数据库中。

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_OTHER

尝试将质量不足（其他场景，如图片有反光、光斑，重复性内容等）添加到图像数据库中。

- 宽高比： 图像宽度与高度之比，如：640*480分辨率的图像，其宽高比为1.33，对应评价Excellent。

图像宽高比

评价

[6, ∞)

Invalid

[4, 6)

Bad

[2.5, 4)

Unfit

[2, 2.5)

Fit

[1.5, 2)

Good

[1, 1.5)

Excellent

- 分辨率：

以640*480为基准，按比例计算。如：选取图像分辨率为320*240，以基准分辨率计算其比值为0.5，对应评价Fit。

图像分辨率比值

评价

[0, 0.2]

Invalid

(0.2, 0.3]

Bad

(0.35, 0.45]

Unfit

(0.45, 0.7]

Fit

(0.7, 0.9]

Good

(0.9, ∞)

Excellent

#### AREngine_ARConfidenceLevel

```ets
enum AREngine_ARConfidenceLevel
```

**描述**

深度置信度。

**起始版本：** 5.0.5(17)

枚举值

描述

****ARENGINE_DEPTH_CONFIDENCE_LOW

该深度图像的置信度较低。

****ARENGINE_DEPTH_CONFIDENCE_MEDIUM

该深度图像的置信度中等。

ARENGINE_DEPTH_CONFIDENCE_HIGH

该深度图像的置信度很高。

#### AREngine_ARDepthMode

```ets
enum AREngine_ARDepthMode
```

**描述**

深度模式。

**起始版本：** 5.0.5(17)

枚举值

描述

****ARENGINE_DEPTH_MODE_DISABLED

不提供深度图像信息。

****ARENGINE_DEPTH_MODE_AUTOMATIC

AR Engine会自动尝试从多种深度源获取深度信息。

 说明：

通常有两种深度源，运动算法和硬件深度传感器 (Time of Flight，简称ToF)。

目前仅支持运动算法。

#### AREngine_ARFocusMode

```ets
enum AREngine_ARFocusMode
```

**描述**

对焦模式。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_FOCUS_MODE_FIXED

固定焦点对焦模式。

****ARENGINE_FOCUS_MODE_AUTO

自动对焦模式。

#### AREngine_ARImageDatabaseMode

```ets
enum AREngine_ARImageDatabaseMode
```

**描述**

用于跟踪的特征库图像添加方式。

**起始版本：** 5.1.0(18)

枚举值

描述

ARENGINE_ADD_NORMAL

正常添加模式。

ARENGINE_ADD_AUTO

循环删除模式。

#### AREngine_ARImageFormat

```ets
enum AREngine_ARImageFormat
```

**描述**

图像数据格式。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_IMAGE_UNKNOWN

无效的图片格式。

****ARENGINE_IMAGE_YUV_420_888

YUV_420_888格式，适用于处理高分辨率的图像数据。

ARENGINE_IMAGE_Y_8

Y_8格式，适用于对图像数据要求较低的精度或存储空间的场景。

**起始版本：** 5.0.5(17)

ARENGINE_IMAGE_Y_16

Y_16格式，适用于对图像数据精度要求较高的场景。

**起始版本：** 5.0.5(17)

#### AREngine_ARImageStreamMode

```ets
enum AREngine_ARImageStreamMode
```

**描述**

设置图片数据流模式，默认情况下系统设置为ARENGINE_IMAGE_STREAM_MODE_PREVIEW。

**起始版本：** 6.0.2(22)

枚举值

描述

****ARENGINE_IMAGE_STREAM_MODE_PREVIEW

预览流模式，可通过[HMS_AREngine_ARFrame_AcquireCameraImage](#ZH-CN_TOPIC_0000002500306234__gad5619c3cbd2b9ea0cfeff22b72f8d81d)接口获取预览流图像。

****ARENGINE_IMAGE_STREAM_MODE_PREVIEW_AND_PHOTO

拍照流加预览流模式，可通过[HMS_AREngine_ARFrame_AcquireCameraPhotoImage](#section18751333994)接口获取拍照流图像。

#### AREngine_ARMeshMode

```ets
enum AREngine_ARMeshMode
```

**描述**

Mesh启用模式。

**起始版本：** 5.1.0(18)

枚举值

描述

ARENGINE_MESH_MODE_DISABLED

网格模式关闭

AR Engine不会处理或显示网格数据。

ARENGINE_MESH_MODE_ENABLE

网格模式开启

AR Engine会尝试处理或显示网格数据。

#### AREngine_ARPlaneFindingMode

```ets
enum AREngine_ARPlaneFindingMode
```

**描述**

平面搜索模式。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_PLANE_FINDING_MODE_DISABLED

禁用平面检测。

****ARENGINE_PLANE_FINDING_MODE_HORIZONTAL

只检测水平面，如地板和桌子。

****ARENGINE_PLANE_FINDING_MODE_VERTICAL

只检测竖直平面，如墙壁。

****ARENGINE_PLANE_FINDING_MODE_HORIZONTAL_AND_VERTICAL

同时检测水平面和竖直平面。

#### AREngine_ARPlaneType

```ets
enum AREngine_ARPlaneType
```

**描述**

平面类型。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_PLANE_FACING_HORIZONTAL_UPWARD

朝上的水平面（例如地面和桌面平台）。

****ARENGINE_PLANE_FACING_HORIZONTAL_DOWNWARD

朝下的水平面（例如天花板）。

****ARENGINE_PLANE_FACING_VERTICAL

垂直的水平面（例如墙壁）。

****ARENGINE_PLANE_FACING_INVALID

无效或不支持的平面类型。这可能是由于环境变化、光线条件或其他因素导致。

#### AREngine_ARPointOrientationMode

```ets
enum AREngine_ARPointOrientationMode
```

**描述**

朝向模式。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_POINT_ORIENTATION_INITIALIZED_TO_IDENTITY

与世界坐标系的朝向一致，但会稍作调整。

****ARENGINE_POINT_ORIENTATION_ESTIMATED_SURFACE_NORMAL

朝向由估计的平面法向量决定。

#### AREngine_ARPoseMode

```ets
enum AREngine_ARPoseMode
```

**描述**

AR Engine输出的相机位姿对齐格式。

**起始版本：** 5.1.0(18)

枚举值

描述

ARENGINE_POSE_MODE_GRAVITY

输出的位姿信息（通过[HMS_AREngine_ARCamera_GetDisplayOrientedPose](#ZH-CN_TOPIC_0000002500306234__ga088648130f3a91cdf8d7b95f5ee1faf2)、[HMS_AREngine_ARCamera_GetPose](#ZH-CN_TOPIC_0000002500306234__ga00df108c4ba187967a10e9c4d2e27d3a)接口返回）为重力坐标系对齐的数据。参见[AR Engine重力对齐世界坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate#section51232054151614)。

ARENGINE_POSE_MODE_GRAVITY_HEADING

输出的位姿信息（通过[HMS_AREngine_ARCamera_GetDisplayOrientedPose](#ZH-CN_TOPIC_0000002500306234__ga088648130f3a91cdf8d7b95f5ee1faf2)、[HMS_AREngine_ARCamera_GetPose](#ZH-CN_TOPIC_0000002500306234__ga00df108c4ba187967a10e9c4d2e27d3a)接口返回）为北向ENU坐标系对齐的数据。参见[AR Engine重力对齐北向坐标系](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-coordinate#section1786771621711)。

#### AREngine_ARPoseType

```ets
enum AREngine_ARPoseType
```

**描述**

位姿类型。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_POSE_TYPE_IDENTITY

默认状态，即没有任何旋转或平移。

****ARENGINE_POSE_TYPE_ROTATE_90

顺时针旋转90度。

****ARENGINE_POSE_TYPE_ROTATE_180

顺时针旋转180度。

****ARENGINE_POSE_TYPE_ROTATE_270

顺时针旋转270度。

#### AREngine_ARPowerMode

```ets
enum AREngine_ARPowerMode
```

**描述**

电源功耗模式。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_POWER_MODE_NORMAL

正常模式，AR Engine在性能和电源消耗之间保持平衡。

****ARENGINE_POWER_MODE_POWER_SAVING

节能模式，AR Engine优先减少电源消耗。这可能会降低一些性能，以换取更长的电池寿命。

ARENGINE_POWER_MODE_PERFORMANCE_FIRST

性能优先模式，AR Engine优先考虑性能，提供更高的处理能力和更快的响应时间。这可能会增加电源消耗。

ARENGINE_POWER_MODE_BOOST

仅输出设备姿态信息模式。功耗低于 ARENGINE_POWER_MODE_NORMAL模式下的功耗。在此模式下，与平面相关的设置（如：[HMS_AREngine_ARConfig_SetPlaneFindingMode](#ZH-CN_TOPIC_0000002500306234__ga884a7db93778e24eef0dfaa794c45674)）不生效。

ARENGINE_POWER_MODE_ULTRA_POWER_SAVING

超级节能模式，AR Engine进一步优化电源消耗，提供比节能模式更低的电源消耗，这可能会损失更多的性能。

#### AREngine_ARPreviewMode

```ets
enum AREngine_ARPreviewMode
```

**描述**

预览模式。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_PREVIEW_MODE_ENABLED

开启相机预览。

****ARENGINE_PREVIEW_MODE_DISABLED

关闭相机预览，如：VR模式，不需要相机预览流。 在此模式下，通过[HMS_AREngine_ARSession_SetCameraGLTexture](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac697e4be36db63ed6098f154aa9ac01c)接口设置的OpenGL纹理 将不会被更新。

#### AREngine_ARSemanticDenseMode

```ets
enum AREngine_ARSemanticDenseMode
```

**描述**

高精几何重建识别模式。

**起始版本：** 6.0.0(20)

枚举值

描述

ARENGINE_SEMANTIC_DENSE_MODE_DISABLED

关闭高精几何重建识别模式。

ARENGINE_SEMANTIC_DENSE_MODE_NORMAL

正常模式，仅开启稠密点云识别。

ARENGINE_SEMANTIC_DENSE_MODE_CUBE_VOLUME

基于高精几何重建的立方体体积测量模式。

ARENGINE_SEMANTIC_DENSE_MODE_CUBE_SPACE

基于高精几何重建的立方体空间容积测量模式。

#### AREngine_ARSemanticMode

```ets
enum AREngine_ARSemanticMode
```

**描述**

语义模式。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_SEMANTIC_MODE_NONE

不使用语义。

****ARENGINE_SEMANTIC_MODE_PLANE

使用平面语义。

****ARENGINE_SEMANTIC_MODE_TARGET

使用物体语义。

#### AREngine_ARSemanticPlaneLabel

```ets
enum AREngine_ARSemanticPlaneLabel
```

**描述**

当前平面识别到的语义类型。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_PLANE_UNKNOWN

未知类型。

****ARENGINE_PLANE_WALL

墙面。

****ARENGINE_PLANE_FLOOR

地面。

****ARENGINE_PLANE_SEAT

座椅。

****ARENGINE_PLANE_TABLE

桌子。

****ARENGINE_PLANE_CEILING

天花板。

****ARENGINE_PLANE_DOOR

门。

****ARENGINE_PLANE_WINDOW

窗户。

****ARENGINE_PLANE_BED

床。

ARENGINE_PLANE_SPACE

平面空间。

**起始版本：** 6.0.0(20)

ARENGINE_CUBE_VOLUME

立方体体积。

**起始版本：** 6.0.0(20)

ARENGINE_CUBE_SPACE

立方体空间。

**起始版本：** 6.0.0(20)

#### AREngine_ARStatus

```ets
enum AREngine_ARStatus
```

**描述**

接口返回错误码。

用于表示一个接口的调用状态。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_PERMISSION_NOT_GRANTED

权限未授予状态。如相机权限未授予。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_DEVICE_NOT_SUPPORTED

不可用：设备不兼容状态。

****ARENGINE_ERROR_FATAL

失败状态。

****ARENGINE_ERROR_SESSION_PAUSED

会话已暂停状态。

****ARENGINE_ERROR_SESSION_NOT_PAUSED

会话未暂停状态。

****ARENGINE_ERROR_NOT_TRACKING

未跟踪状态。

****ARENGINE_ERROR_TEXTURE_NOT_SET

未设置纹理状态。

****ARENGINE_ERROR_MISSING_GL_CONTEXT

缺少GL上下文状态。

****ARENGINE_ERROR_UNSUPPORTED_CONFIGURATION

不支持的配置状态。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

****ARENGINE_ERROR_NOT_AVAILABLE

服务不可用状态。

****ARENGINE_ERROR_CAMERA_NOT_AVAILABLE

相机不可用状态。

ARENGINE_ERROR_IMAGE_EXCEED_NUM_LIMIT

添加的图片数量超过最大数量。

**起始版本：** 5.1.0(18)

ARENGINE_ERROR_IMAGE_INSUFFICIENT_QUALITY

将质量不足的图像添加到图像数据库中。

**起始版本：** 5.1.0(18)

ARENGINE_ERROR_IMAGE_INVALID_DATABASE

没有有效的图像数据库。

**起始版本：** 5.1.0(18)

ARENGINE_ERROR_IMAGE_ADD_IMAGE_TRACKING_STATE

跟踪状态正在运行时无法添加图片。

**起始版本：** 5.1.0(18)

ARENGINE_ERROR_NATIVEBUFFER_CREATE_FAILED

创建NativeBuffer失败。

**起始版本：** 6.0.0(20)

ARENGINE_ERROR_NATIVEBUFFER_WRITE_FAILED

无法写入NativeBuffer。

**起始版本：** 6.0.0(20)

#### AREngine_ARTargetShapeLabel

```ets
enum AREngine_ARTargetShapeLabel
```

**描述**

识别到的物体形状。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_TARGET_SHAPE_UNKNOWN

未知形状。

****ARENGINE_TARGET_SHAPE_CUBE

立方体形状。可以识别规则物体的包围框。

****ARENGINE_TARGET_SHAPE_CIRCLE

圆形形状。

****ARENGINE_TARGET_SHAPE_RECTANGLE

矩形形状。

#### AREngine_ARTrackableType

```ets
enum AREngine_ARTrackableType
```

**描述**

可跟踪对象类型，如平面、点等。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_TRACKABLE_BASE

基础可跟踪对象类型，可作为默认的[AREngine_ARTrackableType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d)类型。

****ARENGINE_TRACKABLE_PLANE

平面类可跟踪对象类型。

****ARENGINE_TRACKABLE_POINT

点类可跟踪对象类型。

ARENGINE_TRACKABLE_AUGMENTED_IMAGE

增强图像类型的可跟踪对象。

**起始版本：** 5.1.0(18)

****ARENGINE_TRACKABLE_TARGET

物体类可跟踪对象类型。

****ARENGINE_TRACKABLE_INVALID

无效的可跟踪对象类型。

#### AREngine_ARTrackingState

```ets
enum AREngine_ARTrackingState
```

**描述**

可跟踪对象的跟踪状态。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_TRACKING_STATE_TRACKING

正在追踪。

****ARENGINE_TRACKING_STATE_PAUSED

暂停追踪。

****ARENGINE_TRACKING_STATE_STOPPED

停止追踪。

#### AREngine_ARTrackingStateReason

```ets
enum AREngine_ARTrackingStateReason
```

**描述**

可能的跟踪失败原因。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_TRACKING_STATE_REASON_NONE

未知原因。这可能是由于系统暂时无法识别可追踪对象，但仍在尝试追踪。

****ARENGINE_TRACKING_STATE_REASON_EXCESSIVE_MOTION

目标移动过快。可追踪对象（如平面、点、图像等）移动速度过快，导致AR Engine无法准确识别和跟踪。

****ARENGINE_TRACKING_STATE_REASON_INSUFFICIENT_FEATURES

视觉特征不足（如弱纹理）。可追踪对象的视觉特征不够丰富，如纹理不明显、颜色过于单一等，导致AR Engine无法准确识别和跟踪。

#### AREngine_ARType

```ets
enum AREngine_ARType
```

**描述**

AR能力类型。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_TYPE_WORLD

环境跟踪能力。

ARENGINE_TYPE_IMAGE

图像特征跟踪能力。

**起始版本：** 5.1.0(18)

#### AREngine_ARUpdateMode

```ets
enum AREngine_ARUpdateMode
```

**描述**

调用[HMS_AREngine_ARSession_Update](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259)方法后数据更新模式。

**起始版本：** 5.0.0(12)

枚举值

描述

****ARENGINE_UPDATE_MODE_BLOCKING

[HMS_AREngine_ARSession_Update](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259)方法在新的帧可用时才返回。

****ARENGINE_UPDATE_MODE_LATEST

[HMS_AREngine_ARSession_Update](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259)方法立刻返回（如果没有新的帧，返回上一帧）。

#### 函数说明

#### HMS_AREngine_ARAnchor_Detach

```ets
AREngine_ARStatus HMS_AREngine_ARAnchor_Detach(AREngine_ARSession *session, AREngine_ARAnchor *anchor)
```

**描述**

通知AR Engine停止跟踪并解绑一个锚点。

但是该函数并不会释放该锚点，这需要通过[HMS_AREngine_ARAnchor_Release](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad04b12f9a2b0415789de5d6e1692f51c)单独来实现。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

anchor

待解绑的锚点对象，参见[AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARAnchor_GetPose

```ets
AREngine_ARStatus HMS_AREngine_ARAnchor_GetPose(const AREngine_ARSession *session, const AREngine_ARAnchor *anchor, AREngine_ARPose *outPose)
```

**描述**

获取指定锚点在世界坐标系中的位姿信息。

当每次调用[HMS_AREngine_ARSession_Update](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259)的时候，[HMS_AREngine_ARAnchor_GetPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad937acfc5d49f0909bdd84677bb0731a)返回的位姿信息可能会发生变化。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

anchor

待检索位姿的锚点，参见[AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)。

outPose

返回锚点对应的位姿对象，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARAnchor_GetTrackingState

```ets
AREngine_ARStatus HMS_AREngine_ARAnchor_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARAnchor *anchor, AREngine_ARTrackingState *outTrackingState)
```

**描述**

获取指定锚点位姿的追踪状态。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

anchor

待获取追踪状态的锚点，参见[AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)。

outTrackingState

返回锚点当前位姿的追踪状态，参见[AREngine_ARTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARAnchor_Release

```ets
void HMS_AREngine_ARAnchor_Release(AREngine_ARAnchor *anchor)
```

**描述**

释放指定锚点对象的内存。

释放前需要先通知AR Engine停止跟踪并解绑锚点，参见[HMS_AREngine_ARAnchor_Detach](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6b731c00cc038f62d21ccb280067114b)。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

anchor

待释放的锚点对象，参见[AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)。

#### HMS_AREngine_ARAnchorList_AcquireItem

```ets
AREngine_ARStatus HMS_AREngine_ARAnchorList_AcquireItem(const AREngine_ARSession *session, const AREngine_ARAnchorList *anchorList, int32_t index, AREngine_ARAnchor **outAnchor)
```

**描述**

从锚点对象列表中获取指定位置的锚点信息。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

anchorList

被检索的锚点对象列表，参见[AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872)。

index

需要获取的锚点在锚点对象列表中的位置，最小为0，最大为49。

outAnchor

待返回的锚点信息，参见[AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAnchorList_Create

```ets
AREngine_ARStatus HMS_AREngine_ARAnchorList_Create(const AREngine_ARSession *session, AREngine_ARAnchorList **outAnchorList)
```

**描述**

创建一个锚点对象列表。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outAnchorList

待创建的锚点对象列表引用，参见[AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARAnchorList_Destroy

```ets
void HMS_AREngine_ARAnchorList_Destroy(AREngine_ARAnchorList *anchorList)
```

**描述**

释放一个锚点对象列表。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

anchorList

待释放的锚点列表对象，参见[AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872)。

#### HMS_AREngine_ARAnchorList_GetSize

```ets
AREngine_ARStatus HMS_AREngine_ARAnchorList_GetSize(const AREngine_ARSession *session, const AREngine_ARAnchorList *anchorList, int32_t *outSize)
```

**描述**

获取锚点对象列表中包含锚点的数量。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

anchorList

锚点对象列表，参见[AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872)。

outSize

返回锚点对象列表中锚点的数量。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAugmentedImage_AcquireName

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImage_AcquireName(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, char *augmentedImageName, uint32_t *outNameLength)
```

**描述**

返回跟踪图像的名称。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

augmentedImage

图像类型的可追踪对象，参见[AREngine_ARAugmentedImage](#section68491824155217)。

augmentedImageName

图像名称，不能超过255字节。

outNameLength

返回图像名称长度。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAugmentedImage_GetCenterPose

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, AREngine_ARPose *outPose)
```

**描述**

获取跟踪图像中心点在世界坐标系中的位姿信息。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

augmentedImage

图像类型的可追踪对象，参见[AREngine_ARAugmentedImage](AR Engine.md#section68491824155217)。

outPose

返回跟踪图像的位姿，参见[AREngine_ARPose](#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAugmentedImage_GetExtendX

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetExtendX(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, float *outExtendX)
```

**描述**

以图像的中心点为坐标原点，获取X轴上的估计值。

返回物理图像的长度，单位为m。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

augmentedImage

图像类型的可追踪对象，参见[AREngine_ARAugmentedImage](AR Engine.md#section68491824155217)。

outExtendX

返回X轴上物理图像的估计长度，以m为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAugmentedImage_GetExtendZ

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetExtendZ(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, float *outExtendZ)
```

**描述**

以图像的中心点为坐标原点，获取Z轴上的估计值。

返回物理图像的宽度，单位为m。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

augmentedImage

图像类型的可追踪对象，参见[AREngine_ARAugmentedImage](AR Engine.md#section68491824155217)。

outExtendZ

返回Z轴上物理图像的估计宽度，以m为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAugmentedImage_GetIndex

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetIndex(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, uint32_t *outIndex)
```

**描述**

获取跟踪图像数据库中跟踪图像的索引。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

augmentedImage

图像类型的可追踪对象，参见[AREngine_ARAugmentedImage](AR Engine.md#section68491824155217)。

outIndex

返回图像的索引。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAugmentedImageDatabase_AddImage

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_AddImage(AREngine_ARAugmentedImageDatabase *database, const AREngine_ARAugmentedImageSource *image, uint32_t *outIndex, AREngine_ARAddAugmentedImageReason *outReason)
```

**描述**

将图像添加到图像数据库并输出对应图像的索引。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

database

跟踪图像数据库，参见[AREngine_ARAugmentedImageDatabase](#section152051642330)。

image

图像信息，参见[AREngine_ARAugmentedImageSource](../graphics/AREngine_ARAugmentedImageSource.md)。

outIndex

返回添加图像的索引。

outReason

返回添加图片失败的原因，参见[AREngine_ARAddAugmentedImageReason](#section2441053595)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

ARENGINE_ERROR_IMAGE_EXCEED_NUM_LIMIT

添加的图片数量超过最大数量。

**起始版本：** 5.1.0(18)

ARENGINE_ERROR_IMAGE_INSUFFICIENT_QUALITY

将质量不足的图像添加到图像数据库中。

**起始版本：** 5.1.0(18)

#### HMS_AREngine_ARAugmentedImageDatabase_Create

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Create(AREngine_ARAugmentedImageDatabase **outDatabase)
```

**描述**

创建一个空的跟踪图像数据库。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

outDatabase

返回指向要创建的图像库的指针，参见[AREngine_ARAugmentedImageDatabase](#section152051642330)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARAugmentedImageDatabase_Deserialize

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Deserialize(const uint8_t *buffer, const uint64_t bufSize, AREngine_ARAugmentedImageDatabase **outDatabase)
```

**描述**

反序列化特征数据库。

用户可以将上次生成的或者保存的buffer数据反序列化为特征数据库后直接使用。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

buffer

跟踪图像数据库缓冲区。

bufSize

跟踪图像数据库缓冲区大小，最大不超过int64类型长度。

outDatabase

返回跟踪图像数据库，参见[AREngine_ARAugmentedImageDatabase](#section152051642330)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARAugmentedImageDatabase_Destroy

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Destroy(AREngine_ARAugmentedImageDatabase *database)
```

**描述**

释放图像数据库对象。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

database

跟踪图像数据库，参见[AREngine_ARAugmentedImageDatabase](AR Engine.md#section152051642330)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAugmentedImageDatabase_GetAddMode

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetAddMode(const AREngine_ARAugmentedImageDatabase *database, AREngine_ARImageDatabaseMode *outAddMode)
```

**描述**

获取添加跟踪图像模式。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

database

跟踪图像数据库，参见[AREngine_ARAugmentedImageDatabase](AR Engine.md#section152051642330)。

outAddMode

返回添加跟踪图像模式。参见[AREngine_ARImageDatabaseMode](#section683253471219)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAugmentedImageDatabase_SetAddMode

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_SetAddMode(const AREngine_ARAugmentedImageDatabase *database, AREngine_ARImageDatabaseMode addMode)
```

**描述**

设置添加跟踪图像模式。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

database

跟踪图像数据库，参见[AREngine_ARAugmentedImageDatabase](AR Engine.md#section152051642330)。

addMode

添加跟踪图像模式。参见[AREngine_ARImageDatabaseMode](#section683253471219)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAugmentedImageDatabase_GetCapacity

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetCapacity(const AREngine_ARAugmentedImageDatabase *database, uint32_t *outCapacity)
```

**描述**

获取可以添加的最大图像数。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

database

跟踪图像数据库，参见[AREngine_ARAugmentedImageDatabase](AR Engine.md#section152051642330)。

outCapacity

返回最大图像数，默认为50。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARAugmentedImageDatabase_GetImageCount

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetImageCount(const AREngine_ARAugmentedImageDatabase *database, uint32_t *outImageCount)
```

**描述**

获取数据库中存储的图像数量。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

database

跟踪图像数据库，参见[AREngine_ARAugmentedImageDatabase](AR Engine.md#section152051642330)。

outImageCount

返回图像数量。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARAugmentedImageDatabase_Serialize

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Serialize(const AREngine_ARAugmentedImageDatabase *database, uint8_t **outBuffer, uint64_t *outBufSize)
```

**描述**

序列化特征数据库。

在添加完图片后，可以将特征库序列化为buffer，开发者可以保存此buffer以供下次使用。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

database

跟踪图像数据库，参见[AREngine_ARAugmentedImageDatabase](AR Engine.md#section152051642330)。

outBuffer

返回跟踪图像数据库缓冲区。

outBufSize

返回跟踪图像数据库缓冲区大小。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARCamera_GetDisplayOrientedPose

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetDisplayOrientedPose(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARPose *outPose)
```

**描述**

设置outPose为虚拟相机（面向显示）在世界空间中的位姿，用以将AR内容渲染到最新帧中。

该位姿是OpenGL相机的位姿，其中X轴正方向为右，Y轴正方向为上，Z轴负方向为相机的观察方向。相机位置即物理相机位置，而相机X轴与Y轴指向受屏幕方向（考虑显示旋转）的影响。

该位姿信息应该在[HMS_AREngine_ARCamera_GetTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dc931eee56ae5ea899f8acc08eb3f36)返回[ARENGINE_TRACKING_STATE_TRACKING](#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)状态的时候才能使用。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

camera

Session对应的相机，参见[AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)。

outPose

返回虚拟相机在世界空间中的位姿，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARCamera_GetImageIntrinsics

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetImageIntrinsics(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARCameraIntrinsics *outIntrinsics)
```

**描述**

获取物理相机离线内参的对象，可通过该对象获取相机的焦距、图像尺寸、主轴点和畸变参数。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

camera

Session对应的相机，参见[AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)。

outIntrinsics

返回相机物理内参对象，参见[AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARCamera_GetPose

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetPose(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARPose *outPose)
```

**描述**

设置outPose为最新帧中物理相机在世界空间中的位姿。该位姿是OpenGL相机的位姿。

其中X轴正方向为右，Y轴正方向为上，Z轴负方向为相机的观察方向。相机位置即物理相机位置，而相机X轴与Y轴指向不受屏幕方向（考虑显示旋转）的影响。

该位姿信息应该在[HMS_AREngine_ARCamera_GetTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dc931eee56ae5ea899f8acc08eb3f36)返回[ARENGINE_TRACKING_STATE_TRACKING](#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)状态的时候才能使用。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

camera

Session对应的相机，参见[AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)。

outPose

物理相机在世界空间中的位姿，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARCamera_GetProjectionMatrix

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetProjectionMatrix(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ClipPlaneDistance clipPlaneDistance, float *outDestColMajor4x4, int32_t destColMajor4x4Num)
```

**描述**

获取用于在相机图像上层渲染虚拟内容的投影矩阵，可用于相机坐标系到裁剪坐标系转换。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

camera

Session对应的相机，参见[AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)。

clipPlaneDistance

OpenGL裁剪平面距离，参见[AREngine_ClipPlaneDistance](AREngine_ClipPlaneDistance.md)。

outDestColMajor4x4

返回一个由16个浮点数组成的数组，其中的数据表示OpenGL中以列为主的均匀变换矩阵。

destColMajor4x4Num

数组大小：[ARENGINE_VIEW_MATRIX_SIZE](#section02261581599)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARCamera_GetTrackingState

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARTrackingState *outTrackingState)
```

**描述**

获取相机的当前追踪状态。

只有当该状态为[ARENGINE_TRACKING_STATE_TRACKING](#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)时，相机的位姿才可用。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

camera

Session对应的相机，参见[AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)。

outTrackingState

返回当前相机的追踪状态，参见[AREngine_ARTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARCamera_GetTrackingStateReason

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetTrackingStateReason(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARTrackingStateReason *outTrackingStateReason)
```

**描述**

获取相机的当前追踪状态为[ARENGINE_TRACKING_STATE_PAUSED](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)时的原因。

当相机的当前追踪状态为[ARENGINE_TRACKING_STATE_TRACKING](#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)时，该函数返回[ARENGINE_TRACKING_STATE_REASON_NONE](#ZH-CN_TOPIC_0000002500306234__ga67774b71935ef2f8a2ae5e5822c3dcdb)。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

camera

Session对应的相机，参见[AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)。

outTrackingStateReason

返回跟踪失败的原因，参见[AREngine_ARTrackingStateReason](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga67774b71935ef2f8a2ae5e5822c3dcdb)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARCamera_GetViewMatrix

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetViewMatrix(const AREngine_ARSession *session, const AREngine_ARCamera *camera, float *outColMajor4x4, int32_t colMajor4x4Num)
```

**描述**

获取最新帧中相机的视图矩阵。

此矩阵执行了[HMS_AREngine_ARCamera_GetDisplayOrientedPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga088648130f3a91cdf8d7b95f5ee1faf2)提供的Pose的逆变换，即从世界坐标系转为相机坐标系。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

camera

Session对应的相机，参见[AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)。

outColMajor4x4

返回一个由16个浮点数组成的数组，其中的数据表示OpenGL中以列为主的均匀变换矩阵。

colMajor4x4Num

数组大小。数组大小定义大于等于[ARENGINE_VIEW_MATRIX_SIZE](#section02261581599)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARCamera_Release

```ets
void HMS_AREngine_ARCamera_Release(AREngine_ARCamera *camera)
```

**描述**

释放对相机的引用。

当调用了[HMS_AREngine_ARFrame_AcquireCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga5295c975a0ff3d633a1dde5a8eb70863)时，需要相应的调用[HMS_AREngine_ARCamera_Release](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga16909b4002b9c6250dad88bb8397adc9)。

当没有[HMS_AREngine_ARFrame_AcquireCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga5295c975a0ff3d633a1dde5a8eb70863)时，调用该方法无效。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

camera

待释放的相机引用，参见[AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)。

#### HMS_AREngine_ARCameraConfig_Create

```ets
AREngine_ARStatus HMS_AREngine_ARCameraConfig_Create(const AREngine_ARSession *session, AREngine_ARCameraConfig **outCameraConfig)
```

**描述**

创建一个相机配置对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outCameraConfig

返回一个指向新分配的相机配置对象地址的指针，参见[AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARCameraConfig_Destroy

```ets
void HMS_AREngine_ARCameraConfig_Destroy(AREngine_ARCameraConfig *cameraConfig)
```

**描述**

释放相机配置对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

cameraConfig

待释放的指向相机配置对象的指针，参见[AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba)。

#### HMS_AREngine_ARCameraConfig_GetImageDimensions

```ets
AREngine_ARStatus HMS_AREngine_ARCameraConfig_GetImageDimensions(const AREngine_ARSession *session, const AREngine_ARCameraConfig *cameraConfig, int32_t *outWidth, int32_t *outHeight)
```

**描述**

从相机配置对象中获取相机送到CPU处理的图像尺寸。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

cameraConfig

指向相机配置对象的指针，参见[AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba)。

outWidth

返回图像的宽度，以像素为单位。

outHeight

返回图像的高度，以像素为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARCameraConfig_GetTextureDimensions

```ets
AREngine_ARStatus HMS_AREngine_ARCameraConfig_GetTextureDimensions(const AREngine_ARSession *session, const AREngine_ARCameraConfig *cameraConfig, int32_t *outWidth, int32_t *outHeight)
```

**描述**

从相机配置对象中获取相机送到GPU处理的图像纹理尺寸。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

cameraConfig

指向相机配置对象的指针，参见[AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba)。

outWidth

返回图像纹理的宽度，以像素为单位。

outHeight

返回图像纹理的高度，以像素为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARCameraIntrinsics_Create

```ets
AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_Create(const AREngine_ARSession *session, AREngine_ARCameraIntrinsics **outIntrinsics)
```

**描述**

创建一个相机内参对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outIntrinsics

返回一个指向新分配的相机内参对象地址的指针，参见[AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARCameraIntrinsics_Destroy

```ets
void HMS_AREngine_ARCameraIntrinsics_Destroy(AREngine_ARCameraIntrinsics *intrinsics)
```

**描述**

释放指定的相机内参对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

intrinsics

待释放的相机内参对象，参见[AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)。

#### HMS_AREngine_ARCameraIntrinsics_GetDistortion

```ets
AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetDistortion(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outDistortion, int32_t distortionNum)
```

**描述**

获取相机的畸变系数。

包含5个分量，其中outDistortion[0]~outDistortion [2]表示k1，k2，k3（径向畸变系数），outDistortion [3]~outDistortion [4]是切向畸变系数。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

intrinsics

指向相机内参对象的指针，参见[AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)。

outDistortion

返回相机畸变参数数组。

distortionNum

相机畸变参数的个数，参见[ARENGINE_DISTORTION_COUNT](#section2059093619593)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARCameraIntrinsics_GetFocalLength

```ets
AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetFocalLength(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outFocalX, float *outFocalY)
```

**描述**

获取指定相机的焦距，焦距以像素为单位。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

intrinsics

指向相机内参对象的指针，参见[AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)。

outFocalX

返回相机内参矩阵x(u)方向的像素焦距。

outFocalY

返回相机内参矩阵y(v)方向的像素焦距。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARCameraIntrinsics_GetImageDimensions

```ets
AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetImageDimensions(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, int32_t *outWidth, int32_t *outHeight)
```

**描述**

获取相机图像的尺寸，包括宽度和高度，以像素为单位。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

intrinsics

指向相机内参对象的指针，参见[AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)。

outWidth

返回相机图像的宽度，以像素为单位。

outHeight

返回相机图像的高度，以像素为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARCameraIntrinsics_GetPrincipalPoint

```ets
AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetPrincipalPoint(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outPrincipalX, float *outPrincipalY)
```

**描述**

获取指定相机的主轴点，主点位置以像素为单位表示。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

intrinsics

指向相机内参对象的指针，参见[AREngine_ARCameraIntrinsics](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)。

outPrincipalX

返回相机X方向的主轴点坐标。

outPrincipalY

返回相机Y方向的主轴点坐标。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_Create

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_Create(const AREngine_ARSession *session, AREngine_ARConfig **outConfig)
```

**描述**

创建具有适当默认配置的配置对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outConfig

返回一个指向新分配的配置对象地址的指针，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARConfig_Destroy

```ets
void HMS_AREngine_ARConfig_Destroy(AREngine_ARConfig *config)
```

**描述**

释放指定的配置对象的内存空间。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

config

待释放的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

#### HMS_AREngine_ARConfig_GetARType

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetARType(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARType *type)
```

**描述**

获取当前使用的AR能力类型。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

type

返回AR Engine当前使用的能力类型，参见[AREngine_ARType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga987888aea7dcaa9abcdb64581c850bf5)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetCameraPreviewMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetCameraPreviewMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPreviewMode *outMode)
```

**描述**

获取当前的预览模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

outMode

返回相机预览模式，参见[AREngine_ARPreviewMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadef0f2099b106b872a014ef6551906ae)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetDepthMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetDepthMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARDepthMode *outDepthMode)
```

**描述**

获取当前的深度模式。

**起始版本：** 5.0.5(17)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

outDepthMode

返回当前深度模式，参见[AREngine_ARDepthMode](#section12321429115215)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetFocusMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetFocusMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARFocusMode *focusMode)
```

**描述**

获取当前配置的相机对焦模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

focusMode

返回当前对焦模式，参见[AREngine_ARFocusMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf50530faa0d094182a0db0c73b75d875)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetMaxMapSize

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetMaxMapSize(const AREngine_ARSession *session, const AREngine_ARConfig *config, uint64_t *maxMapSize)
```

**描述**

获取地图数据使用的最大内存大小。

在执行[HMS_AREngine_ARSession_Configure](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6394ae995148abbe3d00082817bf320a)后，可通过此接口获取当前设置的地图数据最大使用内存大小。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

maxMapSize

返回目前生效的地图数据最大使用内存大小，单位MB。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetMeshMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetMeshMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMeshMode *outMeshMode)
```

**描述**

获取当前mesh模式。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

outMeshMode

返回mesh模式，参见[AREngine_ARMeshMode](#section19436658201620)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetPlaneFindingMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetPlaneFindingMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPlaneFindingMode *planeFindingMode)
```

**描述**

获取当前配置的平面识别模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

planeFindingMode

返回当前平面识别模式，参见[AREngine_ARPlaneFindingMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab8e7db52d819359026fc4a82815d3fff)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetPoseMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetPoseMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPoseMode *poseMode)
```

**描述**

获取相机输出的位姿坐标系对齐模式。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

poseMode

相机位姿模式，参见[AREngine_ARPoseMode](#section1249515330198)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetPowerMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetPowerMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPowerMode *powerMode)
```

**描述**

获取当前配置的功耗模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

powerMode

返回当前功耗模式，参见[AREngine_ARPowerMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3d925e007e2847e69f22af68ec922507)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetSemanticDenseMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetSemanticDenseMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARSemanticDenseMode *outSemanticDenseMode)
```

**描述**

获取已设置的高精几何重建模式。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

outSemanticDenseMode

返回当前高精几何重建模式，参见[AREngine_ARSemanticDenseMode](#section09971756142213)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetSemanticMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetSemanticMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARSemanticMode *mode)
```

**描述**

获取已设置成功的语义识别模式。

该方法在[HMS_AREngine_ARConfig_SetSemanticMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae87c1ef02b6e9bab123fae2086da248)后调用有效。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

mode

返回当前语义模式，参见[AREngine_ARSemanticMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga34d3000de29454b99d89406d288d6ed5)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetUpdateMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetUpdateMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARUpdateMode *updateMode)
```

**描述**

获取当前配置的预览更新模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

updateMode

返回当前预览更新模式，参见[AREngine_ARUpdateMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabd21cc975ee97b7fb2133af0068ebb5e)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetARType

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetARType(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARType type)
```

**描述**

设置当前要使用的AR能力类型。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

type

AR Engine支持的能力类型，参见[AREngine_ARType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga987888aea7dcaa9abcdb64581c850bf5)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_UNSUPPORTED_CONFIGURATION

不支持的配置状态。

#### HMS_AREngine_ARConfig_SetCameraPreviewMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetCameraPreviewMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPreviewMode mode)
```

**描述**

设置预览模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

mode

相机预览模式，参见[AREngine_ARPreviewMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadef0f2099b106b872a014ef6551906ae)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetDepthMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetDepthMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARDepthMode depthMode)
```

**描述**

设置深度模式。

**起始版本：** 5.0.5(17)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

depthMode

深度图像模式，参见[AREngine_ARDepthMode](#section12321429115215)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetFocusMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetFocusMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARFocusMode focusMode)
```

**描述**

设置当前所需的相机对焦模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

focusMode

对焦模式，参见[AREngine_ARFocusMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf50530faa0d094182a0db0c73b75d875)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetMaxMapSize

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetMaxMapSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint64_t maxMapSize)
```

**描述**

设置地图数据最大使用内存大小。

若配置的地图数据最大使用内存范围不合法，则配置最接近用户配置的有效值，默认最大使用内存大小800MB。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

maxMapSize

地图数据最大使用内存大小，单位MB，范围：100MB~16G。 若设备内存占用超过设备硬件限制，可能出现不可预知错误，需要应用侧自行评估设置的内存大小。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetMeshMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetMeshMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARMeshMode meshMode)
```

**描述**

设置mesh模式。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

meshMode

mesh模式，参见[AREngine_ARMeshMode](#section19436658201620)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetPlaneFindingMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetPlaneFindingMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPlaneFindingMode planeFindingMode)
```

**描述**

设置当前所需的平面识别模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

planeFindingMode

平面识别模式，参见[AREngine_ARPlaneFindingMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab8e7db52d819359026fc4a82815d3fff)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetPoseMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetPoseMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPoseMode poseMode)
```

**描述**

设置相机输出的位姿坐标系对齐模式。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

poseMode

相机位姿模式，参见[AREngine_ARPoseMode](#section1249515330198)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetPowerMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetPowerMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPowerMode powerMode)
```

**描述**

设置功耗模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

powerMode

功耗模式，参见[AREngine_ARPowerMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3d925e007e2847e69f22af68ec922507)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetPreviewSize

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetPreviewSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint32_t width, uint32_t height)
```

**描述**

设置预览画面尺寸，仅支持宽高比为4:3，超出范围的值将自动采用默认分辨1440*1080填充。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

width

预览画面的宽，以像素为单位。可调用[OH_CameraManager_GetSupportedCameraOutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapability)查看所用设备支持的数值。

height

预览画面的高，以像素为单位。可调用[OH_CameraManager_GetSupportedCameraOutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapability)查看所用设备支持的数值。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetSemanticDenseMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetSemanticDenseMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARSemanticDenseMode semanticDenseMode)
```

**描述**

设置当前所需的高精几何重建模式。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

semanticDenseMode

高精几何重建模式，参见[AREngine_ARSemanticDenseMode](#section09971756142213)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetSemanticMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetSemanticMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARSemanticMode mode)
```

**描述**

设置当前所需的语义识别模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

mode

语义模式，参见[AREngine_ARSemanticMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga34d3000de29454b99d89406d288d6ed5)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetUpdateMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetUpdateMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARUpdateMode updateMode)
```

**描述**

设置预览更新模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

updateMode

预览更新模式，参见[AREngine_ARUpdateMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabd21cc975ee97b7fb2133af0068ebb5e)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetPhotoStreamSize

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetPhotoStreamSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint32_t width, uint32_t height)
```

**描述**

PreviewAndPhotoMode模式下，设置从拍照流获取图像的分辨率。仅支持4:3大小分辨率。如果超出这个范围，系统会自动设置图像分辨率为该设备在4:3宽高比下的最高分辨率。

**起始版本：** 6.0.2(22)

**参数：**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

width

拍照流图像分辨率的宽，以像素为单位。可调用[OH_CameraManager_GetSupportedCameraOutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapability)查询设备支持的数值。

height

拍照流图像分辨率的高，以像素为单位。可调用[OH_CameraManager_GetSupportedCameraOutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapability)查询设备支持的数值。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_SetImageStreamMode

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraPhotoImage(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARImageStreamMode mode)
```

**描述**

设置图像流模式。

**起始版本：** 6.0.2(22)

**参数：**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

width

拍照流图像分辨率的宽，以像素为单位。可调用[OH_CameraManager_GetSupportedCameraOutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapability)查询设备支持的数值。

height

拍照流图像分辨率的高，以像素为单位。可调用[OH_CameraManager_GetSupportedCameraOutputCapability](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-manager-h#oh_cameramanager_getsupportedcameraoutputcapability)查询设备支持的数值。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARConfig_GetImageStreamMode

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetImageStreamMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARImageStreamMode *outMode)
```

**描述**

获取图像流模式。

**起始版本：** 6.0.2(22)

**参数：**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

指向待获取配置信息的配置对象，参见[AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

outMode

图像流模式，参见[AREngine_ARImageStreamMode](#section184201559356)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARFrame_AcquireCamera

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCamera(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARCamera **outCamera)
```

**描述**

获取当前帧的相机参数对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

outCamera

返回当前帧对应的相机参数对象，参见[AREngine_ARCamera](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARFrame_AcquireCameraImage

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraImage(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outImage)
```

**描述**

获取相机的当前帧的图像。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

outImage

返回返回当前帧的图像对象，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_UNSUPPORTED_CONFIGURATION

不支持的配置状态。

#### HMS_AREngine_ARFrame_AcquireCameraPhotoImage

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraPhotoImage(const AREngine_ARSession *session, const AREngine_ARFrame *frame, HMS_AREngine_PhotoAvailableCallback photoCallback)
```

**描述**

获取当前帧的拍照流图片。

**起始版本：** 6.0.2(22)

**参数：**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

photoCallback

输出拍照流图片的回调。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

ARENGINE_ERROR_UNSUPPORTED_CONFIGURATION

不支持的配置状态。

ARENGINE_ERROR_FATAL

失败状态。

ARENGINE_ERROR_CAMERA_NOT_AVAILABLE

相机不可用状态。

#### HMS_AREngine_ARFrame_AcquireDepthConfidenceImage

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireDepthConfidenceImage(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outConfidenceImage)
```

**描述**

获取当前帧的深度置信度图像。

**起始版本：** 5.0.5(17)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

outConfidenceImage

返回返回当前帧深度置信度图像对象，参见[AREngine_ARImage](#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARFrame_AcquireDepthImage16Bits

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireDepthImage16Bits(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outDepthImage)
```

**描述**

获取当前帧的深度图像。

**起始版本：** 5.0.5(17)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

outDepthImage

返回当前帧深度图像对象，参见[AREngine_ARImage](#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARFrame_AcquirePointCloud

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquirePointCloud(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARPointCloud **outPointCloud)
```

**描述**

返回当前帧的点云数据。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

outPointCloud

返回当前帧的点云对象，参见[AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARFrame_AcquireSceneMesh

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireSceneMesh(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARSceneMesh **outSceneMesh)
```

**描述**

获取当前帧的mesh信息。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

outSceneMesh

返回当前帧的mesh信息，参见[AREngine_ARSceneMesh](#section543212520614)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARFrame_AcquireSemanticDenseData

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireSemanticDenseData(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARSemanticDenseData **outSemanticDenseData)
```

**描述**

获取当前帧的高精几何重建对象数据。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

outSemanticDenseData

返回当前帧的高精几何重建对象数据，参见[AREngine_ARSemanticDenseData](#section1410813229144)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARFrame_Create

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_Create(const AREngine_ARSession *session, AREngine_ARFrame **outFrame)
```

**描述**

创建一个新的[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)对象，将指针存储到*outFrame中。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outFrame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARFrame_Destroy

```ets
void HMS_AREngine_ARFrame_Destroy(AREngine_ARFrame *frame)
```

**描述**

删除当前[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

frame

待销毁的当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

#### HMS_AREngine_ARFrame_GetDisplayGeometryChanged

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_GetDisplayGeometryChanged(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int32_t *outGeometryChangeState)
```

**描述**

获取显示（长宽和旋转）是否发生变化。

如果发生变化，需要重新调用[HMS_AREngine_ARFrame_TransformDisplayUvCoords](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4c7699abab9b82369c0d42b496667fc7)获取正确的纹理贴图坐标。 返回值outGeometryChangeState为0，代表未发生变化，否则为发生了变化。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

outGeometryChangeState

返回显示（长宽和旋转）是否发生变化。0代表未发生变化，否则为发生了变化。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARFrame_GetTimestamp

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int64_t *outTimestampNs)
```

**描述**

获取当前帧对应的时间戳信息，单位为ns。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

outTimestampNs

返回时间戳信息。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARFrame_GetUpdatedTrackables

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_GetUpdatedTrackables(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARTrackableType filterType, AREngine_ARTrackableList * outTrackableList)
```

**描述**

获取[HMS_AREngine_ARSession_Update](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259)更新后发生变化的指定类型的可跟踪对象。

可跟踪对象类型参见[AREngine_ARTrackableType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d)。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

filterType

待返回的可跟踪对象类型，参见[AREngine_ARTrackableType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d)。

outTrackableList

返回可跟踪对象列表，参见[AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARFrame_HitTest

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_HitTest(const AREngine_ARSession *session, const AREngine_ARFrame *frame, float pixelX, float pixelY, AREngine_ARHitResultList *hitResultList)
```

**描述**

从摄像头发射一条射线，该射线的方向由预览区上的点(pixelX，pixelY)确定(pixelX，pixelY可以通过XComponent的[DispatchTouchEvent()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback#dispatchtouchevent)事件获取)。

射线与系统跟踪的平面、Mesh或者是点云中的点碰撞（点云正常识别），从而产生交点，形成碰撞结果。按照交点与设备的距离从近到远进行排序，存放在列表中。(pixelX，pixelY)是像素在预览区上坐标。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

pixelX

x轴坐标，通过[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)获取。

pixelY

y轴坐标，通过[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)获取。

hitResultList

碰撞结果列表，参见[AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARFrame_TransformDisplayUvCoords

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_TransformDisplayUvCoords(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int32_t elementSize, const float *uvsIn, float *uvsOut)
```

**描述**

调整纹理映射坐标，以便可以正确地显示相机捕捉到的背景图片。

若[HMS_AREngine_ARFrame_GetDisplayGeometryChanged](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4fb55932c19ef9c49523a0a5385a9242)返回的outGeometryChangeState不为0，或者使用[HMS_AREngine_ARSession_SetDisplayGeometry](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3f23bf747def8303c3fb261a9e9a2286)设置了新的显示大小则需要调用该方法更新纹理映射坐标，否则不需要更新。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

frame

当前帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

elementSize

待转换的纹理坐标数量，必须是2的倍数（uv坐标），最小为0。

uvsIn

原始输入uv坐标值。数组大小为 elementSize，不能为nullptr。

uvsOut

调整后的uv坐标值。数组大小为 elementSize，不能为nullptr。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARHitResult_AcquireNewAnchor

```ets
AREngine_ARStatus HMS_AREngine_ARHitResult_AcquireNewAnchor(AREngine_ARSession *session, AREngine_ARHitResult *hitResult, AREngine_ARAnchor **outAnchor)
```

**描述**

在碰撞命中位置创建一个新的锚点。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

hitResult

命中检测结果对象，参见[AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)。

outAnchor

返回新创建的锚点对象，参见[AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARHitResult_AcquireTrackable

```ets
AREngine_ARStatus HMS_AREngine_ARHitResult_AcquireTrackable(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, AREngine_ARTrackable **outTrackable)
```

**描述**

获取被命中的可追踪对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

hitResult

命中检测结果对象，参见[AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)。

outTrackable

返回被命中的可追踪对象，参见[AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARHitResult_Create

```ets
AREngine_ARStatus HMS_AREngine_ARHitResult_Create(const AREngine_ARSession *session, AREngine_ARHitResult **outHitResult)
```

**描述**

创建一个空的命中检测结果对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outHitResult

待创建的命中检测结果对象，参见[AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARHitResult_Destroy

```ets
void HMS_AREngine_ARHitResult_Destroy(AREngine_ARHitResult *hitResult)
```

**描述**

释放命中检测结果对象列表，以及其中的所有命中检测结果对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

hitResult

待释放的命中检测结果对象，参见[AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)。

#### HMS_AREngine_ARHitResult_GetDistance

```ets
AREngine_ARStatus HMS_AREngine_ARHitResult_GetDistance(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, float *outDistance)
```

**描述**

返回从相机到命中位置的距离，以m为单位。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

hitResult

命中检测结果对象，参见[AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)。

outDistance

返回相机到命中对象的距离。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARHitResult_GetHitPose

```ets
AREngine_ARStatus HMS_AREngine_ARHitResult_GetHitPose(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, AREngine_ARPose *outPose)
```

**描述**

获取交点的位姿。

其平移向量是交点在世界坐标系的坐标，其旋转分量根据碰撞点的不同类型（平面交点、点云交点）而有不同的定义。

1. 当射线与平面碰撞时，局部坐标系为：X+垂直于射线，平行于跟踪平面；Y+是跟踪平面的法向量；Z+平行于平面，大致指向摄像头。
1. 当射线与点云中的点碰撞时，系统会尝试用点击区域的点云估计一个平面。

  1. 如果[HMS_AREngine_ARPoint_GetOrientationMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad869ed2a4ac6409bf94c768d9d1d8127)接口返回[ARENGINE_POINT_ORIENTATION_ESTIMATED_SURFACE_NORMAL](#ZH-CN_TOPIC_0000002500306234__ga0e2893593f4372954fd97519e0a63855)，则X+垂直于射线，平行于跟踪平面，Y+是跟踪平面的法向量，Z+平行于平面，大致指向摄像头。
  1. 如果返回 [ARENGINE_POINT_ORIENTATION_INITIALIZED_TO_IDENTITY](#ZH-CN_TOPIC_0000002500306234__ga0e2893593f4372954fd97519e0a63855)，则坐标的方向不会随平面的角度发生变化，X+垂直于射线且指向右侧（从设备的角度观察），Y+向上，Z+大致指向摄像头，具体参见朝向模式定义。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

hitResult

命中检测结果对象，参见[AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)。

outPose

返回交点的位姿，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARHitResultList_Create

```ets
AREngine_ARStatus HMS_AREngine_ARHitResultList_Create(const AREngine_ARSession *session, AREngine_ARHitResultList **outHitResultList)
```

**描述**

创建一个命中检测结果对象列表。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outHitResultList

待创建的命中检测结果对象列表，参见[AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARHitResultList_Destroy

```ets
void HMS_AREngine_ARHitResultList_Destroy(AREngine_ARHitResultList *hitResultList)
```

**描述**

释放命中检测结果对象列表，以及其中的所有命中检测结果对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

hitResultList

待释放的命中检测结果对象列表，参见[AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3)。

#### HMS_AREngine_ARHitResultList_GetItem

```ets
AREngine_ARStatus HMS_AREngine_ARHitResultList_GetItem(const AREngine_ARSession *session, const AREngine_ARHitResultList *hitResultList, int32_t index, AREngine_ARHitResult *outHitResult)
```

**描述**

在命中检测结果列表中获取指定索引的命中检测结果对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

hitResultList

命中检测结果对象列表，参见[AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3)。

index

待获取的命中检测结果对象索引。

outHitResult

待获取的命中检测结果对象，参见[AREngine_ARHitResult](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARHitResultList_GetSize

```ets
AREngine_ARStatus HMS_AREngine_ARHitResultList_GetSize(const AREngine_ARSession *session, const AREngine_ARHitResultList *hitResultList, int32_t *outSize)
```

**描述**

获取命中检测结果对象列表中包含的对象数。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

hitResultList

命中检测结果对象列表，参见[AREngine_ARHitResultList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3)。

outSize

返回列表大小。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARImage_GetFormat

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetFormat(const AREngine_ARSession *session, const AREngine_ARImage *image, AREngine_ARImageFormat *outFormat)
```

**描述**

获取当前帧的图像格式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

image

输入图像数据，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

outFormat

返回当前帧的图像格式。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARImage_GetHeight

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetHeight(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outHeight)
```

**描述**

获取当前帧的图像数据的高度。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

image

当前帧图像对象，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

outHeight

返回当前帧的图像的高度，以像素为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARImage_GetNativeBuffer

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetNativeBuffer(const AREngine_ARSession *session, const AREngine_ARImage *image, OH_NativeBuffer **outNativeBuffer)
```

**描述**

获取当前帧图像对象的NativeBuffer数据。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

image

当前帧图像对象，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

outNativeBuffer

返回当前帧图像的NativeBuffer数据。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

ARENGINE_ERROR_NATIVEBUFFER_CREATE_FAILED

创建NativeBuffer失败。

ARENGINE_ERROR_NATIVEBUFFER_WRITE_FAILED

无法写入NativeBuffer。

#### HMS_AREngine_ARImage_GetPlaneCount

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneCount(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outCount)
```

**描述**

获取当前帧图像的平面数量。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

image

当前帧图像对象，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

outCount

返回当前帧图像的平面数量。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARImage_GetPlaneData

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneData(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, const uint8_t **outData, int32_t *outLength)
```

**描述**

获取当前帧图像的平面数据。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

image

当前帧图像对象，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

planeIndex

平面的索引。介于0和n-1，其中n是该图像的平面数。

outData

返回当前图像数据指针。

outLength

返回当前图像的长度，以Byte为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARImage_GetPlanePixelStride

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetPlanePixelStride(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, int32_t *outPixelStride)
```

**描述**

获取图像中两个连续像素的起点之间的字节距离。像素步幅始终大于0。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

image

当前帧图像对象，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

planeIndex

平面的索引。介于0和n-1，其中n是该图像的平面数。

outPixelStride

返回图像的步幅，以Byte为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARImage_GetPlaneRowStride

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneRowStride(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, int32_t *outRowStride)
```

**描述**

获取图像中两个连续像素行的起始位置之间的字节数。行间距始终大于0。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

image

当前帧图像对象，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

planeIndex

平面的索引。介于0和n-1，其中n是该图像的平面数。

outRowStride

返回图像的行跨距，以Byte为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARImage_GetTimestamp

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARImage *image, int64_t *outTimestamp)
```

**描述**

获取图像的时间戳。

时间戳通常是单调递增的，以ns为单位。时间戳的具体含义和时基取决于提供图像的源。 来自不同来源的图像的时间戳可能具有不同的时基，因此不应该相互比较。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

image

当前帧图像对象，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

outTimestamp

返回图像的时间戳，以ns为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARImage_GetWidth

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetWidth(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outWidth)
```

**描述**

获取当前帧的图像数据的宽度。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

image

当前帧图像对象，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

outWidth

返回当前帧的图像的宽度，以像素为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARImage_Release

```ets
void HMS_AREngine_ARImage_Release(AREngine_ARImage *image)
```

**描述**

释放当前帧的图像对象,，由[HMS_AREngine_ARFrame_AcquireCameraImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad5619c3cbd2b9ea0cfeff22b72f8d81d)创建的对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

image

待释放的当前帧图像对象，参见[AREngine_ARImage](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)。

#### HMS_AREngine_ARPlane_AcquireSubsumedBy

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_AcquireSubsumedBy(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPlane **outSubsumedBy)
```

**描述**

获取平面的父平面（一个平面被另一个平面合并时，会产生父平面），如果无父平面返回为NULL。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

plane

待处理的平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

outSubsumedBy

返回指定平面的父平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPlane_GetCenterPose

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPose *outPose)
```

**描述**

获取从平面的局部坐标系到世界坐标系转换的位姿信息。

平面局部坐标系（右手坐标系）为：原点在包裹平面矩形的中心，矩形更长的边方向为X轴，短边方向为Z轴，Y+为平面法向量。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

plane

待处理的平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

outPose

返回平面的局部坐标系到世界坐标系转换的位姿信息，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPlane_GetExtentX

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetExtentX(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outExtentX)
```

**描述**

获取平面的矩形边界沿平面局部坐标系X轴的长度，如矩形的宽度。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

plane

待处理的平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

outExtentX

返回平面的矩形边界沿平面局部坐标系X轴的长度，以m为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPlane_GetExtentZ

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetExtentZ(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outExtentZ)
```

**描述**

获取平面的矩形边界沿平面局部坐标系Z轴的长度，如矩形的高度。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

plane

待处理的平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

outExtentZ

返回平面的矩形边界沿平面局部坐标系Z轴的长度，以m为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPlane_GetLabel

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetLabel(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARSemanticPlaneLabel *label)
```

**描述**

获取平面的语义类型，如桌面、地板等。

使用时需要使用[HMS_AREngine_ARConfig_SetSemanticMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae87c1ef02b6e9bab123fae2086da248)启用语义识别模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

plane

待处理的平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

label

返回当前平面的语义类型，参见[AREngine_ARSemanticPlaneLabel](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gafbb6b69fefdc417ba6437ce2fe587cb1)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPlane_GetPolygon

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetPolygon(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outPolygonXz, int32_t polygonSize)
```

**描述**

获取检测到平面的二维顶点数组，格式为[x1，z1，x2，z2，...]。

这些值均在平面局部坐标系的x-z平面中定义，须经[HMS_AREngine_ARPlane_GetCenterPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabbb03027afb984be8542d00d2eebd063)转换到世界坐标系中。

注意：在垂直平面中返回的值也是局部坐标系中的坐标[x1，z1，x2，z2，….]，需要使用[HMS_AREngine_ARPlane_GetCenterPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabbb03027afb984be8542d00d2eebd063)转换到世界坐标系。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

plane

待处理的平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

outPolygonXz

返回检测到平面的二维顶点数组。

polygonSize

二维顶点数组大小，通过[HMS_AREngine_ARPlane_GetPolygonSize](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga98760556eee2a4a69c33699b7ce3edc6)接口获取。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPlane_GetPolygonSize

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetPolygonSize(const AREngine_ARSession *session, const AREngine_ARPlane *plane, int32_t *outPolygonSize)
```

**描述**

获取检测到平面的二维顶点数组大小。

配合[HMS_AREngine_ARPlane_GetPolygon](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3537ce62e6a92dcdbddff0f39de0fae3)接口使用。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

plane

待处理的平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

outPolygonSize

返回二维顶点数组大小。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPlane_GetType

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetType(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPlaneType *outPlaneType)
```

**描述**

获取平面的类型。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

plane

待处理的平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

outPlaneType

返回平面的类型，参见[AREngine_ARPlaneType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga895db37a92155584c5448bee30a8beab)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPlane_IsPoseInExtents

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_IsPoseInExtents(const AREngine_ARSession *session, const AREngine_ARPlane *plane, const AREngine_ARPose *pose, int32_t *outPoseInExtents)
```

**描述**

判断位姿是否位于平面的矩形范围内。

如果传入的位姿（通过[HMS_AREngine_ARHitResult_GetHitPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8beaa085410712425041e81f9bc6aa09)获取）位于平面的矩形范围内，则返回非0值。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

plane

待处理的平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

pose

位姿信息，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

outPoseInExtents

返回位姿是否位于平面的矩形范围内，0表示不在范围内，非0表示在范围内。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPlane_IsPoseInPolygon

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_IsPoseInPolygon(const AREngine_ARSession *session, const AREngine_ARPlane *plane, const AREngine_ARPose *pose, int32_t *outPoseInPolygon)
```

**描述**

判断位姿是否位于平面的多边形范围内。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

plane

待处理的平面对象，参见[AREngine_ARPlane](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)。

pose

位姿信息，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

outPoseInPolygon

返回位姿是否位于平面的多边形范围内，0表示不在范围内，非0表示在范围内。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPoint_GetOrientationMode

```ets
AREngine_ARStatus HMS_AREngine_ARPoint_GetOrientationMode(const AREngine_ARSession *session, const AREngine_ARPoint *point, AREngine_ARPointOrientationMode *outOrientationMode)
```

**描述**

获取输入点的朝向模式。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

point

输入点对象，参见[AREngine_ARPoint](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6)。

outOrientationMode

返回输入点的朝向模式，参见[AREngine_ARPointOrientationMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0e2893593f4372954fd97519e0a63855)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPoint_GetPose

```ets
AREngine_ARStatus HMS_AREngine_ARPoint_GetPose(const AREngine_ARSession *session, const AREngine_ARPoint *point, AREngine_ARPose *outPose)
```

**描述**

获取输入点的位姿信息。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

point

输入点对象，参见[AREngine_ARPoint](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6)。

outPose

返回输入点的位姿信息，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPointCloud_GetData

```ets
AREngine_ARStatus HMS_AREngine_ARPointCloud_GetData(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, const float **outPointCloudData)
```

**描述**

获取点云中所有点的坐标及置信度数组。

其坐标值都在世界坐标系下，使用右手坐标系表示。点云对象可以通过[HMS_AREngine_ARFrame_AcquirePointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga877f7fc9d9c303f1fd8efb00ec383b34)获取。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

pointCloud

点云对象，参见[AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc)。

outPointCloudData

返回点云中所有点的坐标及置信度数组。数据格式为[x0，y0，z0，c0，x1，y1，z1，c1，x2...]。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPointCloud_GetNumberOfPoints

```ets
AREngine_ARStatus HMS_AREngine_ARPointCloud_GetNumberOfPoints(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, int32_t *outNumberOfPoints)
```

**描述**

获取点云中所有点的坐标及置信度数组大小。

与[HMS_AREngine_ARPointCloud_GetData](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4061cacb3f3ce45e529acb9afbcdc5ce)配合使用。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

pointCloud

点云对象，参见[AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc)。

outNumberOfPoints

返回点云中所有点的坐标及置信度数组大小。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPointCloud_GetTimestamp

```ets
AREngine_ARStatus HMS_AREngine_ARPointCloud_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, int64_t *outTimestampNs)
```

**描述**

获取检测到当前特征点云的时间，以ns为单位。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

pointCloud

点云对象，参见[AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc)。

outTimestampNs

返回检测到当前特征点云的时间。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPointCloud_Release

```ets
void HMS_AREngine_ARPointCloud_Release(AREngine_ARPointCloud *pointCloud)
```

**描述**

释放点云对象使用的内存。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

pointCloud

待释放的点云对象，参见[AREngine_ARPointCloud](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc)。

#### HMS_AREngine_ARPose_Create

```ets
AREngine_ARStatus HMS_AREngine_ARPose_Create(const AREngine_ARSession *session, const float *poseRaw, const uint32_t poseRawSize, AREngine_ARPose **outPose)
```

**描述**

分配并初始化一个新的位姿对象。

可以设置poseRaw为空，来创建未初始化的位姿对象，随后调用[HMS_AREngine_ARPoint_GetPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8255eece88d8dc76c554eed360fb7c7b)、[HMS_AREngine_ARAnchor_GetPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad937acfc5d49f0909bdd84677bb0731a)等为位姿对象赋值。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

poseRaw

位姿数据，包括平移分量与旋转分量，数组大小为7，poseRaw[0]~poseRaw[3]为旋转分量quaternion，poseRaw[4]~poseRaw[6]为平移分量(x，y，z)。

poseRawSize

数组大小. 数组大小大于等于[ARENGINE_POSE_RAW_SIZE](#section14280842115815)。

outPose

返回新创建的位姿对象，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARPose_Destroy

```ets
void HMS_AREngine_ARPose_Destroy(AREngine_ARPose *pose)
```

**描述**

释放位姿对象使用的内存。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

pose

待释放的位姿对象，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

#### HMS_AREngine_ARPose_GetMatrix

```ets
AREngine_ARStatus HMS_AREngine_ARPose_GetMatrix(const AREngine_ARSession *session, const AREngine_ARPose *pose, float *outMatrixColMajor4x4, int32_t matrixColMajor4x4Size)
```

**描述**

将位姿数据转换成4X4的矩阵。

outMatrixColMajor4x4为存放数组，其中的数据按照列优先存储，该矩阵与局部坐标系的坐标点做乘法，可以得到局部坐标系到世界坐标系的转换。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

pose

位姿对象，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

outMatrixColMajor4x4

返回一个大小为16的float数组，数据按照列优先存储。

matrixColMajor4x4Size

数组大小. 数组大小定义为：[ARENGINE_VIEW_MATRIX_SIZE](#section02261581599)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARPose_GetPoseRaw

```ets
AREngine_ARStatus HMS_AREngine_ARPose_GetPoseRaw(const AREngine_ARSession *session, const AREngine_ARPose *pose, float *outPoseRaw, int32_t poseRawSize)
```

**描述**

从位姿对象提取位姿数据。

包括平移分量与旋转分量，数组大小为7，poseRaw[0]~poseRaw[3]为旋转分量quaternion，poseRaw[4]~poseRaw[6]为平移分量(x，y，z)。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

pose

位姿对象，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

outPoseRaw

返回位姿数据。

poseRawSize

数组大小. 数组大小定义为：[ARENGINE_POSE_RAW_SIZE](#section14280842115815)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSceneMesh_AcquireIndexList

```ets
AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireIndexList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outData, int32_t dataSize)
```

**描述**

获取mesh面片的索引集合。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

sceneMesh

当前帧的Mesh信息，参见[AREngine_ARSceneMesh](#section543212520614)。

outData

返回mesh面片的索引集合。

dataSize

mesh面片的索引个数，参见[HMS_AREngine_ARSceneMesh_AcquireIndexListSize](#section12621161917152)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSceneMesh_AcquireIndexListSize

```ets
AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireIndexListSize(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outSize)
```

**描述**

获取mesh面片的索引个数。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

sceneMesh

当前帧的Mesh信息，参见[AREngine_ARSceneMesh](#section543212520614)。

outSize

返回mesh面片的索引个数。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSceneMesh_AcquireVertexList

```ets
AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVertexList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, float *outData, int32_t dataSize)
```

**描述**

获取mesh的顶点集合。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

sceneMesh

当前帧的Mesh信息，参见[AREngine_ARSceneMesh](#section543212520614)。

outData

返回mesh顶点集合，数组内容为每个顶点的世界坐标展开，例如[x1, y1,z1, x2, y2, z2, ...] 。

dataSize

mesh面片的顶点个数，参见[HMS_AREngine_ARSceneMesh_AcquireVerticesSize](#section1860218429179)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSceneMesh_AcquireVertexNormalList

```ets
AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVertexNormalList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, float *outData, int32_t dataSize)
```

**描述**

获取mesh面片的法向量集合。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

sceneMesh

当前帧的Mesh信息，参见[AREngine_ARSceneMesh](#section543212520614)。

outData

返回mesh面片的法线向量集合，数组内容为每个面片法线向量的世界坐标展开，例如[x1,y1,z1, x2, y2, z2, ...]。

dataSize

mesh面片的索引个数，参见[HMS_AREngine_ARSceneMesh_AcquireIndexListSize](#section12621161917152)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSceneMesh_AcquireVerticesSize

```ets
AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVerticesSize(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outSize)
```

**描述**

获取mesh的顶点个数。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

sceneMesh

当前帧的Mesh信息，参见[AREngine_ARSceneMesh](#section543212520614)。

outSize

返回mesh的顶点个数。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSceneMesh_Release

```ets
void HMS_AREngine_ARSceneMesh_Release(AREngine_ARSceneMesh *sceneMesh)
```

**描述**

释放当前帧的mesh信息。

**起始版本：** 5.1.0(18)

**参数:**

名称

描述

sceneMesh

当前帧的Mesh信息，参见[AREngine_ARSceneMesh](#section543212520614)。

#### HMS_AREngine_ARSemanticDense_AcquireCubeData

```ets
AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquireCubeData(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, AREngine_ARSemanticDenseCubeData **outCubeData)
```

**描述**

获取识别到的高精几何重建对象数据中的立方体数据。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

semanticDenseData

高精几何重建对象数据集合，参见[AREngine_ARSemanticDenseData](#section1410813229144)。

outCubeData

返回高精几何重建对象数据中立方体的数据，参见[AREngine_ARSemanticDenseCubeData](AREngine_ARSemanticDenseCubeData.md)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSemanticDense_AcquireCubeDataSize

```ets
AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquireCubeDataSize(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, int64_t *outSize)
```

**描述**

获取识别到的高精几何重建对象数据中的立方体数量。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

semanticDenseData

高精几何重建对象数据集合，参见[AREngine_ARSemanticDenseData](#section1410813229144)。

outSize

返回[AREngine_ARSemanticDenseData](#section1410813229144)对象中立方体数量的大小。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSemanticDense_AcquirePointData

```ets
AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquirePointData(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, AREngine_ARSemanticDensePointData **outPointData)
```

**描述**

获取识别到的高精几何重建对象数据中的稠密点云数据。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

semanticDenseData

高精几何重建对象数据集合，参见[AREngine_ARSemanticDenseData](#section1410813229144)。

outPointData

返回高精几何重建对象数据中稠密点云的数据，参见[AREngine_ARSemanticDensePointData](AREngine_ARSemanticDensePointData.md)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSemanticDense_AcquirePointDataSize

```ets
AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquirePointDataSize(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, int64_t *outSize)
```

**描述**

获取识别到的高精几何重建对象数据中的稠密点云数量。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

semanticDenseData

稠密点云的数据集合，参见[AREngine_ARSemanticDenseData](#section1410813229144)。

outSize

返回[AREngine_ARSemanticDenseData](#section1410813229144)对象中稠密点云数量的大小。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSemanticDense_Release

```ets
void HMS_AREngine_ARSemanticDense_Release(AREngine_ARSemanticDenseData *semanticDenseData)
```

**描述**

释放高精几何重建对象。

**起始版本：** 6.0.0(20)

**参数:**

名称

描述

semanticDenseData

释放高精几何重建对象，参见[AREngine_ARSemanticDenseData](#section1410813229144)。

#### HMS_AREngine_ARSession_AcquireNewAnchor

```ets
AREngine_ARStatus HMS_AREngine_ARSession_AcquireNewAnchor(AREngine_ARSession *session, const AREngine_ARPose *pose, AREngine_ARAnchor **outAnchor)
```

**描述**

创建一个持续跟踪的锚点。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

pose

创建锚点时使用的pose对象，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

outAnchor

被创建的锚点对象，参见[AREngine_ARAnchor](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_NOT_TRACKING

未跟踪状态。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARSession_Configure

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Configure(AREngine_ARSession *session, const AREngine_ARConfig *config)
```

**描述**

配置[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)会话。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

config

需要配置到设备上的配置对象，参见 [AREngine_ARConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

****ARENGINE_ERROR_SESSION_NOT_PAUSED

会话未暂停状态。

#### HMS_AREngine_ARSession_Create

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Create(void *env, void *applicationContext, AREngine_ARSession **outSessionPointer)
```

**描述**

创建一个新的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)会话。

此接口依赖相机、加速度以及陀螺仪传感器权限。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

env

当前APP的JNI运行环境信息。

applicationContext

与应用对应的Context。

outSessionPointer

被创建的会话对象，参见[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_PERMISSION_NOT_GRANTED

权限未授予状态。如相机权限未授予。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_DEVICE_NOT_SUPPORTED

不可用：设备不兼容状态。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARSession_Destroy

```ets
void HMS_AREngine_ARSession_Destroy(AREngine_ARSession *session)
```

**描述**

释放[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)会话使用的资源。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

#### HMS_AREngine_ARSession_GetAllAnchors

```ets
AREngine_ARStatus HMS_AREngine_ARSession_GetAllAnchors(const AREngine_ARSession *session, AREngine_ARAnchorList *outAnchorList)
```

**描述**

获取所有锚点，包括[AREngine_ARTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)中包含的所有状态下的锚点。

应用处理时需要仅绘制[ARENGINE_TRACKING_STATE_TRACKING](#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)状态的锚点，删除[ARENGINE_TRACKING_STATE_STOPPED](#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)状态的锚点。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outAnchorList

返回所有的锚点对象列表，参见[AREngine_ARAnchorList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSession_GetAllTrackables

```ets
AREngine_ARStatus HMS_AREngine_ARSession_GetAllTrackables(const AREngine_ARSession *session, AREngine_ARTrackableType filterType, AREngine_ARTrackableList *outTrackableList)
```

**描述**

获取所有指定类型的可跟踪对象集合。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

filterType

当前指定的可跟踪对象类型，参见[AREngine_ARTrackableType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d)。

outTrackableList

返回指定类型的可跟踪对象集合，参见 [AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSession_GetCameraConfig

```ets
AREngine_ARStatus HMS_AREngine_ARSession_GetCameraConfig(const AREngine_ARSession *session, AREngine_ARCameraConfig *outCameraConfig)
```

**描述**

获取相机配置信息。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outCameraConfig

返回相机配置信息，参见[AREngine_ARCameraConfig](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSession_Pause

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Pause(AREngine_ARSession *session)
```

**描述**

暂停会话，停止相机预览流，不清除平面和锚点数据，释放相机（否则其他应用无法使用相机服务）。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARSession_Resume

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Resume(AREngine_ARSession *session)
```

**描述**

开始运行[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)，或者在调用[HMS_AREngine_ARSession_Pause](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga09dedb5c633141321591db0981629de1)以后恢复[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)的运行状态。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

****ARENGINE_ERROR_CAMERA_NOT_AVAILABLE

相机不可用状态。

#### HMS_AREngine_ARSession_SetCameraGLTexture

```ets
AREngine_ARStatus HMS_AREngine_ARSession_SetCameraGLTexture(AREngine_ARSession *session, uint32_t textureId)
```

**描述**

设置可用于存储相机预览流数据的OpenGL纹理。

应用调用[HMS_AREngine_ARSession_Update](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259)后，AR Engine会更新相机预览到纹理中。

纹理使用时需指定为GL_TEXTURE_EXTERNAL_OES，如：glBindTexture(GL_TEXTURE_EXTERNAL_OES, textureId)。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

textureId

相机预览数据流的OpenGL textureId，大于0。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSession_SetDisplayGeometry

```ets
AREngine_ARStatus HMS_AREngine_ARSession_SetDisplayGeometry(AREngine_ARSession *session, AREngine_ARPoseType rotation, int32_t width, int32_t height)
```

**描述**

设置显示的高和宽，以像素为单位。

该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

rotation

显示旋转常量，值为[AREngine_ARPoseType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae551da7b220b8b38140c3c28882e5010)中定义的枚举值。

width

显示的宽度，以像素为单位。其最大数值受设备屏幕像素限制，可通过[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)获取。

height

显示的高度，以像素为单位。其最大数值受设备屏幕像素限制，可通过[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines)获取。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARSession_Stop

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Stop(AREngine_ARSession *session)
```

**描述**

停止AR Engine，停止相机预览流，清除平面和锚点数据，并释放相机，终止本次会话。

调用后，如果要再次启动，需要新建[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

#### HMS_AREngine_ARSession_Update

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Update(AREngine_ARSession *session, AREngine_ARFrame *outFrame)
```

**描述**

更新AR Engine的计算结果。

应用应在需要获取最新的数据时调用此接口，如相机发生移动以后，使用此接口可以获取新的锚点坐标、平面坐标、相机获取的图像帧等。

如果[HMS_AREngine_ARConfig_GetUpdateMode](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf32a3cb1f345cd5a243683ecdec63cef)为[ARENGINE_UPDATE_MODE_BLOCKING](#ZH-CN_TOPIC_0000002500306234__gabd21cc975ee97b7fb2133af0068ebb5e)状态，那么该函数会阻塞至有新的帧可用。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outFrame

返回更新后的帧对象，参见[AREngine_ARFrame](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_FATAL

失败状态。

****ARENGINE_ERROR_SESSION_PAUSED

会话已暂停状态。

****ARENGINE_ERROR_MISSING_GL_CONTEXT

缺少GL上下文状态。

****ARENGINE_ERROR_CAMERA_NOT_AVAILABLE

相机不可用状态。

ARENGINE_ERROR_IMAGE_INVALID_DATABASE

没有有效的图像数据库。

**起始版本：** 5.1.0(18)

#### HMS_AREngine_ARTarget_GetAxisAlignedBoundingBox

```ets
AREngine_ARStatus HMS_AREngine_ARTarget_GetAxisAlignedBoundingBox(const AREngine_ARSession *session, const AREngine_ARTarget *target, float *outAabb, int32_t aabbSize)
```

**描述**

获取语义物体最小外接包围盒坐标，坐标格式为(xmin，ymin，zmin，xmax，ymax，zmax)。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

target

待处理的目标语义对象，参见[AREngine_ARTarget](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0)。

outAabb

返回当前目标语义识别物体的最小外接包围盒坐标集。

aabbSize

数组大小为：[ARENGINE_AABB_POINT_SIZE](#section1046854145717)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARTarget_GetCenterPose

```ets
AREngine_ARStatus HMS_AREngine_ARTarget_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARTarget *target, AREngine_ARPose *outARPose)
```

**描述**

获取从目标语义对象的局部坐标系到世界坐标系转换的位姿对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

target

待处理的目标语义对象，参见[AREngine_ARTarget](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0)。

outARPose

返回目标语义对象的局部坐标系到世界坐标系转换的位姿，参见[AREngine_ARPose](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARTarget_GetRadius

```ets
AREngine_ARStatus HMS_AREngine_ARTarget_GetRadius(const AREngine_ARSession *session, const AREngine_ARTarget *target, float *radius)
```

**描述**

获取语义物体的球体半径。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

target

待处理的目标语义对象，参见[AREngine_ARTarget](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0)。

radius

返回当前目标语义物体的球体半径，以m为单位。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARTarget_GetShapeType

```ets
AREngine_ARStatus HMS_AREngine_ARTarget_GetShapeType(const AREngine_ARSession *session, const AREngine_ARTarget *target, AREngine_ARTargetShapeLabel *shape)
```

**描述**

获取语义物体的形状类型。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

target

待处理的目标语义对象，参见[AREngine_ARTarget](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0)。

shape

返回当前目标语义识别到的物体形状类型，参见 [AREngine_ARTargetShapeLabel](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaed68dc13cc314da98d79c88b12d3ae49)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARTrackable_AcquireNewAnchor

```ets
AREngine_ARStatus HMS_AREngine_ARTrackable_AcquireNewAnchor(AREngine_ARSession *session, AREngine_ARTrackable *trackable, AREngine_ARPose *pose, AREngine_ARAnchor **outAnchor)
```

**描述**

通过可跟踪对象的位姿信息创建对应的锚点对象，该锚点将和当前的可跟踪对象绑定。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

trackable

可跟踪对象。

pose

可跟踪对象的位姿信息。

outAnchor

新创建的锚点对象。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_NOT_TRACKING

未跟踪状态。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARTrackable_GetAnchors

```ets
AREngine_ARStatus HMS_AREngine_ARTrackable_GetAnchors(AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARAnchorList *outAnchorList)
```

**描述**

获取绑定到输入可跟踪对象的锚点对象列表。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

trackable

可跟踪对象，参见[AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970)。

outAnchorList

返回锚点对象列表，此列表必须使用[HMS_AREngine_ARAnchorList_Create](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga30492334f7a06b98ef0ad5831d33b198)创建。如果使用已经创建的列表，则此列表将被重新赋值。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARTrackable_GetTrackingState

```ets
AREngine_ARStatus HMS_AREngine_ARTrackable_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARTrackingState *outTrackingState)
```

**描述**

获取当前可跟踪对象的跟踪状态。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

trackable

可跟踪对象，参见[AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970)。

outTrackingState

返回可跟踪对象的跟踪状态，参见[AREngine_ARTrackingState](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARTrackable_GetType

```ets
AREngine_ARStatus HMS_AREngine_ARTrackable_GetType(const AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARTrackableType *outTrackableType)
```

**描述**

获取可跟踪对象的类型。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

trackable

可跟踪对象，参见[AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970)。

outTrackableType

返回可跟踪对象的类型，参见[AREngine_ARTrackableType](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARTrackable_Release

```ets
void HMS_AREngine_ARTrackable_Release(AREngine_ARTrackable *trackable)
```

**描述**

释放可跟踪对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

trackable

待释放的可跟踪对象，参见[AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970)。

#### HMS_AREngine_ARTrackableList_AcquireItem

```ets
AREngine_ARStatus HMS_AREngine_ARTrackableList_AcquireItem(const AREngine_ARSession *session, const AREngine_ARTrackableList *trackableList, int32_t index, AREngine_ARTrackable **outTrackable)
```

**描述**

从可跟踪列表中获取指定index的对象。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

trackableList

被检索的可跟踪对象的列表，参见[AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205)。

index

可跟踪对象在可跟踪对象列表中的位置。最大值不超过[HMS_AREngine_ARTrackableList_GetSize](#ZH-CN_TOPIC_0000002500306234__gad9729d4436f3d969286f31b33d07513e)。

outTrackable

返回目标可跟踪对象，参见[AREngine_ARTrackable](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

#### HMS_AREngine_ARTrackableList_Create

```ets
AREngine_ARStatus HMS_AREngine_ARTrackableList_Create(const AREngine_ARSession *session, AREngine_ARTrackableList **outTrackableList)
```

**描述**

创建一个可跟踪对象列表。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

outTrackableList

待创建的可跟踪对象列表，参见[AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205)。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。

****ARENGINE_ERROR_RESOURCE_EXHAUSTED

资源耗尽状态。

#### HMS_AREngine_ARTrackableList_Destroy

```ets
void HMS_AREngine_ARTrackableList_Destroy(AREngine_ARTrackableList *trackableList)
```

**描述**

释放可跟踪对象列表，以及它持有的所有锚点引用。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

trackableList

待释放的可跟踪对象列表，参见[AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205)。

#### HMS_AREngine_ARTrackableList_GetSize

```ets
AREngine_ARStatus HMS_AREngine_ARTrackableList_GetSize(const AREngine_ARSession *session, const AREngine_ARTrackableList *trackableList, int32_t *outSize)
```

**描述**

获取此列表中的可跟踪对象的数量。

**起始版本：** 5.0.0(12)

**参数:**

名称

描述

session

与AR Engine服务交互的[AREngine_ARSession](AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)对象。

trackableList

可跟踪对象列表，参见[AREngine_ARTrackableList](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205)。

outSize

返回可跟踪对象列表中可跟踪对象的数量。

**返回：**

接口执行状态，参见[AREngine_ARStatus](AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)。

状态码

状态信息

****ARENGINE_SUCCESS

成功状态。

****ARENGINE_ERROR_INVALID_ARGUMENT

无效参数状态。如方法入参为空或非法。