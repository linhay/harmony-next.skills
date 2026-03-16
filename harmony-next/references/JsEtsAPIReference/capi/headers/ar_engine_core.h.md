# ar_engine_core.h

#### 概述

本声明用于访问AR Engine（AR引擎服务）的API。提供AR（增强现实）能力的相关接口。AR的基础核心能力，包含：运动跟踪能力、环境跟踪能力和命中检测能力。

**库：** libarengine_ndk.z.so

**系统能力：** SystemCapability.AREngine.Core

**起始版本：** 5.0.0(12)

**相关模块：**[AR Engine](../../topics/media/AR Engine.md)

#### 结构体

名称

描述

struct [AREngine_ARAugmentedImageSource](../../topics/graphics/AREngine_ARAugmentedImageSource.md)

图像数据。

struct [AREngine_ClipPlaneDistance](../../topics/media/AREngine_ClipPlaneDistance.md)

裁剪平面距离数据。

struct [AREngine_ARSemanticDensePointData](../../topics/media/AREngine_ARSemanticDensePointData.md)

高精几何重建对象的稠密点云数据。

struct [AREngine_ARSemanticDenseCubeData](../../topics/media/AREngine_ARSemanticDenseCubeData.md)

高精几何重建对象的立方体数据。

#### 宏定义

名称

描述

