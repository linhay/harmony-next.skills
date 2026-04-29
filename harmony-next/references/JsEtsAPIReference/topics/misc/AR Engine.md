# AR Engine

**概述**

本模块提供AR Engine（AR引擎服务）的AR增强现实能力相关接口。AR Engine的基础核心能力包含：环境识别与运动跟踪能力、图像识别与跟踪能力、人脸识别与跟踪能力和人体骨骼识别与跟踪能力。

起始版本： 5.0.0(12)

**汇总**

**文件**

| 名称 | 描述 |
| --- | --- |
| ar_engine_core.h | 本声明用于访问AR Engine（AR引擎服务）的API。提供AR（增强现实）能力的相关接口。AR的基础核心能力包含：环境识别与运动跟踪能力、图像识别与跟踪能力、人脸识别与跟踪能力和人体骨骼识别与跟踪能力。 |

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct AREngine_ARAugmentedImageSource | 图像数据。 |
| struct AREngine_ClipPlaneDistance | 裁剪平面距离数据。 |
| struct AREngine_ARSemanticDensePointData | 高精几何重建对象的稠密点云数据。 |
| struct AREngine_ARSemanticDenseCubeData | 高精几何重建对象的立方体数据。 |

**宏定义**

| 名称 | 描述 |
| --- | --- |
| ARENGINE_AABB_POINT_SIZE = 6 | 包围盒坐标集数组大小。 |
| ARENGINE_DISTORTION_COUNT = 5 | 相机畸变参数的个数。 |
| ARENGINE_POSE_RAW_SIZE = 7 | 位姿数据数组大小。 |
| ARENGINE_VIEW_MATRIX_SIZE = 16 | 变换矩阵数组大小。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct AREngine_ARAnchor AREngine_ARAnchor | 锚点对象。 |
| typedef struct AREngine_ARAnchorList AREngine_ARAnchorList | 锚点对象列表。 |
| typedef struct AREngine_ARAugmentedImage AREngine_ARAugmentedImage | 跟踪图像对象。 |
| typedef struct AREngine_ARAugmentedImageDatabase AREngine_ARAugmentedImageDatabase | 跟踪图像数据库对象。 |
| typedef struct AREngine_ARCamera AREngine_ARCamera | 当前帧对应的相机信息。 |
| typedef struct AREngine_ARCameraConfig AREngine_ARCameraConfig | 相机的配置信息。 |
| typedef struct AREngine_ARCameraIntrinsics AREngine_ARCameraIntrinsics | 相机内参。 |
| typedef struct AREngine_ARConfig AREngine_ARConfig | 用于配置AREngine_ARSession的能力项（使用哪些能力、模式等）。 |
| typedef struct AREngine_ARFace AREngine_ARFace | 跟踪的人脸对象。 |
| typedef struct AREngine_ARFaceGeometry AREngine_ARFaceGeometry | 人脸拓扑结构对象。 |
| typedef struct AREngine_ARFaceBlendShapes AREngine_ARFaceBlendShapes | 人脸微表情对象。 |
| typedef struct AREngine_ARFrame AREngine_ARFrame | AR Engine处理的一帧数据。 |
| typedef struct AREngine_ARHitResult AREngine_ARHitResult | 命中检测结果对象。 |
| typedef struct AREngine_ARHitResultList AREngine_ARHitResultList | 命中检测结果列表。 |
| typedef struct AREngine_ARImage AREngine_ARImage | 相机视频流帧对象。 |
| typedef struct AREngine_ARPlane AREngine_ARPlane | 平面对象。 |
| typedef struct AREngine_ARPoint AREngine_ARPoint | 点对象。 |
| typedef struct AREngine_ARPointCloud AREngine_ARPointCloud | 可跟踪的3D点云的集合。 |
| typedef struct AREngine_ARPose AREngine_ARPose | 位姿对象。 |
| typedef struct AREngine_ARSceneMesh AREngine_ARSceneMesh | 环境mesh数据的集合。 |
| typedef struct AREngine_ARSemanticDenseData AREngine_ARSemanticDenseData | 表示高精几何重建对象数据的集合。 |
| typedef struct AREngine_ARSession AREngine_ARSession | 管理AR Engine的系统状态。 |
| typedef struct AREngine_ARTarget AREngine_ARTarget | 物体对象。 |
| typedef struct AREngine_ARTrackable AREngine_ARTrackable | 可跟踪对象，如点、平面等。 |
| typedef struct AREngine_ARTrackableList AREngine_ARTrackableList | 可跟踪对象列表。 |
| typedef void (*HMS_AREngine_PhotoAvailableCallback(OH_NativeBuffer *photoBuffer) | 输出拍照流图像回调。 |
| typedef struct AREngine_ARBody AREngine_ARBody | 人体对象。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| AREngine_FeatureType { ARENGINE_FEATURE_TYPE_SLAM = 0, ARENGINE_FEATURE_TYPE_DEPTH = 1, ARENGINE_FEATURE_TYPE_MESH = 2, ARENGINE_FEATURE_TYPE_IMAGE = 3, ARENGINE_FEATURE_TYPE_SEMANTIC_DENSE = 4, ARENGINE_FEATURE_TYPE_SEMANTIC = 5, ARENGINE_FEATURE_TYPE_FACE = 6, ARENGINE_FEATURE_TYPE_BODY = 7 } | AR特性类别。 |
| AREngine_ARAddAugmentedImageReason { ARENGINE_ADD_AUGMENTED_IMAGE_REASON_NONE = 0, ARENGINE_ADD_AUGMENTED_IMAGE_REASON_SIZE_NOT_MATCH = 1, ARENGINE_ADD_AUGMENTED_IMAGE_REASON_LIGHT_ANOMALY = 2, ARENGINE_ADD_AUGMENTED_IMAGE_REASON_FEATURE_LIMIT = 3, ARENGINE_ADD_AUGMENTED_IMAGE_REASON_OTHER = 4 } | 跟踪失败的可能原因。 |
| AREngine_ARAnimojiBlendShape { ARENGINE_ARANIMOJI_EYE_BLINK_LEFT = 0, ARENGINE_ARANIMOJI_EYE_LOOK_DOWN_LEFT = 1, ARENGINE_ARANIMOJI_EYE_LOOK_IN_LEFT = 2, ARENGINE_ARANIMOJI_EYE_LOOK_OUT_LEFT = 3, ARENGINE_ARANIMOJI_EYE_LOOK_UP_LEFT = 4, ARENGINE_ARANIMOJI_EYE_SQUINT_LEFT = 5, ARENGINE_ARANIMOJI_EYE_WIDE_LEFT = 6, ARENGINE_ARANIMOJI_EYE_BLINK_RIGHT = 7, ARENGINE_ARANIMOJI_EYE_LOOK_DOWN_RIGHT = 8, ARENGINE_ARANIMOJI_EYE_LOOK_IN_RIGHT = 9, ARENGINE_ARANIMOJI_EYE_LOOK_OUT_RIGHT = 10, ARENGINE_ARANIMOJI_EYE_LOOK_UP_RIGHT = 11, ARENGINE_ARANIMOJI_EYE_SQUINT_RIGHT = 12, ARENGINE_ARANIMOJI_EYE_WIDE_RIGHT = 13, ARENGINE_ARANIMOJI_JAW_FORWARD = 14, ARENGINE_ARANIMOJI_JAW_LEFT = 15, ARENGINE_ARANIMOJI_JAW_RIGHT = 16, ARENGINE_ARANIMOJI_JAW_OPEN = 17, ARENGINE_ARANIMOJI_MOUTH_FUNNEL = 18, ARENGINE_ARANIMOJI_MOUTH_PUCKER = 19, ARENGINE_ARANIMOJI_MOUTH_LEFT = 20, ARENGINE_ARANIMOJI_MOUTH_RIGHT = 21, ARENGINE_ARANIMOJI_MOUTH_SMILE_LEFT = 22, ARENGINE_ARANIMOJI_MOUTH_SMILE_RIGHT = 23, ARENGINE_ARANIMOJI_MOUTH_FROWN_LEFT = 24, ARENGINE_ARANIMOJI_MOUTH_FROWN_RIGHT = 25, ARENGINE_ARANIMOJI_MOUTH_DIMPLE_LEFT = 26, ARENGINE_ARANIMOJI_MOUTH_DIMPLE_RIGHT = 27, ARENGINE_ARANIMOJI_MOUTH_STRETCH_LEFT = 28, ARENGINE_ARANIMOJI_MOUTH_STRETCH_RIGHT = 29, ARENGINE_ARANIMOJI_MOUTH_ROLL_LOWER = 30, ARENGINE_ARANIMOJI_MOUTH_ROLL_UPPER = 31, ARENGINE_ARANIMOJI_MOUTH_SHRUG_LOWER = 32, ARENGINE_ARANIMOJI_MOUTH_SHRUG_UPPER = 33, ARENGINE_ARANIMOJI_MOUTH_UPPER_UP = 34, ARENGINE_ARANIMOJI_MOUTH_LOWER_DOWN = 35, ARENGINE_ARANIMOJI_MOUTH_LOWER_OUT = 36, ARENGINE_ARANIMOJI_BROW_DOWN_LEFT = 37, ARENGINE_ARANIMOJI_BROW_DOWN_RIGHT = 38, ARENGINE_ARANIMOJI_BROW_INNER_UP = 39, ARENGINE_ARANIMOJI_BROW_OUTER_UP_LEFT = 40, ARENGINE_ARANIMOJI_BROW_OUTER_UP_RIGHT = 41, ARENGINE_ARANIMOJI_CHEEK_PUFF = 42, ARENGINE_ARANIMOJI_CHEEK_SQUINT_LEFT = 43, ARENGINE_ARANIMOJI_CHEEK_SQUINT_RIGHT = 44, ARENGINE_ARANIMOJI_FROWN_NOSE_MOUTH_UP = 45, ARENGINE_ARANIMOJI_TONGUE_IN = 46, ARENGINE_ARANIMOJI_TONGUE_OUT_SLIGHT = 47, ARENGINE_ARANIMOJI_TONGUE_LEFT = 48, ARENGINE_ARANIMOJI_TONGUE_RIGHT = 49, ARENGINE_ARANIMOJI_TONGUE_UP = 50, ARENGINE_ARANIMOJI_TONGUE_DOWN = 51, ARENGINE_ARANIMOJI_TONGUE_LEFT_UP = 52, ARENGINE_ARANIMOJI_TONGUE_LEFT_DOWN = 53, ARENGINE_ARANIMOJI_TONGUE_RIGHT_UP = 54, ARENGINE_ARANIMOJI_TONGUE_RIGHT_DOWN = 55, ARENGINE_ARANIMOJI_LEFT_EYEBALL_LEFT = 56, ARENGINE_ARANIMOJI_LEFT_EYEBALL_RIGHT = 57, ARENGINE_ARANIMOJI_LEFT_EYEBALL_UP = 58, ARENGINE_ARANIMOJI_LEFT_EYEBALL_DOWN = 59, ARENGINE_ARANIMOJI_RIGHT_EYEBALL_LEFT = 60, ARENGINE_ARANIMOJI_RIGHT_EYEBALL_RIGHT = 61, ARENGINE_ARANIMOJI_RIGHT_EYEBALL_UP = 62, ARENGINE_ARANIMOJI_RIGHT_EYEBALL_DOWN = 63 } | 微表情类型。 |
| AREngine_ARAnimojiTriangleLabel { ARENGINE_TRIANGLE_LABEL_NON_FACE = -1, ARENGINE_TRIANGLE_LABEL_FACE_OTHER = 0, ARENGINE_TRIANGLE_LABEL_LOWER_LIP = 1, ARENGINE_TRIANGLE_LABEL_UPPER_LIP = 2, ARENGINE_TRIANGLE_LABEL_LEFT_EYE = 3, ARENGINE_TRIANGLE_LABEL_RIGHT_EYE = 4, ARENGINE_TRIANGLE_LABEL_LEFT_BROW = 5, ARENGINE_TRIANGLE_LABEL_RIGHT_BROW = 6, ARENGINE_TRIANGLE_LABEL_BROW_CENTER = 7, ARENGINE_TRIANGLE_LABEL_NOSE = 8 } | 人脸三角形面片标签。 |
| AREngine_ARCameraLensFacing { ARENGINE_CAMERA_FACING_REAR = 0, ARENGINE_CAMERA_FACING_FRONT = 1 } | 配置摄像机镜头的朝向。 |
| AREngine_ARConfidenceLevel { ARENGINE_DEPTH_CONFIDENCE_LOW = 0, ARENGINE_DEPTH_CONFIDENCE_MEDIUM = 1, ARENGINE_DEPTH_CONFIDENCE_HIGH = 2 } | 深度置信度。 |
| AREngine_ARDepthMode { ARENGINE_DEPTH_MODE_DISABLED = 0, ARENGINE_DEPTH_MODE_AUTOMATIC = 1 } | 深度模式。 |
| AREngine_ARFocusMode { ARENGINE_FOCUS_MODE_FIXED = 0, ARENGINE_FOCUS_MODE_AUTO = 1 } | 对焦模式。 |
| AREngine_ARImageDatabaseMode { ARENGINE_ADD_NORMAL = 0, ARENGINE_ADD_AUTO = 1 } | 用于跟踪的特征库图像添加方式。 |
| AREngine_ARImageFormat { ARENGINE_IMAGE_UNKNOWN = 0, ARENGINE_IMAGE_YUV_420_888 = 2, ARENGINE_IMAGE_Y_8 = 3, ARENGINE_IMAGE_Y_16 = 4 } | 图像数据格式。 |
| AREngine_ARImageStreamMode { ARENGINE_IMAGE_STREAM_MODE_PREVIEW = 0, ARENGINE_IMAGE_STREAM_MODE_PREVIEW_AND_PHOTO = 1 } | 设置图片数据流模式，默认情况下系统设置为ARENGINE_IMAGE_STREAM_MODE_PREVIEW。 |
| AREngine_ARMeshMode { ARENGINE_MESH_MODE_DISABLED = 0, ARENGINE_MESH_MODE_ENABLE=1 } | Mesh启用模式。 |
| AREngine_ARMultiFaceMode { ARENGINE_MULTIFACE_DISABLE = 0x300, ARENGINE_MULTIFACE_ENABLE = 0x800 } | 多人脸检测模式。 |
| AREngine_ARPlaneFindingMode { ARENGINE_PLANE_FINDING_MODE_DISABLED = 0, ARENGINE_PLANE_FINDING_MODE_HORIZONTAL = 1, ARENGINE_PLANE_FINDING_MODE_VERTICAL = 2, ARENGINE_PLANE_FINDING_MODE_HORIZONTAL_AND_VERTICAL = 3 } | 平面搜索模式。 |
| AREngine_ARPlaneType { ARENGINE_PLANE_FACING_HORIZONTAL_UPWARD = 0, ARENGINE_PLANE_FACING_HORIZONTAL_DOWNWARD = 1, ARENGINE_PLANE_FACING_VERTICAL = 2, ARENGINE_PLANE_FACING_INVALID = 3 } | 平面类型。 |
| AREngine_ARPointOrientationMode { ARENGINE_POINT_ORIENTATION_INITIALIZED_TO_IDENTITY = 0, ARENGINE_POINT_ORIENTATION_ESTIMATED_SURFACE_NORMAL = 1 } | 朝向模式。 |
| AREngine_ARPoseMode { ARENGINE_POSE_MODE_GRAVITY = 0, ARENGINE_POSE_MODE_GRAVITY_HEADING = 1 } | AR Engine输出的相机位姿对齐格式。 |
| AREngine_ARPoseType { ARENGINE_POSE_TYPE_IDENTITY = 0, ARENGINE_POSE_TYPE_ROTATE_90 = 1, ARENGINE_POSE_TYPE_ROTATE_180 = 2, ARENGINE_POSE_TYPE_ROTATE_270 = 3 } | 位姿类型。 |
| AREngine_ARPowerMode { ARENGINE_POWER_MODE_NORMAL = 0, ARENGINE_POWER_MODE_POWER_SAVING = 1, ARENGINE_POWER_MODE_PERFORMANCE_FIRST = 2, ARENGINE_POWER_MODE_BOOST = 3 , ARENGINE_POWER_MODE_ULTRA_POWER_SAVING = 11 } | 电源功耗模式。 |
| AREngine_ARPreviewMode { ARENGINE_PREVIEW_MODE_ENABLED = 0, ARENGINE_PREVIEW_MODE_DISABLED = 1 } | 预览模式。 |
| AREngine_ARSemanticDenseMode { ARENGINE_SEMANTIC_DENSE_MODE_DISABLED = 0, ARENGINE_SEMANTIC_DENSE_MODE_NORMAL = 1, ARENGINE_SEMANTIC_DENSE_MODE_CUBE_VOLUME = 2, ARENGINE_SEMANTIC_DENSE_MODE_CUBE_SPACE = 3 } | 高精几何重建识别模式。 |
| AREngine_ARSemanticMode { ARENGINE_SEMANTIC_MODE_NONE = 0, ARENGINE_SEMANTIC_MODE_PLANE = 1, ARENGINE_SEMANTIC_MODE_TARGET = 2 } | 语义模式。 |
| AREngine_ARSemanticPlaneLabel { ARENGINE_PLANE_UNKNOWN = 0, ARENGINE_PLANE_WALL = 1, ARENGINE_PLANE_FLOOR = 2, ARENGINE_PLANE_SEAT = 3, ARENGINE_PLANE_TABLE = 4, ARENGINE_PLANE_CEILING = 5, ARENGINE_PLANE_DOOR = 6, ARENGINE_PLANE_WINDOW = 7, ARENGINE_PLANE_BED = 8, ARENGINE_PLANE_SPACE = 9, ARENGINE_CUBE_VOLUME = 10, ARENGINE_CUBE_SPACE = 11 } | 当前平面识别到的语义类型。 |
| AREngine_ARStatus { ARENGINE_SUCCESS = 0, ARENGINE_ERROR_PERMISSION_NOT_GRANTED = 201, ARENGINE_ERROR_INVALID_ARGUMENT = 401, ARENGINE_ERROR_DEVICE_NOT_SUPPORTED = 801, ARENGINE_ERROR_FATAL = 1009200001, ARENGINE_ERROR_SESSION_PAUSED = 1009200002, ARENGINE_ERROR_SESSION_NOT_PAUSED = 1009200003, ARENGINE_ERROR_NOT_TRACKING = 1009200004, ARENGINE_ERROR_TEXTURE_NOT_SET = 1009200005, ARENGINE_ERROR_MISSING_GL_CONTEXT = 1009200006, ARENGINE_ERROR_UNSUPPORTED_CONFIGURATION = 1009200007, ARENGINE_ERROR_RESOURCE_EXHAUSTED = 1009200008, ARENGINE_ERROR_NOT_AVAILABLE = 1009200009, ARENGINE_ERROR_CAMERA_NOT_AVAILABLE = 1009200010, ARENGINE_ERROR_IMAGE_EXCEED_NUM_LIMIT = 1009200011, ARENGINE_ERROR_IMAGE_INSUFFICIENT_QUALITY = 1009200012, ARENGINE_ERROR_IMAGE_INVALID_DATABASE = 1009200013, ARENGINE_ERROR_IMAGE_ADD_IMAGE_TRACKING_STATE = 1009200014, ARENGINE_ERROR_NATIVEBUFFER_CREATE_FAILED = 1009200015, ARENGINE_ERROR_NATIVEBUFFER_WRITE_FAILED = 1009200016, ARENGINE_CAMERA_SERVICE_FATAL_ERROR = 1009200017 } | 接口返回错误码。 |
| AREngine_ARTargetShapeLabel { ARENGINE_TARGET_SHAPE_UNKNOWN = 0, ARENGINE_TARGET_SHAPE_CUBE = 1, ARENGINE_TARGET_SHAPE_CIRCLE = 2, ARENGINE_TARGET_SHAPE_RECTANGLE = 3 } | 识别到的物体形状。 |
| AREngine_ARTrackableType { ARENGINE_TRACKABLE_BASE = 0x41520100, ARENGINE_TRACKABLE_PLANE = 0x41520101, ARENGINE_TRACKABLE_POINT = 0x41520102, ARENGINE_TRACKABLE_AUGMENTED_IMAGE = 0x41520104, ARENGINE_TRACKABLE_BODY = 0x50000001, ARENGINE_TRACKABLE_FACE = 0x50000002, ARENGINE_TRACKABLE_TARGET = 0x50000008, ARENGINE_TRACKABLE_INVALID = 0 } | 可跟踪对象类型，如平面、点等。 |
| AREngine_ARTrackingState { ARENGINE_TRACKING_STATE_TRACKING = 0, ARENGINE_TRACKING_STATE_PAUSED = 1, ARENGINE_TRACKING_STATE_STOPPED = 2 } | 可跟踪对象的跟踪状态。 |
| AREngine_ARTrackingStateReason { ARENGINE_TRACKING_STATE_REASON_NONE = 0, ARENGINE_TRACKING_STATE_REASON_EXCESSIVE_MOTION = 1, ARENGINE_TRACKING_STATE_REASON_INSUFFICIENT_FEATURES = 2 } | 可能的跟踪失败原因。 |
| AREngine_ARType { ARENGINE_TYPE_WORLD = 0x01, ARENGINE_TYPE_BODY = 0x02, ARENGINE_TYPE_FACE = 0x10, ARENGINE_TYPE_IMAGE = 0x80 } | AR能力类型。 |
| AREngine_ARUpdateMode { ARENGINE_UPDATE_MODE_BLOCKING = 0, ARENGINE_UPDATE_MODE_LATEST = 1 } | 调用HMS_AREngine_ARSession_Update方法后数据更新模式。 |
| AREngine_ARBodySkeletonType { ARENGINE_ARBODY_SKELETON_NECK = 1, ARENGINE_ARBODY_SKELETON_R_SHO = 2, ARENGINE_ARBODY_SKELETON_R_ELBOW = 3, ARENGINE_ARBODY_SKELETON_R_WRIST = 4, ARENGINE_ARBODY_SKELETON_L_SHO = 5, ARENGINE_ARBODY_SKELETON_L_ELBOW = 6, ARENGINE_ARBODY_SKELETON_L_WRIST = 7, ARENGINE_ARBODY_SKELETON_R_HIP = 8, ARENGINE_ARBODY_SKELETON_R_KNEE = 9, ARENGINE_ARBODY_SKELETON_R_ANKLE = 10, ARENGINE_ARBODY_SKELETON_L_HIP = 11, ARENGINE_ARBODY_SKELETON_L_KNEE = 12, ARENGINE_ARBODY_SKELETON_L_ANKLE = 13, ARENGINE_ARBODY_SKELETON_HIP_MID = 14, ARENGINE_ARBODY_SKELETON_R_EAR = 15, ARENGINE_ARBODY_SKELETON_R_EYE = 16, ARENGINE_ARBODY_SKELETON_NOSE = 17, ARENGINE_ARBODY_SKELETON_L_EYE = 18, ARENGINE_ARBODY_SKELETON_L_EAR = 19, ARENGINE_ARBODY_SKELETON_SPINE = 20 } | 骨骼点类型。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| AREngine_ARStatus HMS_AREngine_CheckSupported (AREngine_FeatureType type) | 判断当前设备支不支持AR特性的使用。 说明： 在进行正式开发前，可通过此接口来判断AR特性是否能够正常运行在当前设备。 |
| AREngine_ARStatus HMS_AREngine_ARAnchor_Detach (AREngine_ARSession *session, AREngine_ARAnchor *anchor) | 通知AR Engine停止跟踪并解绑一个锚点。 说明： 由于此函数并没有释放锚点AREngine_ARAnchor，开发者需要通过调用 HMS_AREngine_ARAnchor_Release来释放锚点。 |
| AREngine_ARStatus HMS_AREngine_ARAnchor_GetPose (const AREngine_ARSession *session, const AREngine_ARAnchor *anchor, AREngine_ARPose *outPose) | 获取指定锚点在世界坐标系中的位姿信息。 |
| AREngine_ARStatus HMS_AREngine_ARAnchor_GetTrackingState (const AREngine_ARSession *session, const AREngine_ARAnchor *anchor, AREngine_ARTrackingState *outTrackingState) | 获取指定锚点位姿的追踪状态。 |
| void HMS_AREngine_ARAnchor_Release (AREngine_ARAnchor *anchor) | 释放指定锚点对象的内存。 |
| AREngine_ARStatus HMS_AREngine_ARAnchorList_AcquireItem (const AREngine_ARSession *session, const AREngine_ARAnchorList *anchorList, int32_t index, AREngine_ARAnchor **outAnchor) | 从锚点对象列表中获取指定位置的锚点信息。 |
| AREngine_ARStatus HMS_AREngine_ARAnchorList_Create (const AREngine_ARSession *session, AREngine_ARAnchorList **outAnchorList) | 创建一个锚点对象列表。 |
| void HMS_AREngine_ARAnchorList_Destroy (AREngine_ARAnchorList *anchorList) | 释放一个锚点对象列表。 |
| AREngine_ARStatus HMS_AREngine_ARAnchorList_GetSize (const AREngine_ARSession *session, const AREngine_ARAnchorList *anchorList, int32_t *outSize) | 获取锚点对象列表中包含锚点的数量。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImage_AcquireName (const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, char *augmentedImageName, uint32_t *outNameLength) | 返回跟踪图像的名称。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetCenterPose (const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, AREngine_ARPose *outPose) | 获取跟踪图像中心点在世界坐标系中的位姿信息。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetExtendX (const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, float *outExtendX) | 以图像的中心点为坐标原点，获取X轴上的估计值。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetExtendZ (const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, float *outExtendZ) | 以图像的中心点为坐标原点，获取Z轴上的估计值。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetIndex (const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, uint32_t *outIndex) | 获取跟踪图像数据库中跟踪图像的索引。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_AddImage (AREngine_ARAugmentedImageDatabase *database, const AREngine_ARAugmentedImageSource *image, uint32_t *outIndex, AREngine_ARAddAugmentedImageReason *outReason) | 将图像添加到图像数据库并输出对应图像的索引。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Create (AREngine_ARAugmentedImageDatabase **outDatabase) | 创建一个空的跟踪图像数据库。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Deserialize (const uint8_t *buffer, const uint64_t bufSize, AREngine_ARAugmentedImageDatabase **outDatabase) | 反序列化特征数据库。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Destroy (AREngine_ARAugmentedImageDatabase *database) | 释放图像数据库对象。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetAddMode (const AREngine_ARAugmentedImageDatabase *database, AREngine_ARImageDatabaseMode *outAddMode) | 获取添加跟踪图像模式。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_SetAddMode (const AREngine_ARAugmentedImageDatabase *database, AREngine_ARImageDatabaseMode addMode) | 设置添加跟踪图像模式。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetCapacity (const AREngine_ARAugmentedImageDatabase *database, uint32_t *outCapacity) | 获取可以添加的最大图像数。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetImageCount (const AREngine_ARAugmentedImageDatabase *database, uint32_t *outImageCount) | 获取数据库中存储的图像数量。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Serialize (const AREngine_ARAugmentedImageDatabase *database, uint8_t **outBuffer, uint64_t *outBufSize) | 序列化特征数据库。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetDisplayOrientedPose (const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARPose *outPose) | 设置outPose为虚拟相机（面向显示）在世界空间中的位姿，用以将AR内容渲染到最新帧中。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetImageIntrinsics (const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARCameraIntrinsics *outIntrinsics) | 获取物理相机离线内参的对象，可通过该对象获取相机的焦距、图像尺寸、主轴点和畸变参数。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetPose (const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARPose *outPose) | 设置outPose为最新帧中物理相机在世界空间中的位姿。该位姿是OpenGL相机的位姿。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetProjectionMatrix (const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ClipPlaneDistance clipPlaneDistance, float *outDestColMajor4x4, int32_t destColMajor4x4Num) | 获取用于在相机图像上层渲染虚拟内容的投影矩阵，可用于相机坐标系到裁剪坐标系转换。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetTrackingState (const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARTrackingState *outTrackingState) | 获取相机的当前追踪状态。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetTrackingStateReason (const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARTrackingStateReason *outTrackingStateReason) | 获取相机的当前追踪状态为ARENGINE_TRACKING_STATE_PAUSED时的原因。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetViewMatrix (const AREngine_ARSession *session, const AREngine_ARCamera *camera, float *outColMajor4x4, int32_t colMajor4x4Num) | 获取最新帧中相机的视图矩阵。 |
| void HMS_AREngine_ARCamera_Release (AREngine_ARCamera *camera) | 释放对相机的引用。 |
| AREngine_ARStatus HMS_AREngine_ARCameraConfig_Create (const AREngine_ARSession *session, AREngine_ARCameraConfig **outCameraConfig) | 创建一个相机配置对象。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetCameraLensFacing(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARCameraLensFacing *outFacing) | 获取相机镜头朝向。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetMultiFaceMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMultiFaceMode *outFaceMode) | 获取多人脸检测模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetCameraLensFacing(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARCameraLensFacing facing) | 设置相机镜头朝向，参见AREngine_ARCameraLensFacing。facing设置为ARENGINE_CAMERA_FACING_FRONT时，需要调用HMS_AREngine_ARConfig_SetARType将AR能力类型设置为ARENGINE_TYPE_FACE或ARENGINE_TYPE_BODY才生效。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetMultiFaceMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMultiFaceMode faceMode) | 设置多人脸检测模式。 |
| void HMS_AREngine_ARCameraConfig_Destroy (AREngine_ARCameraConfig *cameraConfig) | 释放相机配置对象。 |
| AREngine_ARStatus HMS_AREngine_ARCameraConfig_GetImageDimensions (const AREngine_ARSession *session, const AREngine_ARCameraConfig *cameraConfig, int32_t *outWidth, int32_t *outHeight) | 从相机配置对象中获取相机送到CPU处理的图像尺寸。 |
| AREngine_ARStatus HMS_AREngine_ARCameraConfig_GetTextureDimensions (const AREngine_ARSession *session, const AREngine_ARCameraConfig *cameraConfig, int32_t *outWidth, int32_t *outHeight) | 从相机配置对象中获取相机送到GPU处理的图像纹理尺寸。 |
| AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_Create (const AREngine_ARSession *session, AREngine_ARCameraIntrinsics **outIntrinsics) | 创建一个相机内参对象。 |
| void HMS_AREngine_ARCameraIntrinsics_Destroy (AREngine_ARCameraIntrinsics *intrinsics) | 释放指定的相机内参对象。 |
| AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetDistortion (const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outDistortion, int32_t distortionNum) | 获取相机的畸变系数。 |
| AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetFocalLength (const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outFocalX, float *outFocalY) | 获取指定相机的焦距，焦距以像素为单位。 |
| AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetImageDimensions (const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, int32_t *outWidth, int32_t *outHeight) | 获取相机图像的尺寸，包括宽度和高度，以像素为单位。 |
| AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetPrincipalPoint (const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outPrincipalX, float *outPrincipalY) | 获取指定相机的主轴点，主点位置以像素为单位表示。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_Create (const AREngine_ARSession *session, AREngine_ARConfig **outConfig) | 创建具有适当默认配置的配置对象。 |
| void HMS_AREngine_ARConfig_Destroy (AREngine_ARConfig *config) | 释放指定的配置对象的内存空间。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetARType (const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARType *type) | 获取当前使用的AR能力类型。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetARType (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARType type) | 设置当前要使用的AR能力类型。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetCameraPreviewMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPreviewMode *outMode) | 获取当前的预览模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetCameraPreviewMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPreviewMode mode) | 设置预览模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetDepthMode (const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARDepthMode *outDepthMode) | 获取当前的深度模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetDepthMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARDepthMode depthMode) | 设置深度模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetFocusMode (const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARFocusMode *focusMode) | 获取当前配置的相机对焦模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetFocusMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARFocusMode focusMode) | 设置当前所需的相机对焦模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetMaxMapSize (const AREngine_ARSession *session, const AREngine_ARConfig *config, uint64_t *maxMapSize) | 获取地图数据使用的最大内存大小。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetMaxMapSize (const AREngine_ARSession *session, AREngine_ARConfig *config, uint64_t maxMapSize) | 设置地图数据最大使用内存大小。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetMeshMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARMeshMode *outMeshMode) | 获取当前mesh模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetMeshMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARMeshMode meshMode) | 设置mesh模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetPlaneFindingMode (const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPlaneFindingMode *planeFindingMode) | 获取当前配置的平面识别模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetPlaneFindingMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPlaneFindingMode planeFindingMode) | 设置当前所需的平面识别模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetPoseMode (const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPoseMode *poseMode) | 获取相机输出的位姿坐标系对齐模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetPoseMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPoseMode poseMode) | 设置相机输出的位姿坐标系对齐模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetPowerMode (const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPowerMode *powerMode) | 获取当前配置的功耗模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetPowerMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPowerMode powerMode) | 设置功耗模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetPreviewSize (const AREngine_ARSession *session, AREngine_ARConfig *config, uint32_t width, uint32_t height) | 设置预览画面尺寸。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetSemanticDenseMode (const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARSemanticDenseMode *outSemanticDenseMode) | 获取已设置的高精几何重建模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetSemanticDenseMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARSemanticDenseMode semanticDenseMode) | 设置当前所需的高精几何重建模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetSemanticMode (const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARSemanticMode *mode) | 获取已设置成功的语义识别模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetSemanticMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARSemanticMode mode) | 设置当前所需的语义识别模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetUpdateMode (const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARUpdateMode *updateMode) | 获取当前配置的预览更新模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetUpdateMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARUpdateMode updateMode) | 设置预览更新模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetPhotoStreamSize (const AREngine_ARSession *session, AREngine_ARConfig *config, uint32_t width, uint32_t height) | 当AREngine_ARImageStreamMode为ARENGINE_IMAGE_STREAM_MODE_PREVIEW_AND_PHOTO时，设置从拍照流获取图像的分辨率。仅支持4:3大小分辨率。如果超出这个范围，系统会自动设置图像分辨率为该设备在4:3宽高比下的最高分辨率。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetImageStreamMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARImageStreamMode mode) | 设置图像流模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetImageStreamMode (const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARImageStreamMode outMode) | 获取图像流模式。 |
| AREngine_ARStatus HMS_AREngine_ARFace_AcquireBlendShapes(const AREngine_ARSession *session, const AREngine_ARFace *face, AREngine_ARFaceBlendShapes **outBlendshapes) | 获取人脸微表情对象。 |
| AREngine_ARStatus HMS_AREngine_ARFace_AcquireGeometry(const AREngine_ARSession *session, const AREngine_ARFace *face, AREngine_ARFaceGeometry **outGeometry) | 获取人脸拓扑结构对象，即人脸Mesh对象。 |
| AREngine_ARStatus HMS_AREngine_ARFace_AcquireViewMatrix(const AREngine_ARSession *session, const AREngine_ARFace *face, float *outColMajor4x4, int32_t colMajor4x4Num) | 获取当前人脸的面视图矩阵。 |
| AREngine_ARStatus HMS_AREngine_ARFace_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARFace *face, AREngine_ARPose *outPose) | 获取人脸Mesh中心的位姿。 |
| AREngine_ARStatus HMS_AREngine_ARFaceBlendShapes_AcquireData(const AREngine_ARSession *session, const AREngine_ARFaceBlendShapes *blendshapes, const float **outData) | 获取所有的微表情参数。 |
| AREngine_ARStatus HMS_AREngine_ARFaceBlendShapes_AcquireTypes(const AREngine_ARSession *session, const AREngine_ARFaceBlendShapes *blendshapes, const AREngine_ARAnimojiBlendShape **types) | 获取所有微表情参数类型。 |
| AREngine_ARStatus HMS_AREngine_ARFaceBlendShapes_GetCount(const AREngine_ARSession *session, const AREngine_ARFaceBlendShapes *blendshapes, int32_t *outSize) | 获取微表情参数个数。 |
| void HMS_AREngine_ARFaceBlendShapes_Release(AREngine_ARFaceBlendShapes *blendshapes) | 释放blendShapes对象，即由HMS_AREngine_ARFace_AcquireBlendShapes创建的对象。 |
| AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireIndices(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, const int32_t **data) | 获取人脸Mesh三角面下标数组。 |
| AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireTexCoord(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, const float **outData) | 获取人脸Mesh纹理坐标点数组。 |
| AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireTriangleLabels(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, const AREngine_ARAnimojiTriangleLabel **data) | 获取人脸Mesh三角面标签。 |
| AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireVertices(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, const float **outData) | 获取人脸Mesh顶点数组。 |
| AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetIndicesSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize) | 获取人脸Mesh三角面下标数组大小。 |
| AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetTexCoordSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize) | 获取人脸Mesh纹理坐标点数组大小。 |
| AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetTriangleCount(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize) | 获取人脸Mesh三角面个数。 |
| AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetTriangleLabelsSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize) | 获取人脸Mesh三角面标签个数。 |
| AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetVerticesSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize) | 获取人脸Mesh顶点数组大小。 |
| void HMS_AREngine_ARFaceGeometry_Release(AREngine_ARFaceGeometry *geometry) | 释放当前人脸几何体对象，即由 HMS_AREngine_ARFace_AcquireGeometry创建的对象。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCamera (const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARCamera **outCamera) | 获取当前帧的相机参数对象。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraImage (const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outImage) | 获取相机的当前帧的图像。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraPhotoImage (const AREngine_ARSession *session, const AREngine_ARFrame *frame, HMS_AREngine_PhotoAvailableCallback photoCallback) | 获取当前帧的拍照流图片。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireDepthConfidenceImage (const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outConfidenceImage) | 获取当前帧的深度置信度图像。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireDepthImage16Bits (const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outDepthImage); | 获取当前帧的深度图像。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquirePointCloud (const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARPointCloud **outPointCloud) | 返回当前帧的点云数据。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireSceneMesh (const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARSceneMesh **outSceneMesh) | 获取当前帧的mesh信息。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireSemanticDenseData (const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARSemanticDenseData **outSemanticDenseData); | 获取当前帧的高精几何重建对象数据。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_Create (const AREngine_ARSession *session, AREngine_ARFrame **outFrame) | 创建一个新的AREngine_ARFrame对象，将指针存储到*outFrame中。 |
| void HMS_AREngine_ARFrame_Destroy (AREngine_ARFrame *frame) | 删除当前AREngine_ARFrame对象。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_GetDisplayGeometryChanged (const AREngine_ARSession *session, const AREngine_ARFrame *frame, int32_t *outGeometryChangeState) | 获取显示（长宽和旋转）是否发生变化。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_GetTimestamp (const AREngine_ARSession *session, const AREngine_ARFrame *frame, int64_t *outTimestampNs) | 获取当前帧对应的时间戳信息，单位为ns。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_GetUpdatedTrackables (const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARTrackableType filterType, AREngine_ARTrackableList *outTrackableList) | 获取HMS_AREngine_ARSession_Update更新后发生变化的指定类型的可跟踪对象。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_HitTest (const AREngine_ARSession *session, const AREngine_ARFrame *frame, float pixelX, float pixelY, AREngine_ARHitResultList *hitResultList) | 从摄像头发射一条射线，该射线的方向由预览区上的点（pixelX，pixelY）确定，（pixelX，pixelY）可以通过XComponent的DispatchTouchEvent事件获取。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_TransformDisplayUvCoords (const AREngine_ARSession *session, const AREngine_ARFrame *frame, int32_t elementSize, const float *uvsIn, float *uvsOut) | 调整纹理映射坐标，以便可以正确地显示相机捕捉到的背景图片。 |
| AREngine_ARStatus HMS_AREngine_ARHitResult_AcquireNewAnchor (AREngine_ARSession *session, AREngine_ARHitResult *hitResult, AREngine_ARAnchor **outAnchor) | 在碰撞命中位置创建一个新的锚点。 |
| AREngine_ARStatus HMS_AREngine_ARHitResult_AcquireTrackable (const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, AREngine_ARTrackable **outTrackable) | 获取被命中的可追踪对象。 |
| AREngine_ARStatus HMS_AREngine_ARHitResult_Create (const AREngine_ARSession *session, AREngine_ARHitResult **outHitResult) | 创建一个空的命中检测结果对象。 |
| void HMS_AREngine_ARHitResult_Destroy (AREngine_ARHitResult *hitResult) | 释放命中检测结果对象使用的内存。 |
| AREngine_ARStatus HMS_AREngine_ARHitResult_GetDistance (const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, float *outDistance) | 返回从相机到命中位置的距离，以m为单位。 |
| AREngine_ARStatus HMS_AREngine_ARHitResult_GetHitPose (const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, AREngine_ARPose *outPose) | 获取交点的位姿。 |
| AREngine_ARStatus HMS_AREngine_ARHitResultList_Create (const AREngine_ARSession *session, AREngine_ARHitResultList **outHitResultList) | 创建一个命中检测结果对象列表。 |
| void HMS_AREngine_ARHitResultList_Destroy (AREngine_ARHitResultList *hitResultList) | 释放命中检测结果对象列表，以及其中的所有命中检测结果对象。 |
| AREngine_ARStatus HMS_AREngine_ARHitResultList_GetItem (const AREngine_ARSession *session, const AREngine_ARHitResultList *hitResultList, int32_t index, AREngine_ARHitResult *outHitResult) | 在命中检测结果列表中获取指定索引的命中检测结果对象。 |
| AREngine_ARStatus HMS_AREngine_ARHitResultList_GetSize (const AREngine_ARSession *session, const AREngine_ARHitResultList *hitResultList, int32_t *outSize) | 获取命中检测结果对象列表中包含的对象数。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetFormat (const AREngine_ARSession *session, const AREngine_ARImage *image, AREngine_ARImageFormat *outFormat) | 获取当前帧的图像格式。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetHeight (const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outHeight) | 获取当前帧的图像数据的高度。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetWidth (const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outWidth) | 获取当前帧的图像数据的宽度。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetNativeBuffer (const AREngine_ARSession *session, const AREngine_ARImage *image, OH_NativeBuffer **outNativeBuffer); | 获取当前帧图像对象的NativeBuffer数据。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneCount (const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outCount) | 获取当前帧图像的平面数量。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneData (const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, const uint8_t **outData, int32_t *outLength) | 获取当前帧图像的平面数据。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetPlanePixelStride (const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, int32_t *outPixelStride) | 获取图像中两个连续像素的起点之间的字节距离。像素步幅始终大于0。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneRowStride (const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, int32_t *outRowStride) | 获取图像中两个连续像素行的起始位置之间的字节数。行间距始终大于0。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetTimestamp (const AREngine_ARSession *session, const AREngine_ARImage *image, int64_t *outTimestamp) | 获取图像的时间戳。 |
| void HMS_AREngine_ARImage_Release (AREngine_ARImage *image) | 释放当前帧的图像对象，由HMS_AREngine_ARFrame_AcquireCameraImage创建的对象。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_AcquireSubsumedBy (const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPlane **outSubsumedBy) | 获取平面的父平面（一个平面被另一个平面合并时，会产生父平面），如果无父平面返回为NULL。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetCenterPose (const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPose *outPose) | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetExtentX (const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outExtentX) | 获取平面的矩形边界沿平面局部坐标系X轴的长度，如矩形的宽度。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetExtentZ (const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outExtentZ) | 获取平面的矩形边界沿平面局部坐标系Z轴的长度，如矩形的高度。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetLabel (const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARSemanticPlaneLabel *label) | 获取平面的语义类型，如桌面、地板等。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetPolygon (const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outPolygonXz, int32_t polygonSize) | 获取检测到平面的二维顶点数组，格式为[x1，z1，x2，z2，...]。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetPolygonSize (const AREngine_ARSession *session, const AREngine_ARPlane *plane, int32_t *outPolygonSize) | 获取检测到平面的二维顶点数组大小。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetType (const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPlaneType *outPlaneType) | 获取平面的类型。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_IsPoseInExtents (const AREngine_ARSession *session, const AREngine_ARPlane *plane, const AREngine_ARPose *pose, int32_t *outPoseInExtents) | 判断位姿是否位于平面的矩形范围内。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_IsPoseInPolygon (const AREngine_ARSession *session, const AREngine_ARPlane *plane, const AREngine_ARPose *pose, int32_t *outPoseInPolygon) | 判断位姿是否位于平面的多边形范围内。 |
| AREngine_ARStatus HMS_AREngine_ARPoint_GetOrientationMode (const AREngine_ARSession *session, const AREngine_ARPoint *point, AREngine_ARPointOrientationMode *outOrientationMode) | 获取输入点的朝向模式。 |
| AREngine_ARStatus HMS_AREngine_ARPoint_GetPose (const AREngine_ARSession *session, const AREngine_ARPoint *point, AREngine_ARPose *outPose) | 获取输入点的位姿信息。 |
| AREngine_ARStatus HMS_AREngine_ARPointCloud_GetData (const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, const float **outPointCloudData) | 获取点云中所有点的坐标及置信度数组。 |
| AREngine_ARStatus HMS_AREngine_ARPointCloud_GetNumberOfPoints (const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, int32_t *outNumberOfPoints) | 获取点云中所有点的坐标及置信度数组大小。 |
| AREngine_ARStatus HMS_AREngine_ARPointCloud_GetTimestamp (const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, int64_t *outTimestampNs) | 获取检测到当前特征点云的时间，以ns为单位。 |
| void HMS_AREngine_ARPointCloud_Release (AREngine_ARPointCloud *pointCloud) | 释放点云对象使用的内存。 |
| AREngine_ARStatus HMS_AREngine_ARPose_Create (const AREngine_ARSession *session, const float *poseRaw, const uint32_t poseRawSize, AREngine_ARPose **outPose) | 分配并初始化一个新的位姿对象。 |
| void HMS_AREngine_ARPose_Destroy (AREngine_ARPose *pose) | 释放位姿对象使用的内存。 |
| AREngine_ARStatus HMS_AREngine_ARPose_GetMatrix (const AREngine_ARSession *session, const AREngine_ARPose *pose, float *outMatrixColMajor4x4, int32_t matrixColMajor4x4Size) | 将位姿数据转换成4X4的矩阵。 |
| AREngine_ARStatus HMS_AREngine_ARPose_GetPoseRaw (const AREngine_ARSession *session, const AREngine_ARPose *pose, float *outPoseRaw, int32_t poseRawSize) | 从位姿对象提取位姿数据。 |
| AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireIndexList (const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outData, int32_t dataSize) | 获取mesh面片的索引集合。 |
| AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireIndexListSize (const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outSize) | 获取mesh面片的索引个数。 |
| AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVertexList (const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, float *outData, int32_t dataSize) | 获取mesh的顶点集合。 |
| AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVertexNormalList (const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, float *outData, int32_t dataSize) | 获取mesh面片的法向量集合。 |
| AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVerticesSize (const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outSize) | 获取mesh的顶点个数。 |
| void HMS_AREngine_ARSceneMesh_Release (AREngine_ARSceneMesh *SceneMesh) | 释放当前帧的mesh信息。 |
| AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquireCubeData (const AREngine_ARSession *session, const AREngine_ARSemanticDenseData *semanticDenseData, AREngine_ARSemanticDenseCubeData **outCubeData) | 获取识别到的高精几何重建对象数据中的立方体数据。 |
| AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquireCubeDataSize (const AREngine_ARSession *session, const AREngine_ARSemanticDenseData *semanticDenseData, int64_t *outSize) | 获取识别到的高精几何重建对象数据中的立方体数量。 |
| AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquirePointData (const AREngine_ARSession *session, const AREngine_ARSemanticDenseData *semanticDenseData, AREngine_ARSemanticDensePointData **outPointData) | 获取识别到的高精几何重建对象数据中的稠密点云数据。 |
| AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquirePointDataSize (const AREngine_ARSession *session, const AREngine_ARSemanticDenseData *semanticDenseData, int64_t *outSize) | 获取识别到的高精几何重建对象数据中的稠密点云数量。 |
| void HMS_AREngine_ARSemanticDense_Release (AREngine_ARSemanticDenseData *semanticDenseData) | 释放高精几何重建对象。 |
| AREngine_ARStatus HMS_AREngine_ARSession_AcquireNewAnchor (AREngine_ARSession *session, const AREngine_ARPose *pose, AREngine_ARAnchor **outAnchor) | 创建一个持续跟踪的锚点。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Configure (AREngine_ARSession *session, const AREngine_ARConfig *config) | 配置AREngine_ARSession会话。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Create (void *env, void *applicationContext, AREngine_ARSession **outSessionPointer) | 创建一个新的AREngine_ARSession会话。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Create_Human_Perception(void *env, void *applicationContext, AREngine_ARSession **outSessionPointer) | 创建一个新的AREngine_ARSession人体追踪会话。 |
| void HMS_AREngine_ARSession_Destroy (AREngine_ARSession *session) | 释放AREngine_ARSession会话使用的资源。 |
| AREngine_ARStatus HMS_AREngine_ARSession_GetCameraConfig (const AREngine_ARSession *session, AREngine_ARCameraConfig *outCameraConfig) | 获取相机配置信息。 |
| AREngine_ARStatus HMS_AREngine_ARSession_GetAllAnchors (const AREngine_ARSession *session, AREngine_ARAnchorList *outAnchorList) | 获取所有锚点，包括AREngine_ARTrackingState中包含的所有状态下的锚点。 |
| AREngine_ARStatus HMS_AREngine_ARSession_GetAllTrackables (const AREngine_ARSession *session, AREngine_ARTrackableType filterType, AREngine_ARTrackableList *outTrackableList) | 获取所有指定类型的可跟踪对象集合。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Pause (AREngine_ARSession *session) | 暂停会话，停止相机预览流，不清除平面和锚点数据，释放相机（否则其他应用无法使用相机服务）。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Resume (AREngine_ARSession *session) | 开始运行AREngine_ARSession，或者在调用HMS_AREngine_ARSession_Pause以后恢复AREngine_ARSession的运行状态。 |
| AREngine_ARStatus HMS_AREngine_ARSession_SetCameraGLTexture (AREngine_ARSession *session, uint32_t textureId) | 设置可用于存储相机预览流数据的OpenGL纹理。 |
| AREngine_ARStatus HMS_AREngine_ARSession_SetDisplayGeometry (AREngine_ARSession *session, AREngine_ARPoseType rotation, int32_t width, int32_t height) | 设置显示的高和宽，以像素为单位。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Stop (AREngine_ARSession *session) | 停止AR Engine，停止相机预览流，清除平面和锚点数据，并释放相机，终止本次会话。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Update (AREngine_ARSession *session, AREngine_ARFrame *outFrame) | 更新AR Engine的计算结果。 |
| AREngine_ARStatus HMS_AREngine_ARTarget_GetAxisAlignedBoundingBox(const AREngine_ARSession *session, const AREngine_ARTarget *target, float *outAabb, int32_t aabbSize) | 获取语义物体最小外接包围盒坐标，坐标格式为（xmin，ymin，zmin，xmax，ymax，zmax)。 |
| AREngine_ARStatus HMS_AREngine_ARTarget_GetCenterPose (const AREngine_ARSession *session, const AREngine_ARTarget *target, AREngine_ARPose *outARPose) | 获取从目标语义对象的局部坐标系到世界坐标系转换的位姿对象。 |
| AREngine_ARStatus HMS_AREngine_ARTarget_GetRadius (const AREngine_ARSession *session, const AREngine_ARTarget *target, float *radius) | 获取语义物体的球体半径。 |
| AREngine_ARStatus HMS_AREngine_ARTarget_GetShapeType (const AREngine_ARSession *session, const AREngine_ARTarget *target, AREngine_ARTargetShapeLabel *shape) | 获取语义物体的形状类型。 |
| AREngine_ARStatus HMS_AREngine_ARTrackable_AcquireNewAnchor (AREngine_ARSession *session, AREngine_ARTrackable *trackable, AREngine_ARPose *pose, AREngine_ARAnchor **outAnchor) | 通过可跟踪对象的位姿信息创建对应的锚点对象，该锚点将和当前的可跟踪对象绑定。 |
| AREngine_ARStatus HMS_AREngine_ARTrackable_GetAnchors (AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARAnchorList *outAnchorList) | 获取绑定到输入可跟踪对象的锚点对象列表。 |
| AREngine_ARStatus HMS_AREngine_ARTrackable_GetTrackingState (const AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARTrackingState *outTrackingState) | 获取当前可跟踪对象的跟踪状态。 |
| AREngine_ARStatus HMS_AREngine_ARTrackable_GetType (const AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARTrackableType *outTrackableType) | 获取可跟踪对象的类型。 |
| void HMS_AREngine_ARTrackable_Release (AREngine_ARTrackable *trackable) | 释放可跟踪对象。 |
| AREngine_ARStatus HMS_AREngine_ARTrackableList_AcquireItem (const AREngine_ARSession *session, const AREngine_ARTrackableList *trackableList, int32_t index, AREngine_ARTrackable **outTrackable) | 从可跟踪列表中获取指定index的对象。 |
| AREngine_ARStatus HMS_AREngine_ARTrackableList_Create (const AREngine_ARSession *session, AREngine_ARTrackableList **outTrackableList) | 创建一个可跟踪对象列表。 |
| void HMS_AREngine_ARTrackableList_Destroy (AREngine_ARTrackableList *trackableList) | 释放可跟踪对象列表，以及它持有的所有锚点引用。 |
| AREngine_ARStatus HMS_AREngine_ARTrackableList_GetSize (const AREngine_ARSession *session, const AREngine_ARTrackableList *trackableList, int32_t *outSize) | 获取此列表中的可跟踪对象的数量。 |
| AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonConfidence(const AREngine_ARSession *session, const AREngine_ARBody *body, const float **outConfidence) | 获取人体对象每个骨骼点检测的置信度。 |
| AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonConnection(const AREngine_ARSession *session, const AREngine_ARBody *body, const AREngine_ARBodySkeletonType **outSkeletonConnection) | 获取人体对象骨骼点之间的链接关系数据。 |
| AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonConnectionSize(const AREngine_ARSession *session, const AREngine_ARBody *body, int32_t *outConnectionCount) | 获取人体对象骨骼点之间的链接关系总数。 |
| AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonTypes(const AREngine_ARSession *session, const AREngine_ARBody *body, const AREngine_ARBodySkeletonType **outSkeletonTypes) | 获取识别出的人体对象骨骼点类型。 |
| AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonPointCount(const AREngine_ARSession *session, const AREngine_ARBody *body, int32_t *outPointCount) | 获取人体对象的骨骼点个数。 |
| AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonPointData2D(const AREngine_ARSession *session, const AREngine_ARBody *body, const float **outSkeletonPointData2D) | 当运行2D骨骼跟踪算法时，返回人体骨骼点的坐标数据。 |
| AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonPointIsValid(const AREngine_ARSession *session, const AREngine_ARBody *body, const int32_t **outSkeletonPointIsValid) | 获取人体对象骨骼点的坐标是否有效，返回有效性数组。 |
| AREngine_ARStatus HMS_AREngine_ARBody_GetBodyTrackId(const AREngine_ARSession *session, const AREngine_ARBody *body, const int32_t *outBodyTrackId) | 获取指定人体对象的标识。 |
| AREngine_ARStatus HMS_AREngine_ARBody_GetBodyTimeStamp(const AREngine_ARSession *session, const AREngine_ARBody *body, int64_t *timeStamp) | 获取人体对象的检测时间点，表示触发检测人体对象距离启动相机的时间间隔，单位为ns。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetBodyDetectedNum(const AREngine_ARSession *session, AREngine_ARConfig *config, int32_t maxNum) | 设置追踪人数。 |

