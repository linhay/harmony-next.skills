# image_receiver_native.h

**概述**

声明从native层获取图片数据的方法。

引用文件： <multimedia/image_framework/image/image_receiver_native.h>

库： libimage_receiver.so

系统能力： SystemCapability.Multimedia.Image.ImageReceiver

起始版本： 12

相关模块： [Image_NativeModule](Image_NativeModule.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH_ImageReceiverNative | OH_ImageReceiverNative | OH_ImageReceiverNative是native层封装的图片接收器结构体，OH_ImageReceiverNative结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。 |
| OH_ImageReceiverOptions | OH_ImageReceiverOptions | 用于定义OH_ImageReceiverOptions数据类型名称。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_ImageReceiver_OnCallback)(OH_ImageReceiverNative *receiver) | OH_ImageReceiver_OnCallback | 定义native层图片的回调方法。 |
| typedef void (*OH_ImageReceiver_ImageArriveCallback)(OH_ImageReceiverNative *receiver, void *userData) | OH_ImageReceiver_ImageArriveCallback | ImageArrive事件的回调方法。 |
| Image_ErrorCode OH_ImageReceiverOptions_Create(OH_ImageReceiverOptions **options) | - | 创建应用层OH_ImageReceiverOptions对象。 |
| Image_ErrorCode OH_ImageReceiverOptions_GetSize(OH_ImageReceiverOptions* options, Image_Size* size) | - | 获取OH_ImageReceiverOptions对象的Image_Size。 |
| Image_ErrorCode OH_ImageReceiverOptions_SetSize(OH_ImageReceiverOptions* options, Image_Size size) | - | 设置OH_ImageReceiverOptions对象的Image_Size。 |
| Image_ErrorCode OH_ImageReceiverOptions_GetCapacity(OH_ImageReceiverOptions* options, int32_t* capacity) | - | 获取OH_ImageReceiverOptions对象的图片缓存容量。 |
| Image_ErrorCode OH_ImageReceiverOptions_SetCapacity(OH_ImageReceiverOptions* options, int32_t capacity) | - | 设置OH_ImageReceiverOptions对象的图片缓存容量。 |
| Image_ErrorCode OH_ImageReceiverOptions_Release(OH_ImageReceiverOptions* options) | - | 释放OH_ImageReceiverOptions对象。 |
| Image_ErrorCode OH_ImageReceiverNative_Create(OH_ImageReceiverOptions* options, OH_ImageReceiverNative** receiver) | - | 创建应用层OH_ImageReceiverNative对象。 |
| Image_ErrorCode OH_ImageReceiverNative_GetReceivingSurfaceId(OH_ImageReceiverNative* receiver, uint64_t* surfaceId) | - | 通过OH_ImageReceiverNative获取SurfaceId。 |
| Image_ErrorCode OH_ImageReceiverNative_ReadLatestImage(OH_ImageReceiverNative* receiver, OH_ImageNative** image) | - | 通过OH_ImageReceiverNative获取最新的一张图片。 注意，此接口需要在OH_ImageReceiver_OnCallback回调后调用，才能正常的接收到数据。并且此接口返回的OH_ImageNative使用完毕后需要调用OH_ImageNative_Release方法释放，释放后才可以继续接收新的数据。 |
| Image_ErrorCode OH_ImageReceiverNative_ReadNextImage(OH_ImageReceiverNative* receiver, OH_ImageNative** image) | - | 通过OH_ImageReceiverNative获取下一张图片。 注意，此接口需要在OH_ImageReceiver_OnCallback回调后调用，才能正常的接收到数据。并且此接口返回的OH_ImageNative使用完毕后需要调用OH_ImageNative_Release方法释放，释放后才可以继续接收新的数据。 |
| Image_ErrorCode OH_ImageReceiverNative_On(OH_ImageReceiverNative* receiver, OH_ImageReceiver_OnCallback callback) | - | 注册一个OH_ImageReceiver_OnCallback回调事件。 每当接收到新的图片，该回调事件就会响应。 |
| Image_ErrorCode OH_ImageReceiverNative_Off(OH_ImageReceiverNative* receiver) | - | 关闭OH_ImageReceiver_OnCallback回调事件。 关闭被OH_ImageReceiverNative_On开启的回调事件。 |
| Image_ErrorCode OH_ImageReceiverNative_GetSize(OH_ImageReceiverNative* receiver, Image_Size* size) | - | 通过OH_ImageReceiverNative获取ImageReceiver的大小。 |
| Image_ErrorCode OH_ImageReceiverNative_GetCapacity(OH_ImageReceiverNative* receiver, int32_t* capacity) | - | 通过OH_ImageReceiverNative获取ImageReceiver的容量。 |
| Image_ErrorCode OH_ImageReceiverNative_Release(OH_ImageReceiverNative* receiver) | - | 释放Native OH_ImageReceiverNative对象。 |
| Image_ErrorCode OH_ImageReceiverNative_OnImageArrive(OH_ImageReceiverNative *receiver, OH_ImageReceiver_ImageArriveCallback callback, void *userData) | - | 注册OH_ImageReceiver_ImageArriveCallback回调。 |
| Image_ErrorCode OH_ImageReceiverNative_OffImageArrive(OH_ImageReceiverNative *receiver, OH_ImageReceiver_ImageArriveCallback callback) | - | 注销OH_ImageReceiver_ImageArriveCallback回调。 |