[ARENGINE_AABB_POINT_SIZE](../../topics/media/AR Engine.md#section1046854145717) = 6

包围盒坐标集数组大小。

[ARENGINE_DISTORTION_COUNT](../../topics/media/AR Engine.md#section2059093619593) = 5

相机畸变参数的个数。

[ARENGINE_POSE_RAW_SIZE](../../topics/media/AR Engine.md#section14280842115815) = 7

位姿数据数组大小。

[ARENGINE_VIEW_MATRIX_SIZE](../../topics/media/AR Engine.md#section02261581599) = 16

变换矩阵数组大小。

#### 类型定义

名称

描述

typedef struct [AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)[AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)

锚点对象。

typedef struct [AREngine_ARAnchorList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872)[AREngine_ARAnchorList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872)

锚点对象列表。

typedef struct [AREngine_ARAugmentedImage](../../topics/media/AR Engine.md#section68491824155217)[AREngine_ARAugmentedImage](../../topics/media/AR Engine.md#section68491824155217)

跟踪图像对象。

typedef struct [AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330)[AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330)

跟踪图像数据库对象。

typedef struct [AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)[AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92)

当前帧对应的相机信息。

typedef struct [AREngine_ARCameraConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba)[AREngine_ARCameraConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba)

相机的配置信息。

typedef struct [AREngine_ARCameraIntrinsics](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)[AREngine_ARCameraIntrinsics](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51)

相机内参。

typedef struct [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)[AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619)

用于配置[AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)的能力项（使用哪些能力、模式等）。

typedef struct [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)[AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)

AR Engine处理的一帧数据。

typedef struct [AREngine_ARHitResult](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)[AREngine_ARHitResult](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507)

命中检测结果对象。

typedef struct [AREngine_ARHitResultList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3)[AREngine_ARHitResultList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3)

命中检测结果列表。

typedef struct [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)[AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59)

相机视频流帧对象。

typedef struct [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)[AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5)

平面对象。

typedef struct [AREngine_ARPoint](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6)[AREngine_ARPoint](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6)

点对象。

typedef struct [AREngine_ARPointCloud](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc)[AREngine_ARPointCloud](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc)

可跟踪的3D点云的集合。

typedef struct [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)[AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604)

位姿对象。

typedef struct [AREngine_ARSceneMesh](../../topics/media/AR Engine.md#section543212520614)[AREngine_ARSceneMesh](../../topics/media/AR Engine.md#section543212520614)

环境mesh数据的集合。

typedef struct [AREngine_ARSemanticDenseData](../../topics/media/AR Engine.md#section1410813229144)[AREngine_ARSemanticDenseData](../../topics/media/AR Engine.md#section1410813229144)

表示高精几何重建对象数据的集合。

typedef struct [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)[AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)

管理AR Engine的系统状态。

typedef struct [AREngine_ARTarget](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0)[AREngine_ARTarget](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0)

物体对象。

typedef struct [AREngine_ARTrackable](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970)[AREngine_ARTrackable](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970)

可跟踪对象，如点、平面等。

typedef struct [AREngine_ARTrackableList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205)[AREngine_ARTrackableList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205)

可跟踪对象列表。

typedef void (*[HMS_AREngine_PhotoAvailableCallback](../../topics/media/AR Engine.md#section430673420224))([OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-oh-nativebuffer) *photoBuffer)

输出拍照流图像回调。

#### 枚举

名称

描述

[AREngine_ARAddAugmentedImageReason](../../topics/media/AR Engine.md#section2441053595) {

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_NONE = 0,

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_SIZE_NOT_MATCH = 1,

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_LIGHT_ANOMALY = 2,

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_FEATURE_LIMIT = 3,

ARENGINE_ADD_AUGMENTED_IMAGE_REASON_OTHER = 4

}

跟踪失败的可能原因。

[AREngine_ARConfidenceLevel](../../topics/media/AR Engine.md#section959011484610) {

ARENGINE_DEPTH_CONFIDENCE_LOW = 0,

ARENGINE_DEPTH_CONFIDENCE_MEDIUM = 1,

ARENGINE_DEPTH_CONFIDENCE_HIGH = 2

}

深度置信度。

[AREngine_ARDepthMode](../../topics/media/AR Engine.md#section12321429115215) {

ARENGINE_DEPTH_MODE_DISABLED = 0,

ARENGINE_DEPTH_MODE_AUTOMATIC = 1

}

深度模式。

[AREngine_ARFocusMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf50530faa0d094182a0db0c73b75d875) {

ARENGINE_FOCUS_MODE_FIXED = 0,

ARENGINE_FOCUS_MODE_AUTO = 1

}

对焦模式。

[AREngine_ARImageDatabaseMode](../../topics/media/AR Engine.md#section683253471219) {

ARENGINE_ADD_NORMAL = 0,

ARENGINE_ADD_AUTO = 1

}

用于跟踪的特征库图像添加方式。

[AREngine_ARImageFormat](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadfcf7a1211ed12a90f377610d0f838ac) {

ARENGINE_IMAGE_UNKNOWN = 0,

ARENGINE_IMAGE_YUV_420_888 = 2,

ARENGINE_IMAGE_Y_8 = 3,

ARENGINE_IMAGE_Y_16 = 4

}

图像数据格式。

[AREngine_ARImageStreamMode](../../topics/media/AR Engine.md#section184201559356) {

ARENGINE_IMAGE_STREAM_MODE_PREVIEW = 0,

ARENGINE_IMAGE_STREAM_MODE_PREVIEW_AND_PHOTO = 1

}

设置图片数据流模式，默认情况下系统设置为ARENGINE_IMAGE_STREAM_MODE_PREVIEW。

[AREngine_ARMeshMode](../../topics/media/AR Engine.md#section19436658201620) {

ARENGINE_MESH_MODE_DISABLED = 0,

ARENGINE_MESH_MODE_ENABLE=1

}

Mesh启用模式。

[AREngine_ARPlaneFindingMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab8e7db52d819359026fc4a82815d3fff) {

ARENGINE_PLANE_FINDING_MODE_DISABLED = 0,

ARENGINE_PLANE_FINDING_MODE_HORIZONTAL = 1,

ARENGINE_PLANE_FINDING_MODE_VERTICAL = 2,

ARENGINE_PLANE_FINDING_MODE_HORIZONTAL_AND_VERTICAL = 3

}

平面搜索模式。

[AREngine_ARPlaneType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga895db37a92155584c5448bee30a8beab) {

ARENGINE_PLANE_FACING_HORIZONTAL_UPWARD = 0,

ARENGINE_PLANE_FACING_HORIZONTAL_DOWNWARD = 1,

ARENGINE_PLANE_FACING_VERTICAL = 2,

ARENGINE_PLANE_FACING_INVALID = 3

}

平面类型。

[AREngine_ARPointOrientationMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0e2893593f4372954fd97519e0a63855) {

ARENGINE_POINT_ORIENTATION_INITIALIZED_TO_IDENTITY = 0,

ARENGINE_POINT_ORIENTATION_ESTIMATED_SURFACE_NORMAL = 1

}

朝向模式。

[AREngine_ARPoseMode](../../topics/media/AR Engine.md#section1249515330198) {

ARENGINE_POSE_MODE_GRAVITY = 0,

ARENGINE_POSE_MODE_GRAVITY_HEADING = 1

}

AR Engine输出的相机位姿对齐格式。

[AREngine_ARPoseType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae551da7b220b8b38140c3c28882e5010) {

ARENGINE_POSE_TYPE_IDENTITY = 0,

ARENGINE_POSE_TYPE_ROTATE_90 = 1,

ARENGINE_POSE_TYPE_ROTATE_180 = 2,

ARENGINE_POSE_TYPE_ROTATE_270 = 3

}

位姿类型。

[AREngine_ARPowerMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3d925e007e2847e69f22af68ec922507) {

ARENGINE_POWER_MODE_NORMAL = 0,

ARENGINE_POWER_MODE_POWER_SAVING = 1,

ARENGINE_POWER_MODE_PERFORMANCE_FIRST = 2,

ARENGINE_POWER_MODE_BOOST = 3 ,

ARENGINE_POWER_MODE_ULTRA_POWER_SAVING = 11

}

电源功耗模式。

[AREngine_ARPreviewMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadef0f2099b106b872a014ef6551906ae) {

ARENGINE_PREVIEW_MODE_ENABLED = 0,

ARENGINE_PREVIEW_MODE_DISABLED = 1

}

预览模式。

[AREngine_ARSemanticDenseMode](../../topics/media/AR Engine.md#section09971756142213) {

ARENGINE_SEMANTIC_DENSE_MODE_DISABLED = 0,

ARENGINE_SEMANTIC_DENSE_MODE_NORMAL = 1,

ARENGINE_SEMANTIC_DENSE_MODE_CUBE_VOLUME = 2,

ARENGINE_SEMANTIC_DENSE_MODE_CUBE_SPACE = 3

}

高精几何重建识别模式。

[AREngine_ARSemanticMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga34d3000de29454b99d89406d288d6ed5) {

ARENGINE_SEMANTIC_MODE_NONE = 0,

ARENGINE_SEMANTIC_MODE_PLANE = 1,

ARENGINE_SEMANTIC_MODE_TARGET = 2

}

语义模式。

[AREngine_ARSemanticPlaneLabel](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gafbb6b69fefdc417ba6437ce2fe587cb1) {

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

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d) {

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

[AREngine_ARTargetShapeLabel](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaed68dc13cc314da98d79c88b12d3ae49) {

ARENGINE_TARGET_SHAPE_UNKNOWN = 0,

ARENGINE_TARGET_SHAPE_CUBE = 1,

ARENGINE_TARGET_SHAPE_CIRCLE = 2,

ARENGINE_TARGET_SHAPE_RECTANGLE = 3

}

识别到的物体形状。

[AREngine_ARTrackableType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d) {

ARENGINE_TRACKABLE_BASE = 0x41520100,

ARENGINE_TRACKABLE_PLANE = 0x41520101,

ARENGINE_TRACKABLE_POINT = 0x41520102,

ARENGINE_TRACKABLE_AUGMENTED_IMAGE = 0x41520104,

ARENGINE_TRACKABLE_TARGET = 0x50000008,

ARENGINE_TRACKABLE_INVALID = 0

}

可跟踪对象类型，如平面、点等。

[AREngine_ARTrackingState](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382) {

ARENGINE_TRACKING_STATE_TRACKING = 0,

ARENGINE_TRACKING_STATE_PAUSED = 1,

ARENGINE_TRACKING_STATE_STOPPED = 2

}

可跟踪对象的跟踪状态。

[AREngine_ARTrackingStateReason](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga67774b71935ef2f8a2ae5e5822c3dcdb) {

ARENGINE_TRACKING_STATE_REASON_NONE = 0,

ARENGINE_TRACKING_STATE_REASON_EXCESSIVE_MOTION = 1,

ARENGINE_TRACKING_STATE_REASON_INSUFFICIENT_FEATURES = 2

}

可能的跟踪失败原因。

[AREngine_ARType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga987888aea7dcaa9abcdb64581c850bf5) {

ARENGINE_TYPE_WORLD = 0x01,

ARENGINE_TYPE_IMAGE = 0x80

}

AR能力类型。

[AREngine_ARUpdateMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabd21cc975ee97b7fb2133af0068ebb5e) {

ARENGINE_UPDATE_MODE_BLOCKING = 0,

ARENGINE_UPDATE_MODE_LATEST = 1

}

调用[HMS_AREngine_ARSession_Update](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259)方法后数据更新模式。

#### 函数

名称

描述

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchor_Detach](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6b731c00cc038f62d21ccb280067114b) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) *anchor)

通知AR Engine停止跟踪并解绑一个锚点。

 注意：

由于此函数并没有释放锚点[AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d)，开发者需要通过调用 [HMS_AREngine_ARAnchor_Release](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad04b12f9a2b0415789de5d6e1692f51c)来释放锚点。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchor_GetPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad937acfc5d49f0909bdd84677bb0731a) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) *anchor, [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

获取指定锚点在世界坐标系中的位姿信息。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchor_GetTrackingState](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6d8c173cc1ef3888f1bedfd6adb2efb3) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) *anchor, [AREngine_ARTrackingState](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382) *outTrackingState)

获取指定锚点位姿的追踪状态。

void [HMS_AREngine_ARAnchor_Release](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad04b12f9a2b0415789de5d6e1692f51c) ([AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) *anchor)

释放指定锚点对象的内存。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchorList_AcquireItem](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f520dddd96c9918163bff8b68f428fc) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAnchorList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) *anchorList, int32_t index, [AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) **outAnchor)

