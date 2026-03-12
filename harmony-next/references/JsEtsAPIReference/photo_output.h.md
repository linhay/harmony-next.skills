# photo_output.h

#### 概述

声明拍照输出概念。

**引用文件：** <ohcamera/photo_output.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：**[OH_Camera](OH_Camera.md)

#### 汇总

#### 结构体

名称typedef关键字描述[PhotoOutput_Callbacks](PhotoOutput_Callbacks.md)PhotoOutput_Callbacks拍照输出的回调。[Camera_PhotoOutput](Camera_PhotoOutput.md)Camera_PhotoOutput

拍照输出对象。

 可以使用[OH_CameraManager_CreatePhotoOutput](camera_manager.h.md#ZH-CN_TOPIC_0000002529445763__oh_cameramanager_createphotooutput)方法创建指针。

#### 函数

名称typedef关键字描述[typedef void (*OH_PhotoOutput_OnFrameStart)(Camera_PhotoOutput* photoOutput)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_onframestart)OH_PhotoOutput_OnFrameStart在[PhotoOutput_Callbacks](zh-cn_topic_0000002529285809.html)中被调用的拍照输出帧启动回调。[typedef void (*OH_PhotoOutput_OnFrameShutter)(Camera_PhotoOutput* photoOutput, Camera_FrameShutterInfo* info)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_onframeshutter)OH_PhotoOutput_OnFrameShutter在[PhotoOutput_Callbacks](zh-cn_topic_0000002529285809.html)中被调用的拍照输出帧快门回调。[typedef void (*OH_PhotoOutput_OnFrameEnd)(Camera_PhotoOutput* photoOutput, int32_t frameCount)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_onframeend)OH_PhotoOutput_OnFrameEnd在[PhotoOutput_Callbacks](zh-cn_topic_0000002529285809.html)中被调用的拍照输出帧结束回调。[typedef void (*OH_PhotoOutput_OnError)(Camera_PhotoOutput* photoOutput, Camera_ErrorCode errorCode)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_onerror)OH_PhotoOutput_OnError在[PhotoOutput_Callbacks](zh-cn_topic_0000002529285809.html)中被调用的拍照输出错误回调。[typedef void (*OH_PhotoOutput_CaptureEnd)(Camera_PhotoOutput* photoOutput, int32_t frameCount)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_captureend)OH_PhotoOutput_CaptureEnd拍照结束回调。[typedef void (*OH_PhotoOutput_CaptureStartWithInfo)(Camera_PhotoOutput* photoOutput, Camera_CaptureStartInfo* Info)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_capturestartwithinfo)OH_PhotoOutput_CaptureStartWithInfo拍照开始回调。[typedef void (*OH_PhotoOutput_OnFrameShutterEnd)(Camera_PhotoOutput* photoOutput, Camera_FrameShutterInfo* Info)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_onframeshutterend)OH_PhotoOutput_OnFrameShutterEnd拍照曝光结束回调。[typedef void (*OH_PhotoOutput_CaptureReady)(Camera_PhotoOutput* photoOutput)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_captureready)OH_PhotoOutput_CaptureReady拍照准备就绪回调。收到回调后，可以继续进行下一次拍照。[typedef void (*OH_PhotoOutput_EstimatedCaptureDuration)(Camera_PhotoOutput* photoOutput, int64_t duration)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_estimatedcaptureduration)OH_PhotoOutput_EstimatedCaptureDuration预计拍照时间回调。[typedef void (*OH_PhotoOutput_PhotoAvailable)(Camera_PhotoOutput* photoOutput, OH_PhotoNative* photo)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_photoavailable)OH_PhotoOutput_PhotoAvailable照片输出可用高分辨率图像回调。[typedef void (*OH_PhotoOutput_PhotoAssetAvailable)(Camera_PhotoOutput* photoOutput, OH_MediaAsset* photoAsset)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_photoassetavailable)OH_PhotoOutput_PhotoAssetAvailable输出照片资源可用回调。[Camera_ErrorCode OH_PhotoOutput_RegisterCallback(Camera_PhotoOutput* photoOutput, PhotoOutput_Callbacks* callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_registercallback)-注册拍照输出更改事件回调。[Camera_ErrorCode OH_PhotoOutput_UnregisterCallback(Camera_PhotoOutput* photoOutput, PhotoOutput_Callbacks* callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_unregistercallback)-注销拍照输出更改事件回调。[Camera_ErrorCode OH_PhotoOutput_RegisterCaptureStartWithInfoCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureStartWithInfo callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_registercapturestartwithinfocallback)-注册拍照开始事件回调。[Camera_ErrorCode OH_PhotoOutput_GetPhotoRotation(Camera_PhotoOutput* photoOutput, int deviceDegree, Camera_ImageRotation* imageRotation)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_getphotorotation)-获取照片旋转角度。[Camera_ErrorCode OH_PhotoOutput_UnregisterCaptureStartWithInfoCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureStartWithInfo callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_unregistercapturestartwithinfocallback)-注销拍照开始事件回调。[Camera_ErrorCode OH_PhotoOutput_RegisterCaptureEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureEnd callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_registercaptureendcallback)-注册拍照结束事件回调。[Camera_ErrorCode OH_PhotoOutput_UnregisterCaptureEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureEnd callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_unregistercaptureendcallback)-注销拍照结束事件回调。[Camera_ErrorCode OH_PhotoOutput_RegisterFrameShutterEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_OnFrameShutterEnd callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_registerframeshutterendcallback)-注册拍照曝光结束事件回调。[Camera_ErrorCode OH_PhotoOutput_UnregisterFrameShutterEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_OnFrameShutterEnd callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_unregisterframeshutterendcallback)-注销拍照曝光结束事件回调。[Camera_ErrorCode OH_PhotoOutput_RegisterCaptureReadyCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureReady callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_registercapturereadycallback)-注册拍照就绪事件回调。收到回调后，可以继续进行下一次拍照。[Camera_ErrorCode OH_PhotoOutput_UnregisterCaptureReadyCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureReady callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_unregistercapturereadycallback)-注销拍照就绪事件回调。[Camera_ErrorCode OH_PhotoOutput_RegisterEstimatedCaptureDurationCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_EstimatedCaptureDuration callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_registerestimatedcapturedurationcallback)-注册预计拍照时间事件回调。[Camera_ErrorCode OH_PhotoOutput_UnregisterEstimatedCaptureDurationCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_EstimatedCaptureDuration callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_unregisterestimatedcapturedurationcallback)-注销预计拍照时间事件回调。[Camera_ErrorCode OH_PhotoOutput_RegisterPhotoAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAvailable callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_registerphotoavailablecallback)-注册输出照片可用回调。[Camera_ErrorCode OH_PhotoOutput_UnregisterPhotoAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAvailable callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_unregisterphotoavailablecallback)-注销输出照片可用回调。[Camera_ErrorCode OH_PhotoOutput_RegisterPhotoAssetAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAssetAvailable callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_registerphotoassetavailablecallback)-注册输出照片资源可用回调。[Camera_ErrorCode OH_PhotoOutput_UnregisterPhotoAssetAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAssetAvailable callback)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_unregisterphotoassetavailablecallback)-注销输出照片资源可用回调。[Camera_ErrorCode OH_PhotoOutput_Capture(Camera_PhotoOutput* photoOutput)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_capture)-

拍摄照片。

 必须在[OH_PreviewOutput_Release](preview_output.h.md#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_release)之前调用，否则会导致无法拍照。

[Camera_ErrorCode OH_PhotoOutput_Capture_WithCaptureSetting(Camera_PhotoOutput* photoOutput, Camera_PhotoCaptureSetting setting)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_capture_withcapturesetting)-使用捕获设置捕获拍照。[Camera_ErrorCode OH_PhotoOutput_Release(Camera_PhotoOutput* photoOutput)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_release)-释放拍照输出。[Camera_ErrorCode OH_PhotoOutput_IsMirrorSupported(Camera_PhotoOutput* photoOutput, bool* isSupported)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_ismirrorsupported)-检查是否支持镜像拍照。[Camera_ErrorCode OH_PhotoOutput_EnableMirror(Camera_PhotoOutput* photoOutput, bool enabled)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_enablemirror)-是否启用动态照片镜像拍照。[Camera_ErrorCode OH_PhotoOutput_GetActiveProfile(Camera_PhotoOutput* photoOutput, Camera_Profile** profile)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_getactiveprofile)-获取当前照片输出配置文件。[Camera_ErrorCode OH_PhotoOutput_DeleteProfile(Camera_Profile* profile)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_deleteprofile)-删除照片配置文件实例。[Camera_ErrorCode OH_PhotoOutput_IsMovingPhotoSupported(Camera_PhotoOutput* photoOutput, bool* isSupported)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_ismovingphotosupported)-检查是否支持动态照片。[Camera_ErrorCode OH_PhotoOutput_EnableMovingPhoto(Camera_PhotoOutput* photoOutput, bool enabled)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_enablemovingphoto)-是否启用动态照片。[Camera_ErrorCode OH_PhotoOutput_IsPhotoQualityPrioritizationSupported(Camera_PhotoOutput* photoOutput, Camera_PhotoQualityPrioritization qualityPrioritization, bool* isSupported)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_isphotoqualityprioritizationsupported)-检查是否支持指定的拍照画质优先策略。[Camera_ErrorCode OH_PhotoOutput_SetPhotoQualityPrioritization(Camera_PhotoOutput* photoOutput, Camera_PhotoQualityPrioritization qualityPrioritization)](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_setphotoqualityprioritization)-设置拍照画质优先策略。

#### 函数说明

#### OH_PhotoOutput_OnFrameStart()

```ets
typedef void (*OH_PhotoOutput_OnFrameStart)(Camera_PhotoOutput* photoOutput)
```

**描述**

在[PhotoOutput_Callbacks](PhotoOutput_Callbacks.md)中被调用的拍照输出帧启动回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。

#### OH_PhotoOutput_OnFrameShutter()

```ets
typedef void (*OH_PhotoOutput_OnFrameShutter)(Camera_PhotoOutput* photoOutput, Camera_FrameShutterInfo* info)
```

**描述**

在[PhotoOutput_Callbacks](PhotoOutput_Callbacks.md)中被调用的拍照输出帧快门回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。[Camera_FrameShutterInfo](Camera_FrameShutterInfo.md)* info回调传递的帧快门回调信息。

#### OH_PhotoOutput_OnFrameEnd()

```ets
typedef void (*OH_PhotoOutput_OnFrameEnd)(Camera_PhotoOutput* photoOutput, int32_t frameCount)
```

**描述**

在[PhotoOutput_Callbacks](PhotoOutput_Callbacks.md)中被调用的拍照输出帧结束回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。int32_t frameCount回调传递的帧计数。

#### OH_PhotoOutput_OnError()

```ets
typedef void (*OH_PhotoOutput_OnError)(Camera_PhotoOutput* photoOutput, Camera_ErrorCode errorCode)
```

**描述**

在[PhotoOutput_Callbacks](PhotoOutput_Callbacks.md)中被调用的拍照输出错误回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode) errorCode拍照输出的错误码。

**参考：**

[CAMERA_SERVICE_FATAL_ERROR](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

#### OH_PhotoOutput_CaptureEnd()

```ets
typedef void (*OH_PhotoOutput_CaptureEnd)(Camera_PhotoOutput* photoOutput, int32_t frameCount)
```

**描述**

拍照结束回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。int32_t frameCount回调传递的帧数。

#### OH_PhotoOutput_CaptureStartWithInfo()

```ets
typedef void (*OH_PhotoOutput_CaptureStartWithInfo)(Camera_PhotoOutput* photoOutput, Camera_CaptureStartInfo* Info)
```

**描述**

拍照开始回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。[Camera_CaptureStartInfo](Camera_CaptureStartInfo.md)* Info回调传递的拍照开始信息。

#### OH_PhotoOutput_OnFrameShutterEnd()

```ets
typedef void (*OH_PhotoOutput_OnFrameShutterEnd)(Camera_PhotoOutput* photoOutput, Camera_FrameShutterInfo* Info)
```

**描述**

拍照曝光结束回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。[Camera_FrameShutterInfo](Camera_FrameShutterInfo.md)* Info回调传递的帧快门回调信息。

#### OH_PhotoOutput_CaptureReady()

```ets
typedef void (*OH_PhotoOutput_CaptureReady)(Camera_PhotoOutput* photoOutput)
```

**描述**

拍照准备就绪回调。收到回调后，可以继续进行下一次拍照。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。

#### OH_PhotoOutput_EstimatedCaptureDuration()

```ets
typedef void (*OH_PhotoOutput_EstimatedCaptureDuration)(Camera_PhotoOutput* photoOutput, int64_t duration)
```

**描述**

预计拍照时间回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。int64_t duration回调传递的预计拍照时间，单位毫秒。

#### OH_PhotoOutput_PhotoAvailable()

```ets
typedef void (*OH_PhotoOutput_PhotoAvailable)(Camera_PhotoOutput* photoOutput, OH_PhotoNative* photo)
```

**描述**

照片输出可用高分辨率图像回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。[OH_PhotoNative](OH_PhotoNative.md)* photo回调传递的OH_PhotoNative。

#### OH_PhotoOutput_PhotoAssetAvailable()

```ets
typedef void (*OH_PhotoOutput_PhotoAssetAvailable)(Camera_PhotoOutput* photoOutput, OH_MediaAsset* photoAsset)
```

**描述**

输出照片资源可用回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递回调的拍照输出实例。[OH_MediaAsset](OH_MediaAsset.md)* photoAsset回调传递的媒体资源。

#### OH_PhotoOutput_RegisterCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_RegisterCallback(Camera_PhotoOutput* photoOutput, PhotoOutput_Callbacks* callback)
```

**描述**

注册拍照输出更改事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[PhotoOutput_Callbacks](PhotoOutput_Callbacks.md)* callback要注册的拍照输出更改事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_UnregisterCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_UnregisterCallback(Camera_PhotoOutput* photoOutput, PhotoOutput_Callbacks* callback)
```

**描述**

注销拍照输出更改事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[PhotoOutput_Callbacks](PhotoOutput_Callbacks.md)* callback要注销的拍照输出更改事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_RegisterCaptureStartWithInfoCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_RegisterCaptureStartWithInfoCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureStartWithInfo callback)
```

**描述**

注册拍照开始事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_CaptureStartWithInfo](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_capturestartwithinfo) callback要注册的拍照开始事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_GetPhotoRotation()

```ets
Camera_ErrorCode OH_PhotoOutput_GetPhotoRotation(Camera_PhotoOutput* photoOutput, int deviceDegree, Camera_ImageRotation* imageRotation)
```

**描述**

获取照片旋转角度。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput用于获取照片旋转角度的拍照输出实例。int deviceDegree当前设备旋转角度。[Camera_ImageRotation](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_imagerotation)* imageRotation照片旋转角度的结果。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_UnregisterCaptureStartWithInfoCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_UnregisterCaptureStartWithInfoCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureStartWithInfo callback)
```

**描述**

注销拍照开始事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_CaptureStartWithInfo](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_capturestartwithinfo) callback要注销的拍照开始事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_RegisterCaptureEndCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_RegisterCaptureEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureEnd callback)
```

**描述**

注册拍照结束事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_CaptureEnd](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_captureend) callback要注册的拍照结束事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_UnregisterCaptureEndCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_UnregisterCaptureEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureEnd callback)
```

