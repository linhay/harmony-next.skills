# format.h

#### 概述

提供张量数据的排列格式。

**引用文件：** <mindspore/format.h>

**库：** libmindspore_lite_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：**[MindSpore](../../topics/misc/MindSpore.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_AI_Format](#ZH-CN_TOPIC_0000002497446158__oh_ai_format)OH_AI_FormatMSTensor保存的数据支持的排列格式。

#### 枚举类型说明

#### OH_AI_Format

```ets
enum OH_AI_Format
```

**描述**

MSTensor保存的数据支持的排列格式。

**起始版本：** 9

枚举项描述OH_AI_FORMAT_NCHW = 0按批次N、通道C、高度H和宽度W的顺序存储张量数据。OH_AI_FORMAT_NHWC = 1按批次N、高度H、宽度W和通道C的顺序存储张量数据。OH_AI_FORMAT_NHWC4 = 2按批次N、高度H、宽度W和通道C的顺序存储张量数据，其中C轴是4字节对齐格式。OH_AI_FORMAT_HWKC = 3按高度H、宽度W、核数K和通道C的顺序存储张量数据。OH_AI_FORMAT_HWCK = 4按高度H、宽度W、通道C和核数K的顺序存储张量数据。OH_AI_FORMAT_KCHW = 5按核数K、通道C、高度H和宽度W的顺序存储张量数据。OH_AI_FORMAT_CKHW = 6按通道C、核数K、高度H和宽度W的顺序存储张量数据。OH_AI_FORMAT_KHWC = 7按核数K、高度H、宽度W和通道C的顺序存储张量数据。OH_AI_FORMAT_CHWK = 8按通道C、高度H、宽度W和核数K的顺序存储张量数据。OH_AI_FORMAT_HW = 9按高度H和宽度W的顺序存储张量数据。OH_AI_FORMAT_HW4 = 10按高度H和宽度W的顺序存储张量数据，其中W轴是4字节对齐格式。OH_AI_FORMAT_NC = 11按批次N和通道C的顺序存储张量数据。OH_AI_FORMAT_NC4 = 12按批次N和通道C的顺序存储张量数据，其中C轴是4字节对齐格式。OH_AI_FORMAT_NC4HW4 = 13按批次N、通道C、高度H和宽度W的顺序存储张量数据，其中C轴和W轴是4字节对齐格式。OH_AI_FORMAT_NCDHW = 15按批次N、通道C、深度D、高度H和宽度W的顺序存储张量数据。OH_AI_FORMAT_NWC = 16按批次N、宽度W和通道C的顺序存储张量数据。OH_AI_FORMAT_NCW = 17按批次N、通道C和宽度W的顺序存储张量数据。