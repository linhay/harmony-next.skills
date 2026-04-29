# pixelmap_native.h

**概述**

访问Pixelmap的API。

引用文件： <multimedia/image_framework/image/pixelmap_native.h>

库： libpixelmap.so

系统能力： SystemCapability.Multimedia.Image.Core

起始版本： 12

相关模块： [Image_NativeModule](Image_NativeModule.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_Pixelmap_HdrStaticMetadata | OH_Pixelmap_HdrStaticMetadata | HDR_STATIC_METADATA关键字对应的静态元数据值。 |
| OH_Pixelmap_HdrDynamicMetadata | OH_Pixelmap_HdrDynamicMetadata | DR_DYNAMIC_METADATA关键字对应的动态元数据值。 |
| OH_Pixelmap_HdrGainmapMetadata | OH_Pixelmap_HdrGainmapMetadata | HDR_GAINMAP_METADATA关键字对应的gainmap相关元数据值，参考ISO 21496-1。 |
| OH_Pixelmap_HdrMetadataValue | OH_Pixelmap_HdrMetadataValue | Pixelmap使用的HDR元数据值，和OH_Pixelmap_HdrMetadataKey关键字相对应。用于OH_PixelmapNative_SetMetadata及OH_PixelmapNative_GetMetadata，有相应OH_Pixelmap_HdrMetadataKey关键字作为入参时，设置或获取到本结构体中相对应的元数据类型的值。 |
| OH_PixelmapNative | - | OH_PixelmapNative结构体是native层封装的图像解码后无压缩的位图格式结构体。  函数创建OH_PixelmapNative使用OH_PixelmapNative_CreatePixelmap函数，默认采用BGRA_8888格式处理数据。  释放OH_PixelmapNative对象使用OH_PixelmapNative_Release函数。 |
| OH_NativeBuffer | - | NativeBuffer结构体类型，用于执行NativeBuffer相关操作。 |
| OH_NativeColorSpaceManager | OH_NativeColorSpaceManager | NativeColorSpaceManager结构体类型，用于执行NativeColorSpaceManager相关操作。 |
| OH_Pixelmap_InitializationOptions | - | OH_Pixelmap_InitializationOptions是native层封装的初始化参数结构体，用于设置Pixelmap的初始化参数。  创建OH_Pixelmap_InitializationOptions对象使用OH_PixelmapInitializationOptions_Create函数。  释放OH_Pixelmap_InitializationOptions对象使用OH_PixelmapInitializationOptions_Release函数。 |
| OH_Pixelmap_ImageInfo | - | 图像像素信息结构体。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| PIXELMAP_ALPHA_TYPE | PIXELMAP_ALPHA_TYPE | Pixelmap透明度类型。 |
| PIXEL_FORMAT | PIXEL_FORMAT | 图片像素格式。 |
| OH_PixelmapNative_AntiAliasingLevel | OH_PixelmapNative_AntiAliasingLevel | Pixelmap缩放时采用的缩放算法。 |
| OH_Pixelmap_HdrMetadataKey | OH_Pixelmap_HdrMetadataKey | Pixelmap使用的HDR相关元数据信息的关键字，用于OH_PixelmapNative_SetMetadata及OH_PixelmapNative_GetMetadata。 |
| OH_Pixelmap_HdrMetadataType | OH_Pixelmap_HdrMetadataType | HDR_METADATA_TYPE关键字对应的值。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| Image_ErrorCode OH_PixelmapInitializationOptions_Create(OH_Pixelmap_InitializationOptions **options) | 创建OH_Pixelmap_InitializationOptions指针。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_GetWidth(OH_Pixelmap_InitializationOptions *options, uint32_t *width) | 获取图片宽。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_SetWidth(OH_Pixelmap_InitializationOptions *options, uint32_t width) | 设置图片宽。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_GetHeight(OH_Pixelmap_InitializationOptions *options, uint32_t *height) | 获取图片高。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_SetHeight(OH_Pixelmap_InitializationOptions *options, uint32_t height) | 设置图片高。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_GetPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t *pixelFormat) | 获取像素格式。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_SetPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t pixelFormat) | 设置像素格式。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_GetSrcPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t *srcpixelFormat) | 获取源像素格式。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_SetSrcPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t srcpixelFormat) | 设置源像素格式。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_GetRowStride(OH_Pixelmap_InitializationOptions *options, int32_t *rowStride) | 获取行跨距。  跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width * 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_SetRowStride(OH_Pixelmap_InitializationOptions *options, int32_t rowStride) | 设置图像跨距。  跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width * 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_GetAlphaType(OH_Pixelmap_InitializationOptions *options, int32_t *alphaType) | 获取透明度类型。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_SetAlphaType(OH_Pixelmap_InitializationOptions *options, int32_t alphaType) | 设置透明度类型。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_GetEditable(OH_Pixelmap_InitializationOptions *options, bool *editable) | 获取可编辑标志。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_SetEditable(OH_Pixelmap_InitializationOptions *options, bool editable) | 设置可编辑标志。 |
| Image_ErrorCode OH_PixelmapInitializationOptions_Release(OH_Pixelmap_InitializationOptions *options) | 释放OH_Pixelmap_InitializationOptions指针。 |
| Image_ErrorCode OH_PixelmapImageInfo_Create(OH_Pixelmap_ImageInfo **info) | 创建OH_Pixelmap_ImageInfo指针。 |
| Image_ErrorCode OH_PixelmapImageInfo_GetWidth(OH_Pixelmap_ImageInfo *info, uint32_t *width) | 获取图片宽。 |
| Image_ErrorCode OH_PixelmapImageInfo_GetHeight(OH_Pixelmap_ImageInfo *info, uint32_t *height) | 获取图片高。 |
| Image_ErrorCode OH_PixelmapImageInfo_GetAlphaMode(OH_Pixelmap_ImageInfo *info, int32_t *AlphaMode) | 获取图片透明通道类型。 |
| Image_ErrorCode OH_PixelmapImageInfo_GetRowStride(OH_Pixelmap_ImageInfo *info, uint32_t *rowStride) | 获取行跨距。 |
| Image_ErrorCode OH_PixelmapImageInfo_GetPixelFormat(OH_Pixelmap_ImageInfo *info, int32_t *pixelFormat) | 获取像素格式。 |
| Image_ErrorCode OH_PixelmapImageInfo_GetAlphaType(OH_Pixelmap_ImageInfo *info, int32_t *alphaType) | 获取OH_PixelmapImageInfo默认的透明通道类型。若要获取图片当前透明通道类型，请使用OH_PixelmapImageInfo_GetAlphaMode。 |
| Image_ErrorCode OH_PixelmapImageInfo_GetDynamicRange(OH_Pixelmap_ImageInfo *info, bool *isHdr) | 获取Pixelmap是否为高动态范围的信息。 |
| Image_ErrorCode OH_PixelmapImageInfo_Release(OH_Pixelmap_ImageInfo *info) | 释放OH_Pixelmap_ImageInfo指针。 |
| Image_ErrorCode OH_PixelmapNative_CreatePixelmap(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options, OH_PixelmapNative **pixelmap) | 通过属性创建PixelMap，默认采用BGRA_8888格式处理数据，其他格式请参考OH_PixelmapInitializationOptions_SetSrcPixelFormat。 |
| Image_ErrorCode OH_PixelmapNative_CreatePixelmapUsingAllocator(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options, IMAGE_ALLOCATOR_MODE allocator, OH_PixelmapNative **pixelmap) | 根据入参options创建pixelmap，pixelmap使用的内存类型可以通过allocator指定。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。 |
| Image_ErrorCode OH_PixelmapNative_ConvertPixelmapNativeToNapi(napi_env env, OH_PixelmapNative *pixelmapNative, napi_value *pixelmapNapi) | 将nativePixelMap对象转换为PixelMapnapi对象。 |
| Image_ErrorCode OH_PixelmapNative_ConvertPixelmapNativeFromNapi(napi_env env, napi_value pixelmapNapi, OH_PixelmapNative **pixelmapNative) | 将PixelMapnapi对象转换为nativePixelMap对象。 |
| Image_ErrorCode OH_PixelmapNative_ReadPixels(OH_PixelmapNative *pixelmap, uint8_t *destination, size_t *bufferSize) | 读取图像像素数据，并按照PixelMap的像素格式写入缓冲区中。 |
| Image_ErrorCode OH_PixelmapNative_WritePixels(OH_PixelmapNative *pixelmap, uint8_t *source, size_t bufferSize) | 读取缓冲区中的图像像素数据，并按照PixelMap的像素格式将结果写入PixelMap。 |
| Image_ErrorCode OH_PixelmapNative_ReadPixelsFromArea(OH_PixelmapNative *pixelmap, Image_PositionArea *area) | 从PixelMap的指定区域中读取像素数据并存入缓冲区。读取出来的数据为BGRA_8888格式。 |
| Image_ErrorCode OH_PixelmapNative_WritePixelsToArea(OH_PixelmapNative *pixelmap, Image_PositionArea *area) | 将缓冲区中的像素数据写入PixelMap的指定区域。数据源应为BGRA_8888格式。 |
| Image_ErrorCode OH_PixelmapNative_GetArgbPixels(OH_PixelmapNative *pixelmap, uint8_t *destination, size_t *bufferSize) | 从PixelMap中读取ARGB格式的数据。 |
| Image_ErrorCode OH_PixelmapNative_ToSdr(OH_PixelmapNative *pixelmap) | 将HDR的图像内容转换为SDR的图像内容。 |
| Image_ErrorCode OH_PixelmapNative_GetImageInfo(OH_PixelmapNative *pixelmap, OH_Pixelmap_ImageInfo *imageInfo) | 获取图像像素信息。 |
| Image_ErrorCode OH_PixelmapNative_Opacity(OH_PixelmapNative *pixelmap, float rate) | 通过设置透明比率来让PixelMap达到对应的透明效果。 |
| Image_ErrorCode OH_PixelmapNative_Scale(OH_PixelmapNative *pixelmap, float scaleX, float scaleY) | 根据输入的宽高对图片进行缩放。 |
| Image_ErrorCode OH_PixelmapNative_ScaleWithAntiAliasing(OH_PixelmapNative *pixelmap, float scaleX, float scaleY, OH_PixelmapNative_AntiAliasingLevel level) | 根据指定的缩放算法和输入的宽高对图片进行缩放。 |
| Image_ErrorCode OH_PixelmapNative_CreateScaledPixelMap(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap, float scaleX, float scaleY) | 根据输入的宽高的缩放比例，创建一个新的缩放后的图片。 |
| Image_ErrorCode OH_PixelmapNative_CreateScaledPixelMapWithAntiAliasing(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap, float scaleX, float scaleY, OH_PixelmapNative_AntiAliasingLevel level) | 根据指定的缩放算法和输入的宽高的缩放比例，创建一个新的缩放后的图片。 |
| Image_ErrorCode OH_PixelmapNative_CreateAlphaPixelmap(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap) | 从源PixelMap创建一个仅含有Alpha通道的PixelMap。 |
| Image_ErrorCode OH_PixelmapNative_Clone(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap) | 从源PixelMap复制出一个新的PixelMap。 |
| Image_ErrorCode OH_PixelmapNative_CreateCroppedAndScaledPixelMap(OH_PixelmapNative *srcPixelmap, Image_Region *region, Image_Scale *scale, OH_PixelmapNative_AntiAliasingLevel level, OH_PixelmapNative **dstPixelmap) | 基于源PixelMap创建一个裁剪并缩放的新PixelMap。 |
| Image_ErrorCode OH_PixelmapNative_Translate(OH_PixelmapNative *pixelmap, float x, float y) | 根据输入的坐标对图片进行位置变换。 |
| Image_ErrorCode OH_PixelmapNative_Rotate(OH_PixelmapNative *pixelmap, float angle) | 根据输入的角度对图片进行旋转。 |
| Image_ErrorCode OH_PixelmapNative_Flip(OH_PixelmapNative *pixelmap, bool shouldFlipHorizontally, bool shouldFlipVertically) | 根据输入的条件对图片进行翻转。 |
| Image_ErrorCode OH_PixelmapNative_Crop(OH_PixelmapNative *pixelmap, Image_Region *region) | 根据输入的尺寸对图片进行裁剪。 |
| Image_ErrorCode OH_PixelmapNative_Release(OH_PixelmapNative *pixelmap) | 释放OH_PixelmapNative指针，推荐使用OH_PixelmapNative_Destroy。 |
| Image_ErrorCode OH_PixelmapNative_Destroy(OH_PixelmapNative **pixelmap) | 释放OH_PixelmapNative指针。 |
| Image_ErrorCode OH_PixelmapNative_ConvertAlphaFormat(OH_PixelmapNative* srcpixelmap, OH_PixelmapNative* dstpixelmap, const bool isPremul) | 将pixelmap的像素数据做预乘和非预乘之间的转换。 |
| Image_ErrorCode OH_PixelmapNative_CreateEmptyPixelmap(OH_Pixelmap_InitializationOptions *options, OH_PixelmapNative **pixelmap) | 利用OH_Pixelmap_InitializationOptions创建空的pixelmap对象，内存数据为0。 |
| Image_ErrorCode OH_PixelmapNative_CreateEmptyPixelmapUsingAllocator(OH_Pixelmap_InitializationOptions *options, IMAGE_ALLOCATOR_MODE allocator, OH_PixelmapNative **pixelmap) | 根据入参options创建空的pixelmap，pixelmap使用的内存类型可以通过allocator指定。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。 |
| Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromSurface(const char *surfaceId, size_t length, OH_PixelmapNative **pixelmap) | 通过Surface的Surface ID创建一个PixelMap。 |
| Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromSurfaceWithTransformation(const char *surfaceId, size_t length, bool transformEnabled, OH_PixelmapNative **pixelmap) | 通过Surface的ID创建一个预览流画面的PixelMap对象。该Surface可能携带旋转或翻转的变换信息。 |
| Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromNativeBuffer(OH_NativeBuffer *nativeBuffer, OH_PixelmapNative **pixelmap) | 通过NativeBuffer创建一个PixelMap。如果NativeBuffer的用途未配置CPU访问权限，则不支持创建。  支持创建的像素格式为RGBA_8888、NV21、NV12、YCBCR_P010、YCRCB_P010。 |
| Image_ErrorCode OH_PixelmapNative_GetNativeBuffer(OH_PixelmapNative *pixelmap, OH_NativeBuffer **nativeBuffer) | 从DMA内存的PixelMap中，获取NativeBuffer对象。 |
| Image_ErrorCode OH_PixelmapNative_GetMetadata(OH_PixelmapNative *pixelmap, OH_Pixelmap_HdrMetadataKey key, OH_Pixelmap_HdrMetadataValue **value) | 获取元数据。 |
| Image_ErrorCode OH_PixelmapNative_SetMetadata(OH_PixelmapNative *pixelmap, OH_Pixelmap_HdrMetadataKey key, OH_Pixelmap_HdrMetadataValue *value) | 设置元数据。 |
| Image_ErrorCode OH_PixelmapNative_SetColorSpaceNative(OH_PixelmapNative *pixelmap, OH_NativeColorSpaceManager *colorSpaceNative) | 设置NativeColorSpaceManager对象。 |
| Image_ErrorCode OH_PixelmapNative_GetColorSpaceNative(OH_PixelmapNative *pixelmap, OH_NativeColorSpaceManager **colorSpaceNative) | 获取NativeColorSpaceManager对象。 |
| Image_ErrorCode OH_PixelmapNative_SetMemoryName(OH_PixelmapNative *pixelmap, char *name, size_t *size) | 设置pixelMap内存名字。 |
| Image_ErrorCode OH_PixelmapNative_GetByteCount(OH_PixelmapNative *pixelmap, uint32_t *byteCount) | 获取Pixelmap中所有像素所占用的总字节数，不包含内存填充。 |
| Image_ErrorCode OH_PixelmapNative_GetAllocationByteCount(OH_PixelmapNative *pixelmap, uint32_t *allocationByteCount) | 获取Pixelmap用于储存像素数据的内存字节数。 |
| Image_ErrorCode OH_PixelmapNative_AccessPixels(OH_PixelmapNative *pixelmap, void **addr) | 获取Pixelmap像素数据的内存地址，并锁定这块内存。  当该内存被锁定时，任何修改或释放该Pixelmap的像素数据的操作均会失败或无效。 |
| Image_ErrorCode OH_PixelmapNative_UnaccessPixels(OH_PixelmapNative *pixelmap) | 释放Pixelmap像素数据的内存锁。  该函数需要与OH_PixelmapNative_AccessPixels匹配使用。 |
| Image_ErrorCode OH_PixelmapNative_GetUniqueId(OH_PixelmapNative *pixelmap, uint32_t *uniqueId) | 获取PixelMap的唯一ID。 |
| Image_ErrorCode OH_PixelmapNative_IsReleased(OH_PixelmapNative *pixelmap, bool *released) | 检测PixelMap是否已被释放。如果已被释放，则任何访问该对象内部数据的方法调用将会失效。 |

