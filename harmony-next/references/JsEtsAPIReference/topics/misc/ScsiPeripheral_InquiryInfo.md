# ScsiPeripheral_InquiryInfo

```ets
typedef struct ScsiPeripheral_InquiryInfo {...} ScsiPeripheral_InquiryInfo
```

#### 概述

SCSI inquiry 数据。

**起始版本：** 18

相关模块： [ScsiPeripheralDDK](ScsiPeripheralDDK.md)

所在头文件： [scsi_peripheral_types.h](scsi_peripheral_types.h.md)

#### 汇总

#### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8_t deviceType | 设备类型。 |
| char idVendor[SCSIPERIPHERAL_VENDOR_ID_LEN + 1] | 制造商 id。 |
| char idProduct[SCSIPERIPHERAL_PRODUCT_ID_LEN + 1] | 生产商 id。 |
| char revProduct[SCSIPERIPHERAL_PRODUCT_REV_LEN + 1] | 产品版本。 |
| ScsiPeripheral_DeviceMemMap* data | 所有的查询数据。 |