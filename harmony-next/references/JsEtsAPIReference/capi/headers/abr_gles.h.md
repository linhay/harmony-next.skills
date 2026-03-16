# abr_gles.h

#### 概述

声明OpenGL ES图形API平台的ABR接口。

**库：** libabr.so

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 5.0.0(12)

**相关模块：**[GraphicsAccelerate](../../topics/graphics/GraphicsAccelerate.md)

#### 汇总

#### 函数

名称

描述

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_MarkFrameBuffer_GLES](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga821fb33620312d3adba51d30254c1ef0)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context)

标记ABR进行自适应渲染处理的GLES Buffer，需要在GLES Buffer开始渲染前调用此接口。

[ABR_ErrorCode](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga72df702d70a8326b5b46c118be6ad1d7)[HMS_ABR_GetScaledTexture_GLES](../../topics/graphics/GraphicsAccelerate.md#section791920394423)([ABR_Context](../../topics/graphics/GraphicsAccelerate.md#ZH-CN_TOPIC_0000002418917005__ga52e8dba39ee979b70826401b3d36574e)* context, uint32_t originTexture, uint32_t* scaledTexture)

根据原始GLES纹理获取ABR渲染后的GLES纹理。