# scsi_peripheral_types.h

#### 概述

提供在SCSI Peripheral DDK（驱动开发工具包）API中使用的枚举变量、结构体和宏。

**引用文件：** <scsi_peripheral/scsi_peripheral_types.h>

**库：** libscsi.z.so

**系统能力：** SystemCapability.Driver.SCSI.Extension

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](SCSIPeripheralDDK.md)

#### 汇总

#### 结构体

名称typedef关键字描述[ScsiPeripheral_DeviceMemMap](ScsiPeripheral_DeviceMemMap.md)ScsiPeripheral_DeviceMemMap通过调用OH_ScsiPeripheral_CreateDeviceMemMap创建的设备内存映射。使用该设备内存映射的缓冲区可以提供更好的性能。[ScsiPeripheral_IORequest](ScsiPeripheral_IORequest.md)ScsiPeripheral_IORequest读/写操作的请求参数。[ScsiPeripheral_Request](ScsiPeripheral_Request.md)ScsiPeripheral_Request请求参数结构体。[ScsiPeripheral_Response](ScsiPeripheral_Response.md)ScsiPeripheral_Response响应参数结构体。[ScsiPeripheral_TestUnitReadyRequest](ScsiPeripheral_TestUnitReadyRequest.md)ScsiPeripheral_TestUnitReadyRequest命令（test unit ready）的请求结构体。[ScsiPeripheral_InquiryRequest](ScsiPeripheral_InquiryRequest.md)ScsiPeripheral_InquiryRequestSCSI命令（inquiry）的请求结构体。[ScsiPeripheral_InquiryInfo](ScsiPeripheral_InquiryInfo.md)ScsiPeripheral_InquiryInfoSCSI inquiry 数据。[ScsiPeripheral_ReadCapacityRequest](ScsiPeripheral_ReadCapacityRequest.md)ScsiPeripheral_ReadCapacityRequestSCSI命令（read capacity）的请求结构体。[ScsiPeripheral_CapacityInfo](ScsiPeripheral_CapacityInfo.md)ScsiPeripheral_CapacityInfoSCSI read capacity 数据。[ScsiPeripheral_RequestSenseRequest](ScsiPeripheral_RequestSenseRequest.md)ScsiPeripheral_RequestSenseRequestSCSI命令（request sense）的请求结构体。[ScsiPeripheral_BasicSenseInfo](ScsiPeripheral_BasicSenseInfo.md)ScsiPeripheral_BasicSenseInfosense data的基本信息。[ScsiPeripheral_VerifyRequest](ScsiPeripheral_VerifyRequest.md)ScsiPeripheral_VerifyRequestSCSI命令（verify）的请求结构体。[ScsiPeripheral_Device](ScsiPeripheral_Device.md)ScsiPeripheral_Device不透明的SCSI设备结构体。

#### 枚举

名称typedef关键字描述[ScsiPeripheral_DdkErrCode](#ZH-CN_TOPIC_0000002497445632__scsiperipheral_ddkerrcode)ScsiPeripheral_DdkErrCodeSCSI Peripheral DDK错误码。[ScsiPeripheral_Status](#ZH-CN_TOPIC_0000002497445632__scsiperipheral_status)ScsiPeripheral_Status定义用于响应的SCSI状态。

#### 枚举类型说明

#### ScsiPeripheral_DdkErrCode

```ets
enum ScsiPeripheral_DdkErrCode
```

**描述**

SCSI Peripheral DDK错误码。

**起始版本：** 18

枚举项描述SCSIPERIPHERAL_DDK_NO_PERM = 201没有权限。SCSIPERIPHERAL_DDK_INVALID_PARAMETER = 401非法参数。SCSIPERIPHERAL_DDK_SUCCESS = 31700000操作成功。SCSIPERIPHERAL_DDK_MEMORY_ERROR = 31700001与内存相关的错误，例如，内存不足、内存数据复制失败或内存申请失败。SCSIPERIPHERAL_DDK_INVALID_OPERATION = 31700002非法操作。SCSIPERIPHERAL_DDK_IO_ERROR = 31700003设备输入/输出操作失败。SCSIPERIPHERAL_DDK_TIMEOUT = 31700004传输超时。SCSIPERIPHERAL_DDK_INIT_ERROR = 31700005DDK初始化错误，或者DDK未初始化。SCSIPERIPHERAL_DDK_SERVICE_ERROR = 31700006与SCSI Peripheral DDK服务的通信失败。SCSIPERIPHERAL_DDK_DEVICE_NOT_FOUND = 31700007设备未找到。

#### ScsiPeripheral_Status

```ets
enum ScsiPeripheral_Status
```

**描述**

定义用于响应的SCSI状态。

**起始版本：** 18

枚举项描述SCSIPERIPHERAL_STATUS_GOOD = 0x00正常状态。SCSIPERIPHERAL_STATUS_CHECK_CONDITION_NEEDED = 0x02需要状态检查。SCSIPERIPHERAL_STATUS_CONDITION_MET = 0x04条件满足。SCSIPERIPHERAL_STATUS_BUSY = 0x08占用中。SCSIPERIPHERAL_STATUS_RESERVATION_CONFLICT = 0x18资源保留冲突。SCSIPERIPHERAL_STATUS_TASK_SET_FULL = 0x28任务集已满。SCSIPERIPHERAL_STATUS_ACA_ACTIVE = 0x30ACA活动状态。SCSIPERIPHERAL_STATUS_TASK_ABORTED = 0x40任务已终止。