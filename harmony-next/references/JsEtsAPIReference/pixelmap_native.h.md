# pixelmap_native.h

#### 概述

访问Pixelmap的API。

**引用文件：** <multimedia/image_framework/image/pixelmap_native.h>

**库：** libpixelmap.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**相关模块：**[Image_NativeModule](Image_NativeModule.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_Pixelmap_HdrStaticMetadata](OH_Pixelmap_HdrStaticMetadata.md)OH_Pixelmap_HdrStaticMetadataHDR_STATIC_METADATA关键字对应的静态元数据值。[OH_Pixelmap_HdrDynamicMetadata](OH_Pixelmap_HdrDynamicMetadata.md)OH_Pixelmap_HdrDynamicMetadataDR_DYNAMIC_METADATA关键字对应的动态元数据值。[OH_Pixelmap_HdrGainmapMetadata](OH_Pixelmap_HdrGainmapMetadata.md)OH_Pixelmap_HdrGainmapMetadataHDR_GAINMAP_METADATA关键字对应的gainmap相关元数据值，参考ISO 21496-1。[OH_Pixelmap_HdrMetadataValue](OH_Pixelmap_HdrMetadataValue.md)OH_Pixelmap_HdrMetadataValuePixelmap使用的HDR元数据值，和OH_Pixelmap_HdrMetadataKey关键字相对应。用于[OH_PixelmapNative_SetMetadata](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_setmetadata)及[OH_PixelmapNative_GetMetadata](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getmetadata)，有相应[OH_Pixelmap_HdrMetadataKey](#ZH-CN_TOPIC_0000002529445819__oh_pixelmap_hdrmetadatakey)关键字作为入参时，设置或获取到本结构体中相对应的元数据类型的值。[OH_PixelmapNative](zh-cn_topic_0000002497445884.html)-

OH_PixelmapNative结构体是native层封装的图像解码后无压缩的位图格式结构体。

 函数创建OH_PixelmapNative使用[OH_PixelmapNative_CreatePixelmap](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createpixelmap)函数，默认采用BGRA_8888格式处理数据。

 释放OH_PixelmapNative对象使用[OH_PixelmapNative_Release](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_release)函数。

[OH_NativeBuffer](OH_NativeBuffer.md)-NativeBuffer结构体类型，用于执行NativeBuffer相关操作。[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md)OH_NativeColorSpaceManagerNativeColorSpaceManager结构体类型，用于执行NativeColorSpaceManager相关操作。[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md)-

OH_Pixelmap_InitializationOptions是native层封装的初始化参数结构体，用于设置Pixelmap的初始化参数。

 创建OH_Pixelmap_InitializationOptions对象使用[OH_PixelmapInitializationOptions_Create](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_create)函数。

 释放OH_Pixelmap_InitializationOptions对象使用[OH_PixelmapInitializationOptions_Release](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_release)函数。

[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md)-图像像素信息结构体。

#### 枚举

名称typedef关键字描述[PIXELMAP_ALPHA_TYPE](#ZH-CN_TOPIC_0000002529445819__pixelmap_alpha_type)PIXELMAP_ALPHA_TYPEPixelmap透明度类型。[PIXEL_FORMAT](#ZH-CN_TOPIC_0000002529445819__pixel_format)PIXEL_FORMAT图片像素格式。[OH_PixelmapNative_AntiAliasingLevel](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_antialiasinglevel)OH_PixelmapNative_AntiAliasingLevelPixelmap缩放时采用的缩放算法。[OH_Pixelmap_HdrMetadataKey](#ZH-CN_TOPIC_0000002529445819__oh_pixelmap_hdrmetadatakey)OH_Pixelmap_HdrMetadataKeyPixelmap使用的HDR相关元数据信息的关键字，用于[OH_PixelmapNative_SetMetadata](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_setmetadata)及[OH_PixelmapNative_GetMetadata](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getmetadata)。[OH_Pixelmap_HdrMetadataType](#ZH-CN_TOPIC_0000002529445819__oh_pixelmap_hdrmetadatatype)OH_Pixelmap_HdrMetadataTypeHDR_METADATA_TYPE关键字对应的值。

#### 函数

名称描述[Image_ErrorCode OH_PixelmapInitializationOptions_Create(OH_Pixelmap_InitializationOptions **options)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_create)创建OH_Pixelmap_InitializationOptions指针。[Image_ErrorCode OH_PixelmapInitializationOptions_GetWidth(OH_Pixelmap_InitializationOptions *options, uint32_t *width)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_getwidth)获取图片宽。[Image_ErrorCode OH_PixelmapInitializationOptions_SetWidth(OH_Pixelmap_InitializationOptions *options, uint32_t width)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_setwidth)设置图片宽。[Image_ErrorCode OH_PixelmapInitializationOptions_GetHeight(OH_Pixelmap_InitializationOptions *options, uint32_t *height)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_getheight)获取图片高。[Image_ErrorCode OH_PixelmapInitializationOptions_SetHeight(OH_Pixelmap_InitializationOptions *options, uint32_t height)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_setheight)设置图片高。[Image_ErrorCode OH_PixelmapInitializationOptions_GetPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t *pixelFormat)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_getpixelformat)获取像素格式。[Image_ErrorCode OH_PixelmapInitializationOptions_SetPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t pixelFormat)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_setpixelformat)设置像素格式。[Image_ErrorCode OH_PixelmapInitializationOptions_GetSrcPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t *srcpixelFormat)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_getsrcpixelformat)获取源像素格式。[Image_ErrorCode OH_PixelmapInitializationOptions_SetSrcPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t srcpixelFormat)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_setsrcpixelformat)设置源像素格式。[Image_ErrorCode OH_PixelmapInitializationOptions_GetRowStride(OH_Pixelmap_InitializationOptions *options, int32_t *rowStride)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_getrowstride)

获取行跨距。

跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width * 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。

[Image_ErrorCode OH_PixelmapInitializationOptions_SetRowStride(OH_Pixelmap_InitializationOptions *options, int32_t rowStride)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_setrowstride)

设置图像跨距。

跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width * 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。