从锚点对象列表中获取指定位置的锚点信息。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchorList_Create](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga30492334f7a06b98ef0ad5831d33b198) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARAnchorList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) **outAnchorList)

创建一个锚点对象列表。

void [HMS_AREngine_ARAnchorList_Destroy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga5b1078469a123466245f65524c9c33be) ([AREngine_ARAnchorList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) *anchorList)

释放一个锚点对象列表。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAnchorList_GetSize](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9e96df41cdb973d7e45c714b1bd31fd1) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAnchorList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) *anchorList, int32_t *outSize)

获取锚点对象列表中包含锚点的数量。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImage_AcquireName](../../topics/media/AR Engine.md#section110712352334) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAugmentedImage](../../topics/media/AR Engine.md#section68491824155217) *augmentedImage, char *augmentedImageName, uint32_t *outNameLength)

返回跟踪图像的名称。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImage_GetCenterPose](../../topics/media/AR Engine.md#section498975343520) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAugmentedImage](../../topics/media/AR Engine.md#section68491824155217) *augmentedImage, [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

获取跟踪图像中心点在世界坐标系中的位姿信息。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImage_GetExtendX](../../topics/media/AR Engine.md#section917593011382) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAugmentedImage](../../topics/media/AR Engine.md#section68491824155217) *augmentedImage, float *outExtendX)

以图像的中心点为坐标原点，获取X轴上的估计值。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImage_GetExtendZ](../../topics/media/AR Engine.md#section9630192711390) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAugmentedImage](../../topics/media/AR Engine.md#section68491824155217) *augmentedImage, float *outExtendZ)

以图像的中心点为坐标原点，获取Z轴上的估计值。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImage_GetIndex](../../topics/media/AR Engine.md#section27041685401) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARAugmentedImage](../../topics/media/AR Engine.md#section68491824155217) *augmentedImage, uint32_t *outIndex)

获取跟踪图像数据库中跟踪图像的索引。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_AddImage](../../topics/media/AR Engine.md#section0315115618403) ([AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330) *database, const [AREngine_ARAugmentedImageSource](../../topics/graphics/AREngine_ARAugmentedImageSource.md) *image, uint32_t *outIndex, [AREngine_ARAddAugmentedImageReason](../../topics/media/AR Engine.md#section2441053595) *outReason)

将图像添加到图像数据库并输出对应图像的索引。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_Create](../../topics/media/AR Engine.md#section4108822184411) ([AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330) **outDatabase)

创建一个空的跟踪图像数据库。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_Deserialize](../../topics/media/AR Engine.md#section1619582764511) (const uint8_t *buffer, const uint64_t bufSize, [AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330) **outDatabase)

反序列化特征数据库。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_Destroy](../../topics/media/AR Engine.md#section14702121818469) ([AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330) *database)

释放图像数据库对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_GetAddMode](../../topics/media/AR Engine.md#section1731662218476) (const [AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330) *database, [AREngine_ARImageDatabaseMode](../../topics/media/AR Engine.md#section683253471219) *outAddMode)

获取添加跟踪图像模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_SetAddMode](../../topics/media/AR Engine.md#section2579104674818) (const [AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330) *database, [AREngine_ARImageDatabaseMode](../../topics/media/AR Engine.md#section683253471219) addMode)

设置添加跟踪图像模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_GetCapacity](../../topics/media/AR Engine.md#section650873916491) (const [AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330) *database, uint32_t *outCapacity)

获取可以添加的最大图像数。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_GetImageCount](../../topics/media/AR Engine.md#section6183812506) (const [AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330) *database, uint32_t *outImageCount)

获取数据库中存储的图像数量。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARAugmentedImageDatabase_Serialize](../../topics/media/AR Engine.md#section6536162875117) (const [AREngine_ARAugmentedImageDatabase](../../topics/media/AR Engine.md#section152051642330) *database, uint8_t **outBuffer, uint64_t *outBufSize)

序列化特征数据库。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetDisplayOrientedPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga088648130f3a91cdf8d7b95f5ee1faf2) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

设置outPose为虚拟相机（面向显示）在世界空间中的位姿，用以将AR内容渲染到最新帧中。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetImageIntrinsics](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8e6f32adc3bd59504042d4e18bfb3432) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ARCameraIntrinsics](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *outIntrinsics)

获取物理相机离线内参的对象，可通过该对象获取相机的焦距、图像尺寸、主轴点和畸变参数。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga00df108c4ba187967a10e9c4d2e27d3a) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