**宏定义说明**

**ARENGINE_AABB_POINT_SIZE**

```ets
const static int32_t ARENGINE_AABB_POINT_SIZE = 6
```

描述

包围盒坐标集数组大小。

起始版本： 5.0.0(12)

**ARENGINE_DISTORTION_COUNT**

```ets
const static int32_t ARENGINE_DISTORTION_COUNT = 5
```

描述

相机畸变参数的个数。

起始版本： 5.0.0(12)

**ARENGINE_POSE_RAW_SIZE**

```ets
const static int32_t ARENGINE_POSE_RAW_SIZE = 7
```

描述

位姿数据数组大小。

起始版本： 5.0.0(12)

**ARENGINE_VIEW_MATRIX_SIZE**

```ets
const static int32_t ARENGINE_VIEW_MATRIX_SIZE = 16
```

描述

变换矩阵数组大小。

起始版本： 5.0.0(12)

**类型定义说明**

**AREngine_ARAnchor**

```ets
typedef struct AREngine_ARAnchor AREngine_ARAnchor
```

描述

锚点对象。

描述与可跟踪对象关联的空间位置。

起始版本： 5.0.0(12)

**AREngine_ARAnchorList**

```ets
typedef struct AREngine_ARAnchorList AREngine_ARAnchorList
```