**描述**

注销拍照结束事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_CaptureEnd](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_captureend) callback要注销的拍照结束事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_RegisterFrameShutterEndCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_RegisterFrameShutterEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_OnFrameShutterEnd callback)
```

**描述**

注册拍照曝光结束事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_OnFrameShutterEnd](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_onframeshutterend) callback要注册的拍照曝光结束事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_UnregisterFrameShutterEndCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_UnregisterFrameShutterEndCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_OnFrameShutterEnd callback)
```

**描述**

注销拍照曝光结束事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_OnFrameShutterEnd](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_onframeshutterend) callback要注销的拍照曝光结束事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_RegisterCaptureReadyCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_RegisterCaptureReadyCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureReady callback)
```

**描述**

注册拍照就绪事件回调。收到回调后，可以继续进行下一次拍照。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_CaptureReady](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_captureready) callback要注册的拍照就绪事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_UnregisterCaptureReadyCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_UnregisterCaptureReadyCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_CaptureReady callback)
```

**描述**

注销拍照就绪事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_CaptureReady](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_captureready) callback要注销的拍照就绪事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_RegisterEstimatedCaptureDurationCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_RegisterEstimatedCaptureDurationCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_EstimatedCaptureDuration callback)
```

**描述**

注册预计拍照时间事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_EstimatedCaptureDuration](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_estimatedcaptureduration) callback要注册的预计拍照时间事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_UnregisterEstimatedCaptureDurationCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_UnregisterEstimatedCaptureDurationCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_EstimatedCaptureDuration callback)
```

