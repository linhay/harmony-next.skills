# scsi_peripheral_api.h

**概述**

声明用于主机侧访问SCSI设备的SCSI Peripheral DDK接口。

引用文件： <scsi_peripheral/scsi_peripheral_api.h>

库： libscsi.z.so

系统能力： SystemCapability.Driver.SCSI.Extension

起始版本： 18

相关模块： [ScsiPeripheralDDK](ScsiPeripheralDDK.md)

**汇总**

**函数**

| 名称 | 描述 |
| --- | --- |
| int32_t OH_ScsiPeripheral_Init(void) | 初始化SCSI Peripheral DDK。 |
| int32_t OH_ScsiPeripheral_Release(void) | 释放SCSI Peripheral DDK。 |
| int32_t OH_ScsiPeripheral_Open(uint64_t deviceId, uint8_t interfaceIndex, ScsiPeripheral_Device **dev) | 打开deviceId和interfaceIndex指定的SCSI设备。 |
| int32_t OH_ScsiPeripheral_Close(ScsiPeripheral_Device **dev) | 关闭SCSI设备。 |
| int32_t OH_ScsiPeripheral_TestUnitReady(ScsiPeripheral_Device *dev, ScsiPeripheral_TestUnitReadyRequest *request,ScsiPeripheral_Response *response) | 检查逻辑单元是否已经准备好。 |
| int32_t OH_ScsiPeripheral_Inquiry(ScsiPeripheral_Device *dev, ScsiPeripheral_InquiryRequest *request,ScsiPeripheral_InquiryInfo *inquiryInfo, ScsiPeripheral_Response *response) | 查询SCSI设备的基本信息。 |
| int32_t OH_ScsiPeripheral_ReadCapacity10(ScsiPeripheral_Device *dev, ScsiPeripheral_ReadCapacityRequest *request,ScsiPeripheral_CapacityInfo *capacityInfo, ScsiPeripheral_Response *response) | 获取SCSI设备的容量信息。 |
| int32_t OH_ScsiPeripheral_RequestSense(ScsiPeripheral_Device *dev, ScsiPeripheral_RequestSenseRequest *request,ScsiPeripheral_Response *response) | 获取sense data（SCSI设备返回给主机的信息，用于报告设备的状态、错误信息以及诊断信息）。 |
| int32_t OH_ScsiPeripheral_Read10(ScsiPeripheral_Device *dev, ScsiPeripheral_IORequest *request,ScsiPeripheral_Response *response) | 从指定逻辑块读取数据。 |
| int32_t OH_ScsiPeripheral_Write10(ScsiPeripheral_Device *dev, ScsiPeripheral_IORequest *request,ScsiPeripheral_Response *response) | 写数据到设备的指定逻辑块。 |
| int32_t OH_ScsiPeripheral_Verify10(ScsiPeripheral_Device *dev, ScsiPeripheral_VerifyRequest *request,ScsiPeripheral_Response *response) | 校验指定逻辑块。 |
| int32_t OH_ScsiPeripheral_SendRequestByCdb(ScsiPeripheral_Device *dev, ScsiPeripheral_Request *request,ScsiPeripheral_Response *response) | 以CDB（Command Descriptor Block）方式发送SCSI命令。 |
| int32_t OH_ScsiPeripheral_CreateDeviceMemMap(ScsiPeripheral_Device *dev, size_t size,ScsiPeripheral_DeviceMemMap **devMmap) | 创建缓冲区。请在缓冲区使用完后，调用OH_ScsiPeripheral_DestroyDeviceMemMap销毁缓冲区，否则会造成资源泄露。 |
| int32_t OH_ScsiPeripheral_DestroyDeviceMemMap(ScsiPeripheral_DeviceMemMap *devMmap) | 销毁缓冲区。请在缓冲区使用完后及时销毁缓冲区，否则会造成资源泄露。 |
| int32_t OH_ScsiPeripheral_ParseBasicSenseInfo(uint8_t *senseData, uint8_t senseDataLen,ScsiPeripheral_BasicSenseInfo *senseInfo) | 解析基本的sense data，包括Information、Command specific information、Sense key specific字段。 |

**函数说明**

**OH_ScsiPeripheral_Init()**

```ets
int32_t OH_ScsiPeripheral_Init(void)
```

描述

初始化SCSI Peripheral DDK。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 初始化DDK失败。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。 |

