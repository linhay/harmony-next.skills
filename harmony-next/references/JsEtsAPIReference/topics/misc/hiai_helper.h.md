# hiai_helper.h

**概述**

查询CANN Kit版本以及检查模型支持情况的接口。

引用文件： <CANNKit/hiai_helper.h>

库： libhiai_foundation.so

系统能力： SystemCapability.AI.HiAIFoundation

起始版本： 4.1.0(11)

相关模块： [CANN](CANN.md)

**汇总**

**枚举**

| 名称 | 描述 |
| --- | --- |
| HiAI_Compatibility { HIAI_COMPATIBILITY_COMPATIBLE = 0, HIAI_COMPATIBILITY_INCOMPATIBLE = 1 } | 编译后模型兼容性结果。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| const char * HMS_HiAI_GetVersion (void) | 获取CANN Kit版本号，并通过返回模板hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3指定X1是否为0来区分是否支持NPU。若X1为0，则表示不支持NPU；若X1为非0，则表示支持NPU。 |
| HiAI_Compatibility HMS_HiAICompatibility_CheckFromFile (const char *file) | 查询编译后储存在文件中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。 |
| HiAI_Compatibility HMS_HiAICompatibility_CheckFromBuffer (const void *data, size_t size) | 查询编译后储存在内存中的模型的兼容性。 若发生不兼容情况，建议重新编译模型。 |