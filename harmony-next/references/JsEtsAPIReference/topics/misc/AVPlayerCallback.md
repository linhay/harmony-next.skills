# AVPlayerCallback

```ets
typedef struct AVPlayerCallback {...} AVPlayerCallback
```

#### 概述

包含了OH_AVPlayerOnInfo和OH_AVPlayerOnError回调函数指针的集合。应用需注册此实例结构体到OH_AVPlayer实例中，并对回调上报的信息进行处理，保证AVPlayer的正常运行。

**起始版本：** 11

**废弃版本：** 12

**替代接口：**[OH_AVPlayerOnInfoCallback](../../capi/headers/avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeroninfocallback)[OH_AVPlayerOnErrorCallback](../../capi/headers/avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeronerrorcallback)

**相关模块：**[AVPlayer](AVPlayer.md)

**所在头文件：**[avplayer_base.h](../../capi/headers/avplayer_base.h.md)

#### 汇总

#### 成员变量

名称描述OH_AVPlayerOnInfo onInfo

监控AVPlayer过程信息，参考[OH_AVPlayerOnInfo](../../capi/headers/avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeroninfo)。

**起始版本：** 11

**废弃版本：** 12

**替代接口：**[OH_AVPlayerOnInfoCallback](../../capi/headers/avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeroninfocallback)

OH_AVPlayerOnError onError

监控AVPlayer操作错误，参考[OH_AVPlayerOnError](../../capi/headers/avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeronerror)。

**起始版本：** 11

**废弃版本：** 12

**替代接口：**[OH_AVPlayerOnErrorCallback](../../capi/headers/avplayer_base.h.md#ZH-CN_TOPIC_0000002529285905__oh_avplayeronerrorcallback)