**OH_ScsiPeripheral_Release()**

```ets
int32_t OH_ScsiPeripheral_Release(void)
```

描述

释放SCSI Peripheral DDK。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。 |

**OH_ScsiPeripheral_Open()**

```ets
int32_t OH_ScsiPeripheral_Open(uint64_t deviceId, uint8_t interfaceIndex, ScsiPeripheral_Device **dev)
```

描述

打开deviceId和interfaceIndex指定的SCSI设备。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| uint64_t deviceId | 设备ID，代表要操作的设备。 |
| uint8_t interfaceIndex | 接口索引，对应SCSI设备的接口。 |
| ScsiPeripheral_Device **dev | 设备句柄，详情参见ScsiPeripheral_Device。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。  SCSIPERIPHERAL_DDK_IO_ERROR DDK发生IO错误。  SCSIPERIPHERAL_DDK_DEVICE_NOT_FOUND 通过deviceId和interfaceIndex找不到设备。  SCSIPERIPHERAL_DDK_INVALID_OPERATION 不支持该操作。  SCSIPERIPHERAL_DDK_TIMEOUT 传输超时。 |

**OH_ScsiPeripheral_Close()**

```ets
int32_t OH_ScsiPeripheral_Close(ScsiPeripheral_Device **dev)
```

描述

关闭SCSI设备。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_Device **dev | 设备句柄，详情参见ScsiPeripheral_Device。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。  SCSIPERIPHERAL_DDK_IO_ERROR DDK发生I/O错误。 |

**OH_ScsiPeripheral_TestUnitReady()**

```ets
int32_t OH_ScsiPeripheral_TestUnitReady(ScsiPeripheral_Device *dev, ScsiPeripheral_TestUnitReadyRequest *request,ScsiPeripheral_Response *response)
```

描述

检查逻辑单元是否已经准备好。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_Device *dev | 设备句柄，详情参见ScsiPeripheral_Device。 |
| ScsiPeripheral_TestUnitReadyRequest *request | 逻辑单元检查命令（test unit ready）的请求信息，详情参见ScsiPeripheral_TestUnitReadyRequest。 |
| ScsiPeripheral_Response *response | 逻辑单元检查命令（test unit ready）的响应信息，详情参见ScsiPeripheral_Response。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空、request为空或者response为空。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。  SCSIPERIPHERAL_DDK_IO_ERROR DDK发生I/O错误。  SCSIPERIPHERAL_DDK_TIMEOUT 传输超时。  SCSIPERIPHERAL_DDK_INVALID_OPERATION 不支持该操作。 |

**OH_ScsiPeripheral_Inquiry()**

```ets
int32_t OH_ScsiPeripheral_Inquiry(ScsiPeripheral_Device *dev, ScsiPeripheral_InquiryRequest *request,ScsiPeripheral_InquiryInfo *inquiryInfo, ScsiPeripheral_Response *response)
```

描述

查询SCSI设备的基本信息。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_Device *dev | 设备句柄，详情参见ScsiPeripheral_Device。 |
| ScsiPeripheral_InquiryRequest *request | inquiry命令的请求信息，详情参见ScsiPeripheral_InquiryRequest。 |
| ScsiPeripheral_InquiryInfo *inquiryInfo | inquiry命令返回的查询信息，详情参见ScsiPeripheral_InquiryInfo。 |
| ScsiPeripheral_Response *response | inquiry命令返回的原始响应信息，详情参见ScsiPeripheral_Response。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空、 request为空、inquiryInfo 为空、inquiryInfo->data或者response为空。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。  SCSIPERIPHERAL_DDK_IO_ERROR DDK发生I/O错误。  SCSIPERIPHERAL_DDK_TIMEOUT 传输超时。  SCSIPERIPHERAL_DDK_INVALID_OPERATION 不支持该操作。 |

**OH_ScsiPeripheral_ReadCapacity10()**

```ets
int32_t OH_ScsiPeripheral_ReadCapacity10(ScsiPeripheral_Device *dev, ScsiPeripheral_ReadCapacityRequest *request,ScsiPeripheral_CapacityInfo *capacityInfo, ScsiPeripheral_Response *response)
```

描述

获取SCSI设备的容量信息。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_Device *dev | 设备句柄，详情参见ScsiPeripheral_Device。 |
| ScsiPeripheral_ReadCapacityRequest *request | read capacity命令的请求信息，详情参见ScsiPeripheral_ReadCapacityRequest。 |
| ScsiPeripheral_CapacityInfo *capacityInfo | read capacity命令返回的容量信息，详情参见ScsiPeripheral_CapacityInfo。 |
| ScsiPeripheral_Response *response | read capacity命令返回的原始响应信息，详情参见ScsiPeripheral_Response。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空、 request为空、capacityInfo为空或者response为空。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。  SCSIPERIPHERAL_DDK_IO_ERROR DDK发生I/O错误。  SCSIPERIPHERAL_DDK_TIMEOUT 传输超时。  SCSIPERIPHERAL_DDK_INVALID_OPERATION 不支持该操作。 |

**OH_ScsiPeripheral_RequestSense()**

```ets
int32_t OH_ScsiPeripheral_RequestSense(ScsiPeripheral_Device *dev, ScsiPeripheral_RequestSenseRequest *request,ScsiPeripheral_Response *response)
```

描述

获取sense data（SCSI设备返回给主机的信息，用于报告设备的状态、错误信息以及诊断信息）。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_Device *dev | 设备句柄，详情参见ScsiPeripheral_Device。 |
| ScsiPeripheral_RequestSenseRequest *request | request sense命令的请求信息，详情参见ScsiPeripheral_RequestSenseRequest。 |
| ScsiPeripheral_Response *response | request sense命令返回的响应信息，详情参见ScsiPeripheral_Response。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空、 request为空或者response为空。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。  SCSIPERIPHERAL_DDK_IO_ERROR DDK发生I/O错误。  SCSIPERIPHERAL_DDK_TIMEOUT 传输超时。  SCSIPERIPHERAL_DDK_INVALID_OPERATION 不支持该操作。 |

**OH_ScsiPeripheral_Read10()**

```ets
int32_t OH_ScsiPeripheral_Read10(ScsiPeripheral_Device *dev, ScsiPeripheral_IORequest *request,ScsiPeripheral_Response *response)
```

描述

从指定逻辑块读取数据。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_Device *dev | 设备句柄，详情参见ScsiPeripheral_Device。 |
| ScsiPeripheral_IORequest *request | read命令的请求信息，详情参见ScsiPeripheral_IORequest。 |
| ScsiPeripheral_Response *response | read命令返回的响应信息，详情参见ScsiPeripheral_Response。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空、 request为空、request->data或者response为空。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。  SCSIPERIPHERAL_DDK_IO_ERROR DDK发生I/O错误。  SCSIPERIPHERAL_DDK_TIMEOUT 传输超时。  SCSIPERIPHERAL_DDK_INVALID_OPERATION 不支持该操作。 |

**OH_ScsiPeripheral_Write10()**

```ets
int32_t OH_ScsiPeripheral_Write10(ScsiPeripheral_Device *dev, ScsiPeripheral_IORequest *request,ScsiPeripheral_Response *response)
```

描述

写数据到设备的指定逻辑块。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_Device *dev | 设备句柄，详情参见ScsiPeripheral_Device。 |
| ScsiPeripheral_IORequest *request | write命令的请求信息，详情参见ScsiPeripheral_IORequest。 |
| ScsiPeripheral_Response *response | write命令返回的响应信息，详情参见ScsiPeripheral_Response。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空、 request为空、request->data为空或者response为空。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。  SCSIPERIPHERAL_DDK_IO_ERROR DDK发生I/O错误。  SCSIPERIPHERAL_DDK_TIMEOUT 传输超时。  SCSIPERIPHERAL_DDK_INVALID_OPERATION 不支持该操作。 |

**OH_ScsiPeripheral_Verify10()**

```ets
int32_t OH_ScsiPeripheral_Verify10(ScsiPeripheral_Device *dev, ScsiPeripheral_VerifyRequest *request,ScsiPeripheral_Response *response)
```

描述

校验指定逻辑块。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_Device *dev | 设备句柄，详情参见ScsiPeripheral_Device。 |
| ScsiPeripheral_VerifyRequest *request | verify命令的请求信息，详情参见ScsiPeripheral_VerifyRequest。 |
| ScsiPeripheral_Response *response | verify命令返回的响应信息，详情参见ScsiPeripheral_Response。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空、request为空或者response为空。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。  SCSIPERIPHERAL_DDK_IO_ERROR DDK发生I/O错误。  SCSIPERIPHERAL_DDK_TIMEOUT 传输超时。  SCSIPERIPHERAL_DDK_INVALID_OPERATION 不支持该操作。 |

