# abr_base.h

**概述**

声明不区分图形API平台的ABR（自适应稳态渲染）接口。

引用文件： <graphics_game_sdk/abr_base.h>

库： libabr.so

系统能力： SystemCapability.GraphicsGame.RenderAccelerate

起始版本： 5.0.0(12)

相关模块： [GraphicsAccelerate](GraphicsAccelerate.md)

**汇总**

**结构体**

| 名称 | 描述 |
| --- | --- |
| struct ABR_Vector3 | 此结构体描述ABR三维向量。 |
| struct ABR_CameraData | 此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef struct ABR_Context ABR_Context | 此结构体描述ABR上下文。 |
| typedef enum ABR_RenderAPI_Type ABR_RenderAPI_Type | 此枚举描述ABR支持的图形API类型。 |
| typedef struct ABR_Vector3 ABR_Vector3 | 此结构体描述ABR三维向量。 |
| typedef struct ABR_CameraData ABR_CameraData | 此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。 |
| typedef enum ABR_ErrorCode ABR_ErrorCode | 此枚举描述ABR接口调用错误码。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| ABR_RenderAPI_Type { RENDER_API_GLES = 0 } | 此枚举描述ABR支持的图形API类型。 |
| ABR_ErrorCode { ABR_SUCCESS = 0, ABR_INVALID_PARAMETER = 401, ABR_CONTEXT_CONFIG_AFTER_ACTIVE = 1009501001, ABR_CONTEXT_NOT_CONFIG = 1009501002, ABR_CONTEXT_NOT_ACTIVE = 1009501003, ABR_METADATA_INVALID = 1009501004, ABR_FRAMEBUFFER_INVALID = 1009501005 } | 此枚举描述ABR接口调用错误码。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| ABR_Context* HMS_ABR_CreateContext(ABR_RenderAPI_Type type) | 创建ABR上下文实例，每次调用会新建ABR_Context对象，并返回指向ABR_Context对象的指针。 |
| ABR_ErrorCode HMS_ABR_SetTargetFps(ABR_Context* context, const uint32_t targetFps) | 配置ABR上下文实例的目标帧率属性。 |
| ABR_ErrorCode HMS_ABR_SetScaleRange(ABR_Context* context, const float minValue, const float maxValue) | 配置ABR上下文实例的Buffer分辨率因子范围属性。 |
| ABR_ErrorCode HMS_ABR_Activate(ABR_Context* context) | 激活ABR上下文实例。激活ABR上下文实例前需调用HMS_ABR_SetTargetFps和HMS_ABR_SetScaleRange接口进行实例属性的配置。 |
| ABR_ErrorCode HMS_ABR_IsActive(ABR_Context* context, bool* isActive) | 查询ABR上下文实例是否处于激活状态。 |
| ABR_ErrorCode HMS_ABR_Deactivate(ABR_Context* context) | 去激活ABR上下文实例，可通过HMS_ABR_Activate重新激活。 |
| ABR_ErrorCode HMS_ABR_UpdateCameraData(ABR_Context* context, ABR_CameraData* data) | 更新每帧相机运动数据，ABR更新相机运动数据前需调用HMS_ABR_Activate接口激活ABR上下文实例。 |
| ABR_ErrorCode HMS_ABR_GetScale(ABR_Context* context, float* scale) | 获取ABR Buffer分辨率因子。 |
| ABR_ErrorCode HMS_ABR_GetNextScale(ABR_Context* context, float* scale) | 获取下一帧的ABR Buffer分辨率因子。 |
| ABR_ErrorCode HMS_ABR_DestroyContext(ABR_Context** context) | 销毁ABR上下文实例并释放内存资源。 |