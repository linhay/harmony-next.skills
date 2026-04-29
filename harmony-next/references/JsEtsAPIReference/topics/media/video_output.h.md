# video_output.h

**概述**

声明录像输出概念。

引用文件： <ohcamera/video_output.h>

库： libohcamera.so

系统能力： SystemCapability.Multimedia.Camera.Core

起始版本： 11

相关模块： [OH_Camera](OH_Camera.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| VideoOutput_Callbacks | VideoOutput_Callbacks | 用于录像输出的回调。 |
| Camera_VideoOutput | Camera_VideoOutput | 录像输出对象。  可以使用OH_CameraManager_CreateVideoOutput方法创建指针。 |

**函数**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| typedef void (*OH_VideoOutput_OnFrameStart)(Camera_VideoOutput* videoOutput) | OH_VideoOutput_OnFrameStart | 在VideoOutput_Callbacks中被调用的录像输出帧开始回调。 |
| typedef void (*OH_VideoOutput_OnFrameEnd)(Camera_VideoOutput* videoOutput, int32_t frameCount) | OH_VideoOutput_OnFrameEnd | 在VideoOutput_Callbacks中被调用的录像输出帧结束回调。 |
| typedef void (*OH_VideoOutput_OnError)(Camera_VideoOutput* videoOutput, Camera_ErrorCode errorCode) | OH_VideoOutput_OnError | 在VideoOutput_Callbacks中被调用的录像输出错误回调。 |
| Camera_ErrorCode OH_VideoOutput_RegisterCallback(Camera_VideoOutput* videoOutput, VideoOutput_Callbacks* callback) | - | 注册录像输出更改事件回调。 |
| Camera_ErrorCode OH_VideoOutput_UnregisterCallback(Camera_VideoOutput* videoOutput, VideoOutput_Callbacks* callback) | - | 注销录像输出更改事件回调。 |
| Camera_ErrorCode OH_VideoOutput_Start(Camera_VideoOutput* videoOutput) | - | 开始录像输出。 |
| Camera_ErrorCode OH_VideoOutput_Stop(Camera_VideoOutput* videoOutput) | - | 停止录像输出。 |
| Camera_ErrorCode OH_VideoOutput_Release(Camera_VideoOutput* videoOutput) | - | 释放录像输出实例。 |
| Camera_ErrorCode OH_VideoOutput_GetActiveProfile(Camera_VideoOutput* videoOutput, Camera_VideoProfile** profile) | - | 获取当前视频输出配置文件。 |
| Camera_ErrorCode OH_VideoOutput_DeleteProfile(Camera_VideoProfile* profile) | - | 删除视频配置文件实例。 |
| Camera_ErrorCode OH_VideoOutput_IsMirrorSupported(Camera_VideoOutput* videoOutput, bool* isSupported) | - | 判断当前视频输出是否支持镜像。 |
| Camera_ErrorCode OH_VideoOutput_EnableMirror(Camera_VideoOutput* videoOutput, bool mirrorMode) | - | 打开/关闭当前视频输出镜像功能。 |
| Camera_ErrorCode OH_VideoOutput_GetVideoRotation(Camera_VideoOutput* videoOutput, int deviceDegree, Camera_ImageRotation* imageRotation) | - | 获取录像旋转角度。 |
| Camera_ErrorCode OH_VideoOutput_GetVideoRotationWithoutDeviceDegree(Camera_VideoOutput* videoOutput, Camera_ImageRotation* imageRotation) | - | 获取录像旋转角度。 |
| Camera_ErrorCode OH_VideoOutput_GetSupportedFrameRates(Camera_VideoOutput* videoOutput, Camera_FrameRateRange** frameRateRange, uint32_t* size) | - | 获取支持的视频输出帧率列表。 |
| Camera_ErrorCode OH_VideoOutput_DeleteFrameRates(Camera_VideoOutput* videoOutput, Camera_FrameRateRange* frameRateRange) | - | 删除帧率列表。 |
| Camera_ErrorCode OH_VideoOutput_SetFrameRate(Camera_VideoOutput* videoOutput, int32_t minFps, int32_t maxFps) | - | 设置视频输出帧率。 |
| Camera_ErrorCode OH_VideoOutput_GetActiveFrameRate(Camera_VideoOutput* videoOutput, Camera_FrameRateRange* frameRateRange) | - | 获取当前视频输出帧率。 |

**函数说明**

**OH_VideoOutput_OnFrameStart()**

```ets
typedef void (*OH_VideoOutput_OnFrameStart)(Camera_VideoOutput* videoOutput)
```

描述

在[VideoOutput_Callbacks](VideoOutput_Callbacks.md)中被调用的录像输出帧开始回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 传递回调的录像输出实例。 |

**OH_VideoOutput_OnFrameEnd()**

```ets
typedef void (*OH_VideoOutput_OnFrameEnd)(Camera_VideoOutput* videoOutput, int32_t frameCount)
```

描述

在[VideoOutput_Callbacks](VideoOutput_Callbacks.md)中被调用的录像输出帧结束回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 传递回调的录像输出实例。 |
| int32_t frameCount | 回调传递的帧计数。 |

**OH_VideoOutput_OnError()**

```ets
typedef void (*OH_VideoOutput_OnError)(Camera_VideoOutput* videoOutput, Camera_ErrorCode errorCode)
```

描述

在[VideoOutput_Callbacks](VideoOutput_Callbacks.md)中被调用的录像输出错误回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 传递回调的录像输出实例。 |
| Camera_ErrorCode errorCode | 录像输出的错误码。 |

参考：

[CAMERA_SERVICE_FATAL_ERROR](camera.h.md#ZH-CN_TOPIC_0000002553361845__camera_errorcode)

**OH_VideoOutput_RegisterCallback()**

```ets
Camera_ErrorCode OH_VideoOutput_RegisterCallback(Camera_VideoOutput* videoOutput, VideoOutput_Callbacks* callback)
```

描述

注册录像输出更改事件回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 录像输出实例。 |
| VideoOutput_Callbacks* callback | 要注册的录像输出更改事件回调。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_VideoOutput_UnregisterCallback()**

```ets
Camera_ErrorCode OH_VideoOutput_UnregisterCallback(Camera_VideoOutput* videoOutput, VideoOutput_Callbacks* callback)
```

描述

注销录像输出更改事件回调。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 录像输出实例。 |
| VideoOutput_Callbacks* callback | 要注销的录像输出更改事件回调。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_VideoOutput_Start()**

```ets
Camera_ErrorCode OH_VideoOutput_Start(Camera_VideoOutput* videoOutput)
```

描述

开始录像输出。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 要启动的录像输出实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_VideoOutput_Stop()**

```ets
Camera_ErrorCode OH_VideoOutput_Stop(Camera_VideoOutput* videoOutput)
```

描述

停止录像输出。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 要停止的录像输出实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_VideoOutput_Release()**

```ets
Camera_ErrorCode OH_VideoOutput_Release(Camera_VideoOutput* videoOutput)
```

描述

释放录像输出实例。

起始版本： 11

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 要释放的录像输出实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_VideoOutput_GetActiveProfile()**

```ets
Camera_ErrorCode OH_VideoOutput_GetActiveProfile(Camera_VideoOutput* videoOutput, Camera_VideoProfile** profile)
```

描述

获取当前视频输出配置文件。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 传递当前视频输出配置文件的录像输出实例。 |
| Camera_VideoProfile** profile | 如果方法调用成功，将记录当前的视频输出配置文件。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_VideoOutput_DeleteProfile()**

```ets
Camera_ErrorCode OH_VideoOutput_DeleteProfile(Camera_VideoProfile* profile)
```

描述

删除视频配置文件实例。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoProfile* profile | 要删除的视频配置文件实例。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_VideoOutput_IsMirrorSupported()**

```ets
 Camera_ErrorCode OH_VideoOutput_IsMirrorSupported(Camera_VideoOutput* videoOutput, bool* isSupported)
```

描述

判断当前视频输出是否支持镜像。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 传递当前视频输出的录像输出实例。 |
| bool* isSupported | 当前视频输出是否支持镜像。true表示当前视频输出支持镜像，false表示不支持。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_VideoOutput_EnableMirror()**

```ets
 Camera_ErrorCode OH_VideoOutput_EnableMirror(Camera_VideoOutput* videoOutput, bool mirrorMode)
```

描述

打开/关闭当前视频输出镜像功能。

起始版本： 15

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 传递当前视频输出的录像输出实例。 |
| bool mirrorMode | 设备是否开启镜像功能。true表示打开镜像功能，false表示关闭镜像功能。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_VideoOutput_GetVideoRotation()**

```ets
 Camera_ErrorCode OH_VideoOutput_GetVideoRotation(Camera_VideoOutput* videoOutput, int deviceDegree, Camera_ImageRotation* imageRotation)
```

描述

获取录像旋转角度。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 传递当前视频输出的录像输出实例。 |
| int deviceDegree | 设备目前相对于自然方向（充电口朝下）顺时针的旋转角度。 |
| Camera_ImageRotation* imageRotation | 录像旋转角度的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_VideoOutput_GetVideoRotationWithoutDeviceDegree()**

```ets
Camera_ErrorCode OH_VideoOutput_GetVideoRotationWithoutDeviceDegree(Camera_VideoOutput* videoOutput, Camera_ImageRotation* imageRotation)
```

描述

获取录像旋转角度。

起始版本： 23

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 传递当前视频输出的录像输出实例。 |
| Camera_ImageRotation* imageRotation | 录像旋转角度的结果。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_VideoOutput_GetSupportedFrameRates()**

```ets
Camera_ErrorCode OH_VideoOutput_GetSupportedFrameRates(Camera_VideoOutput* videoOutput, Camera_FrameRateRange** frameRateRange, uint32_t* size)
```

描述

获取支持的视频输出帧率列表。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 传递支持的视频输出帧率列表的录像输出实例。 |
| Camera_FrameRateRange** frameRateRange | 如果方法调用成功，将记录支持的视频输出帧率列表。 |
| uint32_t* size | 如果方法调用成功，将记录支持的视频输出帧率列表大小。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |

**OH_VideoOutput_DeleteFrameRates()**

```ets
Camera_ErrorCode OH_VideoOutput_DeleteFrameRates(Camera_VideoOutput* videoOutput, Camera_FrameRateRange* frameRateRange)
```

描述

删除帧率列表。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 录像输出实例。 |
| Camera_FrameRateRange* frameRateRange | 要删除的帧率列表。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_VideoOutput_SetFrameRate()**

```ets
Camera_ErrorCode OH_VideoOutput_SetFrameRate(Camera_VideoOutput* videoOutput, int32_t minFps, int32_t maxFps)
```

描述

设置视频输出帧率。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 要设置帧率的录像输出实例。 |
| int32_t minFps | 设置的最小帧率。 |
| int32_t maxFps | 设置的最大帧率。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。 |

**OH_VideoOutput_GetActiveFrameRate()**

```ets
Camera_ErrorCode OH_VideoOutput_GetActiveFrameRate(Camera_VideoOutput* videoOutput, Camera_FrameRateRange* frameRateRange)
```

描述

获取当前视频输出帧率。

起始版本： 12

参数：

| 参数项 | 描述 |
| --- | --- |
| Camera_VideoOutput* videoOutput | 传递当前视频输出帧率的录像输出实例。 |
| Camera_FrameRateRange* frameRateRange | 如果方法调用成功，将记录当前的视频输出帧率。 |

返回：

| 类型 | 说明 |
| --- | --- |
| Camera_ErrorCode | CAMERA_OK：方法调用成功。  CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。  CAMERA_SERVICE_FATAL_ERROR：相机服务异常。 |