设置outPose为最新帧中物理相机在世界空间中的位姿。该位姿是OpenGL相机的位姿。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetProjectionMatrix](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga01feacf9cd393a0598e2ac5cf7b61693) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ClipPlaneDistance](../../topics/media/AREngine_ClipPlaneDistance.md) clipPlaneDistance, float *outDestColMajor4x4, int32_t destColMajor4x4Num)

获取用于在相机图像上层渲染虚拟内容的投影矩阵，可用于相机坐标系到裁剪坐标系转换。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetTrackingState](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dc931eee56ae5ea899f8acc08eb3f36) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ARTrackingState](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382) *outTrackingState)

获取相机的当前追踪状态。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetTrackingStateReason](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab5411813f2e4ac6de4ebbccfc1bbbd35) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, [AREngine_ARTrackingStateReason](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga67774b71935ef2f8a2ae5e5822c3dcdb) *outTrackingStateReason)

获取相机的当前追踪状态为[ARENGINE_TRACKING_STATE_PAUSED](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)时的原因。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCamera_GetViewMatrix](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga130b4689d7d967e812d24fc2be071d68) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera, float *outColMajor4x4, int32_t colMajor4x4Num)

获取最新帧中相机的视图矩阵。

void [HMS_AREngine_ARCamera_Release](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga16909b4002b9c6250dad88bb8397adc9) ([AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) *camera)

释放对相机的引用。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraConfig_Create](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac6402425c6c6390da3c4e57d328da443) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARCameraConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba) **outCameraConfig)

创建一个相机配置对象。

void [HMS_AREngine_ARCameraConfig_Destroy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2540153f0404799943470c41dff3b5f4) ([AREngine_ARCameraConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba) *cameraConfig)

释放相机配置对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraConfig_GetImageDimensions](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac3dc81c1c9e6945dd4a3de30e45ccc8f) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba) *cameraConfig, int32_t *outWidth, int32_t *outHeight)

从相机配置对象中获取相机送到CPU处理的图像尺寸。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraConfig_GetTextureDimensions](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga19ade172d2e2dcd67495f6be1bcc2706) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba) *cameraConfig, int32_t *outWidth, int32_t *outHeight)

从相机配置对象中获取相机送到GPU处理的图像纹理尺寸。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraIntrinsics_Create](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga027e92d8f7b25e6e577a9658545e2c2a) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARCameraIntrinsics](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) **outIntrinsics)

创建一个相机内参对象。

void [HMS_AREngine_ARCameraIntrinsics_Destroy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga09323e31d8bd08e5c1d60bccb118b68b) ([AREngine_ARCameraIntrinsics](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *intrinsics)

释放指定的相机内参对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraIntrinsics_GetDistortion](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7caab88bb0e859921004ab1121ee2b5d) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraIntrinsics](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *intrinsics, float *outDistortion, int32_t distortionNum)

获取相机的畸变系数。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraIntrinsics_GetFocalLength](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab57c6586ac4d2da1b87f1c0394ffc1b3) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraIntrinsics](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *intrinsics, float *outFocalX, float *outFocalY)

获取指定相机的焦距，焦距以像素为单位。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraIntrinsics_GetImageDimensions](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaab99bc9ba5b9b734ef11888fe2bb3f86) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraIntrinsics](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *intrinsics, int32_t *outWidth, int32_t *outHeight)

获取相机图像的尺寸，包括宽度和高度，以像素为单位。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARCameraIntrinsics_GetPrincipalPoint](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb38c1df26e1af9d993574c7f13b8f5c) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARCameraIntrinsics](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga17948eef3aa7ff7f2fa8aff6a63b4b51) *intrinsics, float *outPrincipalX, float *outPrincipalY)

获取指定相机的主轴点，主点位置以像素为单位表示。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_Create](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga97376432184fe702f2451e32b52298fb) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) **outConfig)

创建具有适当默认配置的配置对象。

void [HMS_AREngine_ARConfig_Destroy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac86d0db69e8658f2f6bd267d7b288c0a) ([AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config)

释放指定的配置对象的内存空间。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetARType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga827ca7c2c2f288338f781e87e28ef996) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga987888aea7dcaa9abcdb64581c850bf5) *type)

获取当前使用的AR能力类型。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetARType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf12b21d8591c5265f8a0e847b716d65c) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga987888aea7dcaa9abcdb64581c850bf5) type)

设置当前要使用的AR能力类型。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetCameraPreviewMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf4746b3377bd69a52d0587a582cc4679) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPreviewMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadef0f2099b106b872a014ef6551906ae) *outMode)

获取当前的预览模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetCameraPreviewMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac5e6992e38516f75cc6faf1a34047f5d) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPreviewMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadef0f2099b106b872a014ef6551906ae) mode)

设置预览模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetDepthMode](../../topics/media/AR Engine.md#section6878812194715) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARDepthMode](../../topics/media/AR Engine.md#section12321429115215) *outDepthMode)

获取当前的深度模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetDepthMode](../../topics/media/AR Engine.md#section12608229155413) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARDepthMode](../../topics/media/AR Engine.md#section12321429115215) depthMode)

设置深度模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetFocusMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae92d8207f54468354ed52ad132e172f9) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARFocusMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf50530faa0d094182a0db0c73b75d875) *focusMode)

获取当前配置的相机对焦模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetFocusMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bcf745a74196cb21dca5e4feec18325) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARFocusMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf50530faa0d094182a0db0c73b75d875) focusMode)

设置当前所需的相机对焦模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetMaxMapSize](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga65bae175f2ac6da6dca71988c3ac37df) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, uint64_t *maxMapSize)

获取地图数据使用的最大内存大小。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetMaxMapSize](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga82fd530a4377b0c0e01c9031aa238372) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, uint64_t maxMapSize)

