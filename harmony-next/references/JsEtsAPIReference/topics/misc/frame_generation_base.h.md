# frame_generation_base.h

**概述**

声明不区分图形API平台的超帧接口。

引用文件： <graphics_game_sdk/frame_generation_base.h>

库： libframegeneration.so

系统能力： SystemCapability.GraphicsGame.RenderAccelerate

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct FG_Mat4x4 | 此结构体描述列主序4x4矩阵。 |
| struct FG_AlgorithmModeInfo | 此结构体描述超帧算法模式信息。 |
| struct FG_Dimension2D | 此结构体描述2D图像分辨率，以像素为单位。 |
| struct FG_ResolutionInfo | 此结构体描述超帧输入输出图像的分辨率。 |
| struct FG_Vec3D | 此结构体描述超帧三维向量。 |
| struct FG_PerFrameExtendedCameraInfo | 此结构体描述相机扩展信息。当视图投影矩阵的平移分量非常大时，可以提供更加详细的相机信息以获得更加准确的超帧预测效果。 |
| struct FG_IntegrationInfo | 此结构体描述超帧集成的信息。包括显示模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct FG_Mat4x4 FG_Mat4x4 | 此结构体描述列主序4x4矩阵。 |
| typedef enum FG_PredictionMode FG_PredictionMode | 此枚举描述超帧预测算法模式。 |
| typedef enum FG_MeMode FG_MeMode | 此枚举描述超帧运动估计算法模式，支持基础模式和增强模式。 |
| typedef struct FG_AlgorithmModeInfo FG_AlgorithmModeInfo | 此结构体描述超帧算法模式信息。 |
| typedef enum FG_ErrorCode FG_ErrorCode | 此枚举描述超帧接口调用错误码。 |
| typedef enum FG_CvvZSemantic FG_CvvZSemantic | 此枚举描述经过相机投影变换后，齐次裁剪空间Z/W范围及深度测试模式。 |
| typedef enum FG_PresentMode FG_PresentMode | 定义预测帧呈现模式，该模式包括两种：游戏端预测帧呈现和系统端预测帧呈现。 |
| typedef struct FG_Dimension2D FG_Dimension2D | 此结构体描述2D图像分辨率，以像素为单位。 |
| typedef struct FG_ResolutionInfo FG_ResolutionInfo | 此结构体描述超帧输入输出图像的分辨率。 |
| typedef struct FG_Vec3D FG_Vec3D | 此结构体描述超帧三维向量。 |
| typedef struct FG_PerFrameExtendedCameraInfo FG_PerFrameExtendedCameraInfo | 此结构体描述相机扩展信息。当视图投影矩阵的平移分量非常大时，可以提供更加详细的相机信息以获得更加准确的超帧预测效果。 |
| typedef struct FG_IntegrationInfo | 此结构体描述超帧集成的信息。包括显示模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| FG_PredictionMode { FG_PREDICTION_MODE_INTERPOLATION = 0, FG_PREDICTION_MODE_EXTRAPOLATION = 1 } | 此枚举描述超帧预测算法模式。 |
| FG_MeMode { FG_ME_MODE_BASIC = 0, FG_ME_MODE_ENHANCED = 1 } | 此枚举描述超帧运动估计算法模式，支持基础模式和增强模式。 |
| FG_ErrorCode { FG_SUCCESS = 0, FG_INVALID_PARAMETER = 401, FG_CONTEXT_NOT_CONFIG = 1009500001, FG_CONTEXT_NOT_ACTIVE = 1009500002, FG_COLLECTING_PREVIOUS_FRAMES = 1009500003 } | 此枚举描述超帧接口调用错误码。 |
| FG_CvvZSemantic { FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z = 0, FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_REVERSE_Z = 1, FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_REVERSE_Z = 2, FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_FORWARD_Z = 3 } | 此枚举描述经过相机投影变换后，齐次裁剪空间Z/W范围及深度测试模式。 |
| FG_PresentMode { FG_PRESENT_BY_GAME = 0, FG_PRESENT_BY_SYSTEM = 1 } | 定义预测帧呈现模式，该模式包括两种：游戏端预测帧呈现和系统端预测帧呈现。 |