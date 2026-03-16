# native_image.h

#### 概述

定义获取和使用NativeImage的相关函数。

**引用文件：** <native_image/native_image.h>

**库：** libnative_image.so

**起始版本：** 9

**相关模块：**[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)

#### 汇总

#### 结构体

名称typedef关键字描述[OH_OnFrameAvailableListener](../../topics/components/OH_OnFrameAvailableListener.md)OH_OnFrameAvailableListener一个OH_NativeImage的监听者，通过[OH_NativeImage_SetOnFrameAvailableListener](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_setonframeavailablelistener)接口注册该监听结构体，当有buffer可获取时，将触发回调给用户。[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)OH_NativeImage提供OH_NativeImage结构体声明。[NativeWindow](../../topics/misc/NativeWindow.md)OHNativeWindow提供对NativeWindow的访问功能。[NativeWindowBuffer](../../topics/misc/NativeWindowBuffer.md)OHNativeWindowBuffer提供NativeWindowBuffer结构体声明。

#### 函数

名称typedef关键字描述[typedef void (*OH_OnFrameAvailable)(void *context)](#ZH-CN_TOPIC_0000002497446038__oh_onframeavailable)OH_OnFrameAvailable有buffer可获取时触发的回调函数。[OH_NativeImage* OH_NativeImage_Create(uint32_t textureId, uint32_t textureTarget)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_create)-

创建一个OH_NativeImage实例，该实例与OpenGL ES的纹理ID和纹理目标相关联。

本接口需要与[OH_NativeImage_Destroy](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

[OHNativeWindow* OH_NativeImage_AcquireNativeWindow(OH_NativeImage* image)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_acquirenativewindow)-

获取与OH_NativeImage相关联的OHNativeWindow指针。

本接口为非线程安全类型接口。

OH_NativeImage析构时会将对应的OHNativeWindow实例释放。若从本接口获取OHNativeWindow指针，当OH_NativeImage实例释放时，请将获取到的OHNativeWindow指针置空，防止后续产生野指针。

[int32_t OH_NativeImage_AttachContext(OH_NativeImage* image, uint32_t textureId)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_attachcontext)-

将OH_NativeImage实例附加到当前OpenGL ES上下文，且该OpenGL ES纹理会绑定到GL_TEXTURE_EXTERNAL_OES, 并通过OH_NativeImage进行更新。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_DetachContext(OH_NativeImage* image)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_detachcontext)-

将OH_NativeImage实例从当前OpenGL ES上下文分离。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_UpdateSurfaceImage(OH_NativeImage* image)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)-

通过OH_NativeImage获取最新帧更新相关联的OpenGL ES纹理。

本接口需要在Opengl ES环境上下文的线程中调用。

本接口需要在接收到[OH_OnFrameAvailableListener](../../topics/components/OH_OnFrameAvailableListener.md)回调后调用。

本接口为非线程安全类型接口。

[int64_t OH_NativeImage_GetTimestamp(OH_NativeImage* image)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_gettimestamp)-

获取最近调用OH_NativeImage_UpdateSurfaceImage的纹理图像的相关时间戳。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_GetTransformMatrix(OH_NativeImage* image, float matrix[16])](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_gettransformmatrix)-获取最近调用OH_NativeImage_UpdateSurfaceImage的纹理图像的变化矩阵。[int32_t OH_NativeImage_GetSurfaceId(OH_NativeImage* image, uint64_t* surfaceId)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_getsurfaceid)-

获取OH_NativeImage的surface编号。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_SetOnFrameAvailableListener(OH_NativeImage* image, OH_OnFrameAvailableListener listener)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_setonframeavailablelistener)-

设置帧可用回调。

不允许在回调函数中调用本模块的其他接口。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_UnsetOnFrameAvailableListener(OH_NativeImage* image)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_unsetonframeavailablelistener)-

取消设置帧可用回调。

本接口为非线程安全类型接口。

[void OH_NativeImage_Destroy(OH_NativeImage** image)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_destroy)-

