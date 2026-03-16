# picture_native.h

#### 概述

提供获取picture数据和信息的API。

**引用文件：** <multimedia/image_framework/image/picture_native.h>

**库：** libpicture.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 13

**相关模块：**[Image_NativeModule](../../topics/graphics/Image_NativeModule.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_PictureNative](../../topics/media/OH_PictureNative.md)OH_PictureNativePicture结构体类型，用于执行picture相关操作。[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md)OH_AuxiliaryPictureNativeAuxiliaryPicture结构体类型，用于执行AuxiliaryPicture相关操作。[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md)OH_AuxiliaryPictureInfoAuxiliaryPictureInfo结构体类型，用于执行AuxiliaryPictureInfo相关操作。

#### 枚举

名称typedef关键字描述[Image_AuxiliaryPictureType](#ZH-CN_TOPIC_0000002529285845__image_auxiliarypicturetype)Image_AuxiliaryPictureType辅助图类型。

#### 函数

名称描述[Image_ErrorCode OH_PictureNative_CreatePicture(OH_PixelmapNative *mainPixelmap, OH_PictureNative **picture)](#ZH-CN_TOPIC_0000002529285845__oh_picturenative_createpicture)创建OH_PictureNative指针。[Image_ErrorCode OH_PictureNative_GetMainPixelmap(OH_PictureNative *picture, OH_PixelmapNative **mainPixelmap)](#ZH-CN_TOPIC_0000002529285845__oh_picturenative_getmainpixelmap)获取主图的OH_PixelmapNative指针。[Image_ErrorCode OH_PictureNative_GetHdrComposedPixelmap(OH_PictureNative *picture, OH_PixelmapNative **hdrPixelmap)](#ZH-CN_TOPIC_0000002529285845__oh_picturenative_gethdrcomposedpixelmap)获取hdr图的OH_PixelmapNative指针。[Image_ErrorCode OH_PictureNative_GetGainmapPixelmap(OH_PictureNative *picture, OH_PixelmapNative **gainmapPixelmap)](#ZH-CN_TOPIC_0000002529285845__oh_picturenative_getgainmappixelmap)获取增益图的OH_PixelmapNative指针。[Image_ErrorCode OH_PictureNative_SetAuxiliaryPicture(OH_PictureNative *picture, Image_AuxiliaryPictureType type,OH_AuxiliaryPictureNative *auxiliaryPicture)](#ZH-CN_TOPIC_0000002529285845__oh_picturenative_setauxiliarypicture)设置辅助图。[Image_ErrorCode OH_PictureNative_GetAuxiliaryPicture(OH_PictureNative *picture, Image_AuxiliaryPictureType type,OH_AuxiliaryPictureNative **auxiliaryPicture)](#ZH-CN_TOPIC_0000002529285845__oh_picturenative_getauxiliarypicture)根据类型获取辅助图。[Image_ErrorCode OH_PictureNative_GetMetadata(OH_PictureNative *picture, Image_MetadataType metadataType,OH_PictureMetadata **metadata)](#ZH-CN_TOPIC_0000002529285845__oh_picturenative_getmetadata)获取主图的元数据。[Image_ErrorCode OH_PictureNative_SetMetadata(OH_PictureNative *picture, Image_MetadataType metadataType,OH_PictureMetadata *metadata)](#ZH-CN_TOPIC_0000002529285845__oh_picturenative_setmetadata)设置主图的元数据。[Image_ErrorCode OH_PictureNative_Release(OH_PictureNative *picture)](#ZH-CN_TOPIC_0000002529285845__oh_picturenative_release)释放OH_PictureNative指针。[Image_ErrorCode OH_AuxiliaryPictureNative_Create(uint8_t *data, size_t dataLength, Image_Size *size,Image_AuxiliaryPictureType type, OH_AuxiliaryPictureNative **auxiliaryPicture)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypicturenative_create)创建OH_AuxiliaryPictureNative指针。该接口仅支持传入[像素格式](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__pixel_format)为BGRA_8888的连续像素数据，会创建出RGBA_8888的辅助图。[Image_ErrorCode OH_AuxiliaryPictureNative_WritePixels(OH_AuxiliaryPictureNative *auxiliaryPicture, uint8_t *source,size_t bufferSize)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypicturenative_writepixels)读取缓冲区的图像像素数据，并将结果写入辅助图中。[Image_ErrorCode OH_AuxiliaryPictureNative_ReadPixels(OH_AuxiliaryPictureNative *auxiliaryPicture, uint8_t *destination,size_t *bufferSize)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypicturenative_readpixels)读取辅助图的像素数据，结果写入缓冲区。[Image_ErrorCode OH_AuxiliaryPictureNative_GetType(OH_AuxiliaryPictureNative *auxiliaryPicture,Image_AuxiliaryPictureType *type)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypicturenative_gettype)获取辅助图类型。[Image_ErrorCode OH_AuxiliaryPictureNative_GetInfo(OH_AuxiliaryPictureNative *auxiliaryPicture,OH_AuxiliaryPictureInfo **info)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypicturenative_getinfo)获取辅助图信息。[Image_ErrorCode OH_AuxiliaryPictureNative_SetInfo(OH_AuxiliaryPictureNative *auxiliaryPicture,OH_AuxiliaryPictureInfo *info)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypicturenative_setinfo)设置辅助图信息。[Image_ErrorCode OH_AuxiliaryPictureNative_GetMetadata(OH_AuxiliaryPictureNative *auxiliaryPicture,Image_MetadataType metadataType, OH_PictureMetadata **metadata)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypicturenative_getmetadata)获取辅助图的元数据。[Image_ErrorCode OH_AuxiliaryPictureNative_SetMetadata(OH_AuxiliaryPictureNative *auxiliaryPicture,Image_MetadataType metadataType, OH_PictureMetadata *metadata)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypicturenative_setmetadata)设置辅助图的元数据。[Image_ErrorCode OH_AuxiliaryPictureNative_Release(OH_AuxiliaryPictureNative *picture)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypicturenative_release)释放OH_AuxiliaryPictureNative指针。[Image_ErrorCode OH_AuxiliaryPictureInfo_Create(OH_AuxiliaryPictureInfo **info)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypictureinfo_create)创建一个OH_AuxiliaryPictureInfo对象。[Image_ErrorCode OH_AuxiliaryPictureInfo_GetType(OH_AuxiliaryPictureInfo *info, Image_AuxiliaryPictureType *type)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypictureinfo_gettype)获取OH_AuxiliaryPictureInfo中的辅助图类型。[Image_ErrorCode OH_AuxiliaryPictureInfo_SetType(OH_AuxiliaryPictureInfo *info, Image_AuxiliaryPictureType type)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypictureinfo_settype)设置OH_AuxiliaryPictureInfo中的辅助图类型。[Image_ErrorCode OH_AuxiliaryPictureInfo_GetSize(OH_AuxiliaryPictureInfo *info, Image_Size *size)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypictureinfo_getsize)获取OH_AuxiliaryPictureInfo中的图片尺寸。[Image_ErrorCode OH_AuxiliaryPictureInfo_SetSize(OH_AuxiliaryPictureInfo *info, Image_Size *size)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypictureinfo_setsize)设置OH_AuxiliaryPictureInfo中的图片尺寸。[Image_ErrorCode OH_AuxiliaryPictureInfo_GetRowStride(OH_AuxiliaryPictureInfo *info, uint32_t *rowStride)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypictureinfo_getrowstride)获取OH_AuxiliaryPictureInfo中的行跨距。[Image_ErrorCode OH_AuxiliaryPictureInfo_SetRowStride(OH_AuxiliaryPictureInfo *info, uint32_t rowStride)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypictureinfo_setrowstride)设置OH_AuxiliaryPictureInfo中的行跨距。[Image_ErrorCode OH_AuxiliaryPictureInfo_GetPixelFormat(OH_AuxiliaryPictureInfo *info, PIXEL_FORMAT *pixelFormat)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypictureinfo_getpixelformat)获取OH_AuxiliaryPictureInfo中的像素格式。[Image_ErrorCode OH_AuxiliaryPictureInfo_SetPixelFormat(OH_AuxiliaryPictureInfo *info, PIXEL_FORMAT pixelFormat)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypictureinfo_setpixelformat)设置OH_AuxiliaryPictureInfo中的像素格式。[Image_ErrorCode OH_AuxiliaryPictureInfo_Release(OH_AuxiliaryPictureInfo *info)](#ZH-CN_TOPIC_0000002529285845__oh_auxiliarypictureinfo_release)释放OH_AuxiliaryPictureInfo指针。

#### 枚举类型说明

#### Image_AuxiliaryPictureType

```ets
enum Image_AuxiliaryPictureType
```

**描述**

辅助图类型

**起始版本：** 13

枚举项描述AUXILIARY_PICTURE_TYPE_GAINMAP = 1增益图，代表了一种增强SDR图像以产生具有可变显示调整能力的HDR图像的机制。它是一组描述如何应用gainmap元数据的组合。AUXILIARY_PICTURE_TYPE_DEPTH_MAP = 2深度图，储存图像的深度数据，通过捕捉每个像素与摄像机之间的距离，提供场景的三维结构信息，通常用于3D重建和场景理解。AUXILIARY_PICTURE_TYPE_UNREFOCUS_MAP = 3人像未对焦的原图，提供了一种在人像拍摄中突出背景模糊效果的方式，能够帮助用户在后期处理中选择焦点区域，增加创作自由度。AUXILIARY_PICTURE_TYPE_LINEAR_MAP = 4线性图，用于提供额外的数据视角或补充信息，通常用于视觉效果的增强，它可以包含场景中光照、颜色或其他视觉元素的线性表示。AUXILIARY_PICTURE_TYPE_FRAGMENT_MAP = 5水印裁剪图，表示在原图中被水印覆盖的区域，该图像用于修复或移除水印影响，恢复图像的完整性和可视性。

#### 函数说明

#### OH_PictureNative_CreatePicture()

```ets
Image_ErrorCode OH_PictureNative_CreatePicture(OH_PixelmapNative *mainPixelmap, OH_PictureNative **picture)
```

**描述**

创建OH_PictureNative指针。

**起始版本：** 13

**参数：**

参数项描述[OH_PixelmapNative](../../topics/media/OH_PictureNative.md) *mainPixelmap主图的OH_PixelmapNative指针。[OH_PictureNative](../../topics/media/OH_PictureNative.md) **picture被创建的OH_PictureNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_PictureNative_GetMainPixelmap()

```ets
Image_ErrorCode OH_PictureNative_GetMainPixelmap(OH_PictureNative *picture, OH_PixelmapNative **mainPixelmap)
```

**描述**

获取主图的OH_PixelmapNative指针。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureNative](../../topics/media/OH_PictureNative.md) *picture被操作的OH_PictureNative指针。[OH_PictureNative](../../topics/media/OH_PictureNative.md) **mainPixelmap获取的OH_PixelmapNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_PictureNative_GetHdrComposedPixelmap()

```ets
Image_ErrorCode OH_PictureNative_GetHdrComposedPixelmap(OH_PictureNative *picture, OH_PixelmapNative **hdrPixelmap)
```

**描述**

获取hdr图的OH_PixelmapNative指针。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureNative](../../topics/media/OH_PictureNative.md) *picture被操作的OH_PictureNative指针。[OH_PictureNative](../../topics/media/OH_PictureNative.md) **hdrPixelmap获取的hdr图OH_PixelmapNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_OPERATION：操作不支持，例如picture对象中不包含增益图。

