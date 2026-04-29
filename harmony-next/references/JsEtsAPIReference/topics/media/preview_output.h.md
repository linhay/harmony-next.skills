# preview_output.h

**概述**

声明预览输出概念。

引用文件： <ohcamera/preview_output.h>

库： libohcamera.so

系统能力： SystemCapability.Multimedia.Camera.Core

起始版本： 11

相关模块： [OH_Camera](OH_Camera.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| PreviewOutput_Callbacks | PreviewOutput_Callbacks | 用于预览输出的回调。 |
| Camera_PreviewOutput | Camera_PreviewOutput | 预览输出对象。  可以使用OH_CameraManager_CreatePreviewOutput方法创建指针。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_PreviewOutput_OnFrameStart)(Camera_PreviewOutput* previewOutput) | OH_PreviewOutput_OnFrameStart | 在PreviewOutput_Callbacks中被调用的预览输出帧开始回调。 |
| typedef void (*OH_PreviewOutput_OnFrameEnd)(Camera_PreviewOutput* previewOutput, int32_t frameCount) | OH_PreviewOutput_OnFrameEnd | 在PreviewOutput_Callbacks中被调用的预览输出帧结束回调。 |
| typedef void (*OH_PreviewOutput_OnError)(Camera_PreviewOutput* previewOutput, Camera_ErrorCode errorCode) | OH_PreviewOutput_OnError | 在PreviewOutput_Callbacks中被调用的预览输出帧错误回调。 |
| Camera_ErrorCode OH_PreviewOutput_RegisterCallback(Camera_PreviewOutput* previewOutput, PreviewOutput_Callbacks* callback) | - | 注册预览输出更改事件回调。 |
| Camera_ErrorCode OH_PreviewOutput_UnregisterCallback(Camera_PreviewOutput* previewOutput, PreviewOutput_Callbacks* callback) | - | 注销预览输出更改事件回调。 |
| Camera_ErrorCode OH_PreviewOutput_Start(Camera_PreviewOutput* previewOutput) | - | 开始预览输出。 |
| Camera_ErrorCode OH_PreviewOutput_Stop(Camera_PreviewOutput* previewOutput) | - | 停止预览输出。 |
| Camera_ErrorCode OH_PreviewOutput_Release(Camera_PreviewOutput* previewOutput) | - | 释放预览输出实例。 |
| Camera_ErrorCode OH_PreviewOutput_GetActiveProfile(Camera_PreviewOutput* previewOutput, Camera_Profile** profile) | - | 获取当前预览输出配置文件。 |
| Camera_ErrorCode OH_PreviewOutput_DeleteProfile(Camera_Profile* profile) | - | 删除预览配置文件实例。 |
| Camera_ErrorCode OH_PreviewOutput_GetPreviewRotation(Camera_PreviewOutput* previewOutput, int displayRotation, Camera_ImageRotation* imageRotation) | - | 获取相机预览旋转角度。 |
| Camera_ErrorCode OH_PreviewOutput_GetPreviewRotationWithoutDisplayRotation(Camera_PreviewOutput* previewOutput, Camera_ImageRotation* imageRotation) | - | 获取相机预览旋转角度。 |
| Camera_ErrorCode OH_PreviewOutput_SetPreviewRotation(Camera_PreviewOutput* previewOutput, Camera_ImageRotation previewRotation, bool isDisplayLocked) | - | 设置相机预览旋转角度。 |
| Camera_ErrorCode OH_PreviewOutput_GetSupportedFrameRates(Camera_PreviewOutput* previewOutput, Camera_FrameRateRange** frameRateRange, uint32_t* size) | - | 获取支持的预览输出帧率列表。 |
| Camera_ErrorCode OH_PreviewOutput_DeleteFrameRates(Camera_PreviewOutput* previewOutput, Camera_FrameRateRange* frameRateRange) | - | 删除帧率列表。 |
| Camera_ErrorCode OH_PreviewOutput_SetFrameRate(Camera_PreviewOutput* previewOutput, int32_t minFps, int32_t maxFps) | - | 设置预览输出帧率。 |
| Camera_ErrorCode OH_PreviewOutput_GetActiveFrameRate(Camera_PreviewOutput* previewOutput, Camera_FrameRateRange* frameRateRange) | - | 获取当前预览输出帧率。 |
| Camera_ErrorCode OH_PreviewOutput_IsBandwidthCompressionSupported(Camera_PreviewOutput* previewOutput, bool* isSupported) | - | 检查是否支持预览带宽压缩（指通过编码减少数据量，降低其在传输链路中的带宽占用）。 |
| Camera_ErrorCode OH_PreviewOutput_EnableBandwidthCompression(Camera_PreviewOutput* previewOutput, bool enabled) | - | 使能预览带宽压缩。 该接口只能在使用OH_CaptureSession_CommitConfig()接口之前调用，否则会影响预览流出流格式。 |

