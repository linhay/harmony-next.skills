# OH_AVRecorder_Config

```ets
typedef struct OH_AVRecorder_Config {...} OH_AVRecorder_Config
```

#### 概述

提供媒体AVRecorder的配置定义。

**起始版本：** 18

**相关模块：**[AVRecorder](AVRecorder.md)

**所在头文件：**[avrecorder_base.h](../../capi/headers/avrecorder_base.h.md)

#### 汇总

#### 成员变量

名称描述[OH_AVRecorder_AudioSourceType](../../capi/headers/avrecorder_base.h.md#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_audiosourcetype) audioSourceType录制音频源类型。[OH_AVRecorder_VideoSourceType](../../capi/headers/avrecorder_base.h.md#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_videosourcetype) videoSourceType录制视频源类型。[OH_AVRecorder_Profile](OH_AVRecorder_Profile.md) profile包含音频和视频编码配置。char* url定义文件URL，格式为fd://xx。[OH_AVRecorder_FileGenerationMode](../../capi/headers/avrecorder_base.h.md#ZH-CN_TOPIC_0000002497605916__oh_avrecorder_filegenerationmode) fileGenerationMode指定录制输出文件的生成模式。[OH_AVRecorder_Metadata](OH_AVRecorder_Metadata.md) metadata包含录制媒体的附加元数据。int32_t maxDuration指定录制的最大时长。