设置地图数据最大使用内存大小。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetMeshMode](../../topics/media/AR Engine.md#section5607016063) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARMeshMode](../../topics/media/AR Engine.md#section19436658201620) *outMeshMode)

获取当前mesh模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetMeshMode](../../topics/media/AR Engine.md#section53081741287) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARMeshMode](../../topics/media/AR Engine.md#section19436658201620) meshMode)

设置mesh模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetPlaneFindingMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8aa9412802c98ece87d140b063f50839) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPlaneFindingMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab8e7db52d819359026fc4a82815d3fff) *planeFindingMode)

获取当前配置的平面识别模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetPlaneFindingMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga884a7db93778e24eef0dfaa794c45674) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPlaneFindingMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab8e7db52d819359026fc4a82815d3fff) planeFindingMode)

设置当前所需的平面识别模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetPoseMode](../../topics/media/AR Engine.md#section7289861874) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPoseMode](../../topics/media/AR Engine.md#section1249515330198) *poseMode)

获取相机输出的位姿坐标系对齐模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetPoseMode](../../topics/media/AR Engine.md#section53221628698) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPoseMode](../../topics/media/AR Engine.md#section1249515330198) poseMode)

设置相机输出的位姿坐标系对齐模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetPowerMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3c02b15907c21a20e6efcd018750a29f) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPowerMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3d925e007e2847e69f22af68ec922507) *powerMode)

获取当前配置的功耗模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetPowerMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac5048a3977d04d75ba622a0411b03774) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARPowerMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3d925e007e2847e69f22af68ec922507) powerMode)

设置功耗模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetPreviewSize](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8e9f74ef162604dc9bf07204237b45ab) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, uint32_t width, uint32_t height)

设置预览画面尺寸，仅支持宽高比为4:3，超出范围的值将自动采用默认分辨1440*1080填充。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetSemanticDenseMode](../../topics/media/AR Engine.md#section1099254315514) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARSemanticDenseMode](../../topics/media/AR Engine.md#section09971756142213) *outSemanticDenseMode)

获取已设置的高精几何重建模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetSemanticDenseMode](../../topics/media/AR Engine.md#section1569718841012) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARSemanticDenseMode](../../topics/media/AR Engine.md#section09971756142213) semanticDenseMode)

设置当前所需的高精几何重建模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetSemanticMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga61325a1e0157e477c2ff95c1c0030567) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARSemanticMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga34d3000de29454b99d89406d288d6ed5) *mode)

获取已设置成功的语义识别模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetSemanticMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae87c1ef02b6e9bab123fae2086da248) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARSemanticMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga34d3000de29454b99d89406d288d6ed5) mode)

设置当前所需的语义识别模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetUpdateMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf32a3cb1f345cd5a243683ecdec63cef) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARUpdateMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabd21cc975ee97b7fb2133af0068ebb5e) *updateMode)

获取当前配置的预览更新模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetUpdateMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga871c8aebc084cbba41220d255c46803b) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARUpdateMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabd21cc975ee97b7fb2133af0068ebb5e) updateMode)

设置预览更新模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetPhotoStreamSize](../../topics/media/AR Engine.md#section21861035164816)(const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, uint32_t width, uint32_t height)

PreviewAndPhotoMode模式下，设置从拍照流获取图像的分辨率。仅支持4:3大小分辨率。如果超出这个范围，系统会自动设置图像分辨率为该设备在4:3宽高比下的最高分辨率。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_SetImageStreamMode](../../topics/media/AR Engine.md#section10809428846)(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARImageStreamMode mode)

设置图像流模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARConfig_GetImageStreamMode](../../topics/media/AR Engine.md#section387103819713)(const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config, [AREngine_ARImageStreamMode](../../topics/media/AR Engine.md#section184201559356) *outMode)

获取图像流模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga5295c975a0ff3d633a1dde5a8eb70863) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARCamera](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7bdcf1fb36c404d36e09ad70d2545d92) **outCamera)

获取当前帧的相机参数对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireCameraImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad5619c3cbd2b9ea0cfeff22b72f8d81d) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) **outImage)

获取相机的当前帧的图像。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireCameraPhotoImage](../../topics/media/AR Engine.md#section18751333994)(const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const A[AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)*frame, [HMS_AREngine_PhotoAvailableCallback](../../topics/media/AR Engine.md#section430673420224) photoCallback)

获取当前帧的拍照流图片。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireDepthConfidenceImage](../../topics/media/AR Engine.md#section4424501286) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) **outConfidenceImage)

获取当前帧的深度置信度图像。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireDepthImage16Bits](../../topics/media/AR Engine.md#section138574584154) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) **outDepthImage);

获取当前帧的深度图像。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquirePointCloud](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga877f7fc9d9c303f1fd8efb00ec383b34) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARPointCloud](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc) **outPointCloud)

返回当前帧的点云数据。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireSceneMesh](../../topics/media/AR Engine.md#section25711548111020) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARSceneMesh](../../topics/media/AR Engine.md#section543212520614) **outSceneMesh)

获取当前帧的mesh信息。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_AcquireSemanticDenseData](../../topics/media/AR Engine.md#section17136162216547) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARSemanticDenseData](../../topics/media/AR Engine.md#section1410813229144) **outSemanticDenseData);

获取当前帧的高精几何重建对象数据。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_Create](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadfcb9589137a39c5afcb217e18853a9d) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) **outFrame)

创建一个新的[AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)对象，将指针存储到*outFrame中。

void [HMS_AREngine_ARFrame_Destroy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0ca6a470025dbccb44b4fdefc26513f6) ([AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame)

删除当前[AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719)对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_GetDisplayGeometryChanged](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4fb55932c19ef9c49523a0a5385a9242) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, int32_t *outGeometryChangeState)

获取显示（长宽和旋转）是否发生变化。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_GetTimestamp](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga266c2e5c80a961163d3422b96b079701) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, int64_t *outTimestampNs)

获取当前帧对应的时间戳信息，单位为ns。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_GetUpdatedTrackables](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0fc74148f836093108b85ab4c7ecdd1c) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, [AREngine_ARTrackableType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d) filterType, [AREngine_ARTrackableList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) *outTrackableList)

获取[HMS_AREngine_ARSession_Update](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259)更新后发生变化的指定类型的可跟踪对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_HitTest](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad9377f19261d5bbc2044497729b4e0df) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, float pixelX, float pixelY, [AREngine_ARHitResultList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3) *hitResultList)