#### OH_PictureNative_GetGainmapPixelmap()

```ets
Image_ErrorCode OH_PictureNative_GetGainmapPixelmap(OH_PictureNative *picture, OH_PixelmapNative **gainmapPixelmap)
```

**描述**

获取增益图的OH_PixelmapNative指针。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureNative](../../topics/media/OH_PictureNative.md) *picture被操作的OH_PictureNative指针。[OH_PictureNative](../../topics/media/OH_PictureNative.md) **gainmapPixelmap获取的增益图OH_PixelmapNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_PictureNative_SetAuxiliaryPicture()

```ets
Image_ErrorCode OH_PictureNative_SetAuxiliaryPicture(OH_PictureNative *picture, Image_AuxiliaryPictureType type,OH_AuxiliaryPictureNative *auxiliaryPicture)
```

**描述**

设置辅助图。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureNative](../../topics/media/OH_PictureNative.md) *picture被操作的OH_PictureNative指针。[Image_AuxiliaryPictureType](#ZH-CN_TOPIC_0000002529285845__image_auxiliarypicturetype) type辅助图的类型。[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) *auxiliaryPicture设置的OH_AuxiliaryPictureNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_PictureNative_GetAuxiliaryPicture()

```ets
Image_ErrorCode OH_PictureNative_GetAuxiliaryPicture(OH_PictureNative *picture, Image_AuxiliaryPictureType type,OH_AuxiliaryPictureNative **auxiliaryPicture)
```

**描述**

根据类型获取辅助图。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureNative](../../topics/media/OH_PictureNative.md) *picture被操作的OH_PictureNative指针。[Image_AuxiliaryPictureType](#ZH-CN_TOPIC_0000002529285845__image_auxiliarypicturetype) type辅助图类型。[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) **auxiliaryPicture获取的OH_AuxiliaryPictureNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_PictureNative_GetMetadata()

```ets
Image_ErrorCode OH_PictureNative_GetMetadata(OH_PictureNative *picture, Image_MetadataType metadataType,OH_PictureMetadata **metadata)
```

**描述**

获取主图的元数据。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureNative](../../topics/media/OH_PictureNative.md) *picture被操作的OH_PictureNative指针。[Image_MetadataType](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_metadatatype) metadataType元数据类型。[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) **metadata主图的元数据。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_METADATA：不支持的元数据类型。

