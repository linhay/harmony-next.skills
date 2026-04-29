# image_source_native.h

**概述**

图片解码API。

引用文件： <multimedia/image_framework/image/image_source_native.h>

库： libimage_source.so

系统能力： SystemCapability.Multimedia.Image.ImageSource

起始版本： 12

相关模块： [Image_NativeModule](Image_NativeModule.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_ImageSourceNative | OH_ImageSourceNative | OH_ImageSourceNative是native层封装的ImageSource结构体，用于创建图片数据。 |
| OH_ImageSource_Info | OH_ImageSource_Info | OH_ImageSource_Info是native层封装的ImageSource信息结构体，OH_ImageSource_Info结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。 |
| OH_DecodingOptionsForPicture | OH_DecodingOptionsForPicture | Picture解码参数结构体。通过OH_DecodingOptionsForPicture_Create获取。 |
| OH_DecodingOptions | OH_DecodingOptions | OH_DecodingOptions是native层封装的解码选项参数结构体，用于设置解码选项参数，在创建Pixelmap时作为入参传入，详细信息见OH_ImageSourceNative_CreatePixelmap。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| IMAGE_DYNAMIC_RANGE | IMAGE_DYNAMIC_RANGE | 解码指定期望动态范围。 |
| IMAGE_ALLOCATOR_TYPE | IMAGE_ALLOCATOR_TYPE | 用于分配PixelMap内存的分配器类型。 |
| Image_CropAndScaleStrategy | Image_CropAndScaleStrategy | 在同时指定desiredSize和desiredRegion时执行裁剪和缩放的策略。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| Image_ErrorCode OH_ImageSourceInfo_Create(OH_ImageSource_Info **info) | 创建OH_ImageSource_Info指针。 |
| Image_ErrorCode OH_ImageSourceInfo_GetWidth(OH_ImageSource_Info *info, uint32_t *width) | 获取图片的宽。对于没有width标签的SVG图片，返回默认值0。 |
| Image_ErrorCode OH_ImageSourceInfo_GetHeight(OH_ImageSource_Info *info, uint32_t *height) | 获取图片的高。对于没有height标签的SVG图片，返回默认值0。 |
| Image_ErrorCode OH_ImageSourceInfo_GetDynamicRange(OH_ImageSource_Info *info, bool *isHdr) | 获取图片是否为高动态范围的信息。 |
| Image_ErrorCode OH_ImageSourceInfo_GetMimetype(OH_ImageSource_Info *info, Image_MimeType *mimeType) | 获取图片源的MIME类型。 |
| Image_ErrorCode OH_ImageSourceInfo_Release(OH_ImageSource_Info *info) | 释放OH_ImageSource_Info指针。调用该接口之后，与OH_ImageSourceInfo结构体相关的属性均会被释放。因此在调用该接口前，请务必确认相关属性已不再被需要或对相关属性已完成深拷贝操作。 |
| Image_ErrorCode OH_DecodingOptions_Create(OH_DecodingOptions **options) | 创建OH_DecodingOptions指针。 |
| Image_ErrorCode OH_DecodingOptions_GetPixelFormat(OH_DecodingOptions *options, int32_t *pixelFormat) | 获取pixel格式。 |
| Image_ErrorCode OH_DecodingOptions_SetPixelFormat(OH_DecodingOptions *options, int32_t pixelFormat) | 设置pixel格式。 |
| Image_ErrorCode OH_DecodingOptions_GetIndex(OH_DecodingOptions *options, uint32_t *index) | 获取解码图片序号。 |
| Image_ErrorCode OH_DecodingOptions_SetIndex(OH_DecodingOptions *options, uint32_t index) | 设置解码图片序号。 |
| Image_ErrorCode OH_DecodingOptions_GetRotate(OH_DecodingOptions *options, float *rotate) | 获取旋转角度。 |
| Image_ErrorCode OH_DecodingOptions_SetRotate(OH_DecodingOptions *options, float rotate) | 设置旋转角度。 |
| Image_ErrorCode OH_DecodingOptions_GetDesiredSize(OH_DecodingOptions *options, Image_Size *desiredSize) | 获取期望输出大小。 |
| Image_ErrorCode OH_DecodingOptions_SetDesiredSize(OH_DecodingOptions *options, Image_Size *desiredSize) | 设置期望输出大小。 |
| Image_ErrorCode OH_DecodingOptions_GetDesiredRegion(OH_DecodingOptions *options, Image_Region *desiredRegion) | 获取解码区域。  由于对应SetDesiredRegion接口无法满足区域解码诉求，从API version 19开始，推荐配套使用OH_DecodingOptions_GetCropRegion接口替代。 |
| Image_ErrorCode OH_DecodingOptions_SetDesiredRegion(OH_DecodingOptions *options, Image_Region *desiredRegion) | 设置解码区域。  实际解码结果会按照原图解码，无区域解码效果。从API version 19开始，推荐使用接口OH_DecodingOptions_SetCropRegion替代。 |
| Image_ErrorCode OH_DecodingOptions_GetDesiredDynamicRange(OH_DecodingOptions *options, int32_t *desiredDynamicRange) | 获取解码时设置的期望动态范围。 |
| Image_ErrorCode OH_DecodingOptions_SetDesiredDynamicRange(OH_DecodingOptions *options, int32_t desiredDynamicRange) | 设置解码时的期望动态范围。 |
| Image_ErrorCode OH_DecodingOptions_GetDesiredColorSpace(OH_DecodingOptions *options, int32_t *colorSpace) | 获取解码参数中设置的色彩空间。 |
| Image_ErrorCode OH_DecodingOptions_SetDesiredColorSpace(OH_DecodingOptions *options, int32_t colorSpace) | 设置解码期望得到的色彩空间。 |
| Image_ErrorCode OH_DecodingOptions_SetCropAndScaleStrategy(OH_DecodingOptions *options, int32_t cropAndScaleStrategy) | 设置解码选项的裁剪和缩放策略。 |
| Image_ErrorCode OH_DecodingOptions_GetCropAndScaleStrategy(OH_DecodingOptions *options, int32_t *cropAndScaleStrategy) | 获取解码选项的裁剪和缩放策略。 |
| Image_ErrorCode OH_DecodingOptions_GetCropRegion(OH_DecodingOptions *options, Image_Region *cropRegion) | 获取解码参数中的裁剪区域。 |
| Image_ErrorCode OH_DecodingOptions_SetCropRegion(OH_DecodingOptions *options, Image_Region *cropRegion) | 设置解码参数中的裁剪区域。 |
| Image_ErrorCode OH_DecodingOptions_Release(OH_DecodingOptions *options) | 释放OH_DecodingOptions指针。 |
| Image_ErrorCode OH_ImageSourceNative_CreateFromUri(char *uri, size_t uriSize, OH_ImageSourceNative **res) | 通过uri创建OH_ImageSourceNative指针。 |
| Image_ErrorCode OH_ImageSourceNative_CreateFromFd(int32_t fd, OH_ImageSourceNative **res) | 通过fd创建OH_ImageSourceNative指针。 |
| Image_ErrorCode OH_ImageSourceNative_CreateFromData(uint8_t *data, size_t dataSize, OH_ImageSourceNative **res) | 通过缓冲区数据创建OH_ImageSourceNative指针。  data数据应该是未解码的数据，不要传入类似于RGBA，YUV的像素buffer数据，如果想通过像素buffer数据创建pixelMap，可以调用OH_PixelmapNative_CreatePixelmap这一类接口。 |
| Image_ErrorCode OH_ImageSourceNative_CreateFromDataWithUserBuffer(uint8_t *data, size_t datalength, OH_ImageSourceNative **imageSource) | 由数据缓存创建图片源。传入的数据缓存将在图片源对象中直接访问，在图片源对象的生命周期内，数据缓存需要保持可用。 |
| Image_ErrorCode OH_ImageSourceNative_CreateFromRawFile(RawFileDescriptor *rawFile, OH_ImageSourceNative **res) | 通过图像资源文件的RawFileDescriptor创建OH_ImageSourceNative指针。 |
| Image_ErrorCode OH_ImageSourceNative_CreatePixelmap(OH_ImageSourceNative *source, OH_DecodingOptions *options, OH_PixelmapNative **pixelmap) | 通过图片解码参数创建OH_PixelmapNative指针。 |
| Image_ErrorCode OH_ImageSourceNative_CreatePixelmapUsingAllocator(OH_ImageSourceNative *source, OH_DecodingOptions *options, IMAGE_ALLOCATOR_TYPE allocator, OH_PixelmapNative **pixelmap) | 根据解码参数创建一个PixelMap，PixelMap使用的内存类型可以通过allocatorType来指定。  默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理通过此接口返回的PixelMap时，请始终考虑步幅（stride）的影响。 |
| Image_ErrorCode OH_ImageSourceNative_CreatePixelmapList(OH_ImageSourceNative *source, OH_DecodingOptions *options, OH_PixelmapNative *resVecPixMap[], size_t size) | 通过图片解码参数创建OH_PixelmapNative数组。  注意，此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。 |
| Image_ErrorCode OH_ImageSourceNative_CreatePicture(OH_ImageSourceNative *source, OH_DecodingOptionsForPicture *options, OH_PictureNative **picture) | 通过图片解码创建OH_PictureNative指针。 |
| Image_ErrorCode OH_ImageSourceNative_CreatePictureAtIndex(OH_ImageSourceNative *source, uint32_t index, OH_PictureNative **picture) | 通过指定序号的图片解码创建OH_PictureNative指针。 |
| Image_ErrorCode OH_ImageSourceNative_GetDelayTimeList(OH_ImageSourceNative *source, int32_t *delayTimeList, size_t size) | 获取图像延迟时间数组。 |
| Image_ErrorCode OH_ImageSourceNative_GetImageInfo(OH_ImageSourceNative *source, int32_t index, OH_ImageSource_Info *info) | 获取指定序号的图片信息。 |
| Image_ErrorCode OH_ImageSourceNative_GetImageProperty(OH_ImageSourceNative *source, Image_String *key, Image_String *value) | 获取图片指定属性键的值。该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。 |
| Image_ErrorCode OH_ImageSourceNative_GetImagePropertyShort(OH_ImageSourceNative *source, Image_String *key, uint16_t *value) | 以短整型类型获取图像属性的值。 |
| Image_ErrorCode OH_ImageSourceNative_GetImagePropertyLong(OH_ImageSourceNative *source, Image_String *key, uint32_t *value) | 以长整型类型获取图像属性的值。 |
| Image_ErrorCode OH_ImageSourceNative_GetImagePropertyDouble(OH_ImageSourceNative *source, Image_String *key, double *value) | 以浮点型类型获取图像属性的值。 |
| Image_ErrorCode OH_ImageSourceNative_GetImagePropertyArraySize(OH_ImageSourceNative *source, Image_String *key, size_t *size) | 获取数组类型属性的数组长度或字符串类型属性的字符串长度。 |
| Image_ErrorCode OH_ImageSourceNative_GetImagePropertyString(OH_ImageSourceNative *source, Image_String *key, char *value, size_t size) | 以字符串类型获取图像属性的值。 |
| Image_ErrorCode OH_ImageSourceNative_GetImagePropertyIntArray(OH_ImageSourceNative *source, Image_String *key, int32_t *value, size_t size) | 以整型数组类型获取图像属性的值。 |
| Image_ErrorCode OH_ImageSourceNative_GetImagePropertyDoubleArray(OH_ImageSourceNative *source, Image_String *key, double *value, size_t size) | 以浮点型数组类型获取图像属性的值。 |
| Image_ErrorCode OH_ImageSourceNative_GetImagePropertyBlob(OH_ImageSourceNative *source, Image_String *key, void *value, size_t size) | 以二进制对象类型获取图像属性的值。 |
| Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyShort(OH_ImageSourceNative *source, Image_String *key, uint16_t value) | 修改图像属性中短整型的值。 |
| Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyLong(OH_ImageSourceNative *source, Image_String *key, uint32_t value) | 修改图像属性中长整型的值。 |
| Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyDouble(OH_ImageSourceNative *source, Image_String *key, double value) | 修改图像属性中浮点型的值。 |
| Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyIntArray(OH_ImageSourceNative *source, Image_String *key, int32_t *value, size_t size) | 修改图像属性中整型数组型的值。 |
| Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyDoubleArray(OH_ImageSourceNative *source, Image_String *key, double *value, size_t size) | 修改图像属性中浮点型数组型的值。 |
| Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyBlob(OH_ImageSourceNative *source, Image_String *key, void *value, size_t size) | 修改图像属性中二进制对象的值。 |
| Image_ErrorCode OH_ImageSourceNative_GetImagePropertyWithNull(OH_ImageSourceNative *source, Image_String *key, Image_String *value) | 获取图像属性值。输出的value.data以字符串结束符'\0'结尾。 |
| Image_ErrorCode OH_ImageSourceNative_ModifyImageProperty(OH_ImageSourceNative *source, Image_String *key, Image_String *value) | 通过指定的键修改图片属性的值。 |
| Image_ErrorCode OH_ImageSourceNative_GetFrameCount(OH_ImageSourceNative *source, uint32_t *frameCount) | 获取图像帧数。 |
| Image_ErrorCode OH_ImageSourceNative_GetSupportedFormats(Image_MimeType **supportedFormats, size_t *length) | 获取支持解码的图片格式。 |
| Image_ErrorCode OH_ImageSourceNative_Release(OH_ImageSourceNative *source) | 释放OH_ImageSourceNative指针。 |
| Image_ErrorCode OH_DecodingOptionsForPicture_Create(OH_DecodingOptionsForPicture **options) | 创建OH_DecodingOptionsForPicture指针。 |
| Image_ErrorCode OH_DecodingOptionsForPicture_GetDesiredAuxiliaryPictures(OH_DecodingOptionsForPicture *options, Image_AuxiliaryPictureType **desiredAuxiliaryPictures, size_t *length) | 获取解码时设置的期望辅助图（期望解码出的picture包含的辅助图）。 |
| Image_ErrorCode OH_DecodingOptionsForPicture_SetDesiredAuxiliaryPictures(OH_DecodingOptionsForPicture *options, Image_AuxiliaryPictureType *desiredAuxiliaryPictures, size_t length) | 设置解码选项中的期望辅助图。 |
| Image_ErrorCode OH_DecodingOptionsForPicture_Release(OH_DecodingOptionsForPicture *options) | 释放OH_DecodingOptionsForPicture指针。 |

**枚举类型说明**

**IMAGE_DYNAMIC_RANGE**

```ets
enum IMAGE_DYNAMIC_RANGE
```

描述

解码指定期望动态范围。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| IMAGE_DYNAMIC_RANGE_AUTO = 0 | 根据图片自适应处理。 |
| IMAGE_DYNAMIC_RANGE_SDR = 1 | 标准动态范围。 |
| IMAGE_DYNAMIC_RANGE_HDR = 2 | 高动态范围。 |

**IMAGE_ALLOCATOR_TYPE**

```ets
enum IMAGE_ALLOCATOR_TYPE
```

描述

用于分配PixelMap内存的分配器类型。

起始版本： 15

| 枚举项 | 描述 |
| --- | --- |
| IMAGE_ALLOCATOR_TYPE_AUTO = 0 | 由系统决定使用DMA内存或共享内存来创建PixelMap。 |
| IMAGE_ALLOCATOR_TYPE_DMA = 1 | 使用DMA内存来创建PixelMap。 |
| IMAGE_ALLOCATOR_TYPE_SHARE_MEMORY = 2 | 使用共享内存来创建PixelMap。 |

**Image_CropAndScaleStrategy**

```ets
enum Image_CropAndScaleStrategy
```

描述

在同时指定desiredSize和desiredRegion时执行裁剪和缩放的策略。

 如果在配置解码选项[OH_DecodingOptions](OH_DecodingOptions.md)时，未填入参数Image_CropAndScaleStrategy，并且同时设置了desiredRegion和desiredSize，由于系统对于不同图片格式采用的解码算法不同，最终解码效果将略有差异。

 例如原始图片大小200x200，传入desiredSize:{width: 150, height: 150}，desiredRegion:{x: 0, y: 0, width: 100, height: 100}，即预期解码原图左上角1/4区域，最终将pixelMap大小缩放至150x150返回。

 对于jpeg、webp图片（部分dng图片解码时会优先解码图片中的jpeg预览图，在此场景下也会被视为jpeg图片格式）会先进行下采样，例如按照7/8下采样，再基于175x175的图片大小进行区域裁剪，因此最终的区域内容稍大于原图的左上角1/4区域。

 对于svg图片，由于是矢量图，可以任意缩放不损失清晰度，在解码时会根据desiredSize与原图Size的比例选择缩放比例，在基于缩放后的图片大小进行区域裁剪，因此最终返回的解码区域会有所差异。

 针对该场景，建议在解码选项同时设置了desiredRegion与desiredSize时，参数Image_CropAndScaleStrategy应传入CROP_FIRST参数保证效果一致。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| IMAGE_CROP_AND_SCALE_STRATEGY_SCALE_FIRST = 1 | 先裁剪，后缩放。 |
| IMAGE_CROP_AND_SCALE_STRATEGY_CROP_FIRST = 2 | 先缩放，后裁剪。 |

**函数说明**

**OH_ImageSourceInfo_Create()**

```ets
Image_ErrorCode OH_ImageSourceInfo_Create(OH_ImageSource_Info **info)
```

描述

创建OH_ImageSource_Info指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSource_Info **info | 被操作的OH_ImageSource_Info指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceInfo_GetWidth()**

```ets
Image_ErrorCode OH_ImageSourceInfo_GetWidth(OH_ImageSource_Info *info, uint32_t *width)
```

描述

获取图片的宽。对于没有width标签的SVG图片，返回默认值0。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSource_Info *info | 被操作的OH_ImageSource_Info指针。 |
| uint32_t *width | 图片的宽，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceInfo_GetHeight()**

```ets
Image_ErrorCode OH_ImageSourceInfo_GetHeight(OH_ImageSource_Info *info, uint32_t *height)
```

描述

获取图片的高。对于没有height标签的SVG图片，返回默认值0。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSource_Info *info | 被操作的OH_ImageSource_Info指针。 |
| uint32_t *height | 图片的高，单位：像素高 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceInfo_GetDynamicRange()**

```ets
Image_ErrorCode OH_ImageSourceInfo_GetDynamicRange(OH_ImageSource_Info *info, bool *isHdr)
```

描述

获取图片是否为高动态范围的信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSource_Info *info | 被操作的OH_ImageSource_Info指针。 |
| bool *isHdr | 表示是否为高动态范围（HDR）的信息。true表示是高动态范围的信息，false表示不是高动态范围的信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数校验错误。 |

**OH_ImageSourceInfo_GetMimetype()**

```ets
Image_ErrorCode OH_ImageSourceInfo_GetMimetype(OH_ImageSource_Info *info, Image_MimeType *mimeType)
```

描述

获取图片源的MIME类型。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

- [mimeType结构体的成员变量](Image_String.md#ZH-CN_TOPIC_0000002522082002__成员变量)data为char *类型指针，其指向info结构体内部持有的mimeType地址，释放info会导致该地址对应的内存也被释放。

- 开发者可以自行深拷贝一份mimeType.data，或者等mimeType使用完成后再释放info，以免出现乱码现象。

- mimeType.data没有以'\0'结尾，需要配合mimeType.size一起使用。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSource_Info *info | OH_ImageSource_Info指针。 |
| Image_MimeType *mimeType | 图片源的MIME类型。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：参数错误，INFO或者MIME类型为空。 |

**OH_ImageSourceInfo_Release()**

```ets
Image_ErrorCode OH_ImageSourceInfo_Release(OH_ImageSource_Info *info)
```

描述

释放OH_ImageSource_Info指针。调用该接口之后，与OH_ImageSourceInfo结构体相关的属性均会被释放。因此在调用该接口前，请务必确认相关属性已不再被需要或对相关属性已完成深拷贝操作。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSource_Info *info | 被操作的OH_ImageSource_Info指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_Create()**

```ets
Image_ErrorCode OH_DecodingOptions_Create(OH_DecodingOptions **options)
```

描述

创建OH_DecodingOptions指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions **options | 被操作的OH_DecodingOptions指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_GetPixelFormat()**

```ets
Image_ErrorCode OH_DecodingOptions_GetPixelFormat(OH_DecodingOptions *options, int32_t *pixelFormat)
```

描述

获取pixel格式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| int32_t *pixelFormat | pixel格式PIXEL_FORMAT，默认值为RGBA_8888。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_SetPixelFormat()**

```ets
Image_ErrorCode OH_DecodingOptions_SetPixelFormat(OH_DecodingOptions *options,int32_t pixelFormat)
```

描述

设置pixel格式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| int32_t pixelFormat | pixel格式PIXEL_FORMAT，默认值为RGBA_8888。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_GetIndex()**

```ets
Image_ErrorCode OH_DecodingOptions_GetIndex(OH_DecodingOptions *options, uint32_t *index)
```

描述

获取解码图片序号。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| uint32_t *index | 解码图片序号，默认值为0。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_SetIndex()**

```ets
Image_ErrorCode OH_DecodingOptions_SetIndex(OH_DecodingOptions *options, uint32_t index)
```

描述

设置解码图片序号。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| uint32_t index | 解码图片序号，默认值为0。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_GetRotate()**

```ets
Image_ErrorCode OH_DecodingOptions_GetRotate(OH_DecodingOptions *options, float *rotate)
```

描述

获取旋转角度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| float *rotate | 旋转角度，单位为deg，默认值为0。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_SetRotate()**

```ets
Image_ErrorCode OH_DecodingOptions_SetRotate(OH_DecodingOptions *options, float rotate)
```

描述

设置旋转角度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| float rotate | 旋转角度，单位为deg，默认值为0。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_GetDesiredSize()**

```ets
Image_ErrorCode OH_DecodingOptions_GetDesiredSize(OH_DecodingOptions *options, Image_Size *desiredSize)
```

描述

获取期望输出大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| Image_Size *desiredSize | 期望输出大小，默认为原始图片尺寸。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_SetDesiredSize()**

```ets
Image_ErrorCode OH_DecodingOptions_SetDesiredSize(OH_DecodingOptions *options, Image_Size *desiredSize)
```

描述

设置期望输出大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| Image_Size *desiredSize | 期望输出大小，默认为原始图片尺寸。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_GetDesiredRegion()**

```ets
Image_ErrorCode OH_DecodingOptions_GetDesiredRegion(OH_DecodingOptions *options, Image_Region *desiredRegion)
```

描述

获取解码区域。

 由于对应SetDesiredRegion接口无法满足区域解码诉求，从API version 19开始，推荐配套使用[OH_DecodingOptions_GetCropRegion](#ZH-CN_TOPIC_0000002522081986__oh_decodingoptions_getcropregion)接口替代。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| Image_Region *desiredRegion | 解码区域，默认为完整图片大小的区域。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_SetDesiredRegion()**

```ets
Image_ErrorCode OH_DecodingOptions_SetDesiredRegion(OH_DecodingOptions *options, Image_Region *desiredRegion)
```

描述

设置解码区域。

 实际解码结果会按照原图解码，无区域解码效果。从API version 19开始，推荐使用接口[OH_DecodingOptions_SetCropRegion](#ZH-CN_TOPIC_0000002522081986__oh_decodingoptions_setcropregion)替代。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| Image_Region *desiredRegion | 解码区域，默认为完整图片大小的区域。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptions_GetDesiredDynamicRange()**

```ets
Image_ErrorCode OH_DecodingOptions_GetDesiredDynamicRange(OH_DecodingOptions *options, int32_t *desiredDynamicRange)
```

描述

获取解码时设置的期望动态范围。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| int32_t *desiredDynamicRange | 期望的动态范围值IMAGE_DYNAMIC_RANGE，默认值为SDR。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数校验错误。 |

**OH_DecodingOptions_SetDesiredDynamicRange()**

```ets
Image_ErrorCode OH_DecodingOptions_SetDesiredDynamicRange(OH_DecodingOptions *options, int32_t desiredDynamicRange)
```

描述

设置解码时的期望动态范围。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| int32_t desiredDynamicRange | 期望的动态范围值IMAGE_DYNAMIC_RANGE，默认值为SDR。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数校验错误。 |

**OH_DecodingOptions_GetDesiredColorSpace()**

```ets
Image_ErrorCode OH_DecodingOptions_GetDesiredColorSpace(OH_DecodingOptions *options, int32_t *colorSpace)
```

描述

获取解码参数中设置的色彩空间。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 解码参数。 |
| int32_t *colorSpace | 解码参数中设置的色彩空间，参考ColorSpaceName。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_SOURCE_INVALID_PARAMETER：参数错误。options或colorSpace为空。 |

**OH_DecodingOptions_SetDesiredColorSpace()**

```ets
Image_ErrorCode OH_DecodingOptions_SetDesiredColorSpace(OH_DecodingOptions *options, int32_t colorSpace)
```

描述

设置解码期望得到的色彩空间。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 解码参数。 |
| int32_t colorSpace | 期望的色彩空间，参考ColorSpaceName。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_SOURCE_INVALID_PARAMETER：参数错误。options为空，或者传入了不支持的colorSpace。 |

**OH_DecodingOptions_SetCropAndScaleStrategy()**

```ets
Image_ErrorCode OH_DecodingOptions_SetCropAndScaleStrategy(OH_DecodingOptions *options, int32_t cropAndScaleStrategy)
```

描述

设置解码选项的裁剪和缩放策略。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| int32_t cropAndScaleStrategy | 在同时指定desiredSize和desiredRegion时执行裁剪和缩放的策略。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：options空指针或者cropAndScaleStrategy取值不在Image_CropAndScaleStrategy枚举值定义之中。 |

**OH_DecodingOptions_GetCropAndScaleStrategy()**

```ets
Image_ErrorCode OH_DecodingOptions_GetCropAndScaleStrategy(OH_DecodingOptions *options, int32_t *cropAndScaleStrategy)
```

描述

获取解码选项的裁剪和缩放策略。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |
| int32_t *cropAndScaleStrategy | 指向在同时指定desiredSize和desiredRegion时执行裁剪和缩放策略的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：options或者cropAndScaleStrategy为空指针。 |

**OH_DecodingOptions_GetCropRegion()**

```ets
Image_ErrorCode OH_DecodingOptions_GetCropRegion(OH_DecodingOptions *options, Image_Region *cropRegion)
```

描述

获取解码参数中的裁剪区域。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 指向解码参数指针。 |
| Image_Region *cropRegion | 指向要裁剪的目标区域指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_SOURCE_INVALID_PARAMETER：options或cropRegion为空。 |

**OH_DecodingOptions_SetCropRegion()**

```ets
Image_ErrorCode OH_DecodingOptions_SetCropRegion(OH_DecodingOptions *options, Image_Region *cropRegion)
```

描述

设置解码参数中的裁剪区域。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 指向解码参数指针。 |
| Image_Region *cropRegion | 指向要裁剪的目标区域指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_SOURCE_INVALID_PARAMETER：options或cropRegion为空。 |

**OH_DecodingOptions_Release()**

```ets
Image_ErrorCode OH_DecodingOptions_Release(OH_DecodingOptions *options)
```

描述

释放OH_DecodingOptions指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptions *options | 被操作的OH_DecodingOptions指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceNative_CreateFromUri()**

```ets
Image_ErrorCode OH_ImageSourceNative_CreateFromUri(char *uri, size_t uriSize, OH_ImageSourceNative **res)
```

描述

通过uri创建OH_ImageSourceNative指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| char *uri | 指向图像源URI的指针。只接受文件URI或Base64 URI。当前文件资源只支持绝对路径。 |
| size_t uriSize | URI长度。 |
| OH_ImageSourceNative **res | 指向c++本地层创建的OH_ImageSourceNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。  IMAGE_BAD_SOURCE：解码数据源异常。 |

**OH_ImageSourceNative_CreateFromFd()**

```ets
Image_ErrorCode OH_ImageSourceNative_CreateFromFd(int32_t fd, OH_ImageSourceNative **res)
```

描述

通过fd创建OH_ImageSourceNative指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| int32_t fd | 文件描述符fd。 |
| OH_ImageSourceNative **res | 指向c++本地层创建的OH_ImageSourceNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceNative_CreateFromData()**

```ets
Image_ErrorCode OH_ImageSourceNative_CreateFromData(uint8_t *data, size_t dataSize, OH_ImageSourceNative **res)
```

描述

通过缓冲区数据创建OH_ImageSourceNative指针。

 data数据应该是未解码的数据，不要传入类似于RGBA，YUV的像素buffer数据。

 如果想通过像素buffer数据创建pixelMap，可以调用[OH_PixelmapNative_CreatePixelmap](pixelmap_native.h.md#ZH-CN_TOPIC_0000002522241982__oh_pixelmapnative_createpixelmap)这一类接口。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| uint8_t *data | 图像缓冲区数据。 |
| size_t dataSize | 图像缓冲区数据长度。 |
| OH_ImageSourceNative **res | 指向c++本地层创建的OH_ImageSourceNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。  IMAGE_BAD_SOURCE：解码数据源异常。 |

**OH_ImageSourceNative_CreateFromDataWithUserBuffer()**

```ets
Image_ErrorCode OH_ImageSourceNative_CreateFromDataWithUserBuffer(uint8_t *data, size_t datalength, OH_ImageSourceNative **imageSource)
```

描述

由数据缓存创建图片源。传入的数据缓存将在图片源对象中直接访问，在图片源对象的生命周期内，数据缓存需要保持可用。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| uint8_t *data | 数据缓存指针。 |
| size_t datalength | 数据缓存长度。 |
| OH_ImageSourceNative **imageSource | 图片源的二级指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：data或imageSource是空指针，datalength为0。 |

**OH_ImageSourceNative_CreateFromRawFile()**

```ets
Image_ErrorCode OH_ImageSourceNative_CreateFromRawFile(RawFileDescriptor *rawFile, OH_ImageSourceNative **res)
```

描述

通过图像资源文件的RawFileDescriptor创建OH_ImageSourceNative指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| RawFileDescriptor *rawFile | 指示raw文件的文件描述符。 |
| OH_ImageSourceNative **res | 指向c++本地层创建的OH_ImageSourceNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceNative_CreatePixelmap()**

```ets
Image_ErrorCode OH_ImageSourceNative_CreatePixelmap(OH_ImageSourceNative *source, OH_DecodingOptions *options, OH_PixelmapNative **pixelmap)
```

描述

通过图片解码参数创建OH_PixelmapNative指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。 |
| OH_DecodingOptions *options | 解码参数。 |
| OH_PixelmapNative **pixelmap | 指向c++本地层创建的OH_PixelmapNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceNative_CreatePixelmapUsingAllocator()**

```ets
Image_ErrorCode OH_ImageSourceNative_CreatePixelmapUsingAllocator(OH_ImageSourceNative *source, OH_DecodingOptions *options, IMAGE_ALLOCATOR_TYPE allocator, OH_PixelmapNative **pixelmap)
```

描述

根据解码参数创建一个PixelMap，PixelMap使用的内存类型可以通过allocatorType来指定。

 默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理通过此接口返回的PixelMap时，请始终考虑步幅（stride）的影响。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。 |
| OH_DecodingOptions *options | 解码参数。 |
| IMAGE_ALLOCATOR_TYPE allocator | 指示返回的PixelMap将使用哪种内存类型。 |
| OH_PixelmapNative **pixelmap | 指向c++本地层创建的OH_PixelmapNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。  IMAGE_BAD_SOURCE：数据源异常。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持的MIME类型。  IMAGE_SOURCE_TOO_LARGE：图像过大。  IMAGE_SOURCE_UNSUPPORTED_ALLOCATOR_TYPE：不支持的分配器类型。例如，使用共享内存解码HDR图像，因为只有DMA支持HDR元数据。  IMAGE_SOURCE_UNSUPPORTED_OPTIONS：不支持的选项。例如，无法将图像转换为所需的像素格式。  IMAGE_DECODE_FAILED：解码失败。  IMAGE_SOURCE_ALLOC_FAILED：内存分配失败。 |

**OH_ImageSourceNative_CreatePixelmapList()**

```ets
Image_ErrorCode OH_ImageSourceNative_CreatePixelmapList(OH_ImageSourceNative *source, OH_DecodingOptions *options, OH_PixelmapNative *resVecPixMap[], size_t size)
```

描述

通过图片解码参数创建OH_PixelmapNative数组。

 注意，此接口会一次性解码全部帧，当帧数过多或单帧图像过大时，会占用较大内存，造成系统内存紧张，此种情况推荐使用Image组件显示动图，Image组件采用逐帧解码，占用内存比此接口少。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。 |
| OH_DecodingOptions *options | 解码参数。 |
| OH_PixelmapNative *resVecPixMap[] | 指向c++本地层创建的OH_PixelmapNative对象的指针数组。 |
| size_t size | 数组长度。 用户可以使用OH_ImageSourceNative_GetFrameCount获取。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNSUPPORTED_OPERATION：操作不支持。 |

**OH_ImageSourceNative_CreatePicture()**

```ets
Image_ErrorCode OH_ImageSourceNative_CreatePicture(OH_ImageSourceNative *source, OH_DecodingOptionsForPicture *options, OH_PictureNative **picture)
```

描述

通过图片解码创建OH_PictureNative指针。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。 |
| OH_DecodingOptionsForPicture *options | 解码参数。 |
| OH_PictureNative **picture | 指向c++本地层创建的OH_PictureNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。  IMAGE_DECODE_FAILED：解码失败。 |

**OH_ImageSourceNative_CreatePictureAtIndex()**

```ets
Image_ErrorCode OH_ImageSourceNative_CreatePictureAtIndex(OH_ImageSourceNative *source, uint32_t index, OH_PictureNative **picture)
```

描述

通过指定序号的图片解码创建OH_PictureNative指针。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。 |
| uint32_t index | 解码图片序号。 |
| OH_PictureNative **picture | 指向c++本地层创建的OH_PictureNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_SOURCE：数据源异常。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持的MIME类型。  IMAGE_SOURCE_TOO_LARGE：图像过大。  IMAGE_SOURCE_UNSUPPORTED_OPTIONS：不支持的选项。例如，无效的图片序号。  IMAGE_DECODE_FAILED：解码失败。 |

**OH_ImageSourceNative_GetDelayTimeList()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetDelayTimeList(OH_ImageSourceNative *source, int32_t *delayTimeList, size_t size)
```

描述

获取图像延迟时间数组。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。 |
| int32_t *delayTimeList | 指向获得的延迟时间列表的指针。它不能是空指针。 |
| size_t size | delayTimeList的大小。用户可以从OH_ImageSourceNative_GetFrameCount获得大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceNative_GetImageInfo()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImageInfo(OH_ImageSourceNative *source, int32_t index, OH_ImageSource_Info *info)
```

描述

获取指定序号的图片信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。 |
| int32_t index | 图片序号。对GIF图片可传入[0,N-1],N表示GIF的帧数。对只有一帧数据的图片格式，可传入0。 |
| OH_ImageSource_Info *info | 指向获取的图像源信息的OH_ImageSource_Info指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceNative_GetImageProperty()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImageProperty(OH_ImageSourceNative *source, Image_String *key, Image_String *value)
```

描述

获取图片指定属性键的值。

 该接口获取到的value.data缺少字符串结束符'\0'，请谨慎使用。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。OH_ImageSourceNative使用完成后需要主动释放，参见OH_ImageSourceNative_Release。 |
| Image_String *key | 指向属性的指针。key的取值范围请参考image_common.h的变量中定义的OHOS_IMAGE_PROPERTY_XXX系列常量。 |
| Image_String *value | 指向获取的值的指针（输出参数）。调用本接口前，用户应将value->data置为空指针，并将value->size设为0。接口会为value->data自动分配所需内存，并对value->size赋值。完成对该内存的使用后，用户必须使用C标准库提供的free()函数释放value->data指向的内存，否则会出现内存泄漏。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceNative_GetImagePropertyShort()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImagePropertyShort(OH_ImageSourceNative *source, Image_String *key, uint16_t *value)
```

描述

以短整型类型获取图像属性的值。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](image_common.h.md#ZH-CN_TOPIC_0000002522081984__变量)中定义的OHOS_IMAGE_PROPERTY_XXX系列常量的值：

- NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。

- ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。

- ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。

- DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。

- GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。

- GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。

- ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被查询属性的ImageSource。 |
| Image_String *key | 被查询的属性。 |
| uint16_t *value | 被查询的属性的查询结果。输出参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是短整型的值。 |

**OH_ImageSourceNative_GetImagePropertyLong()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImagePropertyLong(OH_ImageSourceNative *source, Image_String *key, uint32_t *value)
```

描述

以长整型类型获取图像属性的值。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](image_common.h.md#ZH-CN_TOPIC_0000002522081984__变量)中定义的OHOS_IMAGE_PROPERTY_XXX系列常量的值：

- NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。

- ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。

- ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。

- DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。

- GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。

- GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。

- ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被查询属性的ImageSource。 |
| Image_String *key | 被查询的属性。 |
| uint32_t *value | 被查询属性的查询结果。输出参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是长整型的值。 |

**OH_ImageSourceNative_GetImagePropertyDouble()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImagePropertyDouble(OH_ImageSourceNative *source, Image_String *key, double *value)
```

描述

以浮点型类型获取图像属性的值。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](image_common.h.md#ZH-CN_TOPIC_0000002522081984__变量)中定义的OHOS_IMAGE_PROPERTY_XXX系列常量的值：

- NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。

- ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。

- ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。

- DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。

- GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。

- GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。

- ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被查询属性的ImageSource。 |
| Image_String *key | 被查询的属性。 |
| double *value | 被查询属性的查询结果。输出参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是浮点型的值。 |

**OH_ImageSourceNative_GetImagePropertyArraySize()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImagePropertyArraySize(OH_ImageSourceNative *source, Image_String *key, size_t *size)
```

描述

获取数组类型属性的数组长度或字符串类型属性的字符串长度。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被查询属性的ImageSource。 |
| Image_String *key | 被查询的属性。 |
| size_t *size | 数组类型属性的数组长度，字符串类型属性的字符串长度。输出参数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是数组或字符串类型的值。 |

**OH_ImageSourceNative_GetImagePropertyString()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImagePropertyString(OH_ImageSourceNative *source, Image_String *key, char *value, size_t size)
```

描述

以字符串类型获取图像属性的值。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](image_common.h.md#ZH-CN_TOPIC_0000002522081984__变量)中定义的OHOS_IMAGE_PROPERTY_XXX系列常量的值：

- NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。

- ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。

- ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。

- DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。

- GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。

- GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。

- ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被查询属性的ImageSource。 |
| Image_String *key | 被查询的属性。 |
| char *value | 被查询属性的查询结果。输出参数。调用者需要管理内存应用程序并释放。 |
| size_t size | 字符串长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是字符串类型的值。 |

**OH_ImageSourceNative_GetImagePropertyIntArray()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImagePropertyIntArray(OH_ImageSourceNative *source, Image_String *key, int32_t *value, size_t size)
```

描述

以整型数组类型获取图像属性的值。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](image_common.h.md#ZH-CN_TOPIC_0000002522081984__变量)中定义的OHOS_IMAGE_PROPERTY_XXX系列常量的值：

- NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。

- ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。

- ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。

- DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。

- GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。

- GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。

- ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被查询属性的ImageSource。 |
| Image_String *key | 被查询的属性。 |
| int32_t *value | 被查询属性的查询结果。输出参数。调用者需要管理内存应用程序并释放。 |
| size_t size | 字符串长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是整型数组类型的值。 |

**OH_ImageSourceNative_GetImagePropertyDoubleArray()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImagePropertyDoubleArray(OH_ImageSourceNative *source, Image_String *key, double *value, size_t size)
```

描述

以浮点型数组类型获取图像属性的值。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](image_common.h.md#ZH-CN_TOPIC_0000002522081984__变量)中定义的OHOS_IMAGE_PROPERTY_XXX系列常量的值：

- NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。

- ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。

- ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。

- DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。

- GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。

- GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。

- ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被查询属性的ImageSource。 |
| Image_String *key | 被查询的属性。 |
| double *value | 被查询属性的查询结果。输出参数。调用者需要管理内存应用程序并释放。 |
| size_t size | 数组长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是浮点型数组类型的值。 |

**OH_ImageSourceNative_GetImagePropertyBlob()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImagePropertyBlob(OH_ImageSourceNative *source, Image_String *key, void *value, size_t size)
```

描述

以二进制对象类型获取图像属性的值。

   ![image](public_sys-resources/note_3.0-zh-cn.webp)

读取DNG格式图片时，该接口对部分key有特殊处理。以下字段的字符串取值请参考[变量](image_common.h.md#ZH-CN_TOPIC_0000002522081984__变量)中定义的OHOS_IMAGE_PROPERTY_XXX系列常量的值：

- NewSubfileType、ImageWidth、ImageLength、DefaultCropSize、Orientation、Compression、PhotometricInterpretation、PlanarConfiguration、RowsPerStrip、StripOffsets、StripByteCounts、SamplesPerPixel、BitsPerSample、YCbCrCoefficients、YCbCrSubSampling、YCbCrPositioning、ReferenceBlackWhite、XResolution、YResolution、ResolutionUnit字段：返回主图相关的字段值。

- ImageUniqueID字段：根据规范进行校验，不符合规范时会返回空字符串。

- ExifVersion、FlashpixVersion、ColorSpace字段：当图片中不存在该标签时，返回错误码。

- DNGVersion字段：当版本号小于1.0.0.0时，统一返回1.0.0.0。

- GPSVersionID字段：当没有有效的GPS数据时，会清除GPS版本号并返回0。

- GPSAltitudeRef字段：当未设置GPSAltitude时，会设置为0xFFFFFFFF。

- ISOSpeedRatings字段：当该标签值为0或65535时，会优先使用推荐曝光指数，若不存在则依次使用标准输出灵敏度、ISO速度、曝光指数。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被查询属性的ImageSource。 |
| Image_String *key | 被查询的属性。 |
| void *value | 被查询属性的查询结果。输出参数。调用者需要管理内存应用程序并释放。 |
| size_t size | 数组长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是二进制对象类型的值。 |

**OH_ImageSourceNative_ModifyImagePropertyShort()**

```ets
Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyShort(OH_ImageSourceNative *source, Image_String *key, uint16_t value)
```

描述

修改图像属性中短整型的值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被修改属性的ImageSource。 |
| Image_String *key | 被修改的属性。 |
| uint16_t value | 为属性设置的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是短整型的值。 |

**OH_ImageSourceNative_ModifyImagePropertyLong()**

```ets
Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyLong(OH_ImageSourceNative *source, Image_String *key, uint32_t value)
```

描述

修改图像属性中长整型的值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被修改属性的ImageSource。 |
| Image_String *key | 被修改的属性。 |
| uint32_t value | 为属性设置的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是长整型的值。 |

**OH_ImageSourceNative_ModifyImagePropertyDouble()**

```ets
Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyDouble(OH_ImageSourceNative *source, Image_String *key, double value)
```

描述

修改图像属性中浮点型的值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被修改属性的ImageSource。 |
| Image_String *key | 被修改的属性。 |
| double value | 为属性设置的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是浮点型的值。 |

**OH_ImageSourceNative_ModifyImagePropertyIntArray()**

```ets
Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyIntArray(OH_ImageSourceNative *source, Image_String *key, int32_t *value, size_t size)
```

描述

修改图像属性中整型数组型的值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被修改属性的ImageSource。 |
| Image_String *key | 被修改的属性。 |
| int32_t *value | 为属性设置的值。 |
| size_t size | 数组长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是整型数组类型的值。 |

**OH_ImageSourceNative_ModifyImagePropertyDoubleArray()**

```ets
Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyDoubleArray(OH_ImageSourceNative *source, Image_String *key, double *value, size_t size)
```

描述

修改图像属性中浮点型数组型的值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被修改属性的ImageSource。 |
| Image_String *key | 被修改的属性。 |
| double *value | 为属性设置的值。 |
| size_t size | 数组长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是浮点型数组类型的值。 |

**OH_ImageSourceNative_ModifyImagePropertyBlob()**

```ets
Image_ErrorCode OH_ImageSourceNative_ModifyImagePropertyBlob(OH_ImageSourceNative *source, Image_String *key, void *value, size_t size)
```

描述

修改图像属性中二进制对象的值。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被修改属性的ImageSource。 |
| Image_String *key | 被修改的属性。 |
| void *value | 为属性设置的值。 |
| size_t size | 数组长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为nullptr。  IMAGE_SOURCE_UNSUPPORTED_MIME_TYPE：不支持查询当前mimetype的图像属性。  IMAGE_SOURCE_UNSUPPORTED_METADATA：指定的元数据不存在，或者不是二进制对象类型的值。 |

**OH_ImageSourceNative_GetImagePropertyWithNull()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetImagePropertyWithNull(OH_ImageSourceNative *source, Image_String *key, Image_String *value)
```

描述

获取图像属性值。输出的value.data以字符串结束符'\0'结尾。

起始版本： 19

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。OH_ImageSourceNative使用完成后需要主动释放，参见OH_ImageSourceNative_Release。 |
| Image_String *key | 指向属性键的指针。key的取值范围请参考image_common.h的变量中定义的OHOS_IMAGE_PROPERTY_XXX系列常量。 |
| Image_String *value | 指向属性值的指针（输出参数）。调用本接口前，用户应将value->data置为空指针，并将value->size设为0。接口会为value->data自动分配所需内存，并对value->size赋值。完成对该内存的使用后，用户必须使用C标准库提供的free()函数释放value->data指向的内存，否则可能导致内存泄漏。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_SOURCE_INVALID_PARAMETER：source、key或value为空。 |

**OH_ImageSourceNative_ModifyImageProperty()**

```ets
Image_ErrorCode OH_ImageSourceNative_ModifyImageProperty(OH_ImageSourceNative *source, Image_String *key, Image_String *value)
```

描述

通过指定的键修改图片属性的值。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。OH_ImageSourceNative使用完成后需要主动释放，参见OH_ImageSourceNative_Release。 |
| Image_String *key | 指向属性键的指针。key的取值范围请参考image_common.h的变量中定义的OHOS_IMAGE_PROPERTY_XXX系列常量。 |
| Image_String *value | 需要修改的属性值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceNative_GetFrameCount()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetFrameCount(OH_ImageSourceNative *source, uint32_t *frameCount)
```

描述

获取图像帧数。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 被操作的OH_ImageSourceNative指针。 |
| uint32_t *frameCount | 图像帧数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageSourceNative_GetSupportedFormats()**

```ets
Image_ErrorCode OH_ImageSourceNative_GetSupportedFormats(Image_MimeType **supportedFormats, size_t *length)
```

描述

获取支持解码的图片格式。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| Image_MimeType **supportedFormats | 支持解码的图片格式。 |
| size_t *length | 数组长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_SOURCE_INVALID_PARAMETER：参数异常，supportedFormats或length为空。 |

**OH_ImageSourceNative_Release()**

```ets
Image_ErrorCode OH_ImageSourceNative_Release(OH_ImageSourceNative *source)
```

描述

释放OH_ImageSourceNative指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageSourceNative *source | 要释放的OH_ImageSourceNative指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptionsForPicture_Create()**

```ets
Image_ErrorCode OH_DecodingOptionsForPicture_Create(OH_DecodingOptionsForPicture **options)
```

描述

创建OH_DecodingOptionsForPicture指针。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptionsForPicture **options | 被操作的OH_DecodingOptionsForPicture指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptionsForPicture_GetDesiredAuxiliaryPictures()**

```ets
Image_ErrorCode OH_DecodingOptionsForPicture_GetDesiredAuxiliaryPictures(OH_DecodingOptionsForPicture *options, Image_AuxiliaryPictureType **desiredAuxiliaryPictures, size_t *length)
```

描述

获取解码时设置的期望辅助图（期望解码出的picture包含的辅助图）。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptionsForPicture *options | 被操作的OH_DecodingOptionsForPicture指针。 |
| Image_AuxiliaryPictureType **desiredAuxiliaryPictures | 解码选项中的期望辅助图。 |
| size_t *length | 期望辅助图长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptionsForPicture_SetDesiredAuxiliaryPictures()**

```ets
Image_ErrorCode OH_DecodingOptionsForPicture_SetDesiredAuxiliaryPictures(OH_DecodingOptionsForPicture *options, Image_AuxiliaryPictureType *desiredAuxiliaryPictures, size_t length)
```

描述

设置解码选项中的期望辅助图。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptionsForPicture *options | 被操作的OH_DecodingOptionsForPicture指针。 |
| Image_AuxiliaryPictureType *desiredAuxiliaryPictures | 将要设置的期望辅助图。 |
| size_t length | 期望辅助图长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |

**OH_DecodingOptionsForPicture_Release()**

```ets
Image_ErrorCode OH_DecodingOptionsForPicture_Release(OH_DecodingOptionsForPicture *options)
```

描述

释放OH_DecodingOptionsForPicture指针。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_DecodingOptionsForPicture *options | 要释放的OH_DecodingOptionsForPicture指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。   IMAGE_BAD_PARAMETER：参数错误。 |