# video_processing_types.h

#### 概述

视频处理类型定义。

**引用文件：** <multimedia/video_processing_engine/video_processing_types.h>

**库：** libvideo_processing.so

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**起始版本：** 12

**相关模块：**[VideoProcessing](VideoProcessing.md)

#### 汇总

#### 结构体

名称typedef关键字描述[VideoProcessing_ColorSpaceInfo](VideoProcessing_ColorSpaceInfo.md)VideoProcessing_ColorSpaceInfo视频颜色空间信息数据结构。[OH_VideoProcessing](OH_VideoProcessing.md)OH_VideoProcessing

定义视频处理对象。

定义一个OH_VideoProcessing空指针，调用[OH_VideoProcessing_Create](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_create)创建视频处理实例，该指针在创建实例之前必须为空。用户可以对不同的处理类型创建不同的视频处理实例。

[NativeWindow](NativeWindow.md)OHNativeWindow定义NativeWindow对象。[OH_AVFormat](OH_AVFormat.md)OH_AVFormat定义OH_AVFormat对象。[VideoProcessing_Callback](VideoProcessing_Callback.md)VideoProcessing_Callback

视频处理回调对象类型。

定义一个VideoProcessing_Callback空指针，调用[OH_VideoProcessingCallback_Create](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessingcallback_create)来创建一个回调对象。创建之前该指针必须为空。通过调用[OH_VideoProcessing_RegisterCallback](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_registercallback)来向视频处理实例注册回调对象。

#### 枚举