描述

锚点对象列表。

包含一系列锚点对象。

起始版本： 5.0.0(12)

**AREngine_ARAugmentedImage**

```ets
typedef struct AREngine_ARAugmentedImage AREngine_ARAugmentedImage
```

描述

跟踪图像对象。

起始版本： 5.1.0(18)

**AREngine_ARAugmentedImageDatabase**

```ets
typedef struct AREngine_ARAugmentedImageDatabase AREngine_ARAugmentedImageDatabase
```

描述

跟踪图像数据库对象。

起始版本： 5.1.0(18)

**AREngine_ARCamera**

```ets
typedef struct AREngine_ARCamera AREngine_ARCamera
```

描述

当前帧对应的相机信息。

起始版本： 5.0.0(12)

**AREngine_ARCameraConfig**

```ets
typedef struct AREngine_ARCameraConfig AREngine_ARCameraConfig
```

描述

相机的配置信息。

如CPU图像的尺寸，GPU纹理的尺寸。

起始版本： 5.0.0(12)

**AREngine_ARCameraIntrinsics**

```ets
typedef struct AREngine_ARCameraIntrinsics AREngine_ARCameraIntrinsics
```

描述

相机内参。

包括fx；fy；cx；cy；畸变参数。

起始版本： 5.0.0(12)

**AREngine_ARConfig**

```ets
typedef struct AREngine_ARConfig AREngine_ARConfig
```

描述

