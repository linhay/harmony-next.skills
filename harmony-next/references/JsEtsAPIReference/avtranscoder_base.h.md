# avtranscoder_base.h

#### 概述

定义了媒体AVTranscoder的结构体和枚举。

**引用文件：** <multimedia/player_framework/avtranscoder_base.h>

**库：** libavtranscoder.so

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**相关模块：**[AVTranscoder](AVTranscoder.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVTranscoder](OH_AVTranscoder.md)OH_AVTranscoder初始化AVTranscoder。[OH_AVTranscoder_Config](OH_AVTranscoder_Config.md)OH_AVTranscoder_Config初始化AVTranscoder_Config。

#### 枚举

名称typedef关键字描述[OH_AVTranscoder_State](#ZH-CN_TOPIC_0000002529285907__oh_avtranscoder_state)OH_AVTranscoder_State转码状态。

#### 函数

名称typedef关键字描述[typedef void (*OH_AVTranscoder_OnStateChange)(OH_AVTranscoder *transcoder, OH_AVTranscoder_State state, void *userData)](#ZH-CN_TOPIC_0000002529285907__oh_avtranscoder_onstatechange)OH_AVTranscoder_OnStateChange转码过程的状态回调函数。[typedef void (*OH_AVTranscoder_OnError)(OH_AVTranscoder *transcoder, int32_t errorCode, const char *errorMsg, void *userData)](#ZH-CN_TOPIC_0000002529285907__oh_avtranscoder_onerror)OH_AVTranscoder_OnError转码过程中错误事件的回调函数。[typedef void (*OH_AVTranscoder_OnProgressUpdate)(OH_AVTranscoder *transcoder, int32_t progress, void *userData)](#ZH-CN_TOPIC_0000002529285907__oh_avtranscoder_onprogressupdate)OH_AVTranscoder_OnProgressUpdate回调转码进度更新时调用。

#### 枚举类型说明

#### OH_AVTranscoder_State

```ets
enum OH_AVTranscoder_State
```

**描述**

转码状态。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

枚举项描述AVTRANSCODER_PREPARED = 1准备AVTRANSCODER_STARTED = 2开始AVTRANSCODER_PAUSED = 3暂停AVTRANSCODER_CANCELLED = 4取消AVTRANSCODER_COMPLETED = 5完成

#### 函数说明

#### OH_AVTranscoder_OnStateChange()

```ets
typedef void (*OH_AVTranscoder_OnStateChange)(OH_AVTranscoder *transcoder, OH_AVTranscoder_State state, void *userData)
```

**描述**

转码过程的状态回调函数。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

参数项描述[OH_AVTranscoder](OH_AVTranscoder.md) *transcoderOH_AVTranscoder实例的指针。[OH_AVTranscoder_State](#ZH-CN_TOPIC_0000002529285907__oh_avtranscoder_state) state转码状态，详细说明请参见[OH_AVTranscoder_State](#ZH-CN_TOPIC_0000002529285907__oh_avtranscoder_state)。void *userData用户特定数据的指针。

#### OH_AVTranscoder_OnError()

```ets
typedef void (*OH_AVTranscoder_OnError)(OH_AVTranscoder *transcoder, int32_t errorCode, const char *errorMsg,void *userData)
```

**描述**

转码过程中错误事件的回调函数。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

参数项描述[OH_AVTranscoder](OH_AVTranscoder.md) *transcoderOH_AVTranscoder实例的指针。int32_t errorCode

错误码。

 AV_ERR_NO_MEMORY：无内存，取值为1。

 AV_ERR_OPERATE_NOT_PERMIT：操作不允许，取值为2。

 AV_ERR_INVALID_VAL：参数检查失败，取值为3。

 AV_ERR_IO：IO错误，取值为4。

 AV_ERR_INVALID_STATE：当前状态不支持此操作，取值为8。

 AV_ERR_UNSUPPORT：未支持的接口，取值为9。

const char *errorMsg错误消息。void *userData用户特定数据的指针。

#### OH_AVTranscoder_OnProgressUpdate()

```ets
typedef void (*OH_AVTranscoder_OnProgressUpdate)(OH_AVTranscoder *transcoder, int32_t progress, void *userData)
```

**描述**

回调转码进度更新时调用。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

参数项描述[OH_AVTranscoder](OH_AVTranscoder.md) *transcoderOH_AVTranscoder实例的指针。int32_t progress转码进度。void *userData用户特定数据的指针。