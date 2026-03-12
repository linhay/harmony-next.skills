# ScsiPeripheral_Response

```ets
typedef struct ScsiPeripheral_Response {...} ScsiPeripheral_Response
```

#### 概述

响应参数结构体。

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](SCSIPeripheralDDK.md)

**所在头文件：**[scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t senseData[SCSIPERIPHERAL_MAX_SENSE_DATA_LEN]sense data（SCSI设备返回给主机的信息，用于报告设备的状态、错误信息以及诊断信息）。ScsiPeripheral_Status status调用完成时的状态，例如良好（Good）、忙（Busy）。uint8_t maskedStatus在Linux的SCSI通用接口（SG）中，masked_status 字段用于存储经过处理后的SCSI状态，以便应用程序可以更方便地读取和解析。uint8_t msgStatus消息状态。uint8_t sbLenWr指的是实际写入到 Sense Buffer（感应缓冲区）的字节数。uint16_t hostStatus主机适配器状态。 例如：成功(0x00)、无法连接(0x01)、总线忙(0x02)、超时(0x03)。uint16_t driverStatus驱动状态。 例如：成功（0x00）、设备或资源忙(0x01)。int32_t resId实际传输的数据长度差值，即未传输的字节数。uint32_t duration执行命令消耗的时间 (单位: 毫秒)。