用于配置[AREngine_ARSession](#ZH-CN_TOPIC_0000002553362039__arengine_arsession)的能力项（使用哪些能力、模式等）。

起始版本： 5.0.0(12)

**AREngine_ARFace**

```ets
typedef struct AREngine_ARFace AREngine_ARFace
```

描述

跟踪的人脸对象。

起始版本： 6.1.0(23)

**AREngine_ARFaceGeometry**

```ets
typedef struct AREngine_ARFaceGeometry AREngine_ARFaceGeometry
```

描述

人脸拓扑结构对象。

起始版本： 6.1.0(23)

**AREngine_ARFaceBlendShapes**

```ets
typedef struct AREngine_ARFaceBlendShapes AREngine_ARFaceBlendShapes
```

描述

人脸微表情对象。

起始版本： 6.1.0(23)

**AREngine_ARFaceLandmark**

```ets
typedef struct AREngine_ARFaceLandmark AREngine_ARFaceLandmark
```

描述

人脸关键点对象。

起始版本： 6.1.0(23)

**AREngine_ARFrame**

```ets
typedef struct AREngine_ARFrame AREngine_ARFrame
```

描述

AR Engine处理的一帧数据。

起始版本： 5.0.0(12)

**AREngine_ARHitResult**

```ets
typedef struct AREngine_ARHitResult AREngine_ARHitResult
```

描述

命中检测结果对象。

描述单个可跟踪对象的命中检测结果。

起始版本： 5.0.0(12)

**AREngine_ARHitResultList**

```ets
typedef struct AREngine_ARHitResultList AREngine_ARHitResultList
```

描述

命中检测结果列表。

包含一系列命中检测的结果对象。

起始版本： 5.0.0(12)

**AREngine_ARImage**

```ets
typedef struct AREngine_ARImage AREngine_ARImage
```

描述

相机视频流帧对象。

起始版本： 5.0.0(12)

**AREngine_ARPlane**

```ets
typedef struct AREngine_ARPlane AREngine_ARPlane
```

描述

平面对象。

描述被检测到的可跟踪平面信息。

起始版本： 5.0.0(12)

**AREngine_ARPoint**

```ets
typedef struct AREngine_ARPoint AREngine_ARPoint
```

描述

点对象。

描述被检测到的可跟踪点数据。

起始版本： 5.0.0(12)

**AREngine_ARPointCloud**

```ets
typedef struct AREngine_ARPointCloud AREngine_ARPointCloud
```

描述

可跟踪的3D点云的集合。

起始版本： 5.0.0(12)

**AREngine_ARPose**

```ets
typedef struct AREngine_ARPose AREngine_ARPose
```

描述

位姿对象。

描述从一个坐标系到另一个坐标系的不可变的刚体变换，例如平移或旋转。

详细可参考[世界坐标系与位姿示意](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-pose#世界坐标系与位姿示意)。

起始版本： 5.0.0(12)

**AREngine_ARSceneMesh**

```ets
typedef struct AREngine_ARSceneMesh AREngine_ARSceneMesh
```

描述

环境mesh数据的集合。

起始版本： 5.1.0(18)

**AREngine_ARSemanticDenseData**

```ets
typedef struct AREngine_ARSemanticDenseData AREngine_ARSemanticDenseData
```

描述

表示高精几何重建对象数据的集合。

起始版本： 6.0.0(20)

**AREngine_ARSession**

```ets
typedef struct AREngine_ARSession AREngine_ARSession
```

描述

管理AR Engine的系统状态。

起始版本： 5.0.0(12)

**AREngine_ARTarget**

```ets
typedef struct AREngine_ARTarget AREngine_ARTarget
```

描述

物体对象。

描述被检测到的可跟踪语义目标信息，例如语义平面。

起始版本： 5.0.0(12)

**AREngine_ARTrackable**

```ets
typedef struct AREngine_ARTrackable AREngine_ARTrackable
```

描述

可跟踪对象，如点、平面等。

应用获取到此对象后，如需对此对象进行具体操作，如通过[HMS_AREngine_ARPlane_GetCenterPose](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arplane_getcenterpose)接口获取平面的中心点位置， 通过[HMS_AREngine_ARPoint_GetPose](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arpoint_getpose)接口获取点的位姿信息等， 可以根据可跟踪对象类型（通过[HMS_AREngine_ARTrackable_GetType](#ZH-CN_TOPIC_0000002553362039__hms_arengine_artrackable_gettype)接口获取）转换成相应的对象， 如[AREngine_ARPlane](#ZH-CN_TOPIC_0000002553362039__arengine_arplane)，[AREngine_ARPoint](#ZH-CN_TOPIC_0000002553362039__arengine_arpoint)等，转换方式可参考： [AREngine_ARPlane](#ZH-CN_TOPIC_0000002553362039__arengine_arplane) *arPlane = reinterpret_cast<[AREngine_ARPlane](#ZH-CN_TOPIC_0000002553362039__arengine_arplane) *>(trackable)。

起始版本： 5.0.0(12)

**AREngine_ARTrackableList**

```ets
typedef struct AREngine_ARTrackableList AREngine_ARTrackableList
```

描述

可跟踪对象列表。

起始版本： 5.0.0(12)

**HMS_AREngine_PhotoAvailableCallback**

```ets
typedef void (*HMS_AREngine_PhotoAvailableCallback)(OH_NativeBuffer *photoBuffer)
```

描述

输出拍照流图像回调。

起始版本： 6.0.2(22)

**AREngine_ARBody**

```ets
typedef struct AREngine_ARBody AREngine_ARBody
```

描述

人体对象。

起始版本： 6.1.0(23)

**枚举类型说明**

**AREngine_FeatureType**

```ets
enum AREngine_FeatureType
```

描述

AR特性类别。

起始版本： 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_FEATURE_TYPE_SLAM | 平面查找特性。 |
| ARENGINE_FEATURE_TYPE_DEPTH | 深度特性。 |
| ARENGINE_FEATURE_TYPE_MESH | Mesh特性。 |
| ARENGINE_FEATURE_TYPE_IMAGE | 图像特性。 |
| ARENGINE_FEATURE_TYPE_SEMANTIC_DENSE | 高精几何特性。 |
| ARENGINE_FEATURE_TYPE_SEMANTIC | 语义特性。 |
| ARENGINE_FEATURE_TYPE_FACE | 人脸特性。 |
| ARENGINE_FEATURE_TYPE_BODY | 人体骨骼特性。 |

**AREngine_ARAddAugmentedImageReason**

```ets
enum AREngine_ARAddAugmentedImageReason
```

描述

跟踪失败的可能原因。

起始版本： 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_ADD_AUGMENTED_IMAGE_REASON_NONE | 添加的图像符合质量要求。 |
| ARENGINE_ADD_AUGMENTED_IMAGE_REASON_SIZE_NOT_MATCH | 尝试将质量不足（尺寸不匹配）的图像添加到图像数据库。 说明： 图像尺寸评价从宽高比、分辨率两个维度进行。建议宽高比、分辨率的评价为Unfit以上。 |
| ARENGINE_ADD_AUGMENTED_IMAGE_REASON_LIGHT_ANOMALY | 尝试将质量不足（太亮或太暗）的图像添加到图像数据库中。 |
| ARENGINE_ADD_AUGMENTED_IMAGE_REASON_FEATURE_LIMIT | 尝试将质量不足（图像颜色比较单一）的图像添加到图像数据库中。 |
| ARENGINE_ADD_AUGMENTED_IMAGE_REASON_OTHER | 尝试将质量不足（其他场景，如图片有反光、光斑，重复性内容等）添加到图像数据库中。 |

-

宽高比：

图像宽度与高度之比，如：640*480分辨率的图像，其宽高比为1.33，对应评价Excellent。

| 图像宽高比 | 评价 |
| --- | --- |
| [6, ∞) | Invalid |
| [4, 6) | Bad |
| [2.5, 4) | Unfit |
| [2, 2.5) | Fit |
| [1.5, 2) | Good |
| [1, 1.5) | Excellent |

-

分辨率：

以640*480为基准，按比例计算。如：选取图像分辨率为320*240，以基准分辨率计算其比值为0.5，对应评价Fit。

| 图像分辨率比值 | 评价 |
| --- | --- |
| [0, 0.2] | Invalid |
| (0.2, 0.3] | Bad |
| (0.35, 0.45] | Unfit |
| (0.45, 0.7] | Fit |
| (0.7, 0.9] | Good |
| (0.9, ∞) | Excellent |

**AREngine_ARAnimojiBlendShape**

```ets
enum AREngine_ARAnimojiBlendShape
```

描述

微表情类型。

起始版本： 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_ARANIMOJI_EYE_BLINK_LEFT | 左眼闭合。 |
| ARENGINE_ARANIMOJI_EYE_LOOK_DOWN_LEFT | 左上眼皮微下垂。 |
| ARENGINE_ARANIMOJI_EYE_LOOK_IN_LEFT | 左眼内部眼皮向左扩。 |
| ARENGINE_ARANIMOJI_EYE_LOOK_OUT_LEFT | 左眼睑向左扩。 |
| ARENGINE_ARANIMOJI_EYE_LOOK_UP_LEFT | 左眼上眼皮微上抬。 |
| ARENGINE_ARANIMOJI_EYE_SQUINT_LEFT | 左下眼睑上抬。 |
| ARENGINE_ARANIMOJI_EYE_WIDE_LEFT | 左眼瞪大眼。 |
| ARENGINE_ARANIMOJI_EYE_BLINK_RIGHT | 闭右眼。 |
| ARENGINE_ARANIMOJI_EYE_LOOK_DOWN_RIGHT | 右上眼皮微下垂。 |
| ARENGINE_ARANIMOJI_EYE_LOOK_IN_RIGHT | 右眼内部眼皮向右扩。 |
| ARENGINE_ARANIMOJI_EYE_LOOK_OUT_RIGHT | 右眼睑向右扩。 |
| ARENGINE_ARANIMOJI_EYE_LOOK_UP_RIGHT | 右眼上眼皮微上抬。 |
| ARENGINE_ARANIMOJI_EYE_SQUINT_RIGHT | 右下眼睑上抬。 |
| ARENGINE_ARANIMOJI_EYE_WIDE_RIGHT | 右眼瞪大眼。 |
| ARENGINE_ARANIMOJI_JAW_FORWARD | 下巴朝前。 |
| ARENGINE_ARANIMOJI_JAW_LEFT | 下巴朝左。 |
| ARENGINE_ARANIMOJI_JAW_RIGHT | 下巴朝右。 |
| ARENGINE_ARANIMOJI_JAW_OPEN | 张嘴。 |
| ARENGINE_ARANIMOJI_MOUTH_FUNNEL | O型嘴。 |
| ARENGINE_ARANIMOJI_MOUTH_PUCKER | 噘嘴。 |
| ARENGINE_ARANIMOJI_MOUTH_LEFT | 嘴巴向左。 |
| ARENGINE_ARANIMOJI_MOUTH_RIGHT | 嘴巴向右。 |
| ARENGINE_ARANIMOJI_MOUTH_SMILE_LEFT | 左嘴角向左歪。 |
| ARENGINE_ARANIMOJI_MOUTH_SMILE_RIGHT | 右嘴角向右歪。 |
| ARENGINE_ARANIMOJI_MOUTH_FROWN_LEFT | 左嘴角下拉。 |
| ARENGINE_ARANIMOJI_MOUTH_FROWN_RIGHT | 右嘴角下拉。 |
| ARENGINE_ARANIMOJI_MOUTH_DIMPLE_LEFT | 左酒窝上抬。 |
| ARENGINE_ARANIMOJI_MOUTH_DIMPLE_RIGHT | 右酒窝上抬。 |
| ARENGINE_ARANIMOJI_MOUTH_STRETCH_LEFT | 嘴角向左拉。 |
| ARENGINE_ARANIMOJI_MOUTH_STRETCH_RIGHT | 嘴角向右拉。 |
| ARENGINE_ARANIMOJI_MOUTH_ROLL_LOWER | 下嘴唇向内抿嘴。 |
| ARENGINE_ARANIMOJI_MOUTH_ROLL_UPPER | 抿上嘴唇。 |
| ARENGINE_ARANIMOJI_MOUTH_SHRUG_LOWER | 撅下嘴唇。 |
| ARENGINE_ARANIMOJI_MOUTH_SHRUG_UPPER | 撅上嘴唇。 |
| ARENGINE_ARANIMOJI_MOUTH_UPPER_UP | 嘴唇上翻。 |
| ARENGINE_ARANIMOJI_MOUTH_LOWER_DOWN | 下嘴唇朝下。 |
| ARENGINE_ARANIMOJI_MOUTH_LOWER_OUT | 下嘴唇朝外。 |
| ARENGINE_ARANIMOJI_BROW_DOWN_LEFT | 左侧眉毛朝下。 |
| ARENGINE_ARANIMOJI_BROW_DOWN_RIGHT | 右侧眉毛朝下。 |
| ARENGINE_ARANIMOJI_BROW_INNER_UP | 双侧眉毛抬眉。 |
| ARENGINE_ARANIMOJI_BROW_OUTER_UP_LEFT | 左眉外侧向上抬。 |
| ARENGINE_ARANIMOJI_BROW_OUTER_UP_RIGHT | 右眉外侧向上抬。 |
| ARENGINE_ARANIMOJI_CHEEK_PUFF | 鼓腮。 |
| ARENGINE_ARANIMOJI_CHEEK_SQUINT_LEFT | 左脸颊上抬。 |
| ARENGINE_ARANIMOJI_CHEEK_SQUINT_RIGHT | 右脸颊上抬。 |
| ARENGINE_ARANIMOJI_FROWN_NOSE_MOUTH_UP | 鼻子上抬。 |
| ARENGINE_ARANIMOJI_TONGUE_IN | 舌头在嘴里上下位置。 |
| ARENGINE_ARANIMOJI_TONGUE_OUT_SLIGHT | 舌头直伸。 |
| ARENGINE_ARANIMOJI_TONGUE_LEFT | 舌头朝左。 |
| ARENGINE_ARANIMOJI_TONGUE_RIGHT | 舌头朝右。 |
| ARENGINE_ARANIMOJI_TONGUE_UP | 舌头朝上。 |
| ARENGINE_ARANIMOJI_TONGUE_DOWN | 舌头朝下。 |
| ARENGINE_ARANIMOJI_TONGUE_LEFT_UP | 舌头朝左上。 |
| ARENGINE_ARANIMOJI_TONGUE_LEFT_DOWN | 舌头朝左下。 |
| ARENGINE_ARANIMOJI_TONGUE_RIGHT_UP | 舌头朝右上。 |
| ARENGINE_ARANIMOJI_TONGUE_RIGHT_DOWN | 舌头朝右下。 |
| ARENGINE_ARANIMOJI_LEFT_EYEBALL_LEFT | 左眼球向左。 |
| ARENGINE_ARANIMOJI_LEFT_EYEBALL_RIGHT | 左眼球向右。 |
| ARENGINE_ARANIMOJI_LEFT_EYEBALL_UP | 左眼球向上。 |
| ARENGINE_ARANIMOJI_LEFT_EYEBALL_DOWN | 左眼球向下。 |
| ARENGINE_ARANIMOJI_RIGHT_EYEBALL_LEFT | 右眼球向左。 |
| ARENGINE_ARANIMOJI_RIGHT_EYEBALL_RIGHT | 右眼球向右。 |
| ARENGINE_ARANIMOJI_RIGHT_EYEBALL_UP | 右眼球向上。 |
| ARENGINE_ARANIMOJI_RIGHT_EYEBALL_DOWN | 右眼球向下。 |

**AREngine_ARAnimojiTriangleLabel**

```ets
enum AREngine_ARAnimojiTriangleLabel
```

描述

人脸三角形面片标签。

起始版本： 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_TRIANGLE_LABEL_NON_FACE | 不是脸部位。 |
| ARENGINE_TRIANGLE_LABEL_FACE_OTHER | 脸部非关键部位。 |
| ARENGINE_TRIANGLE_LABEL_LOWER_LIP | 下嘴唇。 |
| ARENGINE_TRIANGLE_LABEL_UPPER_LIP | 上嘴唇。 |
| ARENGINE_TRIANGLE_LABEL_LEFT_EYE | 左眼睛。 |
| ARENGINE_TRIANGLE_LABEL_RIGHT_EYE | 右眼睛。 |
| ARENGINE_TRIANGLE_LABEL_LEFT_BROW | 左眉毛。 |
| ARENGINE_TRIANGLE_LABEL_RIGHT_BROW | 右眉毛。 |
| ARENGINE_TRIANGLE_LABEL_BROW_CENTER | 眉心。 |
| ARENGINE_TRIANGLE_LABEL_NOSE | 鼻子。 |

**AREngine_ARCameraLensFacing**

```ets
enum AREngine_ARCameraLensFacing
```

描述

配置摄像机镜头的朝向。

起始版本： 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_CAMERA_FACING_REAR | 后置摄像头。 |
| ARENGINE_CAMERA_FACING_FRONT | 前置摄像头。 |

**AREngine_ARConfidenceLevel**

```ets
enum AREngine_ARConfidenceLevel
```

描述

深度置信度。

起始版本： 5.0.5(17)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_DEPTH_CONFIDENCE_LOW | 该深度图像的置信度较低。 |
| ARENGINE_DEPTH_CONFIDENCE_MEDIUM | 该深度图像的置信度中等。 |
| ARENGINE_DEPTH_CONFIDENCE_HIGH | 该深度图像的置信度很高。 |

**AREngine_ARDepthMode**

```ets
enum AREngine_ARDepthMode
```

描述

深度模式。

起始版本： 5.0.5(17)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_DEPTH_MODE_DISABLED | 不提供深度图像信息。 |
| ARENGINE_DEPTH_MODE_AUTOMATIC | AR Engine会自动尝试从多种深度源获取深度信息。 说明： 通常有两种深度源，运动算法和硬件深度传感器 (Time of Flight，简称ToF)。目前仅支持运动算法。 |

**AREngine_ARFocusMode**

```ets
enum AREngine_ARFocusMode
```

描述

对焦模式。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_FOCUS_MODE_FIXED | 固定焦点对焦模式。 |
| ARENGINE_FOCUS_MODE_AUTO | 自动对焦模式。 |

**AREngine_ARImageDatabaseMode**

```ets
enum AREngine_ARImageDatabaseMode
```

描述

用于跟踪的特征库图像添加方式。

起始版本： 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_ADD_NORMAL | 正常添加模式。 |
| ARENGINE_ADD_AUTO | 循环删除模式。 |

**AREngine_ARImageFormat**

```ets
enum AREngine_ARImageFormat
```

描述

图像数据格式。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_IMAGE_UNKNOWN | 无效的图片格式。 |
| ARENGINE_IMAGE_YUV_420_888 | YUV_420_888格式，适用于处理高分辨率的图像数据。 |
| ARENGINE_IMAGE_Y_8 | Y_8格式，适用于对图像数据要求较低的精度或存储空间的场景。 起始版本： 5.0.5(17) |
| ARENGINE_IMAGE_Y_16 | Y_16格式，适用于对图像数据精度要求较高的场景。 起始版本： 5.0.5(17) |

**AREngine_ARImageStreamMode**

```ets
enum AREngine_ARImageStreamMode
```

描述

设置图片数据流模式，默认情况下系统设置为ARENGINE_IMAGE_STREAM_MODE_PREVIEW。

起始版本： 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_IMAGE_STREAM_MODE_PREVIEW | 预览流模式，可通过HMS_AREngine_ARFrame_AcquireCameraImage接口获取预览流图像。 |
| ARENGINE_IMAGE_STREAM_MODE_PREVIEW_AND_PHOTO | 拍照流加预览流模式，可通过HMS_AREngine_ARFrame_AcquireCameraPhotoImage接口获取拍照流图像。 |

**AREngine_ARMeshMode**

```ets
enum AREngine_ARMeshMode
```

描述

Mesh启用模式。

起始版本： 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_MESH_MODE_DISABLED | 网格模式关闭 AR Engine不会处理或显示网格数据。 |
| ARENGINE_MESH_MODE_ENABLE | 网格模式开启 AR Engine会尝试处理或显示网格数据。 |

**AREngine_ARMultiFaceMode**

```ets
enum AREngine_ARMultiFaceMode
```

描述

多人脸检测模式。

起始版本： 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_MULTIFACE_DISABLE | 多人脸检测模式关闭。 |
| ARENGINE_MULTIFACE_ENABLE | 多人脸检测模式开启。 |

**AREngine_ARPlaneFindingMode**

```ets
enum AREngine_ARPlaneFindingMode
```

描述

平面搜索模式。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_PLANE_FINDING_MODE_DISABLED | 禁用平面检测。 |
| ARENGINE_PLANE_FINDING_MODE_HORIZONTAL | 只检测水平面，如地板和桌子。 |
| ARENGINE_PLANE_FINDING_MODE_VERTICAL | 只检测竖直平面，如墙壁。 |
| ARENGINE_PLANE_FINDING_MODE_HORIZONTAL_AND_VERTICAL | 同时检测水平面和竖直平面。 |

**AREngine_ARPlaneType**

```ets
enum AREngine_ARPlaneType
```

描述

平面类型。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_PLANE_FACING_HORIZONTAL_UPWARD | 朝上的水平面（例如地面和桌面平台）。 |
| ARENGINE_PLANE_FACING_HORIZONTAL_DOWNWARD | 朝下的水平面（例如天花板）。 |
| ARENGINE_PLANE_FACING_VERTICAL | 垂直的水平面（例如墙壁）。 |
| ARENGINE_PLANE_FACING_INVALID | 无效或不支持的平面类型。这可能是由于环境变化、光线条件或其他因素导致。 |

**AREngine_ARPointOrientationMode**

```ets
enum AREngine_ARPointOrientationMode
```

描述

朝向模式。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_POINT_ORIENTATION_INITIALIZED_TO_IDENTITY | 与世界坐标系的朝向一致，但会稍作调整。 |
| ARENGINE_POINT_ORIENTATION_ESTIMATED_SURFACE_NORMAL | 朝向由估计的平面法向量决定。 |

**AREngine_ARPoseMode**

```ets
enum AREngine_ARPoseMode
```

描述

AR Engine输出的相机位姿对齐格式。

起始版本： 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_POSE_MODE_GRAVITY | 输出的位姿信息（通过HMS_AREngine_ARCamera_GetDisplayOrientedPose、HMS_AREngine_ARCamera_GetPose接口返回）为重力坐标系对齐的数据。参见AR Engine重力对齐世界坐标系。 |
| ARENGINE_POSE_MODE_GRAVITY_HEADING | 输出的位姿信息（通过HMS_AREngine_ARCamera_GetDisplayOrientedPose、HMS_AREngine_ARCamera_GetPose接口返回）为北向ENU坐标系对齐的数据。参见AR Engine重力对齐北向坐标系。 |

**AREngine_ARPoseType**

```ets
enum AREngine_ARPoseType
```

描述

位姿类型。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_POSE_TYPE_IDENTITY | 默认状态，即没有任何旋转或平移。 |
| ARENGINE_POSE_TYPE_ROTATE_90 | 顺时针旋转90度。 |
| ARENGINE_POSE_TYPE_ROTATE_180 | 顺时针旋转180度。 |
| ARENGINE_POSE_TYPE_ROTATE_270 | 顺时针旋转270度。 |

**AREngine_ARPowerMode**

```ets
enum AREngine_ARPowerMode
```

描述

电源功耗模式。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_POWER_MODE_NORMAL | 正常模式，AR Engine在性能和电源消耗之间保持平衡。 |
| ARENGINE_POWER_MODE_POWER_SAVING | 节能模式，AR Engine优先减少电源消耗。这可能会降低一些性能，以换取更长的电池寿命。 |
| ARENGINE_POWER_MODE_PERFORMANCE_FIRST | 性能优先模式，AR Engine优先考虑性能，提供更高的处理能力和更快的响应时间。这可能会增加电源消耗。 |
| ARENGINE_POWER_MODE_BOOST | 仅输出设备姿态信息模式。功耗低于 ARENGINE_POWER_MODE_NORMAL模式下的功耗。在此模式下，与平面相关的设置（如：HMS_AREngine_ARConfig_SetPlaneFindingMode）不生效。 |
| ARENGINE_POWER_MODE_ULTRA_POWER_SAVING | 超级节能模式，AR Engine进一步优化电源消耗，提供比节能模式更低的电源消耗，这可能会损失更多的性能。 |

**AREngine_ARPreviewMode**

```ets
enum AREngine_ARPreviewMode
```

描述

预览模式。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_PREVIEW_MODE_ENABLED | 开启相机预览。 |
| ARENGINE_PREVIEW_MODE_DISABLED | 关闭相机预览，如：VR模式，不需要相机预览流。 在此模式下，通过HMS_AREngine_ARSession_SetCameraGLTexture接口设置的OpenGL纹理 将不会被更新。 |

**AREngine_ARSemanticDenseMode**

```ets
enum AREngine_ARSemanticDenseMode
```

描述

高精几何重建识别模式。

起始版本： 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_SEMANTIC_DENSE_MODE_DISABLED | 关闭高精几何重建识别模式。 |
| ARENGINE_SEMANTIC_DENSE_MODE_NORMAL | 正常模式，仅开启稠密点云识别。 |
| ARENGINE_SEMANTIC_DENSE_MODE_CUBE_VOLUME | 基于高精几何重建的立方体体积测量模式。 |
| ARENGINE_SEMANTIC_DENSE_MODE_CUBE_SPACE | 基于高精几何重建的立方体空间容积测量模式。 |

**AREngine_ARSemanticMode**

```ets
enum AREngine_ARSemanticMode
```

描述

语义模式。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_SEMANTIC_MODE_NONE | 不使用语义。 |
| ARENGINE_SEMANTIC_MODE_PLANE | 使用平面语义。 |
| ARENGINE_SEMANTIC_MODE_TARGET | 使用物体语义。 |

**AREngine_ARSemanticPlaneLabel**

```ets
enum AREngine_ARSemanticPlaneLabel
```

描述

当前平面识别到的语义类型。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_PLANE_UNKNOWN | 未知类型。 |
| ARENGINE_PLANE_WALL | 墙面。 |
| ARENGINE_PLANE_FLOOR | 地面。 |
| ARENGINE_PLANE_SEAT | 座椅。 |
| ARENGINE_PLANE_TABLE | 桌子。 |
| ARENGINE_PLANE_CEILING | 天花板。 |
| ARENGINE_PLANE_DOOR | 门。 |
| ARENGINE_PLANE_WINDOW | 窗户。 |
| ARENGINE_PLANE_BED | 床。 |
| ARENGINE_PLANE_SPACE | 平面空间。 起始版本： 6.0.0(20) |
| ARENGINE_CUBE_VOLUME | 立方体体积。 起始版本： 6.0.0(20) |
| ARENGINE_CUBE_SPACE | 立方体空间。 起始版本： 6.0.0(20) |

**AREngine_ARStatus**

```ets
enum AREngine_ARStatus
```

描述

接口返回错误码。

用于表示一个接口的调用状态。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_PERMISSION_NOT_GRANTED | 权限未授予状态。如相机权限未授予。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_DEVICE_NOT_SUPPORTED | 不可用：设备不兼容状态。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |
| ARENGINE_ERROR_SESSION_PAUSED | 会话已暂停状态。 |
| ARENGINE_ERROR_SESSION_NOT_PAUSED | 会话未暂停状态。 |
| ARENGINE_ERROR_NOT_TRACKING | 未跟踪状态。 |
| ARENGINE_ERROR_TEXTURE_NOT_SET | 未设置纹理状态。 |
| ARENGINE_ERROR_MISSING_GL_CONTEXT | 缺少GL上下文状态。 |
| ARENGINE_ERROR_UNSUPPORTED_CONFIGURATION | 不支持的配置状态。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |
| ARENGINE_ERROR_NOT_AVAILABLE | 服务不可用状态。 |
| ARENGINE_ERROR_CAMERA_NOT_AVAILABLE | 相机不可用状态。 |
| ARENGINE_ERROR_IMAGE_EXCEED_NUM_LIMIT | 添加的图片数量超过最大数量。 起始版本： 5.1.0(18) |
| ARENGINE_ERROR_IMAGE_INSUFFICIENT_QUALITY | 将质量不足的图像添加到图像数据库中。 起始版本： 5.1.0(18) |
| ARENGINE_ERROR_IMAGE_INVALID_DATABASE | 没有有效的图像数据库。 起始版本： 5.1.0(18) |
| ARENGINE_ERROR_IMAGE_ADD_IMAGE_TRACKING_STATE | 跟踪状态正在运行时无法添加图片。 起始版本： 5.1.0(18) |
| ARENGINE_ERROR_NATIVEBUFFER_CREATE_FAILED | 创建NativeBuffer失败。 起始版本： 6.0.0(20) |
| ARENGINE_ERROR_NATIVEBUFFER_WRITE_FAILED | 无法写入NativeBuffer。 起始版本： 6.0.0(20) |
| ARENGINE_CAMERA_SERVICE_FATAL_ERROR | 相机服务异常。 起始版本： 6.0.2(22) |

**AREngine_ARTargetShapeLabel**

```ets
enum AREngine_ARTargetShapeLabel
```

描述

识别到的物体形状。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_TARGET_SHAPE_UNKNOWN | 未知形状。 |
| ARENGINE_TARGET_SHAPE_CUBE | 立方体形状。可以识别规则物体的包围框。 |
| ARENGINE_TARGET_SHAPE_CIRCLE | 圆形形状。 |
| ARENGINE_TARGET_SHAPE_RECTANGLE | 矩形形状。 |

**AREngine_ARTrackableType**

```ets
enum AREngine_ARTrackableType
```

描述

可跟踪对象类型，如平面、点等。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_TRACKABLE_BASE | 基础可跟踪对象类型，可作为默认的AREngine_ARTrackableType类型。 |
| ARENGINE_TRACKABLE_PLANE | 平面类可跟踪对象类型。 |
| ARENGINE_TRACKABLE_POINT | 点类可跟踪对象类型。 |
| ARENGINE_TRACKABLE_AUGMENTED_IMAGE | 增强图像类型的可跟踪对象。 起始版本： 5.1.0(18) |
| ARENGINE_TRACKABLE_BODY | 人体追踪对象。 起始版本： 6.1.0(23) |
| ARENGINE_TRACKABLE_FACE | 人脸追踪对象。 起始版本： 6.1.0(23) |
| ARENGINE_TRACKABLE_TARGET | 物体类可跟踪对象类型。 |
| ARENGINE_TRACKABLE_INVALID | 无效的可跟踪对象类型。 |

**AREngine_ARTrackingState**

```ets
enum AREngine_ARTrackingState
```

描述

可跟踪对象的跟踪状态。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_TRACKING_STATE_TRACKING | 正在追踪。 |
| ARENGINE_TRACKING_STATE_PAUSED | 暂停追踪。 |
| ARENGINE_TRACKING_STATE_STOPPED | 停止追踪。 |

**AREngine_ARTrackingStateReason**

```ets
enum AREngine_ARTrackingStateReason
```

描述

可能的跟踪失败原因。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_TRACKING_STATE_REASON_NONE | 未知原因。这可能是由于系统暂时无法识别可追踪对象，但仍在尝试追踪。 |
| ARENGINE_TRACKING_STATE_REASON_EXCESSIVE_MOTION | 目标移动过快。可追踪对象（如平面、点、图像等）移动速度过快，导致AR Engine无法准确识别和跟踪。 |
| ARENGINE_TRACKING_STATE_REASON_INSUFFICIENT_FEATURES | 视觉特征不足（如弱纹理）。可追踪对象的视觉特征不够丰富，如纹理不明显、颜色过于单一等，导致AR Engine无法准确识别和跟踪。 |

**AREngine_ARType**

```ets
enum AREngine_ARType
```

描述

AR能力类型。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_TYPE_WORLD | 环境识别与运动跟踪。 |
| ARENGINE_TYPE_BODY | 人体骨骼识别与跟踪能力。 起始版本： 6.1.0(23) |
| ARENGINE_TYPE_FACE | 人脸识别与跟踪能力。 起始版本： 6.1.0(23) |
| ARENGINE_TYPE_IMAGE | 图像识别与跟踪跟踪能力。 起始版本： 5.1.0(18) |

**AREngine_ARUpdateMode**

```ets
enum AREngine_ARUpdateMode
```

描述

调用[HMS_AREngine_ARSession_Update](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arsession_update)方法后数据更新模式。

起始版本： 5.0.0(12)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_UPDATE_MODE_BLOCKING | HMS_AREngine_ARSession_Update方法在新的帧可用时才返回。 |
| ARENGINE_UPDATE_MODE_LATEST | HMS_AREngine_ARSession_Update方法立刻返回（如果没有新的帧，返回上一帧）。 |

**AREngine_ARBodySkeletonType**

```ets
enum AREngine_ARBodySkeletonType
```

描述

人体骨骼点类型。

起始版本： 6.1.0(23)

| 枚举值 | 描述 |
| --- | --- |
| ARENGINE_ARBODY_SKELETON_NECK | 颈部。 |
| ARENGINE_ARBODY_SKELETON_R_SHO | 右肩。 |
| ARENGINE_ARBODY_SKELETON_R_ELBOW | 右肘。 |
| ARENGINE_ARBODY_SKELETON_R_WRIST | 右腕。 |
| ARENGINE_ARBODY_SKELETON_L_SHO | 左肩。 |
| ARENGINE_ARBODY_SKELETON_L_ELBOW | 左肘。 |
| ARENGINE_ARBODY_SKELETON_L_WRIST | 左腕。 |
| ARENGINE_ARBODY_SKELETON_R_HIP | 右髋部。 |
| ARENGINE_ARBODY_SKELETON_R_KNEE | 右膝。 |
| ARENGINE_ARBODY_SKELETON_R_ANKLE | 右脚踝。 |
| ARENGINE_ARBODY_SKELETON_L_HIP | 左髋部。 |
| ARENGINE_ARBODY_SKELETON_L_KNEE | 左膝。 |
| ARENGINE_ARBODY_SKELETON_L_ANKLE | 左脚踝。 |
| ARENGINE_ARBODY_SKELETON_HIP_MID | 中髋部。 |
| ARENGINE_ARBODY_SKELETON_R_EAR | 右耳。 |
| ARENGINE_ARBODY_SKELETON_R_EYE | 右眼。 |
| ARENGINE_ARBODY_SKELETON_NOSE | 鼻子。 |
| ARENGINE_ARBODY_SKELETON_L_EYE | 左眼。 |
| ARENGINE_ARBODY_SKELETON_L_EAR | 左耳。 |
| ARENGINE_ARBODY_SKELETON_SPINE | 脊柱。 |

**函数说明**

**HMS_AREngine_CheckSupported**

```ets
AREngine_ARStatus HMS_AREngine_CheckSupported(AREngine_FeatureType type)
```

描述

判断AREngine中的某个特性是否在该设备上能够使用。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| type | AR特性类别AREngine_FeatureType对象。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_DEVICE_NOT_SUPPORTED | 当前设备不支持。 |

**HMS_AREngine_ARAnchor_Detach**

```ets
AREngine_ARStatus HMS_AREngine_ARAnchor_Detach(AREngine_ARSession *session, AREngine_ARAnchor *anchor)
```

描述

通知AR Engine停止跟踪并解绑一个锚点。

但是该函数并不会释放该锚点，这需要通过[HMS_AREngine_ARAnchor_Release](#ZH-CN_TOPIC_0000002553362039__hms_arengine_aranchor_release)单独来实现。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| anchor | 待解绑的锚点对象，参见AREngine_ARAnchor。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARAnchor_GetPose**

```ets
AREngine_ARStatus HMS_AREngine_ARAnchor_GetPose(const AREngine_ARSession *session, const AREngine_ARAnchor *anchor, AREngine_ARPose *outPose)
```

描述

获取指定锚点在世界坐标系中的位姿信息。

当每次调用[HMS_AREngine_ARSession_Update](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arsession_update)的时候，[HMS_AREngine_ARAnchor_GetPose](#ZH-CN_TOPIC_0000002553362039__hms_arengine_aranchor_getpose)返回的位姿信息可能会发生变化。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| anchor | 待检索位姿的锚点，参见AREngine_ARAnchor。 |
| outPose | 返回锚点对应的位姿对象，参见AREngine_ARPose。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARAnchor_GetTrackingState**

```ets
AREngine_ARStatus HMS_AREngine_ARAnchor_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARAnchor *anchor, AREngine_ARTrackingState *outTrackingState)
```

描述

获取指定锚点位姿的追踪状态。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| anchor | 待获取追踪状态的锚点，参见AREngine_ARAnchor。 |
| outTrackingState | 返回锚点当前位姿的追踪状态，参见AREngine_ARTrackingState。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARAnchor_Release**

```ets
void HMS_AREngine_ARAnchor_Release(AREngine_ARAnchor *anchor)
```

描述

释放指定锚点对象的内存。

释放前需要先通知AR Engine停止跟踪并解绑锚点，参见[HMS_AREngine_ARAnchor_Detach](#ZH-CN_TOPIC_0000002553362039__hms_arengine_aranchor_detach)。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| anchor | 待释放的锚点对象，参见AREngine_ARAnchor。 |

**HMS_AREngine_ARAnchorList_AcquireItem**

```ets
AREngine_ARStatus HMS_AREngine_ARAnchorList_AcquireItem(const AREngine_ARSession *session, const AREngine_ARAnchorList *anchorList, int32_t index, AREngine_ARAnchor **outAnchor)
```

描述

从锚点对象列表中获取指定位置的锚点信息。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| anchorList | 被检索的锚点对象列表，参见AREngine_ARAnchorList。 |
| index | 需要获取的锚点在锚点对象列表中的位置，最小为0，最大为49。 |
| outAnchor | 待返回的锚点信息，参见AREngine_ARAnchor。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAnchorList_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARAnchorList_Create(const AREngine_ARSession *session, AREngine_ARAnchorList **outAnchorList)
```

描述

创建一个锚点对象列表。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outAnchorList | 待创建的锚点对象列表引用，参见AREngine_ARAnchorList。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARAnchorList_Destroy**

```ets
void HMS_AREngine_ARAnchorList_Destroy(AREngine_ARAnchorList *anchorList)
```

描述

释放一个锚点对象列表。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| anchorList | 待释放的锚点列表对象，参见AREngine_ARAnchorList。 |

**HMS_AREngine_ARAnchorList_GetSize**

```ets
AREngine_ARStatus HMS_AREngine_ARAnchorList_GetSize(const AREngine_ARSession *session, const AREngine_ARAnchorList *anchorList, int32_t *outSize)
```

描述

获取锚点对象列表中包含锚点的数量。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| anchorList | 锚点对象列表，参见AREngine_ARAnchorList。 |
| outSize | 返回锚点对象列表中锚点的数量。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAugmentedImage_AcquireName**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImage_AcquireName(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, char *augmentedImageName, uint32_t *outNameLength)
```

描述

返回跟踪图像的名称。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| augmentedImage | 图像类型的可追踪对象，参见AREngine_ARAugmentedImage。 |
| augmentedImageName | 图像名称，不能超过255字节。 |
| outNameLength | 返回图像名称长度。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAugmentedImage_GetCenterPose**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, AREngine_ARPose *outPose)
```

描述

获取跟踪图像中心点在世界坐标系中的位姿信息。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| augmentedImage | 图像类型的可追踪对象，参见AREngine_ARAugmentedImage。 |
| outPose | 返回跟踪图像的位姿，参见AREngine_ARPose。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAugmentedImage_GetExtendX**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetExtendX(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, float *outExtendX)
```

描述

以图像的中心点为坐标原点，获取X轴上的估计值。

返回物理图像的长度，单位为m。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| augmentedImage | 图像类型的可追踪对象，参见AREngine_ARAugmentedImage。 |
| outExtendX | 返回X轴上物理图像的估计长度，以m为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAugmentedImage_GetExtendZ**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetExtendZ(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, float *outExtendZ)
```

描述

以图像的中心点为坐标原点，获取Z轴上的估计值。

返回物理图像的宽度，单位为m。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| augmentedImage | 图像类型的可追踪对象，参见AREngine_ARAugmentedImage。 |
| outExtendZ | 返回Z轴上物理图像的估计宽度，以m为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAugmentedImage_GetIndex**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetIndex(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, uint32_t *outIndex)
```

描述

获取跟踪图像数据库中跟踪图像的索引。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| augmentedImage | 图像类型的可追踪对象，参见AREngine_ARAugmentedImage。 |
| outIndex | 返回图像的索引。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAugmentedImageDatabase_AddImage**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_AddImage(AREngine_ARAugmentedImageDatabase *database, const AREngine_ARAugmentedImageSource *image, uint32_t *outIndex, AREngine_ARAddAugmentedImageReason *outReason)
```

描述

将图像添加到图像数据库并输出对应图像的索引。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见AREngine_ARAugmentedImageDatabase。 |
| image | 图像信息，参见AREngine_ARAugmentedImageSource。 |
| outIndex | 返回添加图像的索引。 |
| outReason | 返回添加图片失败的原因，参见AREngine_ARAddAugmentedImageReason。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |
| ARENGINE_ERROR_IMAGE_EXCEED_NUM_LIMIT | 添加的图片数量超过最大数量。 起始版本： 5.1.0(18) |
| ARENGINE_ERROR_IMAGE_INSUFFICIENT_QUALITY | 将质量不足的图像添加到图像数据库中。 起始版本： 5.1.0(18) |

**HMS_AREngine_ARAugmentedImageDatabase_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Create(AREngine_ARAugmentedImageDatabase **outDatabase)
```

描述

创建一个空的跟踪图像数据库。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| outDatabase | 返回指向要创建的图像库的指针，参见AREngine_ARAugmentedImageDatabase。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARAugmentedImageDatabase_Deserialize**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Deserialize(const uint8_t *buffer, const uint64_t bufSize, AREngine_ARAugmentedImageDatabase **outDatabase)
```

描述

反序列化特征数据库。

用户可以将上次生成的或者保存的buffer数据反序列化为特征数据库后直接使用。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| buffer | 跟踪图像数据库缓冲区。 |
| bufSize | 跟踪图像数据库缓冲区大小，最大不超过int64类型长度。 |
| outDatabase | 返回跟踪图像数据库，参见AREngine_ARAugmentedImageDatabase。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARAugmentedImageDatabase_Destroy**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Destroy(AREngine_ARAugmentedImageDatabase *database)
```

描述

释放图像数据库对象。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见AREngine_ARAugmentedImageDatabase。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAugmentedImageDatabase_GetAddMode**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetAddMode(const AREngine_ARAugmentedImageDatabase *database, AREngine_ARImageDatabaseMode *outAddMode)
```

描述

获取添加跟踪图像模式。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见AREngine_ARAugmentedImageDatabase。 |
| outAddMode | 返回添加跟踪图像模式。参见AREngine_ARImageDatabaseMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAugmentedImageDatabase_SetAddMode**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_SetAddMode(const AREngine_ARAugmentedImageDatabase *database, AREngine_ARImageDatabaseMode addMode)
```

描述

设置添加跟踪图像模式。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见AREngine_ARAugmentedImageDatabase。 |
| addMode | 添加跟踪图像模式。参见AREngine_ARImageDatabaseMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAugmentedImageDatabase_GetCapacity**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetCapacity(const AREngine_ARAugmentedImageDatabase *database, uint32_t *outCapacity)
```

描述

获取可以添加的最大图像数。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见AREngine_ARAugmentedImageDatabase。 |
| outCapacity | 返回最大图像数，默认为50。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARAugmentedImageDatabase_GetImageCount**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetImageCount(const AREngine_ARAugmentedImageDatabase *database, uint32_t *outImageCount)
```

描述

获取数据库中存储的图像数量。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见AREngine_ARAugmentedImageDatabase。 |
| outImageCount | 返回图像数量。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARAugmentedImageDatabase_Serialize**

```ets
AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Serialize(const AREngine_ARAugmentedImageDatabase *database, uint8_t **outBuffer, uint64_t *outBufSize)
```

描述

序列化特征数据库。

在添加完图片后，可以将特征库序列化为buffer，开发者可以保存此buffer以供下次使用。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| database | 跟踪图像数据库，参见AREngine_ARAugmentedImageDatabase。 |
| outBuffer | 返回跟踪图像数据库缓冲区。 |
| outBufSize | 返回跟踪图像数据库缓冲区大小。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARCamera_GetDisplayOrientedPose**

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetDisplayOrientedPose(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARPose *outPose)
```

描述

设置outPose为虚拟相机（面向显示）在世界空间中的位姿，用以将AR内容渲染到最新帧中。

该位姿是OpenGL相机的位姿，其中X轴正方向为右，Y轴正方向为上，Z轴负方向为相机的观察方向。相机位置即物理相机位置，而相机X轴与Y轴指向受屏幕方向（考虑显示旋转）的影响。

该位姿信息应该在[HMS_AREngine_ARCamera_GetTrackingState](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arcamera_gettrackingstate)返回[ARENGINE_TRACKING_STATE_TRACKING](#ZH-CN_TOPIC_0000002553362039__arengine_artrackingstate)状态的时候才能使用。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| camera | Session对应的相机，参见AREngine_ARCamera。 |
| outPose | 返回虚拟相机在世界空间中的位姿，参见AREngine_ARPose。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCamera_GetImageIntrinsics**

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetImageIntrinsics(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARCameraIntrinsics *outIntrinsics)
```

描述

获取物理相机离线内参的对象，可通过该对象获取相机的焦距、图像尺寸、主轴点和畸变参数。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| camera | Session对应的相机，参见AREngine_ARCamera。 |
| outIntrinsics | 返回相机物理内参对象，参见AREngine_ARCameraIntrinsics。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARCamera_GetPose**

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetPose(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARPose *outPose)
```

描述

设置outPose为最新帧中物理相机在世界空间中的位姿。该位姿是OpenGL相机的位姿。

其中X轴正方向为右，Y轴正方向为上，Z轴负方向为相机的观察方向。相机位置即物理相机位置，而相机X轴与Y轴指向不受屏幕方向（考虑显示旋转）的影响。

该位姿信息应该在[HMS_AREngine_ARCamera_GetTrackingState](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arcamera_gettrackingstate)返回[ARENGINE_TRACKING_STATE_TRACKING](#ZH-CN_TOPIC_0000002553362039__arengine_artrackingstate)状态的时候才能使用。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| camera | Session对应的相机，参见AREngine_ARCamera。 |
| outPose | 物理相机在世界空间中的位姿，参见AREngine_ARPose。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCamera_GetProjectionMatrix**

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetProjectionMatrix(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ClipPlaneDistance clipPlaneDistance, float *outDestColMajor4x4, int32_t destColMajor4x4Num)
```

描述

获取用于在相机图像上层渲染虚拟内容的投影矩阵，可用于相机坐标系到裁剪坐标系转换。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| camera | Session对应的相机，参见AREngine_ARCamera。 |
| clipPlaneDistance | OpenGL裁剪平面距离，参见AREngine_ClipPlaneDistance。 |
| outDestColMajor4x4 | 返回一个由16个浮点数组成的数组，其中的数据表示OpenGL中以列为主的均匀变换矩阵。 |
| destColMajor4x4Num | 数组大小：ARENGINE_VIEW_MATRIX_SIZE。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARCamera_GetTrackingState**

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARTrackingState *outTrackingState)
```

描述

获取相机的当前追踪状态。

只有当该状态为[ARENGINE_TRACKING_STATE_TRACKING](#ZH-CN_TOPIC_0000002553362039__arengine_artrackingstate)时，相机的位姿才可用。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| camera | Session对应的相机，参见AREngine_ARCamera。 |
| outTrackingState | 返回当前相机的追踪状态，参见AREngine_ARTrackingState。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCamera_GetTrackingStateReason**

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetTrackingStateReason(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARTrackingStateReason *outTrackingStateReason)
```

描述

获取相机的当前追踪状态为[ARENGINE_TRACKING_STATE_PAUSED](#ZH-CN_TOPIC_0000002553362039__arengine_artrackingstate)时的原因。

当相机的当前追踪状态为[ARENGINE_TRACKING_STATE_TRACKING](#ZH-CN_TOPIC_0000002553362039__arengine_artrackingstate)时，该函数返回[ARENGINE_TRACKING_STATE_REASON_NONE](#ZH-CN_TOPIC_0000002553362039__arengine_artrackingstatereason)。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| camera | Session对应的相机，参见AREngine_ARCamera。 |
| outTrackingStateReason | 返回跟踪失败的原因，参见AREngine_ARTrackingStateReason。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCamera_GetViewMatrix**

```ets
AREngine_ARStatus HMS_AREngine_ARCamera_GetViewMatrix(const AREngine_ARSession *session, const AREngine_ARCamera *camera, float *outColMajor4x4, int32_t colMajor4x4Num)
```

描述

获取最新帧中相机的视图矩阵。

此矩阵执行了[HMS_AREngine_ARCamera_GetDisplayOrientedPose](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arcamera_getdisplayorientedpose)提供的Pose的逆变换，即从世界坐标系转为相机坐标系。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| camera | Session对应的相机，参见AREngine_ARCamera。 |
| outColMajor4x4 | 返回一个由16个浮点数组成的数组，其中的数据表示OpenGL中以列为主的均匀变换矩阵。 |
| colMajor4x4Num | 数组大小。数组大小定义大于等于ARENGINE_VIEW_MATRIX_SIZE。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCamera_Release**

```ets
void HMS_AREngine_ARCamera_Release(AREngine_ARCamera *camera)
```

描述

释放对相机的引用。

当调用了[HMS_AREngine_ARFrame_AcquireCamera](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arframe_acquirecamera)时，需要相应的调用[HMS_AREngine_ARCamera_Release](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arcamera_release)。

当没有[HMS_AREngine_ARFrame_AcquireCamera](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arframe_acquirecamera)时，调用该方法无效。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| camera | 待释放的相机引用，参见AREngine_ARCamera。 |

**HMS_AREngine_ARCameraConfig_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARCameraConfig_Create(const AREngine_ARSession *session, AREngine_ARCameraConfig **outCameraConfig)
```

描述

创建一个相机配置对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outCameraConfig | 返回一个指向新分配的相机配置对象地址的指针，参见AREngine_ARCameraConfig。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARConfig_GetCameraLensFacing**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetCameraLensFacing(const AREngine_ARSession *session,const AREngine_ARConfig *config, AREngine_ARCameraLensFacing *outFacing)
```

描述

获取相机镜头朝向。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向包含目标配置信息的配置对象，参见AREngine_ARConfig。 |
| outFacing | 相机镜头朝向，参见AREngine_ARCameraLensFacing。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetMultiFaceMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetMultiFaceMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMultiFaceMode *outFaceMode)
```

描述

获取多人脸检测模式。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向包含目标配置信息的配置对象，参见AREngine_ARConfig。 |
| outFaceMode | 多人脸检测模式，参见AREngine_ARMultiFaceMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetCameraLensFacing**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetCameraLensFacing(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARCameraLensFacing facing)
```

描述

设置相机镜头朝向。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向包含目标配置信息的配置对象，参见AREngine_ARConfig。 |
| facing | 设置相机镜头朝向，参见AREngine_ARCameraLensFacing。facing设置为ARENGINE_CAMERA_FACING_FRONT时，需要调用HMS_AREngine_ARConfig_SetARType将AR能力类型设置为ARENGINE_TYPE_FACE或ARENGINE_TYPE_BODY才生效。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetMultiFaceMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetMultiFaceMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMultiFaceMode faceMode)
```

描述

设置多人脸检测模式。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向包含目标配置信息的配置对象，参见AREngine_ARConfig。 |
| faceMode | 多人脸检测模式，参见AREngine_ARMultiFaceMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCameraConfig_Destroy**

```ets
void HMS_AREngine_ARCameraConfig_Destroy(AREngine_ARCameraConfig *cameraConfig)
```

描述

释放相机配置对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| cameraConfig | 待释放的指向相机配置对象的指针，参见AREngine_ARCameraConfig。 |

**HMS_AREngine_ARCameraConfig_GetImageDimensions**

```ets
AREngine_ARStatus HMS_AREngine_ARCameraConfig_GetImageDimensions(const AREngine_ARSession *session, const AREngine_ARCameraConfig *cameraConfig, int32_t *outWidth, int32_t *outHeight)
```

描述

从相机配置对象中获取相机送到CPU处理的图像尺寸。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| cameraConfig | 指向相机配置对象的指针，参见AREngine_ARCameraConfig。 |
| outWidth | 返回图像的宽度，以像素为单位。 |
| outHeight | 返回图像的高度，以像素为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCameraConfig_GetTextureDimensions**

```ets
AREngine_ARStatus HMS_AREngine_ARCameraConfig_GetTextureDimensions(const AREngine_ARSession *session, const AREngine_ARCameraConfig *cameraConfig, int32_t *outWidth, int32_t *outHeight)
```

描述

从相机配置对象中获取相机送到GPU处理的图像纹理尺寸。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| cameraConfig | 指向相机配置对象的指针，参见AREngine_ARCameraConfig。 |
| outWidth | 返回图像纹理的宽度，以像素为单位。 |
| outHeight | 返回图像纹理的高度，以像素为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCameraIntrinsics_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_Create(const AREngine_ARSession *session, AREngine_ARCameraIntrinsics **outIntrinsics)
```

描述

创建一个相机内参对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outIntrinsics | 返回一个指向新分配的相机内参对象地址的指针，参见AREngine_ARCameraIntrinsics。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARCameraIntrinsics_Destroy**

```ets
void HMS_AREngine_ARCameraIntrinsics_Destroy(AREngine_ARCameraIntrinsics *intrinsics)
```

描述

释放指定的相机内参对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| intrinsics | 待释放的相机内参对象，参见AREngine_ARCameraIntrinsics。 |

**HMS_AREngine_ARCameraIntrinsics_GetDistortion**

```ets
AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetDistortion(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outDistortion, int32_t distortionNum)
```

描述

获取相机的畸变系数。

包含5个分量，其中outDistortion[0]outDistortion [2]表示k1，k2，k3（径向畸变系数），outDistortion [3]outDistortion [4]是切向畸变系数。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| intrinsics | 指向相机内参对象的指针，参见AREngine_ARCameraIntrinsics。 |
| outDistortion | 返回相机畸变参数数组。 |
| distortionNum | 相机畸变参数的个数，参见ARENGINE_DISTORTION_COUNT。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCameraIntrinsics_GetFocalLength**

```ets
AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetFocalLength(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outFocalX, float *outFocalY)
```

描述

获取指定相机的焦距，焦距以像素为单位。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| intrinsics | 指向相机内参对象的指针，参见AREngine_ARCameraIntrinsics。 |
| outFocalX | 返回相机内参矩阵x(u)方向的像素焦距。 |
| outFocalY | 返回相机内参矩阵y(v)方向的像素焦距。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCameraIntrinsics_GetImageDimensions**

```ets
AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetImageDimensions(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, int32_t *outWidth, int32_t *outHeight)
```

描述

获取相机图像的尺寸，包括宽度和高度，以像素为单位。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| intrinsics | 指向相机内参对象的指针，参见AREngine_ARCameraIntrinsics。 |
| outWidth | 返回相机图像的宽度，以像素为单位。 |
| outHeight | 返回相机图像的高度，以像素为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARCameraIntrinsics_GetPrincipalPoint**

```ets
AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetPrincipalPoint(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outPrincipalX, float *outPrincipalY)
```

描述

获取指定相机的主轴点，主点位置以像素为单位表示。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| intrinsics | 指向相机内参对象的指针，参见AREngine_ARCameraIntrinsics。 |
| outPrincipalX | 返回相机X方向的主轴点坐标。 |
| outPrincipalY | 返回相机Y方向的主轴点坐标。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_Create(const AREngine_ARSession *session, AREngine_ARConfig **outConfig)
```

描述

创建具有适当默认配置的配置对象。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outConfig | 返回一个指向新分配的配置对象地址的指针，参见AREngine_ARConfig。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARConfig_Destroy**

```ets
void HMS_AREngine_ARConfig_Destroy(AREngine_ARConfig *config)
```

描述

释放指定的配置对象的内存空间。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| config | 待释放的配置对象，参见AREngine_ARConfig。 |

**HMS_AREngine_ARConfig_GetARType**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetARType(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARType *type)
```

描述

获取当前使用的AR能力类型。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| type | 返回AR Engine当前使用的能力类型，参见AREngine_ARType。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetCameraPreviewMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetCameraPreviewMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPreviewMode *outMode)
```

描述

获取当前的预览模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| outMode | 返回相机预览模式，参见AREngine_ARPreviewMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetDepthMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetDepthMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARDepthMode *outDepthMode)
```

描述

获取当前的深度模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.5(17)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| outDepthMode | 返回当前深度模式，参见AREngine_ARDepthMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetFocusMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetFocusMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARFocusMode *focusMode)
```

描述

获取当前配置的相机对焦模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| focusMode | 返回当前对焦模式，参见AREngine_ARFocusMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetMaxMapSize**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetMaxMapSize(const AREngine_ARSession *session, const AREngine_ARConfig *config, uint64_t *maxMapSize)
```

描述

获取地图数据使用的最大内存大小。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

在执行[HMS_AREngine_ARSession_Configure](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arsession_configure)后，可通过此接口获取当前设置的地图数据最大使用内存大小。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| maxMapSize | 返回目前生效的地图数据最大使用内存大小，单位MB。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetMeshMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetMeshMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMeshMode *outMeshMode)
```

描述

获取当前mesh模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| outMeshMode | 返回mesh模式，参见AREngine_ARMeshMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetPlaneFindingMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetPlaneFindingMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPlaneFindingMode *planeFindingMode)
```

描述

获取当前配置的平面识别模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| planeFindingMode | 返回当前平面识别模式，参见AREngine_ARPlaneFindingMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetPoseMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetPoseMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPoseMode *poseMode)
```

描述

获取相机输出的位姿坐标系对齐模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| poseMode | 相机位姿模式，参见AREngine_ARPoseMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetPowerMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetPowerMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPowerMode *powerMode)
```

