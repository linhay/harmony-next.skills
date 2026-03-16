# ScsiPeripheral_IORequest

```ets
typedef struct ScsiPeripheral_IORequest {...} ScsiPeripheral_IORequest
```

#### 概述

读/写操作的请求参数。

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](SCSIPeripheralDDK.md)

**所在头文件：**[scsi_peripheral_types.h](../../capi/headers/scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t lbAddress逻辑块起始地址。uint16_t transferLength需要操作的连续逻辑块的数量。uint8_t controlControl字段，用于指定一些控制信息。uint8_t byte1CDB的第一个字节。uint8_t byte6CDB的第六个字节ScsiPeripheral_DeviceMemMap* data数据传输的缓冲区。uint32_t timeout超时时间（单位：毫秒）。