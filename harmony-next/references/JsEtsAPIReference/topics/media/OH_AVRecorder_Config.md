# OH_AVRecorder_Config

```ets
typedef struct OH_AVRecorder_Config {...} OH_AVRecorder_Config
```

**概述**

提供媒体AVRecorder的配置定义。

起始版本： 18

相关模块： [AVRecorder](AVRecorder.md)

所在头文件： [avrecorder_base.h](avrecorder_base.h.md)

**汇总**

**成员变量**

| 名称 | 描述 |
| --- | --- |
| OH_AVRecorder_AudioSourceType audioSourceType | 录制音频源类型。 |
| OH_AVRecorder_VideoSourceType videoSourceType | 录制视频源类型。 |
| OH_AVRecorder_Profile profile | 包含音频和视频编码配置。 |
| char* url | 定义文件URL，格式为fd://xx。 |
| OH_AVRecorder_FileGenerationMode fileGenerationMode | 指定录制输出文件的生成模式。 |
| OH_AVRecorder_Metadata metadata | 包含录制媒体的附加元数据。 |
| int32_t maxDuration | 指定录制的最大时长。 |