# frame_generation_base.h

#### 概述

声明不区分图形API平台的超帧接口。

**库：** libframegeneration.so

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](../../topics/graphics/GraphicsAccelerate.md)

#### 汇总

#### 结构体

名称

描述

struct [FG_Mat4x4](../../topics/misc/FG_Mat4x4.md)

此结构体描述列主序4x4矩阵。

struct [FG_AlgorithmModeInfo](../../topics/misc/FG_AlgorithmModeInfo.md)

此结构体描述超帧算法模式信息。

struct [FG_Dimension2D](../../topics/misc/FG_Dimension2D.md)

此结构体描述2D图像分辨率，以像素为单位。

struct [FG_ResolutionInfo](../../topics/misc/FG_ResolutionInfo.md)

此结构体描述超帧输入输出图像的分辨率。

struct [FG_Vec3D](../../topics/misc/FG_Vec3D.md)

此结构体描述超帧三维向量。

struct [FG_PerFrameExtendedCameraInfo](../../topics/components/FG_PerFrameExtendedCameraInfo.md)

此结构体描述相机扩展信息。当视图投影矩阵的平移分量非常大时，可以提供更加详细的相机信息以获得更加准确的超帧预测效果。

struct [FG_IntegrationInfo](../../topics/misc/FG_IntegrationInfo.md)

此结构体描述超帧集成的信息。包括显示模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。

#### 类型定义

名称

描述

typedef struct [FG_Mat4x4](../../topics/misc/FG_Mat4x4.md)[FG_Mat4x4](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabbf87d3423630e0b50f19da2cbda3e90)

此结构体描述列主序4x4矩阵。

typedef enum [FG_PredictionMode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766)[FG_PredictionMode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga79e55783a2a38873fc6890c297885275)

此枚举描述超帧预测算法模式。

typedef enum [FG_MeMode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8bd44b6bea12774dd2ee6014d696e7d1)[FG_MeMode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga81cbe226af620e6ef19cd8ec5e9b5256)

此枚举描述超帧运动估计算法模式，支持基础模式和增强模式。

typedef struct [FG_AlgorithmModeInfo](../../topics/misc/FG_AlgorithmModeInfo.md)[FG_AlgorithmModeInfo](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1750087784d7cbf19957243db12a7ba3)

此结构体描述超帧算法模式信息。

typedef enum [FG_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669)[FG_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga394c554fc5d056d702180ee031ccee2c)

此枚举描述超帧接口调用错误码。

typedef enum [FG_CvvZSemantic](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267)[FG_CvvZSemantic](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gabac7987ddc62b712f36d95b185e47bb2)

此枚举描述经过相机投影变换后，齐次裁剪空间Z/W范围及深度测试模式。

typedef enum [FG_PresentMode](../../topics/graphics/GraphicsAccelerate.md#section11881356193212)[FG_PresentMode](../../topics/graphics/GraphicsAccelerate.md#section11881356193212)

定义预测帧呈现模式，该模式包括两种：游戏端预测帧呈现和系统端预测帧呈现。

typedef struct [FG_Dimension2D](../../topics/misc/FG_Dimension2D.md)[FG_Dimension2D](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga545268ccc070666954981580f5764d20)

此结构体描述2D图像分辨率，以像素为单位。

typedef struct [FG_ResolutionInfo](../../topics/misc/FG_ResolutionInfo.md)[FG_ResolutionInfo](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gacbc0d894e11f18711fd4558d45c7cd39)

此结构体描述超帧输入输出图像的分辨率。

typedef struct [FG_Vec3D](../../topics/misc/FG_Vec3D.md)[FG_Vec3D](../../topics/misc/FG_Vec3D.md)

此结构体描述超帧三维向量。

typedef struct [FG_PerFrameExtendedCameraInfo](../../topics/components/FG_PerFrameExtendedCameraInfo.md)[FG_PerFrameExtendedCameraInfo](../../topics/components/FG_PerFrameExtendedCameraInfo.md)

此结构体描述相机扩展信息。当视图投影矩阵的平移分量非常大时，可以提供更加详细的相机信息以获得更加准确的超帧预测效果。

typedef struct [FG_IntegrationInfo](../../topics/misc/FG_IntegrationInfo.md)

此结构体描述超帧集成的信息。包括显示模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。

#### 枚举

名称

描述

[FG_PredictionMode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaea2169cd5ae4bf9e8a17dc58f33e8766) {

FG_PREDICTION_MODE_INTERPOLATION = 0,

FG_PREDICTION_MODE_EXTRAPOLATION = 1

}

此枚举描述超帧预测算法模式。

[FG_MeMode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8bd44b6bea12774dd2ee6014d696e7d1) {

FG_ME_MODE_BASIC = 0,

FG_ME_MODE_ENHANCED = 1

}

此枚举描述超帧运动估计算法模式，支持基础模式和增强模式。

[FG_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga68efbf5ff41faeb835f5587654c1e669) {

FG_SUCCESS = 0,

FG_INVALID_PARAMETER = 401,

FG_CONTEXT_NOT_CONFIG = 1009500001,

FG_CONTEXT_NOT_ACTIVE = 1009500002,

FG_COLLECTING_PREVIOUS_FRAMES = 1009500003

}

此枚举描述超帧接口调用错误码。

[FG_CvvZSemantic](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga530448309918d6d703e28c61a848a267) {

FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_FORWARD_Z = 0,

FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_REVERSE_Z = 1,

FG_CVV_Z_SEMANTIC_MINUS_ONE_TO_ONE_REVERSE_Z = 2,

FG_CVV_Z_SEMANTIC_ZERO_TO_ONE_FORWARD_Z = 3

}

此枚举描述经过相机投影变换后，齐次裁剪空间Z/W范围及深度测试模式。

[FG_PresentMode](../../topics/graphics/GraphicsAccelerate.md#section11881356193212) {

FG_PRESENT_BY_GAME = 0,

FG_PRESENT_BY_SYSTEM = 1

}

定义预测帧呈现模式，该模式包括两种：游戏端预测帧呈现和系统端预测帧呈现。