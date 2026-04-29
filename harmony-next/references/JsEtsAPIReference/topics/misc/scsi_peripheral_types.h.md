# scsi_peripheral_types.h

**概述**

提供在SCSI Peripheral DDK（驱动开发工具包）API中使用的枚举变量、结构体和宏。

引用文件： <scsi_peripheral/scsi_peripheral_types.h>

库： libscsi.z.so

系统能力： SystemCapability.Driver.SCSI.Extension

起始版本： 18

相关模块： [ScsiPeripheralDDK](ScsiPeripheralDDK.md)

**汇总**

**结构体**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ScsiPeripheral_DeviceMemMap | ScsiPeripheral_DeviceMemMap | 通过调用OH_ScsiPeripheral_CreateDeviceMemMap创建的设备内存映射。使用该设备内存映射的缓冲区可以提供更好的性能。 |
| ScsiPeripheral_IORequest | ScsiPeripheral_IORequest | 读/写操作的请求参数。 |
| ScsiPeripheral_Request | ScsiPeripheral_Request | 请求参数结构体。 |
| ScsiPeripheral_Response | ScsiPeripheral_Response | 响应参数结构体。 |
| ScsiPeripheral_TestUnitReadyRequest | ScsiPeripheral_TestUnitReadyRequest | 命令（test unit ready）的请求结构体。 |
| ScsiPeripheral_InquiryRequest | ScsiPeripheral_InquiryRequest | SCSI命令（inquiry）的请求结构体。 |
| ScsiPeripheral_InquiryInfo | ScsiPeripheral_InquiryInfo | SCSI inquiry 数据。 |
| ScsiPeripheral_ReadCapacityRequest | ScsiPeripheral_ReadCapacityRequest | SCSI命令（read capacity）的请求结构体。 |
| ScsiPeripheral_CapacityInfo | ScsiPeripheral_CapacityInfo | SCSI read capacity 数据。 |
| ScsiPeripheral_RequestSenseRequest | ScsiPeripheral_RequestSenseRequest | SCSI命令（request sense）的请求结构体。 |
| ScsiPeripheral_BasicSenseInfo | ScsiPeripheral_BasicSenseInfo | sense data的基本信息。 |
| ScsiPeripheral_VerifyRequest | ScsiPeripheral_VerifyRequest | SCSI命令（verify）的请求结构体。 |
| ScsiPeripheral_Device | ScsiPeripheral_Device | 不透明的SCSI设备结构体。 |

**枚举**

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| ScsiPeripheral_DdkErrCode | ScsiPeripheral_DdkErrCode | SCSI Peripheral DDK错误码。 |
| ScsiPeripheral_Status | ScsiPeripheral_Status | 定义用于响应的SCSI状态。 |

**枚举类型说明**

**ScsiPeripheral_DdkErrCode**

```ets
enum ScsiPeripheral_DdkErrCode
```

描述

SCSI Peripheral DDK错误码。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| SCSIPERIPHERAL_DDK_NO_PERM = 201 | 没有权限。 |
| SCSIPERIPHERAL_DDK_INVALID_PARAMETER = 401 | 非法参数。 |
| SCSIPERIPHERAL_DDK_SUCCESS = 31700000 | 操作成功。 |
| SCSIPERIPHERAL_DDK_MEMORY_ERROR = 31700001 | 与内存相关的错误，例如，内存不足、内存数据复制失败或内存申请失败。 |
| SCSIPERIPHERAL_DDK_INVALID_OPERATION = 31700002 | 非法操作。 |
| SCSIPERIPHERAL_DDK_IO_ERROR = 31700003 | 设备输入/输出操作失败。 |
| SCSIPERIPHERAL_DDK_TIMEOUT = 31700004 | 传输超时。 |
| SCSIPERIPHERAL_DDK_INIT_ERROR = 31700005 | DDK初始化错误，或者DDK未初始化。 |
| SCSIPERIPHERAL_DDK_SERVICE_ERROR = 31700006 | 与SCSI Peripheral DDK服务的通信失败。 |
| SCSIPERIPHERAL_DDK_DEVICE_NOT_FOUND = 31700007 | 设备未找到。 |

**ScsiPeripheral_Status**

```ets
enum ScsiPeripheral_Status
```

描述

定义用于响应的SCSI状态。

起始版本： 18

| 枚举项 | 描述 |
| --- | --- |
| SCSIPERIPHERAL_STATUS_GOOD = 0x00 | 正常状态。 |
| SCSIPERIPHERAL_STATUS_CHECK_CONDITION_NEEDED = 0x02 | 需要状态检查。 |
| SCSIPERIPHERAL_STATUS_CONDITION_MET = 0x04 | 条件满足。 |
| SCSIPERIPHERAL_STATUS_BUSY = 0x08 | 占用中。 |
| SCSIPERIPHERAL_STATUS_RESERVATION_CONFLICT = 0x18 | 资源保留冲突。 |
| SCSIPERIPHERAL_STATUS_TASK_SET_FULL = 0x28 | 任务集已满。 |
| SCSIPERIPHERAL_STATUS_ACA_ACTIVE = 0x30 | ACA活动状态。 |
| SCSIPERIPHERAL_STATUS_TASK_ABORTED = 0x40 | 任务已终止。 |

**SCSIPERIPHERAL_MIN_DESCRIPTOR_FORMAT_SENSE**

```ets
SCSIPERIPHERAL_MIN_DESCRIPTOR_FORMAT_SENSE 8
```

描述

描述符格式传感数据的最小长度。

起始版本： 18

**SCSIPERIPHERAL_MIN_FIXED_FORMAT_SENSE**

```ets
SCSIPERIPHERAL_MIN_FIXED_FORMAT_SENSE 18
```

描述

固定格式传感数据的最小长度。

起始版本： 18

**SCSIPERIPHERAL_MAX_CMD_DESC_BLOCK_LEN**

```ets
SCSIPERIPHERAL_MAX_CMD_DESC_BLOCK_LEN 16
```

描述

命令描述块的最大长度。

起始版本： 18

**SCSIPERIPHERAL_MAX_SENSE_DATA_LEN**

```ets
SCSIPERIPHERAL_MAX_SENSE_DATA_LEN 252
```

描述

传感数据的最大长度。

起始版本： 18

**SCSIPERIPHERAL_VENDOR_ID_LEN**

```ets
SCSIPERIPHERAL_VENDOR_ID_LEN 8
```

描述

厂家标识符的长度。

起始版本： 18

**SCSIPERIPHERAL_PRODUCT_ID_LEN**

```ets
SCSIPERIPHERAL_PRODUCT_ID_LEN 16
```

描述

产品标识符的长度。

起始版本： 18

**SCSIPERIPHERAL_PRODUCT_REV_LEN**

```ets
SCSIPERIPHERAL_PRODUCT_REV_LEN 4
```

描述

产品修订版本号的长度。

起始版本： 18