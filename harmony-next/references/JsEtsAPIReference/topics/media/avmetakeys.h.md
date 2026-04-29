# avmetakeys.h

**概述**

定义音视频元数据键。

引用文件： <multimedia/player_framework/avmetakeys.h>

库： libavmedia_base.so

系统能力： SystemCapability.Multimedia.Media.Core

起始版本： 23

相关模块： [AVMediaBase](AVMediaBase.md)

**汇总**

**变量**

| 名称 | 描述 |
| --- | --- |
| const char * OH_AVMETA_KEY_TRACK_INDEX | 轨道索引，值类型为int32_t。 起始版本： 23 系统能力： SystemCapability.Multimedia.Media.Core |
| const char * OH_AVMETA_KEY_TRACK_TYPE | 轨道类型，值类型为int32_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_MIME_TYPE | 编解码器MIME类型，值类型为字符串（string）。 起始版本： 23 |
| const char * OH_AVMETA_KEY_DURATION | 媒体时长（单位：微秒），值类型为int64_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_BITRATE | 比特率（单位：bps），值类型为int64_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_FRAME_RATE | 视频帧率（每100秒的帧数），值类型为double。 起始版本： 23 |
| const char * OH_AVMETA_KEY_WIDTH | 视频宽度，值类型为int32_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_HEIGHT | 视频高度，值类型为int32_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_CHANNEL_COUNT | 音频声道数，值类型为int32_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_SAMPLE_RATE | 音频采样率（Hz），值类型为int32_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_SAMPLE_DEPTH | 音频采样位深（bit depth），值类型为int32_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_LANGUAGE | 语言标识，值类型为字符串（string）。 起始版本： 23 |
| const char * OH_AVMETA_KEY_TRACK_NAME | 轨道名称，值类型为字符串（string）。 起始版本： 23 |
| const char * OH_AVMETA_KEY_HDR_TYPE | HDR类型，值类型为int32_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_ORIGINAL_WIDTH | 原始视频宽度，值类型为int32_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_ORIGINAL_HEIGHT | 原始视频高度，值类型为int32_t。 起始版本： 23 |
| const char * OH_AVMETA_KEY_REF_TRACK_IDS | 被引用的轨道ID列表，仅用于元数据提取器。 起始版本： 23 |
| const char * OH_AVMETA_KEY_TRACK_REF_TYPE | 轨道引用类型，仅用于元数据提取器。 起始版本： 23 |