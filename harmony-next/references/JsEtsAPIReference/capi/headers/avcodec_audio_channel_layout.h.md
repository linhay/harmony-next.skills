# avcodec_audio_channel_layout.h

#### 概述

音频编解码声道布局枚举的声明。

**引用文件：** <multimedia/player_framework/avcodec_audio_channel_layout.h>

**库：** libnative_media_codecbase.so

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**废弃版本：** 11

**相关模块：**[CodecBase](../../topics/misc/CodecBase.md)

#### 汇总

#### 枚举

名称描述[AudioChannelSet](#ZH-CN_TOPIC_0000002529285749__audiochannelset)音频声道数集合，将每一个声道数映射为int64的变量。(API11废弃)[AudioChannelLayout](#ZH-CN_TOPIC_0000002529285749__audiochannellayout)音频声道数类型，将用户申请的解码器输出格式表示为编解码器的声道类型。(API11废弃)

#### 枚举类型说明

#### AudioChannelSet

```ets
enum AudioChannelSet : uint64_t
```

**描述**

音频声道数集合，将每一个声道数映射为int64的变量。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**废弃版本：** 11

**替代接口：**[OH_AudioChannelSet](native_audio_channel_layout.h.md#ZH-CN_TOPIC_0000002497445760__oh_audiochannelset)

枚举项描述FRONT_LEFT = 1ULL << 0U左前声道FRONT_RIGHT = 1ULL << 1U右前声道FRONT_CENTER = 1ULL << 2U中前声道LOW_FREQUENCY = 1ULL << 3U低频声道BACK_LEFT = 1ULL << 4U左后声道BACK_RIGHT = 1ULL << 5U右后声道FRONT_LEFT_OF_CENTER = 1ULL << 6U左前中置声道FRONT_RIGHT_OF_CENTER = 1ULL << 7U右前中置声道BACK_CENTER = 1ULL << 8U后方中置声道SIDE_LEFT = 1ULL << 9U左侧声道SIDE_RIGHT = 1ULL << 10U右侧声道TOP_CENTER = 1ULL << 11U上方中置声道TOP_FRONT_LEFT = 1ULL << 12U上方左前声道TOP_FRONT_CENTER = 1ULL << 13U上方中前声道TOP_FRONT_RIGHT = 1ULL << 14U上方右前声道TOP_BACK_LEFT = 1ULL << 15U上方左后声道TOP_BACK_CENTER = 1ULL << 16U上方中后声道TOP_BACK_RIGHT = 1ULL << 17U上方右后声道STEREO_LEFT = 1ULL << 29U立体声左声道STEREO_RIGHT = 1ULL << 30U立体声右声道WIDE_LEFT = 1ULL << 31U宽左声道WIDE_RIGHT = 1ULL << 32U宽右声道SURROUND_DIRECT_LEFT = 1ULL << 33U左环绕声道SURROUND_DIRECT_RIGHT = 1ULL << 34U右环绕声道LOW_FREQUENCY_2 = 1ULL << 35U低频声道2TOP_SIDE_LEFT = 1ULL << 36U上方左侧声道TOP_SIDE_RIGHT = 1ULL << 37U上方右侧声道BOTTOM_FRONT_CENTER = 1ULL << 38U下方中前声道BOTTOM_FRONT_LEFT = 1ULL << 39U下方左前声道BOTTOM_FRONT_RIGHT = 1ULL << 40U下方右前声道AMBISONICS_ACN0 = 1ULL << 41U零阶立体声声道数0AMBISONICS_ACN1 = 1ULL << 42U一阶立体声声道数1AMBISONICS_ACN2 = 1ULL << 43U一阶立体声声道数2AMBISONICS_ACN3 = 1ULL << 44U一阶立体声声道数3AMBISONICS_W = AMBISONICS_ACN0同于零阶立体声声道数0AMBISONICS_Y = AMBISONICS_ACN1同于一阶立体声声道数1AMBISONICS_Z = AMBISONICS_ACN2同于一阶立体声声道数2AMBISONICS_X = AMBISONICS_ACN3同于一阶立体声声道数3AMBISONICS_ACN4 = 1ULL << 45U二阶立体声声道数4AMBISONICS_ACN5 = 1ULL << 46U二阶立体声声道数5AMBISONICS_ACN6 = 1ULL << 47U二阶立体声声道数6AMBISONICS_ACN7 = 1ULL << 48U二阶立体声声道数7AMBISONICS_ACN8 = 1ULL << 49U二阶立体声声道数8AMBISONICS_ACN9 = 1ULL << 50U三阶立体声声道数9AMBISONICS_ACN10 = 1ULL << 51U三阶立体声声道数10AMBISONICS_ACN11 = 1ULL << 52U三阶立体声声道数11AMBISONICS_ACN12 = 1ULL << 53U三阶立体声声道数12AMBISONICS_ACN13 = 1ULL << 54U三阶立体声声道数13AMBISONICS_ACN14 = 1ULL << 55U三阶立体声声道数14AMBISONICS_ACN15 = 1ULL << 56U三阶立体声声道数15

#### AudioChannelLayout

```ets
enum AudioChannelLayout : uint64_t
```

**描述**

音频声道数类型，将用户申请的解码器输出格式表示为编解码器的声道类型。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**废弃版本：** 11

**替代接口：**[OH_AudioChannelLayout](native_audio_channel_layout.h.md#ZH-CN_TOPIC_0000002497445760__oh_audiochannellayout)

枚举项描述UNKNOWN_CHANNEL_LAYOUT = 0未知通道布局MONO = (AudioChannelSet::FRONT_CENTER)单通道布局STEREO = (AudioChannelSet::FRONT_LEFT | AudioChannelSet::FRONT_RIGHT)立体声布局CH_2POINT1 = (STEREO | AudioChannelSet::LOW_FREQUENCY)2.1布局CH_2_1 = (STEREO | AudioChannelSet::BACK_CENTER)2_1布局SURROUND = (STEREO | AudioChannelSet::FRONT_CENTER)环绕布局CH_3POINT1 = (SURROUND | AudioChannelSet::LOW_FREQUENCY)3.1布局CH_4POINT0 = (SURROUND | AudioChannelSet::BACK_CENTER)4.0布局CH_4POINT1 = (CH_4POINT0 | AudioChannelSet::LOW_FREQUENCY)4.1布局CH_2_2 = (STEREO | AudioChannelSet::SIDE_LEFT | AudioChannelSet::SIDE_RIGHT)2_2布局QUAD = (STEREO | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_RIGHT)四角形布局CH_5POINT0 = (SURROUND | AudioChannelSet::SIDE_LEFT | AudioChannelSet::SIDE_RIGHT)5.0布局CH_5POINT1 = (CH_5POINT0 | AudioChannelSet::LOW_FREQUENCY)5.1布局CH_5POINT0_BACK = (SURROUND | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_RIGHT)5.0后置布局CH_5POINT1_BACK = (CH_5POINT0_BACK | AudioChannelSet::LOW_FREQUENCY)5.1后置布局CH_6POINT0 = (CH_5POINT0 | AudioChannelSet::BACK_CENTER)6.0布局CH_6POINT0_FRONT = (CH_2_2 | AudioChannelSet::FRONT_LEFT_OF_CENTER | AudioChannelSet::FRONT_RIGHT_OF_CENTER)6.0前置布局HEXAGONAL = (CH_5POINT0_BACK | AudioChannelSet::BACK_CENTER)六角形布局CH_6POINT1 = (CH_5POINT1 | AudioChannelSet::BACK_CENTER)6.1布局CH_6POINT1_BACK = (CH_5POINT1_BACK | AudioChannelSet::BACK_CENTER)6.1后置布局CH_6POINT1_FRONT = (CH_6POINT0_FRONT | AudioChannelSet::LOW_FREQUENCY)6.1前置布局CH_7POINT0 = (CH_5POINT0 | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_RIGHT)7.0布局CH_7POINT0_FRONT = (CH_5POINT0 | AudioChannelSet::FRONT_LEFT_OF_CENTER | AudioChannelSet::FRONT_RIGHT_OF_CENTER)7.0前置布局CH_7POINT1 = (CH_5POINT1 | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_RIGHT)7.1布局CH_7POINT1_WIDE = (CH_5POINT1 | AudioChannelSet::FRONT_LEFT_OF_CENTER | AudioChannelSet::FRONT_RIGHT_OF_CENTER)7.1宽布局CH_7POINT1_WIDE_BACK =7.1后置宽布局CH_3POINT1POINT2 = (CH_3POINT1 | AudioChannelSet::TOP_FRONT_LEFT | AudioChannelSet::TOP_FRONT_RIGHT)3.1.2布局CH_5POINT1POINT2 = (CH_5POINT1 | AudioChannelSet::TOP_SIDE_LEFT | AudioChannelSet::TOP_SIDE_RIGHT)5.1.2布局(CH_5POINT1 | AudioChannelSet::TOP_FRONT_LEFT | AudioChannelSet::TOP_FRONT_RIGHT |AudioChannelSet::TOP_BACK_LEFT | AudioChannelSet::TOP_BACK_RIGHT)5.1.4布局CH_7POINT1POINT2 = (CH_7POINT1 | AudioChannelSet::TOP_SIDE_LEFT | AudioChannelSet::TOP_SIDE_RIGHT)7.1.2布局CH_7POINT1POINT4 = (CH_7POINT1 | AudioChannelSet::TOP_FRONT_LEFT | AudioChannelSet::TOP_FRONT_RIGHT | AudioChannelSet::TOP_BACK_LEFT | AudioChannelSet::TOP_BACK_RIGHT)7.1.4布局CH_9POINT1POINT4 = (CH_7POINT1POINT4 | AudioChannelSet::WIDE_LEFT | AudioChannelSet::WIDE_RIGHT)9.1.4布局CH_9POINT1POINT6 = (CH_9POINT1POINT4 | AudioChannelSet::TOP_SIDE_LEFT | AudioChannelSet::TOP_SIDE_RIGHT)9.1.6布局CH_10POINT2 = (AudioChannelSet::FRONT_LEFT | AudioChannelSet::FRONT_RIGHT | AudioChannelSet::FRONT_CENTER | AudioChannelSet::TOP_FRONT_LEFT | AudioChannelSet::TOP_FRONT_RIGHT | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_RIGHT | AudioChannelSet::BACK_CENTER | AudioChannelSet::SIDE_LEFT | AudioChannelSet::SIDE_RIGHT | AudioChannelSet::WIDE_LEFT | AudioChannelSet::WIDE_RIGHT)10.2布局CH_22POINT2 = (CH_7POINT1POINT4 | AudioChannelSet::FRONT_LEFT_OF_CENTER | AudioChannelSet::FRONT_RIGHT_OF_CENTER | AudioChannelSet::BACK_CENTER | AudioChannelSet::TOP_CENTER | AudioChannelSet::TOP_FRONT_CENTER | AudioChannelSet::TOP_BACK_CENTER | AudioChannelSet::TOP_SIDE_LEFT | AudioChannelSet::TOP_SIDE_RIGHT | AudioChannelSet::BOTTOM_FRONT_LEFT | AudioChannelSet::BOTTOM_FRONT_RIGHT | AudioChannelSet::BOTTOM_FRONT_CENTER | AudioChannelSet::LOW_FREQUENCY_2)22.2布局OCTAGONAL = (CH_5POINT0 | AudioChannelSet::BACK_LEFT | AudioChannelSet::BACK_CENTER | AudioChannelSet::BACK_RIGHT)八边形布局HEXADECAGONAL = (OCTAGONAL | AudioChannelSet::WIDE_LEFT | AudioChannelSet::WIDE_RIGHT | AudioChannelSet::TOP_BACK_LEFT | AudioChannelSet::TOP_BACK_RIGHT | AudioChannelSet::TOP_BACK_CENTER | AudioChannelSet::TOP_FRONT_CENTER | AudioChannelSet::TOP_FRONT_LEFT | AudioChannelSet::TOP_FRONT_RIGHT)六边形布局STEREO_DOWNMIX = (AudioChannelSet::STEREO_LEFT | AudioChannelSet::STEREO_RIGHT)立体声下混布局HOA_FIRST = AudioChannelSet::AMBISONICS_ACN0 | AudioChannelSet::AMBISONICS_ACN1 | AudioChannelSet::AMBISONICS_ACN2 | AudioChannelSet::AMBISONICS_ACN3高阶立体声一阶布局HOA_SECOND = HOA_FIRST | AudioChannelSet::AMBISONICS_ACN4 | AudioChannelSet::AMBISONICS_ACN5 | AudioChannelSet::AMBISONICS_ACN6 | AudioChannelSet::AMBISONICS_ACN7 | AudioChannelSet::AMBISONICS_ACN8高阶立体声二阶布局HOA_THIRD = HOA_SECOND | AudioChannelSet::AMBISONICS_ACN9 | AudioChannelSet::AMBISONICS_ACN10 | AudioChannelSet::AMBISONICS_ACN11 | AudioChannelSet::AMBISONICS_ACN12 | AudioChannelSet::AMBISONICS_ACN13 | AudioChannelSet::AMBISONICS_ACN14 | AudioChannelSet::AMBISONICS_ACN15高阶立体声三阶布局