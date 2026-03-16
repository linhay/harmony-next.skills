# abr_base.h

#### 概述

声明不区分图形API平台的ABR（自适应稳态渲染）接口。

**库：** libabr.so

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](../../topics/graphics/GraphicsAccelerate.md)

#### 汇总

#### 结构体

名称

描述

struct [ABR_Vector3](../../topics/misc/ABR_Vector3.md)

此结构体描述ABR三维向量。

struct [ABR_CameraData](../../topics/media/ABR_CameraData.md)

此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。

#### 类型定义

名称

描述

typedef struct [ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)[ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)

此结构体描述ABR上下文。

typedef enum [ABR_RenderAPI_Type](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9359d16ecefa21f0e6e5f29732cbf6f4)[ABR_RenderAPI_Type](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga3a6ead3a3c0f19a6434e97fda13f42f2)

此枚举描述ABR支持的图形API类型。

typedef struct [ABR_Vector3](../../topics/misc/ABR_Vector3.md)[ABR_Vector3](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga71a845f23f7ec4c0935db8e9f00ab8b9)

此结构体描述ABR三维向量。

typedef struct [ABR_CameraData](../../topics/media/ABR_CameraData.md)[ABR_CameraData](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gada21a47272d5db8e28e2a9bb4fd033d4)

此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。

typedef enum [ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga86d5860f91dc4f1de6b381cd65389b9d)

此枚举描述ABR接口调用错误码。

#### 枚举

名称

描述

[ABR_RenderAPI_Type](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9359d16ecefa21f0e6e5f29732cbf6f4) {

RENDER_API_GLES = 0

}

此枚举描述ABR支持的图形API类型。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7) {

ABR_SUCCESS = 0,

ABR_INVALID_PARAMETER = 401,

ABR_CONTEXT_CONFIG_AFTER_ACTIVE = 1009501001,

ABR_CONTEXT_NOT_CONFIG = 1009501002,

ABR_CONTEXT_NOT_ACTIVE = 1009501003,

ABR_METADATA_INVALID = 1009501004,

ABR_FRAMEBUFFER_INVALID = 1009501005

}

此枚举描述ABR接口调用错误码。

#### 函数

名称

描述

[ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* [HMS_ABR_CreateContext](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga8f785903a5382ff31baef78a3968f66a)([ABR_RenderAPI_Type](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga9359d16ecefa21f0e6e5f29732cbf6f4) type)

创建ABR上下文实例，每次调用会新建[ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)对象，并返回指向[ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)对象的指针。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_SetTargetFps](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6c613e02088d559b9dc1450fde15bc2a)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, const uint32_t targetFps)

配置ABR上下文实例的目标帧率属性。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_SetScaleRange](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1001c6a7739d8ce57bf851986f121bf5)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, const float minValue, const float maxValue)

配置ABR上下文实例的Buffer分辨率因子范围属性。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_Activate](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga463d8d5396bfd5f6ed800ddab616479a)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context)

激活ABR上下文实例。激活ABR上下文实例前需调用[HMS_ABR_SetTargetFps](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga6c613e02088d559b9dc1450fde15bc2a)和[HMS_ABR_SetScaleRange](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga1001c6a7739d8ce57bf851986f121bf5)接口进行实例属性的配置。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_IsActive](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga791519fde19801e6da60094cf077b00f)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, bool* isActive)

查询ABR上下文实例是否处于激活状态。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_Deactivate](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga4abb4b37392e77c15fbedfa8ceba3da4)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context)

去激活ABR上下文实例，可通过[HMS_ABR_Activate](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga463d8d5396bfd5f6ed800ddab616479a)重新激活。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_UpdateCameraData](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga5b895e36d31e46f71d04aba78c8f3716)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, [ABR_CameraData](../../topics/media/ABR_CameraData.md)* data)

更新每帧相机运动数据，ABR更新相机运动数据前需调用[HMS_ABR_Activate](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga463d8d5396bfd5f6ed800ddab616479a)接口激活ABR上下文实例。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_GetScale](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga936129328fea3a5f77b2aae4935f67c6)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, float* scale)

获取ABR Buffer分辨率因子。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_GetNextScale](../../topics/graphics/GraphicsAccelerate.md#section157311245143415)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, float* scale)

获取下一帧的ABR Buffer分辨率因子。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_DestroyContext](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__gaf3c03179b9bcf1b8475230cbbb0d877c)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)** context)

销毁ABR上下文实例并释放内存资源。