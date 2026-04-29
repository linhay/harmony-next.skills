# ar_engine_core.h

**概述**

本声明用于访问AR Engine（AR引擎服务）的API。提供AR（增强现实）能力的相关接口。AR的基础核心能力包含：环境识别与运动跟踪能力、图像识别与跟踪能力、人脸识别与跟踪能力和人体骨骼识别与跟踪能力。

引用文件： <native_buffer/native_buffer.h>

库： libarengine_ndk.z.so

系统能力： SystemCapability.AREngine.Core

起始版本： 5.0.0(12)

相关模块： [AR Engine](AR Engine.md)

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
| AREngine_ARStatus HMS_AREngine_ARAnchor_Detach(AREngine_ARSession *session, AREngine_ARAnchor *anchor) | 通知AR Engine停止跟踪并解绑一个锚点。 说明： 由于此函数并没有释放锚点AREngine_ARAnchor，开发者需要通过调用 HMS_AREngine_ARAnchor_Release来释放锚点。 |
| AREngine_ARStatus HMS_AREngine_ARAnchor_GetPose(const AREngine_ARSession *session, const AREngine_ARAnchor *anchor, AREngine_ARPose *outPose) | 获取指定锚点在世界坐标系中的位姿信息。 |
| AREngine_ARStatus HMS_AREngine_ARAnchor_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARAnchor *anchor, AREngine_ARTrackingState *outTrackingState) | 获取指定锚点位姿的追踪状态。 |
| void HMS_AREngine_ARAnchor_Release(AREngine_ARAnchor *anchor) | 释放指定锚点对象的内存。 |
| AREngine_ARStatus HMS_AREngine_ARAnchorList_AcquireItem(const AREngine_ARSession *session, const AREngine_ARAnchorList *anchorList, int32_t index, AREngine_ARAnchor **outAnchor) | 从锚点对象列表中获取指定位置的锚点信息。 |
| AREngine_ARStatus HMS_AREngine_ARAnchorList_Create(const AREngine_ARSession *session, AREngine_ARAnchorList **outAnchorList) | 创建一个锚点对象列表。 |
| void HMS_AREngine_ARAnchorList_Destroy(AREngine_ARAnchorList *anchorList) | 释放一个锚点对象列表。 |
| AREngine_ARStatus HMS_AREngine_ARAnchorList_GetSize(const AREngine_ARSession *session, const AREngine_ARAnchorList *anchorList, int32_t *outSize) | 获取锚点对象列表中包含锚点的数量。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImage_AcquireName(const AREngine_ARSession *session, const AREngine_ARAnchorList *augmentedImage, char *augmentedImageName, uint32_t *outNameLength) | 返回跟踪图像的名称。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, AREngine_ARPose *outPose) | 获取跟踪图像中心点在世界坐标系中的位姿信息。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetExtendX(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, float *outExtendX) | 以图像的中心点为坐标原点，获取X轴上的估计值。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetExtendZ(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, float *outExtendZ) | 以图像的中心点为坐标原点，获取Z轴上的估计值。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImage_GetIndex(const AREngine_ARSession *session, const AREngine_ARAugmentedImage *augmentedImage, uint32_t *outIndex) | 获取跟踪图像数据库中跟踪图像的索引。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_AddImage(AREngine_ARAugmentedImageDatabase *database, const AREngine_ARAugmentedImageSource *image, uint32_t *outIndex, AREngine_ARAddAugmentedImageReason *outReason) | 将图像添加到图像数据库并输出对应图像的索引。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Create(AREngine_ARAugmentedImageDatabase **outDatabase) | 创建一个空的跟踪图像数据库。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Deserialize(const uint8_t *buffer, const uint64_t bufSize, AREngine_ARAugmentedImageDatabase **outDatabase) | 反序列化特征数据库。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Destroy(AREngine_ARAugmentedImageDatabase *database) | 释放图像数据库对象。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetAddMode(const AREngine_ARAugmentedImageDatabase *database, AREngine_ARImageDatabaseMode *outAddMode) | 获取添加跟踪图像模式。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_SetAddMode(const AREngine_ARAugmentedImageDatabase *database, AREngine_ARImageDatabaseMode addMode) | 设置添加跟踪图像模式。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetCapacity(const AREngine_ARAugmentedImageDatabase *database, uint32_t *outCapacity) | 获取可以添加的最大图像数。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_GetImageCount(const AREngine_ARAugmentedImageDatabase *database, uint32_t *outImageCount) | 获取数据库中存储的图像数量。 |
| AREngine_ARStatus HMS_AREngine_ARAugmentedImageDatabase_Serialize(const AREngine_ARAugmentedImageDatabase *database, uint8_t **outBuffer, uint64_t *outBufSize) | 序列化特征数据库。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetDisplayOrientedPose(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARPose *outPose) | 设置outPose为虚拟相机（面向显示）在世界空间中的位姿，用以将AR内容渲染到最新帧中。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetImageIntrinsics(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARCameraIntrinsics *outIntrinsics) | 获取物理相机离线内参的对象，可通过该对象获取相机的焦距、图像尺寸、主轴点和畸变参数。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetPose(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARPose *outPose) | 设置outPose为最新帧中物理相机在世界空间中的位姿。该位姿是OpenGL相机的位姿。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetProjectionMatrix(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ClipPlaneDistance clipPlaneDistance, float *outDestColMajor4x4, int32_t destColMajor4x4Num) | 获取用于在相机图像上层渲染虚拟内容的投影矩阵，可用于相机坐标系到裁剪坐标系转换。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARTrackingState *outTrackingState) | 获取相机的当前追踪状态。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetTrackingStateReason(const AREngine_ARSession *session, const AREngine_ARCamera *camera, AREngine_ARTrackingStateReason *outTrackingStateReason) | 获取相机的当前追踪状态为ARENGINE_TRACKING_STATE_PAUSED时的原因。 |
| AREngine_ARStatus HMS_AREngine_ARCamera_GetViewMatrix(const AREngine_ARSession *session, const AREngine_ARCamera *camera, float *outColMajor4x4, int32_t colMajor4x4Num) | 获取最新帧中相机的视图矩阵。 |
| void HMS_AREngine_ARCamera_Release(AREngine_ARCamera *camera) | 释放对相机的引用。 |
| AREngine_ARStatus HMS_AREngine_ARCameraConfig_Create(const AREngine_ARSession *session, AREngine_ARCameraConfig **outCameraConfig) | 创建一个相机配置对象。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetCameraLensFacing(const *session, const AREngine_ARConfig *config, AREngine_ARCameraLensFacing *outFacing) | 获取相机镜头朝向。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetMultiFaceMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMultiFaceMode *outFaceMode) | 获取多人脸检测模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetCameraLensFacing(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARCameraLensFacing facing) | 设置相机镜头朝向，参见AREngine_ARCameraLensFacing。facing设置为ARENGINE_CAMERA_FACING_FRONT时，需要调用HMS_AREngine_ARConfig_SetARType将AR能力类型设置为ARENGINE_TYPE_FACE或ARENGINE_TYPE_BODY才生效。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetMultiFaceMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARMultiFaceMode faceMode) | 设置多人脸检测模式。 |
| void HMS_AREngine_ARCameraConfig_Destroy(AREngine_ARCameraConfig *cameraConfig) | 释放相机配置对象。 |
| AREngine_ARStatus HMS_AREngine_ARCameraConfig_GetImageDimensions(const AREngine_ARSession *session, const AREngine_ARCameraConfig *cameraConfig, int32_t *outWidth, int32_t *outHeight) | 从相机配置对象中获取相机送到CPU处理的图像尺寸。 |
| AREngine_ARStatus HMS_AREngine_ARCameraConfig_GetTextureDimensions(const AREngine_ARSession *session, const AREngine_ARCameraConfig *cameraConfig, int32_t *outWidth, int32_t *outHeight) | 从相机配置对象中获取相机送到GPU处理的图像纹理尺寸。 |
| AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_Create(const AREngine_ARSession *session, AREngine_ARCameraIntrinsics **outIntrinsics) | 创建一个相机内参对象。 |
| void HMS_AREngine_ARCameraIntrinsics_Destroy(AREngine_ARCameraIntrinsics *intrinsics) | 释放指定的相机内参对象。 |
| AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetDistortion(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outDistortion, int32_t distortionNum) | 获取相机的畸变系数。 |
| AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetFocalLength(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outFocalX, float *outFocalY) | 获取指定相机的焦距，焦距以像素为单位。 |
| AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetImageDimensions(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, int32_t *outWidth, int32_t *outHeight) | 获取相机图像的尺寸，包括宽度和高度，以像素为单位。 |
| AREngine_ARStatus HMS_AREngine_ARCameraIntrinsics_GetPrincipalPoint(const AREngine_ARSession *session, const AREngine_ARCameraIntrinsics *intrinsics, float *outPrincipalX, float *outPrincipalY) | 获取指定相机的主轴点，主点位置以像素为单位表示。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_Create(const AREngine_ARSession *session, AREngine_ARConfig **outConfig) | 创建具有适当默认配置的配置对象。 |
| void HMS_AREngine_ARConfig_Destroy(AREngine_ARConfig *config) | 释放指定的配置对象的内存空间。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetARType(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARType *type) | 获取当前使用的AR能力类型。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetARType(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARType type) | 设置当前要使用的AR能力类型。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetCameraPreviewMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPreviewMode *outMode) | 获取当前的预览模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetCameraPreviewMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPreviewMode mode) | 设置预览模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetDepthMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARDepthMode *outDepthMode) | 获取当前的深度模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetDepthMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARDepthMode depthMode) | 设置深度模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetFocusMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARFocusMode *focusMode) | 获取当前配置的相机对焦模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetFocusMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARFocusMode focusMode) | 设置当前所需的相机对焦模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetMaxMapSize(const AREngine_ARSession *session, const AREngine_ARConfig *config, uint64_t *maxMapSize) | 获取地图数据使用的最大内存大小。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetMaxMapSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint64_t maxMapSize) | 设置地图数据最大使用内存大小。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetMeshMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARMeshMode *outMeshMode) | 获取当前mesh模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetMeshMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARMeshMode meshMode) | 设置mesh模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetPlaneFindingMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPlaneFindingMode *planeFindingMode) | 获取当前配置的平面识别模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetPlaneFindingMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPlaneFindingMode planeFindingMode) | 设置当前所需的平面识别模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetPoseMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPoseMode *poseMode) | 获取相机输出的位姿坐标系对齐模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetPoseMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPoseMode poseMode) | 设置相机输出的位姿坐标系对齐模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetPowerMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARPowerMode *powerMode) | 获取当前配置的功耗模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetPowerMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARPowerMode powerMode) | 设置功耗模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetPreviewSize(const AREngine_ARSession *session, AREngine_ARConfig *config, uint32_t width, uint32_t height) | 设置预览画面尺寸。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetSemanticDenseMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARSemanticDenseMode *outSemanticDenseMode) | 获取已设置的高精几何重建模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetSemanticDenseMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARSemanticDenseMode semanticDenseMode) | 设置当前所需的高精几何重建模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetSemanticMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARSemanticMode *mode) | 获取已设置成功的语义识别模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetSemanticMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARSemanticMode mode) | 设置当前所需的语义识别模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_GetUpdateMode(const AREngine_ARSession *session, const AREngine_ARConfig *config, AREngine_ARUpdateMode *updateMode) | 获取当前配置的预览更新模式。 |
| AREngine_ARStatus HMS_AREngine_ARConfig_SetUpdateMode(const AREngine_ARSession *session, AREngine_ARConfig *config, AREngine_ARUpdateMode updateMode) | 设置预览更新模式。 |
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
| void HMS_AREngine_ARFaceGeometry_Release(AREngine_ARFaceGeometry *geometry) | 释放当前人脸几何体对象，即由 HMS_AREngine_ARFace_AcquireBlendShapes创建的对象。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCamera(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARCamera **outCamera) | 获取当前帧的相机参数对象。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraImage(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outImage) | 获取相机的当前帧的图像。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireCameraPhotoImage (const AREngine_ARSession *session, const AREngine_ARFrame *frame, HMS_AREngine_PhotoAvailableCallback photoCallback) | 获取当前帧的拍照流图片。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireDepthConfidenceImage(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outConfidenceImage) | 获取当前帧的深度置信度图像。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireDepthImage16Bits(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARImage **outDepthImage); | 获取当前帧的深度图像。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquirePointCloud(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARPointCloud **outPointCloud) | 返回当前帧的点云数据。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireSceneMesh(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARSceneMesh **outSceneMesh) | 获取当前帧的mesh信息。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_AcquireSemanticDenseData(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARSemanticDenseData **outSemanticDenseData); | 获取当前帧的高精几何重建对象数据。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_Create(const AREngine_ARSession *session, AREngine_ARFrame **outFrame) | 创建一个新的AREngine_ARFrame对象，将指针存储到*outFrame中。 |
| void HMS_AREngine_ARFrame_Destroy(AREngine_ARFrame *frame) | 删除当前AREngine_ARFrame对象。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_GetDisplayGeometryChanged(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int32_t *outGeometryChangeState) | 获取显示（长宽和旋转）是否发生变化。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int64_t *outTimestampNs) | 获取当前帧对应的时间戳信息，单位为ns。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_GetUpdatedTrackables(const AREngine_ARSession *session, const AREngine_ARFrame *frame, AREngine_ARTrackableType filterType, AREngine_ARTrackableList *outTrackableList) | 获取HMS_AREngine_ARSession_Update更新后发生变化的指定类型的可跟踪对象。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_HitTest(const AREngine_ARSession *session, const AREngine_ARFrame *frame, float pixelX, float pixelY, AREngine_ARHitResultList *hitResultList) | 从摄像头发射一条射线，该射线的方向由预览区上的点（pixelX，pixelY）确定（pixelX，pixelY）可以通过XComponent的DispatchTouchEvent事件获取）。 |
| AREngine_ARStatus HMS_AREngine_ARFrame_TransformDisplayUvCoords(const AREngine_ARSession *session, const AREngine_ARFrame *frame, int32_t elementSize, const float *uvsIn, float *uvsOut) | 调整纹理映射坐标，以便可以正确地显示相机捕捉到的背景图片。 |
| AREngine_ARStatus HMS_AREngine_ARHitResult_AcquireNewAnchor(AREngine_ARSession *session, AREngine_ARHitResult *hitResult, AREngine_ARAnchor **outAnchor) | 在碰撞命中位置创建一个新的锚点。 |
| AREngine_ARStatus HMS_AREngine_ARHitResult_AcquireTrackable(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, AREngine_ARTrackable **outTrackable) | 获取被命中的可追踪对象。 |
| AREngine_ARStatus HMS_AREngine_ARHitResult_Create(const AREngine_ARSession *session, AREngine_ARHitResult **outHitResult) | 创建一个空的命中检测结果对象。 |
| void HMS_AREngine_ARHitResult_Destroy(AREngine_ARHitResult *hitResult) | 释放命中检测结果对象使用的内存。 |
| AREngine_ARStatus HMS_AREngine_ARHitResult_GetDistance(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, float *outDistance) | 返回从相机到命中位置的距离，以m为单位。 |
| AREngine_ARStatus HMS_AREngine_ARHitResult_GetHitPose(const AREngine_ARSession *session, const AREngine_ARHitResult *hitResult, AREngine_ARPose *outPose) | 获取交点的位姿。 |
| AREngine_ARStatus HMS_AREngine_ARHitResultList_Create(const AREngine_ARSession *session, AREngine_ARHitResultList **outHitResultList) | 创建一个命中检测结果对象列表。 |
| void HMS_AREngine_ARHitResultList_Destroy(AREngine_ARHitResultList *hitResultList) | 释放命中检测结果对象列表，以及其中的所有命中检测结果对象。 |
| AREngine_ARStatus HMS_AREngine_ARHitResultList_GetItem(const AREngine_ARSession *session, const AREngine_ARHitResultList *hitResultList, int32_t index, AREngine_ARHitResult *outHitResult) | 在命中检测结果列表中获取指定索引的命中检测结果对象。 |
| AREngine_ARStatus HMS_AREngine_ARHitResultList_GetSize(const AREngine_ARSession *session, const AREngine_ARHitResultList *hitResultList, int32_t *outSize) | 获取命中检测结果对象列表中包含的对象数。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetFormat(const AREngine_ARSession *session, const AREngine_ARImage *image, AREngine_ARImageFormat *outFormat) | 获取当前帧的图像格式。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetHeight(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outHeight) | 获取当前帧的图像数据的高度。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetWidth(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outWidth) | 获取当前帧的图像数据的宽度。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetNativeBuffer(const AREngine_ARSession *session, const AREngine_ARImage *image, OH_NativeBuffer **outNativeBuffer); | 获取当前帧图像对象的NativeBuffer数据。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneCount(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t *outCount) | 获取当前帧图像的平面数量。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneData(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, const uint8_t **outData, int32_t *outLength) | 获取当前帧图像的平面数据。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetPlanePixelStride(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, int32_t *outPixelStride) | 获取图像中两个连续像素的起点之间的字节距离。像素步幅始终大于0。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetPlaneRowStride(const AREngine_ARSession *session, const AREngine_ARImage *image, int32_t planeIndex, int32_t *outRowStride) | 获取图像中两个连续像素行的起始位置之间的字节数。行间距始终大于0。 |
| AREngine_ARStatus HMS_AREngine_ARImage_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARImage *image, int64_t *outTimestamp) | 获取图像的时间戳。 |
| void HMS_AREngine_ARImage_Release(AREngine_ARImage *image) | 释放当前帧的图像对象，由HMS_AREngine_ARFrame_AcquireCameraImage创建的对象。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_AcquireSubsumedBy(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPlane **outSubsumedBy) | 获取平面的父平面（一个平面被另一个平面合并时，会产生父平面），如果无父平面返回为NULL。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPose *outPose) | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetExtentX(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outExtentX) | 获取平面的矩形边界沿平面局部坐标系X轴的长度，如矩形的宽度。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetExtentZ(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outExtentZ) | 获取平面的矩形边界沿平面局部坐标系Z轴的长度，如矩形的高度。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetLabel(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARSemanticPlaneLabel *label) | 获取平面的语义类型，如桌面、地板等。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetPolygon(const AREngine_ARSession *session, const AREngine_ARPlane *plane, float *outPolygonXz, int32_t polygonSize) | 获取检测到平面的二维顶点数组，格式为[x1，z1，x2，z2，...]。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetPolygonSize(const AREngine_ARSession *session, const AREngine_ARPlane *plane, int32_t *outPolygonSize) | 获取检测到平面的二维顶点数组大小。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_GetType(const AREngine_ARSession *session, const AREngine_ARPlane *plane, AREngine_ARPlaneType *outPlaneType) | 获取平面的类型。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_IsPoseInExtents(const AREngine_ARSession *session, const AREngine_ARPlane *plane, const AREngine_ARPose *pose, int32_t *outPoseInExtents) | 判断位姿是否位于平面的矩形范围内。 |
| AREngine_ARStatus HMS_AREngine_ARPlane_IsPoseInPolygon(const AREngine_ARSession *session, const AREngine_ARPlane *plane, const AREngine_ARPose *pose, int32_t *outPoseInPolygon) | 判断位姿是否位于平面的多边形范围内。 |
| AREngine_ARStatus HMS_AREngine_ARPoint_GetOrientationMode(const AREngine_ARSession *session, const AREngine_ARPoint *point, AREngine_ARPointOrientationMode *outOrientationMode) | 获取输入点的朝向模式。 |
| AREngine_ARStatus HMS_AREngine_ARPoint_GetPose(const AREngine_ARSession *session, const AREngine_ARPoint *point, AREngine_ARPose *outPose) | 获取输入点的位姿信息。 |
| AREngine_ARStatus HMS_AREngine_ARPointCloud_GetData(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, const float **outPointCloudData) | 获取点云中所有点的坐标及置信度数组。 |
| AREngine_ARStatus HMS_AREngine_ARPointCloud_GetNumberOfPoints(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, int32_t *outNumberOfPoints) | 获取点云中所有点的坐标及置信度数组大小。 |
| AREngine_ARStatus HMS_AREngine_ARPointCloud_GetTimestamp(const AREngine_ARSession *session, const AREngine_ARPointCloud *pointCloud, int64_t *outTimestampNs) | 获取检测到当前特征点云的时间，以ns为单位。 |
| void HMS_AREngine_ARPointCloud_Release(AREngine_ARPointCloud *pointCloud) | 释放点云对象使用的内存。 |
| AREngine_ARStatus HMS_AREngine_ARPose_Create(const AREngine_ARSession *session, const float *poseRaw, const uint32_t poseRawSize, AREngine_ARPose **outPose) | 分配并初始化一个新的位姿对象。 |
| void HMS_AREngine_ARPose_Destroy(AREngine_ARPose *pose) | 释放位姿对象使用的内存。 |
| AREngine_ARStatus HMS_AREngine_ARPose_GetMatrix(const AREngine_ARSession *session, const AREngine_ARPose *pose, float *outMatrixColMajor4x4, int32_t matrixColMajor4x4Size) | 将位姿数据转换成4X4的矩阵。 |
| AREngine_ARStatus HMS_AREngine_ARPose_GetPoseRaw(const AREngine_ARSession *session, const AREngine_ARPose *pose, float *outPoseRaw, int32_t poseRawSize) | 从位姿对象提取位姿数据。 |
| AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireIndexList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outData, int32_t dataSize) | 获取mesh面片的索引集合。 |
| AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireIndexListSize(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outSize) | 获取mesh面片的索引个数。 |
| AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVertexList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, float *outData, int32_t dataSize) | 获取mesh的顶点集合。 |
| AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVertexNormalList(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, float *outData, int32_t dataSize) | 获取mesh面片的法向量集合。 |
| AREngine_ARStatus HMS_AREngine_ARSceneMesh_AcquireVerticesSize(const AREngine_ARSession *session, const AREngine_ARSceneMesh *sceneMesh, int32_t *outSize) | 获取mesh的顶点个数。 |
| void HMS_AREngine_ARSceneMesh_Release(AREngine_ARSceneMesh *SceneMesh) | 释放当前帧的mesh信息。 |
| AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquireCubeData(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData *semanticDenseData, AREngine_ARSemanticDenseCubeData **outCubeData) | 获取识别到的高精几何重建对象数据中的立方体数据。 |
| AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquireCubeDataSize(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData *semanticDenseData, int64_t *outSize) | 获取识别到的高精几何重建对象数据中的立方体数量。 |
| AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquirePointData(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData *semanticDenseData, AREngine_ARSemanticDensePointData **outPointData) | 获取识别到的高精几何重建对象数据中的稠密点云数据。 |
| AREngine_ARStatus HMS_AREngine_ARSemanticDense_AcquirePointDataSize(const AREngine_ARSession *session, const AREngine_ARSemanticDenseData *semanticDenseData, int64_t *outSize) | 获取识别到的高精几何重建对象数据中的稠密点云数量。 |
| void HMS_AREngine_ARSemanticDense_Release(AREngine_ARSemanticDenseData *semanticDenseData) | 释放高精几何重建对象。 |
| AREngine_ARStatus HMS_AREngine_ARSession_AcquireNewAnchor(AREngine_ARSession *session, const AREngine_ARPose *pose, AREngine_ARAnchor **outAnchor) | 创建一个持续跟踪的锚点。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Configure(AREngine_ARSession *session, const AREngine_ARConfig *config) | 配置AREngine_ARSession会话。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Create(void *env, void *applicationContext, AREngine_ARSession **outSessionPointer) | 创建一个新的AREngine_ARSession会话。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Create_Human_Perception(void *env, void *applicationContext, AREngine_ARSession **outSessionPointer) | 创建一个新的AREngine_ARSession人体追踪会话。 |
| void HMS_AREngine_ARSession_Destroy(AREngine_ARSession *session) | 释放AREngine_ARSession会话使用的资源。 |
| AREngine_ARStatus HMS_AREngine_ARSession_GetCameraConfig(const AREngine_ARSession *session, AREngine_ARCameraConfig *outCameraConfig) | 获取相机配置信息。 |
| AREngine_ARStatus HMS_AREngine_ARSession_GetAllAnchors(const AREngine_ARSession *session, AREngine_ARAnchorList *outAnchorList) | 获取所有锚点，包括AREngine_ARTrackingState中包含的所有状态下的锚点。 |
| AREngine_ARStatus HMS_AREngine_ARSession_GetAllTrackables(const AREngine_ARSession *session, AREngine_ARTrackableType filterType, AREngine_ARTrackableList *outTrackableList) | 获取所有指定类型的可跟踪对象集合。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Pause(AREngine_ARSession *session) | 暂停会话，停止相机预览流，不清除平面和锚点数据，释放相机（否则其他应用无法使用相机服务）。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Resume(AREngine_ARSession *session) | 开始运行AREngine_ARSession，或者在调用HMS_AREngine_ARSession_Pause以后恢复AREngine_ARSession的运行状态。 |
| AREngine_ARStatus HMS_AREngine_ARSession_SetCameraGLTexture(AREngine_ARSession *session, uint32_t textureId) | 设置可用于存储相机预览流数据的OpenGL纹理。 |
| AREngine_ARStatus HMS_AREngine_ARSession_SetDisplayGeometry(AREngine_ARSession *session, AREngine_ARPoseType rotation, int32_t width, int32_t height) | 设置显示的高和宽，以像素为单位。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Stop(AREngine_ARSession *session) | 停止AR Engine，停止相机预览流，清除平面和锚点数据，并释放相机，终止本次会话。 |
| AREngine_ARStatus HMS_AREngine_ARSession_Update(AREngine_ARSession *session, AREngine_ARFrame *outFrame) | 更新AR Engine的计算结果。 |
| AREngine_ARStatus HMS_AREngine_ARTarget_GetAxisAlignedBoundingBox(const AREngine_ARSession *session, const AREngine_ARTarget *target, float *outAabb, int32_t aabbSize) | 获取语义物体最小外接包围盒坐标，坐标格式为（xmin，ymin，zmin，xmax，ymax，zmax）。 |
| AREngine_ARStatus HMS_AREngine_ARTarget_GetCenterPose(const AREngine_ARSession *session, const AREngine_ARTarget *target, AREngine_ARPose *outARPose) | 获取从目标语义对象的局部坐标系到世界坐标系转换的位姿对象。 |
| AREngine_ARStatus HMS_AREngine_ARTarget_GetRadius(const AREngine_ARSession *session, const AREngine_ARTarget *target, float *radius) | 获取语义物体的球体半径。 |
| AREngine_ARStatus HMS_AREngine_ARTarget_GetShapeType(const AREngine_ARSession *session, const AREngine_ARTarget *target, AREngine_ARTargetShapeLabel *shape) | 获取语义物体的形状类型。 |
| AREngine_ARStatus HMS_AREngine_ARTrackable_AcquireNewAnchor(AREngine_ARSession *session, AREngine_ARTrackable *trackable, AREngine_ARPose *pose, AREngine_ARAnchor **outAnchor) | 通过可跟踪对象的位姿信息创建对应的锚点对象，该锚点将和当前的可跟踪对象绑定。 |
| AREngine_ARStatus HMS_AREngine_ARTrackable_GetAnchors(AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARAnchorList *outAnchorList) | 获取绑定到输入可跟踪对象的锚点对象列表。 |
| AREngine_ARStatus HMS_AREngine_ARTrackable_GetTrackingState(const AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARTrackingState *outTrackingState) | 获取当前可跟踪对象的跟踪状态。 |
| AREngine_ARStatus HMS_AREngine_ARTrackable_GetType(const AREngine_ARSession *session, const AREngine_ARTrackable *trackable, AREngine_ARTrackableType *outTrackableType) | 获取可跟踪对象的类型。 |
| void HMS_AREngine_ARTrackable_Release(AREngine_ARTrackable *trackable) | 释放可跟踪对象。 |
| AREngine_ARStatus HMS_AREngine_ARTrackableList_AcquireItem(const AREngine_ARSession *session, const AREngine_ARTrackableList *trackableList, int32_t index, AREngine_ARTrackable **outTrackable) | 从可跟踪列表中获取指定index的对象。 |
| AREngine_ARStatus HMS_AREngine_ARTrackableList_Create(const AREngine_ARSession *session, AREngine_ARTrackableList **outTrackableList) | 创建一个可跟踪对象列表。 |
| void HMS_AREngine_ARTrackableList_Destroy(AREngine_ARTrackableList *trackableList) | 释放可跟踪对象列表，以及它持有的所有锚点引用。 |
| AREngine_ARStatus HMS_AREngine_ARTrackableList_GetSize(const AREngine_ARSession *session, const AREngine_ARTrackableList *trackableList, int32_t *outSize) | 获取此列表中的可跟踪对象的数量。 |
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