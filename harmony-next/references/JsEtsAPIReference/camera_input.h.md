# camera_input.h

#### 概述

声明相机输入概念。

**引用文件：** <ohcamera/camera_input.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：**[OH_Camera](OH_Camera.md)

#### 汇总

#### 结构体

名称typedef关键字描述[CameraInput_Callbacks](CameraInput_Callbacks.md)CameraInput_Callbacks相机输入错误事件的回调。[Camera_Input](Camera_Input.md)Camera_Input相机输入对象。可以使用[OH_CameraManager_CreateCameraInput](camera_manager.h.md#ZH-CN_TOPIC_0000002529445763__oh_cameramanager_createcamerainput)方法创建指针。

#### 函数

名称typedef关键字描述[typedef void (*OH_CameraInput_OnError)(const Camera_Input* cameraInput, Camera_ErrorCode errorCode)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_onerror)OH_CameraInput_OnError在[CameraInput_Callbacks](zh-cn_topic_0000002529285805.html)中被调用的相机输入错误回调。[Camera_ErrorCode OH_CameraInput_RegisterCallback(Camera_Input* cameraInput, CameraInput_Callbacks* callback)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_registercallback)-注册相机输入更改事件回调。[Camera_ErrorCode OH_CameraInput_UnregisterCallback(Camera_Input* cameraInput, CameraInput_Callbacks* callback)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_unregistercallback)-注销相机输入更改事件回调。[Camera_ErrorCode OH_CameraInput_Open(Camera_Input* cameraInput)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_open)-打开相机。[Camera_ErrorCode OH_CameraInput_OpenSecureCamera(Camera_Input* cameraInput, uint64_t* secureSeqId)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_opensecurecamera)-打开安全相机。[Camera_ErrorCode OH_CameraInput_OpenConcurrentCameras(Camera_Input* cameraInput, Camera_ConcurrentType type)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_openconcurrentcameras)-根据指定并发类型打开相机。[Camera_ErrorCode OH_CameraInput_Close(Camera_Input* cameraInput)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_close)-关闭相机。[Camera_ErrorCode OH_CameraInput_Release(Camera_Input* cameraInput)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_release)-

释放相机输入实例。

 和[OH_CameraInput_Close](camera_input.h.md#ZH-CN_TOPIC_0000002529285789__oh_camerainput_close)只需要调用其中一个，调用之后无须再调用[OH_CameraInput_Close](camera_input.h.md#ZH-CN_TOPIC_0000002529285789__oh_camerainput_close)。

[Camera_ErrorCode OH_CameraInput_IsPhysicalCameraOrientationVariable(Camera_Input* cameraInput, bool* isVariable)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_isphysicalcameraorientationvariable)-查询设备不同折叠状态下，相机物理镜头角度是否可变。[Camera_ErrorCode OH_CameraInput_GetPhysicalCameraOrientation(Camera_Input* cameraInput, uint32_t* orientation)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_getphysicalcameraorientation)-获取设备当前折叠状态下的物理镜头角度。[Camera_ErrorCode OH_CameraInput_UsePhysicalCameraOrientation(Camera_Input* cameraInput, bool isUsed)](#ZH-CN_TOPIC_0000002529285789__oh_camerainput_usephysicalcameraorientation)-选择是否使用物理镜头角度。

#### 函数说明

#### OH_CameraInput_OnError()

```ets
typedef void (*OH_CameraInput_OnError)(const Camera_Input* cameraInput, Camera_ErrorCode errorCode)
```

**描述**

在[CameraInput_Callbacks](CameraInput_Callbacks.md)中被调用的相机输入错误回调。

**起始版本：** 11

**参数：**

参数项描述const [Camera_Input](Camera_Input.md)* cameraInput传递回调的Camera_Input。[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode) errorCode相机输入的Camera_ErrorCode。

**参考：**

[CAMERA_CONFLICT_CAMERA](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

[CAMERA_DEVICE_DISABLED](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

[CAMERA_DEVICE_PREEMPTED](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

[CAMERA_SERVICE_FATAL_ERROR](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

#### OH_CameraInput_RegisterCallback()

```ets
Camera_ErrorCode OH_CameraInput_RegisterCallback(Camera_Input* cameraInput, CameraInput_Callbacks* callback)
```

**描述**

注册相机输入更改事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_Input](Camera_Input.md)* cameraInputCamera_Input实例。[CameraInput_Callbacks](CameraInput_Callbacks.md)* callback要注册的相机输入更改事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CameraInput_UnregisterCallback()

```ets
Camera_ErrorCode OH_CameraInput_UnregisterCallback(Camera_Input* cameraInput, CameraInput_Callbacks* callback)
```

**描述**

注销相机输入更改事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_Input](Camera_Input.md)* cameraInputCamera_Input实例。[CameraInput_Callbacks](CameraInput_Callbacks.md)* callback要注销的相机输入更改事件回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CameraInput_Open()

```ets
Camera_ErrorCode OH_CameraInput_Open(Camera_Input* cameraInput)
```

**描述**

打开相机。

**起始版本：** 11

**参数：**

参数项描述[Camera_Input](Camera_Input.md)* cameraInput要打开的Camera_Input实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_CONFLICT_CAMERA：因冲突而无法使用相机。

 CAMERA_DEVICE_DISABLED：由于安全原因禁用了相机。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CameraInput_OpenSecureCamera()

```ets
Camera_ErrorCode OH_CameraInput_OpenSecureCamera(Camera_Input* cameraInput, uint64_t* secureSeqId)
```

**描述**

打开安全相机。

**起始版本：** 12

**参数：**

参数项描述[Camera_Input](Camera_Input.md)* cameraInput要打开的Camera_Input实例。uint64_t* secureSeqId表示安全摄像头的序列值。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_CONFLICT_CAMERA：因冲突而无法使用相机。

 CAMERA_DEVICE_DISABLED：由于安全原因禁用了相机。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CameraInput_OpenConcurrentCameras()

```ets
Camera_ErrorCode OH_CameraInput_OpenConcurrentCameras(Camera_Input* cameraInput, Camera_ConcurrentType type)
```

**描述**

根据指定并发类型打开相机。

**起始版本：** 18

**参数：**

参数项描述[Camera_Input](Camera_Input.md)* cameraInput要打开的Camera_Input实例。[Camera_ConcurrentType](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_concurrenttype) type指定并发类型。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK: 方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_CONFLICT_CAMERA：因冲突而无法使用相机。

 CAMERA_DEVICE_DISABLED：由于安全原因禁用了相机。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CameraInput_Close()

```ets
Camera_ErrorCode OH_CameraInput_Close(Camera_Input* cameraInput)
```

**描述**

关闭相机。

**起始版本：** 11

**参数：**

参数项描述[Camera_Input](Camera_Input.md)* cameraInput要关闭的Camera_Input实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CameraInput_Release()

```ets
Camera_ErrorCode OH_CameraInput_Release(Camera_Input* cameraInput)
```

**描述**

释放相机输入实例。

 和[OH_CameraInput_Close](camera_input.h.md#ZH-CN_TOPIC_0000002529285789__oh_camerainput_close)只需要调用其中一个，调用之后无须再调用[OH_CameraInput_Close](camera_input.h.md#ZH-CN_TOPIC_0000002529285789__oh_camerainput_close)。

**起始版本：** 11

**参数：**

参数项描述[Camera_Input](Camera_Input.md)* cameraInput要释放的Camera_Input实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CameraInput_IsPhysicalCameraOrientationVariable()

```ets
Camera_ErrorCode OH_CameraInput_IsPhysicalCameraOrientationVariable(Camera_Input* cameraInput, bool* isVariable)
```

**描述**

查询设备不同折叠状态下，相机物理镜头角度是否可变。

**起始版本：** 22

**参数：**

参数项描述[Camera_Input](Camera_Input.md)* cameraInputCamera_Input实例。bool* isVariable查询设备不同折叠状态下，相机物理镜头角度是否可变。true表示可变，false表示不可变。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CameraInput_GetPhysicalCameraOrientation()

```ets
Camera_ErrorCode OH_CameraInput_GetPhysicalCameraOrientation(Camera_Input* cameraInput, uint32_t* orientation)
```

**描述**

获取设备当前折叠状态下的物理镜头角度。

**起始版本：** 22

**参数：**

参数项描述[Camera_Input](Camera_Input.md)* cameraInputCamera_Input实例。uint32_t* orientation如果方法调用成功，将返回设备当前折叠状态下的物理镜头角度。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_CameraInput_UsePhysicalCameraOrientation()

```ets
Camera_ErrorCode OH_CameraInput_UsePhysicalCameraOrientation(Camera_Input* cameraInput, bool isUsed)
```

**描述**

选择是否使用物理镜头角度。

**起始版本：** 22

**参数：**

参数项描述[Camera_Input](Camera_Input.md)* cameraInputCamera_Input实例。bool isUsed选择是否使用物理镜头角度。true表示使用，false表示不使用。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_OPERATION_NOT_ALLOWED：操作不允许。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。