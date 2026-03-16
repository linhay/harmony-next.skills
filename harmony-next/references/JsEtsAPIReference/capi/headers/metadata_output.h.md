# metadata_output.h

#### 概述

声明元数据输出概念。

**引用文件：** <ohcamera/metadata_output.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 11

**相关模块：**[OH_Camera](../../topics/media/OH_Camera.md)

#### 汇总

#### 结构体

名称typedef关键字描述[MetadataOutput_Callbacks](../../topics/misc/MetadataOutput_Callbacks.md)MetadataOutput_Callbacks元数据输出的回调。[Camera_MetadataOutput](../../topics/media/Camera_MetadataOutput.md)Camera_MetadataOutput

元数据输出对象。

 可以使用[OH_CameraManager_CreateMetadataOutput](camera_manager.h.md#ZH-CN_TOPIC_0000002529445763__oh_cameramanager_createmetadataoutput)方法创建指针。

#### 函数

名称typedef关键字描述[typedef void (*OH_MetadataOutput_OnMetadataObjectAvailable)(Camera_MetadataOutput* metadataOutput,Camera_MetadataObject* metadataObject, uint32_t size)](#ZH-CN_TOPIC_0000002497445820__oh_metadataoutput_onmetadataobjectavailable)OH_MetadataOutput_OnMetadataObjectAvailable在[MetadataOutput_Callbacks](../../topics/misc/MetadataOutput_Callbacks.md)中被调用的元数据输出元数据对象可用回调。[typedef void (*OH_MetadataOutput_OnError)(Camera_MetadataOutput* metadataOutput, Camera_ErrorCode errorCode)](#ZH-CN_TOPIC_0000002497445820__oh_metadataoutput_onerror)OH_MetadataOutput_OnError在[MetadataOutput_Callbacks](../../topics/misc/MetadataOutput_Callbacks.md)中被调用的元数据输出错误回调。[Camera_ErrorCode OH_MetadataOutput_RegisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback)](#ZH-CN_TOPIC_0000002497445820__oh_metadataoutput_registercallback)-注册元数据输出更改事件回调。[Camera_ErrorCode OH_MetadataOutput_UnregisterCallback(Camera_MetadataOutput* metadataOutput, MetadataOutput_Callbacks* callback)](#ZH-CN_TOPIC_0000002497445820__oh_metadataoutput_unregistercallback)-注销元数据输出更改事件回调。[Camera_ErrorCode OH_MetadataOutput_Start(Camera_MetadataOutput* metadataOutput)](#ZH-CN_TOPIC_0000002497445820__oh_metadataoutput_start)-启动元数据输出。[Camera_ErrorCode OH_MetadataOutput_Stop(Camera_MetadataOutput* metadataOutput)](#ZH-CN_TOPIC_0000002497445820__oh_metadataoutput_stop)-停止元数据输出。[Camera_ErrorCode OH_MetadataOutput_Release(Camera_MetadataOutput* metadataOutput)](#ZH-CN_TOPIC_0000002497445820__oh_metadataoutput_release)-释放元数据输出实例。

#### 函数说明

#### OH_MetadataOutput_OnMetadataObjectAvailable()

```ets
typedef void (*OH_MetadataOutput_OnMetadataObjectAvailable)(Camera_MetadataOutput* metadataOutput,Camera_MetadataObject* metadataObject, uint32_t size)
```

**描述**

在[MetadataOutput_Callbacks](../../topics/misc/MetadataOutput_Callbacks.md)中被调用的元数据输出元数据对象可用回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_MetadataOutput](../../topics/media/Camera_MetadataOutput.md)* metadataOutput传递回调的元数据输出实例。[Camera_MetadataObject](../../topics/media/Camera_MetadataObject.md)* metadataObject回调传递的元数据实例信息。uint32_t size元数据对象的大小。

#### OH_MetadataOutput_OnError()

```ets
typedef void (*OH_MetadataOutput_OnError)(Camera_MetadataOutput* metadataOutput, Camera_ErrorCode errorCode)
```

**描述**

在[MetadataOutput_Callbacks](../../topics/misc/MetadataOutput_Callbacks.md)中被调用的元数据输出错误回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_MetadataOutput](../../topics/media/Camera_MetadataOutput.md)* metadataOutput传递回调的元数据输出实例。[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode) errorCode元数据输出的错误码。

**参考：**

[CAMERA_SERVICE_FATAL_ERROR](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

#### OH_MetadataOutput_RegisterCallback()

```ets
Camera_ErrorCode OH_MetadataOutput_RegisterCallback(Camera_MetadataOutput* metadataOutput,MetadataOutput_Callbacks* callback)
```

**描述**

注册元数据输出更改事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_MetadataOutput](../../topics/media/Camera_MetadataOutput.md)* metadataOutput元数据输出实例。[MetadataOutput_Callbacks](../../topics/misc/MetadataOutput_Callbacks.md)* callback要注册的元数据输出回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_MetadataOutput_UnregisterCallback()

```ets
Camera_ErrorCode OH_MetadataOutput_UnregisterCallback(Camera_MetadataOutput* metadataOutput,MetadataOutput_Callbacks* callback)
```

**描述**

注销元数据输出更改事件回调。

**起始版本：** 11

**参数：**

参数项描述[Camera_MetadataOutput](../../topics/media/Camera_MetadataOutput.md)* metadataOutput元数据输出实例。[MetadataOutput_Callbacks](../../topics/misc/MetadataOutput_Callbacks.md)* callback要注销的元数据输出回调。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

#### OH_MetadataOutput_Start()

```ets
Camera_ErrorCode OH_MetadataOutput_Start(Camera_MetadataOutput* metadataOutput)
```

**描述**

启动元数据输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_MetadataOutput](../../topics/media/Camera_MetadataOutput.md)* metadataOutput要启动的元数据输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SESSION_NOT_CONFIG：捕获会话未配置。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_MetadataOutput_Stop()

```ets
Camera_ErrorCode OH_MetadataOutput_Stop(Camera_MetadataOutput* metadataOutput)
```

**描述**

停止元数据输出。

**起始版本：** 11

**参数：**

参数项描述[Camera_MetadataOutput](../../topics/media/Camera_MetadataOutput.md)* metadataOutput要停止的元数据输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_MetadataOutput_Release()

```ets
Camera_ErrorCode OH_MetadataOutput_Release(Camera_MetadataOutput* metadataOutput)
```

**描述**

释放元数据输出实例。

**起始版本：** 11

**参数：**

参数项描述[Camera_MetadataOutput](../../topics/media/Camera_MetadataOutput.md)* metadataOutput要释放的元数据输出实例。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功。

 CAMERA_INVALID_ARGUMENT：参数丢失或参数类型不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。