**枚举类型说明**

**PIXELMAP_ALPHA_TYPE**

```ets
enum PIXELMAP_ALPHA_TYPE
```

描述

Pixelmap透明度类型。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| PIXELMAP_ALPHA_TYPE_UNKNOWN = 0 | 未知格式。 |
| PIXELMAP_ALPHA_TYPE_OPAQUE = 1 | 不透明的格式。 |
| PIXELMAP_ALPHA_TYPE_PREMULTIPLIED = 2 | 预乘透明度格式。 |
| PIXELMAP_ALPHA_TYPE_UNPREMULTIPLIED = 3 | 非预乘透明度格式。 |

**PIXEL_FORMAT**

```ets
enum PIXEL_FORMAT
```

描述

图片像素格式。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| PIXEL_FORMAT_UNKNOWN = 0 | 未知格式。 |
| PIXEL_FORMAT_RGB_565 = 2 | RGB_565格式。 |
| PIXEL_FORMAT_RGBA_8888 = 3 | RGBA_8888格式。 |
| PIXEL_FORMAT_BGRA_8888 = 4 | BGRA_8888格式。 |
| PIXEL_FORMAT_RGB_888 = 5 | RGB_888格式。 |
| PIXEL_FORMAT_ALPHA_8 = 6 | ALPHA_8格式。 |
| PIXEL_FORMAT_RGBA_F16 = 7 | RGBA_F16格式。 |
| PIXEL_FORMAT_NV21 = 8 | NV21格式。 |
| PIXEL_FORMAT_NV12 = 9 | NV12格式。 |
| PIXEL_FORMAT_RGBA_1010102 = 10 | RGBA_1010102格式。 |
| PIXEL_FORMAT_YCBCR_P010 = 11 | YCBCR_P010格式。 |
| PIXEL_FORMAT_YCRCB_P010 = 12 | YCRCB_P010格式。 |