**函数说明**

**OH_ImageReceiver_OnCallback()**

```ets
typedef void (*OH_ImageReceiver_OnCallback)(OH_ImageReceiverNative *receiver)
```

描述

定义native层图片的回调方法。

起始版本： 12

**OH_ImageReceiver_ImageArriveCallback()**

```ets
typedef void (*OH_ImageReceiver_ImageArriveCallback)(OH_ImageReceiverNative *receiver, void *userData)
```

描述

ImageArrive事件的回调方法。

起始版本： 20

**OH_ImageReceiverOptions_Create()**

```ets
Image_ErrorCode OH_ImageReceiverOptions_Create(OH_ImageReceiverOptions **options)
```

描述

创建应用层OH_ImageReceiverOptions对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverOptions **options | 表示作为获取结果的 OH_ImageReceiverOptions对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_ALLOC_FAILED：申请内存失败。 |

**OH_ImageReceiverOptions_GetSize()**

```ets
Image_ErrorCode OH_ImageReceiverOptions_GetSize(OH_ImageReceiverOptions* options, Image_Size* size)
```

描述

获取OH_ImageReceiverOptions对象的Image_Size。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverOptions* options | 表示OH_ImageReceiverOptions对象的指针。 |
| Image_Size* size | 表示作为获取结果的Image_Size对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageReceiverOptions_SetSize()**

```ets
Image_ErrorCode OH_ImageReceiverOptions_SetSize(OH_ImageReceiverOptions* options, Image_Size size)
```

描述

设置OH_ImageReceiverOptions对象的Image_Size。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverOptions* options | 表示OH_ImageReceiverOptions对象的指针。 |
| Image_Size size | 表示Image_Size对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageReceiverOptions_GetCapacity()**

```ets
Image_ErrorCode OH_ImageReceiverOptions_GetCapacity(OH_ImageReceiverOptions* options, int32_t* capacity)
```

描述

获取OH_ImageReceiverOptions对象的图片缓存容量。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverOptions* options | 表示OH_ImageReceiverOptions对象的指针。 |
| int32_t* capacity | 表示作为获取结果的图片缓存容量对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageReceiverOptions_SetCapacity()**

```ets
Image_ErrorCode OH_ImageReceiverOptions_SetCapacity(OH_ImageReceiverOptions* options, int32_t capacity)
```

描述

