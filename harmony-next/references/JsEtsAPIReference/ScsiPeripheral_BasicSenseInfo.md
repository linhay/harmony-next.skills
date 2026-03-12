# ScsiPeripheral_BasicSenseInfo

```ets
typedef struct ScsiPeripheral_BasicSenseInfo {...} ScsiPeripheral_BasicSenseInfo
```

#### 概述

sense data的基本信息。

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](SCSIPeripheralDDK.md)

**所在头文件：**[scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

名称描述uint8_t responseCode响应码。bool valid信息有效标志位。uint64_t informationInformation字段。uint64_t commandSpecificCommand-specific information字段。bool sksvSense key specific字段的标志位。uint32_t senseKeySpecificSense key specific字段。