**OH_PixelmapNative_AntiAliasingLevel**

```ets
enum OH_PixelmapNative_AntiAliasingLevel
```

描述

Pixelmap缩放时采用的缩放算法。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| OH_PixelmapNative_AntiAliasing_NONE = 0 | 最近邻插值算法。 |
| OH_PixelmapNative_AntiAliasing_LOW = 1 | 双线性插值算法。 |
| OH_PixelmapNative_AntiAliasing_MEDIUM = 2 | 双线性插值算法，同时开启Mipmap。缩小图片时建议使用。 |
| OH_PixelmapNative_AntiAliasing_HIGH = 3 | 三次插值算法。 |

**OH_Pixelmap_HdrMetadataKey**

```ets
enum OH_Pixelmap_HdrMetadataKey
```

描述

Pixelmap使用的HDR相关元数据信息的关键字，用于[OH_PixelmapNative_SetMetadata](pixelmap_native.h.md#ZH-CN_TOPIC_0000002522241982__oh_pixelmapnative_setmetadata)及[OH_PixelmapNative_GetMetadata](pixelmap_native.h.md#ZH-CN_TOPIC_0000002522241982__oh_pixelmapnative_getmetadata)。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| HDR_METADATA_TYPE = 0 | Pixelmap使用的元数据类型。 |
| HDR_STATIC_METADATA = 1 | 静态元数据。 |
| HDR_DYNAMIC_METADATA = 2 | 动态元数据。 |
| HDR_GAINMAP_METADATA = 3 | Gainmap使用的元数据。 |

**OH_Pixelmap_HdrMetadataType**

```ets
enum OH_Pixelmap_HdrMetadataType
```

描述

HDR_METADATA_TYPE关键字对应的值。

起始版本： 12

| 枚举项 | 描述 |
| --- | --- |
| HDR_METADATA_TYPE_NONE = 0 | 无元数据内容。 |
| HDR_METADATA_TYPE_BASE = 1 | 表示用于基础图的元数据。 |
| HDR_METADATA_TYPE_GAINMAP = 2 | 表示用于Gainmap图的元数据。 |
| HDR_METADATA_TYPE_ALTERNATE = 3 | 表示用于合成后HDR图的元数据。 |

**函数说明**

**OH_PixelmapInitializationOptions_Create()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_Create(OH_Pixelmap_InitializationOptions **options)
```

描述

创建OH_Pixelmap_InitializationOptions指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions **options | 被创建的OH_Pixelmap_InitializationOptions指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_GetWidth()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetWidth(OH_Pixelmap_InitializationOptions *options, uint32_t *width)
```

描述

获取图片宽。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| uint32_t *width | 图片的宽，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_SetWidth()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetWidth(OH_Pixelmap_InitializationOptions *options, uint32_t width)
```

描述

设置图片宽。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| uint32_t width | 图片的宽，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_GetHeight()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetHeight(OH_Pixelmap_InitializationOptions *options, uint32_t *height)
```

描述

获取图片高。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| uint32_t *height | 图片的高，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_SetHeight()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetHeight(OH_Pixelmap_InitializationOptions *options, uint32_t height)
```

描述

设置图片高。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| uint32_t height | 图片的高，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_GetPixelFormat()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t *pixelFormat)
```

描述

获取像素格式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| int32_t *pixelFormat | 像素格式PIXEL_FORMAT。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_SetPixelFormat()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t pixelFormat)
```

描述

设置像素格式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| int32_t pixelFormat | 像素格式PIXEL_FORMAT。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_GetSrcPixelFormat()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetSrcPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t *srcpixelFormat)
```