设置OH_ImageReceiverOptions对象的图片缓存容量。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverOptions* options | 表示OH_ImageReceiverOptions对象的指针。 |
| int32_t capacity | 表示图片缓存容量对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageReceiverOptions_Release()**

```ets
Image_ErrorCode OH_ImageReceiverOptions_Release(OH_ImageReceiverOptions* options)
```

描述

释放OH_ImageReceiverOptions对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverOptions* options | 表示OH_ImageReceiverOptions对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageReceiverNative_Create()**

```ets
Image_ErrorCode OH_ImageReceiverNative_Create(OH_ImageReceiverOptions* options, OH_ImageReceiverNative** receiver)
```

描述

创建应用层OH_ImageReceiverNative对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverOptions* options | 表示OH_ImageReceiverOptions对象的指针。 |
| OH_ImageReceiverNative** receiver | 表示作为获取结果的OH_ImageReceiverNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_ALLOC_FAILED：申请内存失败。 |

**OH_ImageReceiverNative_GetReceivingSurfaceId()**

```ets
Image_ErrorCode OH_ImageReceiverNative_GetReceivingSurfaceId(OH_ImageReceiverNative* receiver, uint64_t* surfaceId)
```

描述

通过OH_ImageReceiverNative获取SurfaceId。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverNative* receiver | 表示OH_ImageReceiverNative对象的指针。 |
| uint64_t* surfaceId | 表示作为获取结果的id对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。  IMAGE_UNKNOWN_ERROR：未知原因错误。 |

**OH_ImageReceiverNative_ReadLatestImage()**

```ets
Image_ErrorCode OH_ImageReceiverNative_ReadLatestImage(OH_ImageReceiverNative* receiver, OH_ImageNative** image)
```

描述

通过OH_ImageReceiverNative获取最新的一张图片。

