# native_avformat.h

#### 概述

声明了OH_AVFormat相关的函数和枚举。

**引用文件：** <multimedia/player_framework/native_avformat.h>

**库：** libnative_media_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**相关模块：**[Core](Core.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVFormat](OH_AVFormat.md)OH_AVFormat为OH_AVFormat接口定义native层对象。

#### 枚举

名称typedef关键字描述[OH_AVPixelFormat](#ZH-CN_TOPIC_0000002497445762__oh_avpixelformat)OH_AVPixelFormat视频像素格式的枚举类。

#### 函数

名称描述[struct OH_AVFormat *OH_AVFormat_Create(void)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_create)创建OH_AVFormat实例，用于读取数据。[struct OH_AVFormat *OH_AVFormat_CreateAudioFormat(const char *mimeType, int32_t sampleRate, int32_t channelCount)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_createaudioformat)创建音频OH_AVFormat实例指针并预设置指定参数，用于读写数据。[struct OH_AVFormat *OH_AVFormat_CreateVideoFormat(const char *mimeType, int32_t width, int32_t height)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_createvideoformat)创建视频OH_AVFormat实例指针并预设置指定参数，用于读写数据。[void OH_AVFormat_Destroy(struct OH_AVFormat *format)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_destroy)销毁OH_AVFormat实例，不允许重复销毁。[bool OH_AVFormat_Copy(struct OH_AVFormat *to, struct OH_AVFormat *from)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_copy)复制OH_AVFormat实例。[bool OH_AVFormat_SetIntValue(struct OH_AVFormat *format, const char *key, int32_t value)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_setintvalue)对OH_AVFormat的[key](zh-cn_topic_0000002497605732.html#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)赋int类型的值。该接口仅能设置int类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。[bool OH_AVFormat_SetLongValue(struct OH_AVFormat *format, const char *key, int64_t value)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_setlongvalue)对OH_AVFormat的[key](zh-cn_topic_0000002497605732.html#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)赋long类型的值。该接口仅能设置long类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。[bool OH_AVFormat_SetFloatValue(struct OH_AVFormat *format, const char *key, float value)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_setfloatvalue)对OH_AVFormat的[key](zh-cn_topic_0000002497605732.html#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)赋float类型的值。该接口仅能设置float类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。[bool OH_AVFormat_SetDoubleValue(struct OH_AVFormat *format, const char *key, double value)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_setdoublevalue)对OH_AVFormat的[key](zh-cn_topic_0000002497605732.html#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)赋double类型的值。该接口仅能设置double类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。[bool OH_AVFormat_SetStringValue(struct OH_AVFormat *format, const char *key, const char *value)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_setstringvalue)对OH_AVFormat的[key](zh-cn_topic_0000002497605732.html#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)赋string类型的值。该接口仅能设置string类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。[bool OH_AVFormat_SetBuffer(struct OH_AVFormat *format, const char *key, const uint8_t *addr, size_t size)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_setbuffer)将指定长度的数据块写入OH_AVFormat。该接口仅能设置buffer类型的参数，参数类型定义详见[native_avcodec_base.h](zh-cn_topic_0000002529445703.html#ZH-CN_TOPIC_0000002529445703__变量)。[bool OH_AVFormat_GetIntValue(struct OH_AVFormat *format, const char *key, int32_t *out)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_getintvalue)从OH_AVFormat的[key](zh-cn_topic_0000002497605732.html#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)获取int类型的值。[bool OH_AVFormat_GetLongValue(struct OH_AVFormat *format, const char *key, int64_t *out)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_getlongvalue)从OH_AVFormat的[key](zh-cn_topic_0000002497605732.html#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)获取long类型的值。[bool OH_AVFormat_GetFloatValue(struct OH_AVFormat *format, const char *key, float *out)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_getfloatvalue)从OH_AVFormat的[key](zh-cn_topic_0000002497605732.html#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)获取float类型的值。[bool OH_AVFormat_GetDoubleValue(struct OH_AVFormat *format, const char *key, double *out)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_getdoublevalue)从OH_AVFormat的[key](zh-cn_topic_0000002497605732.html#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)获取double类型的值。[bool OH_AVFormat_GetStringValue(struct OH_AVFormat *format, const char *key, const char **out)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_getstringvalue)从OH_AVFormat的[key](zh-cn_topic_0000002497605732.html#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)获取string类型的值。[bool OH_AVFormat_GetBuffer(struct OH_AVFormat *format, const char *key, uint8_t **addr, size_t *size)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_getbuffer)从OH_AVFormat中读取指定长度的数据块。[bool OH_AVFormat_GetIntBuffer(struct OH_AVFormat *format, const char *key, int32_t **addr, size_t *size)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_getintbuffer)

从OH_AVFormat中读取一个int32_t数据的数组。

 需要注意的是，获取的buffer生命周期与OH_AVFormat对象绑定，当format销毁时自动失效。

 如果开发者需要长时间保持绑定，应用程序必须将数据显式复制到新分配的内存。

[const char *OH_AVFormat_DumpInfo(struct OH_AVFormat *format)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_dumpinfo)返回OH_AVFormat中包含的key-value组成的字符串。最大可返回1024字节的字符串，销毁format时释放字符串指针。[bool OH_AVFormat_SetIntBuffer(struct OH_AVFormat *format, const char *key, const int32_t *addr, size_t size)](#ZH-CN_TOPIC_0000002497445762__oh_avformat_setintbuffer)将指定长度int32_t类型的数据块写入OH_AVFormat。

#### 枚举类型说明

#### OH_AVPixelFormat

```ets
enum OH_AVPixelFormat
```

**描述**

视频像素格式的枚举类。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

枚举项描述AV_PIXEL_FORMAT_YUVI420 = 1yuv 420 planar。AV_PIXEL_FORMAT_NV12 = 2NV12. yuv 420 semiplanar。AV_PIXEL_FORMAT_NV21 = 3NV21. yvu 420 semiplanar。AV_PIXEL_FORMAT_SURFACE_FORMAT = 4像素格式从surface获取。只作用于Surface模式，Buffer模式不生效。AV_PIXEL_FORMAT_RGBA = 5RGBA8888。AV_PIXEL_FORMAT_RGBA1010102 = 6

RGBA1010102。

**起始版本：** 20

#### 函数说明

#### OH_AVFormat_Create()

```ets
struct OH_AVFormat *OH_AVFormat_Create(void)
```

**描述**

创建OH_AVFormat实例，用于读取数据。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**返回：**

类型说明[struct OH_AVFormat](OH_AVFormat.md) *返回指向OH_AVFormat实例的指针。系统资源不足时返回NULL。

#### OH_AVFormat_CreateAudioFormat()

```ets
struct OH_AVFormat *OH_AVFormat_CreateAudioFormat(const char *mimeType, int32_t sampleRate, int32_t channelCount)
```

**描述**

创建音频OH_AVFormat实例指针并预设置指定参数，用于读写数据。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 10

**参数：**

参数项描述const char *mimeTypeMIME类型描述字符串，请参阅[AVCODEC_MIMETYPE](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。int32_t sampleRate采样率，单位Hz。int32_t channelCount声道个数，如1为单声道，2为双声道。

**返回：**

类型说明[struct OH_AVFormat](OH_AVFormat.md) *

如果创建成功，返回指向OH_AVFormat实例的指针，如果失败，则返回NULL。

 可能的失败原因：

 1. 传入的mimeType为NULL。

 2. 系统资源不足。

#### OH_AVFormat_CreateVideoFormat()

```ets
struct OH_AVFormat *OH_AVFormat_CreateVideoFormat(const char *mimeType, int32_t width, int32_t height)
```

**描述**

创建视频OH_AVFormat实例指针并预设置指定参数，用于读写数据。

**系统能力：** SystemCapability.Multimedia.Media.Core

**参数：**

参数项描述const char *mimeTypeMIME类型描述字符串，请参阅[AVCODEC_MIMETYPE](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。int32_t width图像的宽度，单位为pixel。int32_t height图像的高度，单位为pixel。

**返回：**

类型说明[struct OH_AVFormat](OH_AVFormat.md) *

如果创建成功，返回指向OH_AVFormat实例的指针，如果失败，则返回NULL。

 可能的失败原因：

 1. 传入的mimeType为NULL。

 2. 系统资源不足。

#### OH_AVFormat_Destroy()

```ets
void OH_AVFormat_Destroy(struct OH_AVFormat *format)
```

**描述**

销毁OH_AVFormat实例，不允许重复销毁。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。

#### OH_AVFormat_Copy()

```ets
bool OH_AVFormat_Copy(struct OH_AVFormat *to, struct OH_AVFormat *from)
```

**描述**

复制OH_AVFormat实例。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *toOH_AVFormat实例，用于接收数据。[struct OH_AVFormat](OH_AVFormat.md) *from指向复制数据的OH_AVFormat实例的指针。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入参数为空指针。

 2. 输入的OH_AVFormat参数结构校验失败。

#### OH_AVFormat_SetIntValue()

```ets
bool OH_AVFormat_SetIntValue(struct OH_AVFormat *format, const char *key, int32_t value)
```

**描述**

对OH_AVFormat的[key](CodecBase.md#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)赋int类型的值。该接口仅能设置int类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key写入数据的键。int32_t value写入数据的值。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 设置的key对应的value类型错误。

#### OH_AVFormat_SetLongValue()

```ets
bool OH_AVFormat_SetLongValue(struct OH_AVFormat *format, const char *key, int64_t value)
```

**描述**

对OH_AVFormat的[key](CodecBase.md#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)赋long类型的值。该接口仅能设置long类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key写入数据的键。int64_t value写入数据的值。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 设置的key对应的value类型错误。

#### OH_AVFormat_SetFloatValue()

```ets
bool OH_AVFormat_SetFloatValue(struct OH_AVFormat *format, const char *key, float value)
```

**描述**

对OH_AVFormat的[key](CodecBase.md#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)赋float类型的值。该接口仅能设置float类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key写入数据的键。float value写入数据的值。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 设置的key对应的value类型错误。

#### OH_AVFormat_SetDoubleValue()

```ets
bool OH_AVFormat_SetDoubleValue(struct OH_AVFormat *format, const char *key, double value)
```

**描述**

对OH_AVFormat的[key](CodecBase.md#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)赋double类型的值。该接口仅能设置double类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key写入数据的键。double value写入数据的值。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 设置的key对应的value类型错误。

#### OH_AVFormat_SetStringValue()

```ets
bool OH_AVFormat_SetStringValue(struct OH_AVFormat *format, const char *key, const char *value)
```

**描述**

对OH_AVFormat的[key](CodecBase.md#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)赋string类型的值。该接口仅能设置string类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key写入数据的键。const char *value写入字符串数据（使用建议：设置字符长度不超过256字节）。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 输入value为空指针。

 5. 设置的key对应的value类型错误。

#### OH_AVFormat_SetBuffer()

```ets
bool OH_AVFormat_SetBuffer(struct OH_AVFormat *format, const char *key, const uint8_t *addr, size_t size)
```

**描述**

将指定长度的数据块写入OH_AVFormat。该接口仅能设置buffer类型的参数，参数类型定义详见[native_avcodec_base.h](native_avcodec_base.h.md#ZH-CN_TOPIC_0000002529445703__变量)。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key写入数据的键。const uint8_t *addr写入数据的地址，生命周期由开发者管理。size_t size写入数据的长度，范围为(0, 1]MB。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 输入addr为空指针。

 5. size为0或超过限制1MB。

 6. 设置的key对应的value类型错误。

#### OH_AVFormat_GetIntValue()

```ets
bool OH_AVFormat_GetIntValue(struct OH_AVFormat *format, const char *key, int32_t *out)
```

**描述**

从OH_AVFormat的[key](CodecBase.md#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)获取int类型的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key读取数据的键。int32_t *out读取数据的值。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 输入out为空指针。

 5. 获取的key不存在或者未设置。

#### OH_AVFormat_GetLongValue()

```ets
bool OH_AVFormat_GetLongValue(struct OH_AVFormat *format, const char *key, int64_t *out)
```

**描述**

从OH_AVFormat的[key](CodecBase.md#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)获取long类型的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key读取数据的键。int64_t *out读取数据的值。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 输入out为空指针。

 5. 获取的key不存在或者未设置。

#### OH_AVFormat_GetFloatValue()

```ets
bool OH_AVFormat_GetFloatValue(struct OH_AVFormat *format, const char *key, float *out)
```

**描述**

从OH_AVFormat的[key](CodecBase.md#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)获取float类型的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key读取数据的键。float *out读取数据的值。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 输入out为空指针。

 5. 获取的key不存在或者未设置。

#### OH_AVFormat_GetDoubleValue()

```ets
bool OH_AVFormat_GetDoubleValue(struct OH_AVFormat *format, const char *key, double *out)
```

**描述**

从OH_AVFormat的[key](CodecBase.md#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)获取double类型的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key读取数据的键。double *out读取数据的值。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 输入out为空指针。

 5. 获取的key不存在或者未设置。

#### OH_AVFormat_GetStringValue()

```ets
bool OH_AVFormat_GetStringValue(struct OH_AVFormat *format, const char *key, const char **out)
```

**描述**

从OH_AVFormat的[key](CodecBase.md#ZH-CN_TOPIC_0000002497605732__媒体数据键值对)获取string类型的值。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key读取数据的键。const char **out读取string指针，out数据的生命周期与format内string对应，如果开发者需要长时间保持它，必须进行拷贝内存。out最大输出字符串长度为256字节，如果长度超过256字节，会报false。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 输入out为空指针。

 5. malloc出的out字符串资源不足。

 6. 获取的key不存在或者未设置。

 7. 输出out的长度超过256字节。

#### OH_AVFormat_GetBuffer()

```ets
bool OH_AVFormat_GetBuffer(struct OH_AVFormat *format, const char *key, uint8_t **addr, size_t *size)
```

**描述**

从OH_AVFormat中读取指定长度的数据块。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key要读取数据的键。uint8_t **addr生命周期与format相同，与format一同销毁。如果开发者需要长时间保持它，必须进行内存拷贝。size_t *size读到数据的长度。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 输入addr为空指针。

 5. 输入size为空指针。

 6. 获取的key不存在或者未设置。

#### OH_AVFormat_GetIntBuffer()

```ets
bool OH_AVFormat_GetIntBuffer(struct OH_AVFormat *format, const char *key, int32_t **addr, size_t *size)
```

**描述**

从OH_AVFormat中读取一个int32_t数据的数组。

 需要注意的是，获取的buffer生命周期与OH_AVFormat对象绑定，当format销毁时自动失效。

 如果开发者需要长时间保持绑定，应用程序必须将数据显式复制到新分配的内存。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key要读取数据的键。int32_t **addr保存数据内存的指针。size_t *size读到数据的元素数量。

**返回：**

类型说明bool

返回值为true表示成功，为false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 输入addr为空指针。

 5. 输入size为空指针。

#### OH_AVFormat_DumpInfo()

```ets
const char *OH_AVFormat_DumpInfo(struct OH_AVFormat *format)
```

**描述**

返回OH_AVFormat中包含的key-value组成的字符串。最大可返回1024字节的字符串，销毁format时释放字符串指针。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。

**返回：**

类型说明const char *

如果创建成功，返回一个由key-value组成的字符串，如果失败，则返回NULL。

 可能的失败原因：

 1. 传入的format为NULL。

 2. 系统资源不足。

#### OH_AVFormat_SetIntBuffer()

```ets
bool OH_AVFormat_SetIntBuffer(struct OH_AVFormat *format, const char *key, const int32_t *addr, size_t size)
```

**描述**

将指定长度int32_t类型的数据块写入OH_AVFormat。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 20

**参数：**

参数项描述[struct OH_AVFormat](OH_AVFormat.md) *format指向OH_AVFormat实例的指针。const char *key写入数据的键。const int32_t *addr写入数据的地址，生命周期由开发者管理。size_t size写入数据的长度（以元素为单位，不是字节数）。

**返回：**

类型说明bool

返回true表示成功，返回false表示失败。

 可能的失败原因：

 1. 输入format为空指针。

 2. 输入format参数结构校验失败。

 3. 输入key为空指针。

 4. 输入addr为空指针。

 5. 输入size为0。