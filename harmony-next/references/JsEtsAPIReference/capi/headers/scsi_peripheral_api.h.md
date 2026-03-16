# scsi_peripheral_api.h

#### 概述

声明用于主机侧访问SCSI设备的SCSI Peripheral DDK接口。

**引用文件：** <scsi_peripheral/scsi_peripheral_api.h>

**系统能力：** SystemCapability.Driver.SCSI.Extension

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](../../topics/misc/SCSIPeripheralDDK.md)

#### 汇总

#### 函数

名称描述[int32_t OH_ScsiPeripheral_Init(void)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_init)初始化SCSI Peripheral DDK。[int32_t OH_ScsiPeripheral_Release(void)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_release)释放SCSI Peripheral DDK。[int32_t OH_ScsiPeripheral_Open(uint64_t deviceId, uint8_t interfaceIndex, ScsiPeripheral_Device **dev)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_open)打开deviceId和interfaceIndex指定的SCSI设备。[int32_t OH_ScsiPeripheral_Close(ScsiPeripheral_Device **dev)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_close)关闭SCSI设备。[int32_t OH_ScsiPeripheral_TestUnitReady(ScsiPeripheral_Device *dev, ScsiPeripheral_TestUnitReadyRequest *request,ScsiPeripheral_Response *response)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_testunitready)检查逻辑单元是否已经准备好。[int32_t OH_ScsiPeripheral_Inquiry(ScsiPeripheral_Device *dev, ScsiPeripheral_InquiryRequest *request,ScsiPeripheral_InquiryInfo *inquiryInfo, ScsiPeripheral_Response *response)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_inquiry)查询SCSI设备的基本信息。[int32_t OH_ScsiPeripheral_ReadCapacity10(ScsiPeripheral_Device *dev, ScsiPeripheral_ReadCapacityRequest *request,ScsiPeripheral_CapacityInfo *capacityInfo, ScsiPeripheral_Response *response)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_readcapacity10)获取SCSI设备的容量信息。[int32_t OH_ScsiPeripheral_RequestSense(ScsiPeripheral_Device *dev, ScsiPeripheral_RequestSenseRequest *request,ScsiPeripheral_Response *response)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_requestsense)获取sense data（SCSI设备返回给主机的信息，用于报告设备的状态、错误信息以及诊断信息）。[int32_t OH_ScsiPeripheral_Read10(ScsiPeripheral_Device *dev, ScsiPeripheral_IORequest *request,ScsiPeripheral_Response *response)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_read10)从指定逻辑块读取数据。[int32_t OH_ScsiPeripheral_Write10(ScsiPeripheral_Device *dev, ScsiPeripheral_IORequest *request,ScsiPeripheral_Response *response)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_write10)写数据到设备的指定逻辑块。[int32_t OH_ScsiPeripheral_Verify10(ScsiPeripheral_Device *dev, ScsiPeripheral_VerifyRequest *request,ScsiPeripheral_Response *response)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_verify10)校验指定逻辑块。[int32_t OH_ScsiPeripheral_SendRequestByCdb(ScsiPeripheral_Device *dev, ScsiPeripheral_Request *request,ScsiPeripheral_Response *response)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_sendrequestbycdb)以CDB（Command Descriptor Block）方式发送SCSI命令。[int32_t OH_ScsiPeripheral_CreateDeviceMemMap(ScsiPeripheral_Device *dev, size_t size,ScsiPeripheral_DeviceMemMap **devMmap)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_createdevicememmap)创建缓冲区。请在缓冲区使用完后，调用[OH_ScsiPeripheral_DestroyDeviceMemMap](scsi_peripheral_api.h.md#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_destroydevicememmap)销毁缓冲区，否则会造成资源泄露。[int32_t OH_ScsiPeripheral_DestroyDeviceMemMap(ScsiPeripheral_DeviceMemMap *devMmap)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_destroydevicememmap)销毁缓冲区。请在缓冲区使用完后及时销毁缓冲区，否则会造成资源泄露。[int32_t OH_ScsiPeripheral_ParseBasicSenseInfo(uint8_t *senseData, uint8_t senseDataLen,ScsiPeripheral_BasicSenseInfo *senseInfo)](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_parsebasicsenseinfo)解析基本的sense data，包括Information、Command specific information、Sense key specific字段。

#### 函数说明

#### OH_ScsiPeripheral_Init()

```ets
int32_t OH_ScsiPeripheral_Init(void)
```

**描述**

初始化SCSI Peripheral DDK。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 初始化DDK失败。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

#### OH_ScsiPeripheral_Release()

```ets
int32_t OH_ScsiPeripheral_Release(void)
```

**描述**

释放SCSI Peripheral DDK。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

#### OH_ScsiPeripheral_Open()

```ets
int32_t OH_ScsiPeripheral_Open(uint64_t deviceId, uint8_t interfaceIndex, ScsiPeripheral_Device **dev)
```

**描述**

打开deviceId和interfaceIndex指定的SCSI设备。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述uint64_t deviceId设备ID，代表要操作的设备。uint8_t interfaceIndex接口索引，对应SCSI设备的接口。[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) **dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

[SCSIPERIPHERAL_DDK_IO_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) DDK发生IO错误。

[SCSIPERIPHERAL_DDK_DEVICE_NOT_FOUND](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 通过deviceId和interfaceIndex找不到设备。

[SCSIPERIPHERAL_DDK_INVALID_OPERATION](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 不支持该操作。

#### OH_ScsiPeripheral_Close()

```ets
int32_t OH_ScsiPeripheral_Close(ScsiPeripheral_Device **dev)
```

**描述**

关闭SCSI设备。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) **dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

[SCSIPERIPHERAL_DDK_IO_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) DDK发生I/O错误。

#### OH_ScsiPeripheral_TestUnitReady()

```ets
int32_t OH_ScsiPeripheral_TestUnitReady(ScsiPeripheral_Device *dev, ScsiPeripheral_TestUnitReadyRequest *request,ScsiPeripheral_Response *response)
```

**描述**

检查逻辑单元是否已经准备好。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) *dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。[ScsiPeripheral_TestUnitReadyRequest](../../topics/misc/ScsiPeripheral_TestUnitReadyRequest.md) *request逻辑单元检查命令（test unit ready）的请求信息，详情参见[ScsiPeripheral_TestUnitReadyRequest](../../topics/misc/ScsiPeripheral_TestUnitReadyRequest.md)。[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md) *response逻辑单元检查命令（test unit ready）的响应信息，详情参见[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空、request为空或者response为空。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

[SCSIPERIPHERAL_DDK_IO_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) DDK发生I/O错误。

[SCSIPERIPHERAL_DDK_TIMEOUT](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 传输超时。

[SCSIPERIPHERAL_DDK_INVALID_OPERATION](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 不支持该操作。

#### OH_ScsiPeripheral_Inquiry()

```ets
int32_t OH_ScsiPeripheral_Inquiry(ScsiPeripheral_Device *dev, ScsiPeripheral_InquiryRequest *request,ScsiPeripheral_InquiryInfo *inquiryInfo, ScsiPeripheral_Response *response)
```

**描述**

查询SCSI设备的基本信息。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) *dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。[ScsiPeripheral_InquiryRequest](../../topics/misc/ScsiPeripheral_InquiryRequest.md) *requestinquiry命令的请求信息，详情参见[ScsiPeripheral_InquiryRequest](../../topics/misc/ScsiPeripheral_InquiryRequest.md)。[ScsiPeripheral_InquiryInfo](../../topics/misc/ScsiPeripheral_InquiryInfo.md) *inquiryInfoinquiry命令返回的查询信息，详情参见[ScsiPeripheral_InquiryInfo](../../topics/misc/ScsiPeripheral_InquiryInfo.md)。[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md) *responseinquiry命令返回的原始响应信息，详情参见[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空、 request为空、inquiryInfo 为空、inquiryInfo->data或者response为空。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

[SCSIPERIPHERAL_DDK_IO_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) DDK发生I/O错误。

[SCSIPERIPHERAL_DDK_TIMEOUT](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 传输超时。

[SCSIPERIPHERAL_DDK_INVALID_OPERATION](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 不支持该操作。

#### OH_ScsiPeripheral_ReadCapacity10()

```ets
int32_t OH_ScsiPeripheral_ReadCapacity10(ScsiPeripheral_Device *dev, ScsiPeripheral_ReadCapacityRequest *request,ScsiPeripheral_CapacityInfo *capacityInfo, ScsiPeripheral_Response *response)
```

**描述**

获取SCSI设备的容量信息。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) *dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。[ScsiPeripheral_ReadCapacityRequest](../../topics/misc/ScsiPeripheral_ReadCapacityRequest.md) *requestread capacity命令的请求信息，详情参见[ScsiPeripheral_ReadCapacityRequest](../../topics/misc/ScsiPeripheral_ReadCapacityRequest.md)。[ScsiPeripheral_CapacityInfo](../../topics/misc/ScsiPeripheral_CapacityInfo.md) *capacityInforead capacity命令返回的容量信息，详情参见[ScsiPeripheral_CapacityInfo](../../topics/misc/ScsiPeripheral_CapacityInfo.md)。[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md) *responseread capacity命令返回的原始响应信息，详情参见[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空、 request为空、capacityInfo为空或者response为空。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

[SCSIPERIPHERAL_DDK_IO_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) DDK发生I/O错误。

[SCSIPERIPHERAL_DDK_TIMEOUT](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 传输超时。

[SCSIPERIPHERAL_DDK_INVALID_OPERATION](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 不支持该操作。

#### OH_ScsiPeripheral_RequestSense()

```ets
int32_t OH_ScsiPeripheral_RequestSense(ScsiPeripheral_Device *dev, ScsiPeripheral_RequestSenseRequest *request,ScsiPeripheral_Response *response)
```

**描述**

获取sense data（SCSI设备返回给主机的信息，用于报告设备的状态、错误信息以及诊断信息）。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) *dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。[ScsiPeripheral_RequestSenseRequest](../../topics/misc/ScsiPeripheral_RequestSenseRequest.md) *requestrequest sense命令的请求信息，详情参见[ScsiPeripheral_RequestSenseRequest](../../topics/misc/ScsiPeripheral_RequestSenseRequest.md)。[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md) *responserequest sense命令返回的响应信息，详情参见[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空、 request为空或者response为空。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

[SCSIPERIPHERAL_DDK_IO_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) DDK发生I/O错误。

[SCSIPERIPHERAL_DDK_TIMEOUT](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 传输超时。

[SCSIPERIPHERAL_DDK_INVALID_OPERATION](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 不支持该操作。

#### OH_ScsiPeripheral_Read10()

```ets
int32_t OH_ScsiPeripheral_Read10(ScsiPeripheral_Device *dev, ScsiPeripheral_IORequest *request,ScsiPeripheral_Response *response)
```

**描述**

从指定逻辑块读取数据。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) *dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。[ScsiPeripheral_IORequest](../../topics/misc/ScsiPeripheral_IORequest.md) *requestread命令的请求信息，详情参见[ScsiPeripheral_IORequest](../../topics/misc/ScsiPeripheral_IORequest.md)。[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md) *responseread命令返回的响应信息，详情参见[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空、 request为空、request->data或者response为空。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

[SCSIPERIPHERAL_DDK_IO_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) DDK发生I/O错误。

[SCSIPERIPHERAL_DDK_TIMEOUT](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 传输超时。

[SCSIPERIPHERAL_DDK_INVALID_OPERATION](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 不支持该操作。

#### OH_ScsiPeripheral_Write10()

```ets
int32_t OH_ScsiPeripheral_Write10(ScsiPeripheral_Device *dev, ScsiPeripheral_IORequest *request,ScsiPeripheral_Response *response)
```

**描述**

写数据到设备的指定逻辑块。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) *dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。[ScsiPeripheral_IORequest](../../topics/misc/ScsiPeripheral_IORequest.md) *requestwrite命令的请求信息，详情参见[ScsiPeripheral_IORequest](../../topics/misc/ScsiPeripheral_IORequest.md)。[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md) *responsewrite命令返回的响应信息，详情参见[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空、 request为空、request->data为空或者response为空。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

[SCSIPERIPHERAL_DDK_IO_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) DDK发生I/O错误。

[SCSIPERIPHERAL_DDK_TIMEOUT](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 传输超时。

[SCSIPERIPHERAL_DDK_INVALID_OPERATION](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 不支持该操作。

#### OH_ScsiPeripheral_Verify10()

```ets
int32_t OH_ScsiPeripheral_Verify10(ScsiPeripheral_Device *dev, ScsiPeripheral_VerifyRequest *request,ScsiPeripheral_Response *response)
```

**描述**

校验指定逻辑块。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) *dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。[ScsiPeripheral_VerifyRequest](../../topics/misc/ScsiPeripheral_VerifyRequest.md) *requestverify命令的请求信息，详情参见[ScsiPeripheral_VerifyRequest](../../topics/misc/ScsiPeripheral_VerifyRequest.md)。[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md) *responseverify命令返回的响应信息，详情参见[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空、request为空或者response为空。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

[SCSIPERIPHERAL_DDK_IO_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) DDK发生I/O错误。

[SCSIPERIPHERAL_DDK_TIMEOUT](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 传输超时。

[SCSIPERIPHERAL_DDK_INVALID_OPERATION](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 不支持该操作。

#### OH_ScsiPeripheral_SendRequestByCdb()

```ets
int32_t OH_ScsiPeripheral_SendRequestByCdb(ScsiPeripheral_Device *dev, ScsiPeripheral_Request *request,ScsiPeripheral_Response *response)
```

**描述**

以CDB（Command Descriptor Block）方式发送SCSI命令。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) *dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。[ScsiPeripheral_Request](../../topics/misc/ScsiPeripheral_Request.md) *request请求，详情参见[ScsiPeripheral_Request](../../topics/misc/ScsiPeripheral_Request.md)。[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md) *response响应，详情参见[ScsiPeripheral_Response](../../topics/misc/ScsiPeripheral_Response.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_NO_PERM](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 权限校验失败。

[SCSIPERIPHERAL_DDK_INIT_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 未初始化DDK。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空、 request为空、request->data为

 空、request->cdbLength为0或者response为空。

[SCSIPERIPHERAL_DDK_SERVICE_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 与DDK服务通信失败。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

[SCSIPERIPHERAL_DDK_IO_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) DDK发生I/O错误。

[SCSIPERIPHERAL_DDK_TIMEOUT](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 传输超时。

[SCSIPERIPHERAL_DDK_INVALID_OPERATION](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 不支持该操作。

#### OH_ScsiPeripheral_CreateDeviceMemMap()

```ets
int32_t OH_ScsiPeripheral_CreateDeviceMemMap(ScsiPeripheral_Device *dev, size_t size,ScsiPeripheral_DeviceMemMap **devMmap)
```

**描述**

创建缓冲区。请在缓冲区使用完后，调用[OH_ScsiPeripheral_DestroyDeviceMemMap](scsi_peripheral_api.h.md#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_destroydevicememmap)销毁缓冲区，否则会造成资源泄露。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md) *dev设备句柄，详情参见[ScsiPeripheral_Device](../../topics/system-services/ScsiPeripheral_Device.md)。size_t size缓冲区的大小。[ScsiPeripheral_DeviceMemMap](../../topics/system-services/ScsiPeripheral_DeviceMemMap.md) **devMmap创建的缓冲区通过该参数返回给调用者，详情参见[ScsiPeripheral_DeviceMemMap](../../topics/system-services/ScsiPeripheral_DeviceMemMap.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) dev为空或devMmap为空。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

#### OH_ScsiPeripheral_DestroyDeviceMemMap()

```ets
int32_t OH_ScsiPeripheral_DestroyDeviceMemMap(ScsiPeripheral_DeviceMemMap *devMmap)
```

**描述**

销毁缓冲区。请在缓冲区使用完后及时销毁缓冲区，否则会造成资源泄露。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述[ScsiPeripheral_DeviceMemMap](../../topics/system-services/ScsiPeripheral_DeviceMemMap.md) *devMmap待销毁的由[OH_ScsiPeripheral_CreateDeviceMemMap](#ZH-CN_TOPIC_0000002497605610__oh_scsiperipheral_createdevicememmap)创建的缓冲区，详情参见[ScsiPeripheral_DeviceMemMap](../../topics/system-services/ScsiPeripheral_DeviceMemMap.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) devMmap为空。

[SCSIPERIPHERAL_DDK_MEMORY_ERROR](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 内存操作失败。

#### OH_ScsiPeripheral_ParseBasicSenseInfo()

```ets
int32_t OH_ScsiPeripheral_ParseBasicSenseInfo(uint8_t *senseData, uint8_t senseDataLen,ScsiPeripheral_BasicSenseInfo *senseInfo)
```

**描述**

解析基本的sense data，包括Information、Command specific information、Sense key specific字段。

**需要权限：** ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

**起始版本：** 18

**参数：**

参数项描述uint8_t *senseData待解析的sense data。uint8_t senseDataLensense data长度。[ScsiPeripheral_BasicSenseInfo](../../topics/misc/ScsiPeripheral_BasicSenseInfo.md) *senseInfo用于保存解析后的基本信息，详情参见[ScsiPeripheral_BasicSenseInfo](../../topics/misc/ScsiPeripheral_BasicSenseInfo.md)。

**返回：**

类型说明int32_t

[SCSIPERIPHERAL_DDK_SUCCESS](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) 调用接口成功。

[SCSIPERIPHERAL_DDK_INVALID_PARAMETER](scsi_peripheral_types.h.md#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode) senseData格式不是描述符或固定格式、senseDataLen小于

 SCSIPERIPHERAL_MIN_DESCRIPTOR_FORMAT_SENSE或者senseDataLen小于SCSIPERIPHERAL_MIN_FIXED_FORMAT_SENSE。