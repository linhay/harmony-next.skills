# AVPlayerCallback

```ets
typedef struct AVPlayerCallback {...} AVPlayerCallback
```

**概述**

包含了OH_AVPlayerOnInfo和OH_AVPlayerOnError回调函数指针的集合。应用需注册此实例结构体到OH_AVPlayer实例中，并对回调上报的信息进行处理，保证AVPlayer的正常运行。

起始版本： 11

废弃版本： 12

替代接口： [OH_AVPlayerOnInfoCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002553361969__oh_avplayeroninfocallback) [OH_AVPlayerOnErrorCallback](avplayer_base.h.md#ZH-CN_TOPIC_0000002553361969__oh_avplayeronerrorcallback)

相关模块： [AVPlayer](AVPlayer.md)

所在头文件： [avplayer_base.h](avplayer_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| OH_AVPlayerOnInfo onInfo | 监控AVPlayer过程信息，参考OH_AVPlayerOnInfo。 起始版本： 11 废弃版本： 12 替代接口： OH_AVPlayerOnInfoCallback |
| OH_AVPlayerOnError onError | 监控AVPlayer操作错误，参考OH_AVPlayerOnError。 起始版本： 11 废弃版本： 12 替代接口： OH_AVPlayerOnErrorCallback |