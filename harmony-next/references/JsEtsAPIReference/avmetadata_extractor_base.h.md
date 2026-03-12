# avmetadata_extractor_base.h

#### 概述

定义AVMetadataExtractor常量。

**引用文件：** <multimedia/player_framework/avmetadata_extractor_base.h>

**库：** libavmetadata_extractor.so

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**相关模块：**[AVMetadataExtractor](AVMetadataExtractor.md)

#### 汇总

#### 变量

名称描述static const char* OH_AVMETADATA_EXTRACTOR_ALBUM = "album"

获取专辑标题的关键字，对应值类型为const char*。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_ALBUM_ARTIST = "albumArtist"

获取专辑艺术家的关键字，对应值类型为const char*。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_ARTIST = "artist"

获取媒体资源艺术家的关键字，对应值类型为const char*。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_AUTHOR = "author"

获取媒体资源作者的关键字，对应值类型为const char*。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_DATE_TIME = "dateTime"

获取媒体资源创建时间的关键字，对应值类型为const char*。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_DATE_TIME_FORMAT = "dateTimeFormat"

获取媒体资源创建时间的关键字，对应值类型为const char*，按YYYY-MM-DD HH:mm:ss格式输出。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_COMPOSER = "composer"

获取媒体资源作曲家的关键字，对应值类型为const char*。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_DURATION = "duration"

获取媒体资源时长的关键字，对应值类型为int64_t，单位为毫秒（ms）。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_GENRE = "genre"

获取媒体资源类型或体裁的关键字，对应值类型为const char*。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_HAS_AUDIO = "hasAudio"

获取媒体资源是否包含音频的关键字，对应值类型为int32_t。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_HAS_VIDEO = "hasVideo"

获取媒体资源是否包含视频的关键字，对应值类型为int32_t。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_MIME_TYPE = "mimeType"

获取媒体资源mime类型的关键字，对应值类型为const char*，例如：“video/mp4”、“audio/mp4”和“audio/amr wb”。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_TRACK_COUNT = "trackCount"

获取媒体资源轨道数量的关键字，对应值类型为int32_t。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_SAMPLE_RATE = "sampleRate"

获取音频采样率的关键字，对应值类型为int32_t，单位为赫兹（Hz）。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_TITLE = "title"

获取媒体资源标题的关键字，对应值类型为const char*。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_VIDEO_HEIGHT = "videoHeight"

获取视频高度的关键字，对应值类型为int32_t，单位为像素。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_VIDEO_WIDTH = "videoWidth"

获取视频宽度的关键字，对应值类型为int32_t，单位为像素。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_VIDEO_ORIENTATION = "videoOrientation"

获取视频旋转方向的关键字，对应值类型为int32_t，单位为度（°）。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_VIDEO_IS_HDR_VIVID = "hdrType"

获取是否是HDR Vivid视频的关键字，对应值类型为int32_t。

详情请参阅media_types.h中的[OH_Core_HdrType](media_types.h.md#ZH-CN_TOPIC_0000002497605738__oh_core_hdrtype)。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_LOCATION_LATITUDE = "latitude"

获取地理位置中的纬度值的关键字，对应值类型为float。

**起始版本：** 18

static const char* OH_AVMETADATA_EXTRACTOR_LOCATION_LONGITUDE = "longitude"

获取地理位置中的经度值的关键字，对应值类型为float。

**起始版本：** 18