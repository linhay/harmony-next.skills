# avcodec_audio_channel_layout.h

**概述**

音频编解码声道布局枚举的声明。

引用文件： <multimedia/player_framework/avcodec_audio_channel_layout.h>

库： libnative_media_codecbase.so

系统能力： SystemCapability.Multimedia.Media.CodecBase

起始版本： 10

废弃版本： 11

相关模块： [CodecBase](CodecBase.md)

**汇总**

**枚举**

| 名称 | 描述 |
| --- | --- |
| AudioChannelSet | 音频声道数集合，将每一个声道数映射为int64的变量。(API11废弃) |
| AudioChannelLayout | 音频声道数类型，将用户申请的解码器输出格式表示为编解码器的声道类型。(API11废弃) |

**枚举类型说明**

**AudioChannelSet**

```ets
enum AudioChannelSet : uint64_t
```

描述

音频声道数集合，将每一个声道数映射为int64的变量。

系统能力： SystemCapability.Multimedia.Media.CodecBase

起始版本： 10

废弃版本： 11

替代接口： [OH_AudioChannelSet](native_audio_channel_layout.h.md#ZH-CN_TOPIC_0000002553361781__oh_audiochannelset)

| 枚举项 | 描述 |
| --- | --- |
| FRONT_LEFT = 1ULL << 0U | 左前声道 |
| FRONT_RIGHT = 1ULL << 1U | 右前声道 |
| FRONT_CENTER = 1ULL << 2U | 中前声道 |
| LOW_FREQUENCY = 1ULL << 3U | 低频声道 |
| BACK_LEFT = 1ULL << 4U | 左后声道 |
| BACK_RIGHT = 1ULL << 5U | 右后声道 |
| FRONT_LEFT_OF_CENTER = 1ULL << 6U | 左前中置声道 |
| FRONT_RIGHT_OF_CENTER = 1ULL << 7U | 右前中置声道 |
| BACK_CENTER = 1ULL << 8U | 后方中置声道 |
| SIDE_LEFT = 1ULL << 9U | 左侧声道 |
| SIDE_RIGHT = 1ULL << 10U | 右侧声道 |
| TOP_CENTER = 1ULL << 11U | 上方中置声道 |
| TOP_FRONT_LEFT = 1ULL << 12U | 上方左前声道 |
| TOP_FRONT_CENTER = 1ULL << 13U | 上方中前声道 |
| TOP_FRONT_RIGHT = 1ULL << 14U | 上方右前声道 |
| TOP_BACK_LEFT = 1ULL << 15U | 上方左后声道 |
| TOP_BACK_CENTER = 1ULL << 16U | 上方中后声道 |
| TOP_BACK_RIGHT = 1ULL << 17U | 上方右后声道 |
| STEREO_LEFT = 1ULL << 29U | 立体声左声道 |
| STEREO_RIGHT = 1ULL << 30U | 立体声右声道 |
| WIDE_LEFT = 1ULL << 31U | 宽左声道 |
| WIDE_RIGHT = 1ULL << 32U | 宽右声道 |
| SURROUND_DIRECT_LEFT = 1ULL << 33U | 左环绕声道 |
| SURROUND_DIRECT_RIGHT = 1ULL << 34U | 右环绕声道 |
| LOW_FREQUENCY_2 = 1ULL << 35U | 低频声道2 |
| TOP_SIDE_LEFT = 1ULL << 36U | 上方左侧声道 |
| TOP_SIDE_RIGHT = 1ULL << 37U | 上方右侧声道 |
| BOTTOM_FRONT_CENTER = 1ULL << 38U | 下方中前声道 |
| BOTTOM_FRONT_LEFT = 1ULL << 39U | 下方左前声道 |
| BOTTOM_FRONT_RIGHT = 1ULL << 40U | 下方右前声道 |
| AMBISONICS_ACN0 = 1ULL << 41U | 零阶立体声声道数0 |
| AMBISONICS_ACN1 = 1ULL << 42U | 一阶立体声声道数1 |
| AMBISONICS_ACN2 = 1ULL << 43U | 一阶立体声声道数2 |
| AMBISONICS_ACN3 = 1ULL << 44U | 一阶立体声声道数3 |
| AMBISONICS_W = AMBISONICS_ACN0 | 同于零阶立体声声道数0 |
| AMBISONICS_Y = AMBISONICS_ACN1 | 同于一阶立体声声道数1 |
| AMBISONICS_Z = AMBISONICS_ACN2 | 同于一阶立体声声道数2 |
| AMBISONICS_X = AMBISONICS_ACN3 | 同于一阶立体声声道数3 |
| AMBISONICS_ACN4 = 1ULL << 45U | 二阶立体声声道数4 |
| AMBISONICS_ACN5 = 1ULL << 46U | 二阶立体声声道数5 |
| AMBISONICS_ACN6 = 1ULL << 47U | 二阶立体声声道数6 |
| AMBISONICS_ACN7 = 1ULL << 48U | 二阶立体声声道数7 |
| AMBISONICS_ACN8 = 1ULL << 49U | 二阶立体声声道数8 |
| AMBISONICS_ACN9 = 1ULL << 50U | 三阶立体声声道数9 |
| AMBISONICS_ACN10 = 1ULL << 51U | 三阶立体声声道数10 |
| AMBISONICS_ACN11 = 1ULL << 52U | 三阶立体声声道数11 |
| AMBISONICS_ACN12 = 1ULL << 53U | 三阶立体声声道数12 |
| AMBISONICS_ACN13 = 1ULL << 54U | 三阶立体声声道数13 |
| AMBISONICS_ACN14 = 1ULL << 55U | 三阶立体声声道数14 |
| AMBISONICS_ACN15 = 1ULL << 56U | 三阶立体声声道数15 |

**AudioChannelLayout**

```ets
enum AudioChannelLayout : uint64_t
```

描述

音频声道数类型，将用户申请的解码器输出格式表示为编解码器的声道类型。

系统能力： SystemCapability.Multimedia.Media.CodecBase

起始版本： 10

废弃版本： 11

替代接口： [OH_AudioChannelLayout](native_audio_channel_layout.h.md#ZH-CN_TOPIC_0000002553361781__oh_audiochannellayout)

| 枚举项 | 描述 |
| --- | --- |
| UNKNOWN_CHANNEL_LAYOUT = 0 | 未知通道布局 |
| MONO = (AudioChannelSet::FRONT_CENTER) | 单通道布局 |
| STEREO = (AudioChannelSet::FRONT_LEFT | AudioChannelSet::FRONT_RIGHT) | 立体声布局 |
| CH_2POINT1 = (STEREO | AudioChannelSet::LOW_FREQUENCY) | 2.1布局 |
| CH_2_1 = (STEREO | AudioChannelSet::BACK_CENTER) | 2_1布局 |
| SURROUND = (STEREO | AudioChannelSet::FRONT_CENTER) | 环绕布局 |
| CH_3POINT1 = (SURROUND | AudioChannelSet::LOW_FREQUENCY) | 3.1布局 |
| CH_4POINT0 = (SURROUND | AudioChannelSet::BACK_CENTER) | 4.0布局 |
| CH_4POINT1 = (CH_4POINT0 | AudioChannelSet::LOW_FREQUENCY) | 4.1布局 |
| CH_2_2 = (STEREO | AudioChannelSet::SIDE_LEFT | AudioChannelSet::SIDE_RIGHT) | 2_2布局 |
| QUAD = (STEREO | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_RIGHT) | 四角形布局 |
| CH_5POINT0 = (SURROUND | AudioChannelSet::SIDE_LEFT | AudioChannelSet::SIDE_RIGHT) | 5.0布局 |
| CH_5POINT1 = (CH_5POINT0 | AudioChannelSet::LOW_FREQUENCY) | 5.1布局 |
| CH_5POINT0_BACK = (SURROUND | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_RIGHT) | 5.0后置布局 |
| CH_5POINT1_BACK = (CH_5POINT0_BACK | AudioChannelSet::LOW_FREQUENCY) | 5.1后置布局 |
| CH_6POINT0 = (CH_5POINT0 | AudioChannelSet::BACK_CENTER) | 6.0布局 |
| CH_6POINT0_FRONT = (CH_2_2 | AudioChannelSet::FRONT_LEFT_OF_CENTER | AudioChannelSet::FRONT_RIGHT_OF_CENTER) | 6.0前置布局 |
| HEXAGONAL = (CH_5POINT0_BACK | AudioChannelSet::BACK_CENTER) | 六角形布局 |
| CH_6POINT1 = (CH_5POINT1 | AudioChannelSet::BACK_CENTER) | 6.1布局 |
| CH_6POINT1_BACK = (CH_5POINT1_BACK | AudioChannelSet::BACK_CENTER) | 6.1后置布局 |
| CH_6POINT1_FRONT = (CH_6POINT0_FRONT | AudioChannelSet::LOW_FREQUENCY) | 6.1前置布局 |
| CH_7POINT0 = (CH_5POINT0 | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_RIGHT) | 7.0布局 |
| CH_7POINT0_FRONT = (CH_5POINT0 | AudioChannelSet::FRONT_LEFT_OF_CENTER | AudioChannelSet::FRONT_RIGHT_OF_CENTER) | 7.0前置布局 |
| CH_7POINT1 = (CH_5POINT1 | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_RIGHT) | 7.1布局 |
| CH_7POINT1_WIDE = (CH_5POINT1 | AudioChannelSet::FRONT_LEFT_OF_CENTER | AudioChannelSet::FRONT_RIGHT_OF_CENTER) | 7.1宽布局 |
| CH_7POINT1_WIDE_BACK = | 7.1后置宽布局 |
| CH_3POINT1POINT2 = (CH_3POINT1 | AudioChannelSet::TOP_FRONT_LEFT | AudioChannelSet::TOP_FRONT_RIGHT) | 3.1.2布局 |
| CH_5POINT1POINT2 = (CH_5POINT1 | AudioChannelSet::TOP_SIDE_LEFT | AudioChannelSet::TOP_SIDE_RIGHT) | 5.1.2布局 |
| (CH_5POINT1 | AudioChannelSet::TOP_FRONT_LEFT | AudioChannelSet::TOP_FRONT_RIGHT |AudioChannelSet::TOP_BACK_LEFT | AudioChannelSet::TOP_BACK_RIGHT) | 5.1.4布局 |
| CH_7POINT1POINT2 = (CH_7POINT1 | AudioChannelSet::TOP_SIDE_LEFT | AudioChannelSet::TOP_SIDE_RIGHT) | 7.1.2布局 |
| CH_7POINT1POINT4 = (CH_7POINT1 | AudioChannelSet::TOP_FRONT_LEFT | AudioChannelSet::TOP_FRONT_RIGHT | AudioChannelSet::TOP_BACK_LEFT | AudioChannelSet::TOP_BACK_RIGHT) | 7.1.4布局 |
| CH_9POINT1POINT4 = (CH_7POINT1POINT4 | AudioChannelSet::WIDE_LEFT | AudioChannelSet::WIDE_RIGHT) | 9.1.4布局 |
| CH_9POINT1POINT6 = (CH_9POINT1POINT4 | AudioChannelSet::TOP_SIDE_LEFT | AudioChannelSet::TOP_SIDE_RIGHT) | 9.1.6布局 |
| CH_10POINT2 = (AudioChannelSet::FRONT_LEFT | AudioChannelSet::FRONT_RIGHT | AudioChannelSet::FRONT_CENTER | AudioChannelSet::TOP_FRONT_LEFT | AudioChannelSet::TOP_FRONT_RIGHT | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_RIGHT | AudioChannelSet::BACK_CENTER | AudioChannelSet::SIDE_LEFT | AudioChannelSet::SIDE_RIGHT | AudioChannelSet::WIDE_LEFT | AudioChannelSet::WIDE_RIGHT) | 10.2布局 |
| CH_22POINT2 = (CH_7POINT1POINT4 | AudioChannelSet::FRONT_LEFT_OF_CENTER | AudioChannelSet::FRONT_RIGHT_OF_CENTER | AudioChannelSet::BACK_CENTER | AudioChannelSet::TOP_CENTER | AudioChannelSet::TOP_FRONT_CENTER | AudioChannelSet::TOP_BACK_CENTER | AudioChannelSet::TOP_SIDE_LEFT | AudioChannelSet::TOP_SIDE_RIGHT | AudioChannelSet::BOTTOM_FRONT_LEFT | AudioChannelSet::BOTTOM_FRONT_RIGHT | AudioChannelSet::BOTTOM_FRONT_CENTER | AudioChannelSet::LOW_FREQUENCY_2) | 22.2布局 |
| OCTAGONAL = (CH_5POINT0 | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_CENTER | AudioChannelSet::BACK_RIGHT) | 八边形布局 |
| HEXADECAGONAL = (OCTAGONAL | AudioChannelSet::WIDE_LEFT | AudioChannelSet::WIDE_RIGHT | AudioChannelSet::TOP_BACK_LEFT | AudioChannelSet::TOP_BACK_RIGHT | AudioChannelSet::TOP_BACK_CENTER | AudioChannelSet::TOP_FRONT_CENTER | AudioChannelSet::TOP_FRONT_LEFT | AudioChannelSet::TOP_FRONT_RIGHT) | 六边形布局 |
| STEREO_DOWNMIX = (AudioChannelSet::STEREO_LEFT | AudioChannelSet::STEREO_RIGHT) | 立体声下混布局 |
| HOA_FIRST = AudioChannelSet::AMBISONICS_ACN0 | AudioChannelSet::AMBISONICS_ACN1 | AudioChannelSet::AMBISONICS_ACN2 | AudioChannelSet::AMBISONICS_ACN3 | 高阶立体声一阶布局 |
| HOA_SECOND = HOA_FIRST | AudioChannelSet::AMBISONICS_ACN4 | AudioChannelSet::AMBISONICS_ACN5 | AudioChannelSet::AMBISONICS_ACN6 | AudioChannelSet::AMBISONICS_ACN7 | AudioChannelSet::AMBISONICS_ACN8 | 高阶立体声二阶布局 |
| HOA_THIRD = HOA_SECOND | AudioChannelSet::AMBISONICS_ACN9 | AudioChannelSet::AMBISONICS_ACN10 | AudioChannelSet::AMBISONICS_ACN11 | AudioChannelSet::AMBISONICS_ACN12 | AudioChannelSet::AMBISONICS_ACN13 | AudioChannelSet::AMBISONICS_ACN14 | AudioChannelSet::AMBISONICS_ACN15 | 高阶立体声三阶布局 |