# image_packer_native.h

**概述**

图片编码API。

引用文件： <multimedia/image_framework/image/image_packer_native.h>

库： libimage_packer.so

系统能力： SystemCapability.Multimedia.Image.ImagePacker

起始版本： 12

相关模块： [Image_NativeModule](Image_NativeModule.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_ImagePackerNative | OH_ImagePackerNative | ImagePacker结构体类型，用于执行ImagePacker相关操作。 |
| OH_PackingOptions | OH_PackingOptions | OH_PackingOptions是native层封装的图像编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。 |
| OH_PackingOptionsForSequence | OH_PackingOptionsForSequence | OH_PackingOptionsForSequence是native层封装的图像序列编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| IMAGE_PACKER_DYNAMIC_RANGE | IMAGE_PACKER_DYNAMIC_RANGE | 编码指定动态范围。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| Image_ErrorCode OH_PackingOptions_Create(OH_PackingOptions **options) | 创建PackingOptions结构体的指针。 |
| Image_ErrorCode OH_PackingOptions_GetMimeType(OH_PackingOptions *options, Image_MimeType *format) | 获取MIME类型。该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。 |
| Image_ErrorCode OH_PackingOptions_GetMimeTypeWithNull(OH_PackingOptions *options, Image_MimeType *format) | 获取编解码参数中的MIME类型。输出的format.data以字符串结束符'\0'结尾。 |
| Image_ErrorCode OH_PackingOptions_SetMimeType(OH_PackingOptions *options, Image_MimeType *format) | 设置MIME类型。 |
| Image_ErrorCode OH_PackingOptions_GetQuality(OH_PackingOptions *options, uint32_t *quality) | 获取编码质量。 |
| Image_ErrorCode OH_PackingOptions_SetQuality(OH_PackingOptions *options, uint32_t quality) | 设置编码质量。 |
| Image_ErrorCode OH_PackingOptions_GetNeedsPackProperties(OH_PackingOptions *options, bool *needsPackProperties) | 获取OH_PackingOptions结构体的needsPackProperties参数。 |
| Image_ErrorCode OH_PackingOptions_SetNeedsPackProperties(OH_PackingOptions *options, bool needsPackProperties) | 设置OH_PackingOptions结构体的needsPackProperties参数。 |
| Image_ErrorCode OH_PackingOptions_GetDesiredDynamicRange(OH_PackingOptions options, int32_t desiredDynamicRange) | 获取编码时期望的图片动态范围。 |
| Image_ErrorCode OH_PackingOptions_SetDesiredDynamicRange(OH_PackingOptions *options, int32_t desiredDynamicRange) | 设置编码时期望的图片动态范围。 |
| Image_ErrorCode OH_PackingOptions_Release(OH_PackingOptions *options) | 释放OH_PackingOptions指针。 |
| Image_ErrorCode OH_PackingOptionsForSequence_Create(OH_PackingOptionsForSequence **options) | 创建OH_PackingOptionsForSequence结构体的指针。 |
| Image_ErrorCode OH_PackingOptionsForSequence_SetFrameCount(OH_PackingOptionsForSequence *options, uint32_t frameCount) | 设置编码时指定的帧数。 |
| Image_ErrorCode OH_PackingOptionsForSequence_GetFrameCount(OH_PackingOptionsForSequence *options, uint32_t *frameCount) | 获取编码时指定的帧数。 |
| Image_ErrorCode OH_PackingOptionsForSequence_SetDelayTimeList(OH_PackingOptionsForSequence *options, int32_t *delayTimeList, size_t delayTimeListLength) | 设定编码时图片的延迟时间数组。 |
| Image_ErrorCode OH_PackingOptionsForSequence_GetDelayTimeList(OH_PackingOptionsForSequence *options, int32_t *delayTimeList, size_t delayTimeListLength) | 获取编码时图片的延迟时间数组。 |
| Image_ErrorCode OH_PackingOptionsForSequence_SetDisposalTypes(OH_PackingOptionsForSequence *options, uint32_t *disposalTypes, size_t disposalTypesLength) | 设定编码时图片的过渡帧模式数组。 |
| Image_ErrorCode OH_PackingOptionsForSequence_GetDisposalTypes(OH_PackingOptionsForSequence *options, uint32_t *disposalTypes, size_t disposalTypesLength) | 获取编码时图片的过渡帧模式数组。 |
| Image_ErrorCode OH_PackingOptionsForSequence_SetLoopCount(OH_PackingOptionsForSequence *options, uint32_t loopCount) | 设定编码时图片循环播放次数，取值范围为[0，65535]，0表示无限循环；若无此字段，则表示不循环播放。 |
| Image_ErrorCode OH_PackingOptionsForSequence_GetLoopCount(OH_PackingOptionsForSequence *options, uint32_t *loopCount) | 获取编码时图片循环播放次数。 |
| Image_ErrorCode OH_PackingOptionsForSequence_Release(OH_PackingOptionsForSequence *options) | 释放OH_PackingOptionsForSequence指针。 |
| Image_ErrorCode OH_ImagePackerNative_Create(OH_ImagePackerNative **imagePacker) | 创建OH_ImagePackerNative指针。 |
| Image_ErrorCode OH_ImagePackerNative_PackToDataFromImageSource(OH_ImagePackerNative *imagePacker, OH_PackingOptions *options, OH_ImageSourceNative *imageSource, uint8_t *outData, size_t *size) | 将ImageSource编码为指定格式的数据。 |
| Image_ErrorCode OH_ImagePackerNative_PackToDataFromPixelmap(OH_ImagePackerNative *imagePacker, OH_PackingOptions *options, OH_PixelmapNative *pixelmap, uint8_t *outData, size_t *size) | 将Pixelmap编码为指定格式的数据。 |
| Image_ErrorCode OH_ImagePackerNative_PackToDataFromPicture(OH_ImagePackerNative *imagePacker, OH_PackingOptions *options, OH_PictureNative *picture, uint8_t *outData, size_t *size) | 将Picture编码为指定格式的数据。 |
| Image_ErrorCode OH_ImagePackerNative_PackToDataFromPixelmapSequence(OH_ImagePackerNative *imagePacker, OH_PackingOptionsForSequence *options, OH_PixelmapNative **pixelmapSequence,size_t sequenceLength, uint8_t *outData, size_t *outDataSize) | 将Pixelmap序列编码为数据。 |
| Image_ErrorCode OH_ImagePackerNative_PackToFileFromImageSource(OH_ImagePackerNative *imagePacker, OH_PackingOptions *options, OH_ImageSourceNative *imageSource, int32_t fd) | 将一个ImageSource编码到文件中。 |
| Image_ErrorCode OH_ImagePackerNative_PackToFileFromPixelmap(OH_ImagePackerNative *imagePacker, OH_PackingOptions *options, OH_PixelmapNative *pixelmap, int32_t fd) | 将一个Pixelmap编码到文件中。 |
| Image_ErrorCode OH_ImagePackerNative_PackToFileFromPicture(OH_ImagePackerNative *imagePacker, OH_PackingOptions *options, OH_PictureNative *picture, int32_t fd) | 将一个Picture编码到文件中。 |
| Image_ErrorCode OH_ImagePackerNative_PackToFileFromPixelmapSequence(OH_ImagePackerNative *imagePacker, OH_PackingOptionsForSequence *options, OH_PixelmapNative **pixelmapSequence, size_t sequenceLength, int32_t fd) | 将一个Pixelmap序列编码到文件中。 |
| Image_ErrorCode OH_ImagePackerNative_GetSupportedFormats(Image_MimeType **supportedFormats, size_t *length) | 获取支持编码的图片格式。 |
| Image_ErrorCode OH_ImagePackerNative_Release(OH_ImagePackerNative *imagePacker) | 释放OH_ImagePackerNative指针。 |

**枚举类型说明**

**IMAGE_PACKER_DYNAMIC_RANGE**

```ets
enum IMAGE_PACKER_DYNAMIC_RANGE
```

描述

编码指定动态范围。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| IMAGE_PACKER_DYNAMIC_RANGE_AUTO = 0 | 编码动态范围根据图像信息自适应。 |
| IMAGE_PACKER_DYNAMIC_RANGE_SDR = 1 | 编码图片为标准动态范围。 |

**函数说明**

**OH_PackingOptions_Create()**

```ets
Image_ErrorCode OH_PackingOptions_Create(OH_PackingOptions **options)
```

描述

创建PackingOptions结构体的指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions **options | 用于操作的PackingOptions指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptions_GetMimeType()**

```ets
Image_ErrorCode OH_PackingOptions_GetMimeType(OH_PackingOptions *options,Image_MimeType *format)
```

描述

获取MIME类型。该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions *options | 被操作的OH_PackingOptions指针。 |
| Image_MimeType *format | 图像格式。可传入一个空指针和零大小，系统将分配内存，但必须在使用后释放内存。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptions_GetMimeTypeWithNull()**

```ets
Image_ErrorCode OH_PackingOptions_GetMimeTypeWithNull(OH_PackingOptions *options,Image_MimeType *format)
```

描述

获取编解码参数中的MIME类型。输出的format.data以字符串结束符'\0'结尾。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions *options | 编码参数指针。 |
| Image_MimeType *format | 编码参数中的 MIME 类型的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_PACKER_INVALID_PARAMETER：options或format为空。 |

**OH_PackingOptions_SetMimeType()**

```ets
Image_ErrorCode OH_PackingOptions_SetMimeType(OH_PackingOptions *options,Image_MimeType *format)
```

描述

设置MIME类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions *options | 被操作的OH_PackingOptions指针。 |
| Image_MimeType *format | 图像格式。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptions_GetQuality()**

```ets
Image_ErrorCode OH_PackingOptions_GetQuality(OH_PackingOptions *options,uint32_t *quality)
```

描述

获取编码质量。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions *options | 被操作的OH_PackingOptions指针。 |
| uint32_t *quality | 编码质量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptions_SetQuality()**

```ets
Image_ErrorCode OH_PackingOptions_SetQuality(OH_PackingOptions *options,uint32_t quality)
```

描述

设置编码质量。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions *options | 被操作的OH_PackingOptions指针。 |
| uint32_t quality | 编码质量。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptions_GetNeedsPackProperties()**

```ets
 Image_ErrorCode OH_PackingOptions_GetNeedsPackProperties(OH_PackingOptions *options,bool *needsPackProperties)
```

描述

获取OH_PackingOptions结构体的needsPackProperties参数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions *options | 被操作的OH_PackingOptions指针。 |
| bool *needsPackProperties | 是否需要编码图片属性信息（例如Exif）。true表示需要，false表示不需要。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptions_SetNeedsPackProperties()**

```ets
Image_ErrorCode OH_PackingOptions_SetNeedsPackProperties(OH_PackingOptions *options,bool needsPackProperties)
```

描述

设置OH_PackingOptions结构体的needsPackProperties参数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions *options | 被操作的OH_PackingOptions指针。 |
| bool needsPackProperties | 是否需要编码图片属性信息（例如Exif）。true表示需要，false表示不需要。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptions_GetDesiredDynamicRange()**

```ets
Image_ErrorCode OH_PackingOptions_GetDesiredDynamicRange(OH_PackingOptions *options, int32_t* desiredDynamicRange)
```

描述

获取编码时期望的图片动态范围。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions *options | 被操作的OH_PackingOptions指针。 |
| int32_t* desiredDynamicRange | 期望的动态范围[IMAGE_PACKER_DYNAMIC_RANGE]#image_packer_dynamic_range)。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptions_SetDesiredDynamicRange()**

```ets
Image_ErrorCode OH_PackingOptions_SetDesiredDynamicRange(OH_PackingOptions *options, int32_t desiredDynamicRange)
```

描述

设置编码时期望的图片动态范围。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions *options | 被操作的OH_PackingOptions指针。 |
| int32_t desiredDynamicRange | 期望的动态范围[IMAGE_PACKER_DYNAMIC_RANGE]#image_packer_dynamic_range)。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptions_Release()**

```ets
Image_ErrorCode OH_PackingOptions_Release(OH_PackingOptions *options)
```

描述

释放OH_PackingOptions指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptions *options | 被操作的OH_PackingOptions指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptionsForSequence_Create()**

```ets
Image_ErrorCode OH_PackingOptionsForSequence_Create(OH_PackingOptionsForSequence **options)
```

描述

创建OH_PackingOptionsForSequence结构体的指针。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptionsForSequence **options | 用于操作的OH_PackingOptionsForSequence指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptionsForSequence_SetFrameCount()**

```ets
Image_ErrorCode OH_PackingOptionsForSequence_SetFrameCount(OH_PackingOptionsForSequence *options,uint32_t frameCount)
```

描述

设置编码时指定的帧数。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptionsForSequence *options | 用于操作的OH_PackingOptionsForSequence指针。 |
| uint32_t frameCount | 图片的帧数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptionsForSequence_GetFrameCount()**

```ets
Image_ErrorCode OH_PackingOptionsForSequence_GetFrameCount(OH_PackingOptionsForSequence *options,uint32_t *frameCount)
```

描述

获取编码时指定的帧数。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptionsForSequence *options | 用于操作的OH_PackingOptionsForSequence指针。 |
| uint32_t *frameCount | 图片的帧数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptionsForSequence_SetDelayTimeList()**

```ets
Image_ErrorCode OH_PackingOptionsForSequence_SetDelayTimeList(OH_PackingOptionsForSequence *options,int32_t *delayTimeList, size_t delayTimeListLength)
```

描述

设定编码时图片的延迟时间数组。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptionsForSequence *options | 用于操作的OH_PackingOptionsForSequence指针。 |
| int32_t *delayTimeList | 图片延迟时间数组的指针。 |
| size_t delayTimeListLength | 图片延迟时间数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptionsForSequence_GetDelayTimeList()**

```ets
Image_ErrorCode OH_PackingOptionsForSequence_GetDelayTimeList(OH_PackingOptionsForSequence *options,int32_t *delayTimeList, size_t delayTimeListLength)
```

描述

获取编码时图片的延迟时间数组。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptionsForSequence *options | 用于操作的OH_PackingOptionsForSequence指针。 |
| int32_t *delayTimeList | 图片延迟时间数组的指针。 |
| size_t delayTimeListLength | 图片延迟时间数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptionsForSequence_SetDisposalTypes()**

```ets
Image_ErrorCode OH_PackingOptionsForSequence_SetDisposalTypes(OH_PackingOptionsForSequence *options,uint32_t *disposalTypes, size_t disposalTypesLength)
```

描述

设定编码时图片的过渡帧模式数组。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptionsForSequence *options | 用于操作的OH_PackingOptionsForSequence指针。 |
| uint32_t *disposalTypes | 图片过渡帧模式数组的指针，图片帧过渡模式的参数，如果长度小于frameCount，不足的部分将使用disposalTypes中的最后一个值进行填充，可取值如下： 0：不需要任何操作。 1：保持图形不变。 2：恢复背景色。 3：恢复到之前的状态。 |
| size_t disposalTypesLength | 图片过渡帧模式数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptionsForSequence_GetDisposalTypes()**

```ets
Image_ErrorCode OH_PackingOptionsForSequence_GetDisposalTypes(OH_PackingOptionsForSequence *options,uint32_t *disposalTypes, size_t disposalTypesLength)
```

描述

获取编码时图片的过渡帧模式数组。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptionsForSequence *options | 用于操作的OH_PackingOptionsForSequence指针。 |
| uint32_t *disposalTypes | 图片过渡帧模式数组的指针。 |
| size_t disposalTypesLength | 图片过渡帧模式数组的长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptionsForSequence_SetLoopCount()**

```ets
Image_ErrorCode OH_PackingOptionsForSequence_SetLoopCount(OH_PackingOptionsForSequence *options, uint32_t loopCount)
```

描述

设定编码时图片循环播放次数，取值范围为[0，65535]，0表示无限循环；若无此字段，则表示不循环播放。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptionsForSequence *options | 用于操作的OH_PackingOptionsForSequence指针。 |
| uint32_t loopCount | 图片循环播放次数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptionsForSequence_GetLoopCount()**

```ets
Image_ErrorCode OH_PackingOptionsForSequence_GetLoopCount(OH_PackingOptionsForSequence *options, uint32_t *loopCount)
```

描述

获取编码时图片循环播放次数。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptionsForSequence *options | 用于操作的OH_PackingOptionsForSequence指针。 |
| uint32_t *loopCount | 图片循环播放次数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PackingOptionsForSequence_Release()**

```ets
Image_ErrorCode OH_PackingOptionsForSequence_Release(OH_PackingOptionsForSequence *options)
```

描述

释放OH_PackingOptionsForSequence指针。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PackingOptionsForSequence *options | 用于操作的OH_PackingOptionsForSequence指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImagePackerNative_Create()**

```ets
Image_ErrorCode OH_ImagePackerNative_Create(OH_ImagePackerNative **imagePacker)
```

描述

创建OH_ImagePackerNative指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImagePackerNative **imagePacker | 被操作的OH_ImagePackerNative指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImagePackerNative_PackToDataFromImageSource()**

```ets
Image_ErrorCode OH_ImagePackerNative_PackToDataFromImageSource(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_ImageSourceNative *imageSource, uint8_t *outData, size_t *size)
```

描述

将ImageSource编码为指定格式的数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImagePackerNative *imagePacker | 被操作的OH_ImagePackerNative指针。 |
| OH_PackingOptions *options | 编码选项参数。 |
| OH_ImageSourceNative *imageSource | 用于编码的image source指针。 |
| uint8_t *outData | 用于存储打包图像输出数据的缓冲区。 |
| size_t *size | 用于存储打包图像输出数据的缓冲区大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 IMAGE_DECODE_FAILED：解码失败。 IMAGE_ALLOC_FAILED：申请内存失败。  IMAGE_TOO_LARGE：数据或图片过大。 IMAGE_UNKNOWN_ERROR：未知错误。 |

**OH_ImagePackerNative_PackToDataFromPixelmap()**

```ets
Image_ErrorCode OH_ImagePackerNative_PackToDataFromPixelmap(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PixelmapNative *pixelmap, uint8_t *outData, size_t *size)
```

描述

将Pixelmap编码为指定格式的数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImagePackerNative *imagePacker | 被操作的OH_ImagePackerNative指针。 |
| OH_PackingOptions *options | 编码选项参数。 |
| OH_PixelmapNative *pixelmap | 用于编码的Pixelmap指针。 |
| uint8_t *outData | 用于存储打包图像输出数据的缓冲区。 |
| size_t *size | 用于存储打包图像输出数据的缓冲区大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 IMAGE_DECODE_FAILED：解码失败。 IMAGE_ALLOC_FAILED：申请内存失败。  IMAGE_TOO_LARGE：数据或图片过大。 IMAGE_UNKNOWN_ERROR：未知错误。 |

**OH_ImagePackerNative_PackToDataFromPicture()**

```ets
Image_ErrorCode OH_ImagePackerNative_PackToDataFromPicture(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PictureNative *picture, uint8_t *outData, size_t *size)
```

描述

将Picture编码为指定格式的数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImagePackerNative *imagePacker | 被操作的OH_ImagePackerNative指针。 |
| OH_PackingOptions *options | 编码选项参数。 |
| OH_PictureNative *picture | 用于编码的Picture指针。 |
| uint8_t *outData | 用于存储打包图像输出数据的缓冲区。 |
| size_t *size | 用于存储打包图像输出数据的缓冲区大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 IMAGE_DECODE_FAILED：解码失败。 |

**OH_ImagePackerNative_PackToDataFromPixelmapSequence()**

```ets
Image_ErrorCode OH_ImagePackerNative_PackToDataFromPixelmapSequence(OH_ImagePackerNative *imagePacker,OH_PackingOptionsForSequence *options, OH_PixelmapNative **pixelmapSequence,size_t sequenceLength, uint8_t *outData, size_t *outDataSize)
```

描述

将Pixelmap序列编码为数据。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImagePackerNative *imagePacker | 被操作的OH_ImagePackerNative指针。 |
| OH_PackingOptionsForSequence *options | 编码选项参数 OH_PackingOptionsForSequence。 |
| OH_PixelmapNative **pixelmapSequence | 用于编码的Pixelmap序列指针。 |
| size_t sequenceLength | 用于编码的Pixelmap序列长度。 |
| uint8_t *outData | 用于存储编码后图像输出数据的缓冲区。 |
| size_t *outDataSize | 用于存储编码后图像输出数据的缓冲区大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 IMAGE_DECODE_FAILED：解码失败。 |

**OH_ImagePackerNative_PackToFileFromImageSource()**

```ets
Image_ErrorCode OH_ImagePackerNative_PackToFileFromImageSource(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_ImageSourceNative *imageSource, int32_t fd)
```

描述

将一个ImageSource编码到文件中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImagePackerNative *imagePacker | 被操作的OH_ImagePackerNative指针。 |
| OH_PackingOptions *options | 编码选项参数。 |
| OH_ImageSourceNative *imageSource | 用于编码的image source指针。 |
| int32_t fd | 可写的文件描述符。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 IMAGE_DECODE_FAILED：解码失败。 IMAGE_UNKNOWN_ERROR：未知错误。 |

**OH_ImagePackerNative_PackToFileFromPixelmap()**

```ets
Image_ErrorCode OH_ImagePackerNative_PackToFileFromPixelmap(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PixelmapNative *pixelmap, int32_t fd)
```

描述

将一个Pixelmap编码到文件中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImagePackerNative *imagePacker | 被操作的OH_ImagePackerNative指针。 |
| OH_PackingOptions *options | 编码选项参数。 |
| OH_PixelmapNative *pixelmap | 用于编码的pixelmap指针。 |
| int32_t fd | 可写的文件描述符。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 IMAGE_DECODE_FAILED：解码失败。 IMAGE_UNKNOWN_ERROR：未知错误。 |

**OH_ImagePackerNative_PackToFileFromPicture()**

```ets
Image_ErrorCode OH_ImagePackerNative_PackToFileFromPicture(OH_ImagePackerNative *imagePacker,OH_PackingOptions *options, OH_PictureNative *picture, int32_t fd)
```

描述

将一个Picture编码到文件中。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImagePackerNative *imagePacker | 被操作的OH_ImagePackerNative指针。 |
| OH_PackingOptions *options | 编码选项参数。 |
| OH_PictureNative *picture | 用于编码的picture指针。 |
| int32_t fd | 可写的文件描述符。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 IMAGE_DECODE_FAILED：解码失败。 IMAGE_UNKNOWN_ERROR：未知错误。 |

**OH_ImagePackerNative_PackToFileFromPixelmapSequence()**

```ets
Image_ErrorCode OH_ImagePackerNative_PackToFileFromPixelmapSequence(OH_ImagePackerNative *imagePacker,OH_PackingOptionsForSequence *options, OH_PixelmapNative **pixelmapSequence, size_t sequenceLength, int32_t fd)
```

描述

将一个Pixelmap序列编码到文件中。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImagePackerNative *imagePacker | 被操作的OH_ImagePackerNative指针。 |
| OH_PackingOptionsForSequence *options | 编码选项参数 OH_PackingOptionsForSequence。 |
| OH_PixelmapNative **pixelmapSequence | 用于编码的Pixelmap序列指针。 |
| size_t sequenceLength | 用于编码的Pixelmap序列长度。 |
| int32_t fd | 可写的文件描述符。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 IMAGE_DECODE_FAILED：解码失败。 |

**OH_ImagePackerNative_GetSupportedFormats()**

```ets
Image_ErrorCode OH_ImagePackerNative_GetSupportedFormats(Image_MimeType **supportedFormats, size_t *length)
```

描述

获取支持编码的图片格式。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| Image_MimeType **supportedFormats | 支持编码的图片格式。 |
| size_t *length | 数组长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_PACKER_INVALID_PARAMETER：参数异常，supportedFormats或length为空。 |

**OH_ImagePackerNative_Release()**

```ets
Image_ErrorCode OH_ImagePackerNative_Release(OH_ImagePackerNative *imagePacker)
```

描述

释放OH_ImagePackerNative指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImagePackerNative *imagePacker | 被操作的OH_ImagePackerNative指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |