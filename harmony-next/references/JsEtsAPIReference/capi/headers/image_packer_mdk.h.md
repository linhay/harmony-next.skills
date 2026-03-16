# image_packer_mdk.h

#### 概述

声明用于将图像编码到缓冲区或文件的api。可用于将像素数据编码到目标缓冲区或文件中。

编码过程如下：

通过OH_ImagePacker_Create方法创建编码器对象。

然后通过OH_ImagePacker_InitNative将编码器对象转换为编码器原生对象。

接下来用OH_ImagePacker_PackToData或者OH_ImagePacker_PackToFile将源以特定的编码选项编码进目标区域。

最后通过OH_ImagePacker_Release释放编码器对象。

**引用文件：** <multimedia/image_framework/image_packer_mdk.h>

**库：** libimage_packer_ndk.z.so

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 11

**相关模块：**[Image](../../topics/graphics/Image.md)

#### 汇总

#### 结构体

名称typedef关键字描述[ImagePacker_Opts_](../../topics/graphics/ImagePacker_Opts_.md)ImagePacker_Opts定义图像编码选项信息。[ImagePacker_Native_](../../topics/graphics/ImagePacker_Native_.md)ImagePacker_Native为编码器方法定义native层编码器对象。

#### 函数

名称描述[int32_t OH_ImagePacker_Create(napi_env env, napi_value *res)](#ZH-CN_TOPIC_0000002529285847__oh_imagepacker_create)获取JavaScript native层ImagePacker对象。[ImagePacker_Native* OH_ImagePacker_InitNative(napi_env env, napi_value packer)](#ZH-CN_TOPIC_0000002529285847__oh_imagepacker_initnative)从输入JavaScript native层ImagePacker对象中，转换成ImagePacker_Native值。[int32_t OH_ImagePacker_PackToData(ImagePacker_Native* native, napi_value source,ImagePacker_Opts* opts, uint8_t* outData, size_t* size)](#ZH-CN_TOPIC_0000002529285847__oh_imagepacker_packtodata)通过一个给定的选项ImagePacker_Opts结构体，将输入JavaScript native层PixelMap对象或者ImageSource对象编码并输出到指定的缓存区outData中。[int32_t OH_ImagePacker_PackToFile(ImagePacker_Native* native, napi_value source, ImagePacker_Opts* opts, int fd)](#ZH-CN_TOPIC_0000002529285847__oh_imagepacker_packtofile)通过一个给定的选项ImagePacker_Opts结构体，将输入JavaScript native层PixelMap对象或者ImageSource对象编码并输出到指定的文件中。[int32_t OH_ImagePacker_Release(ImagePacker_Native* native)](#ZH-CN_TOPIC_0000002529285847__oh_imagepacker_release)

释放native层编码器对象[ImagePacker_Native](../../topics/graphics/ImagePacker_Native_.md)。

此API不用于释放JavaScript原生API ImagePacker对象，它用于释放native层对象ImagePacker_Native。

#### 函数说明

#### OH_ImagePacker_Create()

```ets
int32_t OH_ImagePacker_Create(napi_env env, napi_value *res)
```

**描述**

获取JavaScript native层ImagePacker对象。

**起始版本：** 11

**参数：**

参数项描述napi_env env表明JNI环境的指针。napi_value *res表明JavaScript native层ImagePacker对象的指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：执行成功。

IMAGE_RESULT_INVALID_PARAMETER：参数无效。

#### OH_ImagePacker_InitNative()

```ets
ImagePacker_Native* OH_ImagePacker_InitNative(napi_env env, napi_value packer)
```

**描述**

从输入JavaScript native层ImagePacker对象中，转换成ImagePacker_Native值。

**起始版本：** 11

**参数：**

参数项描述napi_env env表明JNI环境的指针。napi_value packer表明JavaScript native层ImagePacker对象。

**返回：**

类型说明[ImagePacker_Native](../../topics/graphics/ImagePacker_Native_.md)*如果操作成功则返回ImagePacker_Native指针，否则返回空指针。

**参考：**

[OH_ImagePacker_Release](#ZH-CN_TOPIC_0000002529285847__oh_imagepacker_release)

#### OH_ImagePacker_PackToData()

```ets
int32_t OH_ImagePacker_PackToData(ImagePacker_Native* native, napi_value source,ImagePacker_Opts* opts, uint8_t* outData, size_t* size)
```

**描述**

通过一个给定的选项ImagePacker_Opts结构体，将输入JavaScript native层PixelMap对象或者ImageSource对象编码并输出到指定的缓存区outData中。

**起始版本：** 11

**参数：**

参数项描述[ImagePacker_Native](../../topics/graphics/ImagePacker_Native_.md)* native表明指向native层ImagePacker的指针。napi_value source表明待编码JavaScript native层PixelMap对象或者ImageSource对象。[ImagePacker_Opts](../../topics/graphics/ImagePacker_Opts_.md)* opts表明位图编码的选项。uint8_t* outData输出的指定缓存区。size_t* size输出的指定缓存区大小。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：执行成功。

 IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 ERR_IMAGE_DATA_ABNORMAL：输出缓冲区异常。

 ERR_IMAGE_MISMATCHED_FORMAT：格式不匹配。

 ERR_IMAGE_MALLOC_ABNORMAL：malloc内部缓冲区错误。

 ERR_IMAGE_DECODE_ABNORMAL：init编解码器内部错误。

ERR_IMAGE_ENCODE_FAILED：编码器在编码过程中出现错误。

**参考：**

[OH_ImagePacker_PackToFile](#ZH-CN_TOPIC_0000002529285847__oh_imagepacker_packtofile)

#### OH_ImagePacker_PackToFile()

```ets
int32_t OH_ImagePacker_PackToFile(ImagePacker_Native* native, napi_value source,ImagePacker_Opts* opts, int fd)
```

**描述**

通过一个给定的选项ImagePacker_Opts结构体，将输入JavaScript native层PixelMap对象或者ImageSource对象编码并输出到指定的文件中。

**起始版本：** 11

**参数：**

参数项描述[ImagePacker_Native](../../topics/graphics/ImagePacker_Native_.md)* native表明指向native层ImagePacker的指针。napi_value source表明待编码JavaScript native层PixelMap对象或者ImageSource对象。[ImagePacker_Opts](../../topics/graphics/ImagePacker_Opts_.md)* opts表明位图编码的选项。int fd输出的指定文件描述符。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：执行成功。

 IMAGE_RESULT_INVALID_PARAMETER：参数无效。

 ERR_IMAGE_DATA_ABNORMAL：输出缓冲区异常。

 ERR_IMAGE_MISMATCHED_FORMAT：格式不匹配。

 ERR_IMAGE_MALLOC_ABNORMAL：malloc内部缓冲区错误。

 ERR_IMAGE_DECODE_ABNORMAL：init编解码器内部错误。

ERR_IMAGE_ENCODE_FAILED：编码器在编码过程中出现错误。

**参考：**

[OH_ImagePacker_PackToData](#ZH-CN_TOPIC_0000002529285847__oh_imagepacker_packtodata)

#### OH_ImagePacker_Release()

```ets
int32_t OH_ImagePacker_Release(ImagePacker_Native* native)
```

**描述**

释放native层编码器对象[ImagePacker_Native](../../topics/graphics/ImagePacker_Native_.md)。

此API不用于释放JavaScript原生API ImagePacker对象，它用于释放native层对象ImagePacker_Native。

通过调用[OH_ImagePacker_InitNative](#ZH-CN_TOPIC_0000002529285847__oh_imagepacker_initnative)解析。

**起始版本：** 11

**参数：**

参数项描述[ImagePacker_Native](../../topics/graphics/ImagePacker_Native_.md)* native表明native层ImagePacker_Native值的指针。

**返回：**

类型说明int32_t

[IRNdkErrCode](image_mdk_common.h.md#ZH-CN_TOPIC_0000002497445876__irndkerrcode)：

IMAGE_RESULT_SUCCESS：执行成功。

**参考：**

[OH_ImagePacker_InitNative](#ZH-CN_TOPIC_0000002529285847__oh_imagepacker_initnative)