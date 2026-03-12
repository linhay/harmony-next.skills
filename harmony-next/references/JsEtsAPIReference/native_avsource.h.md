# native_avsource.h

#### 概述

声明用于音视频媒体数据解析的接口。

**引用文件：** <multimedia/player_framework/native_avsource.h>

**库：** libnative_media_avsource.so

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**相关模块：**[AVSource](AVSource.md)

**相关示例：**[AVCodec](https://gitcode.com/HarmonyOS/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_AVSource](OH_AVSource.md)OH_AVSource为媒体资源接口定义native层对象。

#### 函数

名称描述[OH_AVSource *OH_AVSource_CreateWithDataSource(OH_AVDataSource *dataSource)](#ZH-CN_TOPIC_0000002529445709__oh_avsource_createwithdatasource)

为用户自定义数据源的资源对象创建OH_AVSource实例，可以通过调用[OH_AVSource_Destroy](#ZH-CN_TOPIC_0000002529445709__oh_avsource_destroy)接口释放实例。

参数dataSource生命周期需与返回的指针OH_AVSource *保持一致。

[OH_AVSource *OH_AVSource_CreateWithDataSourceExt(OH_AVDataSourceExt *dataSource, void *userData)](#ZH-CN_TOPIC_0000002529445709__oh_avsource_createwithdatasourceext)

为用户自定义数据源的资源对象创建OH_AVSource实例，可以通过调用[OH_AVSource_Destroy](#ZH-CN_TOPIC_0000002529445709__oh_avsource_destroy)接口释放实例。

 回调支持通过userData传递用户自定义数据。

参数dataSource生命周期需与返回的指针OH_AVSource *保持一致。

[OH_AVSource *OH_AVSource_CreateWithURI(char *uri)](#ZH-CN_TOPIC_0000002529445709__oh_avsource_createwithuri)为统一资源标识符对应的资源对象创建OH_AVSource实例，可以通过调用[OH_AVSource_Destroy](#ZH-CN_TOPIC_0000002529445709__oh_avsource_destroy)接口释放实例。该接口仅支持HTTP渐进式流媒体，不支持HLS/DASH的流媒体；对于HLS/DASH的流媒体播放，推荐使用AVPlayer组件进行开发。[OH_AVSource *OH_AVSource_CreateWithFD(int32_t fd, int64_t offset, int64_t size)](#ZH-CN_TOPIC_0000002529445709__oh_avsource_createwithfd)

为文件描述符对应的资源对象创建OH_AVSource实例。可以通过调用[OH_AVSource_Destroy](#ZH-CN_TOPIC_0000002529445709__oh_avsource_destroy)接口释放实例。

 接口如果传入offset不为文件起始位置，或size不为文件大小时，可能会因数据获取不完整导致OH_AVSource创建失败、后续解封装失败等未定义错误。

[OH_AVErrCode OH_AVSource_Destroy(OH_AVSource *source)](#ZH-CN_TOPIC_0000002529445709__oh_avsource_destroy)

销毁OH_AVSource实例并清理内部资源。

 同一实例只能被销毁一次。销毁的实例在被重新创建之前不能再被使用。建议实例销毁成功后将指针置为NULL。

[OH_AVFormat *OH_AVSource_GetSourceFormat(OH_AVSource *source)](#ZH-CN_TOPIC_0000002529445709__oh_avsource_getsourceformat)

获取媒体资源文件的基础信息。

 需要注意的是，指向的OH_AVFormat实例在生命周期结束时需调用者通过调用接口[OH_AVFormat_Destroy](native_avformat.h.md#ZH-CN_TOPIC_0000002497445762__oh_avformat_destroy)释放。

[OH_AVFormat *OH_AVSource_GetTrackFormat(OH_AVSource *source, uint32_t trackIndex)](#ZH-CN_TOPIC_0000002529445709__oh_avsource_gettrackformat)

获取轨道的基础信息。

 需要注意的是，指向的OH_AVFormat实例在生命周期结束时需调用者通过调用接口[OH_AVFormat_Destroy](native_avformat.h.md#ZH-CN_TOPIC_0000002497445762__oh_avformat_destroy)释放。

[OH_AVFormat *OH_AVSource_GetCustomMetadataFormat(OH_AVSource *source)](#ZH-CN_TOPIC_0000002529445709__oh_avsource_getcustommetadataformat)

获取自定义元数据的基础信息。

 需要注意的是，指向的OH_AVFormat实例在生命周期结束时需开发者通过调用接口[OH_AVFormat_Destroy](native_avformat.h.md#ZH-CN_TOPIC_0000002497445762__oh_avformat_destroy)释放。

#### 函数说明

#### OH_AVSource_CreateWithDataSource()

```ets
OH_AVSource *OH_AVSource_CreateWithDataSource(OH_AVDataSource *dataSource)
```

**描述**

为用户自定义数据源的资源对象创建OH_AVSource实例，可以通过调用[OH_AVSource_Destroy](#ZH-CN_TOPIC_0000002529445709__oh_avsource_destroy)接口释放实例。

参数dataSource生命周期需与返回的指针OH_AVSource *保持一致。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

参数项描述[OH_AVDataSource](OH_AVDataSource.md) *dataSource用户自定义数据源。

**返回：**

类型说明[OH_AVSource](OH_AVSource.md) *

如果执行成功，则返回一个指向OH_AVSource实例的指针，否则返回NULL。

 可能的故障原因：

 1. dataSource为nullptr。

 2. dataSource->size == 0。

 3. 设置数据源失败。

 4. 内存不足。

 5. 解码器引擎为nullptr。

 6. dataSource->readAt == nullptr。

#### OH_AVSource_CreateWithDataSourceExt()

```ets
OH_AVSource *OH_AVSource_CreateWithDataSourceExt(OH_AVDataSourceExt *dataSource, void *userData)
```

**描述**

为用户自定义数据源的资源对象创建OH_AVSource实例，可以通过调用[OH_AVSource_Destroy](#ZH-CN_TOPIC_0000002529445709__oh_avsource_destroy)接口释放实例。

 回调支持通过userData传递用户自定义数据。

参数dataSource生命周期需与返回的指针OH_AVSource *保持一致。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 20

**参数：**

参数项描述[OH_AVDataSourceExt](OH_AVDataSourceExt.md) *dataSource指向数据源结构体的指针，该结构体可用于获取输入数据。void *userData指向用户自定义数据的指针。

**返回：**

类型说明[OH_AVSource](OH_AVSource.md) *

如果执行成功，则返回一个指向OH_AVSource实例的指针，否则返回NULL。

 可能的故障原因：

 1. dataSource为nullptr。

 2. dataSource->size == 0。

 3. 设置数据源失败。

 4. 内存不足。

 5. 解码器引擎为nullptr。

 6. dataSource->readAt == nullptr。

#### OH_AVSource_CreateWithURI()

```ets
OH_AVSource *OH_AVSource_CreateWithURI(char *uri)
```

**描述**

为统一资源标识符对应的资源对象创建OH_AVSource实例，可以通过调用[OH_AVSource_Destroy](#ZH-CN_TOPIC_0000002529445709__oh_avsource_destroy)接口释放实例。该接口仅支持HTTP渐进式流媒体，不支持HLS/DASH的流媒体；对于HLS/DASH的流媒体播放，推荐使用AVPlayer组件进行开发。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**参数：**

参数项描述char *uri远程媒体资源的统一资源标识符。

**返回：**

类型说明[OH_AVSource](OH_AVSource.md) *

执行成功返回一个指向OH_AVSource实例的指针, 否则返回NULL。

 可能的故障原因：

 1. 网络异常。

 2. 资源无效。

 3. 文件格式不支持。

 4. 应用配置明文拦截。

#### OH_AVSource_CreateWithFD()

```ets
OH_AVSource *OH_AVSource_CreateWithFD(int32_t fd, int64_t offset, int64_t size)
```

**描述**

为文件描述符对应的资源对象创建OH_AVSource实例。可以通过调用[OH_AVSource_Destroy](#ZH-CN_TOPIC_0000002529445709__oh_avsource_destroy)接口释放实例。

 接口如果传入offset不为文件起始位置，或size不为文件大小时，可能会因数据获取不完整导致OH_AVSource创建失败、后续解封装失败等未定义错误。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**参数：**

参数项描述int32_t fd数据资源的文件描述符。int64_t offset开始读取数据的位置。int64_t size文件的字节数大小。

**返回：**

类型说明[OH_AVSource](OH_AVSource.md) *

执行成功返回一个指向OH_AVSource实例的指针, 否则返回NULL。

 可能的故障原因：

 1. fd无效。

 2. 传入offset不是文件起始位置。

 3. size错误。

 4. 资源无效。

 5. 文件格式不支持。

#### OH_AVSource_Destroy()

```ets
OH_AVErrCode OH_AVSource_Destroy(OH_AVSource *source)
```

**描述**

销毁OH_AVSource实例并清理内部资源。

 同一实例只能被销毁一次。销毁的实例在被重新创建之前不能再被使用。建议实例销毁成功后将指针置为NULL。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**参数：**

参数项描述[OH_AVSource](OH_AVSource.md) *source指向OH_AVSource实例的指针。

**返回：**

类型说明[OH_AVErrCode](native_averrors.h.md#ZH-CN_TOPIC_0000002497605740__oh_averrcode)

AV_ERR_OK：操作成功。

 AV_ERR_INVALID_VAL：

 1. source指针无效，空指针。

 2. 非OH_AVSource实例。

#### OH_AVSource_GetSourceFormat()

```ets
OH_AVFormat *OH_AVSource_GetSourceFormat(OH_AVSource *source)
```

**描述**

获取媒体资源文件的基础信息。

 需要注意的是，指向的OH_AVFormat实例在生命周期结束时需调用者通过调用接口[OH_AVFormat_Destroy](native_avformat.h.md#ZH-CN_TOPIC_0000002497445762__oh_avformat_destroy)释放。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**参数：**

参数项描述[OH_AVSource](OH_AVSource.md) *source指向OH_AVSource实例的指针。

**返回：**

类型说明[OH_AVFormat](OH_AVFormat.md) *

执行成功返回文件的基础信息，否则返回NULL。

 可能的故障原因：

 1. source指针无效。

 2. 空指针或非OH_AVSource实例。

 3. source没有初始化。

#### OH_AVSource_GetTrackFormat()

```ets
OH_AVFormat *OH_AVSource_GetTrackFormat(OH_AVSource *source, uint32_t trackIndex)
```

**描述**

获取轨道的基础信息。

 需要注意的是，指向的OH_AVFormat实例在生命周期结束时需调用者通过调用接口[OH_AVFormat_Destroy](native_avformat.h.md#ZH-CN_TOPIC_0000002497445762__oh_avformat_destroy)释放。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**参数：**

参数项描述[OH_AVSource](OH_AVSource.md) *source指向OH_AVSource实例的指针。uint32_t trackIndex需要获取信息的轨道的索引。

**返回：**

类型说明[OH_AVFormat](OH_AVFormat.md) *

执行成功返回轨道的基础信息，否则返回NULL。

 可能的故障原因：

 1. source指针无效，空指针或非OH_AVSource实例。

 2. 轨道的索引超出范围。

 3. source没有初始化。

#### OH_AVSource_GetCustomMetadataFormat()

```ets
OH_AVFormat *OH_AVSource_GetCustomMetadataFormat(OH_AVSource *source)
```

**描述**

获取自定义元数据的基础信息。

 需要注意的是，指向的OH_AVFormat实例在生命周期结束时需开发者通过调用接口[OH_AVFormat_Destroy](native_avformat.h.md#ZH-CN_TOPIC_0000002497445762__oh_avformat_destroy)释放。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 18

**参数：**

参数项描述[OH_AVSource](OH_AVSource.md) *source指向OH_AVSource实例的指针。

**返回：**

类型说明[OH_AVFormat](OH_AVFormat.md) *

执行成功返回元数据的基础信息，否则返回NULL。

 可能的故障原因：

 1. source指针无效。

 2. 空指针或非OH_AVSource实例。

 3. source没有初始化。