**函数说明**

**OH_PreviewOutput_OnFrameStart()**

```ets
typedef void (*OH_PreviewOutput_OnFrameStart)(Camera_PreviewOutput* previewOutput)
```

描述

在[PreviewOutput_Callbacks](PreviewOutput_Callbacks.md)中被调用的预览输出帧开始回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 传递回调的预览输出实例。 |

**OH_PreviewOutput_OnFrameEnd()**

```ets
typedef void (*OH_PreviewOutput_OnFrameEnd)(Camera_PreviewOutput* previewOutput, int32_t frameCount)
```

描述

在[PreviewOutput_Callbacks](PreviewOutput_Callbacks.md)中被调用的预览输出帧结束回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 传递回调的预览输出实例。 |
| int32_t frameCount | 回调传递的帧计数。 |

**OH_PreviewOutput_OnError()**

```ets
typedef void (*OH_PreviewOutput_OnError)(Camera_PreviewOutput* previewOutput, Camera_ErrorCode errorCode)
```

描述

在[PreviewOutput_Callbacks](PreviewOutput_Callbacks.md)中被调用的预览输出帧错误回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 传递回调的预览输出实例。 |
| Camera_ErrorCode errorCode | 预览输出的错误码。 |

参考：

[CAMERA_SERVICE_FATAL_ERROR](camera.h.md#ZH-CN_TOPIC_0000002553361845__camera_errorcode)

**OH_PreviewOutput_RegisterCallback()**

```ets
Camera_ErrorCode OH_PreviewOutput_RegisterCallback(Camera_PreviewOutput* previewOutput, PreviewOutput_Callbacks* callback)
```

描述

注册预览输出更改事件回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 预览输出实例。 |
| PreviewOutput_Callbacks* callback | 要注册的预览输出更改事件回调。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_PreviewOutput_UnregisterCallback()**

```ets
Camera_ErrorCode OH_PreviewOutput_UnregisterCallback(Camera_PreviewOutput* previewOutput, PreviewOutput_Callbacks* callback)
```

描述

注销预览输出更改事件回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 预览输出实例。 |
| PreviewOutput_Callbacks* callback | 要注销的预览输出更改事件回调。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_PreviewOutput_Start()**

```ets
Camera_ErrorCode OH_PreviewOutput_Start(Camera_PreviewOutput* previewOutput)
```

描述

开始预览输出。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 要启动的预览输出实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_PreviewOutput_Stop()**

```ets
Camera_ErrorCode OH_PreviewOutput_Stop(Camera_PreviewOutput* previewOutput)
```

描述

停止预览输出。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 要停止的预览输出实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_PreviewOutput_Release()**

```ets
Camera_ErrorCode OH_PreviewOutput_Release(Camera_PreviewOutput* previewOutput)
```

描述

释放预览输出实例。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 要释放的预览输出实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_PreviewOutput_GetActiveProfile()**

```ets
Camera_ErrorCode OH_PreviewOutput_GetActiveProfile(Camera_PreviewOutput* previewOutput, Camera_Profile** profile)
```

描述

获取当前预览输出配置文件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 提供当前预览输出配置文件的预览输出实例。 |
| Camera_Profile** profile | 如果方法调用成功，将记录当前的预览输出配置文件。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_PreviewOutput_DeleteProfile()**

```ets
Camera_ErrorCode OH_PreviewOutput_DeleteProfile(Camera_Profile* profile)
```

描述

删除预览配置文件实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_Profile* profile | 要被删除的预览配置文件实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_PreviewOutput_GetPreviewRotation()**

```ets
Camera_ErrorCode OH_PreviewOutput_GetPreviewRotation(Camera_PreviewOutput* previewOutput, int displayRotation, Camera_ImageRotation* imageRotation)
```

描述

获取相机预览旋转角度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 用于获取预览旋转角度的预览输出实例。 |
| int displayRotation | 当前显示的旋转角度。 |
| Camera_ImageRotation* imageRotation | 预览旋转角度结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_PreviewOutput_GetPreviewRotationWithoutDisplayRotation()**

```ets
Camera_ErrorCode OH_PreviewOutput_GetPreviewRotationWithoutDisplayRotation(Camera_PreviewOutput* previewOutput, Camera_ImageRotation* imageRotation)
```

描述

获取相机预览旋转角度。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 用于获取预览旋转角度的预览输出实例。 |
| Camera_ImageRotation* imageRotation | 预览旋转角度结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_PreviewOutput_SetPreviewRotation()**

```ets
Camera_ErrorCode OH_PreviewOutput_SetPreviewRotation(Camera_PreviewOutput* previewOutput, Camera_ImageRotation previewRotation, bool isDisplayLocked)
```

描述

设置相机预览旋转角度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 用于设置预览旋转角度的预览输出实例。 |
| Camera_ImageRotation previewRotation | 预览的显示旋转角度。 |
| bool isDisplayLocked | Surface在屏幕旋转时是否锁定方向，未设置时默认取值为false，即不锁定方向。true表示锁定方向，false表示不锁定方向。详情请参考SurfaceRotationOptions。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_PreviewOutput_GetSupportedFrameRates()**

```ets
Camera_ErrorCode OH_PreviewOutput_GetSupportedFrameRates(Camera_PreviewOutput* previewOutput, Camera_FrameRateRange** frameRateRange, uint32_t* size)
```

描述

获取支持的预览输出帧率列表。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 传递支持的帧率列表的预览输出实例。 |
| Camera_FrameRateRange** frameRateRange | 如果方法调用成功，将记录支持的预览输出帧率列表。 |
| uint32_t* size | 如果方法调用成功，将记录支持的预览输出帧率列表大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_PreviewOutput_DeleteFrameRates()**

```ets
Camera_ErrorCode OH_PreviewOutput_DeleteFrameRates(Camera_PreviewOutput* previewOutput, Camera_FrameRateRange* frameRateRange)
```

描述

删除帧率列表。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 预览输出实例。 |
| Camera_FrameRateRange* frameRateRange | 要删除的帧率列表。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_PreviewOutput_SetFrameRate()**

```ets
Camera_ErrorCode OH_PreviewOutput_SetFrameRate(Camera_PreviewOutput* previewOutput, int32_t minFps, int32_t maxFps)
```

描述

设置预览输出帧率。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 要设置帧率的预览输出实例。 |
| int32_t minFps | 要设置的最小值。 |
| int32_t maxFps | 要设置的最大值。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_PreviewOutput_GetActiveFrameRate()**

```ets
Camera_ErrorCode OH_PreviewOutput_GetActiveFrameRate(Camera_PreviewOutput* previewOutput, Camera_FrameRateRange* frameRateRange)
```

描述

获取当前预览输出帧率。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 传递当前预览输出帧率的预览输出实例。 |
| Camera_FrameRateRange* frameRateRange | 如果方法调用成功，则将记录当前的Camera_FrameRateRange。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_PreviewOutput_IsBandwidthCompressionSupported()**

```ets
Camera_ErrorCode OH_PreviewOutput_IsBandwidthCompressionSupported(Camera_PreviewOutput* previewOutput, bool* isSupported)
```

描述

检查是否支持预览带宽压缩（指通过编码减少数据量，降低其在传输链路中的带宽占用）。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 预览输出实例。 |
| bool* isSupported | 是否支持带宽压缩的结果。true表示支持，false表示不支持。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_PreviewOutput_EnableBandwidthCompression()**

```ets
Camera_ErrorCode OH_PreviewOutput_EnableBandwidthCompression(Camera_PreviewOutput* previewOutput, bool enabled)
```

描述

使能预览带宽压缩。

 该接口只能在使用[OH_CaptureSession_CommitConfig()](capture_session.h.md#ZH-CN_TOPIC_0000002553361847__oh_capturesession_commitconfig)接口之前调用，否则会影响预览流出流格式。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_PreviewOutput* previewOutput | 传递当前要预览带宽压缩使能的预览输出实例。 |
| bool enabled | 是否使能预览带宽压缩。true表示使能，false表示不使能。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_OPERATION_NOT_ALLOWED: 操作不允许。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SESSION_NOT_CONFIG：相机会话未配置。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |