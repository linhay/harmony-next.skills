# image_receiver_mdk.h

#### 概述

声明从native层获取图片数据的方法。

**库：** libimage_receiver_ndk.z.so

**引用文件：** <multimedia/image_framework/image_receiver_mdk.h>

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 10

**相关模块：**[Image](Image.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OhosImageReceiverInfo](OhosImageReceiverInfo.md)-定义ImageReceiver的相关信息。[ImageReceiverNative_](ImageReceiverNative_.md)ImageReceiverNative用于定义ImageReceiverNative数据类型名称。

#### 函数

名称typedef关键字描述[typedef void (*OH_Image_Receiver_On_Callback)()](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_on_callback)OH_Image_Receiver_On_Callback定义native层图片的回调方法。[int32_t OH_Image_Receiver_CreateImageReceiver(napi_env env, struct OhosImageReceiverInfo info, napi_value* res)](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_createimagereceiver)-创建应用层ImageReceiver对象。[ImageReceiverNative* OH_Image_Receiver_InitImageReceiverNative(napi_env env, napi_value source)](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_initimagereceivernative)-通过应用层ImageReceiver对象初始化native层[ImageReceiverNative](zh-cn_topic_0000002529285871.html)对象。[int32_t OH_Image_Receiver_GetReceivingSurfaceId(const ImageReceiverNative* native, char* id, size_t len)](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_getreceivingsurfaceid)-通过[ImageReceiverNative](zh-cn_topic_0000002529285871.html)获取receiver的id。[int32_t OH_Image_Receiver_ReadLatestImage(const ImageReceiverNative* native, napi_value* image)](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_readlatestimage)-通过[ImageReceiverNative](zh-cn_topic_0000002529285871.html)获取最新的一张图片。[int32_t OH_Image_Receiver_ReadNextImage(const ImageReceiverNative* native, napi_value* image)](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_readnextimage)-通过[ImageReceiverNative](zh-cn_topic_0000002529285871.html)获取下一张图片。[int32_t OH_Image_Receiver_On(const ImageReceiverNative* native, OH_Image_Receiver_On_Callback callback)](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_on)-注册一个[OH_Image_Receiver_On_Callback](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_on_callback)回调事件。每当接收新图片，该回调事件就会响应。[int32_t OH_Image_Receiver_GetSize(const ImageReceiverNative* native, struct OhosImageSize* size)](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_getsize)-通过[ImageReceiverNative](zh-cn_topic_0000002529285871.html)获取ImageReceiver的大小。[int32_t OH_Image_Receiver_GetCapacity(const ImageReceiverNative* native, int32_t* capacity)](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_getcapacity)-通过[ImageReceiverNative](zh-cn_topic_0000002529285871.html)获取ImageReceiver的容量。[int32_t OH_Image_Receiver_GetFormat(const ImageReceiverNative* native, int32_t* format)](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_getformat)-通过[ImageReceiverNative](zh-cn_topic_0000002529285871.html)获取ImageReceiver的格式。[int32_t OH_Image_Receiver_Release(ImageReceiverNative* native)](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_release)-

释放native层[ImageReceiverNative](ImageReceiverNative_.md)对象。

注意，此方法不能释放应用层ImageReceiver对象。

#### 函数说明

#### OH_Image_Receiver_On_Callback()

```ets
typedef void (*OH_Image_Receiver_On_Callback)(void)
```

**描述**

定义native层图片的回调方法。

**起始版本：** 10

#### OH_Image_Receiver_CreateImageReceiver()

```ets
int32_t OH_Image_Receiver_CreateImageReceiver(napi_env env, struct OhosImageReceiverInfo info, napi_value* res)
```

**描述**

创建应用层ImageReceiver对象。

**起始版本：** 10

**参数：**

参数项描述napi_env envnapi的环境指针。struct [OhosImageReceiverInfo](OhosImageReceiverInfo.md) infoImageReceiver数据设置项。napi_value* res应用层的ImageReceiver对象的指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

 IMAGE_RESULT_SUCCESS：操作成功。

 IMAGE_RESULT_BAD_PARAMETER：参数错误。

 IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 IMAGE_RESULT_INVALID_PARAMETER：从surface获取参数失败。

 IMAGE_RESULT_CREATE_SURFACE_FAILED：创建surface失败。

 IMAGE_RESULT_SURFACE_GRALLOC_BUFFER_FAILED：surface分配内存失败。

 IMAGE_RESULT_GET_SURFACE_FAILED：获取surface失败。

 IMAGE_RESULT_MEDIA_RTSP_SURFACE_UNSUPPORT：媒体rtsp surface不支持。

 IMAGE_RESULT_DATA_UNSUPPORT：图像类型不支持。

 IMAGE_RESULT_MEDIA_DATA_UNSUPPORT：媒体类型不支持。

