# native_avbuffer_info.h

#### 概述

声明了媒体数据结构AVBuffer属性的定义。

**引用文件：** <multimedia/player_framework/native_avbuffer_info.h>

**库：** libnative_media_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**相关模块：**[Core](../../topics/misc/Core.md)

**相关示例：**[AVCodec](https://gitcode.com/HarmonyOS/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVCodecBufferAttr](../../topics/misc/OH_AVCodecBufferAttr.md)OH_AVCodecBufferAttr定义OH_AVCodec的缓冲区描述信息。

#### 枚举

名称typedef关键字描述[OH_AVCodecBufferFlags](#ZH-CN_TOPIC_0000002529445705__oh_avcodecbufferflags)OH_AVCodecBufferFlags枚举OH_AVCodec缓冲区标记的类别。

#### 枚举类型说明

#### OH_AVCodecBufferFlags

```ets
enum OH_AVCodecBufferFlags
```

**描述**

枚举OH_AVCodec缓冲区标记的类别。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

枚举项描述AVCODEC_BUFFER_FLAGS_NONE = 0表示为普通帧。AVCODEC_BUFFER_FLAGS_EOS = 1 << 0表示缓冲区是流结束帧。AVCODEC_BUFFER_FLAGS_SYNC_FRAME = 1 << 1表示缓冲区包含关键帧。AVCODEC_BUFFER_FLAGS_INCOMPLETE_FRAME = 1 << 2表示缓冲区中的数据只是帧的一部分。AVCODEC_BUFFER_FLAGS_CODEC_DATA = 1 << 3表示缓冲区包含编解码特定数据。AVCODEC_BUFFER_FLAGS_DISCARD = 1 << 4

表示缓冲区被解码依赖，解码之后的数据可丢弃。

**起始版本：** 12

AVCODEC_BUFFER_FLAGS_DISPOSABLE = 1 << 5

表示缓冲区不被参考可直接丢弃。

**起始版本：** 12