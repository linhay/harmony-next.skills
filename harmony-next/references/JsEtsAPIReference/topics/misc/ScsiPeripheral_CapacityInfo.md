# ScsiPeripheral_CapacityInfo

```ets
typedef struct ScsiPeripheral_CapacityInfo {...} ScsiPeripheral_CapacityInfo
```

#### 概述

SCSI read capacity 数据。

**起始版本：** 18

相关模块： [ScsiPeripheralDDK](ScsiPeripheralDDK.md)

所在头文件： [scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32_t lbAddress | 返回的逻辑单元地址。 |
| uint32_t lbLength | 单个逻辑单元长度，单位：字节。 |