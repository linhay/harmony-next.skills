# ScsiPeripheral_InquiryRequest

```ets
typedef struct ScsiPeripheral_InquiryRequest {...} ScsiPeripheral_InquiryRequest
```

#### 概述

SCSI命令（inquiry）的请求结构体。

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](SCSIPeripheralDDK.md)

**所在头文件：**[scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t pageCodePage code字段。获取设备的某些特定类型的信息时使用。当发出带有特定页面代码的 Inquiry 命令时，设备会返回与该页面代码相关的详细信息。如果 page code 设置为 0x00，则表示请求的是标准的 Inquiry 数据，而非特定页面的数据。uint16_t allocationLengthAllocation length字段，指定了请求方向发起者（通常是主机）为响应数据准备的缓冲区大小。uint8_t controlControl字段，用于指定一些控制信息。uint8_t byte1CDB的第一个字节。uint32_t timeout超时时间(单位: 毫秒)。