从摄像头发射一条射线，该射线的方向由预览区上的点(pixelX，pixelY)确定(pixelX，pixelY可以通过XComponent的[DispatchTouchEvent()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback#dispatchtouchevent)事件获取)。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARFrame_TransformDisplayUvCoords](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4c7699abab9b82369c0d42b496667fc7) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *frame, int32_t elementSize, const float *uvsIn, float *uvsOut)

调整纹理映射坐标，以便可以正确地显示相机捕捉到的背景图片。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResult_AcquireNewAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga30abe7b3457c991815dd79fcfaf26018) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARHitResult](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *hitResult, [AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) **outAnchor)

在碰撞命中位置创建一个新的锚点。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResult_AcquireTrackable](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac3a02e30bb7706d87c4c29d38b363840) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARHitResult](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *hitResult, [AREngine_ARTrackable](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) **outTrackable)

获取被命中的可追踪对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResult_Create](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4b06bcca0f6fc0b081ef8210765d9c91) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARHitResult](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) **outHitResult)

创建一个空的命中检测结果对象。

void [HMS_AREngine_ARHitResult_Destroy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3b3796d7186cb09c4861ebabe2d5b654) ([AREngine_ARHitResult](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *hitResult)

释放命中检测结果对象使用的内存。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResult_GetDistance](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6929e52bb352622806d2298497c6b4c8) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARHitResult](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *hitResult, float *outDistance)

返回从相机到命中位置的距离，以m为单位。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResult_GetHitPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8beaa085410712425041e81f9bc6aa09) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARHitResult](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *hitResult, [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

获取交点的位姿。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResultList_Create](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad5dfe929e7952954764d05b8d69abace) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARHitResultList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3) **outHitResultList)

创建一个命中检测结果对象列表。

void [HMS_AREngine_ARHitResultList_Destroy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae065ef9a28168b420c96b72ca80c892) ([AREngine_ARHitResultList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3) *hitResultList)

释放命中检测结果对象列表，以及其中的所有命中检测结果对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResultList_GetItem](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf165c7a1c9ae003cac2a1c2ac2e5e5c4) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARHitResultList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3) *hitResultList, int32_t index, [AREngine_ARHitResult](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaeb304c8b21122eb7ffda7403316a3507) *outHitResult)

在命中检测结果列表中获取指定索引的命中检测结果对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARHitResultList_GetSize](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga131d081663d457c594664c977bd9033c) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARHitResultList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1f2369453412bd4d77ab8f5aa2d52bb3) *hitResultList, int32_t *outSize)

获取命中检测结果对象列表中包含的对象数。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetFormat](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga852b211c7e285ccc154295eb1c604f37) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, [AREngine_ARImageFormat](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gadfcf7a1211ed12a90f377610d0f838ac) *outFormat)

获取当前帧的图像格式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetHeight](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga34c21703e40868ce0fe5795fa82a08fa) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t *outHeight)

获取当前帧的图像数据的高度。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetWidth](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2c2454e9611dc68e26b8fefb39021597) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t *outWidth)

获取当前帧的图像数据的宽度。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetNativeBuffer](../../topics/media/AR Engine.md#section367418528228) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, [OH_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer) **outNativeBuffer);

获取当前帧图像对象的NativeBuffer数据。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetPlaneCount](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga107fbf6737b499aea941fbbfeab1b3e9) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t *outCount)

获取当前帧图像的平面数量。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetPlaneData](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaedc5247eb982443c3f8a2dc8cfd5fdee) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t planeIndex, const uint8_t **outData, int32_t *outLength)

获取当前帧图像的平面数据。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetPlanePixelStride](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac31f741115e6936f7b8e3ef94579d270) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t planeIndex, int32_t *outPixelStride)

获取图像中两个连续像素的起点之间的字节距离。像素步幅始终大于0。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetPlaneRowStride](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga35e66d4a869539d2261e41df17730691) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int32_t planeIndex, int32_t *outRowStride)

获取图像中两个连续像素行的起始位置之间的字节数。行间距始终大于0。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARImage_GetTimestamp](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7d2c7f1d596d41bfe1c181057283b740) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image, int64_t *outTimestamp)

获取图像的时间戳。

void [HMS_AREngine_ARImage_Release](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga42fd222576edf6507f6d319a3374cd94) ([AREngine_ARImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabfee13b0076f2f00b7efdef2717add59) *image)

释放当前帧的图像对象,，由[HMS_AREngine_ARFrame_AcquireCameraImage](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad5619c3cbd2b9ea0cfeff22b72f8d81d)创建的对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_AcquireSubsumedBy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga56686d6a5ff45fcb04812538aa807ac3) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) **outSubsumedBy)

获取平面的父平面（一个平面被另一个平面合并时，会产生父平面），如果无父平面返回为NULL。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetCenterPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gabbb03027afb984be8542d00d2eebd063) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

获取从平面的局部坐标系到世界坐标系转换的位姿信息。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetExtentX](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga49db45eb6072384247a057c403a69c8d) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, float *outExtentX)

获取平面的矩形边界沿平面局部坐标系X轴的长度，如矩形的宽度。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetExtentZ](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4daf6a365f1107f146c5d264dfee292c) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, float *outExtentZ)

获取平面的矩形边界沿平面局部坐标系Z轴的长度，如矩形的高度。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetLabel](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga913456f9586c82adcdbcae291ec8e17c) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, [AREngine_ARSemanticPlaneLabel](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gafbb6b69fefdc417ba6437ce2fe587cb1) *label)

获取平面的语义类型，如桌面、地板等。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetPolygon](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3537ce62e6a92dcdbddff0f39de0fae3) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, float *outPolygonXz, int32_t polygonSize)

获取检测到平面的二维顶点数组，格式为[x1，z1，x2，z2，...]。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetPolygonSize](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga98760556eee2a4a69c33699b7ce3edc6) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, int32_t *outPolygonSize)

获取检测到平面的二维顶点数组大小。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_GetType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8aa35ca398b38eee8c53bd1db8d6ab88) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, [AREngine_ARPlaneType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga895db37a92155584c5448bee30a8beab) *outPlaneType)

