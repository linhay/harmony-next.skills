# xeg_gles_extension.h

#### 概述

XEngine扩展特性查询接口（OpenGL ES）。

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

**相关模块： **[XEngine](../../topics/misc/XEngine.md)

#### 汇总

#### 宏定义

名称

描述

[XEG_EXTENSIONS](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__xeg_extensions) 0x01U

作为[HMS_XEG_GetString](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_getstring)接口的入参，以获取XEngine支持的OpenGL ES扩展特性。

#### 类型定义

名称

描述

typedef const GLubyte *(GL_APIENTRYP [PFN_HMS_XEG_GETSTRING](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__pfn_hms_xeg_getstring)) (GLenum name)

XEngine OpenGL ES扩展特性查询接口函数指针定义。

#### 函数

名称

描述

const GLubyte * [HMS_XEG_GetString](../../topics/misc/XEngine.md#ZH-CN_TOPIC_0000002328319196__hms_xeg_getstring) (GLenum name)

XEngine OpenGL ES扩展特性查询接口。