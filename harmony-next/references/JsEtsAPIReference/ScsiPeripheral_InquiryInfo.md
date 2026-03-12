# ScsiPeripheral_InquiryInfo

```ets
typedef struct ScsiPeripheral_InquiryInfo {...} ScsiPeripheral_InquiryInfo
```

#### 概述

SCSI inquiry 数据。

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](SCSIPeripheralDDK.md)

**所在头文件：**[scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t deviceType设备类型。char idVendor制造商 id。char idProduct生产商 id。char revProduct产品版本。ScsiPeripheral_DeviceMemMap* data所有的查询数据。