#### OH_Image_Receiver_InitImageReceiverNative()

```ets
ImageReceiverNative* OH_Image_Receiver_InitImageReceiverNative(napi_env env, napi_value source)
```

**描述**

通过应用层ImageReceiver对象初始化native层[ImageReceiverNative](ImageReceiverNative_.md)对象。

**起始版本：** 10

**参数：**

参数项描述napi_env envnapi的环境指针。napi_value sourcenapi的ImageReceiver对象。

**返回：**

类型说明[ImageReceiverNative](ImageReceiverNative_.md)*操作成功则返回ImageReceiverNative指针；如果操作失败，则返回nullptr。

**参考：**

[OH_Image_Receiver_Release](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_release)

#### OH_Image_Receiver_GetReceivingSurfaceId()

```ets
int32_t OH_Image_Receiver_GetReceivingSurfaceId(const ImageReceiverNative* native, char* id, size_t len)
```

**描述**

通过[ImageReceiverNative](ImageReceiverNative_.md)获取receiver的id。

**起始版本：** 10

**参数：**

参数项描述const [ImageReceiverNative](ImageReceiverNative_.md)* nativenative层的ImageReceiverNative指针。char* id指向字符缓冲区的指针，用于获取字符串的id。size_t lenid所对应的字符缓冲区的大小。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

 IMAGE_RESULT_BAD_PARAMETER：参数错误。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

 IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 IMAGE_RESULT_INVALID_PARAMETER：从surface获取参数失败。

 IMAGE_RESULT_GET_SURFACE_FAILED：获取surface失败。

 IMAGE_RESULT_DATA_UNSUPPORT：图像类型不支持。

 IMAGE_RESULT_MEDIA_DATA_UNSUPPORT：媒体类型不支持。

#### OH_Image_Receiver_ReadLatestImage()

```ets
int32_t OH_Image_Receiver_ReadLatestImage(const ImageReceiverNative* native, napi_value* image)
```

**描述**

通过[ImageReceiverNative](ImageReceiverNative_.md)获取最新的一张图片。

注意，此接口需要在[OH_Image_Receiver_On_Callback](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_on_callback)回调后调用，才能正常的接收到数据。并且使用此接口返回Image对象创建的[ImageNative](zh-cn_topic_0000002497605876.html)使用完毕后需要调用[OH_Image_Release](image_mdk.h.md#ZH-CN_TOPIC_0000002497605856__oh_image_release)方法释放，释放后才可以继续接收新的数据。

**起始版本：** 10

**参数：**

参数项描述const [ImageReceiverNative](ImageReceiverNative_.md)* nativenative层的ImageReceiverNative指针。napi_value* image获取到的应用层的Image指针对象。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

 IMAGE_RESULT_BAD_PARAMETER：参数错误。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

 IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 IMAGE_RESULT_INVALID_PARAMETER：从surface获取参数失败。

 IMAGE_RESULT_CREATE_SURFACE_FAILED：创建surface失败。

 IMAGE_RESULT_SURFACE_GRALLOC_BUFFER_FAILED：surface分配内存失败。

 IMAGE_RESULT_GET_SURFACE_FAILED：获取surface失败。

 IMAGE_RESULT_MEDIA_RTSP_SURFACE_UNSUPPORT：媒体rtsp surface不支持。

 IMAGE_RESULT_DATA_UNSUPPORT：图像类型不支持。

 IMAGE_RESULT_MEDIA_DATA_UNSUPPORT：媒体类型不支持。

#### OH_Image_Receiver_ReadNextImage()

```ets
int32_t OH_Image_Receiver_ReadNextImage(const ImageReceiverNative* native, napi_value* image)
```

**描述**

通过[ImageReceiverNative](ImageReceiverNative_.md)获取下一张图片。

注意，此接口需要在[OH_Image_Receiver_On_Callback](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_on_callback)回调后调用，才能正常的接收到数据。并且使用此接口返回Image对象创建的[ImageNative](zh-cn_topic_0000002497605876.html)使用完毕后需要调用[OH_Image_Release](image_mdk.h.md#ZH-CN_TOPIC_0000002497605856__oh_image_release)方法释放，释放后才可以继续接收新的数据。

**起始版本：** 10

**参数：**

参数项描述const [ImageReceiverNative](ImageReceiverNative_.md)* nativenative层的ImageReceiverNative指针。napi_value* image读取到的应用层的Image指针对象。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

 IMAGE_RESULT_BAD_PARAMETER：参数错误。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

 IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 IMAGE_RESULT_INVALID_PARAMETER：从surface获取参数失败。

 IMAGE_RESULT_CREATE_SURFACE_FAILED：创建surface失败。

 IMAGE_RESULT_SURFACE_GRALLOC_BUFFER_FAILED：surface分配内存失败。

 IMAGE_RESULT_GET_SURFACE_FAILED：获取surface失败。

 IMAGE_RESULT_MEDIA_RTSP_SURFACE_UNSUPPORT：媒体rtsp surface不支持。

 IMAGE_RESULT_DATA_UNSUPPORT：图像类型不支持。

 IMAGE_RESULT_MEDIA_DATA_UNSUPPORT：媒体类型不支持。

#### OH_Image_Receiver_On()

```ets
int32_t OH_Image_Receiver_On(const ImageReceiverNative* native, OH_Image_Receiver_On_Callback callback)
```

**描述**

注册一个[OH_Image_Receiver_On_Callback](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_on_callback)回调事件。每当接收新图片，该回调事件就会响应。

**起始版本：** 10

**参数：**

参数项描述const [ImageReceiverNative](ImageReceiverNative_.md)* nativenative层的ImageReceiverNative指针。[OH_Image_Receiver_On_Callback](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_on_callback) callback[OH_Image_Receiver_On_Callback](#ZH-CN_TOPIC_0000002497445878__oh_image_receiver_on_callback)事件的回调函数。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

 IMAGE_RESULT_BAD_PARAMETER：参数错误。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

 IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 IMAGE_RESULT_INVALID_PARAMETER：从surface获取参数失败。

 IMAGE_RESULT_GET_SURFACE_FAILED：获取surface失败。

 IMAGE_RESULT_DATA_UNSUPPORT：图像类型不支持。

 IMAGE_RESULT_MEDIA_DATA_UNSUPPORT：媒体类型不支持。

#### OH_Image_Receiver_GetSize()

```ets
int32_t OH_Image_Receiver_GetSize(const ImageReceiverNative* native, struct OhosImageSize* size)
```

**描述**

通过[ImageReceiverNative](ImageReceiverNative_.md)获取ImageReceiver的大小。

**起始版本：** 10

**参数：**

参数项描述const [ImageReceiverNative](ImageReceiverNative_.md)* nativenative层的ImageReceiverNative指针。struct [OhosImageSize](OhosImageSize.md)* size作为结果的OhosImageSize指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

 IMAGE_RESULT_BAD_PARAMETER：参数错误。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

 IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 IMAGE_RESULT_DATA_UNSUPPORT：图像类型不支持。

#### OH_Image_Receiver_GetCapacity()

```ets
int32_t OH_Image_Receiver_GetCapacity(const ImageReceiverNative* native, int32_t* capacity)
```

**描述**

通过[ImageReceiverNative](ImageReceiverNative_.md)获取ImageReceiver的容量。

**起始版本：** 10

**参数：**

参数项描述const [ImageReceiverNative](ImageReceiverNative_.md)* nativenative层的ImageReceiverNative指针。int32_t* capacity作为结果的指向容量的指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

 IMAGE_RESULT_BAD_PARAMETER：参数错误。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

 IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 IMAGE_RESULT_DATA_UNSUPPORT：图像类型不支持。

#### OH_Image_Receiver_GetFormat()

```ets
int32_t OH_Image_Receiver_GetFormat(const ImageReceiverNative* native, int32_t* format)
```

**描述**

通过[ImageReceiverNative](ImageReceiverNative_.md)获取ImageReceiver的格式。

**起始版本：** 10

**参数：**

参数项描述const [ImageReceiverNative](ImageReceiverNative_.md)* nativenative层的ImageReceiverNative指针。int32_t* format作为结果的指向格式的指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

 IMAGE_RESULT_BAD_PARAMETER：参数错误。

IMAGE_RESULT_JNI_ENV_ABNORMAL：JNI环境异常。

 IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 IMAGE_RESULT_DATA_UNSUPPORT：图像类型不支持。

#### OH_Image_Receiver_Release()

```ets
int32_t OH_Image_Receiver_Release(ImageReceiverNative* native)
```

**描述**

释放native层[ImageReceiverNative](ImageReceiverNative_.md)对象。

注意，此方法不能释放应用层ImageReceiver对象。

**起始版本：** 10

**参数：**

参数项描述[ImageReceiverNative](ImageReceiverNative_.md)* nativenative层的ImageReceiverNative指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：操作成功。

 IMAGE_RESULT_BAD_PARAMETER：参数错误。

 IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 IMAGE_RESULT_DATA_UNSUPPORT：图像类型不支持。