**描述**

注销预计拍照时间事件回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_EstimatedCaptureDuration](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_estimatedcaptureduration) callback要注销的预计拍照时间事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_RegisterPhotoAvailableCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_RegisterPhotoAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAvailable callback)
```

**描述**

注册输出照片可用回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_PhotoAvailable](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_photoavailable) callback要注册的输出照片可用回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_UnregisterPhotoAvailableCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_UnregisterPhotoAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAvailable callback)
```

**描述**

注销输出照片可用回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_PhotoAvailable](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_photoavailable) callback要注销的输出照片可用回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_RegisterPhotoAssetAvailableCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_RegisterPhotoAssetAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAssetAvailable callback)
```

**描述**

注册输出照片资源可用回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_PhotoAssetAvailable](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_photoassetavailable) callback要注册的输出照片资源可用回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_UnregisterPhotoAssetAvailableCallback()

```ets
Camera_ErrorCode OH_PhotoOutput_UnregisterPhotoAssetAvailableCallback(Camera_PhotoOutput* photoOutput, OH_PhotoOutput_PhotoAssetAvailable callback)
```

**描述**

注销输出照片资源可用回调。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例。[OH_PhotoOutput_PhotoAssetAvailable](#ZH-CN_TOPIC_0000002529445765__oh_photooutput_photoassetavailable) callback要注销的输出照片资源可用回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_Capture()

```ets
Camera_ErrorCode OH_PhotoOutput_Capture(Camera_PhotoOutput* photoOutput)
```

**描述**

拍摄照片。

 必须在[OH_PreviewOutput_Release](preview_output.h.md#ZH-CN_TOPIC_0000002497605802__oh_previewoutput_release)之前调用，否则会导致无法拍照。

**起始版本：** 11

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput用于捕获拍照的拍照输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_RUNNING：捕获会话未运行。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_Capture_WithCaptureSetting()

```ets
Camera_ErrorCode OH_PhotoOutput_Capture_WithCaptureSetting(Camera_PhotoOutput* photoOutput, Camera_PhotoCaptureSetting setting)
```

**描述**

使用捕获设置捕获拍照。

**起始版本：** 11

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput用于捕获拍照的拍照输出实例。[Camera_PhotoCaptureSetting](Camera_PhotoCaptureSetting.md) setting用于捕获拍照的[Camera_PhotoCaptureSetting](Camera_PhotoCaptureSetting.md)。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_RUNNING：捕获会话未运行。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_Release()

```ets
Camera_ErrorCode OH_PhotoOutput_Release(Camera_PhotoOutput* photoOutput)
```

**描述**

释放拍照输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput要释放的拍照输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_IsMirrorSupported()

```ets
Camera_ErrorCode OH_PhotoOutput_IsMirrorSupported(Camera_PhotoOutput* photoOutput, bool* isSupported)
```

**描述**

检查是否支持镜像拍照。

**起始版本：** 11

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例，用于检查是否支持镜像。bool* isSupported是否支持镜像的结果。true表示支持镜像，false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_EnableMirror()

```ets
Camera_ErrorCode OH_PhotoOutput_EnableMirror(Camera_PhotoOutput* photoOutput, bool enabled)
```

**描述**

是否启用动态照片镜像拍照。

**起始版本：** 13

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput拍照输出实例，用于确认是否启用镜像拍照。bool enabled是否启用动态照片镜像拍照的结果，true为开启动态照片镜像拍照，false为关闭动态照片镜像拍照。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_GetActiveProfile()

```ets
Camera_ErrorCode OH_PhotoOutput_GetActiveProfile(Camera_PhotoOutput* photoOutput, Camera_Profile** profile)
```

**描述**

获取当前照片输出配置文件。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput传递当前配置文件的拍照输出实例。[Camera_Profile](Camera_Profile.md)** profile如果方法调用成功，将记录照片输出配置文件。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_DeleteProfile()

```ets
Camera_ErrorCode OH_PhotoOutput_DeleteProfile(Camera_Profile* profile)
```

**描述**

删除照片配置文件实例。

**起始版本：** 12

**参数：**

参数项描述[Camera_Profile](Camera_Profile.md)* profile要被删除的照片配置文件实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_PhotoOutput_IsMovingPhotoSupported()

```ets
Camera_ErrorCode OH_PhotoOutput_IsMovingPhotoSupported(Camera_PhotoOutput* photoOutput, bool* isSupported)
```

**描述**

检查是否支持动态照片。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput用于检查是否支持动态照片的拍照输出实例。bool* isSupported是否支持动态照片的结果。true表示支持动态照片，false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_EnableMovingPhoto()

```ets
Camera_ErrorCode OH_PhotoOutput_EnableMovingPhoto(Camera_PhotoOutput* photoOutput, bool enabled)
```

**描述**

是否启用动态照片。

**起始版本：** 12

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput用于启用或禁用动态照片的拍照输出实例。bool enabled是否启用动态照片。true表示启用动态照片，false表示不启用。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_IsPhotoQualityPrioritizationSupported()

```ets
Camera_ErrorCode OH_PhotoOutput_IsPhotoQualityPrioritizationSupported(Camera_PhotoOutput* photoOutput, Camera_PhotoQualityPrioritization qualityPrioritization, bool* isSupported)
```

**描述**

检查是否支持指定的拍照画质优先策略。

**起始版本：** 21

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput用于获取是否支持拍照画质优先策略的拍照输出实例。[Camera_PhotoQualityPrioritization](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_photoqualityprioritization) qualityPrioritization要检查的拍照画质优先策略。bool* isSupported是否支持指定的拍照画质优先策略。true表示支持，false表示不支持。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_PhotoOutput_SetPhotoQualityPrioritization()

```ets
Camera_ErrorCode OH_PhotoOutput_SetPhotoQualityPrioritization(Camera_PhotoOutput* photoOutput, Camera_PhotoQualityPrioritization qualityPrioritization)
```

**描述**

设置拍照画质优先策略。

**起始版本：** 21

**参数：**

参数项描述[Camera_PhotoOutput](Camera_PhotoOutput.md)* photoOutput用于设置拍照画质优先策略的拍照输出实例。[Camera_PhotoQualityPrioritization](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_photoqualityprioritization) qualityPrioritization要设置的拍照画质优先策略。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。