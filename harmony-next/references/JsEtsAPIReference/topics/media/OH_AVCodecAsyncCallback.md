# OH_AVCodecAsyncCallback

```ets
typedef struct OH_AVCodecAsyncCallback {...} OH_AVCodecAsyncCallback
```

**概述**

OH_AVCodec中所有异步回调函数指针的集合。将该结构体的实例注册到OH_AVCodec实例中，并处理回调上报的信息，以保证OH_AVCodec的正常运行。

起始版本： 9

废弃版本： 11

替代接口： [OH_AVCodecCallback](OH_AVCodecCallback.md)

相关模块： [CodecBase](CodecBase.md)

所在头文件： [native_avcodec_base.h](native_avcodec_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| OH_AVCodecOnError onError | 监控编解码器操作错误。 |
| OH_AVCodecOnStreamChanged onStreamChanged | 监控编解码器流变化。 |
| OH_AVCodecOnNeedInputData onNeedInputData | 监控编解码器需要输入数据。 |
| OH_AVCodecOnNewOutputData onNeedOutputData | 监控编解码器已生成输出数据。 |