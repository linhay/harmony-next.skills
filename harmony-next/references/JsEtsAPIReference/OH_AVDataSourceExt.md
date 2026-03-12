# OH_AVDataSourceExt

```ets
typedef struct OH_AVDataSourceExt {...} OH_AVDataSourceExt
```

#### 概述

用户自定义数据源，回调支持通过userData传递用户自定义数据。

**起始版本：** 20

**相关模块：**[CodecBase](CodecBase.md)

**所在头文件：**[native_avcodec_base.h](native_avcodec_base.h.md)

#### 汇总

#### 成员变量

名称描述int64_t size数据源的总大小。[OH_AVDataSourceReadAtExt](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__oh_avdatasourcereadatext) readAt数据源的数据回调。