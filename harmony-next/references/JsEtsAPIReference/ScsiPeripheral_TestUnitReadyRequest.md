# ScsiPeripheral_TestUnitReadyRequest

```ets
typedef struct ScsiPeripheral_TestUnitReadyRequest {...} ScsiPeripheral_TestUnitReadyRequest
```

#### 概述

命令（test unit ready）的请求结构体。

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](SCSIPeripheralDDK.md)

**所在头文件：**[scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t controlControl字段，用于指定一些控制信息。uint32_t timeout超时时间(单位: 毫秒)。