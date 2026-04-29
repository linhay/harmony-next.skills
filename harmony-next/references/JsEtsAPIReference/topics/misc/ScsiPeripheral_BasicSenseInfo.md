# ScsiPeripheral_BasicSenseInfo

```ets
typedef struct ScsiPeripheral_BasicSenseInfo {...} ScsiPeripheral_BasicSenseInfo
```

#### 概述

sense data的基本信息。

**起始版本：** 18

相关模块： [ScsiPeripheralDDK](ScsiPeripheralDDK.md)

所在头文件： [scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8_t responseCode | 响应码。 |
| bool valid | 信息有效标志位。 |
| uint64_t information | Information字段。 |
| uint64_t commandSpecific | Command-specific information字段。 |
| bool sksv | Sense key specific字段的标志位。 |
| uint32_t senseKeySpecific | Sense key specific字段。 |