获取平面的类型。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_IsPoseInExtents](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8ded2552569a9e89c1befe8f15123af6) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, const [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, int32_t *outPoseInExtents)

判断位姿是否位于平面的矩形范围内。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPlane_IsPoseInPolygon](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab00d22a9c927a2745821023e8e72a8d0) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPlane](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76f9bdb23634312b8488fcbaff4aa9b5) *plane, const [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, int32_t *outPoseInPolygon)

判断位姿是否位于平面的多边形范围内。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPoint_GetOrientationMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad869ed2a4ac6409bf94c768d9d1d8127) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPoint](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6) *point, [AREngine_ARPointOrientationMode](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0e2893593f4372954fd97519e0a63855) *outOrientationMode)

获取输入点的朝向模式。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPoint_GetPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga8255eece88d8dc76c554eed360fb7c7b) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPoint](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7b6923d92487d68e77543dd223364d6) *point, [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outPose)

获取输入点的位姿信息。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPointCloud_GetData](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4061cacb3f3ce45e529acb9afbcdc5ce) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPointCloud](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc) *pointCloud, const float **outPointCloudData)

获取点云中所有点的坐标及置信度数组。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPointCloud_GetNumberOfPoints](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad9701fe82b6468f33f6741cc7f347d45) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPointCloud](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc) *pointCloud, int32_t *outNumberOfPoints)

获取点云中所有点的坐标及置信度数组大小。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPointCloud_GetTimestamp](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9e430d52fa372903bcbe40ca5f6a9d9d) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPointCloud](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc) *pointCloud, int64_t *outTimestampNs)

获取检测到当前特征点云的时间，以ns为单位。

void [HMS_AREngine_ARPointCloud_Release](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3751c56632f7f6d383cf9409ec6769bc) ([AREngine_ARPointCloud](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc054cea4851be61b160f32b433737fc) *pointCloud)

释放点云对象使用的内存。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPose_Create](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gafb471f39563ca1a4947d4f87c77e24e2) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const float *poseRaw, const uint32_t poseRawSize, [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) **outPose)

分配并初始化一个新的位姿对象。

void [HMS_AREngine_ARPose_Destroy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab988254f4654c8aaadb5740061846057) ([AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose)

释放位姿对象使用的内存。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPose_GetMatrix](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga787f4daf9efd13c79737ef18cef6d7c7) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, float *outMatrixColMajor4x4, int32_t matrixColMajor4x4Size)

将位姿数据转换成4X4的矩阵。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARPose_GetPoseRaw](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1ee66c006ffe8255cc04f2a24c277709) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, float *outPoseRaw, int32_t poseRawSize)

从位姿对象提取位姿数据。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSceneMesh_AcquireIndexList](../../topics/media/AR Engine.md#section7629354145) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSceneMesh](../../topics/media/AR Engine.md#section543212520614) *sceneMesh, int32_t *outData, int32_t dataSize)

获取mesh面片的索引集合。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSceneMesh_AcquireIndexListSize](../../topics/media/AR Engine.md#section12621161917152) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSceneMesh](../../topics/media/AR Engine.md#section543212520614) *sceneMesh, int32_t *outSize)

获取mesh面片的索引个数。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSceneMesh_AcquireVertexList](../../topics/media/AR Engine.md#section2126723166) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSceneMesh](../../topics/media/AR Engine.md#section543212520614) *sceneMesh, float *outData, int32_t dataSize)

获取mesh的顶点集合。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSceneMesh_AcquireVertexNormalList](../../topics/media/AR Engine.md#section115249588168) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSceneMesh](../../topics/media/AR Engine.md#section543212520614) *sceneMesh, float *outData, int32_t dataSize)

获取mesh面片的法向量集合。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSceneMesh_AcquireVerticesSize](../../topics/media/AR Engine.md#section1860218429179) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSceneMesh](../../topics/media/AR Engine.md#section543212520614) *sceneMesh, int32_t *outSize)

获取mesh的顶点个数。

void [HMS_AREngine_ARSceneMesh_Release](../../topics/media/AR Engine.md#section446832931813) ([AREngine_ARSceneMesh](../../topics/media/AR Engine.md#section543212520614) *SceneMesh)

释放当前帧的mesh信息。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSemanticDense_AcquireCubeData](../../topics/media/AR Engine.md#section7554459949) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSemanticDenseData](../../topics/media/AR Engine.md#section1410813229144) *semanticDenseData, [AREngine_ARSemanticDenseCubeData](../../topics/media/AREngine_ARSemanticDenseCubeData.md) **outCubeData)

获取识别到的高精几何重建对象数据中的立方体数据。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSemanticDense_AcquireCubeDataSize](../../topics/media/AR Engine.md#section383013458212) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSemanticDenseData](../../topics/media/AR Engine.md#section1410813229144) *semanticDenseData, int64_t *outSize)

获取识别到的高精几何重建对象数据中的立方体数量。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSemanticDense_AcquirePointData](../../topics/media/AR Engine.md#section288942515910) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSemanticDenseData](../../topics/media/AR Engine.md#section1410813229144) *semanticDenseData, [AREngine_ARSemanticDensePointData](../../topics/media/AREngine_ARSemanticDensePointData.md) **outPointData)

获取识别到的高精几何重建对象数据中的稠密点云数据。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSemanticDense_AcquirePointDataSize](../../topics/media/AR Engine.md#section6669112114532) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARSemanticDenseData](../../topics/media/AR Engine.md#section1410813229144) *semanticDenseData, int64_t *outSize)

获取识别到的高精几何重建对象数据中的稠密点云数量。

void [HMS_AREngine_ARSemanticDense_Release](../../topics/media/AR Engine.md#section390280482) ([AREngine_ARSemanticDenseData](../../topics/media/AR Engine.md#section1410813229144) *semanticDenseData)

释放高精几何重建对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_AcquireNewAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2ae6dee4baab7cf2c5d0cdd1c845cf0c) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, [AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) **outAnchor)

创建一个持续跟踪的锚点。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Configure](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6394ae995148abbe3d00082817bf320a) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab0b32ef6018535fd30000f4b6d65f619) *config)