[Image_ErrorCode OH_PixelmapInitializationOptions_GetAlphaType(OH_Pixelmap_InitializationOptions *options, int32_t *alphaType)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_getalphatype)获取透明度类型。[Image_ErrorCode OH_PixelmapInitializationOptions_SetAlphaType(OH_Pixelmap_InitializationOptions *options, int32_t alphaType)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_setalphatype)设置透明度类型。[Image_ErrorCode OH_PixelmapInitializationOptions_GetEditable(OH_Pixelmap_InitializationOptions *options, bool *editable)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_geteditable)获取可编辑标志。[Image_ErrorCode OH_PixelmapInitializationOptions_SetEditable(OH_Pixelmap_InitializationOptions *options, bool editable)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_seteditable)设置可编辑标志。[Image_ErrorCode OH_PixelmapInitializationOptions_Release(OH_Pixelmap_InitializationOptions *options)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_release)释放OH_Pixelmap_InitializationOptions指针。[Image_ErrorCode OH_PixelmapImageInfo_Create(OH_Pixelmap_ImageInfo **info)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_create)创建OH_Pixelmap_ImageInfo指针。[Image_ErrorCode OH_PixelmapImageInfo_GetWidth(OH_Pixelmap_ImageInfo *info, uint32_t *width)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getwidth)获取图片宽。[Image_ErrorCode OH_PixelmapImageInfo_GetHeight(OH_Pixelmap_ImageInfo *info, uint32_t *height)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getheight)获取图片高。[Image_ErrorCode OH_PixelmapImageInfo_GetAlphaMode(OH_Pixelmap_ImageInfo *info, int32_t *AlphaMode)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getalphamode)获取图片透明通道类型。[Image_ErrorCode OH_PixelmapImageInfo_GetRowStride(OH_Pixelmap_ImageInfo *info, uint32_t *rowStride)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getrowstride)获取行跨距。[Image_ErrorCode OH_PixelmapImageInfo_GetPixelFormat(OH_Pixelmap_ImageInfo *info, int32_t *pixelFormat)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getpixelformat)获取像素格式。[Image_ErrorCode OH_PixelmapImageInfo_GetAlphaType(OH_Pixelmap_ImageInfo *info, int32_t *alphaType)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getalphatype)获取OH_PixelmapImageInfo默认的透明通道类型。若要获取图片当前透明通道类型，请使用[OH_PixelmapImageInfo_GetAlphaMode](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getalphamode)。[Image_ErrorCode OH_PixelmapImageInfo_GetDynamicRange(OH_Pixelmap_ImageInfo *info, bool *isHdr)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getdynamicrange)获取Pixelmap是否为高动态范围的信息。[Image_ErrorCode OH_PixelmapImageInfo_Release(OH_Pixelmap_ImageInfo *info)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_release)释放OH_Pixelmap_ImageInfo指针。[Image_ErrorCode OH_PixelmapNative_CreatePixelmap(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options, OH_PixelmapNative **pixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createpixelmap)通过属性创建PixelMap，默认采用BGRA_8888格式处理数据，其他格式请参考[OH_PixelmapInitializationOptions_SetSrcPixelFormat](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_setsrcpixelformat)。[Image_ErrorCode OH_PixelmapNative_CreatePixelmapUsingAllocator(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options, IMAGE_ALLOCATOR_MODE allocator, OH_PixelmapNative **pixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createpixelmapusingallocator)根据入参options创建pixelmap，pixelmap使用的内存类型可以通过allocator指定。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。[Image_ErrorCode OH_PixelmapNative_ConvertPixelmapNativeToNapi(napi_env env, OH_PixelmapNative *pixelmapNative, napi_value *pixelmapNapi)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_convertpixelmapnativetonapi)将nativePixelMap对象转换为PixelMapnapi对象。[Image_ErrorCode OH_PixelmapNative_ConvertPixelmapNativeFromNapi(napi_env env, napi_value pixelmapNapi, OH_PixelmapNative **pixelmapNative)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_convertpixelmapnativefromnapi)将PixelMapnapi对象转换为nativePixelMap对象。[Image_ErrorCode OH_PixelmapNative_ReadPixels(OH_PixelmapNative *pixelmap, uint8_t *destination, size_t *bufferSize)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_readpixels)读取图像像素数据，并按照PixelMap的像素格式写入缓冲区中。[Image_ErrorCode OH_PixelmapNative_WritePixels(OH_PixelmapNative *pixelmap, uint8_t *source, size_t bufferSize)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_writepixels)读取缓冲区中的图像像素数据，并按照PixelMap的像素格式将结果写入PixelMap。[Image_ErrorCode OH_PixelmapNative_ReadPixelsFromArea(OH_PixelmapNative *pixelmap, Image_PositionArea *area)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_readpixelsfromarea)从PixelMap的指定区域中读取像素数据并存入缓冲区。读取出来的数据为BGRA_8888格式。[Image_ErrorCode OH_PixelmapNative_WritePixelsToArea(OH_PixelmapNative *pixelmap, Image_PositionArea *area)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_writepixelstoarea)将缓冲区中的像素数据写入PixelMap的指定区域。数据源应为BGRA_8888格式。[Image_ErrorCode OH_PixelmapNative_GetArgbPixels(OH_PixelmapNative *pixelmap, uint8_t *destination, size_t *bufferSize)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getargbpixels)从PixelMap中读取ARGB格式的数据。[Image_ErrorCode OH_PixelmapNative_ToSdr(OH_PixelmapNative *pixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_tosdr)将HDR的图像内容转换为SDR的图像内容。[Image_ErrorCode OH_PixelmapNative_GetImageInfo(OH_PixelmapNative *pixelmap, OH_Pixelmap_ImageInfo *imageInfo)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getimageinfo)获取图像像素信息。[Image_ErrorCode OH_PixelmapNative_Opacity(OH_PixelmapNative *pixelmap, float rate)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_opacity)通过设置透明比率来让PixelMap达到对应的透明效果。[Image_ErrorCode OH_PixelmapNative_Scale(OH_PixelmapNative *pixelmap, float scaleX, float scaleY)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_scale)根据输入的宽高对图片进行缩放。[Image_ErrorCode OH_PixelmapNative_ScaleWithAntiAliasing(OH_PixelmapNative *pixelmap, float scaleX, float scaleY, OH_PixelmapNative_AntiAliasingLevel level)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_scalewithantialiasing)根据指定的缩放算法和输入的宽高对图片进行缩放。[Image_ErrorCode OH_PixelmapNative_CreateScaledPixelMap(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap, float scaleX, float scaleY)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createscaledpixelmap)根据输入的宽高的缩放比例，创建一个新的缩放后的图片。[Image_ErrorCode OH_PixelmapNative_CreateScaledPixelMapWithAntiAliasing(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap, float scaleX, float scaleY, OH_PixelmapNative_AntiAliasingLevel level)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createscaledpixelmapwithantialiasing)根据指定的缩放算法和输入的宽高的缩放比例，创建一个新的缩放后的图片。[Image_ErrorCode OH_PixelmapNative_CreateAlphaPixelmap(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createalphapixelmap)从源PixelMap创建一个仅含有Alpha通道的PixelMap。[Image_ErrorCode OH_PixelmapNative_Clone(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_clone)从源PixelMap复制出一个新的PixelMap。[Image_ErrorCode OH_PixelmapNative_CreateCroppedAndScaledPixelMap(OH_PixelmapNative *srcPixelmap, Image_Region *region, Image_Scale *scale, OH_PixelmapNative_AntiAliasingLevel level, OH_PixelmapNative **dstPixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createcroppedandscaledpixelmap)基于源PixelMap创建一个裁剪并缩放的新PixelMap。[Image_ErrorCode OH_PixelmapNative_Translate(OH_PixelmapNative *pixelmap, float x, float y)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_translate)根据输入的坐标对图片进行位置变换。[Image_ErrorCode OH_PixelmapNative_Rotate(OH_PixelmapNative *pixelmap, float angle)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_rotate)根据输入的角度对图片进行旋转。[Image_ErrorCode OH_PixelmapNative_Flip(OH_PixelmapNative *pixelmap, bool shouldFilpHorizontally, bool shouldFilpVertically)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_flip)根据输入的条件对图片进行翻转。[Image_ErrorCode OH_PixelmapNative_Crop(OH_PixelmapNative *pixelmap, Image_Region *region)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_crop)根据输入的尺寸对图片进行裁剪。[Image_ErrorCode OH_PixelmapNative_Release(OH_PixelmapNative *pixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_release)释放OH_PixelmapNative指针，推荐使用[OH_PixelmapNative_Destroy](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_destroy)。[Image_ErrorCode OH_PixelmapNative_Destroy(OH_PixelmapNative **pixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_destroy)释放OH_PixelmapNative指针。[Image_ErrorCode OH_PixelmapNative_ConvertAlphaFormat(OH_PixelmapNative* srcpixelmap, OH_PixelmapNative* dstpixelmap, const bool isPremul)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_convertalphaformat)将pixelmap的像素数据做预乘和非预乘之间的转换。[Image_ErrorCode OH_PixelmapNative_CreateEmptyPixelmap(OH_Pixelmap_InitializationOptions *options, OH_PixelmapNative **pixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createemptypixelmap)利用OH_Pixelmap_InitializationOptions创建空的pixelmap对象，内存数据为0。[Image_ErrorCode OH_PixelmapNative_CreateEmptyPixelmapUsingAllocator(OH_Pixelmap_InitializationOptions *options, IMAGE_ALLOCATOR_MODE allocator, OH_PixelmapNative **pixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createemptypixelmapusingallocator)根据入参options创建空的pixelmap，pixelmap使用的内存类型可以通过allocator指定。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。[Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromSurface(const char *surfaceId, size_t length, OH_PixelmapNative **pixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createpixelmapfromsurface)通过Surface的Surface ID创建一个PixelMap。[Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromNativeBuffer(OH_NativeBuffer *nativeBuffer, OH_PixelmapNative **pixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_createpixelmapfromnativebuffer)

通过NativeBuffer创建一个PixelMap。如果NativeBuffer的用途未配置CPU访问权限，则不支持创建。

 支持创建的像素格式为RGBA_8888、NV21、NV12、YCBCR_P010、YCRCB_P010。

[Image_ErrorCode OH_PixelmapNative_GetNativeBuffer(OH_PixelmapNative *pixelmap, OH_NativeBuffer **nativeBuffer)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getnativebuffer)从DMA内存的PixelMap中，获取NativeBuffer对象。[Image_ErrorCode OH_PixelmapNative_GetMetadata(OH_PixelmapNative *pixelmap, OH_Pixelmap_HdrMetadataKey key, OH_Pixelmap_HdrMetadataValue **value)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getmetadata)获取元数据。[Image_ErrorCode OH_PixelmapNative_SetMetadata(OH_PixelmapNative *pixelmap, OH_Pixelmap_HdrMetadataKey key, OH_Pixelmap_HdrMetadataValue *value)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_setmetadata)设置元数据。[Image_ErrorCode OH_PixelmapNative_SetColorSpaceNative(OH_PixelmapNative *pixelmap, OH_NativeColorSpaceManager *colorSpaceNative)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_setcolorspacenative)设置NativeColorSpaceManager对象。[Image_ErrorCode OH_PixelmapNative_GetColorSpaceNative(OH_PixelmapNative *pixelmap, OH_NativeColorSpaceManager **colorSpaceNative)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getcolorspacenative)获取NativeColorSpaceManager对象。[Image_ErrorCode OH_PixelmapNative_SetMemoryName(OH_PixelmapNative *pixelmap, char *name, size_t *size)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_setmemoryname)设置pixelMap内存名字。[Image_ErrorCode OH_PixelmapNative_GetByteCount(OH_PixelmapNative *pixelmap, uint32_t *byteCount)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getbytecount)获取Pixelmap中所有像素所占用的总字节数，不包含内存填充。[Image_ErrorCode OH_PixelmapNative_GetAllocationByteCount(OH_PixelmapNative *pixelmap, uint32_t *allocationByteCount)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getallocationbytecount)获取Pixelmap用于储存像素数据的内存字节数。[Image_ErrorCode OH_PixelmapNative_AccessPixels(OH_PixelmapNative *pixelmap, void **addr)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_accesspixels)

获取Pixelmap像素数据的内存地址，并锁定这块内存。

当该内存被锁定时，任何修改或释放该Pixelmap的像素数据的操作均会失败或无效。

[Image_ErrorCode OH_PixelmapNative_UnaccessPixels(OH_PixelmapNative *pixelmap)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_unaccesspixels)

释放Pixelmap像素数据的内存锁。

该函数需要与[OH_PixelmapNative_AccessPixels](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_accesspixels)匹配使用。

[Image_ErrorCode OH_PixelmapNative_GetUniqueId(OH_PixelmapNative *pixelmap, uint32_t *uniqueId)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getuniqueid)获取PixelMap的唯一ID。[Image_ErrorCode OH_PixelmapNative_IsReleased(OH_PixelmapNative *pixelmap, bool *released)](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_isreleased)检测PixelMap是否已被释放。如果已被释放，则任何访问该对象内部数据的方法调用将会失效。

#### 枚举类型说明

#### PIXELMAP_ALPHA_TYPE

```ets
enum PIXELMAP_ALPHA_TYPE
```

**描述**

Pixelmap透明度类型。

**起始版本：** 12

枚举项描述PIXELMAP_ALPHA_TYPE_UNKNOWN = 0未知格式。PIXELMAP_ALPHA_TYPE_OPAQUE = 1不透明的格式。PIXELMAP_ALPHA_TYPE_PREMULTIPLIED = 2预乘透明度格式。PIXELMAP_ALPHA_TYPE_UNPREMULTIPLIED = 3非预乘透明度格式。

#### PIXEL_FORMAT

```ets
enum PIXEL_FORMAT
```

**描述**

图片像素格式。

**起始版本：** 12

枚举项描述PIXEL_FORMAT_UNKNOWN = 0未知格式。PIXEL_FORMAT_RGB_565 = 2RGB_565格式。PIXEL_FORMAT_RGBA_8888 = 3RGBA_8888格式。PIXEL_FORMAT_BGRA_8888 = 4BGRA_8888格式。PIXEL_FORMAT_RGB_888 = 5RGB_888格式。PIXEL_FORMAT_ALPHA_8 = 6ALPHA_8格式。PIXEL_FORMAT_RGBA_F16 = 7RGBA_F16格式。PIXEL_FORMAT_NV21 = 8NV21格式。PIXEL_FORMAT_NV12 = 9NV12格式。PIXEL_FORMAT_RGBA_1010102 = 10RGBA_1010102格式。PIXEL_FORMAT_YCBCR_P010 = 11YCBCR_P010格式。PIXEL_FORMAT_YCRCB_P010 =12YCRCB_P010格式。

#### OH_PixelmapNative_AntiAliasingLevel

```ets
enum OH_PixelmapNative_AntiAliasingLevel
```

**描述**

Pixelmap缩放时采用的缩放算法。

**起始版本：** 12

枚举项描述OH_PixelmapNative_AntiAliasing_NONE = 0最近邻插值算法。OH_PixelmapNative_AntiAliasing_LOW = 1双线性插值算法。OH_PixelmapNative_AntiAliasing_MEDIUM = 2双线性插值算法，同时开启Mipmap。缩小图片时建议使用。OH_PixelmapNative_AntiAliasing_HIGH = 3三次插值算法。

#### OH_Pixelmap_HdrMetadataKey

```ets
enum OH_Pixelmap_HdrMetadataKey
```

**描述**

Pixelmap使用的HDR相关元数据信息的关键字，用于[OH_PixelmapNative_SetMetadata](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_setmetadata)及[OH_PixelmapNative_GetMetadata](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_getmetadata)。

**起始版本：** 12

枚举项描述HDR_METADATA_TYPE = 0Pixelmap使用的元数据类型。HDR_STATIC_METADATA = 1静态元数据。HDR_DYNAMIC_METADATA = 2动态元数据。HDR_GAINMAP_METADATA = 3Gainmap使用的元数据。

#### OH_Pixelmap_HdrMetadataType

```ets
enum OH_Pixelmap_HdrMetadataType
```

**描述**

HDR_METADATA_TYPE关键字对应的值。

**起始版本：** 12

枚举项描述HDR_METADATA_TYPE_NONE = 0无元数据内容。HDR_METADATA_TYPE_BASE = 1表示用于基础图的元数据。HDR_METADATA_TYPE_GAINMAP = 2表示用于Gainmap图的元数据。HDR_METADATA_TYPE_ALTERNATE = 3表示用于合成后HDR图的元数据。

#### 函数说明

#### OH_PixelmapInitializationOptions_Create()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_Create(OH_Pixelmap_InitializationOptions **options)
```

**描述**

创建OH_Pixelmap_InitializationOptions指针。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) **options被创建的OH_Pixelmap_InitializationOptions指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_GetWidth()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetWidth(OH_Pixelmap_InitializationOptions *options, uint32_t *width)
```

**描述**

获取图片宽。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。uint32_t *width图片的宽，单位：像素。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_SetWidth()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetWidth(OH_Pixelmap_InitializationOptions *options, uint32_t width)
```

**描述**

设置图片宽。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。uint32_t width图片的宽，单位：像素。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_GetHeight()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetHeight(OH_Pixelmap_InitializationOptions *options, uint32_t *height)
```

**描述**

获取图片高。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。uint32_t *height图片的高，单位：像素。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_SetHeight()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetHeight(OH_Pixelmap_InitializationOptions *options, uint32_t height)
```

**描述**

设置图片高。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。uint32_t height图片的高，单位：像素。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_GetPixelFormat()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t *pixelFormat)
```

**描述**

获取像素格式。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。int32_t *pixelFormat像素格式[PIXEL_FORMAT](#ZH-CN_TOPIC_0000002529445819__pixel_format)。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_SetPixelFormat()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t pixelFormat)
```

**描述**

设置像素格式。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。int32_t pixelFormat像素格式[PIXEL_FORMAT](#ZH-CN_TOPIC_0000002529445819__pixel_format)。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_GetSrcPixelFormat()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetSrcPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t *srcpixelFormat)
```

**描述**

获取源像素格式。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。int32_t *srcpixelFormat像素格式[PIXEL_FORMAT](#ZH-CN_TOPIC_0000002529445819__pixel_format)。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_SetSrcPixelFormat()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetSrcPixelFormat(OH_Pixelmap_InitializationOptions *options, int32_t srcpixelFormat)
```

**描述**

设置源像素格式。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。int32_t srcpixelFormat源像素格式[PIXEL_FORMAT](#ZH-CN_TOPIC_0000002529445819__pixel_format)。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_GetRowStride()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetRowStride(OH_Pixelmap_InitializationOptions *options, int32_t *rowStride)
```

**描述**

获取行跨距。

 跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width * 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。int32_t *rowStride跨距，单位：字节。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNKNOWN_ERROR：options被释放。

#### OH_PixelmapInitializationOptions_SetRowStride()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetRowStride(OH_Pixelmap_InitializationOptions *options, int32_t rowStride)
```

**描述**

设置图像跨距。

跨距，图像每行占用的真实内存大小，单位为字节。跨距 = width * 单位像素字节数 + padding，padding为每行为内存对齐做的填充区域。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。int32_t rowStride跨距，单位：字节。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNKNOWN_ERROR：options被释放。

#### OH_PixelmapInitializationOptions_GetAlphaType()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetAlphaType(OH_Pixelmap_InitializationOptions *options, int32_t *alphaType)
```

**描述**

获取透明度类型。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。int32_t *alphaType透明度类型[PIXELMAP_ALPHA_TYPE](#ZH-CN_TOPIC_0000002529445819__pixelmap_alpha_type)。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_SetAlphaType()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetAlphaType(OH_Pixelmap_InitializationOptions *options, int32_t alphaType)
```

**描述**

设置透明度类型。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。int32_t alphaType透明度类型[PIXELMAP_ALPHA_TYPE](#ZH-CN_TOPIC_0000002529445819__pixelmap_alpha_type)。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_GetEditable()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_GetEditable(OH_Pixelmap_InitializationOptions *options, bool *editable)
```

**描述**

获取可编辑标志。

**起始版本：** 18

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。bool *editable可编辑标志。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_SetEditable()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_SetEditable(OH_Pixelmap_InitializationOptions *options, bool editable)
```

**描述**

设置可编辑标志。

**起始版本：** 18

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被操作的OH_Pixelmap_InitializationOptions指针。bool editable可编辑标志。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapInitializationOptions_Release()

```ets
Image_ErrorCode OH_PixelmapInitializationOptions_Release(OH_Pixelmap_InitializationOptions *options)
```

**描述**

释放OH_Pixelmap_InitializationOptions指针。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options被释放的OH_Pixelmap_InitializationOptions指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapImageInfo_Create()

```ets
Image_ErrorCode OH_PixelmapImageInfo_Create(OH_Pixelmap_ImageInfo **info)
```

**描述**

创建OH_Pixelmap_ImageInfo指针。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md) **info被创建的OH_Pixelmap_ImageInfo指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapImageInfo_GetWidth()

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetWidth(OH_Pixelmap_ImageInfo *info, uint32_t *width)
```

**描述**

获取图片宽。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md) *info被操作的OH_Pixelmap_ImageInfo指针。uint32_t *width图片宽，单位：像素。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapImageInfo_GetHeight()

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetHeight(OH_Pixelmap_ImageInfo *info, uint32_t *height)
```

**描述**

获取图片高。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md) *info被操作的OH_Pixelmap_ImageInfo指针。uint32_t *height图片高，单位：像素。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapImageInfo_GetAlphaMode()

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetAlphaMode(OH_Pixelmap_ImageInfo *info, int32_t *AlphaMode)
```

**描述**

获取图片透明通道类型。

**起始版本：** 20

**参数：**

参数项描述[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md) *info被操作的OH_Pixelmap_ImageInfo指针。int32_t *AlphaMode被操作的alpha格式的指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapImageInfo_GetRowStride()

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetRowStride(OH_Pixelmap_ImageInfo *info, uint32_t *rowStride)
```

**描述**

获取行跨距。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md) *info被操作的OH_Pixelmap_ImageInfo指针。uint32_t *rowStride跨距，内存中每行像素所占的空间。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapImageInfo_GetPixelFormat()

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetPixelFormat(OH_Pixelmap_ImageInfo *info, int32_t *pixelFormat)
```

**描述**

获取像素格式。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md) *info被操作的OH_Pixelmap_ImageInfo指针。int32_t *pixelFormat像素格式[PIXEL_FORMAT](#ZH-CN_TOPIC_0000002529445819__pixel_format)。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapImageInfo_GetAlphaType()

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetAlphaType(OH_Pixelmap_ImageInfo *info, int32_t *alphaType)
```

**描述**

获取OH_PixelmapImageInfo默认的透明通道类型。若要获取图片当前透明通道类型，请使用[OH_PixelmapImageInfo_GetAlphaMode](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapimageinfo_getalphamode)。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md) *info被操作的OH_Pixelmap_ImageInfo指针。int32_t *alphaType透明度类型[PIXELMAP_ALPHA_TYPE](#ZH-CN_TOPIC_0000002529445819__pixelmap_alpha_type)。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapImageInfo_GetDynamicRange()

```ets
Image_ErrorCode OH_PixelmapImageInfo_GetDynamicRange(OH_Pixelmap_ImageInfo *info, bool *isHdr)
```

**描述**

获取Pixelmap是否为高动态范围的信息。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md) *info被操作的OH_Pixelmap_ImageInfo指针。bool *isHdr表示是否为HDR。true表示是HDR，false表示不是HDR。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数校验错误。

#### OH_PixelmapImageInfo_Release()

```ets
Image_ErrorCode OH_PixelmapImageInfo_Release(OH_Pixelmap_ImageInfo *info)
```

**描述**

释放OH_Pixelmap_ImageInfo指针。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md) *info被释放的OH_Pixelmap_ImageInfo指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_CreatePixelmap()

```ets
Image_ErrorCode OH_PixelmapNative_CreatePixelmap(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options, OH_PixelmapNative **pixelmap)
```

**描述**

通过属性创建PixelMap，默认采用BGRA_8888格式处理数据，其他格式请参考[OH_PixelmapInitializationOptions_SetSrcPixelFormat](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapinitializationoptions_setsrcpixelformat)。

**起始版本：** 12

**参数：**

参数项描述uint8_t *dataBGRA_8888格式的颜色数组。size_t dataLength数组长度。[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options创建像素的属性。[OH_PixelmapNative](OH_PixelmapNative.md) **pixelmap被创建的OH_PixelmapNative对象指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_OPERATION：操作不支持。

#### OH_PixelmapNative_CreatePixelmapUsingAllocator()

```ets
Image_ErrorCode OH_PixelmapNative_CreatePixelmapUsingAllocator(uint8_t *data, size_t dataLength, OH_Pixelmap_InitializationOptions *options, IMAGE_ALLOCATOR_MODE allocator, OH_PixelmapNative **pixelmap)
```

**描述**

根据入参options创建pixelmap，pixelmap使用的内存类型可以通过allocator指定。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。

**起始版本：** 20

**参数：**

参数项描述uint8_t *dataBGRA_8888格式的数据。size_t dataLength数组长度。[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options创建pixelmap的选项。[IMAGE_ALLOCATOR_MODE](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_allocator_mode) allocator决定pixelmap内存分配的类型。[OH_PixelmapNative](OH_PixelmapNative.md) **pixelmap被创建的OH_PixelmapNative对象指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_OPERATION：操作不支持。

 IMAGE_TOO_LARGE：图像过大，无法分配内存。

 IMAGE_DMA_OPERATION_FAILED：DMA内存操作失败。

 IMAGE_ALLOCATOR_MODE_UNSUPPORTED：不支持分配当前内存类型。例如，使用共享内存创建HDR图。

#### OH_PixelmapNative_ConvertPixelmapNativeToNapi()

```ets
Image_ErrorCode OH_PixelmapNative_ConvertPixelmapNativeToNapi(napi_env env, OH_PixelmapNative *pixelmapNative, napi_value *pixelmapNapi)
```

**描述**

将nativePixelMap对象转换为PixelMapnapi对象。

**起始版本：** 12

**参数：**

参数项描述napi_env envnapi的环境指针。[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmapNative被操作的OH_PixelmapNative指针。napi_value *pixelmapNapi转换出来的PixelMapnapi对象指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：pixelmapNative为空。

#### OH_PixelmapNative_ConvertPixelmapNativeFromNapi()

```ets
Image_ErrorCode OH_PixelmapNative_ConvertPixelmapNativeFromNapi(napi_env env, napi_value pixelmapNapi, OH_PixelmapNative **pixelmapNative)
```

**描述**

将PixelMapnapi对象转换为nativePixelMap对象。

**起始版本：** 12

**参数：**

参数项描述napi_env envnapi的环境指针。napi_value pixelmapNapi需要转换的PixelMapnapi对象。[OH_PixelmapNative](OH_PixelmapNative.md) **pixelmapNative转换出的OH_PixelmapNative对象指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：pixelmapNative是nullptr，或者pixelmapNapi不是PixelMapNapi对象。

#### OH_PixelmapNative_ReadPixels()

```ets
Image_ErrorCode OH_PixelmapNative_ReadPixels(OH_PixelmapNative *pixelmap, uint8_t *destination, size_t *bufferSize)
```

**描述**

读取图像像素数据，并按照PixelMap的像素格式写入缓冲区中。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。uint8_t *destination缓冲区，获取的图像像素数据写入到该内存区域内。size_t *bufferSize缓冲区大小。RGBA格式的缓冲区大小等于width * height * 4，NV21与NV12格式的缓冲区大小等于width * height+((width+1)/2) * ((height+1)/2) * 2。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNKNOWN_ERROR：未知错误。

#### OH_PixelmapNative_WritePixels()

```ets
Image_ErrorCode OH_PixelmapNative_WritePixels(OH_PixelmapNative *pixelmap, uint8_t *source, size_t bufferSize)
```

**描述**

读取缓冲区中的图像像素数据，并按照PixelMap的像素格式将结果写入PixelMap。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。uint8_t *source图像像素数据。size_t bufferSize图像像素数据长度。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_OPERATION：操作不支持。

 IMAGE_UNKNOWN_ERROR：未知错误。

#### OH_PixelmapNative_ReadPixelsFromArea()

```ets
Image_ErrorCode OH_PixelmapNative_ReadPixelsFromArea(OH_PixelmapNative *pixelmap, Image_PositionArea *area)
```

**描述**

从PixelMap的指定区域中读取像素数据并存入缓冲区。读取出来的数据为BGRA_8888格式。

**起始版本：** 22

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被读取的PixelMap。[Image_PositionArea](Image_PositionArea.md) *area读取数据的PixelMap指定区域。数据会被读取并拷贝至area->pixels。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：操作成功。

 IMAGE_BAD_PARAMETER：参数无效，例如：pixelmap或area有误。

 IMAGE_UNKNOWN_ERROR：未知的内部错误，例如：不支持的像素格式。

#### OH_PixelmapNative_WritePixelsToArea()

```ets
Image_ErrorCode OH_PixelmapNative_WritePixelsToArea(OH_PixelmapNative *pixelmap, Image_PositionArea *area)
```

**描述**

将缓冲区中的像素数据写入PixelMap的指定区域。数据源应为BGRA_8888格式。

**起始版本：** 22

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被写入的PixelMap。[Image_PositionArea](Image_PositionArea.md) *area写入数据的PixelMap指定区域。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：操作成功。

 IMAGE_BAD_PARAMETER：参数无效，例如：pixelmap或area有误。

 IMAGE_UNSUPPORTED_OPERATION：PixelMap不可编辑。

 IMAGE_UNKNOWN_ERROR：未知的内部错误，例如：不支持的像素格式。

#### OH_PixelmapNative_GetArgbPixels()

```ets
Image_ErrorCode OH_PixelmapNative_GetArgbPixels(OH_PixelmapNative *pixelmap, uint8_t *destination, size_t *bufferSize)
```

**描述**

从PixelMap中读取ARGB格式的数据。

**起始版本：** 13

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。uint8_t *destination缓冲区，获取的图像像素数据写入到该内存区域内。size_t *bufferSize缓冲区大小。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_CONVERSION：PixelMap格式不支持读取ARGB数据。

 IMAGE_ALLOC_FAILED：内存申请失败。

 IMAGE_COPY_FAILED：内存数据拷贝、读取、操作失败。

#### OH_PixelmapNative_ToSdr()

```ets
Image_ErrorCode OH_PixelmapNative_ToSdr(OH_PixelmapNative *pixelmap)
```

**描述**

将HDR的图像内容转换为SDR的图像内容。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_OPERATION：操作不支持。

#### OH_PixelmapNative_GetImageInfo()

```ets
Image_ErrorCode OH_PixelmapNative_GetImageInfo(OH_PixelmapNative *pixelmap, OH_Pixelmap_ImageInfo *imageInfo)
```

**描述**

获取图像像素信息。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。[OH_Pixelmap_ImageInfo](OH_Pixelmap_ImageInfo.md) *imageInfo图像像素信息。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_Opacity()

```ets
Image_ErrorCode OH_PixelmapNative_Opacity(OH_PixelmapNative *pixelmap, float rate)
```

**描述**

通过设置透明比率来让PixelMap达到对应的透明效果。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。float rate透明比率的值。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_Scale()

```ets
Image_ErrorCode OH_PixelmapNative_Scale(OH_PixelmapNative *pixelmap, float scaleX, float scaleY)
```

**描述**

根据输入的宽高对图片进行缩放。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。float scaleX宽度的缩放比例。float scaleY高度的缩放比例。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_ScaleWithAntiAliasing()

```ets
Image_ErrorCode OH_PixelmapNative_ScaleWithAntiAliasing(OH_PixelmapNative *pixelmap, float scaleX, float scaleY, OH_PixelmapNative_AntiAliasingLevel level)
```

**描述**

根据指定的缩放算法和输入的宽高对图片进行缩放。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。float scaleX宽度的缩放比例。float scaleY高度的缩放比例。[OH_PixelmapNative_AntiAliasingLevel](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_antialiasinglevel) level缩放算法。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_TOO_LARGE：图片过大。

 IMAGE_ALLOC_FAILED：内存申请失败。

 IMAGE_UNKNOWN_ERROR：pixelmap已经被释放。

#### OH_PixelmapNative_CreateScaledPixelMap()

```ets
Image_ErrorCode OH_PixelmapNative_CreateScaledPixelMap(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap, float scaleX, float scaleY)
```

**描述**

根据输入的宽高的缩放比例，创建一个新的缩放后的图片。

**起始版本：** 18

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *srcPixelmap被操作的OH_PixelmapNative指针，源pixelmap对象指针。[OH_PixelmapNative](OH_PixelmapNative.md) **dstPixelmap被操作的OH_PixelmapNative指针，目标pixelmap对象指针。float scaleX宽度的缩放比例。float scaleY高度的缩放比例。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_CreateScaledPixelMapWithAntiAliasing()

```ets
Image_ErrorCode OH_PixelmapNative_CreateScaledPixelMapWithAntiAliasing(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap, float scaleX, float scaleY, OH_PixelmapNative_AntiAliasingLevel level)
```

**描述**

根据指定的缩放算法和输入的宽高的缩放比例，创建一个新的缩放后的图片。

**起始版本：** 18

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *srcPixelmap被操作的OH_PixelmapNative指针，源pixelmap对象指针。[OH_PixelmapNative](OH_PixelmapNative.md) **dstPixelmap被操作的OH_PixelmapNative指针，目标pixelmap对象指针。float scaleX宽度的缩放比例。float scaleY高度的缩放比例。[OH_PixelmapNative_AntiAliasingLevel](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_antialiasinglevel) level缩放算法。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_TOO_LARGE：图片过大。

 IMAGE_ALLOC_FAILED：内存申请失败。

#### OH_PixelmapNative_CreateAlphaPixelmap()

```ets
Image_ErrorCode OH_PixelmapNative_CreateAlphaPixelmap(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap)
```

**描述**

从源PixelMap创建一个仅含有Alpha通道的PixelMap。

**起始版本：** 22

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *srcPixelmap提供Alpha通道数据的源PixelMap。[OH_PixelmapNative](OH_PixelmapNative.md) **dstPixelmap被创建的目标PixelMap。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：操作成功。

 IMAGE_BAD_PARAMETER：参数无效，例如：srcPixelmap或dstPixelmap有误。

#### OH_PixelmapNative_Clone()

```ets
Image_ErrorCode OH_PixelmapNative_Clone(OH_PixelmapNative *srcPixelmap, OH_PixelmapNative **dstPixelmap)
```

**描述**

从源PixelMap复制出一个新的PixelMap。

**起始版本：** 22

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *srcPixelmap被复制的源PixelMap。[OH_PixelmapNative](OH_PixelmapNative.md) **dstPixelmap被创建的目标PixelMap。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：操作成功。

 IMAGE_BAD_PARAMETER：参数无效，例如：srcPixelmap或dstPixelmap有误。

 IMAGE_UNSUPPORTED_DATA_FORMAT：像素格式不支持。

 IMAGE_TOO_LARGE：源PixelMap的尺寸过大。

 IMAGE_INIT_FAILED：目标PixelMap初始化失败。

 IMAGE_ALLOC_FAILED：内存申请或数据复制失败。

#### OH_PixelmapNative_CreateCroppedAndScaledPixelMap()

```ets
Image_ErrorCode OH_PixelmapNative_CreateCroppedAndScaledPixelMap(OH_PixelmapNative *srcPixelmap, Image_Region *region, Image_Scale *scale, OH_PixelmapNative_AntiAliasingLevel level, OH_PixelmapNative **dstPixelmap)
```

**描述**

基于源PixelMap创建一个裁剪并缩放的新PixelMap。

**起始版本：** 22

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *srcPixelmap源PixelMap。[Image_Region](Image_Region.md) *region裁剪区域。[Image_Scale](Image_Scale.md) *scale宽和高的缩放倍数。不能为0。[OH_PixelmapNative_AntiAliasingLevel](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_antialiasinglevel) level要使用的缩放插值算法。[OH_PixelmapNative](zh-cn_topic_0000002497445884.html) **dstPixelmap被创建的目标PixelMap。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：操作成功。

 IMAGE_BAD_PARAMETER：参数无效，例如：srcPixelmap、region、scale或dstPixelmap有误。

 IMAGE_UNSUPPORTED_DATA_FORMAT：像素格式不支持。

 IMAGE_TOO_LARGE：源PixelMap的尺寸过大。

 IMAGE_INIT_FAILED：目标PixelMap初始化失败。

 IMAGE_ALLOC_FAILED：内存申请或数据复制失败。

#### OH_PixelmapNative_Translate()

```ets
Image_ErrorCode OH_PixelmapNative_Translate(OH_PixelmapNative *pixelmap, float x, float y)
```

**描述**

根据输入的坐标对图片进行位置变换。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。float x区域横坐标。float y区域纵坐标。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_Rotate()

```ets
Image_ErrorCode OH_PixelmapNative_Rotate(OH_PixelmapNative *pixelmap, float angle)
```

**描述**

根据输入的角度对图片进行旋转。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。float angle图片旋转的角度，单位为deg。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_Flip()

```ets
Image_ErrorCode OH_PixelmapNative_Flip(OH_PixelmapNative *pixelmap, bool shouldFilpHorizontally, bool shouldFilpVertically)
```

**描述**

根据输入的条件对图片进行翻转。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。bool shouldFilpHorizontally是否水平翻转图像。bool shouldFilpVertically是否垂直翻转图像。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_Crop()

```ets
Image_ErrorCode OH_PixelmapNative_Crop(OH_PixelmapNative *pixelmap, Image_Region *region)
```

**描述**

根据输入的尺寸对图片进行裁剪。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。[Image_Region](Image_Region.md) *region裁剪的尺寸。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_Release()

```ets
Image_ErrorCode OH_PixelmapNative_Release(OH_PixelmapNative *pixelmap)
```

**描述**

释放OH_PixelmapNative指针，推荐使用[OH_PixelmapNative_Destroy](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_destroy)。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被释放的OH_PixelmapNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_Destroy()

```ets
Image_ErrorCode OH_PixelmapNative_Destroy(OH_PixelmapNative **pixelmap)
```

**描述**

释放OH_PixelmapNative指针。

**起始版本：** 18

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) **pixelmap被释放的OH_PixelmapNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_ConvertAlphaFormat()

```ets
Image_ErrorCode OH_PixelmapNative_ConvertAlphaFormat(OH_PixelmapNative* srcpixelmap, OH_PixelmapNative* dstpixelmap, const bool isPremul)
```

**描述**

将pixelmap的像素数据做预乘和非预乘之间的转换。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md)* srcpixelmap被操作的OH_PixelmapNative指针，源pixelmap对象指针。[OH_PixelmapNative](OH_PixelmapNative.md)* dstpixelmap被操作的OH_PixelmapNative指针，目标pixelmap对象指针。const bool isPremul转换方式，true为非预乘转预乘，false为预乘转非预乘。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_CreateEmptyPixelmap()

```ets
Image_ErrorCode OH_PixelmapNative_CreateEmptyPixelmap(OH_Pixelmap_InitializationOptions *options, OH_PixelmapNative **pixelmap)
```

**描述**

利用OH_Pixelmap_InitializationOptions创建空的pixelmap对象，内存数据为0。

**起始版本：** 12

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options创建像素的属性。[OH_PixelmapNative](OH_PixelmapNative.md) **pixelmap被创建的OH_PixelmapNative对象指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_CreateEmptyPixelmapUsingAllocator()

```ets
Image_ErrorCode OH_PixelmapNative_CreateEmptyPixelmapUsingAllocator(OH_Pixelmap_InitializationOptions *options, IMAGE_ALLOCATOR_MODE allocator, OH_PixelmapNative **pixelmap)
```

**描述**

根据入参options创建空的pixelmap，pixelmap使用的内存类型可以通过allocator指定。默认情况下，系统会根据图像类型、图像大小、平台能力等选择内存类型。在处理此接口返回的像素图时，需要考虑步长影响。

**起始版本：** 20

**参数：**

参数项描述[OH_Pixelmap_InitializationOptions](OH_Pixelmap_InitializationOptions.md) *options创建pixelmap的选项。[IMAGE_ALLOCATOR_MODE](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_allocator_mode) allocator决定pixelmap内存分配的类型。[OH_PixelmapNative](OH_PixelmapNative.md) **pixelmap被创建的OH_PixelmapNative对象指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_OPERATION：操作不支持。

 IMAGE_TOO_LARGE：图像过大，无法分配内存。

 IMAGE_DMA_OPERATION_FAILED：DMA内存操作失败。

 IMAGE_ALLOCATOR_MODE_UNSUPPORTED：不支持分配当前内存类型。例如，使用共享内存创建HDR图。

#### OH_PixelmapNative_CreatePixelmapFromSurface()

```ets
Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromSurface(const char *surfaceId, size_t length, OH_PixelmapNative **pixelmap)
```

**描述**

通过Surface的Surface ID创建一个PixelMap。

**起始版本：** 22

**参数：**

参数项描述const char *surfaceIdSurface ID字符串。size_t lengthSurface ID字符串的长度。[OH_PixelmapNative](OH_PixelmapNative.md) **pixelmap被创建的PixelMap。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：操作成功。

 IMAGE_BAD_PARAMETER：参数无效，例如：surfaceId或pixelmap有误。

 IMAGE_CREATE_PIXELMAP_FAILED：PixelMap创建失败。

#### OH_PixelmapNative_CreatePixelmapFromNativeBuffer()

```ets
Image_ErrorCode OH_PixelmapNative_CreatePixelmapFromNativeBuffer(OH_NativeBuffer *nativeBuffer, OH_PixelmapNative **pixelmap)
```

**描述**

通过NativeBuffer创建一个PixelMap。如果NativeBuffer的用途未配置CPU访问权限，则不支持创建。

 支持创建的像素格式为RGBA_8888、NV21、NV12、YCBCR_P010、YCRCB_P010。

**起始版本：** 22

**参数：**

参数项描述[OH_NativeBuffer](OH_NativeBuffer.md) *nativeBuffer含有PixelMap数据的NativeBuffer对象。[OH_PixelmapNative](OH_PixelmapNative.md) **pixelmap被创建的PixelMap。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：操作成功。

 IMAGE_BAD_PARAMETER：参数无效，例如：nativeBuffer或pixelmap有误，像素格式不支持，或未配置CPU访问权限。

 IMAGE_CREATE_PIXELMAP_FAILED：PixelMap创建失败。

#### OH_PixelmapNative_GetNativeBuffer()

```ets
Image_ErrorCode OH_PixelmapNative_GetNativeBuffer(OH_PixelmapNative *pixelmap, OH_NativeBuffer **nativeBuffer)
```

**描述**

从DMA内存的PixelMap中，获取NativeBuffer对象。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap要获取NativeBuffer的源PixelMap。[OH_NativeBuffer](OH_NativeBuffer.md) **nativeBuffer被创建的NativeBuffer对象指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_DMA_NOT_EXIST：不是DMA内存。

 IMAGE_DMA_OPERATION_FAILED：DMA内存操作失败。

#### OH_PixelmapNative_GetMetadata()

```ets
Image_ErrorCode OH_PixelmapNative_GetMetadata(OH_PixelmapNative *pixelmap, OH_Pixelmap_HdrMetadataKey key, OH_Pixelmap_HdrMetadataValue **value)
```

**描述**

获取元数据。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。[OH_Pixelmap_HdrMetadataKey](#ZH-CN_TOPIC_0000002529445819__oh_pixelmap_hdrmetadatakey) key元数据的关键字。[OH_Pixelmap_HdrMetadataValue](zh-cn_topic_0000002529445831.html) **value元数据的值。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_DMA_NOT_EXIST：不存在DMA内存。

 IMAGE_COPY_FAILED：如果内存拷贝失败。

#### OH_PixelmapNative_SetMetadata()

```ets
Image_ErrorCode OH_PixelmapNative_SetMetadata(OH_PixelmapNative *pixelmap, OH_Pixelmap_HdrMetadataKey key, OH_Pixelmap_HdrMetadataValue *value)
```

**描述**

设置元数据。

**起始版本：** 12

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。[OH_Pixelmap_HdrMetadataKey](#ZH-CN_TOPIC_0000002529445819__oh_pixelmap_hdrmetadatakey) key元数据的关键字。[OH_Pixelmap_HdrMetadataValue](zh-cn_topic_0000002529445831.html) *value元数据的值。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_DMA_NOT_EXIST：不存在DMA内存。

 IMAGE_COPY_FAILED：如果内存拷贝失败。

#### OH_PixelmapNative_SetColorSpaceNative()

```ets
Image_ErrorCode OH_PixelmapNative_SetColorSpaceNative(OH_PixelmapNative *pixelmap, OH_NativeColorSpaceManager *colorSpaceNative)
```

**描述**

设置NativeColorSpaceManager对象。

**起始版本：** 13

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap要设置NativeColorSpaceManager的目标PixelMap。[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md) *colorSpaceNative要设置的NativeColorSpaceManager对象。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_GetColorSpaceNative()

```ets
Image_ErrorCode OH_PixelmapNative_GetColorSpaceNative(OH_PixelmapNative *pixelmap, OH_NativeColorSpaceManager **colorSpaceNative)
```

**描述**

获取NativeColorSpaceManager对象。

**起始版本：** 13

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap获取到NativeColorSpaceManager的源PixelMap。[OH_NativeColorSpaceManager](OH_NativeColorSpaceManager.md) **colorSpaceNative获取到的NativeColorSpaceManager对象。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：参数错误。

#### OH_PixelmapNative_SetMemoryName()

```ets
Image_ErrorCode OH_PixelmapNative_SetMemoryName(OH_PixelmapNative *pixelmap, char *name, size_t *size)
```

**描述**

设置pixelMap内存名字。

**起始版本：** 13

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的OH_PixelmapNative指针。char *name需要被设置的PixelMap内存名称。size_t *size需要被设置的PixelMap内存名称的字节大小。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：名字长度超过取值范围。DMA内存名字取值范围为[1, 255]，ASHMEM内存名字取值范围为[1, 244]，单位字节。

 IMAGE_UNSUPPORTED_MEMORY_FORMAT：既不是DMA内存也不是ASHMEM内存。

#### OH_PixelmapNative_GetByteCount()

```ets
Image_ErrorCode OH_PixelmapNative_GetByteCount(OH_PixelmapNative *pixelmap, uint32_t *byteCount)
```

**描述**

获取Pixelmap中所有像素所占用的总字节数，不包含内存填充。

**起始版本：** 18

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的Pixelmap指针。uint32_t *byteCount获取的总字节数。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：pixelmap或byteCount参数无效。

#### OH_PixelmapNative_GetAllocationByteCount()

```ets
Image_ErrorCode OH_PixelmapNative_GetAllocationByteCount(OH_PixelmapNative *pixelmap, uint32_t *allocationByteCount)
```

**描述**

获取Pixelmap用于储存像素数据的内存字节数。

**起始版本：** 18

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的Pixelmap指针。uint32_t *allocationByteCount获取的内存字节数。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：pixelmap或allocationByteCount参数无效。

#### OH_PixelmapNative_AccessPixels()

```ets
Image_ErrorCode OH_PixelmapNative_AccessPixels(OH_PixelmapNative *pixelmap, void **addr)
```

**描述**

获取Pixelmap像素数据的内存地址，并锁定这块内存。

 当该内存被锁定时，任何修改或释放该Pixelmap的像素数据的操作均会失败或无效。

**起始版本：** 15

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的Pixelmap指针。void **addrPixelmap内存地址的双指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：pixelmap或addr参数无效。

 IMAGE_LOCK_UNLOCK_FAILED：内存锁定失败。

#### OH_PixelmapNative_UnaccessPixels()

```ets
Image_ErrorCode OH_PixelmapNative_UnaccessPixels(OH_PixelmapNative *pixelmap)
```

**描述**

释放Pixelmap像素数据的内存锁。

 该函数需要与[OH_PixelmapNative_AccessPixels](#ZH-CN_TOPIC_0000002529445819__oh_pixelmapnative_accesspixels)匹配使用。

**起始版本：** 15

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被操作的Pixelmap指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

 IMAGE_BAD_PARAMETER：pixelmap参数无效。

 IMAGE_LOCK_UNLOCK_FAILED：内存解锁失败。

#### OH_PixelmapNative_GetUniqueId()

```ets
Image_ErrorCode OH_PixelmapNative_GetUniqueId(OH_PixelmapNative *pixelmap, uint32_t *uniqueId)
```

**描述**

获取PixelMap的唯一ID。

**起始版本：** 22

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap获取唯一ID的PixelMap。uint32_t *uniqueId获取的唯一ID。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：操作成功。

 IMAGE_BAD_PARAMETER：参数无效，例如：pixelmap或uniqueId有误。

#### OH_PixelmapNative_IsReleased()

```ets
Image_ErrorCode OH_PixelmapNative_IsReleased(OH_PixelmapNative *pixelmap, bool *released)
```

**描述**

检测PixelMap是否已被释放。如果已被释放，则任何访问该对象内部数据的方法调用将会失效。

**起始版本：** 22

**参数：**

参数项描述[OH_PixelmapNative](OH_PixelmapNative.md) *pixelmap被检测的PixelMap。bool *releasedPixelMap是否已被释放。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：操作成功。

 IMAGE_BAD_PARAMETER：参数无效，例如：pixelmap或released有误。