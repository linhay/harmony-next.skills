# ScsiPeripheral_ReadCapacityRequest

```ets
typedef struct ScsiPeripheral_ReadCapacityRequest {...} ScsiPeripheral_ReadCapacityRequest
```

#### 概述

SCSI命令（read capacity）的请求结构体。

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](SCSIPeripheralDDK.md)

**所在头文件：**[scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t lbAddress逻辑单元地址。uint8_t controlControl字段，用于指定一些控制信息。uint8_t byte8CDB的第八个字节。uint32_t timeout超时时间(单位: 毫秒)。