描述

获取当前配置的功耗模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| powerMode | 返回当前功耗模式，参见AREngine_ARPowerMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetSemanticDenseMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetSemanticDenseMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARSemanticDenseMode *outSemanticDenseMode)
```

描述

获取已设置的高精几何重建模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.0(20)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| outSemanticDenseMode | 返回当前高精几何重建模式，参见AREngine_ARSemanticDenseMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetSemanticMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetSemanticMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARSemanticMode *mode)
```

描述

获取已设置成功的语义识别模式。

该方法在[HMS_AREngine_ARConfig_SetSemanticMode](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arconfig_setsemanticmode)后调用有效。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| mode | 返回当前语义模式，参见AREngine_ARSemanticMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetUpdateMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetUpdateMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARUpdateMode *updateMode)
```

描述

获取当前配置的预览更新模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| updateMode | 返回当前预览更新模式，参见AREngine_ARUpdateMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetARType**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetARType(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARType type)
```

描述

设置当前要使用的AR能力类型。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| type | AR Engine支持的能力类型，参见AREngine_ARType。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_UNSUPPORTED_CONFIGURATION | 不支持的配置状态。 |

**HMS_AREngine_ARConfig_SetCameraPreviewMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetCameraPreviewMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPreviewMode mode)
```

描述

设置预览模式。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| mode | 相机预览模式，参见AREngine_ARPreviewMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetDepthMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetDepthMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARDepthMode depthMode)
```

