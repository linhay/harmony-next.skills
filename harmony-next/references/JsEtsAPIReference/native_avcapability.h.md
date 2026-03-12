# native_avcapability.h

#### 概述

声明用于编解码能力查询到的Native API。

**引用文件：** <multimedia/player_framework/native_avcapability.h>

**库：** libnative_media_codecbase.so

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**相关模块：**[AVCapability](AVCapability.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVRange](OH_AVRange.md)OH_AVRange范围包含最小值和最大值。[OH_AVCapability](OH_AVCapability.md)OH_AVCapability为OH_AVCapability接口定义native层对象。

#### 枚举

名称typedef关键字描述[OH_AVCodecCategory](#ZH-CN_TOPIC_0000002497445758__oh_avcodeccategory)OH_AVCodecCategory编解码器类别。[OH_AVCapabilityFeature](#ZH-CN_TOPIC_0000002497445758__oh_avcapabilityfeature)OH_AVCapabilityFeature可以在特定编解码器场景中使用的可选特性。

#### 函数

名称描述[OH_AVCapability *OH_AVCodec_GetCapability(const char *mime, bool isEncoder)](#ZH-CN_TOPIC_0000002497445758__oh_avcodec_getcapability)获取系统推荐的编解码器能力。[OH_AVCapability *OH_AVCodec_GetCapabilityByCategory(const char *mime, bool isEncoder, OH_AVCodecCategory category)](#ZH-CN_TOPIC_0000002497445758__oh_avcodec_getcapabilitybycategory)获取指定类别中的编解码器能力。通过指定类别，匹配的编解码器仅限于硬件编解码器或软件编解码器。[bool OH_AVCapability_IsHardware(OH_AVCapability *capability)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_ishardware)检查能力实例是否描述了硬件编解码器。[const char *OH_AVCapability_GetName(OH_AVCapability *capability)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getname)获取编解码器名称。[int32_t OH_AVCapability_GetMaxSupportedInstances(OH_AVCapability *capability)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getmaxsupportedinstances)获取编解码器支持的最大实例数。[OH_AVErrCode OH_AVCapability_GetEncoderBitrateRange(OH_AVCapability *capability, OH_AVRange *bitrateRange)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getencoderbitraterange)获取编码器支持的比特率范围。[bool OH_AVCapability_IsEncoderBitrateModeSupported(OH_AVCapability *capability, OH_BitrateMode bitrateMode)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_isencoderbitratemodesupported)检查编码器是否支持特定的比特率模式。[OH_AVErrCode OH_AVCapability_GetEncoderQualityRange(OH_AVCapability *capability, OH_AVRange *qualityRange)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getencoderqualityrange)获取编码器支持的质量范围。[OH_AVErrCode OH_AVCapability_GetEncoderComplexityRange(OH_AVCapability *capability, OH_AVRange *complexityRange)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getencodercomplexityrange)获取编码器支持的编码器复杂性范围。[OH_AVErrCode OH_AVCapability_GetAudioSupportedSampleRates(OH_AVCapability *capability, const int32_t **sampleRates, uint32_t *sampleRateNum)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getaudiosupportedsamplerates)获取音频编解码器支持的采样率。[OH_AVErrCode OH_AVCapability_GetAudioSupportedSampleRateRanges(OH_AVCapability *capability, OH_AVRange **sampleRateRanges, uint32_t *rangesNum)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getaudiosupportedsamplerateranges)获取音频编解码器支持的采样率范围。[OH_AVErrCode OH_AVCapability_GetAudioChannelCountRange(OH_AVCapability *capability, OH_AVRange *channelCountRange)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getaudiochannelcountrange)获取音频编解码器支持的音频通道计数范围。[OH_AVErrCode OH_AVCapability_GetVideoWidthAlignment(OH_AVCapability *capability, int32_t *widthAlignment)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideowidthalignment)获取视频编解码器支持的视频宽度对齐。[OH_AVErrCode OH_AVCapability_GetVideoHeightAlignment(OH_AVCapability *capability, int32_t *heightAlignment)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideoheightalignment)获取视频编解码器支持的视频高度对齐。[OH_AVErrCode OH_AVCapability_GetVideoWidthRangeForHeight(OH_AVCapability *capability, int32_t height, OH_AVRange *widthRange)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideowidthrangeforheight)获取指定高度情况下视频编解码器支持的视频宽度范围。[OH_AVErrCode OH_AVCapability_GetVideoHeightRangeForWidth(OH_AVCapability *capability, int32_t width, OH_AVRange *heightRange)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideoheightrangeforwidth)获取指定宽度情况下视频编解码器支持的视频高度范围。[OH_AVErrCode OH_AVCapability_GetVideoWidthRange(OH_AVCapability *capability, OH_AVRange *widthRange)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideowidthrange)获取视频编解码器支持的视频宽度范围。[OH_AVErrCode OH_AVCapability_GetVideoHeightRange(OH_AVCapability *capability, OH_AVRange *heightRange)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideoheightrange)获取视频编解码器支持的视频高度范围。[bool OH_AVCapability_IsVideoSizeSupported(OH_AVCapability *capability, int32_t width, int32_t height)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_isvideosizesupported)检查视频编解码器是否支持特定的视频大小。[OH_AVErrCode OH_AVCapability_GetVideoFrameRateRange(OH_AVCapability *capability, OH_AVRange *frameRateRange)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideoframeraterange)获取视频编解码器支持的视频帧率范围。[OH_AVErrCode OH_AVCapability_GetVideoFrameRateRangeForSize(OH_AVCapability *capability, int32_t width, int32_t height, OH_AVRange *frameRateRange)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideoframeraterangeforsize)获取指定视频大小的视频编解码器支持的视频帧率范围。[bool OH_AVCapability_AreVideoSizeAndFrameRateSupported(OH_AVCapability *capability, int32_t width, int32_t height, int32_t frameRate)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_arevideosizeandframeratesupported)检查视频编解码器是否支持视频大小和帧率的特定组合。[OH_AVErrCode OH_AVCapability_GetVideoSupportedPixelFormats(OH_AVCapability *capability, const int32_t **pixelFormats, uint32_t *pixelFormatNum)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideosupportedpixelformats)获取视频编解码器支持的视频像素格式。[OH_AVErrCode OH_AVCapability_GetVideoSupportedNativeBufferFormats(OH_AVCapability *capability, const OH_NativeBuffer_Format **nativeBufferFormats, uint32_t *nativeBufferFormatNum)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideosupportednativebufferformats)获取视频编解码器支持的OH_NativeBuffer格式。该函数提供了视频编解码器能够处理的OH_NativeBuffer格式信息，具体取值可见OH_NativeBuffer_Format。[OH_AVErrCode OH_AVCapability_GetSupportedProfiles(OH_AVCapability *capability, const int32_t **profiles, uint32_t *profileNum)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getsupportedprofiles)获取编解码器支持的档次。[OH_AVErrCode OH_AVCapability_GetSupportedLevelsForProfile(OH_AVCapability *capability, int32_t profile, const int32_t **levels, uint32_t *levelNum)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getsupportedlevelsforprofile)获取特定档次支持的编解码器级别。[bool OH_AVCapability_AreProfileAndLevelSupported(OH_AVCapability *capability, int32_t profile, int32_t level)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_areprofileandlevelsupported)检查编解码器是否支持档次和级别的特定组合。[bool OH_AVCapability_IsFeatureSupported(OH_AVCapability *capability, OH_AVCapabilityFeature feature)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_isfeaturesupported)检查编解码器是否支持指定特性。[OH_AVFormat *OH_AVCapability_GetFeatureProperties(OH_AVCapability *capability, OH_AVCapabilityFeature feature)](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getfeatureproperties)获取指定特性的属性。需要注意的是，返回值指向的OH_AVFormat实例的生命周期需要调用者手动释放。

#### 枚举类型说明

#### OH_AVCodecCategory

```ets
enum OH_AVCodecCategory
```

**描述**

编解码器类别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

枚举项描述HARDWARE = 0硬件编解码。SOFTWARE软件编解码。

#### OH_AVCapabilityFeature

```ets
enum OH_AVCapabilityFeature
```

**描述**

可以在特定编解码器场景中使用的可选特性。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 12

枚举项描述VIDEO_ENCODER_TEMPORAL_SCALABILITY = 0编解码器支持时域可分层特性，只用于视频编码场景。VIDEO_ENCODER_LONG_TERM_REFERENCE = 1编解码器支持长期参考帧特性，只用于视频编码场景。VIDEO_LOW_LATENCY = 2编解码器支持低时延特性，只用于视频解码场景。VIDEO_ENCODER_B_FRAME = 7

编解码器支持B帧特性，只用于视频编码场景。

**起始版本：** 20

#### 函数说明

#### OH_AVCodec_GetCapability()

```ets
OH_AVCapability *OH_AVCodec_GetCapability(const char *mime, bool isEncoder)
```

**描述**

获取系统推荐的编解码器能力。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述const char *mimeMIME类型描述字符串，请参阅[AVCODEC_MIME_TYPE](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。bool isEncoder编码器为true，解码器为false。

**返回：**

类型说明[OH_AVCapability](OH_AVCapability.md) *如果现有编解码器匹配，则返回能力实例，如果指定的MIME类型与任何现有编解码器不匹配，则返回NULL。

#### OH_AVCodec_GetCapabilityByCategory()

```ets
OH_AVCapability *OH_AVCodec_GetCapabilityByCategory(const char *mime, bool isEncoder, OH_AVCodecCategory category)
```

**描述**

获取指定类别中的编解码器能力。通过指定类别，匹配的编解码器仅限于硬件编解码器或软件编解码器。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述const char *mimeMIME类型描述字符串，请参阅[AVCODEC_MIME_TYPE](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。bool isEncoder编码器为true，解码器为false。[OH_AVCodecCategory](#ZH-CN_TOPIC_0000002497445758__oh_avcodeccategory) category编解码器类别。

**返回：**

类型说明[OH_AVCapability](OH_AVCapability.md) *如果现有编解码器匹配，则返回能力实例，如果指定的MIME类型与任何现有编解码器不匹配，则返回NULL。

#### OH_AVCapability_IsHardware()

```ets
bool OH_AVCapability_IsHardware(OH_AVCapability *capability)
```

**描述**

检查能力实例是否描述了硬件编解码器。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编解码能力指针。

**返回：**

类型说明bool如果能力实例描述的是硬件编解码器，则返回true，如果功能实例描述的是软件编解码器，则为false。

#### OH_AVCapability_GetName()

```ets
const char *OH_AVCapability_GetName(OH_AVCapability *capability)
```

**描述**

获取编解码器名称。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编解码能力指针。

**返回：**

类型说明const char *返回编解码器名称字符串。

#### OH_AVCapability_GetMaxSupportedInstances()

```ets
int32_t OH_AVCapability_GetMaxSupportedInstances(OH_AVCapability *capability)
```

**描述**

获取编解码器支持的最大实例数。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编解码能力指针。

**返回：**

类型说明int32_t返回支持的最大编解码器实例数。

#### OH_AVCapability_GetEncoderBitrateRange()

```ets
OH_AVErrCode OH_AVCapability_GetEncoderBitrateRange(OH_AVCapability *capability, OH_AVRange *bitrateRange)
```

**描述**

获取编码器支持的比特率范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编码器能力指针。如果给的是解码器能力指针，会导致未定义行为。[OH_AVRange](OH_AVRange.md) *bitrateRange输出参数。编码器码率范围。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向编码器码率范围的指针为空指针。

#### OH_AVCapability_IsEncoderBitrateModeSupported()

```ets
bool OH_AVCapability_IsEncoderBitrateModeSupported(OH_AVCapability *capability, OH_BitrateMode bitrateMode)
```

**描述**

检查编码器是否支持特定的比特率模式。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编码器能力指针。如果给的是解码器能力指针，会导致未定义行为。[OH_BitrateMode](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__oh_bitratemode) bitrateMode比特率模式。

**返回：**

类型说明bool如果支持该比特率模式，则返回true；如果不支持该比特率模式，则返回false。

#### OH_AVCapability_GetEncoderQualityRange()

```ets
OH_AVErrCode OH_AVCapability_GetEncoderQualityRange(OH_AVCapability *capability, OH_AVRange *qualityRange)
```

**描述**

获取编码器支持的质量范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编码器能力指针。如果给的是解码器能力指针，会导致未定义行为。[OH_AVRange](OH_AVRange.md) *qualityRange输出参数。编码器质量范围。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向编码器质量范围的指针为空指针。

#### OH_AVCapability_GetEncoderComplexityRange()

```ets
OH_AVErrCode OH_AVCapability_GetEncoderComplexityRange(OH_AVCapability *capability, OH_AVRange *complexityRange)
```

**描述**

获取编码器支持的编码器复杂性范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编码器能力指针。如果给的是解码器能力指针，会导致未定义行为。[OH_AVRange](OH_AVRange.md) *complexityRange输出参数。编码器复杂度范围。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向编码器复杂度范围的指针为空指针。

#### OH_AVCapability_GetAudioSupportedSampleRates()

```ets
OH_AVErrCode OH_AVCapability_GetAudioSupportedSampleRates(OH_AVCapability *capability, const int32_t **sampleRates, uint32_t *sampleRateNum)
```

**描述**

获取音频编解码器支持的采样率。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability音频编解码能力指针。如果给的是视频编解码器能力指针，会导致未定义行为。const int32_t **sampleRates输出参数。指向采样率数组的指针。uint32_t *sampleRateNum输出参数。采样率数组的元素数目。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向采样率数组的指针为空指针，或者指向采样率数组的元素数目的指针为空指针。

 AV_ERR_UNKNOWN：未知错误。

 AV_ERR_NO_MEMORY：内部使用内存分配失败。

#### OH_AVCapability_GetAudioSupportedSampleRateRanges()

```ets
OH_AVErrCode OH_AVCapability_GetAudioSupportedSampleRateRanges(OH_AVCapability *capability, OH_AVRange **sampleRateRanges, uint32_t *rangesNum)
```

**描述**

获取音频编解码器支持的采样率范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 20

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability音频编解码能力指针。如果给的是视频编解码器能力指针，会导致未定义行为。[OH_AVRange](OH_AVRange.md) **sampleRateRanges输出参数。指向采样率范围数组的指针。uint32_t *rangesNum输出参数。采样率范围数组的元素数目。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向采样率范围数组的指针为空指针，或者指向采样率范围数组的元素数目的指针为空指针。

 AV_ERR_UNKNOWN：未知错误。

 AV_ERR_NO_MEMORY：内部使用内存分配失败。

#### OH_AVCapability_GetAudioChannelCountRange()

```ets
OH_AVErrCode OH_AVCapability_GetAudioChannelCountRange(OH_AVCapability *capability, OH_AVRange *channelCountRange)
```

**描述**

获取音频编解码器支持的音频通道计数范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability音频编解码能力指针。如果给的是视频编解码器能力指针，会导致未定义行为。[OH_AVRange](OH_AVRange.md) *channelCountRange输出参数。音频通道计数范围。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向音频通道计数范围的指针为空指针。

#### OH_AVCapability_GetVideoWidthAlignment()

```ets
OH_AVErrCode OH_AVCapability_GetVideoWidthAlignment(OH_AVCapability *capability, int32_t *widthAlignment)
```

**描述**

获取视频编解码器支持的视频宽度对齐。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。int32_t *widthAlignment输出参数。视频宽度对齐。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向视频宽度对齐的指针为空指针。

#### OH_AVCapability_GetVideoHeightAlignment()

```ets
OH_AVErrCode OH_AVCapability_GetVideoHeightAlignment(OH_AVCapability *capability, int32_t *heightAlignment)
```

**描述**

获取视频编解码器支持的视频高度对齐。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。int32_t *heightAlignment输出参数。视频高度对齐。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向视频高度对齐的指针为空指针。

#### OH_AVCapability_GetVideoWidthRangeForHeight()

```ets
OH_AVErrCode OH_AVCapability_GetVideoWidthRangeForHeight(OH_AVCapability *capability, int32_t height, OH_AVRange *widthRange)
```

**描述**

获取指定高度情况下视频编解码器支持的视频宽度范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。int32_t height视频垂直像素数。[OH_AVRange](OH_AVRange.md) *widthRange输出参数。视频宽度范围。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者高度不在通过[OH_AVCapability_GetVideoHeightRange](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideoheightrange)获取支持的高度范围中，或者指向宽度范围的指针为空指针。

#### OH_AVCapability_GetVideoHeightRangeForWidth()

```ets
OH_AVErrCode OH_AVCapability_GetVideoHeightRangeForWidth(OH_AVCapability *capability, int32_t width, OH_AVRange *heightRange)
```

**描述**

获取指定宽度情况下视频编解码器支持的视频高度范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。int32_t width视频水平像素数。[OH_AVRange](OH_AVRange.md) *heightRange输出参数。视频高度范围。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者宽度不在通过[OH_AVCapability_GetVideoWidthRange](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getvideowidthrange)获取支持的宽度范围中，或者指向高度范围的指针为空指针。

#### OH_AVCapability_GetVideoWidthRange()

```ets
OH_AVErrCode OH_AVCapability_GetVideoWidthRange(OH_AVCapability *capability, OH_AVRange *widthRange)
```

**描述**

获取视频编解码器支持的视频宽度范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。[OH_AVRange](OH_AVRange.md) *widthRange输出参数。视频宽度范围。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向视频宽度范围的指针为空指针。

#### OH_AVCapability_GetVideoHeightRange()

```ets
OH_AVErrCode OH_AVCapability_GetVideoHeightRange(OH_AVCapability *capability, OH_AVRange *heightRange)
```

**描述**

获取视频编解码器支持的视频高度范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。[OH_AVRange](OH_AVRange.md) *heightRange输出参数。视频高度范围。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向视频高度范围的指针为空指针。

#### OH_AVCapability_IsVideoSizeSupported()

```ets
bool OH_AVCapability_IsVideoSizeSupported(OH_AVCapability *capability, int32_t width, int32_t height)
```

**描述**

检查视频编解码器是否支持特定的视频大小。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。int32_t width视频水平像素数。int32_t height视频垂直像素数。

**返回：**

类型说明bool如果支持该视频大小，则返回true，如果不支持该视频大小，则返回false。

#### OH_AVCapability_GetVideoFrameRateRange()

```ets
OH_AVErrCode OH_AVCapability_GetVideoFrameRateRange(OH_AVCapability *capability, OH_AVRange *frameRateRange)
```

**描述**

获取视频编解码器支持的视频帧率范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。[OH_AVRange](OH_AVRange.md) *frameRateRange输出参数。视频帧率范围。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向视频帧率范围的指针为空指针。

#### OH_AVCapability_GetVideoFrameRateRangeForSize()

```ets
OH_AVErrCode OH_AVCapability_GetVideoFrameRateRangeForSize(OH_AVCapability *capability, int32_t width, int32_t height, OH_AVRange *frameRateRange)
```

**描述**

获取指定视频大小的视频编解码器支持的视频帧率范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。int32_t width视频水平像素数。int32_t height视频垂直像素数。[OH_AVRange](OH_AVRange.md) *frameRateRange输出参数。视频帧率范围。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者宽度和高度组合不支持，或者指向帧率范围的指针为空指针。

#### OH_AVCapability_AreVideoSizeAndFrameRateSupported()

```ets
bool OH_AVCapability_AreVideoSizeAndFrameRateSupported(OH_AVCapability *capability, int32_t width, int32_t height, int32_t frameRate)
```

**描述**

检查视频编解码器是否支持视频大小和帧率的特定组合。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。int32_t width视频水平像素数。int32_t height视频垂直像素数。int32_t frameRate每秒帧数。

**返回：**

类型说明bool如果支持视频大小和帧率的组合，则返回true。如果不支持，则为false。

#### OH_AVCapability_GetVideoSupportedPixelFormats()

```ets
OH_AVErrCode OH_AVCapability_GetVideoSupportedPixelFormats(OH_AVCapability *capability, const int32_t **pixelFormats, uint32_t *pixelFormatNum)
```

**描述**

获取视频编解码器支持的视频像素格式。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。const int32_t **pixelFormats输出参数。指向视频像素格式数组的指针。uint32_t *pixelFormatNum输出参数。像素格式数组的元素数目。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向视频像素格式数组的指针为空指针，或者指向像素格式数组的元素数目的指针为空指针。

 AV_ERR_UNKNOWN：未知错误。

 AV_ERR_NO_MEMORY：内部使用内存分配失败。

#### OH_AVCapability_GetVideoSupportedNativeBufferFormats()

```ets
OH_AVErrCode OH_AVCapability_GetVideoSupportedNativeBufferFormats(OH_AVCapability *capability, const OH_NativeBuffer_Format **nativeBufferFormats, uint32_t *nativeBufferFormatNum)
```

**描述**

获取视频编解码器支持的OH_NativeBuffer格式。该函数提供了视频编解码器能够处理的OH_NativeBuffer格式信息，具体取值可见OH_NativeBuffer_Format。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 22

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability视频编解码能力指针。const [OH_NativeBuffer_Format](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_format) **nativeBufferFormats输出参数。指向OH_NativeBuffer_Format数组的指针。uint32_t *nativeBufferFormatNum输出参数。OH_NativeBuffer_Format数组的元素数目。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效、能力实例是音频编码解码器能力、指向NativeBuffer格式数组的指针为空指针、

 或指向NativeBuffer格式数组的元素数目的指针为空指针。

 AV_ERR_UNKNOWN：未知错误。

 AV_ERR_NO_MEMORY：内部使用内存分配失败。

#### OH_AVCapability_GetSupportedProfiles()

```ets
OH_AVErrCode OH_AVCapability_GetSupportedProfiles(OH_AVCapability *capability, const int32_t **profiles, uint32_t *profileNum)
```

**描述**

获取编解码器支持的档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编解码能力指针。const int32_t **profiles输出参数。指向档次数组的指针。uint32_t *profileNum输出参数。档次数组的元素数目。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者指向档次数组的指针为空指针，或者指向档次数组的元素数目的指针为空指针。

 AV_ERR_UNKNOWN：未知错误。

 AV_ERR_NO_MEMORY：内部使用内存分配失败。

#### OH_AVCapability_GetSupportedLevelsForProfile()

```ets
OH_AVErrCode OH_AVCapability_GetSupportedLevelsForProfile(OH_AVCapability *capability, int32_t profile, const int32_t **levels, uint32_t *levelNum)
```

**描述**

获取特定档次支持的编解码器级别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编解码能力指针。int32_t profile编解码器档次。const int32_t **levels输出参数。指向级别数组的指针。uint32_t *levelNum输出参数。级别数组的元素数目。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：执行成功。

 AV_ERR_INVALID_VAL：能力实例无效，或者档次不在通过[OH_AVCapability_GetSupportedProfiles](#ZH-CN_TOPIC_0000002497445758__oh_avcapability_getsupportedprofiles)获取支持的档次数组中，或者指向级别数组的指针为空指针，或者指向级别数组的元素数目的指针为空指针。

 AV_ERR_UNKNOWN：未知错误。

 AV_ERR_NO_MEMORY：内部使用内存分配失败。

#### OH_AVCapability_AreProfileAndLevelSupported()

```ets
bool OH_AVCapability_AreProfileAndLevelSupported(OH_AVCapability *capability, int32_t profile, int32_t level)
```

**描述**

检查编解码器是否支持档次和级别的特定组合。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编解码能力指针。int32_t profile编解码器档次。int32_t level编解码器级别。

**返回：**

类型说明bool如果支持档次和级别的组合，则返回true。如果不支持，则为false。

#### OH_AVCapability_IsFeatureSupported()

```ets
bool OH_AVCapability_IsFeatureSupported(OH_AVCapability *capability, OH_AVCapabilityFeature feature)
```

**描述**

检查编解码器是否支持指定特性。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 12

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编解码能力指针。[OH_AVCapabilityFeature](#ZH-CN_TOPIC_0000002497445758__oh_avcapabilityfeature) feature编解码特性。

**返回：**

类型说明bool如果支持该特性，则返回true。如果不支持，则为false。

#### OH_AVCapability_GetFeatureProperties()

```ets
OH_AVFormat *OH_AVCapability_GetFeatureProperties(OH_AVCapability *capability, OH_AVCapabilityFeature feature)
```

**描述**

获取指定特性的属性。需要注意的是，返回值指向的OH_AVFormat实例的生命周期需要调用者手动释放。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 12

**参数：**

参数项描述[OH_AVCapability](OH_AVCapability.md) *capability编解码能力指针。[OH_AVCapabilityFeature](#ZH-CN_TOPIC_0000002497445758__oh_avcapabilityfeature) feature编解码特性。

**返回：**

类型说明[OH_AVFormat](OH_AVFormat.md) *返回指向OH_AVFormat实例的指针。