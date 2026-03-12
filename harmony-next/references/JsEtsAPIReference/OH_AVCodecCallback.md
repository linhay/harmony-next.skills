# OH_AVCodecCallback

```ets
typedef struct OH_AVCodecCallback {...} OH_AVCodecCallback
```

#### 概述

OH_AVCodec中所有异步回调函数指针的集合。将该结构体的实例注册到OH_AVCodec实例中，并处理回调上报的信息，以保证OH_AVCodec的正常运行。

使用指导请参见[视频编码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/video-encoding)中的“Surface模式步骤-4或Buffer模式步骤-3”。

**起始版本：** 11

**相关模块：**[CodecBase](CodecBase.md)

**所在头文件：**[native_avcodec_base.h](native_avcodec_base.h.md)

#### 汇总

#### 成员变量

名称描述[OH_AVCodecOnError](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__oh_avcodeconerror) onError监控编解码器操作错误。[OH_AVCodecOnStreamChanged](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__oh_avcodeconstreamchanged) onStreamChanged监控编解码器流变化。[OH_AVCodecOnNeedInputBuffer](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__oh_avcodeconneedinputbuffer) onNeedInputBuffer监控编解码器需要输入数据。[OH_AVCodecOnNewOutputBuffer](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__oh_avcodeconnewoutputbuffer) onNewOutputBuffer监控编解码器已生成输出数据。