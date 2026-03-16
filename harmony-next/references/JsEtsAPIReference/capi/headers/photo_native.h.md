# photo_native.h

#### 概述

声明相机照片的概念。

**引用文件：** <ohcamera/photo_native.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 12

**相关模块：**[OH_Camera](../../topics/media/OH_Camera.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_PhotoNative](../../topics/misc/OH_PhotoNative.md)OH_PhotoNative

相机照片对象。

 全质量图对象。

#### 函数

名称描述[Camera_ErrorCode OH_PhotoNative_GetMainImage(OH_PhotoNative* photo, OH_ImageNative** mainImage)](#ZH-CN_TOPIC_0000002529285791__oh_photonative_getmainimage)获取全质量图。[Camera_ErrorCode OH_PhotoNative_Release(OH_PhotoNative* photo)](#ZH-CN_TOPIC_0000002529285791__oh_photonative_release)释放全质量图实例。

#### 函数说明

#### OH_PhotoNative_GetMainImage()

```ets
Camera_ErrorCode OH_PhotoNative_GetMainImage(OH_PhotoNative* photo, OH_ImageNative** mainImage)
```

**描述**

获取全质量图。

**起始版本：** 12

**参数：**

参数项描述[OH_PhotoNative](../../topics/misc/OH_PhotoNative.md)* photoOH_PhotoNative实例。[OH_ImageNative](../../topics/graphics/OH_ImageNative.md)** mainImage用于获取全质量图的OH_ImageNative。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoNative_Release()

```ets
Camera_ErrorCode OH_PhotoNative_Release(OH_PhotoNative* photo)
```

**描述**

释放全质量图实例。

**起始版本：** 12

**参数：**

参数项描述[OH_PhotoNative](../../topics/misc/OH_PhotoNative.md)* photo要被释放的OH_PhotoNative实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。