描述

设置深度模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.5(17)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| depthMode | 深度图像模式，参见AREngine_ARDepthMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetFocusMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetFocusMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARFocusMode focusMode)
```

描述

设置当前所需的相机对焦模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| focusMode | 对焦模式，参见AREngine_ARFocusMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetMaxMapSize**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetMaxMapSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint64_t maxMapSize)
```

描述

设置地图数据最大使用内存大小。

若配置的地图数据最大使用内存范围不合法，则配置最接近用户配置的有效值，默认最大使用内存大小800MB。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| maxMapSize | 地图数据最大使用内存大小，单位MB，范围：100MB~16G。 若设备内存占用超过设备硬件限制，可能出现不可预知错误，需要应用侧自行评估设置的内存大小。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetMeshMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetMeshMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARMeshMode meshMode)
```

描述

设置mesh模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| meshMode | mesh模式，参见AREngine_ARMeshMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetPlaneFindingMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetPlaneFindingMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPlaneFindingMode planeFindingMode)
```

描述

设置当前所需的平面识别模式。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| planeFindingMode | 平面识别模式，参见AREngine_ARPlaneFindingMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetPoseMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetPoseMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPoseMode poseMode)
```

描述

设置相机输出的位姿坐标系对齐模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| poseMode | 相机位姿模式，参见AREngine_ARPoseMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetPowerMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetPowerMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPowerMode powerMode)
```

描述

设置功耗模式。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| powerMode | 功耗模式，参见AREngine_ARPowerMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetPreviewSize**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetPreviewSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint32_t width, uint32_t height)
```

描述

设置预览画面尺寸。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| width | 预览画面的宽，以像素为单位。可调用OH_CameraManager_GetSupportedCameraOutputCapability查看。 |
| height | 预览画面的高，以像素为单位。可调用OH_CameraManager_GetSupportedCameraOutputCapability查看。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetSemanticDenseMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetSemanticDenseMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARSemanticDenseMode semanticDenseMode)
```

描述

设置当前所需的高精几何重建模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.0(20)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| semanticDenseMode | 高精几何重建模式，参见AREngine_ARSemanticDenseMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetSemanticMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetSemanticMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARSemanticMode mode)
```

描述

设置当前所需的语义识别模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| mode | 语义模式，参见AREngine_ARSemanticMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetUpdateMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetUpdateMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARUpdateMode updateMode)
```

描述

设置预览更新模式。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| updateMode | 预览更新模式，参见AREngine_ARUpdateMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetPhotoStreamSize**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetPhotoStreamSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint32_t width, uint32_t height)
```

描述

当[AREngine_ARImageStreamMode](#ZH-CN_TOPIC_0000002553362039__arengine_arimagestreammode)为ARENGINE_IMAGE_STREAM_MODE_PREVIEW_AND_PHOTO时，设置从拍照流获取图像的分辨率。仅支持4:3大小分辨率。如果超出这个范围，系统会自动设置图像分辨率为该设备在4:3宽高比下的最高分辨率。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.2(22)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| width | 拍照流图像分辨率的宽，以像素为单位。可调用OH_CameraManager_GetSupportedCameraOutputCapability查询设备支持的数值。 |
| height | 拍照流图像分辨率的宽，以像素为单位。可调用OH_CameraManager_GetSupportedCameraOutputCapability查询设备支持的数值。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetImageStreamMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetImageStreamMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARImageStreamMode mode)
```

描述

设置图像流模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.2(22)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| mode | 图像流模式，参见AREngine_ARImageStreamMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_GetImageStreamMode**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_GetImageStreamMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARImageStreamMode *outMode)
```

描述

获取图像流模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.2(22)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| outMode | 图像流模式，参见AREngine_ARImageStreamMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFace_AcquireBlendShapes**

```ets
AREngine_ARStatus HMS_AREngine_ARFace_AcquireBlendShapes(const AREngine_ARSession *session, const AREngine_ARFace *face, AREngine_ARFaceBlendShapes **outBlendshapes)
```

描述

获取人脸微表情对象。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| face | 当前人脸对象，参见AREngine_ARFace。 |
| outBlendshapes | 当前人脸的微表情对象，参见AREngine_ARFaceBlendShapes。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARFace_AcquireGeometry**

```ets
AREngine_ARStatus HMS_AREngine_ARFace_AcquireGeometry(const AREngine_ARSession *session, const AREngine_ARFace *face, AREngine_ARFaceGeometry **outGeometry)
```

描述

获取人脸拓扑结构对象，即人脸Mesh对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| face | 当前人脸对象，参见AREngine_ARFace。 |
| outGeometry | 当前人脸的拓扑结构对象，参见AREngine_ARFaceGeometry。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARFace_AcquireLandmark**

```ets
AREngine_ARStatus HMS_AREngine_ARFace_AcquireLandmark(const AREngine_ARSession *session, const AREngine_ARFace *face, AREngine_ARFaceLandmark **outLandmark)
```

描述

获取人脸关键点对象。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| face | 当前人脸对象，参见AREngine_ARFace。 |
| outLandmark | 当前人脸的关键点对象，参见AREngine_ARFaceLandmark。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARFace_AcquireViewMatrix**

```ets
AREngine_ARStatus HMS_AREngine_ARFace_AcquireViewMatrix(const AREngine_ARSession *session, const AREngine_ARFace *face, float *outColMajor4x4, int32_t colMajor4x4Num)
```

描述

获取当前人脸的面视图矩阵。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| face | 当前人脸对象，参见AREngine_ARFace。 |
| outColMajor4x4 | 当前人脸的视角视图矩阵数据。由16个浮点数组成的数组，表示OpenGL中的列主序统一变换矩阵。 |
| colMajor4x4Num | outColMajor4x4 的大小。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFace_GetCenterPose**

```ets
AREngine_ARStatus HMS_AREngine_ARFace_GetCenterPose(const AREngine_ARSession *session,const AREngine_ARFace *face, AREngine_ARPose *outPose)
```

描述

获取人脸Mesh中心的位姿。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| face | 当前人脸对象，参见AREngine_ARFace。 |
| outPose | 人脸的中心位姿信息，参见AREngine_ARPose。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceBlendShapes_AcquireData**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceBlendShapes_AcquireData(const AREngine_ARSession *session, const AREngine_ARFaceBlendShapes *blendshapes, const float **outData)
```

描述

获取所有的微表情参数。

起始版本： 6.1.0(23)

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| blendshapes | 当前人脸的微表情对象，参见AREngine_ARFaceBlendShapes。 |
| outData | 人脸微表情参数的集合。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceBlendShapes_AcquireTypes**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceBlendShapes_AcquireTypes(const AREngine_ARSession *session, const AREngine_ARFaceBlendShapes *blendshapes, const AREngine_ARAnimojiBlendShape **types)
```

描述

获取所有微表情参数类型。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| blendshapes | 当前人脸的微表情对象，参见AREngine_ARFaceBlendShapes。 |
| types | 人脸微表情类型集合，参见AREngine_ARAnimojiBlendShape。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceBlendShapes_GetCount**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceBlendShapes_GetCount(const AREngine_ARSession *session, const AREngine_ARFaceBlendShapes *blendshapes, int32_t *outSize)
```

描述

获取微表情参数个数。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| blendshapes | 当前人脸的微表情对象，参见AREngine_ARFaceBlendShapes。 |
| outSize | 人脸微表情参数个数。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceBlendShapes_Release**

```ets
void HMS_AREngine_ARFaceBlendShapes_Release(AREngine_ARFaceBlendShapes *blendshapes)
```

描述

释放blendShapes对象，即由[HMS_AREngine_ARFace_AcquireBlendShapes](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arface_acquireblendshapes)创建的对象。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| blendshapes | 当前人脸微表情对象，参见AREngine_ARFaceBlendShapes。 |

**HMS_AREngine_ARFaceGeometry_AcquireIndices**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireIndices(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t **data)
```

描述

获取人脸Mesh三角面下标数组。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| geometry | 当前人脸Mesh对象，参见AREngine_ARFaceGeometry。 |
| data | 三角形索引集合。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceGeometry_AcquireTexCoord**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireTexCoord(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, const float **outData)
```

描述

获取人脸Mesh纹理坐标点数组。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| geometry | 当前人脸Mesh对象，参见AREngine_ARFaceGeometry。 |
| outData | 人脸Mesh纹理坐标集。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceGeometry_AcquireTriangleLabels**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireTriangleLabels(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, const AREngine_ARAnimojiTriangleLabel **data)
```

描述

获取人脸Mesh三角面标签。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| geometry | 当前人脸Mesh对象，参见AREngine_ARFaceGeometry。 |
| data | 三角形面标签的集合，参见AREngine_ARAnimojiTriangleLabel。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceGeometry_AcquireVertices**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceGeometry_AcquireVertices(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, const float **outData)
```

描述

获取人脸Mesh顶点数组。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| geometry | 当前人脸Mesh对象，参见AREngine_ARFaceGeometry。 |
| outData | 顶点集合，格式为 [x0, y0, z0, x1, y1, z1,...]。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceGeometry_GetIndicesSize**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetIndicesSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize)
```

描述

获取人脸Mesh三角面下标数组大小。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| geometry | 当前人脸Mesh对象，参见AREngine_ARFaceGeometry。 |
| outSize | 三角形索引数组的大小。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceGeometry_GetTexCoordSize**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetTexCoordSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize)
```

描述

获取人脸Mesh纹理坐标点数组大小。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| geometry | 当前人脸Mesh对象，参见AREngine_ARFaceGeometry。 |
| outSize | 纹理坐标数组的大小。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceGeometry_GetTriangleCount**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetTriangleCount(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize)
```

描述

获取人脸Mesh三角面个数。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| geometry | 当前人脸Mesh对象，参见AREngine_ARFaceGeometry。 |
| outSize | 三角形面数量。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceGeometry_GetTriangleLabelsSize**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetTriangleLabelsSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize)
```

描述

获取人脸Mesh三角面标签个数。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| geometry | 当前人脸Mesh对象，参见AREngine_ARFaceGeometry。 |
| outSize | 三角面标签的个数。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceGeometry_GetVerticesSize**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceGeometry_GetVerticesSize(const AREngine_ARSession *session, const AREngine_ARFaceGeometry *geometry, int32_t *outSize)
```

描述

获取人脸Mesh顶点数组大小。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| geometry | 当前人脸Mesh对象，参见AREngine_ARFaceGeometry。 |
| outSize | 人脸Mesh顶点数量。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceGeometry_Release**

```ets
void HMS_AREngine_ARFaceGeometry_Release(AREngine_ARFaceGeometry *geometry)
```

描述

释放当前人脸几何体对象，即由 [HMS_AREngine_ARFace_AcquireGeometry](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arface_acquiregeometry)创建的对象。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| geometry | 当前人脸Mesh对象，参见AREngine_ARFaceGeometry。 |

**HMS_AREngine_ARFaceLandmark_AcquireVertices2D**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceLandmark_AcquireVertices2D(const AREngine_ARSession *session, const AREngine_ARFaceLandmark *landmark, const float **outData)
```

描述

获取人脸关键点的2D位姿信息。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| landmark | 当前人脸的关键点对象，参见AREngine_ARFaceLandmark。 |
| outData | 人脸关键点2D位姿信息。 |

**HMS_AREngine_ARFaceLandmark_AcquireVertices3D**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceLandmark_AcquireVertices3D(const AREngine_ARSession *session, const AREngine_ARFaceLandmark *landmark, const float **outData)
```

描述

获取人脸关键点的3D位姿信息。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| landmark | 当前人脸的关键点对象，参见AREngine_ARFaceLandmark。 |
| outData | 人脸关键点3D位姿信息。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceLandmark_GetCount**

```ets
AREngine_ARStatus HMS_AREngine_ARFaceLandmark_GetCount(const AREngine_ARSession *session, const AREngine_ARFaceLandmark *landmark, int32_t *outSize)
```

描述

获取人脸关键点个数。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| landmark | 当前人脸的关键点对象，参见AREngine_ARFaceLandmark。 |
| outSize | 人脸关键点个数。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFaceLandmark_Release**

```ets
void HMS_AREngine_ARFaceLandmark_Release(AREngine_ARFaceLandmark *landmark)
```

描述

释放landmark对象，即由[HMS_AREngine_ARFace_AcquireLandmark](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arface_acquirelandmark)创建的对象。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| landmark | 当前人脸的关键点对象，参见AREngine_ARFaceLandmark。 |

**HMS_AREngine_ARFrame_AcquireCamera**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCamera(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARCamera **outCamera)
```

描述

获取当前帧的相机参数对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| outCamera | 返回当前帧对应的相机参数对象，参见AREngine_ARCamera。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARFrame_AcquireCameraImage**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraImage(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outImage)
```

描述

获取相机的当前帧的图像。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| outImage | 返回返回当前帧的图像对象，参见AREngine_ARImage。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_UNSUPPORTED_CONFIGURATION | 不支持的配置状态。 |

**HMS_AREngine_ARFrame_AcquireCameraPhotoImage**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraPhotoImage(const AREngine_ARSession *session, const AAREngine_ARFrame*frame, HMS_AREngine_PhotoAvailableCallback photoCallback)
```

描述

获取当前帧的拍照流图片。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.2(22)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| photoCallback | 输出拍照流图片的回调，参见HMS_AREngine_PhotoAvailableCallback。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_UNSUPPORTED_CONFIGURATION | 不支持的配置状态。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |
| ARENGINE_ERROR_CAMERA_NOT_AVAILABLE | 相机不可用状态。 |
| ARENGINE_CAMERA_SERVICE_FATAL_ERROR | 相机服务异常。 |

**HMS_AREngine_ARFrame_AcquireDepthConfidenceImage**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireDepthConfidenceImage(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outConfidenceImage)
```

描述

获取当前帧的深度置信度图像。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.5(17)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| outConfidenceImage | 返回返回当前帧深度置信度图像对象，参见AREngine_ARImage。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFrame_AcquireDepthImage16Bits**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireDepthImage16Bits(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outDepthImage)
```

描述

获取当前帧的深度图像。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.5(17)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| outDepthImage | 返回当前帧深度图像对象，参见AREngine_ARImage。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFrame_AcquirePointCloud**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquirePointCloud(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARPointCloud **outPointCloud)
```

描述

返回当前帧的点云数据。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| outPointCloud | 返回当前帧的点云对象，参见AREngine_ARPointCloud。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARFrame_AcquireSceneMesh**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireSceneMesh(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARSceneMesh **outSceneMesh)
```

描述

获取当前帧的mesh信息。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| outSceneMesh | 返回当前帧的mesh信息，参见AREngine_ARSceneMesh。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARFrame_AcquireSemanticDenseData**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_AcquireSemanticDenseData(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARSemanticDenseData **outSemanticDenseData)
```

描述

获取当前帧的高精几何重建对象数据。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.0(20)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| outSemanticDenseData | 返回当前帧的高精几何重建对象数据，参见AREngine_ARSemanticDenseData。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARFrame_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_Create(const AREngine_ARSession *session, AREngine_ARFrame **outFrame)
```

描述