#### OH_PictureNative_SetMetadata()

```ets
Image_ErrorCode OH_PictureNative_SetMetadata(OH_PictureNative *picture, Image_MetadataType metadataType,OH_PictureMetadata *metadata)
```

**描述**

设置主图的元数据。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureNative](../../topics/media/OH_PictureNative.md) *picture被操作的OH_PictureNative指针。[Image_MetadataType](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_metadatatype) metadataType元数据类型。[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) *metadata将设置的元数据。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_METADATA：不支持的元数据类型。

#### OH_PictureNative_Release()

```ets
Image_ErrorCode OH_PictureNative_Release(OH_PictureNative *picture)
```

**描述**

释放OH_PictureNative指针。

**起始版本：** 13

**参数：**

参数项描述[OH_PictureNative](../../topics/media/OH_PictureNative.md) *picture被操作的OH_PictureNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureNative_Create()

```ets
Image_ErrorCode OH_AuxiliaryPictureNative_Create(uint8_t *data, size_t dataLength, Image_Size *size,Image_AuxiliaryPictureType type, OH_AuxiliaryPictureNative **auxiliaryPicture)
```

**描述**

创建OH_AuxiliaryPictureNative指针。该接口仅支持传入[像素格式](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__pixel_format)为BGRA_8888的连续像素数据，会创建出RGBA_8888的辅助图。