配置[AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)会话。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Create](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga47713cb18234569e03b5216b6c8442d3) (void *env, void *applicationContext, [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) **outSessionPointer)

创建一个新的[AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)会话。

void [HMS_AREngine_ARSession_Destroy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3a2be9998c9cd6373ff1f5209b645a95) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session)

释放[AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)会话使用的资源。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_GetCameraConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga31b28b049ac25b94c02fb27ca56c497d) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARCameraConfig](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9b7a5a2082a4127f85a1c9a95cb9acba) *outCameraConfig)

获取相机配置信息。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_GetAllAnchors](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga4828823e5f3cc1067dbd6a2c8b9c9635) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARAnchorList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) *outAnchorList)

获取所有锚点，包括[AREngine_ARTrackingState](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382)中包含的所有状态下的锚点。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_GetAllTrackables](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac5b39338f95317671d8de6d4f409cf9c) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARTrackableType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d) filterType, [AREngine_ARTrackableList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) *outTrackableList)

获取所有指定类型的可跟踪对象集合。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Pause](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga09dedb5c633141321591db0981629de1) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session)

暂停会话，停止相机预览流，不清除平面和锚点数据，释放相机（否则其他应用无法使用相机服务）。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Resume](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7138d56b767738b8aadcbc74f4c328db) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session)

开始运行[AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)，或者在调用[HMS_AREngine_ARSession_Pause](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga09dedb5c633141321591db0981629de1)以后恢复[AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650)的运行状态。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_SetCameraGLTexture](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac697e4be36db63ed6098f154aa9ac01c) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, uint32_t textureId)

设置可用于存储相机预览流数据的OpenGL纹理。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_SetDisplayGeometry](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga3f23bf747def8303c3fb261a9e9a2286) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARPoseType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae551da7b220b8b38140c3c28882e5010) rotation, int32_t width, int32_t height)

设置显示的高和宽，以像素为单位。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Stop](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0b7405ae0fc1e1257103192a2b7b48d3) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session)

停止AR Engine，停止相机预览流，清除平面和锚点数据，并释放相机，终止本次会话。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARSession_Update](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga1d1cacf372a8011a439f0e4e76994259) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARFrame](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaf35f728a1179ef54a3eba9f1cf021719) *outFrame)

更新AR Engine的计算结果。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTarget_GetAxisAlignedBoundingBox](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaaf54fe7a3c38dbb4c0bcaa3c83dd0d76)(const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTarget](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0) *target, float *outAabb, int32_t aabbSize)

获取语义物体最小外接包围盒坐标，坐标格式为(xmin，ymin，zmin，xmax，ymax，zmax)。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTarget_GetCenterPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaa9a304640d54942be238a7ddd2c13276) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTarget](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0) *target, [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *outARPose)

获取从目标语义对象的局部坐标系到世界坐标系转换的位姿对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTarget_GetRadius](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga0fb23a8217c7191f765b0d656160ffa1) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTarget](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0) *target, float *radius)

获取语义物体的球体半径。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTarget_GetShapeType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6c702efd6c4fdc3eeb8f5dc38968ec65) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTarget](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga9af9c1d51ed065f80b373824e0425fa0) *target, [AREngine_ARTargetShapeLabel](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaed68dc13cc314da98d79c88b12d3ae49) *shape)

获取语义物体的形状类型。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackable_AcquireNewAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacf03897f0ac28d338143f3fa350c1491) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARTrackable](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) *trackable, [AREngine_ARPose](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab2fa63142ebfb09f0c2ddf88cdb86604) *pose, [AREngine_ARAnchor](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga76c16c9d68ba9a3b76f1869c60d8ca1d) **outAnchor)

通过可跟踪对象的位姿信息创建对应的锚点对象，该锚点将和当前的可跟踪对象绑定。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackable_GetAnchors](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gac7a3b98b0281f2e31ac3d9c47b0dffab) ([AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTrackable](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) *trackable, [AREngine_ARAnchorList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga516a7f0954dcfda438799aa9e7c6e872) *outAnchorList)

获取绑定到输入可跟踪对象的锚点对象列表。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackable_GetTrackingState](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7805739b2dbeae0d3b04242538a4a840) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTrackable](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) *trackable, [AREngine_ARTrackingState](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gaae57d2f58331e1033b60cdb2d506a382) *outTrackingState)

获取当前可跟踪对象的跟踪状态。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackable_GetType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga72c800291d0df799fa795db3d3485e4f) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTrackable](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) *trackable, [AREngine_ARTrackableType](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga993948a19fd2bdfa5b946e13a8d4fe3d) *outTrackableType)

获取可跟踪对象的类型。

void [HMS_AREngine_ARTrackable_Release](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga6ec735cd18e955442f29416ff58ddd64) ([AREngine_ARTrackable](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) *trackable)

释放可跟踪对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackableList_AcquireItem](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gab1782eeeeddc01b77a140af915cb351c) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTrackableList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) *trackableList, int32_t index, [AREngine_ARTrackable](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga54808ebd1a6ed026494acdd945c4f970) **outTrackable)

从可跟踪列表中获取指定index的对象。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackableList_Create](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga7860d63545ab862e9f3b1fe0a8a83d42) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, [AREngine_ARTrackableList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) **outTrackableList)

创建一个可跟踪对象列表。

void [HMS_AREngine_ARTrackableList_Destroy](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad6e2ffd71d7cdaa3ae553937437b37c8) ([AREngine_ARTrackableList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) *trackableList)

释放可跟踪对象列表，以及它持有的所有锚点引用。

[AREngine_ARStatus](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gacc90fb9320a5ba10bb23f7a37440885d)[HMS_AREngine_ARTrackableList_GetSize](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gad9729d4436f3d969286f31b33d07513e) (const [AREngine_ARSession](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__ga2dbf3585f50628750ec855501c043650) *session, const [AREngine_ARTrackableList](../../topics/media/AR Engine.md#ZH-CN_TOPIC_0000002500306234__gae69e4963b595036fc5e6119a055bb205) *trackableList, int32_t *outSize)

获取此列表中的可跟踪对象的数量。