描述

获取源像素格式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| int32_t *srcpixelFormat | 像素格式PIXEL_FORMAT。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_SetSrcPixelFormat()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetSrcPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t srcpixelFormat)
```

描述

设置源像素格式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| int32_t srcpixelFormat | 源像素格式PIXEL_FORMAT。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_GetRowStride()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetRowStride(OH_Pixelmap_InitializationOptions *options, int32_t *rowStride)
```

描述

获取行跨距。

 跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width * 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| int32_t *rowStride | 跨距，单位：字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNKNOWN_ERROR：options被释放。 |

**OH_PixelmapInitializationOptions_SetRowStride()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetRowStride(OH_Pixelmap_InitializationOptions *options, int32_t rowStride)
```

描述

设置图像跨距。

 跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width * 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| int32_t rowStride | 跨距，单位：字节。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNKNOWN_ERROR：options被释放。 |

**OH_PixelmapInitializationOptions_GetAlphaType()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetAlphaType(OH_Pixelmap_InitializationOptions *options, int32_t *alphaType)
```

描述

获取透明度类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| int32_t *alphaType | 透明度类型PIXELMAP_ALPHA_TYPE。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_SetAlphaType()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetAlphaType(OH_Pixelmap_InitializationOptions *options, int32_t alphaType)
```

描述

设置透明度类型。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| int32_t alphaType | 透明度类型PIXELMAP_ALPHA_TYPE。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_GetEditable()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetEditable(OH_Pixelmap_InitializationOptions *options, bool *editable)
```

描述

获取可编辑标志。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| bool *editable | 可编辑标志。true表示可编辑，false表示不可编辑。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_SetEditable()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetEditable(OH_Pixelmap_InitializationOptions *options, bool editable)
```

描述

设置可编辑标志。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被操作的OH_Pixelmap_InitializationOptions指针。 |
| bool editable | 可编辑标志。true表示可编辑，false表示不可编辑。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapInitializationOptions_Release()**

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_Release(OH_Pixelmap_InitializationOptions *options)
```

描述

释放OH_Pixelmap_InitializationOptions指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 被释放的OH_Pixelmap_InitializationOptions指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapImageInfo_Create()**

```ets
Image_ErrorCode OH_PixelmapImageInfo_Create(OH_Pixelmap_ImageInfo **info)
```

描述

创建OH_Pixelmap_ImageInfo指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_ImageInfo **info | 被创建的OH_Pixelmap_ImageInfo指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapImageInfo_GetWidth()**

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetWidth(OH_Pixelmap_ImageInfo *info, uint32_t *width)
```

描述

获取图片宽。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_ImageInfo *info | 被操作的OH_Pixelmap_ImageInfo指针。 |
| uint32_t *width | 图片宽，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapImageInfo_GetHeight()**

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetHeight(OH_Pixelmap_ImageInfo *info, uint32_t *height)
```

描述

获取图片高。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_ImageInfo *info | 被操作的OH_Pixelmap_ImageInfo指针。 |
| uint32_t *height | 图片高，单位：像素。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapImageInfo_GetAlphaMode()**

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetAlphaMode(OH_Pixelmap_ImageInfo *info, int32_t *AlphaMode)
```

描述

获取图片透明通道类型。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_ImageInfo *info | 被操作的OH_Pixelmap_ImageInfo指针。 |
| int32_t *AlphaMode | 被操作的alpha格式的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapImageInfo_GetRowStride()**

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetRowStride(OH_Pixelmap_ImageInfo *info, uint32_t *rowStride)
```

描述

获取行跨距。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_ImageInfo *info | 被操作的OH_Pixelmap_ImageInfo指针。 |
| uint32_t *rowStride | 跨距，内存中每行像素所占的空间。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapImageInfo_GetPixelFormat()**

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetPixelFormat(OH_Pixelmap_ImageInfo *info, int32_t *pixelFormat)
```

描述

获取像素格式。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_ImageInfo *info | 被操作的OH_Pixelmap_ImageInfo指针。 |
| int32_t *pixelFormat | 像素格式PIXEL_FORMAT。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapImageInfo_GetAlphaType()**

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetAlphaType(OH_Pixelmap_ImageInfo *info, int32_t *alphaType)
```

描述

