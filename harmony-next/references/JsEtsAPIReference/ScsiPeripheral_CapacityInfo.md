# ScsiPeripheral_CapacityInfo

```ets
typedef struct ScsiPeripheral_CapacityInfo {...} ScsiPeripheral_CapacityInfo
```

#### 概述

SCSI read capacity 数据。

**起始版本：** 18

**相关模块：**[SCSIPeripheralDDK](SCSIPeripheralDDK.md)

**所在头文件：**[scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

名称描述uint32_t lbAddress返回的逻辑单元地址。uint32_t lbLength单个逻辑单元长度，单位：字节。