**起始版本：** 13

**参数：**

参数项描述uint8_t *data图像数据。size_t dataLength图像数据长度。[Image_Size](../../topics/graphics/Image_Size.md) *size辅助图尺寸。[Image_AuxiliaryPictureType](#ZH-CN_TOPIC_0000002529285845__image_auxiliarypicturetype) type辅助图类型。[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) **auxiliaryPicture被创建的OH_AuxiliaryPictureNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureNative_WritePixels()

```ets
Image_ErrorCode OH_AuxiliaryPictureNative_WritePixels(OH_AuxiliaryPictureNative *auxiliaryPicture, uint8_t *source,size_t bufferSize)
```

**描述**

读取缓冲区的图像像素数据，并将结果写入辅助图中。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) *auxiliaryPicture被操作的OH_AuxiliaryPictureNative指针。uint8_t *source将被写入的图像像素数据。size_t bufferSize图像像素数据长度。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_ALLOC_FAILED：内存分配失败。

 IMAGE_COPY_FAILED：内存拷贝失败。

#### OH_AuxiliaryPictureNative_ReadPixels()

```ets
Image_ErrorCode OH_AuxiliaryPictureNative_ReadPixels(OH_AuxiliaryPictureNative *auxiliaryPicture, uint8_t *destination,size_t *bufferSize)
```

