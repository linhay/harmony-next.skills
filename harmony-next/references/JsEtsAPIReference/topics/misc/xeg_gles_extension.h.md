# xeg_gles_extension.h

**概述**

XEngine扩展特性查询接口（OpenGL ES）。

引用文件：<xengine/xeg_gles_extension.h>

库： libxengine.so

系统能力： SystemCapability.Graphic.XEngine

起始版本： 5.0.0(12)

相关模块： [XEngine](XEngine.md)

**汇总**

**宏定义**

| 名称 | 描述 |
| --- | --- |
| XEG_EXTENSIONS 0x01U | 作为HMS_XEG_GetString接口的入参，以获取XEngine支持的OpenGL ES扩展特性。 |

**类型定义**

| 名称 | 描述 |
| --- | --- |
| typedef const GLubyte *(GL_APIENTRYP PFN_HMS_XEG_GETSTRING) (GLenum name) | XEngine OpenGL ES扩展特性查询接口函数指针定义。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| const GLubyte * HMS_XEG_GetString (GLenum name) | XEngine OpenGL ES扩展特性查询接口。 |