销毁通过OH_NativeImage_Create创建的OH_NativeImage实例, 销毁后该

OH_NativeImage指针会被赋值为空。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_GetTransformMatrixV2(OH_NativeImage* image, float matrix[16])](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_gettransformmatrixv2)-

根据生产端设置的旋转角度，获取最近调用OH_NativeImage_UpdateSurfaceImage的纹理图像的变化矩阵。

matrix在[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口调用后，才会更新。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_GetBufferMatrix(OH_NativeImage* image, float matrix[16])](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_getbuffermatrix)-

获取根据生产端设置的旋转角度和buffer实际有效内容区域计算出的变换矩阵。

本接口返回一个变换矩阵，该矩阵是[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)在消费buffer，即调用[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)或者[OH_NativeImage_AcquireNativeWindowBuffer](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_acquirenativewindowbuffer)时，根据buffer的旋转角度和实际有效内容区域计算所得。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_AcquireNativeWindowBuffer(OH_NativeImage* image,OHNativeWindowBuffer** nativeWindowBuffer, int* fenceFd)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_acquirenativewindowbuffer)-

通过消费端的OH_NativeImage获取一个OHNativeWindowBuffer。

本接口不能与[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口将会创建一个OHNativeWindowBuffer。

当使用OHNativeWindowBuffer时，用户需要通过[OH_NativeWindow_NativeObjectReference](external_window.h.md#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectreference)接口将其引用计数加一。

当OHNativeWindowBuffer使用完，用户需要通过[OH_NativeWindow_NativeObjectUnreference](external_window.h.md#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectunreference)接口将其引用计数减一。

本接口需要和[OH_NativeImage_ReleaseNativeWindowBuffer](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_releasenativewindowbuffer)接口配合使用，否则会存在内存泄露。

当fenceFd使用完，用户需要将其close。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_ReleaseNativeWindowBuffer(OH_NativeImage* image,OHNativeWindowBuffer* nativeWindowBuffer, int fenceFd)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_releasenativewindowbuffer)-

通过OH_NativeImage实例将OHNativeWindowBuffer归还到buffer队列中。

系统会将fenceFd关闭，无需用户close。

本接口为非线程安全类型接口。

[OH_NativeImage* OH_ConsumerSurface_Create(void)](#ZH-CN_TOPIC_0000002497446038__oh_consumersurface_create)-

创建一个OH_NativeImage实例，作为surface的消费端。

本接口仅用于surface消费端的内存轮转，创建的OH_NativeImage内部不会主动进行内存渲染处理。

本接口不能与[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口与[OH_NativeImage_AcquireNativeWindowBuffer](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_acquirenativewindowbuffer)和[OH_NativeImage_ReleaseNativeWindowBuffer](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_releasenativewindowbuffer)配合使用。

本接口需要和[OH_NativeImage_Destroy](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

[int32_t OH_ConsumerSurface_SetDefaultUsage(OH_NativeImage* image, uint64_t usage)](#ZH-CN_TOPIC_0000002497446038__oh_consumersurface_setdefaultusage)-

设置默认读写方式。

本接口为非线程安全类型接口。

[int32_t OH_ConsumerSurface_SetDefaultSize(OH_NativeImage* image, int32_t width, int32_t height)](#ZH-CN_TOPIC_0000002497446038__oh_consumersurface_setdefaultsize)-

设置几何图形默认尺寸。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_SetDropBufferMode(OH_NativeImage* image, bool isOpen)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_setdropbuffermode)-

设置OH_NativeImage是否为渲染丢帧模式。

处于此模式时，大部分生产端生产的buffer将会被丢弃，最新的buffer会及时上屏渲染。

此模式不能同时保证帧率高的要求。

此接口建议在[OH_NativeImage_Create](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_create)接口调用后立即调用。

此接口在与[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口一起使用的场景下才会生效。

本接口为非线程安全类型接口。

[OH_NativeImage* OH_NativeImage_CreateWithSingleBufferMode(uint32_t textureId, uint32_t textureTarget, bool singleBufferMode)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_createwithsinglebuffermode)-

使用纹理ID创建一个OH_NativeImage实例，该实例与OpenGL ES的纹理ID和纹理目标相关联，并选择是否设置单buffer模式。

本接口需要与[OH_NativeImage_Destroy](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

[OH_NativeImage* OH_ConsumerSurface_CreateWithSingleBufferMode(bool singleBufferMode)](#ZH-CN_TOPIC_0000002497446038__oh_consumersurface_createwithsinglebuffermode)-

不使用纹理ID创建一个[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)实例，作为surface的消费端，并选择是否设置单buffer模式。

本接口仅用于surface消费端的内存轮转，创建的[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)内部不会主动进行内存渲染处理。

本接口不能与[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口需要和[OH_NativeImage_Destroy](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_ReleaseTextImage(OH_NativeImage* image)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_releasetextimage)-

解除SurfaceBuffer与纹理的绑定，将纹理恢复到未使用状态。

单buffer模式下，需要调用该接口释放纹理，否则生产者下次无法申请buffer。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_GetColorSpace(OH_NativeImage* image, OH_NativeBuffer_ColorSpace* colorSpace)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_getcolorspace)-

获取最近调用[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)的纹理图像的相关色彩空间。

本接口为非线程安全类型接口。

[int32_t OH_NativeImage_AcquireLatestNativeWindowBuffer(OH_NativeImage* image, OHNativeWindowBuffer** nativeWindowBuffer, int* fenceFd)](#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_acquirelatestnativewindowbuffer)-

通过消费端的OH_NativeImage获取一个生产者最近生产的OHNativeWindowBuffer，并将其余buffer丢弃。

消费端可以通过[OH_OnFrameAvailableListener](../../topics/components/OH_OnFrameAvailableListener.md)注册的回调，收到所有可用buffer（包括被丢弃的buffer)的回调。

本接口不能与[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口为非线程安全类型接口。

#### 函数说明

#### OH_OnFrameAvailable()

```ets
typedef void (*OH_OnFrameAvailable)(void *context)
```

**描述**

有buffer可获取时触发的回调函数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 11

**参数：**

参数项描述void *context用户自定义的上下文信息，会在回调触发时返回给用户。

#### OH_NativeImage_Create()

```ets
OH_NativeImage* OH_NativeImage_Create(uint32_t textureId, uint32_t textureTarget)
```

**描述**

创建一个OH_NativeImage实例，该实例与OpenGL ES的纹理ID和纹理目标相关联。

本接口需要与[OH_NativeImage_Destroy](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

参数项描述uint32_t textureIdOpenGL ES的纹理ID，OH_NativeImage实例会与之相关联。uint32_t textureTargetOpenGL ES的纹理目标，取值范围为GL_TEXTURE_2D和GL_TEXTURE_EXTERNAL_OES，具体可见[选择纹理类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-12)。

**返回：**

类型说明OH_NativeImage*创建成功则返回一个指向OH_NativeImage实例的指针，否则返回NULL。

#### OH_NativeImage_AcquireNativeWindow()

```ets
OHNativeWindow* OH_NativeImage_AcquireNativeWindow(OH_NativeImage* image)
```

**描述**

获取与OH_NativeImage相关联的OHNativeWindow指针。

本接口为非线程安全类型接口。

OH_NativeImage析构时会将对应的OHNativeWindow实例释放。若从本接口获取OHNativeWindow指针，当OH_NativeImage实例释放时，请将获取到的OHNativeWindow指针置空，防止后续产生野指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。

**返回：**

类型说明[OHNativeWindow](../../topics/misc/NativeWindow.md)*成功则返回一个指向OHNativeWindow实例的指针，否则返回NULL。

#### OH_NativeImage_AttachContext()

```ets
int32_t OH_NativeImage_AttachContext(OH_NativeImage* image, uint32_t textureId)
```

**描述**

将OH_NativeImage实例附加到当前OpenGL ES上下文，且该OpenGL ES纹理会绑定到GL_TEXTURE_EXTERNAL_OES, 并通过OH_NativeImage进行更新。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。uint32_t textureId是OH_NativeImage要附加到的OpenGL ES纹理的id。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeImage_DetachContext()

```ets
int32_t OH_NativeImage_DetachContext(OH_NativeImage* image)
```

**描述**

将OH_NativeImage实例从当前OpenGL ES上下文分离。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeImage_UpdateSurfaceImage()

```ets
int32_t OH_NativeImage_UpdateSurfaceImage(OH_NativeImage* image)
```

**描述**

通过OH_NativeImage获取最新帧更新相关联的OpenGL ES纹理。

本接口需要在Opengl ES环境上下文的线程中调用。

本接口需要在接收到[OH_OnFrameAvailableListener](../../topics/components/OH_OnFrameAvailableListener.md)回调后调用。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeImage_GetTimestamp()

```ets
int64_t OH_NativeImage_GetTimestamp(OH_NativeImage* image)
```

**描述**

获取最近调用OH_NativeImage_UpdateSurfaceImage的纹理图像的相关时间戳。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。

**返回：**

类型说明int64_t返回纹理图像的相关时间戳。

#### OH_NativeImage_GetTransformMatrix()

```ets
int32_t OH_NativeImage_GetTransformMatrix(OH_NativeImage* image, float matrix[16])
```

**描述**

获取最近调用OH_NativeImage_UpdateSurfaceImage的纹理图像的变化矩阵。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**废弃版本：** 从API version 12开始废弃。

**替代接口：**[OH_NativeImage_GetTransformMatrixV2](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_gettransformmatrixv2)

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。matrix用来存储要获取的4*4的变化矩阵。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeImage_GetSurfaceId()

```ets
int32_t OH_NativeImage_GetSurfaceId(OH_NativeImage* image, uint64_t* surfaceId)
```

**描述**

获取OH_NativeImage的surface编号。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 11

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。uint64_t* surfaceId是指向surface编号的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeImage_SetOnFrameAvailableListener()

```ets
int32_t OH_NativeImage_SetOnFrameAvailableListener(OH_NativeImage* image, OH_OnFrameAvailableListener listener)
```

**描述**

设置帧可用回调。

不允许在回调函数中调用本模块的其他接口。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 11

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。[OH_OnFrameAvailableListener](../../topics/components/OH_OnFrameAvailableListener.md) listener表示回调监听者。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeImage_UnsetOnFrameAvailableListener()

```ets
int32_t OH_NativeImage_UnsetOnFrameAvailableListener(OH_NativeImage* image)
```

**描述**

取消设置帧可用回调。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 11

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。

**返回：**

类型说明int32_t返回值为0表示执行成功，其他返回值可参考[OHNativeErrorCode](graphic_error_code.h.md#ZH-CN_TOPIC_0000002497446040__ohnativeerrorcode)。

#### OH_NativeImage_Destroy()

```ets
void OH_NativeImage_Destroy(OH_NativeImage** image)
```

**描述**

销毁通过OH_NativeImage_Create创建的OH_NativeImage实例, 销毁后该

OH_NativeImage指针会被赋值为空。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 9

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)** image指向OH_NativeImage实例的指针。

#### OH_NativeImage_GetTransformMatrixV2()

```ets
int32_t OH_NativeImage_GetTransformMatrixV2(OH_NativeImage* image, float matrix[16])
```

**描述**

根据生产端设置的旋转角度，获取最近调用OH_NativeImage_UpdateSurfaceImage的纹理图像的变化矩阵。

matrix在[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口调用后，才会更新。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 12

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。matrix用来存储要获取的4*4的变化矩阵。

**返回：**

类型说明int32_t

返回接口执行结果。NATIVE_ERROR_OK，表示接口执行成功。

 返回NATIVE_ERROR_INVALID_ARGUMENTS，对应错误码为40001000，表示image参数为空。

 返回NATIVE_ERROR_UNKNOWN，对应错误码为50002000，表示未知错误，请查看日志。

#### OH_NativeImage_GetBufferMatrix()

```ets
int32_t OH_NativeImage_GetBufferMatrix(OH_NativeImage* image, float matrix[16])
```

**描述**

获取根据生产端设置的旋转角度和buffer实际有效内容区域计算出的变换矩阵。

本接口返回一个变换矩阵，该矩阵是[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)在消费buffer，即调用[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)或者[OH_NativeImage_AcquireNativeWindowBuffer](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_acquirenativewindowbuffer)时，根据buffer的旋转角度和实际有效内容区域计算所得。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 15

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)实例的指针。matrix用于存储获取的4*4变换矩阵。

**返回：**

类型说明int32_t

返回接口执行结果。NATIVE_ERROR_OK，表示接口执行成功。

 返回NATIVE_ERROR_INVALID_ARGUMENTS，对应错误码为40001000，表示image参数为空。

 返回NATIVE_ERROR_MEM_OPERATION_ERROR，对应错误码为30001000，表示内存操作错误，获取变换矩阵失败。

#### OH_NativeImage_AcquireNativeWindowBuffer()

```ets
int32_t OH_NativeImage_AcquireNativeWindowBuffer(OH_NativeImage* image,OHNativeWindowBuffer** nativeWindowBuffer, int* fenceFd)
```

**描述**

通过消费端的OH_NativeImage获取一个OHNativeWindowBuffer。本接口不能与[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口将会创建一个OHNativeWindowBuffer。当使用OHNativeWindowBuffer时，用户需要通过[OH_NativeWindow_NativeObjectReference](external_window.h.md#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectreference)接口将其引用计数加一。当OHNativeWindowBuffer使用完，用户需要通过[OH_NativeWindow_NativeObjectUnreference](external_window.h.md#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectunreference)接口将其引用计数减一。

本接口需要和[OH_NativeImage_ReleaseNativeWindowBuffer](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_releasenativewindowbuffer)接口配合使用，否则会存在内存泄露。

当fenceFd使用完，用户需要将其close。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 12

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。[OHNativeWindowBuffer](../../topics/misc/NativeWindowBuffer.md)** nativeWindowBuffer指向OHNativeWindowBuffer指针的指针。int* fenceFd指向文件描述符句柄的指针。

**返回：**

类型说明int32_t

执行成功时返回NATIVE_ERROR_OK。

 image, nativeWindowBuffer, fenceFd是空指针时返回NATIVE_ERROR_INVALID_ARGUMENTS。

 没有buffer可以消费时返回NATIVE_ERROR_NO_BUFFER。

#### OH_NativeImage_ReleaseNativeWindowBuffer()

```ets
int32_t OH_NativeImage_ReleaseNativeWindowBuffer(OH_NativeImage* image,OHNativeWindowBuffer* nativeWindowBuffer, int fenceFd)
```

**描述**

通过OH_NativeImage实例将OHNativeWindowBuffer归还到buffer队列中。

系统会将fenceFd关闭，无需用户close。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 12

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。[OHNativeWindowBuffer](../../topics/misc/NativeWindowBuffer.md)* nativeWindowBuffer指向OHNativeWindowBuffer实例的指针。int fenceFd指向文件描述符句柄, 用于并发同步控制。

**返回：**

类型说明int32_t

执行成功时返回NATIVE_ERROR_OK。

 image, nativeWindowBuffer是空指针时返回NATIVE_ERROR_INVALID_ARGUMENTS。

 nativeWindowBuffer为状态非法时返回NATIVE_ERROR_BUFFER_STATE_INVALID。

 nativeWindowBuffer不在缓存中返回NATIVE_ERROR_BUFFER_NOT_IN_CACHE。

#### OH_ConsumerSurface_Create()

```ets
OH_NativeImage* OH_ConsumerSurface_Create(void)
```

**描述**

创建一个OH_NativeImage实例，作为surface的消费端。

本接口仅用于surface消费端的内存轮转，创建的OH_NativeImage内部不会主动进行内存渲染处理。

本接口不能与[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口与[OH_NativeImage_AcquireNativeWindowBuffer](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_acquirenativewindowbuffer)和[OH_NativeImage_ReleaseNativeWindowBuffer](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_releasenativewindowbuffer)配合使用。

本接口需要和[OH_NativeImage_Destroy](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 12

**返回：**

类型说明[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)*成功则返回一个指向OH_NativeImage实例的指针，否则返回NULL。

#### OH_ConsumerSurface_SetDefaultUsage()

```ets
int32_t OH_ConsumerSurface_SetDefaultUsage(OH_NativeImage* image, uint64_t usage)
```

**描述**

设置默认读写方式。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 13

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。uint64_t usage表示读写方式。枚举值参考[OH_NativeBuffer_Usage](native_buffer.h.md#ZH-CN_TOPIC_0000002529445959__oh_nativebuffer_usage)。

**返回：**

类型说明int32_t

执行成功时返回NATIVE_ERROR_OK。

 image是空指针时返回NATIVE_ERROR_INVALID_ARGUMENTS。

#### OH_ConsumerSurface_SetDefaultSize()

```ets
int32_t OH_ConsumerSurface_SetDefaultSize(OH_NativeImage* image, int32_t width, int32_t height)
```

**描述**

设置几何图形默认尺寸。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 13

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。int32_t width表示几何图形宽度，取值范围大于0，单位为像素。int32_t height表示几何图形高度，取值范围大于0，单位为像素。

**返回：**

类型说明int32_t

执行成功时返回NATIVE_ERROR_OK。

 image是空指针时，或width、height小于等于0时返回NATIVE_ERROR_INVALID_ARGUMENTS。

#### OH_NativeImage_SetDropBufferMode()

```ets
int32_t OH_NativeImage_SetDropBufferMode(OH_NativeImage* image, bool isOpen)
```

**描述**

设置OH_NativeImage是否为渲染丢帧模式。

处于此模式时，大部分生产端生产的buffer将会被丢弃，最新的buffer会及时上屏渲染。

此模式不能同时保证帧率高的要求。

此接口建议在[OH_NativeImage_Create](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_create)接口调用后立即调用。

此接口在与[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口一起使用的场景下才会生效。

本接口为非线程安全类型接口。

通过[OH_NativeImage_SetOnFrameAvailableListener](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_setonframeavailablelistener)设置的listener回调不会因为设置了丢帧模式而减少。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 17

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。bool isOpen是否设置渲染丢帧。true表示设置为渲染丢帧模式，false表示不设置。

**返回：**

类型说明int32_t

执行成功时返回NATIVE_ERROR_OK。

 image是空指针时返回NATIVE_ERROR_INVALID_ARGUMENTS。

#### OH_NativeImage_CreateWithSingleBufferMode()

```ets
OH_NativeImage* OH_NativeImage_CreateWithSingleBufferMode(uint32_t textureId, uint32_t textureTarget, bool singleBufferMode)
```

**描述**

使用纹理ID创建一个OH_NativeImage实例，该实例与OpenGL ES的纹理ID和纹理目标相关联，并选择是否设置单buffer模式。

本接口需要与[OH_NativeImage_Destroy](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 22

**参数：**

参数项描述uint32_t textureIdOpenGL ES的纹理ID，OH_NativeImage实例会与之相关联。uint32_t textureTargetOpenGL ES的纹理目标，具体可见[选择纹理类型](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-12)。bool singleBufferMode是否设置单buffer模式。true表示设置为单buffer模式，false表示不设置。

**返回：**

类型说明[OH_NativeImage*](../../topics/graphics/OH_NativeImage.md)创建成功则返回一个指向OH_NativeImage实例的指针，否则返回NULL。

#### OH_ConsumerSurface_CreateWithSingleBufferMode()

```ets
OH_NativeImage* OH_ConsumerSurface_CreateWithSingleBufferMode(bool singleBufferMode)
```

**描述**

不使用纹理ID创建一个[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)实例，作为surface的消费端，并选择是否设置单buffer模式。

本接口仅用于surface消费端的内存轮转，创建的[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)内部不会主动进行内存渲染处理。

本接口不能与[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口需要和[OH_NativeImage_Destroy](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_destroy)接口配合使用，否则会存在内存泄露。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 22

**参数：**

参数项描述bool singleBufferMode是否设置单buffer模式。true表示设置为单buffer模式，false表示不设置。

**返回：**

类型说明[OH_NativeImage*](../../topics/graphics/OH_NativeImage.md)成功则返回一个指向[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)实例的指针，否则返回NULL。

#### OH_NativeImage_ReleaseTextImage()

```ets
int32_t OH_NativeImage_ReleaseTextImage(OH_NativeImage* image)
```

**描述**

解除SurfaceBuffer与纹理的绑定，将纹理恢复到未使用状态。

单buffer模式下，需要调用该接口释放纹理，否则生产者下次无法申请buffer。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 22

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)实例的指针。

**返回：**

类型说明int32_t

执行成功时返回NATIVE_ERROR_OK。

image是空指针时返回NATIVE_ERROR_INVALID_ARGUMENTS。

#### OH_NativeImage_GetColorSpace()

```ets
int32_t OH_NativeImage_GetColorSpace(OH_NativeImage* image, OH_NativeBuffer_ColorSpace* colorSpace)
```

**描述**

获取最近调用[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)的纹理图像的相关色彩空间。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 22

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)实例的指针。OH_NativeBuffer_ColorSpace* colorSpace为[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)设置的颜色空间，其值从[OH_NativeBuffer_ColorSpace](buffer_common.h.md#ZH-CN_TOPIC_0000002529285985__oh_nativebuffer_colorspace)获取。

**返回：**

类型说明int32_t

执行成功时返回NATIVE_ERROR_OK。

image，colorSpace是空指针时返回NATIVE_ERROR_INVALID_ARGUMENTS。

#### OH_NativeImage_AcquireLatestNativeWindowBuffer()

```ets
int32_t OH_NativeImage_AcquireLatestNativeWindowBuffer(OH_NativeImage* image, OHNativeWindowBuffer** nativeWindowBuffer, int* fenceFd)
```

**描述**

通过消费端的OH_NativeImage获取一个生产者最近生产的OHNativeWindowBuffer，并将其余buffer丢弃。

消费端可以通过[OH_OnFrameAvailableListener](../../topics/components/OH_OnFrameAvailableListener.md)注册的回调，收到所有可用buffer（包括被丢弃的buffer)的回调。

本接口不能与[OH_NativeImage_UpdateSurfaceImage](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_updatesurfaceimage)接口同时使用。

本接口将会创建一个OHNativeWindowBuffer。当使用OHNativeWindowBuffer时，用户需要通过[OH_NativeWindow_NativeObjectReference](external_window.h.md#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectreference)接口将其引用计数加一。

当OHNativeWindowBuffer使用完，用户需要通过[OH_NativeWindow_NativeObjectUnreference](external_window.h.md#ZH-CN_TOPIC_0000002497606020__oh_nativewindow_nativeobjectunreference)接口将其引用计数减一。

本接口需要和[OH_NativeImage_ReleaseNativeWindowBuffer](native_image.h.md#ZH-CN_TOPIC_0000002497446038__oh_nativeimage_releasenativewindowbuffer)接口配合使用，否则会存在内存泄露。

当fenceFd使用完，用户需要将其close。

本接口为非线程安全类型接口。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeImage

**起始版本：** 22

**参数：**

参数项描述[OH_NativeImage](../../topics/graphics/OH_NativeImage.md)* image指向OH_NativeImage实例的指针。[OHNativeWindowBuffer](../../topics/misc/NativeWindowBuffer.md)** nativeWindowBuffer指向OHNativeWindowBuffer的二级指针。int* fenceFd指向文件描述符句柄的指针。

**返回：**

类型说明int32_t

执行成功时返回NATIVE_ERROR_OK。

image，nativeWindowBuffer或fenceFd是空指针时返回NATIVE_ERROR_INVALID_ARGUMENTS。

没有buffer可以消费时返回NATIVE_ERROR_NO_BUFFER。