创建一个新的[AREngine_ARFrame](#ZH-CN_TOPIC_0000002553362039__arengine_arframe)对象，将指针存储到*outFrame中。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outFrame | 当前帧对象，参见AREngine_ARFrame。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARFrame_Destroy**

```ets
void HMS_AREngine_ARFrame_Destroy(AREngine_ARFrame *frame)
```

描述

删除当前[AREngine_ARFrame](#ZH-CN_TOPIC_0000002553362039__arengine_arframe)对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| frame | 待销毁的当前帧对象，参见AREngine_ARFrame。 |

**HMS_AREngine_ARFrame_GetDisplayGeometryChanged**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_GetDisplayGeometryChanged(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int32_t *outGeometryChangeState)
```

描述

获取显示（长宽和旋转）是否发生变化。

如果发生变化，需要重新调用[HMS_AREngine_ARFrame_TransformDisplayUvCoords](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arframe_transformdisplayuvcoords)获取正确的纹理贴图坐标。 返回值outGeometryChangeState为0，代表未发生变化，否则为发生了变化。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| outGeometryChangeState | 返回显示（长宽和旋转）是否发生变化。0代表未发生变化，否则为发生了变化。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFrame_GetTimestamp**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int64_t *outTimestampNs)
```

描述

获取当前帧对应的时间戳信息，单位为ns。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| outTimestampNs | 返回时间戳信息。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFrame_GetUpdatedTrackables**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_GetUpdatedTrackables(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARTrackableType filterType, AREngine_ARTrackableList * outTrackableList)
```

描述

获取[HMS_AREngine_ARSession_Update](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arsession_update)更新后发生变化的指定类型的可跟踪对象。

可跟踪对象类型参见[AREngine_ARTrackableType](#ZH-CN_TOPIC_0000002553362039__arengine_artrackabletype)。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| filterType | 待返回的可跟踪对象类型，参见AREngine_ARTrackableType。 |
| outTrackableList | 返回可跟踪对象列表，参见AREngine_ARTrackableList。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARFrame_HitTest**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_HitTest(const AREngine_ARSession *session, const AREngine_ARFrame *frame, float pixelX, float pixelY, AREngine_ARHitResultList *hitResultList)
```

描述

从摄像头发射一条射线，该射线的方向由预览区上的点（pixelX，pixelY）确定，（pixelX，pixelY）可以通过XComponent的[DispatchTouchEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback#dispatchtouchevent)事件获取。

射线与系统跟踪的平面或者是点云中的点碰撞（点云正常识别），从而产生交点，形成碰撞结果。按照交点与设备的距离从近到远进行排序，存放在列表中。(pixelX，pixelY)是像素在预览区上坐标。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| pixelX | x轴坐标，通过XComponent获取。 |
| pixelY | y轴坐标，通过XComponent获取。 |
| hitResultList | 碰撞结果列表，参见AREngine_ARHitResultList。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARFrame_TransformDisplayUvCoords**

```ets
AREngine_ARStatus HMS_AREngine_ARFrame_TransformDisplayUvCoords(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int32_t elementSize, const float *uvsIn, float *uvsOut)
```

描述

调整纹理映射坐标，以便可以正确地显示相机捕捉到的背景图片。

若[HMS_AREngine_ARFrame_GetDisplayGeometryChanged](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arframe_getdisplaygeometrychanged)返回的outGeometryChangeState不为0，或者使用[HMS_AREngine_ARSession_SetDisplayGeometry](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arsession_setdisplaygeometry)设置了新的显示大小则需要调用该方法更新纹理映射坐标，否则不需要更新。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| frame | 当前帧对象，参见AREngine_ARFrame。 |
| elementSize | 待转换的纹理坐标数量，必须是2的倍数（uv坐标），最小为0。 |
| uvsIn | 原始输入uv坐标值。数组大小为 elementSize，不能为nullptr。 |
| uvsOut | 调整后的uv坐标值。数组大小为 elementSize，不能为nullptr。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARHitResult_AcquireNewAnchor**

```ets
AREngine_ARStatus HMS_AREngine_ARHitResult_AcquireNewAnchor(AREngine_ARSession *session, AREngine_ARHitResult *hitResult, AREngine_ARAnchor **outAnchor)
```

描述

在碰撞命中位置创建一个新的锚点。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| hitResult | 命中检测结果对象，参见AREngine_ARHitResult。 |
| outAnchor | 返回新创建的锚点对象，参见AREngine_ARAnchor。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARHitResult_AcquireTrackable**

```ets
AREngine_ARStatus HMS_AREngine_ARHitResult_AcquireTrackable(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, AREngine_ARTrackable **outTrackable)
```

描述

获取被命中的可追踪对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| hitResult | 命中检测结果对象，参见AREngine_ARHitResult。 |
| outTrackable | 返回被命中的可追踪对象，参见AREngine_ARTrackable。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARHitResult_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARHitResult_Create(const AREngine_ARSession *session, AREngine_ARHitResult **outHitResult)
```

描述

创建一个空的命中检测结果对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outHitResult | 待创建的命中检测结果对象，参见AREngine_ARHitResult。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARHitResult_Destroy**

```ets
void HMS_AREngine_ARHitResult_Destroy(AREngine_ARHitResult *hitResult)
```

描述

释放命中检测结果对象列表，以及其中的所有命中检测结果对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| hitResult | 待释放的命中检测结果对象，参见AREngine_ARHitResult。 |

**HMS_AREngine_ARHitResult_GetDistance**

```ets
AREngine_ARStatus HMS_AREngine_ARHitResult_GetDistance(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, float *outDistance)
```

描述

返回从相机到命中位置的距离，以m为单位。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| hitResult | 命中检测结果对象，参见AREngine_ARHitResult。 |
| outDistance | 返回相机到命中对象的距离。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARHitResult_GetHitPose**

```ets
AREngine_ARStatus HMS_AREngine_ARHitResult_GetHitPose(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, AREngine_ARPose *outPose)
```

描述

获取交点的位姿。

其平移向量是交点在世界坐标系的坐标，其旋转分量根据碰撞点的不同类型（平面交点、点云交点）而有不同的定义。

1.

当射线与平面碰撞时，局部坐标系为：X+垂直于射线，平行于跟踪平面；Y+是跟踪平面的法向量；Z+平行于平面，大致指向摄像头。

1.

当射线与点云中的点碰撞时，系统会尝试用点击区域的点云估计一个平面。

  1. 如果[HMS_AREngine_ARPoint_GetOrientationMode](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arpoint_getorientationmode)接口返回[ARENGINE_POINT_ORIENTATION_ESTIMATED_SURFACE_NORMAL](#ZH-CN_TOPIC_0000002553362039__arengine_arpointorientationmode)，则X+垂直于射线，平行于跟踪平面，Y+是跟踪平面的法向量，Z+平行于平面，大致指向摄像头。

  1. 如果返回 [ARENGINE_POINT_ORIENTATION_INITIALIZED_TO_IDENTITY](#ZH-CN_TOPIC_0000002553362039__arengine_arpointorientationmode)，则坐标的方向不会随平面的角度发生变化，X+垂直于射线且指向右侧（从设备的角度观察），Y+向上，Z+大致指向摄像头，具体参见朝向模式定义。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| hitResult | 命中检测结果对象，参见AREngine_ARHitResult。 |
| outPose | 返回交点的位姿，参见AREngine_ARPose。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARHitResultList_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARHitResultList_Create(const AREngine_ARSession *session, AREngine_ARHitResultList **outHitResultList)
```

描述

创建一个命中检测结果对象列表。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outHitResultList | 待创建的命中检测结果对象列表，参见AREngine_ARHitResultList。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARHitResultList_Destroy**

```ets
void HMS_AREngine_ARHitResultList_Destroy(AREngine_ARHitResultList *hitResultList)
```

描述

释放命中检测结果对象列表，以及其中的所有命中检测结果对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| hitResultList | 待释放的命中检测结果对象列表，参见AREngine_ARHitResultList。 |

**HMS_AREngine_ARHitResultList_GetItem**

```ets
AREngine_ARStatus HMS_AREngine_ARHitResultList_GetItem(const AREngine_ARSession *session, const AREngine_ARHitResultList *hitResultList, int32_t index, AREngine_ARHitResult *outHitResult)
```

描述

在命中检测结果列表中获取指定索引的命中检测结果对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| hitResultList | 命中检测结果对象列表，参见AREngine_ARHitResultList。 |
| index | 待获取的命中检测结果对象索引。 |
| outHitResult | 待获取的命中检测结果对象，参见AREngine_ARHitResult。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARHitResultList_GetSize**

```ets
AREngine_ARStatus HMS_AREngine_ARHitResultList_GetSize(const AREngine_ARSession *session, const AREngine_ARHitResultList *hitResultList, int32_t *outSize)
```

描述

获取命中检测结果对象列表中包含的对象数。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| hitResultList | 命中检测结果对象列表，参见AREngine_ARHitResultList。 |
| outSize | 返回列表大小。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARImage_GetFormat**

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetFormat(const AREngine_ARSession *session, const AREngine_ARImage *image, AREngine_ARImageFormat *outFormat)
```

描述

获取当前帧的图像格式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| image | 输入图像数据，参见AREngine_ARImage。 |
| outFormat | 返回当前帧的图像格式。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARImage_GetHeight**

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetHeight(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outHeight)
```

描述

获取当前帧的图像数据的高度。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| image | 当前帧图像对象，参见AREngine_ARImage。 |
| outHeight | 返回当前帧的图像的高度，以像素为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARImage_GetNativeBuffer**

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetNativeBuffer(const AREngine_ARSession *session, const AREngine_ARImage *image, OH_NativeBuffer **outNativeBuffer)
```

描述

获取当前帧图像对象的NativeBuffer数据。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.0(20)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| image | 当前帧图像对象，参见AREngine_ARImage。 |
| outNativeBuffer | 返回当前帧图像的NativeBuffer数据。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |
| ARENGINE_ERROR_NATIVEBUFFER_CREATE_FAILED | 创建NativeBuffer失败。 |
| ARENGINE_ERROR_NATIVEBUFFER_WRITE_FAILED | 无法写入NativeBuffer。 |

**HMS_AREngine_ARImage_GetPlaneCount**

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneCount(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outCount)
```

描述

获取当前帧图像的平面数量。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| image | 当前帧图像对象，参见AREngine_ARImage。 |
| outCount | 返回当前帧图像的平面数量。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARImage_GetPlaneData**

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneData(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, const uint8_t **outData, int32_t *outLength)
```

描述

获取当前帧图像的平面数据。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| image | 当前帧图像对象，参见AREngine_ARImage。 |
| planeIndex | 平面的索引。介于0和n-1，其中n是该图像的平面数。 |
| outData | 返回当前图像数据指针。 |
| outLength | 返回当前图像的长度，以Byte为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARImage_GetPlanePixelStride**

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetPlanePixelStride(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, int32_t *outPixelStride)
```

描述

获取图像中两个连续像素的起点之间的字节距离。像素步幅始终大于0。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| image | 当前帧图像对象，参见AREngine_ARImage。 |
| planeIndex | 平面的索引。介于0和n-1，其中n是该图像的平面数。 |
| outPixelStride | 返回图像的步幅，以Byte为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARImage_GetPlaneRowStride**

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneRowStride(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, int32_t *outRowStride)
```

描述

获取图像中两个连续像素行的起始位置之间的字节数。行间距始终大于0。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| image | 当前帧图像对象，参见AREngine_ARImage。 |
| planeIndex | 平面的索引。介于0和n-1，其中n是该图像的平面数。 |
| outRowStride | 返回图像的行跨距，以Byte为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARImage_GetTimestamp**

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARImage *image, int64_t *outTimestamp)
```

描述

获取图像的时间戳。

时间戳通常是单调递增的，以ns为单位。时间戳的具体含义和时基取决于提供图像的源。 来自不同来源的图像的时间戳可能具有不同的时基，因此不应该相互比较。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| image | 当前帧图像对象，参见AREngine_ARImage。 |
| outTimestamp | 返回图像的时间戳，以ns为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARImage_GetWidth**

```ets
AREngine_ARStatus HMS_AREngine_ARImage_GetWidth(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outWidth)
```

描述

获取当前帧的图像数据的宽度。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| image | 当前帧图像对象，参见AREngine_ARImage。 |
| outWidth | 返回当前帧的图像的宽度，以像素为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARImage_Release**

```ets
void HMS_AREngine_ARImage_Release(AREngine_ARImage *image)
```

描述

释放当前帧的图像对象，由[HMS_AREngine_ARFrame_AcquireCameraImage](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arframe_acquirecameraimage)创建的对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| image | 待释放的当前帧图像对象，参见AREngine_ARImage。 |

**HMS_AREngine_ARPlane_AcquireSubsumedBy**

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_AcquireSubsumedBy(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPlane **outSubsumedBy)
```

描述

获取平面的父平面（一个平面被另一个平面合并时，会产生父平面），如果无父平面返回为NULL。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| plane | 待处理的平面对象，参见AREngine_ARPlane。 |
| outSubsumedBy | 返回指定平面的父平面对象，参见AREngine_ARPlane。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPlane_GetCenterPose**

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPose *outPose)
```

描述

获取从平面的局部坐标系到世界坐标系转换的位姿信息。

平面局部坐标系（右手坐标系）为：原点在包裹平面矩形的中心，矩形更长的边方向为X轴，短边方向为Z轴，Y+为平面法向量。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| plane | 待处理的平面对象，参见AREngine_ARPlane。 |
| outPose | 返回平面的局部坐标系到世界坐标系转换的位姿信息，参见AREngine_ARPose。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPlane_GetExtentX**

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetExtentX(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outExtentX)
```

描述

获取平面的矩形边界沿平面局部坐标系X轴的长度，如矩形的宽度。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| plane | 待处理的平面对象，参见AREngine_ARPlane。 |
| outExtentX | 返回平面的矩形边界沿平面局部坐标系X轴的长度，以m为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPlane_GetExtentZ**

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetExtentZ(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outExtentZ)
```

描述

获取平面的矩形边界沿平面局部坐标系Z轴的长度，如矩形的高度。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| plane | 待处理的平面对象，参见AREngine_ARPlane。 |
| outExtentZ | 返回平面的矩形边界沿平面局部坐标系Z轴的长度，以m为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPlane_GetLabel**

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetLabel(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARSemanticPlaneLabel *label)
```

描述

获取平面的语义类型，如桌面、地板等。

使用时需要使用[HMS_AREngine_ARConfig_SetSemanticMode](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arconfig_setsemanticmode)启用语义识别模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| plane | 待处理的平面对象，参见AREngine_ARPlane。 |
| label | 返回当前平面的语义类型，参见AREngine_ARSemanticPlaneLabel。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPlane_GetPolygon**

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetPolygon(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outPolygonXz, int32_t polygonSize)
```

描述

获取检测到平面的二维顶点数组，格式为[x1，z1，x2，z2，...]。

这些值均在平面局部坐标系的x-z平面中定义，须经[HMS_AREngine_ARPlane_GetCenterPose](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arplane_getcenterpose)转换到世界坐标系中。

在垂直平面中返回的值也是局部坐标系中的坐标[x1，z1，x2，z2，….]，需要使用[HMS_AREngine_ARPlane_GetCenterPose](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arplane_getcenterpose)转换到世界坐标系。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| plane | 待处理的平面对象，参见AREngine_ARPlane。 |
| outPolygonXz | 返回检测到平面的二维顶点数组。 |
| polygonSize | 二维顶点数组大小，通过HMS_AREngine_ARPlane_GetPolygonSize接口获取。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPlane_GetPolygonSize**

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetPolygonSize(const AREngine_ARSession *session, const AREngine_ARPlane *plane, int32_t *outPolygonSize)
```

描述

获取检测到平面的二维顶点数组大小。

配合[HMS_AREngine_ARPlane_GetPolygon](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arplane_getpolygon)接口使用。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| plane | 待处理的平面对象，参见AREngine_ARPlane。 |
| outPolygonSize | 返回二维顶点数组大小。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPlane_GetType**

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_GetType(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPlaneType *outPlaneType)
```

描述

获取平面的类型。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| plane | 待处理的平面对象，参见AREngine_ARPlane。 |
| outPlaneType | 返回平面的类型，参见AREngine_ARPlaneType。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPlane_IsPoseInExtents**

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_IsPoseInExtents(const AREngine_ARSession *session, const AREngine_ARPlane *plane, const AREngine_ARPose *pose, int32_t *outPoseInExtents)
```

描述

判断位姿是否位于平面的矩形范围内。

如果传入的位姿（通过[HMS_AREngine_ARHitResult_GetHitPose](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arhitresult_gethitpose)获取）位于平面的矩形范围内，则返回非0值。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| plane | 待处理的平面对象，参见AREngine_ARPlane。 |
| pose | 位姿信息，参见AREngine_ARPose。 |
| outPoseInExtents | 返回位姿是否位于平面的矩形范围内，0表示不在范围内，非0表示在范围内。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPlane_IsPoseInPolygon**

```ets
AREngine_ARStatus HMS_AREngine_ARPlane_IsPoseInPolygon(const AREngine_ARSession *session, const AREngine_ARPlane *plane, const AREngine_ARPose *pose, int32_t *outPoseInPolygon)
```

描述

判断位姿是否位于平面的多边形范围内。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| plane | 待处理的平面对象，参见AREngine_ARPlane。 |
| pose | 位姿信息，参见AREngine_ARPose。 |
| outPoseInPolygon | 返回位姿是否位于平面的多边形范围内，0表示不在范围内，非0表示在范围内。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPoint_GetOrientationMode**

```ets
AREngine_ARStatus HMS_AREngine_ARPoint_GetOrientationMode(const AREngine_ARSession *session, const AREngine_ARPoint *point, AREngine_ARPointOrientationMode *outOrientationMode)
```

描述

获取输入点的朝向模式。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| point | 输入点对象，参见AREngine_ARPoint。 |
| outOrientationMode | 返回输入点的朝向模式，参见AREngine_ARPointOrientationMode。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPoint_GetPose**

```ets
AREngine_ARStatus HMS_AREngine_ARPoint_GetPose(const AREngine_ARSession *session, const AREngine_ARPoint *point, AREngine_ARPose *outPose)
```

描述

获取输入点的位姿信息。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| point | 输入点对象，参见AREngine_ARPoint。 |
| outPose | 返回输入点的位姿信息，参见AREngine_ARPose。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPointCloud_GetData**

```ets
AREngine_ARStatus HMS_AREngine_ARPointCloud_GetData(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, const float **outPointCloudData)
```

描述

获取点云中所有点的坐标及置信度数组。

其坐标值都在世界坐标系下，使用右手坐标系表示。点云对象可以通过[HMS_AREngine_ARFrame_AcquirePointCloud](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arframe_acquirepointcloud)获取。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| pointCloud | 点云对象，参见AREngine_ARPointCloud。 |
| outPointCloudData | 返回点云中所有点的坐标及置信度数组。数据格式为[x0，y0，z0，c0，x1，y1，z1，c1，x2...]。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPointCloud_GetNumberOfPoints**

```ets
AREngine_ARStatus HMS_AREngine_ARPointCloud_GetNumberOfPoints(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, int32_t *outNumberOfPoints)
```

描述

获取点云中所有点的坐标及置信度数组大小。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

与[HMS_AREngine_ARPointCloud_GetData](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arpointcloud_getdata)配合使用。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| pointCloud | 点云对象，参见AREngine_ARPointCloud。 |
| outNumberOfPoints | 返回点云中所有点的坐标及置信度数组大小。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPointCloud_GetTimestamp**

```ets
AREngine_ARStatus HMS_AREngine_ARPointCloud_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, int64_t *outTimestampNs)
```

描述

获取检测到当前特征点云的时间，以ns为单位。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| pointCloud | 点云对象，参见AREngine_ARPointCloud。 |
| outTimestampNs | 返回检测到当前特征点云的时间。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPointCloud_Release**

```ets
void HMS_AREngine_ARPointCloud_Release(AREngine_ARPointCloud *pointCloud)
```

描述

释放点云对象使用的内存。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| pointCloud | 待释放的点云对象，参见AREngine_ARPointCloud。 |

**HMS_AREngine_ARPose_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARPose_Create(const AREngine_ARSession *session, const float *poseRaw, const uint32_t poseRawSize, AREngine_ARPose **outPose)
```

描述

分配并初始化一个新的位姿对象。

可以设置poseRaw为空，来创建未初始化的位姿对象，随后调用[HMS_AREngine_ARPoint_GetPose](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arpoint_getpose)、[HMS_AREngine_ARAnchor_GetPose](#ZH-CN_TOPIC_0000002553362039__hms_arengine_aranchor_getpose)等为位姿对象赋值。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| poseRaw | 位姿数据，包括平移分量与旋转分量，数组大小为7，poseRaw[0]poseRaw[3]为旋转分量quaternion，poseRaw[4]poseRaw[6]为平移分量(x，y，z)。 |
| poseRawSize | 数组大小。取值范围：大于等于ARENGINE_POSE_RAW_SIZE。 |
| outPose | 返回新创建的位姿对象，参见AREngine_ARPose。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARPose_Destroy**

```ets
void HMS_AREngine_ARPose_Destroy(AREngine_ARPose *pose)
```

描述

释放位姿对象使用的内存。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| pose | 待释放的位姿对象，参见AREngine_ARPose。 |

**HMS_AREngine_ARPose_GetMatrix**

```ets
AREngine_ARStatus HMS_AREngine_ARPose_GetMatrix(const AREngine_ARSession *session, const AREngine_ARPose *pose, float *outMatrixColMajor4x4, int32_t matrixColMajor4x4Size)
```

描述

将位姿数据转换成4X4的矩阵。

outMatrixColMajor4x4为存放数组，其中的数据按照列优先存储，该矩阵与局部坐标系的坐标点做乘法，可以得到局部坐标系到世界坐标系的转换。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| pose | 位姿对象，参见AREngine_ARPose。 |
| outMatrixColMajor4x4 | 返回一个大小为16的float数组，数据按照列优先存储。 |
| matrixColMajor4x4Size | 数组大小。数组大小定义为：ARENGINE_VIEW_MATRIX_SIZE。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARPose_GetPoseRaw**

```ets
AREngine_ARStatus HMS_AREngine_ARPose_GetPoseRaw(const AREngine_ARSession *session, const AREngine_ARPose *pose, float *outPoseRaw, int32_t poseRawSize)
```

描述

从位姿对象提取位姿数据。

包括平移分量与旋转分量，数组大小为7，poseRaw[0]poseRaw[3]为旋转分量quaternion，poseRaw[4]poseRaw[6]为平移分量(x，y，z)。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| pose | 位姿对象，参见AREngine_ARPose。 |
| outPoseRaw | 返回位姿数据。 |
| poseRawSize | 数组大小。数组大小定义为：ARENGINE_POSE_RAW_SIZE。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSceneMesh_AcquireIndexList**

```ets
AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireIndexList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outData, int32_t dataSize)
```

描述

获取mesh面片的索引集合。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| sceneMesh | 当前帧的Mesh信息，参见AREngine_ARSceneMesh。 |
| outData | 返回mesh面片的索引集合。 |
| dataSize | mesh面片的索引个数，参见HMS_AREngine_ARSceneMesh_AcquireIndexListSize。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSceneMesh_AcquireIndexListSize**

```ets
AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireIndexListSize(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outSize)
```

描述

获取mesh面片的索引个数。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| sceneMesh | 当前帧的Mesh信息，参见AREngine_ARSceneMesh。 |
| outSize | 返回mesh面片的索引个数。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSceneMesh_AcquireVertexList**

```ets
AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVertexList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, float *outData, int32_t dataSize)
```

描述

获取mesh的顶点集合。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| sceneMesh | 当前帧的Mesh信息，参见AREngine_ARSceneMesh。 |
| outData | 返回mesh顶点集合，数组内容为每个顶点的世界坐标展开，例如[x1, y1,z1, x2, y2, z2, ...] 。 |
| dataSize | mesh面片的顶点个数，参见HMS_AREngine_ARSceneMesh_AcquireVerticesSize。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSceneMesh_AcquireVertexNormalList**

```ets
AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVertexNormalList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, float *outData, int32_t dataSize)
```

描述

获取mesh面片的法向量集合。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| sceneMesh | 当前帧的Mesh信息，参见AREngine_ARSceneMesh。 |
| outData | 返回mesh面片的法线向量集合，数组内容为每个面片法线向量的世界坐标展开，例如[x1,y1,z1, x2, y2, z2, ...]。 |
| dataSize | mesh面片的索引个数，参见HMS_AREngine_ARSceneMesh_AcquireIndexListSize。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSceneMesh_AcquireVerticesSize**

```ets
AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVerticesSize(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outSize)
```

描述

获取mesh的顶点个数。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| sceneMesh | 当前帧的Mesh信息，参见AREngine_ARSceneMesh。 |
| outSize | 返回mesh的顶点个数。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSceneMesh_Release**

```ets
void HMS_AREngine_ARSceneMesh_Release(AREngine_ARSceneMesh *sceneMesh)
```

描述

释放当前帧的mesh信息。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.1.0(18)

参数：

| 名称 | 描述 |
| --- | --- |
| sceneMesh | 当前帧的Mesh信息，参见AREngine_ARSceneMesh。 |

**HMS_AREngine_ARSemanticDense_AcquireCubeData**

```ets
AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquireCubeData(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, AREngine_ARSemanticDenseCubeData **outCubeData)
```

描述

获取识别到的高精几何重建对象数据中的立方体数据。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.0(20)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| semanticDenseData | 高精几何重建对象数据集合，参见AREngine_ARSemanticDenseData。 |
| outCubeData | 返回高精几何重建对象数据中立方体的数据，参见AREngine_ARSemanticDenseCubeData。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSemanticDense_AcquireCubeDataSize**

```ets
AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquireCubeDataSize(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, int64_t *outSize)
```

描述

获取识别到的高精几何重建对象数据中的立方体数量。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.0(20)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| semanticDenseData | 高精几何重建对象数据集合，参见AREngine_ARSemanticDenseData。 |
| outSize | 返回AREngine_ARSemanticDenseData对象中立方体数量的大小。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSemanticDense_AcquirePointData**

```ets
AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquirePointData(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, AREngine_ARSemanticDensePointData **outPointData)
```

描述

获取识别到的高精几何重建对象数据中的稠密点云数据。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.0(20)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| semanticDenseData | 高精几何重建对象数据集合，参见AREngine_ARSemanticDenseData。 |
| outPointData | 返回高精几何重建对象数据中稠密点云的数据，参见AREngine_ARSemanticDensePointData。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSemanticDense_AcquirePointDataSize**

```ets
AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquirePointDataSize(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData* semanticDenseData, int64_t *outSize)
```

描述

获取识别到的高精几何重建对象数据中的稠密点云数量。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.0.0(20)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| semanticDenseData | 稠密点云的数据集合，参见AREngine_ARSemanticDenseData。 |
| outSize | 返回AREngine_ARSemanticDenseData对象中稠密点云数量的大小。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSemanticDense_Release**

```ets
void HMS_AREngine_ARSemanticDense_Release(AREngine_ARSemanticDenseData *semanticDenseData)
```

描述

释放高精几何重建对象。

起始版本： 6.0.0(20)

参数：

| 名称 | 描述 |
| --- | --- |
| semanticDenseData | 释放高精几何重建对象，参见AREngine_ARSemanticDenseData。 |

**HMS_AREngine_ARSession_AcquireNewAnchor**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_AcquireNewAnchor(AREngine_ARSession *session, const AREngine_ARPose *pose, AREngine_ARAnchor **outAnchor)
```

描述

创建一个持续跟踪的锚点。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| pose | 创建锚点时使用的pose对象，参见AREngine_ARPose。 |
| outAnchor | 被创建的锚点对象，参见AREngine_ARAnchor。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_NOT_TRACKING | 未跟踪状态。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARSession_Configure**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Configure(AREngine_ARSession *session, const AREngine_ARConfig *config)
```

描述

配置[AREngine_ARSession](#ZH-CN_TOPIC_0000002553362039__arengine_arsession)会话。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 需要配置到设备上的配置对象，参见 AREngine_ARConfig。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |
| ARENGINE_ERROR_SESSION_NOT_PAUSED | 会话未暂停状态。 |

**HMS_AREngine_ARSession_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Create(void *env, void *applicationContext, AREngine_ARSession **outSessionPointer)
```

描述

创建一个新的[AREngine_ARSession](#ZH-CN_TOPIC_0000002553362039__arengine_arsession)会话。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中调用会返回801错误码，可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

需要权限： ohos.permission.CAMERA and ohos.permission.GYROSCOPE and ohos.permission.ACCELEROMETER

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| env | 当前APP的JNI运行环境信息。 |
| applicationContext | 与应用对应的Context。 |
| outSessionPointer | 被创建的会话对象，参见AREngine_ARSession。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_PERMISSION_NOT_GRANTED | 权限未授予状态。如相机权限未授予。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_DEVICE_NOT_SUPPORTED | 不可用：设备不兼容状态。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARSession_Create_Human_Perception**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Create_Human_Perception(void *env, void *applicationContext, REngine_ARSession **outSessionPointer)
```

描述

创建一个新的[AREngine_ARSession](#ZH-CN_TOPIC_0000002553362039__arengine_arsession)人体追踪会话。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

需要权限： ohos.permission.CAMERA

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| env | 当前APP的JNI运行环境信息。 |
| applicationContext | 与应用对应的Context。 |
| outSessionPointer | 被创建的会话对象，参见AREngine_ARSession。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_PERMISSION_NOT_GRANTED | 权限未授予状态。如相机权限未授予。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_DEVICE_NOT_SUPPORTED | 不可用：设备不兼容状态。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARSession_Destroy**

```ets
void HMS_AREngine_ARSession_Destroy(AREngine_ARSession *session)
```

描述

释放[AREngine_ARSession](#ZH-CN_TOPIC_0000002553362039__arengine_arsession)会话使用的资源。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |

**HMS_AREngine_ARSession_GetAllAnchors**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_GetAllAnchors(const AREngine_ARSession *session, AREngine_ARAnchorList *outAnchorList)
```

描述

获取所有锚点，包括[AREngine_ARTrackingState](#ZH-CN_TOPIC_0000002553362039__arengine_artrackingstate)中包含的所有状态下的锚点。

应用处理时需要仅绘制[ARENGINE_TRACKING_STATE_TRACKING](#ZH-CN_TOPIC_0000002553362039__arengine_artrackingstate)状态的锚点，删除[ARENGINE_TRACKING_STATE_STOPPED](#ZH-CN_TOPIC_0000002553362039__arengine_artrackingstate)状态的锚点。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outAnchorList | 返回所有的锚点对象列表，参见AREngine_ARAnchorList。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSession_GetAllTrackables**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_GetAllTrackables(const AREngine_ARSession *session, AREngine_ARTrackableType filterType, AREngine_ARTrackableList *outTrackableList)
```

描述

获取所有指定类型的可跟踪对象集合。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| filterType | 当前指定的可跟踪对象类型，参见AREngine_ARTrackableType。 |
| outTrackableList | 返回指定类型的可跟踪对象集合，参见 AREngine_ARTrackableList。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSession_GetCameraConfig**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_GetCameraConfig(const AREngine_ARSession *session, AREngine_ARCameraConfig *outCameraConfig)
```

描述

获取相机配置信息。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outCameraConfig | 返回相机配置信息，参见AREngine_ARCameraConfig。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSession_Pause**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Pause(AREngine_ARSession *session)
```

描述

暂停会话，停止相机预览流，不清除平面和锚点数据，释放相机（否则其他应用无法使用相机服务）。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARSession_Resume**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Resume(AREngine_ARSession *session)
```

描述

开始运行[AREngine_ARSession](#ZH-CN_TOPIC_0000002553362039__arengine_arsession)，或者在调用[HMS_AREngine_ARSession_Pause](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arsession_pause)以后恢复[AREngine_ARSession](#ZH-CN_TOPIC_0000002553362039__arengine_arsession)的运行状态。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |
| ARENGINE_ERROR_CAMERA_NOT_AVAILABLE | 相机不可用状态。 |

**HMS_AREngine_ARSession_SetCameraGLTexture**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_SetCameraGLTexture(AREngine_ARSession *session, uint32_t textureId)
```

描述

设置可用于存储相机预览流数据的OpenGL纹理。

应用调用[HMS_AREngine_ARSession_Update](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arsession_update)后，AR Engine会更新相机预览到纹理中。

纹理使用时需指定为GL_TEXTURE_EXTERNAL_OES，如：glBindTexture(GL_TEXTURE_EXTERNAL_OES, textureId)。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| textureId | 相机预览数据流的OpenGL textureId，大于0。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSession_SetDisplayGeometry**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_SetDisplayGeometry(AREngine_ARSession *session, AREngine_ARPoseType rotation, int32_t width, int32_t height)
```

描述

设置显示的高和宽，以像素为单位。

该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| rotation | 显示旋转常量，值为AREngine_ARPoseType中定义的枚举值。 |
| width | 显示的宽度，以像素为单位。其最大数值受设备屏幕像素限制，可通过XComponent获取。 |
| height | 显示的高度，以像素为单位。其最大数值受设备屏幕像素限制，可通过XComponent获取。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARSession_Stop**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Stop(AREngine_ARSession *session)
```

描述

停止AR Engine，停止相机预览流，清除平面和锚点数据，并释放相机，终止本次会话。

调用后，如果要再次启动，需要新建[AREngine_ARSession](#ZH-CN_TOPIC_0000002553362039__arengine_arsession)。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |

**HMS_AREngine_ARSession_Update**

```ets
AREngine_ARStatus HMS_AREngine_ARSession_Update(AREngine_ARSession *session, AREngine_ARFrame *outFrame)
```

描述

更新AR Engine的计算结果。

应用应在需要获取最新的数据时调用此接口，如相机发生移动以后，使用此接口可以获取新的锚点坐标、平面坐标、相机获取的图像帧等。

如果[HMS_AREngine_ARConfig_GetUpdateMode](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arconfig_getupdatemode)为[ARENGINE_UPDATE_MODE_BLOCKING](#ZH-CN_TOPIC_0000002553362039__arengine_arupdatemode)状态，那么该函数会阻塞至有新的帧可用。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outFrame | 返回更新后的帧对象，参见AREngine_ARFrame。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_FATAL | 失败状态。 |
| ARENGINE_ERROR_SESSION_PAUSED | 会话已暂停状态。 |
| ARENGINE_ERROR_MISSING_GL_CONTEXT | 缺少GL上下文状态。 |
| ARENGINE_ERROR_CAMERA_NOT_AVAILABLE | 相机不可用状态。 |
| ARENGINE_ERROR_IMAGE_INVALID_DATABASE | 没有有效的图像数据库。 起始版本： 5.1.0(18) |

**HMS_AREngine_ARTarget_GetAxisAlignedBoundingBox**

```ets
AREngine_ARStatus HMS_AREngine_ARTarget_GetAxisAlignedBoundingBox(const AREngine_ARSession *session, const AREngine_ARTarget *target, float *outAabb, int32_t aabbSize)
```

描述

获取语义物体最小外接包围盒坐标，坐标格式为(xmin，ymin，zmin，xmax，ymax，zmax)。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| target | 待处理的目标语义对象，参见AREngine_ARTarget。 |
| outAabb | 返回当前目标语义识别物体的最小外接包围盒坐标集。 |
| aabbSize | 数组大小为：ARENGINE_AABB_POINT_SIZE。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARTarget_GetCenterPose**

```ets
AREngine_ARStatus HMS_AREngine_ARTarget_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARTarget *target, AREngine_ARPose *outARPose)
```

描述

获取从目标语义对象的局部坐标系到世界坐标系转换的位姿对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| target | 待处理的目标语义对象，参见AREngine_ARTarget。 |
| outARPose | 返回目标语义对象的局部坐标系到世界坐标系转换的位姿，参见AREngine_ARPose。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARTarget_GetRadius**

```ets
AREngine_ARStatus HMS_AREngine_ARTarget_GetRadius(const AREngine_ARSession *session, const AREngine_ARTarget *target, float *radius)
```

描述

获取语义物体的球体半径。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| target | 待处理的目标语义对象，参见AREngine_ARTarget。 |
| radius | 返回当前目标语义物体的球体半径，以m为单位。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARTarget_GetShapeType**

```ets
AREngine_ARStatus HMS_AREngine_ARTarget_GetShapeType(const AREngine_ARSession *session, const AREngine_ARTarget *target, AREngine_ARTargetShapeLabel *shape)
```

描述

获取语义物体的形状类型。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| target | 待处理的目标语义对象，参见AREngine_ARTarget。 |
| shape | 返回当前目标语义识别到的物体形状类型，参见 AREngine_ARTargetShapeLabel。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARTrackable_AcquireNewAnchor**

```ets
AREngine_ARStatus HMS_AREngine_ARTrackable_AcquireNewAnchor(AREngine_ARSession *session, AREngine_ARTrackable *trackable, AREngine_ARPose *pose, AREngine_ARAnchor **outAnchor)
```

描述

通过可跟踪对象的位姿信息创建对应的锚点对象，该锚点将和当前的可跟踪对象绑定。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| trackable | 可跟踪对象。 |
| pose | 可跟踪对象的位姿信息。 |
| outAnchor | 新创建的锚点对象。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_NOT_TRACKING | 未跟踪状态。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARTrackable_GetAnchors**

```ets
AREngine_ARStatus HMS_AREngine_ARTrackable_GetAnchors(AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARAnchorList *outAnchorList)
```

描述

获取绑定到输入可跟踪对象的锚点对象列表。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| trackable | 可跟踪对象，参见AREngine_ARTrackable。 |
| outAnchorList | 返回锚点对象列表，此列表必须使用HMS_AREngine_ARAnchorList_Create创建。如果使用已经创建的列表，则此列表将被重新赋值。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARTrackable_GetTrackingState**

```ets
AREngine_ARStatus HMS_AREngine_ARTrackable_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARTrackingState *outTrackingState)
```

描述

获取当前可跟踪对象的跟踪状态。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| trackable | 可跟踪对象，参见AREngine_ARTrackable。 |
| outTrackingState | 返回可跟踪对象的跟踪状态，参见AREngine_ARTrackingState。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARTrackable_GetType**

```ets
AREngine_ARStatus HMS_AREngine_ARTrackable_GetType(const AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARTrackableType *outTrackableType)
```

描述

获取可跟踪对象的类型。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| trackable | 可跟踪对象，参见AREngine_ARTrackable。 |
| outTrackableType | 返回可跟踪对象的类型，参见AREngine_ARTrackableType。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARTrackable_Release**

```ets
void HMS_AREngine_ARTrackable_Release(AREngine_ARTrackable *trackable)
```

描述

释放可跟踪对象。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| trackable | 待释放的可跟踪对象，参见AREngine_ARTrackable。 |

**HMS_AREngine_ARTrackableList_AcquireItem**

```ets
AREngine_ARStatus HMS_AREngine_ARTrackableList_AcquireItem(const AREngine_ARSession *session, const AREngine_ARTrackableList *trackableList, int32_t index, AREngine_ARTrackable **outTrackable)
```

描述

从可跟踪列表中获取指定index的对象。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| trackableList | 被检索的可跟踪对象的列表，参见AREngine_ARTrackableList。 |
| index | 可跟踪对象在可跟踪对象列表中的位置。最大值不超过HMS_AREngine_ARTrackableList_GetSize。 |
| outTrackable | 返回目标可跟踪对象，参见AREngine_ARTrackable。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARTrackableList_Create**

```ets
AREngine_ARStatus HMS_AREngine_ARTrackableList_Create(const AREngine_ARSession *session, AREngine_ARTrackableList **outTrackableList)
```

描述

创建一个可跟踪对象列表。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| outTrackableList | 待创建的可跟踪对象列表，参见AREngine_ARTrackableList。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |
| ARENGINE_ERROR_RESOURCE_EXHAUSTED | 资源耗尽状态。 |

**HMS_AREngine_ARTrackableList_Destroy**

```ets
void HMS_AREngine_ARTrackableList_Destroy(AREngine_ARTrackableList *trackableList)
```

描述

释放可跟踪对象列表，以及它持有的所有锚点引用。

设备行为差异： 该接口在部分手机和部分平板设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| trackableList | 待释放的可跟踪对象列表，参见AREngine_ARTrackableList。 |

**HMS_AREngine_ARTrackableList_GetSize**

```ets
AREngine_ARStatus HMS_AREngine_ARTrackableList_GetSize(const AREngine_ARSession *session, const AREngine_ARTrackableList *trackableList, int32_t *outSize)
```

描述

获取此列表中的可跟踪对象的数量。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 5.0.0(12)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| trackableList | 可跟踪对象列表，参见AREngine_ARTrackableList。 |
| outSize | 返回可跟踪对象列表中可跟踪对象的数量。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARBody_GetSkeletonConfidence**

```ets
AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonConfidence(const AREngine_ARSession *session, const AREngine_ARBody *body, const float **outConfidence)
```

描述

获取人体对象每个骨骼点检测的置信度。置信度数组大小为骨骼点个数，且与[HMS_AREngine_ARBody_GetSkeletonTypes](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arbody_getskeletontypes)返回的骨骼类型顺序一致，每一个元素为[0，1]范围的置信度值。置信度趋于1，代表识别的骨骼点越准确。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| body | 待识别骨骼点置信度的人体对象，参见AREngine_ARBody。 |
| outConfidence | 骨骼点置信度。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARBody_GetSkeletonConnection**

```ets
AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonConnection(const AREngine_ARSession *session, const AREngine_ARBody *body, const AREngine_ARBodySkeletonType **outSkeletonConnection)
```

描述

获取人体对象骨骼点之间的链接关系数据。一个链接关系表示为两个骨骼点的类型。如返回值为[ARENGINE_ARBODY_SKELETON_R_WRIST，ARENGINE_ARBODY_SKELETON_R_ELBOW，...]，表示右手腕与右手肘相连成为一条骨骼。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| body | 待识别骨骼点链接关系数据的人体对象，参见AREngine_ARBody。 |
| outSkeletonConnection | 骨骼点之间的链接关系，参见AREngine_ARBodySkeletonType。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARBody_GetSkeletonConnectionSize**

```ets
AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonConnectionSize(const AREngine_ARSession *session, const AREngine_ARBody *body, int32_t *outConnectionCount)
```

描述

获取人体对象骨骼点之间的链接关系总数。该函数一般与[HMS_AREngine_ARBody_GetSkeletonConnection](#ZH-CN_TOPIC_0000002553362039__hms_arengine_arbody_getskeletonconnection)对应使用。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| body | 待获取骨骼点链接关系总数的人体对象，参见AREngine_ARBody。 |
| outConnectionCount | 骨骼点之间的链接关系总数。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARBody_GetSkeletonTypes**

```ets
AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonTypes(const AREngine_ARSession *session, const AREngine_ARBody *body, const AREngine_ARBodySkeletonType **outSkeletonTypes)
```

描述

获取识别出的人体对象骨骼点类型。骨骼点类型可参见[AREngine_ARBodySkeletonType](#ZH-CN_TOPIC_0000002553362039__arengine_arbodyskeletontype)。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| body | 待获取骨骼点类型的人体对象，参见AREngine_ARBody。 |
| outSkeletonTypes | 人体对象中识别出的骨骼点类型，参见AREngine_ARBodySkeletonType。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARBody_GetSkeletonPointCount**

```ets
AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonPointCount(const AREngine_ARSession *session, const AREngine_ARBody *body, int32_t *outPointCount)
```

描述

获取人体对象中识别出的骨骼点个数。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| body | 待获取骨骼点数的人体对象，参见AREngine_ARBody。 |
| outPointCount | 人体对象中识别出的骨骼点个数。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARBody_GetSkeletonPointData2D**

```ets
AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonPointData2D(const AREngine_ARSession *session, const AREngine_ARBody *body, const float **outSkeletonPointData2D)
```

描述

当运行2D骨骼跟踪算法时，返回人体骨骼点的2D坐标数据。返回值的格式为 [x0，y0，x1，y1，…]的数组。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| body | 人体对象，参见AREngine_ARBody。 |
| outSkeletonPointData2D | 人体骨骼点的2D坐标。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARBody_GetSkeletonPointIsValid**

```ets
AREngine_ARStatus HMS_AREngine_ARBody_GetSkeletonPointIsValid(const AREngine_ARSession *session, const AREngine_ARBody *body, const int32_t **outSkeletonPointIsValid)
```

描述

获取人体对象骨骼点的坐标是否有效，返回有效性数组。值为0说明骨骼点坐标数据无效，1说明骨骼点坐标数据有效。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| body | 待获取坐标有效性数组的人体对象，参见AREngine_ARBody。 |
| outSkeletonPointIsValid | 坐标有效性数组。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARBody_GetBodyTrackId**

```ets
AREngine_ARStatus HMS_AREngine_ARBody_GetBodyTrackId(const AREngine_ARSession *session, const AREngine_ARBody *body, const int32_t *outBodyTrackId)
```

描述

获取指定人体对象的标识。当识别出多个Body时，每个Body有个标识，可以通过该接口获取指定人体对象的标识。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| body | 待获取标识的人体对象，参见AREngine_ARBody。 |
| outBodyTrackId | 人体对象对应的标识。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARBody_GetBodyTimeStamp**

```ets
AREngine_ARStatus HMS_AREngine_ARBody_GetBodyTimeStamp(const AREngine_ARSession *session, const AREngine_ARBody *body, int64_t *timeStamp)
```

描述

获取人体对象的检测时间点，表示触发检测人体对象距离启动相机的时间间隔，单位为ns。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| body | 待获取检测时间点的人体对象，参见AREngine_ARBody。 |
| timeStamp | 人体对象的检测时间点。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |

**HMS_AREngine_ARConfig_SetBodyDetectedNum**

```ets
AREngine_ARStatus HMS_AREngine_ARConfig_SetBodyDetectedNum(const AREngine_ARSession *session, AREngine_ARConfig *config, int32_t maxNum)
```

描述

设置追踪人数。

设备行为差异： 该接口在部分手机，部分平板以及TV设备中可以正常调用，在其他设备中无法正常调用。开发者可以通过使用[HMS_AREngine_CheckSupported](#ZH-CN_TOPIC_0000002553362039__hms_arengine_checksupported)接口查询能力是否支持。

起始版本： 6.1.0(23)

参数：

| 名称 | 描述 |
| --- | --- |
| session | 与AR Engine服务交互的AREngine_ARSession对象。 |
| config | 指向待获取配置信息的配置对象，参见AREngine_ARConfig。 |
| maxNum | 追踪人数，当前支持1或2，默认为1，若设置的追踪人数超过2，则按2处理。 |

返回：

接口执行状态，参见[AREngine_ARStatus](#ZH-CN_TOPIC_0000002553362039__arengine_arstatus)。

| 状态码 | 状态信息 |
| --- | --- |
| ARENGINE_SUCCESS | 成功状态。 |
| ARENGINE_ERROR_INVALID_ARGUMENT | 无效参数状态。如方法入参为空或非法。 |