获取OH_PixelmapImageInfo默认的透明通道类型。若要获取图片当前透明通道类型，请使用[OH_PixelmapImageInfo_GetAlphaMode](pixelmap_native.h.md#ZH-CN_TOPIC_0000002522241982__oh_pixelmapimageinfo_getalphamode)。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_ImageInfo *info | 被操作的OH_Pixelmap_ImageInfo指针。 |
| int32_t *alphaType | 透明度类型PIXELMAP_ALPHA_TYPE。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapImageInfo_GetDynamicRange()**

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetDynamicRange(OH_Pixelmap_ImageInfo *info, bool *isHdr)
```

描述

获取Pixelmap是否为高动态范围的信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_ImageInfo *info | 被操作的OH_Pixelmap_ImageInfo指针。 |
| bool *isHdr | 表示是否为高动态范围（HDR）的信息。true表示是高动态范围的信息，false表示不是高动态范围的信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数校验错误。 |

**OH_PixelmapImageInfo_Release()**

```ets
Image_ErrorCode OH_PixelmapImageInfo_Release(OH_Pixelmap_ImageInfo *info)
```

描述

释放OH_Pixelmap_ImageInfo指针。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_ImageInfo *info | 被释放的OH_Pixelmap_ImageInfo指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_CreatePixelmap()**

```ets
Image_ErrorCode OH_PixelmapNative_CreatePixelmap(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options, OH_PixelmapNative **pixelmap)
```

描述

通过属性创建PixelMap，默认采用BGRA_8888格式处理数据，其他格式请参考[OH_PixelmapInitializationOptions_SetSrcPixelFormat](pixelmap_native.h.md#ZH-CN_TOPIC_0000002522241982__oh_pixelmapinitializationoptions_setsrcpixelformat)。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| uint8_t *data | BGRA_8888格式的颜色数组。 |
| size_t dataLength | 数组长度。 |
| OH_Pixelmap_InitializationOptions *options | 创建像素的属性。 |
| OH_PixelmapNative **pixelmap | 被创建的OH_PixelmapNative对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNSUPPORTED_OPERATION：操作不支持。 |

**OH_PixelmapNative_CreatePixelmapUsingAllocator()**

```ets
Image_ErrorCode OH_PixelmapNative_CreatePixelmapUsingAllocator(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options, IMAGE_ALLOCATOR_MODE allocator, OH_PixelmapNative **pixelmap)
```

描述

根据入参options创建pixelmap，pixelmap使用的内存类型可以通过allocator指定。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| uint8_t *data | BGRA_8888格式的数据。 |
| size_t dataLength | 数组长度。 |
| OH_Pixelmap_InitializationOptions *options | 创建pixelmap的选项。 |
| IMAGE_ALLOCATOR_MODE allocator | 决定pixelmap内存分配的类型。 |
| OH_PixelmapNative **pixelmap | 被创建的OH_PixelmapNative对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNSUPPORTED_OPERATION：操作不支持。  IMAGE_TOO_LARGE：图像过大，无法分配内存。  IMAGE_DMA_OPERATION_FAILED：DMA内存操作失败。  IMAGE_ALLOCATOR_MODE_UNSUPPORTED：不支持分配当前内存类型。例如，使用共享内存创建HDR图。 |

**OH_PixelmapNative_ConvertPixelmapNativeToNapi()**

```ets
Image_ErrorCode OH_PixelmapNative_ConvertPixelmapNativeToNapi(napi_env env, OH_PixelmapNative *pixelmapNative, napi_value *pixelmapNapi)
```

描述

将nativePixelMap对象转换为PixelMapnapi对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| napi_env env | napi的环境指针。 |
| OH_PixelmapNative *pixelmapNative | 被操作的OH_PixelmapNative指针。 |
| napi_value *pixelmapNapi | 转换出来的PixelMapnapi对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：pixelmapNative为空。 |

**OH_PixelmapNative_ConvertPixelmapNativeFromNapi()**

```ets
Image_ErrorCode OH_PixelmapNative_ConvertPixelmapNativeFromNapi(napi_env env, napi_value pixelmapNapi, OH_PixelmapNative **pixelmapNative)
```

描述

将PixelMapnapi对象转换为nativePixelMap对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| napi_env env | napi的环境指针。 |
| napi_value pixelmapNapi | 需要转换的PixelMapnapi对象。 |
| OH_PixelmapNative **pixelmapNative | 转换出的OH_PixelmapNative对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：pixelmapNative是nullptr，或者pixelmapNapi不是PixelMapNapi对象。 |

**OH_PixelmapNative_ReadPixels()**

```ets
Image_ErrorCode OH_PixelmapNative_ReadPixels(OH_PixelmapNative *pixelmap, uint8_t *destination, size_t *bufferSize)
```

描述

读取图像像素数据，并按照PixelMap的像素格式写入缓冲区中。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| uint8_t *destination | 缓冲区，获取的图像像素数据写入到该内存区域内。 |
| size_t *bufferSize | 缓冲区大小。RGBA格式的缓冲区大小等于width * height * 4，NV21与NV12格式的缓冲区大小等于width * height+((width+1)/2) * ((height+1)/2) * 2。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNKNOWN_ERROR：未知错误。 |

**OH_PixelmapNative_WritePixels()**

```ets
Image_ErrorCode OH_PixelmapNative_WritePixels(OH_PixelmapNative *pixelmap, uint8_t *source, size_t bufferSize)
```

描述

读取缓冲区中的图像像素数据，并按照PixelMap的像素格式将结果写入PixelMap。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| uint8_t *source | 图像像素数据。 |
| size_t bufferSize | 图像像素数据长度。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNSUPPORTED_OPERATION：操作不支持。  IMAGE_UNKNOWN_ERROR：未知错误。 |

**OH_PixelmapNative_ReadPixelsFromArea()**

```ets
Image_ErrorCode OH_PixelmapNative_ReadPixelsFromArea(OH_PixelmapNative *pixelmap, Image_PositionArea *area)
```

描述

从PixelMap的指定区域中读取像素数据并存入缓冲区。读取出来的数据为BGRA_8888格式。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被读取的PixelMap。 |
| Image_PositionArea *area | 读取数据的PixelMap指定区域。数据会被读取并拷贝至area->pixels。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_BAD_PARAMETER：参数无效，例如：pixelmap或area有误。  IMAGE_UNKNOWN_ERROR：未知的内部错误，例如：不支持的像素格式。 |

**OH_PixelmapNative_WritePixelsToArea()**

```ets
Image_ErrorCode OH_PixelmapNative_WritePixelsToArea(OH_PixelmapNative *pixelmap, Image_PositionArea *area)
```

描述

将缓冲区中的像素数据写入PixelMap的指定区域。数据源应为BGRA_8888格式。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被写入的PixelMap。 |
| Image_PositionArea *area | 写入数据的PixelMap指定区域。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_BAD_PARAMETER：参数无效，例如：pixelmap或area有误。  IMAGE_UNSUPPORTED_OPERATION：PixelMap不可编辑。  IMAGE_UNKNOWN_ERROR：未知的内部错误，例如：不支持的像素格式。 |

**OH_PixelmapNative_GetArgbPixels()**

```ets
Image_ErrorCode OH_PixelmapNative_GetArgbPixels(OH_PixelmapNative *pixelmap, uint8_t *destination, size_t *bufferSize)
```

描述

从PixelMap中读取ARGB格式的数据。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| uint8_t *destination | 缓冲区，获取的图像像素数据写入到该内存区域内。 |
| size_t *bufferSize | 缓冲区大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNSUPPORTED_CONVERSION：PixelMap格式不支持读取ARGB数据。  IMAGE_ALLOC_FAILED：内存申请失败。  IMAGE_COPY_FAILED：内存数据拷贝、读取、操作失败。 |

**OH_PixelmapNative_ToSdr()**

```ets
Image_ErrorCode OH_PixelmapNative_ToSdr(OH_PixelmapNative *pixelmap)
```

描述

将HDR的图像内容转换为SDR的图像内容。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNSUPPORTED_OPERATION：操作不支持。 |

**OH_PixelmapNative_GetImageInfo()**

```ets
Image_ErrorCode OH_PixelmapNative_GetImageInfo(OH_PixelmapNative *pixelmap, OH_Pixelmap_ImageInfo *imageInfo)
```

描述

获取图像像素信息。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| OH_Pixelmap_ImageInfo *imageInfo | 图像像素信息。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_Opacity()**

```ets
Image_ErrorCode OH_PixelmapNative_Opacity(OH_PixelmapNative *pixelmap, float rate)
```

描述

通过设置透明比率来让PixelMap达到对应的透明效果。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| float rate | 透明比率的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_Scale()**

```ets
Image_ErrorCode OH_PixelmapNative_Scale(OH_PixelmapNative *pixelmap, float scaleX, float scaleY)
```

描述

根据输入的宽高对图片进行缩放。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| float scaleX | 宽度的缩放比例。 |
| float scaleY | 高度的缩放比例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_ScaleWithAntiAliasing()**

```ets
Image_ErrorCode OH_PixelmapNative_ScaleWithAntiAliasing(OH_PixelmapNative *pixelmap, float scaleX, float scaleY, OH_PixelmapNative_AntiAliasingLevel level)
```

描述

根据指定的缩放算法和输入的宽高对图片进行缩放。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| float scaleX | 宽度的缩放比例。 |
| float scaleY | 高度的缩放比例。 |
| OH_PixelmapNative_AntiAliasingLevel level | 缩放算法。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_TOO_LARGE：图片过大。  IMAGE_ALLOC_FAILED：内存申请失败。  IMAGE_UNKNOWN_ERROR：pixelmap已经被释放。 |

**OH_PixelmapNative_CreateScaledPixelMap()**

```ets
Image_ErrorCode OH_PixelmapNative_CreateScaledPixelMap(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap, float scaleX, float scaleY)
```

描述

根据输入的宽高的缩放比例，创建一个新的缩放后的图片。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *srcPixelmap | 被操作的OH_PixelmapNative指针，源pixelmap对象指针。 |
| OH_PixelmapNative **dstPixelmap | 被操作的OH_PixelmapNative指针，目标pixelmap对象指针。 |
| float scaleX | 宽度的缩放比例。 |
| float scaleY | 高度的缩放比例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_CreateScaledPixelMapWithAntiAliasing()**

```ets
Image_ErrorCode OH_PixelmapNative_CreateScaledPixelMapWithAntiAliasing(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap, float scaleX, float scaleY, OH_PixelmapNative_AntiAliasingLevel level)
```

描述

根据指定的缩放算法和输入的宽高的缩放比例，创建一个新的缩放后的图片。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *srcPixelmap | 被操作的OH_PixelmapNative指针，源pixelmap对象指针。 |
| OH_PixelmapNative **dstPixelmap | 被操作的OH_PixelmapNative指针，目标pixelmap对象指针。 |
| float scaleX | 宽度的缩放比例。 |
| float scaleY | 高度的缩放比例。 |
| OH_PixelmapNative_AntiAliasingLevel level | 缩放算法。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_TOO_LARGE：图片过大。  IMAGE_ALLOC_FAILED：内存申请失败。 |

**OH_PixelmapNative_CreateAlphaPixelmap()**

```ets
Image_ErrorCode OH_PixelmapNative_CreateAlphaPixelmap(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap)
```

描述

从源PixelMap创建一个仅含有Alpha通道的PixelMap。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *srcPixelmap | 提供Alpha通道数据的源PixelMap。 |
| OH_PixelmapNative **dstPixelmap | 被创建的目标PixelMap。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_BAD_PARAMETER：参数无效，例如：srcPixelmap或dstPixelmap有误。 |

**OH_PixelmapNative_Clone()**

```ets
Image_ErrorCode OH_PixelmapNative_Clone(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap)
```

描述

从源PixelMap复制出一个新的PixelMap。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *srcPixelmap | 被复制的源PixelMap。 |
| OH_PixelmapNative **dstPixelmap | 被创建的目标PixelMap。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_BAD_PARAMETER：参数无效，例如：srcPixelmap或dstPixelmap有误。  IMAGE_UNSUPPORTED_DATA_FORMAT：像素格式不支持。  IMAGE_TOO_LARGE：源PixelMap的尺寸过大。  IMAGE_INIT_FAILED：目标PixelMap初始化失败。  IMAGE_ALLOC_FAILED：内存申请或数据复制失败。 |

**OH_PixelmapNative_CreateCroppedAndScaledPixelMap()**

```ets
Image_ErrorCode OH_PixelmapNative_CreateCroppedAndScaledPixelMap(OH_PixelmapNative *srcPixelmap, Image_Region *region, Image_Scale *scale, OH_PixelmapNative_AntiAliasingLevel level, OH_PixelmapNative **dstPixelmap)
```

描述

基于源PixelMap创建一个裁剪并缩放的新PixelMap。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *srcPixelmap | 源PixelMap。 |
| Image_Region *region | 裁剪区域。 |
| Image_Scale *scale | 宽和高的缩放倍数。不能为0。 |
| OH_PixelmapNative_AntiAliasingLevel level | 要使用的缩放插值算法。 |
| OH_PixelmapNative **dstPixelmap | 被创建的目标PixelMap。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_BAD_PARAMETER：参数无效，例如：srcPixelmap、region、scale或dstPixelmap有误。  IMAGE_UNSUPPORTED_DATA_FORMAT：像素格式不支持。  IMAGE_TOO_LARGE：源PixelMap的尺寸过大。  IMAGE_INIT_FAILED：目标PixelMap初始化失败。  IMAGE_ALLOC_FAILED：内存申请或数据复制失败。 |

**OH_PixelmapNative_Translate()**

```ets
Image_ErrorCode OH_PixelmapNative_Translate(OH_PixelmapNative *pixelmap, float x, float y)
```

描述

根据输入的坐标对图片进行位置变换。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| float x | 区域横坐标。 |
| float y | 区域纵坐标。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_Rotate()**

```ets
Image_ErrorCode OH_PixelmapNative_Rotate(OH_PixelmapNative *pixelmap, float angle)
```

描述

根据输入的角度对图片进行旋转。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| float angle | 图片旋转的角度，单位为deg。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_Flip()**

```ets
Image_ErrorCode OH_PixelmapNative_Flip(OH_PixelmapNative *pixelmap, bool shouldFlipHorizontally, bool shouldFlipVertically)
```

描述

根据输入的条件对图片进行翻转。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| bool shouldFlipHorizontally | 是否水平翻转图像。true表示进行水平翻转，false表示不进行水平翻转。 |
| bool shouldFlipVertically | 是否垂直翻转图像。true表示进行垂直翻转，false表示不进行垂直翻转。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_Crop()**

```ets
Image_ErrorCode OH_PixelmapNative_Crop(OH_PixelmapNative *pixelmap, Image_Region *region)
```

描述

根据输入的尺寸对图片进行裁剪。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| Image_Region *region | 裁剪的尺寸。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_Release()**

```ets
Image_ErrorCode OH_PixelmapNative_Release(OH_PixelmapNative *pixelmap)
```

描述

释放OH_PixelmapNative指针，推荐使用[OH_PixelmapNative_Destroy](pixelmap_native.h.md#ZH-CN_TOPIC_0000002522241982__oh_pixelmapnative_destroy)。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被释放的OH_PixelmapNative指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_Destroy()**

```ets
Image_ErrorCode OH_PixelmapNative_Destroy(OH_PixelmapNative **pixelmap)
```

描述

释放OH_PixelmapNative指针。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative **pixelmap | 被释放的OH_PixelmapNative指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_ConvertAlphaFormat()**

```ets
Image_ErrorCode OH_PixelmapNative_ConvertAlphaFormat(OH_PixelmapNative* srcpixelmap, OH_PixelmapNative* dstpixelmap, const bool isPremul)
```

描述

将pixelmap的像素数据做预乘和非预乘之间的转换。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative* srcpixelmap | 被操作的OH_PixelmapNative指针，源pixelmap对象指针。 |
| OH_PixelmapNative* dstpixelmap | 被操作的OH_PixelmapNative指针，目标pixelmap对象指针。 |
| const bool isPremul | 转换方式，true为非预乘转预乘，false为预乘转非预乘。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_CreateEmptyPixelmap()**

```ets
Image_ErrorCode OH_PixelmapNative_CreateEmptyPixelmap(OH_Pixelmap_InitializationOptions *options, OH_PixelmapNative **pixelmap)
```

描述

利用OH_Pixelmap_InitializationOptions创建空的pixelmap对象，内存数据为0。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 创建像素的属性。 |
| OH_PixelmapNative **pixelmap | 被创建的OH_PixelmapNative对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_CreateEmptyPixelmapUsingAllocator()**

```ets
Image_ErrorCode OH_PixelmapNative_CreateEmptyPixelmapUsingAllocator(OH_Pixelmap_InitializationOptions *options, IMAGE_ALLOCATOR_MODE allocator, OH_PixelmapNative **pixelmap)
```

描述

根据入参options创建空的pixelmap，pixelmap使用的内存类型可以通过allocator指定。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_Pixelmap_InitializationOptions *options | 创建pixelmap的选项。 |
| IMAGE_ALLOCATOR_MODE allocator | 决定pixelmap内存分配的类型。 |
| OH_PixelmapNative **pixelmap | 被创建的OH_PixelmapNative对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNSUPPORTED_OPERATION：操作不支持。  IMAGE_TOO_LARGE：图像过大，无法分配内存。  IMAGE_DMA_OPERATION_FAILED：DMA内存操作失败。  IMAGE_ALLOCATOR_MODE_UNSUPPORTED：不支持分配当前内存类型。例如，使用共享内存创建HDR图。 |

**OH_PixelmapNative_CreatePixelmapFromSurface()**

```ets
Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromSurface(const char *surfaceId, size_t length, OH_PixelmapNative **pixelmap)
```

描述

通过Surface的Surface ID创建一个PixelMap。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *surfaceId | Surface ID字符串。 |
| size_t length | Surface ID字符串的长度。 |
| OH_PixelmapNative **pixelmap | 被创建的PixelMap。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_BAD_PARAMETER：参数无效，例如：surfaceId或pixelmap有误。  IMAGE_CREATE_PIXELMAP_FAILED：PixelMap创建失败。 |

**OH_PixelmapNative_CreatePixelmapFromSurfaceWithTransformation()**

```ets
Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromSurfaceWithTransformation(const char *surfaceId, size_t length, bool transformEnabled, OH_PixelmapNative **pixelmap)
```

描述

通过Surface的ID创建一个预览流画面的PixelMap对象。该Surface可能携带旋转或翻转的变换信息。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| const char *surfaceId | 对应Surface的ID字符串。 |
| size_t length | 对应Surface的ID字符串长度。 |
| bool transformEnabled | 是否对携带变换信息的Surface预先进行逆变换来消除PixelMap的旋转或翻转效果。若Surface未携带变换信息，本参数不生效。  如果是true，则进行逆变换，变换的角度与Surface携带的角度一致且方向相反，输出的PixelMap无旋转或翻转效果；  如果是false，则不进行逆变换，输出的PixelMap会根据Surface中的变换信息而带有旋转或翻转效果。 |
| OH_PixelmapNative **pixelmap | 被创建的PixelMap。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_INVALID_PARAMETER：参数无效，例如：surfaceId或pixelmap有误。  IMAGE_UNSUPPORTED_OPERATION：不支持的操作，例如：跨平台时调用。  IMAGE_GET_IMAGE_DATA_FAILED：获取Surface的数据失败。  IMAGE_CREATE_PIXELMAP_FAILED：PixelMap创建失败。 |

参考：

[OH_PixelmapNative](OH_PixelmapNative.md)

**OH_PixelmapNative_CreatePixelmapFromNativeBuffer()**

```ets
Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromNativeBuffer(OH_NativeBuffer *nativeBuffer, OH_PixelmapNative **pixelmap)
```

描述

通过NativeBuffer创建一个PixelMap。如果NativeBuffer的用途未配置CPU访问权限，则不支持创建。

 支持创建的像素格式为RGBA_8888、NV21、NV12、YCBCR_P010、YCRCB_P010。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_NativeBuffer *nativeBuffer | 含有PixelMap数据的NativeBuffer对象。 |
| OH_PixelmapNative **pixelmap | 被创建的PixelMap。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_BAD_PARAMETER：参数无效，例如：nativeBuffer或pixelmap有误，像素格式不支持，或未配置CPU访问权限。  IMAGE_CREATE_PIXELMAP_FAILED：PixelMap创建失败。 |

**OH_PixelmapNative_GetNativeBuffer()**

```ets
Image_ErrorCode OH_PixelmapNative_GetNativeBuffer(OH_PixelmapNative *pixelmap, OH_NativeBuffer **nativeBuffer)
```

描述

从DMA内存的PixelMap中，获取NativeBuffer对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 要获取NativeBuffer的源PixelMap。 |
| OH_NativeBuffer **nativeBuffer | 被创建的NativeBuffer对象指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_DMA_NOT_EXIST：不是DMA内存。  IMAGE_DMA_OPERATION_FAILED：DMA内存操作失败。 |

**OH_PixelmapNative_GetMetadata()**

```ets
Image_ErrorCode OH_PixelmapNative_GetMetadata(OH_PixelmapNative *pixelmap, OH_Pixelmap_HdrMetadataKey key, OH_Pixelmap_HdrMetadataValue **value)
```

描述

获取元数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| OH_Pixelmap_HdrMetadataKey key | 元数据的关键字。 |
| OH_Pixelmap_HdrMetadataValue **value | 元数据的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_DMA_NOT_EXIST：不存在DMA内存。  IMAGE_COPY_FAILED：如果内存拷贝失败。 |

**OH_PixelmapNative_SetMetadata()**

```ets
Image_ErrorCode OH_PixelmapNative_SetMetadata(OH_PixelmapNative *pixelmap, OH_Pixelmap_HdrMetadataKey key, OH_Pixelmap_HdrMetadataValue *value)
```

描述

设置元数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| OH_Pixelmap_HdrMetadataKey key | 元数据的关键字。 |
| OH_Pixelmap_HdrMetadataValue *value | 元数据的值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_DMA_NOT_EXIST：不存在DMA内存。  IMAGE_COPY_FAILED：如果内存拷贝失败。 |

**OH_PixelmapNative_SetColorSpaceNative()**

```ets
Image_ErrorCode OH_PixelmapNative_SetColorSpaceNative(OH_PixelmapNative *pixelmap, OH_NativeColorSpaceManager *colorSpaceNative)
```

描述

设置NativeColorSpaceManager对象。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 要设置NativeColorSpaceManager的目标PixelMap。 |
| OH_NativeColorSpaceManager *colorSpaceNative | 要设置的NativeColorSpaceManager对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_GetColorSpaceNative()**

```ets
Image_ErrorCode OH_PixelmapNative_GetColorSpaceNative(OH_PixelmapNative *pixelmap, OH_NativeColorSpaceManager **colorSpaceNative)
```

描述

获取NativeColorSpaceManager对象。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 获取到NativeColorSpaceManager的源PixelMap。 |
| OH_NativeColorSpaceManager **colorSpaceNative | 获取到的NativeColorSpaceManager对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 |

**OH_PixelmapNative_SetMemoryName()**

```ets
Image_ErrorCode OH_PixelmapNative_SetMemoryName(OH_PixelmapNative *pixelmap, char *name, size_t *size)
```

描述

设置pixelMap内存名字。

起始版本： 13

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的OH_PixelmapNative指针。 |
| char *name | 需要被设置的PixelMap内存名称。 |
| size_t *size | 需要被设置的PixelMap内存名称的字节大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：名字长度超过取值范围。DMA内存名字取值范围为[1, 255]，ASHMEM内存名字取值范围为[1, 244]，单位字节。  IMAGE_UNSUPPORTED_MEMORY_FORMAT：既不是DMA内存也不是ASHMEM内存。 |

**OH_PixelmapNative_GetByteCount()**

```ets
Image_ErrorCode OH_PixelmapNative_GetByteCount(OH_PixelmapNative *pixelmap, uint32_t *byteCount)
```

描述

获取Pixelmap中所有像素所占用的总字节数，不包含内存填充。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的Pixelmap指针。 |
| uint32_t *byteCount | 获取的总字节数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：pixelmap或byteCount参数无效。 |

**OH_PixelmapNative_GetAllocationByteCount()**

```ets
Image_ErrorCode OH_PixelmapNative_GetAllocationByteCount(OH_PixelmapNative *pixelmap, uint32_t *allocationByteCount)
```

描述

获取Pixelmap用于储存像素数据的内存字节数。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的Pixelmap指针。 |
| uint32_t *allocationByteCount | 获取的内存字节数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：pixelmap或allocationByteCount参数无效。 |

**OH_PixelmapNative_AccessPixels()**

```ets
Image_ErrorCode OH_PixelmapNative_AccessPixels(OH_PixelmapNative *pixelmap, void **addr)
```

描述

获取Pixelmap像素数据的内存地址，并锁定这块内存。

 当该内存被锁定时，任何修改或释放该Pixelmap的像素数据的操作均会失败或无效。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的Pixelmap指针。 |
| void **addr | Pixelmap内存地址的双指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：pixelmap或addr参数无效。  IMAGE_LOCK_UNLOCK_FAILED：内存锁定失败。 |

**OH_PixelmapNative_UnaccessPixels()**

```ets
Image_ErrorCode OH_PixelmapNative_UnaccessPixels(OH_PixelmapNative *pixelmap)
```

描述

释放Pixelmap像素数据的内存锁。

 该函数需要与[OH_PixelmapNative_AccessPixels](pixelmap_native.h.md#ZH-CN_TOPIC_0000002522241982__oh_pixelmapnative_accesspixels)匹配使用。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被操作的Pixelmap指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：pixelmap参数无效。  IMAGE_LOCK_UNLOCK_FAILED：内存解锁失败。 |

**OH_PixelmapNative_GetUniqueId()**

```ets
Image_ErrorCode OH_PixelmapNative_GetUniqueId(OH_PixelmapNative *pixelmap, uint32_t *uniqueId)
```

描述

获取PixelMap的唯一ID。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 获取唯一ID的PixelMap。 |
| uint32_t *uniqueId | 获取的唯一ID。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_BAD_PARAMETER：参数无效，例如：pixelmap或uniqueId有误。 |

**OH_PixelmapNative_IsReleased()**

```ets
Image_ErrorCode OH_PixelmapNative_IsReleased(OH_PixelmapNative *pixelmap, bool *released)
```

描述

检测PixelMap是否已被释放。如果已被释放，则任何访问该对象内部数据的方法调用将会失效。

起始版本： 22

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PixelmapNative *pixelmap | 被检测的PixelMap。 |
| bool *released | 获取的PixelMap的释放状态。true表示已被释放，false表示未被释放。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_BAD_PARAMETER：参数无效，例如：pixelmap或released有误。 |