**OH_ScsiPeripheral_SendRequestByCdb()**

```ets
int32_t OH_ScsiPeripheral_SendRequestByCdb(ScsiPeripheral_Device *dev, ScsiPeripheral_Request *request,ScsiPeripheral_Response *response)
```

描述

以CDB（Command Descriptor Block）方式发送SCSI命令。

需要权限： ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_Device *dev | 设备句柄，详情参见ScsiPeripheral_Device。 |
| ScsiPeripheral_Request *request | 请求，详情参见ScsiPeripheral_Request。 |
| ScsiPeripheral_Response *response | 响应，详情参见ScsiPeripheral_Response。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_NO_PERM 权限校验失败。  SCSIPERIPHERAL_DDK_INIT_ERROR 未初始化DDK。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空、 request为空、request->data为  空、request->cdbLength为0或者response为空。  SCSIPERIPHERAL_DDK_SERVICE_ERROR 与DDK服务通信失败。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。  SCSIPERIPHERAL_DDK_IO_ERROR DDK发生I/O错误。  SCSIPERIPHERAL_DDK_TIMEOUT 传输超时。  SCSIPERIPHERAL_DDK_INVALID_OPERATION 不支持该操作。 |

**OH_ScsiPeripheral_CreateDeviceMemMap()**

```ets
int32_t OH_ScsiPeripheral_CreateDeviceMemMap(ScsiPeripheral_Device *dev, size_t size,ScsiPeripheral_DeviceMemMap **devMmap)
```

描述

创建缓冲区。请在缓冲区使用完后，调用[OH_ScsiPeripheral_DestroyDeviceMemMap](scsi_peripheral_api.h.md#ZH-CN_TOPIC_0000002553361637__oh_scsiperipheral_destroydevicememmap)销毁缓冲区，否则会造成资源泄露。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_Device *dev | 设备句柄，详情参见ScsiPeripheral_Device。 |
| size_t size | 缓冲区的大小。 |
| ScsiPeripheral_DeviceMemMap **devMmap | 创建的缓冲区通过该参数返回给调用者，详情参见ScsiPeripheral_DeviceMemMap。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER dev为空或devMmap为空。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。 |

**OH_ScsiPeripheral_DestroyDeviceMemMap()**

```ets
int32_t OH_ScsiPeripheral_DestroyDeviceMemMap(ScsiPeripheral_DeviceMemMap *devMmap)
```

描述

销毁缓冲区。请在缓冲区使用完后及时销毁缓冲区，否则会造成资源泄露。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| ScsiPeripheral_DeviceMemMap *devMmap | 待销毁的由OH_ScsiPeripheral_CreateDeviceMemMap创建的缓冲区，详情参见ScsiPeripheral_DeviceMemMap。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER devMmap为空。  SCSIPERIPHERAL_DDK_MEMORY_ERROR 内存操作失败。 |

**OH_ScsiPeripheral_ParseBasicSenseInfo()**

```ets
int32_t OH_ScsiPeripheral_ParseBasicSenseInfo(uint8_t *senseData, uint8_t senseDataLen,ScsiPeripheral_BasicSenseInfo *senseInfo)
```

描述

解析基本的sense data，包括Information、Command specific information、Sense key specific字段。

起始版本： 18

参数：

| 参数项 | 描述 |
| --- | --- |
| uint8_t *senseData | 待解析的sense data。 |
| uint8_t senseDataLen | sense data长度。 |
| ScsiPeripheral_BasicSenseInfo *senseInfo | 用于保存解析后的基本信息，详情参见ScsiPeripheral_BasicSenseInfo。 |

返回：

| 类型 | 说明 |
| --- | --- |
| int32_t | SCSIPERIPHERAL_DDK_SUCCESS 调用接口成功。  SCSIPERIPHERAL_DDK_INVALID_PARAMETER senseData格式不是描述符或固定格式、senseDataLen小于  SCSIPERIPHERAL_MIN_DESCRIPTOR_FORMAT_SENSE或者senseDataLen小于SCSIPERIPHERAL_MIN_FIXED_FORMAT_SENSE。 |