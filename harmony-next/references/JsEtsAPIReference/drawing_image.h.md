# drawing_image.h

#### 概述

文件中定义了与图片相关的功能函数。

**引用文件：** <native_drawing/drawing_image.h>

**库：** libnative_drawing.so

**起始版本：** 12

**相关模块：**[Drawing](Drawing.md)

#### 汇总

#### 函数

名称描述[OH_Drawing_Image* OH_Drawing_ImageCreate(void)](#ZH-CN_TOPIC_0000002529285993__oh_drawing_imagecreate)创建一个图片对象，描述了要绘制的二维像素数组。[void OH_Drawing_ImageDestroy(OH_Drawing_Image* image)](#ZH-CN_TOPIC_0000002529285993__oh_drawing_imagedestroy)销毁图片对象并回收该对象占有内存。[bool OH_Drawing_ImageBuildFromBitmap(OH_Drawing_Image* image, OH_Drawing_Bitmap* bitmap)](#ZH-CN_TOPIC_0000002529285993__oh_drawing_imagebuildfrombitmap)

从位图构造图片对象内容，共享或复制位图像素。如果位图被标记为不可变状态，像素内存是共享的，不是复制。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

image、bitmap任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[int32_t OH_Drawing_ImageGetWidth(OH_Drawing_Image* image)](#ZH-CN_TOPIC_0000002529285993__oh_drawing_imagegetwidth)

获取图片宽度，即每行的像素个数。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

image为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[int32_t OH_Drawing_ImageGetHeight(OH_Drawing_Image* image)](#ZH-CN_TOPIC_0000002529285993__oh_drawing_imagegetheight)

获取图片高度，即像素行数。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

image为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

[void OH_Drawing_ImageGetImageInfo(OH_Drawing_Image* image, OH_Drawing_Image_Info* imageInfo)](#ZH-CN_TOPIC_0000002529285993__oh_drawing_imagegetimageinfo)

获取图片信息。调用该接口后，传入的图片信息对象被填充。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

image、imageInfo任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

#### 函数说明

#### OH_Drawing_ImageCreate()

```ets
OH_Drawing_Image* OH_Drawing_ImageCreate(void)
```

**描述**

创建一个图片对象，描述了要绘制的二维像素数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**返回：**

类型说明[OH_Drawing_Image](OH_Drawing_Image.md)*函数返回一个指针，指针指向创建的图片对象[OH_Drawing_Image](OH_Drawing_Image.md)。

#### OH_Drawing_ImageDestroy()

```ets
void OH_Drawing_ImageDestroy(OH_Drawing_Image* image)
```

**描述**

销毁图片对象并回收该对象占有内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Image](OH_Drawing_Image.md)* image指向图片对象[OH_Drawing_Image](OH_Drawing_Image.md)的指针。

#### OH_Drawing_ImageBuildFromBitmap()

```ets
bool OH_Drawing_ImageBuildFromBitmap(OH_Drawing_Image* image, OH_Drawing_Bitmap* bitmap)
```

**描述**

从位图构造图片对象内容，共享或复制位图像素。如果位图被标记为不可变状态，像素内存是共享的，不是复制。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

image、bitmap任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Image](OH_Drawing_Image.md)* image指向图片对象[OH_Drawing_Image](OH_Drawing_Image.md)的指针。[OH_Drawing_Bitmap](OH_Drawing_Bitmap.md)* bitmap指向位图对象[OH_Drawing_Bitmap](OH_Drawing_Bitmap.md)的指针。

**返回：**

类型说明bool函数返回true表示构造图片内容成功，函数返回false表示构建图片内容失败。

#### OH_Drawing_ImageGetWidth()

```ets
int32_t OH_Drawing_ImageGetWidth(OH_Drawing_Image* image)
```

**描述**

获取图片宽度，即每行的像素个数。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

image为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Image](OH_Drawing_Image.md)* image指向图片对象[OH_Drawing_Image](OH_Drawing_Image.md)的指针。

**返回：**

类型说明int32_t函数返回图片宽度。

#### OH_Drawing_ImageGetHeight()

```ets
int32_t OH_Drawing_ImageGetHeight(OH_Drawing_Image* image)
```

**描述**

获取图片高度，即像素行数。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

image为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Image](OH_Drawing_Image.md)* image指向图片对象[OH_Drawing_Image](OH_Drawing_Image.md)的指针。

**返回：**

类型说明int32_t函数返回图片高度。

#### OH_Drawing_ImageGetImageInfo()

```ets
void OH_Drawing_ImageGetImageInfo(OH_Drawing_Image* image, OH_Drawing_Image_Info* imageInfo)
```

**描述**

获取图片信息。调用该接口后，传入的图片信息对象被填充。

本接口会产生错误码，可以通过[OH_Drawing_ErrorCodeGet](drawing_error_code.h.md#ZH-CN_TOPIC_0000002497606000__oh_drawing_errorcodeget)查看错误码的取值。

image、imageInfo任意一个为NULL时返回OH_DRAWING_ERROR_INVALID_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

参数项描述[OH_Drawing_Image](OH_Drawing_Image.md)* image指向图片对象[OH_Drawing_Image](OH_Drawing_Image.md)的指针。[OH_Drawing_Image_Info](OH_Drawing_Image_Info.md)* imageInfo指向图片信息对象[OH_Drawing_Image_Info](OH_Drawing_Image_Info.md)的指针，开发者可调用[OH_Drawing_Image_Info](OH_Drawing_Image_Info.md)创建。