# photo_native.h

**概述**

声明相机照片的概念。

引用文件： <ohcamera/photo_native.h>

库： libohcamera.so

系统能力： SystemCapability.Multimedia.Camera.Core

起始版本： 12

相关模块： [OH_Camera](OH_Camera.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_PhotoNative | OH_PhotoNative | 相机照片对象。  全质量图对象。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| Camera_ErrorCode OH_PhotoNative_GetMainImage(OH_PhotoNative* photo, OH_ImageNative** mainImage) | 获取全质量图。 |
| Camera_ErrorCode OH_PhotoNative_GetUncompressedImage(OH_PhotoNative* photo, OH_PictureNative** picture) | 获取非压缩图片。 |
| Camera_ErrorCode OH_PhotoNative_Release(OH_PhotoNative* photo) | 释放全质量图实例。 |

**函数说明**

**OH_PhotoNative_GetMainImage()**

```ets
Camera_ErrorCode OH_PhotoNative_GetMainImage(OH_PhotoNative* photo, OH_ImageNative** mainImage)
```

描述

获取全质量图。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PhotoNative* photo | OH_PhotoNative实例。 |
| OH_ImageNative** mainImage | 用于获取全质量图的OH_ImageNative。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_PhotoNative_GetUncompressedImage()**

```ets
Camera_ErrorCode OH_PhotoNative_GetUncompressedImage(OH_PhotoNative* photo, OH_PictureNative** picture)
```

描述

获取非压缩图片。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PhotoNative* photo | OH_PhotoNative实例。 |
| OH_PictureNative** picture | 用于获取非压缩图片的OH_PictureNative。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_PhotoNative_Release()**

```ets
Camera_ErrorCode OH_PhotoNative_Release(OH_PhotoNative* photo)
```

描述

释放全质量图实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_PhotoNative* photo | 要被释放的OH_PhotoNative实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |