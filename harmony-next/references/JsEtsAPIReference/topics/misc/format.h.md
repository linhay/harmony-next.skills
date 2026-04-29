# format.h

**概述**

提供张量数据的排列格式。

引用文件： <mindspore/format.h>

库： libmindspore_lite_ndk.so

系统能力： SystemCapability.Ai.MindSpore

起始版本： 9

相关模块： [MindSpore](MindSpore.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AI_Format | OH_AI_Format | MSTensor保存的数据支持的排列格式。 |

**枚举类型说明**

**OH_AI_Format**

```ets
enum OH_AI_Format
```

描述

MSTensor保存的数据支持的排列格式。

起始版本： 9

| 枚举项 | 描述 |
| --- | --- |
| OH_AI_FORMAT_NCHW = 0 | 按批次N、通道C、高度H和宽度W的顺序存储张量数据。 |
| OH_AI_FORMAT_NHWC = 1 | 按批次N、高度H、宽度W和通道C的顺序存储张量数据。 |
| OH_AI_FORMAT_NHWC4 = 2 | 按批次N、高度H、宽度W和通道C的顺序存储张量数据，其中C轴是4字节对齐格式。 |
| OH_AI_FORMAT_HWKC = 3 | 按高度H、宽度W、核数K和通道C的顺序存储张量数据。 |
| OH_AI_FORMAT_HWCK = 4 | 按高度H、宽度W、通道C和核数K的顺序存储张量数据。 |
| OH_AI_FORMAT_KCHW = 5 | 按核数K、通道C、高度H和宽度W的顺序存储张量数据。 |
| OH_AI_FORMAT_CKHW = 6 | 按通道C、核数K、高度H和宽度W的顺序存储张量数据。 |
| OH_AI_FORMAT_KHWC = 7 | 按核数K、高度H、宽度W和通道C的顺序存储张量数据。 |
| OH_AI_FORMAT_CHWK = 8 | 按通道C、高度H、宽度W和核数K的顺序存储张量数据。 |
| OH_AI_FORMAT_HW = 9 | 按高度H和宽度W的顺序存储张量数据。 |
| OH_AI_FORMAT_HW4 = 10 | 按高度H和宽度W的顺序存储张量数据，其中W轴是4字节对齐格式。 |
| OH_AI_FORMAT_NC = 11 | 按批次N和通道C的顺序存储张量数据。 |
| OH_AI_FORMAT_NC4 = 12 | 按批次N和通道C的顺序存储张量数据，其中C轴是4字节对齐格式。 |
| OH_AI_FORMAT_NC4HW4 = 13 | 按批次N、通道C、高度H和宽度W的顺序存储张量数据，其中C轴和W轴是4字节对齐格式。 |
| OH_AI_FORMAT_NCDHW = 15 | 按批次N、通道C、深度D、高度H和宽度W的顺序存储张量数据。 |
| OH_AI_FORMAT_NWC = 16 | 按批次N、宽度W和通道C的顺序存储张量数据。 |
| OH_AI_FORMAT_NCW = 17 | 按批次N、通道C和宽度W的顺序存储张量数据。 |