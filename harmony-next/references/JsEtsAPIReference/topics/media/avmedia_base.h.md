# avmedia_base.h

**概述**

定义AVMedia的结构体和枚举类型。

引用文件： <multimedia/player_framework/avmedia_base.h>

库： libavmedia_base.so

系统能力： SystemCapability.Multimedia.Media.Core

起始版本： 23

相关模块： [AVMediaBase](AVMediaBase.md)

**汇总**

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_AVMedia_SeekMode | OH_AVMedia_SeekMode | 指定时间点和帧对应关系的枚举类型。 |

**枚举类型说明**

**OH_AVMedia_SeekMode**

```ets
enum OH_AVMedia_SeekMode
```

描述

指定时间点和帧对应关系的枚举类型。

起始版本： 23

| 枚举项 | 描述 |
| --- | --- |
| OH_AVMEDIA_SEEK_NEXT_SYNC = 0 | 表示选取传入时间点或之后的关键帧。 |
| OH_AVMEDIA_SEEK_PREVIOUS_SYNC = 1 | 表示选取传入时间点或之前的关键帧。 |
| OH_AVMEDIA_SEEK_CLOSEST_SYNC = 2 | 表示选取离传入时间点最近的关键帧。 |
| OH_AVMEDIA_SEEK_CLOSEST = 3 | 表示选取离传入时间点最近的帧，该帧不一定是关键帧。 |