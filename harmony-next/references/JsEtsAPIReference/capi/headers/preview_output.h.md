# preview_output.h

#### 概述

声明预览输出概念。

**引用文件：** <ohcamera/preview_output.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：**[OH_Camera](../../topics/media/OH_Camera.md)

#### 汇总

#### 结构体

名称typedef关键字描述[PreviewOutput_Callbacks](../../topics/misc/PreviewOutput_Callbacks.md)PreviewOutput_Callbacks用于预览输出的回调。[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)Camera_PreviewOutput

预览输出对象。

 可以使用[OH_CameraManager_CreatePreviewOutput](camera_manager.h.md#ZH-CN_TOPIC_0000002529445763__oh_cameramanager_createpreviewoutput)方法创建指针。

#### 函数

名称typedef关键字描述[typedef void (*OH_PreviewOutput_OnFrameStart)(Camera_PreviewOutput* previewOutput)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_onframestart)OH_PreviewOutput_OnFrameStart在[PreviewOutput_Callbacks](../../topics/misc/PreviewOutput_Callbacks.md)中被调用的预览输出帧开始回调。[typedef void (*OH_PreviewOutput_OnFrameEnd)(Camera_PreviewOutput* previewOutput, int32_t frameCount)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_onframeend)OH_PreviewOutput_OnFrameEnd在[PreviewOutput_Callbacks](../../topics/misc/PreviewOutput_Callbacks.md)中被调用的预览输出帧结束回调。[typedef void (*OH_PreviewOutput_OnError)(Camera_PreviewOutput* previewOutput, Camera_ErrorCode errorCode)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_onerror)OH_PreviewOutput_OnError在[PreviewOutput_Callbacks](../../topics/misc/PreviewOutput_Callbacks.md)中被调用的预览输出帧错误回调。[Camera_ErrorCode OH_PreviewOutput_RegisterCallback(Camera_PreviewOutput* previewOutput, PreviewOutput_Callbacks* callback)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_registercallback)-注册预览输出更改事件回调。[Camera_ErrorCode OH_PreviewOutput_UnregisterCallback(Camera_PreviewOutput* previewOutput, PreviewOutput_Callbacks* callback)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_unregistercallback)-注销预览输出更改事件回调。[Camera_ErrorCode OH_PreviewOutput_Start(Camera_PreviewOutput* previewOutput)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_start)-开始预览输出。[Camera_ErrorCode OH_PreviewOutput_Stop(Camera_PreviewOutput* previewOutput)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_stop)-停止预览输出。[Camera_ErrorCode OH_PreviewOutput_Release(Camera_PreviewOutput* previewOutput)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_release)-释放预览输出实例。[Camera_ErrorCode OH_PreviewOutput_GetActiveProfile(Camera_PreviewOutput* previewOutput, Camera_Profile** profile)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_getactiveprofile)-获取当前预览输出配置文件。[Camera_ErrorCode OH_PreviewOutput_DeleteProfile(Camera_Profile* profile)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_deleteprofile)-删除预览配置文件实例。[Camera_ErrorCode OH_PreviewOutput_GetPreviewRotation(Camera_PreviewOutput* previewOutput, int displayRotation, Camera_ImageRotation* imageRotation)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_getpreviewrotation)-获取相机预览旋转角度。[Camera_ErrorCode OH_PreviewOutput_SetPreviewRotation(Camera_PreviewOutput* previewOutput, Camera_ImageRotation previewRotation, bool isDisplayLocked)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_setpreviewrotation)-设置相机预览旋转角度。[Camera_ErrorCode OH_PreviewOutput_GetSupportedFrameRates(Camera_PreviewOutput* previewOutput, Camera_FrameRateRange** frameRateRange, uint32_t* size)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_getsupportedframerates)-获取支持的预览输出帧率列表。[Camera_ErrorCode OH_PreviewOutput_DeleteFrameRates(Camera_PreviewOutput* previewOutput, Camera_FrameRateRange* frameRateRange)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_deleteframerates)-删除帧率列表。[Camera_ErrorCode OH_PreviewOutput_SetFrameRate(Camera_PreviewOutput* previewOutput, int32_t minFps, int32_t maxFps)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_setframerate)-设置预览输出帧率。[Camera_ErrorCode OH_PreviewOutput_GetActiveFrameRate(Camera_PreviewOutput* previewOutput, Camera_FrameRateRange* frameRateRange)](#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_getactiveframerate)-获取当前预览输出帧率。

#### 函数说明

#### OH_PreviewOutput_OnFrameStart()

```ets
typedef void (*OH_PreviewOutput_OnFrameStart)(Camera_PreviewOutput* previewOutput)
```

**描述**

在[PreviewOutput_Callbacks](../../topics/misc/PreviewOutput_Callbacks.md)中被调用的预览输出帧开始回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput传递回调的预览输出实例。

#### OH_PreviewOutput_OnFrameEnd()

```ets
typedef void (*OH_PreviewOutput_OnFrameEnd)(Camera_PreviewOutput* previewOutput, int32_t frameCount)
```

**描述**

在[PreviewOutput_Callbacks](../../topics/misc/PreviewOutput_Callbacks.md)中被调用的预览输出帧结束回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput传递回调的预览输出实例。int32_t frameCount回调传递的帧计数。

#### OH_PreviewOutput_OnError()

```ets
typedef void (*OH_PreviewOutput_OnError)(Camera_PreviewOutput* previewOutput, Camera_ErrorCode errorCode)
```

**描述**

在[PreviewOutput_Callbacks](../../topics/misc/PreviewOutput_Callbacks.md)中被调用的预览输出帧错误回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput传递回调的预览输出实例。[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode) errorCode预览输出的错误码。

**参考：**

[CAMERA_SERVICE_FATAL_ERROR](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

#### OH_PreviewOutput_RegisterCallback()

```ets
Camera_ErrorCode OH_PreviewOutput_RegisterCallback(Camera_PreviewOutput* previewOutput,PreviewOutput_Callbacks* callback)
```

**描述**

注册预览输出更改事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput预览输出实例。[PreviewOutput_Callbacks](../../topics/misc/PreviewOutput_Callbacks.md)* callback要注册的预览输出更改事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PreviewOutput_UnregisterCallback()

```ets
Camera_ErrorCode OH_PreviewOutput_UnregisterCallback(Camera_PreviewOutput* previewOutput,PreviewOutput_Callbacks* callback)
```

**描述**

注销预览输出更改事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput预览输出实例。[PreviewOutput_Callbacks](../../topics/misc/PreviewOutput_Callbacks.md)* callback要注销的预览输出更改事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PreviewOutput_Start()

```ets
Camera_ErrorCode OH_PreviewOutput_Start(Camera_PreviewOutput* previewOutput)
```

**描述**

开始预览输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput要启动的预览输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PreviewOutput_Stop()

```ets
Camera_ErrorCode OH_PreviewOutput_Stop(Camera_PreviewOutput* previewOutput)
```

**描述**

停止预览输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput要停止的预览输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PreviewOutput_Release()

```ets
Camera_ErrorCode OH_PreviewOutput_Release(Camera_PreviewOutput* previewOutput)
```

**描述**

释放预览输出实例。

**起始版本：** 11

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput要释放的预览输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PreviewOutput_GetActiveProfile()

```ets
Camera_ErrorCode OH_PreviewOutput_GetActiveProfile(Camera_PreviewOutput* previewOutput, Camera_Profile** profile)
```

**描述**

获取当前预览输出配置文件。

**起始版本：** 12

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput提供当前预览输出配置文件的预览输出实例。[Camera_Profile](../../topics/media/Camera_Profile.md)** profile如果方法调用成功，将记录当前的预览输出配置文件。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PreviewOutput_DeleteProfile()

```ets
Camera_ErrorCode OH_PreviewOutput_DeleteProfile(Camera_Profile* profile)
```

**描述**

删除预览配置文件实例。

**起始版本：** 12

**参数：**

参数项描述[Camera_Profile](../../topics/media/Camera_Profile.md)* profile要被删除的预览配置文件实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PreviewOutput_GetPreviewRotation()

```ets
Camera_ErrorCode OH_PreviewOutput_GetPreviewRotation(Camera_PreviewOutput* previewOutput, int displayRotation,Camera_ImageRotation* imageRotation)
```

**描述**

获取相机预览旋转角度。

**起始版本：** 12

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput用于获取预览旋转角度的预览输出实例。int displayRotation当前显示的旋转角度。[Camera_ImageRotation](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_imagerotation)* imageRotation预览旋转角度结果。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PreviewOutput_SetPreviewRotation()

```ets
Camera_ErrorCode OH_PreviewOutput_SetPreviewRotation(Camera_PreviewOutput* previewOutput,Camera_ImageRotation previewRotation, bool isDisplayLocked)
```

**描述**

设置相机预览旋转角度。

**起始版本：** 12

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput用于设置预览旋转角度的预览输出实例。[Camera_ImageRotation](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_imagerotation) previewRotation预览的显示旋转角度。bool isDisplayLockedSurface在屏幕旋转时是否锁定方向，未设置时默认取值为false，即不锁定方向。true表示锁定方向，false表示不锁定方向。详情请参考[SurfaceRotationOptions](../../topics/components/XComponent.md#ZH-CN_TOPIC_0000002529444889__surfacerotationoptions12对象说明)

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PreviewOutput_GetSupportedFrameRates()

```ets
Camera_ErrorCode OH_PreviewOutput_GetSupportedFrameRates(Camera_PreviewOutput* previewOutput,Camera_FrameRateRange** frameRateRange, uint32_t* size)
```

**描述**

获取支持的预览输出帧率列表。

**起始版本：** 12

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput传递支持的帧率列表的预览输出实例。[Camera_FrameRateRange](../../topics/components/Camera_FrameRateRange.md)** frameRateRange如果方法调用成功，将记录支持的预览输出帧率列表。uint32_t* size如果方法调用成功，将记录支持的预览输出帧率列表大小。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PreviewOutput_DeleteFrameRates()

```ets
Camera_ErrorCode OH_PreviewOutput_DeleteFrameRates(Camera_PreviewOutput* previewOutput,Camera_FrameRateRange* frameRateRange)
```

**描述**

删除帧率列表。

**起始版本：** 12

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput预览输出实例。[Camera_FrameRateRange](../../topics/components/Camera_FrameRateRange.md)* frameRateRange要删除的帧率列表。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PreviewOutput_SetFrameRate()

```ets
Camera_ErrorCode OH_PreviewOutput_SetFrameRate(Camera_PreviewOutput* previewOutput,int32_t minFps, int32_t maxFps)
```

**描述**

设置预览输出帧率。

**起始版本：** 12

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput要设置帧率的预览输出实例。int32_t minFps要设置的最小值。int32_t maxFps要设置的最大值。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PreviewOutput_GetActiveFrameRate()

```ets
Camera_ErrorCode OH_PreviewOutput_GetActiveFrameRate(Camera_PreviewOutput* previewOutput,Camera_FrameRateRange* frameRateRange)
```

**描述**

获取当前预览输出帧率。

**起始版本：** 12

**参数：**

参数项描述[Camera_PreviewOutput](../../topics/media/Camera_PreviewOutput.md)* previewOutput传递当前预览输出帧率的预览输出实例。[Camera_FrameRateRange](../../topics/components/Camera_FrameRateRange.md)* frameRateRange如果方法调用成功，则将记录当前的[Camera_FrameRateRange](../../topics/components/Camera_FrameRateRange.md)。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。