**描述**

读取辅助图的像素数据，结果写入缓冲区。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) *auxiliaryPicture被操作的OH_AuxiliaryPictureNative指针。uint8_t *destination缓冲区，获取的辅助图像素数据写入到该内存区域内。size_t *bufferSize缓冲区大小。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_ALLOC_FAILED：内存分配失败。

 IMAGE_COPY_FAILED：内存拷贝失败。

#### OH_AuxiliaryPictureNative_GetType()

```ets
Image_ErrorCode OH_AuxiliaryPictureNative_GetType(OH_AuxiliaryPictureNative *auxiliaryPicture,Image_AuxiliaryPictureType *type)
```

**描述**

获取辅助图类型。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) *auxiliaryPicture被操作的OH_AuxiliaryPictureNative指针。[Image_AuxiliaryPictureType](#ZH-CN_TOPIC_0000002529285845__image_auxiliarypicturetype) *type辅助图类型。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureNative_GetInfo()

```ets
Image_ErrorCode OH_AuxiliaryPictureNative_GetInfo(OH_AuxiliaryPictureNative *auxiliaryPicture,OH_AuxiliaryPictureInfo **info)
```

**描述**

获取辅助图信息。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) *auxiliaryPicture被操作的OH_AuxiliaryPictureNative指针。[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) **info辅助图信息。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureNative_SetInfo()

```ets
Image_ErrorCode OH_AuxiliaryPictureNative_SetInfo(OH_AuxiliaryPictureNative *auxiliaryPicture,OH_AuxiliaryPictureInfo *info)
```

**描述**

设置辅助图信息。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) *auxiliaryPicture将操作的OH_AuxiliaryPictureNative指针。[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) *info将要设置的辅助图信息。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureNative_GetMetadata()

```ets
Image_ErrorCode OH_AuxiliaryPictureNative_GetMetadata(OH_AuxiliaryPictureNative *auxiliaryPicture,Image_MetadataType metadataType, OH_PictureMetadata **metadata)
```

**描述**

获取辅助图的元数据。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) *auxiliaryPicture将操作的OH_AuxiliaryPictureNative指针。[Image_MetadataType](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_metadatatype) metadataType元数据类型。[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) **metadata获取的元数据。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_METADATA：不支持的元数据类型，或者元数据类型与辅助图片类型不匹配。

#### OH_AuxiliaryPictureNative_SetMetadata()

```ets
Image_ErrorCode OH_AuxiliaryPictureNative_SetMetadata(OH_AuxiliaryPictureNative *auxiliaryPicture,Image_MetadataType metadataType, OH_PictureMetadata *metadata)
```

**描述**

设置辅助图的元数据。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) *auxiliaryPicture将操作的OH_AuxiliaryPictureNative指针。[Image_MetadataType](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_metadatatype) metadataType元数据类型。[OH_PictureMetadata](../../topics/media/OH_PictureMetadata.md) *metadata将要设置的元数据。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

 IMAGE_UNSUPPORTED_METADATA：不支持的元数据类型，或者元数据类型与辅助图片类型不匹配。

#### OH_AuxiliaryPictureNative_Release()

```ets
Image_ErrorCode OH_AuxiliaryPictureNative_Release(OH_AuxiliaryPictureNative *picture)
```

**描述**

释放OH_AuxiliaryPictureNative指针。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureNative](../../topics/media/OH_AuxiliaryPictureNative.md) *picture将操作的OH_AuxiliaryPictureNative指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureInfo_Create()

```ets
Image_ErrorCode OH_AuxiliaryPictureInfo_Create(OH_AuxiliaryPictureInfo **info)
```

**描述**

创建一个OH_AuxiliaryPictureInfo对象。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) **info将操作的OH_AuxiliaryPictureInfo指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureInfo_GetType()

```ets
Image_ErrorCode OH_AuxiliaryPictureInfo_GetType(OH_AuxiliaryPictureInfo *info, Image_AuxiliaryPictureType *type)
```

**描述**

