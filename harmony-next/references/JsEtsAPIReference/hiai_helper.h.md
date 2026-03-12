# hiai_helper.h

#### 概述

查询CANN Kit版本以及检查模型支持情况的接口。

**库：** libhiai_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

**相关模块：**[CANN](CANN.md)

#### 汇总

#### 枚举

名称

描述

[HiAI_Compatibility](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_compatibility) {

HIAI_COMPATIBILITY_COMPATIBLE = 0,

HIAI_COMPATIBILITY_INCOMPATIBLE = 1

}

编译后模型兼容性结果。

#### 函数

名称

描述

const char * [HMS_HiAI_GetVersion](CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiai_getversion) (void)

获取CANN Kit版本号。

[HiAI_Compatibility](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_compatibility)[HMS_HiAICompatibility_CheckFromFile](CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaicompatibility_checkfromfile) (const char *file)

查询编译后储存在文件中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。

[HiAI_Compatibility](CANN.md#ZH-CN_TOPIC_0000002528648479__hiai_compatibility)[HMS_HiAICompatibility_CheckFromBuffer](CANN.md#ZH-CN_TOPIC_0000002528648479__hms_hiaicompatibility_checkfrombuffer) (const void *data, size_t size)

查询编译后储存在内存中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。