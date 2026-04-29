# image_pixel_map_napi.h

**概述**

声明可以锁定并访问pixelmap数据的方法，声明解锁的方法。

库： libpixelmap_ndk.z.so

系统能力： SystemCapability.Multimedia.Image.Core

引用文件： <multimedia/image_framework/image_pixel_map_napi.h>

起始版本： 8

相关模块： [Image](Image.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OhosPixelMapInfo | - | 用于定义PixelMap的相关信息。 |

**枚举**

| 名称 | 描述 |
| --- | --- |
| 方法返回的错误码 | 函数方法返回值的错误码的枚举。 |
| 像素格式 | 像素格式的枚举。 |
| anonymous enum | PixelMap缩放类型的枚举。 |

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t OH_GetImageInfo(napi_env env, napi_value value, OhosPixelMapInfo *info) | 获取PixelMap的信息，并记录信息到OhosPixelMapInfo结构中。 |
| int32_t OH_AccessPixels(napi_env env, napi_value value, void** addrPtr) | 获取PixelMap对象数据的内存地址，并锁定该内存。 函数执行成功后，*addrPtr就是获取的待访问的内存地址。访问操作完成后，必须要使用OH_UnAccessPixels来释放锁，否则的话资源无法被释放。待解锁后，内存地址就不可以再被访问和操作。 |
| int32_t OH_UnAccessPixels(napi_env env, napi_value value) | 释放PixelMap对象数据的内存锁，用于匹配方法OH_AccessPixels。 |

**枚举类型说明**

**方法返回的错误码**

```ets
enum anonymous enum
```

描述

函数方法返回值的错误码的枚举。

起始版本： 8

废弃版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OHOS_IMAGE_RESULT_SUCCESS = 0 | 成功的结果。 |
| OHOS_IMAGE_RESULT_BAD_PARAMETER = -1 | 无效值。 |

**像素格式**

```ets
enum anonymous enum
```

描述

像素格式的枚举。

起始版本： 8

废弃版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OHOS_PIXEL_MAP_FORMAT_NONE = 0 | 未知的格式。 |
| OHOS_PIXEL_MAP_FORMAT_RGBA_8888 = 3 | RGBA_8888格式。 |
| OHOS_PIXEL_MAP_FORMAT_RGB_565 = 2 | RGB_565格式。 |

**PixelMap缩放类型**

```ets
enum anonymous enum
```

描述

PixelMap缩放类型的枚举。

起始版本： 10

| 枚举项 | 描述 |
| --- | --- |
| OHOS_PIXEL_MAP_SCALE_MODE_FIT_TARGET_SIZE = 0 | 适应目标图片大小的格式。 |
| OHOS_PIXEL_MAP_SCALE_MODE_CENTER_CROP = 1 | 以中心进行缩放的格式。 |

**函数说明**

**OH_GetImageInfo()**

```ets
int32_t OH_GetImageInfo(napi_env env, napi_value value, OhosPixelMapInfo *info)
```

描述

获取PixelMap的信息，并记录信息到[OhosPixelMapInfo](OhosPixelMapInfo.md)结构中。

起始版本： 8

废弃版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| napi_env env | napi的环境指针。 |
| napi_value value | 应用层的PixelMap对象。 |
| OhosPixelMapInfo *info | 用于保存信息的指针对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码： OHOS_IMAGE_RESULT_SUCCESS：操作成功。 OHOS_IMAGE_RESULT_BAD_PARAMETER：操作失败。 |

**OH_AccessPixels()**

```ets
int32_t OH_AccessPixels(napi_env env, napi_value value, void** addrPtr)
```

描述

获取PixelMap对象数据的内存地址，并锁定该内存。

函数执行成功后，*addrPtr就是获取的待访问的内存地址。访问操作完成后，必须要使用[OH_UnAccessPixels](#ZH-CN_TOPIC_0000002553201951__oh_unaccesspixels)来释放锁，否则的话资源无法被释放。待解锁后，内存地址就不可以再被访问和操作。

起始版本： 8

废弃版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| napi_env env | napi的环境指针。 |
| napi_value value | 应用层的PixelMap对象。 |
| void** addrPtr | 用于指向的内存地址的双指针对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码： OHOS_IMAGE_RESULT_SUCCESS：操作成功。 OHOS_IMAGE_RESULT_BAD_PARAMETER：操作失败。 |

**OH_UnAccessPixels()**

```ets
int32_t OH_UnAccessPixels(napi_env env, napi_value value)
```

描述

释放PixelMap对象数据的内存锁，用于匹配方法[OH_AccessPixels](#ZH-CN_TOPIC_0000002553201951__oh_accesspixels)。

起始版本： 8

废弃版本： 10

参数：

| 参数项 | 描述 |
| --- | --- |
| napi_env env | napi的环境指针。 |
| napi_value value | 应用层的PixelMap对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | 错误码： OHOS_IMAGE_RESULT_SUCCESS：操作成功。 OHOS_IMAGE_RESULT_BAD_PARAMETER：操作失败。 |