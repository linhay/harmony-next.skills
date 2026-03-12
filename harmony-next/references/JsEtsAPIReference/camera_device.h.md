# camera_device.h

#### 概述

声明相机的基本概念。

**引用文件：** <ohcamera/camera_device.h>

**库：** libohcamera.so

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 12

**相关模块：**[OH_Camera](OH_Camera.md)

#### 汇总

#### 函数

名称描述[Camera_ErrorCode OH_CameraDevice_GetCameraOrientation(Camera_Device* camera, uint32_t* orientation)](#ZH-CN_TOPIC_0000002497445818__oh_cameradevice_getcameraorientation)获取相机设备的传感器方向属性。[Camera_ErrorCode OH_CameraDevice_GetHostDeviceName(Camera_Device* camera, char** hostDeviceName)](#ZH-CN_TOPIC_0000002497445818__oh_cameradevice_gethostdevicename)获取远程设备名称。[Camera_ErrorCode OH_CameraDevice_GetHostDeviceType(Camera_Device* camera, Camera_HostDeviceType* hostDeviceType)](#ZH-CN_TOPIC_0000002497445818__oh_cameradevice_gethostdevicetype)获取远程设备类型。

#### 函数说明

#### OH_CameraDevice_GetCameraOrientation()

```ets
Camera_ErrorCode OH_CameraDevice_GetCameraOrientation(Camera_Device* camera, uint32_t* orientation)
```

**描述**

获取相机设备的传感器方向属性。

**起始版本：** 12

**参数：**

参数项描述[Camera_Device](Camera_Device.md)* camera用于获取属性的Camera_Device。uint32_t* orientation返回相机sensor角度属性。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功，返回传感器方向属性。

 CAMERA_CAMERA_INVALID_ARGUMENT：参数丢失或者参数不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CameraDevice_GetHostDeviceName()

```ets
Camera_ErrorCode OH_CameraDevice_GetHostDeviceName(Camera_Device* camera, char** hostDeviceName)
```

**描述**

获取远程设备名称。

**起始版本：** 15

**参数：**

参数项描述[Camera_Device](Camera_Device.md)* camera用于获取属性的Camera_Device。char** hostDeviceName返回远程设备名称属性。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功，将返回远程设备名称属性。

 CAMERA_CAMERA_INVALID_ARGUMENT：参数丢失或者参数不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。

#### OH_CameraDevice_GetHostDeviceType()

```ets
Camera_ErrorCode OH_CameraDevice_GetHostDeviceType(Camera_Device* camera, Camera_HostDeviceType* hostDeviceType)
```

**描述**

获取远程设备类型。

**起始版本：** 15

**参数：**

参数项描述[Camera_Device](Camera_Device.md)* camera用于获取属性的Camera_Device。[Camera_HostDeviceType](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_hostdevicetype)* hostDeviceType远程设备类型属性。

**返回：**

类型说明[Camera_ErrorCode](camera.h.md#ZH-CN_TOPIC_0000002497605798__camera_errorcode)

CAMERA_OK：方法调用成功，将返回远程设备名称属性。

 CAMERA_CAMERA_INVALID_ARGUMENT：参数丢失或者参数不正确。

 CAMERA_SERVICE_FATAL_ERROR：相机服务异常。