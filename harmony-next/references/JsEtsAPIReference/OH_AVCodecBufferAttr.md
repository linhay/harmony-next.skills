# OH_AVCodecBufferAttr

```ets
typedef struct OH_AVCodecBufferAttr {...} OH_AVCodecBufferAttr
```

#### 概述

定义OH_AVCodec的缓冲区描述信息。

**起始版本：** 9

**相关模块：**[Core](Core.md)

**所在头文件：**[native_avbuffer_info.h](native_avbuffer_info.h.md)

#### 汇总

#### 成员变量

名称描述int64_t pts此缓冲区的显示时间戳（以微秒为单位）。int32_t size缓冲区中包含的数据的大小（以字节为单位）。int32_t offset此缓冲区中有效数据的起始偏移量。uint32_t flags此缓冲区具有的标志，请参阅[OH_AVCodecBufferFlags](native_avbuffer_info.h.md#ZH-CN_TOPIC_0000002529445705__oh_avcodecbufferflags)。