注意，此接口需要在[OH_ImageReceiver_OnCallback](#ZH-CN_TOPIC_0000002553201947__oh_imagereceiver_oncallback)回调后调用，才能正常的接收到数据。并且此接口返回的OH_ImageNative使用完毕后需要调用[OH_ImageNative_Release](image_native.h.md#ZH-CN_TOPIC_0000002553361903__oh_imagenative_release)方法释放，释放后才可以继续接收新的数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverNative* receiver | 表示OH_ImageReceiverNative对象的指针。 |
| OH_ImageNative** image | 获取到的应用层的OH_ImageNative指针对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 IMAGE_UNKNOWN_ERROR：未知原因错误。  IMAGE_ALLOC_FAILED：申请内存失败。 |

**OH_ImageReceiverNative_ReadNextImage()**

```ets
Image_ErrorCode OH_ImageReceiverNative_ReadNextImage(OH_ImageReceiverNative* receiver, OH_ImageNative** image)
```

描述

通过OH_ImageReceiverNative获取下一张图片。

注意，此接口需要在[OH_ImageReceiver_OnCallback](#ZH-CN_TOPIC_0000002553201947__oh_imagereceiver_oncallback)回调后调用，才能正常的接收到数据。并且此接口返回的OH_ImageNative使用完毕后需要调用[OH_ImageNative_Release](image_native.h.md#ZH-CN_TOPIC_0000002553361903__oh_imagenative_release)方法释放，释放后才可以继续接收新的数据。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverNative* receiver | 表示OH_ImageReceiverNative对象的指针。 |
| OH_ImageNative** image | 获取到的应用层的OH_ImageNative指针对象。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。  IMAGE_BAD_PARAMETER：参数错误。 IMAGE_UNKNOWN_ERROR：未知原因错误。  IMAGE_ALLOC_FAILED：申请内存失败。 |

**OH_ImageReceiverNative_On()**

```ets
Image_ErrorCode OH_ImageReceiverNative_On(OH_ImageReceiverNative* receiver, OH_ImageReceiver_OnCallback callback)
```

描述

注册一个[OH_ImageReceiver_OnCallback](#ZH-CN_TOPIC_0000002553201947__oh_imagereceiver_oncallback)回调事件。

每当接收到新的图片，该回调事件就会响应。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverNative* receiver | 表示OH_ImageReceiverNative对象的指针。 |
| OH_ImageReceiver_OnCallback callback | 表示OH_ImageReceiver_OnCallback事件的回调函数。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageReceiverNative_Off()**

```ets
Image_ErrorCode OH_ImageReceiverNative_Off(OH_ImageReceiverNative* receiver)
```

描述

关闭[OH_ImageReceiver_OnCallback](#ZH-CN_TOPIC_0000002553201947__oh_imagereceiver_oncallback)回调事件。

关闭被[OH_ImageReceiverNative_On](#ZH-CN_TOPIC_0000002553201947__oh_imagereceivernative_on)开启的回调事件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverNative* receiver | 表示OH_ImageReceiverNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageReceiverNative_GetSize()**

```ets
Image_ErrorCode OH_ImageReceiverNative_GetSize(OH_ImageReceiverNative* receiver, Image_Size* size)
```

描述

通过OH_ImageReceiverNative获取ImageReceiver的大小。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverNative* receiver | 表示OH_ImageReceiverNative对象的指针。 |
| Image_Size* size | 表示作为获取结果的Image_Size对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageReceiverNative_GetCapacity()**

```ets
Image_ErrorCode OH_ImageReceiverNative_GetCapacity(OH_ImageReceiverNative* receiver, int32_t* capacity)
```

描述

通过OH_ImageReceiverNative获取ImageReceiver的容量。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverNative* receiver | 表示OH_ImageReceiverNative对象的指针。 |
| int32_t* capacity | 表示作为获取结果的图片缓存容量对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageReceiverNative_Release()**

```ets
Image_ErrorCode OH_ImageReceiverNative_Release(OH_ImageReceiverNative* receiver)
```

描述

释放Native OH_ImageReceiverNative对象。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverNative* receiver | 表示OH_ImageReceiverNative对象的指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：执行成功。 IMAGE_BAD_PARAMETER：参数错误。 |

**OH_ImageReceiverNative_OnImageArrive()**

```ets
Image_ErrorCode OH_ImageReceiverNative_OnImageArrive(OH_ImageReceiverNative *receiver,OH_ImageReceiver_ImageArriveCallback callback, void *userData)
```

描述

注册[OH_ImageReceiver_ImageArriveCallback](#ZH-CN_TOPIC_0000002553201947__oh_imagereceiver_imagearrivecallback)回调。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverNative *receiver | 处理回调的OH_ImageReceiverNative对象。 |
| OH_ImageReceiver_ImageArriveCallback callback | 要注册的OH_ImageReceiver_ImageArriveCallback回调方法。 |
| void *userData | 用户自定义数据指针。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_RECEIVER_INVALID_PARAMETER：参数错误。 |

**OH_ImageReceiverNative_OffImageArrive()**

```ets
Image_ErrorCode OH_ImageReceiverNative_OffImageArrive(OH_ImageReceiverNative *receiver,OH_ImageReceiver_ImageArriveCallback callback)
```

描述

注销[OH_ImageReceiver_ImageArriveCallback](#ZH-CN_TOPIC_0000002553201947__oh_imagereceiver_imagearrivecallback)回调。

起始版本： 20

参数：

| 参数项 | 描述 |
| --- | --- |
| OH_ImageReceiverNative *receiver | 处理回调的OH_ImageReceiverNative对象。 |
| OH_ImageReceiver_ImageArriveCallback callback | 要注册的OH_ImageReceiver_ImageArriveCallback回调。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Image_ErrorCode | IMAGE_SUCCESS：操作成功。  IMAGE_RECEIVER_INVALID_PARAMETER：参数错误，receiver或callback未注册。 |