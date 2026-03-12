# buffer_common.h

#### 概述

提供NativeBuffer模块的公共类型定义。

**引用文件：** <native_buffer/buffer_common.h>

**库：** libnative_buffer.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

**相关模块：**[OH_NativeBuffer](OH_NativeBuffer.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_NativeBuffer_ColorXY](OH_NativeBuffer_ColorXY.md)OH_NativeBuffer_ColorXY表示基色的X和Y坐标。[OH_NativeBuffer_Smpte2086](OH_NativeBuffer_Smpte2086.md)OH_NativeBuffer_Smpte2086表示smpte2086静态元数据。[OH_NativeBuffer_Cta861](OH_NativeBuffer_Cta861.md)OH_NativeBuffer_Cta861表示CTA-861.3静态元数据。[OH_NativeBuffer_StaticMetadata](OH_NativeBuffer_StaticMetadata.md)OH_NativeBuffer_StaticMetadata表示HDR静态元数据。

#### 枚举

名称typedef关键字描述[OH_NativeBuffer_ColorSpace](#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace)OH_NativeBuffer_ColorSpaceOH_NativeBuffer的颜色空间。[OH_NativeBuffer_MetadataType](#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatatype)OH_NativeBuffer_MetadataTypeOH_NativeBuffer的图像标准。[OH_NativeBuffer_MetadataKey](#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatakey)OH_NativeBuffer_MetadataKey表示OH_NativeBuffer的描述信息的键值，如HDR元数据，ROI元数据等。[OH_NativeBuffer_Format](#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_format)OH_NativeBuffer_FormatOH_NativeBuffer格式的枚举。[OH_NativeBuffer_TransformType](#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_transformtype)OH_NativeBuffer_TransformTypeOH_NativeBuffer转换类型的枚举。

#### 枚举类型说明

#### OH_NativeBuffer_ColorSpace

```ets
enum OH_NativeBuffer_ColorSpace
```

**描述**

OH_NativeBuffer的颜色空间。

从API version 12开始，此枚举由native_buffer.h移动至此头文件。

API version 12之前，使用该枚举请引用native_buffer.h头文件；从API version 12开始，引用native_buffer.h或buffer_common.h均可正常使用该枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 11

枚举项描述OH_COLORSPACE_NONE无颜色空间。OH_COLORSPACE_BT601_EBU_FULL色域范围为BT601_P，传递函数为BT709，转换矩阵为BT601_P，数据范围为RANGE_FULL。OH_COLORSPACE_BT601_SMPTE_C_FULL色域范围为BT601_N，传递函数为BT709，转换矩阵为BT601_N，数据范围为RANGE_FULL。OH_COLORSPACE_BT709_FULL色域范围为BT709，传递函数为BT709，转换矩阵为BT709，数据范围为RANGE_FULL。OH_COLORSPACE_BT2020_HLG_FULL色域范围为BT2020，传递函数为HLG，转换矩阵为BT2020，数据范围为RANGE_FULL。OH_COLORSPACE_BT2020_PQ_FULL色域范围为BT2020，传递函数为PQ，转换矩阵为BT2020，数据范围为RANGE_FULL。OH_COLORSPACE_BT601_EBU_LIMIT色域范围为BT601_P，传递函数为BT709，转换矩阵为BT601_P，数据范围为RANGE_LIMITED。OH_COLORSPACE_BT601_SMPTE_C_LIMIT色域范围为BT601_N，传递函数为BT709，转换矩阵为BT601_N，数据范围为RANGE_LIMITED。OH_COLORSPACE_BT709_LIMIT色域范围为BT709，传递函数为BT709，转换矩阵为BT709，数据范围为RANGE_LIMITED。OH_COLORSPACE_BT2020_HLG_LIMIT色域范围为BT2020，传递函数为HLG，转换矩阵为BT2020，数据范围为RANGE_LIMITED。OH_COLORSPACE_BT2020_PQ_LIMIT色域范围为BT2020，传递函数为PQ，转换矩阵为BT2020，数据范围为RANGE_LIMITED。OH_COLORSPACE_SRGB_FULL色域范围为SRGB，传递函数为SRGB，转换矩阵为BT601_N，数据范围为RANGE_FULL。OH_COLORSPACE_P3_FULL色域范围为P3_D65，传递函数为SRGB，转换矩阵为P3，数据范围为RANGE_FULL。OH_COLORSPACE_P3_HLG_FULL色域范围为P3_D65，传递函数为HLG，转换矩阵为P3，数据范围为RANGE_FULL。OH_COLORSPACE_P3_PQ_FULL色域范围为P3_D65，传递函数为PQ，转换矩阵为P3，数据范围为RANGE_FULL。OH_COLORSPACE_ADOBERGB_FULL色域范围为ADOBERGB，传递函数为ADOBERGB，转换矩阵为ADOBERGB，数据范围为RANGE_FULL。OH_COLORSPACE_SRGB_LIMIT色域范围为SRGB，传递函数为SRGB，转换矩阵为BT601_N，数据范围为RANGE_LIMITED。OH_COLORSPACE_P3_LIMIT色域范围为P3_D65，传递函数为SRGB，转换矩阵为P3，数据范围为RANGE_LIMITED。OH_COLORSPACE_P3_HLG_LIMIT色域范围为P3_D65，传递函数为HLG，转换矩阵为P3，数据范围为RANGE_LIMITED。OH_COLORSPACE_P3_PQ_LIMIT色域范围为P3_D65，传递函数为PQ，转换矩阵为P3，数据范围为RANGE_LIMITED。OH_COLORSPACE_ADOBERGB_LIMIT色域范围为ADOBERGB，传递函数为ADOBERGB，转换矩阵为ADOBERGB，数据范围为RANGE_LIMITED。OH_COLORSPACE_LINEAR_SRGB色域范围为SRGB，传递函数为LINEAR。OH_COLORSPACE_LINEAR_BT709等同于 OH_COLORSPACE_LINEAR_SRGB。OH_COLORSPACE_LINEAR_P3色域范围为P3_D65，传递函数为LINEAR。OH_COLORSPACE_LINEAR_BT2020色域范围为BT2020，传递函数为LINEAR。OH_COLORSPACE_DISPLAY_SRGB等同于OH_COLORSPACE_SRGB_FULL。OH_COLORSPACE_DISPLAY_P3_SRGB等同于OH_COLORSPACE_P3_FULL。OH_COLORSPACE_DISPLAY_P3_HLG等同于OH_COLORSPACE_P3_HLG_FULL。OH_COLORSPACE_DISPLAY_P3_PQ等同于OH_COLORSPACE_P3_PQ_FULL。OH_COLORSPACE_DISPLAY_BT2020_SRGB色域范围为BT2020，传递函数为SRGB，转换矩阵为BT2020，数据范围为RANGE_FULL。OH_COLORSPACE_DISPLAY_BT2020_HLG等同于 OH_COLORSPACE_BT2020_HLG_FULL。OH_COLORSPACE_DISPLAY_BT2020_PQ等同于OH_COLORSPACE_BT2020_PQ_FULL。

#### OH_NativeBuffer_MetadataType

```ets
enum OH_NativeBuffer_MetadataType
```

**描述**

OH_NativeBuffer的图像标准。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

枚举项描述OH_VIDEO_HDR_HLG视频HLG。OH_VIDEO_HDR_HDR10视频HDR10。OH_VIDEO_HDR_VIVID视频HDR VIVID。OH_IMAGE_HDR_VIVID_DUAL

图片HDR VIVID DUAL。

**起始版本：** 22

OH_IMAGE_HDR_VIVID_SINGLE

图片HDR VIVID SINGLE。

**起始版本：** 22

OH_VIDEO_NONE = -1

无元数据。

**起始版本：** 13

#### OH_NativeBuffer_MetadataKey

```ets
enum OH_NativeBuffer_MetadataKey
```

**描述**

表示OH_NativeBuffer的描述信息的键值，如HDR元数据，ROI元数据等。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

枚举项描述OH_HDR_METADATA_TYPE元数据类型，其值见[OH_NativeBuffer_MetadataType](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_metadatatype)，size为OH_NativeBuffer_MetadataType大小。OH_HDR_STATIC_METADATA静态元数据，其值见[OH_NativeBuffer_StaticMetadata](OH_NativeBuffer_StaticMetadata.md)，size为OH_NativeBuffer_StaticMetadata大小。OH_HDR_DYNAMIC_METADATA动态元数据，其值见视频流中SEI的字节流，size的取值范围为1-3000。OH_REGION_OF_INTEREST_METADATA

视频编解码感兴趣区域（ROI）元数据，配置格式示例：“Top1,Left1-Bottom1,Right1=QpOffset1;Top2,Left2-Bottom2,Right2=QpOffset2;”。

每个ROI框由位置信息（Top,Left-Bottom,Right），编码质量偏移信息（QpOffset）组成，到分号结束。

ROI框的编码质量偏移信息可以缺省，缺省值为-3，缺省时配置示例：“Top1,Left1-Bottom1,Right1;Top2,Left2-Bottom2,Right2;”。

每组ROI元数据最多支持同时配置6个ROI，且其累计面积不超过全图的1/5。

该枚举值仅支持通过[OH_NativeBuffer_SetMetadataValue()](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_setmetadatavalue)接口调用。

**起始版本：** 22

#### OH_NativeBuffer_Format

```ets
enum OH_NativeBuffer_Format
```

**描述**

OH_NativeBuffer格式的枚举。

从API version 22开始，此枚举由native_buffer.h移动至此头文件。

API version 22之前，使用该枚举请引用native_buffer.h头文件；从API version 22开始，引用native_buffer.h或buffer_common.h均可正常使用该枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 10

枚举项描述NATIVEBUFFER_PIXEL_FMT_CLUT8 = 0

CLUT8格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_CLUT1

CLUT1格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_CLUT4

CLUT4格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_RGB_565 = 3RGB565格式。NATIVEBUFFER_PIXEL_FMT_RGBA_5658RGBA5658格式。NATIVEBUFFER_PIXEL_FMT_RGBX_4444RGBX4444格式。NATIVEBUFFER_PIXEL_FMT_RGBA_4444RGBA4444格式。NATIVEBUFFER_PIXEL_FMT_RGB_444RGB444格式。NATIVEBUFFER_PIXEL_FMT_RGBX_5551RGBX5551格式。NATIVEBUFFER_PIXEL_FMT_RGBA_5551RGBA5551格式。NATIVEBUFFER_PIXEL_FMT_RGB_555RGB555格式。NATIVEBUFFER_PIXEL_FMT_RGBX_8888RGBX8888格式。NATIVEBUFFER_PIXEL_FMT_RGBA_8888RGBA8888格式。NATIVEBUFFER_PIXEL_FMT_RGB_888RGB888格式。NATIVEBUFFER_PIXEL_FMT_BGR_565BGR565格式。NATIVEBUFFER_PIXEL_FMT_BGRX_4444BGRX4444格式。NATIVEBUFFER_PIXEL_FMT_BGRA_4444BGRA4444格式。NATIVEBUFFER_PIXEL_FMT_BGRX_5551BGRX5551格式。NATIVEBUFFER_PIXEL_FMT_BGRA_5551BGRA5551格式。NATIVEBUFFER_PIXEL_FMT_BGRX_8888BGRX8888格式。NATIVEBUFFER_PIXEL_FMT_BGRA_8888BGRA8888格式。NATIVEBUFFER_PIXEL_FMT_YUV_422_I

YUV422 interleaved 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_YCBCR_422_SP

YCBCR422 semi-planar 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_YCRCB_422_SP

YCRCB422 semi-planar 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_YCBCR_420_SP

YCBCR420 semi-planar 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_YCRCB_420_SP

YCRCB420 semi-planar 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_YCBCR_422_P

YCBCR422 planar 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_YCRCB_422_P

YCRCB422 planar 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_YCBCR_420_P

YCBCR420 planar 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_YCRCB_420_P

YCRCB420 planar 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_YUYV_422_PKG

YUYV422 packed 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_UYVY_422_PKG

UYVY422 packed 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_YVYU_422_PKG

YVYU422 packed 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_VYUY_422_PKG

VYUY422 packed 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_RGBA_1010102RGBA_1010102 packed 格式。NATIVEBUFFER_PIXEL_FMT_YCBCR_P010YCBCR420 semi-planar 10bit packed 格式。NATIVEBUFFER_PIXEL_FMT_YCRCB_P010YCRCB420 semi-planar 10bit packed 格式。NATIVEBUFFER_PIXEL_FMT_RAW10Raw 10bit packed 格式。NATIVEBUFFER_PIXEL_FMT_BLOB

BLOB格式。

**起始版本：** 15

NATIVEBUFFER_PIXEL_FMT_RGBA16_FLOAT

RGBA16 float格式。

**起始版本：** 15

NATIVEBUFFER_PIXEL_FMT_Y8 = 40

Y8格式。

**起始版本：** 20

NATIVEBUFFER_PIXEL_FMT_Y16 = 41

Y16格式。

**起始版本：** 20

NATIVEBUFFER_PIXEL_FMT_VENDER_MASK = 0X7FFF0000

vender mask 格式。

**起始版本：** 12

NATIVEBUFFER_PIXEL_FMT_BUTT = 0X7FFFFFFF无效格式。

#### OH_NativeBuffer_TransformType

```ets
enum OH_NativeBuffer_TransformType
```

**描述**

OH_NativeBuffer转换类型的枚举。

从API version 22开始，此枚举由native_buffer.h移动至此头文件。

API version 22之前，使用该枚举请引用native_buffer.h头文件；从API version 22开始，引用native_buffer.h或buffer_common.h均可正常使用该枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeBuffer

**起始版本：** 12

枚举项描述NATIVEBUFFER_ROTATE_NONE = 0不旋转。NATIVEBUFFER_ROTATE_90旋转90度。NATIVEBUFFER_ROTATE_180旋转180度。NATIVEBUFFER_ROTATE_270旋转270度。NATIVEBUFFER_FLIP_H水平翻转。NATIVEBUFFER_FLIP_V垂直翻转。NATIVEBUFFER_FLIP_H_ROT90水平翻转并旋转90度。NATIVEBUFFER_FLIP_V_ROT90垂直翻转并旋转90度。NATIVEBUFFER_FLIP_H_ROT180水平翻转并旋转180度。NATIVEBUFFER_FLIP_V_ROT180垂直翻转并旋转180度。NATIVEBUFFER_FLIP_H_ROT270水平翻转并旋转270度。NATIVEBUFFER_FLIP_V_ROT270垂直翻转并旋转270度。