获取OH_AuxiliaryPictureInfo中的辅助图类型。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) *info将操作的OH_AuxiliaryPictureInfo指针。[Image_AuxiliaryPictureType](#ZH-CN_TOPIC_0000002529285845__image_auxiliarypicturetype) *type获取的辅助图类型。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureInfo_SetType()

```ets
Image_ErrorCode OH_AuxiliaryPictureInfo_SetType(OH_AuxiliaryPictureInfo *info, Image_AuxiliaryPictureType type)
```

**描述**

设置OH_AuxiliaryPictureInfo中的辅助图类型。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) *info将操作的OH_AuxiliaryPictureInfo指针。[Image_AuxiliaryPictureType](#ZH-CN_TOPIC_0000002529285845__image_auxiliarypicturetype) type将要设置的辅助图类型。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureInfo_GetSize()

```ets
Image_ErrorCode OH_AuxiliaryPictureInfo_GetSize(OH_AuxiliaryPictureInfo *info, Image_Size *size)
```

**描述**

获取OH_AuxiliaryPictureInfo中的图片尺寸。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) *info将操作的OH_AuxiliaryPictureInfo指针。[Image_Size](../../topics/graphics/Image_Size.md) *size获取的图片尺寸。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureInfo_SetSize()

```ets
Image_ErrorCode OH_AuxiliaryPictureInfo_SetSize(OH_AuxiliaryPictureInfo *info, Image_Size *size)
```

**描述**

设置OH_AuxiliaryPictureInfo中的图片尺寸。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) *info将操作的OH_AuxiliaryPictureInfo指针。[Image_Size](../../topics/graphics/Image_Size.md) *size将要设置的图片尺寸。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureInfo_GetRowStride()

```ets
Image_ErrorCode OH_AuxiliaryPictureInfo_GetRowStride(OH_AuxiliaryPictureInfo *info, uint32_t *rowStride)
```

**描述**

获取OH_AuxiliaryPictureInfo中的行跨距。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) *info将操作的OH_AuxiliaryPictureInfo指针。uint32_t *rowStride跨距，内存中每行像素所占的空间。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureInfo_SetRowStride()

```ets
Image_ErrorCode OH_AuxiliaryPictureInfo_SetRowStride(OH_AuxiliaryPictureInfo *info, uint32_t rowStride)
```

**描述**

设置OH_AuxiliaryPictureInfo中的行跨距。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) *info将操作的OH_AuxiliaryPictureInfo指针。uint32_t rowStride跨距，内存中每行像素所占的空间。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureInfo_GetPixelFormat()

```ets
Image_ErrorCode OH_AuxiliaryPictureInfo_GetPixelFormat(OH_AuxiliaryPictureInfo *info, PIXEL_FORMAT *pixelFormat)
```

**描述**

获取OH_AuxiliaryPictureInfo中的像素格式。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) *info将操作的OH_AuxiliaryPictureInfo指针。[PIXEL_FORMAT](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__pixel_format) *pixelFormat获取的像素格式。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureInfo_SetPixelFormat()

```ets
Image_ErrorCode OH_AuxiliaryPictureInfo_SetPixelFormat(OH_AuxiliaryPictureInfo *info, PIXEL_FORMAT pixelFormat)
```

**描述**

设置OH_AuxiliaryPictureInfo中的像素格式。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) *info将操作的OH_AuxiliaryPictureInfo指针。[PIXEL_FORMAT](pixelmap_native.h.md#ZH-CN_TOPIC_0000002529445819__pixel_format) pixelFormat将要设置的像素格式。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。

#### OH_AuxiliaryPictureInfo_Release()

```ets
Image_ErrorCode OH_AuxiliaryPictureInfo_Release(OH_AuxiliaryPictureInfo *info)
```

**描述**

释放OH_AuxiliaryPictureInfo指针。

**起始版本：** 13

**参数：**

参数项描述[OH_AuxiliaryPictureInfo](../../topics/media/OH_AuxiliaryPictureInfo.md) *info将操作的OH_AuxiliaryPictureInfo指针。

**返回：**

类型说明[Image_ErrorCode](image_common.h.md#ZH-CN_TOPIC_0000002497445872__image_errorcode)

IMAGE_SUCCESS：执行成功。

IMAGE_BAD_PARAMETER：参数错误。