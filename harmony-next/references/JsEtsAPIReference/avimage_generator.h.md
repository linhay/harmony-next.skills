# avimage_generator.h

#### 概述

定义AVImageGenerator接口。使用其C API从视频资源中获取指定时间点视频帧。

**引用文件：** <multimedia/player_framework/avimage_generator.h>

**库：** libavimage_generator.so

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**相关模块：**[AVImageGenerator](AVImageGenerator.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVImageGenerator](OH_AVImageGenerator.md)OH_AVImageGenerator定义OH_AVImageGenerator类型，用于生成指定时间点视频帧。

#### 函数

名称描述[OH_AVImageGenerator* OH_AVImageGenerator_Create(void)](#ZH-CN_TOPIC_0000002497445932__oh_avimagegenerator_create)创建OH_AVImageGenerator实例，用于生成指定时间点视频帧。[OH_AVErrCode OH_AVImageGenerator_SetFDSource(OH_AVImageGenerator* generator, int32_t fd, int64_t offset, int64_t size)](#ZH-CN_TOPIC_0000002497445932__oh_avimagegenerator_setfdsource)通过媒体文件描述设置数据源。[OH_AVErrCode OH_AVImageGenerator_FetchFrameByTime(OH_AVImageGenerator* generator, int64_t timeUs, OH_AVImageGenerator_QueryOptions options, OH_PixelmapNative** pixelMap)](#ZH-CN_TOPIC_0000002497445932__oh_avimagegenerator_fetchframebytime)

从视频资源中获取指定时间点视频帧。

此函数必须在[OH_AVImageGenerator_SetFDSource](#ZH-CN_TOPIC_0000002497445932__oh_avimagegenerator_setfdsource)之后调用。

[OH_AVErrCode OH_AVImageGenerator_Release(OH_AVImageGenerator* generator)](#ZH-CN_TOPIC_0000002497445932__oh_avimagegenerator_release)释放用于OH_AVImageGenerator的资源以及销毁OH_AVImageGenerator实例。

#### 函数说明

#### OH_AVImageGenerator_Create()

```ets
OH_AVImageGenerator* OH_AVImageGenerator_Create(void)
```

**描述**

创建OH_AVImageGenerator实例，用于生成指定时间点视频帧。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**返回：**

类型说明[OH_AVImageGenerator](OH_AVImageGenerator.md)*

创建成功时返回指向OH_AVImageGenerator实例的指针，否则返回空指针。

 可能的失败原因：HstEngineFactory未能创建AVMetadataHelperEngine。

#### OH_AVImageGenerator_SetFDSource()

```ets
OH_AVErrCode OH_AVImageGenerator_SetFDSource(OH_AVImageGenerator* generator,int32_t fd, int64_t offset, int64_t size)
```

**描述**

通过媒体文件描述设置数据源。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**参数：**

参数项描述[OH_AVImageGenerator](OH_AVImageGenerator.md)* generator指向OH_AVImageGenerator实例的指针。int32_t fd媒体源的文件描述符。int64_t offset媒体源在文件描述符中的偏移量。int64_t size媒体源的大小。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入的generator为空指针或参数无效。

 AV_ERR_OPERATE_NOT_PERMIT：操作被禁止。

 AV_ERR_NO_MEMORY：内部内存分配失败。

#### OH_AVImageGenerator_FetchFrameByTime()

```ets
OH_AVErrCode OH_AVImageGenerator_FetchFrameByTime(OH_AVImageGenerator* generator,int64_t timeUs, OH_AVImageGenerator_QueryOptions options, OH_PixelmapNative** pixelMap)
```

**描述**

从视频资源中获取指定时间点视频帧。

此函数必须在[OH_AVImageGenerator_SetFDSource](#ZH-CN_TOPIC_0000002497445932__oh_avimagegenerator_setfdsource)之后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**参数：**

参数项描述[OH_AVImageGenerator](OH_AVImageGenerator.md)* generator指向OH_AVImageGenerator实例的指针。int64_t timeUs需要获取的视频帧在视频中的时间点，单位为微秒（μs）。[OH_AVImageGenerator_QueryOptions](avimage_generator_base.h.md#ZH-CN_TOPIC_0000002529285903__oh_avimagegenerator_queryoptions) options关于给定时间Us和视频帧之间关系的时间选项。[OH_PixelmapNative](OH_PixelmapNative.md)** pixelMap获取的视频帧对象。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入的generator为空指针或参数无效。

 AV_ERR_OPERATE_NOT_PERMIT：操作被禁止。

 AV_ERR_UNSUPPORTED_FORMAT：格式不支持。

 AV_ERR_NO_MEMORY：内部内存分配失败。

#### OH_AVImageGenerator_Release()

```ets
OH_AVErrCode OH_AVImageGenerator_Release(OH_AVImageGenerator* generator)
```

**描述**

释放用于OH_AVImageGenerator的资源以及销毁OH_AVImageGenerator实例。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 18

**参数：**

参数项描述[OH_AVImageGenerator](OH_AVImageGenerator.md)* generator指向OH_AVImageGenerator实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：输入的generator为空指针或参数无效。