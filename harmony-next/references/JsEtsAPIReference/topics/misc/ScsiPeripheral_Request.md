# ScsiPeripheral_Request

```ets
typedef struct ScsiPeripheral_Request {...} ScsiPeripheral_Request
```

#### 概述

请求参数结构体。

**起始版本：** 18

相关模块： [ScsiPeripheralDDK](ScsiPeripheralDDK.md)

所在头文件： [scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8_t commandDescriptorBlock[SCSIPERIPHERAL_MAX_CMD_DESC_BLOCK_LEN] | 命令描述符块。 |
| uint8_t cdbLength | 命令描述符块的长度。 |
| int8_t dataTransferDirection | 数据传输方向。 |
| ScsiPeripheral_DeviceMemMap* data | 数据传输的缓冲区。 |
| uint32_t timeout | 超时时间（单位：毫秒）。 |