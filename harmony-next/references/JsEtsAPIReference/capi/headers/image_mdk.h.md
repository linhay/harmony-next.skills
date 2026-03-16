# image_mdk.h

#### 概述

声明访问图像矩形、大小、格式和组件数据的函数。

**引用文件：** <multimedia/image_framework/image_mdk.h>

**库：** libimage_ndk.z.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 10

**相关模块：**[Image](../../topics/graphics/Image.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OhosImageRect](../../topics/graphics/OhosImageRect.md)-定义图像矩形信息。[ImageNative_](../../topics/graphics/ImageNative_.md)ImageNative为图像接口定义native层图像对象。[OhosImageComponent](../../topics/components/OhosImageComponent.md)-定义图像组成信息。

#### 枚举

名称描述[图像格式](#ZH-CN_TOPIC_0000002497605856__图像格式)图像格式枚举值。[图像颜色通道类型](#ZH-CN_TOPIC_0000002497605856__图像颜色通道类型)图像颜色通道类型枚举值。

#### 函数

名称描述[ImageNative* OH_Image_InitImageNative(napi_env env, napi_value source)](#ZH-CN_TOPIC_0000002497605856__oh_image_initimagenative)从输入的JavaScript Native API图像对象中解析native ImageNative对象。[int32_t OH_Image_ClipRect(const ImageNative* native, struct OhosImageRect* rect)](#ZH-CN_TOPIC_0000002497605856__oh_image_cliprect)获取native ImageNative对象OhosImageRect信息。[int32_t OH_Image_Size(const ImageNative* native, struct OhosImageSize* size)](#ZH-CN_TOPIC_0000002497605856__oh_image_size)获取native ImageNative对象的OhosImageSize信息。[int32_t OH_Image_Format(const ImageNative* native, int32_t* format)](#ZH-CN_TOPIC_0000002497605856__oh_image_format)获取native ImageNative对象的图像格式。[int32_t OH_Image_GetComponent(const ImageNative* native, int32_t componentType, struct OhosImageComponent* componentNative)](#ZH-CN_TOPIC_0000002497605856__oh_image_getcomponent)从native ImageNative对象中获取OhosImageComponent。[int32_t OH_Image_Release(ImageNative* native)](#ZH-CN_TOPIC_0000002497605856__oh_image_release)

释放ImageNative native对象。

这个方法无法释放JavaScript Native API Image对象，而是释放被[OH_Image_InitImageNative](image_mdk.h.md#ZH-CN_TOPIC_0000002497605856__oh_image_initimagenative)解析的ImageNative native对象。

#### 枚举类型说明

#### 图像格式

```ets
enum anonymous enum
```

**描述**

图像格式枚举值。

**起始版本：** 10

枚举项描述OHOS_IMAGE_FORMAT_YCBCR_422_SP = 1000YCBCR422 semi-planar格式。OHOS_IMAGE_FORMAT_JPEG = 2000JPEG编码格式。

#### 图像颜色通道类型

```ets
enum anonymous enum
```

**描述**

图像颜色通道类型枚举值。

**起始版本：** 10

枚举项描述OHOS_IMAGE_COMPONENT_FORMAT_YUV_Y = 1亮度信息。OHOS_IMAGE_COMPONENT_FORMAT_YUV_U = 2色度信息。OHOS_IMAGE_COMPONENT_FORMAT_YUV_V = 3色差值信息。OHOS_IMAGE_COMPONENT_FORMAT_JPEG = 4Jpeg格式。

#### 函数说明

#### OH_Image_InitImageNative()

```ets
ImageNative* OH_Image_InitImageNative(napi_env env, napi_value source)
```

**描述**

从输入的JavaScript Native API图像对象中解析native ImageNative对象。

**起始版本：** 10

**参数：**

参数项描述napi_env env表示指向JNI环境的指针。napi_value source表示JavaScript Native API图像对象。

**返回：**

类型说明[ImageNative](../../topics/graphics/ImageNative_.md)*如果操作成功返回ImageNative指针对象，如果操作失败返回空指针。

**参考：**

[OH_Image_Release](#ZH-CN_TOPIC_0000002497605856__oh_image_release)

#### OH_Image_ClipRect()

```ets
int32_t OH_Image_ClipRect(const ImageNative* native, struct OhosImageRect* rect)
```

**描述**

获取native ImageNative对象OhosImageRect信息。

**起始版本：** 10

**参数：**

参数项描述const [ImageNative](../../topics/graphics/ImageNative_.md)* native表示指向ImageNative native层对象的指针。struct [OhosImageRect](../../topics/graphics/OhosImageRect.md)* rect表示作为转换结果的OhosImageRect对象指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

IMAGE_RESULT_INVALID_PARAMETER：参数无效。

IMAGE_RESULT_SURFACE_GET_PARAMETER_FAILED：从surface获取参数失败。

IMAGE_RESULT_BAD_PARAMETER：参数错误。

#### OH_Image_Size()

```ets
int32_t OH_Image_Size(const ImageNative* native, struct OhosImageSize* size)
```

**描述**

获取native ImageNative对象的OhosImageSize信息。

如果ImageNative对象所存储的是相机预览流数据，即YUV图像数据，那么获取到的OhosImageSize中的宽高分别对应YUV图像的宽高；如果ImageNative对象所存储的是相机拍照流数据，即JPEG图像，由于已经是编码后的数据，OhosImageSize中的宽等于JPEG数据大小，高等于1。

ImageNative对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId传给相机的previewOutput还是captureOutput。相机预览与拍照最佳实践请参考[预览流二次处理(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-preview-imagereceiver)与[拍照(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting)。

**起始版本：** 10

**参数：**

参数项描述const [ImageNative](../../topics/graphics/ImageNative_.md)* native表示ImageNative native对象的指针。struct [OhosImageSize](../../topics/graphics/OhosImageSize.md)* size表示作为转换结果的OhosImageSize对象的指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

IMAGE_RESULT_INVALID_PARAMETER：参数无效。

IMAGE_RESULT_SURFACE_GET_PARAMETER_FAILED：从surface获取参数失败。

IMAGE_RESULT_BAD_PARAMETER：参数错误。

#### OH_Image_Format()

```ets
int32_t OH_Image_Format(const ImageNative* native, int32_t* format)
```

**描述**

获取native ImageNative对象的图像格式。

**起始版本：** 10

**参数：**

参数项描述const [ImageNative](../../topics/graphics/ImageNative_.md)* native表示ImageNative native对象的指针。int32_t* format表示作为转换结果的图像格式对象的指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

IMAGE_RESULT_INVALID_PARAMETER：参数无效。

IMAGE_RESULT_SURFACE_GET_PARAMETER_FAILED：从surface获取参数失败。

IMAGE_RESULT_BAD_PARAMETER：参数错误。

#### OH_Image_GetComponent()

```ets
int32_t OH_Image_GetComponent(const ImageNative* native, int32_t componentType, struct OhosImageComponent* componentNative)
```

**描述**

从native ImageNative对象中获取OhosImageComponent。

**起始版本：** 10

**参数：**

参数项描述const [ImageNative](../../topics/graphics/ImageNative_.md)* native表示ImageNative native对象的指针。int32_t componentType表示所需组件的组件类型。struct [OhosImageComponent](../../topics/components/OhosImageComponent.md)* componentNative表示转换结果的OhosImageComponent对象的指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

IMAGE_RESULT_INVALID_PARAMETER：参数无效。

IMAGE_RESULT_SURFACE_GET_PARAMETER_FAILED：从surface获取参数失败。

IMAGE_RESULT_BAD_PARAMETER：参数错误。

#### OH_Image_Release()

```ets
int32_t OH_Image_Release(ImageNative* native)
```

**描述**

释放ImageNative native对象。

这个方法无法释放JavaScript Native API Image对象，而是释放被[OH_Image_InitImageNative](image_mdk.h.md#ZH-CN_TOPIC_0000002497605856__oh_image_initimagenative)解析的ImageNative native对象。

**起始版本：** 10

**参数：**

参数项描述[ImageNative](../../topics/graphics/ImageNative_.md)* native表示ImageNative native对象的指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

IMAGE_RESULT_INVALID_PARAMETER：参数无效。

IMAGE_RESULT_BAD_PARAMETER：参数错误。

**参考：**

[OH_Image_InitImageNative](#ZH-CN_TOPIC_0000002497605856__oh_image_initimagenative)