名称typedef关键字描述[VideoDetailEnhancer_QualityLevel](#ZH-CN_TOPIC_0000002497605922__videodetailenhancer_qualitylevel)VideoDetailEnhancer_QualityLevel用于细节增强的质量等级。[VideoMetadataGeneratorStyleControl](#ZH-CN_TOPIC_0000002497605922__videometadatageneratorstylecontrol)VideoMetadataGeneratorStyleControl视频元数据生成的风格模式。参数的具体取值请参考[VIDEO_METADATA_GENERATOR_STYLE_CONTROL](#ZH-CN_TOPIC_0000002497605922__变量)。[VideoProcessing_ErrorCode](#ZH-CN_TOPIC_0000002497605922__videoprocessing_errorcode)VideoProcessing_ErrorCode视频处理错误码。[VideoProcessing_State](#ZH-CN_TOPIC_0000002497605922__videoprocessing_state)VideoProcessing_State

视频处理状态。

视频处理状态通过回调函数[OH_VideoProcessingCallback_OnState](#ZH-CN_TOPIC_0000002497605922__oh_videoprocessingcallback_onstate)进行报告。

#### 函数

名称typedef关键字描述[typedef void (*OH_VideoProcessingCallback_OnError)(OH_VideoProcessing* videoProcessor, VideoProcessing_ErrorCode error, void* userData)](#ZH-CN_TOPIC_0000002497605922__oh_videoprocessingcallback_onerror)OH_VideoProcessingCallback_OnError

视频处理过程中报告错误的回调函数指针。

 错误码[VideoProcessing_ErrorCode](#ZH-CN_TOPIC_0000002497605922__videoprocessing_errorcode)：VIDEO_PROCESSING_ERROR_UNSUPPORTED_PROCESSING，不支持的处理，比如不支持输入输出的颜色空间类型转换。

 VIDEO_PROCESSING_ERROR_INVALID_VALUE，无效的视频属性，比如视频的颜色空间无效。

 VIDEO_PROCESSING_ERROR_NO_MEMORY，内存不足。

 VIDEO_PROCESSING_ERROR_PROCESS_FAILED，处理过程中出错。

[typedef void (*OH_VideoProcessingCallback_OnState)(OH_VideoProcessing* videoProcessor, VideoProcessing_State state, void* userData)](#ZH-CN_TOPIC_0000002497605922__oh_videoprocessingcallback_onstate)OH_VideoProcessingCallback_OnState

报告视频处理状态的回调函数指针。

[OH_VideoProcessing_Start](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_start)成功调用之后状态会变为[VideoProcessing_State](#ZH-CN_TOPIC_0000002497605922__videoprocessing_state).VIDEO_PROCESSING_STATE_RUNNING。调用[OH_VideoProcessing_Stop](zh-cn_topic_0000002529445885.html#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_stop)，所有的缓存buffer处理完成后，状态会变为[VideoProcessing_State](#ZH-CN_TOPIC_0000002497605922__videoprocessing_state).VIDEO_PROCESSING_STATE_STOPPED。

[typedef void (*OH_VideoProcessingCallback_OnNewOutputBuffer)(OH_VideoProcessing* videoProcessor, uint32_t index, void* userData)](#ZH-CN_TOPIC_0000002497605922__oh_videoprocessingcallback_onnewoutputbuffer)OH_VideoProcessingCallback_OnNewOutputBuffer

报告输出buffer已填充好数据的回调函数指针。

每个新输出buffer填充好数据之后该buffer的索引就会报告给用户。调用[OH_VideoProcessing_RenderOutputBuffer](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_renderoutputbuffer)根据索引来处理渲染并输出该buffer。如果未注册该函数，则输出buffer填充好数据后不会报告用户，而是直接进行处理渲染并输出。

#### 变量

名称描述const int32_t VIDEO_PROCESSING_TYPE_COLOR_SPACE_CONVERSION

表示创建颜色空间转换视频处理实例。

调用[OH_VideoProcessing_Create](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_create)创建颜色空间转换视频处理实例，如果不支持该能力返回[VideoProcessing_ErrorCode](#ZH-CN_TOPIC_0000002497605922__videoprocessing_errorcode).VIDEO_PROCESSING_ERROR_UNSUPPORTED_PROCESSING。

**起始版本：** 12

const int32_t VIDEO_PROCESSING_TYPE_METADATA_GENERATION

表示创建元数据生成视频处理实例。

调用[OH_VideoProcessing_Create](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_create)创建元数据生成视频处理实例，如果不支持该能力返回[VideoProcessing_ErrorCode](#ZH-CN_TOPIC_0000002497605922__videoprocessing_errorcode).VIDEO_PROCESSING_ERROR_UNSUPPORTED_PROCESSING。

**起始版本：** 12

const int32_t VIDEO_PROCESSING_TYPE_DETAIL_ENHANCER

表示创建细节增强视频处理实例。

调用[OH_VideoProcessing_Create](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_create)创建细节增强视频处理实例，如果不支持该能力返回[VideoProcessing_ErrorCode](#ZH-CN_TOPIC_0000002497605922__videoprocessing_errorcode).VIDEO_PROCESSING_ERROR_UNSUPPORTED_PROCESSING。

**起始版本：** 12

const char* VIDEO_DETAIL_ENHANCER_PARAMETER_KEY_QUALITY_LEVEL

指定视频细节增强的质量等级，参考[VideoDetailEnhancer_QualityLevel](#ZH-CN_TOPIC_0000002497605922__videodetailenhancer_qualitylevel)查看具体取值。

调用[OH_VideoProcessing_SetParameter](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_setparameter)设置质量等级。

调用[OH_VideoProcessing_GetParameter](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_getparameter)获取当前质量等级。

**起始版本：** 12

const char * VIDEO_METADATA_GENERATOR_STYLE_CONTROL

指定视频元数据生成的风格模式。具体取值请参考[VideoMetadataGeneratorStyleControl](#ZH-CN_TOPIC_0000002497605922__videometadatageneratorstylecontrol)。调用[OH_AVFormat_SetIntValue](zh-cn_topic_0000002497445762.html#ZH-CN_TOPIC_0000002497445762__oh_avformat_setintvalue)设置视频元数据生成的风格模式到AVFormat参数。调用[OH_VideoProcessing_SetParameter](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_setparameter)设置当前视频元数据生成的风格模式。调用[OH_VideoProcessing_GetParameter](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_getparameter)获取当前视频元数据生成的风格模式。

**起始版本：** 22

#### 枚举类型说明

#### VideoDetailEnhancer_QualityLevel

```ets
enum VideoDetailEnhancer_QualityLevel
```

**描述**

用于细节增强的质量等级。参数[VIDEO_DETAIL_ENHANCER_PARAMETER_KEY_QUALITY_LEVEL](#ZH-CN_TOPIC_0000002497605922__变量)的具体取值，设置方法详见开发指南。

**起始版本：** 12

枚举项描述VIDEO_DETAIL_ENHANCER_QUALITY_LEVEL_NONE无细节增强。VIDEO_DETAIL_ENHANCER_QUALITY_LEVEL_LOW低质量等级细节增强，速度较快，默认设置。VIDEO_DETAIL_ENHANCER_QUALITY_LEVEL_MEDIUM中等质量等级细节增强，速度适中。VIDEO_DETAIL_ENHANCER_QUALITY_LEVEL_HIGH高质量等级细节增强，速度相对较慢。

**参考：**

[OH_VideoProcessing_SetParameter](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_setparameter)

[OH_VideoProcessing_GetParameter](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_getparameter)

#### VideoMetadataGeneratorStyleControl

```ets
enum VideoMetadataGeneratorStyleControl
```

**描述**

视频元数据生成的风格模式。参数的具体取值请参考[VIDEO_METADATA_GENERATOR_STYLE_CONTROL](#ZH-CN_TOPIC_0000002497605922__变量)。

**起始版本：** 22

枚举项描述VIDEO_METADATA_GENERATOR_CONTRAST_MODE = 0对比度优先模式。VIDEO_METADATA_GENERATOR_BRIGHT_MODE = 1亮度优先模式。

**参考：**

[OH_VideoProcessing_SetParameter](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_setparameter)

[OH_VideoProcessing_GetParameter](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_getparameter)

[OH_AVFormat_SetIntValue](native_avformat.h.md#ZH-CN_TOPIC_0000002497445762__oh_avformat_setintvalue)

#### VideoProcessing_ErrorCode

```ets
enum VideoProcessing_ErrorCode
```

**描述**

视频处理错误码。

**起始版本：** 12

枚举项描述VIDEO_PROCESSING_SUCCESS处理成功。VIDEO_PROCESSING_ERROR_INVALID_PARAMETER = 401

输入参数无效。以下情况都会返回该错误码：

1. 无效的输入或输出视频buffer，视频buffer为空。

2. 无效的参数，参数为空。

3. 无效的处理类型。

VIDEO_PROCESSING_ERROR_UNKNOWN = 29210001未知错误，比如GPU计算失败或memcpy失败。VIDEO_PROCESSING_ERROR_INITIALIZE_FAILED视频处理全局环境初始化失败，比如初始化GPU环境失败。VIDEO_PROCESSING_ERROR_CREATE_FAILED创建视频处理实例失败，比如实例总数超出上限。VIDEO_PROCESSING_ERROR_PROCESS_FAILED处理过程失败，比如处理时间超时。VIDEO_PROCESSING_ERROR_UNSUPPORTED_PROCESSING不支持的处理类型，可以调用OH_VideoProcessing_IsXXXSupported来检查是否支持这种处理。VIDEO_PROCESSING_ERROR_OPERATION_NOT_PERMITTED不允许的操作，比如不满足调用接口所需的运行状态下调用该接口。VIDEO_PROCESSING_ERROR_NO_MEMORY内存不足。VIDEO_PROCESSING_ERROR_INVALID_INSTANCE视频处理实例无效，比如视频处理实例为空实例。VIDEO_PROCESSING_ERROR_INVALID_VALUE

输入值无效，以下情况都会造成这种错误：

1. 视频buffer宽高太大或者颜色空间错误。

2. 参数包含无效的值，比如细节增强的质量等级错误。

#### VideoProcessing_State

```ets
enum VideoProcessing_State
```

**描述**

视频处理状态。视频处理状态通过回调函数[OH_VideoProcessingCallback_OnState](#ZH-CN_TOPIC_0000002497605922__oh_videoprocessingcallback_onstate)进行报告。

**起始版本：** 12

枚举项描述VIDEO_PROCESSING_STATE_RUNNING视频处理进行中。VIDEO_PROCESSING_STATE_STOPPED视频处理已停止。

#### 函数说明

#### OH_VideoProcessingCallback_OnError()

```ets
typedef void (*OH_VideoProcessingCallback_OnError)(OH_VideoProcessing* videoProcessor, VideoProcessing_ErrorCode error, void* userData)
```

**描述**

视频处理过程中报告错误的回调函数指针。

错误码[VideoProcessing_ErrorCode](#ZH-CN_TOPIC_0000002497605922__videoprocessing_errorcode)：

VIDEO_PROCESSING_ERROR_UNSUPPORTED_PROCESSING，不支持的处理，比如不支持输入输出的颜色空间类型转换。

VIDEO_PROCESSING_ERROR_INVALID_VALUE，无效的视频属性，比如视频的颜色空间无效。

VIDEO_PROCESSING_ERROR_NO_MEMORY，内存不足。

VIDEO_PROCESSING_ERROR_PROCESS_FAILED，处理过程中出错。

**起始版本：** 12

**参数：**

参数项描述[OH_VideoProcessing](OH_VideoProcessing.md)* videoProcessor视频处理实例。[VideoProcessing_ErrorCode](#ZH-CN_TOPIC_0000002497605922__videoprocessing_errorcode) error报告给用户的错误码。void* userData用户的自定义数据。

#### OH_VideoProcessingCallback_OnState()

```ets
typedef void (*OH_VideoProcessingCallback_OnState)(OH_VideoProcessing* videoProcessor, VideoProcessing_State state, void* userData)
```

**描述**

报告视频处理状态的回调函数指针。

[OH_VideoProcessing_Start](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_start)成功调用之后状态会变为[VideoProcessing_State](#ZH-CN_TOPIC_0000002497605922__videoprocessing_state).VIDEO_PROCESSING_STATE_RUNNING。调用[OH_VideoProcessing_Stop](zh-cn_topic_0000002529445885.html#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_stop)，所有的缓存buffer处理完成后，状态会变为[VideoProcessing_State](#ZH-CN_TOPIC_0000002497605922__videoprocessing_state).VIDEO_PROCESSING_STATE_STOPPED。

**起始版本：** 12

**参数：**

参数项描述[OH_VideoProcessing](OH_VideoProcessing.md)* videoProcessor视频处理实例。[VideoProcessing_State](#ZH-CN_TOPIC_0000002497605922__videoprocessing_state) state视频处理状态。void* userData用户的自定义数据。

#### OH_VideoProcessingCallback_OnNewOutputBuffer()

```ets
typedef void (*OH_VideoProcessingCallback_OnNewOutputBuffer)(OH_VideoProcessing* videoProcessor, uint32_t index, void* userData)
```

**描述**

报告输出buffer已填充好数据的回调函数指针。

每个新输出buffer填充好数据之后该buffer的索引就会报告给用户。调用[OH_VideoProcessing_RenderOutputBuffer](video_processing.h.md#ZH-CN_TOPIC_0000002529445885__oh_videoprocessing_renderoutputbuffer)根据索引来处理渲染并输出该buffer。如果未注册该函数，则输出buffer填充好数据后不会报告用户，而是直接进行处理渲染并输出。

**起始版本：** 12

**参数：**

参数项描述[OH_VideoProcessing](OH_VideoProcessing.md)* videoProcessor视频处理实例。uint32_t index新输出buffer的索引。void* userData用户自定义的数据。