# video_output.h

#### 概述

声明录像输出概念。

**引用文件：** <ohcamera/video_output.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：**[OH_Camera](../../topics/media/OH_Camera.md)

#### 汇总

#### 结构体

名称typedef关键字描述[VideoOutput_Callbacks](../../topics/media/VideoOutput_Callbacks.md)VideoOutput_Callbacks用于录像输出的回调。[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)Camera_VideoOutput

录像输出对象。

 可以使用[OH_CameraManager_CreateVideoOutput](camera_manager.h.md#ZH-CN_TOPIC_0000002529445763__oh_cameramanager_createvideooutput)方法创建指针。

#### 函数

名称typedef关键字描述[typedef void (*OH_VideoOutput_OnFrameStart)(Camera_VideoOutput* videoOutput)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_onframestart)OH_VideoOutput_OnFrameStart在[VideoOutput_Callbacks](../../topics/media/VideoOutput_Callbacks.md)中被调用的录像输出帧开始回调。[typedef void (*OH_VideoOutput_OnFrameEnd)(Camera_VideoOutput* videoOutput, int32_t frameCount)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_onframeend)OH_VideoOutput_OnFrameEnd在[VideoOutput_Callbacks](../../topics/media/VideoOutput_Callbacks.md)中被调用的录像输出帧结束回调。[typedef void (*OH_VideoOutput_OnError)(Camera_VideoOutput* videoOutput, Camera_ErrorCode errorCode)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_onerror)OH_VideoOutput_OnError在[VideoOutput_Callbacks](../../topics/media/VideoOutput_Callbacks.md)中被调用的录像输出错误回调。[Camera_ErrorCode OH_VideoOutput_RegisterCallback(Camera_VideoOutput* videoOutput, VideoOutput_Callbacks* callback)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_registercallback)-注册录像输出更改事件回调。[Camera_ErrorCode OH_VideoOutput_UnregisterCallback(Camera_VideoOutput* videoOutput, VideoOutput_Callbacks* callback)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_unregistercallback)-注销录像输出更改事件回调。[Camera_ErrorCode OH_VideoOutput_Start(Camera_VideoOutput* videoOutput)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_start)-开始录像输出。[Camera_ErrorCode OH_VideoOutput_Stop(Camera_VideoOutput* videoOutput)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_stop)-停止录像输出。[Camera_ErrorCode OH_VideoOutput_Release(Camera_VideoOutput* videoOutput)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_release)-释放录像输出实例。[Camera_ErrorCode OH_VideoOutput_GetActiveProfile(Camera_VideoOutput* videoOutput, Camera_VideoProfile** profile)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_getactiveprofile)-获取当前视频输出配置文件。[Camera_ErrorCode OH_VideoOutput_DeleteProfile(Camera_VideoProfile* profile)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_deleteprofile)-删除视频配置文件实例。[ Camera_ErrorCode OH_VideoOutput_IsMirrorSupported(Camera_VideoOutput* videoOutput, bool* isSupported)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_ismirrorsupported)-判断当前视频输出是否支持镜像。[ Camera_ErrorCode OH_VideoOutput_EnableMirror(Camera_VideoOutput* videoOutput, bool mirrorMode)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_enablemirror)-打开/关闭当前视频输出镜像功能。[ Camera_ErrorCode OH_VideoOutput_GetVideoRotation(Camera_VideoOutput* videoOutput, int deviceDegree, Camera_ImageRotation* imageRotation)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_getvideorotation)-获取当前视频输出应当设置的旋转角度。[Camera_ErrorCode OH_VideoOutput_GetSupportedFrameRates(Camera_VideoOutput* videoOutput, Camera_FrameRateRange** frameRateRange, uint32_t* size)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_getsupportedframerates)-获取支持的视频输出帧率列表。[Camera_ErrorCode OH_VideoOutput_DeleteFrameRates(Camera_VideoOutput* videoOutput, Camera_FrameRateRange* frameRateRange)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_deleteframerates)-删除帧率列表。[Camera_ErrorCode OH_VideoOutput_SetFrameRate(Camera_VideoOutput* videoOutput,int32_t minFps, int32_t maxFps)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_setframerate)-设置视频输出帧率。[Camera_ErrorCode OH_VideoOutput_GetActiveFrameRate(Camera_VideoOutput* videoOutput, Camera_FrameRateRange* frameRateRange)](#ZH-CN_TOPIC_0000002497445822__oh_videooutput_getactiveframerate)-获取当前视频输出帧率。

#### 函数说明

#### OH_VideoOutput_OnFrameStart()

```ets
typedef void (*OH_VideoOutput_OnFrameStart)(Camera_VideoOutput* videoOutput)
```

**描述**

在[VideoOutput_Callbacks](../../topics/media/VideoOutput_Callbacks.md)中被调用的录像输出帧开始回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput传递回调的录像输出实例。

#### OH_VideoOutput_OnFrameEnd()

```ets
typedef void (*OH_VideoOutput_OnFrameEnd)(Camera_VideoOutput* videoOutput, int32_t frameCount)
```

**描述**

在[VideoOutput_Callbacks](../../topics/media/VideoOutput_Callbacks.md)中被调用的录像输出帧结束回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput传递回调的录像输出实例。int32_t frameCount回调传递的帧计数。

#### OH_VideoOutput_OnError()

```ets
typedef void (*OH_VideoOutput_OnError)(Camera_VideoOutput* videoOutput, Camera_ErrorCode errorCode)
```

**描述**

在[VideoOutput_Callbacks](../../topics/media/VideoOutput_Callbacks.md)中被调用的录像输出错误回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput传递回调的录像输出实例。[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode) errorCode录像输出的错误码。

**参考：**

[CAMERA_SERVICE_FATAL_ERROR](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

#### OH_VideoOutput_RegisterCallback()

```ets
Camera_ErrorCode OH_VideoOutput_RegisterCallback(Camera_VideoOutput* videoOutput, VideoOutput_Callbacks* callback)
```

**描述**

注册录像输出更改事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput录像输出实例。[VideoOutput_Callbacks](../../topics/media/VideoOutput_Callbacks.md)* callback要注册的录像输出更改事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_VideoOutput_UnregisterCallback()

```ets
Camera_ErrorCode OH_VideoOutput_UnregisterCallback(Camera_VideoOutput* videoOutput, VideoOutput_Callbacks* callback)
```

**描述**

注销录像输出更改事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput录像输出实例。[VideoOutput_Callbacks](../../topics/media/VideoOutput_Callbacks.md)* callback要注销的录像输出更改事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_VideoOutput_Start()

```ets
Camera_ErrorCode OH_VideoOutput_Start(Camera_VideoOutput* videoOutput)
```

**描述**

开始录像输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput要启动的录像输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_VideoOutput_Stop()

```ets
Camera_ErrorCode OH_VideoOutput_Stop(Camera_VideoOutput* videoOutput)
```

**描述**

停止录像输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput要停止的录像输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_VideoOutput_Release()

```ets
Camera_ErrorCode OH_VideoOutput_Release(Camera_VideoOutput* videoOutput)
```

**描述**

释放录像输出实例。

**起始版本：** 11

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput要释放的录像输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_VideoOutput_GetActiveProfile()

```ets
Camera_ErrorCode OH_VideoOutput_GetActiveProfile(Camera_VideoOutput* videoOutput, Camera_VideoProfile** profile)
```

**描述**

获取当前视频输出配置文件。

**起始版本：** 12

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput传递当前视频输出配置文件的录像输出实例。[Camera_VideoProfile](../../topics/media/Camera_VideoProfile.md)** profile如果方法调用成功，将记录当前的视频输出配置文件。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_VideoOutput_DeleteProfile()

```ets
Camera_ErrorCode OH_VideoOutput_DeleteProfile(Camera_VideoProfile* profile)
```

**描述**

删除视频配置文件实例。

**起始版本：** 12

**参数：**

参数项描述[Camera_VideoProfile](../../topics/media/Camera_VideoProfile.md)* profile要删除的视频配置文件实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_VideoOutput_IsMirrorSupported()

```ets
 Camera_ErrorCode OH_VideoOutput_IsMirrorSupported(Camera_VideoOutput* videoOutput, bool* isSupported)
```

**描述**

判断当前视频输出是否支持镜像。

**起始版本：** 15

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput传递当前视频输出的录像输出实例。bool* isSupported当前视频输出是否支持镜像。true表示当前视频输出支持镜像，false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_VideoOutput_EnableMirror()

```ets
 Camera_ErrorCode OH_VideoOutput_EnableMirror(Camera_VideoOutput* videoOutput, bool mirrorMode)
```

**描述**

打开/关闭当前视频输出镜像功能。

**起始版本：** 15

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput传递当前视频输出的录像输出实例。bool mirrorMode设备是否开启镜像功能。true表示打开镜像功能，false表示关闭镜像功能。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_VideoOutput_GetVideoRotation()

```ets
 Camera_ErrorCode  OH_VideoOutput_GetVideoRotation(Camera_VideoOutput* videoOutput, int deviceDegree,Camera_ImageRotation* imageRotation)
```

**描述**

获取当前视频输出应当设置的旋转角度。

**起始版本：** 12

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput传递当前视频输出的录像输出实例。int deviceDegree设备目前相对于自然方向（充电口朝下）顺时针的旋转角度。[Camera_ImageRotation](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_imagerotation)* imageRotation当前视频输出应当设置的旋转角度。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_VideoOutput_GetSupportedFrameRates()

```ets
Camera_ErrorCode OH_VideoOutput_GetSupportedFrameRates(Camera_VideoOutput* videoOutput,Camera_FrameRateRange** frameRateRange, uint32_t* size)
```

**描述**

获取支持的视频输出帧率列表。

**起始版本：** 12

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput传递支持的视频输出帧率列表的录像输出实例。[Camera_FrameRateRange](../../topics/components/Camera_FrameRateRange.md)** frameRateRange如果方法调用成功，将记录支持的视频输出帧率列表。uint32_t* size如果方法调用成功，将记录支持的视频输出帧率列表大小。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_VideoOutput_DeleteFrameRates()

```ets
Camera_ErrorCode OH_VideoOutput_DeleteFrameRates(Camera_VideoOutput* videoOutput,Camera_FrameRateRange* frameRateRange)
```

**描述**

删除帧率列表。

**起始版本：** 12

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput录像输出实例。[Camera_FrameRateRange](../../topics/components/Camera_FrameRateRange.md)* frameRateRange要删除的帧率列表。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_VideoOutput_SetFrameRate()

```ets
Camera_ErrorCode OH_VideoOutput_SetFrameRate(Camera_VideoOutput* videoOutput,int32_t minFps, int32_t maxFps)
```

**描述**

设置视频输出帧率。

**起始版本：** 12

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput要设置帧率的录像输出实例。int32_t minFps设置的最小帧率。int32_t maxFps设置的最大帧率。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_VideoOutput_GetActiveFrameRate()

```ets
Camera_ErrorCode OH_VideoOutput_GetActiveFrameRate(Camera_VideoOutput* videoOutput,Camera_FrameRateRange* frameRateRange)
```

**描述**

获取当前视频输出帧率。

**起始版本：** 12

**参数：**

参数项描述[Camera_VideoOutput](../../topics/media/Camera_VideoOutput.md)* videoOutput传递当前视频输出帧率的录像输出实例。[Camera_FrameRateRange](../../topics/components/Camera_FrameRateRange.md)* frameRateRange如果方法调用成功，将记录当前的视频输出帧率。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。