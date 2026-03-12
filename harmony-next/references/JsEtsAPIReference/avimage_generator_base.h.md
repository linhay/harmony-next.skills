# avimage_generator_base.h

#### 概述

定义AVImageGenerator的枚举。

**引用文件：** <multimedia/player_framework/avimage_generator_base.h>

**库：** libavimage_generator.so

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**相关模块：**[AVImageGenerator](AVImageGenerator.md)

#### 汇总

#### 枚举

名称typedef关键字描述[OH_AVImageGenerator_QueryOptions](#ZH-CN_TOPIC_0000002529285903__oh_avimagegenerator_queryoptions)OH_AVImageGenerator_QueryOptions指定时间点与视频帧对应关系的枚举类型。

#### 枚举类型说明

#### OH_AVImageGenerator_QueryOptions

```ets
enum OH_AVImageGenerator_QueryOptions
```

**描述**

指定时间点与视频帧对应关系的枚举类型。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

枚举项描述OH_AVIMAGE_GENERATOR_QUERY_NEXT_SYNC = 0此选项用于选取传入时间点或之后的关键帧。OH_AVIMAGE_GENERATOR_QUERY_PREVIOUS_SYNC = 1此选项用于选取传入时间点或之前的关键帧。OH_AVIMAGE_GENERATOR_QUERY_CLOSEST_SYNC = 2此选项用于选取离传入时间点最近的关键帧。OH_AVIMAGE_GENERATOR_QUERY_CLOSEST = 3此选项用于选取离传入时间点最近的帧，该帧不一定是关键帧。