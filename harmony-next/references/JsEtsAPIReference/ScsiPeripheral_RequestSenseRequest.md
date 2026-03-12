# ScsiPeripheral_RequestSenseRequest

```ets
typedef struct ScsiPeripheral_RequestSenseRequest {...} ScsiPeripheral_RequestSenseRequest
```

#### 概述

SCSI命令（request sense）的请求结构体。

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](SCSIPeripheralDDK.md)

**所在头文件：**[scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t allocationLengthAllocation length字段，指定了请求方向发起者（通常是主机）为响应数据准备的缓冲区大小。uint8_t controlControl字段，用于指定一些控制信息。uint8_t byte1CDB的第一个字节。uint32_t timeout超时时间(单位: 毫秒)。